<!--
title: 66%的十亿美元级公司任由关键漏洞未修复——AI漏洞挖掘炒作背后被忽视的现实
cover: https://cdn.thenewstack.io/media/2026/10/bed61db0-ivan-vranic-j9-2liz2_rc-unsplash.jpg
summary: Chainguard推出了由AI驱动的安全工具Harness，利用前沿模型查找并修复传统扫描仪漏掉的代码漏洞。同时调查发现，66%的十亿美元级公司会故意让严重漏洞保持未修复状态，凸显出AI漏洞发现与人类修复速度之间的巨大鸿沟。
-->

Chainguard推出了由AI驱动的安全工具Harness，利用前沿模型查找并修复传统扫描仪漏掉的代码漏洞。同时调查发现，66%的十亿美元级公司会故意让严重漏洞保持未修复状态，凸显出AI漏洞发现与人类修复速度之间的巨大鸿沟。

> 译自：[66% of billion-dollar companies leave critical bugs unpatched — the part the AI bug-hunting hype leaves out](https://thenewstack.io/chainguard-mythos-security-harness/)
> 
> 作者：Amanda Caswell

**Chainguard 推出了一个由 AI 驱动的安全防护框架（Security Harness）**，它利用前沿模型（包括 Anthropic 受限制的 Claude Mythos 5.1）来查找并修复传统扫描器遗漏的应用代码中的可利用漏洞。

开发者无需直接访问 Mythos 即可使用 Chainguard Harness，因为 Chainguard 最初构建该工具是为了在 Glasswing 项目中配合该模型进行自身的工作，并且该公司计划随着时间的推移向其他前沿模型开放 Harness，而不是将其绑定到单一模型上。

该公司向 *The New Stack* 表示，Harness 已经在经历过广泛安全扫描的代码库中发现了严重漏洞，其中包括用于关键基础设施的软件。这些发现中首个公之于众的是开源推理引擎 vLLM 中现已修复的一个漏洞，而关键基础设施的漏洞在 Chainguard 与上游维护者协调修复的同时仍处于保密状态。

Harness 于周三宣布推出，它与 Workspaces、Checks 和扩展的 Libraries 保护一同构成了四款产品的发布阵容，将 Chainguard 的业务范围从强化的容器镜像和依赖项扩展到了智能体执行环境和 CI 验证。

## 无需 Glasswing 即可访问 Mythos

Anthropic 已将 Claude Mythos 5.1 的访问权限限制给参与 [Project Glasswing](https://www.anthropic.com/glasswing) 的组织，这使得 Chainguard 能够为原本无法接触该模型的客户运行由 Mythos 驱动的漏洞研究。

Chainguard 告诉 *The New Stack*：“我们最初构建 Chainguard Harness 是为了在 Project Glasswing 中将其用于我们自己的 Claude Mythos，”“Harness 最初在 Claude Mythos 5.1 上运行，但我们的目标是让 Harness 与模型无关，始终与前沿 AI 保持一致。”

Harness 也将通过 Anthropic 的 Claude Marketplace 提供，允许团队使用现有的 Anthropic 支出承诺，而不必争取单独的预算。

> “我们最初构建 Chainguard Harness 是为了在 Project Glasswing 中将其用于我们自己的 Claude Mythos。”

## 验证 vLLM 中的漏洞

Chainguard 的 [来自 Harness 的首次公开披露](https://www.chainguard.dev/unchained/the-first-disclosure-from-our-mythos-harness) 针对的是 vLLM，这是一个许多团队用来提供大语言模型服务的开源引擎。在 v0.31.0 之前的版本中，一个客户端可以强制更改返回给共享同一引擎的其他客户端的输出，并且被篡改的响应看起来像是一个正常的、成功的完成，没有任何内容写入日志，对于任何运行多租户推理的人来说，这是一种特别安静的故障模式。

Chainguard 告诉 *The New Stack*：“我们的防护框架独立发现了该问题并在干净的构建上进行了重现，”并指出该 bug 已在 v0.31.0 中修复，并在公告 GHSA-6cxc-2vcg-w5qc 下进行了跟踪。该公司补充说，“许多其他发现，包括关键基础设施软件中的一些发现，现在正在协调披露，”并且 Chainguard 将在上游修复到位后分享详细信息。

> “许多其他发现，包括关键基础设施软件中的一些发现，现在正在协调披露。”

## 修补前的证明

对于一个依赖 AI 模型来寻找缺陷的工具来说，考虑到 AI 生成的漏洞报告会给维护者带来多少噪音，更大的问题是这些发现是否经得起推敲。“Harness 在通过在全新的、隔离的环境中重现潜在利用程序来计算之前，会先证明漏洞是可利用的，”Chainguard 告诉 *The New Stack*，任何不能一致重现的内容都会被排除在报告之外。

建议的修复措施也要经过相同的概念验证，因此攻击必须针对原始代码成功，并针对修补后的版本失败，然后修复才能推进。然后，Chainguard 工程师会在每个修复和报告到达客户之前对其进行批准和审查，从而在最终发布的产品中保持人类的参与。

> “Harness 在通过在全新的、隔离的环境中重现潜在利用程序来计算之前，会先证明漏洞是可利用的。”

## AI 利用鸿沟

这些产品的发布伴随着 [*The AI Exploit Gap*](https://www.chainguard.dev/unchained) 的发布，这是一份由 Chainguard 委托 Wakefield Research 对九个市场的 1,300 名安全领导者进行的调查。超过一半的人表示，他们的组织有时会明知故犯地让高危或严重漏洞保持未修补状态，在收入达到 10 亿美元或更多的公司中，这一比例达到了 66%，而在收入低于 2.5 亿美元的公司中这一比例为 27%。

Chainguard 的首席信息安全官 [Quincy Castro](https://www.linkedin.com/in/quincy-castro/) 在一份声明中表示：“AI 可以在几分钟内找到并串联缺陷，而修复它们仍然以人类的速度前进，并与产品截止日期和正常运行时间竞争，” “对大多数人来说，更快地修补是不可行的，而且它将消耗越来越多的资源来跟上步伐。”

## 用于智能体的隔离微虚拟机

每个开发者和编码智能体都获得一个硬件隔离的微虚拟机（microVM），其网络策略限制了对内部系统的访问。

凭据保留在智能体环境之外，从而限制了受损智能体或恶意依赖项可以触及的内容。签名的活动日志记录了每个智能体所做的事情，以便团队能够在多个自主会话中保持审计跟踪。

## 智能体循环内部的 CI

Chainguard Checks 允许编码智能体在开发过程中直接运行 CI 检查并在几秒钟内收到签名的结果。智能体可以在打开拉取请求之前运行测试、检查失败并修改代码，从而避免了 CI 队列的管理难度，因为随着 Cognition、Microsoft 和 Augment Code 等供应商[将编码智能体变成共享的团队基础设施](https://thenewstack.io/coding-agents-team-infrastructure/)并并行运行多个会话，CI 队列变得越来越难以管理。

为了避免每次运行都重新构建环境，Checks 使用了预先安装了依赖项的热快照，并在锁文件（lockfile）更改时在后台对其进行刷新。每个工作流程步骤都在从 Chainguard OS 软件包（包括符合 FIPS 标准的工具链）构建的独立硬件隔离微虚拟机中运行。通过 Workspaces，智能体会在验证期间暂停会话，并在上下文中恢复结构化的失败日志。

运行程序（Runner）绝不保存长期凭据。相反，主机端代理将短期凭据注入到出站请求中，而声明性出口策略限制了网络访问，如果微虚拟机尝试未经授权的连接，则可以终止它。成功的运行会产生与执行环境、测试结果和提交相关的签名证明，合并门（merge gates）可以对其进行验证而无需重新运行套件。Checks 现已推出测试版。

## 库锁定突发漏洞

Chainguard Libraries 正在为 Go 和 .NET 添加安全软件包端点，以及针对 JavaScript 和 Go 的 CVE 修复，同时 Java 和 Python 的支持将扩展到涵盖通过 AI 辅助研究发现的新披露的漏洞，包括编码智能体可能已经拉入项目的依赖项中的缺陷。

Harness 的发现将直接反馈到该管道中。当 Harness 在开源软件中发现经过验证的漏洞时，Chainguard 会通过协调披露将其发送出去，构建并审查补丁，并通过 Chainguard Repository 分发修复后的工件。

Chainguard 告诉 *The New Stack*，该公司的 Athena 成员在公开披露之前获得私有的、经过硬化的修补构建，而其他 Libraries 客户则在禁运解除后收到它们，这意味着公司“可以在披露后立即保持免受 AI 发现的漏洞的侵害。”

这些更改建立在 [Chainguard Repository](https://thenewstack.io/chainguard-repository-ai-agents/)（一个针对开源依赖项的策略强制端点）及其[与 Cursor 的合作](https://thenewstack.io/cursor-chainguard-agentic-ai-secure/)的基础之上，允许编码智能体通过 Chainguard 的目录解析软件包，而不是直接从公共注册表中拉取。