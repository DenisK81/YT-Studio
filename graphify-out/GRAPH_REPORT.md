# Graph Report - .  (2026-07-25)

## Corpus Check
- 4 files · ~88,312 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 448 nodes · 698 edges · 30 communities (20 shown, 10 thin omitted)
- Extraction: 93% EXTRACTED · 6% INFERRED · 1% AMBIGUOUS · INFERRED: 42 edges (avg confidence: 0.87)
- Token cost: 63,427 input · 0 output

## Community Hubs (Navigation)
- Visual Style & Real-Photo Policy
- Monica Sementilli Case Package
- Banfield Auto-Run & Candidates
- Core Pipeline Policies
- Config Schema Properties A
- Config Schema Properties B
- Config Schema Properties C
- Kouri Richins Case Package
- Config Schema Enum Values
- Research & Story Structure Rules
- Asset Generation Script
- Mugshot Redaction Policy
- YouTube Agent Module (real API)
- Claude Code Settings/Permissions
- Voice & Music Tool Notes
- Image Generation Tool Notes
- n8n Workflow Builder
- Channel Identity & Phase 1 Scope
- Graphify Native Integration
- Graphify Incremental Update Workflow
- Image Generation Tool
- Test-In-Isolation Policy
- Human-Gated Publishing Rule
- Tool Registry Reuse Policy
- Channel Trailer & Voice Choice
- Remotion Render Prep
- Shorts Render Prep
- No-Speculative-Scaffolding Style Rule
- Agent-As-System-Prompt Concept
- Project README

## God Nodes (most connected - your core abstractions)
1. `Video Script` - 22 edges
2. `Stage 4 Full 14-Agent Pipeline n8n Test` - 17 edges
3. `Fact-Check Report` - 17 edges
4. `Tools/remotion_assembly_tool.md (referenced, not read this chunk)` - 14 edges
5. `Brendan Banfield Auto-Run — ResearchOutput.md` - 14 edges
6. `Brendan Banfield (convicted husband)` - 14 edges
7. `Person Photos Research` - 14 edges
8. `Juliana Peres Magalhães (au pair)` - 13 edges
9. `QC Checklist` - 12 edges
10. `Shorts Agent` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Shorts Agent` --conceptually_related_to--> `Shorts release pacing rule: one strong short day-of, remaining shorts one per day after (rationale: avoid dumping all 5 shorts on day one)`  [INFERRED]
  ProductionStudio/Agents/shorts_agent.md → ProductionStudio/Agents/publishing_agent.md
- `Kouri Richins Case — Voiceover.txt` --implements--> `Template — Voiceover.txt`  [INFERRED]
  ProductionStudio/Cases/kouri-richins-fentanyl-murder/Voiceover.txt → ProductionStudio/Templates/Voiceover.txt
- `Tools/royalty_free_music_tool.md (referenced, not read this chunk)` --semantically_similar_to--> `Tools/mugshot_fetch_tool.md (referenced, not read this chunk)`  [INFERRED] [semantically similar]
  ProductionStudio/Agents/video_assembly_agent.md → ProductionStudio/Cases/brendan-banfield-double-murder/PersonPhotos.md
- `Brendan Banfield Case — SEO.md (main)` --semantically_similar_to--> `2025-2026 true-crime genre trend: victim-centered storytelling, primary-footage format, TikTok-driven virality`  [INFERRED] [semantically similar]
  ProductionStudio/Cases/brendan-banfield-double-murder/SEO.md → ProductionStudio/Cases/brendan-banfield-double-murder/auto-run-2026-07-21/ResearchOutput.md
- `Shorts Agent` --conceptually_related_to--> `No-clickbait-lies policy (rationale: true-crime audiences disengage from fake mystery/oversold claims)`  [EXTRACTED]
  ProductionStudio/Agents/shorts_agent.md → ProductionStudio/Agents/seo_agent.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Graphify Incremental Update Workflow (query-first + doc-vs-code update)** — claude_md_graphify_memory_principle, claude_md_graphify_query_first_rule, claude_md_graphify_doc_vs_code_gap, claude_md_graphify_full_update_flow, claude_md_monica_sementilli_stale_incident, claude_md_graphify_merge_shrink_guard [EXTRACTED 1.00]
- **Core production pipeline docs sharing the 64-scene structure** — productionstudio_cases_monica_sementilli_hairdresser_murder_script_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_imageprompts_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_voiceover_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_checklist_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_factcheck_doc [INFERRED 0.85]
- **Shorts/thumbnail/publish-plan coordinated release assets** — productionstudio_cases_monica_sementilli_hairdresser_murder_shorts_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_thumbnail_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_publishplan_doc [INFERRED 0.85]
- **The four central figures in the murder conspiracy** — productionstudio_cases_monica_sementilli_hairdresser_murder_script_monica_sementilli, productionstudio_cases_monica_sementilli_hairdresser_murder_script_fabio_sementilli, productionstudio_cases_monica_sementilli_hairdresser_murder_script_robert_baker, productionstudio_cases_monica_sementilli_hairdresser_murder_script_christopher_austin [EXTRACTED 1.00]
- **Brendan Banfield case Stage-1 isolated-agent test artifacts** — productionstudio_cases_brendan_banfield_double_murder_checklist, productionstudio_cases_brendan_banfield_double_murder_imageprompts, productionstudio_cases_brendan_banfield_double_murder_personphotos, productionstudio_cases_brendan_banfield_double_murder_publishplan [EXTRACTED 0.95]
- **Minimum-5-independent-sources sourcing policy applied across four case files** — productionstudio_cases_brendan_banfield_double_murder_sources, productionstudio_cases_dalia_dippolito_murder_for_hire_sources, productionstudio_cases_devyn_michaels_decapitation_sources, productionstudio_cases_eric_thompson_jon_tokuhara_murder_sources [EXTRACTED 1.00]
- **2026-07-21 automated production pipeline stages for the Brendan Banfield case** — productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_researchoutput, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_factcheck, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_script, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_imageprompts, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_seo, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_shorts, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_thumbnail, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_voiceover, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_checklist, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_publishplan [INFERRED 0.85]
- **Manual (2026-07-19) vs automated (2026-07-21) production versions of the same Banfield case deliverables** — productionstudio_cases_brendan_banfield_double_murder_script, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_script, productionstudio_cases_brendan_banfield_double_murder_seo, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_seo, productionstudio_cases_brendan_banfield_double_murder_shorts, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_shorts [INFERRED 0.85]
- **Kouri Richins Case Production Package** — productionstudio_cases_kouri_richins_fentanyl_murder_checklist, productionstudio_cases_kouri_richins_fentanyl_murder_factcheck, productionstudio_cases_kouri_richins_fentanyl_murder_script, productionstudio_cases_kouri_richins_fentanyl_murder_voiceover, productionstudio_cases_kouri_richins_fentanyl_murder_imageprompts, productionstudio_cases_kouri_richins_fentanyl_murder_seo, productionstudio_cases_kouri_richins_fentanyl_murder_shorts, productionstudio_cases_kouri_richins_fentanyl_murder_thumbnail, productionstudio_cases_kouri_richins_fentanyl_murder_publishplan, productionstudio_cases_kouri_richins_fentanyl_murder_sources [EXTRACTED 0.95]
- **Templates Fixed Output Contract Pattern** — productionstudio_templates_script, productionstudio_templates_voiceover, productionstudio_templates_imageprompts, productionstudio_templates_seo, productionstudio_templates_shorts, productionstudio_templates_checklist, productionstudio_templates_sources, productionstudio_templates_thumbnail [EXTRACTED 0.95]
- **Kouri Richins Case — Motive Triangle (Debt, Insurance, Affair)** — productionstudio_cases_kouri_richins_fentanyl_murder_sources_kouri_richins, productionstudio_cases_kouri_richins_fentanyl_murder_sources_eric_richins, productionstudio_cases_kouri_richins_fentanyl_murder_sources_robert_josh_grossman [INFERRED 0.85]
- **Stage 3 Link Contract Gaps and Fixes** — productionstudio_tests_stage3_link_audit, productionstudio_tools_image_gen_tool, productionstudio_tools_remotion_assembly_tool [INFERRED 0.80]
- **Local Phase 2 Infrastructure Bootstrap (Remotion + n8n + fal.ai)** — productionstudio_tests_stage4_n8n_local_bootstrap, productionstudio_tests_stage4_remotion_local_render_test, productionstudio_tools_image_gen_tool [EXTRACTED 1.00]
- **Real-World Asset Sourcing Tools with Channel-Owner Risk Decisions** — productionstudio_tools_mugshot_fetch_tool, productionstudio_tools_royalty_free_music_tool, productionstudio_tools_mugshot_fetch_tool_outlet_attribution_exception, productionstudio_tools_royalty_free_music_tool_sourcing_decision [INFERRED 0.75]

## Communities (30 total, 10 thin omitted)

### Community 0 - "Visual Style & Real-Photo Policy"
Cohesion: 0.07
Nodes (52): Channel fixed visual brand style (photorealistic, cinematic, 35mm, 16:9, dark backgrounds, colors #111111/#FFFFFF/#A30E15/#4D4D4D/#BDBDBD, Bebas Neue/Oswald headline), scene_id convention shared across Scene Planner, Voice, Image, Assembly agents, [[SCENE:NNNN]] inline marker convention (rationale: naive word-count estimates drifted 74% from real audio, so real caption/scene timing must come from ElevenLabs per-character alignment, not estimation), Tool Management Policy: never solve the same problem twice (rationale: avoid duplicate/competing tools), Brendan Banfield, Christine Banfield, Joseph Ryan, Image Generation Agent (+44 more)

### Community 1 - "Monica Sementilli Case Package"
Cohesion: 0.08
Nodes (50): QC Checklist, Kouri Richins production precedent (prior case that left person-photo gap undocumented), Scene 0056 garbled-text QC fix - rationale: fal.ai Flux schnell can't render legible on-screen text, so prompt rewritten to describe illegible document, Scene 0062 tonal-mismatch QC fix - rationale: original video-wall render was tonally wrong, rewritten to simple TV-glow shot, SceneList.json (estimated scene/runtime plan), Assets/audio/.../timing.json (real ElevenLabs voice timing), Austin's stabbing role flagged as ambiguous, not asserted in script - rationale: only one summarized source phrased it ambiguously, not cleanly corroborated across outlets, Fact-Check Report (+42 more)

### Community 2 - "Banfield Auto-Run & Candidates"
Cohesion: 0.13
Nodes (41): Brendan Banfield Auto-Run — Checklist.md, Brendan Banfield Auto-Run — FactCheck.md, Brendan Banfield Auto-Run — ImagePrompts.md, Brendan Banfield Auto-Run — PublishPlan.md, banfield_auto_draft.mp4 (rendered video asset), Brendan Banfield Auto-Run — ResearchOutput.md, Ana Walshe (alternate candidate case, victim), Brian Walshe (alternate candidate case, defendant) (+33 more)

### Community 3 - "Core Pipeline Policies"
Cohesion: 0.06
Nodes (36): checklist_status field (renamed from 'status' 2026-07-20 so it exactly matches Publishing Agent's gating input), Human-gated publishing rule (rationale: publishing is irreversible/public, no exceptions even in a fully automated pipeline), Shorts release pacing rule: one strong short day-of, remaining shorts one per day after (rationale: avoid dumping all 5 shorts on day one), fatal-affairs-project-brief.md (referenced, not read this chunk), Publishing Agent, Quality Control Agent, Banfield case (previously produced video; source of the real redacted mugshot reused in the trailer under the newsworthy-exception analysis), Fatal Affairs Channel Trailer (~60s movie-trailer-style channel preview, replaces unbranded preview; rendered 2026-07-25 at 30.1s/903 frames, awaiting channel owner review before manual upload) (+28 more)

### Community 4 - "Config Schema Properties A"
Cohesion: 0.05
Nodes (36): description, type, const, description, const, description, type, const (+28 more)

### Community 5 - "Config Schema Properties B"
Cohesion: 0.08
Nodes (25): const, const, const, properties, properties, type, properties, type (+17 more)

### Community 6 - "Config Schema Properties C"
Cohesion: 0.09
Nodes (22): properties, const, const, const, const, description, const, description (+14 more)

### Community 7 - "Kouri Richins Case Package"
Cohesion: 0.20
Nodes (21): Shorts Agent, Kouri Richins Case — Checklist.md, Flux Schnell On-Screen Text Rendering Limitation, Kouri Richins Case — FactCheck.md, Kouri Richins Case — ImagePrompts.md, Kouri Richins Case — PublishPlan.md, Kouri Richins Case — Script.md, Kouri Richins Case — SEO.md (+13 more)

### Community 8 - "Config Schema Enum Values"
Cohesion: 0.10
Nodes (20): default, enum, image, publish, video_assembly, voice_id, voice_model, properties (+12 more)

### Community 9 - "Research & Story Structure Rules"
Cohesion: 0.16
Nodes (18): Discovery sources for candidate cases (DOJ/USAO press feeds, r/TrueCrime, r/UnresolvedMysteries, Websleuths) distinct from the citation source list, Fixed 10-beat script structure: Hook, Conflict, Mystery, Escalation, Evidence, Twist, Investigation, Final Reveal, Aftermath, Question, No-clickbait-lies policy (rationale: true-crime audiences disengage from fake mystery/oversold claims), Research source priority list (FBI/DOJ/court docs/AP/CourtTV/Law&Crime/Oxygen; Wikipedia timeline-only; Reddit sentiment-only), Shanna Golyar, Fact Verification Agent, Research Agent, SEO Agent (+10 more)

### Community 10 - "Asset Generation Script"
Cohesion: 0.20
Nodes (16): Orchestration Decision — No n8n / No Standalone API Key for Phase 1, cmd_audio(), cmd_images(), get_bytes(), main(), parse_voiceover(), post_json(), Local, no-n8n, no-Anthropic-key asset generator for a case.  Phase 1 default ( (+8 more)

### Community 11 - "Mugshot Redaction Policy"
Cohesion: 0.15
Nodes (16): Track 1 mugshot redaction policy (Haar-cascade face+eye detection, eyes_blacked, raw file kept only for verification, never used in output), Fairfax County Police Department, Juliana Peres Magalhães, WJLA (news outlet), Brendan Banfield Case PersonPhotos, Assets/images/real_photos/banfield_mugshot_REDACTED.jpg — real photo, eyes redacted per mugshot_fetch_tool's standing policy, Real-Photo Sourcing Decision (Mugshot/Redaction Policy), Template — SEO.md (+8 more)

### Community 12 - "YouTube Agent Module (real API)"
Cohesion: 0.18
Nodes (15): cmd_auth(), cmd_channel_info(), confirm_publish(), _find_client_secret_file(), get_authenticated_service(), list_uploads(), prepare_upload(), Official YouTube Data API v3 wrapper - the single module every future publish go (+7 more)

### Community 13 - "Claude Code Settings/Permissions"
Cohesion: 0.13
Nodes (14): hooks, PreToolUse, permissions, ask, defaultMode, deny, $schema, Bash(curl *) (+6 more)

### Community 14 - "Voice & Music Tool Notes"
Cohesion: 0.22
Nodes (9): Background music — Stage 2 live-test attempt (2026-07-19), Default provider notes (ElevenLabs, verify against current docs before building), Gap closure (2026-07-19) — concrete fix for the two shape mismatches above, Implementation notes, Interface, Purpose, Real-timestamp captioning — fixed endpoint choice (2026-07-21), Stage 1/2 live-test result (2026-07-19) (+1 more)

### Community 15 - "Image Generation Tool Notes"
Cohesion: 0.25
Nodes (8): Default provider: fal.ai + Flux, Fallback / secondary providers (keep the interface provider-agnostic), Implementation notes, Interface, Purpose, Stage 2 live-test result (2026-07-19), Stage 4 live-test result (2026-07-20/21) — confirmed working through n8n, not just direct Python, Tool: image_gen_tool

### Community 16 - "n8n Workflow Builder"
Cohesion: 0.29
Nodes (3): Build the Fatal Affairs master pipeline workflow for n8n (local Phase 2 trial)., JS expr: concatenated text blocks of an Anthropic node's response., txt()

### Community 17 - "Channel Identity & Phase 1 Scope"
Cohesion: 0.40
Nodes (5): Fatal Affairs (channel), Russian in chat, English in code/docs, Molly Watson / James Addie script (first real test case), Phase 1: manual production, Phase 2: full automated pipeline

### Community 18 - "Graphify Native Integration"
Cohesion: 0.50
Nodes (4): ProductionStudio/Documentation/ARCHITECTURE.md, Knowledge graph as project's actual memory, Query graph before grep/read-cold rule, ProductionStudio (studio memory)

### Community 19 - "Graphify Incremental Update Workflow"
Cohesion: 0.67
Nodes (4): Bare `graphify update .` is AST-only, skips docs, Required full /graphify --update flow after doc edits, Don't force a shrinking merge unless stubs confirmed, Monica Sementilli case went un-indexed (stale-graph incident)

## Ambiguous Edges - Review These
- `Brendan Banfield Case PersonPhotos` → `Juliana Peres Magalhães`  [AMBIGUOUS]
  ProductionStudio/Cases/brendan-banfield-double-murder/PersonPhotos.md · relation: references
- `fatal-affairs-project-brief.md (referenced, not read this chunk)` → `youtube_publish_tool — wraps YouTube Data API v3 for upload + metadata, publish call always gated by explicit human confirmation`  [AMBIGUOUS]
  ProductionStudio/Tools/youtube_publish_tool.md · relation: references
- `Brendan Banfield Auto-Run — Script.md` → `Christine Banfield (victim, wife)`  [AMBIGUOUS]
  ProductionStudio/Cases/brendan-banfield-double-murder/auto-run-2026-07-21/Script.md · relation: references
- `Brendan Banfield Auto-Run — Script.md` → `Joseph Ryan (victim, second victim)`  [AMBIGUOUS]
  ProductionStudio/Cases/brendan-banfield-double-murder/auto-run-2026-07-21/Script.md · relation: references
- `Brendan Banfield Auto-Run — Thumbnail.md` → `Brendan Banfield (convicted husband)`  [AMBIGUOUS]
  ProductionStudio/Cases/brendan-banfield-double-murder/auto-run-2026-07-21/Thumbnail.md · relation: references
- `Brendan Banfield Auto-Run — Voiceover.txt` → `Christine Banfield (victim, wife)`  [AMBIGUOUS]
  ProductionStudio/Cases/brendan-banfield-double-murder/auto-run-2026-07-21/Voiceover.txt · relation: references
- `Brendan Banfield Auto-Run — Voiceover.txt` → `Joseph Ryan (victim, second victim)`  [AMBIGUOUS]
  ProductionStudio/Cases/brendan-banfield-double-murder/auto-run-2026-07-21/Voiceover.txt · relation: references

## Knowledge Gaps
- **148 isolated node(s):** `$schema`, `title`, `type`, `type`, `const` (+143 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Brendan Banfield Case PersonPhotos` and `Juliana Peres Magalhães`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `fatal-affairs-project-brief.md (referenced, not read this chunk)` and `youtube_publish_tool — wraps YouTube Data API v3 for upload + metadata, publish call always gated by explicit human confirmation`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Brendan Banfield Auto-Run — Script.md` and `Christine Banfield (victim, wife)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Brendan Banfield Auto-Run — Script.md` and `Joseph Ryan (victim, second victim)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Brendan Banfield Auto-Run — Thumbnail.md` and `Brendan Banfield (convicted husband)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Brendan Banfield Auto-Run — Voiceover.txt` and `Christine Banfield (victim, wife)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Brendan Banfield Auto-Run — Voiceover.txt` and `Joseph Ryan (victim, second victim)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._