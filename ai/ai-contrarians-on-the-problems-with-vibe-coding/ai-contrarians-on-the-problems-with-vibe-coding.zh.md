“现在到底是怎么回事？”工程师 [David DeGraw](https://github.com/catskull)，又名 Catskull，在上周的一篇[博客文章](https://catskull.net/what-the-hell-is-going-on-right-now.html)中问道。

氛围编程。一些开发者表示，现在发生的就是氛围编程——它让每个人都精疲力尽，毁掉一切。

DeGraw 写道：“工程师们正在 burnout（精疲力竭）。各个组织期望他们的高级[工程人员能够审查](https://thenewstack.io/ai-coding-assistants-are-reshaping-engineering-not-replacing-engineers/)并为无法工作的 ‘氛围编程’ 功能做出贡献。”

他对 AI 影响的批评并不孤单。和 DeGraw 一样，许多人认为 AI 就像那位没穿衣服的皇帝。

## Devin 实验

AI 反对者认为，不仅是前沿的[大型语言模型](https://thenewstack.io/will-llms-and-vibe-coding-fuel-a-developer-renaissance/)存在问题，专业的 AI 工具也一样。

Answer.AI 的编程团队花了一个月的时间使用 [Devin](https://devin.ai/)，它声称自己是“完全自主的软件工程师”。它于 2024 年 3 月首次发布。

机器学习工程师 [Hamel Husain](https://x.com/HamelHusain) 和数据科学家 [Isaac Flath](https://www.linkedin.com/in/isaacflath/) 以及 [John Whitaker](https://github.com/johnowhitaker) 在 1 月份公开分享了[他们使用该工具的经验](https://www.answer.ai/posts/2025-01-08-devin.html)。他们发现，起初代码有点冗长，但可以工作。

他们写道：“我们曾设想让 Devin 在我们的会议期间编写文档，或者在我们专注于设计工作时调试问题。但随着我们扩大测试范围，裂缝出现了。”

看起来很简单的任务需要几天而不是几个小时。Devin 会陷入技术死胡同。他们还补充说，它还会创建过于复杂、无法使用的解决方案。

他们指出，Devin 甚至会推进实际上不可能完成的任务。

他们指出：“当被要求将多个应用程序部署到单个 Railway 部署（Railway 不支持）时，Devin 没有识别出这个限制，而是花了一天多的时间尝试各种方法并虚构不存在的功能。”

这导致了这样的观察：“最令人沮丧的不是失败本身——所有工具都有局限性——而是我们花了多少时间试图挽救这些尝试。”

他们开始将其记录在三个类别中：

1. 从头开始创建新项目；
2. 执行研究任务；以及
3. 分析/修改现有项目。

他们写道，在 20 个任务中，有 14 个失败，3 个成功——包括他们最初的两个——以及 3 个不确定的结果。

他们写道：“更说明问题的是，我们无法辨别出任何模式来预测哪些任务会成功。看起来与我们早期成功案例相似的任务会以意想不到的方式失败。”

## AI 夺走了什么

[Luciano Nooijen](https://github.com/lucianonooijen/) 也对 [AI 工具感到失望](https://lucianonooijen.com/blog/why-i-stopped-using-ai-code-editors/)。他是游戏行业的工程师，专注于在线游戏客户端开发、多人游戏功能和引擎编程。他从 [ChatGPT](https://thenewstack.io/does-chatgpt-encourage-dangerous-delusions/) 到 [GitHub Copilot](https://thenewstack.io/the-top-ai-tool-for-devs-isnt-github-copilot-new-report-finds/) 都进行了尝试，并且从 2022 年末 ChatGPT 首次发布时开始，就将 AI 工具作为其工作流程的一部分。他在 2023 年继续在其开发工作流程中使用基于 AI 的工具。

Nooijen 写道：“最初，我对这些 [LLM](https://thenewstack.io/introduction-to-llms/) 的能力印象非常深刻。我可以简单地复制粘贴晦涩的编译器错误以及 C++ 源代码，然后被告知错误的原因，这感觉就像魔法一样。”

但他将其比作具有完全自动驾驶 (FSD) 功能的特斯拉汽车。

他写道：“依赖特斯拉的 FSD 夺走了我进入自动驾驶的能力。使用 AI 驱动的代码编辑器有点类似。”

最初，Nooijen 觉得 AI 辅助编程速度更快。但当他在处理个人副项目时不得不放弃他的 AI 工具时，他意识到 AI 也夺走了一些东西。

他写道：“我觉得自己完成一些相当基础的软件开发的能力不如一年前左右。突然，我非常清楚自己变得多么依赖 AI 工具。每当我定义一个函数时，我都会在编辑器中暂停，等待 AI 工具为我编写实现。我花了一些力气才回忆起手动编写单元测试的语法。”

Nooijen 还注意到，随着时间的推移，AI 变得越来越没用。它也削弱了他对自己能力的信心。

他说：“它不仅让我失去了乐趣，而且我开始对自己做出一些实现决策感到有些不安全。很明显，因为我不经常练习基础知识，所以我处理更难的部分的能力也较差。”

2024 年，Nooijen 从他的代码编辑器中删除了所有 LLM 集成，并恢复到非辅助编码。

Nooijen 写道：“你使用一种语言、框架或代码库的时间越长，你就越能培养出对正确方法的这种直觉。这种直觉是我在很大程度上依赖 AI 工具时慢慢失去的。而这来自一位首席开发人员。”

他也忍不住想知道开发人员如何才能希望通过[“氛围编程”](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)的方式晋升为高级开发人员。

Nooijen 质疑道：“当 AI 工具出现故障或变得过于昂贵时，你将从哪里获得维护和扩展氛围编程代码库的技能？”

## 后开发者时代？并非如此

前端开发人员和培训师 Josh Comeau 认为，[AI 取代](https://www.joshwcomeau.com/blog/the-post-developer-era/) [前端开发人员](https://roadmap.sh/frontend) 的预测被夸大了。

Comeau 在他对编程中使用的 AI 软件的评估中写道：“据我所知，每个 AI 成功案例仍然需要熟练的人类开发人员作为必要成分。因此，我认为可以肯定地说，我们没有生活在后开发者时代。”

Comeau 尝试了 [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/)，发现它需要指导。他也将其比作驾驶汽车，但使用的是巡航控制。

他说：“这有点像在高速公路上使用‘巡航控制’：汽车基本上会驶向你所指的方向，但你仍然需要一只手放在方向盘上，保持稳定。否则，汽车会慢慢开始偏离车道。如果你不偶尔将其推回正轨，你最终会掉进沟里。”

他写道，AI 也是如此。

他补充说：“如果我不知道如何编写代码，我就不会注意到该模型输出中细微但至关重要的问题。我不知道如何纠正方向，甚至没有意识到需要纠正方向！”

他说，LLM 确实为他节省了时间。但总的来说，他仍然花费大部分时间自己编写代码。

## AI 正在毁掉一代程序员吗？

但 AI 带来的真正威胁可能在于它如何影响下一代开发人员。DeGraw 认为，初级开发人员过度依赖该工具。他写道，最好的工程师喜欢帮助新团队成员做出贡献和学习，但如果一切都只是 AI 提示的素材，他们就无法做到这一点。

DeGraw 写道：“那些倒霉的年轻程序员没有将他们的评论铭记于心、进行反思并将其用作学习机会，而是将反馈简单地用作他们 ‘AI’ 杰作中的下一个提示。我亲眼目睹并听到了第一手的叙述，其中非常明显的是，一位初级工程师在（滥用）LLM 工具。”

但现在，围绕 AI 存在一种“[集体思维](https://www.psychologytoday.com/us/basics/groupthink)”心态。

他说：“在最近一次公司全体会议上，我看到一个初级工程师团队演示了他们的最新工作。我无法告诉你它到底做了什么，甚至它应该做什么——他们自己似乎也不明白。一位高级经理为他们的 ‘成功’ 欢呼，怂恿他们吹嘘自己使用 ‘AI’ 工具，他们回答说，‘这是 Claude 编写的 4,000 行代码。’ 全场鼓掌。”

但他补充说，当你深入研究代码时，就会发现问题。DeGraw 引用的一位朋友花了一个月的时间在一个开发人员团队中，负责审查一个大量使用氛围编程的 pull request。

他写道：“一个月。审查 LLM 产生的垃圾。每月支付 ChatGPT 20 美元，然后让一个真正的工程师团队尝试审查和合并代码，这样做能节省多少成本？”

AI 的另一个痛点也可能对初级开发人员不利：许多公司认为 AI 将使开发人员变得过时。Comeau 写道，这意味着一些公司没有像他们原本可能的那样“积极地”招聘。

Comeau 表示：“公司没有招聘他们需要的开发人员，因为他们确信 AGI（通用人工智能）指日可待，当那个鸡蛋孵化出来时，我们根本不需要人类开发人员了。‘很快就会到来了’，他们已经说了好几年了。”