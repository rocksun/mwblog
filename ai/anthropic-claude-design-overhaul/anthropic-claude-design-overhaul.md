<!--
title: Anthropic重塑Claude Design以优化流程，设计与开发人员对其成效各执一词
cover: https://cdn.thenewstack.io/media/2026/06/d62ce8ec-logan-voss-7melalyaj7a-unsplash-scaled.jpg
summary: Anthropic对Claude Design进行了重大更新，旨在改善设计与开发的交接效率并强化品牌一致性。尽管增加了多项集成与功能，但关于该工具能否真正降低沟通成本及Token消耗效率，业界人士持有不同意见，普遍认为人类在协作中仍占据主导地位。
-->

Anthropic对Claude Design进行了重大更新，旨在改善设计与开发的交接效率并强化品牌一致性。尽管增加了多项集成与功能，但关于该工具能否真正降低沟通成本及Token消耗效率，业界人士持有不同意见，普遍认为人类在协作中仍占据主导地位。

> 译自：[Anthropic overhauled Claude Design to fix the handoff. A designer and an engineer disagree on whether it worked.](https://thenewstack.io/anthropic-claude-design-overhaul/)
> 
> 作者：Meredith Shubel

**Anthropic 本周宣布对 Claude Design 进行重大升级**，这是该公司四月份作为研究预览版发布的设计工具。此次更新旨在通过全新的双向“设计-代码”集成来简化设计与工程团队之间的交接流程，并使用户更容易创建符合品牌指南的设计。

此外，Anthropic 表示听取了用户反馈并[做出改进](https://claude.com/blog/claude-design-stays-on-brand-for-daily-work)，以解决困扰早期用户的 Token 低效问题。同时，它还增加了一个新的编辑器和更多的连接器，以便与 Adobe、Base44、Canva、Gamma、Lovable、Miro、Replit、Vercel 和 Wix 等工具轻松共享。

但 [ABM Industries](https://www.abm.com/) 的首席 AI 产品设计师 [Alfie Martin](https://www.linkedin.com/in/alfieisbored/) 向 *The New Stack* 表示，她认为 Claude Design 并未实质性地减少部门之间繁琐的往复沟通。

尽管她承认该工具可以简化原型设计，但她警告称，Token 效率可能仍然是个问题，而且要求 Claude 自行完成每一个设计更新，默认情况下并不是最高效的工作方式。

“Token 使用成本很高，而 Claude Design 的消耗量很大，”Martin 说，“很多时候，自己手动设计组件或修改细节所花的时间反而更短。”

## Claude Design 与 Claude Code 联系更紧密

这家 AI 公司表示，新版本的 Claude Design 现在与 Claude Code 的协作更加紧密，允许用户在设计和编码之间来回切换，同时保持工作同步。

在单向流程上，开发人员可以在 Claude Code 中运行 `/design-sync` 命令，直接从本地代码库将设计系统拉取到 Claude Design 中，以便设计师能够基于现有组件进行工作。当需要交付时，设计师可以轻松地将其传递给 Claude Code，从而保持工作流的连续性。

在反向流程上，开发人员可以运行 `/design` 命令直接在 Claude Code 中创建、编辑和同步设计项目，无需离开终端。

当被问及 Claude Design 的升级如何影响工作流时，[Henry AI](https://www.henry.ai/) 的全栈软件工程师 [Roman Martynenko](https://www.linkedin.com/in/roman-martynenko-15b91a141/) 向 *The New Stack* 表示，他对“设计-代码”集成持相对乐观态度，称他可能会选择基于终端的工作方式，但也认可 Web 界面对于设计师、项目经理和评审工作的重要性：

“我理想的工作流是：在 Web UI 中进行设计探索，然后在 Claude Code 中结合实际的代码库上下文进行工程级别的交接。”

## 保持品牌一致性变得更加容易

根据 Anthropic 的说法，Claude Design 更新的一大亮点是它“现在可以在跨项目中严格遵守你的设计系统”。换句话说，它将品牌一致性作为了默认设置。

用户可以从 GitHub 仓库、设计文件或原始上传内容中导入一个或多个设计系统。这样，对于 Claude Design 创建的每个新项目，它都会自动继承品牌资产（如字体、颜色、间距），并在展示最终结果之前根据这些指南验证其输出。

Anthropic 的设计师 Nate Parrott 在接受 [*Fast Company*](https://www.fastcompany.com/91561193/anthropics-updated-claude-design-gives-vibe-coders-and-their-design-overlords-more-control) 采访时表示，对于有严格品牌规范的公司来说，这一新功能在维护一致性方面可能会产生实质性的影响，而四月份的版本在这方面表现吃力。

对于那些希望限制不符合品牌规范工作的领导者来说，这可能是一个受欢迎的控制手段。作为 Claude Design 管理员，用户可以设置标准设计系统并禁止其他人进行编辑。

此次更新还带来了新的编辑器，允许通过布局控件进行更精细的调整，使用户能够“拖拽、调整大小和对齐元素”。

## 不再有单独的使用限制

四月份，[*The New Stack* 体验了 Claude Design](https://thenewstack.io/anthropic-claude-design-launch/)，并很快遇到了 Token 问题。仅仅构建一个设计系统和一个新闻网站原型（加上一些微调和解释视频）就足以耗尽每周配额的 50% 以上。

Anthropic 表示它听到了类似的反馈并做出了调整。

此次工具更新取消了单独的使用限制，将 Claude Design 与 Claude Code、聊天功能和 Cowork 纳入了共享池。如果耗尽了使用限额，Claude Design 将无法使用——直到使用量重置或购买更多使用点数。

共享池可能更便于管理 Token 使用，但它是否能真正改变消耗速度还有待观察。

## Anthropic 可能试图将 Claude Design 推向各处，但这并不能解决所有问题

通过增加新的连接器并深化“设计-代码”集成，Anthropic 似乎一心想让 Claude 成为人们工作方式中更重要的一部分。然而，虽然六月份的更新确实使 Claude Design 变得更实用，但它并不能解决所有问题。

理论上，将 Claude Design 连接到设计师和开发人员已经在使用的更多工具，应该会减少团队之间的摩擦，特别是在最终实现与初始设计不匹配时。但正如 Martin 所指出的，设计师与开发人员之间的往复沟通依然存在，且 Token 成本意味着 AI 制作并不总是比人工制作更高效。

归根结底，更快、符合品牌规范的设计和更快捷的交接可能会鼓励更多的实验，但正如 Martin 所言，Anthropic 所建议的“让 Claude 从头到尾构建整个事物”并不是未来。相反，她预计会出现一种混合模型，即像 Claude 这样的工具辅助早期的概念验证，但最终决策权仍掌握在人类手中。