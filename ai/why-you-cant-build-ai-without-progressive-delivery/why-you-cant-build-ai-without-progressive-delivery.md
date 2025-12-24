<!--
title: 没了渐进式交付，你的AI根本建不起来！
cover: https://cdn.thenewstack.io/media/2025/12/8fb8076a-for-thumbnail-13.png
summary: 渐进式交付对AI开发至关重要，因AI输出不确定。它提供防护栏，如特性标志和可观测性，以管理和衡量AI系统。书中强调DevOps应加入用户反馈，实现精准交付并衡量成功。
-->

渐进式交付对AI开发至关重要，因AI输出不确定。它提供防护栏，如特性标志和可观测性，以管理和衡量AI系统。书中强调DevOps应加入用户反馈，实现精准交付并衡量成功。

> 译自：[Why You Can't Build AI Without Progressive Delivery](https://thenewstack.io/why-you-cant-build-ai-without-progressive-delivery/)
> 
> 作者：Heather Joslyn

[前任](https://thenewstack.io/github-loses-its-ceo-and-independence/) [GitHub](https://github.blog/) 首席执行官 Thomas Dohmke 曾告诉 James Governor：“没有渐进式交付，你无法进行基于人工智能的开发。”

这是一个惊人的说法，但 RedMonk 分析公司联合创始人、《渐进式交付》新书合著者 Governor 认为这种联系显而易见。

在本期 The New Stack Makers 节目中，Governor 与 TNS 创始人兼出版商 Alex Williams 在 [AWS re:Invent](https://reinvent.awsevents.com/on-demand) 上坐下来，探讨了过去十年改变了软件发布方式的相同原则，为何不仅依然相关，而且对于任何使用人工智能进行构建的人来说都至关重要。

## 为不确定性而构建的防护栏

当你思考人工智能系统在生产环境中的实际作用时，这种相似性就变得清晰起来。模型会[产生幻觉](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/)。大型语言模型之间的行为差异很大。输出是非确定性的，这是传统软件从未有过的。

“你正在推出一些东西，你不确定它将如何表现，系统将如何表现。如果你改变了模型会怎样？那会产生什么影响？” Governor 问道。“我们需要衡量这一点。我们需要看到它的实际行为。如果你知道，那么就考虑进行回滚。所有这些——这就是渐进式交付。”

他补充说，从特性标志、金丝雀发布和可观测性中产生的实践，不仅仅是人工智能应用程序的锦上添花。它们是基础。人工智能概念，如评估、版本控制和受控发布，都源于传统的软件交付生命周期。

## DevOps 遗漏了某些人

但 Governor 的书不仅仅关于人工智能。它挑战了我们谈论软件交付方式中根深蒂固的一个基本假设。

“在 DevOps 中，你有开发（Dev），你有运维（Ops），对吧？但第三个循环在哪里？”他问道。“用户在哪里，以及用户对你的数字产品和服务的体验的反馈在哪里？”

这本书基于一个由四个 A（abundance、autonomy、alignment 和 automation，即丰富性、自主性、一致性和自动化）组成的框架，论证渐进式交付弥合了这一差距。它旨在在正确的时间将正确的产品交付给正确用户，并实际衡量你是否成功。为了强调这一点，Governor 引用了 Honeycomb.io 的联合创始人兼首席技术官 Charity Majors 的话：“如果用户不满意，你有五个九的可用性也没关系。”

他指出[亚马逊](https://aws.amazon.com/?utm_content=inline+mention)是应对这些紧张关系的案例研究。该公司传奇的“双披萨团队”和服务所有权模型赋予工程师巨大的自主权，但也因不同团队做出不同的工具选择而带来了协作一致性挑战。现在，亚马逊正在追求更多的标准化，试图在开发者自由和组织一致性之间取得平衡。

收听完整的对话，了解这本书如何与合著者 Kim Harrison、Heidi Waterhouse 和 Adam Zinman 一起完成，为何 IT Revolution 的 Gene Kim 决定出版它，以及 Governor 从与亲身经历这些渐进式交付挑战的公司交谈中学到了什么。