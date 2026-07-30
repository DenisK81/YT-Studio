# Graph Report - .  (2026-07-30)

## Corpus Check
- 15 files · ~115,588 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 565 nodes · 818 edges · 57 communities (29 shown, 28 thin omitted)
- Extraction: 94% EXTRACTED · 5% INFERRED · 1% AMBIGUOUS · INFERRED: 44 edges (avg confidence: 0.89)
- Token cost: 99,965 input · 0 output

## Community Hubs (Navigation)
- Channel Brand & Publishing Policy
- QC & Timing Precedents
- Config Schema (part 1)
- Devyn Michaels Case & New QC Tooling
- Story Structure & Kickoff
- Banfield Auto-Run Case
- Sementilli Publish Plan & Playlists
- YouTube Agent API
- Config Schema (part 2)
- Config Schema (part 3)
- Real-Photo Mandate & QC Gates
- Config Schema (part 4)
- generate_case_assets.py
- Claude Settings & Hooks
- Muliaga Case People & Facts
- Tool Manager Agent
- Channel Trailer
- Music & Voice Tool Specs
- Image Gen Tool Spec
- Research Agent & Pipeline Overview
- Mugshot Tool & SEO Export Tests
- n8n Master Workflow
- process_pipeline_audio.py
- Muliaga Playlist Resolution
- Candidate Case Research (Dippolito/Thompson)
- n8n Full Pipeline Test & Orchestration Decision
- Muliaga Publishing & QC Link
- Muliaga Post-Publish QC Findings
- Chapter Loudness QC Rule
- AI Artifact Scan QC Rule
- Australia Real-Photo Jurisdiction Note
- ElevenLabs Voice IDs
- Real-Photo Sourcing Decision History
- Remotion Render Prep
- Short Render Prep
- ElevenLabs Studio API
- fal.ai Flux schnell
- graphify As Project Memory Rule
- Molly Watson / James Addie Case
- n8n Orchestrator
- Phase 1
- Phase 2
- Playlists By Theme Not Case Name
- Publishing Timezone Rule
- Altered/Synthetic Content Disclosure Check Ru
- YouTube Data API v3
- Standing finding: international/lesser-known 
- Sandbox curl-Block Workaround
- Short 2 — Three Kids Watched
- Short 3 — He Accused His Own Brother
- Thumbnail CTR Growth-Gap Finding
- Track 2 — Non-Person Scene Photos Rules
- Fixed Caption Style Spec
- Caption Timing Source-of-Truth Bug
- Background Music Mixing Spec
- Voice Agent Trailing-Prose-to-TTS Bug
- YT-Studio README

## God Nodes (most connected - your core abstractions)
1. `Video Script` - 22 edges
2. `Fact-Check Report` - 17 edges
3. `Brendan Banfield (convicted husband)` - 14 edges
4. `Stage 4 Full 14-Agent Pipeline n8n Test` - 14 edges
5. `Person Photos Research` - 14 edges
6. `get_authenticated_service()` - 14 edges
7. `Brendan Banfield Auto-Run — ResearchOutput.md` - 13 edges
8. `Juliana Peres Magalhães (au pair)` - 13 edges
9. `QC Checklist` - 12 edges
10. `Brendan Banfield Case — Script.md (main)` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Archival-Material Usage Finding (2026-07-28)` --semantically_similar_to--> `Real Photos Mandatory Per Case Policy`  [INFERRED] [semantically similar]
  ProductionStudio/Documentation/TREND_LOG.md → CLAUDE.md
- `Remotion Assembly Tool` --semantically_similar_to--> `Remotion (Video Assembly)`  [INFERRED] [semantically similar]
  ProductionStudio/Tools/remotion_assembly_tool.md → CLAUDE.md
- `Tools/royalty_free_music_tool.md (referenced, not read this chunk)` --semantically_similar_to--> `Tools/mugshot_fetch_tool.md (referenced, not read this chunk)`  [INFERRED] [semantically similar]
  ProductionStudio/Agents/video_assembly_agent.md → ProductionStudio/Cases/brendan-banfield-double-murder/PersonPhotos.md
- `Brendan Banfield Case — SEO.md (main)` --semantically_similar_to--> `2025-2026 true-crime genre trend: victim-centered storytelling, primary-footage format, TikTok-driven virality`  [INFERRED] [semantically similar]
  ProductionStudio/Cases/brendan-banfield-double-murder/SEO.md → ProductionStudio/Cases/brendan-banfield-double-murder/auto-run-2026-07-21/ResearchOutput.md
- `Kouri Richins Case — Checklist.md` --implements--> `Template — Checklist.md`  [INFERRED]
  ProductionStudio/Cases/kouri-richins-fentanyl-murder/Checklist.md → ProductionStudio/Templates/Checklist.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Real-photo redaction sourcing and max-zoom QC verification flow** — productionstudio_cases_devyn_michaels_decapitation_personphotos_michaelsbookingphoto, productionstudio_cases_devyn_michaels_decapitation_checklist_maxzoomredactionqcrule, productionstudio_cases_devyn_michaels_decapitation_personphotos_rimonimuliagacase, productionstudio_cases_devyn_michaels_decapitation_thumbnail [INFERRED 0.80]
- **Michaels/Johnathan/Deviere love-triangle structure driving playlist choice** — productionstudio_cases_devyn_michaels_decapitation_factcheck_devynmichaels, productionstudio_cases_devyn_michaels_decapitation_factcheck_johnathanwillette, productionstudio_cases_devyn_michaels_decapitation_factcheck_devierewillette, productionstudio_cases_devyn_michaels_decapitation_publishplan_lovetrianglemurdersplaylist [INFERRED 0.75]
- **Loudness measurement to permanent pipeline automation** — productionstudio_cases_devyn_michaels_decapitation_checklist_loudnessnormalizationqcrule, productionstudio_cases_devyn_michaels_decapitation_checklist_generatecaseassetscmdaudio, productionstudio_cases_devyn_michaels_decapitation_voiceover [EXTRACTED 1.00]
- **2026-07-28 Post-Publish QC Findings (Rimoni Muliaga)** — productionstudio_cases_rimoni_muliaga_jealousy_murder_checklist_redaction_margin_leak, productionstudio_cases_rimoni_muliaga_jealousy_murder_checklist_gavel_artifact, productionstudio_cases_rimoni_muliaga_jealousy_murder_checklist_loudness_swing, productionstudio_cases_rimoni_muliaga_jealousy_murder_checklist_qc_record [EXTRACTED 1.00]
- **Real Photo Sourcing Pipeline For Rimoni Muliaga Case** — productionstudio_tools_mugshot_fetch_tool_tool, productionstudio_cases_rimoni_muliaga_jealousy_murder_personphotos_court_escort_photo, productionstudio_cases_rimoni_muliaga_jealousy_murder_personphotos_prison_van_photo, productionstudio_cases_rimoni_muliaga_jealousy_murder_personphotos_redaction_reliability_note [EXTRACTED 1.00]
- **TREND_LOG Research Driving Remotion Assembly Updates** — productionstudio_documentation_trend_log_cold_open_finding, productionstudio_documentation_trend_log_visual_variety_finding, productionstudio_tools_remotion_assembly_tool_channel_bumper, productionstudio_tools_remotion_assembly_tool_tool [EXTRACTED 1.00]
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

## Communities (57 total, 28 thin omitted)

### Community 0 - "Channel Brand & Publishing Policy"
Cohesion: 0.07
Nodes (57): Channel fixed visual brand style (photorealistic, cinematic, 35mm, 16:9, dark backgrounds, colors #111111/#FFFFFF/#A30E15/#4D4D4D/#BDBDBD, Bebas Neue/Oswald headline), Human-gated publishing rule (rationale: publishing is irreversible/public, no exceptions even in a fully automated pipeline), scene_id convention shared across Scene Planner, Voice, Image, Assembly agents, [[SCENE:NNNN]] inline marker convention (rationale: naive word-count estimates drifted 74% from real audio, so real caption/scene timing must come from ElevenLabs per-character alignment, not estimation), Shorts release pacing rule: one strong short day-of, remaining shorts one per day after (rationale: avoid dumping all 5 shorts on day one), Track 1 mugshot redaction policy (Haar-cascade face+eye detection, eyes_blacked, raw file kept only for verification, never used in output), Brendan Banfield, Christine Banfield (+49 more)

### Community 1 - "QC & Timing Precedents"
Cohesion: 0.08
Nodes (48): QC Checklist, Kouri Richins production precedent (prior case that left person-photo gap undocumented), Scene 0056 garbled-text QC fix - rationale: fal.ai Flux schnell can't render legible on-screen text, so prompt rewritten to describe illegible document, Scene 0062 tonal-mismatch QC fix - rationale: original video-wall render was tonally wrong, rewritten to simple TV-glow shot, SceneList.json (estimated scene/runtime plan), Assets/audio/.../timing.json (real ElevenLabs voice timing), Austin's stabbing role flagged as ambiguous, not asserted in script - rationale: only one summarized source phrased it ambiguously, not cleanly corroborated across outlets, Fact-Check Report (+40 more)

### Community 2 - "Config Schema (part 1)"
Cohesion: 0.05
Nodes (36): description, type, const, description, const, description, type, const (+28 more)

### Community 3 - "Devyn Michaels Case & New QC Tooling"
Cohesion: 0.09
Nodes (34): Devyn Michaels Case Checklist.md, Devyn Michaels Decapitation Case (Henderson, NV), ChannelBumper.tsx (2.5s branded stinger), generate_case_assets.py cmd_audio() (automated loudness fix), Chapter-to-chapter loudness normalization QC rule (ffmpeg loudnorm, -24 LUFS), Max-zoom redaction verification QC rule, Mandatory pre-render visual-artifact scan QC rule (garbled on-screen text), Devyn Michaels Case FactCheck.md (+26 more)

### Community 4 - "Story Structure & Kickoff"
Cohesion: 0.07
Nodes (28): Fixed 10-beat script structure: Hook, Conflict, Mystery, Escalation, Evidence, Twist, Investigation, Final Reveal, Aftermath, Question, Shanna Golyar, fatal-affairs-project-brief.md (referenced, not read this chunk), Fact Verification Agent, Story Agent, Build order, Handoff to Claude Code, What NOT to do (+20 more)

### Community 5 - "Banfield Auto-Run Case"
Cohesion: 0.19
Nodes (32): Brendan Banfield Auto-Run — Checklist.md, Brendan Banfield Auto-Run — FactCheck.md, Brendan Banfield Auto-Run — ImagePrompts.md, Brendan Banfield Auto-Run — PublishPlan.md, banfield_auto_draft.mp4 (rendered video asset), Brendan Banfield Auto-Run — ResearchOutput.md, Ana Walshe (alternate candidate case, victim), Brian Walshe (alternate candidate case, defendant) (+24 more)

### Community 6 - "Sementilli Publish Plan & Playlists"
Cohesion: 0.13
Nodes (27): awaiting_human_confirmation now false for these 4 videos only; hard rule unchanged for future publishes, Playlist: Love Triangle Murders (PLex0mHScQ9nU), Playlist: Murder For Insurance Money (PLVCbFw1Wp6mk), Updated 'playlists' field: 3 theme playlists this case's videos belong to, Release plan: main video + 4 Shorts, 2026-07-25/26/27, 2026-07-26 update: original one-short-per-day plan superseded by 2-shorts-per-day real schedule, Playlist: Wife Killed Husband (PLe6_jN9U_ijM), add_video_to_playlist(playlist_id, video_id) (+19 more)

### Community 7 - "YouTube Agent API"
Cohesion: 0.11
Nodes (27): add_video_to_playlist(), cmd_auth(), cmd_channel_info(), confirm_publish(), delete_playlist(), _find_client_secret_file(), find_playlist_by_title(), get_authenticated_service() (+19 more)

### Community 8 - "Config Schema (part 2)"
Cohesion: 0.08
Nodes (25): const, const, const, properties, properties, type, properties, type (+17 more)

### Community 9 - "Config Schema (part 3)"
Cohesion: 0.09
Nodes (22): properties, const, const, const, const, description, const, description (+14 more)

### Community 10 - "Real-Photo Mandate & QC Gates"
Cohesion: 0.10
Nodes (21): Real Photos Mandatory Per Case Policy, Remotion (Video Assembly), Quality Control Agent, Real-Photo Attempt Check (mandatory QC gate), Redaction-Under-Zoom Check, Post-Publish Redaction Margin Leak (Scene 0038, Prison Van), 3 Real-Photo Scenes (0028, 0031, 0038), 45-Scene AI/Real Image Prompt Set (+13 more)

### Community 11 - "Config Schema (part 4)"
Cohesion: 0.10
Nodes (20): default, enum, image, publish, video_assembly, voice_id, voice_model, properties (+12 more)

### Community 12 - "generate_case_assets.py"
Cohesion: 0.19
Nodes (18): cmd_audio(), cmd_images(), _find_ffmpeg(), get_bytes(), main(), normalize_chapter_loudness(), parse_voiceover(), post_json() (+10 more)

### Community 13 - "Claude Settings & Hooks"
Cohesion: 0.13
Nodes (14): hooks, PreToolUse, permissions, ask, defaultMode, deny, $schema, Bash(curl *) (+6 more)

### Community 14 - "Muliaga Case People & Facts"
Cohesion: 0.22
Nodes (15): Warning-Sign Sequencing Ambiguity Finding, DPP v MULIAGA [2026] VSC 145, Justice James Gorton, Leuma Muliaga (Brother, Falsely Suspected), Lise Muliaga (Victim), Marama Randall (Sister-in-law Witness), Michael McGrath (Defense Barrister), Patrick Bourke KC (Prosecutor) (+7 more)

### Community 15 - "Tool Manager Agent"
Cohesion: 0.25
Nodes (9): Tool Management Policy: never solve the same problem twice (rationale: avoid duplicate/competing tools), Tool Manager Agent, Tests/stage1_tool_manager_agent_test.md (referenced, not read this chunk), extend_existing Output Shape, n8n Local Bootstrap Test, CLI-Driven vs UI-Driven n8n Automation Finding, Remotion Local Render Test, Tools/royalty_free_music_tool.md (referenced, not read this chunk) (+1 more)

### Community 16 - "Channel Trailer"
Cohesion: 0.22
Nodes (9): Banfield case (previously produced video; source of the real redacted mugshot reused in the trailer under the newsworthy-exception analysis), Fatal Affairs Channel Trailer (~60s movie-trailer-style channel preview, replaces unbranded preview; rendered 2026-07-25 at 30.1s/903 frames, awaiting channel owner review before manual upload), Config/config.schema.json (source of channel name, slogan, colors, fonts used in trailer), Fatal Affairs (channel name, slogan "Every Affair Has a Story. Some End in Murder."), fal.ai Flux schnell image-generation pipeline (used for the two freshly-generated generic trailer images, corkboard.png and crimetape_rain.png, chosen over third-party stock/footage specifically to avoid a new ungoverned rights question for a channel-level asset), Kouri Richins fentanyl-murder case (already-produced video whose stills are reused as trailer collage images, cleared rights), Monica Sementilli hairdresser-murder case (already-produced video whose stills are reused as trailer collage images, cleared rights), Assets/renders/fatal-affairs-channel-trailer.mp4 (gitignored render, 1920x1080, 903 frames @ 30fps, 30.1s, spot-checked cold open/mugshot beat/logo-CTA sequence) (+1 more)

### Community 17 - "Music & Voice Tool Specs"
Cohesion: 0.22
Nodes (9): Background music — Stage 2 live-test attempt (2026-07-19), Default provider notes (ElevenLabs, verify against current docs before building), Gap closure (2026-07-19) — concrete fix for the two shape mismatches above, Implementation notes, Interface, Purpose, Real-timestamp captioning — fixed endpoint choice (2026-07-21), Stage 1/2 live-test result (2026-07-19) (+1 more)

### Community 18 - "Image Gen Tool Spec"
Cohesion: 0.25
Nodes (8): Default provider: fal.ai + Flux, Fallback / secondary providers (keep the interface provider-agnostic), Implementation notes, Interface, Purpose, Stage 2 live-test result (2026-07-19), Stage 4 live-test result (2026-07-20/21) — confirmed working through n8n, not just direct Python, Tool: image_gen_tool

### Community 19 - "Research Agent & Pipeline Overview"
Cohesion: 0.29
Nodes (7): Covered-case memory (added 2026-07-21): Cases/covered_cases.json injected as 'covered_cases' input on every discovery run; never propose a case already on that list — added after the pipeline independently re-picked the already-in-production Banfield case, Discovery sources (added 2026-07-19), distinct from the fixed citation-source list: DOJ/USAO/state AG press-release feeds and forums (r/TrueCrime, r/UnresolvedMysteries, Websleuths) are valid for finding candidates, though anything found still needs the full citation-source verification pass, Research Agent — given a case query, gathers raw factual material from priority sources and produces a structured case brief, never a finished script, Trend tracking integration (broadened 2026-07-26): Research Agent must read Documentation/TREND_LOG.md before starting a new discovery run (avoid re-searching recently logged findings) and append any new finding after the run, in TREND_LOG.md's documented format, Full agent pipeline: Research -> Fact Verification -> Story -> Scene Planner -> Voice/Image -> Video Assembly -> Shorts/Thumbnail/SEO -> Quality Control -> Publishing (human-gated), Shorts Agent requirement (2026-07-19): new shorts_agent.md runs immediately after Video Assembly Agent, hard 45s cap per Short, one hook under 3 seconds, fixed karaoke caption style, Trend-grounding requirement (2026-07-19): Research Agent must run a real web search for genre_trend_notes every run rather than asserting trends from memory; a trending frame must never override the facts of a case

### Community 20 - "Mugshot Tool & SEO Export Tests"
Cohesion: 0.33
Nodes (7): Assets/images/real_photos/banfield_mugshot_REDACTED.jpg — real photo, eyes redacted per mugshot_fetch_tool's standing policy, Template — SEO.md, Mugshot Tool Stage 2 Test, SEO Export & GitHub Sync Stage 2 Test, GitHub Sync Tool, Tools/mugshot_fetch_tool.md (referenced, not read this chunk), SEO Export Tool

### Community 21 - "n8n Master Workflow"
Cohesion: 0.29
Nodes (3): Build the Fatal Affairs master pipeline workflow for n8n (local Phase 2 trial)., JS expr: concatenated text blocks of an Anthropic node's response., txt()

### Community 22 - "process_pipeline_audio.py"
Cohesion: 0.43
Nodes (6): load_rawoutput(), main(), node_items(), Post-process an n8n execution's rawOutput after the ElevenLabs with-timestamps, Group a per-character alignment into per-word (start, end, word) spans,     spl, word_spans()

### Community 23 - "Muliaga Playlist Resolution"
Cohesion: 0.47
Nodes (6): Channel Footer Required In Descriptions, Love Triangle Murders (Playlist), Wife Killed Husband (Playlist), Playlist Assignment Gap Finding, Unfounded Jealousy Murders Playlist (PLcyGDM96lozc), Rimoni Muliaga SEO Metadata (titles/description/tags)

### Community 24 - "Candidate Case Research (Dippolito/Thompson)"
Cohesion: 0.33
Nodes (6): Minimum 5 independent sources sourcing policy, Dalia Dippolito Case — Sources.md, Dalia Dippolito (defendant), Eric Thompson Case — Sources.md, Eric Thompson (defendant), Jon Tokuhara (victim)

### Community 25 - "n8n Full Pipeline Test & Orchestration Decision"
Cohesion: 0.33
Nodes (6): Stage 4 Full 14-Agent Pipeline n8n Test, ElevenLabs Concurrency and n8n Batching Fixes, Mixed Opus/Sonnet Model Cost Optimization, Orchestration Decision: Claude Code Direct Execution over n8n, Trailing Meta-Prose Narration Bug Fix, Pipeline Overview

### Community 26 - "Muliaga Publishing & QC Link"
Cohesion: 0.40
Nodes (5): Publishing Agent (Agents/publishing_agent.md), youtube_agent.py (Workflows), checklist_status Field (renamed from status), Rimoni Muliaga Release Plan (5 videos), Stage 3 link contracts (2026-07-20): 4 real schema mismatches found and fixed between adjacent agents, including QC's 'status' field renamed to 'checklist_status' to match Publishing Agent's expected input exactly

### Community 27 - "Muliaga Post-Publish QC Findings"
Cohesion: 0.50
Nodes (5): Rimoni Muliaga QC Checklist Record, Automated Redaction Reliability Note (Haar Cascade Failure), Cold-Open/Bumper Retention Finding (2026-07-28), Automated OpenCV Redaction Method, ChannelBumper.tsx (2.5s Branded Stinger)

### Community 28 - "Chapter Loudness QC Rule"
Cohesion: 1.00
Nodes (3): Chapter-to-Chapter Loudness Check, Post-Publish Chapter Loudness Swing Finding, Chapter-to-Chapter Loudness Inconsistency (Root Cause)

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
- **170 isolated node(s):** `$schema`, `title`, `type`, `type`, `const` (+165 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **28 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

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
- **Why does `Brendan Banfield Case PublishPlan` connect `Channel Brand & Publishing Policy` to `Config Schema (part 1)`?**
  _High betweenness centrality (0.116) - this node is a cross-community bridge._