**A 438-billion-parameter reasoning model** isn’t an obvious choice when speed is a priority. Multiverse Computing is betting that compression can make it one.

On Wednesday, the Spanish company launched Quasar 438B, its first large-scale model and a system designed specifically for coding and enterprise agents. Quasar achieves a score of 43 on Artificial Analysis’ Intelligence Index and 69.3 on Terminal-Bench v2.1, while Artificial Analysis currently records its output speed at approximately 183 tokens per second. Multiverse is positioning Quasar as the European model with the highest score on the Intelligence Index, outperforming Mistral Medium 3.5 (30) and NVIDIA Nemotron 3 Ultra (38).

> Multiverse is betting that a 438B-parameter model can be fast and inexpensive enough for agents that repeatedly reason, call tools, and check the results.

That puts Quasar in an interesting middle ground. It doesn’t match the strongest models on coding performance, but Multiverse is betting that a 438B-parameter model can be fast and inexpensive enough for agents that repeatedly reason, call tools, and check the results.

The model features a context window of one million tokens, is available in English and Spanish, and can be accessed via the Multiverse CompactifAI API.

## Compression claims, missing details

Multiverse built CompactifAI to shrink large AI models so they need less memory and compute to run. The company says it can reduce model size by 80% to 95% with only a small loss in accuracy, but it hasn’t disclosed how much Quasar was compressed or which model it started with.

In July, Multiverse announced a $570 million Series C to expand its library of compressed models and commercialize the technology. Quasar is the biggest test of that approach so far.

Multiverse hasn’t said what hardware is required to run Quasar or how much the compression reduces its memory and compute needs. That matters for agents, which may repeatedly call the model and other tools before finishing a task.

> Multiverse hasn’t said what hardware it takes to run Quasar or how much the compression cuts its memory and compute needs.

## Coding benchmarks show tradeoffs

In Multiverse’s comparison, Quasar’s Terminal-Bench v2.1 score of 69.3 places it ahead of Mistral Medium 3.5 but still well behind the best frontier systems, while Claude Opus 5 achieves the highest score on that benchmark at 89.1.

Multiverse is pitching Quasar for software engineering, technical copilots, research, and workflow automation. Its 1-million-token context window gives agents room to work with large codebases and hold onto information as a task progresses, although processing more context also requires more compute. That can be especially important in coding, where [code that passes every test can still trip up the next AI agent](https://thenewstack.io/go-language-ai-agents/) if it loses track of what came before.

## Agent latency beyond throughput

Artificial Analysis found that Quasar starts responding in about 1.1 seconds and can produce a 500-token response, including reasoning, in around 15.3 seconds. Those numbers are fast, but an agent also has to wait for tools, process growing context, and make repeated model calls over the course of a task. The [agent tooling layer itself](https://thenewstack.io/ard-agent-discovery-specification/) is still catching up to what these models need.

> Those numbers are fast, but an agent also has to wait for tools, process growing context, and make repeated model calls over the course of a task.

## Proprietary model, open questions

Quasar is proprietary and only available through Multiverse’s API, so developers can’t inspect the weights or run it on their own hardware. For now, that also makes it difficult to know whether the speed Multiverse is reporting will carry over to everyday agent use.

Quasar also arrives as [European AI companies are building more of their own model and compute infrastructure](https://thenewstack.io/mistral-third-party-open-models/) instead of relying on U.S. hyperscalers. Multiverse is taking a different route, using compression to make a 400B-plus model cheaper and faster to run. The next step is to see how that holds up against benchmarks.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)