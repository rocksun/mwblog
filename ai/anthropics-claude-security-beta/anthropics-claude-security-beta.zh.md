周四，Anthropic 将 [Claude Security](https://claude.com/claude-code-security)（Claude Code Web 版中的一项防御性安全工具，可扫描代码库中的漏洞并提供修复建议）结束了封闭预览。

该工具现已面向 Claude Enterprise 客户开启测试（beta），不久后将支持 Team 和 Max 方案的用户（这是一项新变化，因为此前的私测仅限于 Enterprise 和 Team 用户）。

> Claude Security 现已面向 Claude Enterprise 客户开启测试。

Anthropic 在二月份[启动](https://www.anthropic.com/news/claude-code-security)了 Claude Code Security 的私密预览。这发生在 [Claude Mythos 和 Project Glasswing](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) 的发布之前，但在许多方面，我们讨论的是类似的工具和使命。

该公司表示，自发布以来，“数百家组织”已使用 Claude Security 修复了生产代码中的问题，“而现有工具多年来一直忽略了这些问题”。

## Mythos Lite

修复其他工具忽略的生产代码问题一直是 Mythos 的卖点——这也是 Anthropic 尚未公开的原因之一。获得 Mythos 访问权限的组织在[最近几周](https://www.wired.com/story/mozilla-used-anthropics-mythos-to-find-271-bugs-in-firefox/)[如是说](https://thenewstack.io/claude-mythos-preview-simulation/)。

Claude Security 的风险可能会降低，因为作为其核心的 Opus 4.7 [并不像 Mythos 那样聪明](https://thenewstack.io/claude-opus-47-launch/)，但如果你可以轻松地扫描自己的代码库以查找安全漏洞，你也可以扫描任何开源库以寻找潜在的零日攻击（即便 Claude Security 不会为你编写漏洞利用程序）。

> Claude Security 专注于利用并行运行的多个智能体扫描整个代码库。

Claude Security 专注于利用并行运行的多个智能体扫描整个代码库。虽然其他一些工具可能会查找已知问题，但 Claude Security 会步进源代码并检查数据流，以构建更完整的攻击面图景。

如果工具检测到问题，它会运行额外的验证流水线，在通知分析师之前验证问题是否被正确识别。正如 Anthropic 所指出的，为了做到这一点，Claude 会质疑自己的发现，以确保减少误报。

这种工具与 Claude Code 或其他编程智能体结合的承诺在于，发现问题与修复问题之间的差距现在已经变得很小。

Anthropic 在其公告中表示：“用户可以开启一个 Claude Code 会话，在语境中处理补丁，而无需在安全和工程部门之间进行为期数天的反复沟通。”默认情况下，每一项发现都包含一个可供安全部门审查和批准的推荐补丁。

在预览期间，团队增加的新功能包括：计划定期扫描的能力、通过评论忽略任何发现的能力，以及可将扫描结果导入现有工具的 CSV 和 Markdown 导出功能。

## 代码审查（Code Review）又如何？

值得注意的是，Anthropic 还提供了另一种扫描 GitHub 项目整个代码库并查找其中问题的工具：Claude Code Review。Code Review 是 [Claude Code 的多智能体代码审查工具](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/)，它使用智能体扫描代码库中的各种漏洞，包括安全漏洞，但其关注点更广。

当 Code Review 发布时，*The New Stack* [询问了](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/) Anthropic 的 Claude Code 产品主管 Cat Wu 关于 Code Security 与 Code Review 之间的关系。当时，Cat Wu 表示，虽然 Code Review 会标记安全问题，“但它不如 Claude Code Security 那样彻底”。