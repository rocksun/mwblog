**As more companies plug AI agents into the deepest depths** of their internal data banks, how can they be sure those agents *actually* understand how the business works? Right now, many of these organizations are stuck manually building a Markdown file, hoping they find time to rewrite it each time the business changes.

[**Modus**](https://www.getmodus.com/), for its part, thinks it has found a better way. The startup that formally exits stealth this week with $10 million in funding in tow is building what is [coming to be known](https://posthog.com/blog/what-is-a-context-warehouse) in industry parlance as a “context warehouse” — a layer that sits alongside a company’s existing data warehouse, continuously mapping how the business operates across its systems, and handing an AI agent only the relevant slice of that map when it needs it.

In real terms, Modus crawls relevant assets from sources like GitHub, dbt, Jira, Snowflake, and Postgres, using what it calls a Context Miner to continuously learn how the business operates. What it finds gets turned into “dynamically generated skills”: Short, purpose-built briefs, assembled in real time by a second system, the Context Composer, and handed to an agent the moment it’s given a task.

Modus co-founder and CTO [Tomer Mesika](https://www.linkedin.com/in/tomer-mesika-0aa7b242/) tells *The New Stack* that this mining runs continuously, guided by its own internal logic for what to check and how often.

“We have a lot of mechanisms in place to know what to mine from the organization, at what cadence, how to look for deltas, when to dive deeper in, and when not to,” Mesika says.

> “We have a lot of mechanisms in place to know what to mine from the organization, at what cadence, how to look for deltas, when to dive deeper in, and when not to.”

[Daniel Shimoni](https://www.linkedin.com/in/danielshimoni/), Modus co-founder and CEO, draws a direct line to data warehousing to highlight the gap he’s trying to close. Companies have spent years building infrastructure to store and organize their data, he argues, but nothing equivalent exists for the understanding that sits atop it.

“There’s a logic behind data warehouses — companies already know that is where they manage their data,” Shimoni tells *The New Stack*. “But where do they manage their context? Where do they actually understand what contexts exist in their organization, that they can actually use to ensure agents only have what they need?”

![Modus founders Tomer Mesika (CTO) and Daniel Shimoni (CEO)](https://cdn.thenewstack.io/media/2026/07/bc80492e-daniel-tomer-1-1024x683.jpg)

*Modus founders Tomer Mesika (CTO) and Daniel Shimoni (CEO)*.

Shimoni says even that first step is hard enough on its own. But keeping a company’s context accurate as the business changes is harder still.

“We’ve noticed that building the context the first time is already a challenge, but maintaining it is the bigger issue,” Shimoni says. “So Modus always learns from what the company is doing, and whenever something shifts or changes in the business, it makes sure that only the relevant and updated context is fed to agents.”

> “Building the context the first time is already a challenge, but maintaining it is the bigger issue.”

## Who’s buying, and why cost matters

Shimoni says Modus is targeting engineering teams, the CTO office, and VPs of R&D, as well as data teams and a newer category of AI teams.

“AI teams weren’t really around last year; it seems that a lot of data teams are transitioning to becoming VP of data and AI, or AI enablement,” Shimoni says. “So really, it’s the people who are in charge of having this AI enablement mandate in the organization, making sure AI is scaled in the organization.”

Pitching enterprises a shiny new context warehouse becomes much easier when the promise is steeped in helping them [cut costs](https://thenewstack.io/how-cut-ai-costs/). Spend has become one of the defining anxieties of enterprise AI this year, with companies [switching providers in pursuit of cheaper models](https://thenewstack.io/lindy-deepseek-anthropic-switch/), to entire [economic models being built around the price of a token](https://thenewstack.io/tokenomics-foundation/).

> “You want the bigger models to do the heavy and complex tasks to get great value. The problem is that they are wasting a lot of their effort and a lot of their token usage on menial tasks.”

Mesika says this is a central component of Modus’s *modus* *operandi*, arguing that frontier models end up spending a chunk of their token budget on work unrelated to actually answering a question.

“You want the bigger models to do the heavy and complex tasks to get great value,” Mesika says. “The problem is that they are wasting a lot of their effort and a lot of their token usage on menial tasks.”

Those menial tasks, in Mesika’s telling, include combing through pull requests or Jira tickets just to determine what’s relevant before an agent can start the job it was assigned to.

One approach to this problem is to hand the sorting work to a smaller, cheaper model. Mesika says Modus takes that further: rather than retrieving that context at the moment a question is asked, it uses small language models alongside search engines, vector search, and a graph database, all built up in advance, to do that work continuously in the background. By the time an expensive frontier model gets involved, it’s only ever handed a finished brief of exactly what it needs.

![Modus dashboard](https://cdn.thenewstack.io/media/2026/07/6399950e-context-warehouse--1024x661.png)

*Modus dashboard*

## “Everyone’s talking about context”

Shimoni and Mesika both come from data-centric companies — [Lusha](https://www.lusha.com/hp/), a go-to-market data platform, and [Cyera](https://www.cyera.com/), a cybersecurity data company, respectively — before leaving their roles in September 2025 to start Modus together.

The two had known each other for years, and spent much of the previous year comparing notes on a problem they were both running into in very different jobs.

> “We decided this is a problem worth solving, and it seems like we were spot on, because everybody’s talking about context.”

“Some of the challenges were very similar — how do we combine a lot of various data assets into one place where AI can work?” Shimoni says. “We just started to notice that this is the gap — to make AI run with confidence, at scale, across a company. We decided this is a problem worth solving, and it seems like we were spot on, because everybody’s talking about context.”

Modus closed a hitherto unannounced $10 million seed round shortly after founding, led by Insight Partners. Other backers include Soma Capital and a handful of angel investors, among them founders from Cyera and Wix.com. The company began hiring its first employees in January 2026.

The broader takeaway from Modus’s pitch is now among the most common refrains emanating from AI circles this year: that the [model itself is no longer the bottleneck](https://thenewstack.io/ai-agent-infrastructure-bottleneck/); what limits an AI system now is everything built around it. And for Modus, that realization has been more or less present since its inception.

“Even last year […] we could already see that model capabilities weren’t the bottleneck,” Shimoni says. “It was more making sure that they actually have access to the context they need in order to give you the right answers.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)