Ox-alpha, the stealth model that quickly became the most popular model on OpenRouter in the last few days, is actually Z.ai’s GLM-5.3-Flash, a 320 billion-parameter hybrid model (with 18 billion active parameters) that the team specifically trained for ultra-low-cost inference.

On Wednesday, Z.ai [unmasked](https://z.ai/blog/glm-5.3-flash) the stealth model and made its weights available on [Hugging Face](https://huggingface.co/zai-org/GLM-5.3-Flash) under the MIT license.

It’s also already available on a number of inference platforms, including OpenRouter, where it’s currently available at $0.075 per million input tokens and $0.25 per million output tokens (though those prices reflect a 50% discount).

## Benchmarks: It’s good, but not Fable

While some of the early hype put the model at the level of Anthropic’s Claude Fable 5, the benchmarks don’t bear this out. But the model can, for the most part, keep up with a Claude Opus 4.8 and OpenAI’s GPT-5.6 Terra when set to its max-effort reasoning mode.

On the [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/models/glm-5-3-flash), GLM-5.3-Flash sits at 57 points, in line with GPT-5.6 Terra, Google’s Gemini 3.7 Flash, Meta’s Muse Spark 1.2, and Qwen 3.8 2.4T A95B.

When it comes to its performance in [driving AI agents](https://artificialanalysis.ai/models/glm-5-3-flash?intelligence=agentic-index), which may be a better indication of how it will perform in real-world use cases, it’s doing even better than its competitors.

The model is able to understand multimodal inputs, including images, videos, and files. Z.ai also stresses that it trained the model to do better at visual tasks like building presentations and websites, as well as at standard knowledge work tasks like working with documents, spreadsheets, and dashboards, all of which also benefit from the model’s improved visual capabilities.

![](https://cdn.thenewstack.io/media/2026/08/640a3339-rjg_rlhpzl-1024x638.webp)

Credit: Z.ai.

One caveat: the model is very chatty and burns a lot of tokens, which isn’t unusual for smaller models that need more reasoning steps to achieve this kind of performance. Because the inference costs are so low, though, that’s not too much of an issue.

## Cheap inference on Chinese chips

None of these competing models comes close to matching Z.ai’s pricing, and that may just be the most important takeaway from this launch. These Chinese open-weight models — including those from Alibaba, Deepseek, and Moonshot (Kimi) — are getting closer and closer to the performance of what American frontier labs can achieve — and they are making them available at a very low cost (and for free for those who have the hardware to run them).

![](https://cdn.thenewstack.io/media/2026/08/8db4c472-h1hakxndmx.png-1024x729.webp)

Credit: Z.ai.

One fact that tripped many early ox-alpha users up was the fact that the lab behind the model was able to serve 100 trillion free tokens per day (according to OpenCode). Very few infrastructure providers can handle that. But as it turns out, Z.ai did all of this on Chinese AI chips, something the company heavily stresses [in its announcement](https://z.ai/blog/glm-5.3-flash).

“Compared with our initial baseline on the same hardware, we achieved a 3× improvement in end-to-end serving performance, reaching hardware efficiency and per-token cost comparable to mainstream NVIDIA GPUs,” Z.ai writes. “This demonstrates that Chinese chips can support frontier-model inference efficiently and economically at scale.”

![](https://cdn.thenewstack.io/media/2026/08/8100a788-sy_ehd3wzx-1024x682.webp)

Credit: Z.ai.

## Linear and sparse attention

The company doesn’t go into details, but notes that the individual chips are limited in compute and memory capacity. But Z.ai built its own inference engine based on SGLang for this serving stack — with the help of its flagship GLM-5.3 model powering an infrastructure agent, which the company says created “a feedback loop in which the model helped optimize the system serving the model itself.”

Z.ai doesn’t say what chips the model was trained on, but the company does note that it was trained on a 30 trillion multimodal pre-training corpus and that the team used a hybrid architecture that combines linear and sparse attention.

![](https://cdn.thenewstack.io/media/2026/08/2732b7df-hyqvzw2wze.png-1024x544.webp)

Credit: Z.ai.

“Linear attention captures local dependencies through state modeling, while sparse attention retrieves relevant global context through a lightweight indexer,” the team explains, and also notes that compared to the full GLM 5.3 model, GLM 5.3-Flash’s architecture reduces the compute by 3x and KV cache size by 4.4x.

The model has a context window of 1 million tokens, so those reduced KV cache sizes make a substantial difference.

For developers, the calculus here is pretty straightforward. A model that matches Opus 4.8 on the benchmarks that matter for agents, at a tenth of the price, is hard to ignore. For the U.S. labs, the harder question is what happens now that Chinese labs can serve at this scale.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)