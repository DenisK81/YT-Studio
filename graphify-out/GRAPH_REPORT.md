# Graph Report - .  (2026-08-05)

## Corpus Check
- 26 files · ~153,458 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 709 nodes · 1109 edges · 67 communities (35 shown, 32 thin omitted)
- Extraction: 95% EXTRACTED · 4% INFERRED · 1% AMBIGUOUS · INFERRED: 46 edges (avg confidence: 0.88)
- Token cost: 236,116 input · 0 output

## Community Hubs (Navigation)
- Publishing Rules & Pacing
- Kevin West Case Docs
- Richins Case QC Fixes
- JSON Schema Config Fields
- Thompson Release & Playlists
- Banfield Auto-Run Case
- Buchanan Case Investigation
- Thompson Case Sources & QC
- Config Schema Fields
- JSON Schema Properties
- Richins Case Documents
- Audio Generation Script
- Script Structure & Agent Handoff
- Real-Photo Redaction QC Policy
- Channel Visual Brand Style
- Claude Settings & Hooks
- Muliaga Case Trial Details
- SEO & Shorts Agent Specs
- n8n Pipeline Testing
- Scene ID & Agent Conventions
- Channel Trailer Production
- Voice/Caption Tooling Notes
- Sementilli Case Release Plan
- Research Agent Discovery Rules
- Test Plan Stages
- n8n Master Workflow Builder
- Pipeline Audio Post-Processing
- Muliaga Playlist Assignment
- Publishing & QC Field Rename
- Tool Management Policy
- Image Generation Text-Hallucination
- Muliaga QC & Redaction
- SEO Export & GitHub Sync
- Music Bed Content-ID Fix
- Fact Check Tool
- Post-Publish Artifact Finding
- Post-Publish Loudness Finding
- Devyn Michaels Script/Voiceover
- Track 1 Photo Rules
- ElevenLabs Voice Choices
- Real-Photo Mandate Policy
- Remotion Render Prep Script
- Short Render Prep Script
- ElevenLabs Voice API
- fal.ai Flux Schnell Default
- Graphify Memory Rule
- Molly Watson Case
- n8n Orchestrator
- Phase 1 Manual Production
- Phase 2 Automated Pipeline
- Theme-Based Playlists
- Publishing Timezone Rule
- Remotion Video Assembly
- Synthetic Content Disclosure
- YouTube Data API
- International Case Sourcing
- Henderson Nevada Location
- Thompson Case Script
- Thompson Case Voiceover
- Curl-Block Workaround
- Muliaga Short 2
- Muliaga Short 3
- Banfield Mugshot Photo
- Thumbnail CTR Finding
- Visual Format Variety Finding
- Track 2 Scene Photo Rules
- YT-Studio README

## God Nodes (most connected - your core abstractions)
1. `Remotion Assembly Tool Spec` - 22 edges
2. `Video Script` - 22 edges
3. `Kevin West Case — FactCheck.md` - 21 edges
4. `Fact-Check Report` - 17 edges
5. `get_authenticated_service()` - 16 edges
6. `Walter Buchanan murder of Darrel Odhiambo (case)` - 16 edges
7. `Kevin West Case — Checklist.md` - 15 edges
8. `Brendan Banfield (convicted husband)` - 14 edges
9. `Person Photos Research` - 14 edges
10. `Brendan Banfield Auto-Run — ResearchOutput.md` - 13 edges

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
- **Kevin West Murder Trial & Sentencing Participants** — productionstudio_cases_kevin_west_staged_seizure_murder_factcheck_kevin_west, productionstudio_cases_kevin_west_staged_seizure_murder_factcheck_marcy_west, productionstudio_cases_kevin_west_staged_seizure_murder_factcheck_cynthia_ward, productionstudio_cases_kevin_west_staged_seizure_murder_factcheck_judge_robert_lewis, productionstudio_cases_kevin_west_staged_seizure_murder_factcheck_ted_west, productionstudio_cases_kevin_west_staged_seizure_murder_factcheck_megan_west [INFERRED 0.85]
- **Kevin West Case Production Pipeline Documents** — productionstudio_cases_kevin_west_staged_seizure_murder_checklist, productionstudio_cases_kevin_west_staged_seizure_murder_factcheck, productionstudio_cases_kevin_west_staged_seizure_murder_imageprompts, productionstudio_cases_kevin_west_staged_seizure_murder_personphotos, productionstudio_cases_kevin_west_staged_seizure_murder_publishplan, productionstudio_cases_kevin_west_staged_seizure_murder_seo, productionstudio_cases_kevin_west_staged_seizure_murder_script, productionstudio_cases_kevin_west_staged_seizure_murder_shorts, productionstudio_cases_kevin_west_staged_seizure_murder_sources, productionstudio_cases_kevin_west_staged_seizure_murder_thumbnail, productionstudio_cases_kevin_west_staged_seizure_murder_voiceover [INFERRED 0.85]
- **Cross-Case Real-Photo Ken-Burns QC Precedent Chain** — productionstudio_cases_kevin_west_staged_seizure_murder_personphotos_kenburns_redaction_maxzoom_verification, productionstudio_cases_walter_buchanan_case, productionstudio_cases_rimoni_muliaga_case, productionstudio_cases_michael_thompson_staged_suicide_murder_case [INFERRED 0.85]
- **Real-photo Track 1 + Track 2 assets for Michael Thompson case** — productionstudio_cases_michael_thompson_staged_suicide_murder_personphotos, productionstudio_cases_michael_thompson_staged_suicide_murder_imageprompts, productionstudio_cases_michael_thompson_staged_suicide_murder_thumbnail, productionstudio_cases_michael_thompson_staged_suicide_murder_real_photo_mandate, productionstudio_cases_michael_thompson_staged_suicide_murder_michael_thompson, productionstudio_cases_michael_thompson_staged_suicide_murder_kimberley_thompson, productionstudio_cases_michael_thompson_staged_suicide_murder_nottingham_crown_court [EXTRACTED 1.00]
- **YouTube publish/schedule pipeline for Michael Thompson case** — productionstudio_cases_michael_thompson_staged_suicide_murder_publishplan, productionstudio_workflows_youtube_agent_confirm_publish, productionstudio_workflows_youtube_agent_prepare_upload, productionstudio_workflows_youtube_agent_post_comment, productionstudio_workflows_youtube_agent_add_video_to_playlist, productionstudio_agents_publishing_agent, productionstudio_cases_michael_thompson_staged_suicide_murder_husband_killed_wife_playlist [EXTRACTED 1.00]
- **Photo redaction and zoom QC process for Michael Thompson case** — productionstudio_cases_michael_thompson_staged_suicide_murder_personphotos, productionstudio_cases_michael_thompson_staged_suicide_murder_eyes_blacked_redaction, productionstudio_cases_michael_thompson_staged_suicide_murder_manual_debug_grid_method, productionstudio_cases_michael_thompson_staged_suicide_murder_max_zoom_verification, productionstudio_cases_michael_thompson_staged_suicide_murder_thumbnail [INFERRED 0.85]
- **Flux Schnell Text-Hallucination Fix Pattern Family** — productionstudio_tools_image_gen_tool_text_hallucination_monumental_architecture, productionstudio_tools_image_gen_tool_text_hallucination_branded_electronics [INFERRED 0.85]
- **Official government/law-enforcement sourcing base (Judiciary of Scotland, COPFS, Police Scotland) anchoring FactCheck.md and Sources.md** — productionstudio_cases_walter_buchanan_murder_factcheck_case, productionstudio_cases_walter_buchanan_murder_factcheck_judiciary_of_scotland, productionstudio_cases_walter_buchanan_murder_factcheck_copfs, productionstudio_cases_walter_buchanan_murder_factcheck_police_scotland, productionstudio_cases_walter_buchanan_murder_sources_doc [EXTRACTED 1.00]
- **Real-photo sourcing-to-render pipeline: PersonPhotos.md sourcing/redaction feeds ImagePrompts.md scene placement and Thumbnail.md, surfacing the portrait-crop and AVIF bugs** — productionstudio_cases_walter_buchanan_murder_personphotos_doc, productionstudio_cases_walter_buchanan_murder_imageprompts_doc, productionstudio_cases_walter_buchanan_murder_thumbnail_doc, productionstudio_cases_walter_buchanan_murder_personphotos_portrait_crop_redaction_bug, productionstudio_cases_walter_buchanan_murder_personphotos_avif_image_format_bug [EXTRACTED 1.00]
- **Publish workflow: PublishPlan.md and SEO.md drive youtube_publish_tool.md's confirm_publish()/get_or_create_playlist()/post_comment() to create the Husband Killed Wife playlist and post pinned comments** — productionstudio_cases_walter_buchanan_murder_publishplan_doc, productionstudio_cases_walter_buchanan_murder_seo_doc, productionstudio_tools_youtube_publish_tool_doc, productionstudio_cases_walter_buchanan_murder_seo_husband_killed_wife_playlist, productionstudio_tools_youtube_publish_tool_pinned_comment_automation [EXTRACTED 1.00]
- **Henderson Decapitation Trial Participants** — productionstudio_cases_devyn_michaels_decapitation_factcheck_devyn_michaels, productionstudio_cases_devyn_michaels_decapitation_factcheck_johnathan_willette, productionstudio_cases_devyn_michaels_decapitation_factcheck_deviere_willette, productionstudio_cases_devyn_michaels_decapitation_factcheck_robert_draskovich, productionstudio_cases_devyn_michaels_decapitation_factcheck_john_giordani, productionstudio_cases_devyn_michaels_decapitation_factcheck_brittni_griffith, productionstudio_cases_devyn_michaels_decapitation_factcheck_dr_stephanie_yagi [EXTRACTED 1.00]
- **Devyn Michaels 2026-07-28 QC Gates** — productionstudio_cases_devyn_michaels_decapitation_checklist_wide_redaction_margin_rule, productionstudio_cases_devyn_michaels_decapitation_checklist_visual_artifact_qc_scan, productionstudio_cases_devyn_michaels_decapitation_checklist_loudness_normalization_qc [INFERRED 0.85]
- **Devyn Michaels Shorts Batch** — productionstudio_cases_devyn_michaels_decapitation_shorts_short_1_never_tested, productionstudio_cases_devyn_michaels_decapitation_shorts_short_2_married_the_son, productionstudio_cases_devyn_michaels_decapitation_shorts_short_3_she_blamed_her_own_husband, productionstudio_cases_devyn_michaels_decapitation_shorts_short_4_buckle_up [EXTRACTED 1.00]
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
- **Stage 3 Link Contract Gaps and Fixes** — productionstudio_tests_stage3_link_audit, productionstudio_tools_remotion_assembly_tool [INFERRED 0.80]
- **Local Phase 2 Infrastructure Bootstrap (Remotion + n8n + fal.ai)** — productionstudio_tests_stage4_n8n_local_bootstrap, productionstudio_tests_stage4_remotion_local_render_test [EXTRACTED 1.00]

## Communities (67 total, 32 thin omitted)

### Community 0 - "Publishing Rules & Pacing"
Cohesion: 0.05
Nodes (58): Human-gated publishing rule (rationale: publishing is irreversible/public, no exceptions even in a fully automated pipeline), Shorts release pacing rule: one strong short day-of, remaining shorts one per day after (rationale: avoid dumping all 5 shorts on day one), Publishing Agent, Devyn Michaels Case QC Checklist, ChannelBumper Integration (First Real Case), Chapter-to-Chapter Loudness Normalization QC, Playlist Decision: Love Triangle Murders, Extended Source Research (10 Outlets) (+50 more)

### Community 1 - "Kevin West Case Docs"
Cohesion: 0.06
Nodes (56): Kevin West Case — Checklist.md, Real Photo Mandate QC Result (2 person photos + 1 scene photo sourced, Marcy West wall hit documented), SceneList.json, Kevin West Case — FactCheck.md, Brian Walker (defense attorney), Camas-Washougal Fire Department, Clark County Medical Examiner, Clark County Superior Court (+48 more)

### Community 2 - "Richins Case QC Fixes"
Cohesion: 0.08
Nodes (48): QC Checklist, Kouri Richins production precedent (prior case that left person-photo gap undocumented), Scene 0056 garbled-text QC fix - rationale: fal.ai Flux schnell can't render legible on-screen text, so prompt rewritten to describe illegible document, Scene 0062 tonal-mismatch QC fix - rationale: original video-wall render was tonally wrong, rewritten to simple TV-glow shot, SceneList.json (estimated scene/runtime plan), Assets/audio/.../timing.json (real ElevenLabs voice timing), Austin's stabbing role flagged as ambiguous, not asserted in script - rationale: only one summarized source phrased it ambiguously, not cleanly corroborated across outlets, Fact-Check Report (+40 more)

### Community 3 - "JSON Schema Config Fields"
Cohesion: 0.04
Nodes (45): description, properties, type, const, const, default, enum, const (+37 more)

### Community 4 - "Thompson Release & Playlists"
Cohesion: 0.08
Nodes (40): 5-Video Release Schedule (LA Local Time), Husband Killed Wife playlist (PLbNIKr64Fk0Y), PublishPlan.md (Michael Thompson case), SEO.md (Michael Thompson case), add_video_to_playlist(), youtube_agent.py CHANNEL_FOOTER constant, cmd_auth(), cmd_channel_info() (+32 more)

### Community 5 - "Banfield Auto-Run Case"
Cohesion: 0.14
Nodes (38): Brendan Banfield Auto-Run — Checklist.md, Brendan Banfield Auto-Run — FactCheck.md, Brendan Banfield Auto-Run — ImagePrompts.md, Brendan Banfield Auto-Run — PublishPlan.md, banfield_auto_draft.mp4 (rendered video asset), Brendan Banfield Auto-Run — ResearchOutput.md, Ana Walshe (alternate candidate case, victim), Brian Walshe (alternate candidate case, defendant) (+30 more)

### Community 6 - "Buchanan Case Investigation"
Cohesion: 0.14
Nodes (38): fal.ai Flux schnell carved/engraved-text hallucination on monumental architecture, Channel bumper added to both intro AND outro (2026-07-30 decision), Checklist.md — Walter Buchanan case QC checklist, Walter Buchanan murder of Darrel Odhiambo (case), "Consciousness of guilt" legal finding (omissions to 911/paramedics), Crown Office and Procurator Fiscal Service (COPFS), Darrel Odhiambo (victim, 37, wife), FactCheck.md — Walter Buchanan case fact verification (+30 more)

### Community 7 - "Thompson Case Sources & QC"
Cohesion: 0.11
Nodes (35): ChannelBumper.tsx intro/outro convention, Checklist.md (Michael Thompson case), Crown Prosecution Service (official source), Devyn Michaels case (prior-case precedent, referenced), Dionne Bounds (victim's sister), Crown Prosecutor Emma Cornell, Eyes-blacked redaction (30%/40% margin), FactCheck.md (Michael Thompson case) (+27 more)

### Community 8 - "Config Schema Fields"
Cohesion: 0.06
Nodes (33): const, description, const, description, type, const, const, const (+25 more)

### Community 9 - "JSON Schema Properties"
Cohesion: 0.08
Nodes (25): const, const, const, properties, properties, type, properties, type (+17 more)

### Community 10 - "Richins Case Documents"
Cohesion: 0.19
Nodes (22): Fact Verification Agent, Kouri Richins Case — Checklist.md, Flux Schnell On-Screen Text Rendering Limitation, Kouri Richins Case — FactCheck.md, Kouri Richins Case — ImagePrompts.md, Kouri Richins Case — PublishPlan.md, Kouri Richins Case — Script.md, Kouri Richins Case — SEO.md (+14 more)

### Community 11 - "Audio Generation Script"
Cohesion: 0.18
Nodes (19): Chapter-to-Chapter Loudness Normalization Fix, cmd_audio(), cmd_images(), _find_ffmpeg(), get_bytes(), main(), normalize_chapter_loudness(), parse_voiceover() (+11 more)

### Community 12 - "Script Structure & Agent Handoff"
Cohesion: 0.12
Nodes (17): Fixed 10-beat script structure: Hook, Conflict, Mystery, Escalation, Evidence, Twist, Investigation, Final Reveal, Aftermath, Question, Shanna Golyar, fatal-affairs-project-brief.md (referenced, not read this chunk), Story Agent, Build order, Handoff to Claude Code, What NOT to do, Documentation — SELF_IMPROVEMENT_PROCESS.md (+9 more)

### Community 13 - "Real-Photo Redaction QC Policy"
Cohesion: 0.12
Nodes (18): Real Photos Mandatory Per Case Policy, Quality Control Agent, Real-Photo Attempt Check (mandatory QC gate), Redaction-Under-Zoom Check, Post-Publish Redaction Margin Leak (Scene 0038, Prison Van), 3 Real-Photo Scenes (0028, 0031, 0038), 45-Scene AI/Real Image Prompt Set, Muliaga Court Escort Photo (Redacted) (+10 more)

### Community 14 - "Channel Visual Brand Style"
Cohesion: 0.20
Nodes (16): Channel fixed visual brand style (photorealistic, cinematic, 35mm, 16:9, dark backgrounds, colors #111111/#FFFFFF/#A30E15/#4D4D4D/#BDBDBD, Bebas Neue/Oswald headline), Track 1 mugshot redaction policy (Haar-cascade face+eye detection, eyes_blacked, raw file kept only for verification, never used in output), Brendan Banfield, Christine Banfield, Fairfax County Police Department, Joseph Ryan, Juliana Peres Magalhães, WJLA (news outlet) (+8 more)

### Community 15 - "Claude Settings & Hooks"
Cohesion: 0.13
Nodes (14): hooks, PreToolUse, permissions, ask, defaultMode, deny, $schema, Bash(curl *) (+6 more)

### Community 16 - "Muliaga Case Trial Details"
Cohesion: 0.22
Nodes (15): Warning-Sign Sequencing Ambiguity Finding, DPP v MULIAGA [2026] VSC 145, Justice James Gorton, Leuma Muliaga (Brother, Falsely Suspected), Lise Muliaga (Victim), Marama Randall (Sister-in-law Witness), Michael McGrath (Defense Barrister), Patrick Bourke KC (Prosecutor) (+7 more)

### Community 17 - "SEO & Shorts Agent Specs"
Cohesion: 0.19
Nodes (13): SEO Agent — generates the full SEO package (titles, description, chapters, pinned comment, tags, hashtags) for a finished video, informed by Templates/SuccessRules.md, SEO Agent 'Channel footer required' rule (added 2026-07-26) — description must always end with the CHANNEL_FOOTER constant (channel name + working @handle link) on its own line; added after a real viewer commented on a published Short asking which channel it was from, and two already-published main videos had a 'Follow Fatal Affairs' line with a broken placeholder bracket instead of an actual link — exactly the gap that caused it, SEO Agent tags/hashtags limits — tags total combined length must not exceed 500 characters (~8-15 focused tags, not padding filler); hashtags 3-5 total ordered strongest-first, never more than 15 (YouTube silently discards all hashtags past that point), Shorts Agent — runs immediately after Video Assembly Agent's final render; selects moments from the finished long-form video for standalone Shorts, writes each Short's own hook, and specifies caption/pacing treatment, Shorts Agent description channel-footer requirement (added 2026-07-26) — each Short's description must end with the CHANNEL_FOOTER constant (channel name + working @handle link) on its own line, added after a real viewer commented on a published Short asking which channel it was from, Shorts visual style (research-grounded, added 2026-07-21) — cold-open dramatic close-up face image with hook_overlay_text burned in (brand white/#A30E15, black stroke), captions center-frame (not lower-third like main video), CTA in final 3-5 seconds as bold on-screen text, hard 45-second cap per Short, ends on a genuine open question not a manufactured one, ARCHITECTURE.md, Stage 3 Two-Node Link Audit (+5 more)

### Community 18 - "n8n Pipeline Testing"
Cohesion: 0.22
Nodes (10): Mugshot Tool Stage 2 Test, Stage 4 Full 14-Agent Pipeline n8n Test, ElevenLabs Concurrency and n8n Batching Fixes, Mixed Opus/Sonnet Model Cost Optimization, Orchestration Decision: Claude Code Direct Execution over n8n, Trailing Meta-Prose Narration Bug Fix, n8n Local Bootstrap Test, CLI-Driven vs UI-Driven n8n Automation Finding (+2 more)

### Community 19 - "Scene ID & Agent Conventions"
Cohesion: 0.29
Nodes (10): scene_id convention shared across Scene Planner, Voice, Image, Assembly agents, [[SCENE:NNNN]] inline marker convention (rationale: naive word-count estimates drifted 74% from real audio, so real caption/scene timing must come from ElevenLabs per-character alignment, not estimation), Image Generation Agent, Scene Planner Agent, Video Assembly Agent, Voice Production Agent, ProductionStudio/Assets README, Template — Script.md (+2 more)

### Community 20 - "Channel Trailer Production"
Cohesion: 0.22
Nodes (9): Banfield case (previously produced video; source of the real redacted mugshot reused in the trailer under the newsworthy-exception analysis), Fatal Affairs Channel Trailer (~60s movie-trailer-style channel preview, replaces unbranded preview; rendered 2026-07-25 at 30.1s/903 frames, awaiting channel owner review before manual upload), Config/config.schema.json (source of channel name, slogan, colors, fonts used in trailer), Fatal Affairs (channel name, slogan "Every Affair Has a Story. Some End in Murder."), fal.ai Flux schnell image-generation pipeline (used for the two freshly-generated generic trailer images, corkboard.png and crimetape_rain.png, chosen over third-party stock/footage specifically to avoid a new ungoverned rights question for a channel-level asset), Kouri Richins fentanyl-murder case (already-produced video whose stills are reused as trailer collage images, cleared rights), Monica Sementilli hairdresser-murder case (already-produced video whose stills are reused as trailer collage images, cleared rights), Assets/renders/fatal-affairs-channel-trailer.mp4 (gitignored render, 1920x1080, 903 frames @ 30fps, 30.1s, spot-checked cold open/mugshot beat/logo-CTA sequence) (+1 more)

### Community 21 - "Voice/Caption Tooling Notes"
Cohesion: 0.22
Nodes (9): Background music — Stage 2 live-test attempt (2026-07-19), Default provider notes (ElevenLabs, verify against current docs before building), Gap closure (2026-07-19) — concrete fix for the two shape mismatches above, Implementation notes, Interface, Purpose, Real-timestamp captioning — fixed endpoint choice (2026-07-21), Stage 1/2 live-test result (2026-07-19) (+1 more)

### Community 22 - "Sementilli Case Release Plan"
Cohesion: 0.32
Nodes (7): awaiting_human_confirmation now false for these 4 videos only; hard rule unchanged for future publishes, Playlist: Love Triangle Murders (PLex0mHScQ9nU), Playlist: Murder For Insurance Money (PLVCbFw1Wp6mk), Updated 'playlists' field: 3 theme playlists this case's videos belong to, Release plan: main video + 4 Shorts, 2026-07-25/26/27, 2026-07-26 update: original one-short-per-day plan superseded by 2-shorts-per-day real schedule, Playlist: Wife Killed Husband (PLe6_jN9U_ijM)

### Community 23 - "Research Agent Discovery Rules"
Cohesion: 0.29
Nodes (7): Covered-case memory (added 2026-07-21): Cases/covered_cases.json injected as 'covered_cases' input on every discovery run; never propose a case already on that list — added after the pipeline independently re-picked the already-in-production Banfield case, Discovery sources (added 2026-07-19), distinct from the fixed citation-source list: DOJ/USAO/state AG press-release feeds and forums (r/TrueCrime, r/UnresolvedMysteries, Websleuths) are valid for finding candidates, though anything found still needs the full citation-source verification pass, Research Agent — given a case query, gathers raw factual material from priority sources and produces a structured case brief, never a finished script, Trend tracking integration (broadened 2026-07-26): Research Agent must read Documentation/TREND_LOG.md before starting a new discovery run (avoid re-searching recently logged findings) and append any new finding after the run, in TREND_LOG.md's documented format, Full agent pipeline: Research -> Fact Verification -> Story -> Scene Planner -> Voice/Image -> Video Assembly -> Shorts/Thumbnail/SEO -> Quality Control -> Publishing (human-gated), Shorts Agent requirement (2026-07-19): new shorts_agent.md runs immediately after Video Assembly Agent, hard 45s cap per Short, one hook under 3 seconds, fixed karaoke caption style, Trend-grounding requirement (2026-07-19): Research Agent must run a real web search for genre_trend_notes every run rather than asserting trends from memory; a trending frame must never override the facts of a case

### Community 24 - "Test Plan Stages"
Cohesion: 0.29
Nodes (7): Regression check, Stage 1 — Agents in isolation, Stage 2 — Tools in isolation, Stage 3 — Two-node links, Stage 4 — Full chain, one real case, dry-run publish, Stage 5 — First real publish, Test Plan

### Community 25 - "n8n Master Workflow Builder"
Cohesion: 0.29
Nodes (3): Build the Fatal Affairs master pipeline workflow for n8n (local Phase 2 trial)., JS expr: concatenated text blocks of an Anthropic node's response., txt()

### Community 26 - "Pipeline Audio Post-Processing"
Cohesion: 0.43
Nodes (6): load_rawoutput(), main(), node_items(), Post-process an n8n execution's rawOutput after the ElevenLabs with-timestamps, Group a per-character alignment into per-word (start, end, word) spans,     spl, word_spans()

### Community 27 - "Muliaga Playlist Assignment"
Cohesion: 0.47
Nodes (6): Channel Footer Required In Descriptions, Love Triangle Murders (Playlist), Wife Killed Husband (Playlist), Playlist Assignment Gap Finding, Unfounded Jealousy Murders Playlist (PLcyGDM96lozc), Rimoni Muliaga SEO Metadata (titles/description/tags)

### Community 28 - "Publishing & QC Field Rename"
Cohesion: 0.40
Nodes (5): Publishing Agent (Agents/publishing_agent.md), youtube_agent.py (Workflows), checklist_status Field (renamed from status), Rimoni Muliaga Release Plan (5 videos), Stage 3 link contracts (2026-07-20): 4 real schema mismatches found and fixed between adjacent agents, including QC's 'status' field renamed to 'checklist_status' to match Publishing Agent's expected input exactly

### Community 29 - "Tool Management Policy"
Cohesion: 0.60
Nodes (4): Tool Management Policy: never solve the same problem twice (rationale: avoid duplicate/competing tools), Tool Manager Agent, Tests/stage1_tool_manager_agent_test.md (referenced, not read this chunk), extend_existing Output Shape

### Community 30 - "Image Generation Text-Hallucination"
Cohesion: 0.60
Nodes (5): Image Generation Tool Spec, fal.ai Flux schnell, fal.ai nano-banana (Gemini 2.5 Flash Image), Text-Hallucination Pattern: Branded Electronics, Text-Hallucination Pattern: Monumental Architecture

### Community 31 - "Muliaga QC & Redaction"
Cohesion: 0.50
Nodes (4): Rimoni Muliaga QC Checklist Record, Automated Redaction Reliability Note (Haar Cascade Failure), Cold-Open/Bumper Retention Finding (2026-07-28), Automated OpenCV Redaction Method

### Community 32 - "SEO Export & GitHub Sync"
Cohesion: 0.67
Nodes (4): Template — SEO.md, SEO Export & GitHub Sync Stage 2 Test, GitHub Sync Tool, SEO Export Tool

### Community 33 - "Music Bed Content-ID Fix"
Cohesion: 0.83
Nodes (4): bed_05.mp3 "Dark Forest" Content ID Claim, _BED_POOL Fix Excluding bed_05, Royalty-Free Music Tool Spec, Pixabay Music 10-Track Bed Set

### Community 34 - "Fact Check Tool"
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
- **191 isolated node(s):** `$schema`, `title`, `type`, `type`, `const` (+186 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **32 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

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
- **Why does `Remotion Assembly Tool Spec` connect `SEO & Shorts Agent Specs` to `Publishing Rules & Pacing`, `Config Schema Fields`, `Richins Case Documents`, `Audio Generation Script`, `Channel Visual Brand Style`, `n8n Pipeline Testing`, `Scene ID & Agent Conventions`, `Pipeline Audio Post-Processing`, `Tool Management Policy`?**
  _High betweenness centrality (0.185) - this node is a cross-community bridge._