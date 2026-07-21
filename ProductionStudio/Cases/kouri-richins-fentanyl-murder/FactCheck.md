```json
{
  "verified_claims": [
    { "claim": "Eric Richins, 39, died March 4, 2022 at the family home outside Park City, Utah, from a fentanyl overdose roughly five times a lethal dose, delivered in a Moscow Mule cocktail.", "source_url": "https://abcnews.com/US/closing-arguments-murder-trial-kouri-richins-utah-mom/story?id=131117904" },
    { "claim": "A first poisoning attempt, via a fentanyl-laced sandwich, occurred approximately 17 days earlier, around Valentine's Day 2022.", "source_url": "https://www.cbsnews.com/news/kouri-richins-sentenced-husbands-murder-fentanyl-laced-cocktail-murder/" },
    { "claim": "Kouri Richins was convicted March 16, 2026 on all five counts: first-degree aggravated murder, attempted aggravated murder, two counts of insurance fraud, and forgery.", "source_url": "https://abcnews.com/US/closing-arguments-murder-trial-kouri-richins-utah-mom/story?id=131117904" },
    { "claim": "She was sentenced May 13, 2026 (Eric's birthday) to life without parole, plus consecutive terms of 5 years to life for attempted murder, 1-15 years on each insurance-fraud count, and up to 5 years for forgery. Judge Richard Mrazik stated she was 'simply too dangerous to ever be free.'", "source_url": "https://www.cbsnews.com/news/kouri-richins-sentenced-husbands-murder-fentanyl-laced-cocktail-murder/" },
    { "claim": "Prosecutors' theory of motive: roughly $1.8 million in real estate debt, over $2 million in life-insurance policies on Eric (one obtained via a forged signature), and a relationship with boyfriend Robert Josh Grossman that began in early 2020.", "source_url": "https://www.biography.com/crime/a70499053/who-is-kouri-richins-case-and-murder-trial" },
    { "claim": "A text from Richins to her boyfriend read: 'If he could just go away and you could just be here! Life would be so perfect!!' Grossman testified about their relationship at trial on March 4, 2026.", "source_url": "https://abcnews.com/US/closing-arguments-murder-trial-kouri-richins-utah-mom/story?id=131117904" },
    { "claim": "Former housekeeper Carmen Lauber testified Richins asked her four times to obtain stronger drugs, at one point requesting what she called 'the Michael Jackson stuff.'", "source_url": "https://www.biography.com/crime/a70499053/who-is-kouri-richins-case-and-murder-trial" },
    { "claim": "Richins self-published a children's grief book, 'Are You With Me?', in March 2023 and promoted it on local media before her arrest in May 2023.", "source_url": "https://www.cbsnews.com/news/kouri-richins-sentenced-husbands-murder-fentanyl-laced-cocktail-murder/" },
    { "claim": "Eric and Kouri had three sons, ages 9, 7, and 5 at the time of his death; their victim-impact statements, read by counselors at sentencing, asked for the harshest possible sentence.", "source_url": "https://www.biography.com/crime/a70499053/who-is-kouri-richins-case-and-murder-trial" },
    { "claim": "Eric's sister Katie Richins-Benson said Eric believed Richins was 'evil'; another sister, Amy, said: 'Just very happy that we got justice for my brother.'", "source_url": "https://www.cbsnews.com/news/kouri-richins-sentenced-husbands-murder-fentanyl-laced-cocktail-murder/" },
    { "claim": "At sentencing, Richins maintained her innocence, stating 'God did not put me in this world to take a life,' and was granted a 28-day extension to file an appeal.", "source_url": "https://www.cbsnews.com/news/kouri-richins-sentenced-husbands-murder-fentanyl-laced-cocktail-murder/" }
  ],
  "flagged_claims": [
    { "claim": "That Richins 'killed almost all of' Eric's animals and attempted to poison one of their sons with fentanyl, causing a seizure.", "reason": "single-source only, and reported specifically as a claim within the sons' victim-impact statements at sentencing (read by counselors), not as an independently charged or adjudicated fact. Richins was never charged with harming a child. Usable ONLY as an attributed family allegation ('the sons' statements alleged...'), never as narrated fact." }
  ],
  "confidence_score": 0.85,
  "sources_used_per_scene": {
    "note": "Scene-level mapping not yet applicable - Scene Planner has not run yet this pass. All claims above trace to Sources.md, which lists 3 directly-fetched primary outlets (ABC News, Biography.com, CBS News) plus 2 corroborating outlets found via search (CNN, NewsNation) - 5 independent sources, clearing the minimum."
  }
}
```

**Escalation check (per `Agents/fact_verification_agent.md`):** no flagged claim here is load-bearing for the hook or twist — the twist (children's-book author convicted of poisoning her husband for insurance/an affair, after a first failed attempt) stands entirely on the verified claims above. The flagged child-poisoning allegation is dramatic but not necessary to the story's spine, so it is dropped from the script rather than escalated as a blocker — consistent with the spec's "never invent or smooth over" rule, applied here as "never assert an unadjudicated allegation as fact."
