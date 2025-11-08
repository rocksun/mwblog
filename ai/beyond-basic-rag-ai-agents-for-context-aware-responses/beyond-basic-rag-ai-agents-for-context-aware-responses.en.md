It’s been fewer than three years since the first release of ChatGPT. The initial [large language models (LLMs)](https://thenewstack.io/introduction-to-llms) were popular, but far from accurate. So [retrieval-augmented generation (RAG)](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary) emerged as an approach that markedly improves generative AI results by automatically feeding current and relevant proprietary data into LLMs.

RAG incorporates structured data from spreadsheets and relational databases as well as unstructured data from emails, PDFs, chats, social media and more. It preprocesses and indexes this information and harnesses semantic search tools to retrieve what’s needed for a specific query by referencing internal data pools in addition to more generic LLM data to provide far more relevant answers.

> …84% of data and analytics leaders say their data strategies need a complete overhaul for their AI ambitions to succeed.

Supplementing LLMs with more trusted internal data produces better AI output as fresher information can be used from verified sources. But RAG is far from perfect.

It is challenged by complex, unstructured data like tables, charts, emails and social media posts. For example, it may misinterpret formatting within certain types of unstructured information and produce faulty responses. In other cases, RAG can output answers that are too general, too detailed or incomplete.

This severely constrains the value organizations can extract from their vast stores of unstructured data. The stakes are high, as a new Salesforce report found that [84% of data and analytics leaders say](https://www.salesforce.com/resources/research-reports/state-of-data-analytics/) their data strategies need a complete overhaul for their AI ambitions to succeed. This problem must be overcome if autonomous AI agents are to be implemented broadly and effectively.

## Understanding the Limitations of RAG

Why does RAG tend to misinterpret some forms of unstructured information? The retrieval mechanisms it utilizes create several issues:

**Poor chunking:** Simple methods of splitting documents can separate related information, like tables from their text, leading to loss of context. This process ignores the document’s internal structure (headings, bullet points), treating it as a flat stream of text. For example, a table might be separated from the explanatory text, making the retrieved data unhelpful.

**Semantic gaps:**While semantic search finds similar concepts, it can fail with ambiguous queries, take them too literally or struggle when the answer requires multi-hop reasoning across several documents. The system might retrieve an irrelevant chunk that is semantically similar but factually incorrect. For example, it may retrieve keywords but from the wrong part of the document or a completely unrelated document.

**Non-textual data issues:** RAG struggles to handle non-textual elements like tables and charts. It may also misinterpret scanned documents due to errors in the optical character recognition (OCR) process.

**Hallucinations:** Incomplete or contradictory retrieved data can cause the LLM to “hallucinate” or provide inconsistent answers. This isn’t a rare occurrence; [89% of data and analytics leaders with AI](https://www.salesforce.com/resources/research-reports/state-of-data-analytics/) in production say they’ve experienced inaccurate or misleading AI outputs. With leaders estimating that over a quarter (26%) of their organizational data is untrustworthy, the root of the problem becomes clear. And the lack of traceability in the RAG pipeline makes it difficult to verify the source of the information.

**Continuity:** RAG tends to treat data transformation and preprocessing as one-time tasks rather than a continuous process.

In essence, traditional RAG implementations are insufficient for the complexity of real-world data. This is prompting a strategic shift. Instead of chasing bigger models, the focus is now on building the unified data foundation required to make them truly usable. That unified foundation is the first critical step to delivering accurate, secure, contextual and enterprise-ready AI. This doesn’t mean the industry is abandoning RAG. Instead, it’s developing advanced systems to comprehensively handle unstructured data. Being able to process these formats is a crucial differentiator in today’s competitive landscape.

## The Importance of Continuous RAG Experimentation

To provide more relevant and accurate answers, we must experiment to improve unstructured performance. To do so, we must learn how best to inject LLMs at key RAG stages and optimize metadata to boost the accuracy of answers. This is vital for both immediate gains and long-term innovation. In some cases, it might demand stripping HTML tags. In other cases, flattening data structures may be the best way to handle tables, charts and complex formatting within documents.

RAG experimentation, then, calls for refining how structured and unstructured data are processed and leveraged to maximize their value. It entails building “graphs of significance” that map out how different data entities connect, allowing AI to make personalized recommendations and find the most relevant information for any given query.

> Instead of chasing bigger models, the focus is now on building the unified data foundation required to make them truly usable.

Rather than just using the LLM to generate an answer, LLMs are injected at key RAG stages so that each step is performed more intelligently and accurately. This transforms RAG from simple retrieval into personalized data recommendations based on the most relevant information for a given query.

But experimentation isn’t a one-time deal. Continuous data transformation and preprocessing adjustments can go a long way toward ensuring the data fed into AI models is of the highest quality. By doing so, AI output becomes more accurate and effective. This continuous learning process entails constantly testing how documents are transformed, content is parsed and data is preprocessed.

## Key Use Cases for Agentic RAG

The new approach to RAG utilizes [AI-based agents](https://thenewstack.io/beyond-ai-models-data-platform-requirements-for-agentic-ai) to level up the information retrieval process. These agents quickly learn to route user queries to the most appropriate data sources, analyze queries and refine them to improve accuracy and relevance. They generate detailed plans of action and can execute those plans to achieve certain goals or accomplish specific tasks with grounded business context.

Domain-specific AI agents add flexibility and can function across a broad range of diverse applications and internal teams (sales, marketing, finance and more). They can learn, adapt, refine and improve output relevance over time. As they scale easily, they are suitable for large enterprise applications. And their multimodal nature means they can interpret and create content across a broad range of modalities, including text, images, audio and video.

Use cases include:

* Answering questions smoothly, precisely and efficiently in real time via virtual assistants or chatbots.
* Automating customer support tasks such as resolving common inquiries, scheduling appointments and providing technical assistance.
* Automating retrieval, cleansing and integration processes that streamline the management and analysis of massive data sets.
* Raising the confidence level of predictions and forecasts by business intelligence applications used in market research, competitive analysis and trend identification.
* Aiding researchers in literature reviews, diving deeply into large data sets and generating hypotheses by providing relevant and structured information.

## Closing the Gap: From Data Insights to Real-Time Action

What if the gap between knowing our data and acting on it disappeared? What if every insight we had could instantly become action? We can achieve this by building autonomous agents on top of LLMs and RAG. These systems create a layer of intelligent context, allowing your data, business logic and customer data to finally speak the same language.

This unified understanding allows agents to be fueled by the full depth of your enterprise data — the trillions of records and real-time signals previously trapped in dashboards. The result is highly autonomous agents that deliver nuanced, business-specific interactions. This is how we eliminate the lag that causes missed opportunities, ensuring every engagement is powered by **intelligent context** — right when it matters most.

*Learn more about the agentic capabilities of the [Salesforce Data 360](https://www.salesforce.com/data/%20) and how it takes RAG to the next level by improving reasoning, trust and accuracy.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/08/d00c7f3f-rahulauradkar-600x600.jpg)

Rahul Auradkar is EVP & GM - Data 360 and AI Foundations at Salesforce.

Read more from Rahul Auradkar](https://thenewstack.io/author/rahul-auradkar/)