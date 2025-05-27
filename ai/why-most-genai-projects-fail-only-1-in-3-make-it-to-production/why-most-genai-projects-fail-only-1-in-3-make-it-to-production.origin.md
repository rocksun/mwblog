# Why Most GenAI Projects Fail: Only 1 in 3 Make It to Production
![Featued image for: Why Most GenAI Projects Fail: Only 1 in 3 Make It to Production](https://cdn.thenewstack.io/media/2025/05/23631ba9-seo-galaxy-yushnkbhf3q-unsplash-1024x683.jpg)
[SEO Galaxy](https://unsplash.com/@seogalaxy?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-woman-covering-her-face-while-looking-at-a-laptop-yusHnkBhF3Q?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
AI is experiencing the fastest enterprise adoption curve in tech history — usage is surging, budgets are multiplying, and use cases are expanding from generative AI (GenAI) to fully autonomous, agentic systems. But there’s a catch: most AI apps never make it to production.

The main problem isn’t model performance, infrastructure, or even cost—it’s data. Specifically, [data security and privacy](https://thenewstack.io/building-privacy-aware-ai-software-with-vector-databases/) are repeatedly mentioned as blockers. Without robust, dynamic access controls, GenAI systems [risk leaking sensitive data and introducing security](https://thenewstack.io/flaw-in-r-creates-supply-chain-security-risks/) vulnerabilities that could cause reputational damage, competitive losses, and legal exposure.

This article explores GenAI’s rise, why so many initiatives stall, and how [authorization as a service](https://www.osohq.com/cloud/authorization-service) can help engineering teams ship AI applications faster without compromising on safety or control.

## The Fastest Ramp Ever? GenAI’s speed, Shift, and Spend by the Numbers
Stanford University’s [2025 AI Index](https://hai.stanford.edu/ai-index/2025-ai-index-report) shows adoption accelerating with 78% of organizations using AI in 2024, up from 55% the year before. Nutanix’s [2025 Enterprise Cloud Index](https://www.nutanix.com/enterprise-cloud-index) found that over 80% of organizations have already implemented a GenAI strategy.

Adoption is being matched by investment. Menlo Ventures reports [enterprise GenAI spending](https://menlovc.com/2024-the-state-of-generative-ai-in-the-enterprise/) grew 6x in 2024 over the previous 12 months. Spending as a proportion of total IT budgets is only increasing:

- Boston Consulting Group
[forecast GenAI budgets](https://www.bcg.com/publications/2024/it-spending-pulse-as-genai-investment-grows-other-it-projects-get-squeezed)growing 60% over the next three years. [Gartner predicts](https://www.gartner.com/en/articles/2025-trends-for-tech-ceos)$3 trillion in enterprise spending on AI between 2023 and 2027. Its research also predicts that*“within a few years, buyer**organizations will spend more money on software with GenAI features than they will on software without them.*”
Putting these forecasts into context, very few enterprises had even heard of GenAI before OpenAI’s release of ChatGPT as a research preview in November 2022, let alone allocated budget to it.

## What Happens When AI Stops Asking and Starts Acting?
Today, the top three GenAI use cases center on content creation, customer or employee support automation, and software engineering. However, as __CIO.com__[ states](https://www.cio.com/article/3478721/top-7-generative-ai-use-cases-for-business.html), these are only the “tip of the iceberg.”

Building on GenAI, we are now seeing significant focus on agentic AI—autonomous LLM-based systems capable of making decisions and performing tasks without constant human supervision. The concept of agentic AI extends beyond traditional regimented automation by enabling systems to understand context, adapt to new information and external events, often (but now always) collaborating with a “human in the loop” to solve complex challenges. Consider automating business workflows such as supply chain management, legal discovery, accounting returns, engineering and design projects, research & strategic planning, and many others.

As models grow in sophistication and domain-specific LLMs become more accessible, activities that were once the exclusive preserve of human cognition and problem-solving are being augmented (and disrupted?) by the machines. Consider Stanford University’s research cited earlier. It found:

- Model performance benchmarked against human performance improved by up to 67% in just 12 months.
- Meanwhile, costs are plummeting, with inference costs (often the most expensive part of AI) falling a massive 280x in just two years. Today, Moore’s Law seems “quaint.”
The obvious conclusion we can draw from all of this is that as LLMs become more capable and costs fall, so the abundance and breadth of use cases for AI will only expand.

## Why Do GenAI Projects Fail To Make Production?
Adoption is growing, use cases are expanding, and money flows.

So why, according to a [recent survey for Informatica](https://www.itpro.com/technology/artificial-intelligence/only-a-handful-of-generative-ai-projects-make-it-into-production-heres-why), are only 38% of AI projects making it into production? A [survey from Dataiku](https://www.bigdatawire.com/2024/08/30/genai-adoption-by-the-numbers-2/) paints an even gloomier picture with only 20% of GenAI applications developed by enterprises currently in production. [Gartner predicts](https://www.bigdatawire.com/this-just-in/gartner-predicts-30-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025/) 30% of GenAI projects will be abandoned after proof of concept by the end of 2025.

Why is this? Across multiple surveys, we see similar conclusions — it’s all about the data:

- The Nutanix survey found that data privacy and security was the most important data-related aspect of GenAI implementation. 95% of respondents said privacy is a priority, and the same percentage admitted their organization could do more to secure GenAI models and applications.
- A
[YouGov survey for BigID](https://www.agilitypr.com/pr-news/pr-tech-ai/the-top-generative-ai-concern-for-the-remainder-of-2024-is-data-security-risk-say-decision-makers-what-companies-can-do-to-protect-data/)found that more than two-thirds of organizations rank data security risks as their top AI concern with 50% finding it the top challenge during implementation. - 77% of survey respondents to the Dataiku study identify their biggest AI worries are a lack of governance and usage control.
In the early stage of any new tech adoption wave, concerns around security and privacy often prove to be overblown, or are mitigated by new controls and design patterns. This isn’t the case with Gen AI. Quite the reverse in fact. Concerns over data privacy are growing as more projects near production readiness. A [report from Deloitte](https://www.techrepublic.com/article/genai-data-privacy-concern-deloitte/) found that in 2023 only 22% of tech professionals ranked it among their top three concerns. In 2024 that figure had risen more than threefold to 72%.

## When AI Knows Too Much and The Hidden Threat Inside Your AI Stack
Let’s make it clear that concerns [around data security](https://thenewstack.io/how-to-put-guardrails-around-containerized-llms-on-kubernetes/) and privacy in AI aren’t hypothetical. In early 2023, Samsung banned ChatGPT after an engineer inadvertently [leaked sensitive internal source code](https://thenewstack.io/twitters-source-code-leak-adds-to-elon-musks-social-media-mess/) by submitting it in a prompt. This wasn’t an isolated case — BigID reports that nearly 50% of organizations have already experienced adverse business outcomes from AI usage, including data breaches.

LLMs introduce real risk when data access is not controlled correctly. [Models trained and tuned on internal data](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/) or used in Retrieval Augmented Generation (RAG) workflows can expose personally identifiable information (PII), intellectual property (IP), or confidential insights in their outputs. This is especially concerning in customer-facing apps or internal tools where the model has access to sensitive or regulated data. AI chatbots might unintentionally surface internal records, contracts, pricing, or support history. Enterprise search tools could reveal financials or strategic plans to unauthorized users.

The risks are amplified in software engineering. AI coding assistants may leak proprietary code or introduce vulnerabilities — especially if they retain context across sessions or lack proper sandboxing. In some cases, adversarial prompts can deliberately extract sensitive content, turning helpful tools into potential breach vectors.

The consequences are severe: regulatory penalties, competitive risk, reputational damage, and legal exposure.

Only by enforcing robust [LLM access controls](https://www.osohq.com/llm-access-control), secure model architectures, and strict data governance policies will enterprises be successful in scaling the percentage of AI apps that make it to production.

## Fix the Permissions Problem and Unlock the AI Potential
Authorization is foundational to any software application — it governs who can access which data, perform specific actions, and interact with different parts of the system, making it essential for both functionality and security.

The stakes are even higher in GenAI and agentic AI systems. These applications often operate autonomously, interact with sensitive data, and trigger downstream actions. That makes fine-grained, dynamic authorization critical to prevent unintended behavior, data leakage, or malicious misuse.

- “I don’t want to be the one causing a data leak.”
- “I thought I was implementing RAG, not developing an authorization system.”
- “If I can’t connect my LLM to my customer data, no one will use my chatbot.”
- “My security team is stopping me from putting my agentic AI app into production.”
Here at [Oso](https://www.osohq.com/), we’ve heard the concerns above echoed by many engineering teams. As they wrestle with how to build LLM access controls, one challenge consistently stands out: ensuring that generative and agentic AI apps only share information with users authorized to see it.

As a practical guide to help everyone develop AI apps, we have put together [a tutorial that steps through building an authorized LLM chatbot with Oso Cloud](https://www.osohq.com/post/building-an-authorized-rag-chatbot-with-oso-cloud). It guides engineers through integrating fine-grained authorization into a chatbot that uses internal documents as context, ensuring users only access information they can see.

The tutorial covers setting up a vector database, generating embeddings and responses with OpenAI, and enforcing access controls with Oso Cloud. Accompanied by a full demo application with working code, engineers can clone the repository and start building their own secure, context-aware chatbots immediately.

![](https://cdn.thenewstack.io/media/2025/05/e7a68071-image1.png)
Figure 1: Data flow within a typical RAG architecture in an agentic AI app

## From Authorization That Slows to Authorization That Flows
Productboard is a customer-centric [product management platform](https://thenewstack.io/a-platform-team-product-manager-determines-devops-success/) that enables organizations to bring the right products to market faster. As it expanded from serving small and medium-sized businesses to engaging with large enterprises, Productboard encountered authorization challenges.

The company turned to Oso to help it meet new enterprise demands such as more granular and customizable access controls, field-level permissions, and managing access across complex, nested data structures. Additionally, as the company shifted to a microservices architecture, Oso simplified how permissions were consistently enforced across distributed systems. Productboard partnered with Oso for expert support through migration, policy design, and AI integration

As Productboard introduced AI-powered capabilities through its new [Productboard Pulse](https://www.productboard.com/product/voice-of-customer/) platform, having a robust authorization foundation proved critical.

Productboard Pulse aggregates customer feedback from tools like support, CRM, and analytics into a unified view, allowing teams to surface insights via natural language queries. It uses a retrieval-augmented generation (RAG) architecture to enrich LLM prompts with contextual data, but only data each user is authorized to see. Oso plays a central role in this workflow, enforcing fine-grained, dynamic access controls that ensure sensitive feedback is only accessible to the right users. By leveraging Oso, Productboard accelerated development, avoided costly reimplementation of permissions logic, and ensured secure, scalable access across distributed data sources, enabling them to deliver AI features quickly and confidently.

As one of the company’s lead staff engineers on the project stated:

*“Oso made building Productboard Pulse much faster, since every API can just call Oso to figure out what’s allowed, no matter where the data resides. By building on top of a proven authorization foundation, we’ve avoided the biggest hurdles derailing AI efforts in many companies.”*
You can read the full [Productboard and Oso case study](https://www.osohq.com/customers/productboard) to learn more.

## Where Do We Go From Here?
The AI wave is here and it’s moving fast. But turning that momentum into real business value depends on more than models and GPUs. Without fine-grained, flexible authorization, AI projects stall at the proof-of-concept phase or worse, expose your organization to data leaks, security risks, and compliance failures. Remember to consider authorization-as-a-service solutions to help remove access controls as a blocker to shipping your AI apps.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)