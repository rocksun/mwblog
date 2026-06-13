About a year ago, Google [demoed a diffusion model](https://thenewstack.io/googles-gemini-models-go-deeper/) at its I/O developer conference, but went quiet about the technology soon after.

On Wednesday, however, Google broke that silence with the launch of [DiffusionGemma](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/), an experimental 26B mixture-of-experts model that uses diffusion to generate text 4x faster than its existing Gemma models.

Diffusion has long been the standard for generating images (think Stable Diffusion). Instead of generating one word at a time, models like DiffusionGemma or Inception’s [Mercury 2](https://thenewstack.io/inception-labs-mercury-2-diffusion/) generate words in parallel.

At first, those blocks of text don’t make sense and seem random. But then, with each new step, the model refines the text and reduces the noise until it becomes the answer you were looking for. If you’ve ever looked at a diffusion image model generate images in real-time, that’s essentially the same process, but for text.

![](https://cdn.thenewstack.io/media/2026/06/89465e57-diffusion_process_3_1.gif)

*Credit: Google*

With each step, the model denoises 256 tokens in parallel, which is why it can be much faster than a traditional autoregressive large language model. It basically iterates on the text with each step until it.

All of these tokens attend to all others, which Google says is especially helpful for use cases such as inline editing, code infilling, working with amino acid sequences, and mathematical graphs.

![](https://cdn.thenewstack.io/media/2026/06/1363fff6-updated-intelligence_vs_latency_.width-1000.format-webp.webp)

*Credit: Google*

Google says DiffusionGemma can produce more than 1,000 tokens per second on a single Nvidia H100. And since the model uses the mixture-of-experts technique, it doesn’t have to keep the full 26 billion parameters in memory; instead, it activates only 3.8 billion during inference. This means it can easily run on a GPU with 18GB of VRAM.

There are some tradeoffs, though. On all benchmarks, the DiffusionGemma model underperforms when compared to Gemma 4 26B A4B. That’s something Google itself acknowledges. There’s no technical reason why a diffusion model couldn’t perform just as well as a more traditional large language model, but the focus here is on speed.

“For applications that demand maximum quality, we recommend deploying standard Gemma 4,” Google says in its announcement.

![](https://cdn.thenewstack.io/media/2026/06/68237f49-diffusiongemma__benchmark__bar_l.width-1000.format-webp.webp)

*Credit: Google*

## Availability

The model is now available on [HuggingFace](https://huggingface.co/google/diffusiongemma-26B-A4B-it), with Unsloth and other quantizations available for those who want to run it locally using [llama.cpp](https://unsloth.ai/docs/models/diffusiongemma) and (soon) similar local inference tools.

Google also worked with Nvidia to optimize the model for its hardware, including high-end GPUs like the  GeForce RTX 5090 and 4090, as well as the Nvidia DGX Spark and DGX Station (for those who can afford them). Nvidia NIMs are also available for the model.


[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)