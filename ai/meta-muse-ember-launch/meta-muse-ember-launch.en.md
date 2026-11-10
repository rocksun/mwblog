![](https://cdn.thenewstack.io/media/2026/11/5d1eee3e-blog-header-visual-1024x576.png)

Meta on Monday debuted [Muse Ember](https://research.meta.ai/blog/muse-ember), a smaller, more efficient multimodal member of its Muse model family.

The company is clearly taking a similar approach to the other frontier labs, with a family of models that cover everything from focused, high-volume tasks (think OpenAI’s GPT-6 Luna and Anthropic’s [Claude Haiku 5.5](https://thenewstack.io/anthropic-claude-haiku-5-5/)) to frontier intelligence like OpenAI’s GPT-6 Astra, Anthropic’s Claude Fable 5.1, and, most recently, Meta’s [Muse Wonder Full](https://thenewstack.io/muse-wonder-claude-fable/). And just like its competitors, Meta is pitching the smaller model for agentic subtasks like reading files, running tests, and making targeted fixes, with a larger model like Muse Wonder doing the planning.

Muse Ember is available in Muse Code and through the Meta Model API under the model ID `muse-ember-1.0`. It will likely soon be available on services like OpenRouter and on the neoclouds, too, given that Meta has done the same for its other Muse models in the past.

Like with previous Muse model releases, Meta is keeping Ember’s model weights private.

Ember is Meta’s take on a small, price-efficient model, and at least when it comes to the benchmarks, it’s a strong entry.

![](https://cdn.thenewstack.io/media/2026/11/7ce96132-intelligence-vs.-cost-per-task-lm-1024x576.png)





Credit: Meta.

At max reasoning, Meta puts Ember at about $0.14 per task on the [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), compared with $0.41 for Haiku and $0.15 for Luna. Ember matches Haiku’s rounded score at about a third of the cost and scores higher than Luna for about a cent less per task.

At xhigh, the other Ember setting shown in Meta’s chart, the model scores about 34 at roughly $0.12 per task.

## Muse Ember pricing

Ember, which has a 1M-token context window and supports up to 512K output tokens, is priced at $0.10 per million input tokens, $0.004 per million cached input tokens, and $0.50 per million output tokens. Those input and output rates match [GPT-6 Luna](https://thenewstack.io/openai-gpt-6-sol-luna-release/) and Claude Haiku 5.5 at their standard short-context prices. Both charge $0.01 per million cached input tokens at those rates, with higher prices for longer prompts. Ember is available in Muse Code and through the Meta Model API as `muse-ember-1.0`, with support for the Responses API.

## How Chinese rivals compare

And while Meta doesn’t directly compare the new model to Chinese competitors like [DeepSeek V4.1 Flash 1017](https://thenewstack.io/deepseek-flash-haiku-test/), Z.ai’s GLM-5.3 Flash, and MiniMax M3.1 Flash in the chart, Ember undercuts the listed uncached input rates for all three. It also undercuts DeepSeek’s direct off-peak and MiniMax’s listed output prices and matches GLM’s. DeepSeek has a slightly lower off-peak cache-hit rate of $0.003 per million tokens.

On Artificial Analysis’ Intelligence Index, for example, Ember scores 36 at max reasoning, while DeepSeek V4.1 Flash 1017 is at 33, MiniMax at 29, and GLM at 28. OpenAI’s GPT-6 Luna, meanwhile, scores 28 on this same benchmark, while Haiku gets to 36, both at max reasoning.

## Muse Ember vs. Muse Spark

Meta’s own [Muse Spark 1.3](https://thenewstack.io/muse-spark-1-3-gemini/) scores 37 at max reasoning and costs $2.39 per task at the standard API rates used in the comparison. Meta also offers a Spark Contributor tier, where it uses requests to improve its products. That tier matches Ember’s uncached input price and charges $0.20 per million output tokens.

![](https://cdn.thenewstack.io/media/2026/11/8b1b16ed-muse-ember-and-muse-spark-1.3-comparison-lm-1024x409.png)





Credit: Meta.

Meta reports a lead over Haiku and Luna on its own Personal Superintelligence Index, a measure of personal and knowledge work. One benchmark where Ember doesn’t fare as well is FrontierCode 2.0, which evaluates whether a repository maintainer would merge an agent’s changes. Ember scores 27.2 percent, compared with 34.9 percent for Haiku and 28.5 percent for DeepSeek. Spark 1.3 scores 23.1 percent.

![](https://cdn.thenewstack.io/media/2026/11/77e246a3-muse-ember-evaluation-results-lm-921x1024.png)





Meta Muse Ember benchmarks. Credit: Meta.

## Computer use on OSWorld

Ember can take text, images, audio, and video as inputs, and Meta says it can operate desktop apps from screenshots.

On [OSWorld 2.1](https://osworld-v2.xlang.ai/#leaderboard), it got nearly the same partial-credit score as Haiku, 69.5 percent versus 68.9 percent, but finished more tasks outright, 33.8 percent versus 27.8 percent for Haiku and 17 percent for Luna. In a separate OSWorld 2.1 run, Spark 1.3 earned nearly identical partial credit to Ember and completed 39.25 percent of tasks.

Meta says the new model is the first it trained using the larger Muse Wonder Full model. That’s similar to what the company did with Muse Wonder to train the specialized models it began rolling out to [its Muse personal agent and Meta AI](https://thenewstack.io/meta-muse-specialized-models/).

The post [Meta launches Muse Ember to take on Claude Haiku and GPT-6 Luna](https://thenewstack.io/meta-muse-ember-launch/) appeared first on [The New Stack](https://thenewstack.io).