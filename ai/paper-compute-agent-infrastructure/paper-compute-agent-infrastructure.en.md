“Everyone’s building agents, not enough people are building the systems underneath them,” open source veteran [Brian Douglas](https://www.linkedin.com/in/brianldouglas/) wrote on LinkedIn [last month](https://www.linkedin.com/posts/brianldouglas_newjob-ugcPost-7442176114288144384-Nh5-/), as he announced his new company.

It’s a claim that, while hard to measure definitively, mostly holds up to scrutiny. Companies are already [building and deploying agents](https://thenewstack.io/how-to-build-production-ready-ai-agents-with-rag-and-fastapi/) to some degree, but the infrastructure behind them is often improvised—part SDK, part cloud plumbing, part internal tooling. The pieces are there, sure, but they haven’t yet settled into anything like a coherent system.

And this is what Douglas and his CTO co-founder, [John McBride,](https://www.linkedin.com/in/jpmcb/) are addressing with [Paper Compute Company](https://papercompute.com/), a startup building the missing layer beneath AI agents – doing so entirely on an open source foundation.

“What’s missing from the current setup is that people need to have the confidence to run this stuff in all different types of situations,” Douglas tells *The New Stack*. “Having proper cloud native tooling to control agents and LLMs in production – that’s where we’re seeing a lot of energy happening right now in the market. We weren’t seeing this three months ago.”

> “Having proper cloud native tooling to control agents and LLMs in production – that’s where we’re seeing a lot of energy happening right now in the market. We weren’t seeing this three months ago.”

While the company was formally unveiled in March, Douglas and McBride had been setting the wheels in motion with a series of product launches. In February, they [open-sourced *Tapes*](https://papercompute.com/blog/introducing-tapes/), a zero-instrumentation observability layer that captures and records agent activity without requiring changes to application code.

The system sits between AI agents and their inference providers, capturing telemetry. It includes a proxy service to intercept and record traffic, an API server to query sessions, messages, and metadata, a CLI client to manage recordings and run searches, and a terminal UI to trace agent activity step by step.

![Tapes](https://cdn.thenewstack.io/media/2026/04/e2795a69-tapes-1024x600.png)

***Tapes***

That was [followed shortly after by *StereOS*](https://papercompute.com/blog/introducing-stereos/), a hardened Linux-based operating system designed to run AI agents in isolated, sandboxed environments, giving teams more control over how those systems behave in production.

![StereOS](https://cdn.thenewstack.io/media/2026/04/43d33af4-stereosgif.gif)

***StereOS***

The aim is to address a core problem with AI agents: once they are running in production, teams often lack both visibility into what they are doing and control over how far they can go.

“Tapes show you what happened — StereOS makes sure it can’t go further than it should,” Douglas writes in the company’s [March launch blog post](https://papercompute.com/blog/introducing-paper-compute/).

Paper Compute [created a Gmail agent demo](https://papercompute.com/gmail/) showing how this works, using [an OpenClaw agent](https://thenewstack.io/persistent-ai-agents-compared/) running inside a StereOS virtual machine to triage an inbox under strict controls. It can read messages and classify them, but cannot delete or send replies, nor can it access anything beyond a small allowlist of external services.

Every interaction with the model is captured by Tapes as a complete, replayable log — prompts, responses, and decisions stored locally in a tamper-evident record. When the session ends, the environment is torn down, and credentials are destroyed, but the full execution history remains available for inspection.

## Open source meets engineering and AI infra

Douglas is a familiar face in open source circles. After a stint as GitHub’s director of developer advocacy, he led ecosystem and developer experience efforts at the Cloud Native Computing Foundation (CNCF), after the CNCF’s parent Linux Foundation [acquired *Open Sauced*](https://web.archive.org/web/20251117220928/https://opensauced.pizza/blog/opensauced-is-joining-the-linux-foundation), a [developer insights platform he founded](https://thenewstack.io/after-github-brian-douglas-builds-an-open-source-startup/) to help contributors find and engage with open source projects.

McBride, meanwhile, previously collaborated with Douglas both at the Linux Foundation and at Open Sauced as its lead AI engineer, having previously worked as an engineer at Amazon Web Services (AWS).

The Paper Compute team has also just [brought on founding engineer Matthew Yeazel](https://www.linkedin.com/feed/update/urn:li:activity:7449484145686380545/), who spent several years at AWS working across EC2, Amazon Linux, and Bottlerocket, the container-focused operating system.

> Paper Compute is effectively trying to sit somewhere between developer tooling and core infrastructure, with a team shaped by experience building and operating systems at scale.

That mix of open-source, infrastructure, and systems-engineering experience reflects what Paper Compute is effectively trying to do: sit somewhere between developer tooling and core infrastructure, with a team shaped by experience building and operating systems at scale.

“We know what production infrastructure looks like – agents deserve the same rigor,” Douglas says.

## Understanding systems

As more teams begin running agents in production, understanding what those systems are actually doing becomes a challenge. The data exists, but it’s often incomplete, hard to access, or tied to the specific SDK or framework on which the agent was built.

In many cases, the only way to inspect an agent’s behavior is through the tooling provided by the platform itself — frameworks like LangChain and its companion observability tool, LangSmith, which capture traces, logs, and execution paths, but have historically done so within their own ecosystems.

Douglas points to a simple example: when an agent fails, the goal is not to reconstruct what happened after the fact, but to have a complete record already in place—one that can be queried directly.

“So instead of wondering how you got somewhere, you can just interact with the data,” he said. “There’s no SDK, no extra code—it just runs in the background.”

That points to where Douglas sees the longer-term value — not in the infrastructure itself, but in what it captures. Agent activity, he argues, generates a record of how systems behave and decisions get made that becomes valuable in its own right.

“The value is actually more in the data that goes through the agents,” he says.

While it’s still early days for Paper Compute, the company is already beginning to sketch out what a commercial offering around its open-source projects might look like.

## Pay-per compute: A data play

At its core, Paper Compute isn’t just building tooling, but trying to establish a layer for running and managing AI agents in production — one that spans observability, execution, and, eventually, orchestration.

The company name itself reflects that thinking. “You end up paying for compute,” Douglas said, pointing to a model where usage — and the data flowing through these systems — becomes central to how the platform is monetized.

That means building on top of the telemetry captured by tools like Tapes, turning agent sessions into reusable “skills,” and using that data to optimize how models are deployed and run.

Early versions of the platform are already being tested internally, with the team beginning to show the system to prospective users.

> Longer term, the company is aiming at teams that need tighter control over how AI systems operate.

Longer term, the company is aiming at teams that need tighter control over how AI systems operate – particularly in regulated or on-premise environments, where security, compliance, and auditability are paramount.

Douglas, for his part, draws a parallel with an earlier wave of infrastructure. “We had Kubernetes, like, 13 years ago, when cloud native infrastructure started to take shape,” he says. “Now we’re seeing a similar wave with AI tooling.”

By way of example, Kubernetes is increasingly being used to orchestrate [GPU-heavy AI workloads](https://www.civo.com/learn/kubernetes-llama-deploy-ai-models-llm-gpu-cluster), extending the same model it established for scaling CPU-based applications to a new class of compute-intensive systems.

At the same time, open standards like [OpenTelemetry are evolving](https://grafana.com/blog/a-complete-guide-to-llm-observability-with-opentelemetry-and-grafana-cloud/) to capture traces, metrics, and logs from LLM and agent systems, offering a more consistent, vendor-neutral way to understand how these systems behave in production.

That, Douglas suggests, could bring the ecosystem to a similar point of maturity. “Through open source, we’re going to see that tooling commoditized,” he says. “And in the next six months, I think we’ll see enterprises — banks, large companies — ready to scale this.”

“But the tooling still needs to give them the trust to run agents in production,” Douglas adds.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)