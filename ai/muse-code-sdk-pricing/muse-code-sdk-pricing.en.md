**Meta [has formally](https://developer.meta.com/ai/resources/blog/muse-code-new-plans-and-features/) launched [Muse Code](https://developer.meta.com/ai/products/muse-code/) out of beta**, less than a month after first [debuting the coding agent](https://thenewstack.io/meta-muse-code/).

Alongside a host of new features and an SDK, Meta has introduced a trio of new subscription plans ranging from $5 to $50 per month, adding predictable monthly pricing to a product that already stood out at launch for aggressively undercutting rival coding agents on cost.

Powered by Meta’s own [Muse Spark 1.2 model](https://developer.meta.com/ai/models/muse-spark/), Muse Code is effectively Meta’s answer to Anthropic’s Claude Code and OpenAI’s Codex: a terminal-based coding agent designed to handle complex software engineering tasks across large codebases.

In its initial guise, Muse Code already included asynchronous background agents that remain active throughout a coding session to gather information and support the main agent. Meta also pitched it as capable of handling long-running engineering tasks across large repositories, from planning a change through to writing and validating the code.

For its full public launch, Meta has added several new capabilities. One is inter-session messaging, which lets separate Muse Code sessions share context and state directly when their work overlaps.

![Inter-session messaging in Muse Code](https://cdn.thenewstack.io/media/2026/09/7b600f4b-gif-1-1intersessionmessaging.gif)

*Inter-session messaging in Muse Code*

On top of that, Meta has also introduced Workflows, which builds on the existing multi-agent capability by orchestrating teams of specialized agents across larger jobs, carrying intermediate work between stages and returning a single result at the end. Developers can also monitor and steer the agents through a dedicated Workflows control room.

Another notable addition is a rewind feature, which allows developers to roll back the conversation and code changes to an earlier point in a Muse Code session.

![Rewind in Muse Code](https://cdn.thenewstack.io/media/2026/09/905a22b7-rewindgif.gif)

*Rewind in Muse Code*

## The pricing factor

One of the more contentious aspects of Muse Code at launch was its pricing setup. At the time, Meta offered two pay-as-you-go tiers. Its Standard tier charged $1.25 per million input tokens and $4.25 per million output tokens, while the so-called “Contributor” tier scythed those rates to just $0.10 and $0.20, respectively. The catch, of course, was that Contributor users had to opt in to having their prompts and completions used to help improve Meta’s products, a trade-off several engineering leaders [told *The New Stack* at the time](https://thenewstack.io/meta-muse-code/) would rule it out for their proprietary code.

> “One of the more contentious aspects of Muse Code at launch was its pricing setup.”

Price doesn’t tell the whole story, however. *The New Stack* [ran Muse Code and Claude Code](https://thenewstack.io/meta-muse-claude-code/) through the same three coding tasks. While Muse Code cost much less, it consumed substantially more tokens and produced a weaker result on a refactoring task, leaving dead code behind on another. That raised a broader question around how much its price actually tells developers about the cost of getting useful work done.

With the full launch, Meta has introduced a trio of subscription tiers alongside its existing pay-as-you-go options.

The Everyday Usage plan costs $5 per month; High Usage costs $15 and promises three times as much usage; and the $50 Power Usage plan offers 10 times as much usage. Meta says the $5 plan typically provides 10 to 50 requests every 5 hours, though the number varies with the complexity of the work.

![Muse Code subscription pricing](https://cdn.thenewstack.io/media/2026/09/77b02204-pricingtier-1024x391.webp)

*Muse Code subscription pricing*

That puts Muse Code well below its main rivals on headline subscription price. Anthropic includes Claude Code with its $20-a-month Pro plan, while its $100 Max 5x and $200 Max 20x plans provide 5x and 20x Pro’s per-session usage, respectively. OpenAI follows a similar approach: Codex is included with the $20 Plus plan, while its $100 and $200 Pro tiers provide 5x and 20x the usage of Plus, respectively.

However, the actual amount of coding work those plans buy is harder to compare. Anthropic doesn’t currently publish an absolute number of Claude Code prompts for Pro, Max 5x, or Max 20x; instead, it expresses the two Max allowances as multiples of Pro. It also applies five-hour and weekly limits. OpenAI, on the other hand, is a little more helpful [with its pricing page](https://learn.chatgpt.com/docs/pricing): For GPT-5.6 Sol, it estimates 10–100 local Codex messages every five hours on Plus; 50–500 on Pro 5x; and 200–2,000 on Pro 20x. Even then, OpenAI says actual usage varies with factors such as the model, task complexity, context, reasoning, and tools, so Meta’s 10-to-50-request estimate still doesn’t translate neatly into an apples-to-apples comparison.

> “After all the Claude and ChatGPT usage-limit drama, this is refreshingly simple.”

[Muhammad Navaid](https://www.linkedin.com/in/mnavaidd/), a senior machine learning engineer, took to social media on Tuesday to highlight the simplicity of Meta’s proportional pricing structure, in which each price increase maps directly to the advertised increase in usage. “After all the Claude and ChatGPT [usage-limit drama](https://thenewstack.io/claude-code-usage-limits/), this is refreshingly simple,” he [writes](https://www.linkedin.com/feed/update/urn:li:activity:7500515585143844864/) on LinkedIn. “And honestly, this is how AI coding subscriptions should work.”

Others were less enthusiastic about what such low prices might ultimately mean. [Ashok Gelal](https://www.linkedin.com/in/ashokgelal/), co-founder and CEO of Msty AI, describes the pricing as “unbelievably low,” but hints at the data concerns that accompanied Muse Code’s original launch.

“The biggest concern here is Meta itself,” Gelal [writes](http://x.com/ashokgelal/status/2094517356349333543) on X.

## Building on Muse Code

While the new subscriptions change *how* developers pay for Muse Code, another aspect of the public launch expands *what* they can do with it. A [new SDK](https://github.com/meta-models/muse-code-sdk), currently in developer preview, extends Muse Code beyond its command-line interface.

In a post [on X](https://x.com/finkd/status/2094500475710099945?s=20), Mark Zuckerberg notes that the aim is to enable developers to build their own agents on Muse Code.

“Embed them in your apps, connect custom tools, stream progress, and resume sessions later,” Zuckerberg [writes](https://x.com/finkd/status/2094500479866736747?s=20).

In real terms, the SDK lets developers control Muse Code programmatically—meaning their own software can start and resume sessions, send instructions, handle responses, and respond to what the agent does, rather than requiring someone to operate Muse Code manually via the terminal. That could support everything from IDE integrations and internal engineering tools to standalone agentic products built on top of Muse Code.

Meta isn’t alone here. Anthropic’s [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) similarly lets developers build applications around Claude Code’s capabilities, while OpenAI offers a [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) for embedding its coding agent into other tools and services.

Meta has also published the Muse Session Protocol ([MSP](https://github.com/meta-models/muse-code-sdk/tree/main/schema/msp)), the underlying protocol that external clients use to communicate with Muse Code sessions. Developers can use Meta’s TypeScript SDK or implement MSP directly in another language.

The broader significance, perhaps, lies in how quickly Meta is opening Muse Code to third-party development. Less than a month after launching the CLI in beta, it’s already giving developers the tools to embed Muse Code in their own interfaces, applications, and agents.

Meta may be moving fast because it has to. Claude Code and Codex already have a head start, leaving Muse Code with little choice but to compete hard on price and features.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)