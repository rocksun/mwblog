Anthropic [announced Friday](https://claude.com/blog/1m-context-ga) that the 1-million-token context window for [Claude Opus 4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) and [Claude Sonnet 4.6](https://thenewstack.io/claude-sonnet-46-launch/) is now generally available, with standard pricing replacing the premium long-context rates that previously kicked in once prompts crossed a certain size threshold.

The company debuted the two models within weeks of each other in February. Claude Opus 4.6 is Anthropic’s flagship model for enterprise workloads that require sustained reasoning across large internal datasets and complex coding tasks. Claude Sonnet 4.6, meanwhile, is the company’s more efficient general-purpose model, designed for high-throughput developer use and production applications that need strong reasoning performance at lower cost than Opus.

Both models shipped with a 1-million-token context window — a limit that allows developers to place very large amounts of information into a single prompt. That can include entire code repositories, lengthy research papers, legal filings, or large collections of internal documents that an AI system needs to analyze together.

There was, however, an important caveat: While the models technically supported prompts approaching the 1-million-token limit, requests exceeding roughly 200,000 tokens were billed at higher “long-context” pricing tiers, moving the entire request into a premium rate band.

That pricing distinction is what Anthropic has now removed.

Under the new arrangement, requests are billed at the same per-token rate regardless of prompt size. A prompt containing hundreds of thousands of tokens is now priced using the same per-token rate as a much smaller request.

## The road to 1 million tokens

Anthropic’s move toward million-token context windows has unfolded in stages over the past two years.

Earlier Claude models launched with a 200,000-token limit, already one of the largest publicly available context windows at the time. When Anthropic introduced the [Claude 3 family in early 2024](https://www.anthropic.com/news/claude-3-family), the company noted that the models were technically capable of processing inputs exceeding one million tokens, though access to those larger contexts was initially limited to “specific use-cases” and available only on request.

The first public release of a 1-million-token window [arrived in August 2025](https://thenewstack.io/anthropics-claude-sonnet-4-model-gets-a-1m-token-context-window/), when Anthropic introduced the capability in Claude Sonnet 4. The jump represented a fivefold increase over the earlier Sonnet models, albeit with a tiered pricing structure tied to prompt size.

It’s also worth noting that Anthropic was, in some respects, playing catch-up: [both Google](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) and [OpenAI had already](https://thenewstack.io/openai-releases-new-models-trained-for-developers/) introduced models capable of handling prompts approaching one million tokens.

Still, the million-token milestone has become an increasingly visible benchmark among AI model providers. Larger context windows allow models to process longer documents or broader datasets without breaking the task into multiple steps.

Under the current pricing, Claude Opus 4.6 costs about $5 per million input tokens and $25 per million output tokens, while Claude Sonnet 4.6 costs roughly $3 per million input tokens and $15 per million output tokens. Previously, Sonnet input pricing rose from about $3 to roughly $6 per million tokens once prompts exceeded the long-context threshold, while Opus input pricing increased from about $5 to around $10 per million tokens. Output token pricing also rose under the premium tier.

Anthropic said the 1-million-token context window is available on the Claude Platform natively and through Amazon Bedrock, Google Cloud’s Vertex AI, and Microsoft Foundry. Claude Code Max, Team, and Enterprise users running Opus 4.6 will also get the full 1-million-token context window by default.

## What cheaper long prompts change for developers

For developers, the removal of the long-context surcharge could influence how applications are designed.

A popular mechanism for keeping costs down has been to minimize the amount of information sent to a model at once. Retrieval systems — which pull only the most relevant snippets of data — became a common architectural pattern partly because sending very large prompts could quickly become expensive.

With the premium tier gone, so is that constraint. Developers can still rely on retrieval systems to manage token usage, but they may also choose to send larger bodies of information directly to the model when a broader context is useful.

That could make certain workflows simpler. Instead of chunking documents into smaller segments or orchestrating multiple model calls, developers can sometimes place a larger slice of data into a single prompt and ask the model to reason across it.

For AI-native coding tools, this approach is particularly attractive. A model with access to a large context window can inspect more of a codebase at once — including multiple files, documentation, and previous conversations — which can improve tasks such as debugging, code refactoring, or generating pull requests.

[Brad Feld](https://www.linkedin.com/in/bfeld/), Techstars co-founder and venture capitalist, said the larger context window can remove some of the engineering workarounds developers previously needed to manage limited context sizes.

“The 1M token context window for Claude Code changes the engineering calculus completely,” Feld [writes](https://www.linkedin.com/posts/bfeld_the-1m-token-context-window-for-claude-code-activity-7438444810929336320-ExTT/) in a LinkedIn post. “I built four markdown state machines totaling 4,700 lines to manage my development workflow — from ticket to deployment. Most of that complexity existed because of the 200K context limit.”

With a larger window, he writes, many of those mechanisms become unnecessary.

“With 1M tokens, reliability is largely solved by having enough room. The constraint shifts to wall-clock speed — and speed comes from parallelism.”

Translated, the model now has enough memory to keep track of long tasks, and the main bottleneck becomes how quickly it can process all that information.

It’s worth stressing that removing the surcharge doesn’t make large prompts free. Token usage still increases with input size, and developers must weigh this cost against other architectural approaches.

But by eliminating the pricing threshold, Anthropic has made long-context workloads easier to experiment with — and potentially easier to deploy in production systems.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)