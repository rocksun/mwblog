Meta on Thursday launched Muse Spark Open, a new 816B open model (with 42B active parameters) that the company argues is the “most capable US open-weight model to date.”

The [new model is available](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) through the APIs of Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter, and Together AI. And since it’s an open model, you can also download the weights from Amazon SageMaker AI, Google Cloud Model Garden, Hugging Face, and Microsoft’s Foundry Model Catalog.

## Open Weights, semi-open license

Overall, Muse Spark Open, which features the industry-standard 1 million token window, looks to be an extremely capable model that, depending on the benchmark, is on par with or beats some of the best Chinese models. Like with some of the [newer Chinese models](https://thenewstack.io/zai-glm-weights-license/), though, the weights may be open but the license doesn’t tell the same story.

Meta is launching the new model under the “[Muse Model License](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B/blob/main/LICENSE.md).” This license, Meta says, has “limited commercial terms, which allow many developers to use the model for free.”

Specifically, this means any company that has more than $20 million in gross revenue during any consecutive twelve-month period must “notify Meta and enter into a separate written agreement with Meta before offering the Software or any Derivatives as part of that Model as a Service business.”

Any company using the model must also “prominently display ‘Built with Muse Spark Open’ in the user interface of each product or service” that uses the model or a derivative model that was created, trained, fine-tuned, or distilled from Muse Spark Open.

Overall, this looks a lot like the license that Moonshot uses for Kimi K3, for example.

Internal use and building the model into your own product are free, and the license’s usage policy bars military and critical infrastructure deployments, a carve-out Meta added for the U.S. government with Llama in 2024.

Unlike Anthropic’s [new usage policy for Claude](https://www.anthropic.com/news/2026-usage-policy-update), though, you can abuse the model as much as you want.

## Benchmarks

The company says it built the new model for “coding and agentic work, it excels at long-horizon tasks, complex software engineering, and multi-step reasoning.”

The two U.S. models Muse Spark Open competes with are essentially Thinking Machines’ Inkling and Nvidia’s Nemotron 3 Ultra. In Meta’s own benchmarks, its new model beats them across the board — often by 20 points or more.

![](https://cdn.thenewstack.io/media/2026/10/a9c1bb66-eval-table_light-851x1024.png)

Credit: Meta.

The closer fight, however, is with Chinese open models that many developers already run today. Spark Open leads Kimi K3, GLM 5.3, and Qwen3.8 on the agentic and tool-use benchmarks, including JobBench and MCP-Atlas, and roughly ties them on SciCode.

Coding is where it trails.

On Terminal-Bench 2.1, Kimi K3 scores 85.0 and GLM 5.3 83.9 against Spark Open’s 76.4.

On DeepSWE 1.1, the spread is 68 to 60. That’s the same gap Meta acknowledged when it launched the closed version of Spark in April, and it doesn’t look like it’s made much progress since.

## Muse Spark Open on the Mac you can’t afford

You’re unlikely to run an 816B model locally, but if you have two new Mac Studios with M5 Ultra chips and 512 GB, Meta says you could link them and use MLX to run the model on them.

The company did just that to run Muse Code, powered by Muse Spark, and ship updates to the Ice Cubes Mastodon client, for example. Apple doesn’t currently sell the 512 GB Mac Studio to mere mortals, but in a few weeks, you will be able to buy two of those machines for the [price of a compact car](https://www.apple.com/shop/buy-mac/mac-studio).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)