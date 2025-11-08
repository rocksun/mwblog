在面对大量基础设施策略违规积压问题时，组织现在可以向 Pulumi 寻求帮助，因为该公司今天宣布其 Neo AI [平台工程师](https://thenewstack.io/what-makes-the-ideal-platform-engineer/)能够自动识别并大规模修复云基础设施中的[合规问题](https://thenewstack.io/5-best-practices-for-devsecops-teams-to-ensure-compliance/)。

Pulumi Insights 副总裁 Craig Symonds 表示，这项新产品解决了[平台团队](https://thenewstack.io/streamlining-your-platform-teams-workloads/)的一个关键痛点：尽管安全和治理工具擅长检测策略违规，但修复它们仍然是一个手动且耗时的过程。对于追求像 [HITRUST](https://info.hitrustalliance.net/cybersecurity-framework) 或 [FedRAMP](https://www.fedramp.gov/) 等框架的公司来说，这些积压的违规可能超过 100,000 条。

Pulumi 首席执行官兼联合创始人 Joe Duffy 在一份声明中表示：“平台团队告诉我们，他们无法跟上其工具识别出的策略违规数量。检测是必要的，但还不够。Neo 通过理解上下文中的策略违规，生成适当的[基础设施即代码](https://thenewstack.io/introduction-to-infrastructure-as-code/) [IaC] 修复方案，并在团队选择时自动应用它们，从而解决了修复的空白。”

## 从检测到修复

Pulumi 的方法解决了 IDC 分析师 Jim Mercer 所称的[基础设施治理](https://thenewstack.io/governance-as-code-your-infrastructures-missing-guardrail/)中的一个关键转变。

Mercer 在一份声明中表示：“基础设施治理的挑战已从检测转向大规模修复。组织正被策略违规积压所淹没，这些积压的增长速度超过了团队手动处理它们的速度。”

这些新功能将 Pulumi 的[策略即代码](https://thenewstack.io/is-policy-as-code-the-cure-for-multicloud-config-chaos/)框架从预防扩展到主动修复。Symonds 在一次简报中告诉 The New Stack，虽然该平台已经阻止了不合规基础设施的部署，但它现在可以扫描现有基础设施，识别违规行为并使用 AI 生成修复方案。

Neo 分析上下文中的策略违规，生成适当的 IaC 更改，并可以自动应用这些更改（通过可配置的防护措施），或者通过审批工作流进行人工审查。该 AI 代理还内置了安全保障——它不能进行违反组织策略的更改，因为这些防护措施已内置到 Pulumi 的 IaC 引擎本身。

## 实际影响

Symonds 表示，一位客户面临 30,000 条 HITRUST 合规违规，他们估计手动修复将需要一年多的时间，但使用 Neo 的批量修复功能，已在短短几周内解决了其中约 20% 的问题。

[Spear AI](https://spear.ai/) 首席执行官 Michael Hunter 强调了更广泛的合规优势。Hunter 在一份声明中表示：“我们允许审计师访问我们的策略包，因为在代码中理解和证明控制措施比在文档和图表中容易得多。借助 Pulumi 的策略即代码方法，手动审查过程已经消失。我们将 ATO（操作授权）的时间线从一年半缩短到预计三个月内获得批准。”

## 审计、修复、预防

增强的平台遵循三阶段工作流程：

*   **审计：** Pulumi 扫描任何云提供商的基础设施（包括尚未通过 Pulumi 管理的资源），并根据预构建的合规框架（包括 CIS、NIST、PCI DSS、HITRUST、ISO 27001 和 SOC 2）识别策略违规。
*   **修复：** 团队可以批量将违规分配给 Neo。该 AI 代理生成包含必要 IaC 更改的拉取请求。对于尚未在 IaC 控制下的资源，Neo 首先将其导入代码，然后修复违规。
*   **预防：** 一旦清除违规，团队在部署时应用相同的策略，将其集成到 CI/CD 管道中，以在不合规更改到达生产环境之前将其阻止。

## 以开发者为中心的安全

Symonds 表示，Pulumi 的策略不同于传统的安全运营工具，它将合规性直接嵌入到开发者工作流程中。策略违规会出现在工程师日常使用的同一个 IaC 平台中，而不是要求他们上下文切换到单独的安全工具。

他指出：“如果能获得信息，开发者喜欢一开始就做正确的事情。他们讨厌不得不回到三个月前的工作，重新审视并找出如何修复当时就应该修复的安全问题。”

Symonds 表示，这种[左移](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/)方法旨在弥合识别违规的安全团队与必须修复违规的工程团队之间的鸿沟——这是一个摩擦点，已催生了数十亿美元的安全工具投资。

## 可用性

策略功能适用于所有 Pulumi Cloud 客户，包括 Team、Enterprise 和 Business Critical 级别。Neo 的审计扫描和 AI 驱动的修复功能包含在 Enterprise 和 Business Critical 客户套餐中。