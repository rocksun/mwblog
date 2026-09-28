New models are coming out thick and fast, almost on a weekly cadence, ranging from the powerful proprietary systems coming out of the major US AI labs to the more open alternatives being released by some of China’s biggest tech companies.

On Tuesday alone, [Anthropic debuted Claude Opus 5.5](https://thenewstack.io/claude-opus-5-5-lifecycle/), while [OpenAI launched GPT-6 Sol and Luna](https://thenewstack.io/gpt-sol-alignment-gaps/), each accompanied by their the usual claims about how they outperform their rivals. Amidst all the hullabaloo of the frontier-model frenzy, however, [Xiaomi also debuted MiMo-V2.6](https://mimo.xiaomi.com/mimo-v2-6), another powerful open model from one of China’s growing ranks of AI developers.

All the initial headline numbers look pretty promising, too. The flagship [MiMo-V2.6-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL) is a trillion-parameter model, with 42 billion parameters active at a time, a one-million-token context window, and support for text, images, audio and video. Broadly speaking, that puts it in the same frontier territory as the latest models from OpenAI and Anthropic: GPT-6 Sol has a 1.05-million-token context window, while Claude Opus 5.5 has a one-million-token window, though neither company discloses comparable parameter counts.

Xiaomi, for its part, makes broad claims of frontier-level performance across coding, agentic tasks, cybersecurity, multimodal work and research. Independent analysis lends some weight to those claims –Artificial Analysis [gives MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) an Intelligence Index score of 46, ranking it first among the 114 large open-weight models it tracks.

![Artificial Analysis  Intelligence Index](https://cdn.thenewstack.io/media/2026/09/b019f9a5-screenshot-2026-09-23-at-15-27-41-mimo-v2.6-pro-intelligence-performance-price-analysis-artificial-analysis.png)

*Artificial Analysis Intelligence Index*

So far, so good. But arguably the bigger story in Xiaomi’s offering is the manner in which it trained the model, how much of that process it showed in public, and what it’s releasing afterward.

## A public record

Xiaomi [livestreamed its RL training](https://mimo.xiaomi.com/rl/) through a public dashboard, exposing metrics from the production reinforcement-learning runs in real time over a five-day period starting on September 15. By the time the runs had finished, the dashboard showed costs of $854,044 for the smaller [MiMo-V2.6-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL) model and $2,620,670 for Pro — about $3.5 million combined.

![Xiaomi livestreamed its RL runs over a 5-day period.](https://cdn.thenewstack.io/media/2026/09/6fbce13b-livestreamdata-1024x401.png)

*Xiaomi livestreamed its RL runs over a 5-day period.*

It’s worth noting that this figure covers only the RL stage; Xiaomi hasn’t said what pretraining the models cost. Even so, public RL bills are rare. The closest precedents came last year, when MiniMax said the RL phase of its 456-billion-parameter [MiniMax-M1 cost](https://www.minimax.io/news/minimaxm1) $534,700 in GPU rental, and DeepSeek put the RL training of its 671-billion-parameter R1 [at $294,000](https://www.theregister.com/software/2025/09/19/deepseek-didnt-really-train-its-flagship-model-for-294000/1025726). Both were leading open reasoning models when they launched, though the comparison only goes so far: MiMo-V2.6-Pro is larger, and its RL run targeted longer, agentic tasks.

Shortly after the stream began, [Fuli Luo](https://x.com/_LuoFuli), who leads Xiaomi’s MiMo team after previously working at DeepSeek, [took to X](https://x.com/_LuoFuli/status/2100296686719610932) to explain the thinking behind the project. The team, she said, had spent almost six months exploring how far RL could be pushed, increasing the amount of training, the variety of environments and agent setups, and the resources used to grade the model’s attempts.

“We’ll open-source the details piece by piece over the coming weeks,” she added.

Responding on X, Hugging Face co-founder and chief science officer [Thomas Wolf](https://www.linkedin.com/in/thom-wolf) called [the move](https://x.com/Thom_Wolf/status/2100581195255775636) an “Impressive level of openness on such a large run.”

However, what Xiaomi’s putting out alongside the finished models is arguably just as interesting. The company has released the model weights under the permissive MIT license, alongside its [technical report](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf) and a [9-billion-parameter Qwen-based model](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B), intended as a starting point for further agentic RL research.

> “Impressive level of openness on such a large run.”

Xiaomi says it has also “fully open-sourced” a broader set of RL resources: more than 7,000 task environments spanning software engineering, vulnerability reproduction, knowledge work and web development; an end-to-end training framework covering everything from environment interaction to reward evaluation and policy optimization; and lightweight agent harnesses for experimenting with different tools, prompts and context setups. At the time of writing, however, Xiaomi’s [link to the open-source collection on Hugging Face](https://huggingface.co/collections/XiaomiMiMo/mimo-v26) contain only the three model releases, with the 7,000-plus environments and other supporting resources not surfaced there. Luo had said earlier that Xiaomi would be open-sourcing the various elements “over the coming weeks.”

As the [results began arriving this week](https://x.com/ArtificialAnlys/status/2102128560962187701), attention in the research community quickly moved beyond the benchmark score to what Xiaomi had committed to releasing overall. [Elie Bakouch](https://www.linkedin.com/in/eliebak/), a former Hugging Face researcher who is now a research engineer at Prime Intellect, singled out the promised RL resources.

“The most insane part, they will release ~7k RL training data and the framework leading to this top 6 model on AA,” Bakouch [writes on X](https://x.com/eliebakouch/status/2102136275708879078). “They also shipped the model + tech report less than 1 week after starting the final RL run.”

Wolf went further, arguing that access to the environments in which models learn may now be especially valuable for open research, as more model development shifts toward RL with verifiable rewards ([RLVR](https://www.promptfoo.dev/blog/rlvr-explained/)). Because RLVR depends on tasks whose outcomes can be automatically checked — whether code passes a test, for example — the environments themselves become a crucial ingredient in training.

> “Releasing many high quality open-source RL environments is the most impactful thing anyone can do to push the open-source frontier right now.”

“Releasing many high quality open-source RL environments is the most impactful thing anyone can do to push the open-source frontier right now,” Wolf [writes](https://x.com/Thom_Wolf/status/2102137611011674173). “The equivalent of sharing high quality pretraining data, but in the new RLVR paradigm.”

## Open-weight vs open-source

So while the benchmarks around Xiaomi’s latest model are notable in their own right, it’s the company’s approach that is generating much of the fanfare so far.

Indeed, MiMo-V2.6 serves as a useful example of a distinction that [often gets muddied in the AI sphere](https://techcrunch.com/2024/06/22/what-does-open-source-ai-mean-anyway/): “open-weight” and “open-source” are routinely used as though they mean the same thing, but they don’t. Many “open” models amount largely to downloadable weights — essentially, the vast collection of numerical values a model learned during training, which can then be used to run or fine-tune it — while much of what went into producing them remains closed.

Some companies have gone further in muddying those terms. Meta, for example, has often referred to its Llama models as open-source [despite significant restrictions](https://www.forkable.io/p/metas-new-llama-4-ai-models-arent) that have [led open-source advocates](https://opensource.org/blog/metas-llama-license-is-still-not-open-source) to push back heavily on that description.

And so MiMo-V2.6 goes further than most open-source releases. Its MIT license carries none of the conditions that the likes of [Moonshot’s Kimi K3](https://pub.towardsai.net/is-kimi-k3-free-to-use-commercially-the-license-decoded-204896e1ecd5?gi=3e26d880934b) and [Alibaba’s Qwen3.8-Max](https://www.scmp.com/tech/tech-trends/article/3363927/alibaba-adds-commercial-restrictions-open-weight-qwen38-max-ai-model) attach for large commercial users. And if the environments are released as promised, outside researchers will have much more of the post-training process to inspect and build on.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)