<!--
title: 攻克开发者面临的3大企业AI难题
cover: https://cdn.thenewstack.io/media/2025/09/97662511-2025stackoverflowdevelopersurvey.jpg
summary: Stack Overflow调查显示，开发者对工作满意度上升，但对AI信任度下降。普遍使用AI，但对其生成的代码质量和企业内部数据缺乏存在挑战。企业需要解决AI代码质量问题，并提供内部知识库访问。
-->

Stack Overflow调查显示，开发者对工作满意度上升，但对AI信任度下降。普遍使用AI，但对其生成的代码质量和企业内部数据缺乏存在挑战。企业需要解决AI代码质量问题，并提供内部知识库访问。

> 译自：[Solving 3 Enterprise AI Problems Developers Face](https://thenewstack.io/solving-3-enterprise-ai-problems-developers-face/)
> 
> 作者：Loraine Lawson

今年的 Stack Overflow 调查发现，有 24% 的开发者对工作感到满意。这几乎是每四位开发者中就有一位。

当然，这并不是一个压倒性的比例，但比去年好，去年只有五分之一（即 20%）的人表示他们对目前的工作感到满意。

与此同时，他们似乎与 AI 达成了不安的和平：78.5% 的人表示他们每天到每月都会使用 AI。相比之下，有 16.2% 的人没有使用 AI 工具，也不打算使用。另有 5.3% 的人尚未使用工具，但计划很快使用。超过 33,660 名受访者（占 68.7%）回答了这个问题。

程序员们似乎也越来越习惯使用 AI 代理，有 [23% 的人经常使用 AI 代理](https://thenewstack.io/23-of-devs-regularly-use-ai-agents-per-stack-overflow-survey/)。

[2025 年 Stack Overflow 开发者调查](https://survey.stackoverflow.co/2025/) 发现，现在有 64% 的人表示 AI 不会对他们的工作构成威胁，略低于去年的 68%。调查还发现，目前在开发工作流程中[主要使用 AI 工具完成任务](https://thenewstack.io/ai-combined-with-agile-lets-developers-focus-on-craft/)的受访者对 AI 非常满意，并且经常使用 AI 搜索答案或学习新概念。

[![Stack Overflow 开发者调查显示，四分之一的开发者对工作感到满意，高于去年。28.4% 的人不满意，47.1% 的人感到自满。](https://cdn.thenewstack.io/media/2025/09/d0a703aa-stackoverflow-dev-survey-2025-work-job-satisfaction-job-sat-social.png)](https://cdn.thenewstack.io/media/2025/09/d0a703aa-stackoverflow-dev-survey-2025-work-job-satisfaction-job-sat-social.png)

*图片来自 Stack Overflow 2025 年开发者调查，根据 [开放数据库许可证](https://opendatacommons.org/licenses/odbl/) 授权。*

The New Stack 与 Stack Overflow 的首席产品技术官 Jody Bailey 讨论了调查结果。我们还询问了他如何在 Stack Overflow 自己的 IT 部门和企业开发者中看待 AI。

“开发者的定义将会演变，”Bailey 预测。“实际上，会有更多的人进行开发，因为它会更容易。工具和 AI 模型将继续变得更好。”

他表示，更好的 AI 将导致更多的员工，包括开发者，使用 AI 将他们的想法变为现实。

“我们有很多工程师和开发者都有非常棒的想法，[但]时间有限，能力有限，”他说。“同样，在设计和产品方面，这些工具将使人们能够更有效地展示他们的想法。这将使他们能够进行更多的创新，并真正专注于解决用户问题，而不是一直纠结于代码。”

但他指出，使用 AI 进行开发也存在挑战，尤其是在企业环境中。

## 挑战一：关于 AI 用的行政命令

Bailey 表示，尽管使用量增加，但对 AI 生成的答案和代码的信任度正在下降，这表明人们对 AI 工具持健康的怀疑态度。

在所有 Stack Overflow 受访者中，大多数人或多或少地不信任 AI 结果——占 45.7%，而信任 AI 结果的占 30.7%（只有 60.78% 的受访者回答了这个问题）。当调查将其分解为仅限专业开发者时（52.4% 的回复），他们发现 46% 的人不信任 AI，而 32.3% 的人信任 AI。

[![图表显示 3.1% 的人非常信任 AI；29.6% 的人有些信任 AI；26.1% 的人有些不信任 AI；19.6% 的人非常不信任 AI。](https://cdn.thenewstack.io/media/2025/09/0f1c7776-stackoverflow-dev-survey-2025-ai-developer-tools-ai-acc-social.png)](https://cdn.thenewstack.io/media/2025/09/0f1c7776-stackoverflow-dev-survey-2025-ai-developer-tools-ai-acc-social.png)

*图片来自 Stack Overflow 2025 年开发者调查，根据 [开放数据库许可证](https://opendatacommons.org/licenses/odbl/) 授权。*

高级领导层和开发者之间也存在脱节。Bailey 说，高管们倾向于认为 AI 可以搞定一切，而且速度非常快。一些领导者甚至对招聘设置了上限，除非团队能够证明这项工作不能用 AI 完成。另一些人则表示，如果开发者不使用 AI，那么他们就没有工作。

Bailey 认为这两种方法都是错误的。

“我的经验[是]这种命令往往会适得其反，”他说。“期望所有代码都由 AI 编写可能设定了错误的期望。盲目信任我们从 AI 生成的任何东西而不经过适当的审查和理解是不可行的。”

## 挑战二：糟糕的 AI 生成代码

虽然领导者似乎认为 AI 可以处理编码任务，但这并不是高级开发者所看到的。他们看到 AI 完成了大约 80% 的项目，但留下了 20% 未完成。不幸的是，这 20% 未完成的部分最终需要付出更多的努力。

开发者不信任 AI 的很大一部分原因还在于 AI 产生糟糕或无意义的代码。对于高级开发者来说，这导致了一个糟糕的选择：修复可能由不充分的提示创建的错误 AI 代码，或者只是从头开始自己编写代码。

“高级工程师[们]在问自己，[生成代码](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/)并修复它还是直接编写代码会更快，”Bailey 说。“有时编辑比调整需要更多的工作。”

> “关于如何使用 AI 生成代码，仍然有很多需要学习的地方。我们看到的一件事是，你提示某件事的方式会对实际生成的内容产生多大的影响。”
> 
> **– Jody Bailey，Stack Overflow 首席产品技术官**

Bailey 说，企业解决 AI 创建的[糟糕代码](https://thenewstack.io/bad-code-stalls-developer-velocity/)问题的一种方法是要求开发者提交他们的提示以及拉取请求。

“关于如何使用 AI 生成代码，仍然有很多需要学习的地方，”他说。“我们看到的一件事是，你提示某件事的方式会对实际生成的内容产生多大的影响。”

高级工程师说，如果有人不理解代码，他们怎么能提出正确的问题，他补充道。通过在拉取请求中包含提示，高级开发者可以确定措辞不当的提示在创建有缺陷的代码中扮演了什么角色。

“我认为这是一个非常聪明的想法，因为它很像你面试一名工程师时，你可能会要求他们解决一个问题。你不期望他们必须写出所有代码，而是告诉我你会如何思考它，”他说。

## 挑战三：AI 缺乏关于内部代码和实践的数据

另一个常见问题是[大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms/) 缺乏特定于公司代码库、标准和最佳实践的专有知识。为了弥补这些问题，开发者需要访问基于他们组织自己的内部编码知识库的工具。

[![近 64% 的开发者表示 AI 不会对他们的工作构成威胁。](https://cdn.thenewstack.io/media/2025/09/8e3971e8-stackoverflow-dev-survey-2025-work-job-satisfaction-ai-threat-social.png)](https://cdn.thenewstack.io/media/2025/09/8e3971e8-stackoverflow-dev-survey-2025-work-job-satisfaction-ai-threat-social.png)

*图片来自 Stack Overflow 2025 年开发者调查，根据 [开放数据库许可证](https://opendatacommons.org/licenses/odbl/) 授权。*

“另一件事，尤其是在大型企业中，是他们使用的几乎所有 AI 工具都建立在公共信息语料库上，这些信息可能与他们的特定组织相关，也可能无关，”Bailey 说。“那么，如何在开发者需要的时候将更细微或专有的信息交给他们呢？”

Stack Overflow 正在通过提供有关编码的知识来帮助解决这个问题。例如，Stack Overflow 提供 Stack Overflow for Teams，这是一种面向工程师的企业 SaaS 解决方案，已被 20,000 多个组织使用。它提供了一个知识智能层，以帮助开发者在编码时访问相关的内部文档和最佳实践。

他还补充说，计划通过 [模型上下文协议](https://thenewstack.io/building-your-first-model-context-protocol-server/) 或 IDE 来提供更多知识。

Bailey 说，LLM 提供了很多编码标准：它们可以完成函数，并且可以为你编写代码。但这一切都是基于行业的标准实践。问题在于如何在组织内呈现这些特定标准，并使它们成为流程的一部分。

“我们正在构建的一件事实际上是知识智能层，”Bailey 说。“我们想要做的是[在他们编写代码时将它放在他们的指尖](https://thenewstack.io/developers-put-ai-bots-to-the-test-of-writing-code/)，而不是让他们停下来去寻找这些信息。”