2025 is shaping up to be the year [agentic AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) crossed from research to production. Gartner reports that [34% of businesses now deploy AI agents](https://www.gartner.com/en/articles/ai-agents), and by 2028, up to 15% of daily work decisions will be made autonomously, with a third of enterprise software applications expected to include some form of agentic capability.

Yet so far, the promise behind agentic AI hasn’t matched the reality on the ground.

“Most agentic AI projects right now are early stage experiments or proof of concepts that are mostly driven by hype,” [said Anushree Verma, a senior analyst at Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027). “This can blind organizations to the real cost and complexity of deploying AI agents at scale, stalling projects from moving into production.”

The problem, as it turns out, might not be the intelligence of AI models that have the spotlight — it’s probably their [cloud infrastructure](https://thenewstack.io/introduction-to-cloud-native-computing) too.

Agentic AI introduces a new kind of workload: thousands or even millions of semi-autonomous processes that perceive, reason, act and collaborate over time. They hold memory, context and goals. These properties break most of the cloud architecture patterns that the industry has spent two decades perfecting.

To understand why so many agentic projects stall, and what might unblock them, The New Stack spoke with [Matthew Gregory](https://www.linkedin.com/in/matthewgregory/), founder and CEO of [Autonomy](https://autonomy.computer/?utm_content=inline+mention), a new platform as a service (PaaS) built entirely around what is called the [actor model](https://www.geeksforgeeks.org/system-design/actor-model-in-distributed-systems/). Having spent years exploring what it takes to run autonomous, distributed systems at production scale, Gregory and his team are confident that this is how this next wave of AI products will be built.

“Familiar cloud architecture patterns have actually become barriers,” Gregory said. “Agentic products function differently than modern web apps, and they need tools designed for that difference.”

## How the Actor Model Provides a Foundation for AI Agents

The actor model isn’t new. First conceived in 1973, it was inspired by concepts in physics like general relativity and quantum mechanics. It has since become an elegant pattern for managing concurrency, one that quietly powers some of today’s most demanding systems, including WhatsApp, Discord and Databricks.

In the actor model, the basic unit of computation isn’t a container or function, but an actor — a lightweight, independent entity that “owns” its own state, processes messages asynchronously and communicates with other actors through message passing. Hundreds of thousands of actors can run in parallel inside a single process: starting up in milliseconds, idling cheaply and persisting for as long as they are needed.

> “If you put an agent in a container, it idles while you pay for the capacity. At scale, that’s a DevOps nightmare.”  
> **— Matthew Gregory, founder and CEO of Autonomy**

For AI agents, modeling each one as a single actor is an almost perfect fit. Actors (agents) are:

* **Stateful:** Each actor remembers its identity, memories, context and goals.
* **Long-lived:** Actors can stay idle for long periods without wasting resources.
* **Asynchronous:** They yield gracefully while waiting for [large language model (LLM)](https://thenewstack.io/what-large-language-models-can-do-well-now-and-what-they-cant/)  completions or tool responses.
* **Massively parallel:** Millions can coordinate and collaborate to support agentic patterns like subagents and orchestrated workflows.
* **Built-in messaging:** Mailboxes and queues make secure communication natural.

“An actor has a tiny footprint and handles concurrency and messaging beautifully,” Gregory explained. “It’s the right atomic unit for agentic systems.”

## Why Containers and Serverless Fall Short

Simply put, traditional cloud primitives weren’t designed for agentic workloads. While serverless functions are perfect for short, stateless bursts of work that are measured in milliseconds, they are much less suitable for an agent that must hold memory and context across long-running tasks. Reconstructing an agent’s state with every invocation adds latency and cost, while also breaking continuity.

Containers, on the other hand, preserve state but come with weight. Keeping thousands — let alone millions — of mostly idle containers online is operationally painful and financially unsustainable.

“If you put an agent in a container, it idles while you pay for the capacity. At scale, that’s a DevOps nightmare,” Gregory said. “Go serverless, and the agent forgets who it was every time it wakes up. Actors give you persistent state and exceptional cost efficiency.”

In other words, actors let developers think in terms of relationships and collaboration without the operational overhead or resource waste that causes most agentic prototypes to fail.

## Solving Trust and Data Security for Autonomous Agents

Even if the issues of concurrency and scale are solved, another challenge quickly surfaces: trust. Agents don’t just compute; they must also communicate — often across clouds, services and organizations. Each interaction must be authenticated, encrypted and verifiable.

Autonomy addresses this with Private Links, a secure messaging layer built on top of the open source [Ockam](https://docs.ockam.io/) toolkit that Gregory’s team launched several years ago. Every agent on the platform mints a unique cryptographic non-human identity (NHI), then establishes mutually authenticated, end-to-end encrypted channels with its peers. This eliminates any need for VPNs, public endpoints and shared secrets in the cryptographic sense.

“Data in motion is one of the hardest problems for agentic developers,” Gregory said. “Private Links solve that with opinionated cryptography and protocols baked in from Day 1. Better yet, an agent running on the Autonomy Computer can create a secure connection with any other agent, model context protocol server, tool, application or data store in any other cloud or network.”

That heritage matters. Ockam — an identity, messaging and access-control library with a vibrant open source community — has been battle-tested for secure communication between distributed systems. Autonomy extends those same trust primitives to the world of AI agents.

“In a way, we’ve got a five-year head start on the problems that need solving to ship agentic products,” Gregory noted. “Autonomy builds directly on that foundation.”

## From Pieces to Platform

Even with the right architecture and security model, many teams still drown in integration work. The typical agentic stack today involves a dozen frameworks — LangChain for LLM tooling, CrewAI for multiagent coordination, plus vector databases, schedulers, observability layers, identity, maybe even some Kafka and a mess of custom glue. Each solves one piece; none form a coherent whole.

“Infrastructure is hard to scale and easy to get wrong,” Gregory said. “As a product company, you end up spending all your time on plumbing instead of product.”

Autonomy’s platform as a service aims to close that gap. It packages the actor runtime, trust layer and observability tools into a single environment. Developers build locally with their Python SDK, then deploy into a globally distributed runtime without touching containers, Kubernetes or serverless orchestration. Scaling, routing and secure messaging come built in.

At first glance, Autonomy might look like another agentic framework, but there is an important distinction. Frameworks help you build; platforms help you ship. Gregory illustrates it well with this analogy: “It’s like the relationship between Next.js and [Vercel](https://vercel.com/), or between Rails and [Heroku](https://www.heroku.com/?utm_content=inline+mention). Frameworks get you to code; platforms get you to customers.”

> “Just telling people to ‘go use actors’ doesn’t make all the problems of distributed systems go away — it just hands them a new set of hard engineering challenges.”  
> **— Matthew Gregory**

## Actors Need Good Architecture Too

While the actor model offers the right foundation for agentic systems, it isn’t a silver bullet just by itself. Engineers who have previously built actor-based frameworks will know the trade-offs well: tracing a single request across thousands of asynchronous actors can be notoriously difficult; unbounded concurrency can lead to message storms; and recovering state if an actor crashes or restarts requires careful orchestration. The actor model works great for agents, but it also needs some guardrails too.

“Those are all real problems,” acknowledged Gregory. “Just telling people to ‘go use actors’ doesn’t make all the problems of distributed systems go away — it just hands them a new set of hard engineering challenges. Building a runtime that handles agent identity, tracing, scheduling, failure recovery and security correctly is a [serious piece of infrastructure work](https://thenewstack.io/runtime-context-missing-piece-in-kubernetes-security/). That’s exactly the burden we wanted Autonomy to take off the developer’s plate.”

By recognizing the long-known challenges with actor-based runtimes, and by designing its platform to address them, Autonomy turns a once-esoteric architecture into something that lean teams can use to ship reliable, production-grade agentic systems.

## Developer Experience: Small Teams, Big Ambitions

Currently, Autonomy’s initial audience is small, fast-moving teams — startups and “startup-mode” groups inside larger enterprises that need to ship quickly but who are hamstrung by a limited headcount. These teams can’t afford to build bespoke infrastructure that is tuned to scale before they ship to production.

“We’re really, really obsessed with developer experiences,” Gregory said. “Teams constrained by people, time or resources will need something that just works, something that’s automagical, at full scale.”

The platform already includes enterprise-grade tools such as logs, metrics, evals and secure endpoints for observability and operations. But notably, Autonomy’s biggest advantage seems to be its simplicity. Developers can  [focus on what their agentic products can do](https://thenewstack.io/agentic-ai-is-quickly-revolutionizing-ides-and-developer-productivity/), not how to make them run.

## Why This Architectural Shift Matters Now

If the last decade of cloud computing was about elastic compute, the next one will be about elastic autonomy — running not just more servers, but more *decisions*. The architectural unit of that future isn’t a container or function, it’s an actor.

The actor model provides the foundation for systems that can think, remember and coordinate at scale. It’s an idea that has existed for half a century, but the recent rise of agentic AI finally gives it a renewed mainstream purpose.

Autonomy’s bet is that a PaaS built around actors — with trust and security woven in — will become the default substrate for these systems. Teams that embrace this model won’t just build smarter agents; they will ship production-ready products faster.

“We’re not inventing a new idea so much as putting a thousand architectural decisions into a single platform and offering it as a simple product experience,” Gregory said. “Actors have always fit this problem. Now, the Autonomy platform makes it easy for every builder to ship a scaleable, connected agentic product.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/09/69f0904d-tgcfilao_400x400.jpg)

Kimberley Mok is a tech and design reporter who covers artificial intelligence, robotics, quantum computing, tech culture and science stories for The New Stack. Trained as an architect, she is also an illustrator and multidisciplinary designer who has been passionate...

Read more from Kimberley Mok](https://thenewstack.io/author/kimberleymok/)