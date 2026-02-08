<!--
title: Anthropic 为 Cowork 引入插件，非开发者也能玩转 AI！
cover: https://cdn.thenewstack.io/media/2026/01/db825967-austin-distel-wawefydpkag-unsplash-scaled.jpg
summary: Anthropic 为 Cowork 引入了插件系统，赋予非开发人员强大的扩展能力。该系统提供多样化功能插件，涵盖生产力、销售、金融等多个领域，并支持应用内创建和管理。插件基于本地文件系统，易于分享，旨在让 Claude 成为“跨职能专家”。
-->

Anthropic 为 Cowork 引入了插件系统，赋予非开发人员强大的扩展能力。该系统提供多样化功能插件，涵盖生产力、销售、金融等多个领域，并支持应用内创建和管理。插件基于本地文件系统，易于分享，旨在让 Claude 成为“跨职能专家”。

> 译自：[Anthropic brings plugins to Cowork](https://thenewstack.io/anthropic-brings-plugins-to-cowork/)
> 
> 作者：Frederic Lardinois

Anthropic 正在通过插件系统扩展 Cowork，该系统捆绑了技能、连接器、斜杠命令和子代理，为非开发人员提供了 Claude Code 用户已经熟悉的扩展性。

[Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork) 于两周前推出，是 Anthropic 针对知识工作者推出的 Claude Code 版本，这些工作者不想编写代码，但希望拥有一个类似的代理工具来帮助他们创建或清理文档、[组织文件](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/)以及总结大量本地存储的文档。

为了帮助新用户开始使用插件，Anthropic 于周五在 GitHub 上推出了 [11 款开源插件](https://github.com/anthropics/knowledge-work-plugins)，涵盖了广泛的使用场景，展示了这项新功能的可能性。

![](https://cdn.thenewstack.io/media/2026/01/fa598ea8-cowork-plugins-1-scaled.png)

*Claude 桌面应用中的 Cowork（图片来源：Anthropic）。*

其中包括用于任务、日历和日常工作流的生产力插件。对于销售和营销用户，有帮助他们研究潜在客户和准备交易，或起草内容和规划活动的插件。金融用户使用插件分析财务数据和构建预测模型。企业搜索、法律、客户支持、产品管理，甚至生物学研究也有类似的插件。

还有一个用于创建和自定义其他插件的元插件。鉴于每家公司对某些业务流程都有自己的看法，此功能是必需的，但通过将其作为单独的插件，Anthropic 也消除了直接编辑这些文件的复杂性。

实际上，这意味着例如销售插件包括一个连接器，可以将 Claude 与 CRM 工具和知识库集成。它还包括用于启动潜在客户研究或完成通话跟进的斜杠命令。

Cowork 团队写道，所有这些都意味着 Claude 现在可以成为“跨职能专家”。

![](https://cdn.thenewstack.io/media/2026/01/21a57ea3-cowork-plugins-2-scaled.png)

*在 Claude 桌面应用中管理 Cowork 插件（图片来源：Anthropic）。*

由于 Cowork 基于本地文件系统，插件也是如此。这使得它们非常易于组装和共享。

Cowork 所基于的 Claude Code 也遵循相同的流程。其内容略有不同（主要是技能、代理和[钩子](https://thenewstack.io/gemini-cli-gets-its-hooks-into-the-agentic-development-loop/)），但设置 Claude Code 插件的过程也同样基于文件系统。

由于 Cowork 专为不一定熟悉终端的用户设计，因此插件安装在应用内进行，并且构建插件使用“插件创建”插件——无需 CLI。Claude 桌面应用还允许用户浏览每个插件包的内容。

Cowork 插件现已向所有 Claude 专业版和尊享版用户开放。