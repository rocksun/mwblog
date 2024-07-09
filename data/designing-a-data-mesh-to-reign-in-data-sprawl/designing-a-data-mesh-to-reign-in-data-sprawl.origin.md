# Designing a Data Mesh To Reign in Data Sprawl
![Featued image for: Designing a Data Mesh To Reign in Data Sprawl](https://cdn.thenewstack.io/media/2024/07/464d562a-data-mesh-reign-data-sprawl-1024x576.jpg)
As much as possible, I like to [field customer calls](https://thenewstack.io/want-killer-features-foster-dev-user-communication/). I like to hear what backend teams are working on, what they are building, what is working, what isn’t. What strategies they are considering, what code languages they’ve given up on, what problems they are wrestling with and what solutions they are exploring.

I love these calls because I am endlessly curious. It’s fascinating to see the various approaches different developers will take to solve similar problems. I also love these calls because I’m a futurist (also pronounced “impatient”). I can’t wait to see what trends will rise out of the hotbed of various text editors. I firmly believe that the best code is the code that hasn’t been written.

One trend that has recently been cropping up more and more in conversation is data mesh. In a race to get away from the monolith and create more agile data access, companies adopted microservices to unlock consumer/producer access and faster app development. But in doing so, they also inadvertently created sprawl. Operational data has become increasingly fragmented, and to reign it in, more teams are looking to data mesh as a solution.

I’ll begin with some background on data mesh and its history, then share some pointers on creating a strong data mesh foundation for your organization.

## What Is Data Mesh?
Data mesh is a decentralized data architecture — itself a subcategory of software architecture — designed to enable businesses to become more data-driven.

As my colleague [Rajoshi Ghosh](https://www.linkedin.com/in/rajoshighosh/) describes it, “[The idea behind data mesh](https://hasura.io/blog/graphql-and-the-data-mesh-developer-productivity-in-an-age-of-exploding-data?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=why-data-mesh-demands-more-attention) was to create an architecture that unlocked access to a growing number of distributed domain data sets, by treating data as a product and implementing open standardization to enable an ecosystem of interoperable distributed data products.”

## History of Data Mesh
Data mesh was largely invented in 2019 by [Zhamak Dehghani](https://www.linkedin.com/in/zhamak-dehghani/) at [ThoughtWorks](https://en.wikipedia.org/wiki/Thoughtworks). ThoughtWorks is an influential technology company whose chief scientist, [Martin Fowler](https://www.linkedin.com/in/martin-fowler-com/), helped mint another big idea in software — [agile development](https://thenewstack.io/heres-what-a-software-architect-does-in-an-agile-team/) — in 2001. Agile was a rebranding of Extreme Programming (XP) after Microsoft Windows XP was released in 2001. Like XP, agile was framed as a set of guiding “principles” but stripped of XP’s implementation details.

While data mesh is more of a younger sibling to, rather than a descendant of, agile, it is also framed in the same ThoughtWorks “house style” as a set of vague principles. Data mesh is also a descendant of domain-driven design (DDD), created by software design consultant Eric Evans in 2003. Like data mesh, DDD also recommends decentralization, though more in how software teams and their processes are organized rather than the software product itself.

Alongside this history of software design theory is a history of software design actuality, especially in the design of data systems. A good candidate for marking the beginning of the recent history of data systems is the rise of big data and [cloud computing](https://thenewstack.io/cloud-native/) circa 2010. Cloud computing and commodity hardware accelerated the downward trend on infrastructure costs, lowering the expense of generating and storing data. Smartphones and ad networks readily exploited the added capacity, generating data volumes significantly larger than what anyone had seen before. The standard data processing tools in use at the time — [data warehouses, data marts and data cubes](https://aws.amazon.com/what-is/data-mart/) — were built on already decades-old technology. They struggled to handle these massive data volumes, even in cases as simple as computing sums and averages.

This new era was dubbed “big data,” and specialized scale-out NoSQL data processing systems like Apache Hadoop and Apache Spark emerged to handle the massive amount of data from smartphones and ad networks. A key way these tools addressed the issue was to “push compute to data.” Pushing compute to data was an arduous, technically challenging task, which helped drive the centralization of data when the first general-purpose scale-out SQL software solutions, [AWS](https://aws.amazon.com/?utm_content=inline+mention) Redshift and [Google](https://cloud.google.com/?utm_content=inline+mention) [BigQuery](https://en.wikipedia.org/wiki/BigQuery), became usable five years later.

These factors preserved and even intensified the existing bias toward centralization in data systems, and all were driven and determined by technology. From the previous generation of vertically scaled data warehouses to the current generation of horizontally scaled data warehouses to the extract-transform-load (ETL) pipelines that feed the Hadoop and Spark batch job analytics, these were specialized technologies demanding specific skills and, consequently, centralization.

The trend toward centralization continues, but the demand for specialization has relaxed as data technology has evolved. Products like AWS Redshift [Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) and AWS [Athena](https://aws.amazon.com/what-is/presto/) thoroughly separated compute and storage, offered a SQL interface over heterogeneous data in object stores, relaxed the demand for transformation (the “T” in “ETL”), and encouraged dumping raw data into data lakes in AWS S3, Google Cloud Storage or [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure Blob Storage. Next-generation data warehouses like [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) and ClickHouse continued this trend by removing the need for specialized data warehouse schema designs altogether.

Specialization is just one of the forces that drove centralization. Others include data governance, data stewardship and the technology impediments to any alternative. This brings us to 2019 and sets the stage for the data mesh.

Dehghani identified countervailing forces driving toward decentralization, articulated those as threads and wove them into a narrative. Then she connected this narrative to previous big ideas like DDD and microservices, urged practitioners to overcome the impediments involving data governance, stewardship and more, distilled a set of guiding principles, and branded the whole package “data mesh.”

The four guiding principles she outlined are:

**Domain ownership:**Divide the data architecture into components according to the business units and assign responsibility for those components to those business units.**Data as a product:**Assign elevated responsibility to those business units over their data components, requiring them to offer the same level of quality to the data as they would to any product.**Self-serve data platform:**Provide those business units with software and hardware infrastructure, which enables them to meet their elevated responsibility.**Federated computational governance:**Foster collaboration so that the responsibility to comply with governance policies can be optimally shared between those business units and a central authority.
However, she left out concrete implementation details and actionable advice on how to *obtain* a data mesh. *This* brings us to 2024 and sets the stage for the current state of the (data) mesh.

## Aligning Technologies With Data Mesh Principles
Among the technologies used to make data mesh a reality, a self-serve platform is necessary. This can be analyzed along two dimensions: what the data is, and how the data is served.

### Data
Data typically falls into two broad categories: operational and analytical.

- Operational data comprises traditional online transaction processing (OLTP) data facilitating ongoing business functions, demanding low latency and high recency, allowing low volume, and comprising a mix of read and write operations.
- Analytical data involves traditional online analytical processing (OLAP) data for decision support, demanding high volume, allowing high latency and low recency, and comprising exclusively read operations.
### Serving
Serving data typically is performed either with a query language or with an API.

- Query language is a general-purpose, highly flexible, high-expressivity language that represents the full intent of ad-hoc data requests in a single operation. It’s usually for OLAP over OLTP and powering decision support and business intelligence (BI) systems, e.g. SQL.
- APIs are special-purpose highly-inflexible low-expressivity sets of Remote Procedure Calls (RPC) that represent a preordained data request usually for OLTP over OLAP and powering desktop and mobile applications, e.g. REST
A data mesh may be over operational data, analytical data or both. Consequently, a data mesh may be powered by a query language, APIs or both. The list of candidate query languages is quite short: [SQL](https://roadmap.sh/sql) and [GraphQL](https://roadmap.sh/graphql). The list of candidate API formats is equally short: REST and GraphQL. The careful reader will note the presence of GraphQL in both of these lists; there will be more on that later.

## Bringing Data Mesh to Life
Three technologies emerge to make data mesh a reality: data catalogs, API gateways and distributed query engines.

**Data Catalogs**
Data catalogs such as [Atlan](https://atlan.com/), [Collibra](https://www.collibra.com/) and [Amundsen](https://www.amundsen.io/) abide by three of the four guiding principles: domain ownership, data as a product and federated computational governance. Where they tend to fall down is in the fourth principle, self-serve data platform. A few — notably [Alation](https://www.alation.com/) and [OpenMetadata](https://open-metadata.org/) — do offer a limited self-serve data platform using pass-through SQL. However, they generally lack the ability to blend and join heterogeneous data from multiple sources, stunting their ability to grow into a full-blown data mesh.

**API Gateways **
API gateways such as [Hasura](https://hasura.io/?utm_content=inline+mention) and [Apollo Router](https://www.apollographql.com/docs/router/) tend to concentrate on just one guiding principle: self-serve data platform. Both manage this by settling on GraphQL, which is both a query language and an API format.

As a query language, GraphQL arguably is less powerful than SQL; however, its limitations coupled with its uniformity, its machine-readability and its self-describing nature make GraphQL an effective self-serve data platform for heterogeneous data from multiple sources. Moreover, in its dual role as a query language and an API format, GraphQL covers both analytical OLAP data and operational OLTP data.

Where GraphQL and API gateways tend to fall down is in the principles of domain ownership, data as a product and federated computational governance. There is some progress on this front, however, with the introduction of [Hasura Schema Registry](https://hasura.io/blog/breeze-through-collaboration-with-the-hasura-schema-registry), [Hive](https://the-guild.dev/graphql/hive) from The Guild and [Apollo Studio](https://studio.apollographql.com/).

**Distributed Query Engines **
Not to be overlooked are distributed query engines such as [Trino](https://trino.io/) and [PrestoDB](https://prestodb.io/). These build on the simpler pass-through SQL of data catalogs like Atlan and OpenMetadata with a much more sophisticated execution model that adds cross-database joins, predicate push-downs and relatively efficient query processing. Large latencies may limit their utility for operational data, but they are quite promising for the analytical data workloads of data meshes, at minimum.

## Crafting the Ideal Data Mesh Recipe
Currently, a real data mesh that takes theory into practice must be cobbled together from parts. Few (if any) products on the market adequately adhere to all four of the four guiding principles. A recipe for creating a data mesh would include these two components:

**Data catalog:**Domain ownership, data as a product and federated computational governance require a vast suite of services, including lineage, provenance, quality metrics, documentation and collaboration. So far, only data catalogs offer the complete suite in earnest: Consequently, a data catalog is a non-optional piece of your data mesh recipe.**API gateway:**If operational data workloads are among your data mesh workloads, an[API gateway is almost a “must-have.”](https://hasura.io/blog/elevating-your-api-strategy-with-hasura)The few options all use GraphQL, so GraphQL must also be present in your data mesh recipe. The two leading options, Hasura and Apollo Router,[work well together](https://hasura.io/blog/accelerate-your-apollo-graphql-federation-journey-with-hasura?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=why-data-mesh-demands-more-attention), however only Hasura is really set up for adapting existing data sources with GraphQL.
A distributed query engine like Trino or Presto is another option to augment the data mesh’s self-serve data platform, but at the cost of additional operational complexity.

## Wrapping Up
Building and deploying a data mesh from these components is a tall order that involves details beyond the scope of this introductory article. Hopefully it has helped to clarify the history of data mesh, explain how it fits within an overall data strategy, dispel some of the vagueness around data mesh, develop a mental model about data mesh, and offer concrete and actionable advice to take data mesh from theory into practice.

One thing I do know: We are just scratching the surface of its potential. Many are recognizing its utility in machine learning, analytics or data-intensive applications, all of which are becoming table stakes to compete in today’s data ecosystem To quote Rajoshi again, [with data mesh](https://hasura.io/blog/graphql-and-the-data-mesh-developer-productivity-in-an-age-of-exploding-data?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=why-data-mesh-demands-more-attention), “organizations are much better equipped to navigate the evolving demands of data-driven app development, setting a new standard for efficiency in the digital era.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)