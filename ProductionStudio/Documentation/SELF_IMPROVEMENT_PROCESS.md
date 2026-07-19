# Self-Improvement Process

The brief asks for a studio that "gets better after every project." Since none of the agents
here have persistent memory (they're stateless API calls — see `ARCHITECTURE.md`), the learning
loop has to be file-based, not magical. Concretely:

## After every finished video

1. **Quality Control Agent** produces `Templates/Checklist.md` for the finished project —
   what passed, what needed a fix, what got flagged.

2. **Tool Manager Agent** checks `Tools/tool_registry.json`: which tools were used, which
   failed or needed a manual override, whether any tool should be merged/retired.

3. **A retro step** (run by the Story/SEO agents, or a human, reading the finished project's
   real performance data once it's live) appends structured notes to
   `Templates/SuccessRules.md`:
   - which case topic/angle performed
   - which hook/first-30-seconds approach got retention
   - which title (of the 3 generated) got used / got clicked
   - which thumbnail concept worked
   - which recurring errors showed up in QC across projects
   - which words/phrases keep appearing in high performers

4. **`SuccessRules.md` gets re-injected** as part of the input to the Story Agent and SEO Agent
   on the *next* project — that's the entire "self-improvement" mechanism. It's a growing,
   human-readable file, not a black-box model update.

## Why this is intentionally simple

A more elaborate "the AI watches itself and rewires its own prompts" design would be harder to
debug and easier to quietly go wrong. A flat file that a human can read, edit, or roll back is
safer for a one-person media business, and it's exactly as automatable — n8n just needs to read
`SuccessRules.md` into the relevant prompts, which is a file-read node, not a research project.

## Cadence

Realistically: do this retro after each of the first 10 videos (the test-the-hypothesis phase
already planned in `fatal-affairs-project-brief.md`), not after every single short. Once
patterns stabilize, monthly is probably enough.
