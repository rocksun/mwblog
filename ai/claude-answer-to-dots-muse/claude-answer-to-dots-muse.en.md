*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

OpenAI launched [Dots at DevDay](https://thenewstack.io/openai-dots-gpt6-agents/) on Tuesday. Each Dot is an always-on agent with its own cloud computer and browser, hooked into the 4,000-plus apps that already connect to ChatGPT. In OpenAI’s own example, a Dot sees a bug alert land in Slack and starts digging in on its own. Cool.

And before Dots, Meta launched Muse, and it’s crushing the mobile install numbers previously set by ChatGPT. And before Muse, xAI shipped its version, Grok Bot, in August.

Anthropic’s version, though different in a couple of ways, [arrived two weeks ago as an update to Claude,](https://thenewstack.io/claude-cowork-vs-chatgpt-work-benchmark/) and without a cute name or fuzzy mascot. This update folds Cowork, which has worked since July [to run scheduled jobs after a user closes their laptop](https://thenewstack.io/claude-cowork-cloud-mobile/) without being asked, into the main Claude app.

Anthropic made the right call with Cowork, whether or not it ever matches Muse’s downloads. Always-on agents are too young to have a winner, and the moats are shallow. A feature one lab ships tends to show up at its rivals within weeks or months. Meta needs Muse to be a blockbuster. Anthropic needs the people already building with Claude to hand it real, recurring work and keep coming back. Repeat use and finished jobs matter more than a flashy launch.

## Always-on agents are too early to have a winner

This wave of always-on personal agents took off less than a year ago. Peter Steinberger pushed a weekend project called Clawdbot to GitHub last November. It lived on a spare computer, took prompts over WhatsApp or Telegram, and relied mostly on Claude. Anthropic [sent the lawyers in January](https://laravel-news.com/clawdbot-rebrands-to-moltbot-after-trademark-request-from-anthropic), so [it became Moltbot](https://thenewstack.io/moltbook-the-singularity-or-hype/), then OpenClaw a couple of days later. It turned into a security headache, and in February Steinberger joined OpenAI. On Tuesday, the foundation that runs the project [released an early, pre-1.0 version of OpenClaw Enterprise](https://thenewstack.io/openclaw-enterprise-kubernetes-agents/) for companies to try internally.

Ten months, three names, one OpenAI hire and an enterprise edition. Ideas move between these products faster than ever. Meta’s Nat Friedman [said Muse was heavily inspired by OpenClaw](https://thenextweb.com/news/meta-muse-openclaw-friedman-soul-md), and users digging through Muse found a SOUL.md personality file nearly identical to OpenClaw’s.

A feature one lab ships shows up at its rivals within months.

Where an early version of each AI assistant and agent feature launched, and who offers one now.

| Feature | Example of an early launch | Now also at |
| --- | --- | --- |
| Deep research reports | Google Gemini (Dec. 2024) | OpenAI, Anthropic, Perplexity |
| Terminal coding agent | Claude Code (Feb. 2025) | OpenAI Codex, Gemini CLI, Meta Muse Code |
| Agent personality file | OpenClaw (SOUL.md) | Meta Muse |
| Agent with its own work identity | Anthropic Claude Tag (June 2026) | OpenAI specialist Dots (preview) |
| Chat and agent work in one window | OpenAI Work mode (July 2026) | Claude (Sept. 2026) |

Anthropic’s September merge is on the list above as a copier, two months behind OpenAI’s Work mode — though Cowork’s cloud and scheduled-task features shipped July 7, two days before Work mode. Jessica Wachtel [tested both on our site](https://thenewstack.io/claude-cowork-vs-chatgpt-work-benchmark/) across three developer tasks and found them tied on accuracy, with ChatGPT faster and Claude more thorough. When a product is this young, a me-too launch is how a lab gets its own users in the room to see what they do with it.

Muse is a hit. Counting only iOS, [Apptopia estimated 359,000 daily U.S. users](https://techcrunch.com/2026/09/21/metas-muse-is-outpacing-chatgpts-early-mobile-launch/) in Muse’s first 12 days, compared with 231,000 for ChatGPT’s iOS app at the same point. Sensor Tower [estimated](https://techcrunch.com/2026/09/25/meta-is-putting-its-muscle-behind-muse-as-the-ai-app-takes-off/) more than 3.4 million downloads as of September 24, though other firms’ counts vary.

Meta needs this. Its Reality Labs division spent tens of billions of dollars on the metaverse without a mainstream product to show for it. Llama 4 landed so flat last year that Zuckerberg rebuilt his AI division around a new superintelligence lab, notably taking a 49% stake in Scale AI and hiring its founder Alexandr Wang.

Muse is the first product from that rebuild to break through, and it got there on Meta’s user base: Apptopia found that more than 95% of Muse users also use Facebook. Muse has a free tier, paid plans at $20 and $100 a month, and connectors to Shopify and Stripe checkout, enabling agents to buy things. Meta’s route runs through scale. Scale has a downside, too. Janakiram MSV explains for TNS [why Amazon started blocking Muse](https://thenewstack.io/amazon-meta-muse-block/) two weeks after launch, and it’s well worth your time because this is a new wedge in ecommerce.

OpenAI and xAI started at the paid end. The price of entry for Dots? A ChatGPT Pro plan at $100 to $500 a month, or a Business Premium or Enterprise account. Sam Altman called Dots a premium product because each one needs so much compute. Grok Bot reached 418,000 weekly users by mid-September, [per Bloomberg](https://www.bloomberg.com/news/articles/2026-09-22/spacexai-s-grok-bot-agent-tops-400-000-users-after-first-month), and xAI just launched Team Bots on Monday.

Neither company needs Meta’s install base to learn something useful. Paying customers already spend money on AI, and retention will show whether they keep using the agent once the novelty wears off.

## Anthropic shipped its version to the people already building with Claude

Anthropic did what I’d expect from labs right now. It shipped fast, shipped to paying subs, and put the agent inside the app those people already use. The merged Claude hit Pro and Max customers, with Team and Free plans coming soon. Teams have had [Claude Tag in Slack since June](https://thenewstack.io/anthropic-claude-tag-slack/), a proactive teammate with its own identity and audit trail. Cat Wu said an internal version accounts for about [65% of the product teams’ code changes](https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive). Developers have had Managed Agents for hosted, long-running agents since April.

What Anthropic hasn’t done is put Claude where Muse lives. Muse works inside Meta-owned WhatsApp, but Claude still asks you to open the Claude app or tag it in Slack. That workflow might matter for mainstream consumers. Teams wiring an agent into their code care more about what it can touch. Jani [laid out the difference](https://thenewstack.io/persistent-ai-agent-identities/) on our site in August: Grok Bots share one cloud computer and one set of logins across the whole roster, while Claude Tag joins a Slack workspace with its own service identity and channel-scoped access. Before handing agents your logins, know what you’re getting into.

Those are the users Anthropic should want. Writers on *Towards Data Science* have spent the year showing what builders do with always-on agents. [Samir Saci put a team of OpenClaw agents](https://towardsdatascience.com/i-simulated-an-international-supply-chain-and-let-openclaw-monitor-it/) on a supply chain simulation to chase down late shipments. Eivind Kjosbakken’s [guide to running a fleet](https://towardsdatascience.com/how-to-orchestrate-a-fleet-of-openclaw-bots/) of OpenClaw bots walks through nightly QA bots that test an app and report bugs, plus agents that check invoices. Both ran their agents on OpenAI’s Codex. OpenAI runs its own OpenClaw agent, Androidclaw, that traces broken builds and, in some cases, merges the fix, [*VentureBeat* reported](https://venturebeat.com/orchestration/openclaw-launches-free-enterprise-control-plane-for-persistent-ai-agents-backed-by-openai-red-hat-and-nvidia). Anthropic needs that kind of work running on Claude.

I set up OpenClaw on an old Mac Mini this spring, and I had so many questions (and breakthroughs). That’s why builders, coders, and developers are critical to product development: They ask these questions out loud in GitHub issues and Discord threads, and the answers end up in the product.

The obvious objection is trust. It’s fair. An always-on agent holds credentials and acts while nobody is watching. xAI’s own documentation tells users not to treat Grok Bots as a security boundary, and the OpenClaw Foundation says most IT departments ban agent platforms outright. Anthropic’s defaults lean cautious: Claude asks before it acts unless you tell it otherwise, and Tag keeps its own audit trail. If builders don’t come back, or each finished task takes more supervision than doing it themselves, the experiment hasn’t worked. But if they keep finding useful work to hand off, their questions and breakthroughs become the roadmap.

That’s the race that matters for Claude, Dots and Muse: becoming the agent people trust with the next job.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)