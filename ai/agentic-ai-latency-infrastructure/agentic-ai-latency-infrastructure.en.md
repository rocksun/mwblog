**Half of enterprise AI deployments are missing** their own latency targets at peak load. This is the headline finding of [Akamai’s State of AI Inference 2026 report](https://www.akamai.com/lp/the-state-of-ai-inference), which surveyed 200 AI practitioners and found that 82% of organizations say their most critical use cases require end-to-end response times of 500 milliseconds or less. A total of 64% of organizations now require end-to-end response times of less than 250 milliseconds for their most important use cases, yet 50% of deployments are failing to meet these latency demands at peak load.

My colleague Ari Weil, who leads product marketing for our cloud computing business and ran point on that research, [summarizes the findings](https://www.akamai.com/blog/cloud/ai-study-organizations-struggle-maintain-latency-scale) well: “The enterprise AI honeymoon phase is over… they are hitting the latency wall.”

## **Agentic workflows aren’t a “single round trip”**

The latency issue stems from the way agents work. It’s an iterative process, somewhat like a king sending out knights, emissaries, and messengers to conduct the business of the kingdom. There are many comings and goings, not just one person sent on a single round trip.

For instance, when an agent built on a framework like LangChain, CrewAI, or Pydantic AI received a user request, it can fan out into dozens of sequential operations such as a reasoning call, a tool invocation, an API lookup, or a context retrieval. Then an agent may execute another reasoning call to decide what to do with what just came back. Every one of these operations or “hops” that must cross a wide-area network to reach a centralized data center adds latency, and a chain of 50 hops can multiply that transport time into seconds on its own, regardless of how fast the model generates tokens.

In fact, in a [paper posted to arXiv in November 2025](https://arxiv.org/abs/2511.00739), researchers found that CPU-side processing can account for up to 90.6% of total latency in agentic workloads. In other words, your GPU might finish a reasoning step in a few hundred milliseconds, but then it might have to wait on additional tool call runs to CPUs in distant data centers. This is what causes spikes in GPU idle time.

> “More GPU capacity does nothing for this. You can’t brute-force your way out of a wait state.”

More GPU capacity does nothing for this. You can’t brute-force your way out of a wait state. This is the part of the conversation the industry keeps skipping, mostly because “buy more GPUs” is a much quicker fix to suggest than “figure out where your CPU-bound work is actually executing and why it’s so far from the data it needs.”

## **We need new benchmarks to fix the latency issue**

One reason the looming latency wall sneaks up on teams is that they are not looking at the right benchmarks for agentic workloads. Most LLM-serving benchmarks measure tokens per second and GPU utilization on a single box. That’s great if the workload is indeed on a single box (i.e., one model answering one prompt), but that’s not the case with agentic workloads. Those benchmarks don’t address an agentic response that, say, makes a 50-hop chain cross a WAN 4 times to reach 4 separate services.

> “Staging may pass the benchmarks because it tests the model, but production tests the whole chain, including every hop your serving engine was never designed to see.”

That’s where the gap lies: Staging may pass the benchmarks because it tests the model, but production tests the whole chain, including every hop your serving engine was never designed to see.

## **The 500ms wall is not a soft target**

This is showing up at scale because agents are moving into production faster than most teams’ architecture is evolving to support them. [LangChain’s State of Agent Engineering 2026 survey](https://www.langchain.com/state-of-agent-engineering) of more than 1,300 professionals found that 57.3% of organizations now have agents running in production, up from 51% a year earlier. *Among those builders, latency has become the second-most-cited barrier to production, behind only output quality.*

This is a serious issue for application teams. The 500ms threshold in Akamai’s survey isn’t a performance goal teams can afford to miss. For a live customer interaction or a real-time compliance check, that 500ms determines whether the application works or it doesn’t.

## **We’ve solved this problem before**

There’s a reason this feels familiar to anyone who was building for the web in 1999. Akamai exists because of a nearly identical problem. MIT researchers Tom Leighton and Danny Lewin founded the company to answer a challenge posed by Tim Berners-Lee: fix what the press had started calling the “World Wide Wait,” the crushing latency of pulling every request back to a small number of centralized servers. When the trailer for *The Phantom Menace* crashed sites across the internet in 1999, the culprit was distance: millions of browsers all reaching for the same far-away origin server at the same moment. The fix moved content to thousands of points closer to the people requesting it, instead of trying to build a faster origin.

Agentic AI is running into the same wall, just in a different vehicle. AI works just fine on centralized inference if you’re talking about running batch jobs overnight. But today’s applications built on agentic AI are real-time loops sitting inside live transactions, and the fix for agentic lag is distribution. Instead of expanding racks of CPUs and GPUs at the center, we need to move agentic execution to where the model’s tools, context data, and users actually live.

## **Agentic AI needs a tiered architecture, not a bigger data center**

In practice, agentic AI requires a tiered architecture, one that includes a centralized core, regional GPU clusters, and CPUs at the Edge.

* Centralized core—perfect for heavy reasoning over large context windows, where the round trip to a large model matters less than the model’s raw capability.
* Regional GPU clusters, increasingly built on hardware like NVIDIA’s Blackwell platform—ideal for localized inference, so the heaviest compute sits closer to where demand actually concentrates.
* Edge CPUs—the essential component for speed. This is the nexus for tool execution, orchestration, and context retrieval, since these are the steps that happen most often in a chain and benefit most from sitting next to the data and APIs they call.

We’ve built Akamai Inference Cloud around this tiered framework. It’s the same distribution logic behind our AI Grid Orchestrator. We route CPU-bound orchestration and tool calling to the edge, and keep GPU-bound reasoning where it makes sense, regionally or centrally.

## **What to demand before you commit**

The good news is you don’t need to distribute every workload to the edge on day one. But before you commit to a production architecture, you should know which of your agent’s dozens of hops are latency-sensitive and which aren’t. Then build a defined performance budget for each one.

> “The teams that treat it as a GPU-shopping decision will be back here in six months, staring at the same four-second response time, wondering why more compute didn’t help.”

My advice is this: Before signing off on a large-scale inference deployment, ask your infrastructure for four things:

1. Portability across regions and providers
2. Elasticity to absorb peak load without falling over
3. Data locality so tool calls aren’t crossing oceans to reach the context they need
4. A performance budget you’ve actually tested against production traffic, not staging traffic.

The teams that address this infrastructure decision now will be the ones whose agents still work when the benchmark environment transitions to real users. The teams that treat it as a GPU-shopping decision will be back here in six months, staring at the same four-second response time, wondering why more compute didn’t help.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/08/e234ae95-cropped-999cb32a-jon-alexander-akamai-600x600.jpeg)

Jon Alexander is Senior Vice President of Product for the Cloud Technology Group at Akamai. He is responsible for the strategy, roadmap, and success of the cloud computing and delivery products. Alexander joined Akamai in 2017 and led various product...

Read more from Jon Alexander](https://thenewstack.io/author/jon-alexander/)