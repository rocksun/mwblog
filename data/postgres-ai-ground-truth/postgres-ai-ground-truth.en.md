Everyone, it seems, is rushing to [build AI applications](https://thenewstack.io/what-developers-need-to-build-successful-ai-apps/) and agents, seeking new tools to support everything from customer support to internal document retrieval.

But to work reliably, AI applications and agents need access to existing enterprise data, like customer records or support questions. Without this information, stumped agents will simply fill in the blank themselves, a.k.a. hallucinate.

It’s why Jensen Huang, co-founder, president, and [CEO of Nvidia](https://thenewstack.io/nvidia-ceo-details-a-new-ai-way-of-developing-software/), called structured data the “ground truth for AI” in his recent GTC keynote speech.

[Phillip Merrick](https://www.linkedin.com/in/phillipmerrick/), co-founder and Chief Product Officer at [pgEdge](https://www.pgedge.com/), agrees.

“An enterprise needs the agents and AI applications that they built to reference the data that they already have,” Merrick tells *The New Stack*. “So it [structured data] really is the ground truth for AI… It’s how you make sure your LLM [large language model] and your agents aren’t hallucinating; you point them at the actual data.

And Postgres is the best place to point them for that data.”

## Postgres leads the pack for AI workloads

Why [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/)? Merrick isn’t the only one who thinks the database is the best fit for building AI applications.

When asked which database environment they’ve done work in over the past year and which they want to work in over the next year, 66% of all respondents to the [Stack Overflow 2025 Developer Survey](https://survey.stackoverflow.co/2025/technology#most-popular-technologies-database-database:~:text=What%20is%20it%20like%20to%20be%20the%20most%20desired%20and%20the%20most%20admired%20technology%20in%20your%20category%3F%20The%20answer%20lies%20with%20PostgreSQL%2C%20ranked%20highest%20for%20both%20since%202023!) said Postgres.

There’s a good reason the database has held this title since 2023. As Merrick describes it to *The New Stack*, “It’s elegant; it’s easy to get started with and easy to use and easy to develop against,” calling it “the database of choice for AI applications.”

Listing some of the reasons [why Postgres shines](https://thenewstack.io/why-ai-workloads-are-fueling-a-move-back-to-postgres/), Merrick highlights the database’s open source model, underscoring that it is “true” open source: “Postgres is a truly community-based open source project where the contributors are operating as part of a community and not on behalf of their employers.”

> “Postgres is a truly community-based open source project where the contributors are operating as part of a community and not on behalf of their employers.”

He doesn’t name names but indicates that many proprietary databases, though they may call themselves open source, often have some commercial holdbacks. For developers building AI applications, committing to such a proprietary database is a short path to dreaded vendor lock-in.

Scalability is another critical infrastructure concern for AI workloads that Merrick says Postgres is primed for, noting that [OpenAI’s API](https://openai.com/index/scaling-postgresql/) is built on Postgres.

## A one-stop shop for AI data and workloads…

In touting its intuitive, open-source model and scalability, Merrick adds that Postgres is more than a relational database. Through its extension architecture, it can also absorb other database patterns.

Particularly as custom-built vector databases (like [Pinecone](https://thenewstack.io/pinecone-revamps-vector-database-architecture-for-ai-apps/)) come to the fore, Merrick is quick to underscore the advantages of opting for a general-purpose database (i.e., Postgres) with a vector extension (i.e., pgvector):

“Pgvector is just as performant as those standalone vector databases, but with the advantage that it’s standard Postgres. It’s what you’re using for all your other data,” he explains. “Why would you go to one of those proprietary specialist vendor databases just for vectors when you can just do it in Postgres, where you’re doing everything else?”

It’s worth noting that there are instances where developers may prefer to use a proprietary database for greater speed. However, Merrick claims the number of use cases requiring this specialization is dwindling.

Although Huang may have dubbed structured data the ground truth for AI, unstructured data (e.g., support tickets, knowledge bases, etc.) still plays a key role in building successful AI applications. Merrick says Postgres is primed to support both.

He explains that developers can feed their documentation and other unstructured data into Postgres, use pgvector to store, index, and query embeddings, and then build chatbots on top using RAG ([retrieval-augmented generation](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/)).

“So [you’re] using Postgres, not just for your structured data and your vectors but also for your unstructured documents,” Merrick says. “That gives you a great strategy for building your chatbots and agents that need to operate over large bodies of non-structured data.”

He points to the [pgEdge Agentic AI Toolkit for Postgres](https://www.pgedge.com/products/agentic-ai-postgres) as one example of enterprise-grade Postgres-based infrastructure that helps developers build agentic AI applications, supporting the entire cycle from document ingestion to embedding generation to retrieval. “The [pgEdge] docloader takes care of getting your document[s] into Postgres,” explains Merrick. “And then you use that with a vectorizer, and that automatically gets your vectors for you.”

Beyond initial ingestion, Merricks reminds developers to also think about ongoing vector maintenance (i.e., ensuring vectors stay up to date when content changes), something he says many overlook:

“People don’t realize they’re going to have to worry about [it] because, out of the box, things like pgvector don’t give you automatic updates of vectors when the underlying content changes.”

> “People don’t realize they’re going to have to worry about [it] because, out of the box, things like pgvector don’t give you automatic updates of vectors when the underlying content changes.”

That’s why pgEdge’s agentic AI toolkit also includes pgEdge Vectorizer, a Postgres extension that automatically chunks text context and generates vector embeddings to maintain vectors as content changes, and a full-featured MCP (Model Context Protocol) server that works with most version of Postgres and enables AI application builders and code generators (e.g., Claude Code) to connect to both new and existing Postgres databases.

## …with security for mission-critical industries

Whether used separately or together in various combinations, Merrick says the technologies in this toolkit (fully open-source and free for all Postgres users) make it significantly easier for developers to build AI applications on Postgres, whether agentic AI applications or more familiar chatbots operating on a knowledge base.

Either way, he says Postgres is indisputably the way to go, as it provides enterprises with the high availability, data sovereignty, and security needed to deploy and scale AI applications, especially for mission-critical applications in industries like finance, healthcare, telco, and government.

He chalks these advantages up, in part, to the deployment flexibility that Postgres affords, allowing enterprises to run applications on managed cloud databases, self-managed cloud accounts, or on-premises. “So you’ve got that complete flexibility,” Merrick says. “Not all Postgres vendors actually offer this advantage of Postgres. pgEdge does.”

Alongside this flexibility, another likely reason Postgres has become the favored database among developers is its tried-and-true security, to which Merrick says pgEdge adds with its AI tools:

“In our [MCP server](https://www.pgedge.com/download/ai-toolkit), we have both user-based and token-based authentication. We run with encrypted traffic using TLS. And then, while our MCP server supports both read-only and read-write models, by default, everything is read-only, unless you tell it otherwise.”

These security features, combined with distributed Postgres capabilities that support data sovereignty, help enterprises both prevent data leaks and comply with regulations like GDPR, making Postgres the clear front-runner for developing AI applications.

Now it’s up to enterprises to invest in the right infrastructure.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)