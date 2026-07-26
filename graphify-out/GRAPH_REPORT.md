# Graph Report - .  (2026-07-25)

## Corpus Check
- 4 files · ~89,499 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 468 nodes · 768 edges · 27 communities (22 shown, 5 thin omitted)
- Extraction: 92% EXTRACTED · 7% INFERRED · 1% AMBIGUOUS · INFERRED: 53 edges (avg confidence: 0.9)
- Token cost: 80,924 input · 0 output

## Community Hubs (Navigation)
- Monica Sementilli Case Package
- Playlist Theme Rules & Scheduling
- Banfield Auto-Run & Candidates
- Research & Story Structure Rules
- Config Schema Properties A
- YouTube Agent Module (real API)
- Config Schema Properties B
- Core Pipeline Policies
- Config Schema Properties C
- Mugshot Redaction Policy
- Config Schema Enum Values
- Asset Generation Script
- Claude Code Settings/Permissions
- Scene Marker & Timing Convention
- Visual Style & Brand Identity
- n8n Orchestration History
- Brendan Banfield Case Package
- Voice & Music Tool Notes
- Image Generation Tool Notes
- Test Plan Stages
- n8n Workflow Builder Script
- Audio Post-Processing Script
- Channel Trailer Voice Choice
- Remotion Render Prep
- Shorts Render Prep
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
8. `get_authenticated_service()` - 14 edges
9. `Juliana Peres Magalhães (au pair)` - 13 edges
10. `QC Checklist` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Playlists are by theme/motive, never by case name (decided 2026-07-26)` --semantically_similar_to--> `Playlists (added 2026-07-26, revised same day): pivot from per-case to theme playlists`  [INFERRED] [semantically similar]
  CLAUDE.md → ProductionStudio/Tools/youtube_publish_tool.md
- `Playlist: Love Triangle Murders` --semantically_similar_to--> `Playlist: Love Triangle Murders (PLex0mHScQ9nU)`  [INFERRED] [semantically similar]
  CLAUDE.md → ProductionStudio/Cases/monica-sementilli-hairdresser-murder/PublishPlan.md
- `Playlist: Love Triangle Murders` --semantically_similar_to--> `Playlist: Love Triangle Murders`  [INFERRED] [semantically similar]
  CLAUDE.md → ProductionStudio/Tools/youtube_publish_tool.md
- `Playlist: Wife Killed Husband` --semantically_similar_to--> `Playlist: Wife Killed Husband (PLe6_jN9U_ijM)`  [INFERRED] [semantically similar]
  CLAUDE.md → ProductionStudio/Cases/monica-sementilli-hairdresser-murder/PublishPlan.md
- `Playlist: Wife Killed Husband` --semantically_similar_to--> `Playlist: Wife Killed Husband`  [INFERRED] [semantically similar]
  CLAUDE.md → ProductionStudio/Tools/youtube_publish_tool.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core production pipeline docs sharing the 64-scene structure** — productionstudio_cases_monica_sementilli_hairdresser_murder_script_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_imageprompts_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_voiceover_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_checklist_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_factcheck_doc [INFERRED 0.85]
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

## Communities (27 total, 5 thin omitted)

### Community 0 - "Monica Sementilli Case Package"
Cohesion: 0.08
Nodes (48): QC Checklist, Kouri Richins production precedent (prior case that left person-photo gap undocumented), Scene 0056 garbled-text QC fix - rationale: fal.ai Flux schnell can't render legible on-screen text, so prompt rewritten to describe illegible document, Scene 0062 tonal-mismatch QC fix - rationale: original video-wall render was tonally wrong, rewritten to simple TV-glow shot, SceneList.json (estimated scene/runtime plan), Assets/audio/.../timing.json (real ElevenLabs voice timing), Austin's stabbing role flagged as ambiguous, not asserted in script - rationale: only one summarized source phrased it ambiguously, not cleanly corroborated across outlets, Fact-Check Report (+40 more)

### Community 1 - "Playlist Theme Rules & Scheduling"
Cohesion: 0.10
Nodes (38): youtube_agent.py add_video_to_playlist(), added as soon as each video is uploaded, youtube_agent.py get_or_create_playlist() (idempotent by title), A video normally belongs in 2-3 theme playlists at once (overlap expected, not a bug), Playlist: Framed The Wrong Person, Playlist: Love Triangle Murders, Playlist: Murder For Insurance Money, Playlists are by theme/motive, never by case name (decided 2026-07-26), Playlist: Wife Killed Husband (+30 more)

### Community 2 - "Banfield Auto-Run & Candidates"
Cohesion: 0.13
Nodes (41): Brendan Banfield Auto-Run — Checklist.md, Brendan Banfield Auto-Run — FactCheck.md, Brendan Banfield Auto-Run — ImagePrompts.md, Brendan Banfield Auto-Run — PublishPlan.md, banfield_auto_draft.mp4 (rendered video asset), Brendan Banfield Auto-Run — ResearchOutput.md, Ana Walshe (alternate candidate case, victim), Brian Walshe (alternate candidate case, defendant) (+33 more)

### Community 3 - "Research & Story Structure Rules"
Cohesion: 0.07
Nodes (34): Discovery sources for candidate cases (DOJ/USAO press feeds, r/TrueCrime, r/UnresolvedMysteries, Websleuths) distinct from the citation source list, Fixed 10-beat script structure: Hook, Conflict, Mystery, Escalation, Evidence, Twist, Investigation, Final Reveal, Aftermath, Question, No-clickbait-lies policy (rationale: true-crime audiences disengage from fake mystery/oversold claims), Research source priority list (FBI/DOJ/court docs/AP/CourtTV/Law&Crime/Oxygen; Wikipedia timeline-only; Reddit sentiment-only), Shanna Golyar, fatal-affairs-project-brief.md (referenced, not read this chunk), Fact Verification Agent, Research Agent (+26 more)

### Community 4 - "Config Schema Properties A"
Cohesion: 0.06
Nodes (33): description, type, const, description, const, description, type, const (+25 more)

### Community 5 - "YouTube Agent Module (real API)"
Cohesion: 0.11
Nodes (27): add_video_to_playlist(), cmd_auth(), cmd_channel_info(), confirm_publish(), delete_playlist(), _find_client_secret_file(), find_playlist_by_title(), get_authenticated_service() (+19 more)

### Community 6 - "Config Schema Properties B"
Cohesion: 0.08
Nodes (25): const, const, const, properties, properties, type, properties, type (+17 more)

### Community 7 - "Core Pipeline Policies"
Cohesion: 0.16
Nodes (24): checklist_status field (renamed from 'status' 2026-07-20 so it exactly matches Publishing Agent's gating input), Human-gated publishing rule (rationale: publishing is irreversible/public, no exceptions even in a fully automated pipeline), Shorts release pacing rule: one strong short day-of, remaining shorts one per day after (rationale: avoid dumping all 5 shorts on day one), Publishing Agent, Quality Control Agent, Kouri Richins Case — Checklist.md, Flux Schnell On-Screen Text Rendering Limitation, Kouri Richins Case — FactCheck.md (+16 more)

### Community 8 - "Config Schema Properties C"
Cohesion: 0.09
Nodes (22): properties, const, const, const, const, description, const, description (+14 more)

### Community 9 - "Mugshot Redaction Policy"
Cohesion: 0.10
Nodes (21): Track 1 mugshot redaction policy (Haar-cascade face+eye detection, eyes_blacked, raw file kept only for verification, never used in output), Fairfax County Police Department, Juliana Peres Magalhães, WJLA (news outlet), Brendan Banfield Case PersonPhotos, Banfield case (previously produced video; source of the real redacted mugshot reused in the trailer under the newsworthy-exception analysis), Assets/images/real_photos/banfield_mugshot_REDACTED.jpg — real photo, eyes redacted per mugshot_fetch_tool's standing policy, Fatal Affairs Channel Trailer (~60s movie-trailer-style channel preview, replaces unbranded preview; rendered 2026-07-25 at 30.1s/903 frames, awaiting channel owner review before manual upload) (+13 more)

### Community 10 - "Config Schema Enum Values"
Cohesion: 0.10
Nodes (20): default, enum, image, publish, video_assembly, voice_id, voice_model, properties (+12 more)

### Community 11 - "Asset Generation Script"
Cohesion: 0.22
Nodes (15): cmd_audio(), cmd_images(), get_bytes(), main(), parse_voiceover(), post_json(), Local, no-n8n, no-Anthropic-key asset generator for a case.  Phase 1 default (, Group per-character alignment into (start, end, word) spans on whitespace. (+7 more)

### Community 12 - "Claude Code Settings/Permissions"
Cohesion: 0.13
Nodes (14): hooks, PreToolUse, permissions, ask, defaultMode, deny, $schema, Bash(curl *) (+6 more)

### Community 13 - "Scene Marker & Timing Convention"
Cohesion: 0.21
Nodes (14): scene_id convention shared across Scene Planner, Voice, Image, Assembly agents, [[SCENE:NNNN]] inline marker convention (rationale: naive word-count estimates drifted 74% from real audio, so real caption/scene timing must come from ElevenLabs per-character alignment, not estimation), Tool Management Policy: never solve the same problem twice (rationale: avoid duplicate/competing tools), Scene Planner Agent, Tool Manager Agent, Video Assembly Agent, Voice Production Agent, ProductionStudio/Assets README (+6 more)

### Community 14 - "Visual Style & Brand Identity"
Cohesion: 0.26
Nodes (11): Channel fixed visual brand style (photorealistic, cinematic, 35mm, 16:9, dark backgrounds, colors #111111/#FFFFFF/#A30E15/#4D4D4D/#BDBDBD, Bebas Neue/Oswald headline), Image Generation Agent, Image Planning Agent, Shorts Agent, Thumbnail Agent, Shorts Visual Style Requirement, Template — ImagePrompts.md, Template — Shorts.md (+3 more)

### Community 15 - "n8n Orchestration History"
Cohesion: 0.27
Nodes (11): Orchestration Decision — No n8n / No Standalone API Key for Phase 1, Stage 4 Full 14-Agent Pipeline n8n Test, ElevenLabs Concurrency and n8n Batching Fixes, Mixed Opus/Sonnet Model Cost Optimization, Orchestration Decision: Claude Code Direct Execution over n8n, Trailing Meta-Prose Narration Bug Fix, Remotion Local Render Test, Tools/remotion_assembly_tool.md (referenced, not read this chunk) (+3 more)

### Community 16 - "Brendan Banfield Case Package"
Cohesion: 0.29
Nodes (10): Brendan Banfield, Christine Banfield, Joseph Ryan, Brendan Banfield Case Checklist, Brendan Banfield Case ImagePrompts, Brendan Banfield Case PublishPlan, Brendan Banfield Case SceneList.json (referenced, not read this chunk), $schema (+2 more)

### Community 17 - "Voice & Music Tool Notes"
Cohesion: 0.22
Nodes (9): Background music — Stage 2 live-test attempt (2026-07-19), Default provider notes (ElevenLabs, verify against current docs before building), Gap closure (2026-07-19) — concrete fix for the two shape mismatches above, Implementation notes, Interface, Purpose, Real-timestamp captioning — fixed endpoint choice (2026-07-21), Stage 1/2 live-test result (2026-07-19) (+1 more)

### Community 18 - "Image Generation Tool Notes"
Cohesion: 0.25
Nodes (8): Default provider: fal.ai + Flux, Fallback / secondary providers (keep the interface provider-agnostic), Implementation notes, Interface, Purpose, Stage 2 live-test result (2026-07-19), Stage 4 live-test result (2026-07-20/21) — confirmed working through n8n, not just direct Python, Tool: image_gen_tool

### Community 19 - "Test Plan Stages"
Cohesion: 0.29
Nodes (7): Regression check, Stage 1 — Agents in isolation, Stage 2 — Tools in isolation, Stage 3 — Two-node links, Stage 4 — Full chain, one real case, dry-run publish, Stage 5 — First real publish, Test Plan

### Community 20 - "n8n Workflow Builder Script"
Cohesion: 0.29
Nodes (3): Build the Fatal Affairs master pipeline workflow for n8n (local Phase 2 trial)., JS expr: concatenated text blocks of an Anthropic node's response., txt()

### Community 21 - "Audio Post-Processing Script"
Cohesion: 0.43
Nodes (6): load_rawoutput(), main(), node_items(), Post-process an n8n execution's rawOutput after the ElevenLabs with-timestamps, Group a per-character alignment into per-word (start, end, word) spans,     spl, word_spans()

## Ambiguous Edges - Review These
- `Brendan Banfield Case PersonPhotos` → `Juliana Peres Magalhães`  [AMBIGUOUS]
  ProductionStudio/Cases/brendan-banfield-double-murder/PersonPhotos.md · relation: references
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
- **141 isolated node(s):** `$schema`, `title`, `type`, `type`, `const` (+136 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Brendan Banfield Case PersonPhotos` and `Juliana Peres Magalhães`?**
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
- **Why does `properties` connect `Config Schema Properties A` to `Brendan Banfield Case Package`?**
  _High betweenness centrality (0.204) - this node is a cross-community bridge._