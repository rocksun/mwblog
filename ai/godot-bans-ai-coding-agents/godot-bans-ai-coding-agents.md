<!--
title: “AI贡献令人沮丧”：Godot封禁AI辅助编程以维护其导师模式
cover: https://cdn.thenewstack.io/media/2026/07/0e4bd158-ian-mikraz-v3mr-cgboue-unsplash-scaled.jpg
summary: Godot引擎计划修改贡献政策，限制AI生成的代码。此举旨在减轻维护者负担，并保护其独特的导师文化。社区认为，代码审查不仅是质量把控，更是培养未来维护者的核心途径，而AI缺乏教学互动价值。
-->

Godot引擎计划修改贡献政策，限制AI生成的代码。此举旨在减轻维护者负担，并保护其独特的导师文化。社区认为，代码审查不仅是质量把控，更是培养未来维护者的核心途径，而AI缺乏教学互动价值。

> 译自：["AI contributions are demoralizing": Godot bans coding agents to save its mentoring model](https://thenewstack.io/godot-bans-ai-coding-agents/)
> 
> 作者：Paul Sawers

[Godot Engine](https://godotengine.org/) 是 Unity 等游戏引擎的开源替代品，它正在修改其[贡献政策](https://contributing.godotengine.org/en/latest/pull_requests/pull_request_guidelines.html)，旨在禁止在其代码库中使用大多数 AI 生成的代码。

此举是在[Godot基金会](https://godot.foundation/)（管理该项目的非营利组织）进行了数月的内部讨论后做出的。维护者们表示，他们已无法应对日益增长的合并请求（pull requests）积压，其中许多是由 AI 编写的。

然而，基金会也指出，这种压力不仅仅是因为要管理海量的 AI 生成垃圾内容，更关乎代码审查的本质目的。他们认为，审查代码一直是一项艰苦的工作，但它同时也起到了培训未来维护者的作用；一旦贡献者变成了机器而非真人，这种作用就不复存在了。

> “AI 贡献还带来了一种令人沮丧的额外痛苦。”

正如基金会所言，“AI 贡献还带来了一种令人沮丧的额外痛苦”，因为针对合并请求留下的反馈不会改变模型下一次的表现，而且基金会表示，他们无法信任那些深度依赖 AI 的用户能够足够理解自己的代码，从而根据反馈采取行动。

“审查 PR 已经是一项繁琐的工作，但它是有回报的，因为审查者通常认为他们的努力有助于培养一名新的贡献者（他可能成为未来的维护者/审查者），”基金会[写道](https://godotengine.org/article/contribution-policy-2026/)。“如果针对 PR 的反馈仅仅被机器吸收，而没有用于指导潜在的未来维护者，那么将业余时间花费在 PR 审查上就变得很难证明其合理性。”

> “审查 PR 已经是一项繁琐的工作，但它是有回报的，因为审查者通常认为他们的努力有助于培养一名新的贡献者。”

## 填补空白

据基金会称，自主 AI 智能体和“氛围编程”（vibe-coded）的合并请求已经触发了 Godot GitHub 代码库的自动封禁，尽管这目前尚未写入 Godot 已发布的贡献指南中。这项新更新目前仍在制定中，它将走得更远：通过禁止 AI 生成任何实质性的代码片段来填补这一空白，无论请求是来自机器人，还是来自复制粘贴 AI 输出的人类——即使该人类随后对代码进行了审查和披露。

贡献者仍然可以将 AI 用于狭窄、低风险的任务，如代码补全、正则表达式或查找替换，前提是必须在合并请求中进行披露。除人工编写文本的机器翻译外，与维护者讨论中生成的 AI 文本也是禁止的。

值得注意的是，新的贡献者（定义为合并 PR 数量在三个或以下的任何人）现在必须在提交新功能或大规模重构之前获得明确的批准。

## “贡献者扑克”

Godot 的导师制论点在开源领域并非全然新鲜。早在四月份，[系统编程语言 Zig](https://thenewstack.io/introduction-to-zig-a-potential-heir-to-c/) 就针对 AI 辅助贡献采用了[类似的零容忍政策](https://kristoff.it/blog/contributor-poker-and-ai/)，Zig 软件基金会社区副总裁 [Loris Cro](https://kristoff.it/) 认为，审查合并请求的全部意义在于投资于提交代码的人，而不仅仅是代码本身。他将这种动态称为“贡献者扑克”，并写道“在贡献者扑克中，你押注的是贡献者，而不是他们第一个 PR 的内容”——这个想法他借用了扑克格言“玩的是人，而不是牌”。

Cro 认为，AI 生成的合并请求完全破坏了这种逻辑，因为如果另一端没有人从中学习，维护者的审查时间就无法培养出未来的贡献者。

包括终端模拟器 [Ghostty](https://github.com/ghostty-org/ghostty/pull/10412) 和 C 库 [curl](https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/) 在内的其他项目，也因同样的根本问题限制或关闭了部分贡献渠道，其理由更多地集中在审查负担和虚假错误报告上，而非专门针对导师制。

## 人才管道

Godot 和 Zig 的政策反映了人们对 AI 对软件初级人才管道影响的更广泛担忧，潜在的忧虑大体相同，只是发生在不同的节点上。这种担忧的企业版是关于入门级职位的消失，因为 AI 现在可以完成曾经分配给初级开发人员的任务。

正如 *The New Stack* [在四月份报道的那样](https://thenewstack.io/agentic-ai-junior-developer-crisis/)，微软的 Mark Russinovich 和 Scott Hanselman [警告称](https://cacm.acm.org/opinion/redefining-the-software-engineering-profession-for-ai/)，一旦公司依赖配备 AI 工具的高级工程师，而不是雇用初级开发人员，“该行业的职业人才管道就会崩溃，组织将面临没有下一代经验丰富的工程师的未来。”

> “我们需要采取措施减轻维护者的负担，同时确保我们仍然有渠道指导新贡献者成为未来的维护者。”

同样的问题在开源版本中即使没有导致任何人失业也会出现。初级贡献者仍然存在，并且仍然愿意提交代码——但如果这些代码是由 AI 编写而不是由他们自己编写的，维护者的反馈就没有落脚点，将首次贡献者转化为未来维护者的非正式管道就会停止运作，就像贡献者从未出现过一样。

Godot 基金会表示，预计会随着 AI 工具的变化不断重新审视该政策，并将目前的方法描述为“保守的”。

“我们需要采取措施减轻维护者的负担，同时确保我们仍然有渠道指导新贡献者成为未来的维护者，”基金会表示。