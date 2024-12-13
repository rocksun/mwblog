# 3 AI Trends Developers Need to Know in 2025
![Featued image for: 3 AI Trends Developers Need to Know in 2025](https://cdn.thenewstack.io/media/2024/12/4e34f0d8-ai-1024x576.png)
Interest in AI has [surged since 2020](https://thenewstack.io/the-year-in-ai-whats-behind-in-2020-and-whats-ahead/) and dominated conversations across headlines and boardrooms ever since. So it’s unsurprising that business development has followed suit — [81% of IT leaders](https://report.confluent.io/key-findings/data-streaming-roi) listed AI and machine learning as an important or top priority in their 2024 budgets, according to survey results in Confluent’s Data Streaming Report.

But is all this attention and investment leading to a near-term future where AI is ubiquitous and functions as intended? It all depends on whether businesses have a sufficient pipeline of engineers equipped with new skills, the right tools and trustworthy data to turn AI promises into real-world capabilities.

Let’s look at the [AI trends](https://thenewstack.io/ai/) that will have the biggest impact on engineering teams and our advice on how to overcome these challenges.

**Trend #1: Hallucinations will continue to be a significant barrier to production as LLM use cases grow.
**
[Large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms) continue to follow a corollary to Moore’s Law, exponentially growing with the amount of training data they consider, the number of parameters that define them and the size of the context window that their attention can consider. Yet, model interpretability remains elusive in general. LLMs in general are poor reasoning agents, so coupling them with machinery we already know works will get us a lot further in [overcoming the hallucinations](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/) that result in relying on LLMs alone.
**Developer Impact**
LLMs are stochastic in nature, while many traditional QA best practices assume the tested system is deterministic. Developers will have to rely on different approaches to test and build confidence in LLM-enabled applications. We can apply historically useful machine learning (ML) techniques and other technologies to measure output quality and minimize hallucinations. With application-specific guardrails in place, engineers can build LLMs capable of reliably identifying when they’re hallucinating or providing information with low confidence scores.

Compared to LLMs, using a small fine-tuned language model will provide a better response. However, developers need to feed it with the right insights, such as events and timely and personalized data, so it can succeed. One promising pattern developers can use to reduce the impact of hallucinations is [retrieval-augmented generation](https://thenewstack.io/how-to-scale-rag-and-build-more-accurate-llms/) (RAG), coupling prompts at inference time with relevant domain-specific information.

**Trend #2: Agentic AI will be more capable of independent decision-making.**
Agentic AI systems promise to make decisions and act independently on behalf of specific business functions, teams and even individuals within the business. However as AI models become more sophisticated, they tend to lose transparency, and that introduces difficult questions for engineering teams to answer when building and deploying AI agents.

**Developer Impact **
Compared to less automated systems, it’s much more difficult to recognize errors in AI before dependent systems consume the outputs. Implementing RAG with real-time data pipelines can help augment agentic AI solutions with important context to improve environmental awareness and decision-making.

As these solutions go from conception to development and production, more organizations will need a [data-streaming platform](https://www.youtube.com/watch?v=hrB71pMVjpw) (DSP) complete with streaming, processing and governance capabilities to sustainably build and scale these capabilities in the long term. Event-driven architectures enabled with a DSP provide an implementation framework for agentic systems, modeling them as asynchronous workflows of composable microservices. This approach promotes the reusability of individual components of agentic systems and makes the larger systems easier to analyze and scale than if they are created as large monoliths.

**Trend #3: Engineering teams are shifting to dynamic data access for AI models.**
Rising demand for dynamic or real-time data access isn’t unique to only AI/ML initiatives, but it has contributed to the growth of real-time intelligence. Over the last decade, engineering teams have increasingly used open source streaming engines like [Apache Kafka](https://kafka.apache.org/) and [Apache Flink](https://flink.apache.org/) to power real-time recommendations, predictions and anomaly detection.

**Developer Impact**
This trend will also affect the infrastructure and teams behind these projects. This shift to real-time data access will allow for more flexible and dynamic data organizations, which enables human users, chatbots and even AI agents to quickly access and query a wide range of data.

## Empowering Engineers With New AI Skills and Better Data
Companies looking for ways to reduce complexity and costs when building real-time AI solutions need to shift data processing left and use data contracts to enable dynamic access to trustworthy data products. The resulting data products can be consumed as either data streams or open table formats. This approach allows data teams to facilitate efficient data processing, supplying engineers with data in a clean, consistent format and enabling them to build dynamic AI applications with more confidence and less risk.

However, providing engineers with trustworthy data isn’t enough to ensure AI initiatives succeed. Leaders also need to motivate experienced engineers to train and mentor junior team members with the time, resources and support to focus on building differentiated applications.

Data engineers can use LLMs and GenAI tools to develop their prompt engineering skills and increase their familiarity with coding templates. It can help if engineers stay sharp on computer science fundamentals, increase their proficiency in popular languages in the data and AI/ML spaces like [Python](https://thenewstack.io/5-python-libraries-every-data-engineer-should-know/) and [Java](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/), and understand real-time data processing and event guarantees.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)