What do you do when a technology you’ve become dependent on belongs to someone else? You buy the startup behind it, of course. And that’s exactly what data warehouse company [MotherDuck](https://motherduck.com/) has done with [Tower](https://www.tower.dev/), a data infrastructure startup whose technology was already powering MotherDuck’s AI-built data pipelines.

The deal, announced on Tuesday, is MotherDuck’s first acquisition in its four-year history, bringing both Tower’s technology and team in-house as MotherDuck pushes further into AI agents that can build and operate data pipelines.

## Tower takes flight

Tower was founded out of Germany in late 2024 by ex-Snowflake engineers [Serhii Sokolenko](https://www.linkedin.com/in/ssokolenko/) (CEO) and [Brad Heller](https://www.linkedin.com/in/bradhe/) (CTO). Their pitch: once a developer, or an AI assistant, has written the code for a data pipeline, someone still has to package it, deploy it to the right infrastructure, wire up credentials, and maintain it — the unglamorous work, Sokolenko told *The New Stack* [back in March](https://thenewstack.io/tower-python-data-pipelines/), that amounts to data engineering’s “last mile.”

Tower, essentially, is a managed runtime for Python pipelines — it packages the code, deploys it, and keeps it running in production. It also offers tools built on top of that runtime, like the browser-based AI agent [Tower Control](https://control.tower.dev/) that allows users to describe the pipeline they want in plain language.

![With Tower Control, Tower Control, users can describe the pipeline they want in plain language.](https://cdn.thenewstack.io/media/2026/08/15286e2c-gigf1.gif)

*With Tower Control, users can describe the pipeline they want in plain language.*

Control can then generate the code, deploy it as a Tower app, and run it — effectively taking the process from prompt to production without the developer having to set up the underlying runtime themselves.

![Control can generate the code, deploy it as a Tower app.](https://cdn.thenewstack.io/media/2026/08/b86ca8af-gigf2.gif)

*Control can generate the code, deploy it as a Tower app.*

MotherDuck, for its part, is a serverless data warehouse built on the open-source database [DuckDB](https://duckdb.org/), founded in 2022 by [Jordan Tigani](https://www.linkedin.com/in/jordantigani/), a former engineering lead at Google focused on BigQuery. The company [has raised](https://motherduck.com/blog/announcing-series-seed-and-a/) some $100 million [since its inception](https://techcrunch.com/2023/09/20/database-startup-motherduck-lands-52-5m-to-grow-its-duckdb-based-platform/).

MotherDuck’s [original pitch](https://thenewstack.io/motherducks-hybrid-query-execution-enhances-real-time-data-analytics/) leaned on speed and local compute: queries could run on a laptop via DuckDB, in MotherDuck’s cloud, or across both — a departure from the likes of Snowflake, Databricks and BigQuery’s cloud-first model. More recently, MotherDuck [has extended](https://thenewstack.io/motherduck-duckdb-mcp-collaboration/) that approach to AI agents, using MCP to let agents interact directly with data. And things took a more operational turn in June with the [launch of Flights](https://motherduck.com/blog/flights-agent-native-ingest/), a feature that exposes a general-purpose Python runtime through the same MCP server, letting agents create, run and schedule data pipelines.

And Tower, as it turns out, was the key infrastructure underpinning Flights.

## ‘We became their largest customer almost overnight’

Tower’s involvement with MotherDuck actually predates Flights. Tigani says MotherDuck had initially been looking for a third-party tool it could recommend to customers as an easier way to get data into its warehouses. But then advances in AI changed the nature of the problem the company thought it needed to solve.

> “When AI suddenly started to be able to solve data problems, we realized we were thinking about the problem wrong.”

“When AI suddenly started to be able to solve data problems, we realized we were thinking about the problem wrong,” Tigani tells *The New Stack*. “Claude can solve that problem we were trying to address by writing the connectors to help people move their data, but what it can’t do is the sandboxing and scheduling.”

That left MotherDuck needing somewhere to safely execute the code those agents generated, manage credentials and run jobs on a schedule. And as luck would have it, Tower already provided those capabilities.

“It perfectly solved our problem and let us ship Flights in only a matter of weeks,” Tigani adds.

For MotherDuck, Tower had supplied the missing execution layer; for Tower, that realization translated into a significant customer relationship. “We became their largest customer almost overnight, and our teams have been shipping together ever since,” Tigani says.

Having Tower on its radar so early also gave MotherDuck a chance to test the technology — and the team behind it — before deciding whether to build something similar itself. Tigani says the calculation ultimately came down to how quickly MotherDuck could get the capabilities it wanted into customers’ hands.

“It’s always tempting to build yourself, but after trying out Tower, we realized pretty quickly that there were a bunch of problems we were going to have to solve to make our underlying infrastructure actually work well, and Tower was pretty much exactly what we needed,” he says.

Ultimately, the more central Tower became to what MotherDuck wanted to build, the stronger the case became for owning the technology outright. Once Tower was executing jobs created and scheduled inside MotherDuck, Tigani argues, customers would inevitably hold MotherDuck accountable for the security, reliability and behavior of that runtime.

“There’s a rule I’ve relearned at every infrastructure company I’ve worked at: you can rent a feature, but you can’t rent a foundation,” Tigani says. “When an agent inside MotherDuck builds a job and schedules it, the thing executing that job is our product — whatever logo is on it.”

> “There’s a rule I’ve relearned at every infrastructure company I’ve worked at: you can rent a feature, but you can’t rent a foundation.”

One example of what MotherDuck now hopes to do with that technology involves bringing Flights together with [Dives](https://motherduck.com/docs/key-tasks/dives/), an AI-generated data visualization feature it [debuted in February](https://motherduck.com/blog/duck-dive-and-answer/). Tower can generate stable URLs for jobs running through Flights, effectively allowing those jobs to act as data APIs that a Dive — or another frontend — can call.

Tigani gives the example of an application displaying user recommendations. A Dive could generate the interface for viewing those recommendations, while a Flight could handle requests to create or modify them. Rather than giving the frontend broad write access to the underlying data, the Flight can constrain and validate what changes users are allowed to make.

“When you put them together, you can build rich applications,” Tigani says.

## Tower’s next chapter

All of this raises an obvious question for Tower customers. Part of the startup’s pitch was that developers could use its runtime without tying themselves to a particular data platform, and now Tower itself belongs to one.

Tower co-founder and CEO [Serhii Sokolenko](https://www.linkedin.com/in/ssokolenko/) argues that MotherDuck represents a different kind of home to that of the industry’s larger cloud data platforms. His case is that Tower can become more deeply integrated without being bent around an architecture established long before AI agents entered the picture.

“Joining a hyperscaler usually means adapting to its legacy architecture,” Sokolenko tells *The New Stack*. “Joining MotherDuck lets us help shape where data and AI infrastructure are heading.”

> “Joining a hyperscaler usually means adapting to its legacy architecture.”

There is still a trade-off, though. Tower is giving up some of the breadth that came with being database-agnostic in exchange for building much more specifically around one platform — a bet that tighter integration will ultimately produce a better experience than supporting many systems at arm’s length.

“By focusing Tower’s Pythonic compute specifically on MotherDuck, we’re trading broad, basic connectivity for deep, native execution,” he says.

Sokolenko’s argument is that the “lock-in” question then shifts down a layer. Tower may now be tied much more closely to MotherDuck, but because MotherDuck itself is built on DuckDB, he says the underlying data remains open and portable. The aim is to bring the runtime, agents and warehouse closer together without trapping the data itself inside a proprietary system.

That also helps explain why MotherDuck’s hybrid execution model appealed to Tower. DuckDB lets work move between local and cloud compute, which Sokolenko sees as closely aligned with Tower’s own direction.

“This directly matches Tower’s vision — allowing business users and agents to move seamlessly from local data exploration to cloud production execution,” he says.

For Tower’s existing customers, the immediate future means a move toward MotherDuck. Sokolenko says Tower customers are already in discussions with MotherDuck about migration paths, while people who have used Tower previously will be invited to try MotherDuck and its broader agentic data capabilities.

Tigani confirms that MotherDuck is working to move existing Tower customers onto Flights, though he concedes that the two products aren’t entirely identical. “There are a couple of differences, and we’re working on closing the gaps to make the transition more seamless,” he says.

Tower’s technology will meanwhile be folded more deeply into MotherDuck itself. Today, MotherDuck has two separate sandboxed, on-demand runtimes: Flights, which is backed by Tower, and [Ducklings](https://motherduck.com/docs/about-motherduck/billing/duckling-sizes/), its serverless DuckDB instances. Tigani says the plan is eventually to merge the two, combining the near-instant startup of Ducklings with the more robust sandboxing provided by Tower jobs.

## Surfing the agent wave

MotherDuck is hardly alone in pushing data agents beyond answering questions. Databricks’ [Genie Code](https://www.databricks.com/blog/introducing-genie-code) can generate and run code, build pipelines and debug failures inside Databricks. Snowflake, meanwhile, has been moving in a similar direction [with the likes of CoCo](https://www.snowflake.com/en/news/press-releases/snowflake-unveils-cortex-code-an-ai-coding-agent-that-drastically-increases-productivity-by-understanding-your-enterprise-data-context/), its AI coding agent, while [newer CoCo Automations](https://docs.snowflake.com/en/release-notes/2026/other/2026-08-21-cortex-code-automations-preview) can schedule unattended agent runs inside Snowflake-managed sandboxes.

The details differ, but both point toward a broader shift in the data industry: giving AI agents the infrastructure to act on data and operate the systems around it, rather than simply query what is already there.

> “AI makes it possible to build useful features that we could never fathom five to 10 years ago. The platform is the most complex part of the data estate, and so warehouse vendors are well positioned to be at the center of whatever new patterns emerge.”

Tigani has been predicting something close to this for some time. Earlier this year, [he outlined](https://motherduck.com/blog/water-town-agent-swarm-data-stack/) a future in which data engineering increasingly becomes an agent-supervision problem, with agents handling tasks such as building and repairing pipelines and responding to changes in schemas and data quality, while humans oversee their work. He also [previously likened](https://motherduck.com/blog/future-casting-the-modern-data-stack/) the advance of LLMs to a wave that data companies will have to learn to ride.

“The way I like to think about it is this — data platform vendors are reacting to new opportunities to make lives better for their customers,” Tigani says. “AI makes it possible to build useful features that we could never fathom five to 10 years ago. The platform is the most complex part of the data estate, and so warehouse vendors are well positioned to be at the center of whatever new patterns emerge. The Tower acquisition gives us a platform for deploying, tracking, and scheduling data agents, which should set us up well to surf that wave.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)