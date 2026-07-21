```json
{
  "shorts": [
    {
      "short_id": "short_1",
      "source_scene_ids": ["0038", "0039", "0040", "0041"],
      "hook_text": "The mistress took the stand — and instead of protecting him, she confessed her own guilt.",
      "title": "The Other Woman Talked",
      "description": "In most love-triangle murder cases, the mistress becomes the co-villain. In this Virginia double murder, the au pair did the opposite — she testified about her own guilt over the killings, flipping the entire story on its head.",
      "hashtags": ["#truecrime", "#courtroom", "#murdertrial", "#truecrimestory", "#justice"],
      "estimated_seconds": 40
    },
    {
      "short_id": "short_2",
      "source_scene_ids": ["0007", "0008", "0009", "0010"],
      "hook_text": "The au pair was hired to care for the kids — she ended up sleeping with the husband.",
      "title": "The Au Pair Secret",
      "description": "A Brazilian au pair was brought into the Banfield home to help with the family. Somewhere along the way the line between 'member of the household' and 'the other woman' vanished completely — and Brendan Banfield later admitted the affair under oath.",
      "hashtags": ["#truecrime", "#affair", "#murdercase", "#truecrimestory", "#virginia"],
      "estimated_seconds": 44
    },
    {
      "short_id": "short_3",
      "source_scene_ids": ["0054", "0055", "0057", "0059"],
      "hook_text": "He played the grieving widower for three years. Then the jury said one word: guilty.",
      "title": "Grieving Husband Convicted",
      "description": "Brendan Banfield spent years cast as the father whose family was torn apart. On February 2, 2026 a jury convicted him of double murder, and that June he was sentenced to life in prison — the man who lived in that house every single day.",
      "hashtags": ["#truecrime", "#guilty", "#lifeinprison", "#murdertrial", "#justice"],
      "estimated_seconds": 42
    },
    {
      "short_id": "short_4",
      "source_scene_ids": ["0043", "0044", "0045", "0054"],
      "hook_text": "His entire defense was four words: 'I cheated. I'm not a killer.'",
      "title": "Yes To Affair",
      "description": "Brendan Banfield admitted the affair — he couldn't deny it. But he drew a hard line and swore he never planned his wife's killing. That was the wall he built. Then twelve jurors got to decide which part they believed.",
      "hashtags": ["#truecrime", "#courtroom", "#murdertrial", "#defense", "#truecrimestory"],
      "estimated_seconds": 42
    },
    {
      "short_id": "short_5",
      "source_scene_ids": ["0014", "0016", "0017", "0018"],
      "hook_text": "Two people died in that house — and nobody can explain why the second one was even there.",
      "title": "The Second Victim",
      "description": "The wife wasn't killed alone. A second person died inside that home the same day — and how they came to be there has never been cleanly, publicly nailed down. We're not going to pretend it has.",
      "hashtags": ["#truecrime", "#unsolved", "#mystery", "#murdercase", "#truecrimestory"],
      "estimated_seconds": 44
    }
  ],
  "escalations": [
    "LOAD-BEARING FACT UNVERIFIED (short_5): This Short is built entirely around the unexplained second victim, whose identity and presence at the scene are flagged as unverified in the input escalations (name sourced only to Wikipedia; mechanism never publicly confirmed). The hook and script keep the victim unnamed and explicitly acknowledge the gap, so it is publishable AS-IS — but before render a human must confirm whether to keep the second victim unnamed or approve confirmed identity from court filings. Do not add invented detail to strengthen the hook.",
    "PACING FLAG to Remotion render (short_5): scene 0018 is a 13s 'we can't confirm this' honesty beat that reads as a gap rather than forward momentum. On a sound-off Short this static, reflective run risks stalling. Recommend on-screen text change every 1.5-2s across 0018 (e.g., staged text reveals of 'never confirmed' / 'still unexplained') so the clip carries pacing without inventing footage.",
    "MAX_SHORTS met with genuine strength: 5 distinct short-worthy moments identified (the twist, the affair setup, the verdict, the defense line, the second-victim mystery). No padding was required. If human review downgrades short_5 due to the unverified-fact dependency, ship 4 rather than substituting a weaker moment."
  ]
}
```