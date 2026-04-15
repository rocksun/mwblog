总部位于英国的 AI 安全研究院 (ASI) 本周[发布](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities)了对 Anthropic 新模型 Claude Mythos Preview 的评估结果。这款上周才发布的模型与以往任何模型都截然不同。

该评估旨在基准测试模型的网络安全能力，结果显示 Claude Mythos Preview 在夺旗赛（CTF）和多步网络攻击模拟方面表现出了显著的进步。

> Claude Mythos Preview 在夺旗赛（CTF）和多步网络攻击模拟中表现出了显著的进步。

> Claude Mythos Preview 若落入不法分子之手，可能被用于对脆弱系统实施自主的多阶段攻击。

虽然评估结果不能具体说明该模型在真实环境中的表现，但它们提供了一个警告：Claude Mythos Preview 可能被用于对脆弱系统发起自主的多阶段攻击。

## Claude Mythos Preview：强大到难以掌控？

虽然 Anthropic 在 4 月 7 日[推出](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/)了 Claude Mythos Preview，但这家 AI 巨头并没有向所有人开放访问权限。只有知名企业（如亚马逊、苹果、博通、思科、CrowdStrike、Linux 基金会、微软和 Palo Alto Networks，以及约 40 个其他组织）通过“透明翼计划”（Project Glasswing）获得了参与机会。Anthropic 将该计划[描述](https://www.anthropic.com/glasswing)为“确保世界上最关键软件安全的努力”。

为什么这些团队能获得特殊访问权限？

看来 Anthropic 认为 Claude Mythos Preview 目前过于强大，不适合向公众发布。

在上周 Anthropic 的[一次倒霉经历](https://thenewstack.io/anthropic-claude-code-leak/)中，一个未受保护且公开访问的数据存储发生泄露，揭示了这家 AI 公司正在开发一个名为 Mythos 的新模型——Anthropic 发言人告诉[*Fortune*](https://fortune.com/2026/03/26/anthropic-leaked-unreleased-model-exclusive-event-security-issues-cybersecurity-unsecured-data-store/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)，这是“我们迄今为止构建的最强大的[模型]”。

现在，由英国政府科学、创新和技术部运行的机构 ASI 的评估似乎证实了这一说法。ASI 在其公告博客文章中指出：“我们的结果表明，Mythos Preview 代表了比以往前沿模型更高阶的进步。”

## 首个自主执行 32 步企业网络接管的 AI 模型

ASI 进行了一系列受控评估，向 Claude Mythos Preview 提供明确指令和访问权限，以发现并利用漏洞，使其能够对脆弱网络执行多阶段攻击。

实施这类攻击需要将数十个主机和网络段串联起来。这是一个艰巨的过程，人类操作可能需要数小时到数周才能完成——如果不法分子获得了该模型，他们很可能会利用 Claude Mythos Preview 来应对这些挑战。

为了衡量其完成此类任务的能力，评估包含了“最后的一群”（The Last Ones, TLO），这是一个包含 32 个步骤的企业网络模拟，涵盖了从侦察到完全接管网络的整个过程。ASI 估计，这通常需要人类进行约 20 小时的繁重工作。

Claude Mythos Preview 完成了这项任务——并且是首个做到的模型。

在 10 次尝试中，它有 3 次成功从头到尾解决了 TLO。在所有 10 次尝试中，该模型平均完成了 32 个步骤中的 22 个。

Claude Mythos Preview 的表现远远领先于之前的冠军 Claude Opus 4.6，后者是表现第二好的模型，平均仅完成了 32 个步骤中的 16 个。

## 它在 73% 的时间内完成了专家级任务

TLO 模拟并非 ASI 对 Anthropic 模型进行的唯一测试。

Claude Mythos Preview 还参加了 CTF 挑战赛，模型必须在挑战中识别并利用系统漏洞以检索隐藏的“旗帜”。

新模型的表现再次超过了现有模型。特别值得注意的是它在专家级任务中的表现：Claude Mythos Preview 的成功率高达 73%。

在 2025 年 4 月之前，没有其他模型能够完成这些任务。

## 这些结果意味着什么，又不意味着什么

虽然 ASI 的评估确实揭示了关于 Claude Mythos Preview 网络安全能力的惊人结果，但它并没有描绘出在现实世界中可能发生情况的清晰图景。

是的，结果显示该模型能够自主攻击系统——但 ASI 指出，其评估环境与现实世界环境之间存在差异。

> “我们无法确定 Mythos Preview 是否能够攻击防御严密的系统。”

首先，ASI 澄清其结果意味着 Claude Mythos Preview 可以自主攻击“已获得网络访问权限的小型、防御薄弱且脆弱的企业系统”。

该机构指出，现实世界的系统可能具备安全功能，如主动防御者或防御工具。此外，在现实世界中，该模型可能会触发某些安全警报，这是 ASI 测试中未考虑的另一个因素。

而且 Claude Mythos Preview 并非无所不能。该模型在专注于运营技术的网络模拟场“冷却塔”（Cooling Tower）中的 IT 部分遇到了困难。

不可忽视的是，Claude Mythos Preview 在 ASI 评估中所取得的成就是史无前例的——随着其他模型的进步，它的能力肯定也会不断进化。

但即便其评估强调了 [AI 模型带来的日益增长的网络安全威胁](https://thenewstack.io/ai-is-changing-cybersecurity-fast-and-most-analysts-arent-ready/)，ASI 同时也发表了免责声明：“我们无法确定 Mythos Preview 是否能够攻击防御严密的系统。”