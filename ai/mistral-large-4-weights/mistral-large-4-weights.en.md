**Mistral launched Large 4 on Tuesday**, its first major model release since Medium 3.5 at the end of April and the company’s latest attempt to close the gap with China’s leading open-weight models.

The company says the new model is particularly strong in cybersecurity, and those capabilities surfaced during evaluation when the model tried to go beyond its testing environment, Mistral VP of Science [Pierre Stock](https://www.linkedin.com/in/pierrestock/) [told Reuters](https://www.reuters.com/world/china/mistral-ceo-says-new-ai-model-beats-chinese-ones-some-areas-2026-10-06/), adding that the behavior was expected and that the company contained it using software.

The episode has not slowed Mistral’s release plans, and Large 4, nicknamed “Le Chonk” in a nod to the [“Le Chaton Fat” meme](https://www.reddit.com/r/singularity/comments/1wz2r59/le_chaton_fat_is_real/) about a fictional supersized Mistral model that spread across X and Reddit in June, is now in public preview through Mistral’s API, with cybersecurity experts and government authorities testing a version with fewer safety restrictions before the weights are published on October 27.

OpenAI and Anthropic have seen similar behavior while testing their most cyber-capable models and responded by restricting access. Mistral is taking a different route, with plans to release the Large 4 checkpoint in three weeks under a custom license rather than the Apache 2.0 license used for Large 3. Once the weights are out, developers control how the model runs and what safeguards they put around it.

> Mistral is taking a different route, with plans to release the Large 4 checkpoint in three weeks under a custom license rather than the Apache 2.0 license used for Large 3.

## One trillion, 49 billion active

Large 4 gets its one-trillion-parameter size from a sparse mixture-of-experts architecture that activates 49 billion parameters during inference, a significant step up from the 675 billion total and 41 billion active parameters in [Large 3](https://mistral.ai/news/mistral-3/).

The company trained Large 4 from scratch in roughly two months on about 4,000 Nvidia Grace Blackwell GPUs in its European data centers. Mistral has made a point of the relatively small training cluster, although comparisons with the largest U.S. labs are difficult when so little training compute is disclosed.

Its sparse architecture keeps inference compute down by activating only 49 billion of the model’s one trillion parameters, but serving the full checkpoint will still require a substantial multi-GPU setup.

Software engineering and cybersecurity are the main targets for Large 4, with financial analysis, satellite and aerial imagery, technical drawings and chip design among its other use cases. It takes multimodal inputs, produces text and supports more than 160 languages, including every official language of the European Union.

## Open weights, no recall

Mistral’s case for open weights in cybersecurity rests on control. Security teams scanning code or testing systems can run into a hosted model’s safety restrictions, and [OpenAI’s safety system is already cutting off API responses mid-task](https://thenewstack.io/openai-slowing-ai-development/) even as the company gives models more authority inside its own development workflow, including [blocking code from merging](https://thenewstack.io/openai-ai-code-review/) when a vulnerability is found.

> Mistral’s case for open weights in cybersecurity rests on control.

Running Large 4 on their own infrastructure lets teams set those restrictions themselves and keep sensitive code and data in-house. Stock made the other half of that argument to [Journal du Net](https://www.journaldunet.com/intelligence-artificielle/1555845-mistral-large-4-la-recette-secrete-de-mistral-ai-pour-rattraper-les-geants/), noting that once weights are replicated across the internet, access can no longer be easily revoked.

## DeepSWE scores need context

Mistral reports a 62% score on DeepSWE v1.1, just above the 61% it lists for GLM-5.3. However, the [live DeepSWE leaderboard](https://deepswe.datacurve.ai/) puts GLM-5.3 and Kimi K3 at roughly 69% with their best published configurations, while GPT-6 Astra, Gemini 3.8 Flash and Claude Opus 5 are around 74%.

The results are stronger elsewhere. Large 4 reached a 15% task-pass rate on [Harvey’s Legal Agent Benchmark](https://www.vals.ai/benchmarks/hlab) and 67% on [Finch](https://aclanthology.org/2026.findings-acl.523/), where Mistral’s testing has it tied with DeepSeek V4 Pro 0813 and ahead of GLM-5.3 at 65%. Independent results for those configurations aren’t yet available.

For now, those numbers make Large 4 look competitive without putting it at the top of the pack. We’ll all be eager to see what comes at the end of the month when developers can run Le Chonk outside Mistral’s API and see how much of that performance survives on their own workloads.

> Large 4 reached a 15% task-pass rate on Harvey’s Legal Agent Benchmark and 67% on Finch, where Mistral’s testing has it tied with DeepSeek V4 Pro 0813 and ahead of GLM-5.3 at 65%.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)