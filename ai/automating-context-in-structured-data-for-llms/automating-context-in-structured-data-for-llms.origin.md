# Automating Context in Structured Data for LLMs
![Featued image for: Automating Context in Structured Data for LLMs](https://cdn.thenewstack.io/media/2024/07/e529156d-meaning-1024x576.jpg)
With the growth of machine learning and generative AI, users are learning they can’t just throw a bunch of data into a model and expect anything close to reliable results. The missing element: context.

Structured data in particular can be useless in [large language models](https://roadmap.sh/guides/introduction-to-llms) without some knowledge of the consistent definition of the words, how they are used in a particular context and the relationships between data.

Too often, though, organizations have data in myriad different stores in different formats and named inconsistently. Israeli startup [illumex](https://illumex.ai/) is tackling the problem with what it calls a “Generative Semantic Fabric” between data stores and AI applications, automatically creating a knowledge graph of all a company’s data, its meaning, context and usage to create an ontology according to business function.

This aligned business meaning and domain-specific context allows organizations to trust the results of their AI initiatives, according to [Inna Tokarev Sela](https://www.linkedin.com/in/innatokarev/?original_referer=https%3A%2F%2Fwww%2Egoogle%2Ecom%2F&originalSubdomain=il), founder and CEO of illumex.

## Creating a Knowledge Graph
Gartner has [urged businesses to adopt a semantic approach](https://info.cambridgesemantics.com/gartner-adopt-a-data-semantics-approach-to-drive-business-value#:~:text=Per%20Gartner%C2%AE%2C%20%E2%80%9CData%20and,value%20and%20break%20data%20silos.%E2%80%9D) to enterprise data to break down silos and drive business value. It recommends [knowledge graphs](https://thenewstack.io/using-chatgpt-for-questions-specific-to-your-company-data/) as machine-readable data structures to represent semantic knowledge. Its report states:

- Semantic models are necessary when you want to understand and describe how things work and relate, or you need to unambiguously exchange or reuse data.
- Businesses that do not use semantic modeling are limited in their ability to source and integrate external data or expose internal data for downstream tasks.
- Application of generative AI technologies accelerates the process of populating a knowledge graph and tagging a document against known relationships. This technology lowers the barriers to rich data semantics and increases data interoperability.
Before you can [turn AI loose on your company data](https://thenewstack.io/using-chatgpt-for-questions-specific-to-your-company-data/), you need to have consistent definitions for the terms involved, but many times that doesn’t happen.

“For starters, sometimes relational structured data is not properly labeled. It has all kinds of abbreviations, and partial naming. Some databases have a limitation of eight characters. So they have all kinds of inventive names in the underlying data. To be able to use semantic models with RAG [retrieval-augmented generation] or other technologies, you first need to semantically label all your data. So, this is like quality control,” Sela said.

First, the platform [maps a company’s existing data](https://thenewstack.io/data-fabric-or-data-mesh-find-the-happy-medium/) in all its sources: databases, warehouses, data lakes and business applications. It creates a knowledge graph by analyzing metadata on a company’s various structured datasets. Business logic for that data is embedded into the data lineage as well as industry knowledge about terminology, workflows, metrics, analysis and tags for each business function.

“We combine dozens of semantic models, not all of them are LLMs, some of them are not traditional ones and also some graph models. They actually understand the structure of customers’ existing metadata and usage — the schema structure of their key queries, also the structure of the business applications. And this gives us the initial understanding of how existing usage looks like,” she said.

This data could show a customer is related to a product, a vendor, an SKU and so on.

“So it comes down to a very rich graph with all existing connections, metrics, analysis embedded in them, and all possible and relevant questions, which come from industry knowledge, are also embedded in them,” she said.

## Tracking Usage as It Happens
Formerly assistant vice president and head of AI at Sisense and senior director of machine learning at SAP, Sela founded illumex in 2021. Its enterprise users include Israel’s Teva Pharmaceutical Industries and New York-based Carson Optical. The company recently announced a $13 million seed round of funding.

Illumex continuously monitors and updates the knowledge graph as it receives information about changes in meaning or usage. You can track the origins and transformations of data elements across your entire data ecosystem. You also can look at the potential effect of changing one data element on other tables, reports, BI dashboards and even specific graphics.

It interprets prompt questions to map queries to the right semantic and data objects and translates the prompt to SQL that can be used in GenAI tools like ChatGPT or Llama.

**The Problem With RAG**
Though considered a way to augment commercial AI models with other, more relevant information such as internal company data, illumex product manager Sagi Keren compares setting up RAG with [assembling Ikea furniture without instructions](https://illumex.ai/blog/dont-get-ragged-by-your-rag-why-generative-semantic-fabric-is-the-future/). It requires data preparation including consistent semantic labeling, setting up vector embeddings and then ongoing maintenance.

That requires tools and processes to continually monitor appropriate sourcing and freshness of the data to prevent hallucinations or merely irrelevance. He also points to unexpected costs from APIs making too-frequent calls to the vector database.

Beyond the need for consistent labeling, RAG requires examples of how data is used for fine-tuning. Those samples generally don’t cover all the possible uses of that data, Sele said.

“You just provide a sample … and it can have customization to a limited degree. This is why companies are still struggling to have consistent results because this training doesn’t really allow consistency in all questions. It has even limited capacity to provide reliability on the same question repeated again and again and again,” she said.

“So when you use RAG, it only addresses the semantic proximity. Right? It doesn’t really address the context of the question. In Generative Semantic Fabric, you actually have relationships embedded as part of it. So [it] understands that a customer belongs to a specific ID or group. It can actually ask about sales context, or maybe marketing, … and has lots of contexts embedded.”

Though semantic consistency previously was handled with catalogs, that approach doesn’t scale in the age of AI, Seles said. The automated [semantic layer](https://thenewstack.io/demystifying-the-metrics-store-and-semantic-layer/) should help ease the friction between business users of the data and the tech side.

“I personally don’t believe people who are doing their day job have to have to understand how algorithms work or how data is named and where it’s stored,” she said.

“Even if the question is not articulated in exactly the language the database uses behind the scenes, you are able to … match customers’ questions to the right business terms, right metrics … And then because its mapping is deterministic, we’re able to create SQL from that to run the data source or to automate context to any type of LLM runtime. So you can pull the Hugging Face, you can pull GPT and other technologies, and

The knowledge graph enables the governance team to see all the agreed-upon definitions and control what the user is going to get as an output. we create automated context for any of them,” she said, adding that it means there’s no lock-in to a specific GenAI vendor.

The system integrates with tools like Slack and Microsoft Teams so users can use natural language to submit queries.

They can say, “’OK, this was your question. This is how we understood it.’ This will help customers define this; this is where data is coming from. And this is how they understood the logic of your question. So they also give feedback to the end user to basically understand if the condition was understood and mapped correctly to the underlying data,” she said.

In addition to generating a real-time business term glossary, it provides column-level provenance of the data, auto-tagging for personally identifiable information (PII), a data exploration feature and alerting on things like duplication of work, breaking changes and projected impact of changes. Its AI Assistant can auto-generate suggested business terms and metrics. With the collaborative analysis function, saved queries automatically provide business context, like the data sources, usage patterns, associated business terms, and related analyses.

As part of its AI readiness management, it enables data teams to understand data lineage and apply governance and specification workflows.

Gartner says [illumex faces the same challenges](https://get.promethium.ai/cool-vendor-successful-generative-ai-projects-require-better-metadata-management) as any vendor relying on knowledge graphs, semantics and metadata: the need for extensive education about them for use at the enterprise level.

“As the industry still struggles with open metadata-sharing standards, illumex may find it difficult to maintain support for bidirectional metadata sharing,” its report states.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)