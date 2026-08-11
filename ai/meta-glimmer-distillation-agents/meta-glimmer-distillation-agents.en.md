Meta released [Muse Glimmer](https://developer.meta.com/ai/models/muse-glimmer/) on Monday, a 30-billion-parameter open-weight model designed to run agentic workflows on local hardware. It’s available for download on [Hugging Face](https://huggingface.co/meta-models), but even more notable is how Meta turned its larger Muse Spark model into something small enough to work as a local agent.

The model was trained using Spark, allowing it to learn how the larger model handles complex tasks. Then Glimmer was compressed, and a lightweight secondary model was added to accelerate longer tasks. This approach demonstrates how companies can convert effective cloud models into smaller agents for local deployment — a process that [Sam Altman recently dismissed as a competitive concern](https://thenewstack.io/altman-security-distillation-scale/) but that Meta is now building into an end-to-end pipeline.

A local agent can manage routine tasks on the device, while a larger cloud model provides training and handles more complex jobs. However, this introduces an additional deployment chain for developers to manage.

## Distillation as deployment pipeline

According to Meta’s technical announcement, Glimmer was pretrained on Muse Spark’s outputs using [logit distillation](https://medium.com/@bravekjh/logit-distillation-teaching-ai-to-learn-like-a-pro-with-python-code-e38423a30b45). Meta followed that stage with longer-context training that placed more emphasis on agents and richer reasoning traces. Post-training combined supervised fine-tuning, reinforcement learning, and on-policy distillation across coding, reasoning, and agentic tasks.

Distillation is often used to reduce inference costs or fit models onto smaller devices, but Muse Glimmer shows how it can also connect centrally trained models with local agents that run closer to users and their data.

[DeepSeek recently demonstrated a related dynamic](https://thenewstack.io/deepseek-v4-flash-open-weights/) when its smaller model outperformed its own flagship, suggesting that a well-distilled student can sometimes match or exceed a larger model on targeted tasks.

For example, a company could use a larger model to train a local coding agent, allowing it to inspect repositories and use development tools without sending source code to the cloud. Meta is already investing heavily in this direction — [its internal training program exposed engineers to roughly 800 real coding failures](https://thenewstack.io/meta-metacode-engineer-training/) to shape how its models handle agentic development work.

Meta describes Glimmer as an “always-on” local agent that supports a context window exceeding 131,000 tokens, accepts text and image input, enables function calling, supports failure recovery, and offers multiple reasoning settings.

## Hardware costs of local inference

Meta states that Glimmer can run on a Mac or PC with a single consumer GPU. While accurate, this does not guarantee optimal performance on a typical laptop. At full precision, the model requires over 55GB of memory. Meta developed 4-bit versions that reduce the model size to under 20GB, allowing space for the context cache, vision encoder, and speculative-decoding model.

The smallest official configuration, K-Quant-17GB, is designed for systems with 24GB of memory. Meta tested this on Apple’s M4 Max and M5 Max chips and Nvidia’s RTX 5090. The 17GB quantization reduced average accuracy across 15 benchmarks by 1%. The larger dynamic quantization, targeting 32GB, resulted in a reported 0.2% decline.

Glimmer includes a small “drafter” based on [DFlash’s](https://github.com/z-lab/dflash) speculative-decoding capabilities. The drafter predicts blocks of 16 tokens, which the main model verifies in parallel. In Meta’s tests, this increased generation speed on an RTX 5090 from 74.9 to 233.4 tokens per second, from 23.7 to 37.8 on an M4 Max, and from 26.6 to 50.2 on an M5 Max.

AMD separately reported speeds of up to 24 tokens per second on a Ryzen AI Max+ 395 and 53 tokens per second on a Radeon AI Pro R9700.

## Versioning the full agent stack

Once a model has been distilled, compressed, and connected to an agent scaffold, its name no longer tells developers exactly how the finished system will behave. An agent built from Muse Spark 1.1 will not automatically pick up improvements made in Spark 1.2, so developers will have to rebuild and test it before rolling out the updated version.

Model compression introduces additional variability. While Meta’s tests showed minimal overall performance decline, Glimmer may not behave consistently across different tools and data, particularly if developers modify its reasoning level, system prompt, or agent scaffold.

> Testing only the full-precision version is insufficient if production uses the 17GB quantized model via llama.cpp on employee hardware.

Engineering teams using this approach will need to track more than the model weights and test the same setup they plan to use in production. Results from the full-precision model may not reflect how the 17GB quantized version performs through llama.cpp on employee hardware.

Meta’s benchmarks reflect those differences. Glimmer scored 75.5 on MCP Atlas, compared with 54.2 for Gemma4-31B and 62.5 for Qwen3.6-27B. It also narrowly beat Qwen on SWE-Bench Pro, scoring 51.2 against 50.2, although Qwen performed better on OSWorld-Verified, TerminalBench 2.1 and SWE-Bench Verified.

![](https://cdn.thenewstack.io/media/2026/08/de12fdf4-media-550x1024.webp)

Credit: Meta.

## Security falls on the developer

Keeping inference on the device can prevent source code from leaving the machine but doesn’t prevent the agent from mishandling that information.

In [Meta’s model card](https://huggingface.co/meta-models/Muse-Glimmer-30B), Glimmer recorded a 28.4% attack success rate on Siren AgentDojo. Gemma4-31B scored 25.6%, while Qwen3.6-27B scored 40.3%.

Glimmer also recorded a 26.4% violation rate on Meta’s contextual-integrity evaluation, CI Memories. Meta recommends deploying the model within a larger system that includes additional safeguards, rather than treating it as a secure standalone endpoint.

When the model runs locally, responsibility for security falls primarily on the developer. Without a cloud provider to enforce tool permissions, record requests, or block suspicious actions, applications must implement their own sandboxing, confirmation steps, credential boundaries, and audit records.

As [recent real-world containment failures have shown](https://thenewstack.io/anthropic-claude-containment-failure/), even heavily tested models can behave unpredictably when given access to real systems — and [the security community is still working out how to scope that problem](https://thenewstack.io/apple-ai-bug-report-caps/).

An agent capable of reading malicious documents and accessing local files should not inherit the full permissions of the user who launched it.

Meta plans to release an open-weight version of Muse Spark 1.2 in the coming weeks, giving developers the option to use the larger model for challenging tasks while Glimmer handles more routine work locally. Glimmer will not replace cloud models, and its hardware requirements mean it will not run everywhere, but it shows how a larger, more powerful model can be used to create a smaller agent that runs closer to the user.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)