After pre-announcing Nemotron 3 Ultra, a 550-billion-parameter open-weight mixture-of-experts model, at Computex, Nvidia on Thursday released the model on platforms like [Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4), [ModelScope](https://modelscope.ai/collections/nv-community/Nemotron-3x), [OpenRouter](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b) (with a free endpoint), and [build.nvidia.com](https://build.nvidia.com/).

The new model uses the same latent mixture-of-experts technique and [Mamba 2](https://goombalab.github.io/blog/2024/mamba2-part1-model/) architecture as the other models in the Nemotron 3 family, bringing the number of active parameters down to 55 billion. It can support context windows of up to 1 million tokens.

As Nvidia notes, the new model has been tuned to power long-running agents that need to plan, call tools, and iterate over complex tasks. For this, the model needs to be not just smart enough but also fast enough. Indeed, Nvidia is emphasizing speed with this release, noting that it is significantly faster than its previous generation of models.

Given the current concerns around token costs, what may matter more here is that Nvidia also claims the model could save users up to 30% compared to similarly powerful models.

![](https://cdn.thenewstack.io/media/2026/06/82f066ae-nemotron-3-ultra-aa-quadrant-chart-scaled-1-1024x468.png)

Credit: Nvidia

While it is the fastest model among its direct competitors like Kimi-K2.6, Qwen-3.5, and GML-5.1 — and the best U.S. open-weight model yet — it does still trail the best of these Chinese models on most benchmarks, even if only by a few points.

And while Nvidia calls this a frontier model, the benchmarks don’t quite tell this story. On GDPVal, which tests how well a model performs real-world, economically valuable tasks, Nemotron 3 Ultra — in its NVFP4 variant, which uses Nvidia’s new quantization-aware pre-training technique — scores 47.9%. By comparison, OpenAI’s GPT-5.5 scores 84.9%.

![](https://cdn.thenewstack.io/media/2026/06/4fbb7e19-screenshot-2026-06-04-at-16.16.35-1024x577.png)

Credit: Nvidia

Benchmarks don’t always capture a model’s strengths, though, and Nvidia notes that the model can handle “the orchestration and hardest reasoning calls in an autonomous workflow: architectural decisions in long-running coding sessions, synthesis across hundreds of research sources and verification across thousands of interdependent constraints.”

![](https://cdn.thenewstack.io/media/2026/06/c53886af-accuracy_plot-2-1024x587.png)

Credit: Nvidia

The model was trained on a curated dataset of 14.8 trillion tokens, enabling it to support 12 languages (English, French, Spanish, Italian, German, Japanese, Korean, Hindi, Brazilian Portuguese, and Chinese) and 43 programming languages.

Nvidia is making the weights, datasets, and training recipes available. The model is available under the OpenMDW-1.1 license.


[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)