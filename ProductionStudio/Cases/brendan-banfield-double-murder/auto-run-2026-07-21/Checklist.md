```json
{
  "checklist_status": "warning",
  "issues": [
    {
      "area": "story_consistency",
      "severity": "warning",
      "detail": "PASS — the twist (au pair testifies to her own guilt / husband admits affair but denies murder) follows logically from the setup, and the reveal (guilty double murder, life sentence) is earned. No inconsistency. Listed for completeness, not blocking."
    },
    {
      "area": "timeline_consistency",
      "severity": "warning",
      "detail": "PASS — Feb 2023 killings, Jan 2026 trial/testimony, Feb 2 2026 verdict, June 5 2026 sentencing are consistent across Script, scene list, Voiceover, SEO, and match verified facts. Listed for completeness, not blocking."
    },
    {
      "area": "fact_consistency",
      "severity": "warning",
      "detail": "Load-bearing unverified facts (wife 'Christine Banfield', second victim 'Joseph Ryan') are Wikipedia-only and are correctly NOT asserted anywhere in Script, Voiceover, SEO, Shorts, or image prompts — victims are referred to only as 'his wife' and 'a second victim,' and UNKNOWN items (second victim's presence mechanism, au pair's legal status, formal motive, forensic evidence) are explicitly named as gaps rather than smoothed over. Text side is clean. HOWEVER this remains a mandatory HUMAN DECISION before publish (confirm identities from Commonwealth's Attorney release / court filings, OR approve running with the second victim unnamed). See escalations."
    },
    {
      "area": "scene_consistency",
      "severity": "warning",
      "detail": "All 70 scenes (0001-0070) have a matching image prompt AND are covered by the 7 chapter voiceover chunks (CH01=0001-0013, CH02=0014-0027, CH03=0028-0036, CH04=0037-0045, CH05=0046-0053, CH06=0054-0060, CH07=0061-0070). Text-side scene coverage is complete; actual rendered audio/image files are PENDING (see missing_assets)."
    },
    {
      "area": "voice_timing",
      "severity": "warning",
      "detail": "PENDING — no assembly report provided this run (render is out-of-band). Sum of scene estimated_seconds ≈ 12.5 min planned duration; actual render duration and voice/subtitle sync cannot be verified. SEO chapter timestamps are self-declared estimates and must be re-checked against the final edit runtime before publish."
    },
    {
      "area": "missing_assets",
      "severity": "warning",
      "detail": "PENDING per run limitation — 7 chapter audio MP3s and 70 scene images are produced out-of-band locally; their existence/format/quality cannot be confirmed at this stage. Must be verified before publish."
    },
    {
      "area": "grammar_readability",
      "severity": "warning",
      "detail": "PASS — Script, Voiceover, SEO, Shorts, and thumbnail copy are clean, readable, and consistent in voice. No grammar/spelling issues detected. Listed for completeness, not blocking."
    },
    {
      "area": "export_integrity",
      "severity": "warning",
      "detail": "PENDING per run limitation — final Remotion render file existence, playability, and correct format (16:9 MP4) cannot be checked in-band this run. Must be verified before publish."
    },
    {
      "area": "legal_review",
      "severity": "warning",
      "detail": "Case involves real, named, living people (a convicted individual, Brendan Banfield, and a testifying witness, Juliana Peres Magalhães). Image prompts and thumbnail deliberately use anonymized/obscured-face reenactment framing and name no real person likeness. Recommend a HUMAN legal/style sign-off confirming the anonymized-reenactment approach before image generation. See escalations."
    },
    {
      "area": "retention",
      "severity": "warning",
      "detail": "Non-blocking editorial note — recurring 'we can't confirm this' honesty beats (scenes 0018-0019, 0034-0036, 0062-0063) function as gaps rather than forward momentum and may soften pacing; Short_5 (scene 0018) is a 13s reflective beat that risks stalling on a sound-off Short. Optional tightening / on-screen text staging recommended, not required."
    }
  ],
  "qc_questions": {
    "stop_scrolling": true,
    "would_click": true,
    "hook_can_improve": false,
    "retention_can_improve": true
  },
  "escalations": [
    "HUMAN DECISION REQUIRED BEFORE PUBLISH (blocks 'pass'): The load-bearing victim identities (wife 'Christine Banfield' and second victim 'Joseph Ryan') are sourced ONLY to Wikipedia — restricted to timeline-verification and not a valid assertion source. All downstream text correctly avoids asserting these names and honestly flags the second victim's presence mechanism, the au pair's legal status, the formal motive, and forensic evidence as UNKNOWN. A human must either (a) confirm the victim identities from the Commonwealth's Attorney release / court filings, or (b) approve running with the second victim unnamed, before this project is cleared for publish.",
    "LEGAL/STYLE SIGN-OFF RECOMMENDED: Content depicts and names real, living people (a convicted person and a testifying witness). Image prompts/thumbnail use anonymized reenactment framing with no real-person likeness. Recommend human confirmation that this approach is acceptable before image generation.",
    "STATUS RATIONALE: checklist_status is 'warning' (NOT 'pass'), so the Publishing Agent is gated and must not proceed. It is not 'fail' because no text-side consistency/grammar/story/timeline check actually failed and no flagged/unknown claim is asserted in the final output; the outstanding items are (1) PENDING out-of-band asset/export/timing verification per this run's stated limitation, and (2) mandatory human decisions on victim identity and legal review. If a human resolves the victim-identity decision and asset/export/timing checks are confirmed, this can be re-run for a clean 'pass'. Per spec, this agent never overrides a fail into a pass — no fail condition was met here; publish remains blocked pending the human decisions above."
  ]
}
```