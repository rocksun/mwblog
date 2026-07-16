<!--
title: 企业反击：守住数据，拒绝AI账单
cover: https://cdn.thenewstack.io/media/2026/07/5fb580c6-a-c-0biutmdyrc4-unsplash.jpg
summary: 随着AI应用深化，企业担忧闭源AI实验室通过数据训练模型并反向抢占自身市场。为此，企业正转向部署私有化、低成本的开源模型，以确保数据安全并打破技术依赖。
-->

随着AI应用深化，企业担忧闭源AI实验室通过数据训练模型并反向抢占自身市场。为此，企业正转向部署私有化、低成本的开源模型，以确保数据安全并打破技术依赖。

> 译自：[The enterprise strikes back: Keep your data, ditch the AI bill.](https://thenewstack.io/enterprise-data-ai-labs/)
> 
> 作者：Alex Wilhelm

随着AI成本危机开始从风口浪尖消退，一个相关的担忧正在抬头：保护企业数据免受AI实验室侵害的必要性。正如成本问题一样，关于数据的担忧早已不是什么新鲜事。

但随着AI行业的成熟，企业正变得忧心忡忡。当推理负载尚且适中时，AI使用成本问题并不重要；同样，当企业只是计划使用而非实际应用AI时，数据方面的担忧也可以被忽略。

科技界的几种声音正为这两个担忧提供同一个解决方案：在内部使用基于私有数据训练的低成本开源AI模型。

让我来为你梳理一下……

使用来自OpenAI、Anthropic或SpaceXAI等公司的闭源AI的企业，需要支付高额溢价才能获得市场上最强大的模型。除了支付令人咋舌的Token费用外，企业还在用自己的数据“买单”，将信息喂给AI实验室以创建新的、更智能的模型。然后，这些实验室再将这些模型高价卖回给同样的企业客户。

> 除了支付令人咋舌的Token费用外，企业还在用自己的数据“买单”，将信息喂给AI实验室以创建新的、更智能的模型。然后，这些实验室再将这些模型高价卖回给同样的企业客户。

除了制造依赖循环，为什么这种情况令人担忧？AI实验室正在[水平扩张](https://www.cautiousoptimism.news/the-ai-agents-are-coming-for-microsoft-office/)，构建诸如Claude Cowork、ChatGPT Work以及即将推出的Cursor (SpaceXAI)通用智能体等工具，试图打入其客户目前占据主导地位的软件领域。

> AI实验室正在水平扩张……试图打入其客户目前占据主导地位的软件领域。

微软尤其可能成为目标。该公司在[Microsoft 365](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/choosing-the-right-ai-model-in-microsoft-365-flexibility-control-and-confidence/4530762) (Office)中提供第三方模型，花费巨资向其客户提供由那些[现在试图抢夺其市场份额](https://www.cautiousoptimism.news/the-ai-agents-are-coming-for-microsoft-office/)的公司制造的AI模型。

对于微软来说，这是一个严峻的时刻。见鬼，如果你是Redmond，你可能已经开始[尝试使用开源权重的中国模型](https://www.axios.com/2026/06/16/microsoft-copilot-cowork-tokenmaxxing-cowork)，甚至开始使用自主研发的模型来处理推理负载。

大型AI实验室意识到了这种潜在的利益冲突，这就是为什么[OpenAI表示](https://developers.openai.com/api/docs/guides/your-data#default-usage-policies-by-endpoint)API使用“不会被用于训练或改进OpenAI模型”。[Anthropic](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)、[xAi](https://docs.x.ai/developers/faq/security)和[Google](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention)也表达了类似的立场，有些甚至还提供了零数据留存计划。

但这些政策并不能阻止它们的竞争对手发出“AI实验室正在窃取你们数据”的警报。

***本文摘自《Cautious Optimism》，这是一份专注于技术、商业和权力的*** ***略带乐观*** ***的出版物。*** ***阅读关于数据隐私的解决方案及其成本，请访问 [Cautious Optimism](https://www.cautiousoptimism.news/the-anthropic-fable-mess-explained?utm_source=The+New+Stack&utm_medium=referral&utm_campaign=Article+Excerpt)。***