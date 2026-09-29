<!--
title: Meta挖来MongoDB CEO发力企业级AI——但Llama缺席了
cover: https://cdn.thenewstack.io/media/2024/06/4f526464-llama-7690169_1920.jpg
summary: Meta宣布成立Meta Enterprise Platform发力企业级AI，并挖来MongoDB CEO CJ Desai执掌该业务。然而，发布中却未提及开源模型Llama的去向，引发业界对Meta未来开源路线的猜测。
-->

Meta宣布成立Meta Enterprise Platform发力企业级AI，并挖来MongoDB CEO CJ Desai执掌该业务。然而，发布中却未提及开源模型Llama的去向，引发业界对Meta未来开源路线的猜测。

> 译自：[Meta hired MongoDB's CEO to build its enterprise AI business — but Llama is missing](https://thenewstack.io/meta-enterprise-platform-desai/)
> 
> 作者：Amanda Caswell

**Meta于周一宣布**将围绕其AI模型和代理构建全新的企业级业务，并已聘请 MongoDB CEO CJ Desai 来负责该业务。这项名为 Meta Enterprise Platform 的新举措，将把 Meta 为其消费者应用和广告商构建的技术提供给希望将其部署在自身业务内部的企业和开发人员。

在 X（原 Twitter）的一篇帖子中，Mark Zuckerberg 将其描述为 Meta 业务的“下一个主要支柱”，将企业级AI与公司的广告和消费级应用并列为三大核心。

[Desai](https://www.linkedin.com/in/chirantan-cj-desai-aa346/) 将加入 Meta 担任企业平台首席官（Chief Enterprise Platform Officer），并直接向 Zuckerberg 汇报。在 2025 年 11 月刚上任 CEO 不到一年后，他[卸任了 MongoDB 的职务，立即生效](https://www.mongodb.com/company/newsroom/press-releases/mongodb-announces-ceo-transition)，该公司已任命前 CEO [Dev Ittycheria](https://www.linkedin.com/in/dittycheria/) 为临时总裁兼 CEO。

对于开发者而言，在[此次发布](https://about.fb.com/news/2026/09/launching-meta-enterprise-platform/)中更迫切的问题是他们可以用它构建什么。Zuckerberg 表示，Meta 将把其“全套技术栈”带给企业和开发者，首批推出的是 Muse 代理、Meta Business Agent、Muse API 和 Muse Code。

Meta 本月早些时候推出了 Muse，作为面向消费者的个人AI代理；而 6 月份推出的 Meta Business Agent 则负责处理 Meta 各平台上企业与客户的互动。Muse API 和 Muse Code 是最直接面向开发者的产品，它们让 Meta 与 OpenAI、Anthropic 和 Google 在构建代理和编码工作流的工程团队方面展开更激烈的竞争。Muse 也在拓展 Meta 自身的应用之外，[Shopify 在其商店中整合了 Muse，而亚马逊则屏蔽了它](https://thenewstack.io/amazon-meta-muse-block/)。

## Muse API 的企业条款仍未明确

尽管开发者已经可以使用 Muse API 和 Muse Code，但 Meta 周一并未公布 Muse API 或 Muse Code 的企业定价、全面上市日期或服务条款：Muse Code 自 8 月以来一直处于测试阶段，而 Meta 从 7 月开始通过其 API 收取 Muse Spark 模型的费用，价格为每百万输入 Token 1.25 美元，每百万输出 Token 4.25 美元。

一旦这些条款出台，各团队就有充分的理由仔细审查它们，包括 Meta 如何处理模型更新，因为模型变更很容易扰乱正在运行的系统。

## Llama 现在处于什么位置

Llama 是 Meta 多年来一直向开发者推广的模型系列，作为希望在自己的基础设施上运行和微调模型的团队的开源权重选项，但在 Meta 对新企业技术栈的描述中却完全不见踪影。Meta 尚未说明 Llama 是否会成为 Enterprise Platform 的一部分。今年 7 月，Meta 首次通过 Muse Spark 开始直接向开发者对其自有模型收费，但它也发布了较小的 Muse Glimmer 模型的开源权重，并承诺提供 Muse Spark 的开源权重版本，因此现在判断这一转变对已经将 Llama 投入生产环境的团队意味着什么还为时过早。

## Desai 的数据层剧本

在 MongoDB，Desai 已经在思考如何将代理投入生产环境。今年 5 月，该公司在数据平台中[加入了持久化代理记忆、自动化嵌入和其他AI功能](https://www.mongodb.com/company/newsroom/press-releases/mongodb-makes-enterprise-ai-production-ready)，Desai 认为模型只是挑战的一部分，将代理投入生产很大程度上取决于其背后的数据层。现在 Meta 面临着类似的挑战。在企业内部工作的代理需要持久的上下文、访问不断变化的数据的权限，以及在员工已经使用的应用程序内部采取行动的方式。其他公司正在用不同的方式解决同一问题，从 Perplexity（其[代理帮助构建了一个它们不允许运行的数据库](https://thenewstack.io/perplexity-cobbledb-ai-database/)），到 Microsoft（其[赋予了 Copilot 代理自己的电子邮件、日历和组织架构图中的位置](https://thenewstack.io/copilot-agents-identity-runtime/)）。

Desai 过去的职位将其背景延伸到了基础设施和工作流软件领域。他曾领导 Cloudflare 的产品和工程，该公司此后一直致力于成为[AI网络的经济层](https://thenewstack.io/cloudflare-ai-web-economics/)，他在 ServiceNow 度过了近八年时间，最终成为总裁兼 COO。

在[随公告发布的声明](https://about.fb.com/news/2026/09/launching-meta-enterprise-platform)中，Desai 表示 Meta Enterprise Platform 将专注于将 Meta 的AI技术栈转化为企业可以在自身业务内部部署的产品和服务，并且安全和隐私“从一开始”就内置于 Meta 的企业产品中。Meta 已经[公布了其针对 Muse 的安全和保障方法](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)，但周一的公告并未涉及数据保留、客户数据训练、租户隔离、身份控制或合规认证，企业买家在授予 Meta 的代理访问内部数据和系统的权限之前，会希望得到这些答案。

Meta 已经与其想要触达的许多企业建立了关系。Zuckerberg 曾指出，使用 Meta 产品的数十亿人和其平台上的数亿家企业，其中许多是已经使用 Facebook、Instagram 和 WhatsApp 进行营销和客户服务的中小企业。Enterprise Platform 可以将这种关系进一步推进，将 Meta 的AI直接置于企业自身的运营之中。

但要赢得大型企业的开发者将更加困难，因为他们的工程团队在过去几年里一直围绕 OpenAI、Anthropic、Google 等公司的模型和平台进行构建。Meta 需要提供能给团队带来超越触达能力的产品，他们才会将另一个平台加入自己的技术栈或彻底迁移过来。

## 开发者只能部分评估的平台

目前，Meta Enterprise Platform 更多的是一种战略而非产品——尽管其中的某些部分已经落入开发者手中——这留下了一个巨大的未解之谜：Meta 的企业级AI未来是否仍包含 Llama，或者 Muse 是否标志着向更受控平台的转变，即开发者通过 Meta 本身访问其最新的代理技术，尽管 Meta 承诺为 Muse Spark 提供开源权重。