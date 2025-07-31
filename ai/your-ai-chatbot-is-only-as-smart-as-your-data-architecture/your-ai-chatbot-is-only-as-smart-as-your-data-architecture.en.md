I have been in the data movement space for almost twenty years, and I have witnessed dramatic changes in the way we utilize data to uncover insights and make informed decisions. From machine learning to generative AI (GenAI), we have rapidly increased our ability to leverage data for innovation. However, at the same time, organizations struggle to build applications that work effectively at scale, despite having the vast capabilities of AI at their fingertips. The reason is that [generative AI is only as good as the data](https://thenewstack.io/kumo-surfaces-structured-data-patterns-generative-ai-misses/) it ingests.

To illustrate my point, I want to examine a real business case that can be solved with the successful implementation of generative AI and robust data infrastructure.

## **The Analytics Bottleneck Slowing Teams**

With sales, marketing, finance, and operations leadership all submitting requests to a centralized data team, the problems are likely to grow exponentially. Many organizations attempt to address this issue by assigning an embedded data analyst to teams. Still, this approach increases costs and often proves difficult to implement, as it is challenging to find a specialist with the right domain experience for the role.

This analytics bottleneck creates multiple issues that can affect overall operational efficiency. Business teams often postpone critical decisions while awaiting data analysis, which stalls innovation and erodes a competitive advantage. Furthermore, they are unable to explore [data freely and use their business knowledge](https://thenewstack.io/better-llm-integration-with-content-centric-knowledge-graphs/) to uncover insights that data teams might not discover on their own. Other risks include inconsistent analysis across teams, with differing KPIs that can lead to confusion within the organization.

That is simply not a productive use of your [data team’s time](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/). And there is a better way.

## **The Promise of AI-Powered Self-Service Analytics**

Generative AI offers a compelling solution to this challenge. Imagine a marketing manager typing a question into a chatbot, such as, “How are sales compared to last quarter?” and receiving an immediate response with relevant metrics and visualizations. No JIRA tickets, just instant insights.

With the advent of generative AI, this solution is now feasible for many businesses. Conversational analytics platforms leveraging LLMs can interpret natural language questions and turn them into SQL queries. From those queries, they can easily pull metrics and generate relevant data visualizations. It’s rather like working with a data analyst, as opposed to writing endless queries into a terminal.

## **Effective Self-Service Analytics Starts Under the Hood**

A truly effective self-service [analytics solution starts with a unified data](https://thenewstack.io/qa-snowflake-analytics-chief-on-centralizing-data-for-ai/) foundation. Before an LLM can answer questions about your business, it needs access to a comprehensive, well-structured data layer. Organizations with siloed data across multiple systems will struggle to implement effective self-service analytics, regardless of how sophisticated their LLM implementation might be.

Modern business intelligence also requires going beyond traditional structured data. While analytics once focused primarily on numbers in tables, today’s solutions must incorporate meeting transcripts, customer feedback, and even rich media like images and videos. A robust data infrastructure must handle both data types seamlessly, creating a unified layer that the LLM can query regardless of the original format.

## **Maintaining Data Sovereignty and Staying Competitive**

As organizations explore generative AI for analytics, many turn to third-party solutions that require sending proprietary data to external providers. But this is never a good deal.

Your data isn’t just a record of past activity; it represents your competitive advantage. Customer behaviors, product performance metrics, and operational patterns contain unique insights that differentiate your business. When you expose this first-party data to external systems, you risk exposing your intellectual property, as your unique business patterns could inform competitors. You also face regulatory compliance issues since data governance requirements may prohibit specific data from leaving your control.

The most sophisticated implementations are now training custom LLMs on internal data, creating domain-specific models that understand the organization’s unique terminology, metrics, and business rules without exposing sensitive information to third parties.

## **A Real World Example**

A North American fintech [company operates with a lean data](https://thenewstack.io/can-companies-really-self-host-at-scale/) team and has a growing business that demands more and more insights. They didn’t have the budget to expand their team, so they decided to build a self-serve analytics chatbot.

Their infrastructure integrates structured data from Microsoft SQL databases with unstructured data from cloud storage services, such as Azure Blob and [Amazon](https://aws.amazon.com/?utm_content=inline+mention) S3. All this data is stored in a [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) cloud data warehouse, creating a single source of truth. By connecting their cloud data warehouse to Snowflake Cortex AI, the company made a natural language interface that transforms how business users interact with data. Employees can ask questions directly to the data through natural language and receive immediate insights.

The company’s senior leadership recognized early on that data needed to be stored in a unified layer, with both structured and unstructured sources, to provide real context for the chatbot. [Context requires all data](https://thenewstack.io/is-model-context-protocol-the-new-api/) and metadata to be stored and accessed together with proper organization, so that the LLM has the proper knowledge to make decisions and prepare insights.

Without the company’s investment into infrastructure, the chatbot would not be reliable, and without reliability, AI loses trust.

## **Invest in Infrastructure for Long-Term Success**

While generative AI has captured imaginations with its ability to understand and generate human language, the success of self-service analytics ultimately depends on the quality, completeness, and accessibility of the underlying data.

By building on a solid data foundation and maintaining control of proprietary information, businesses can deliver on the promise of democratized analytics without compromising security or accuracy. This transforms data from a bottlenecked resource into a true competitive advantage.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/05/5174bda5-cropped-fa484a55-michel-03-headshot-current-june-2023-1-scaled-1-600x600.jpg)

Michel Tricot is co-founder and CEO of Airbyte, which started in 2020 as an open-source data integration platform with a vision of commoditizing data integration pipelines across all industries and organizations. He has been working in data engineering for the...

Read more from Michel Tricot](https://thenewstack.io/author/micheltricot/)