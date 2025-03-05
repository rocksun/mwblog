# Agentic AI is the New Web App, and Your AI Strategy Must Evolve
![Featued image for: Agentic AI is the New Web App, and Your AI Strategy Must Evolve](https://cdn.thenewstack.io/media/2025/03/9de63de7-phillip-glickman-2umo15jszkm-unsplash-1024x681.jpg)
[Phillip Glickman](https://unsplash.com/@phillipglickman?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/green-and-multicolored-robot-figurine-2umO15jsZKM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
Two years into the generative AI revolution, the LLMs that power tools like ChatGPT and Claude have become startlingly powerful. However, [according to Salesforce CEO Marc Benioff](https://www.salesforce.com/blog/the-agentic-ai-era-after-the-dawn-heres-what-to-expect/), they may be reaching their limits. Per Benioff, the next evolution is not necessarily more intelligent LLMs but autonomous AI agents that leverage LLMs to execute tasks independently.

Benioff is serious about agentic AI, launching Agentforce last year to bring millions of AI agents to Salesforce customers. He’s not alone: consider that Jeremiah Owyang, former Forrester analyst turned venture capitalist, predicted that there will soon be [more AI agents than humans](https://web-strategist.com/blog/2024/09/24/five-ai-agent-predictions/), with as many as [100 AI agents](https://www.linkedin.com/posts/jowyang_vid-spend-10-minutes-with-me-on-this-video-activity-7267255917669171201-eZTK) per person. If even a fraction of these predictions come true, it will have profound implications for the future of e-commerce.

Imagine a world where AI agents take over both sides of the customer-vendor interaction. Customer-facing assets like websites and web apps could be broadly replaced by — or at least integrated with — [AI agents personalized to the customer](https://thenewstack.io/evolving-from-pre-ai-to-agentic-ai-apps-a-4-step-model/). These agents could then interact with a customer’s AI agent, automating the sales cycle with agent-to-agent transactions.

Salesforce isn’t the only one embracing agentic AI. According to a survey of 1,100 executives at large enterprises by [CapGemini](https://www.capgemini.com/insights/research-library/generative-ai-in-organizations-2024/), 10 percent of organizations already use AI agents, more than half plan to use them in the next year, and 82% plan to integrate them within the next three years. Sixty-four percent of these executives expected agentic AI to improve customer service and satisfaction. By 2028, [Gartner](https://www.gartner.com/en/articles/intelligent-agent-in-ai) predicts that 33% of enterprise software applications will include agentic AI.

Given these predictions, it’s only a matter of time before customers expect AI agents to provide them with the information they need to make a purchasing decision rather than searching for it themselves.

The architecture required to deploy agentic AI is now being developed for enterprises looking to stay ahead of the curve and integrate it into their web apps. Specifically, to facilitate thousands of customer interactions worldwide, enterprises will need the ability to deploy low-latency AI inference at the edge.

**Building the Architecture to Support Agentic AI Inference at the Edge**
Developing the architecture to support low-latency inference at the edge is a critical prerequisite for [agentic AI operations](https://thenewstack.io/the-rise-of-ai-agents-how-arazzo-is-defining-the-future-of-api-workflows/) at scale, especially in e-commerce, where AI agents must interface in real-time with customers worldwide. This shift to the edge is already underway: a recent study by[ S&P Global Market Intelligence](https://blogs.vultr.com/New-Report-from-SP-Global-Market-Intelligence-and-Vultr-Provides-Unique-Glimpse-into-Path-to-AI-Maturity) (commissioned by Vultr) found that more than 80% of the 1,000 AI and IT professionals surveyed expect to grow their AI edge operations in the coming year.

However, most enterprises do not have the infrastructure to support edge AI inference at scale, nor will they ever. GPUs and other specialized AI chips are exorbitantly expensive and quickly obsolete, making it impractical to invest in these resources internally.

AI inference served from edge environments requires a different tech stack to make AI at scale cost-effective. For most enterprises, a serverless approach to AI inference will be optimal for both cost and performance.

**Serverless Inference: The Optimal Choice for Cost and Performance**
To avoid the capital expense of procuring dedicated AI chips that will quickly become obsolete, a serverless approach leverages cloud-provider-managed resources to match each AI workload with the optimal compute resource for the task. In short, serverless inference allows the enterprise to leave the infrastructure concerns to cloud providers who deal with this daily.

Leveraging a serverless approach allows enterprises to take advantage of cloud providers’ *silicon diversity* — the hyper-specialization of AI compute chips to address the unique compute requirements at each stage of the AI model lifecycle. From the client’s perspective, a serverless approach automatically manages the scaling of appropriate resources based on the AI workload and use case requirements to optimize cost and performance.

With a serverless approach to managing computing resources and optimizing costs, the next step is to develop the [architecture to support low-latency data streaming](https://thenewstack.io/finding-the-right-data-architecture-for-rag-pipelines/) with data governance controls in place to keep customer data secure.

**Maintaining Data Sovereignty and Privacy With Real-Time Agentic AI Inference**
To go beyond generic AI applications like ChatGPT, agentic AI applications need access to sensitive proprietary data. This is especially true in an e-commerce context, where customer data is essential for AI agents to provide customers with contextually relevant information. Of course, whenever AI models tap into proprietary data, the enterprise must abide by local data governance requirements.

Vector stores and retrieval-augmented generation (RAG) are effective [strategies for maintaining data](https://thenewstack.io/choosing-the-right-database-strategy-on-premises-or-cloud/) governance controls to fuel agentic AI inference wherever the data resides. In this approach, sensitive data is held in vector stores secured with local data governance controls, which AI agents access as needed using [RAG rather than directly training the models on sensitive data](https://thenewstack.io/rag-without-openai-bentoml-octoai-and-milvus/).

Vector stores and RAG enable contextually appropriate insights without exposing sensitive data to a third-party model provider. The vector store’s contents can be replenished without retraining the entire model, which lowers training costs. This approach also makes models more easily transportable across geographies while upholding local data sovereignty requirements.

Data governance aside, enterprises also need low-latency [data streaming to facilitate real-time](https://thenewstack.io/why-we-use-apache-kafka-for-real-time-data-at-scale/) agentic AI interactions. [Apache Kafka](https://kafka.apache.org/), an open source streaming data platform, is ideal for feeding real-time streaming data into agentic AI applications. With RAG and vector stores, Apache Kafka enables low-latency agentic AI applications on the edge while maintaining local governance.

**Agentic AI Intensifies the Need for the Right Architectural Approach**
Compared to traditional AI, [agentic AI will significantly burden engineering](https://thenewstack.io/making-good-on-the-promise-of-open-source-ai/) teams with configuring and maintaining the complex infrastructure required to support swarms of AI agents distributed across vast geographies and thousands of edge devices. The only viable approach is serverless inference combined with RAG and managed Kafka, which ensures that tasks executed by AI agents will be performed accurately and securely with no meaningful latency.

By outsourcing the complexities of infrastructure provisioning, configuring, and auto-scaling to cloud providers, engineering teams can focus on building a robust AI application layer, developing purpose-built AI agents, and prioritizing the customer experience. A serverless approach to AI infrastructure sets the perfect foundation for building a new agentic future for the customer journey.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)