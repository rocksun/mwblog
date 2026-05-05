The essentially composable nature of modern enterprise software stacks enables architectural freedom. Software developers are able to take advantage of componentized and containerized logic to create optimized code deployments, which can themselves be shifted between workloads that traverse [multi-cloud instances](https://thenewstack.io/multicloud-architecture-what-i-want-to-see/).

[Agentic functions](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/) are enjoying some of the same freedom of movement, but unstandardized AI agent telemetry leaves us in the Wild West.

Developers are empowering agents in production with the ability to call multiple system tools, invoke connections to AI models (language, visual and so on, both large and small) and even “improve” user requests and hand off work to other domain-specific agents.

That’s all great news for system adaptability, but it’s a nightmare waiting to happen for agent telemetry.

> “When you use standards like [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) and [OpenInference](https://github.com/Arize-ai/openinference), you keep optionality without losing visibility… The trace format stays consistent even as the stack changes.” – Richard Young, Arize.

## Why agent telemetry matters

Inside the wider universe of observability, telemetry at this level lets software engineers know where agents exist, what connections they are entitled to and what actions they have taken.

According technical director of partner solutions architecture at AI agent engineering company [Arize](https://arize.com/), [Richard Young](https://www.linkedin.com/in/riyoung/)**,** the agent telemetry challenge is not a question of where integration points exist, he says that the “important part is portability”, not just of agents, but of the telemetry standards we use to measure them.

“When you use standards like [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) and [OpenInference](https://www.openinference.xyz/), you keep optionality without losing visibility. Standardized agent telemetry lets you change frameworks, models, tools, or observability backends without rebuilding your instrumentation every time. The trace format stays consistent even as the stack changes,” writese Young, on [his organization’s blog](https://arize.com/blog/agent-telemetry-standards/) channel.

For Young, the real story isn’t a point-to-point integration, but the push toward a shared telemetry model for agents.

## Google Cloud & Arize AI

Arize is partnering with Google Cloud subsequent to the hyperscaler launching [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) last month. The Arize AX enterprise agent development platform not only receives traces (chronological records of software execution event history) from the Gemini Agent service, it also aligns agent telemetry around OpenTelemetry and OpenInference. This is done so software engineering teams can instrument agents once, analyze behavior consistently, and avoid locking critical observability data inside a single platform.

CEO of cloud resource optimization company [EfficientEther](https://www.efficientether.co.uk/), [Ryan Mangan](https://www.linkedin.com/in/ryanmangan01/), tells *The New Stack* that in any live production software deployment, you can’t operate what you can’t see, and that goes double for agents.

“A single agent run can include request rewriting, retrieval, multiple tool and model calls, retries, and handoffs before producing a final answer,” Mangan says. “Without structured telemetry covering each of those steps, debugging becomes painstaking guesswork and evaluation becomes extremely difficult.”

Mangan agrees that standards like OpenTelemetry and OpenInference matter because they give developers a consistent way to understand what an agent actually did, regardless of which framework, model, or platform produced it.

## Google Cloud NEXT

OpenTelemetry arrived back in 2019, created through a merger of two initiatives, Google’s OpenCensus and the [Cloud Native Computing Foundation](https://thenewstack.io/cncf-kubernetes-is-foundational-infrastructure-for-ai/)’s OpenTracing project.

In [a Google Cloud NEXT session](https://www.youtube.com/watch?v=nLH0IqHLxaA), Arize AI founder and CEO [Jason Lopatecki](https://www.linkedin.com/in/jason-lopatecki-9509941/) and Google Cloud product leader [Rami Shalom](https://www.linkedin.com/in/ramishalom/) spent time discussing how enterprise AI agents need to be monitored and improved on the road ahead. Arize’s Young referenced this session and explained that observability has already “gone through this transition once”, when teams dealt with competing tracing standards, vendor-specific SDKs, and fragmented instrumentation.

## Instrument once, route anywhere

The bottom line that’s starting to become evident here is that teams need the ability to instrument once, but route anywhere.

Founding engineer and Field CTO at cloud-native observability platform company [groundcover](https://www.groundcov), [Noam Levy](https://www.linkedin.com/in/noam-e-levy/) tells *The New Stack* that OpenTelemetry has indeed quickly become regarded as essential. But he cautions, adopting the standard doesn’t solve the harder problem: how telemetry is actually collected, normalized, and trusted at scale.

“The next question isn’t just whether teams can afford to pay SaaS vendors to store and interpret that data — it’s whether that model holds up given the volume and privacy demands of agent-driven systems,” Levy says. “And even then, OpenTelemetry alone doesn’t unify agent observability. Teams still have to reconcile fragmented telemetry across providers i..e OpenAI looks different from Anthropic, which forces them to build systems that constantly adapt to upstream changes.

Levy suggests that this is where [eBPF changes the foundation](https://thenewstack.io/research-ebpf-not-always-a-silver-bullet-for-network-apps/). By operating at the operating system level, [eBPF](https://thenewstack.io/research-ebpf-not-always-a-silver-bullet-for-network-apps/) allows teams to observe system behavior without relying on application-level instrumentation, capturing signals directly from how software actually runs rather than how it’s instrumented.

> “OpenTelemetry agent conventions are being written by ML engineers for ML engineers, but… the CISO hasn’t shown up to that conversation yet.” – David Girvin, Sumo Logic.

## Simultaneously spawning sub-agents

AI security researcher at log analytics and cloud security information & event management (SIEM) company [Sumo Logic](https://www.sumologic.com/lp/brand?igaag=140437100557&igaat=&igacm=18132769092&igacr=782768763076&igakw=sumo%20logic&igamt=e&igant=g&cq_cmp=18132769092&utm_source=google&utm_medium=paid-search&utm_campaign=Google_Search_EMEA_UK-IE_Brand_Core_All_Exact&utm_adgroup=Core&utm_term=sumo%20logic&utm_id=701VK00000KhD8BYAV&gclsrc=aw.ds&&hstk_creative=782768763076&hstk_campaign=18132769092&hstk_network=googleAds&gad_source=1&gad_campaignid=18132769092&gbraid=0AAAAADviF06i7NbW--ctkclkkasHN1aG4&gclid=CjwKCAjwntHPBhAaEiwA_Xp6RkMMuKanZ4TjfE9gI0nWLaRRVKw5uYmT5FBswLEYwk8pPb_9BNIxfhoCQqcQAvD_BwE), [David Girvin](https://www.linkedin.com/in/david-a-girvin/), tells *The New Stack* that converging on OpenTelemetry as a foundation for agent telemetry is genuinely important, but the harder problem is what teams do when that telemetry arrives into a platform at scale.

“A single agent run is a manageable transcript,” Girvin says. “A thousand agents all running across production, handing off between each other, calling external tools, hitting retrieval systems and spawning sub-agents simultaneously? That becomes a data problem.”

Advocating some wider tool democracy here, Girvin reminds us that OpenTelemetry agent conventions are being written by ML engineers for ML engineers, but, he warns, the CISO hasn’t shown up to that conversation yet. When they do, he says that teams that have instrumented purely for observability will find their telemetry doesn’t hold up for board-level investigation.

## How to question an agent

With the increasing autonomy granted to agents, we now need traces to illustrate the path followed by an agent to deliver its end output. Without this, software engineers will struggle to evaluate, debug and improve agent actions.

That means agent traces need to answer the following questions: what was the original user request and now was it transformed; which models, tools and data sources were employed; to what degree did latency, hallucination, policy failure, or bad retrieval occur; and which steps agentic code execution steps should be further analyzed for improvement?

## Standardization before agentification

In the spirit of not running before we can walk, the industry appears to be forming a solidifying consensus around the need to standardize measures of agent behavior. When those measures also include standardized methods of measurement, then we may achieve structured agent telemetry with enough semantic detail to support evaluation and agentic improvement.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)