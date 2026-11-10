AI coding agents have certainly made it easier to transform an idea into a working application. However, getting that application off a local machine and into the hands of real users remains a hurdle, requiring essential infrastructure steps spanning everything from hosting and database provisioning, to critical security checks.

Cursor, the AI coding platform acquired by Elon Musk’s SpaceX for [$60 billion](https://uk.finance.yahoo.com/news/spacex-completes-record-60-billion-131413932.html) back [in August](https://cursor.com/blog/joining-spacex), [acknowledged the problem](https://x.com/cursor_ai/status/2118458629091426304) in an X post published on Thursday.

“Agents have made it easier to write code, but most apps never make it off localhost,” the company notes.

To address this, Cursor [is introducing](https://cursor.com/changelog/build-live-apps) new [app-building and deployment functionality](https://cursor.com/docs/cloud-agent/apps), designed to take AI-generated applications from development to a live, shareable URL, without users having to even think about the underlying infrastructure themselves.

> “Agents have made it easier to write code, but most apps never make it off localhost.”

## Built on cloud agents

The new feature is built around [cloud agents](https://cursor.com/cloud), which Cursor [introduced last year](https://cursor.com/blog/cloud-agents) as a way for developers to run multiple AI coding agents remotely without having to keep their laptops engaged. At the time, the company highlighted their ability to fix bugs, handle smaller coding tasks and implement some complex features.

With this latest update, those same agents can now take applications all the way through to deployment, handling the important steps needed to make them accessible to other users. The functionality is only available through cloud agents, though, which means it can’t be used with agents running locally.

Users start by describing the application they want to build in natural language, with Cursor managing the code generation and development process as usual.

![1. Prompt Cursor as usual](https://cdn.thenewstack.io/media/2026/11/ce19aa68-gif1.gif)

*1. Prompt Cursor as usual*

From there, the agent creates the application and sets up the underlying project, including the necessary components to get it running.

![2. Cursor's agent builds the application](https://cdn.thenewstack.io/media/2026/11/9632b6e7-gif2.gif)

*2. Cursor’s agent builds the application*

Once the application is ready, users can preview the result before deciding whether to hit publish.

![3. Preview the app before publishing](https://cdn.thenewstack.io/media/2026/11/38bbe001-gif3.gif)

*3. Preview the app before publishing*

Publishing makes the application accessible through a live URL, allowing users to share it with colleagues or other users without having to configure hosting themselves.

![4. Share the app via a live link](https://cdn.thenewstack.io/media/2026/11/7005f0ac-gif4.gif)

*4. Share the app via a live link*

It’s worth noting that there are two ways to get started. Users building an application from scratch will automatically have a new repository created on [Cursor Origin](https://cursor.com/origin), the company’s [Git-based code-hosting platform launched in August](https://thenewstack.io/cursor-origin-github-alternative/) as an agent-centric alternative to GitHub.

Alternatively, users can deploy applications from an existing GitHub repository. This means developers who already have an application under development can use Cursor’s cloud agents to prepare and publish it, without having to move their code to Origin or set up deployment infrastructure manually.

Judging by Cursor’s [own examples](https://cursor.com/changelog/build-live-apps), the feature seemingly targets employees who need to create internal business applications, such as sales dashboards, onboarding programs, customer presentations and developer portals. So in that regard, it could prove a boon for non-developers who have an idea for a tool but lack the technical nous to get it running themselves.

Of course, there’s nothing restricting the feature to business applications. An aspiring vibe coder could just as easily create a neighbourhood football league tracker or interactive family holiday planner. And because individual subscribers can publish apps publicly, those creations can be shared with anyone who has the link.

## Under the hood: hosting, databases and security

Cursor had actually begun closing this gap, when in August [it introduced the ability](https://cursor.com/changelog/start-from-scratch) to preview cloud-agent projects and publish them to a live URL. However, users still needed to connect their own Vercel accounts.

![Cursor's earlier app-building feature, introduced in August 2026.](https://cdn.thenewstack.io/media/2026/11/1b2de6db-gif5.gif)

*Cursor’s earlier app-building feature, introduced in August 2026.*

The latest release removes that requirement while introducing various new smarts to the mix.

Behind the scenes, Cursor now takes care of several infrastructure requirements, including hosting, databases, and authentication.

For hosting, Cursor automatically creates a dedicated account for each team or individual subscriber, isolated from other customers. While Cursor’s announcement doesn’t identify the underlying hosting provider, Vercel [revealed in a separate response](https://x.com/vercel/status/2118464668444557411) on X that the new functionality is built on its [Vercel for Platforms infrastructure](https://vercel.com/for/platforms). This basically allows users to deploy applications without having to create their own Vercel accounts or configure hosting themselves.

If an application needs a database, Cursor provisions one using PostgreSQL, while private and team applications are protected by Cursor’s existing sign-in system. Individual subscribers can also make their apps publicly accessible.

Applications can connect to external services, such as company databases or data warehouses, with users supplying the necessary credentials. Cursor says these secrets are managed separately, meaning the AI agent never sees their actual values.

Then there’s the thorny issue of security. When users choose to publish an application, Cursor says it runs “a series of deterministic and agentic security checks” before allowing it to go live. These include mandatory checks for exposed credentials, secrets and sensitive files, alongside an AI-powered review intended to identify more serious vulnerabilities.

However, it’s unclear how reliably these automated checks can identify more complex problems, such as incorrectly configured database permissions or application-level access controls. This is an important consideration for organisations contemplating connecting AI-generated applications to sensitive internal systems, where additional security scrutiny would still be advisable.

There is precedent for such concerns, too. In May last year, [Semafor reported](https://www.semafor.com/article/05/29/2025/the-hottest-new-vibe-coding-startup-lovable-is-a-sitting-duck-for-hackers) that two Replit employees examined 1,645 Lovable-built applications and discovered that 170 of them exposed sensitive information. The problems involved incorrectly configured database permissions, highlighting the difficulties of securing applications created through AI tools. Lovable says it [subsequently introduced](https://lovable.dev/blog/secure-vibe-coding) further security checks to identify potential vulnerabilities before applications are published.

## Cursor moves onto Lovable and Replit’s turf

Of course, Cursor is entering territory already occupied by the likes of [Lovable](https://lovable.dev/) and [Replit](https://thenewstack.io/replit-shopify-storefront-integration/), which allow users to create and publish applications through natural-language prompts.

While Cursor’s latest announcement emphasizes internal business tools, Lovable and Replit have traditionally appealed to a broader audience of aspiring application creators. Still, the overlap is clear, and Cursor’s move into deployment has already caught the attention of developers.

> “Cursor just came for the localhost graveyard.”

One software engineer [writes on X](https://x.com/thecsguy/status/2118482491900076141?a=XUyRWnUp9QtfP70Fq5E&s=20) that “*cursor just came for the localhost graveyard*,” riffing on Cursor’s own messaging about AI-generated applications that never make it beyond local development.

There’s also an interesting overlap with [Grok Build](https://grok.com/build), particularly given SpaceX’s acquisition of Cursor in August.

SpaceXAI introduced [Grok’s Build Mode in July](https://x.ai/news/grok-build-mode), before expanding it to all Grok plans the [following month](https://x.ai/news/grok-build-for-everyone). The feature allows users to create apps, games and websites directly inside a Grok conversation, then publish them to shareable grok.me links.

That bears something of a resemblance to Cursor’s latest offering, although Cursor is approaching it through its established coding environment and cloud agents, and with a stronger emphasis on business applications and managed infrastructure.

The overlap hasn’t gone unnoticed though. One X user [responded to Cursor’s announcement](https://x.com/amsultan2010/status/2118459411437895889?a=fRQ4Odh-YGNBjve3A58&s=20) by asking, “*so cursor is now properly replacing grok build*?”

There’s no indication that Grok Build *is* being replaced, but the two offerings now cover some notably similar ground, raising questions about how SpaceXAI intends to distinguish them going forward.

For those wanting to check out Cursor’s new functionality, it’s available on *all* paid Cursor plans with cloud agents enabled.

With deployment increasingly becoming part of the AI coding experience, Cursor’s latest move could put further pressure on dedicated app-building platforms as the distinction between tools aimed at professional developers and those targeting aspiring vibe coders continues to narrow.

[Vibe Coding
Step-by-step guide to master Vibe Coding in 2026

What is vibe coding?
The vibe coder mindset
Plan before you Code
Tech Stack and Coding
Prompting Best Practices
Context
Debugging
Master Version Control
Testing
Security Best Practices](https://roadmap.sh/vibe-coding?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=cursor-ai-app-deployment)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)