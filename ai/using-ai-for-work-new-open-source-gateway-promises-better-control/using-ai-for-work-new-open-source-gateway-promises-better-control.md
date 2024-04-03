
<!--
title: 使用AI工作：新的开源网关承诺更好的控制
cover: https://cdn.thenewstack.io/media/2024/03/976ee8ec-india-gate-3526277_1920.jpg
-->

开发者在尝试使用 AI 时面临组织挑战，包括安全和成本问题。Kong 的新 AI 网关承诺提供帮助。

> 译自 [Using AI for Work: New Open Source Gateway Promises Better Control](https://thenewstack.io/using-ai-for-work-new-open-source-gateway-promises-better-control/)，作者 Loraine Lawson。

Developers face several challenges when implementing large language models (LLMs) for generative AI applications.

First, organizations worry about data leaking into the public when users interact with LLMs, said [Marco Palladino](https://www.linkedin.com/in/marcopalladino/), co-founder and CTO of open source API management platform Kong. Second, they worry about [AI hallucinations](https://thenewstack.io/reduce-ai-hallucinations-with-retrieval-augmented-generation/). Third, they worry about the cost of making API calls to cloud-based LLMs, he added.

“They understand the power of AI, they want to use AI, but they’re also very concerned about making sure that the organization is using AI responsibly,” Palladino said. “Some organizations are implementing AI from a testing perspective, but they don’t really know how to put it into production. The capability that we’re giving them is to make sure that there’s governance, compliance and abuse prevention for their AI traffic.”

Kong created an AI Gateway that integrates into its [API management middleware](https://thenewstack.io/what-is-api-management/) to help organizations address these challenges. It’s available as an open source plugin for [Kong Gateway 3.6](https://docs.konghq.com/gateway/latest/get-started/ai-gateway/).

## AI as an API Use Case

Fundamentally, AI is an API use case, just as the internet today is largely driven by APIs, and as microservices are driven by APIs, AI will be driven by API consumption, Palladino asserted.

“There are three things we can do with AI: We can consume AI, [we can train AI](https://thenewstack.io/meeting-the-operational-challenges-of-training-llms/), or we can use APIs to have AI interact with the world. Whether we’re consuming it, training it, or having AI interact with other services, other data, or all three, APIs are driving all of that,” he said. “AI just happens to be the latest digital use case that is driving API consumption in the world.”

That seems to be how it’s playing out: It’s easier to leverage existing generative pretrained transformers (GPTs) like OpenAI’s ChatGPT 4 via APIs than it is to build your own. Plus, developers are unlikely to connect to just one LLM, given that LLMs can address different use cases, he added. One reason for this, The New Stack has been told, is that one way to reduce hallucinations is to use a second LLM to fact-check the first LLM’s answers before serving them.

“Organizations are consuming LLMs based on the datasets that they’ve been trained on, and they’re consuming AI technologies that are better suited for the job,” he said. “It’s never going to be one technology to rule them all. It’s going to be multiple LLMs.”

## Controlling AI for Enterprise Use

However, calling all of these cloud model AI APIs can get expensive. The trend Kong is seeing is that enterprise-scale organizations are spinning up self-hosted LLMs, which are cheaper and faster from a latency perspective, with cloud LLMs as a backup for when the self-hosted LLMs aren’t sufficient or go down, Palladino said. The AI Gateway supports this scenario, giving developers “one API to rule them all,” he added.

“We’ve been working with a select design partners and customers of ours to create an AI Gateway that makes developers more productive by giving [them] one API that they can use to consume any number of LLMs,” Palladino said. “They don’t have to build an integration to one LLM and another LLM and another LLM; they can build it once, and then they can very easily [choose which LLMs they want to support](https://thenewstack.io/pivot-ai-devs-move-to-switch-llms-reduce-openai-dependency/), and today we support six LLMs in our product.”

So far, the AI Gateway has API integrations with the following [cloud LLM providers](https://thenewstack.io/generative-ai-cloud-services-aws-azure-or-google-cloud/):

* OpenAI
* Google AI Platform
* Azure OpenAI Service
* Cohere
* AI21 Labs
* Gemini

Kong plans to add support for [Hugging Face’s open source LLM](https://thenewstack.io/machine-learning-is-as-easy-as-an-api-says-hugging-face/) and [AWS Bedrock](https://thenewstack.io/generative-ai-cloud-services-aws-azure-or-google-cloud/).

“You build it once, you can switch between any of the other LLMs that we support, and once you do that, we provide a way to centrally manage your AI credentials, AI analytics, AI security on top of the gateway, so that if we want to rotate our tokens, if we want to capture AI
[可观测性日志](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/)，我们可以在网关层上执行此操作，”他说。“我们不必更改我们的应用程序或在我们的应用程序中构建内容；网关会为我们执行此操作。”

网关还为组织提供了一种围绕 AI 提供治理和合规性的方法，因为它包含一个防火墙，该防火墙只允许特定类型的提示，并允许组织建立有关提示的参数。例如，它可以执行亵渎检查或确保没有执行任何非法操作，他说。网关还包含一个编排引擎，该引擎管理自托管 LLM 和云 LLM 之间的流量，以帮助提高性能并降低使用 AI 的成本，他补充说。

“我们为他们提供的能力是确保治理和合规性以及防止滥用其 AI 流量，因此他们确信他们可以对任何 AI 消费开发者实施其规则，”他说。“我们为他们提供基础设施，以便能够使用 API 上线并投入生产。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。