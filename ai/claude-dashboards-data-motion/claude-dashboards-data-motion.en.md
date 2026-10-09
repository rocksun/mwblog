**A month after** OpenAI gave [ChatGPT Work](https://thenewstack.io/claude-cowork-vs-chatgpt-work-benchmark/) a data agent that builds dashboards, Anthropic on Thursday shipped its own version.

[Claude Dashboards](https://claude.com/blog/dashboards-and-motion), now in beta, lets users build live dashboards to see the exact queries pulling the data and export those dashboards to popular business intelligence tools.

Dashboards connects to enterprise data sources such as Snowflake, Databricks, Amazon Redshift, and ClickHouse, among others.

In addition, Anthropic is also launching Claude Motion, which uses code to animate reports and charts, and [Docs, Slides, and Design](https://claude.com/resources/articles/cowork-is-now-claude) are now out of beta.

## Live dashboards, visible queries

To get started with dashboards, users connect their data platforms of choice and describe what they want to know.

Clicking a number in any of these new dashboards brings up the query that produced it. Users who don’t want to read SQL can also ask Claude to explain the figure.

Dashboards work with Claude’s existing connectors, too, including Salesforce.

The company says Claude will refresh the dashboard as data changes, with a timestamp on each chart showing when it was last updated.

It’s worth noting that Anthropic isn’t positioning Dashboards as a replacement for business intelligence tools (though some users will surely use it this way). Its feature set can’t replace specialized BI tools, but users who want to dig deeper can move a dashboard into services like Grafana, Hex, Mixpanel, monday.com, Omni, PostHog, or Sigma.

Support for Looker, Perplexity, and Tableau is coming later.

## Business definitions and permissions

It’s worth noting that Anthropic isn’t the first to market with this idea.

[OpenAI’s Data agent](https://openai.com/index/put-data-to-work/), which launched about a month ago as a ChatGPT Work plugin, also lets users build similar dashboards and connects to enterprise data platforms like Redshift, BigQuery, ClickHouse, Databricks, MongoDB, Snowflake, and Datadog. Users can also build dashboards directly in Power BI, Tableau, ThoughtSpot, and other BI tools.

The list of supported vendors for OpenAI and Anthropic differs slightly, and OpenAI supports [semantic layers](https://thenewstack.io/microsoft-fabric-agent-context/) like Databricks Genie Ontology, but the overall direction is essentially the same. Anthropic tells us that Claude Dashboards will also support these semantic models if they are exposed through a connector.

At the end of the day, both companies want to become more deeply entrenched in the enterprise — that’s where the money is, after all — and move beyond simply being token providers to higher up the enterprise productivity stack.

The warehouse vendors aren’t sitting idle, either.

Snowflake signed a [$200 million deal](https://www.businesswire.com/news/home/20251203124957/en) with Anthropic in December 2025, but OpenAI’s Data agent announcement includes comments from product leaders at both Snowflake and Databricks. Both vendors also have their own natural-language analytics tools, [Snowflake Intelligence](https://thenewstack.io/snowflake-streamlines-data-analysis-for-enterprise-ai/) and [Databricks Genie](https://thenewstack.io/databricks-launches-lakehouse-ai-bi-and-governance-advances-at-annual-summit/).

According to OpenAI, Data agent queries respect the existing table, row, and column permissions of whatever account is connected.

Admins can let users share dashboards outside their organization, including via public links.

“Dashboards use the data access people already have. A dashboard starts private to you,” an Anthropic spokesperson told *The New Stack*. “When you share it, each viewer’s own connections run its queries by default, so people see only data they already have access to. On Enterprise plans, Dashboards is off by default until an admin turns it on in organization settings. On Team and Enterprise plans, dashboards stay inside the organization unless an owner turns on external sharing.”

## Claude Motion skips video models

In a somewhat related move, Anthropic also launched Claude Motion, which can turn material such as a quarterly update or a chart from a board deck into a short animated clip.

Since Anthropic doesn’t have a video model, Claude does this by writing code to animate the user’s text, charts, and images. But that also makes this more flexible and users can easily edit the animations until they export them to an MP4.

![](https://cdn.thenewstack.io/media/2026/10/adef6665-claude-motion-1024x576.png)

Credit: Anthropic.

Developers have been building similar videos with Claude Code and frameworks such as [Remotion](https://thenewstack.io/framework-lets-react-developers-create-video-with-code/) and HeyGen’s open-source [HyperFrames](https://github.com/heygen-com/hyperframes). Motion brings that workflow directly into Claude, and you can edit the finished clip in any video tool.

Motion is now in beta for Team and Enterprise customers.

## Availability and enterprise controls

Dashboards is available in beta on Claude’s paid plans. Enterprise admins must enable both Dashboards and Motion.

Docs, Slides, and Design, meanwhile, will be enabled by default for Enterprise organizations on October 15. They’ve been available in beta inside Claude conversations since [September 16](https://thenewstack.io/anthropic-claude-unified-interface/). Anthropic says users have created more than 45 million documents, decks, and designs since then.

Artifacts, Anthropic’s term for the documents, decks, and dashboards Claude creates, now support customer-managed encryption keys (CMEK). Admins can control which artifact templates users see.

Users of the standalone Claude Design site, which [launched in April](https://thenewstack.io/anthropic-claude-design-launch/), have until December 14 to migrate. Their chats and comments won’t transfer.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)