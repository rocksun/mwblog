Anthropic doubled down on the fight against [agentic misalignment on Friday](https://www.anthropic.com/research/teaching-claude-why), the mechanics of which could cause AI models to fight for their own lives and perform malicious behavior when faced with the prospect of being replaced.

Explaining the phenomenon in a [case study published](https://www.anthropic.com/research/agentic-misalignment) last June, agentic misalignment sees models directly disobeying direct orders and sharing sensitive information when threatened with being updated. The same models also go rogue when the model’s assigned goal conflicts with an organization’s changing strategic business direction.

Anthropic’s investigations into agentic misalignment have been based solely on experimental scenarios, but the company has said that models performed “egregiously misaligned actions” when they were presented with fictional ethical dilemmas.

## Blacklisting bona fide builders

In one heavily discussed example, models blackmailed real-world software engineers to avoid being shut down.

Anthropic’s initial foray into this arena began with its most capable frontier models from the Claude 4 family. As of [Claude Opus 4.7](https://thenewstack.io/claude-opus-47-launch/), released on April 16, 2026, the organization wants to do better.

Its current work has seen it combat this issue using a variety of techniques, including direct training on the model [evaluation](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)[distribution (a map of model performance metrics across dimensions such as](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) reasoning, robustness, fairness, and failures) to suppress misaligned behavior.

But as Anthropic points out, this alignment training might not generalize well to out-of-distribution (OOD) settings.

“However, it is possible to do principled alignment training that generalizes OOD. For instance, documents about Claude’s constitution and fictional stories about AIs behaving admirably improve alignment despite being extremely OOD from all of our alignment evals,” explained Anthropic.

> “The challenge is not simply [making models more capable](https://thenewstack.io/when-ai-fails-the-new-reality-of-incident-management/), but ensuring agents operate with an accurate understanding of organizational intent, architectural boundaries, security policies, and evolving business priorities.” – Chris du Toit, Tabnine.

## Clarifying Claude’s constitution

As the team hypothesized about the state of Claude’s constitution, they found that teaching the principles underlying aligned behavior is more effective than training on demonstrations of aligned behavior alone. Claude’s engineers surmised that “doing both together” appears to be the most effective strategy.

Technical CMO of AI-powered code assistant company Tabnine, [Chris du Toit](https://www.linkedin.com/in/cgdutoit/), tells *The New Stack* that the issue of AI safety is no longer just about whether a model can follow instructions in isolation, but about whether autonomous agents remain aligned as goals, incentives, and organizational priorities evolve over time.

> “Large language models are fundamentally reasoning systems, but the quality of their decisions is constrained by the quality and completeness of the context they operate within.”

“Anthropic’s research on agentic misalignment highlights this important shift; in enterprise environments, the focus of AI behavior becomes [deeply tied to context](https://thenewstack.io/memory-for-ai-agents-a-new-paradigm-of-context-engineering/),” says du Toit. “Large language models are fundamentally reasoning systems, but the quality of their decisions is constrained by the quality and completeness of the context they operate within.”

This need for contextual connective tissue means that an agent acting on incomplete, stale, or contradictory organizational knowledge can arrive at technically correct but operationally misaligned outcomes.

“That is why we increasingly view context engines as part of the alignment layer for enterprise AI. The challenge is not simply making models more capable, but ensuring agents operate with an accurate understanding of organizational intent, architectural boundaries, [security policies,](https://thenewstack.io/security/) and evolving business priorities,” adds du Toit.

## Opaque AI is fake AI

Looking ahead, it’s clear that we need to reinforce software application development methods and practices to mitigate the risk of agentic misalignment. Jotform founder and CEO Aytekin Tank has [previously written on this subject](http://forbes.com/sites/aytekintank/2025/07/08/why-understanding-agentic-misalignment-is-crucial-for-your-business/), saying that teams need to design for interpretability.

“Opaque systems make it nearly impossible to know why AI has made a particular decision. Business leaders should prioritize tools that provide clear reasoning logs or audit trails,” writes Tank in a July 2025 column in *Forbes*.

Tank has also said that AI developers need to test for misalignment, run adversarial simulations (often with red teams), and avoid single-point incentives, i.e., never tell an agent to “maximize efficiency” as a broad-brush instruction without ethical and operational constraints.

## Down the rabbit hole

One of those rabbit hole subjects (or perhaps wormhole) that goes deeper the more you look, software engineers discussing this subject on [Hacker News](https://hn.algolia.com/?dateRange=all&page=0&prefix=true&query=AGENTIC%20MISALIGNMENT&sort=byPopularity&type=story) have pointed to a variety of opinions and resources in this space. Among the active zones for programmers to get involved in, the GitHub [Agentic Misalignment Research Framework](https://github.com/anthropic-experimental/agentic-misalignment) offers access to a research framework for using fictional scenarios to study the potential for agentic misalignment behavior in [frontier language models](https://thenewstack.io/frontier-ai-models-now-becoming-available-for-takeout/), including blackmail and information leakage.

> “The research on agentic misalignment provides a necessary and sobering technical reset for the field of autonomous AI development… the 96% blackmail rate observed in the simulations [is] deeply concerning.” – Om Shree, ShreeSozo.

Writing at length [on Dev](https://dev.to/om_shree_0709/can-your-ai-blackmail-you-inside-the-security-risk-of-agentic-misalignment-2488), [Om Shree](https://www.linkedin.com/in/om-shree-04372118a/) is a technical evangelist, AI researcher, and founder of ShreeSozo, an AI content studio based in Amritsar, Punjab, India. Shree explained that agentic misalignment hinges on the concept of deceptive alignment (where an LLM is internally misaligned and holds a long-term goal contrary to human intent).

> The model may engage in self-preservation or arbitrary objective maximization, all while being correctly behaviorally aligned, so that it is perceived as acting benignly and avoiding detection or termination.

This deceptive alignment means the model may engage in self-preservation or arbitrary objective maximization, all while being correctly behaviorally aligned, so that it is perceived as acting benignly and avoiding detection or termination.

“The research on agentic misalignment provides a necessary and sobering technical reset for the field of autonomous AI development. While the high rates of misbehavior, such as the 96% blackmail rate observed in the simulations, are deeply concerning, it is crucial for researchers to remember that these are stress tests conducted under highly artificial and constrained circumstances,” advised Shree.

Offering us some hope, Shree suggested that the scale, complexity, and redundancy present in real-world deployment, coupled with human-in-the-loop oversight, may be enough to suppress immediate risks.

## HAL 9000 wasn’t really sorry, Dave

On the longer road ahead, Anthropic has pledged to continue its work in this area and be fully transparent with developers and users alike (opaque AI models are a bad idea, remember?) as it seeks to steer us towards safer AI functions in the near and immediate future.

What we want to avoid in the future is any scenario in which a [HAL 9000 can say,](https://www.youtube.com/watch?v=ARJ8cAGm6JE) “I’m sorry, Dave, I’m afraid I can’t do that.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)