```json
{
  "release_plan": [],
  "awaiting_human_confirmation": true,
  "blocking_issues": [
    {
      "area": "checklist_status",
      "detail": "checklist_status is 'warning' (not 'pass'). Publishing is gated; no release plan is produced until this clears to 'pass'."
    },
    {
      "area": "fact_consistency / victim identity",
      "detail": "HUMAN DECISION REQUIRED: Load-bearing victim identities (wife 'Christine Banfield', second victim 'Joseph Ryan') are Wikipedia-only and are correctly NOT asserted in any final text. A human must either (a) confirm identities from the Commonwealth's Attorney release / court filings, or (b) approve running with the second victim unnamed, before publish."
    },
    {
      "area": "legal_review",
      "detail": "LEGAL/STYLE SIGN-OFF RECOMMENDED: Content depicts and names real, living people (a convicted person and a testifying witness, Juliana Peres Magalhães). Anonymized reenactment framing is used with no real-person likeness. Human confirmation of this approach is recommended before image generation."
    },
    {
      "area": "missing_assets",
      "detail": "PENDING: 7 chapter audio MP3s and 70 scene images are produced out-of-band; existence, format, and quality unverified. Must be confirmed before publish."
    },
    {
      "area": "export_integrity",
      "detail": "PENDING: Final Remotion render file existence, playability, and 16:9 MP4 format cannot be confirmed this run. Must be verified before publish."
    },
    {
      "area": "voice_timing",
      "detail": "PENDING: No assembly report this run. SEO chapter timestamps are self-declared estimates (~12.5 min planned) and must be re-checked against final edit runtime before publish."
    }
  ],
  "prepared_package_reference": {
    "final_video": "Assets/renders/final.mp4",
    "seo": "SEO.md",
    "thumbnail": "Thumbnail.md",
    "shorts_count": 5,
    "note": "Package assembled but NOT cleared. Intended release pacing (for reference once cleared): main video + strongest short on release day, remaining 4 shorts one per day thereafter — never all 5 on day one. No release_plan dates issued while status != pass."
  },
  "escalations": [
    "PUBLISH BLOCKED — checklist_status='warning', not 'pass'. This agent prepares only and never presses publish; per hard rule, publishing always requires explicit human confirmation regardless.",
    "HUMAN DECISION REQUIRED (blocks pass): Confirm victim identities from Commonwealth's Attorney release / court filings, OR approve running with the second victim unnamed. All downstream text currently avoids asserting Wikipedia-only names — do not add names without human confirmation.",
    "LEGAL/STYLE SIGN-OFF RECOMMENDED: Confirm anonymized-reenactment approach is acceptable for content naming real, living people before image generation.",
    "OUT-OF-BAND VERIFICATION REQUIRED: Confirm rendered audio (7 MP3s), scene images (70), final 16:9 MP4 export integrity/playability, and actual runtime vs SEO chapter timestamps before any publish action.",
    "SHORTS NOTE: short_5 depends on the unverified second-victim fact. It keeps the victim unnamed and acknowledges the gap (publishable as-is), but if human review downgrades it, ship 4 shorts rather than substituting a weaker moment.",
    "NEXT STEP: Once victim-identity decision is resolved and asset/export/timing checks pass, re-run for a clean 'pass' and dated release_plan. This agent does not override a warning into a pass."
  ]
}
```