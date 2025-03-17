
<!--
title: AI Agent如何开始自动化企业
cover: https://cdn.thenewstack.io/media/2025/02/99637b45-alexander-mils-zzl4cvkd9mq-unsplashb.jpg
summary: Orby推出企业级AI模型LAM，用ActIO收集百万级“痕迹”数据，探索Salesforce、SAP等软件的自动化任务。对比OpenAI Operator，Orby强调“grounding”和AI Agent软件栈。建议CIO关注用户痛点，利用AI Agent简化耗时但易于自动化的流程，如费用报告审计，无需API集成，但需重视安全和人工参与。
-->

Orby推出企业级AI模型LAM，用ActIO收集百万级“痕迹”数据，探索Salesforce、SAP等软件的自动化任务。对比OpenAI Operator，Orby强调“grounding”和AI Agent软件栈。建议CIO关注用户痛点，利用AI Agent简化耗时但易于自动化的流程，如费用报告审计，无需API集成，但需重视安全和人工参与。

> 译自：[How AI Agents Are Starting To Automate the Enterprise](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/)
> 
> 作者：Richard MacManus

到目前为止，2025 年是 [AI agent](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 的一年——生成式 AI 技术被用于自动化操作。我们已经看到了 OpenAI 的 Operator 的首次亮相，展示了一个可以浏览网页并为你完成任务的原型 [agent](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/)。现在，一家名为 [Orby](https://www.orby.ai/) 的新公司正在将同样的方法引入企业，它称之为大型行动模型 (LAM) 的一种 AI 模型。

我与 Orby 的联合创始人兼首席技术官 Will Lu 谈论了企业中的 agent。在加入 Orby 之前，Lu 曾是 Google Cloud AI 的工程负责人。

那么什么是 LAM？它与 LLM 究竟有何不同？Lu 解释说，与 LLM 将文本或图像作为输入并生成文本或图像作为输出不同，LAM 专门为企业环境中的自动化任务而设计。他提到 Salesforce 和 SAP 作为其 LAM 探索过的 IT 软件产品的示例，目的是识别可以自动化的任务。

他继续说，LAM 将*行动*作为输入——例如应用程序屏幕截图、网页 HTML 内容、用户交互（例如鼠标点击和键盘输入）。他说，Orby 的 LAM 可以使用这些上下文来自动化复杂的工作流程。

![](https://cdn.thenewstack.io/media/2025/02/a2b30c8e-actio-orby-feb25.png)

*Orby ActIO 图;通过 Orby*

## 企业软件的痕迹

Lu 用“痕迹”一词来描述其基础 LAM（名为 [ActIO](https://www.orby.ai/actio)）一直在收集的工作流程数据。他说，它已经收集了“超过一百万条痕迹，通常一条痕迹可能有 10 到 50 步长”。

在之后的澄清邮件中，Lu 扩展了“痕迹”的定义：

“…痕迹是完成特定任务的一系列操作。一个操作被捕获为上下文、网页应用程序的屏幕截图和 html 以及桌面应用程序的可访问性树的组合，以及诸如鼠标点击、按键类型等事件。”

他接着解释说，他们的软件会主动探索企业软件环境（例如，Salesforce、ERP 系统），以识别可以自动化的任务。该 agent 自主尝试这些任务，并且性能最佳的尝试（成功的痕迹）用于微调模型。

像大多数其他大型语言模型一样，Orby 已经在开放的 Web 数据上训练了 ActIO。但是，Lu 补充说，他们还可以使用客户的专有数据进行微调。

## 与 OpenAI 的 Operator 的比较

Orby 的解决方案与 OpenAI 的 Operator 有相似之处，后者于 1 月底 [推出](https://openai.com/index/introducing-operator/)。Operator 目前仅适用于 Pro 用户（每月 200 美元），OpenAI 将其描述为“一个可以使用自己的浏览器为你执行任务的 agent 的研究预览”。在评论中，《纽约时报》的 Kevin Roose [称其为](https://www.nytimes.com/2025/02/01/technology/openai-operator-agent.html)“与其说是一个我建议使用的产品，不如说是一个有趣的演示——而且绝对不是大多数人需要每月花费 200 美元的东西。”

我问 Lu，Orby 与 OpenAI Operator 相比如何？

他说，其中一个区别是 Orby 有一个它称之为“grounding”的概念。

“基本上，grounding 是 [对于] 你想要做的特定操作——例如，提交报告。所以这就是操作，然后你想找到可以完成该操作的元素，然后触发它。这称为 grounding 步骤。”

这个概念来自 Orby 与俄亥俄州立大学合作的一个项目，名为 [UGround](https://osu-nlp-group.github.io/UGround/)——被描述为“一种通用的视觉 grounding 模型，用于通过 GUI 上的像素坐标定位操作的元素”。UGround 在来自 130 万张屏幕截图的 1000 万个元素上进行了训练。

> “当涉及到真正复杂的、真实的企业用例时，我们期望技术人员确保它能够大规模运行。”
>
> – Will Lu, Orby CTO

Lu 还指出，Orby 拥有一个 AI agent 软件堆栈，可提供给企业。

“所以基本上 […] 我们将其设计为用户可以演示如何完成任务。基于该演示，我们生成描述和描述下的代码以供运行。然后 […] 开发人员可以进入，查看描述和生成的代码，并根据他们的需求进行修改——然后根据应用程序定义的代码运行 agent。”

Lu 补充说，对于简单的任务，非技术员工可以运行这些任务。但是对于更复杂的“操作”，通常会涉及开发人员。

“当涉及到真正复杂的、真正的企业用例时，我们期望技术人员确保它能够大规模运行。例如，当一项任务目前由 100 个人完成时，您需要确保虚拟机设置正确，代理在相同的环境中运行，并且他们可以访问所有系统和所有凭据。”

## 给 CIO 的建议

AI 代理，或者用时髦的术语来说，[智能代理 AI](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/)，已经迅速成为企业 IT 部门需要考虑的优先事项。所以我问 Lu，当考虑是否以及何时使用 AI 代理时，他会给 CIO 和其他企业 IT 领导者什么建议。

“我认为最关键的是找到用户正在寻找的真正的业务痛点，”他回答说。“然后，当涉及到业务痛点时，我们希望确定对用户来说非常耗时的步骤。”

他补充说，这些步骤对于人类员工来说可能很耗时，但“对于计算机来说真的非常容易”。

Orby 客户的一个用例是费用报告审计。

“几乎每个企业都有这个流程，而且这个流程有点乏味，”Lu 说。“你必须打开一份报告，查看所有的收据，查看所有填写的信息，然后检查信息是否匹配 [...]。还要根据公司定义的政策检查这些报告——例如，不允许饮酒。”

> “……只要我们的代理能够访问系统 [...]，我们就可以登录系统，然后开展工作。”
>
> – Lu

作为一名科技记者，我的本能后续问题是询问 Orby 的软件连接到哪些 API——例如，SAP。但 Lu 证实，这一切都是通过 AI 代理完成的；不需要 API。

“这就是我们解决方案的优势。我们 [Orby 的软件] 主要像人类操作这些系统一样操作这些应用程序。因此，不需要实际的集成。因此，只要我们的代理能够访问系统，只要我们有凭据，我们就可以登录系统，然后开展工作。”

那么，安全问题呢？Lu 证实，安全“始终是几乎所有企业的首要要求”，并且他们与每位客户合作解决这个问题。

最后，值得注意的是，即使 Orby 的目标是帮助企业自动化工作流程，但目前始终有人工参与。

“整个智能代理工作流程设计是我们整个产品的核心，因为今天的模型仍然不能 100% 工作，而且这种情况还会持续很长时间，”Lu 说。“因此，我们通过设计内置了人工参与流程。”