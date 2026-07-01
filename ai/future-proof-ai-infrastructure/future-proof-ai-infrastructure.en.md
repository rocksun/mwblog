For two years, the AI infrastructure race has been dominated by one question: Who has the fastest GPU? Jim Keller thinks that’s becoming the wrong question.

In a [recent interview with *EE Times*](https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions), the Tenstorrent CEO argues that the riskiest move an organization can make right now is optimizing its AI infrastructure for the models it’s running today. It’s not because those models are bad — but because they won’t be the models it’s running in 18 months. [Keller](https://www.linkedin.com/in/jimbkeller/) invoked Rent’s Rule and Amdahl’s Law to argue that memory, networking, and system-level balance now matter more than peak floating-point performance.

> Not because those models are bad — but because they won’t be the models it’s running in 18 months.

It sounds like the start of Keller’s product pitch, but there’s real weight behind it, because AI has evolved faster than the infrastructure underneath it. And the companies that spent hundreds of millions building around one generation of models are now staring down the cost of doing it all over again.

That fear is called lock-in, and it’s reshaping how the biggest players in AI think about hardware.

## Workloads outgrew the GPU

In 2023 and 2024, AI infrastructure was a relatively simple procurement problem: Train large language models, serve them to users, and buy as many GPUs as Nvidia can ship. The workloads were predictable and GPUs handled them well.

Then AI outgrew the infrastructure it had been built for.

Reasoning models spend more time working through problems instead of jumping straight to an answer. Agents bounce between APIs, databases and code before completing a task. Multimodal models mix text with images, audio and video. None of those workloads stress hardware in quite the same way — and that’s forcing infrastructure teams to rethink assumptions that made perfect sense just two years ago.

> AI outgrew the infrastructure it had been built for.

No single chip architecture handles all of that equally well. And the organizations building AI infrastructure are starting to realize that the question isn’t just *which accelerator is fastest* — it’s *how do we build systems that won’t need to be torn apart every time AI takes another leap?*

## Nvidia is already selling one answer

Look at what Jensen Huang has been talking about, and it’s not GPUs anymore.

At GTC 2026, Nvidia [unveiled the Vera Rubin platform](https://nvidianews.nvidia.com/news/nvidia-vera-rubin-platform) — seven chips designed to operate as a single system: the Rubin GPU, Vera CPU, NVLink 6 switch, ConnectX-9 networking, BlueField-4 DPU, and more. The Vera CPU exists

for the CPU-intensive work of agentic AI — tool calls, code execution, orchestration. Nvidia calls these deployments “AI factories,” and the language is deliberate. They’re selling complete infrastructure, not individual accelerators.

When the company with 70% market share stops leading with GPU benchmarks and starts talking about system-level co-design, it tells you where the center of gravity in this market is moving.

That reframing matters. When the company with 70% market share stops leading with GPU benchmarks and starts talking about system-level co-design, it tells you where the center of gravity in this market is moving. Compute still matters. But Nvidia is conceding — through its product architecture if not its marketing — that raw accelerator performance alone won’t be enough for what’s coming.

## Hyperscalers design their own silicon

AMD sees the same problem, even if it’s taking a different route. [Helios](https://www.amd.com/en/newsroom/press-releases/2026-1-5-amd-and-its-partners-share-their-vision-for-ai-ev.html) brings together CPUs, GPUs and networking into one rack-scale platform, reflecting a broader shift away from treating the GPU as the center of the universe. The pitch isn’t “our accelerator is faster.” It’s that the infrastructure surrounding the chip increasingly matters just as much as the chip itself.

The hyperscalers have been making this argument with their wallets for even longer. Google has spent a decade co-designing its [TPU silicon, interconnects and software framework](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/) — its seventh-generation Ironwood chip is now generally available — giving it unusual control over the full stack. Amazon went the opposite direction, building [separate chips for separate jobs](https://aws.amazon.com/ai/machine-learning/trainium/): Trainium for training, Inferentia for inference, with Trainium3 now in production and serving customers like Anthropic. Microsoft’s [Maia 200](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/) targets inference costs, while the company simultaneously deploys Nvidia’s Vera Rubin NVL72 for training and experimentation — arguably the most pragmatic dual-track strategy in the market.

Behind all of them sits Broadcom, whose AI semiconductor revenue recently crossed [$10 billion in a single quarter](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-first-quarter-fiscal-year-2026-financial), driven by staggering demand for custom accelerators and data center switches. Broadcom designs custom accelerators for Google, Meta and others while supplying the Tomahawk and Jericho switch silicon that connects those accelerators at data center scale. Custom ASIC shipments are projected to grow roughly 45% year over year in 2026 — triple the growth rate of merchant GPUs.

Then there are the companies that decided building a better GPU wasn’t the answer.

Cerebras questioned the need for thousands of interconnected chips, opting instead for a wafer-scale processor that keeps far more of the workload on a single piece of silicon. Groq took the opposite approach, optimizing almost entirely for inference. SambaNova focused on enterprise AI, building systems where efficiently serving multiple models matters more than posting the fastest benchmark.

## Adaptability beats raw speed

The first wave of generative AI rewarded whoever could buy the most compute. That made sense when most organizations were solving the same problem. Today, AI workloads are changing so quickly that infrastructure teams are starting to optimize for something different: adaptability.

Keller’s example illustrates the point. Tenstorrent’s BlackHole architecture uses standard Ethernet instead of proprietary interconnects, allowing its hardware to slot alongside existing GPU deployments rather than replacing them. Keller told [EE Times](https://www.eetimes.com/jim-keller-on-tenstorrents-blackhole-scaling-and-ipo-ambitions) that one customer used Tenstorrent’s Galaxy servers to increase token throughput on GPUs they already owned instead of rebuilding their infrastructure from scratch.

Whether Tenstorrent’s approach becomes the industry standard is almost beside the point.

The bigger idea is already spreading. Across the industry, companies are spending less time asking how to build the fastest AI hardware and more time asking how to build hardware that won’t have to be replaced every time AI takes another leap forward.

## The question that matters now

No one knows what AI workloads will look like three or five years from now. That’s the problem.

Infrastructure refresh cycles are measured in years. AI models seem to reinvent themselves every few months. Building around today’s workloads is starting to look like a risky bet when tomorrow’s could demand something different.

> Infrastructure refresh cycles are measured in years. AI models seem to reinvent themselves every few months.

Every company is responding in its own way. They have different strategies but are still asking the same question: **How do you build infrastructure that outlasts the AI running on it?**

That may prove to be a more important engineering challenge than building the next record-breaking accelerator. And it’s the challenge driving companies from Nvidia and AMD to Google, Amazon, Broadcom and Tenstorrent.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)