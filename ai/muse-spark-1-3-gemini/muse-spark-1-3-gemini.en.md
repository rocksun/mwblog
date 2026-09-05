It has been a big week for Meta in the AI sphere, formally [launching its Muse Code coding agent out of beta](https://thenewstack.io/muse-code-sdk-pricing/) with a triumvirate of new subscription plans. Then late on Wednesday, the company [unveiled Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3), the latest version of its low-cost reasoning model, with Meta claiming its biggest gains yet in coding and agentic tasks.

Available through Muse Code and the [Meta Model API](https://developer.meta.com/ai/products/meta-model-api/), Muse Spark 1.3 is the latest iteration of the reasoning model Meta first [introduced in April](https://ai.meta.com/blog/introducing-muse-spark-msl/), and arrives less than a month after the release of [Muse Spark 1.2](https://thenewstack.io/meta-muse-code/). Meta CEO Mark Zuckerberg took to social media to hype the new release, describing it as delivering “frontier performance almost too cheap to meter.”

> “This is the biggest jump we’ve made so far on coding and agentic work.”

“This is the biggest jump we’ve made so far on coding and agentic work,” Zuckerberg [writes on X](https://x.com/finkd/status/2095232032896946311).

## Open-weight release ‘coming soon’

Zuckerberg also confirmed that the open-weight releases of Muse Spark will be “coming soon,” a move that could let developers download and run the model on their own infrastructure, bypassing Meta’s hosted API.

Exactly how permissive that will be, however, isn’t clear, as Meta has yet to publish the licence terms that will accompany the release. Its previous open-weight models [have carried](https://thenewstack.io/meta-open-source-models/) varying restrictions on use, so those details will determine how freely Spark can be modified, redistributed or deployed.

Notably, Zuckerberg also teased Meta’s much-hyped next model, codenamed Watermelon, using the somewhat apt watermelon emoji.

That model is understood to be a much larger system than Spark and was reportedly still in training in July, according to a *Business Insider* [report](https://x.com/finkd/status/2095232032896946311?s=20) at the time. There is still no firm word on when Watermelon will see the light of day, though the implication from Zuckerberg is that it won’t be long.

For now, though, Meta is making some sizeable claims for Spark 1.3 itself. Zuckerberg accompanies his post with a benchmark table pitting the model against OpenAI’s [GPT-5.6 Sol](https://thenewstack.io/developers-review-gpt-56-sol/) and Anthropic’s [Claude Opus 5](https://thenewstack.io/anthropics-opus-5-almost-fable-5/) across coding, agentic, computer-use and long-context tests.

Among the standout figures, Muse Spark 1.3 scored 75.4% on the DeepSWE coding benchmark and 98.1% on the 512K-1M version of the MRCR long-context test.

![Muse Spark 1.3: Benchmarked](https://cdn.thenewstack.io/media/2026/09/93e7fb99-becnhamrk-1024x920.png)

*Muse Spark 1.3: Benchmarked*

These are Meta-assembled results, however. The company says its Spark 1.3 scores were generated through the Meta Model API, while comparison figures are drawn from a mixture of Meta’s own evaluations, official leaderboards and results reported by rival model providers. Meta [also describes its testing](https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology) of third-party models as “best-effort,” meaning the table shouldn’t be read as a single independent head-to-head test conducted under identical conditions

There is another caveat to these results: Meta ran Spark 1.3 at its new “max” reasoning level for the headline comparisons, while the highest reasoning level generally available to developers today is “xhigh.” Max remains in limited preview while Meta completes additional safety testing.

## “Gloves are off”: How Spark 1.3 stacks up

Independent testing by *Artificial Analysis* does [offer a useful outside perspective](https://artificialanalysis.ai/articles/muse-spark-1-3). The San Francisco-based company, which specializes in benchmarking AI models and providers, gives the publicly available Muse Spark 1.3 xhigh a score of 61 on its Intelligence Index, four points ahead of Spark 1.2 and level with GPT-5.6 Sol max, Grok 4.6 high and Claude Opus 5 high. It was also able to test the limited-preview max version, which scored 62, placing it behind only Claude Fable 5.1 and Claude Opus 5 among the models in its comparison at launch.

![Artificial Analysis Intelligence Index (credit: Artificial Analysis)](https://cdn.thenewstack.io/media/2026/09/94865237-stuff-1024x404.png)

*Artificial Analysis Intelligence Index (credit: Artificial Analysis)*

[Alex Volkov](https://www.linkedin.com/in/alex-volkov-/), AI evangelist at cloud infrastructure company CoreWeave, points to the chart as evidence of how quickly Meta has closed the gap with the leading models.

“Damn, gloves are off!,” Volkov [writes on X](https://x.com/altryne/status/2095252967452737785), calling the showing “quite the statement” from Meta while predicting “busy weeks ahead of us!”

> “Damn, gloves are off!”

Cost is another part of Meta’s pitch. Artificial Analysis describes Spark 1.3 xhigh as the “most cost-efficient model” at its level of measured intelligence, with its combination of a 61 Intelligence Index score and comparatively low per-task cost placing it on the company’s Pareto line.

![Intelligence Index vs. Cost per Intelligence Index Task (Credit: Artificial Analysis)](https://cdn.thenewstack.io/media/2026/09/42576232-acost-1024x484.png)

*Intelligence Index vs. Cost per Intelligence Index Task (Credit: Artificial Analysis)*

Artificial Analysis calculates that Spark 1.3 xhigh costs around $0.55 per Intelligence Index task, the lowest of any model scoring 59 or higher on its index. GPT-5.6 Sol max and Grok 4.6 high, both tied with Spark at 61, came in at $0.95 and $0.94 respectively.

Spark 1.3 was still more expensive per task than Spark 1.2’s $0.40, with Artificial Analysis attributing that increase largely to the newer model consuming around 57% more input tokens on agentic evaluations.

![Cost per Intelligence Index Task (Credit: Artificial Analysis)](https://cdn.thenewstack.io/media/2026/09/961395e5-bcost-1024x401.png)

*Cost per Intelligence Index Task (Credit: Artificial Analysis)*

## Muse meets Gemini: A ‘playground slapfight’

It’s worth noting that shortly before Meta unveiled Muse Spark 1.3, Google [released](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) a new low-cost model of its own: Gemini 3.8 Flash, its [third Flash release in just six weeks](https://thenewstack.io/google-ships-its-third-gemini-flash-model-in-six-weeks/). Google also pitched its model as its best reasoning and coding Flash model yet, while keeping introductory pricing at $0.75 per million input tokens and $3.75 per million output tokens.

Artificial Analysis [initially placed](https://artificialanalysis.ai/articles/gemini-3-8-flash) Gemini 3.8 Flash (high) on its Intelligence-versus-Cost Pareto frontier — essentially the group of models for which there is no alternative that is both more capable and cheaper. Gemini [scored 59](https://artificialanalysis.ai/models/gemini-3-8-flash) on the Intelligence Index at a cost of $0.58 per task.

However, just a few hours later, Muse Spark 1.3 xhigh arrived at 61 and $0.55 per task, beating Gemini 3.8 Flash on both measures and pushing it off that frontier.

> “Google was ahead only a few hours.”

This point was not lost on many in the AI community. Indeed, AI researcher [Benjamin Marie](https://www.linkedin.com/in/benjamin-marie-a992b816b/) notes [on X](https://x.com/bnjmn_marie/status/2095251751737971190) that “Google was ahead only a few hours.

[Florian Brand](https://www.linkedin.com/in/florianbrand-de/), a research engineer at AI infrastructure and research company [Prime Intellect](https://www.primeintellect.ai/), also sums up the turnaround succinctly.

“Gemini 3.8 held a spot at the pareto frontier for \*checks notes\* 3.5 hours,” Brand [writes on X](https://x.com/xeophon/status/2095255269060006397).

And none other than Meta’s chief AI officer himself [Alexandr Wang](https://www.linkedin.com/in/alexandrwang/) weighed in, taking the time to cast shade at Google off the back of the Artificial Analysis report.

However, [Corey Quinn](https://www.linkedin.com/in/coquinn/), co-founder and chief cloud economist at cloud and AI cost management company Duckbill, is quick to mock the exchange, suggesting that neither Meta nor Google are meaningfully setting the pace in the AI arms race.   
  
“Meta casting shade at Google in AI is a playground slapfight outside a MMA championship,” Quinn [writes on X](https://x.com/QuinnyPig/status/2095287236397031558).

## Muse Code enters the scene

For context, Muse Spark 1.3 is the fourth version of the model Meta has shipped since April, and follows Muse [Spark 1.1 in July](https://thenewstack.io/meta-muse-spark-api/) and 1.2 the month after. Arguably the more important part of Meta’s push, though, is the agent harness it’s building around the model.

That comes in the form of [Muse Code](https://developer.meta.com/ai/products/muse-code/), Meta’s terminal-based coding agent, which arrived in beta alongside Spark 1.2 [in early August](https://thenewstack.io/meta-muse-code/). It officially launched on Tuesday, replete with new subscription plans starting at just $5 per month and a new SDK also hitting developer preview.

So while Meta is clearly trying to compete with the frontier labs on model quality, evidenced by the gains in the Muse Spark lineup, it’s also chasing them a level up, where Anthropic’s Claude Code and OpenAI’s Codex have set the pace for how developers actually work with an agent day to day.

And this explains why so much of the 1.3 release language centers on coding and agentic work specifically. The model is a key piece of a broader developer platform Meta is now pushing hard on price as much as capability.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)