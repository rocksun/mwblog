The major [static application security testing (SAST)](https://thenewstack.io/why-you-still-need-dynamic-application-security-testing/) vendors are now wrapping a [large language model](https://thenewstack.io/llm/) around their legacy scanning engines and calling it next-generation.

The question to ask is whether any of them is actually different, or whether the industry has simply rebranded the same noise problem with an AI label.

[Checkmarx](https://checkmarx.com/) made a strong move this week, unveiling a new SAST engine that combines a deterministic rules-based scanner, an LLM trained on security data, and a third engine purpose-built to classify findings as true or false positives before they reach a development team.

The company claims an F1 score of 0.499 against a category average of 0.20, and says the engine found 327 true positives missed by a leading frontier model in head-to-head testing across four production codebases — though it declined to name which frontier model it tested against. An F1 score is a performance metric used to evaluate automated detection models.

“Three engines run together to deliver unified protection: our deterministic rules foundation enterprises have relied on for two decades, AI-powered coverage for every language developers and AI coding assistants write today, and the Findings Analysis Engine (FAE) that classifies true and false positives before a single result reaches your team,” [Jonathan Rende](https://www.linkedin.com/in/frank-emery-b835523b/), Chief Product Officer at Checkmarx, says in a statement.

## Orchestration as the actual product

The architecture seems less novel than the company suggests. Checkmarx’s LLM is not purpose-built; it starts from foundational models fine-tuned with proprietary security data. What Checkmarx is pushing is the orchestration layer. That is, the idea that the three engines run together automatically, without customers having to assemble their own multi-engine workflows.

“Neither of these solutions is good enough on its own,” [Frank Emery](https://www.linkedin.com/in/frank-emery-b835523b/), Director of Product Management at Checkmarx, tells *The New Stack*, referring to the split between traditional query-based scanners and purely LLM-based tools. “Our approach leverages both [deterministic](https://thenewstack.io/how-etcd-solved-its-knowledge-drain-with-deterministic-testing/) and [non-deterministic](https://thenewstack.io/martin-fowler-on-preparing-for-ais-nondeterministic-computing/) LLM-based engines, so end users have a high degree of configurability and determinism, but they’re also able to support languages very rapidly and cover more of their codebases.”

## A category converging on the same answer

Legacy query-based tools are deterministic and auditable but slow to support new languages and prone to generating false positives that pull engineers off productive work. Purely LLM-based scanners handle any language immediately but produce non-deterministic results, making compliance and governance difficult. It seems like every incumbent is now pushing some version of both.

What distinguishes approaches is where the integration happens and who manages it. Checkmarx’s argument is that hiding the complexity behind a single scan trigger is the actual product. Users get determinism where they need it, language coverage where legacy tools fall short, and a noise filter, which is their FAE, which suppresses false positives before they surface, Emery notes.

## The noise problem gets worse

The noise argument is the strongest. AI coding tools have driven code volume sharply higher, with Emery estimating that customers are committing one to one-and-a-half times as much code as they did a few years ago. False-positive triage, which is already a drag on AppSec teams, scales poorly at that volume.

“If you run a scan and get 10 findings, a handful could be false positives, but to find that out, you have to manually assess each one, and that pulls developers or security professionals out of their flow,” Emery says. “As development pace increases and backlogs grow, that kind of noise is becoming much worse for teams to handle.”

In a statement, Checkmarx CEO [Sandeep Johri](https://www.linkedin.com/in/sandeepjohri/) put this sentiment more bluntly: “Our research found that 75% of code shipped today is vulnerable, because the speed at which AI creates code has far outpaced the speed needed to keep it safe.”

## Attackability as the new prioritization metric

Underneath the new engine is a prioritization concept Checkmarx calls “Attackability,” an exploitability score that traces the attack path from the source, evaluating sanitizers, vector accessibility, and business relevance. The idea is to shift AppSec reporting away from raw vulnerability counts toward what really needs fixing, giving security teams a defensible metric for board-level conversations, Emery says.

Whether Checkmarx’s orchestration-first argument holds up against competitors making similar claims will depend on what enterprise buyers find when they run it against their own codebases.

Checkmarx SAST and the Finding Analysis Engine are available now on the Checkmarx One platform. Existing subscribers are upgraded automatically.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)