Cursor, the AI coding tool recently acquired by Elon Musk’s SpaceX in a [$60 billion all-stock deal,](https://thenewstack.io/spacex-cursor-ai-coding/) has launched a model router designed to direct every coding request to whichever model handles it best, bypassing the need to pay frontier prices for work that doesn’t need it.

Under the hood, the new [Cursor Router](https://cursor.com/docs/cursor-router) uses a triage system à la a hospital emergency room: It looks at what a request actually needs — how hard it is, what it’s for, the surrounding code — and picks a model that is the best fit. A quick fix goes somewhere cheap, while a genuinely hard problem gets escalated to something closer to frontier-grade.

Notably, developers and admins also have access to three distinct modes that nudge that balance in either direction, favoring speed and cost over raw power, or vice versa if needed.

![Choosing from three optimization modes](https://cdn.thenewstack.io/media/2026/07/441a3375-gif3.gif)

*Choosing from three optimization modes*

The broader rationale for Cursor Router, according to the company’s own field CTO [David Pan](https://www.linkedin.com/in/davepan/) in a social media post on Wednesday, is that developers shouldn’t have to become experts in model performance just to write code.

> “We briefly went insane and decided every software engineer should also become an expert in model benchmarks, thinking levels, and cache hit rate.”

“We briefly went insane and decided every software engineer should also become an expert in model benchmarks, thinking levels, and cache hit rates,” Pan writes.

Early community feedback has largely echoed Pan’s sentiment: [Fatih Arslan](https://www.linkedin.com/in/arslanfatih/), a software engineer at [PlanetScale](https://planetscale.com/), notes on X that engineers already juggle the choice between cost and capability by hand — defaulting to a cheap, fast model for routine work and saving the slow, expensive one for “serious tasks.”

“We already spend quite a bit [of] time on [choosing models],” Arslan [writes](https://x.com/fatih/status/2080047596081414417). “Why not automate that part? Cursor Router does the automation.”

> “We already spend quite a bit time on it [choosing models]. Why not automate that part?”

In a separate [blog post](https://cursor.com/blog/router) published on Wednesday, Cursor claims that early access customers saved 30-50% compared to routing everything through Opus 4.8, with no drop in output quality.

## Working model: Taking control of the stack

The launch follows a run of moves by Cursor to control more of its own AI stack. In May, the company [released Composer 2.5](https://thenewstack.io/cursor-composer-benchmarks/), an update to its in-house coding model built for long tasks at a lower cost than frontier options from Anthropic and OpenAI. Composer 2.5, like [its predecessor](https://thenewstack.io/cursors-composer-2-beats-opus/), is built on Moonshot AI’s [Kimi K2.5](https://www.kimi.com/ai-models/kimi-k2-5), an open-weight model out of China.

Now, with the weight of one of the world’s most valuable companies behind it (SpaceX has attained a market cap of $1.5 trillion since its June IPO), Cursor is pushing a powerful frontier model of its own.

On July 8, [Cursor and SpaceXAI jointly released](https://thenewstack.io/grok-45-opus-killer-launch/) Grok 4.5, a mixture-of-experts model built on a new foundation dubbed V9, which Musk had previously noted was roughly 1.5 trillion parameters. The model’s trained on trillions of tokens of real Cursor usage data and available across all Cursor plans at $2 per million input tokens and $6 per million output tokens.

With Composer handling cheap, fast work, and now the Grok-branded frontier line for more serious horsepower, Cursor has its own models in the mix alongside the usual list of outside providers. And this gets to the heart of *why* Cursor built Router: Most developers pick one model and stick with it regardless of the task, billing simple work at frontier prices it doesn’t need.

Sending every request to its own models would be the easy way to keep that money in-house, but it would also mean shipping inferior output on some tasks — so Router instead sends each request to whichever model actually suits it, Cursor’s own or not.

## The lay of the land

Model routing itself isn’t exactly new. [OpenRouter](https://openrouter.ai/) has offered a version since 2023: a single API sitting in front of more than [400 models](https://openrouter.ai/models) from over 60 providers, including OpenAI, Anthropic and Google. Its own [auto-router](https://openrouter.ai/openrouter/auto) feature does roughly what Cursor Router does — classify a request, then send it to whichever model fits the task and the person’s stated preference between cost and quality.

More recently, [OpenRouter launched Fusion](https://openrouter.ai/blog/announcements/fusion-beats-frontier/), which takes a slightly different approach: instead of picking one model, it sends a prompt to several models at once and uses a judge model to synthesize the strongest answer out of all of them.

This past month ushered another entrant to the mix: Japan’s [Sakana AI released Fugu in June](https://thenewstack.io/sakana-fugu-ai-sovereignty/), which instead breaks a single task into subtasks and routes each piece to a different model, pitched by Sakana as a hedge against relying on any one AI provider.

> “[Cursor Router is] a great example of how a technological innovation immediately translates into a product improvement.”

Not everyone rates some of these other attempts, though. On Wednesday, [Kirill Balakhonov](https://www.linkedin.com/in/kirill-balakhonov/), head of AI products at [Nethermind](https://www.nethermind.io/), argues [on LinkedIn](https://www.linkedin.com/posts/kirill-balakhonov_as-i-expected-sakana-fugu-is-already-forgotten-share-7485807826494320641-Jdqc/) that Cursor’s version succeeds precisely because it’s focused on coding specifically, rather than trying to be a general-purpose router for any task.

“A great example of how a technological innovation immediately translates into a product improvement… rather than an abstract idea like Sakana Fugu or OpenRouter Fusion,” Balakhonov [writes](https://www.linkedin.com/posts/kirill-balakhonov_as-i-expected-sakana-fugu-is-already-forgotten-share-7485807826494320641-Jdqc/), predicting both of those broader routing efforts would fade from use.

What’s new, perhaps, is some of the names emerging behind an array of model diversity efforts. In early July, [Microsoft launched a $2.5 billion services unit](https://thenewstack.io/enterprise-ai-model-routing/) dubbed Microsoft Frontier Company, embedding thousands of engineers at customer sites to help them build with a mix of AI models.

Judson Althoff, CEO of Microsoft Commercial Business, [told Reuters](https://finance.yahoo.com/technology/ai/articles/microsoft-2-5-billion-unit-165003043.html) at the time that the push came partly from watching rivals like DeepSeek and Google’s Gemini close the gap on OpenAI. Referring to the original Copilot, he admitted, “we made a mistake by binding it to OpenAI models only.”

If the company with the deepest single-model relationship in the industry [is walking it back](https://thenewstack.io/openai-microsoft-partnership-restructured/), the idea for model flexibility has clearly gone mainstream — certainly if this week is anything to go by.

On Tuesday, [Ramp](https://ramp.com/), the [$44 billion](https://techcrunch.com/2026/06/04/ramp-raises-750m-at-44b-valuation-as-investors-hunger-for-fintechs-with-an-ai-story/) spend-management behemoth, [opened up Ramp Router](https://ramp.com/router), an early-access public version of the model router it built to manage its own AI bills internally, which it says cut its LLM costs by roughly 30%. It’s free to start, requires no Ramp account, and routes across OpenAI, Gemini, and select open-source models including Kimi through an OpenAI-compatible endpoint.

The very same day, [Jyoti Mann from](https://www.linkedin.com/posts/jyoti-mann-873a4317b_scoop-metas-internal-incubator-for-ai-powered-share-7485464037544194050-dt-b/) *The Information* [reported](https://www.theinformation.com/articles/metas-ai-incubator-developing-openrouter-rival-cut-coding-costs) that Meta is also working on a model router. According to internal documents cited in the report, an incubator inside Meta called AAI Labs is developing a new product named Switchboard that would score each request for difficulty and send simpler ones to smaller, cheaper models — aimed initially at cutting Meta’s own AI agent costs, though it reportedly could end up as a public release.

Meta has particular reason to want this. Data from [Runpod’s State of AI report](https://thenewstack.io/runpod-ai-infrastructure-reality/), published in March, suggests Meta’s open Llama models are now a marginal presence in production: Llama 4 has near-zero real-world deployment, with Alibaba’s Qwen having overtaken it as the most-deployed self-hosted LLM.

Meta has also been building proprietary models in response. Muse Spark, its first model out of the newly formed Meta Superintelligence Labs, [shipped in April](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/). That was followed in July [by Muse Spark 1.1](https://thenewstack.io/meta-muse-spark-api/), Meta’s first model with a public, paid API, priced at roughly a quarter of what OpenAI and Anthropic charge for comparable models.

Meta is aggressively targeting the incumbents, and Switchboard fits the same pattern: a way to make it easier for users to cut costs, switch models freely, and, where it makes sense, land requests on Meta’s own models instead.

But amidst all this hullaballoo about model routing, there is perhaps a broader question of openness. Not of the models themselves, which is a fervent debate in itself, but of whether the routing decision itself — the logic that decides which model handles which request — should sit inside a vendor’s own closed product at all.

> “Is anyone building this as open-source?”

[Elvis Saravia](https://www.linkedin.com/in/omarsar/), a former technical product marketing manager at Meta AI who co-founded [DAIR.AI](https://www.dair.ai/), took to X to argue that it shouldn’t, given how differently teams weigh cost against quality.

“Is anyone building this as open-source?” Saravia [asks](https://x.com/omarsar0/status/2080034479020593525). “It feels like this is something you don’t want to offload to an API. We all work with different trade-offs, so we need the ability to achieve custom routing.”

As for Cursor’s own version, Router is currently available to Teams and Enterprise customers only, across desktop, web, iOS, CLI, and Cursor’s SDK. It’s not yet clear whether it will eventually land on individual plans.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)