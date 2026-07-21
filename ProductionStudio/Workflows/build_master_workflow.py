"""Build the Fatal Affairs master pipeline workflow for n8n (local Phase 2 trial).

Reads Agents/*.md as system prompts, wires 11 Anthropic LLM nodes + ElevenLabs TTS
branch + fal.ai image branch, per Stage 3 link contracts. Keys come from env
(ANTHROPIC_API_KEY_N8N, ELEVENLABS_API_KEY, FAL_KEY) and are embedded into the
local workflow JSON only (scratchpad + local n8n SQLite; never committed).

Out-of-band by design: Video Assembly (local Remotion render), Tool Manager
(design-time agent), YouTube publish (always human-gated).

Cost note (2026-07-21): the first full trial run cost ~$4.50 on ANTHROPIC_API_KEY_N8N
(11 Opus 4.8 calls, plus a partial re-run from an ElevenLabs concurrency bug, now
fixed). Model mix below cuts that: Opus 4.8 stays only on Research/Story/QC (the
reasoning- and accuracy-critical steps); everything else runs on Sonnet 5.

Caption-sync note (2026-07-21): the first render's captions drifted badly after ~9
minutes and went nonsensical near the end. Root cause: captions were built from
Scene Planner's SceneList.json scene text, but Voice Production Agent legitimately
rewrites/expands that text for natural narration (chapter 7 alone came out 74%
longer than the scene list) - so captions and audio were, in the worst chapter,
showing/saying different words. Fixed at the root: Voice Production Agent now
emits inline [[SCENE:NNNN]] markers in its chapter output, TTS runs against
ElevenLabs' with-timestamps endpoint (real per-character audio alignment), and the
post-processing script (Workflows/process_pipeline_audio.py) derives real per-word
caption timing and real scene/image boundaries directly from that alignment -
never from an estimate, and always from the exact words actually spoken.
"""
import json
import os
import sys

REPO = "D:/SHOPS/AI Projects/YT_Crime/YT-Studio"
AGENTS = REPO + "/ProductionStudio/Agents"
ASSETS = REPO + "/ProductionStudio/Assets"

CASE_QUERY = os.environ.get("PIPELINE_CASE_QUERY", "find next true crime candidate case")

ant_key = os.environ["ANTHROPIC_API_KEY_N8N"]
el_key = os.environ["ELEVENLABS_API_KEY"]
fal_key = os.environ["FAL_KEY"]

VOICE_ID = "wSChTcAxdiTjLPhHeyrM"  # Jimmy - Canadian Podcast Narration (fixed in config)

# Model mix: Opus 4.8 for reasoning/accuracy-critical steps, Sonnet 5 for the rest.
MODEL_OPUS = "claude-opus-4-8"
MODEL_SONNET = "claude-sonnet-5"

def read_agent(fname):
    with open(os.path.join(AGENTS, fname), encoding="utf-8") as f:
        return f.read()

# --- system prompts: full agent spec files (raw strings in a Set node, never
# expression-parsed, so braces in their JSON schemas are safe) ---
FRAME = (
    "You are running as an automated n8n pipeline node. Follow the agent spec below "
    "exactly. Output ONLY what the spec's Output section defines - no preamble, no "
    "commentary outside the defined output. If the spec says to escalate to a human, "
    "still produce your best output but put the escalation flag INSIDE the output "
    "(add an 'escalations' array field to JSON outputs, or an '> ESCALATION:' line "
    "in markdown/text outputs).\n\n--- AGENT SPEC ---\n\n"
)

prompts = {
    "sys_research": FRAME + read_agent("research_agent.md"),
    "sys_factcheck": FRAME + read_agent("fact_verification_agent.md"),
    "sys_story": FRAME + read_agent("story_agent.md"),
    "sys_scene": FRAME + read_agent("scene_planner_agent.md"),
    "sys_voice": FRAME + read_agent("voice_production_agent.md"),
    "sys_imgplan": FRAME + read_agent("image_planning_agent.md"),
    "sys_seo": FRAME + read_agent("seo_agent.md"),
    "sys_thumb": FRAME + read_agent("thumbnail_agent.md"),
    "sys_shorts": FRAME + read_agent("shorts_agent.md"),
    "sys_qc": FRAME + read_agent("quality_control_agent.md"),
    "sys_publish": FRAME + read_agent("publishing_agent.md"),
}

# Research Agent memory: covered-cases registry injected into every discovery run.
# Single-quoted JS string fragment; sanitized so it can't break the expression.
with open(REPO + "/ProductionStudio/Cases/covered_cases.json", encoding="utf-8") as f:
    _covered = json.load(f)["cases"]
covered_cases_js = "; ".join(
    c["case_name"] + " (aka: " + ", ".join(c.get("aka", [])) + ")"
    for c in _covered
).replace("'", "").replace("{", "").replace("}", "")

def txt(node_name):
    """JS expr: concatenated text blocks of an Anthropic node's response."""
    return (
        "$('" + node_name + "').first().json.content"
        ".filter(b => b.type === 'text').map(b => b.text).join('\\n')"
    )

def anthropic_node(nid, name, pos, sys_key, user_expr, max_tokens, tools_js=None, model=MODEL_SONNET):
    body = (
        "={{ JSON.stringify({ model: '" + model + "', max_tokens: " + str(max_tokens)
        + ", thinking: { type: 'adaptive' }, "
        + ("tools: " + tools_js + ", " if tools_js else "")
        + "system: $('Agent Prompts').first().json." + sys_key
        + ", messages: [ { role: 'user', content: " + user_expr + " } ] }) }}"
    )
    return {
        "id": nid,
        "name": name,
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.2,
        "position": pos,
        "retryOnFail": True,
        "maxTries": 2,
        "waitBetweenTries": 5000,
        "parameters": {
            "method": "POST",
            "url": "https://api.anthropic.com/v1/messages",
            "sendHeaders": True,
            "headerParameters": {"parameters": [
                {"name": "x-api-key", "value": ant_key},
                {"name": "anthropic-version", "value": "2023-06-01"},
                {"name": "Content-Type", "value": "application/json"},
            ]},
            "sendBody": True,
            "specifyBody": "json",
            "jsonBody": body,
            "options": {"timeout": 600000},
        },
    }

nodes = []
conns = {}

def connect(src, dst):
    conns.setdefault(src, {"main": [[]]})["main"][0].append(
        {"node": dst, "type": "main", "index": 0}
    )

# --- entry ---
nodes.append({
    "id": "manual_trigger", "name": "Manual Trigger",
    "type": "n8n-nodes-base.manualTrigger", "typeVersion": 1,
    "position": [0, 400], "parameters": {},
})
nodes.append({
    "id": "case_input", "name": "Case Input",
    "type": "n8n-nodes-base.set", "typeVersion": 3.4,
    "position": [200, 400],
    "parameters": {
        "assignments": {"assignments": [
            {"id": "a1", "name": "case_query", "value": CASE_QUERY, "type": "string"},
        ]},
        "options": {},
    },
})
prompt_assignments = [
    {"id": "p%d" % i, "name": k, "value": v, "type": "string"}
    for i, (k, v) in enumerate(prompts.items())
]
nodes.append({
    "id": "agent_prompts", "name": "Agent Prompts",
    "type": "n8n-nodes-base.set", "typeVersion": 3.4,
    "position": [400, 400],
    "parameters": {"assignments": {"assignments": prompt_assignments},
                   "options": {}},
})
connect("Manual Trigger", "Case Input")
connect("Case Input", "Agent Prompts")

# --- main LLM chain ---
nodes.append(anthropic_node(
    "research", "Research Agent", [600, 400], "sys_research",
    "'Case query: ' + $('Case Input').first().json.case_query + "
    "'\\nchannel_niche: affairs / betrayal / murder / love triangle / missing persons"
    "\\nn_candidates: 5"
    "\\ncovered_cases (ALREADY COVERED by this channel - NEVER propose these or their "
    "aliases as candidates): " + covered_cases_js + "'",
    12000,
    tools_js="[ { type: 'web_search_20260209', name: 'web_search', max_uses: 8 } ]",
    model=MODEL_OPUS,
))
connect("Agent Prompts", "Research Agent")

nodes.append(anthropic_node(
    "factcheck", "Fact Verification Agent", [800, 400], "sys_factcheck",
    "'Research Agent output is below. Per your Stage 3 link note: pick the strongest "
    "candidate (if several are close in strength, proceed with the strongest but state "
    "the close call explicitly in an escalations field), derive "
    "script_draft_or_scene_claims by flattening that candidate sources[].key_facts, "
    "summary and timeline_draft into atomic claim strings, then verify each claim "
    "against the sources. Start your output with a line: CHOSEN CASE: <case_name>."
    "\\n\\n' + " + txt("Research Agent"),
    8000,
))
connect("Research Agent", "Fact Verification Agent")

nodes.append(anthropic_node(
    "story", "Story Agent", [1000, 400], "sys_story",
    "'success_rules: (empty - first automated run)\\n\\nFact Verification output "
    "(build ONLY on verified_claims):\\n\\n' + " + txt("Fact Verification Agent")
    + " + '\\n\\nResearch output (for timeline_draft of the chosen case):\\n\\n' + "
    + txt("Research Agent"),
    16000,
    model=MODEL_OPUS,
))
connect("Fact Verification Agent", "Story Agent")

nodes.append(anthropic_node(
    "scene", "Scene Planner Agent", [1200, 400], "sys_scene",
    "'script_md:\\n\\n' + " + txt("Story Agent"),
    16000,
))
connect("Story Agent", "Scene Planner Agent")

nodes.append(anthropic_node(
    "voice", "Voice Production Agent", [1400, 400], "sys_voice",
    "'Scenes JSON below. OUTPUT FORMAT REQUIREMENT for this pipeline: precede each "
    "chapter chunk with a header line of exactly this shape: "
    "=== CHAPTER 01 (scenes 0001-0008) === (two-digit chapter number, real scene "
    "range). Within the chapter body, immediately before the narration text written "
    "for each individual scene_id, insert an inline marker of exactly this shape on "
    "its own: [[SCENE:0001]] (four-digit scene_id, double brackets, no space "
    "inside). One marker per scene_id, in order, even when a scene is merged or "
    "reworded into a longer or shorter passage than the original scene text - the "
    "marker marks where that scene narration actually begins, not a word-count "
    "boundary. These markers are stripped before the text reaches text-to-speech and "
    "are used only to time-align captions and images to the real narration, so place "
    "them precisely at the real start of each scene content, not evenly spaced. No "
    "other double-bracket or triple-equals markup anywhere.\\n\\n' + "
    + txt("Scene Planner Agent"),
    16000,
))
connect("Scene Planner Agent", "Voice Production Agent")

nodes.append(anthropic_node(
    "imgplan", "Image Planning Agent", [1600, 400], "sys_imgplan",
    "'Scenes JSON:\\n\\n' + " + txt("Scene Planner Agent"),
    16000,
))
connect("Voice Production Agent", "Image Planning Agent")

nodes.append(anthropic_node(
    "seo", "SEO Agent", [1800, 400], "sys_seo",
    "'success_rules: (empty - first automated run)\\n\\nscript_md:\\n\\n' + "
    + txt("Story Agent")
    + " + '\\n\\nResearch output - use genre_trend_notes and the CHOSEN candidate "
    "viral_potential_notes only:\\n\\n' + " + txt("Research Agent"),
    8000,
))
connect("Image Planning Agent", "SEO Agent")

nodes.append(anthropic_node(
    "thumb", "Thumbnail Agent", [2000, 400], "sys_thumb",
    "'Derive case_summary and twist from this verified script; brand_style per your "
    "spec.\\n\\nscript_md:\\n\\n' + " + txt("Story Agent"),
    2000,
))
connect("SEO Agent", "Thumbnail Agent")

nodes.append(anthropic_node(
    "shorts", "Shorts Agent", [2200, 400], "sys_shorts",
    "'max_shorts: 5. NOTE: the final render happens out-of-band in Remotion after "
    "this run - select source_scene_ids from the scene list below; case summary and "
    "twist are derivable from the scene texts.\\n\\nScenes JSON:\\n\\n' + "
    + txt("Scene Planner Agent"),
    4000,
))
connect("Thumbnail Agent", "Shorts Agent")

nodes.append(anthropic_node(
    "qc", "Quality Control Agent", [2400, 400], "sys_qc",
    "'KNOWN LIMITATION of this run: the Remotion render + audio/image files are "
    "produced out-of-band locally, so treat export-integrity and asset-file checks as "
    "PENDING (list them as warnings, not fails). Evaluate everything text-side "
    "fully.\\n\\n=== Fact Verification ===\\n' + " + txt("Fact Verification Agent")
    + " + '\\n\\n=== Script.md ===\\n' + " + txt("Story Agent")
    + " + '\\n\\n=== Scene list ===\\n' + " + txt("Scene Planner Agent")
    + " + '\\n\\n=== Voiceover.txt ===\\n' + " + txt("Voice Production Agent")
    + " + '\\n\\n=== ImagePrompts ===\\n' + " + txt("Image Planning Agent")
    + " + '\\n\\n=== Thumbnail.md ===\\n' + " + txt("Thumbnail Agent")
    + " + '\\n\\n=== SEO.md ===\\n' + " + txt("SEO Agent")
    + " + '\\n\\n=== Shorts.md ===\\n' + " + txt("Shorts Agent"),
    6000,
    model=MODEL_OPUS,
))
connect("Shorts Agent", "Quality Control Agent")

nodes.append(anthropic_node(
    "publish", "Publishing Agent (prepare only)", [2600, 400], "sys_publish",
    "'HARD RULE REMINDER: prepare only, no publish call exists in this pipeline. If "
    "checklist_status is not pass, output awaiting_human_confirmation with the "
    "blocking issues instead of a release plan.\\n\\n=== Checklist ===\\n' + "
    + txt("Quality Control Agent")
    + " + '\\n\\n=== SEO.md ===\\n' + " + txt("SEO Agent")
    + " + '\\n\\n=== Thumbnail.md ===\\n' + " + txt("Thumbnail Agent")
    + " + '\\n\\n=== Shorts.md ===\\n' + " + txt("Shorts Agent"),
    3000,
))
connect("Quality Control Agent", "Publishing Agent (prepare only)")

# --- branch A: voiceover -> strip [[SCENE:NNNN]] markers -> ElevenLabs TTS
# with-timestamps per chapter. Real per-character alignment comes back in the
# JSON response; Workflows/process_pipeline_audio.py (run after n8n execute)
# decodes the base64 audio, derives real per-word caption timing and real
# scene/image boundaries from the marker offsets + alignment, and writes the
# mp3 + alignment files to disk. No file-write node needed inside n8n for this
# branch anymore (also sidesteps n8n's default disk-write restriction).
nodes.append({
    "id": "parse_chapters", "name": "Parse Chapters",
    "type": "n8n-nodes-base.code", "typeVersion": 2,
    "position": [1600, 700],
    "parameters": {"jsCode": (
        "const txt = $('Voice Production Agent').first().json.content"
        ".filter(b => b.type === 'text').map(b => b.text).join('\\n');\n"
        "const parts = txt.split(/^===\\s*CHAPTER\\s+/m).slice(1);\n"
        "if (!parts.length) throw new Error('No chapter headers found in voiceover');\n"
        "return parts.map(p => {\n"
        "  const num = (p.match(/^(\\d+)/) || [null, '00'])[1].padStart(2, '0');\n"
        "  const body = p.substring(p.indexOf('===') + 3).trim();\n"
        "  const markerRe = /\\[\\[SCENE:(\\d{4})\\]\\]\\s*/g;\n"
        "  let clean = '';\n"
        "  let lastIndex = 0;\n"
        "  const markers = [];\n"
        "  let m;\n"
        "  while ((m = markerRe.exec(body)) !== null) {\n"
        "    clean += body.slice(lastIndex, m.index);\n"
        "    markers.push({ scene_id: m[1], charOffset: clean.length });\n"
        "    lastIndex = markerRe.lastIndex;\n"
        "  }\n"
        "  clean += body.slice(lastIndex);\n"
        "  if (!markers.length) throw new Error('Chapter ' + num + ' has no [[SCENE:NNNN]] markers');\n"
        "  if (clean.length > 9500) throw new Error('Chapter ' + num + ' exceeds TTS char limit');\n"
        "  return { json: { chapter_label: 'chapter_' + num, text: clean, scene_markers: markers } };\n"
        "});"
    )},
})
connect("Voice Production Agent", "Parse Chapters")

nodes.append({
    "id": "tts", "name": "ElevenLabs TTS (with-timestamps)",
    "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
    "position": [1800, 700],
    "retryOnFail": True, "maxTries": 2, "waitBetweenTries": 5000,
    "parameters": {
        "method": "POST",
        "url": "https://api.elevenlabs.io/v1/text-to-speech/" + VOICE_ID + "/with-timestamps?output_format=mp3_44100_128",
        "sendHeaders": True,
        "headerParameters": {"parameters": [
            {"name": "xi-api-key", "value": el_key},
            {"name": "Content-Type", "value": "application/json"},
        ]},
        "sendBody": True,
        "specifyBody": "json",
        "jsonBody": "={{ JSON.stringify({ text: $json.text, model_id: 'eleven_multilingual_v2' }) }}",
        "options": {
            "timeout": 300000,
            "batching": {"batch": {"batchSize": 1, "batchInterval": 20000}},
        },
    },
})
connect("Parse Chapters", "ElevenLabs TTS (with-timestamps)")

# --- branch B: image prompts -> fal.ai Flux schnell -> png files ---
nodes.append({
    "id": "parse_prompts", "name": "Parse Image Prompts",
    "type": "n8n-nodes-base.code", "typeVersion": 2,
    "position": [1800, 1000],
    "parameters": {"jsCode": (
        "let txt = $('Image Planning Agent').first().json.content"
        ".filter(b => b.type === 'text').map(b => b.text).join('\\n').trim();\n"
        "const fence = txt.match(/```(?:json)?\\s*([\\s\\S]*?)```/);\n"
        "if (fence) txt = fence[1];\n"
        "const data = JSON.parse(txt.slice(txt.indexOf('{'), txt.lastIndexOf('}') + 1));\n"
        "if (!data.prompts || !data.prompts.length) throw new Error('No prompts parsed');\n"
        "// Stage 3 contract: Image Generation Agent merges style_tags into the prompt string\n"
        "return data.prompts.map(p => ({ json: { scene_id: p.scene_id, "
        "prompt: p.prompt + ', ' + (p.style_tags || []).join(', ') } }));"
    )},
})
connect("Image Planning Agent", "Parse Image Prompts")

nodes.append({
    "id": "fal_gen", "name": "fal Flux schnell",
    "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
    "position": [2000, 1000],
    "retryOnFail": True, "maxTries": 2, "waitBetweenTries": 3000,
    "parameters": {
        "method": "POST",
        "url": "https://fal.run/fal-ai/flux/schnell",
        "sendHeaders": True,
        "headerParameters": {"parameters": [
            {"name": "Authorization", "value": "Key " + fal_key},
            {"name": "Content-Type", "value": "application/json"},
        ]},
        "sendBody": True,
        "specifyBody": "json",
        "jsonBody": "={{ JSON.stringify({ prompt: $json.prompt, image_size: 'landscape_16_9', num_images: 1, output_format: 'png' }) }}",
        "options": {
            "timeout": 120000,
            "batching": {"batch": {"batchSize": 1, "batchInterval": 500}},
        },
    },
})
connect("Parse Image Prompts", "fal Flux schnell")

nodes.append({
    "id": "download_img", "name": "Download Image",
    "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
    "position": [2200, 1000],
    "retryOnFail": True, "maxTries": 2, "waitBetweenTries": 3000,
    "parameters": {
        "method": "GET",
        "url": "={{ $json.images[0].url }}",
        "options": {
            "timeout": 120000,
            "batching": {"batch": {"batchSize": 1, "batchInterval": 200}},
            "response": {"response": {"responseFormat": "file", "outputPropertyName": "data"}},
        },
    },
})
connect("fal Flux schnell", "Download Image")

nodes.append({
    "id": "save_img", "name": "Save Scene Image",
    "type": "n8n-nodes-base.readWriteFile", "typeVersion": 1,
    "position": [2400, 1000],
    "parameters": {
        "operation": "write",
        "fileName": "=" + ASSETS + "/images/{{ $('Parse Image Prompts').item.json.scene_id }}.png",
        "dataPropertyName": "data",
        "options": {},
    },
})
connect("Download Image", "Save Scene Image")

workflow = {
    "id": "fa11a57e9f01ab2e",
    "name": "Fatal Affairs - Master Pipeline (local)",
    "nodes": nodes,
    "connections": conns,
    "active": False,
    "settings": {"executionTimeout": 5400},
}

# SECURITY: the generated JSON embeds real API keys - it must NEVER land inside
# the repo tree. Write to WORKFLOW_OUT_DIR (or the system temp dir by default).
import tempfile
out_dir = os.environ.get("WORKFLOW_OUT_DIR", tempfile.gettempdir())
if os.path.abspath(out_dir).startswith(os.path.abspath(REPO)):
    sys.exit("refusing to write key-bearing workflow JSON inside the repo")
out_path = os.path.join(out_dir, "n8n_master_workflow.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(workflow, f, indent=2, ensure_ascii=False)

print("wrote", out_path)
print("case_query:", CASE_QUERY)
print("nodes:", len(nodes))
for w in nodes:
    print(" -", w["name"])
