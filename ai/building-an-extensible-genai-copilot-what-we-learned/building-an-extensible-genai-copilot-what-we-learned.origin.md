# Building an Extensible GenAI Copilot: What We Learned
![Featued image for: Building an Extensible GenAI Copilot: What We Learned](https://cdn.thenewstack.io/media/2024/09/fffc5006-building-extensible-genai-copilot-1024x576.jpg)
Our [generative AI (GenAI)](https://thenewstack.io/ai/) journey began with a single use case: How could we make it easier for our customers to navigate the vast landscape of documentation and features within our platform?

It’s crucial that our users can quickly access and understand the product information they need to use our enterprise platform. So, our product team tasked our development team with developing a solution to simplify this process and enhance the overall user experience.

A few months ago, we launched Rafay Copilot, a GenAI-driven bot designed to do just that. This was no small feat. We faced many obstacles when building Copilot — from overcoming the steep learning curve of the AI landscape to ensuring the accuracy of responses and seamless integration with our existing systems. These obstacles forced us to rethink and refine our approach, pushing the boundaries of what we believed was possible with GenAI.

However, these challenges provided us with invaluable insights. As we worked through the complexities of creating Rafay Copilot, we began to see the broader potential of Gen AI. The problems we solved and our breakthroughs led us to realize that what we had developed could be expanded far beyond its original scope and into other areas of our platform.

**Defining the Copilot Architecture**
GenAI has the potential to apply to many use cases in our product, so a major goal while defining the Rafay Copilot architecture was to ensure that it could be easily extended to support other use cases. Such an architecture should be flexible and scalable to support more advanced use cases such as agents or other types of copilots.

We used the [LangChain](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) framework to chain the requests before sending them to the [large language models (LLMs)](https://thenewstack.io/llm/). Qdrant serves as our vector database, efficiently storing and retrieving text embeddings. To monitor the system’s behavior and performance, we rely on Langfuse, which helps us track costs and debug AI services effectively.

Retrieval-augmented generation (RAG) allows the chatbot to access and retrieve specific private data, such as company documentation or proprietary knowledge, to provide more accurate and contextually relevant responses. Langfuse is our [observability](https://thenewstack.io/observability/) platform for monitoring and debugging AI applications.

LangGraph, while not currently implemented, could potentially be used for creating more complex, multistep AI workflows. LangSmith, another tool in the LangChain ecosystem, offers debugging and testing capabilities for LLM applications, which we may explore in future iterations.

### API Gateway and AI Service Layer
All incoming requests to Rafay Copilot go through a centralized API gateway, which we call rafay-hub. This gateway’s primary responsibility is to handle authentication and standardize API requests for our upstream services, ensuring that only authorized users can access the system. Once authenticated and standardized, the request is forwarded to the AI service, which is a proxy for all our agents.

The AI service’s primary role is to decide which agent service should handle the request. We’ve designed this so that it’s easy for us to extend the system in the future. For example, we have an agent service specifically for interacting with OpenAI’s API for our GenAI chatbot. However, the modular design of this layer allows us to add new agents as needed, whether they involve other generative AI models or entirely different types of AI services.

### Agent Services and LLM Integration
Once the AI service determines the appropriate agent, the request is sent to the corresponding agent service. This agent interacts directly with the underlying LLMs. The prompts that guide these interactions are stored in a [Kubernetes](https://roadmap.sh/kubernetes) (K8s) config map, which allows us to adjust them quickly based on system performance or user feedback. This configuration-driven approach enables rapid iteration and fine-tuning, ensuring our chatbot delivers the best possible responses for users.

### Vector Database and Observability
To provide accurate and up-to-date information from our documentation, we’ve implemented a Kubernetes cron job that regularly pulls data from our GitHub repository, where all the docs are stored in Markdown format. This job processes the data and stores it in Qdrant, our vector database, making it easy for the chatbot to retrieve relevant information quickly.

For observability, we’ve integrated Langfuse into the agent services as a callback. This integration allows us to monitor the system in real time, providing insights into costs, responses and customer feedback when interacting with Copilot.

In summary, the Rafay Copilot architecture is thoughtfully designed to meet our users’ evolving needs. It focuses on flexibility, scalability and ease of future expansion.

**Overcoming Challenges**
Even though the architecture diagram above may make it appear that the process was straightforward, we faced multiple hurdles while building Rafay Copilot. Development posed significant challenges, which I’ve outlined below to give you a clearer picture.

**Steep learning curve:**For any organization beginning its AI journey, understanding the AI landscape presents a steep learning curve.**Evaluating LLM options:**With the rise of Generative AI, an overwhelming number of LLMs are available, both from cloud providers and the open source community. Deciding which LLM is best for your business is challenging, and making the wrong choice can significantly impact your outcomes.**Governance:****Cost management:**Since GenAI apps charge based on token usage, it’s crucial to have governance in place to monitor and control costs. Admins need the ability to assign token limits to users or teams on a daily, weekly or monthly basis.**Guardrails:**Security is another key aspect. When interacting with LLMs, especially cloud-based ones, there’s always a risk of users inadvertently leaking sensitive data.**Secrets management:**Managing API keys in an enterprise setting can be complex, especially when multiple users are involved. A gateway is necessary to handle this securely.**Access management:**In organizations that use multiple models, proper access management is essential so that admins can control who has access to which models and to what datasets.
**Prompt evaluation:**Similar to LLM evaluation,[prompt evaluation](https://roadmap.sh/prompt-engineering)is critical to the success of your AI app. Even small changes in wording can lead to entirely different responses, making this a crucial but challenging task.**Observability:**Like any production-ready application, AI apps require strong observability. Integrating tools like LangSmith, Langfuse and LangGraph into GenAI apps takes time and effort, not to mention the ongoing maintenance required by the site reliability engineering (SRE) team.
## Conclusion
Building GenAI applications may sound easy, with a plethora of development tools and frameworks currently available. This may be the case for the early experimentation phase.

However, building enterprise-grade GenAI applications and deploying them in production has many challenges, including finding the right LLM, managing costs, devising data access controls, deploying prompt guardrails and maintaining observability. We used the insights we learned from building Rafay Copilot to develop [GenAI Playgrounds](https://rafay.co/platform/genai-playgrounds/), an integrated development environment (IDE) for developers to prototype and build GenAI applications rapidly. You can try it for free on Rafay’s website.

Enterprise platform teams must carefully look at all the security, data and cost-related considerations and adopt an enterprise-level strategy to solve these challenges before embracing Gen AI widely in the organization. It’s recommended that enterprise platform teams build an in-house solution or use a commercial tool to address these challenges and accelerate GenAI application development and deployment.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)