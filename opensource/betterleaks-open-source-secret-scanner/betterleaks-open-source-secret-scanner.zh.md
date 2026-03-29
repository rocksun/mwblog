Gitleaks 创建者推出的一款新的开源秘密扫描工具，旨在接替其广泛使用的前身，采用重新设计过的检测方法、更灵活的验证、更快的扫描速度以及对其开发更大的控制权。

这个被谦逊地命名为 “[Betterleaks](https://github.com/betterleaks/betterleaks)” 的项目，已获得 [Aikido](https://www.aikido.dev/) 的赞助，这是一家 [市值十亿美元](https://www.aikido.dev/blog/aikido-funding-series-b) 的安全初创公司，正在支持各种开源工具。

对于不熟悉系统安全复杂性的人来说，秘密是现代软件基础设施的核心，它使服务能够相互认证、访问数据库和调用外部 API。这些凭证——密钥、密码和令牌——在开发过程中经常存储在代码中，无论是在配置文件、脚本还是测试环境中。虽然本意可能是之后将它们移动到更安全的地方，但在早期阶段，通常更容易将其硬编码，从而使其容易被带到不该出现的地方。

当代码共享范围超出预期时，这就会成为一个问题。存储库被公开、日志被导出，或者代码在环境之间复制，包括凭证。一旦暴露，这些字符串就可能被自动扫描代码托管平台和其他公共来源以获取可用凭证的机器人拾取。

当代码共享范围超出预期时，这就会成为一个问题。存储库被公开、日志被导出，或者代码在环境之间复制，包括凭证。一旦暴露，这些字符串就可能被自动扫描代码托管平台和其他公共来源以获取可用凭证的机器人拾取。

落入不法分子之手，这些凭证可能被用于访问云基础设施、启动额外的计算资源、提取数据或实施各种恶意行为。

## 公开的秘密

现在编写的代码量正在增加这种压力。AI 工具可以快速生成大量代码，通常较少进行手动审查，这增加了凭证泄露的可能性。

Gitleaks 的创建者兼其继任者 [Betterleaks](https://betterleaks.com/) 的 [Zach Rice](http://www.linkedin.com/in/zricethezav/) 告诉 *The New Stack*，他认为当开发者在开发过程中过度依赖 AI 助手时，就会发生这种情况。他描述了一种常见模式：开发者在测试时短暂地将真实凭证插入代码中，收到助手的警告，然后通过告诉模型忽略并继续来覆盖该警告。

> “我向你保证，大多数人都在这样做，而不是花时间正确管理他们的秘密。”

“我向你保证，大多数人都在这样做，而不是花时间正确管理他们的秘密，” Rice 说。

这种行为被 AI 辅助开发的节奏和反馈循环所强化。开发者可以快速生成和迭代代码，这种风格通常被称为 [氛围编程](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)，即在不仔细检查的情况下接受并优化输出。

更广泛地说，一些从业者将这种反馈循环描述为 “[AI 精神病](https://www.psychologytoday.com/gb/blog/urban-survival/202507/the-emerging-problem-of-ai-psychosis)”，即与 AI 系统的持续互动可能导致过度依赖和对输出审查的减少。简单来说，AI 正在成为第二大脑，[通常以牺牲用户的第一大脑为代价](https://stackoverflow.blog/2026/03/19/ai-is-becoming-a-second-brain-at-the-expense-of-your-first-one/)。

“如果你处于这种代码被快速生成、即时满足的循环中…… 你会忘记，” Rice 说。“你完全忘记了那些你告诉 AI 代理不必担心的秘密。我敢说，LLM 肯定会增加秘密泄露的风险。”

## 回溯源头

为了理解 Betterleaks 今天的努力目标，有必要回顾到 2018 年，当时 Rice 提交了 Gitleaks 的第一行代码，最初这是一个他在业余时间可以从头开始塑造的副项目。

当时，像以 Python 为中心的 [TruffleHog](https://trufflesecurity.com/trufflehog) 等现有工具已经可以扫描代码中暴露的凭证，但 Rice 看到了一个机会，可以用 Go 重写该方法，添加一个用户可控的配置系统，并使其更快。

“我想要一个可以进行一些创意控制并改进的工具，” Rice 说。

他将最初的想法归功于 [Dylan Ayrey](https://www.linkedin.com/in/dylanayrey/)，TruffleHog 的创建者，后来也是 [Truffle Security](https://trufflesecurity.com/) 的创始人，他是最早将秘密扫描识别为一个独特问题领域的人之一。

“他发现了这个问题，然后我只是想在下班后找个项目来做——一个编写代码的创意出口，” Rice 说。

Rice 公开Gitleaks，随着人们对凭证泄露风险的认识提高，该项目开始受到关注。随着时间的推移，Gitleaks 成为工程团队广泛采用的工具，仅在 GitHub 上就获得了超过 25,000 颗星和 2600 万次下载。

![Gitleaks 拥有 2.5 万颗星且还在增长](https://cdn.thenewstack.io/media/2026/03/b0c96dd6-gitleaksstarhistory-1024x750.png)

***Gitleaks 拥有 2.5 万颗星且还在增长***

包括 GitLab 和 Red Hat 在内的公司将其集成到自己的系统或在内部运行，以扫描存储库和管道中的暴露凭证。事实上，Rice 后来加入 GitLab 担任高级软件工程师，在那里他从事安全工具的开发，尽管 Gitleaks 本身的大部分工作仍然是在业余时间完成的。

2023 年，Rice 加入了 Ayrey 的 Truffle Security 公司，这是一家围绕 TruffleHog 建立的公司，该公司还将包括 [Nosey Parker](https://github.com/praetorian-inc/noseyparker) 在内的其他开源秘密扫描项目整合到一起——旨在 “[统一核心管理](https://www.intelcapital.com/truffle-blogsecrets-everywhere-why-we-co-led-truffle-securitys-series-b/)” 该领域几个最广泛使用的工具。

然而，这一举动改变了 Gitleaks 的背景。在 Truffle，Rice 的重心转向 TruffleHog，Gitleaks 的开发速度减缓。虽然他继续维护它，但该项目已无法以同样的方式推进，大部分支持工作仍在下班后进行。

Rice 在本月的 [Betterleaks 发布帖](https://www.aikido.dev/blog/betterleaks-gitleaks-successor) 中也暗示了这一点，他在其中描述了失去对项目的控制。

> “坦白说，我不再完全控制 Gitleaks 的存储库和名称了，” Rice 指出。“这很糟糕，但它也给了我重新开始的机会。一些……*更好*的东西？”

## 即插即用的替代品

Rice 于二月初加入 Aikido，担任秘密扫描主管，其简单的任务是：构建最好的开源秘密扫描器。

因此，根据 Rice 自己的描述，Betterleaks 是 Gitleaks 的一个即插即用替代品：旧的 CLI 命令仍然有效，旧的配置仍然有效，团队应该能够无需重新配置即可切换。

最明显的变化在于 Betterleaks 处理验证的方式。Betterleaks 没有在 Go 中硬编码该逻辑，而是使用通用表达式语言（[CEL](https://cel.dev/)）来定义检查，以确定候选字符串是否可能是真实的秘密。CEL 被设计为快速、可移植且安全地嵌入到其他应用程序中，这使其非常适合编写验证规则，而无需将扫描器本身变成一堆自定义代码。简而言之，这意味着它为安全团队提供了一种更灵活的方式来定义什么应该被视为有效凭证以及什么应该被忽略。

Rice 也正在尝试替换秘密扫描中一种较不精确的工具。传统扫描器通常依赖于 [熵](https://en.wikipedia.org/wiki/Entropic_security)，这是一种衡量字符串随机程度的指标。Betterleaks 转而使用 Rice 称之为基于 [BPE](https://en.wikipedia.org/wiki/Byte-pair_encoding) 分词的令牌效率扫描。其理念是普通文本和机器凭证在经过分词器时会以不同的方式分解。

其余的改变更多是技术性的，但同样重要。Betterleaks 使用纯 Go 编写，不依赖 [CGO](https://go.dev/wiki/cgo) 或 [Hyperscan](https://www.intel.com/content/www/us/en/developer/articles/technical/introduction-to-hyperscan.html)，因此它不依赖外部 C 库或专用扫描引擎，使其更容易在不同环境中一致运行。它还增加了对双重和三重编码凭证的默认检测，并支持并行化 Git 扫描，以实现更快的存储库扫描。

Betterleaks 的路线图更为宏大。Rice 表示，未来的版本将扫描除 Git 存储库和文件之外的更多来源，添加使用匿名数据的可选基于 LLM 的分类，在提供商公开正确 API 时支持秘密撤销，映射泄露凭证实际可以访问的内容等等。

对 Rice 来说，目标是在推进开发的同时不强迫现有用户切换。尽管他现在的重心是 Betterleaks，但他表示 Gitleaks 对于选择继续使用它的人来说将保持稳定。

“希望这不会对社区造成太大的反弹——我热爱 Gitleaks 社区，我不想分裂它，” Rice 说。“所以如果你想继续使用 Gitleaks，请随意。它很稳定，安全补丁之类的，我会继续做。但如果你想要 Gitleaks 的下一代和进化版本，那就切换到 Betterleaks。”

## “为 AI 代理时代做好准备”

尽管许多开源项目的建立都着眼于催生商业产品，但 Betterleaks 本身不太可能朝这个方向发展。

该项目在 MIT 许可证下开源，Rice 保留所有权，Aikido 充当赞助商而非完全所有者。该公司支持这项工作，作为其更广泛地推动开源安全工具的一部分，其中包括 OpenGrep（Semgrep 的一个分支）、Zen、Intel 和 [Safe Chain](https://www.aikido.dev/blog/introducing-safe-chain) 等项目。

“就像 Aikido 对 OpenGrep 所做的那样，我们致力于为安全社区提供真正优秀的开源项目，” Rice 解释道。“一个强大的开源项目是许多安全产品的支柱。是的，它对其他公司有益，但拥有这些稳定项目对 Aikido 来说也非常有益。”

值得注意的是，Rice 并非独自构建 Betterleaks。来自 Gitleaks 社区的三位长期贡献者——加拿大皇家银行软件开发总监 [Richard Gomez](https://www.linkedin.com/in/r-gomez/)；Red Hat 高级信息安全分析师 [Braxton Plaxco](https://www.linkedin.com/in/bplaxco/)；以及 Amazon 软件工程师 [Ahrav Dutta](https://www.linkedin.com/in/ahrav/)——是共同维护者，他表示这一转变旨在提高稳定性并确保项目不依赖于个人。

> “Betterleaks 为 AI 代理时代做好了准备…… 当代码生成时，你可以检查它是否有秘密——如果发现一个，就会被标记。就是这样。”

这种结构反映了安全工具如何发展的更广泛视角：在开放中构建，并设计得足够灵活，以适应不同的环境——包括 AI 驱动的开发设置。

Rice 表示，AI 代理已经严重依赖命令行工具来导航和分析代码。Betterleaks 的构建也考虑到了这种模式，使其能够像 [Grep](https://en.wikipedia.org/wiki/Grep) 等工具一样融入自动化工作流程。

“Betterleaks 为 AI 代理时代做好了准备，” Rice 说。“AI 代理使用起来真的很容易。当代码生成时，你可以检查它是否有秘密——如果发现一个，就会被标记。就是这样。”

结果是一款安全扫描器，其目标不仅是事后捕获泄露的凭证，还在于成为代码编写循环的一部分——无论是人类还是机器编写的代码。