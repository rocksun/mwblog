If software engineers are no longer writing code, what are they doing? That’s the question on millions of minds.

AI tools are now [widely used](https://thenewstack.io/ai-engineering/) by developers, but [fear of layoffs](https://www.theguardian.com/technology/ng-interactive/2026/jul/12/software-developers-engineers-ai) remains a concern. On the other hand, coding is only one part of software engineering. This creates an opportunity for engineers to get closer to the business and to the context of their role’s purpose within their organization and industry.

“I like to think in parallels. In 2009, I was like, what if Ops was more like Dev?” wondered [Patrick Debois](https://www.linkedin.com/in/patrickdebois/), a member of technical staff at Tessl, [coiner of the term DevOps, and founder of the DevOpsDays global event series](https://thenewstack.io/qa-patrick-debois-on-the-past-present-and-future-of-devops/).

His comments came during PlatformCon London earlier this summer, where he told the audience that as context — the specified knowledge AI uses for tasks — replaces human code, “the software development lifecycle becomes the context development lifecycle.”

This lifecycle has grown from a single CI/CD feedback loop to a series of concentric loops around generating, evaluating via test-driven development, distributing context as a package, and observation. This growth is being spurred by a shift in how individual developers, teams, and whole organizations think. And it opens a whole new opportunity for [platform engineering](https://thenewstack.io/platform-engineering/) teams.

![](https://cdn.thenewstack.io/media/2026/07/495764a7-context-development-lifecycle-1024x549.png)

“The mindset change for a developer that I would advocate is that if the agent didn’t do what you want, stop correcting the code. Improve the system, not the prompt,” Debois tells *The New Stack*. “That kind of shift is from ‘I’ll do it together with my agent,’ over to ‘I’ll help my agent do it better’.”

Debois sees this as a necessary shift from deterministic to non-deterministic and probabilistic systems and workflows. And it’s one that involves as many changes to the way we work as to the technology itself. But it can’t be just done by an individual engineer or at the team level. Like DevOps, it is a change that can only be realized at scale.

## How to become a context-driven organization

It may have felt like we flipped a switch and every company was — *wham!* — “AI-first.” In reality, just like DevOps, microservices, and cloud transformations before it, AI is making a continuous transition into the foreseeable future. So how does your engineering organization get onto the right context-driven path?

At the team level, Debois says, a good question to ask is how many touches does one need for agents to work? Different engineers across different teams will feed in different points of context, including:

* Codebase
* [Specifications](https://thenewstack.io/spec-driven-development-the-key-to-scalable-ai-agents/)
* Post-mortems
* Documentation Slack messages
* Architectural decision records
* Code samples
* Use cases
* Compliance guidelines

For context and therefore agents to scale, you need to know what agents individuals and teams are producing and their outputs.

“When you’re optimizing for A, and we’re optimizing for B, let’s make sure that the whole context that we give is optimized for the whole team,” Debois explains, including “If you are optimizing the system for your laptop, can we optimize it for the team workflow? And then you just scale up, like, can we do this on the platform level? Or across multiple teams?”

“It’s not something you seek out,” Debois tells *The New Stack*. “Maybe they can speed it up, but you would see the signs of ‘Oh, I have context, and you have context. Sure, it’s on Slack. What if this was in the repo and I can reuse this?” following the pattern in tech that has any trend spreading from a single enthusiast, to an enthusiastic team, to a couple of teams, and eventually being built into the platform.

Like all tool-driven changes, AI is as much about the people and processes as it is the tech. But, he argues, the tools open up possibilities for behavioral changes.

“The fundamental change is the system, not the prompt,” he continues. “And then look for collaboration directions from solo to sharing things, and now working on the [context building] as a team together.”

## Context engineering evolves to harness engineering

Organizations may think that context is fed into your agentic systems just once, or a couple of times a year when rules change, but, Debois warned, it’s not meant to be Waterfall. It’s iterative. If the context isn’t, then engineers fall back into the bad habit of rephrasing prompts or just fixing the code itself. Relying solely on traditional feedback loops means your AI agent fleet will not return on its investment.

“There is the industry narrative that if there’s a problem with AI, we just use more AI,” Debois tells the PlatformCon audience. He gave the example of how one large language model (LLM) or AI agent generates some code. “We ask the LLM to assess this, and it will call almost like a unit test. It hasn’t run the code; it just looks at the code.”

There’s some value in that, perhaps in enforcing API endpoints or other binary quality gates, but, he says, it’s not enough. Instead, if you specify what you need within the context, then that drives how the agent runs and evaluates the code.

But it shouldn’t stop there. The next stage of agentic AI maturity, he contends, is grounded in harnesses and loops.

Harness engineering focuses on building the infrastructure, guardrails, and tools that wrap around an LLM to support the development of reliable, autonomous agents.

Debois defines an agent’s inner harness as logs, metrics, and traces behind query APIs, “so the coding agent sees the consequences and improves,” all of which feed into that living loop of generation, evaluation, distribution, and observation.

![](https://cdn.thenewstack.io/media/2026/07/dc6e7834-agent-inner-harness-1024x563.png)

With this pattern, the agents “autonomically know that something is wrong without you having to tell them all the time,” he says, because “it has sensors in a way that knows what fails, what it improved, and then can go back to improving these walls,” even when engineers are hard-coding something.

Again, harnesses should not be built in isolation serving a single developer or team.

“They’re building a harness for the whole world, so imagine the consensus of this is how we do tests, and this is how we do verification, and all the knowledge that is currently in all these different teams,” Debois says. “People start building on that same pipeline.”

The reality is that most organizations end up with multiple pipelines, but these loops become the next evolution of each organization’s feedback loops. And thus, building for AI coordination leads to better organizational collaboration.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)