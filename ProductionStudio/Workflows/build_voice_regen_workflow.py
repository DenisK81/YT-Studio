"""Regenerate ONLY Voice Production Agent + timestamped TTS for an existing
case, reusing its already-generated SceneList.json - no Research/Fact
Verification/Story/etc. re-run, no re-payment of the rest of the chain.

Useful whenever the voice/caption pipeline needs re-testing (e.g. after a
prompt or timing-code fix) without spending on the full 11-agent run again.

Usage:
    CASE_DIR=".../Cases/<slug>/<run>" python build_voice_regen_workflow.py
"""
import json
import os
import sys
import tempfile

REPO = "D:/SHOPS/AI Projects/YT_Crime/YT-Studio"
AGENTS = REPO + "/ProductionStudio/Agents"

CASE_DIR = os.environ.get(
    "CASE_DIR",
    REPO + "/ProductionStudio/Cases/brendan-banfield-double-murder/auto-run-2026-07-21",
)

ant_key = os.environ["ANTHROPIC_API_KEY_N8N"]
el_key = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "wSChTcAxdiTjLPhHeyrM"
MODEL_SONNET = "claude-sonnet-5"

with open(os.path.join(AGENTS, "voice_production_agent.md"), encoding="utf-8") as f:
    voice_spec = f.read()
FRAME = (
    "You are running as an automated n8n pipeline node. Follow the agent spec below "
    "exactly. Output ONLY what the spec's Output section defines - no preamble, no "
    "commentary outside the defined output.\n\n--- AGENT SPEC ---\n\n"
)
sys_voice = FRAME + voice_spec

with open(os.path.join(CASE_DIR, "SceneList.json"), encoding="utf-8") as f:
    scenes_json = f.read()

user_instruction = (
    "Scenes JSON below. OUTPUT FORMAT REQUIREMENT for this pipeline: precede each "
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
    "other double-bracket or triple-equals markup anywhere.\n\nScenes JSON:\n\n"
    + scenes_json
)

nodes = [
    {
        "id": "manual_trigger", "name": "Manual Trigger",
        "type": "n8n-nodes-base.manualTrigger", "typeVersion": 1,
        "position": [0, 300], "parameters": {},
    },
    {
        "id": "agent_prompts", "name": "Agent Prompts",
        "type": "n8n-nodes-base.set", "typeVersion": 3.4,
        "position": [200, 300],
        "parameters": {"assignments": {"assignments": [
            {"id": "p1", "name": "sys_voice", "value": sys_voice, "type": "string"},
            {"id": "p2", "name": "user_instruction", "value": user_instruction, "type": "string"},
        ]}, "options": {}},
    },
    {
        "id": "voice", "name": "Voice Production Agent",
        "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
        "position": [400, 300],
        "retryOnFail": True, "maxTries": 2, "waitBetweenTries": 5000,
        "parameters": {
            "method": "POST",
            "url": "https://api.anthropic.com/v1/messages",
            "sendHeaders": True,
            "headerParameters": {"parameters": [
                {"name": "x-api-key", "value": ant_key},
                {"name": "anthropic-version", "value": "2023-06-01"},
                {"name": "Content-Type", "value": "application/json"},
            ]},
            "sendBody": True, "specifyBody": "json",
            "jsonBody": (
                "={{ JSON.stringify({ model: '" + MODEL_SONNET + "', max_tokens: 16000, "
                "thinking: { type: 'adaptive' }, "
                "system: $('Agent Prompts').first().json.sys_voice, "
                "messages: [ { role: 'user', content: $('Agent Prompts').first().json.user_instruction } ] }) }}"
            ),
            "options": {"timeout": 600000},
        },
    },
    {
        "id": "parse_chapters", "name": "Parse Chapters",
        "type": "n8n-nodes-base.code", "typeVersion": 2,
        "position": [600, 300],
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
    },
    {
        "id": "tts", "name": "ElevenLabs TTS (with-timestamps)",
        "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
        "position": [800, 300],
        "retryOnFail": True, "maxTries": 2, "waitBetweenTries": 5000,
        "parameters": {
            "method": "POST",
            "url": "https://api.elevenlabs.io/v1/text-to-speech/" + VOICE_ID + "/with-timestamps?output_format=mp3_44100_128",
            "sendHeaders": True,
            "headerParameters": {"parameters": [
                {"name": "xi-api-key", "value": el_key},
                {"name": "Content-Type", "value": "application/json"},
            ]},
            "sendBody": True, "specifyBody": "json",
            "jsonBody": "={{ JSON.stringify({ text: $json.text, model_id: 'eleven_multilingual_v2' }) }}",
            "options": {
                "timeout": 300000,
                "batching": {"batch": {"batchSize": 1, "batchInterval": 20000}},
            },
        },
    },
]

conns = {
    "Manual Trigger": {"main": [[{"node": "Agent Prompts", "type": "main", "index": 0}]]},
    "Agent Prompts": {"main": [[{"node": "Voice Production Agent", "type": "main", "index": 0}]]},
    "Voice Production Agent": {"main": [[{"node": "Parse Chapters", "type": "main", "index": 0}]]},
    "Parse Chapters": {"main": [[{"node": "ElevenLabs TTS (with-timestamps)", "type": "main", "index": 0}]]},
}

workflow = {
    "id": "fa55e91c4d02ab7f",
    "name": "Fatal Affairs - Voice Regen (with-timestamps)",
    "nodes": nodes,
    "connections": conns,
    "active": False,
    "settings": {"executionTimeout": 1800},
}

out_dir = os.environ.get("WORKFLOW_OUT_DIR", tempfile.gettempdir())
if os.path.abspath(out_dir).startswith(os.path.abspath(REPO)):
    sys.exit("refusing to write key-bearing workflow JSON inside the repo")
out_path = os.path.join(out_dir, "n8n_voice_regen_workflow.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(workflow, f, indent=2, ensure_ascii=False)
print("wrote", out_path)
print("case:", CASE_DIR)
