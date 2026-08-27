Security teams are discovering that the most capable AI models cost too much to run on routine, high-volume work, and they’re finding that out after the first invoice arrives. I lead a security operations team, and I’ve brought detection costs down to roughly $1 per day for trust and safety work.

That number surprises people, because enterprise AI is supposed to be expensive. It isn’t, if you design the work correctly. The teams burning through budget are skipping the design work that determines which cases should reach a model at all.

## The funnel is the cost lever

Detection funneling isn’t new. Before LLMs, security teams built layered filters to narrow high-volume event streams down to the cases worth a human analyst’s time. The same logic applies to AI spend. The narrower and more precise the funnel feeding your models, the lower your cost per accurate outcome.

> “The narrower and more precise the funnel feeding your models, the lower your cost per accurate outcome.”

In trust and safety, most abuse is identifiable before any model runs. Deterministic, rules-based pattern detection captures a significant portion of volume upfront. Account age, email provider, and behavioral signals all feed automated filters that resolve the obvious cases and narrow what remains. Only the subset that clears those filters reaches an LLM. That’s where the dollar-a-day figure comes from. A well-designed funnel keeps expensive work to a minimum.

Think of it like a home security system. You don’t need a camera monitoring everyone who walks past your house. You care once someone’s actually inside, and that’s when you bring in the higher capability response.

## Tiered models, tiered cost

For cases that clear the initial funnel, a lightweight model handles the first pass. The output is structured — a determination of malicious or benign at high or low confidence. High-confidence outcomes resolve automatically, while low-confidence cases escalate to a more capable model with broader context and stronger reasoning.

Only a fraction of events reach that second tier. We ran structured efficacy testing across model options and found only a 1-2% difference in accuracy between lightweight and frontier models for our use cases. [Frontier models cost](https://thenewstack.io/googles-new-gemini-3-flash-rivals-frontier-models-at-a-fraction-of-the-cost/) roughly five times more per token. That math only works if the cases reaching them need that capability.

Prompt engineering matters as much as model selection. One prompt I wrote for agentic detections runs over 1,900 words, covering every scenario the agent is likely to encounter, including when to escalate and when to act autonomously. Not every case needs that depth. Some trust and safety prompts are two or three sentences, but the scope of what you’re asking an agent to handle determines the precision the prompt requires.

> “Frontier models cost roughly five times more per token. That math only works if the cases reaching them need that capability.”

Context is what separates accurate AI analysis from hallucination. Give a model an abuse report and ask whether the user is abusive, and it may take the report at face value. Give it the actual artifact being reported, along with the report, and it can independently assess whether the claim holds up.

## Where humans still belong

Automation handles the clear cases. It’s the ambiguous ones that [need judgment](https://thenewstack.io/human-purpose-ai-agents/) that agents don’t yet have.

Distinguishing a legitimate security researcher who hosts malware samples for analysis from a malicious actor who hosts the same content to target others requires discernment that AI still struggles with. So does a dispute in an issue thread where the terms of service could be interpreted differently. These cases reach a human because the question itself requires contextual reasoning the current generation of agents  [can’t reliably provide](https://thenewstack.io/4-reasons-agentic-ai-is-failing/).

> “Automation handles the clear cases. It’s the ambiguous ones that need judgment that agents don’t yet have.”

The goal is to give human reviewers the time to spend on the cases that actually need them. Instead of clicking through individual events, engineers on my team are building systems, writing prompts, and defining patterns that orchestrate detection at scale.

## What this means in practice

Attackers try new obfuscation techniques, and we adapt prompts and models to catch them. It’s iterative work, closer in spirit to detection engineering than a one-time deployment. Prompt engineering is just another form of that: write the rule, test the output, tune when accuracy slips.

The cost question is solvable if you treat it as a design problem from the start. How much reaches a model, in what form, and with what context determines the bill. Most teams that find AI expensive haven’t made those decisions deliberately.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/08/1f416266-matt-coons.png)

Matt Coons is a senior manager of security operations at GitLab.

Read more from Matt Coons](https://thenewstack.io/author/matt-coons/)