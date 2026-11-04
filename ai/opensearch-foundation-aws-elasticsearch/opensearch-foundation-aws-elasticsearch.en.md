**OpenSearch has come a long way** since Amazon Web Services first [announced the project](https://aws.amazon.com/blogs/opensource/stepping-up-for-a-truly-open-source-elasticsearch/) back in January 2021, in response to [Elastic’s decision to move Elasticsearch](https://www.elastic.co/blog/licensing-change) and its accompanying visualization tool, [Kibana](https://www.elastic.co/lp/kibana), away from Apache 2.0 and onto a combination of proprietary and source-available licenses. Elastic said at the time that the reason was to prevent cloud behemoths such as AWS from offering Elasticsearch “as a service” without giving anything back, while also accusing AWS of [violating the Elasticsearch trademark](https://www.elastic.co/blog/elastic-and-amazon-reach-agreement-on-trademark-infringement-lawsuit).

While Elastic subsequently [returned Elasticsearch and Kibana](https://thenewstack.io/whats-behind-elastics-unexpected-return-to-open-source/) to open source by adding AGPL as a licensing option, [making up with AWS along the way](https://venturebeat.com/business/once-frenemies-elastic-and-aws-are-now-besties), OpenSearch has continued forging its own path as an independent open source project — albeit one still closely associated with the technology giant that created it.

## Reducing the AWS dependency

A major milestone came in September 2024, when [AWS transferred OpenSearch to the Linux Foundation](https://thenewstack.io/aws-transfers-opensearch-to-the-linux-foundation/), establishing the OpenSearch Software Foundation and placing the project under “vendor-neutral” governance. The move was intended to give other companies greater confidence that they could contribute to OpenSearch without AWS retaining ultimate control over its future.

Two years on, [OpenSearch](https://opensearch.org/) shows signs of gaining traction beyond its original backer. Figures provided to *The New Stack* by the OpenSearch Software Foundation show that AWS’s share of contribution activities across the project’s repositories has fallen from 91% in its first year to 72% in 2025–26. Meanwhile, Amazon-affiliated engineers accounted for 95% of maintainers in the core OpenSearch repository in [April 2022](https://github.com/opensearch-project/OpenSearch/blob/a6b4967dcf39b7ff3d47aff0a75314becbce72f4/MAINTAINERS.md), compared with 71% today.

The shift is also visible in how organizations are deploying the software. In the *[2026 Open Data Infrastructure Report](https://www.linuxfoundation.org/research/opensearch-data-infrastructure-2026)*, published last month by the Linux Foundation and the OpenSearch Software Foundation, data suggest that self-managed deployments have grown faster than Amazon’s managed OpenSearch Service since 2024. Some 60% of surveyed OpenSearch users now run self-managed deployments in the cloud, up from 37% in 2024, while use of Amazon’s managed service rose more modestly, from 44% to 48%.

Yet AWS’s historical association with OpenSearch remains an obstacle for some prospective users. According to the report, nearly a quarter (24%) of 71 surveyed non-adopters cite concerns about the project’s vendor neutrality and historical ties to AWS as reasons for staying away.

The figures point to a challenge that a change in governance alone cannot resolve: convincing prospective users and contributors that OpenSearch’s future is no longer determined primarily by AWS.

## ‘A watershed moment’ for OpenSearch

*The New Stack* caught up with [Bianca Lewis](https://www.linkedin.com/in/biancalewis/), executive director of the OpenSearch Software Foundation, at [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/) in Prague this month to discuss the project’s evolution beyond its Elasticsearch origins, including any lingering perception of AWS influence.

Lewis argues that the project’s legal independence, achieved more than two years ago, provides an important foundation for building that trust.

> “When they donated it to the Linux Foundation, that was a watershed moment.”

“When they donated it to the Linux Foundation, that was a watershed moment,” Lewis tells *The New Stack*. “Because they couldn’t close OpenSearch and they couldn’t change the license. They didn’t own the application anymore.”

Lewis also suggests the decision made commercial sense for AWS, whose cloud business generates revenue from the computing resources used to run applications, rather than necessarily owning the applications themselves.

“AWS don’t make money from applications,” she says. “AWS make money from compute. So operating, growing OpenSearch long term was never in AWS’s plan.”

> “AWS don’t make money from applications. AWS make money from compute. So operating, growing OpenSearch long term was never in AWS’s plan.”

But questions remain about how much influence AWS continues to wield. The company still accounts for nearly three-quarters of recorded contribution activities across OpenSearch’s repositories. And while AWS holds just four of the 15 voting seats on the project’s Technical Steering Committee (TSC), an AWS employee, [Andrew Ross](https://www.linkedin.com/in/andrew-ross-781ab1a/), was just reelected committee chair in October.

## The AI opportunity for OpenSearch

While AWS’s influence remains evident in OpenSearch’s governance, the software itself has changed considerably since the fork. And Lewis readily acknowledges just how closely it resembled Elasticsearch in the early days.

“It’s undeniable that the early versions of OpenSearch was Elasticsearch with a different name,” she says. “They had the same plugins. Even a lot of the documentation of OpenSearch was Elasticsearch documentation. [But] when it got donated to the Linux Foundation a couple years back, it had already well and truly diverged from its original mother project.”

Today, OpenSearch is positioning itself as infrastructure for applications that need to search, analyze and retrieve data, including those built around large language models (LLMs). Its support for vector and hybrid search, for example, makes it relevant to retrieval-augmented generation (RAG), where AI applications retrieve information from external sources to supplement model responses.

The project’s latest release, OpenSearch 3.9, [which debuted in September](https://opensearch.org/blog/get-to-know-opensearch-3-9/), builds on those capabilities with improvements aimed at helping developers search and retrieve information for AI applications, alongside updates to performance, monitoring, and alerting.

Lewis believes this creates an opportunity for OpenSearch to become a central component of enterprise AI infrastructure.

“If you decide that you wanted your AI infrastructure on an open platform, I think [OpenSearch] today is just the default choice,” she says.

## Winning the enterprise

Ambitions are one thing. Turning those ambitions into long-term enterprise adoption is something else entirely. The Foundation’s report indicates that a substantial proportion of OpenSearch deployments remain experimental, with organizations still evaluating the technology or using it for applications that could be replaced.

Asked about this, Lewis points to the amount of time it can take for companies to move away from established commercial platforms, particularly when they are tied to multiyear licensing agreements.

“They might have a three-year contract for Splunk, a license for five years with Elastic,” she says. “So they’re not just chucking that out.”

In other words, companies may be testing OpenSearch while continuing to use products they have already paid for. But there is, of course, no guarantee those evaluations will result in permanent deployments.

Lewis argues that one reason organizations might eventually make the switch is the freedom to change technology providers without having to rebuild their applications.

> “What if I get locked in? And if I get locked in and I want to leave, what does that look like? Do I have to rearchitect all my applications?”

“What if I get locked in? And if I get locked in and I want to leave, what does that look like? Do I have to rearchitect all my applications?,” she says.

That concern extends beyond licensing costs. Enterprises must also consider the engineering effort involved in changing suppliers, moving data, and maintaining applications over time.

And this all brings the discussion back to the question of OpenSearch’s independence. If organizations are choosing the platform partly to avoid dependence on individual vendors, the project’s ability to attract and retain contributors beyond AWS becomes all the more important.

Asked what she hopes OpenSearch will look like five years from now, Lewis returns to the question of vendor influence — and her ambition for a project that no single company dominates.

“To have a truly sustainable, fast, innovating platform, which is not dominated or heavily influenced by any single vendor in the world,” she says. “Then, you’ve got a stable platform.”

[Data Engineer Roadmap
Step by step guide to becoming a Data Engineer in 2026

Introduction
Learn the Basics
Data Generation
Data Storage
Relational Databases
NoSQL Databsases
Data Warehousing
Data Warehousing Architectures
Data Ingestion
Infrastructure as Code - IaC](https://roadmap.sh/data-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=opensearch-foundation-aws-elasticsearch)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)