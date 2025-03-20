
<!--
title: Cloudflare for AI帮助企业安全地使用AI
cover: https://cdn.thenewstack.io/media/2025/03/36e838c5-aicloudfordevelopers.jpg
summary: Cloudflare 发布 Cloudflare for AI，解决企业 AI 安全难题！通过 Firewall for AI 发现 Shadow IT，Cloudflare AI Gateway 监控提示类型，利用 Llama Guard 检测有害提示，保障 LLM 安全。助力企业安全拥抱 AI，加速云原生创新！
-->

Cloudflare 发布 Cloudflare for AI，解决企业 AI 安全难题！通过 Firewall for AI 发现 Shadow IT，Cloudflare AI Gateway 监控提示类型，利用 Llama Guard 检测有害提示，保障 LLM 安全。助力企业安全拥抱 AI，加速云原生创新！

> 译自：[Cloudflare for AI Helps Businesses Safely Use AI](https://thenewstack.io/cloudflare-for-ai-helps-businesses-safely-use-ai/)
> 
> 作者：Frederic Lardinois

内容分发和安全服务 [Cloudflare](https://cloudflare.com) 今天宣布推出 Cloudflare for AI，这是一套新的安全工具，旨在解决企业在使用 AI 模型和服务时面临的一些最紧迫的安全问题。

这些工具包括监控员工如何使用这些工具，发现他们何时使用未经授权的服务，以及阻止信息泄露给这些模型。这项新服务还可以检测何时向模型提交不适当或有害的 [提示](https://thenewstack.io/beyond-prompt-engineering-governing-prompts-and-ai-models/)。

正如 Cloudflare 在今天的公告中所解释的那样，这里的想法是帮助企业对他们为员工和用户启用的 AI 工作负载更有信心。

![](https://cdn.thenewstack.io/media/2025/03/a4087a30-unnamed-2.png)

“在未来十年，一个组织的 AI 战略将决定其命运——创新者将蓬勃发展，而那些抵制者将消失。随着各组织竞相实施新模型并[尝试使用 AI 来推动](https://thenewstack.io/improving-developer-experience-drives-profitability/)创新，‘快速行动，打破常规’已成为他们的座右铭，” Matthew Prince，Cloudflare 的联合创始人兼 CEO 说道。“但是，在实验和安全之间通常缺少一个环节。Cloudflare for AI 允许客户以他们想要的任何方向快速行动，并提供必要的保障措施，以实现 AI 的快速部署和使用。它是当今唯一一套可以在不阻碍创新的前提下解决客户最紧迫问题的工具。”

整个套件由多个服务组成。例如，Firewall for AI 允许企业发现员工实际使用的 AI 应用程序。影子 IT 这个由来已久的问题依然存在。当员工吵着要使用这些新的 AI 工具时，安全团队通常无法了解他们在做什么。现在，他们将获得关于哪些工具正在使用的报告，并且可以在必要时阻止它们。

![](https://cdn.thenewstack.io/media/2025/03/f3442f74-unnamed.png)

同样，Cloudflare AI Gateway 是该公司于 2023 年推出的，它可以深入了解公司内部正在使用的模型以及提交的提示类型，这反过来意味着防火墙可以阻止可能暴露个人身份信息和其他数据泄露的提示到达模型。

目前市场上很少有工具专注于阻止有害提示。为了检测这些提示，Cloudflare 正在使用 Llama Guard，[Meta 用于保护 LLM](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/) 对话的工具。Cloudflare 表示，这将有助于使模型符合其预期用途。

当然，Cloudflare 并不是唯一看到这些工具市场的公司。例如，[Kong](https://konghq.com/products/kong-ai-gateway?utm_source=google&utm_medium=cpc&utm_campaign=ai&utm_term=kong%20ai%20gateway&utm_content=kong-ai-gateway_landing-page_search&gad_source=1&gbraid=0AAAAAD3UpvSnUSJsx_bwhPYxViTt0CMGC&gclid=Cj0KCQjws-S-BhD2ARIsALssG0byTYS6UyfExkqLrvfg3zA6vqhXA4EpU7ALoC67E3nAqRKbALsb0T8aAk7CEALw_wcB) 和 [IBM](https://www.ibm.com/products/api-connect/ai-gateway) 提供了以 API 为中心的解决方案，以及 [F5 ](https://www.f5.com/products/ai-gateway) 和 [Databricks](https://www.databricks.com/product/ai-gateway) 提供的解决方案。