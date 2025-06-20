
<!--
title: 追逐AI自主性，当心错失Agentic的近期回报
cover: https://cdn.thenewstack.io/media/2025/06/11212830-exoskeleton123.jpeg
summary: 大型推理模型在复杂算法挑战中表现不佳，但编码助手在特定任务中表现出色。AI工程结合实验和直觉，将AI应用于实际问题。代理应专注于小目标和现有工作流程，利用AI改进软件开发，而非完全替代。开发人员应构建真实产品，进行测试和测量，以实现有意义的变革。
-->

大型推理模型在复杂算法挑战中表现不佳，但编码助手在特定任务中表现出色。AI工程结合实验和直觉，将AI应用于实际问题。代理应专注于小目标和现有工作流程，利用AI改进软件开发，而非完全替代。开发人员应构建真实产品，进行测试和测量，以实现有意义的变革。

> 译自：[Chasing AI Autonomy Misses Near-Term Agentic Returns](https://thenewstack.io/chasing-ai-autonomy-misses-near-term-agentic-returns/)
> 
> 作者：Jonathan Eyler-Werve

Apple 最近发表了一篇论文，要求大型推理模型 (LRM) 解决一些简单但冗长的算法挑战，例如汉诺塔圆盘排序难题。结果模型惨败。模型能够解决三个圆盘的汉诺塔挑战（其中圆盘根据简单的规则在桩之间移动），但在八个或更多圆盘时失败。该论文表明，即使提供了算法，[模型也会猜测规则的输出](https://www.anthropic.com/research/tracing-thoughts-language-model)。

Apple 的发现并非独一无二。在题为“[Mind The Gap: Deep Learning Doesn’t Learn Deeply](https://arxiv.org/abs/2505.18623)”的论文中，[Subbarao Kambhampati](https://www.linkedin.com/in/subbarao-kambhampati-3260708/) 写道，对模型内部运作的检查表明，在算法挑战中成功的模型在内部并不忠实于算法。换句话说，得到正确答案的模型可能正在使用“替代策略”，类似于我的青少年在考试前一晚死记硬背朝代：*正确的答案是你认识的名字。* Kambhampati 认为，[LRM 与](https://arxiv.org/html/2504.09762v1)它们所改编的[大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/) 没有根本区别。

正如统计学家所说：所有模型都是错误的，但有些是有用的。

## 少一些推理，多一些算法

正如 [Gary Marcus](https://x.com/GaryMarcus) 所写，[LLM](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/)“不能替代优秀的、定义明确的传统算法。” 我一直在提示 [Claude](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) 为我[输出算法](https://claude.ai/public/artifacts/b49e1119-c0f9-479b-9678-32b73af32658)。我要求它为该算法编写一个验证器。然后，我要求它给我一个[演示应用程序](https://claude.ai/public/artifacts/01d5ee53-84b7-41b0-acae-c16585844ce8)，展示解决方案。

该模型第一次就解决了汉诺塔问题。

![](https://cdn.thenewstack.io/media/2025/06/f4176d34-image1.gif)

由 LLM 编写的算法比调用 AI 获得相同结果更好：它具有良好的可扩展性，比机器学习 (ML) 模型更有效，并且应该像浏览器中的任何其他内容一样准确地运行。编写代码的模型得益于许多已发布的参考解决方案，这些解决方案也是学习编码的主要内容，对于“我是否在赚钱？”和“我的披萨什么时候到？”等关键业务问题也是如此。

## 实验与直觉

为了从基础模型中获得价值，我们需要将它们指向适当范围的问题。在实践中，确定 AI 问题范围的工作是实验和开发者直觉的结合，在企业环境中，使用开发者平台可以安全地尝试小批量实验。（披露：我在 [VMware Tanzu Platform](https://www.vmware.com/products/app-platform/tanzu) 上从事这项工作。）您可以将全栈开发和模型意识的这种结合称为“AI 工程”。

我的队友和 AI 工程师 [Brian Friedman](https://www.linkedin.com/in/bryanmfriedman?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAADmNKcBbSK382e8_UxUekKinr4fh1hKSO4&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BJ14Bs90tTseEVQMNKJNt0Q%3D%3D) 说：“需要付出努力……你必须以狭隘的方式提供你组织的具体信息，以便获得具体而准确的回复。我们需要将检索增强生成之类的东西视为前进的方向，而不是权宜之计或反模式，以便安全有效地使用 AI。”

## 代理：比我们一直在做的要好

这让我们了解了代理，这也是推理模型存在的原因。如果推理模型能够像零样本解决方案一样思考漫长的工作流程，那将非常可爱：*帮我找一张机票，我不在乎怎么找。* 更可能的情况是，我们将继续编写软件。

我们将确定小的中间目标并存储结果。我们将调用服务和工具以及验证器。我们将用 Java 和 Python 以及 Go 实现算法。我们将一路获得来自人类的反馈。我们将担心延迟、安全和碳排放。

像 Claude、Devstral 和 [Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) 这样的编码助手很可能可以为我们完成一些工作。但是，弄清楚用户想要什么以及测试产品市场契合度的缓慢工作仍然必须进行。

![](https://cdn.thenewstack.io/media/2025/06/da41945e-image3.jpg)

基础模型解决了难题。我天生就持怀疑态度，因此在过去的五年里，我一直在用现实世界的问题测试 LLM，构建代码分析、搜索、摘要、结账和客户支持工具。在“将相关的 JSON 位从数据库传输到 UI”的范围内，推理模型被证明是稳定、准确和快速的。现在集成很便宜。分类有效。您可以将业务规则以自然语言的形式添加到应用程序中——“执行此操作，除非是以下情况之一”——并且它在第一天运行良好。

作为一名开发人员，令人愉快的惊喜开始多于可怕的惊喜。

最近影响者从“代理”到“代理应用程序”的回退是一种令人鼓舞的炒作周期修正。正如我之前所写，[现有的软件工作流程](https://thenewstack.io/ai-agents-why-workflows-are-the-llm-use-case-to-watch/) 是不太成熟的代理采用的近期目标。我们以一种令人难以置信的通用方式解决了自然语言理解。这只是现在在高价值工作流程中实现产品化（我将把像 ChatGPT 这样的消费者聊天机器人留到另一天讨论）。企业从容易以美元衡量的领域开始（销售团队优先级、客户支持、[站点可靠性工程](https://techdocs.broadcom.com/us/en/vmware-tanzu/cloudhealth/tanzu-cloudhealth/saas/tnz-cloudhealth/exploring-cloudhealth-new-experience-nx-intelligent-assist.html) [SRE]），但在未来十年，它将逐渐渗透到披萨店和零售仓库等场所，作为小的但有用的流程改进。用户不需要知道其中存在基础模型。他们只是想要更好的软件。

## 机器人可以洗衣服，但只能为软件开发人员洗

第一波半自治代理今天在开发人员的笔记本电脑上运行。在标题为“[我的 AI 怀疑论者朋友们都疯了](https://fly.io/blog/youre-all-nuts/)”的帖子中，软件工程师 [Thomas Ptacek](https://x.com/tqbf) 写道：

“如今使用 LLM 进行编码的人都在使用代理。代理可以自行浏览你的代码库。他们直接编写文件。他们运行工具。他们编译代码、运行测试并迭代结果。他们还：

* 将树中或在线其他树中的任意代码拉入其上下文窗口，
* 运行标准的 Unix 工具来导航树并提取信息，
* 与 Git 交互，
* 运行现有的工具，如 linter、格式化程序和模型检查器，以及
* 通过 MCP 进行基本上任意的工具调用（你设置的）。

我的经验和各种[研究](https://www.microsoft.com/en-us/research/publication/towards-effective-ai-support-for-developers-a-survey-of-desires-and-concerns/) [支持](https://getdx.com/research/devex-what-actually-drives-productivity/) 这一点。票务、测试、代码存储库和部署管道都表示为工具，通常使用 [模型上下文协议](https://spring.io/blog/2024/12/11/spring-ai-mcp-announcement) (MCP) 将它们连接起来。连接到代码编辑器的机器人允许开发人员提出问题，例如“嘿，Tanzu Platform，此用例批准使用什么数据基础设施？”，并获得由他们正在处理的内容在上下文中塑造的答案。

这是对所有知识工作者的“代理”组织的一种暗示：不是高度自治的机器人，而是围绕着有权能的人类的一种可操纵的动力装甲，他们可以更快地开始工作，更安全地工作，并将更多时间花在困难（甚至有趣）的问题上。

![](https://cdn.thenewstack.io/media/2025/06/6605e9c7-image2-1024x606.png)

与此同时，构建者继续构建。我的前 Sprout Social 同事 [Kevin Stanton](https://www.linkedin.com/in/stantonk?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAABGMzoBFokCpvsb23c9PsRdBNjGFi1EXC8&lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3B6zFW9BHaRKiGbmXJfqdJgw%3D%3D) [发布](https://www.linkedin.com/posts/activity-7336172175130882048-41OL?utm_source=share&utm_medium=member_desktop&rcm=ACoAAACMg-oB-ggwAYzEbksUHvF-GZvbiThb9ZU)，“迫不及待地想让这个炒作周期结束。唯一的出路是构建真实的东西，忽略闲聊。”

运行小型测试。测量结果。在现实约束中使用现实数据，如果必须，手动组装模型的上下文输入，或者更好的是，使用平台快速安全地连接数据、计算、推理和评估组件。所有这些力量的目的不是为了用虚无缥缈的原型给你的老板留下深刻印象，也不是为了通过 AI 新闻稿来提振下滑的股价，而是为了制造更好的产品。尝试一些东西。展示给客户。倾听。

好吧，但是重大的变革性变化呢？这就是。你会在事后看到它。
