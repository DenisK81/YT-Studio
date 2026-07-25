# Graph Report - .  (2026-07-25)

## Corpus Check
- 22 files · ~86,017 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 406 nodes · 698 edges · 19 communities (16 shown, 3 thin omitted)
- Extraction: 94% EXTRACTED · 5% INFERRED · 1% AMBIGUOUS · INFERRED: 35 edges (avg confidence: 0.88)
- Token cost: 123,889 input · 0 output

## Community Hubs (Navigation)
- Visual Style & Real-Photo Policy
- Cross-Case QC & Fact-Flagging
- Core Pipeline Policies
- Banfield Auto-Run & Candidates
- Config Schema Properties A
- Config Schema Properties B
- Config Schema Enum Values
- Config Schema Properties C
- Asset Generation Script
- Kouri Richins Case Files
- Voice & Music Tool Notes
- Claude Code Settings/Permissions
- Research & Discovery Sources
- Image Generation Tool
- Test Plan Stages
- n8n Workflow Builder
- Remotion Render Prep
- Shorts Render Prep
- Project README

## God Nodes (most connected - your core abstractions)
1. `ARCHITECTURE.md (referenced, not read this chunk)` - 25 edges
2. `Video Script` - 22 edges
3. `CLAUDE.md (Project Instructions)` - 18 edges
4. `Stage 4 Full 14-Agent Pipeline n8n Test` - 17 edges
5. `Fact-Check Report` - 17 edges
6. `Tools/remotion_assembly_tool.md (referenced, not read this chunk)` - 15 edges
7. `Brendan Banfield Auto-Run — ResearchOutput.md` - 14 edges
8. `Brendan Banfield (convicted husband)` - 14 edges
9. `Person Photos Research` - 14 edges
10. `Juliana Peres Magalhães (au pair)` - 13 edges

## Surprising Connections (you probably didn't know these)
- `Video Assembly Agent` --conceptually_related_to--> `Remotion (video assembly)`  [EXTRACTED]
  ProductionStudio/Agents/video_assembly_agent.md → CLAUDE.md
- `Brendan Banfield Case Checklist` --references--> `Phase 2: full automated pipeline (n8n, agents wired end-to-end, auto-publishing)`  [EXTRACTED]
  ProductionStudio/Cases/brendan-banfield-double-murder/Checklist.md → CLAUDE.md
- `ARCHITECTURE.md (referenced, not read this chunk)` --references--> `Template — Thumbnail.md`  [EXTRACTED]
  CLAUDE.md → ProductionStudio/Templates/Thumbnail.md
- `James Addie` --conceptually_related_to--> `Shanna Golyar`  [AMBIGUOUS]
  CLAUDE.md → ProductionStudio/Agents/story_agent.md
- `CLAUDE.md (Project Instructions)` --references--> `Human-gated publishing rule (rationale: publishing is irreversible/public, no exceptions even in a fully automated pipeline)`  [EXTRACTED]
  CLAUDE.md → ProductionStudio/Agents/publishing_agent.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core production pipeline docs sharing the 64-scene structure** — productionstudio_cases_monica_sementilli_hairdresser_murder_script_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_imageprompts_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_voiceover_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_checklist_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_factcheck_doc [INFERRED 0.85]
- **Shorts/thumbnail/publish-plan coordinated release assets** — productionstudio_cases_monica_sementilli_hairdresser_murder_shorts_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_thumbnail_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_publishplan_doc [INFERRED 0.85]
- **The four central figures in the murder conspiracy** — productionstudio_cases_monica_sementilli_hairdresser_murder_script_monica_sementilli, productionstudio_cases_monica_sementilli_hairdresser_murder_script_fabio_sementilli, productionstudio_cases_monica_sementilli_hairdresser_murder_script_robert_baker, productionstudio_cases_monica_sementilli_hairdresser_murder_script_christopher_austin [EXTRACTED 1.00]
- **Fatal Affairs Studio production-pipeline agent chain (Research -> Fact Verification -> Story -> Scene Planner -> Voice/Image Planning -> Image Generation -> Video Assembly -> Shorts -> SEO/Thumbnail -> Quality Control -> Publishing)** — productionstudio_agents_research_agent, productionstudio_agents_fact_verification_agent, productionstudio_agents_story_agent, productionstudio_agents_scene_planner_agent, productionstudio_agents_voice_production_agent, productionstudio_agents_image_planning_agent, productionstudio_agents_image_generation_agent, productionstudio_agents_video_assembly_agent, productionstudio_agents_shorts_agent, productionstudio_agents_seo_agent, productionstudio_agents_thumbnail_agent, productionstudio_agents_quality_control_agent, productionstudio_agents_publishing_agent [EXTRACTED 0.95]
- **Brendan Banfield case Stage-1 isolated-agent test artifacts** — productionstudio_cases_brendan_banfield_double_murder_checklist, productionstudio_cases_brendan_banfield_double_murder_imageprompts, productionstudio_cases_brendan_banfield_double_murder_personphotos, productionstudio_cases_brendan_banfield_double_murder_publishplan [EXTRACTED 0.95]
- **Phase 1 (manual, Node-less) vs Phase 2 (full automated pipeline) scoping decisions** — claude_md, kickoff_prompt, productionstudio_agents_video_assembly_agent, productionstudio_cases_brendan_banfield_double_murder_checklist, concept_phase1_manual_production, concept_phase2_automated_pipeline [INFERRED 0.85]
- **Minimum-5-independent-sources sourcing policy applied across four case files** — productionstudio_cases_brendan_banfield_double_murder_sources, productionstudio_cases_dalia_dippolito_murder_for_hire_sources, productionstudio_cases_devyn_michaels_decapitation_sources, productionstudio_cases_eric_thompson_jon_tokuhara_murder_sources [EXTRACTED 1.00]
- **2026-07-21 automated production pipeline stages for the Brendan Banfield case** — productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_researchoutput, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_factcheck, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_script, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_imageprompts, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_seo, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_shorts, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_thumbnail, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_voiceover, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_checklist, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_publishplan [INFERRED 0.85]
- **Manual (2026-07-19) vs automated (2026-07-21) production versions of the same Banfield case deliverables** — productionstudio_cases_brendan_banfield_double_murder_script, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_script, productionstudio_cases_brendan_banfield_double_murder_seo, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_seo, productionstudio_cases_brendan_banfield_double_murder_shorts, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_shorts [INFERRED 0.85]
- **Kouri Richins Case Production Package** — productionstudio_cases_kouri_richins_fentanyl_murder_checklist, productionstudio_cases_kouri_richins_fentanyl_murder_factcheck, productionstudio_cases_kouri_richins_fentanyl_murder_script, productionstudio_cases_kouri_richins_fentanyl_murder_voiceover, productionstudio_cases_kouri_richins_fentanyl_murder_imageprompts, productionstudio_cases_kouri_richins_fentanyl_murder_seo, productionstudio_cases_kouri_richins_fentanyl_murder_shorts, productionstudio_cases_kouri_richins_fentanyl_murder_thumbnail, productionstudio_cases_kouri_richins_fentanyl_murder_publishplan, productionstudio_cases_kouri_richins_fentanyl_murder_sources [EXTRACTED 0.95]
- **Templates Fixed Output Contract Pattern** — productionstudio_templates_script, productionstudio_templates_voiceover, productionstudio_templates_imageprompts, productionstudio_templates_seo, productionstudio_templates_shorts, productionstudio_templates_checklist, productionstudio_templates_sources, productionstudio_templates_thumbnail [EXTRACTED 0.95]
- **Kouri Richins Case — Motive Triangle (Debt, Insurance, Affair)** — productionstudio_cases_kouri_richins_fentanyl_murder_sources_kouri_richins, productionstudio_cases_kouri_richins_fentanyl_murder_sources_eric_richins, productionstudio_cases_kouri_richins_fentanyl_murder_sources_robert_josh_grossman [INFERRED 0.85]
- **Stage 3 Link Contract Gaps and Fixes** — productionstudio_tests_stage3_link_audit, productionstudio_tools_image_gen_tool, productionstudio_tools_remotion_assembly_tool [INFERRED 0.80]
- **Local Phase 2 Infrastructure Bootstrap (Remotion + n8n + fal.ai)** — productionstudio_tests_stage4_n8n_local_bootstrap, productionstudio_tests_stage4_remotion_local_render_test, productionstudio_tools_image_gen_tool [EXTRACTED 1.00]
- **Real-World Asset Sourcing Tools with Channel-Owner Risk Decisions** — productionstudio_tools_mugshot_fetch_tool, productionstudio_tools_royalty_free_music_tool, productionstudio_tools_mugshot_fetch_tool_outlet_attribution_exception, productionstudio_tools_royalty_free_music_tool_sourcing_decision [INFERRED 0.75]

## Communities (19 total, 3 thin omitted)

### Community 0 - "Visual Style & Real-Photo Policy"
Cohesion: 0.07
Nodes (58): Channel fixed visual brand style (photorealistic, cinematic, 35mm, 16:9, dark backgrounds, colors #111111/#FFFFFF/#A30E15/#4D4D4D/#BDBDBD, Bebas Neue/Oswald headline), scene_id convention shared across Scene Planner, Voice, Image, Assembly agents, [[SCENE:NNNN]] inline marker convention (rationale: naive word-count estimates drifted 74% from real audio, so real caption/scene timing must come from ElevenLabs per-character alignment, not estimation), Track 1 mugshot redaction policy (Haar-cascade face+eye detection, eyes_blacked, raw file kept only for verification, never used in output), Brendan Banfield, Christine Banfield, Fairfax County Police Department, Joseph Ryan (+50 more)

### Community 1 - "Cross-Case QC & Fact-Flagging"
Cohesion: 0.08
Nodes (50): QC Checklist, Kouri Richins production precedent (prior case that left person-photo gap undocumented), Scene 0056 garbled-text QC fix - rationale: fal.ai Flux schnell can't render legible on-screen text, so prompt rewritten to describe illegible document, Scene 0062 tonal-mismatch QC fix - rationale: original video-wall render was tonally wrong, rewritten to simple TV-glow shot, SceneList.json (estimated scene/runtime plan), Assets/audio/.../timing.json (real ElevenLabs voice timing), Austin's stabbing role flagged as ambiguous, not asserted in script - rationale: only one summarized source phrased it ambiguously, not cleanly corroborated across outlets, Fact-Check Report (+42 more)

### Community 2 - "Core Pipeline Policies"
Cohesion: 0.06
Nodes (42): CLAUDE.md (Project Instructions), checklist_status field (renamed from 'status' 2026-07-20 so it exactly matches Publishing Agent's gating input), ElevenLabs Studio API (Voice), fal.ai + Flux schnell (Phase 1 default image provider), Fixed 10-beat script structure: Hook, Conflict, Mystery, Escalation, Evidence, Twist, Investigation, Final Reveal, Aftermath, Question, User's Hetzner VPS (intended n8n host, not yet installed), Human-gated publishing rule (rationale: publishing is irreversible/public, no exceptions even in a fully automated pipeline), Image Policy: never depend on a single image provider (Flux default, Leonardo/Replicate fallback, Midjourney manual-only) (+34 more)

### Community 3 - "Banfield Auto-Run & Candidates"
Cohesion: 0.13
Nodes (41): Brendan Banfield Auto-Run — Checklist.md, Brendan Banfield Auto-Run — FactCheck.md, Brendan Banfield Auto-Run — ImagePrompts.md, Brendan Banfield Auto-Run — PublishPlan.md, banfield_auto_draft.mp4 (rendered video asset), Brendan Banfield Auto-Run — ResearchOutput.md, Ana Walshe (alternate candidate case, victim), Brian Walshe (alternate candidate case, defendant) (+33 more)

### Community 4 - "Config Schema Properties A"
Cohesion: 0.06
Nodes (33): const, description, const, description, type, const, const, const (+25 more)

### Community 5 - "Config Schema Properties B"
Cohesion: 0.08
Nodes (25): const, const, const, properties, properties, type, properties, type (+17 more)

### Community 6 - "Config Schema Enum Values"
Cohesion: 0.08
Nodes (24): default, enum, image, publish, video_assembly, voice, voice_id, voice_model (+16 more)

### Community 7 - "Config Schema Properties C"
Cohesion: 0.10
Nodes (21): description, properties, type, const, const, const, const, description (+13 more)

### Community 8 - "Asset Generation Script"
Cohesion: 0.20
Nodes (16): Orchestration Decision — No n8n / No Standalone API Key for Phase 1, cmd_audio(), cmd_images(), get_bytes(), main(), parse_voiceover(), post_json(), Local, no-n8n, no-Anthropic-key asset generator for a case.  Phase 1 default ( (+8 more)

### Community 9 - "Kouri Richins Case Files"
Cohesion: 0.27
Nodes (17): Kouri Richins Case — Checklist.md, Flux Schnell On-Screen Text Rendering Limitation, Kouri Richins Case — FactCheck.md, Kouri Richins Case — ImagePrompts.md, Kouri Richins Case — PublishPlan.md, Kouri Richins Case — Script.md, Kouri Richins Case — SEO.md, Kouri Richins Case — Shorts.md (+9 more)

### Community 10 - "Voice & Music Tool Notes"
Cohesion: 0.14
Nodes (15): Background music — Stage 2 live-test attempt (2026-07-19), Default provider notes (ElevenLabs, verify against current docs before building), Gap closure (2026-07-19) — concrete fix for the two shape mismatches above, Implementation notes, Interface, Purpose, Real-timestamp captioning — fixed endpoint choice (2026-07-21), Stage 1/2 live-test result (2026-07-19) (+7 more)

### Community 11 - "Claude Code Settings/Permissions"
Cohesion: 0.15
Nodes (12): permissions, ask, defaultMode, deny, $schema, Bash(curl *), Bash(gh pr merge *), Bash(git push *) (+4 more)

### Community 12 - "Research & Discovery Sources"
Cohesion: 0.22
Nodes (13): Discovery sources for candidate cases (DOJ/USAO press feeds, r/TrueCrime, r/UnresolvedMysteries, Websleuths) distinct from the citation source list, No-clickbait-lies policy (rationale: true-crime audiences disengage from fake mystery/oversold claims), Research source priority list (FBI/DOJ/court docs/AP/CourtTV/Law&Crime/Oxygen; Wikipedia timeline-only; Reddit sentiment-only), Research Agent, SEO Agent, Cases/covered_cases.json (referenced, not read this chunk), Kouri Richins Case — Sources.md, Sonam Raghuvanshi Case — Sources.md (+5 more)

### Community 13 - "Image Generation Tool"
Cohesion: 0.25
Nodes (8): Default provider: fal.ai + Flux, Fallback / secondary providers (keep the interface provider-agnostic), Implementation notes, Interface, Purpose, Stage 2 live-test result (2026-07-19), Stage 4 live-test result (2026-07-20/21) — confirmed working through n8n, not just direct Python, Tool: image_gen_tool

### Community 14 - "Test Plan Stages"
Cohesion: 0.29
Nodes (7): Regression check, Stage 1 — Agents in isolation, Stage 2 — Tools in isolation, Stage 3 — Two-node links, Stage 4 — Full chain, one real case, dry-run publish, Stage 5 — First real publish, Test Plan

### Community 15 - "n8n Workflow Builder"
Cohesion: 0.29
Nodes (3): Build the Fatal Affairs master pipeline workflow for n8n (local Phase 2 trial)., JS expr: concatenated text blocks of an Anthropic node's response., txt()

## Ambiguous Edges - Review These
- `Brendan Banfield Case PersonPhotos` → `Juliana Peres Magalhães`  [AMBIGUOUS]
  ProductionStudio/Cases/brendan-banfield-double-murder/PersonPhotos.md · relation: references
- `Molly Watson (channel's first real test case)` → `James Addie`  [AMBIGUOUS]
  CLAUDE.md · relation: conceptually_related_to
- `James Addie` → `Shanna Golyar`  [AMBIGUOUS]
  ProductionStudio/Agents/story_agent.md · relation: conceptually_related_to
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
- **130 isolated node(s):** `$schema`, `defaultMode`, `Read(./.env)`, `Read(./**/secrets/**)`, `Read(~/.ssh/**)` (+125 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Brendan Banfield Case PersonPhotos` and `Juliana Peres Magalhães`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Molly Watson (channel's first real test case)` and `James Addie`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `James Addie` and `Shanna Golyar`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Brendan Banfield Auto-Run — Script.md` and `Christine Banfield (victim, wife)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Brendan Banfield Auto-Run — Script.md` and `Joseph Ryan (victim, second victim)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Brendan Banfield Auto-Run — Thumbnail.md` and `Brendan Banfield (convicted husband)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Brendan Banfield Auto-Run — Voiceover.txt` and `Christine Banfield (victim, wife)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._