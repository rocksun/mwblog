Over the past few months, something quietly shifted. Frameworks like CrewAI, AutoGen, and LangGraph are no longer just showing up in demos—they’re running in production.

Teams are wiring together planners, tool-using agents, retrievers, and external APIs, then handing them real work. Incident response, internal copilots, automation pipelines – it’s all starting to look less like experimentation and more like infrastructure.

And once these systems are live, the problems become obvious very quickly. Not the usual “LLMs hallucinate” problem. Something more operational.

Right now, we’re very good at building agents and not very good at operating them. The frameworks make composition easy, but they stop short of giving you real control once [things are running at scale](https://thenewstack.io/what-it-takes-to-scale-ai-agents-in-production/).

And that gap shows up immediately in production.

The uncomfortable reality is that a lot of teams deploying [multi-agent systems](https://thenewstack.io/operations-shift-assistants-to-autonomous-multiagent-systems/) today are operating them with less visibility than they had for microservices 10 years ago. They’re trusting outputs without fully understanding the path that produced them.

That works for a demo. It doesn’t hold up when these systems start touching real data, real users, and real money.

What actually breaks is the system itself. A request that should take one or two steps turns into dozens of model calls. Agents bounce off each other, retrying, rephrasing, looping just enough to stay functional but not enough to be efficient. Latency creeps up. Costs follow. Nothing crashes, so nothing alerts. You just notice that things feel… off.

> “A request that should take one or two steps turns into dozens of model calls. Nothing crashes, so nothing alerts. You just notice that things feel… off.”

Or worse, everything appears to work, but the answer is subtly wrong. One agent times out, another compensates, a third fills in gaps with partial context. By the time you see the output, the failure is buried somewhere deep in a chain of decisions you can’t easily reconstruct.

Then, there is data. Not a single obvious leak, but a gradual propagation. One agent reads something sensitive, another summarizes it, a third includes it in a prompt to an external model. At no point does anything look explicitly dangerous, yet the system as a whole crosses boundaries it shouldn’t.

The common thread here is that nobody really sees what is going on.

Most teams try to bolt on the tools they already have. Logs, traces, maybe some prompt capture. That helps at the edges, but it doesn’t answer the core question: how did the system actually arrive at this outcome?

Agent systems aren’t just distributed systems with more API calls. They behave more like evolving execution graphs, where decisions are made dynamically and paths change depending on intermediate results. Watching individual calls is like looking at a single stack frame and trying to infer the entire program.

> “Agent systems aren’t just distributed systems with more API calls. They behave more like evolving execution graphs.”

[What is missing is visibility](https://thenewstack.io/jaeger-v2-ai-observability/) at the level where these systems actually operate.

You need to see how a request unfolds across agents, how deep the reasoning chain goes, where it branches, and where it loops back on itself. You need to understand not just that tokens were consumed, but why they kept growing across steps. And you need to track how data moves – not just where it started, but how it was transformed and where it ultimately ended up.

Without that, you’re left debugging symptoms. A slow response here, a higher bill there, an occasional wrong answer. The underlying behavior remains opaque.

What is especially interesting is that these systems do develop patterns over time. Even though they’re not deterministic, they’re not random either. Certain flows become common, certain depths of reasoning become typical. That baseline is incredibly useful because the real signal is when the system deviates from it. When an agent suddenly takes a path it never took before, or starts accessing data it normally wouldn’t, or expands a reasoning chain far beyond its usual shape.

That’s where monitoring should live – not in static rules, but in understanding the system’s normal behavior well enough to recognize when it drifts.

The question isn’t whether agents need monitoring. It’s whether we’re willing to treat them like the systems they’ve already become.

Right now, most aren’t and that needs fixing.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/601e5d5a-image001.png)

Moshe Bar is a serial entrepreneur. He was previously co-founder of Qumranet (sold to Red Hat) which created the industry standard KVM hypervisor, which today powers nearly all cloud offerings. He also co-founded software company XenSource, the makers of the...](https://thenewstack.io/author/moshebar/)