**Ready or not, the agentic enterprise is here**, and the key to enabling it efficiently is being debated from various perspectives. Strategies can range from DIY schemes to best-of-breed point solutions to a single, governed, AI-powered tool that manages it all with minimal human oversight.

[Snowflake](https://snowflake.com), fresh off reworking its [Cortex Code](https://www.snowflake.com/en/product/features/cortex-code/) as [Snowflake CoCo](https://www.snowflake.com/en/news/press-releases/snowflake-coco-redefines-enterprise-ai-development-as-the-coding-agent-built-for-faster-easier-and-more-powerful-innovation-anywhere/), is firing a fastball to developers, urging them to stop being slowed by context switching across tools and start building on a trusted data foundation.

The Menlo Park, California-based company announced this week new capabilities for CoCo, an AI-based coding agent designed to simplify enterprise development by enabling builders to automate workflows, develop apps, and operationalize AI with simple prompts.

![](https://cdn.thenewstack.io/media/2026/06/b94ef866-1678972096373.jpg)

Bala Kasiviswanathan of Snowflake

CoCo is deeply integrated with Snowflake’s governed data platform and is now available through new interfaces, including a native desktop app, a mobile app, and a Slack integration. It features autonomous task execution through automations and cloud agents.

The company also introduced [Snowflake Datastream](https://www.snowflake.com/en/product/features/datastream/), a new, fully managed, Kafka-compatible streaming service that enables enterprises to stream real-time data directly into Snowflake, eliminating the need for separate streaming infrastructure and simplifying the creation of real-time AI apps when paired with CoCo.

In an interview with *The New Stack* during the conference, [Bala Kasiviswanathan](https://www.linkedin.com/in/balak/), Snowflake’s Vice President of Developer and AI Experiences, laid out the company’s case for a developer-centric vision in which high-velocity productivity and enterprise-grade governance are not mutually exclusive. He detailed how the company’s new tools solve global IT headaches from compliance at scale to real-time supply chain disruption.

![](https://cdn.thenewstack.io/media/2026/06/4894432f-screenshot-2026-06-04-at-15.11.10-1024x539.png)

*Snowflake CEO Sridhar Ramaswamy at Snowflake Summit on June 2, 2026.*

## **The core problem: fragmentation and context switching**

Kasiviswanathan, who joined Snowflake from the startup [Simpplr](https://www.linkedin.com/company/simpplr/) and previously worked on machine learning projects at [Google Cloud’s Apigee](https://cloud.google.com/apigee), is tasked with making Snowflake a go-to platform for both internal teams and external developers. His primary message to the community addresses the pervasive pain point of fragmentation: “I think there are a lot of developers in our customers today who would like to do more and are probably having to switch context a lot in terms of different tools,” he says.

> “I think there are a lot of developers in our customers today who would like to do more and are probably having to switch context a lot in terms of different tools.”  
> —Bala Kasiviswanathan, Snowflake’s Vice President of Developer and AI Experiences

CoCo is a primary data coding agent for any data, Kasiviswanathan says. “It is based on a platform that is backed, trusted, and governed. The platform aims to help enterprise developers get more stuff done and also expand who can be a ‘builder’ within an organization, since CoCo is plain-language driven, and not only for expert coders.”

## **Model agnostic and governed by design**

CoCo’s underlying architecture is defined by its platform independence. While Snowflake itself is built on SQL, its AI coding agent is designed to be model-agnostic.

“You can use any foundation model you want because some customers will say, ‘Hey, we have ruled only to use cloud [models],'” Kasiviswanathan said. “Someone will say we have ruled only to use GPT. We are model agnostic, so you can pick your model. Every company has many different vendors. That’s a reality. And all of them don’t want to keep moving data.”

The real magic, he says, resides in Snowflake’s internal harness, which ensures the agent understands three important components: Snowflake’s infrastructure, permissioning, and the data itself.

> “We are model agnostic, so you can pick your model. Every company has many different vendors. That’s a reality. And all of them don’t want to keep moving data.”  
> —Kasiviswanathan

This focus on governance and trust is a non-negotiable prerequisite for building serious, grounded AI systems. As Snowflake CEO [Sridhar Ramaswamy](https://www.linkedin.com/in/sridhar-ramaswamy/) told conference-goers in the Summit keynote address, the ultimate goal is to offer “a system of decision-making via an agentic control plane that coordinates enterprise data, AI models, and applications with guaranteed trust and governance.”

## **An open flow for all data, everywhere**

Snowflake is extending its tools beyond its own data infrastructure, directly tackling the vendor-lock-in reality faced by every large enterprise. Kasiviswanathan underlined Snowflake’s major investment and contributions to open source, citing projects such as the [Apache Iceberg](https://www.snowflake.com/resource/7-snowflake-reference-architectures-application-builders/?utm_source=google&utm_medium=paidsearch&utm_campaign=na-us-en-nb-datapipelinegeneral-epb&utm_content=go-rsa-evg-eb-7-snowflake-reference-architectures-application-builders-versionb&utm_term=c-g-data%20pipeline-b-781716122286&gad_source=1&gad_campaignid=15215602515&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxL5N1PSn7HuyPUk5u-Cwb4HjjkmUAPZbbJxJ6sEznzD_xH0Bc989SgaAhOqEALw_wcB) format, [Apache Polaris](https://www.snowflake.com/en/blog/introducing-polaris-catalog/), and the [Apache Arrow protocol](https://arrow.apache.org/).

Snowflake’s strategy is all about enabling access to data in an open format and building interesting things on top of it. During the conference, the company showcased CoCo by using data simultaneously from Google Cloud Storage, Snowflake Iceberg tables, and several other platforms.

CoCo’s utility supports data on the Snowflake platform from major ecosystem players, including [Postgres](https://www.postgresql.org/), [AWS Glue](https://aws.amazon.com/glue/), [dbt](https://www.getdbt.com/), [Apache Airflow](https://airflow.apache.org/), and [Databricks](https://www.databricks.com/).

## **Meeting developers where they are**

Snowflake ensures that CoCo is accessible throughout a developer’s entire workflow. New tools announced at the Summit include:

* **A new desktop application:** CoCo is now a proper Integrated Development Environment (IDE).
* **An agent SDK:** Allows developers to call CoCo from outside applications.
* **Workflow extensions:** Plugins for popular tools, including a VS Code extension for Visual Studio users, and a CoCo plugin for Clock code.
* **Ubiquitous access:** Plans for a mobile application and a Slack bot are in the works, with availability set for later this year.

Beyond direct tools, Snowflake is fostering partnerships with leading developer platforms such as [Vercel](https://vercel.com/), [Superblocks](https://www.superblocks.com/), and [Retool](https://retool.com/). These partnerships enable Enterprise customers already standardized on those tools to build applications against Snowflake and even deploy them onto the platform from within. For example, Vercel eliminates the complex DevSecOps concerns of security permissions, deployment costs, and maintenance associated with managing application infrastructure outside the data platform.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/314a85cc-cropped-89f126f8-chrisp-600x600.png)

Chris J. Preimesberger, a contributing writer/editor at several publications since June 2021, is former editor in chief of eWEEK. He was responsible for the publication's coverage for a decade (2011-2021). In his 16 years and more than 5,000 articles at...

Read more from Chris J. Preimesberger](https://thenewstack.io/author/chris-j-preimesberger/)