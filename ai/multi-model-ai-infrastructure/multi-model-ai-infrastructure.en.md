Vercel CEO [Guillermo Rauch](http://linkedin.com/in/rauchg) and Coinbase CEO [Brian Armstrong](https://www.linkedin.com/in/barmstrong/) run very different companies, but they’re making the same architectural bet. Instead of building around a single AI provider, both are designing production systems that can route work across multiple models.

Rauch and Armstrong aren’t making this decision in a vacuum. Frontier models have become much closer in capability for everyday engineering work, open-weight alternatives have improved dramatically, and the price gap keeps widening. That makes it much easier to justify routing work across several models instead of committing to one.

## Trillion tokens, zero loyalty

In an interview with [*TechCrunch*](https://techcrunch.com/2026/07/06/vercel-ceo-guillermo-rauch-on-the-fight-to-split-off-models-from-agents/), Rauch said that Vercel now routes more than a trillion tokens a day across millions of deployments, and that the company is actively moving away from one-lab partnerships. Rauch’s point highlights that the model has become just one interchangeable component in a larger inference pipeline.

That’s a significant position from the CEO of a company that serves as deployment infrastructure for a huge share of the frontend ecosystem. Rauch is [calling single-lab partnerships obsolete](https://letsdatascience.com/news/vercel-ceo-calls-single-lab-partnerships-obsolete-82f78a60).

> Rauch is calling single-lab partnerships obsolete.

## Cheaper defaults, smarter routing

Armstrong is making the same bet, and the financial results state his case. Coinbase [cut its internal AI spend by nearly half](https://analyticsindiamag.com/ai-news/coinbase-cuts-ai-spend-by-half-with-open-weight-models-smarter-routing/) while overall token usage continued to grow, without imposing usage caps on engineers.

Their playbook basically runs on three core levers.

First, it’s an internal LLM gateway. Coinbase deliberately defaults its engineers to lower-cost open-weight models, specifically Z.ai’s GLM 5.2 and Moonshot AI’s Kimi 2.7. Engineers can still pull down a stronger model if a specific job absolutely demands it, but the pricing gap makes the default choice obvious. GLM 5.2 costs roughly $1.40 per million input tokens and $4.40 per million output tokens.

Compare that to Anthropic’s Opus 4.8, which sits around $5 for input and $25 for output. You are looking at a three- to six-times cost reduction per token. And it holds its own on major coding benchmarks, scoring 62.1 on SWE-bench Pro, compared to GPT-5.5’s 58.6. Plus, because Coinbase self-hosts these models, zero code or query data ever leaves their environment.

The second lever is task-based routing. Armstrong makes a highly practical point here, suggesting teams want a frontier model to do the heavy lifting for complex planning, but for pure execution tasks, where cheaper models perform just as well, there is zero reason to pay top dollar.

The third piece is aggressive caching. By keeping a conversation locked to the same model as long as the cached context is valid, Coinbase managed to push its cache hit rate from a measly 5% up to 60%. That 12x jump is a massive cost driver.

## Gateways as control planes

If you want to understand Armstrong’s broader mindset, listen to his recent chat on the [*Sourcery*](https://open.spotify.com/show/2Ni3Tese9CtZa3oxpCjgTg) podcast. He casually mentioned that Coinbase now operates with roughly 1,200 full-time AI agents, a number they calculate by normalizing compute hours to a standard 40- to 60-hour workweek. At that scale, he argues that human developers have absolutely no business manually choosing which model to use. The infrastructure has to automate that decision entirely.

> Human developers have absolutely no business manually choosing which model to use.

Because foundation models are becoming so easy to swap in and out, the engineering focus is shifting to the surrounding infrastructure. Like a centralized control plane, a gateway intercepts every prompt and makes a dynamic, split-second decision about whether a workload actually requires the expensive reasoning capabilities of a frontier model or a cheaper, faster alternative can handle it. The infrastructure makes that call based on the cache state, the complexity of the task, and real-time pricing.

Teams need visibility into latency, uptime, token consumption, and cost across all providers because using multiple model providers changes observability requirements. Without that data, it’s difficult to know whether routing decisions are actually improving performance or reducing costs.

## Test before you trust

Evaluation becomes just as important. Lower-cost models need to be continuously tested against the workloads that matter to an organization before they are deployed to production traffic. Public benchmarks are a useful starting point, but are no substitute for measuring how a model performs on your own code, data, and workflows.

> Trying to pick the single best AI provider is a losing game.
>
> What’s striking is that Vercel and Coinbase arrived at remarkably similar architectures despite solving different problems. Both assume that today’s best model probably won’t stay on top for long. If that’s true, the competitive advantage shifts away from the model itself and toward the infrastructure that decides which one to use.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)