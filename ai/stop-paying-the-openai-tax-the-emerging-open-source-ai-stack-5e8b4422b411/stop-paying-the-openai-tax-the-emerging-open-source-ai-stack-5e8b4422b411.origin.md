# Stop Paying the OpenAI Tax: The Emerging Open-Source AI Stack
*A set of open-source models and tools that enables any developer to build a state-of-the-art AI application.*
If we could go back in time and tell software engineers that their apps would be powered by mysterious AI, whose inner workings we’d have no knowledge of, and that they would surrender their most sensitive data to shadowy third parties for the convenience of the experience, they would probably shake their heads in disbelief. But here we are.

Today, developers worldwide are reimagining their applications around AI, and by default that has meant integrating proprietary large language models (LLMs) into every facet. But while proprietary LLMs like those from OpenAI and Anthropic sparked the AI revolution, they also present significant drawbacks: staggering costs, data privacy concerns, vendor lock-in, and lack of customizability. The trade-off of performance and control for revolutionary capabilities initially felt like a bargain worth making, but many developers today want a different way.

But revolutions have a way of democratizing what was once exclusive. While the initial AI buzz focused on proprietary models, the real revolution has been the meteoric rise of open-source LLMs as a viable alternative to proprietary models from the likes of OpenAI. There has also been a quiet explosion of innovation in open-source AI tools that enable developers to leverage the increased reasoning capabilities of open-source LLMs and translate them into useful applications — everything from model deployment and hosting tools to data storage and retrieval, to frontend and backend web frameworks.

To help you navigate this new landscape, and based on conversations with hundreds of developers and other AI tool builders, we’re sharing our picks for the **“Easy Mode” open-source AI stack** — the most developer-friendly models and tools for building AI applications. Here’s how the stack’s components work together to empower developers and reshape the future of AI:

*The “Easy Mode” open-source AI stack. A selection of the top models and tools that make it easy for developers to build AI applications that enable maximum control over data privacy, cost, and performance.*
This open-source suite of AI tools returns full control over deployment, privacy, and performance to developers, all without sacrificing the intelligence of their app. Developers now have the tools to build and deploy AI solutions however they want — locally, in the cloud, or at the edge. And they retain 100 percent control over their data and don’t have to worry about what “trusted” third parties might do with potentially sensitive information. This isn’t just a technical shift; it’s a cultural one, marking a return to the core values of developer autonomy and innovation.

This is the promise of the open-source AI stack — a set of models and tools that enables any developer to build a state-of-the-art AI application. It’s more than just a set of technologies; it’s a move toward making innovation accessible to every developer.

# Key Components of the Open-Source AI Stack
# 1. LLMs: Open-source models
*A selection of the top open-source free LLMs that rival proprietary models from OpenAI, Anthropic, and Google. These include Llama 3.3 from Meta, the Mistral model family, the Qwen family of models, Phi 3 from Microsoft, and DeepMind’s Gemma 2.*
Open-source large language models are at the forefront of democratizing AI. Models like the [Llama 3 family from Meta](https://www.llama.com/?ref=timescale.ghost.io), [Mistral 7B and Pixtral 12B](https://mistral.ai/technology/?ref=timescale.ghost.io#models), [Qwen 2.5](https://github.com/QwenLM/Qwen2.5?ref=timescale.ghost.io) from Alibaba Cloud, [Phi 3](https://azure.microsoft.com/en-us/blog/introducing-phi-3-redefining-whats-possible-with-slms/?ref=timescale.ghost.io) from Microsoft, and [Gemma 2](https://blog.google/technology/developers/google-gemma-2/?ref=timescale.ghost.io) from DeepMind are free to download and use and can be run by any developer with access to sufficient hardware.

These open-source models rival proprietary solutions, offering the following advantages:

**Greater data control:**Using open-source models keeps all data private, eliminating reliance on third parties and giving developers greater guarantees of security and compliance.**Competitive reasoning performance:**Open-source models are increasingly competitive on benchmarks like[MMLU](https://paperswithcode.com/dataset/mmlu?ref=timescale.ghost.io),[HumanEval](https://github.com/openai/human-eval?ref=timescale.ghost.io), and[MATH Reasoning](https://paperswithcode.com/sota/math-word-problem-solving-on-math?ref=timescale.ghost.io), indicating the shrinking gap in reasoning between open-source and proprietary models.**Deployment flexibility and customizability:**You can adapt models for niche use cases without vendor constraints by fine-tuning yourself or accessing publicly available model fine-tunes and variants.**Efficiency and scalability of smaller models**: Smaller open-source models often require less computational power, making them cost-effective and easier to deploy on resource-constrained devices or environments while still delivering strong performance for specific tasks.
# 2. Embedding models: Open-source embedding models
*A selection of the top open-source embedding models. These include Nomic, BGE from BAAI, the Sentence Transformers family, and models from Jina AI, amongst others.*
Vector embeddings are extremely useful in modern AI applications. They power search and RAG (retrieval-augmented generation) capabilities to enable LLM apps to respond with more grounded, contextually relevant answers.

Just like in open-source LLMs, there has been significant progress in open-source embedding models that rival proprietary solutions like OpenAI’s text-embedding-3 model family and Cohere’s embed-multilingual-v3.0. The leading open-source embedding models include:

Open-source family of embedding models featuring various sizes and specializations, from the lightweight all-minilm to multilingual models.**Sentence Transformers / SBERT:****Nomic:**BGE (BAAI General Embedding) models map text to dense vectors for retrieval, classification, and semantic search tasks. The latest BGE-M3 model supports over 100 languages and can process documents up to 8,192 tokens. It features multi-functionality (dense retrieval, multi-vector retrieval, sparse retrieval) capabilities.**BGE (BAAI):**Jina AI’s jina-embeddings-v3 is a 570-million parameter model supporting 89 languages, with exceptional performance in 30 core languages. It features an 8,192 token input length, configurable output dimensions up to 1,024, and specialized capabilities for query-document retrieval, clustering, classification, and text matching.**Jina AI:**
# 3. Model access and deployment: Ollama
*Ollama has become the default tool for developers to access and build with open-source LLMs and embedding models.*
Deploying AI models used to be like attempting to launch a space shuttle from your garage. It required an intimidating constellation of expertise: teams of PhDs, complex infrastructure, and resources that would make most organizations buckle. [ Ollama](https://ollama.com/?ref=timescale.ghost.io) has changed the game entirely, allowing developers to run state-of-the-art models with a single command:

`ollama run llama3.2`
By providing access to hundreds of LLMs and embedding models via a single tool, abstracting away infrastructure challenges, and streamlining deployment, Ollama transforms what once felt insurmountable into a seamless, intuitive process. It empowers developers to focus on solving real-world problems, bridging the gap between innovation and practicality both for personal and enterprise projects.

With open-source models and Ollama’s simplicity, developers gain unprecedented freedom to deploy AI however they choose. Case in point: All the models mentioned in the open-source LLMs and embedding models sections above are available via Ollama!

# 4. Data storage and retrieval: PostgreSQL, pgvector and pgai
*PostgreSQL, the open-source database, and its ecosystem of open-source extensions for AI use cases like pgvector and pgai, is the ideal choice for developers wanting to build AI applications.*
Good data and good retrieval are at the heart of the RAG revolution in AI, enabling developers to create LLM applications that give users highly accurate, contextually grounded, hallucination-free answers.

However, the best AI applications go beyond using a vector database — they involve a combination of unstructured, structured, and application data and vector searches over large datasets with complex filters. Such retrieval systems ensure your users get the most contextually relevant answers, but building them can be complex and, in some cases, require multiple database systems and custom data pipelines:

- You need to store documents and other source data to create a knowledge base to be searched against.
- You need a way to pre-process that data, create vector embeddings from it, and keep those embeddings in sync as your knowledge base changes.
- You also need the ability to store and search vector embeddings, often at large scale and with complex filters on both metadata and other user data. Not to mention handling concerns like multi-tenancy, permissions and access control, and high availability, amongst other practical concerns.
The good news is that PostgreSQL, [the most loved database in the world](https://survey.stackoverflow.co/2024/technology?ref=timescale.ghost.io#1-databases), is transforming beyond a trusted relational database into the data layer that powers AI applications, with support for structured data, unstructured data, and fast, accurate vector search.

PostgreSQL is open source and has an ecosystem of open-source extensions that have made it the go-to database to power storage and retrieval for AI applications:

**Vector search:**Extensions like[pgvector](https://github.com/pgvector/pgvector?ref=timescale.ghost.io)and[pgvectorscale](https://github.com/timescale/pgvectorscale/?utm_source=blog&utm_medium=website&utm_campaign=december-AI-launch&utm_content=pgaivectorizer-github)enable vector storage and similarity search,[outperforming specialized vector databases](https://www.timescale.com/blog/pgvector-vs-pinecone/?ref=timescale.ghost.io).**Ease of use:**Extensions like[pgai](https://github.com/timescale/pgai/?utm_source=blog&utm_medium=website&utm_campaign=december-AI-launch&utm_content=pgai-github)simplify accessing LLMs to reason on data in PostgreSQL, and features like[pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer-quick-start.md/?utm_source=blog&utm_medium=website&utm_campaign=december-AI-launch&utm_content=pgaivectorizer-github)make embedding creation and sync as intuitive as traditional database indexes.**Integration and ecosystem:**Pgai’s support for Ollama makes it easy to access state-of-the-art open-source models for embedding creation or reasoning.
**Example:** Perform semantic search with a few lines of SQL:
`CREATE TABLE IF NOT EXISTS blog (`
id SERIAL PRIMARY KEY,
title TEXT,
authors TEXT,
contents TEXT,
metadata JSONB
);
INSERT INTO blog (title, authors, contents, metadata) VALUES ('The Future of Artificial Intelligence', 'Dr. Alan Turing', 'As we look towards the future, artificial intelligence continues to evolve...', '{"tags": ["AI", "technology", "future"], "read_time": 12, "published_date": "2024-04-01"}');
--insert more data here
--Vectorize data in the contents column using models from Ollama
SELECT ai.create_vectorizer(
'blog'::regclass,
destination => 'blog_contents_embeddings',
embedding => ai.embedding_ollama('nomic-embed-text', 768),
chunking =>
ai.chunking_recursive_character_text_splitter('contents')
);
-- Perform semantic search
SELECT
b.title,
b.contents,
be.chunk,
be.embedding <=> ai.ollama_embed('nomic-embed-text', 'What comes next in AI') as distance
FROM blog_contents_embeddings be
JOIN blog b ON b.id = be.id
ORDER BY distance
LIMIT 3;
# 5. Backend: FastAPI
Your application backend connects intelligent models to user-facing applications, and FastAPI has become the framework of choice for developers. It offers:

**Speed and simplicity:**asynchronous programming ensures low latency and high throughput.**Developer-friendly design:**automatic API documentation and type hinting enable rapid iteration.**Seamless integration:**ideal for real-time applications like chatbots, recommendation engines, and predictive analytics.
FastAPI eliminates backend bottlenecks, allowing developers to scale AI applications from prototypes to production effortlessly. Imagine deploying a recommendation system powered by an open-source model. FastAPI’s asynchronous capabilities ensure user requests are processed instantly, while its automatic documentation keeps collaboration seamless. Together, these features turn complex backend workflows into manageable, efficient systems.

# 6. Frontend: NextJS
A frontend for AI apps needs to handle complex state management and dynamic updates, and [NextJS](https://nextjs.org/?ref=timescale.ghost.io) has emerged as the go-to React framework for production deployments.

It offers a number of helpful capabilities:

**Hybrid rendering:**Server-side rendering (SSR) and client-side static rendering give you flexible rendering and caching options for each page. Next.js provides robust server-side capabilities that are particularly beneficial for AI applications. The framework’s SSR helps manage computationally intensive AI tasks efficiently while reducing the load on client devices. This is especially important when handling complex AI model interactions and data processing.**Real-time streaming and updates:**It seamlessly integrates with various real-time solutions to support fluid, dynamic interactions, especially important for AI chat and other UIs displaying dynamic content.**Integration with Vercel AI SDK:**The Vercel AI SDK (also open source) is purpose-built for creating AI applications with Next.js and supports both client-side and server-side AI functionalities. It integrates well with[Ollama](https://sdk.vercel.ai/providers/community-providers/ollama?ref=timescale.ghost.io)and provides utilities for handling AI model inference, streaming responses, and connecting with providers.
# 7. The missing piece: Evaluation and validation
While the open-source AI stack has matured, evaluation remains a key challenge. Projects like [LangFuse](https://langfuse.com/?ref=timescale.ghost.io) and [Phoenix from Arize](https://github.com/Arize-ai/phoenix?ref=timescale.ghost.io) offer promise, but the ecosystem still lacks a comprehensive framework for testing and validating AI models. This gap represents an opportunity for innovation — a chance for the community to define reliable, real-world AI applications.

**Why this matters:** Unlike traditional applications, LLMs are non-deterministic, which means that if you deploy an AI application without evaluation and validation, you have no way to judge the performance of your application. A robust evaluation system is critical to ensure your application performs well both now and as the system evolves.
We should say that we find this gap in capability particularly intriguing given the open-source community’s strong track record in creating tools for observability and monitoring. We think that the evaluation ecosystem, in general, is nascent and that the right approach has yet to be found. We suspect current systems are too cookie-cutter and underappreciate the diversity in evaluation needs across projects. What’s needed is a shift in perspective akin to the **GitOps revolution** in DevOps, and that’s why we are particularly excited to see open-source-driven innovation unleashed in this area.

# Open Access to Innovation: What Will You Build?
The open-source AI stack isn’t just a collection of tools — it’s a movement. Developers now have the freedom to build, innovate, and control their AI applications without vendor lock-ins or privacy concerns.

With open-source AI, you get:

- Freedom to deploy anywhere — locally, in the cloud, or at the edge.
- Full control over data — no third-party sharing.
- Customizability to fit your needs.
- Collaboration with a global community.
It’s not just about tech; it’s about creating what’s yours. Whether you’re deploying models, building RAG apps, or launching new AI services, the open-source stack lets you do it your way.

Get started now:

[Deploy](https://ollama.com/?ref=timescale.ghost.io)an open-source model with Ollama.[Build a RAG app](https://github.com/timescale/pgai/?utm_source=blog&utm_medium=website&utm_campaign=december-AI-launch&utm_content=pgai-github)with PostgreSQL.[Create](https://fastapi.tiangolo.com/?ref=timescale.ghost.io)your backend with FastAPI.
Experiment, iterate, and contribute. The open-source AI revolution is here — what will you build?

*This article was written by Matvey Arye and Avthar Sewrathan *a*nd originally published **here** on the Timescale official blog on December 16, 2024.*