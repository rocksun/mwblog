The shiny upper surface of agentic AI services showcased in chatbots and copilots belies where the real development is happening right now. Spoiler alert: it’s AI infrastructure. Foundation data services company MinIO launched a new context memory store this Tuesday, known as MemKV, to tackle a deeply rooted challenge in the AI base layer.

Central to an AI model’s operation, a context memory store is a software-based tier of architectural logic built to retain situational data pertaining to model tasks, user preferences, and interactions.

## TTFT (Time to First Token)

This is the stuff of four-letter acronyms. MinIO calls out its technology’s ability to improve both TTFT (Time to First Token) and TPOT (Time Per Output Token) in AI inference workloads. MemKV achieves new speeds in this realm by providing petabyte-scale, native flash-based context memory accessed end-to-end over 800 Gigabit Ethernet Remote Direct Memory Access ([GbE RDMA](https://www.nas.nasa.gov/assets/nas/pdf/papers/NAS_Technical_Report_NAS-2014-01.pdf)).

MemKV joins AIStor as the second pillar of MinIO’s data foundation product portfolio. AIStor is a software-defined object storage platform built for the AI era. The new MinIO MemKV product delivers persistent, shared context across GPU clusters at a scale that the company has claimed existing memory and storage tiers cannot.

## What is recompute tax?

As AI starts to perform complex [multi-step reasoning tasks](https://thenewstack.io/system-two-ai-the-dawn-of-reasoning-agents-in-business/), memory (or, as the AI industry now likes to call it, [context](https://www.developerway.com/posts/how-ai-remembers-and-forgets-part1)) is routinely lost because the infrastructure closest to the GPU cannot hold enough of it. When context is lost, the GPU repeats work it has already completed, and we call that “recompute tax”, which is clearly a drain on time, energy, and resources.

> “Any [GPU performing recompute actions](https://thenewstack.io/gpu-orchestration-in-kubernetes-device-plugin-or-gpu-operator/) is not an inefficiency, it is ‘structural drag’ that the industry can not sustain given the GPU density that hyperscalers and neoclouds are building towards.” – MinIO co-founder and CEO, AB Periasamy.

Put in direct terms, MinIO claims that MemKV “dramatically reduces” the recompute tax for AI inference workloads. On representative benchmarks published on the [company’s blog](https://www.min.io/blog), MemKV delivered an improvement in time-to-first-token at production concurrency. Top line numbers include 95%+ better GPU utilization and around 50% lower cost per token.

[AB Periasamy](https://www.linkedin.com/in/abperiasamy/), co-founder and CEO of MinIO, has said that any GPU performing recompute actions is not an inefficiency, “it is structural drag” that the industry can not sustain given the GPU density that hyperscalers and neoclouds are building towards.

## A new blend of tokenomics

[Don Gentile](https://www.linkedin.com/in/dongentile/), analyst at HyperFRAME Research, has called for the AI conversation to move on from raw model performance to token economics and the cost of operating AI at scale.

“That [shift onwards] is driving new focus on how systems retain and share context during inference,” said Gentile. “MinIO’s MemKV addresses a costly inefficiency: rerunning prior calculations when context cannot be shared across GPUs. Eliminating that friction improves utilization and lowers the cost of enterprise AI.”

Diving deeper then, with microsecond retrieval at petascale now available, how should software engineers rethink state management for globally distributed GPU clusters? MinIO CTO, [Ugur Tigli](https://www.linkedin.com/in/ugur-tigli-9a9323/), tells *The New Stack* that developers should really “stop treating context like throwaway scratch” and start treating it like real state, more along the lines of persistent storage.

## Welcome to context‑as‑a‑service

“With MemKV, context becomes a durable, addressable state you can save, share, and reload – closer to a database row or an object than a cache entry,” Tigli says. “Think of it like a mental model providing context‑as‑a‑service: one shared brain that every inference replica, every agent, and even every tenant reads from – instead of each one rebuilding the same context from scratch on every call.”

In operational terms for software developers, Tigli explains that three things change in practice.

Developers can make the serving layer stateless and put the session and agent state into MemKV instead of pinning it to a single GPU. Any replica can then pick up any conversation mid‑flight and the scheduler routes to whichever GPU is free, so that the GPU pulls the cached context out of MemKV in microseconds. There are no sticky sessions, no replica affinity, and no thread loss when a pod restarts.

## Don’t boil the context ocean

Developers can deploy per region, not globally; they don’t have to try to mirror every byte of context across continents. They can deploy a MemKV instance locally on each GPU cluster.

“Don’t think of MemKV like persistent storage that needs to be replicated, treat geographic placement as a performance choice, not a correctness one,” says Tigli.

> “Developers no longer need to architect around cache eviction – context is durably offloaded and retrievable in microseconds, not milliseconds.” –  MinIO CTO, Ugur Tigli,

Thirdly, he explains that teams can be explicit about what stays and what goes. This means software engineers can pin the keys for active sessions so they don’t get evicted under load. They can also cache popular prefixes (long system prompts, frequently retrieved RAG passages) separately from per‑user state, so a single chatty user can’t push the shared assets out.

“All this means that, in the developer’s inference workflow, the recompute tax disappears,” says Tigli. “With file-based storage, when GPU memory runs out of key value (KV) cache, the context is either evicted or has to be recomputed – a specialized KV store eliminates that. Developers no longer need to architect around cache eviction – context is durably offloaded and retrievable in microseconds, not milliseconds.”

## Deeper into safer data layers?

As we push the agentic AI development conversation downward through the infrastructure layer, a new responsibility for robustness also comes to the fore.

[Karthik Swarnam](https://www.linkedin.com/in/kswarnam/), chief security and trust officer at exposure management platform company [ArmorCode](https://www.armorcode.com/), tells *The New Stack* that the need for context memory stores for AI inference represents another major enterprise challenge around the continuity of trust in AI.

“It is not enough to secure the model itself. Organizations will also need to secure the memory layer that determines what context an AI system retains, recalls, and acts upon over time,” Swarnam says. “As these systems become more persistent and interconnected, the attack surface expands beyond prompts into contextual data that could be manipulated, poisoned, or exposed in ways that are difficult to detect.”

From a security posture perspective, Swarnam says this reality raises important questions about provenance, access control, retention policies, and whether enterprises can reliably trace how AI decisions were influenced over time. He suggests that the industry is starting to recognize that memory infrastructure is becoming just as critical to AI governance and security as the models themselves.

## Catch the Non-Volatile Memory Express

Unlike approaches that retrofit file-storage architectures into the inference data path, MemK moves data directly from Non-Volatile Memory Express (NVMe) to the AI data path via end-to-end RDMA transport, with no HTTP overhead, no file system translation, and no storage servers between the GPU and its context.

The bottom line from CEO Periasamy and CTO Tigli is that the yield economics of token use at the scale required for today’s agentic functions demand something purpose-built for the inference data path. This, say the pair, is why MemKV was designed and built.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)