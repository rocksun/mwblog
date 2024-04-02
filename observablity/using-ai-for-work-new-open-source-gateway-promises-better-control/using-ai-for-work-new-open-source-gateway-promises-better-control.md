
<!--
title: 利用人工智能工作：新的开源网关承诺更好的控制
cover: https://cdn.thenewstack.io/media/2024/03/976ee8ec-india-gate-3526277_1920.jpg
-->

开发者在尝试使用 AI 时面临组织挑战，包括安全和成本问题。Kong 的新 AI 网关承诺提供帮助。

> 译自 [Using AI for Work: New Open Source Gateway Promises Better Control](https://thenewstack.io/using-ai-for-work-new-open-source-gateway-promises-better-control/)，作者 Loraine Lawson。

开发人员在为生成式AI应用程序实现大型语言模型(LLM)时面临着一些挑战。

首先，组织担心用户与LLM交互时会泄露数据，Kong开源API管理平台的联合创始人和CTO [Marco Palladino](https://www.linkedin.com/in/marcopalladino/)表示。其次，他们担心[AI产生幻觉](https://thenewstack.io/reduce-ai-hallucinations-with-retrieval-augmented-generation/)。第三，他们担心调用基于云的LLM API的成本。

"他们理解AI的力量，希望使用AI，但也非常关注如何确保组织以负责任的方式使用AI，"Palladino说。"一些组织正在测试AI，但他们不太确定如何将其投入生产。我们为他们提供的能力是确保对其AI流量进行管理、合规和滥用防护。"

Kong创建了一个AI网关，集成到其[API管理中间件](https://thenewstack.io/what-is-api-management/)中，以帮助组织解决这些挑战。它作为[Kong网关3.6的一个开源插件提供](https://docs.konghq.com/gateway/latest/get-started/ai-gateway/)。

## AI作为API用例

从根本上讲，AI是一种API用例，Palladino断言，就像互联网现在主要由API驱动，微服务由API驱动一样，AI也将由API消耗驱动。

我们有三种方式可以使用AI: 我们可以消费AI、[训练AI](https://thenewstack.io/meeting-the-operational-challenges-of-training-llms/)或让AI消费API与世界互动。无论我们消费它、训练它，还是让AI与其他服务、数据互动，或全部三种情况，API都在驱动这一切，"他说。"AI只不过是最新的数字化用例，正在推动全球API消耗。"  

这确实似乎是发展的方向: 通过API消费现有的预训练生成式转换器(GPT)如OpenAI的ChatGPT 4，比构建自己的LLM更容易。此外，开发人员不太可能只连接一个LLM，因为不同的LLM擅长解决不同的用例，他补充道。造成这种情况的一个原因是，减少幻觉的一种方式是使用第二个LLM来核实第一个LLM的答案，然后再提供。

"组织根据LLM训练所用的数据集来消费LLM，并消费更适合特定工作的AI技术，"他说。"永远不会有一种技术适合所有用例。将需要多个LLM。"

## 控制企业中的AI

但是调用所有这些云模型AI API也会很昂贵。Kong看到的趋势是，大型企业组织正在启动自托管LLM，成本更低，延迟也更小。当自托管LLM不够用或宕机时，云LLM作为备份，Palladino说。AI网关支持这种场景，为开发人员提供"一个API来统治所有API"。 

"我们一直在与一些特殊的设计合作伙伴和客户合作，创建了AI网关，使开发人员能够更高效地工作，为他们提供一个API来消费任意多个LLM，"Palladino说。"他们不必为一个LLM构建应用程序集成，然后为另一个LLM构建，再为另一个LLM构建。他们只需构建一次，就可以非常轻松地[选择要支持哪些LLM](https://thenewstack.io/pivot-ai-devs-move-to-switch-llms-reduce-openai-dependency/)，而在我们的产品中，目前支持6种LLM。"

到目前为止，AI网关已经与以下[云LLM提供商](https://thenewstack.io/generative-ai-cloud-services-aws-azure-or-google-cloud/)的API集成:

* [OpenAI](https://openai.com/)
* [Azure AI](https://azure.microsoft.com/en-us/free/ai)
* [Anthropic](https://www.anthropic.com/)
* [Cohere](https://thenewstack.io/ai21-labs-releases-jurassic-2-its-new-large-language-model/)
* [Mistral](https://mistral.ai/)
* [Meta’s Llama](https://llama.meta.com/)

Kong计划增加对[Hugging Face开源LLM](https://thenewstack.io/machine-learning-is-as-easy-as-an-api-says-hugging-face/)和[AWS Bedrock](https://thenewstack.io/generative-ai-cloud-services-aws-azure-or-google-cloud/)的支持。

“您只需构建一次，就可以在支持的其他 LLM 之间切换。完成此操作后，我们在网关之上提供了一个集中管理 AI 凭据、AI 分析、AI 安全的方法，这样，如果我们要轮换令牌，如果我们要捕获 AI [可观测性日志](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/)，我们就可以在网关层上完成此操作。”他说。“我们不必更改应用程序或在应用程序中构建内容;网关会为我们完成此操作。”

网关还为组织提供了一种围绕 AI 提供治理和合规性的方式，因为它包含了一个防火墙，该防火墙只允许特定类型的提示，并允许组织针对提示建立参数。他表示，例如，它可以执行脏话检查或确保没有执行任何非法操作。他补充说，网关还包含一个编排引擎，该引擎管理自托管 LLM 和云 LLM 之间的流量，以帮助提高性能并降低使用 AI 的成本。

他表示，“我们为他们提供的能力是确保治理、合规性和防止滥用其 AI 流量，因此他们确信他们可以在任何 AI 消费开发人员之上实施其规则”。“我们为他们提供基础设施，以便能够使用 API 上线并投入生产。”