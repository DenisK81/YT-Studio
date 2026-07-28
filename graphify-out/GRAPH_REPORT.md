# Graph Report - .  (2026-07-27)

## Corpus Check
- 5 files · ~91,361 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 477 nodes · 739 edges · 27 communities (22 shown, 5 thin omitted)
- Extraction: 93% EXTRACTED · 6% INFERRED · 1% AMBIGUOUS · INFERRED: 48 edges (avg confidence: 0.85)
- Token cost: 68,089 input · 0 output

## Community Hubs (Navigation)
- Visual Style & Brand Identity
- Monica Sementilli Case Package
- Banfield Auto-Run & Candidates
- Config Schema Properties A
- Publishing Schedule & Playlists
- YouTube Agent Module (real API)
- Config Schema Properties B
- Channel Footer Rule
- Kouri Richins Case Package
- Config Schema Properties C
- Core Pipeline Policies
- Config Schema Enum Values
- Asset Generation Script
- Claude Code Settings/Permissions
- Graphify Native Integration
- Publishing Agent Link Fixes
- Mandatory Real-Photo QC Check
- Channel Trailer Real-Photo Reuse
- Voice & Music Tool Notes
- Image Generation Tool Notes
- Test Plan Stages
- n8n Workflow Builder
- Channel Trailer Voice Choice
- Remotion Render Prep
- Shorts Render Prep
- Trend Log: International Case Opportunity
- Project README

## God Nodes (most connected - your core abstractions)
1. `Video Script` - 22 edges
2. `Fact-Check Report` - 17 edges
3. `Stage 4 Full 14-Agent Pipeline n8n Test` - 15 edges
4. `Brendan Banfield Auto-Run — ResearchOutput.md` - 14 edges
5. `Brendan Banfield (convicted husband)` - 14 edges
6. `Person Photos Research` - 14 edges
7. `get_authenticated_service()` - 14 edges
8. `Tools/remotion_assembly_tool.md (referenced, not read this chunk)` - 13 edges
9. `Juliana Peres Magalhães (au pair)` - 13 edges
10. `QC Checklist` - 12 edges

## Surprising Connections (you probably didn't know these)
- `graphify knowledge graph at graphify-out/ treated as this project's actual memory — query before grepping/reading cold; bare 'graphify update .' is AST-only and silently skips Markdown/JSON case docs, agent specs, tool specs; full /graphify --update flow required after editing any of those before ending the session` --conceptually_related_to--> `Trend Log — persistent, cross-case memory of real trend research across the true-crime genre (YouTube, Reddit, X, competitor channels), distinct from Templates/SuccessRules.md; started 2026-07-26 after the channel owner asked for ongoing trend-tracking`  [INFERRED]
  CLAUDE.md → ProductionStudio/Documentation/TREND_LOG.md
- `Kouri Richins Case — Voiceover.txt` --implements--> `Template — Voiceover.txt`  [INFERRED]
  ProductionStudio/Cases/kouri-richins-fentanyl-murder/Voiceover.txt → ProductionStudio/Templates/Voiceover.txt
- `Brendan Banfield Case — SEO.md (main)` --semantically_similar_to--> `2025-2026 true-crime genre trend: victim-centered storytelling, primary-footage format, TikTok-driven virality`  [INFERRED] [semantically similar]
  ProductionStudio/Cases/brendan-banfield-double-murder/SEO.md → ProductionStudio/Cases/brendan-banfield-double-murder/auto-run-2026-07-21/ResearchOutput.md
- `Kouri Richins Case — Checklist.md` --implements--> `Template — Checklist.md`  [INFERRED]
  ProductionStudio/Cases/kouri-richins-fentanyl-murder/Checklist.md → ProductionStudio/Templates/Checklist.md
- `Playlist: Love Triangle Murders` --semantically_similar_to--> `Playlist: Love Triangle Murders (PLex0mHScQ9nU)`  [INFERRED] [semantically similar]
  ProductionStudio/Tools/youtube_publish_tool.md → ProductionStudio/Cases/monica-sementilli-hairdresser-murder/PublishPlan.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **YouTube's January 2026 'AI slop' enforcement policy (three-strike system) and mandatory synthetic-content disclosure toggle as the shared rationale escalating real photos from recommended to mandatory, described consistently across CLAUDE.md, ARCHITECTURE.md, TREND_LOG.md, and mugshot_fetch_tool.md** — productionstudio_documentation_architecture_real_photo_mandatory_escalation, productionstudio_tools_mugshot_fetch_tool_mandatory_escalation [INFERRED 0.85]
- **Quality Control Agent's new real-photo-attempt check and synthetic-disclosure reminder implement the ARCHITECTURE.md real-photo-mandatory escalation** — productionstudio_agents_quality_control_agent_real_photo_attempt_check, productionstudio_agents_quality_control_agent_synthetic_disclosure_reminder, productionstudio_documentation_architecture_real_photo_mandatory_escalation [INFERRED 0.85]
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

## Communities (27 total, 5 thin omitted)

### Community 0 - "Visual Style & Brand Identity"
Cohesion: 0.07
Nodes (48): Channel fixed visual brand style (photorealistic, cinematic, 35mm, 16:9, dark backgrounds, colors #111111/#FFFFFF/#A30E15/#4D4D4D/#BDBDBD, Bebas Neue/Oswald headline), scene_id convention shared across Scene Planner, Voice, Image, Assembly agents, [[SCENE:NNNN]] inline marker convention (rationale: naive word-count estimates drifted 74% from real audio, so real caption/scene timing must come from ElevenLabs per-character alignment, not estimation), Tool Management Policy: never solve the same problem twice (rationale: avoid duplicate/competing tools), Image Generation Agent, Image Planning Agent, Scene Planner Agent, Thumbnail Agent (+40 more)

### Community 1 - "Monica Sementilli Case Package"
Cohesion: 0.08
Nodes (48): QC Checklist, Kouri Richins production precedent (prior case that left person-photo gap undocumented), Scene 0056 garbled-text QC fix - rationale: fal.ai Flux schnell can't render legible on-screen text, so prompt rewritten to describe illegible document, Scene 0062 tonal-mismatch QC fix - rationale: original video-wall render was tonally wrong, rewritten to simple TV-glow shot, SceneList.json (estimated scene/runtime plan), Assets/audio/.../timing.json (real ElevenLabs voice timing), Austin's stabbing role flagged as ambiguous, not asserted in script - rationale: only one summarized source phrased it ambiguously, not cleanly corroborated across outlets, Fact-Check Report (+40 more)

### Community 2 - "Banfield Auto-Run & Candidates"
Cohesion: 0.13
Nodes (41): Brendan Banfield Auto-Run — Checklist.md, Brendan Banfield Auto-Run — FactCheck.md, Brendan Banfield Auto-Run — ImagePrompts.md, Brendan Banfield Auto-Run — PublishPlan.md, banfield_auto_draft.mp4 (rendered video asset), Brendan Banfield Auto-Run — ResearchOutput.md, Ana Walshe (alternate candidate case, victim), Brian Walshe (alternate candidate case, defendant) (+33 more)

### Community 3 - "Config Schema Properties A"
Cohesion: 0.05
Nodes (36): description, type, const, description, const, description, type, const (+28 more)

### Community 4 - "Publishing Schedule & Playlists"
Cohesion: 0.13
Nodes (27): awaiting_human_confirmation now false for these 4 videos only; hard rule unchanged for future publishes, Playlist: Love Triangle Murders (PLex0mHScQ9nU), Playlist: Murder For Insurance Money (PLVCbFw1Wp6mk), Updated 'playlists' field: 3 theme playlists this case's videos belong to, Release plan: main video + 4 Shorts, 2026-07-25/26/27, 2026-07-26 update: original one-short-per-day plan superseded by 2-shorts-per-day real schedule, Playlist: Wife Killed Husband (PLe6_jN9U_ijM), add_video_to_playlist(playlist_id, video_id) (+19 more)

### Community 5 - "YouTube Agent Module (real API)"
Cohesion: 0.11
Nodes (27): add_video_to_playlist(), cmd_auth(), cmd_channel_info(), confirm_publish(), delete_playlist(), _find_client_secret_file(), find_playlist_by_title(), get_authenticated_service() (+19 more)

### Community 6 - "Config Schema Properties B"
Cohesion: 0.08
Nodes (25): const, const, const, properties, properties, type, properties, type (+17 more)

### Community 7 - "Channel Footer Rule"
Cohesion: 0.13
Nodes (23): CHANNEL_FOOTER constant in Workflows/youtube_agent.py — channel name + working @handle link, currently https://www.youtube.com/@fatalaffairs-f1i, Every video/Short description must end with the channel name + a working link (CHANNEL_FOOTER constant) — confirmed 2026-07-26 after a real viewer commented on a published Short asking which channel it was from; retroactively applied to all 20 videos already on the channel that day; never leave a bracket placeholder like '[link to X]' in description text meant to be pasted directly into YouTube, Human-gated publishing rule (rationale: publishing is irreversible/public, no exceptions even in a fully automated pipeline), Shorts release pacing rule: one strong short day-of, remaining shorts one per day after (rationale: avoid dumping all 5 shorts on day one), Track 1 mugshot redaction policy (Haar-cascade face+eye detection, eyes_blacked, raw file kept only for verification, never used in output), Brendan Banfield, Christine Banfield, Fairfax County Police Department (+15 more)

### Community 8 - "Kouri Richins Case Package"
Cohesion: 0.19
Nodes (22): Fact Verification Agent, Kouri Richins Case — Checklist.md, Flux Schnell On-Screen Text Rendering Limitation, Kouri Richins Case — FactCheck.md, Kouri Richins Case — ImagePrompts.md, Kouri Richins Case — PublishPlan.md, Kouri Richins Case — Script.md, Kouri Richins Case — SEO.md (+14 more)

### Community 9 - "Config Schema Properties C"
Cohesion: 0.09
Nodes (22): properties, const, const, const, const, description, const, description (+14 more)

### Community 10 - "Core Pipeline Policies"
Cohesion: 0.12
Nodes (17): Fixed 10-beat script structure: Hook, Conflict, Mystery, Escalation, Evidence, Twist, Investigation, Final Reveal, Aftermath, Question, Shanna Golyar, fatal-affairs-project-brief.md (referenced, not read this chunk), Story Agent, Build order, Handoff to Claude Code, What NOT to do, Documentation — SELF_IMPROVEMENT_PROCESS.md (+9 more)

### Community 11 - "Config Schema Enum Values"
Cohesion: 0.10
Nodes (20): default, enum, image, publish, video_assembly, voice_id, voice_model, properties (+12 more)

### Community 12 - "Asset Generation Script"
Cohesion: 0.22
Nodes (15): cmd_audio(), cmd_images(), get_bytes(), main(), parse_voiceover(), post_json(), Local, no-n8n, no-Anthropic-key asset generator for a case.  Phase 1 default (, Group per-character alignment into (start, end, word) spans on whitespace. (+7 more)

### Community 13 - "Claude Code Settings/Permissions"
Cohesion: 0.13
Nodes (14): hooks, PreToolUse, permissions, ask, defaultMode, deny, $schema, Bash(curl *) (+6 more)

### Community 14 - "Graphify Native Integration"
Cohesion: 0.22
Nodes (11): graphify knowledge graph at graphify-out/ treated as this project's actual memory — query before grepping/reading cold; bare 'graphify update .' is AST-only and silently skips Markdown/JSON case docs, agent specs, tool specs; full /graphify --update flow required after editing any of those before ending the session, Molly Watson / James Addie script — first real test case; chapters 6-16 and the ending drafted separately from this repo, status of chapters 1-5 to be confirmed with user, Phase 1: manual production, testing the channel hypothesis on the first 10 videos — Phase 2 (n8n, agents wired end to end, auto-publishing) only starts once explicitly requested, Playlists are by theme/motive, never by case name (decided 2026-07-26) — replaces an earlier 'one playlist per case' attempt the channel owner rejected after checking competitor true-crime channels' organization; a video normally belongs in 2-4 themed playlists at once, Publishing timezone: America/Los_Angeles (Pacific), confirmed 2026-07-26 — scheduling planned in LA local time, converted to UTC for publishAt via a real timezone library, never hardcoded UTC offsets, Real photos mandatory per case, not optional (escalated 2026-07-26) — run both mugshot_fetch_tool tracks before Image Generation fills gaps with AI; never ship a case 100% AI-generated; rationale: concrete evidence this channel isn't YouTube's targeted 2026 'AI slop' enforcement wave (mass-produced template content, three-strike policy), Trend Log — persistent, cross-case memory of real trend research across the true-crime genre (YouTube, Reddit, X, competitor channels), distinct from Templates/SuccessRules.md; started 2026-07-26 after the channel owner asked for ongoing trend-tracking, 2026-07-26 finding: YouTube's January 2026 enforcement wave specifically targets 'AI slop' (mass-produced template AI content) under a three-strike system, plus a new 'altered or synthetic' content disclosure requirement at upload — direct platform-survival risk that is the concrete reason real photos became mandatory, rather than just a stylistic preference; synthetic-content disclosure check added to quality_control_agent.md's pre-publish checklist (+3 more)

### Community 15 - "Publishing Agent Link Fixes"
Cohesion: 0.20
Nodes (10): Stage 3 link fix (2026-07-20): output field renamed from 'status' to 'checklist_status' to match Publishing Agent's expected input field exactly, Quality Control Agent — final gate before publishing, aggregates all prior stage outputs into Templates/Checklist.md; only a pass allows Publishing Agent to proceed, Covered-case memory (added 2026-07-21): Cases/covered_cases.json injected as 'covered_cases' input on every discovery run; never propose a case already on that list — added after the pipeline independently re-picked the already-in-production Banfield case, Discovery sources (added 2026-07-19), distinct from the fixed citation-source list: DOJ/USAO/state AG press-release feeds and forums (r/TrueCrime, r/UnresolvedMysteries, Websleuths) are valid for finding candidates, though anything found still needs the full citation-source verification pass, Research Agent — given a case query, gathers raw factual material from priority sources and produces a structured case brief, never a finished script, Trend tracking integration (broadened 2026-07-26): Research Agent must read Documentation/TREND_LOG.md before starting a new discovery run (avoid re-searching recently logged findings) and append any new finding after the run, in TREND_LOG.md's documented format, Full agent pipeline: Research -> Fact Verification -> Story -> Scene Planner -> Voice/Image -> Video Assembly -> Shorts/Thumbnail/SEO -> Quality Control -> Publishing (human-gated), Shorts Agent requirement (2026-07-19): new shorts_agent.md runs immediately after Video Assembly Agent, hard 45s cap per Short, one hook under 3 seconds, fixed karaoke caption style (+2 more)

### Community 16 - "Mandatory Real-Photo QC Check"
Cohesion: 0.25
Nodes (9): New QC check (added 2026-07-26, mandatory): case must have PersonPhotos.md documenting a real attempt at both mugshot_fetch_tool tracks. Zero real photos with no documented access-wall reason is a fail, not a warning — concrete evidence the video isn't YouTube's targeted 'AI slop'. Also confirms every identifiable real photo has eyes-blacked/blurred redaction applied., New QC check: synthetic-content disclosure reminder — flags for Publishing Agent that YouTube Studio's 'Altered or synthetic content' toggle needs a human decision at upload time for videos with realistic AI-generated scenes; QC agent cannot set it itself, only ensures it isn't forgotten, Real-photo sourcing decision (2026-07-19): mugshot_fetch_tool unblocked via the 'newsworthy' exception to right-of-publicity claims, two-track policy (person photos mandatorily redacted; non-person photos any source) — originally a preference to 'mix in real photos, don't ship 100% AI-generated', Real photos now MANDATORY per case, not optional mixing (escalated 2026-07-26). Rationale: YouTube's January 2026 enforcement wave specifically targets 'AI slop' (mass-produced, template-based AI content judged to add no original insight) under a three-strike system (warning -> 90-day Partner Program suspension -> permanent removal). Real, downloaded crime-scene/court photos are concrete evidence this studio is not template AI slop. Also requires checking YouTube Studio's 'Altered or synthetic content' disclosure toggle before every publish (confirmed 2026-07-26) — added to quality_control_agent.md / publishing_agent.md's pre-publish checklist., Escalated 2026-07-26 from 'recommended mixing' to 'mandatory attempt, every case, no exceptions.' Rationale: see ARCHITECTURE.md's 'Real photos are now MANDATORY per case' section (YouTube's 2026 AI-slop enforcement policy). Every new case must run both tracks before Image Generation fills gaps; genuinely blocked access must be a documented, checked outcome in PersonPhotos.md (per the Monica Sementilli standard), never silently skipped as the Kouri Richins production did., mugshot_fetch_tool — fetches real photos for a case to mix with Image Generation Agent's AI-generated stills, not to replace them; two tracks (person photos vs non-person photos) with different legal-risk rules, Redaction automated (confirmed 2026-07-20): OpenCV Haar cascades (frontalface then eye-detection restricted to upper 60% of face box) draw a black bar over both eyes in under a second, no external model/GPU needed; fallback to fixed proportional estimate if eye detection fails, Track 1 — person photos (mugshots, booking photos, court exhibits): official public-record sources only (sheriff/jail booking pages, state DOC inmate-lookup, court/prosecutor exhibits), mandatory eyes-blacked redaction, outlet-attribution exception for explicitly officially-credited republished mugshots (+1 more)

### Community 17 - "Channel Trailer Real-Photo Reuse"
Cohesion: 0.22
Nodes (9): Banfield case (previously produced video; source of the real redacted mugshot reused in the trailer under the newsworthy-exception analysis), Fatal Affairs Channel Trailer (~60s movie-trailer-style channel preview, replaces unbranded preview; rendered 2026-07-25 at 30.1s/903 frames, awaiting channel owner review before manual upload), Config/config.schema.json (source of channel name, slogan, colors, fonts used in trailer), Fatal Affairs (channel name, slogan "Every Affair Has a Story. Some End in Murder."), fal.ai Flux schnell image-generation pipeline (used for the two freshly-generated generic trailer images, corkboard.png and crimetape_rain.png, chosen over third-party stock/footage specifically to avoid a new ungoverned rights question for a channel-level asset), Kouri Richins fentanyl-murder case (already-produced video whose stills are reused as trailer collage images, cleared rights), Monica Sementilli hairdresser-murder case (already-produced video whose stills are reused as trailer collage images, cleared rights), Assets/renders/fatal-affairs-channel-trailer.mp4 (gitignored render, 1920x1080, 903 frames @ 30fps, 30.1s, spot-checked cold open/mugshot beat/logo-CTA sequence) (+1 more)

### Community 18 - "Voice & Music Tool Notes"
Cohesion: 0.22
Nodes (9): Background music — Stage 2 live-test attempt (2026-07-19), Default provider notes (ElevenLabs, verify against current docs before building), Gap closure (2026-07-19) — concrete fix for the two shape mismatches above, Implementation notes, Interface, Purpose, Real-timestamp captioning — fixed endpoint choice (2026-07-21), Stage 1/2 live-test result (2026-07-19) (+1 more)

### Community 19 - "Image Generation Tool Notes"
Cohesion: 0.25
Nodes (8): Default provider: fal.ai + Flux, Fallback / secondary providers (keep the interface provider-agnostic), Implementation notes, Interface, Purpose, Stage 2 live-test result (2026-07-19), Stage 4 live-test result (2026-07-20/21) — confirmed working through n8n, not just direct Python, Tool: image_gen_tool

### Community 20 - "Test Plan Stages"
Cohesion: 0.29
Nodes (7): Regression check, Stage 1 — Agents in isolation, Stage 2 — Tools in isolation, Stage 3 — Two-node links, Stage 4 — Full chain, one real case, dry-run publish, Stage 5 — First real publish, Test Plan

### Community 21 - "n8n Workflow Builder"
Cohesion: 0.29
Nodes (3): Build the Fatal Affairs master pipeline workflow for n8n (local Phase 2 trial)., JS expr: concatenated text blocks of an Anthropic node's response., txt()

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
- **152 isolated node(s):** `$schema`, `title`, `type`, `type`, `const` (+147 more)
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
- **Why does `Brendan Banfield Case PublishPlan` connect `Channel Footer Rule` to `Visual Style & Brand Identity`, `Config Schema Properties A`?**
  _High betweenness centrality (0.165) - this node is a cross-community bridge._