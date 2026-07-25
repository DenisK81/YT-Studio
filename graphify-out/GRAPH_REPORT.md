# Graph Report - .  (2026-07-24)

## Corpus Check
- 99 files · ~73,388 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 319 nodes · 564 edges · 17 communities (14 shown, 3 thin omitted)
- Extraction: 93% EXTRACTED · 6% INFERRED · 1% AMBIGUOUS · INFERRED: 32 edges (avg confidence: 0.88)
- Token cost: 536,587 input · 0 output

## Community Hubs (Navigation)
- Production Agents & Style Rules
- Project Stack & Policies
- Brendan Banfield Auto-Run
- Brendan Banfield Case & Research Policy
- Config Schema Fragments
- Config Schema: Providers & Channel
- Config Schema: Audio Tracks
- Config Schema: Voice & Publish
- Kouri Richins Case Package
- Case Asset Generator Script
- Config Schema: Captions
- Claude Settings Permissions
- Other Cases: Source Verification
- n8n Workflow Builder Script
- Remotion Render Prep Script
- Shorts Render Prep Script
- Repo Root README

## God Nodes (most connected - your core abstractions)
1. `ARCHITECTURE.md (referenced, not read this chunk)` - 25 edges
2. `CLAUDE.md (Project Instructions)` - 18 edges
3. `Stage 4 Full 14-Agent Pipeline n8n Test` - 17 edges
4. `Tools/remotion_assembly_tool.md (referenced, not read this chunk)` - 15 edges
5. `Tests/TEST_PLAN.md (referenced, not read this chunk)` - 14 edges
6. `Brendan Banfield Auto-Run — ResearchOutput.md` - 14 edges
7. `Brendan Banfield (convicted husband)` - 14 edges
8. `Juliana Peres Magalhães (au pair)` - 13 edges
9. `Shorts Agent` - 12 edges
10. `Tools/elevenlabs_voice_tool.md (referenced, not read this chunk)` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Tools/image_gen_tool.md (referenced, not read this chunk)` --semantically_similar_to--> `Tools/elevenlabs_voice_tool.md (referenced, not read this chunk)`  [INFERRED] [semantically similar]
  CLAUDE.md → ProductionStudio/Agents/voice_production_agent.md
- `Video Assembly Agent` --conceptually_related_to--> `Remotion (video assembly)`  [EXTRACTED]
  ProductionStudio/Agents/video_assembly_agent.md → CLAUDE.md
- `ARCHITECTURE.md (referenced, not read this chunk)` --references--> `Templates/Thumbnail.md (referenced, not read this chunk)`  [EXTRACTED]
  CLAUDE.md → ProductionStudio/Agents/thumbnail_agent.md
- `Tests/TEST_PLAN.md (referenced, not read this chunk)` --references--> `Orchestration Decision: Claude Code Direct Execution over n8n`  [EXTRACTED]
  CLAUDE.md → ProductionStudio/Tests/stage4_full_pipeline_n8n_test.md
- `James Addie` --conceptually_related_to--> `Shanna Golyar`  [AMBIGUOUS]
  CLAUDE.md → ProductionStudio/Agents/story_agent.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
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

## Communities (17 total, 3 thin omitted)

### Community 0 - "Production Agents & Style Rules"
Cohesion: 0.08
Nodes (52): Channel fixed visual brand style (photorealistic, cinematic, 35mm, 16:9, dark backgrounds, colors #111111/#FFFFFF/#A30E15/#4D4D4D/#BDBDBD, Bebas Neue/Oswald headline), No-clickbait-lies policy (rationale: true-crime audiences disengage from fake mystery/oversold claims), scene_id convention shared across Scene Planner, Voice, Image, Assembly agents, [[SCENE:NNNN]] inline marker convention (rationale: naive word-count estimates drifted 74% from real audio, so real caption/scene timing must come from ElevenLabs per-character alignment, not estimation), Image Generation Agent, Image Planning Agent, Scene Planner Agent, SEO Agent (+44 more)

### Community 1 - "Project Stack & Policies"
Cohesion: 0.09
Nodes (36): CLAUDE.md (Project Instructions), checklist_status field (renamed from 'status' 2026-07-20 so it exactly matches Publishing Agent's gating input), ElevenLabs Studio API (Voice), fal.ai + Flux schnell (Phase 1 default image provider), Fixed 10-beat script structure: Hook, Conflict, Mystery, Escalation, Evidence, Twist, Investigation, Final Reveal, Aftermath, Question, User's Hetzner VPS (intended n8n host, not yet installed), Human-gated publishing rule (rationale: publishing is irreversible/public, no exceptions even in a fully automated pipeline), Image Policy: never depend on a single image provider (Flux default, Leonardo/Replicate fallback, Midjourney manual-only) (+28 more)

### Community 2 - "Brendan Banfield Auto-Run"
Cohesion: 0.19
Nodes (32): Brendan Banfield Auto-Run — Checklist.md, Brendan Banfield Auto-Run — FactCheck.md, Brendan Banfield Auto-Run — ImagePrompts.md, Brendan Banfield Auto-Run — PublishPlan.md, banfield_auto_draft.mp4 (rendered video asset), Brendan Banfield Auto-Run — ResearchOutput.md, Ana Walshe (alternate candidate case, victim), Brian Walshe (alternate candidate case, defendant) (+24 more)

### Community 3 - "Brendan Banfield Case & Research Policy"
Cohesion: 0.12
Nodes (25): Discovery sources for candidate cases (DOJ/USAO press feeds, r/TrueCrime, r/UnresolvedMysteries, Websleuths) distinct from the citation source list, Phase 1: manual production, testing channel hypothesis on first 10 videos (rationale: validate the channel before investing in automation), Phase 2: full automated pipeline (n8n, agents wired end-to-end, auto-publishing), Research source priority list (FBI/DOJ/court docs/AP/CourtTV/Law&Crime/Oxygen; Wikipedia timeline-only; Reddit sentiment-only), Track 1 mugshot redaction policy (Haar-cascade face+eye detection, eyes_blacked, raw file kept only for verification, never used in output), Brendan Banfield, Christine Banfield, Fairfax County Police Department (+17 more)

### Community 4 - "Config Schema Fragments"
Cohesion: 0.08
Nodes (25): const, const, const, properties, properties, type, properties, type (+17 more)

### Community 5 - "Config Schema: Providers & Channel"
Cohesion: 0.09
Nodes (21): description, type, type, const, properties, background_music, channel, main_video_and_first_short_same_day (+13 more)

### Community 6 - "Config Schema: Audio Tracks"
Cohesion: 0.09
Nodes (22): properties, const, const, const, const, description, const, description (+14 more)

### Community 7 - "Config Schema: Voice & Publish"
Cohesion: 0.10
Nodes (20): default, enum, image, publish, video_assembly, voice_id, voice_model, properties (+12 more)

### Community 8 - "Kouri Richins Case Package"
Cohesion: 0.27
Nodes (17): Kouri Richins Case — Checklist.md, Flux Schnell On-Screen Text Rendering Limitation, Kouri Richins Case — FactCheck.md, Kouri Richins Case — ImagePrompts.md, Kouri Richins Case — PublishPlan.md, Kouri Richins Case — Script.md, Kouri Richins Case — SEO.md, Kouri Richins Case — Shorts.md (+9 more)

### Community 9 - "Case Asset Generator Script"
Cohesion: 0.22
Nodes (15): cmd_audio(), cmd_images(), get_bytes(), main(), parse_voiceover(), post_json(), Local, no-n8n, no-Anthropic-key asset generator for a case.  Phase 1 default (, Group per-character alignment into (start, end, word) spans on whitespace. (+7 more)

### Community 10 - "Config Schema: Captions"
Cohesion: 0.13
Nodes (15): const, description, const, description, const, const, description, caption_font (+7 more)

### Community 11 - "Claude Settings Permissions"
Cohesion: 0.15
Nodes (12): permissions, ask, defaultMode, deny, $schema, Bash(curl *), Bash(gh pr merge *), Bash(git push *) (+4 more)

### Community 12 - "Other Cases: Source Verification"
Cohesion: 0.25
Nodes (9): Minimum 5 independent sources sourcing policy, Dalia Dippolito Case — Sources.md, Dalia Dippolito (defendant), Devyn Michaels Case — Sources.md, Devyn Michaels (defendant), Johnathan Willette (victim), Eric Thompson Case — Sources.md, Eric Thompson (defendant) (+1 more)

### Community 13 - "n8n Workflow Builder Script"
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
- **83 isolated node(s):** `$schema`, `defaultMode`, `Read(./.env)`, `Read(./**/secrets/**)`, `Read(~/.ssh/**)` (+78 more)
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