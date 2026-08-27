**Shopify CEO [Tobi Lütke](https://www.linkedin.com/in/tobiaslutke/) 正在考虑禁止**公司内部使用 Claude Code，但并非因为他认为 Anthropic 的编程代理不够出色。他说，问题在于一个 Markdown 文件。

“我正在考虑禁止在 Shopify 使用 Claude Code，直到他们改变主意并阅读 AGENTS.md 和 .agents/skills 等文件，” Lütke 周二在 [X 上](https://x.com/tobi/status/2092259436538495186)发文称。

> “我正在考虑禁止在 Shopify 使用 Claude Code，直到他们改变主意并阅读 AGENTS.md 和 .agents/skills 等文件。”

虽然这听起来像是对 AI 编程工具如何配置的小分歧，但在 Shopify 这样规模的公司，即使是微小的差异也可能迅速演变成更大的问题。

Shopify 有数千名开发者在一个巨大的单一存储库（monorepo）中工作，由于他们并未统一使用相同的 AI 编程工具，每个代理都需要为它正在处理的代码库部分拾取正确的指令。如果一个编程代理无法像其他代理那样获取相同的指令，开发者最终可能会面临 [在不同规则下运行的代理](https://thenewstack.io/go-language-ai-agents/) 的情况。

“Agents 和 Claude 文件会递归应用到树结构中，” Lütke 在 [后续帖子](https://x.com/tobi/status/2092308116524138711) 中写道。“在一个拥有数千名 [开发者] 的单一存储库中，确实会发生某个目录缺失这两个文件中的一个的情况，这意味着一部分开发者是在‘前额叶切除’状态下工作。”

Shopify 已经构建了自动化工具来规避这种差异，但 Lütke 的核心反对意见是其工程师本不应该处理这些问题。

“我们用自动化解决了这个问题，但这是一种不该支付的愚蠢复杂性税，” 他写道。

> “我们用自动化解决了这个问题，但这是一种不该支付的愚蠢复杂性税。”

## 指示 AI 代理如何工作的那些文件

现在编程代理的能力越来越强，工程团队需要提供代码库持久化指令的方法，这就是 AGENTS.md 和 CLAUDE.md 等文件发挥作用的地方。

开发者可以将构建命令、测试要求和编码约定等直接放入存储库的文件中，这样代理在工作时就可以获取这些信息，而不必每次都被告知。问题在于，编程工具尚未统一使用相同的标准。

OpenAI 在 2025 年 8 月推出了 AGENTS.md，旨在为编程代理提供项目特定的指令；到 12 月，OpenAI 表示它已被超过 60,000 个开源项目和代理框架使用，并得到了包括 Codex、Cursor、Gemini CLI、GitHub Copilot、Jules 和 VS Code 等工具的支持。OpenAI 随后将该格式移交给了 Linux 基金会旗下的 Agentic AI Foundation。

> “Agents 和 Claude 文件会递归应用到树结构中……某个目录缺失这两个文件中的一个，这意味着一部分开发者是在‘前额叶切除’状态下工作。”

## AGENTS.md 和 CLAUDE.md 的分歧点

然而，Claude Code 的处理方式有所不同。它使用 CLAUDE.md 来处理项目指令，并可以在工作时从存储库的不同部分拾取这些文件。它没有原生读取 AGENTS.md，这是开发者一直要求 Anthropic 做出改变的地方。

Anthropic 确实提供了一些变通方法，包括从 CLAUDE.md 文件导入 AGENTS.md 或使用符号链接，但在大型存储库中，团队仍然必须确保这些指令在它们出现的所有地方保持同步。

## 平台团队承担成本

在大型代码库中，这些指令可以存在于整个目录树中，根据代理所处理的内容为其提供不同的指导。Claude Code 使用 CLAUDE.md 来实现这一点，在遍历存储库时拾取相关的指令文件。

这也是为什么 Lütke 的例子如此重要的原因。如果一个目录包含供读取 AGENTS.md 的工具使用的指令，但 Claude Code 无法获得等效的指令，那么使用 Claude 的开发者最终可能会在缺乏相同上下文的情况下工作。

[开发者已经要求 Anthropic 支持 AGENTS.md 近一年了](https://github.com/anthropics/claude-code/issues/7060)。最近的请求继续推动原生支持，包括 [一个专注于递归发现 AGENTS.md 的请求](https://github.com/anthropics/claude-code/issues/69151)，Anthropic 已将其关闭为“未计划”。

Shopify 并非个例。一项 [2026 年对 2,926 个 GitHub 存储库的研究](https://arxiv.org/abs/2602.14690) 发现，上下文文件现在是开发者为编程代理提供指令的最常见方式，且 AGENTS.md 已经在多种不同工具中被使用。

Shopify 已经构建了自动化工具来处理这个问题，Lütke 明确指出了这一点，并强调随着公司在同一个存储库中引入更多的编程代理，让这些工具保持同步已成为平台团队的另一项工作。