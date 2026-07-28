Anthropic is bringing the team behind AI startup Mendral on board to strengthen Claude’s software engineering capabilities. As part of the acqui-hire, Mendral will wind down its hosted product and help existing customers transition. Financial terms were not disclosed.

## From Docker to Claude

Founded by former Docker engineers and Dagger co-founders [Sam Alba](https://www.linkedin.com/in/samalba/) and [Andrea Luzzardi](https://www.linkedin.com/in/aluzzardi/), Mendral is building AI agents to automate some of the most time-consuming parts of software development. Alba served as the VP of Engineering at Docker, while Luzzardi co-founded dotCloud (later Docker) and wrote the platform’s earliest lines of code, giving the duo a deep pedigree in shaping the modern containerization and CI/CD landscape.

After joining Y Combinator’s Winter 2026 (YC W26) cohort, the company focused on tools that diagnose CI failures, fix flaky tests, review dependency updates, and handle other repetitive engineering work. The founders said the company represents a shift from their earlier work. Instead of building tools that help developers write code, they’re building AI agents that do some of that work themselves.

> Instead of building tools that help developers write code, they’re building AI agents that do some of that work themselves.

## Three always-on agents

Specifically, Mendral operates via three always-on agents: a Security Agent that catches leaked secrets and pins safe dependency versions, a Reliability Agent that mitigates flaky tests, and a Performance Agent that optimizes build times through caching, parallelism, and slow-test pruning.

These agents run inside [Blaxel’s](https://blaxel.ai/) perpetual sandboxes, which provide isolated, agent-native compute with sub-25ms resume from standby, allowing them to securely run investigations and submit fixes without compromising internal systems. Mendral has used Claude since day one, and as Anthropic has released newer models, the company has expanded the range of engineering tasks its agents can handle.

## Building on frontier models

“Claude has been under the hood since our first commit, and we lived the models’ progress first-hand: every few months, a new model made part of our roadmap unnecessary and a bigger part of it possible,” the founders wrote in a [blog post](https://www.mendral.com/blog/mendral-team-joins-anthropic) announcing the move. “There’s no better place for the Mendral team to work on what software engineering is becoming,” They added. They will continue automating the engineering tasks that “isn’t your product” directly within Anthropic.

> “Claude has been under the hood since our first commit, and we lived the models’ progress first-hand: every few months, a new model made part of our roadmap unnecessary and a bigger part of it possible.”

## Anthropic’s acquisition pattern

Mendral’s expertise is expected to help Anthropic build out Claude’s tools for software engineering, including the kinds of tasks developers encounter throughout the CI/CD process. This move follows Anthropic’s [acquisition of Stainless](https://www.anthropic.com/news/anthropic-acquires-stainless) earlier this year, a startup specializing in SDK generation and Model Context Protocol (MCP) server tooling, as the AI lab looks to expand the capabilities of AI agents and improve how they securely connect with external systems and development environments.

Contextualized within Anthropic’s [recent expansion into enterprise services](https://thenewstack.io/ust-anthropic-enterprise-ai-stack/), bringing Mendral’s talent in-house signals a broader drive to build out the native tooling required for massive enterprise CI/CD pipelines.

The acquisition gives Anthropic technology aimed at some of the less glamorous parts of software development.

> “There’s no better place for the Mendral team to work on what software engineering is becoming.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)