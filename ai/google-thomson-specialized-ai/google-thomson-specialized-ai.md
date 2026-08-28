<!--
title: 谷歌的新型法律AI揭示了企业技术栈层面的更大竞争格局
cover: https://cdn.thenewstack.io/media/2026/08/90b62094-curated-lifestyle-jkda-yy-sm4-unsplash-scaled.jpg
summary: 本文探讨了谷歌推出的法律专用AI解决方案及Thomson Reuters的同类产品，指出企业级AI竞争已从单纯的模型能力转向垂直领域的全栈集成与定制化方案，核心差异在于数据积累、模型训练及生态体系的深度整合。
-->

本文探讨了谷歌推出的法律专用AI解决方案及Thomson Reuters的同类产品，指出企业级AI竞争已从单纯的模型能力转向垂直领域的全栈集成与定制化方案，核心差异在于数据积累、模型训练及生态体系的深度整合。

> 译自：[Google’s new legal AI exposes a bigger battle over the enterprise stack](https://thenewstack.io/google-thomson-specialized-ai/)
> 
> 作者：Meredith Shubel

**Google Cloud 本周推出了 Gemini Enterprise for Legal**，这是一个专门构建的代理式AI解决方案，旨在实现法律工作流程的自动化，包括合同审查、法规监控、文档起草和数据发现。这标志着企业级AI竞争的下一个阶段将取决于谁能最好地专业化技术栈，而不仅仅是谁能构建出最强大的基础模型。

此次发布与 [Gemini Enterprise for Financial Services](https://www.googlecloudpresscorner.com/2026-08-25-Google-Cloud-Launches-Gemini-Enterprise-for-Financial-Services) 同步进行，这是另一个面向金融专业人士的代理式AI解决方案。这两者是谷歌所描述的“一系列构建在安全、完全受治理的 Gemini Enterprise 平台之上的专业化、封装式行业解决方案”中的首批产品。

[Gemini Enterprise for Legal](https://www.googlecloudpresscorner.com/2026-08-25-Google-Cloud-Launches-Gemini-Enterprise-for-Legal) 的发布是在 [Thomson Reuters’ Thomson](https://thenewstack.io/thomson-reuters-ai-model/) 首次亮相约 24 小时后，后者是该公司为法律、税务和合规工作开发的专用AI模型，耗资 4000 万美元。

尽管 Gemini Enterprise for Legal 和 Thomson 在表面上看起来相似——两者都旨在让AI在法律工作流中发挥更大作用——但它们在结构上截然不同。谷歌的新产品是一个围绕其现有 Gemini 模型构建的代理式系统。而 Thomson 则是一个专有模型，该公司使用其自有的专业内容和主题专家的输入对其进行了进一步训练。

尽管如此，在一些重要方面，这些发布是同一硬币的两面。两者都表明，各公司正在推动AI向专业领域转型，但这种专业化可以来自技术栈的不同层级。

## 专业化AI不一定意味着要有一个专业化的模型

谷歌和 Thomson Reuters 都在采取行动构建更专业化的AI，但他们是从不同的角度切入的。

Thomson Reuters 通过获取现有的开源基础模型，并投入数百万美元利用其自身收藏的数十年内容（包括 Westlaw、Practical Law、Checkpoint 和 Reuters）以及专家评估来训练模型，从而引起了轰动。最终产出的 Thomson 模型甚至在一些基准评估中击败了 Gemini 3.1 Pro、Claude Opus 4.8 和 GPT-5.5。

与此同时，谷歌正围绕模型通过代理、集成、工具和治理构建大部分法律专业化功能，尽管该公司表示其解决方案可能也包括模型优化。

> 两者都表明，各公司正在推动AI向专业领域转型，但这种专业化可以来自技术栈的不同层级。

Gemini Enterprise for Legal 构建在谷歌自己的AI技术栈之上，该技术栈涵盖了全球基础设施、定制芯片、基础模型以及一个AI就绪的数据平台。虽然 Thomson Reuters 似乎在强调拥有专有数据并利用其进一步训练模型可以带来优势，但谷歌的方法表明，通过在基础模型层之上工作，同样可以实现专业化AI。

该解决方案围绕四个核心组件：1) 为引导AI代理完成法律任务而专门构建的专业技能；2) 用于连接 DocuSign 等法律行业平台的安全模型上下文协议（MCP）集成；3) 访问由第三方代理、法律技术提供商和咨询合作伙伴（如 Accenture 和 Deloitte）组成的专业网络；4) 用于风险管理、审计日志记录和治理的控制平面。

通过这些组件的协同工作，谷歌表示 Gemini Enterprise for Legal 可以自动化并加速一系列法律运营，例如自动化数据发现和数据主体访问请求（DSAR）响应，并自主跟踪立法更新、法院案卷和监管机构以更新政策草案。它还可以加速合同审查和谈判、起草 NDA 文档、准备法院文件、编辑法律文档以及构建和更新合同手册。

## 拥有模型并不意味着要全力投入其中

Thomson Reuters 在发布 Thomson 时的一个突出观点是，该公司独立训练的模型在多项专业和通用评估中表现优于领先模型。

但这并不意味着该公司完全放弃了前沿模型。相反，它选择了一种根据哪种模型最适合手头任务而进行的“挑选”策略。

看看 CoCounsel Legal 就知道了，这是 Thomson Reuters 的AI助手，构建在 Anthropic 的 Claude Agent SDK 之上，旨在帮助法律专业人士进行研究、分析和起草工作。作为其首次部署，Thomson 将在 Tabular Analysis 产品中工作，这是一个用于分析大量文档的文档审查工具。当 Thomson 比其他领先模型具有真正优势时，CoCounsel Legal 将让它发挥主导作用；但当其他模型更适合任务时，AI助手会将工作引导至相应的模型。

## 模型选择现在只是拼图的一部分

关于如何将AI适应特定领域任务的大部分讨论看起来都像是一个模型问题：获取现有的最佳通用模型，并为其提供正确的数据和上下文。但这两次发布表明，情况正在变得更加复杂。

> 展望未来，竞争优势可能越来越属于那些能够带来别人无法轻易获取的独特价值的人。

是的，模型仍然是开发专业化AI的基础部分，但这并不是差异化的唯一途径。展望未来，竞争优势可能越来越属于那些能够带来别人无法轻易获取的独特价值的人。

对于谷歌来说，那是其集成的AI和云技术栈，Gemini Enterprise for Legal 通过专业技能、MCP集成、治理和工具对其进行了扩展。对于 Thomson Reuters 而言，这种优势看起来不同：这是一个构建在数十年内容和专家知识之上的专有、专业化模型，且运行在一个多模型系统内部。

这两种方法都没有抹杀底层模型的重要性。但两者都表明，仅有一个强大的模型不足以引领专业化AI。对于开发者来说，这引发了一个问题：技术栈的哪一部分值得拥有？