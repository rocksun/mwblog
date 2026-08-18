Alibaba recently made the open weights of its 2.4 trillion parameter Qwen3.8 model [available](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B). That’s a massive model, and its benchmarks put it in direct competition with closed frontier models from American labs. But what’s maybe even more interesting is that on Friday, Alibaba also made a dense [27 billion parameter version of Qwen 3.8 available](https://huggingface.co/collections/Qwen/qwen38) under the Apache 2.0 license.

That’s a model that you could run locally on a well-specced Macbook Pro or Mac Studio, for example — and it might be worth doing so, because according to Alibaba’s benchmarks, the model’s performance is in the same league as Anthropic’s Opus 4.6 running at its Max setting.

On quite a few benchmarks, it even outperforms Anthropic’s former flagship model, which was state-of-the-art six months ago [when it launched in February](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/), especially when it comes to some computer use, coding and knowledge work tests.

Add to that the fact that the model also has vision capabilities — including videos — and this becomes a compelling option for local usage (assuming you have the hardware to support it).

## Caveats

As usual, the caveat here is that benchmarks don’t always measure how well a model performs in the real world, and for agentic use cases, the harness they run in can be as important as the model itself. Early reports say the model [tends to overthink](https://news.ycombinator.com/item?id=49299605), for example.

It also looks like Alibaba’s benchmarks describe the original checkpoint, not the quantized versions most local users will run. Quantization may make a model practical on consumer hardware, but there is always a quality tradeoff.

Still, overall, these are impressive results for a model that you could run locally.

![](https://cdn.thenewstack.io/media/2026/08/18936970-hpso4qibgaar-sb-1024x895.jpeg)

Credit: Alibaba.

Alibaba notes that the model significantly outperforms the previous-generation Qwen 3.7-Plus, especially in coding and knowledge work tasks, and some of the performance jumps are quite impressive, including a step up on the DeepSWE agentic coding benchmarks from 14.2 points to 42.2.

That’s still behind the current frontier (and other open models like the newly released

[GLM-5.3](https://z.ai/blog/glm-5.3)

), but even Google’s mid-tier Gemini 3.6 Flash only got to 49% on this test, and you’re not running that model on your laptop anytime soon.

![](https://cdn.thenewstack.io/media/2026/08/10b0e960-hpso5qhasaelxuc-1024x984.jpeg)

Credit: Alibaba.

Alibaba also compares the model with Meta’s [Muse Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B), another recently released local model in roughly the same size class. Qwen3.8-27B leads it on every test for which Alibaba reports scores for both models.

Glimmer, it seems, was the right name for that model.

## The hardware you need to run Qwen 3.8 27B locally

Speed is another issue, of course. As of now, Alibaba hasn’t released a smaller Qwen3.8 27B mixture-of-experts sibling. Such a model could activate fewer parameters per token and run faster than the dense 27B release. It previously did so for the Qwen 3.6-35B model, for example.

The unquantized Qwen3.8-27B repository is 55.6GB, before accounting for the inference runtime and context cache. That’s not what most people will run.

The good news for Mac users is that community-created [MLX conversions for Apple silicon](https://huggingface.co/mlx-community/Qwen3.8-27B-4bit) are already available. The 4-bit version is about 16.1GB, while the [8-bit version](https://huggingface.co/mlx-community/Qwen3.8-27B-8bit) is 29.5GB. That makes a Mac with 32GB of unified memory a resonable platform for running a 4-bit version at a moderate context length. If you have it, 48GB or 64GB would obviously provides considerably more room for higher precision or longer prompts.

By default, the model supports 262,000 tokens of context, which can be extended (and will be by Alibaba for its hosted production version) to 1 million tokens by using the [YaRN method](https://github.com/jquesnelle/yarn). That doesn’t mean you can use that full context window on your desktop (the key-value cache consumes more memory as the prompt grows).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)