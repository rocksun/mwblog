# How Apollo Makes LLMs More Reliable With GraphQL
![Featued image for: How Apollo Makes LLMs More Reliable With GraphQL](https://cdn.thenewstack.io/media/2024/10/6633051f-aakash-dhage-i5_hrkczgvk-unsplash-1024x576.jpg)
NEW YORK — We all know how AI/ML can be a hit or miss for [DevOps](https://thenewstack.io/devops/) support and [application development](https://thenewstack.io/the-reality-of-edge-application-development/). However, in the case of [GraphQL search queries,](https://thenewstack.io/graphql-to-rest-api-connectors-is-apollos-biggest-thing/) it appears to function at least reasonably well — and there is much more to come.

This was one of the key takeaways from [Apollo GraphQL](https://www.apollographql.com/?utm_content=inline+mention)’s [Annual Users Conference](https://summit.graphql.com/connect) here earlier this month. At the venue, the company rolled out what is not just another AI offering that in too many cases seems perfunctory at best, but one they claim already provides tangible value: the Apollo GenAI Toolkit.

“With its release of the Apollo GenAI Toolkit, Apollo now has all the tools needed to provide AI with the hints and hooks necessary to translate intent into the desired result,” [Matt DeBergalis,](https://www.linkedin.com/in/debergalis) CTO and co-founder of Apollo GraphQL, said during the conference keynote. “This approach ensures the process remains agile, experimental and safe.”

The Apollo GenAI Toolkit is used to build [large language models (LLMs)](https://thenewstack.io/llm/) and LLM-powered applications on top of a graph, along with an open source template to help users get started, DeBergalis said.

There are two fundamental ideas in this architecture: The first is that the graph will be used for [orchestration](https://thenewstack.io/llamaindex-and-the-new-world-of-llm-orchestration-frameworks/), DeBergalis said. In this setup, the LLM’s role is to translate the user’s natural language request into a [GraphQL](https://thenewstack.io/the-unlikely-journey-of-graphql/) query that accurately expresses the user’s intent. The graph’s role, in turn, is to execute that query, orchestrating the appropriate API calls while enforcing the necessary security and rules for the request, DeBergalis said.

The second part addresses where the queries come from. In this architecture, the [chatbot](https://thenewstack.io/5-ways-chatgpt-could-supercharge-chatbots/) is restricted to selecting from a library of safe, pre-written queries. These queries are stored in a [vector database](https://thenewstack.io/what-is-a-real-vector-database/), like [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention), where a similarity search is conducted. This process allows the LLM to choose the most relevant query from the library based on the user’s request. It then uses context provided by the user — such as the name of an item or other details— to translate that into the specific arguments for the query, DeBergalis said.

“If you’re familiar with LLM functions and plugins, think of this approach as a ‘smart function factory,’” DeBergalis said. “You don’t need to write new code every time you want to expand the LLM’s capabilities — you simply write a query. This makes the process both safe and efficient.”

In a demo during the keynote, an LLM was taught to incorporate end-user responses for queries that involved [retrieval-augmented generation (RAG)](https://thenewstack.io/graph-rag-how-to-squeeze-more-value-from-ai/) data in a MongoDB database. It learned how to identify a persisted query. The end user in the demo was able to gain information about a snowboard in real time.

## GraphQL Right Stuff
The more

[@GraphQL]can automate the federation of APIs for orchestration, the less developers have to worry about managing infrastructure so they can do their work. One of my takeaways from the[#GraphQLSummit]and[@apollographql]CTO[@debergalis]´s keynote.[pic.twitter.com/ziqSfr5QUm]— BC Gain (@bcamerongain)

[October 9, 2024]
The reason GraphQL is particularly well-suited for search queries largely lies in its limited scope for LLMs to consider. There are only so many specific requests that can be made, making it inherently less complex than wide-scale LLMs, which attempt to address a much broader range of tasks. The focused nature of GraphQL queries aligns well with LLMs, as the scope is more manageable, leading to more consistent and accurate results.


[@apollographql]’s Ben Newman during his talk “An AI-enabled Supergraph: From Text-to-Query to Conversational Agents” at[#graphqlsummit]: “Are LLMs “any good at writing GraphQL queries?..I have some good news: they really are.” at[@thenewstack][pic.twitter.com/TFmJEpU40z]— BC Gain (@bcamerongain)

[October 10, 2024]
During the keynote, software architect [Benjamin Newman](https://www.linkedin.com/in/newben/) described how Apollo has added a connector subgraph that uses a [REST API](https://thenewstack.io/rest-still-outshines-graphql-for-many-api-use-cases/) to communicate with the original system that serves as a good fit for AI. While this might seem like an increase in complexity with the connector, the real benefit is that users have a uniform query interface that can be used by customers through chatbots and their chat UIs, as well as by developers behind the scenes in their IDEs for coding system notations, Newman said.

“Although it’s difficult to predict what the intermediate layer will look like as agents improve, the agents will eventually be able to use the same tools that humans use — namely, GraphQL queries and the router, along with all the advantages that come with GraphQL,” he said. “So, whatever AI experiences you end up building, if they interact with APIs, you’ll likely wish you had a GraphQL layer to mediate those interactions.”

For those skeptical of AI, adopting GraphQL “sooner rather than later is advisable,” Newman said. “At the end of the day, you only need AI to provide a flexible, natural language frontend that can take user requests and translate them into machine-executable operations,” Newman said. “It’s a mouthful, but all of these technologies exist today and work incredibly well.”

The main feature is how AI works well with the use of persistent queries with GraphQL. Because the chatbot can trust that these queries are safe to execute, it can operate behind the scenes without needing to ask for permission each time, Newman said. This allows the chatbot to respond more conversationally. There’s much more that could be done to make the system more intelligent. For example, if a persistent query isn’t available, it could fall back to generating a new query in real time,” Newman said.

## Hype Buster
“We can use

[#LLMs]as they exist today to turn[@GraphQL]into self-documented … entities that human users can use today..and then just wait for agents to catch up,”[@apollographql]’s Ben Newman said during his talk today at[#graphqlsummit].[@graphqlsummit][@thenewstack][pic.twitter.com/QRSpChSEoB]— BC Gain (@bcamerongain)

[October 10, 2024]
AI is not necessarily living up to the hype when applied to all systems for developers and operations teams, at least not as yet. Newman, during his keynote, cited Salesforce, as “ready to proclaim victory” with the launch of its new product, [Agentforce](https://www.salesforce.com/agentforce/).

“They promise that this is what AI was meant to be, with their marketing team on record claiming that they’ll have 1 billion agents using Agentforce by the end of 2025,” Newman said. “This might prove useful over time, and it’s clear that engineers are working hard to solve interesting problems, However, it seems incredibly premature to declare this kind of victory.”

Newman shared with me that, in many cases, organizations are prematurely relying on RAG systems that cannot adequately process data in a way that makes LLMs useful.

“A lot of people end up setting up these RAG systems where they’re just dumping any old type of document into it — like, PDFs are notoriously difficult to vectorize, and it’s just so much harder than it has to be if you sort of know what you’re going to be answering questions about,” Newman told me after his keynote.

Referring to Salesforce making claims about AI, Newman told me: “Reading that, my blood pressure rose a little. I can imagine the engineers working on that product were probably quite proud of it, but then the marketing team just ran away with their claims.”

## RAG-Centric
As generative AI gains ground with GraphQL and across computing in general, RAG will play a key role. The GraphQL use case also covers MongoDB’s vector instances, chatbot infrastructure and other processes. As [Benjamin Flast,](https://www.linkedin.com/in/benjamin-flast) director of product, search, and AI at MongoDB, explained during the keynote, RAG brings context into applications and supports prompts for LLMs to be more consistent.

“The way that it works is you take some sort of retrieval mechanism, whether that’s a database query or some vector search query, and you go and fetch the relevant logic and you bring it into the model to ground the results that it’s going to prompt,” Flast said. “And this helps with applications, you know, across the board, including chatbots and others that I already mentioned, but just making them more reliable and consistent.”

Meanwhile, other use cases are emerging. GraphQL search queries already serve as an excellent use case for LLM support, which includes chatbots, knowledge assistants, code assistants and knowledge management, Flast said.

“We’re primarily seeing that there are more safe use cases happening today. And these are finding a good fit, and people are comfortable with what they’re doing, and for the most part, you know, they’re good today,” he said. “But rapidly, we’re already seeing people start to push the boundaries of where they bring these apps into production and what kind of capabilities they’re building using generative AI.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)