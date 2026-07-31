# Graph Report - D:/SHOPS/AI Projects/YT_Crime/YT-Studio  (2026-07-31)

## Corpus Check
- 28 files · ~127,046 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 619 nodes · 939 edges · 60 communities (31 shown, 29 thin omitted)
- Extraction: 94% EXTRACTED · 5% INFERRED · 1% AMBIGUOUS · INFERRED: 51 edges (avg confidence: 0.87)
- Token cost: 0 input · 265,407 output

## Community Hubs (Navigation)
- Devyn Michaels Case QC & Production
- Walter Buchanan Case QC & Production
- Monica Sementilli Case QC & Production
- Config Schema Properties
- Config Schema Properties (Generic)
- Brendan Banfield Auto-Run Case
- YouTube Publishing Tool
- Multi-Case Publish Plans & Playlists
- Config Schema Properties (Types)
- Channel Brand Style & SEO Agent
- Script Structure & Studio Scaffold
- Kouri Richins Case
- Case Asset Generation Script
- Rimoni Muliaga Case QC & Real Photos
- Claude Code Settings & Hooks
- Rimoni Muliaga Case Trial Details
- Walter Buchanan Image Prompts & Tool Registry
- Phase 2 n8n Testing & Pipeline Decisions
- Fatal Affairs Channel Trailer
- ElevenLabs Voice Tool
- Scene/Script Templates & Scene ID Convention
- Research Agent & Discovery Pipeline
- Test Plan Stages
- n8n Master Workflow Builder Script
- n8n Audio Post-Processing Script
- Playlist & SEO Metadata (Rimoni Muliaga)
- Case Sourcing Policy & Candidates
- Publishing Agent & Schema Fixes
- Tool Manager Agent
- Rimoni Muliaga QC & Redaction Findings
- Fact Check Tool
- AI Image Artifact QC Rule
- Chapter Loudness QC Rule
- Devyn Michaels Script & Voiceover
- Track 1 Person Photo Policy (Australia Note)
- ElevenLabs Voice Selection
- Real Photo Mandate Policy
- Remotion Render Prep Script (Main Video)
- Remotion Render Prep Script (Shorts)
- ElevenLabs Studio API
- fal.ai Flux Schnell
- Graphify Project Memory Rule
- Molly Watson / James Addie Case
- n8n Orchestrator
- Phase 1 Manual Production
- Phase 2 Automated Pipeline
- Theme-Based Playlists Policy
- Publishing Timezone Rule
- Remotion Video Assembly
- Synthetic Content Disclosure Rule
- YouTube Data API v3
- International Case Sourcing Trend
- Henderson Nevada Location
- Sandbox curl-Block Workaround
- Short: Three Kids Watched
- Short: He Accused His Own Brother
- Thumbnail CTR Growth-Gap Finding
- Visual Format Variety Finding
- Track 2 Scene Photo Policy
- YT-Studio README

## God Nodes (most connected - your core abstractions)
1. `Remotion Assembly Tool Spec` - 26 edges
2. `Video Script` - 22 edges
3. `Fact-Check Report` - 17 edges
4. `Brendan Banfield (convicted husband)` - 14 edges
5. `Stage 4 Full 14-Agent Pipeline n8n Test` - 14 edges
6. `Person Photos Research` - 14 edges
7. `get_authenticated_service()` - 14 edges
8. `Brendan Banfield Auto-Run — ResearchOutput.md` - 13 edges
9. `Juliana Peres Magalhães (au pair)` - 13 edges
10. `mugshot_fetch_tool` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Archival-Material Usage Finding (2026-07-28)` --semantically_similar_to--> `Real Photos Mandatory Per Case Policy`  [INFERRED] [semantically similar]
  ProductionStudio/Documentation/TREND_LOG.md → CLAUDE.md
- `Chapter-to-Chapter Loudness Normalization QC` --references--> `cmd_audio()`  [EXTRACTED]
  ProductionStudio/Cases/devyn-michaels-decapitation/Checklist.md → ProductionStudio/Workflows/generate_case_assets.py
- `Kouri Richins Case — Voiceover.txt` --implements--> `Template — Voiceover.txt`  [INFERRED]
  ProductionStudio/Cases/kouri-richins-fentanyl-murder/Voiceover.txt → ProductionStudio/Templates/Voiceover.txt
- `Remotion Assembly Tool Spec` --references--> `cmd_audio()`  [EXTRACTED]
  ProductionStudio/Tools/remotion_assembly_tool.md → ProductionStudio/Workflows/generate_case_assets.py
- `Remotion Assembly Tool Spec` --references--> `parse_voiceover()`  [EXTRACTED]
  ProductionStudio/Tools/remotion_assembly_tool.md → ProductionStudio/Workflows/generate_case_assets.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Henderson Decapitation Trial Participants** — productionstudio_cases_devyn_michaels_decapitation_factcheck_devyn_michaels, productionstudio_cases_devyn_michaels_decapitation_factcheck_johnathan_willette, productionstudio_cases_devyn_michaels_decapitation_factcheck_deviere_willette, productionstudio_cases_devyn_michaels_decapitation_factcheck_robert_draskovich, productionstudio_cases_devyn_michaels_decapitation_factcheck_john_giordani, productionstudio_cases_devyn_michaels_decapitation_factcheck_brittni_griffith, productionstudio_cases_devyn_michaels_decapitation_factcheck_dr_stephanie_yagi [EXTRACTED 1.00]
- **Devyn Michaels 2026-07-28 QC Gates** — productionstudio_cases_devyn_michaels_decapitation_checklist_wide_redaction_margin_rule, productionstudio_cases_devyn_michaels_decapitation_checklist_visual_artifact_qc_scan, productionstudio_cases_devyn_michaels_decapitation_checklist_loudness_normalization_qc [INFERRED 0.85]
- **Devyn Michaels Shorts Batch** — productionstudio_cases_devyn_michaels_decapitation_shorts_short_1_never_tested, productionstudio_cases_devyn_michaels_decapitation_shorts_short_2_married_the_son, productionstudio_cases_devyn_michaels_decapitation_shorts_short_3_she_blamed_her_own_husband, productionstudio_cases_devyn_michaels_decapitation_shorts_short_4_buckle_up [EXTRACTED 1.00]
- **Walter Buchanan Murder Case Key Figures** — productionstudio_cases_walter_buchanan_murder_factcheck_walter_buchanan, productionstudio_cases_walter_buchanan_murder_factcheck_darrel_odhiambo, productionstudio_cases_walter_buchanan_murder_factcheck_lord_cubie, productionstudio_cases_walter_buchanan_murder_factcheck_moira_orr [EXTRACTED 1.00]
- **Walter Buchanan Case Official Government/Law-Enforcement Sources** — productionstudio_cases_walter_buchanan_murder_sources_police_scotland, productionstudio_cases_walter_buchanan_murder_sources_copfs, productionstudio_cases_walter_buchanan_murder_sources_judiciary_of_scotland [EXTRACTED 1.00]
- **Channel Intro/Outro Bumper Implementation Pipeline** — src_channelbumper_channelbumpercomponent, src_walterbuchanantrial, productionstudio_tools_remotion_assembly_tool_channel_outro_bumper_decision [INFERRED 0.85]
- **2026-07-28 Post-Publish QC Findings (Rimoni Muliaga)** — productionstudio_cases_rimoni_muliaga_jealousy_murder_checklist_redaction_margin_leak, productionstudio_cases_rimoni_muliaga_jealousy_murder_checklist_gavel_artifact, productionstudio_cases_rimoni_muliaga_jealousy_murder_checklist_loudness_swing, productionstudio_cases_rimoni_muliaga_jealousy_murder_checklist_qc_record [EXTRACTED 1.00]
- **Real Photo Sourcing Pipeline For Rimoni Muliaga Case** — productionstudio_tools_mugshot_fetch_tool_tool, productionstudio_cases_rimoni_muliaga_jealousy_murder_personphotos_court_escort_photo, productionstudio_cases_rimoni_muliaga_jealousy_murder_personphotos_prison_van_photo, productionstudio_cases_rimoni_muliaga_jealousy_murder_personphotos_redaction_reliability_note [EXTRACTED 1.00]
- **TREND_LOG Research Driving Remotion Assembly Updates** — productionstudio_documentation_trend_log_cold_open_finding, productionstudio_documentation_trend_log_visual_variety_finding [EXTRACTED 1.00]
- **YouTube's January 2026 'AI slop' enforcement policy (three-strike system) and mandatory synthetic-content disclosure toggle as the shared rationale escalating real photos from recommended to mandatory, described consistently across CLAUDE.md, ARCHITECTURE.md, TREND_LOG.md, and mugshot_fetch_tool.md** — productionstudio_documentation_architecture_real_photo_mandatory_escalation [INFERRED 0.85]
- **Research Agent's trend-tracking flow: reads TREND_LOG.md before discovery, appends new findings after, and specifically acts on the standing international-case growth-opportunity finding logged there** — productionstudio_agents_research_agent_trend_log_integration, productionstudio_agents_research_agent_international_case_finding [INFERRED 0.85]
- **Core production pipeline docs sharing the 64-scene structure** — productionstudio_cases_monica_sementilli_hairdresser_murder_script_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_imageprompts_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_voiceover_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_checklist_doc, productionstudio_cases_monica_sementilli_hairdresser_murder_factcheck_doc [INFERRED 0.85]
- **The four central figures in the murder conspiracy** — productionstudio_cases_monica_sementilli_hairdresser_murder_script_monica_sementilli, productionstudio_cases_monica_sementilli_hairdresser_murder_script_fabio_sementilli, productionstudio_cases_monica_sementilli_hairdresser_murder_script_robert_baker, productionstudio_cases_monica_sementilli_hairdresser_murder_script_christopher_austin [EXTRACTED 1.00]
- **Brendan Banfield case Stage-1 isolated-agent test artifacts** — productionstudio_cases_brendan_banfield_double_murder_checklist, productionstudio_cases_brendan_banfield_double_murder_imageprompts, productionstudio_cases_brendan_banfield_double_murder_personphotos, productionstudio_cases_brendan_banfield_double_murder_publishplan [EXTRACTED 0.95]
- **Minimum-5-independent-sources sourcing policy applied across four case files** — productionstudio_cases_brendan_banfield_double_murder_sources, productionstudio_cases_dalia_dippolito_murder_for_hire_sources, productionstudio_cases_devyn_michaels_decapitation_sources, productionstudio_cases_eric_thompson_jon_tokuhara_murder_sources [EXTRACTED 1.00]
- **2026-07-21 automated production pipeline stages for the Brendan Banfield case** — productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_researchoutput, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_factcheck, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_script, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_imageprompts, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_seo, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_shorts, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_thumbnail, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_voiceover, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_checklist, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_publishplan [INFERRED 0.85]
- **Manual (2026-07-19) vs automated (2026-07-21) production versions of the same Banfield case deliverables** — productionstudio_cases_brendan_banfield_double_murder_script, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_script, productionstudio_cases_brendan_banfield_double_murder_seo, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_seo, productionstudio_cases_brendan_banfield_double_murder_shorts, productionstudio_cases_brendan_banfield_double_murder_auto_run_2026_07_21_shorts [INFERRED 0.85]
- **Kouri Richins Case Production Package** — productionstudio_cases_kouri_richins_fentanyl_murder_checklist, productionstudio_cases_kouri_richins_fentanyl_murder_factcheck, productionstudio_cases_kouri_richins_fentanyl_murder_script, productionstudio_cases_kouri_richins_fentanyl_murder_voiceover, productionstudio_cases_kouri_richins_fentanyl_murder_imageprompts, productionstudio_cases_kouri_richins_fentanyl_murder_seo, productionstudio_cases_kouri_richins_fentanyl_murder_shorts, productionstudio_cases_kouri_richins_fentanyl_murder_thumbnail, productionstudio_cases_kouri_richins_fentanyl_murder_publishplan, productionstudio_cases_kouri_richins_fentanyl_murder_sources [EXTRACTED 0.95]
- **Kouri Richins Case — Motive Triangle (Debt, Insurance, Affair)** — productionstudio_cases_kouri_richins_fentanyl_murder_sources_kouri_richins, productionstudio_cases_kouri_richins_fentanyl_murder_sources_eric_richins, productionstudio_cases_kouri_richins_fentanyl_murder_sources_robert_josh_grossman [INFERRED 0.85]
- **Stage 3 Link Contract Gaps and Fixes** — productionstudio_tests_stage3_link_audit, productionstudio_tools_image_gen_tool, productionstudio_tools_remotion_assembly_tool [INFERRED 0.80]
- **Local Phase 2 Infrastructure Bootstrap (Remotion + n8n + fal.ai)** — productionstudio_tests_stage4_n8n_local_bootstrap, productionstudio_tests_stage4_remotion_local_render_test, productionstudio_tools_image_gen_tool [EXTRACTED 1.00]

## Communities (60 total, 29 thin omitted)

### Community 0 - "Devyn Michaels Case QC & Production"
Cohesion: 0.06
Nodes (55): Devyn Michaels Case QC Checklist, ChannelBumper Integration (First Real Case), Chapter-to-Chapter Loudness Normalization QC, Playlist Decision: Love Triangle Murders, Extended Source Research (10 Outlets), Untested Swords Fact Ambiguity, Mandatory Pre-Render Visual Artifact Scan, Wide Redaction Margin Rule (30%/40%) (+47 more)

### Community 1 - "Walter Buchanan Case QC & Production"
Cohesion: 0.07
Nodes (48): quality_control_agent, Walter Buchanan Case Checklist, First Outro Bumper Use (Walter Buchanan Case), Walter Buchanan Case Fact Check, Consciousness of Guilt Finding, Darrel Odhiambo, Lord Cubie, Moira Orr (+40 more)

### Community 2 - "Monica Sementilli Case QC & Production"
Cohesion: 0.08
Nodes (48): QC Checklist, Kouri Richins production precedent (prior case that left person-photo gap undocumented), Scene 0056 garbled-text QC fix - rationale: fal.ai Flux schnell can't render legible on-screen text, so prompt rewritten to describe illegible document, Scene 0062 tonal-mismatch QC fix - rationale: original video-wall render was tonally wrong, rewritten to simple TV-glow shot, SceneList.json (estimated scene/runtime plan), Assets/audio/.../timing.json (real ElevenLabs voice timing), Austin's stabbing role flagged as ambiguous, not asserted in script - rationale: only one summarized source phrased it ambiguously, not cleanly corroborated across outlets, Fact-Check Report (+40 more)

### Community 3 - "Config Schema Properties"
Cohesion: 0.05
Nodes (42): properties, const, const, default, enum, const, const, description (+34 more)

### Community 4 - "Config Schema Properties (Generic)"
Cohesion: 0.06
Nodes (33): description, type, const, description, const, description, type, const (+25 more)

### Community 5 - "Brendan Banfield Auto-Run Case"
Cohesion: 0.19
Nodes (32): Brendan Banfield Auto-Run — Checklist.md, Brendan Banfield Auto-Run — FactCheck.md, Brendan Banfield Auto-Run — ImagePrompts.md, Brendan Banfield Auto-Run — PublishPlan.md, banfield_auto_draft.mp4 (rendered video asset), Brendan Banfield Auto-Run — ResearchOutput.md, Ana Walshe (alternate candidate case, victim), Brian Walshe (alternate candidate case, defendant) (+24 more)

### Community 6 - "YouTube Publishing Tool"
Cohesion: 0.11
Nodes (28): 5-Video Release Schedule (LA Local Time), add_video_to_playlist(), cmd_auth(), cmd_channel_info(), confirm_publish(), delete_playlist(), _find_client_secret_file(), find_playlist_by_title() (+20 more)

### Community 7 - "Multi-Case Publish Plans & Playlists"
Cohesion: 0.13
Nodes (27): awaiting_human_confirmation now false for these 4 videos only; hard rule unchanged for future publishes, Playlist: Love Triangle Murders (PLex0mHScQ9nU), Playlist: Murder For Insurance Money (PLVCbFw1Wp6mk), Updated 'playlists' field: 3 theme playlists this case's videos belong to, Release plan: main video + 4 Shorts, 2026-07-25/26/27, 2026-07-26 update: original one-short-per-day plan superseded by 2-shorts-per-day real schedule, Playlist: Wife Killed Husband (PLe6_jN9U_ijM), add_video_to_playlist(playlist_id, video_id) (+19 more)

### Community 8 - "Config Schema Properties (Types)"
Cohesion: 0.08
Nodes (25): const, const, const, properties, properties, type, properties, type (+17 more)

### Community 9 - "Channel Brand Style & SEO Agent"
Cohesion: 0.13
Nodes (24): Channel fixed visual brand style (photorealistic, cinematic, 35mm, 16:9, dark backgrounds, colors #111111/#FFFFFF/#A30E15/#4D4D4D/#BDBDBD, Bebas Neue/Oswald headline), Track 1 mugshot redaction policy (Haar-cascade face+eye detection, eyes_blacked, raw file kept only for verification, never used in output), Brendan Banfield, Christine Banfield, Fairfax County Police Department, Joseph Ryan, Juliana Peres Magalhães, WJLA (news outlet) (+16 more)

### Community 10 - "Script Structure & Studio Scaffold"
Cohesion: 0.10
Nodes (20): Fixed 10-beat script structure: Hook, Conflict, Mystery, Escalation, Evidence, Twist, Investigation, Final Reveal, Aftermath, Question, Human-gated publishing rule (rationale: publishing is irreversible/public, no exceptions even in a fully automated pipeline), Shorts release pacing rule: one strong short day-of, remaining shorts one per day after (rationale: avoid dumping all 5 shorts on day one), Shanna Golyar, fatal-affairs-project-brief.md (referenced, not read this chunk), Publishing Agent, Story Agent, Build order (+12 more)

### Community 11 - "Kouri Richins Case"
Cohesion: 0.19
Nodes (22): Fact Verification Agent, Kouri Richins Case — Checklist.md, Flux Schnell On-Screen Text Rendering Limitation, Kouri Richins Case — FactCheck.md, Kouri Richins Case — ImagePrompts.md, Kouri Richins Case — PublishPlan.md, Kouri Richins Case — Script.md, Kouri Richins Case — SEO.md (+14 more)

### Community 12 - "Case Asset Generation Script"
Cohesion: 0.19
Nodes (18): cmd_audio(), cmd_images(), _find_ffmpeg(), get_bytes(), main(), normalize_chapter_loudness(), parse_voiceover(), post_json() (+10 more)

### Community 13 - "Rimoni Muliaga Case QC & Real Photos"
Cohesion: 0.12
Nodes (18): Real Photos Mandatory Per Case Policy, Quality Control Agent, Real-Photo Attempt Check (mandatory QC gate), Redaction-Under-Zoom Check, Post-Publish Redaction Margin Leak (Scene 0038, Prison Van), 3 Real-Photo Scenes (0028, 0031, 0038), 45-Scene AI/Real Image Prompt Set, Muliaga Court Escort Photo (Redacted) (+10 more)

### Community 14 - "Claude Code Settings & Hooks"
Cohesion: 0.13
Nodes (14): hooks, PreToolUse, permissions, ask, defaultMode, deny, $schema, Bash(curl *) (+6 more)

### Community 15 - "Rimoni Muliaga Case Trial Details"
Cohesion: 0.22
Nodes (15): Warning-Sign Sequencing Ambiguity Finding, DPP v MULIAGA [2026] VSC 145, Justice James Gorton, Leuma Muliaga (Brother, Falsely Suspected), Lise Muliaga (Victim), Marama Randall (Sister-in-law Witness), Michael McGrath (Defense Barrister), Patrick Bourke KC (Prosecutor) (+7 more)

### Community 16 - "Walter Buchanan Image Prompts & Tool Registry"
Cohesion: 0.24
Nodes (10): Walter Buchanan Case Image Prompts, Assets/images/real_photos/banfield_mugshot_REDACTED.jpg — real photo, eyes redacted per mugshot_fetch_tool's standing policy, Template — SEO.md, SEO Export & GitHub Sync Stage 2 Test, Remotion Local Render Test, GitHub Sync Tool, mugshot_fetch_tool, royalty_free_music_tool (+2 more)

### Community 17 - "Phase 2 n8n Testing & Pipeline Decisions"
Cohesion: 0.22
Nodes (9): Mugshot Tool Stage 2 Test, Stage 4 Full 14-Agent Pipeline n8n Test, ElevenLabs Concurrency and n8n Batching Fixes, Mixed Opus/Sonnet Model Cost Optimization, Orchestration Decision: Claude Code Direct Execution over n8n, Trailing Meta-Prose Narration Bug Fix, n8n Local Bootstrap Test, CLI-Driven vs UI-Driven n8n Automation Finding (+1 more)

### Community 18 - "Fatal Affairs Channel Trailer"
Cohesion: 0.22
Nodes (9): Banfield case (previously produced video; source of the real redacted mugshot reused in the trailer under the newsworthy-exception analysis), Fatal Affairs Channel Trailer (~60s movie-trailer-style channel preview, replaces unbranded preview; rendered 2026-07-25 at 30.1s/903 frames, awaiting channel owner review before manual upload), Config/config.schema.json (source of channel name, slogan, colors, fonts used in trailer), Fatal Affairs (channel name, slogan "Every Affair Has a Story. Some End in Murder."), fal.ai Flux schnell image-generation pipeline (used for the two freshly-generated generic trailer images, corkboard.png and crimetape_rain.png, chosen over third-party stock/footage specifically to avoid a new ungoverned rights question for a channel-level asset), Kouri Richins fentanyl-murder case (already-produced video whose stills are reused as trailer collage images, cleared rights), Monica Sementilli hairdresser-murder case (already-produced video whose stills are reused as trailer collage images, cleared rights), Assets/renders/fatal-affairs-channel-trailer.mp4 (gitignored render, 1920x1080, 903 frames @ 30fps, 30.1s, spot-checked cold open/mugshot beat/logo-CTA sequence) (+1 more)

### Community 19 - "ElevenLabs Voice Tool"
Cohesion: 0.22
Nodes (9): Background music — Stage 2 live-test attempt (2026-07-19), Default provider notes (ElevenLabs, verify against current docs before building), Gap closure (2026-07-19) — concrete fix for the two shape mismatches above, Implementation notes, Interface, Purpose, Real-timestamp captioning — fixed endpoint choice (2026-07-21), Stage 1/2 live-test result (2026-07-19) (+1 more)

### Community 20 - "Scene/Script Templates & Scene ID Convention"
Cohesion: 0.32
Nodes (8): scene_id convention shared across Scene Planner, Voice, Image, Assembly agents, [[SCENE:NNNN]] inline marker convention (rationale: naive word-count estimates drifted 74% from real audio, so real caption/scene timing must come from ElevenLabs per-character alignment, not estimation), Scene Planner Agent, Video Assembly Agent, Voice Production Agent, ProductionStudio/Assets README, Template — Script.md, Template — Voiceover.txt

### Community 21 - "Research Agent & Discovery Pipeline"
Cohesion: 0.29
Nodes (7): Covered-case memory (added 2026-07-21): Cases/covered_cases.json injected as 'covered_cases' input on every discovery run; never propose a case already on that list — added after the pipeline independently re-picked the already-in-production Banfield case, Discovery sources (added 2026-07-19), distinct from the fixed citation-source list: DOJ/USAO/state AG press-release feeds and forums (r/TrueCrime, r/UnresolvedMysteries, Websleuths) are valid for finding candidates, though anything found still needs the full citation-source verification pass, Research Agent — given a case query, gathers raw factual material from priority sources and produces a structured case brief, never a finished script, Trend tracking integration (broadened 2026-07-26): Research Agent must read Documentation/TREND_LOG.md before starting a new discovery run (avoid re-searching recently logged findings) and append any new finding after the run, in TREND_LOG.md's documented format, Full agent pipeline: Research -> Fact Verification -> Story -> Scene Planner -> Voice/Image -> Video Assembly -> Shorts/Thumbnail/SEO -> Quality Control -> Publishing (human-gated), Shorts Agent requirement (2026-07-19): new shorts_agent.md runs immediately after Video Assembly Agent, hard 45s cap per Short, one hook under 3 seconds, fixed karaoke caption style, Trend-grounding requirement (2026-07-19): Research Agent must run a real web search for genre_trend_notes every run rather than asserting trends from memory; a trending frame must never override the facts of a case

### Community 22 - "Test Plan Stages"
Cohesion: 0.29
Nodes (7): Regression check, Stage 1 — Agents in isolation, Stage 2 — Tools in isolation, Stage 3 — Two-node links, Stage 4 — Full chain, one real case, dry-run publish, Stage 5 — First real publish, Test Plan

### Community 23 - "n8n Master Workflow Builder Script"
Cohesion: 0.29
Nodes (3): Build the Fatal Affairs master pipeline workflow for n8n (local Phase 2 trial)., JS expr: concatenated text blocks of an Anthropic node's response., txt()

### Community 24 - "n8n Audio Post-Processing Script"
Cohesion: 0.43
Nodes (6): load_rawoutput(), main(), node_items(), Post-process an n8n execution's rawOutput after the ElevenLabs with-timestamps, Group a per-character alignment into per-word (start, end, word) spans,     spl, word_spans()

### Community 25 - "Playlist & SEO Metadata (Rimoni Muliaga)"
Cohesion: 0.47
Nodes (6): Channel Footer Required In Descriptions, Love Triangle Murders (Playlist), Wife Killed Husband (Playlist), Playlist Assignment Gap Finding, Unfounded Jealousy Murders Playlist (PLcyGDM96lozc), Rimoni Muliaga SEO Metadata (titles/description/tags)

### Community 26 - "Case Sourcing Policy & Candidates"
Cohesion: 0.33
Nodes (6): Minimum 5 independent sources sourcing policy, Dalia Dippolito Case — Sources.md, Dalia Dippolito (defendant), Eric Thompson Case — Sources.md, Eric Thompson (defendant), Jon Tokuhara (victim)

### Community 27 - "Publishing Agent & Schema Fixes"
Cohesion: 0.40
Nodes (5): Publishing Agent (Agents/publishing_agent.md), youtube_agent.py (Workflows), checklist_status Field (renamed from status), Rimoni Muliaga Release Plan (5 videos), Stage 3 link contracts (2026-07-20): 4 real schema mismatches found and fixed between adjacent agents, including QC's 'status' field renamed to 'checklist_status' to match Publishing Agent's expected input exactly

### Community 28 - "Tool Manager Agent"
Cohesion: 0.60
Nodes (4): Tool Management Policy: never solve the same problem twice (rationale: avoid duplicate/competing tools), Tool Manager Agent, Tests/stage1_tool_manager_agent_test.md (referenced, not read this chunk), extend_existing Output Shape

### Community 29 - "Rimoni Muliaga QC & Redaction Findings"
Cohesion: 0.50
Nodes (4): Rimoni Muliaga QC Checklist Record, Automated Redaction Reliability Note (Haar Cascade Failure), Cold-Open/Bumper Retention Finding (2026-07-28), Automated OpenCV Redaction Method

### Community 30 - "Fact Check Tool"
Cohesion: 1.00
Nodes (3): Fact Check Tool Stage 2 Test, Fact Check Tool, Fixed Source Priority Ranking

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
- **175 isolated node(s):** `$schema`, `title`, `type`, `type`, `const` (+170 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **29 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

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
- **Why does `Remotion Assembly Tool Spec` connect `Walter Buchanan Case QC & Production` to `Devyn Michaels Case QC & Production`, `Channel Brand Style & SEO Agent`, `Kouri Richins Case`, `Case Asset Generation Script`, `Walter Buchanan Image Prompts & Tool Registry`, `Phase 2 n8n Testing & Pipeline Decisions`, `Scene/Script Templates & Scene ID Convention`, `n8n Audio Post-Processing Script`, `Tool Manager Agent`?**
  _High betweenness centrality (0.242) - this node is a cross-community bridge._