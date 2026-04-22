GitHub 宣布暂停其 Copilot 个人版的全新注册，并收紧了现有用户的使用限制。这一举措标志着这款应用最广泛的 AI 编程工具正面临日益增长的压力。

GitHub 母公司 Microsoft 的产品开发副总裁 [Joe Binder](https://www.linkedin.com/in/joe-binder-ba781ab2/) 在[周一发布的博客文章](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/)中写道，随着 AI 辅助开发需求激增，这些调整旨在为当前客户维持“可靠且可预测的体验”。

“智能体工作流从根本上改变了 Copilot 的算力需求，”Binder 表示，“长时间运行的并行会话现在经常消耗远超原始计划结构所能支持的资源。”

> “智能体工作流从根本上改变了 Copilot 的算力需求。”

GitHub 在 [2021 年首次推出了 Copilot](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)，作为一款代码补全工具，它可以在开发者输入时提供代码片段和函数的建议。早期版本专注于编辑器内的行内辅助，无需过多交互即可加速日常编码任务。

在随后的几年里，Copilot 的功能已远超自动补全，[深入嵌入到智能体领域](https://thenewstack.io/github-copilot-wants-to-become-your-peer-programmer/)。GitHub 引入了 [Copilot CLI 等工具](https://thenewstack.io/github-launches-its-coding-agent/)，允许开发者直接在终端发出自然语言指令，并由系统代其执行多步任务。

由于这些变化，用户的使用习惯也发生了改变。开发者不再只是寻求简短的代码建议，而是越来越多地将更复杂的工作交给 Copilot，要求它在更长的会话中进行调试、重构和构建功能。

“随着 Copilot 的智能体能力迅速扩展，智能体正在承担更多工作，越来越多的客户触及了旨在维持服务可靠性的使用限制，”Binder 说道，“如果不采取进一步行动，服务质量对每个人都会下降。”

> “随着 Copilot 的智能体能力迅速扩展，智能体正在承担更多工作，越来越多的客户触及了旨在维持服务可靠性的使用限制。”

展望未来，GitHub 的这一决定将影响包括 Copilot Pro 和 Pro+ 在内的付费层级，以及学生计划，新订阅将暂时关闭。现有用户仍能在不同计划间升级，而 Copilot Free 仍对新注册开放——毕竟，保留一个开放的入口可以为未来输送付费用户。

不仅如此，此次更新还引入了更严格的使用上限，GitHub 调整了不同模型和功能在各计划中的分配。虽然 GitHub 尚未分享具体数字或澄清这些上限相较于之前收紧了多少，但 Pro+ 计划现在提供的使用上限已达到标准 Pro 层级的五倍以上。GitHub 表示，需要更高上限的用户可以升级到 Pro+，且使用上限现在将直接显示在 Visual Studio Code 和 Copilot CLI 等工具中。

此外，该公司还在调整对高级模型的访问权限。Opus 模型不再包含在 Pro 计划中，且[新发布的 Opus 4.7](https://thenewstack.io/claude-opus-47-launch/) 仅限于 Pro+ 层级。GitHub 还确认，作为过渡的一部分，包括 [Opus 4.5](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/) 和 [4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) 在内的早期 Opus 版本正从 Pro+ 中移除。

## 访问控制

值得注意的是，Copilot 仍然是一款订阅制产品，现有用户支付固定的月费。但更严格限制的引入，反映了这些订阅管理方式的转变。

GitHub 并没有在付费层级内提供事实上的开放式访问，而是更加依赖使用控制——跟踪请求并在达到特定阈值后应用限制。这使得 Copilot 更接近一种受使用限制的服务，即便计费方式本身尚未改变。

但有报告称，这种方法可能会进一步演变。Ed Zitron 在 [*Where’s Your Ed At?*](https://www.wheresyoured.at/news-microsoft-to-shift-github-copilot-users-to-token-based-billing-reduce-rate-limits-2/) 中暗示，GitHub 正在探索转向针对个人的按 Token 计费模式，这将使成本与消耗更直接地挂钩。

GitHub 尚未确认任何此类计划，但 Zitron 引用公司文件指出，“运行 GitHub Copilot 的每周成本自年初以来已翻了一番”。

目前，暂停新注册立即减少了进入系统的额外需求流。而通过降低使用上限和更严格的模型访问权限来收紧限制，则控制了现有用户的消耗量。

> “更严格限制的引入反映了这些订阅管理方式的转变。GitHub 并没有在付费层级内提供事实上的开放式访问，而是更加依赖使用控制……”

## 压力倍增

GitHub 的最新举措紧随几天前采取的类似步骤。4 月初，该公司因其免费试用系统“滥用现象显著增加”而[暂停了新的 Copilot Pro 试用](https://github.blog/changelog/2026-04-10-pausing-new-github-copilot-pro-trials/)。虽然那一决定限制了新用户体验产品的方式，但最新的变化影响更深——而且 GitHub 并非孤例。

Anthropic 方面最近几周也[调整了](https://x.com/trq212/status/2037254607001559305)对其 Claude 模型使用限制的应用方式，在高峰时段重新分配会话限制，以便部分用户能[更迅速地触及这些上限](https://thenewstack.io/claude-code-usage-limits/)。

另外，Anthropic 最近还采取行动限制其订阅在 [OpenClaw 等第三方工具](https://thenewstack.io/persistent-ai-agents-compared/)中的使用，通过第三方工具的使用不再包含在订阅内，而是单独计费。

Anthropic 的 Claude Code 负责人 [Boris Cherny](https://www.linkedin.com/in/bcherny/) 4 月早些时候[在 X 上表示](https://x.com/bcherny/status/2040206440556826908?s=20)，这反映了订阅设计方式与当前使用模式之间的不匹配。

“我们一直在努力满足 Claude 需求的增长，而我们的订阅并不是为这些第三方工具的使用模式而构建的，”Cherny 写道，“容量是我们审慎管理的一种资源，我们正在优先考虑使用我们产品和 API 的客户。”

对于这两家公司来说，做法是相似的：限制用户进入系统的途径，并在用户进入后对其使用方式实施更严格的控制。

目前，GitHub 正在通过访问限制和使用上限来缓解这一压力。这种情况是会维持下去，还是会让位给更直接的按需计费模式，将取决于底层需求的演变。