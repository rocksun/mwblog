Anthropic 为 Claude Code 和 Claude Cowork 发布了更新，为 macOS 桌面带来了计算机使用功能，实现了自主任务执行。周一宣布的这项新功能意味着，你现在可以要求 Claude 在 [Claude Code](http://anthropics-claude-code-comes-to-web-and-mobile/) 或 Claude Cowork 中，使用计算机上的各种应用或工具来执行任务。

在执行任务时，Claude 会首先选择最有效的方法，依赖其连接器（如 Slack 或 Gmail 等服务的[连接器](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)）。当没有可用连接器时，Claude 将接管你的浏览器、鼠标、键盘和屏幕，通过滚动、指向和点击来打开和导航桌面应用，以验证任务完成情况。值得注意的是，这些屏幕交互虽然也能完成任务，但比直接集成要慢。

结合你计算机上的应用、文件和工具，具备计算机使用能力的 Claude 可以执行诸如自动检查早间电子邮件、将分散的指标编译成格式化电子表格以及打开拉取请求等任务。

此功能紧随上周 [Dispatch 发布](http://claude-dispatch-versus-openclaw/)之后，Dispatch 是 Claude Cowork 中的一项新功能，允许你在手机和桌面之间与 Claude 对话。与 Dispatch 结合使用，Claude 新的计算机使用功能意味着你可以直接通过手机分配任务给 Claude，完全脱离屏幕，稍后打开桌面查看完成的工作。

无需设置，但你需要确保计算机处于唤醒并运行状态，并且 Claude 桌面应用已打开。

## 安全性如何？

Anthropic 在其[公告](https://claude.com/blog/dispatch-and-computer-use)中概述了为确保 Claude 合规所设置的防护措施。

首先，助手在访问每个新应用之前会征求你的许可。某些应用默认被列入黑名单（你可以添加更多），并且你保留随时关闭 Claude 的权利。

同时，也设置了防护措施以最大程度地降低风险，例如提示注入。Anthropic 的公告解释道：“当 Claude 使用你的计算机时，我们的系统将自动扫描模型中的激活状态，以检测此类活动。”

此外，Claude 本身也经过训练，旨在避免危险操作，例如资金转账、输入敏感数据、修改或删除文件或捕捉面部图像。所有敏感数据（例如密码、健康信息等）都将自动排除在 [Claude 的记忆](http://claudes-free-plan-can-now-remember-you/)之外。

尽管如此，该公司承认风险依然存在——用户应采取措施保护敏感数据免受 Claude 自主操作的风险。

当该功能启用时，Claude 会截取你计算机的屏幕截图，捕获屏幕上可见的任何信息，无论是敏感的还是非敏感的。在推出此计算机使用功能之前，Anthropic 的支持文档建议关闭任何包含机密信息的文件或应用，例如法律或财务文件。

用户还应拒绝敏感应用（例如银行、医疗）的权限，仔细调整提示以避免意外操作，并优先处理简单任务（例如研究和整理），而不是复杂的多步骤工作流。

Anthropic 在其公告中提醒道：“与 Claude 编写代码或与文本交互的能力相比，计算机使用功能仍处于早期阶段”，并承认该功能“并非总能完美运行”，有时“需要第二次尝试”。

那么，为何是现在？

Claude 和 Cowork 中的计算机使用功能正处于研究预览阶段，目前仅适用于 Claude Pro 和 Claude Max 订阅者（不包括 Team 或 Enterprise 计划），且仅限 macOS。

Anthropic 在其公告中解释了此次发布的原因：“我们提前分享它，是因为我们想了解它在哪些方面有效，哪些方面不足。”

当被问及将如何随着不断演变的威胁来持续改进安全性时，Anthropic 告诉 *The New Stack*，它旨在利用实际使用情况和反馈来进一步完善其安全防护措施。这就是为什么该功能正在逐步推出，并计划在公司了解更多功能使用方式后加强其安全性。