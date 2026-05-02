Meta’s decided its new proprietary AI LLM, Muse Spark, would be much more profitable than the open-source Llama. What are Llama users to do?

Back in 2023, [Meta released Llama 2.0 and proclaimed it to be open source.](https://thenewstack.io/metas-llama-2-is-not-open-source-and-thats-ok/) Even if [Llama wasn’t actually open source](https://thenewstack.io/open-source-ai-and-the-llama-2-kerfuffle/), it sounded good to developers.

Indeed, in October 2024, Meta founder and CEO Mark Zuckerberg proclaimed, “[Open Source AI is the Path Forward.](https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/)” In March of last year, the company issued a press release [celebrating](https://about.fb.com/news/2025/03/celebrating-1-billion-downloads-llama/) 1 billion downloads of Llama.

That was then. This is now.

For all practical purposes, Meta has abandoned developing Llama in favor of its new proprietary program, [Muse Spark](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/), announced this month. Meta Superintelligence Labs — a new division formed in 2025 after Zuckerberg recruited Scale AI’s Alexandr Wang to jump-start Meta’s AI efforts — developed the model.

Zuckerberg was [reportedly](https://www.bloomberg.com/news/articles/2025-06-10/zuckerberg-recruits-new-superintelligence-ai-group-at-meta) unhappy with how Llama models lagged behind ChatGPT and Claude, and so Muse Spark was built from scratch with entirely new infrastructure, architecture, and data pipelines. The company also went on a “[blockbuster spending spree](https://www.wsj.com/tech/ai/meta-ai-hiring-freeze-fda6b3c4)” to poach AI talent from the competition. Muse Spark is in no way, shape, or form a child of Llama.

We don’t know exactly why Meta dropped Llama from its priority list, as the company hasn’t addressed it. When *The New Stack* asked Meta about Llama and Muse Spark, the company didn’t respond.

![](https://cdn.thenewstack.io/media/2026/04/b1ac3a12-04_search.gif)

*A screenshot showing Meta’s Muse Spark* *AI.*

What we can see, though, from what Meta has said publicly, is that while it states that “current Llama models will continue to be available as open source,” this only confirms that existing models will remain available and says nothing about future development. The expectation within the AI community is that [Llama will receive incremental updates and maintenance](https://miraflow.ai/blog/meta-ended-llama-built-muse-spark-changes-everything-2026). You can forget about it receiving Muse Spark’s massive frontier investment.

> There is no migration path from Llama to Muse Spark because they have fundamentally different deployment models.

## No clear migration path

What does this mean for current Llama users? They’re in trouble. There is no migration path from Llama to Muse Spark because they have fundamentally different deployment models. Llama offers downloadable open weights for self-hosting and fine-tuning, while Muse Spark is cloud-only with no downloadable weights, no self-hosting capability, and currently only private API preview access. Even if [Meta keeps its promise to open-source some of its newer models](https://thenewstack.io/meta-open-source-models/), it’s hard to imagine how Llama users could migrate to these platforms.

As [Andrew Ng](https://www.linkedin.com/in/andrewyng) writes in *[The Batch](https://www.deeplearning.ai/the-batch/issue-349/#:~:text=The%20proprietary%20release%20has%20raised%20concerns%20among%20developers%2C%20many%20of%20whom%20have%20built%20projects%20on%20open%2Dweights%20Llama%20models.)*, his AI newsletter, “The proprietary release has raised concerns among developers, many of whom have built projects on open-weights Llama models.” At the same time, Ng writes, Meta’s shift may help it “to compete for business customers alongside OpenAI, Google, and Anthropic. However, its pivot away from being the leading U.S. champion of open weights is a significant loss for the developer community.”

> Meta’s move away from being the leading U.S. champion of open weights is a significant loss for the developer community.

This isn’t, by the way, a small number of developers. A year ago, Meta reported that [Llama had been downloaded 1.2 billion times.](https://finance.yahoo.com/news/meta-says-llama-ai-models-174133533.html) Even then, however, developers thought [Meta was no longer investing in Llama at the level it needed to be to compete with the leading frontier models](https://www.businessinsider.com/meta-ai-llama-was-big-deal-developers-see-untapped-potential-2025-5) of the day. Nevertheless, thousands of companies and an untold number of developers and individuals are [still using Llama](https://theirstack.com/en/technology/meta-llama/us). What can they do?

## Three options for developers

Llama developers do have some options. These include:

1. You can continue [using existing Llama models, which remain available on major cloud providers](https://www.llama.com/docs/getting-the-models/405b-partners/). These LLMs, however,  will increasingly lag behind their frontier competitors.
2. Switch to competing open-source models from Mistral, DeepSeek, or Alibaba’s Qwen.
3. Migrate to proprietary APIs from the major AI providers. Meta’s in-house programmers, for example, had [moved to Claude Sonnet](https://hackernoon.com/meta-abandons-llama-in-favor-of-claude-sonnet) long before Muse Spark arrived.

The switching costs are substantial. Migrations require rewriting vendor-specific APIs, adapting proprietary training data, and integrating custom tooling and workflows. [AI migration is not easy, nor is it cheap](https://www.theregister.com/2026/04/28/locked_stocked_and_losing_budget/).

## Llama forks fill the gap

Perhaps the easiest way forward will be to use one or more of the numerous Llama forks. The most important of these is the Llama inference engine fork [llama.cpp](https://github.com/ggml-org/llama.cpp). This is a popular C++ inference engine for running Llama models locally. Llama.cpp supports a wide variety of large language models, extending far beyond just Meta’s Llama family. From it, several other significant forks have emerged.

Perhaps the most well-known of these is [ik\_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp). This is a performance-focused fork that promises to deliver better CPU and hybrid GPU/CPU performance than llama.cpp. There’s also a Rockchip NPU fork, [Rkllama](https://github.com/NotPunchnox/rkllama).  This engine integrates llama.cpp with Rockchip NPU acceleration for embedded systems like the RK3588 chip, designed to work with nearly all standard llama.cpp-compatible models. Lastly, there’s [llama-rs](https://github.com/onehr/llama-rs), which is a Rust implementation marketed as an “ultra fast fork for local AI.”

Finally, there’s [OpenLLaMA](https://github.com/openlm-research/open_llama), which is an Apache-licensed open-source reproduction of Meta’s original LLaMA models. It’s available in 3B, 7B, and 13B parameter versions, all trained on 1 trillion tokens. It comes with weights for PyTorch and JAX.

Meta may benefit from this change. Llama users, however, must now find another way forward. Wish them luck. They’re going to need it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)