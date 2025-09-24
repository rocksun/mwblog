Business intelligence service provider [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) has kicked off a vendor-neutral initiative to create a standard for adding contextual information to structured and unstructured BI data.

To be built in YAML (probably) and ultimately managed by a standalone entity, the Open Semantic Interchange (OSI) aims to be a “universal semantic data framework,” enabling different organizations to share data across their platforms using a common set of definitions.

Thus far, [Snowflake](https://thenewstack.io/qa-snowflake-analytics-chief-on-centralizing-data-for-ai/), [Salesforce](https://www.salesforce.com/data/?utm_content=inline+mention), [dbt Labs](https://www.getdbt.com/product/what-is-dbt) are leading the effort. Other partners in the project include BlackRock, Mistral AI and RelationalAI. The project announced its charter on Tuesday.

## The Growing Need for a Universal Data Standard for AI

While we already have data sharing standards aplenty, the emerging popularity of AI agents has created new needs for standardization.

“Every single customer I talk to is trying to figure out how to deliver on the crazy demand for agentic experiences, and how to do it in a way that doesn’t create a mess,” of conflicting information, said [Josh Klahr](https://www.linkedin.com/in/jklahr/), who does product management for the Snowflake Data Cloud.

Conflicting definitions have long been a challenge for the BI space, but now that agentic development is a thing, the demand for some sort of unity has skyrocketed, he said.

“You need to have a single semantic model, ideally one that’s sitting at the kind of layer that allows for interoperability across all the different partners,” Klahr said.

By now, most organizations have multiple sources of data, in multiple formats, making it difficult for AI systems to find and calculate against. The Snowflake customer has a median of five different BI tools.

Concepts and formulas such as “ad spend,” “active customer,” and “gross profit margin” may all be defined differently within different systems. OSI would provide a standard definition for all.

“So that instead of the LLM needing to figure out how to calculate profit margin, you just give it the name of the metric, which has the actual calculation associated with it, and LLM just knows how to compile the profit margin,” Klahr said.

“Then, when I’m in Tableau or ThoughtSpot, I ask for profit margin, and the calculations match. ”

## Introducing the Open Semantic Interchange (OSI)

The duty of the newly launched OSI working group is not to provide definitions, but rather to establish a format for specifying definitions in various ways. It’s up to the end-users to define the metrics and their definitions.

The OSI actual specification has not be published yet, Klahr said. The group needs to get up and running first.

Most likely, the format they will base OSI on will be [YAML](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/), a [widely used](https://thenewstack.io/kubernetes-is-getting-a-better-yaml/) configuration language with some [basic programming capabilities](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/). A lot of the group’s participants already use YAML for various tasks, he said.

In a press statement, BlackRock said OSI would work with its [Aladdin platform](https://www.blackrock.com/aladdin/resources/faqs), where it would unify the investment management process with a common data language for public and private markets.

“This is the Rosetta Stone for business data,” said [Southard Jones](https://www.linkedin.com/in/southardjones/), Tableau chief product officer, in a statement.

## How the OSI Framework Aims To Standardize Definitions

The Snowflake engineers are basing the idea of the semantic layer on a feature on its own AI and business intelligence (BI) platform, called [Semantic Views](https://docs.snowflake.com/en/user-guide/views-semantic/overview), which helped customers reconcile multiple sources of data. They may be running BI tools and keeping data catalogues, but very little of it was actually cross-referenceable.

“The question of interoperability really started to emerge from customer conversations,” Klahr said.

The Semantic Definition file will consist of a number of other attributes, including pointers to base tables, joint keys and relationships. It may also include a set of metrics, synonyms and metrics for that definition, as well as custom instructions for AI.

## The Role of Vendors and the Open Source Community

The working group has no plans, at this time, to build a run-time engine. This would be the job of a vendor to provide. With Snowflake itself, for instance, the company has a service to render OSI-like definitions into materialized views.

The group plans to create an open source repository to hold the specification itself, as well as converters that different partners may contribute.

It is also inviting other organizations to join. “We want as many members as possible to participate,” he said.

The OSI group is not the only effort to give AI more metadata to work with. A creator of the RSS syndication format has helped field  “[Really Simple Licensing](https://rslcollective.org/),” a [robots.txt-like file](https://arstechnica.com/tech-policy/2025/09/pay-per-output-ai-firms-blindsided-by-beefed-up-robots-txt-instructions/) to provide a uniform way of expressing content copyright and licensing information to web scrapers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)