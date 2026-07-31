**OpenAI has detailed, in a new engineering blog post**, how the [GPT-5.6](https://thenewstack.io/openai-gpt-56-live/) model family balances capability and cost across its stack. The most important claim is a benchmark result in which the company reports that its flagship model, GPT-5.6 Sol, with maximum reasoning, outperforms Claude Fable 5 from Anthropic on the [Artificial Analysis](https://artificialanalysis.ai/) Coding Agent Index. The margin comes with 54% fewer output tokens.

For developers, what matters most is how OpenAI arrived at the benchmark results and the role GPT-5.6 Sol played in optimizing the infrastructure that now serves it.

The family spans three models across the price curve. In addition to Sol, there is Terra, which performs as well as GPT-5.5 on intelligence benchmarks at half the price, and Luna, the fastest and most affordable, which is priced 80% below Sol.

> The efficiencies come from optimizations at four layers, spanning the models, inference, the API stack, and the agentic harness behind Codex and ChatGPT Work.

According to the post reviewed by *The New Stack* ahead of its publication, the efficiencies come from optimizations across four layers: models, inference, the API stack, and the agentic harness behind [Codex](https://openai.com/codex/) and [ChatGPT Work](https://chatgpt.com/work/). The architecture diagrams in the post draw the same separation as three planes: the local harness, CPU-bound API orchestration, and GPU-bound model inference.

![](https://cdn.thenewstack.io/media/2026/07/6954702a-openai-efficiency-1024x814.jpg)

*Source: OpenAI*

For developers building and operating agents, the post is worth reading less as a product announcement and more as a systems paper. Nearly every technique it describes, from incremental tokenization to append-only context, applies to any team running a tool-calling loop at scale.

## A model that rewrites its own serving code

The efficiency work starts in training. OpenAI says GPT-5.6 is trained to achieve more work per token, with training optimized for both task success and efficiency so the model takes a more direct path through a task.

With Codex, GPT-5.6 Sol autonomously rewrote and optimized OpenAI’s production kernels, the core code that executes the mathematical operations making up the model. OpenAI says this worked in part because GPT-5.6 is trained to write and improve kernels in [Triton](https://github.com/triton-lang/triton) and [Gluon](https://github.com/triton-lang/triton/tree/main/python/tutorials/gluon). Both are open-source GPU programming languages maintained by OpenAI. These efforts, combined with broader kernel advancements from the model, reduced end-to-end serving costs by 20%.

Correctness is the obvious concern when a model rewrites the code it runs on. To address it, OpenAI reports heavy investment in verification tooling. That includes the open-source Floating-Point Sanitizer (FpSan), which validates the kernels GPT-5.6 Sol produces before they reach production.

The model went further with speculative decoding, a technique in which a smaller draft model proposes several tokens that the primary model verifies in parallel. The approach will feel familiar to anyone who understands how modern CPUs speculatively execute instructions ahead of a branch. Accepted proposals produce multiple output tokens from a single pass of the primary model. That reduces the expensive sequential computation the primary model would otherwise perform.

GPT-5.6 Sol in Codex improved its own draft model by designing and running hundreds of experiments on its architecture, with changes tested across size, structure, and features. The model also launched and monitored the speculative training process. It intervened autonomously when hardware failed or training became unstable. OpenAI reports the resulting improvements lifted token-generation efficiency by more than 15%.

## More tokens from the same GPUs

OpenAI frames its inference work around a single objective – serving more tokens with the same hardware while preserving the intelligence, latency, availability, and reliability users expect. In a compute-constrained market where demand grows faster than capacity, that objective influences every design decision in the serving path.

Load balancing operates at three distinct levels. Globally, requests are routed based on geography, available capacity, and accelerator type. Within a cluster, work is distributed across model instances based on load, context length, and cache availability. Within each instance, work is partitioned across accelerators, the model’s experts, and computing cores. GPT-5.6 Sol in Codex helps OpenAI analyze production traffic and identify previously overlooked sources of imbalance. The same loop tests new routing strategies and helps engineers constantly tune the heuristics. OpenAI states that these load-balancing improvements alone dramatically reduced the cost of serving its models.

The key-value (KV) cache received the same treatment. When processing uncached input tokens, the model builds the KV cache in a single compute-intensive pass, then repeatedly reads from and extends it during generation. The optimal serving configuration depends heavily on prompt length, batch size, and cache hit rate. It covers batching, sharding, and cache management, and the configuration space was previously too large to tune systematically. With GPT-5.6 Sol in Codex, OpenAI analyzed production workloads and generated candidate configurations. The company says this makes workload-specific optimization practical at a level that broad heuristics could not reach earlier.

## Process only what changed

The API team focuses on everything that happens around a model call. After a prompt is submitted, the API stack receives the request, loads context, and validates the input. Safety checks run next, and the text is converted into tokens for inference. OpenAI measures this overhead through time to first token (TTFT), time between tokens (TBT), and end-to-end time (E2E).

Tokenization is an O(n) operation, so longer prompts take longer to process. Codex would send the full conversation context after every tool call. That meant paying to tokenize the same conversation dozens of times per turn, even though only a small amount of context was new in each request. OpenAI solved this with a WebSocket integration that hoists tokenization state to the server. The first call renders and tokenizes the full prompt. Later calls send only the new input with a reference to the conversation, bringing the operation closer to O(1). The pattern mirrors an incremental build system that recompiles only the files that changed rather than the whole project.

These savings compound in tool-heavy workflows, where every tool result triggers another round trip through the API. For rollouts with 20 or more tool calls, OpenAI reports up to roughly 40% faster end-to-end execution.

Hardware turned out to matter as much as protocol design. All of OpenAI’s infrastructure runs on [Kubernetes](https://kubernetes.io/). The company found that nodes with the same instance type often carried different CPU generations, with many running outdated processors. In its measurements, the older processors consumed roughly twice the CPU resources for the same work. Reweighting traffic toward newer processors improved TTFT by about 20%, and CPU generation is now part of capacity planning.

OpenAI names four fates for application-layer overhead: delete it, overlap it with useful work, run it on faster hardware, or make the code consume fewer CPU cycles. Its asyncio changes move work off the critical path, while newer hardware and Rust implementations make the remaining work faster and more predictable.

## An append-only harness

The agentic harness is a Rust-based orchestration layer that connects the models, tools, and the user’s environment. In a single turn, Codex might inspect source code, search deployment history, and read incident reports. Editing a file and running the tests each add another request. Since a task can require 30 model requests, an extra second per request adds up quickly.

Context bloat is the first target for the harness. As agents gain access to more tools, skills, plugins, and conversation history, context windows expand. The growth increases cost, distracts the model, and prompts unnecessary reasoning. The harness counters this with deferred discovery, which surfaces integrations, custom [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) tools, skills, and plugins only when needed. Tool output is capped at 10,000 tokens by default unless the model requests a different limit.

Prompt caching drives the second design choice. An agent loop resends the same instructions, tool definitions, and earlier results multiple times within a turn. The harness therefore treats all model-visible history as append-only, with new messages and tool results added at the end rather than inserted into earlier context. Tools are presented in a deterministic order, and runtime settings, such as approval policies, are applied during execution rather than embedded in tool definitions. OpenAI credits this design for the high prompt-cache hit rates in Codex and ChatGPT Work.

![](https://cdn.thenewstack.io/media/2026/07/3bdf587c-context-append-1024x606.jpg)

Source: OpenAI

Platform teams building internal agents can adopt every one of these choices without OpenAI’s scale. Append-only context, deterministic tool ordering, and capped tool output attack token spend directly. That makes them the most portable lessons in the post for enterprises watching inference bills grow with each new agent deployment.

## Where the gains come from

The post associates a number with most of its optimizations, and the figures are OpenAI’s own production measurements. Taken together, they show how modest individual wins compound across a serving stack.

| Layer | Technique | Claimed gain |
| --- | --- | --- |
| Model inference | Autonomous kernel rewrites in Triton and Gluon | 20% lower end-to-end serving costs |
| Model inference | Speculative decoding with a self-improved draft model | Over 15% better token-generation efficiency |
| API stack | Stateful WebSockets with incremental tokenization | Up to roughly 40% faster runs at 20+ tool calls |
| API stack | Routing traffic toward newer CPU generations | About 20% better time to first token |
| Agent harness | Deferred discovery and a 10,000-token tool output cap | Reduced context bloat and cost |

## The key takeaways

In summary, OpenAI describes the GPT-5.6 efficiency gains as the result of years of compounding improvements. They span research, inference, the API stack, and the agentic harness. The company states that the model’s role in landing many of them makes it optimistic that the pace of optimization will accelerate. Kernel work is called out as an area of continued investment.

The post positions efficiency, alongside raw intelligence, as the axis on which frontier labs now compete. The claimed 54% output-token advantage over Claude Fable 5 shows how OpenAI intends to fight that battle. The engineering blog makes a plausible case that software optimization is becoming an important lever alongside hardware improvements in reducing the cost of serving frontier models. The figures remain OpenAI’s own production measurements. The autonomy on display operates within Codex, with engineers in the loop. Developers and enterprises benefit either way, as these under-the-hood improvements reach them as more capable models at lower prices across the cost-intelligence curve.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)