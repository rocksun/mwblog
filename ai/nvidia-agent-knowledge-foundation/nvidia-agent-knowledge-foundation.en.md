Every enterprise company is currently trying to figure out how to have its AI tools work with its data. Meanwhile, every major enterprise vendor that works with those enterprises (think SAP, Microsoft, Salesforce, Workday, etc.) is making a claim on becoming the central hub for managing and securing that data.

But what about the companies that want to do it themselves?

Nvidia, on Wednesday, [announced](https://blogs.nvidia.com/blog/enterprise-platforms-agent-toolkit) how it wants to provide enterprise AI agents with the data they need to make sense of company data — all without competing with the data platforms that already store it.

At its GTC Berlin conference Wednesday, the company added Agent Knowledge Foundation to its [Agent Toolkit](https://thenewstack.io/nvidia-openshell-agent-runtime/). This new collection of open-source components bundles the company’s Nemotron Retriever models, a new Auto-Ontology library, the Kumo family of models for structured data, and its CUDA-X data processing libraries.

With this system, Nvidia says, the data can stay where it is and remain managed under the access rules these companies already have in place.

Today, as Adel El Hallak, Nvidia’s vice president of product for agentic AI, tells *The New Stack*, enterprises may be able to connect an agent to a vendor like Snowflake, but that doesn’t help the agent understand the overall enterprise context.

“I wish it was as easy as connected to my Snowflake system, connected to my email exchange, connected to my knowledge base, and then all of a sudden, magically, the AI understands all the data. But the reality is different,” he says.

Large language models are “great at predicting next tokens,” El Hallak argues, but when presented with a single spreadsheet that has “a whole bunch of tabs,” the agent will have a hard time finding something specific. “It’s gonna struggle,” he says.

## Better retrieval, fewer lookups

“In the world of agents, you want the most accurate embedding models or reranking models,” El Hallak says, even if that adds a bit of latency to each lookup. The agent then gets “much more pertinent information. So the number of lookups at the end, the overall latency actually goes down.”

Nvidia says its Nemotron Retriever embedding model raised search relevance by 65% in tests on an open source OpenSearch setup, needing fewer search steps and adding hardly any latency. SAP’s fine-tuned version of the reranker ran nearly three times faster, Nvidia says, and ServiceNow got better reranking quality with close to 25% less latency.

## From RAG to ontologies

“RAG was awesome, but is it good enough?” El Hallak asks. Knowledge graphs, he says, represent concepts and the relationships between them better than retrieval-augmented generation, which pulls in chunks of text based on similarity.

Nvidia’s [Auto-Ontology library](https://catalog.ngc.nvidia.com/orgs/nvidia/-/containers/auto-ontology/-) builds those graphs from a company’s own tables and maps raw data to business concepts like customers, products, and orders. Its listing in Nvidia’s NGC software catalog shows a REST API and a Model Context Protocol (MCP) server that agents can use to query it.

“You and I, it’s easy for us to understand. A tier is the same thing as a plan when you’re looking at a mobile carrier,” El Hallak says, but LLMs “mess those up.”

Nvidia bought Illumex, an Israeli startup that automated the creation of semantic layers and ontologies for enterprise data, for a reported $75 million in February. At the time, an Nvidia spokesperson told [Globes](https://en.globes.co.il/en/article-1001535871) that the team’s ontology expertise would help it build “libraries and models that will enable the adoption of Agentic AI in organizations.”

## Predictions from tables

Kumo, the startup Nvidia bought in June in a deal The Information valued at more than $400 million, built [foundation models for relational data](https://thenewstack.io/kumo-ai-foundation-models/). Nvidia has since released several Kumo models as open weights on Hugging Face, including Kumo Tabular in September.

El Hallak says those models replace the per-task pipelines data teams used to build “for every classification, for every churn, for every sentiment analysis.”

“The whole point of the ontology … is to bring harmonization as you create those knowledge graphs, so there’s [consistency] across the tables, and then you could use Kumo to drive predictive analytics,” he says.

## Partners, not rivals

“I’m not looking to compete with, for example, a Snowflake. On the contrary, I want to partner with them,” El Hallak says.

Nvidia’s own supply chain team uses Agent Knowledge Foundation through Palantir’s Foundry platform, [building on earlier work](https://thenewstack.io/ai-factories-are-among-the-most-complex-systems-ever-built-nvidia-and-palantir-turn-nvidias-supply-chain-into-a-proving-ground-for-sovereign-ai/) between the two companies. Databricks is pairing a Kumo anomaly detection model with Genie Ontology, the context layer it introduced in June, and Snowflake customers can run Kumo models in Snowflake Notebooks.

“I’m not thinking about ACLs and data access and all those things. That’s why I need the partners,” El Hallak says, referring to access control lists and other security features that its enterprise partners offer.

## Owning the stack

Not every vendor is taking that route. SAP closed its acquisition of Prior Labs, the company behind the TabPFN tabular models, in July and committed more than €1 billion to it over four years. It now offers TabPFN-3.5 Plus in SAP AI Core alongside [its own RPT models](https://thenewstack.io/sap-expands-its-ai-stack-for-developers/).

Nvidia, meanwhile, distributes its models through Hugging Face, which it agreed to buy for $12.9 billion in September. “We just build little weights and models, and we publish them on Hugging Face,” El Hallak says.

That leaves Nvidia building the models, while the likes of Snowflake and Databricks keep control over the data and the permissions around it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)