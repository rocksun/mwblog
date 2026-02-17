OpenAI’s new [GPT-5.3-Codex-Spark](https://openai.com/index/introducing-gpt-5-3-codex-spark/) model is a bit of a departure for the company’s family of Codex software development models: its focus is squarely on reducing latency.

Powered by Cerebras’ 125-petaflop [Wafer Scale Engine 3](https://www.cerebras.ai/chip), the Codex Spark model is meant for use cases where latency matters as much — or more — than intelligence. And fast it is: Codex Spark can deliver [more than 1,000 tokens per second](https://www.cerebras.ai/blog/openai-codexspark).

When OpenAI launched GPT-5.3-Codex only a few days ago, it highlighted how the team was able to bring down latency by 25 percent. However, whereas that model excels at long-running coding and agentic tasks, where latency is less important, Codex Spark is designed for rapid prototyping and obtaining answers quickly.

The core idea here is to have two models that are complementary: a fast one for real-time collaboration and a slower one for long-running tasks where deeper reasoning is called for.

OpenAI notes that its new model is best suited for making small, very targeted edits to code. An additional benefit of the speed, though, is that the model can be easily interrupted and redirected, helping developers iterate quickly.

However, since it’s optimized for this use case, it will also only feature a 128,000-token context window at launch. It is also text-only. Over time, the team plans to add additional capabilities to this faster model family, including larger models, longer context lengths, and multimodal inputs.

## Benchmarks

The company admits that the new model will underperform GPT-5.3-Codex, “but can accomplish the tasks in a fraction of the time.”

On the standard SWE-Bench Pro benchmark, Codex Spark indeed scores significantly lower than GPT-5.3-Codex, but it does get to usable results much faster, which may just be enough for many use cases.

![](https://cdn.thenewstack.io/media/2026/02/905a1e10-swe-bench-pro.png)

Credit: OpenAI.

On Terminal-Bench 2.0, which looks at how well the model performs at agentic workflows in the terminal, it also scores significantly lower than the larger GPT-5.3-Codex (58.4% vs 77.3%).

## Availability

The GPT-5.3-Codex-Spark tier is now available as a research preview for ChatGPT Pro users in the CLI, VS Code and the [Codex app](https://thenewstack.io/openais-codex-desktop-app-is-all-about-managing-agents/) (which has now been downloaded more than 1 million times). A select number of OpenAI partners will also get early access to Codex Spark in the API.

OpenAI notes that capacity for the new Codex Spark model may be constrained, with slower access and temporary queuing. The model will have its own rate limits, and using it will not count toward the company’s regular rate limits.

Since it’s not available in the API yet, OpenAI has not published any pricing information.

## Why OpenAI opted for Cerebras’ wafer-scale AI accelerators

Using different model tiers is not exactly a new idea, of course. Anthropic, with its three tiers of models (Haiku, Sonnet, and Opus), and others have long used a similar approach of offering models that are mostly differentiated by their intelligence, speed, and pricing. OpenAI itself has long offered [nano](https://developers.openai.com/api/docs/models/gpt-5-nano) versions of its models.

The major difference here is that OpenAI is also using a very different hardware platform for this new model.

It’s no coincidence that OpenAI chose to run this model on Cerebras’ hardware. Early in 2026, the two companies announced a multi-year partnership agreement that is reportedly [worth up to $10 billion](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html). Under this agreement, Cerebras will build and host data centers that will deliver 750 megawatts of capacity to run its wafer-scale chips for OpenAI.

Cerebras’ chips are gigantic when compared with most standard GPUs and AI accelerators. NVIDIA’s flagship Blackwell B200 accelerator features 208 billion transistors. Cerebras’ chip features four trillion, spread between almost 900,000 cores.

But it’s not just the pure computing power. At this point, the real bottleneck for inference isn’t compute but [memory bandwidth](https://thenewstack.io/why-d-matrix-bets-on-in-memory-compute-to-break-the-ai-inference-bottleneck/). Cerebras promises to do away with this bottleneck by using on-chip memory and up to 27 petabytes per second of internal bandwidth.

In its announcement, OpenAI stresses that GPUs remain foundational for its training and inference pipelines. But the company also notes that “Cerebras complements that foundation by excelling at workflows that demand extremely low latency, tightening the end-to-end loop so Codex feels more responsive as you iterate.”

As [Sean Lie](https://www.linkedin.com/in/sean-lie-4a80097/), the CTO and co-founder of Cerebras, puts it: “What excites us most about GPT-5.3-Codex Spark is partnering with OpenAI and the developer community to discover what fast inference makes possible — new interaction patterns, new use cases, and a fundamentally different model experience. This preview is just the beginning.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)