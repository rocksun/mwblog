TOKYO — In his keynote speech at [Open Source Summit Japan](https://events.linuxfoundation.org/open-source-summit-japan/) on Monday, [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) Executive Director [Jim Zemlin](https://www.linkedin.com/in/zemlin) argued that “Artificial intelligence may not be in a full-blown bubble, but large language models [LLMs] just might be.”

Why? Zemlin started by pointing to staggering investment numbers that have dominated headlines. Morgan Stanley, he noted, estimates that [$3 trillion will be spent on AI data centers between now and 2028](https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/ai-investing-credit-markets-andrew-sheets), with hyperscalers such as [Amazon](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention), [Meta](https://about.meta.com/?utm_content=inline+mention) and [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) accounting for roughly half of that total.

“That is more investment than the GDP of many small countries,” Zemlin told the crowd, emphasizing that most businesses, and even most nations, cannot meaningfully compete in such capital-intensive infrastructure buildouts.

More crucial, he said, is the [energy demand tied to AI’s accelerating inference workloads](https://thenewstack.io/ai-consumes-lots-of-energy-can-it-ever-be-sustainable/). He cited Google’s 50 times year-over-year spike in inference volume, specifically [AI usage across Google](https://techcrunch.com/snippet/3009919/usage-of-googles-ai-is-skyrocketing/), which climbed from 9.7 trillion tokens in April 2024 to more than 480 trillion tokens in April 2025.

Moreover, he echoed AWS President [Andy Jassy’s belief](https://www.linkedin.com/in/andy-jassy-8b1615/) that [the single biggest constraint on AI growth today is power](https://www.businessinsider.com/amazon-tumbles-ceo-andy-jassy-aws-cloud-ai-growth-concerns-2025-7). Zemlin argued that the AI boom is fundamentally a story about physical infrastructure, GPUs, energy and data centers, not just algorithms, models and software.

Nevertheless, despite this hardware-heavy environment, Zemlin said the real leverage for open source lies elsewhere: in the model and software infrastructure layers.

Specifically, in the last year alone, [open-weight models](https://techcrunch.com/snippet/3009919/usage-of-googles-ai-is-skyrocketing/) emerging from China, such as [DeepSeek](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/), closed the performance gap with commercial frontier models. Zemlin added, “We’re also seeing those open-weight models being used to distill smaller industry-specific models.” For example, he pointed to [TinyLlama](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) for [Llama 3](https://www.llama.com/) and [DistilBert](https://huggingface.co/docs/transformers/en/model_doc/distilbert) for [BERT](https://huggingface.co/docs/transformers/en/model_doc/bert).

## The Economics of AI

This combination of open-weight models and distillation techniques has changed the economics of the AI sector. According to Zemlin, “Open source has largely caught up with the frontier models, the proprietary models, in the U.S. [Open-weight models](https://thenewstack.io/nathan-lamberts-atom-project-seeks-american-open-source-ai-models/) are generally three to six months behind.”

That’s more than good enough for economical AI work. Zemlin quoted the Linux Foundation’s chief economist, [Frank Nagle](https://www.linkedin.com/in/frank-nagle/), who recently quantified that mismatch. According to Zemlin, Nagel’s analysis shows that although [open models are dramatically cheaper and nearly as capable](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5767103), closed models still capture 95% of revenue, leaving an estimated $24.8 billion in annual overspending on proprietary systems.

Therefore, “I think we’re not in an AI bubble,” Zemlin said. “But we could be in an LLM bubble.”

As enterprises begin prioritizing efficient, affordable deployments, he predicted 2026 will mark “an era of performance and efficiency” dominated by open ecosystems.

## Is PARK the New LAMP Stack?

Zemlin also highlighted the emergence of what he calls the PARK stack: [PyTorch](https://thenewstack.io/why-pytorch-won/), AI, [Ray](https://github.com/ray-project/ray) and Kubernetes. ([Ray is an open source distributed computing framework](https://thenewstack.io/ray-comes-to-the-pytorch-foundation/) for simplifying scaling AI and machine learning [ML] workloads.) He believes the AI generation that will define tomorrow’s tech stack, just as the LAMP stack defined the early web era. Already, he claimed, PARK is fast becoming the default platform for AI deployment at scale.

He compared this moment to the evolution of the Linux kernel, where collective pressure from a global developer community repeatedly drove efficiency gains across diverse hardware. In AI, open source tools like [vLLM](https://docs.vllm.ai/en/latest/) and [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) are now squeezing more performance out of GPUs, cutting power usage and reducing cost per token.

“This is what open source is really good at,” Zemlin said. “Improving price-per-token and price-per-kilowatt.” It’s also where open source software helps cut the AI hardware infrastructure’s ever-growing power price tag.

Zemlin then turned toward the emerging “agentic” layer of AI, that is, systems that plan, reason and act autonomously. Zemlin described a stack still in its adolescence but rapidly formalizing around open protocols, including early deployments of [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) and [Agent2Agent (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) servers.

While only a minority of organizations are using MCP in production today, Zemlin suggested that 2026 will usher in a wave of real enterprise automation: multiagent workflows, learned orchestration, validation frameworks and new blends of deterministic and nondeterministic systems.

“Agentic AI doesn’t need to be determined by model size,” he stressed. “It’s about how you architect the solution.”

## ‘AI Hasn’t Changed All That Much Yet’

Zemlin closed his keynote by emphasizing that despite the hype, “AI hasn’t changed all that much yet.” What will change it, he argued, is open collaboration.

Open source, he said, prevents vendor lock-in, improves trust and transparency, and provides “universal connectors” for the coming era of interoperable AI systems. From training to inference to orchestration, he said, the Linux Foundation intends to serve as a central hub for that work alongside global research labs and industry partners.

“We’re really, really excited to be a small part of this world,” he said, promising major announcements still to come.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)