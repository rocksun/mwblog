Ahead of its flagship GTC conference next week, Nvidia on Wednesday [launched](https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/) the second model in its open-weight [Nemotron 3 family](https://thenewstack.io/nvidias-launches-the-next-generation-of-its-nemotron-models/): Nemotron 3 Super, a 120-billion-parameter model with a 1-million-token context window, tuned for speed and efficiency.

Last December, Nvidia debuted Nemotron 3 Nano, a smaller 30-billion-parameter model that used many of the same optimization techniques as the larger Super model. But where that smaller model was especially useful for smaller targeted tasks, Nvidia is positioning Nemotron 3 Super as a model that can “run complex agentic AI systems at scale.”

## Nemotron 3 Super availability

The new model is now available on [build.nvidia.com](https://build.nvidia.com/), Perplexity, OpenRouter, and Hugging Face. Enterprises will also be able to access it through Google Cloud’s Vertex AI, Oracle Cloud Infrastructure, and — soon — Amazon Bedrock and Microsoft Azure, as well as on platforms like Coreweave, Crusoe, Nebius, and Together AI.

For those with the necessary hardware, Nvidia is also making it available as a NIM.

Since it is currently available for free on [OpenRouter](https://openrouter.ai/nvidia/nemotron-3-super-120b-a12b:free), many people will likely try it with their [claws](https://thenewstack.io/nanoclaw-minimalist-ai-agents/).

Like the Nano model, Nemotron 3 Super uses the same [hybrid latent](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)[mixture-of-experts](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models) and Mamaba-Transformer architecture, which should help it excel at tracking context across long tasks without too much memory overhead. This architecture also allows the model to call upon 4x as many expert specialists during inference as previous models, at the same inference cost. (For more, view [Nvidia’s full research paper](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf).)

![](https://cdn.thenewstack.io/media/2026/03/32ed02d8-image2-2.webp)

Side-by-side comparison of standard MoE vs. latent MoE architectures (credit: Nvidia).

One interesting fact is that the model was trained on synthetic data from other frontier reasoning models, and Nvidia is publishing over 10 trillion tokens of [pre-](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1.1) and [post-training](https://huggingface.co/collections/nvidia/nemotron-post-training-v3) data sets with this release, as well as 15 training environments for reinforcement learning and evaluation recipes.

This matters, given that quite a few enterprises, [including ServiceNow](https://thenewstack.io/servicenow-launches-a-control-tower-for-agents/), used the previous Nemotron variants to fine-tune their own models. Nvidia itself has also used these models as the basis for some of its research and more specialized models.

VIDEO

## Nemotron 3 Super benchmarks

When Nvidia first announced the Nemotron family, the Super model was still supposed to be a 100-billion-parameter model with 10 billion active parameters, but the company clearly scaled its ambition up a bit.

Maybe that’s also to match [OpenAI’s gpt-oss-120B model](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/#:~:text=OpenAI%20Releases%20Two%20Open%20Source%20Models), which launched last August. It’s this OpenAI model, after all, that most people will likely compare Nemotron 3 Super to.

![](https://cdn.thenewstack.io/media/2026/03/5b31a1db-super-3-aa-scaled.png)

Credit: Artificial Analysis.

Looking at the benchmarks, Artificial Analysis puts the model’s overall intelligence at 36, slightly above gpt-oss-120B at 33 points and well behind leading models like Gemini 3.1 Pro or GPT-5.4, which both score 57 points.

This still puts Nemotron 3 Super well above older open models like Qwen3 Next 80B, but also behind newer models like Qwen3.5 122B, DeepSeek V3.2, and GLM-5 (though that is a significantly larger model).

![](https://cdn.thenewstack.io/media/2026/03/a5ab6369-nemotron-3-super-scaled.png)

Artificial Analysis looks at Nemotron 3 (credit: Artificial Analysis).

But where Nemotron 3 Super excels is speed. At 478 output tokens per second, according to [Artificial Analysis](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/providers), it’s faster than any previous model. Gpt-oss-120B is the second-fastest model, at 264 output tokens per second, and Nvidia notes that it also achieves 7.5x higher inference throughput than Qwen3.5-122B.

## Where’s Nemotron 3 Ultra?

There’s no word yet on when we can expect Nemotron 3 Ultra, the family’s largest model at 500 billion parameters, which Nvidia teased in its original announcement from last year. Maybe we’ll see that at GTC in a few days.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)