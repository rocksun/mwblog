# 3 Reasons Data Engineers Are the Unsung Heroes of GenAI
![Featued image for: 3 Reasons Data Engineers Are the Unsung Heroes of GenAI](https://cdn.thenewstack.io/media/2024/03/4ba5b17e-technology-4256272_1280-1024x683.jpg)
Over the last 18 months, advancements in generative AI have created an insatiable appetite among boards and business leaders. As of September, 87% of C-suite executives
[surveyed by IDC](https://www.idc.com/getdoc.jsp?containerId=US50123123&pageType=PRINTFRIENDLY) say they’re at least exploring potential use cases. And another [77% of business leaders](https://www.salesforce.com/resources/research-reports/state-of-data-analytics/) fear they’re already missing out on the benefits of GenAI, according to a November 2023 [report from Salesforce](https://www.salesforce.com/resources/research-reports/state-of-data-analytics/).
But data leaders understand that no matter how much FOMO their CEOs experience after watching a flashy demo, implementing the
[latest LLMs](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) has to be done thoughtfully. To deliver meaningful business value, [those models](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/) need to be supplied with quality data — while maintaining security, privacy and scalability.
In most organizations, there are key contributors already doing that work:
[data engineers](https://thenewstack.io/top-10-tools-for-data-engineers/). And given the current state of how companies achieve [enterprise-ready AI](https://www.montecarlodata.com/blog-the-moat-for-enterprise-ai-is-rag-fine-tuning/), data engineers will be increasingly essential going forward.
## The Essential Role of Data Engineers in Enterprise AI
Within any modern data team, data engineers are responsible for building and maintaining the underlying infrastructure of the data stack. Their pipelines and workflows enable applications, analysts, business consumers and data scientists to access and use the data they need to get their work done.
As organizations begin to layer generative AI into their products, data engineers will be integral to expanding existing infrastructure and governance to encompass the latest models and technologies. Let’s explore three specific ways
[data engineers will contribute to AI success](https://thenewstack.io/data-engineer-critical-role-for-data-success/).
### 1. Facilitate RAG to Improve LLM Outputs
At this moment, most organizations achieving success with GenAI are using
[retrieval-augmented generation (RAG)](https://www.montecarlodata.com/blog-the-moat-for-enterprise-ai-is-rag-fine-tuning/). This involves incorporating a knowledge source or dataset into their generative process — giving an LLM access to a dynamic database while responding to prompts. For example, with RAG fully implemented, a consumer-facing chatbot would be able to pull specific customer data to reference during a support interaction.
For most use cases, RAG is a better fit than
[fine-tuning](https://www.anyscale.com/blog/fine-tuning-is-for-form-not-facts)—retraining an existing LLM on a smaller, specific dataset. Fine-tuning requires considerable computational resources and large volumes of data, and typically involves a higher risk of overfitting.
Effectively implementing RAG requires quality data pipelines that feed
[company data](https://thenewstack.io/the-next-wave-of-big-data-companies-in-the-age-of-chatgpt/) to AI models. Data engineers are responsible for ensuring:
- The database is accurate and relevant, with regular updates and quality checks
- Retrieval processes are optimized and prompts are addressed with correct and contextually appropriate data
- Data inputs are continuously monitored and refined through
[data observability](https://thenewstack.io/what-is-data-observability-and-why-does-it-matter/)
The preference for RAG may change as the technology evolves, but for now, it’s generally considered the most practical path forward for enterprise AI. It also helps reduce
[hallucinations](https://www.pinecone.io/learn/options-for-solving-hallucinations-in-generative-ai/) and inaccuracies, while improving transparency for data teams.
### 2. Maintain Security and Privacy
Data engineers already play a key role in data governance, ensuring that databases have the proper built-in roles and security controls to ensure privacy and compliance. When RAG is implemented, those controls need to be extended and applied consistently throughout the pipelines.
For instance, a company’s LLM shouldn’t be using any customer data for its own training, and a customer-facing chatbot must confirm a user’s identity and permissions before sharing sensitive data. Data engineers play a pivotal role in maintaining compliance with regulations and best practices.
### 3. Reliable, High-Quality Data
Ultimately, the success of GenAI depends on data quality. Without accurate, reliable data consistently made available to LLMs, even the most advanced models won’t produce useful outputs.
Over the last five years, leading data engineers have adopted observability tooling — including automated monitoring and alerting, similar to DevOps observability software — to help improve data quality. Observability helps data teams monitor and proactively respond to incidents like failed Airflow jobs, broken APIs and misformatted third-party data that put data health at risk. And with end-to-end data lineage, teams gain visibility into upstream and downstream dependencies.
Data engineers can provide transparency when observability tooling is applied across the modern AI stack, including vector databases. Lineage allows engineers to trace the source of the data as it’s converted to embeddings, then use that data to generate rich text that the LLM puts in front of the user. This visibility helps data teams understand how LLMs operate, improve their outputs, and quickly troubleshoot incidents.
As Vishnu Ram, VP of engineering at CreditKarma,
[told us](https://www.montecarlodata.com/blog-credit-karmas-journey-to-reliable-generative-ai-models-with-data-observability/): “We need to be able to observe the data. We need to understand what data we’re putting into the LLM, and if the LLM is coming up with its own thing, we need to know that — and then know how to deal with that situation. If you don’t have observability of what goes into the LLM and what comes out, you’re screwed.”
## Data Engineers Are the Future of AI-Driven Organizations
AI technologies are evolving at a head-spinning pace. But even as fine-tuning models and more advanced custom training become feasible for enterprises, the need to ensure data quality, security and privacy will not change.
As organizations invest in generative AI applications, the quality and availability of their data will be more valuable than ever before. That means the workflows and data engineering processes may change, but their importance within organizations has only just begun.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)