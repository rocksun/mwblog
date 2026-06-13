[Databricks](https://www.databricks.com/) on Wednesday launched OpenSharing, the successor to its open-source [Delta Sharing](https://github.com/delta-io/delta-sharing) protocol.

This updated protocol adds support for [Apache Iceberg](https://iceberg.apache.org/) REST Catalog clients and brings on-premises storage vendors into the ecosystem, starting with [Everpure](https://www.everpuredata.com/) (previously Pure Storage), [MinIO](https://www.min.io/), and [Qumulo](https://qumulo.com/).

Also, OpenSharing is now a standalone [Linux Foundation](https://www.linuxfoundation.org/) project and extends Delta Sharing’s zero-copy sharing beyond tables to include agent skills, AI models, and unstructured data.

Most layers of the agent stack have settled on a standard by now:

OpenSharing builds on this stack by providing a protocol that helps organizations securely share data and AI assets with one another.

## From Delta Sharing to OpenSharing

Databricks [launched Delta Sharing in 2021](https://www.databricks.com/company/newsroom/press-releases/databricks-unveils-delta-sharing-the-worlds-first-open-protocol-for-real-time-secure-data-sharing-and-collaboration-between-organizations) as a sub-project of [Delta Lake](https://delta.io/), Databricks’ open-source table format. At the time, it billed this as the first open protocol for secure data sharing across organizations. The company says it has since become the most widely adopted open data sharing protocol, with thousands of customers and partners, including Amadeus, Atlassian, LSEG, SAP, Stripe, and The Trade Desk.

As Databricks co-founder and CTO Matei Zaharia puts it in today’s announcement, “Delta Sharing proved the industry would choose open over locked-in.”

It’s worth noting that nothing changes for existing Delta Sharing users. Current Delta Sharing deployments keep working. OpenSharing adds new asset types, recipients, and sources, without introducing breaking changes.

## Don’t email agent skills

[Akram Chetibi](https://www.linkedin.com/in/akram-chetibi-752763b/), who leads the Databricks product team for ecosystem and partner integrations, tells *The New Stack* in an exclusive interview that agent skills are the most requested new asset type, followed by AI models.

Before joining Databricks in late 2023, Chetibi was a founding product manager at [AWS Data Exchange](https://aws.amazon.com/data-exchange/) and helped start the [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) business.

“There is no easy way today to share an agent skill,” Chetibi says. “If I ask you today to share with me an agent skill, how would you do it? […] You would email me a file, but then if I want an update, how do I get the update? You email me another file.”

Databricks calls OpenSharing the first open, vendor-neutral protocol for securely sharing AI assets. The alternatives today are custom integrations or single-vendor marketplaces, such as Salesforce’s [AgentExchange](https://www.salesforce.com/agentforce/agentexchange/) or the agent storefronts inside the AWS and Microsoft marketplaces.

With OpenSharing, a provider can publish a skill or model once, and any partner can consume it through standard APIs for discovery, authorization, and access, with zero-copy access at the source.

It’s worth noting that the protocol does *not* prescribe what a skill or model has to look like.

## How the protocol works

Chetibi says the requirements for external collaboration remain constant, regardless of the asset. “They want something that works across clouds, across regions, and across platforms, and they want something that is what is typically referred to as zero copy or live sharing,” he says.

The general object model carries over from Delta Sharing. Providers package assets into a share. That share contains schemas, and a schema can now hold a table, an AI model, or an agent skill.

The mechanics underneath differ by asset type. Structured data is in Parquet and can be shared via signed URLs for individual partitions, exposed through Delta- or Iceberg-compatible APIs, with features like a change data feed. Unstructured data and AI assets work by vending cloud tokens for the underlying storage, in a cloud-agnostic way.

The protocol covers external, read-only sharing across administrative boundaries; internal governance is not part of this announcement, though Chetibi says to “stay tuned” on that front.

## One more API: Iceberg

OpenSharing now also supports the Apache Iceberg APIs. Iceberg has become something of a standard for sharing analytic tables, complementary to Parquet. But, Chetibi argues, “the formats are becoming less and less relevant — at the end of the day, [they’re] all like Parquet with some metadata around them.”

Delta Sharing already had connectors for Apache Spark, Power BI, Excel, and Python, and even Snowflake supports it as a recipient. By adding the Iceberg API, any tool that supports it becomes another destination a provider can reach.

Databricks has been heading this way for a while. It bought Tabular, founded by Apache Iceberg’s creators, for a [reported $2 billion](https://techcrunch.com/2024/08/14/databricks-reportedly-paid-2-billion-in-tabular-acquisition/) in 2024, and it is pitching [metadata convergence between Delta and Iceberg](https://www.snowflake.com/en/blog/engineering/iceberg-summit-2026-recap-v4-spec/) in the Iceberg v4 spec.

Snowflake, meanwhile, [extended its](https://www.snowflake.com/en/blog/data-sharing-open-table-formats/) [sharing](https://www.snowflake.com/en/blog/data-sharing-open-table-formats/) to Iceberg and Delta tables across clouds and regions and claims a sharing ecosystem 2.5 times the size of its competitors’. Both companies now describe their sharing strategies as open. But while Databricks ships a protocol others can implement, Snowflake’s sharing runs through its platform.

## Taking the protocol on-prem

Everpure (formerly known as Pure Storage, which [rebranded in February](https://www.sdxcentral.com/news/pure-storage-relaunches-as-everpure-pivoting-to-ai-focused-data-management/)), MinIO, and Qumulo offer a managed OpenSharing service at launch, with Cohesity, Commvault, Hewlett Packard Enterprise, NetApp, Nutanix, Rubrik, and VAST Data slated to follow.

The storage vendors run the OpenSharing server themselves, so customers don’t have to stand one up.

> “This is an open protocol that is truly open, and it’s used and supported by many other platforms that are not Databricks.”

“Once these partners host the server locally on-prem, you can then easily connect to it using the same protocol you would connect to any other cloud or platform, Chetibi says.

Two things had to happen first, says Chetibi: The protocol needed support for unstructured data and AI assets, since on-prem estates are not just tables, and Databricks wanted the storage providers, rather than customers, to operate the servers.

## Open governance

OpenSharing follows Delta Lake and Unity Catalog, which Databricks [donated to LF AI & Data in June 2024](https://lfaidata.foundation/blog/2024/06/20/welcoming-unity-catalog-to-the-lf-ai-data-foundation-a-milestone-in-open-data-and-ai-governance/), as the company’s projects under the Linux Foundation umbrella.

“We don’t want it to be like a Databricks thing — this is an open protocol that is truly open, and it’s used and supported by many other platforms that are not Databricks,” Chetibi says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)