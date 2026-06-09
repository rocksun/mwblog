<!--
title: OpenClaw 擅用 Gavriel Cohen 代码，暴露出 AI Agent 的责任困局
cover: https://cdn.thenewstack.io/media/2026/06/dd3a5f08-kuliation-jolxzmw38uo-unsplash-scaled.jpg
summary: OpenClaw未经授权使用代码，暴露出AI Agent空有自主权却缺乏问责制的问题。文章指出，未来人类开发者的核心价值在于为AI生成的结果进行签字和承担责任。
-->

OpenClaw未经授权使用代码，暴露出AI Agent空有自主权却缺乏问责制的问题。文章指出，未来人类开发者的核心价值在于为AI生成的结果进行签字和承担责任。

> 译自：[OpenClaw used Gavriel Cohen's code and exposed the AI Agent accountability problem](https://thenewstack.io/openclaw-cohens-ai-agent-accountability-problem/)
> 
> 作者：Matthew Burns

*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 动态，解释它们对将这项技术付诸实践的个人和组织的意义。我们的宗旨很简单：学会使用 AI 的工作者将定义其行业的下一个时代，而本期简报旨在帮助您成为其中一员。*

---

**快速公告！** 前沿部署工程师（Forward Deployed Engineer）路线图现已在 [Roadmap.sh](http://roadmap.sh) 上线。[FDE 正成为](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/) [科技界最炙手可热的角色之一](https://thenewstack.io/why-the-forward-deployed-engineer-is-techs-hottest-job/)，我们迅速行动，[制作了一份分步指南](https://roadmap.sh/forward-deployed-engineer)，旨在帮助您快速掌握所需技能。

**极简 Agent NanoClaw 背后的开发者 Gavriel Cohen** 发现，自己的代码在未经授权且未署名的情况下被用在了 OpenClaw 中。他公开退出了该项目，而 [David Eastman 为 *The New Stack* 撰写的报道](https://thenewstack.io/nanoclaw-openclaw-agent-security/) 成为我们旗下各出版物本周阅读量遥遥领先的第一名。

我的看法是：**我们在建立与之配套的问责机制之前，就赋予了编程 Agent 自主权。** 而且这种自主权并非未来，而是现在。Anthropic 在周四发布的递归自我提升报告中指出，Claude 现在编写了该公司合并代码的 80% 以上。上周我曾提出，Token 极大化（tokenmaxxing）时代可能正在结束，Token 自律成了新的技能。至少在成本端我们迎来了工具：Paul Sawers 报道称，[Cursor 降低了价格并增加了企业支出控制](https://thenewstack.io/cursor-pricing-token-billing/)，而就在同一周，[GitHub 转向按 Token 计费](https://thenewstack.io/github-copilot-token-billing/) 导致一些用户的账单飙升。

Token 正在获得支出控制。但信任并不像产品功能那样容易构建，用户也开始收回他们的信任。

## 没人承担责任的一周

相比于一桩丑闻，我更倾向于将 [OpenClaw 与 Cohen](https://thenewstack.io/nanoclaw-openclaw-agent-security/) 的故事看作一次预演。OpenClaw 的全部吸引力在于你可以运行它、分叉它，并在其中使用任何 AI 模型。正是这种开放性，导致一名在职开发者的代码在没人能说清是谁在何时、以何种条款放入的情况下，最终进入了该 Agent 中。Cohen 的回应之所以重要，在于他没有选择做什么：没有提起许可证投诉，没有提交拉取请求，也没有提出和解要求。他看着一个自己在不知情的情况下协助构建的工具，得出没有人对它所吸纳的内容负责的结论，然后离开了。**这个故事之所以迅速传播，是因为成千上万的开发者突然开始好奇 OpenClaw 是否也使用了他们的代码。**

此外还有结构性的问题。Darryl K. Taft 报道了 [Aikido Security 的发现，即被赋予自主管理依赖项权限的 AI 编程 Agent](https://thenewstack.io/aikido-ai-agents-security/) 正在安装无人拥有的软件包。标题——“*这里没有问责制*”——并非夸张，而是对供应链的准确描述。这两篇报道都没有争论 Agent 是否有效。Agent 运行得很好。它们正在准确执行它们被设计要做的事情——在一个人人尚未决定谁来承担后果的生态系统中自主行动。

Linus Torvalds 本周也遇到了同样的问题。B. Cameron Gain 报道了[这位 Linux 创始人在听到“99% 的代码都是 AI 写的”这一说法时的愤怒](https://thenewstack.io/torvalds-ai-programming-productivity/)，该报道被广泛转载。Linus Torvalds 并非反对 AI，他只是对一个抹杀了人类参与的数字做出了反应。他所愤怒的这一趋势是真实的。Anthropic 本周报告称，其工程师交付的代码量是两年前的 8 倍，其中一名员工距离上一次手动编写代码已经过去了五个月。

生成不等于创作（authored）。创作者身份才是创造问责制的基础：需要有人能说出代码的作用、为何存在，以及在出现问题时由谁来修复。现在 AI 拥有了自主权，它急需问责制，而且要快。

# 市场开始重新评估问责制的价值

JetBrains 正在带领 Mellum2 走向 Claude Code 无法涉足的领域。该公司 [开源了其编程模型](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/)。这意味着可以在本地针对企业代码库运行开放权重模型，而无需将代码传出大楼——这些代码通常因为法律、合规或纯粹的常识而被禁止进入他人的云端。JetBrains 没有人声称 Mellum2 的思考能力超越了 Claude。他们销售的是截然不同的东西：一个你可以审查、在自己的硬件上运行并对其负责的模型。这是将“可问责性”作为一项功能，我认为这是明智之举。JetBrains 将自己视为 AI 编程市场中[最后一家独立的主要开发工具公司](https://thenewstack.io/jetbrains-independent-ai-coding/)，而这个市场正越来越多地与模型实验室和超大规模云厂商绑定。

谷歌本周则反其道而行之，[将免费、Pro 和 Ultra 用户从开源的 Gemini CLI 转移](https://thenewstack.io/google-antigravity-cli/) 到闭源的 Antigravity CLI。在 OpenClaw 斩获超过 30 万颗星几天后，[谷歌也推出了 Spark](https://thenewstack.io/gemini-spark-vs-openclaw/)，这是一款闭源 Agent，也是对最受欢迎的开源 Agent 的直接回应。但在 Gavriel Cohen 事件之后，向首批用户推销一款闭源 Agent 可能比谷歌想象的要困难得多。

## Anthropic 递归自我提升报告的真实内容

Anthropic 本周发布了一份重要报告。“[当 AI 自我构建时](https://www.anthropic.com/institute/recursive-self-improvement)”是该公司对其自身自动化情况的报告，其中包含了一些令人震惊的坦白。

根据这份报告，Claude 已经攀登上了研究工作的头两级阶梯：执行任务和设计方法。第三步是选择问题，Claude 也开始在这方面发力。Anthropic 的基准测试指出了一项令人惊讶但还很粗糙的数据：在公司旨在提高模型训练代码运行速度的测试中，Claude 在一年内将速度提升从约 3 倍飙升至约 52 倍。在这项任务中，一名经验丰富的人类需要四到八个小时才能达到 4 倍。当 Anthropic 重放那些偏离方向的真实研究会话时，其最优秀的模型在 11 月有 51% 的时间能比研究人员更好地选择下一步，到 4 月这一比例上升到了 64%。判断力本曾被视为人类持久的优势，现在，这一优势也在被篡食。

**来自内部的引言听起来像是一个互助会**：在顺利的日子里，一名员工承认，“我禁不住会想，我做的任何事情都不重要了”；在糟糕的日子里，“我意识到我根本不知道自己一直在忙些什么”。工作岗位正在实时从“创作者”转变为“审查者”，人类似乎正在承受痛苦。

令人惊讶的是，报告称如果其他实验室也这样做，且能够证实他们确实停下来了，Anthropic 愿意放慢甚至暂停前沿开发。这感觉像是一个空头承诺。核实是无法做到的，而且有数万亿美元的资金正致力于让 AI 以尽可能快的速度发展。

这份报告得出了与本周其他所有事件相同的结论。人类很快就会停止编写代码，转而审查代码，而人类的审查反过来又成为了 AI 自身发展的瓶颈。突然之间，最稀缺的资源不再是算力，而是需要承担责任的人类。

但是，企业还能容忍人类放慢进度多久？

对我来说，在可预见的未来，人类必须保持在闭环中。但这个闭环本身的形态将会发生变化。AI 在审查方面会变得更好。工具和护栏也会得到改进。对进度放缓感到不满的公司也会试图将审查自动化，使用 Agent 来检查 Agent，其中一些尝试会成功（一些则不会）。

无法被自动化取代的部分，是那个对结果负责的人。

这就是隐藏在所有这些动态背后的职业建议。在未来几年胜出的开发者不会是那些用 AI 生成最多代码的人，而是那些签字确认具有真正分量的人。

Agent 首先获得了自主权。而承担责任依然是人类的工作。