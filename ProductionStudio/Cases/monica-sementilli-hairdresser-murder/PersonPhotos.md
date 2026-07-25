# Person Photos — Monica Sementilli hairdresser murder (Track 1 attempt, mugshot_fetch_tool)

## Status: blocked, not skipped — escalating per `Tools/mugshot_fetch_tool.md`'s own rule

A real, documented attempt was made to find official-source person photos for Monica
Sementilli, Robert Baker, and Christopher Austin before defaulting to generation — this was not
silently skipped the way the Kouri Richins production skipped it.

## What was found
- **LAPD's own press release** on the arrests (`lapdonline.org/newsroom/suspects-arrested-for-homicide-in-woodland-hills-nr17184aj/`)
  is very likely to carry official booking photos released by the investigating agency itself —
  the strongest possible Track 1 source. **Blocked: returns HTTP 403 to automated fetch.**
- **CDCR's inmate locator** (`inmatelocator.cdcr.ca.gov`) would have Monica Sementilli's current
  post-sentencing photo (she is incarcerated at Central California Women's Facility, Chowchilla)
  — Track 1 priority #2 per the tool spec. **Blocked: it's an interactive search form, not a
  fetchable static page** — needs a human to run the search manually in a browser.
- **People magazine's coverage is reported (via web search) to include a Monica Sementilli
  mugshot**, but no direct, fetchable article URL/image URL could be confirmed within this
  session's search results.
- **ABC7's own sentencing-day photo** (`cdn.abcotvs.com/dip/images/16828288_062325-kabc-woodland-hills-sentencing-img.jpg`,
  captioned as ABC7's own photography from the 2025-06-23 sentencing) was identified as a
  possible Track 2 (non-person / not clearly identifying) candidate, but **could not be
  downloaded — this sandbox's Bash tool denies outbound `curl` to arbitrary CDN hosts**, unlike
  the allowlisted fal.ai/ElevenLabs endpoints `generate_case_assets.py` already uses. Never
  visually confirmed, so never used.
- **CBS 48 Hours' own photos** of Baker and Monica together at Fabio's wake exist
  (`assets2.cbsnewsstatic.com/.../baker-monica.jpg`, credited to "48 Hours") but these are the
  outlet's own private-event photography, not an official-source booking photo — would need a
  fresh legal read before treating as Track 1, and wasn't pursued further given the session's
  time budget on this one sub-step.

## Decision
None of the above cleared the bar (official source + successfully downloaded + visually
verified) within this session. Per `Tools/mugshot_fetch_tool.md`'s escalation rule ("No
public-record person-photo exists for a subject who is nonetheless central to the story... a
content decision, not a tool decision"), this case proceeds with **AI-generated
silhouette/reenactment imagery only** for Monica Sementilli, Robert Baker, and Christopher
Austin — `ImagePrompts.md` was deliberately written to use backlit silhouettes, hands-only shots,
and shadow compositions for these three rather than attempting face-forward "portrait" generation
of a real person.

## Open item for the channel owner
If you want a real photo for this case specifically, the two live leads are:
1. Run a manual search on `inmatelocator.cdcr.ca.gov` for "Sementilli" — should return her
   current CDCR photo directly in a browser (no automation blocker for a human).
2. Open `https://www.lapdonline.org/newsroom/suspects-arrested-for-homicide-in-woodland-hills-nr17184aj/`
   directly in a browser — it 403'd only to the automated fetch tool, may load fine for you.

If either turns up a usable image, send it over and the OpenCV eye-redaction step (same one used
for the Banfield mugshot) can be applied and swapped in before the render.
