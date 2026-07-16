[Prefect](https://www.prefect.io/), best known for the eponymous open-source data pipeline and workflow orchestrator, has [announced](https://www.prefect.io/prefect-acquires-dagster) that it’s acquiring [Dagster](https://dagster.io/), one of the biggest alternatives to [Apache Airflow](https://thenewstack.io/apache-airflow-3-0-from-data-pipelines-to-ai-inference/) alongside Prefect itself.

The deal, which has yet to formally close, folds two of the most established Airflow challengers into a single company. Dagster, the open-source orchestrator, and [Dagster+](https://dagster.io/lp/dagster-plus-trial), the fully managed cloud incarnation, will keep their existing names, pricing, and product roadmaps, with some 40 people from the Dagster team moving over to Prefect as part of the deal.

In a [LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7482460618369753088/) published on Monday, Prefect founder and CEO [Jeremiah Lowin](https://www.linkedin.com/in/jlowin/) explains that the acquisition is a bet on the various components an AI agent needs to run reliably: clearly defined goals, paired with the flexibility to improvise when its own decisions send it down a path nobody scripted.

Dagster, according to Lowin, handles the goal-setting side by defining and tracking outcomes; Prefect handles the improvising by running the work itself; and [FastMCP](https://gofastmcp.com/), Prefect’s own tool for connecting agents to outside systems, controls what those agents are allowed to touchd along the way.

> “The modern orchestration category has a new center of gravity.”

For Lowin, the acquisition is all about creating scale.

“The modern orchestration category has a new center of gravity,” Lowin writes.

## Two become one

That “scale” pitch comes some seven years after Prefect and Dagster competed, both emerging as challengers to Airflow, the default tool most teams used to schedule and run their data pipelines.

Prefect set out to simplify and make production workflow orchestration more reliable for Python developers. Dagster, for its part, focused on making data pipelines easier to define, understand, and verify, placing greater emphasis on what a pipeline should produce rather than simply running a sequence of tasks.

> “For years, Prefect and Dagster have raised the bar for each other and our category. That competition produced two exceptional products and two of the strongest open-source communities in the data ecosystem.”

“For years, Prefect and Dagster have raised the bar for each other and our category,” Lowin writes. “That competition produced two exceptional products and two of the strongest open-source communities in the data ecosystem.”

The strengths each company built for running pipelines are now being stretched to cover something bigger, with Prefect betting those same strengths are what agentic workloads will need next.

## The AI transition

Both companies have been repositioning around AI agents for a while. Back in 2024, [Prefect 3.0 landed with an explicit focus](https://www.prefect.io/blog/introducing-prefect-3-0) on supporting agentic workflows. A year later, [Dagster debuted Components](https://dagster.io/blog/accelerate-data-pipeline-development-with-dagster-components), pitched as a way to build pipelines using reusable, YAML-based building blocks rather than hand-written Python. Shortly after, [Dagster went further with Compass](https://dagster.io/blog/introducing-compass), a tool that lets analysts query data using plain-language prompts sent through Slack instead of writing SQL.

None of that matches the reach of what Prefect built with FastMCP. The framework works with the Model Context Protocol (MCP), the open standard Anthropic [released in late 2024](https://www.anthropic.com/news/model-context-protocol), which lets [AI models discover](https://thenewstack.io/why-the-model-context-protocol-won/) and call external tools and data, allowing developers to build MCP servers by writing plain Python functions instead of hand-coding the protocol directly. Prefect [shipped FastMCP the same month](https://jlowin.dev/blog/introducing-fastmcp) that MCP itself launched, and Anthropic later adopted it as the [official Python SDK](https://pypi.org/project/mcp/) for MCP.

That evolution of both companies has now led to a very strategic acquisition, but the deal has ramifications for those who have been steering Dagster since its earliest days. [Nick Schrock](https://www.linkedin.com/in/schrockn/), who founded Dagster and moved from [CEO to CTO in 2022](https://dagster.io/blog/pete-hunt-path-to-elementl-part2) to make way for [Pete Hunt](https://www.linkedin.com/in/pwhunt/), is named alongside Hunt in the official [acquisition announcement](https://www.businesswire.com/news/home/20260713065285/en/Prefect-Acquires-Dagster-Uniting-the-Two-Leading-Modern-Orchestrators) as staying on to “serve as strategic advisors to Prefect” while remaining “active in the open-source community.”

However, Schrock’s [own blog post](https://dagster.io/blog/prefect-is-acquiring-dagster), published on Monday, reads far more like a clean break from Dagster.

“I want to share that I’ll be moving on from the project and company,” Schrock writes.

Schrock’s departure closes one chapter for Dagster. The acquisition itself, however, opens another, with Prefect betting that the ideas both companies spent years developing for data orchestration will prove just as valuable as AI agents move into production.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)