Developers are paying closer attention to how much their AI coding tools cost them to run, and for good reason. GitHub recently moved Copilot to usage-based billing tied to the model you pick, while elsewhere, an AI agent startup said [switching from Anthropic to DeepSeek](https://thenewstack.io/lindy-deepseek-anthropic-switch/) would save it millions of dollars.

Against that backdrop, developers have been looking for ways to cut token consumption by reducing wasteful filler and padding in AI replies. The goal, ultimately, is to get the agent to answer as directly as possible, in as few words as possible, without losing any of the substance. This has seemingly come to be known as “caveman mode” — dropping articles and grammar in favor of short, blunt fragments, in the style of the stereotypical grunting caveman of old sitcoms and cartoons.

In truth, some developers will likely recognize this from [The Grug Brained Developer](https://grugbrain.dev/), a long-running essay on software design by [Carson Gross](https://bigsky.software/cv/), creator of [htmx](https://htmx.org/), written entirely in the same broken, blunt style. But this time around, the target isn’t code complexity; it’s verbosity in an AI’s replies.

## “Skill make agent talk like caveman”

The idea has surfaced in different forms. Enterprise search giant Elastic built its own version for Elasticsearch, reporting a 63.6% average token reduction across eight internal test scenarios.

[Sri Kolagani](https://www.linkedin.com/in/sriharideep/), director of Salesforce engineering at Elastic, [writes in an April blog post](https://www.elastic.co/search-labs/blog/elastic-caveman-ai-token-reduction) that the conversational padding that LLMs wrap around answers carries a real cost when querying Elasticsearch, where what you actually need are index names, field mappings, and ES|QL queries, not pleasantries.

“This isn’t just annoying; it’s expensive,” Kolagani writes. “Every token costs money and adds latency. For production Elasticsearch queries, that overhead compounds fast.”

However, the tool that properly went viral was a free, installable Claude Code skill [on GitHub](https://github.com/juliusbrussee/caveman), built by the Netherlands-based developer [Julius Brussee](https://www.linkedin.com/in/julius-brussee/). It picked up tens of thousands of stars and forks, generating front-page discussions on online communities [such as Hacker News](https://news.ycombinator.com/item?id=47647455) in the process.

> “This isn’t just annoying; it’s expensive. Every token costs money and adds latency. For production Elasticsearch queries, that overhead compounds fast.”

Its pitch, in its own Caveman vernacular:

“Skill make agent talk like caveman. Why use many token when few do trick. Filler die. Code, commands stay byte-exact.”

And its headline claim? A 65% cut in output tokens.

## Caveman-talk savings, put to the test

[JetBrains](https://www.jetbrains.com/), the [company behind IDEs](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/) including IntelliJ and Rider, decided to test that specific skill rather than take its 65% headline saving at face value.

Using [Harbor](https://www.harborframework.com/), an open-source agent evaluation framework, and tasks from [SkillsBench](https://www.skillsbench.ai/), a community benchmark built to measure how much AI agent skills actually help, JetBrains engineer [Denis Shiryaev](https://www.linkedin.com/in/dshiryaev/) [writes in a July blog post](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/) that they ran a paired benchmark across 86 real coding tasks on Claude Code, comparing the skill activated against a stock, unmodified session.

The gap between the claim and the result was not insignificant. Advertised saving: 65%. What JetBrains actually measured: 8.5%, a figure that only held once the test scaled up. Indeed, an early run on just 10 tasks initially indicated something closer to 30%.

The shortfall ultimately boils down to what the skill can and can’t handle in real coding projects, versus the kind of casual chatbot exchange its headline number was measured against.

> “Advertised savings come from chat-style prose answers. Agentic output is different.”

“Advertised savings come from chat-style prose answers. Agentic output is different,” Shiryaev writes, noting that code, diffs, tool invocations, and exact error strings dominate the token stream, something the skill leaves verbatim. “Only the narration between tool calls gets compressed, and there is not much of it,” he adds.

## Does talking like a troglodyte make Claude dumber?

It’s a concern that came up almost immediately when the skill first went viral, with [commenters on Reddit](https://www.reddit.com/r/ClaudeAI/comments/1sble09/taught_claude_to_talk_like_a_caveman_to_use_75/) raising concerns that forcing an AI model to answer in a stripped-down, less articulate register might come at the cost of its ability to reason.

JetBrains’ benchmark suggests that worry doesn’t hold up, at least not in the tasks it tested. Task outcomes across the 86 paired runs were statistically indistinguishable between the skill-activated and stock sessions.

Shiryaev’s overall verdict of Caveman was that it’s “safe, honest about style, [but] oversold on savings.”

“Use it if you like it,” Shiryaev writes in that blog post. “It is fun, and it costs you nothing measurable in quality. Just do not expect huge savings on daily agentic tasks: a high-single-digit percentage is the realistic ceiling.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)