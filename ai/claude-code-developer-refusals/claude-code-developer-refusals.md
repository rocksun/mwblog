<!--
title: 开发者正在故意降级他们的AI——而且这确实有效
cover: https://cdn.thenewstack.io/media/2026/11/2b66602e-risky-ming-2k9rzbhzaem-unsplash-scaled.jpg
summary: Anthropic为防止IP侵权更新了Claude Code的限制，导致其拒绝处理多项合法的逆向工程和游戏开发任务。许多开发者被迫切换到旧版模型以完成工作，这暴露出托管式智能体存在的不确定性风险。
-->

Anthropic为防止IP侵权更新了Claude Code的限制，导致其拒绝处理多项合法的逆向工程和游戏开发任务。许多开发者被迫切换到旧版模型以完成工作，这暴露出托管式智能体存在的不确定性风险。

> 译自：[Developers are downgrading their AI on purpose — and it's working](https://thenewstack.io/claude-code-developer-refusals/)
> 
> 作者：Amanda Caswell

**Anthropic 已确认其在 Claude Code 中添加了新的限制**，以防止用户重新创建现有的电子游戏。但开发者表示，Claude Opus 5.5 还拒绝了它以前能够处理的逆向工程和软件分析任务，这引发了人们对 Anthropic 可能还修改了其他内容的质疑。

对于一些开发者来说，这些拒绝已经影响了他们的工作。一位开发者[表示，付费客户项目已经停滞](https://github.com/anthropics/claude-code/issues/106167)，因为 Claude Code 无法用于现有的游戏，[而其他人则表示该模型拒绝](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-confirms-new-claude-code-limits-to-prevent-game-cloning-users-report-opus-5-5-is-also-actively-blocking-reverse-engineering-tasks)分析软件。至少有一位开发者通过切换到较旧的 Claude 模型恢复了工作。

周五，Anthropic 技术团队成员 [Addy Osmani](https://www.linkedin.com/in/addyosmani/) [在 X 上](https://x.com/addyosmani/status/2116213240363729013) 确认，该公司故意修改了 Claude Code 的指令。

> “我们在 Opus 5.5 上的 Claude Code 提示词中添加了两句话，以引导它不要重新创建某人特定的游戏，因为使用 Claude 侵犯知识产权违反了我们的使用政策。”

Osmani 写道：“我们在 Opus 5.5 上的 Claude Code 提示词中添加了两句话，以引导它不要重新创建某人特定的游戏，因为使用 Claude 侵犯知识产权违反了我们的使用政策。”

他澄清说，开发者应该仍然能够创建原创游戏、在既定类型内进行构建以及使用他们自己的设计和素材。

他补充说：“我们将继续迭代，以确保我们达到正确的平衡，”并邀请开发者在 Claude 拒绝涉及他们自己创作的工作时联系他。

Anthropic 尚未公开确认逆向工程被拒绝是否与新指令或单独的网络安全限制有关。

## 逆向工程碰壁

投诉不仅限于游戏开发。开发者表示，Opus 5.5 正在拒绝以前可以正常工作的软件分析任务。美国群联电子（Phison Electronics USA）的技术作家 [Jarred Walton](https://www.linkedin.com/in/jarred-walton-6290a72/) 在[测试他正在开发的软件时遇到了拒绝](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-confirms-new-claude-code-limits-to-prevent-game-cloning-users-report-opus-5-5-is-also-actively-blocking-reverse-engineering-tasks)，但切换到 Opus 4.8 使他能够继续工作。

虽然 Anthropic 试图在不阻碍合法开发工作的情况下防止滥用，但随着 Claude Code 突然拒绝它曾经处理过的工作，且对这种变化几乎没有解释，开发者们发现自己无法完成任务。

> 随着 Claude Code 突然拒绝它曾经处理过的工作，且对这种变化几乎没有解释，开发者们发现自己无法完成任务。

## 付费客户工作停滞

10 月 30 日，Conflict Simulations LLC 创始人兼首席执行官 [Ray Weiss](https://www.linkedin.com/in/ray-weiss-992777125/) [在 GitHub 上报告称](https://github.com/anthropics/claude-code/issues/106167)，Claude Code 已停止处理它支持了数月的付费客户项目。

他的公司为拥有实体游戏的客户创建桌面战棋游戏的自定义数字版本。Weiss 表示，这些项目使用原始代码和客户提供的材料，但 Claude Code 现在由于对重新创建现有游戏的限制而拒绝继续这项工作。

Weiss 希望 Anthropic 区分侵权和委托开发，提供验证流程，并记录对 Claude Code 指令的重大更改。

## 托管智能体的风险

该投诉突显了托管式编码智能体的一个更大问题。Anthropic 可以在开发者不更改其代码、工具或提示的情况下更改 Claude Code 的允许行为。一天前还可行的工作可能会在第二天突然被阻止。

> 一天前还可行的工作可能会在第二天突然被阻止。

10 月 6 日，Anthropic [扩展了其网络安全验证计划](https://www.anthropic.com/news/cyber-verification-program)，在承认其安全防护措施可能会阻碍合法的网络安全工作后，允许经过审查的安全研究人员访问较少限制的环境。

目前仍不清楚这些安全防护措施是否是最近遭到拒绝的原因，特别是考虑到开发者表示他们可以使用旧的 Claude 模型完成一些相同的任务。

## 开发者只能靠猜测

逆向工程除了安全研究之外还有合法的用途。10 月，红帽（Red Hat）工程总监 [Christian Schaller](https://www.linkedin.com/in/cschalle/) 使用 Claude Code 来帮助[逆向工程扫描仪驱动程序](https://thenewstack.io/claude-code-linux-driver/)，为制造商更改了芯片组的硬件带来 Linux 支持。

Anthropic 已经承认其游戏克隆限制需要完善，但开发者仍然不知道为什么 Claude Code 会拒绝一些以前可以正常工作的逆向工程任务，或者接下来哪些工作流程可能会受到影响。

*The New Stack* 就拒绝是否与新的游戏克隆限制或其他安全防护措施有关一事联系了 Anthropic。该公司在发表前未予回应。