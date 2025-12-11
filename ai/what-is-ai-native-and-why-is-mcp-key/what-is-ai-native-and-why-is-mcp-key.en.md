Unlike cloud native, the term “AI native” is ill-defined. One might even say undefined. Many have glommed onto the term as a successor to the term cloud native, with the intention of garnering a halo effect from its predecessor.

The issue, however, is that the term cloud native arose organically as a way to describe a set of architectures, practices, patterns, technologies and related innovations that marked a massive shift in system architectures. This shift was most succinctly described in the famous “[pets vs. cattle](http://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/)” analogy.

Unfortunately, today “AI native” is an aspirational marketing term that is used more to say “Hey, we are using AI” rather than to highlight a shift in system architectures. Why is this? It’s because we are so early in the Autonomous Era (aka, the “AI Era”).

Barely a handful of years into this era, many of these practices, patterns and technologies are either brand new, misunderstood or simply haven’t even arrived yet.

Among the new technologies, some bright spots such as [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) are leading the way. Even so, we are still far from clearly defining what “AI native” is.

Although AI is evolving rapidly, many of the patterns that are to be defined will only arise through the adoption of AI and agentic workflows. For the Autonomous Era, much of the frontier technology is rapidly outpacing adoption. For us to look forward, we must look back.

The rise of the Cloud Era and cloud native applications is our best guide for the future. Looking closely at the rapid arrival and evolution of MCP — barely more than a year old — also provides us with some idea of where we are in defining what “AI native” should mean.

## The Rise of Cloud Native

As early as 2010, pundits and early cloud adopters were discussing the core tenets of cloud native architectures. These discussions predated the actual term, but the ideas were already beginning to be fairly well formed.

Cloud native as a term [did not gain popularity until nearly 2014](https://trends.google.com/trends/explore?date=all&q=%22cloud%20native%22&hl=en). In 2010, we used terms like “cloud ready” or “cloud-centric.” In fact, here’s a quote from the [interview that I did with Adrian Cockcroft](https://cloudscaling.com/blog/cloud-computing/cloud-innovators-netflix-strategy-reflects-google-philosophy/), then chief architect of Netflix. At the time, Cockcroft was working to rearchitect and replatform Netflix’s video service into a cloud native architecture on [AWS](https://aws.amazon.com/?utm_content=inline+mention), migrating from its legacy “pets” infrastructure in its own data center.

Cockcroft: “The key challenge is to get into the same mindset as the [Googles](https://cloud.google.com/?utm_content=inline+mention) of this world, the availability and robustness of your apps and services has to be designed into your software architecture, you have to assume that the hardware and underlying services are ephemeral, unreliable and may be broken or unavailable at any point, and that the other tenants in the multitenant public cloud will add random congestion and variance. In reality you always had this problem at scale, even with the most reliable hardware, so *cloud-ready architecture* is about taking the patterns you have to use at large scale, and using them at a smaller scale to leverage the lowest cost infrastructure.”

Around 2014-2015, with the rise of Kubernetes, and the founding of the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention), the term “cloud native” entered the common lingo. Kubernetes, one of the first truly cloud native application delivery platforms, exited Google, bringing hyperscaler sensibilities and architectures in a packaged form, standardizing patterns, and the rest is history.

[![The rise of cloud native timeline.](https://cdn.thenewstack.io/media/2025/12/7a98faf9-image1.png)](https://cdn.thenewstack.io/media/2025/12/7a98faf9-image1.png)

So, whether you measure the start of cloud computing from the advent of the “pay-by-the-drink” business model that Salesforce.com pioneered in 2000 or the public launch of AWS EC2 in 2008, there is a time lag of at least six years between cloud as an innovation and “cloud native” as a fully crystallized industry term. Why is this?

It’s because between the early 2000s and 2014, as cloud was being adopted, we were in the process of discovering, implementing and normalizing the patterns. Outside of the hyperscalers, discussions of CAP theorem (choose two: consistency, availability or partition tolerance), loose-coupling, eventual consistency, circuit breaker patterns, backoff-and-retry, horizontal scaling and all of the rest were few and far between. Nowadays this is all old hat and well understood throughout the industry.

Which brings us to today and the early misguided attempts to define “AI native” before we have even figured out what the patterns are supposed to be.

## Looking Closely at MCP and ‘AI Native’

There is no doubt that AI is changing the entire IT stack, and we are looking down the barrel of a massive architectural shift. At the infrastructure layer, what were once niche technologies used only in supercomputing/high-performance computing centers are now being [broadly deployed for new AI factories](https://www.mirantis.com/resources/mirantis-ai-factory-reference-architecture/) within enterprises and government agencies.

Horizontal scaling has shifted toward more of a “right-scaling” model: horizontal, vertical or both. So-called “accelerated computing” means a shift from traditional CPUs to GPUs, tensor processing units (TPUs) or Application-Specific Integrated Circuits (ASICs)/Field-Programmable Gate Arrays (FPGAs) designed for vector-based computation. Disaggregated white box systems are giving way to vertically integrated, vendor-centric systems designed to pump out the most tokens per second for the lowest cost.

Meanwhile, AI agents, which deliver the largest value in AI, largely depend on generative AI (GenAI)/machine learning (ML) inference engines to be their “fuzzy logic” brains. These agents consist of minimalist scaffolding and tools, wrapped around inference engines ( “reasoning large language models [LLMs]”) that provide all the core business logic.

Highly deterministic classic code is giving way to nondeterministic “thinking machines” that — at this point-in-time — still require guardrails, evaluations and humans in the loop to ensure quality output.

Yet, the upside is obvious: These systems, while less deterministic, can simultaneously handle uncertainty, edge cases and unanticipated situations in ways that deterministic classic code never could. Most importantly, like with the rise of [cloud native technologies](https://thenewstack.io/cloud-native/ "cloud native technologies") before it, it’s clear that not everything will change.

Classic code must be intertwined with and work seamlessly with AI logic. We are even seeing bleeding-edge work to dynamically interpolate [classic code and LLM logic](https://dl.acm.org/doi/10.1145/3763092).

While AI has been with us for decades, just as many of the patterns behind “cloud” were with us for decades before they congealed into a form, it is only in the past few years, with GenAI, that AI has become something fully formed and usable for mass adoption.

Now, in this Autonomous Era, we are in the process of understanding how it will transform the entire IT stack, and adoption of AI agents is where the real learning will happen.

It’s far too early to understand what “AI native” means. Only a few years in, we just know a handful of the emerging patterns. We are only now discovering what works and what does not. Let’s look at the recent emergence of MCP and its rapid evolution as an example.

First, MCP appears to have arisen out of a direct need identified within Anthropic. Necessity is the mother of invention, while a pithy saying, has been proven true time and again.

Launched barely a year ago, MCP saw rapid adoption, warts and all. Within a few short months, Anthropic shipped a major update to MCP to include authentication and basic security, a serious oversight in the original release.

A few months later, another release was shipped, providing the MCP Registry, a minor oversight, but another obvious shortcoming. Most recently, Anthropic has started to pivot from its initial focus on MCP servers providing “tools” for agents to call, toward a model using classic deterministic code to call multiple tools, saving context window/data degradation and dramatically increasing efficiency.

This is no criticism. This is how the sausage is made. If Anthropic had waited until MCP was “perfect,” it might not have had rapid adoption. This is the canonical minimum viable product (MVP) route that is so lauded in Silicon Valley circles, followed by rapid iterations based on feedback, customer need and practical learning. This is also how we learn the patterns, technologies and architectures that will eventually become “AI native.”

Not everything we learn about “AI native” will come through MCP. Learning will happen across the spectrum, yet MCP will be a centerpiece, both because Anthropic has shown an ability to rapidly innovate and because of the recent announcement of the [open source Agentic AI Foundation](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/).

I’m reminded of how OpenStack “sucked the oxygen out of the room” when it launched, putting a nail in the coffin of its predecessors like CloudStack, Eucalyptus, OpenNebula and others. Similarly, an open source MCP will simply accelerate, driving further innovation, creating an MCP ecosystem and helping us get to “AI native” faster and further. No doubt about it, Anthropic has put alternatives such as Google’s Agent2Agent (A2A) on notice that it intends for MCP to be the standard, not one among many.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/10/79390449-cropped-2934c701-randy-bias-head-shot.jpg)

Randy Bias is a pioneering advocate for cloud, DevOps, and open source technology, recognized for driving successful open sourcing efforts in enterprises of all sizes and significantly influencing the industry’s transition from proprietary models. He has played a critical role...

Read more from Randy Bias](https://thenewstack.io/author/randy-bias1/)