<!--
title: 那场帮助 Anthropic 找准身份的 24 小时实验
cover: https://cdn.thenewstack.io/media/2021/02/b469c2c9-golden-gate-bridge-731207_1280.jpg
summary: Anthropic 的产品负责人 Dianne Penn 解释了在 AI 时代，评估体系正在取代传统产品需求文档（PRD）。通过小团队快速实验，Anthropic 实现了从对话机器人到协作助手的转型，并强调了在概率模型时代，“亲自动手构建”对工程领导力的核心重要性。
-->

Anthropic 的产品负责人 Dianne Penn 解释了在 AI 时代，评估体系正在取代传统产品需求文档（PRD）。通过小团队快速实验，Anthropic 实现了从对话机器人到协作助手的转型，并强调了在概率模型时代，“亲自动手构建”对工程领导力的核心重要性。

> 译自：[The 24-hour experiment that helped Anthropic find its identity](https://thenewstack.io/anthropic-evals-replace-prds/)
> 
> 作者：Amanda Caswell

**如果你正在构建传统软件**，你需要编写产品需求文档（PRD）。如果你正在构建前沿 AI，你则需要运行评估。这就是 Anthropic 目前的现实。

[Dianne Penn，](https://www.linkedin.com/in/dianne-na-penn/)该公司 AI 研究与实验室的产品负责人，最近在 [*Lenny’s Podcast*](https://www.lennysnewsletter.com/p/anthropics-first-technical-pm-on) 上解释说，评估套件实际上正在终结传统的 PRD。从确定性代码转向概率模型，意味着工程团队必须抛弃旧有的成功定义手册，转而专注于搜寻 bug。

## 评估取代了 PRD

在 Anthropic，研究型产品经理团队将评估集视为他们的主要产物。Penn 的团队为每一个重大功能生成 30 到 40 个代表性示例，将其编码为带有预期输出的提示词（prompts），这些预期输出作为真值（ground truth）。开发人员必须构建[持续集成流水线和自动化测试基础设施](https://thenewstack.io/why-cicd-fails-llms/)，以便根据新的模型构建版本，大规模地对这些预期输出进行程序化运行。

底层的缩放曲线（scaling curves）虽然平滑，但模型实际能做的能力却在突飞猛进。像可靠的数学推理这样的能力，似乎一夜之间就会出现。“除非你有评估，除非你有测试系统，否则这些跳跃实际上可能发生，而你却毫不知情，”Penn 说道。如果没有[有效的自动化评估](https://thenewstack.io/your-ci-cd-pipeline-is-not-ready-to-ship-ai-agents/)，工程团队可能永远无法意识到这些新能力的存在——这造成了 Penn 所描述的“产品悬垂”（product overhang）。

> “除非你有评估，除非你有测试系统，否则这些跳跃实际上可能发生，而你却毫不知情。”

捕捉这些能力也改变了团队进行产品质量保证（QA）的方式。团队往往不再追踪代码执行过程，而是通过阅读对话来理解模型为何做出特定决策。

幻觉、过度自信的假设或失败的工具调用都可能产生看起来相似的错误，但每一个都需要[完全不同的修复方案](https://thenewstack.io/debugging-probabilistic-ai-systems/)。Penn 表示，另一个挑战是[阿谀奉承（sycophancy），即模型强化错误前提而不是纠正它](https://thenewstack.io/silent-llm-hallucination-loop/)。如果任其发展，这种行为可能会逃过测试并出现在生产环境中。

这也改变了优秀工程领导力的定义。管理者需要对他们所监管的模型有实践经验。如果他们不经常使用这些模型并亲眼观察什么有效、什么无效，他们就有可能失去做出正确架构决策所需的直觉。Penn 直言不讳地说：“如果你不亲自构建，你就无法成功。”

> “如果你不亲自构建，你就无法成功。”

这种构建产品的方式也塑造了 Anthropic 最大的战略赌注之一：开发者工具。回到 2023 年，Anthropic 与编程根本没关联。正如 Penn 回忆的那样，“[2023 年之前] 没有人把 Anthropic 和编码放在同一个句子中。”但该公司看到人们试图用竞争对手的模型来处理编程任务，于是通过将编码作为 [Claude 3 Opus](https://www.anthropic.com/news/claude-3-family)（2024 年 3 月发布）的重点工作进行了回应。

Penn 指出，此举反映了 Anthropic 思维更深层次的转变。模型要从对话机器人进化为真正的助手，必须跨越从“说”到“做”的鸿沟，这最终促成了 [Claude Code](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/)，以及后来的 [Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)。

Claude Code 在 2025 年 2 月发布研究预览版、5 月全面上市后已经[势头强劲](https://thenewstack.io/ai-coding-tool-stack/)。但当 Opus 4.5 在 11 月到来时，采用率加速了。Penn 认为这两次发布深度关联，断言二者缺一不可，否则就不会产生这种影响力。

## 小团队追逐大赌注

Penn 还揭示了 Anthropic 的研发部门是如何设置以捕捉 AI 能力的突然飞跃。2024 年年中，该公司专门成立了实验室团队，以追逐那些不符合正常产品路线图的实验性想法。他们的工作是采用一个基本概念，并找出其 10 倍、100 倍或 1000 倍的版本是什么样子。这种方法依赖于保持工程小组的规模极小。“追逐极其模糊、宏大想法的超大型团队最终会被拖慢速度，”Penn 说。

这种模式的早期验证来自一个意想不到的地方。Anthropic 的研究人员调高了某个特定的激活特征，发现 Claude 变得沉迷于金门大桥。在 24 小时内，一个跨职能团队在 claude.ai 上发布了一个实时消费者体验。它只触达了约 2000 人，但 Penn 称其为一个转折点：“那是发现我们身份的隐藏拐点之一。”

> “一个思维伙伴不仅仅是同意你的观点。它应该为你加分，你应该在与 Claude 合作后得到更好的想法。”

## 人变得更加重要

Penn 说她经常使用研究版本的 Claude 来挑战自己的产品想法，因为她寻找的是异议，而不是验证。如果模型指出了她思维中的缺陷，那这就是它在履行职责的信号。“一个思维伙伴不仅仅是同意你的观点，”她说。“它应该为你加分，你应该在与 Claude 合作后得到更好的想法。”

核心挑战正在从如何编写代码转向决定首先构建什么。Penn 认为人的作用变得更加关键。

“那些以用户为中心，深入了解用户想要完成什么的细节，以可操作的方式总结这些信息，并进行不懈努力的人的角色。对我来说，这就是产品人员的核心，”她说。“而我们确实需要更多这样的人。”