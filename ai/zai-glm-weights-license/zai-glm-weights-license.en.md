Earlier in August, Z.ai, the Chinese AI lab behind the viral [ox-alpha model](https://thenewstack.io/ox-alpha-privacy-terms/) that turned out to be [GLM-5.3-Flash](https://thenewstack.io/glm-5-3-flash-chinese-chips/), launched its flagship GLM-5.3 model. On Friday, the company made the model’s weights available on [Hugging Face](https://huggingface.co/zai-org/GLM-5.3), which Nvidia may soon own. Several third-party inference services already host it and make it available on services like OpenRouter, which Stripe will soon own.

As *The New Stack’s* Amanda Caswell [reported](https://thenewstack.io/glm-5-3-post-training-coding/) when the model originally launched, Z.ai’s focus on training GLM-5.3 was on post-training. The result isn’t simply a large jump in benchmark performance over its predecessor, GLM-5.2, but a model that is often ahead of other Chinese open-weight models and can keep pace with current models from the large U.S. frontier labs.

## A new license only hyperscalers won’t love

One thing Z.ai definitely changed is the model’s license. While GLM-5.2 shipped under the permissive [MIT license](http://huggingface.co/zai-org/GLM-5.2/raw/main/LICENSE), the new model ships under what the company calls the GLM-5.3 license and it has one major caveat: companies that want to host the model (not just route it like OpenRouter or embed it into a product), and have an aggregate revenue of more than $10 billion over any 12 consecutive months, “must pass Z.AI’s security review before using the Software or its derivative works for any commercial purpose.”

For individual users, nothing really changes — the license is more specific to models and includes the rights to run, deploy, and fine-tune. But for hyperscalers (and the neoclouds — once they hit these revenue numbers), there are now hoops to jump through.

![](https://cdn.thenewstack.io/media/2026/08/459fa358-screenshot-2026-08-28-at-10.01.37-am-1024x584.png)

The company says it held the GLM-5.3 open weights back for two weeks for safety evaluation and hardening. GLM-5.3 hits 84.5 percent on CyberGym, a vulnerability discovery benchmark, which Z.ai says is the best published result. That number is self-reported, of course, and nobody outside the company has reproduced it yet.

Z.ai says it used the model to find 2,436 vulnerabilities across 269 open-source projects, including the Linux kernel, though only a few dozen of those findings are publicly inspectable so far.

Despite the safety framing, it’s worth noting that the license itself contains no acceptable-use section and also says nothing about cyber or offensive security.

Whether Z.ai changed its license for security reasons or to better monetize its own models is a question worth asking, of course. With the launch of GLM-5.3-Flash, the company stressed that inference was running on Chinese chips, so Z.ai has definitely shown interest in owning the inference layer for these models, after all. And now that these open-weight models are getting so close to the performance of what U.S. frontier labs are producing, there’s more money to be made there, too.

Back in 2023 and 2024, Z.ai also used a custom license for models like ChatGLM3-6B. Under that license, registration was required for commercial use. From then on, though, all new Z.ai models were licensed under the MIT license.

Z.ai’s license is also more restrictive than those used by other Chinese labs. [Moonshot](https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE), for example, says that if a model-as-a-service provider offers access to Kimi K3 and has more than 100 million active users or more than $20 million in monthly revenue, “‘Kimi K3’ must be prominently displayed on the user interface of such product or service.”

DeepSeek still uses the basic [MIT license](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) for its flagship models.

## Running GLM-5.3

Under the hood, GLM-5.3 is the same 753-billion-parameter mixture-of-experts architecture as GLM-5.2, with a 1 million-token context window and a maximum output of 128,000 tokens.

The weights ship in BF16 and FP8 and run on vLLM, SGLang, KTransformers, and Hugging Face’s own Transformers library.

![](https://cdn.thenewstack.io/media/2026/08/3ac592e1-screenshot-2026-08-28-at-9.23.36-am-1024x833.png)

Credit: Z.ai.

The two-week gap between the API launch and the open release is new for Z.ai. GLM-5.2’s weights were available on launch day.

Even though the model is now open-weight, you’re not all that likely to run it locally — unless you have a very powerful machine. Even the 2-bit quants, which Unsloth [says](https://unsloth.ai/docs/models/glm-5.3) will still achieve about 86 percent top-1 accuracy, need 245GB of memory. That just fits on a Mac with 256GB of unified memory. The 8-bit quants need 810GB.

For $1.40/$4.40 per million input/output tokens, it’s also significantly cheaper to use than virtually all of its most direct competitors — though the GLM-5.3-Flash model at $0.15/$0.47 has a pretty unbeatable price/performance ratio right now.

## What’s next

At first glance, the license is a small change in absolute terms, but it comes in the same week that Nvidia moved to acquire Hugging Face for a reported $12.9 billion and Stripe agreed to acquire OpenRouter. If both deals close, the repository where developers download open-weight models and the marketplace where they rent them will be owned by American companies, while [the models themselves](https://openrouter.ai/rankings#top-models) increasingly come out of Chinese labs.

Z.ai kept MIT for Flash, so the company hasn’t completely abandoned permissive licensing, but it has stopped applying it to its best model. If GLM-5.4 ships the same way, the company’s MIT years will look like the customer acquisition phase, and open weights will start to look less like a gift to the ecosystem and more like a distribution channel with terms attached.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)