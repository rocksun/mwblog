当谷歌上周在其 I/O 大会上宣布将 [Antigravity 重新定位为开发和管理自主 AI 智能体团队的平台](https://thenewstack.io/google-io-antigravity-codemender-ai-agentic/)时，这一宣传迅速呈现出人们熟悉的走向。

对于在过去两个月里关注该领域的人来说，接下来的内容感觉有点像*似曾相识*：对 Antigravity 智能体的一次 API 调用就会启动一个远程 Linux 沙箱，智能体在其中进行推理、调用工具、运行代码并浏览网页。你通过编写 `AGENTS.md` 文件和 `SKILL.md` 文件来扩展它，将其注册为具名智能体，而无需编写任何编排代码。

在过去的两个月里，我已经看到另外两家厂商两次发布了这一产品，这一趋势充分说明了托管智能体运行时变得多么重要——它变得如此重要，以至于已经变得不再重要，成了一个无足轻重的因素，因为许多实验室都在加入这项服务。

## 同样的运行时在六周内发布了三次

Anthropic 于 4 月 8 日将 [Claude 托管智能体 (Claude Managed Agents)](http://anthropic-wants-to-run-your-ai-agents-for-you/) 推向了公开测试。其宣传点在于，对于生产级智能体而言，基础设施——而非智能本身——已经成为了瓶颈，因此 Anthropic 将负责智能体循环、沙箱、状态和凭证范围限定。

紧接着，AWS 于 4 月 22 日预览了 [Bedrock AgentCore](https://thenewstack.io/openai-bedrock-trainium-silicon/) 中的托管框架。该运行时本身在这之前就已经存在，[于 2025 年发布](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/)，但 4 月的更新增加了关键的部分——一个配置优先的框架，它声明了模型、工具和指令，并无需定制的编排代码即可运行循环。

随后，谷歌在 I/O 大会上凭借 Gemini API 中的托管智能体（Managed Agents）再次做了同样的事情。

三家厂商在六周内推出了几乎相同形态的运行时。每一次发布公告都在讲述同一个故事：过去构建生产级智能体意味着要将模型 API、沙箱、编排层和托管拼凑在一起，而托管版本则将所有这些简化为了配置和少量的 API 调用。

当三家公司在六周内独立趋向于同一个产品时，运行时就已经成了基本门槛，而不是选择某个平台而非另一个平台的理由。

## Markdown 文件正成为无人投票表决的配置标准

谷歌的托管智能体是通过 `AGENTS.md` 和 `SKILL.md` 来定义的。[Anthropic 去年将智能体技能 (Agent Skills)](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/) 作为 Markdown 目录进行了发布，而 `SKILL.md` 现在在 Claude Code 和托管智能体中起到了承重支柱的作用。[`AGENTS.md`](https://agents.md/) 是一种开放格式，它诞生于 OpenAI Codex、Cursor、Amp、Jules 和 Factory 的共同努力，目前存在于 60,000 多个开源仓库中，并由 Linux 基金会管理。AWS 也倾向于同样的方向，在其框架旁发布了适用于 Claude Code、Codex、Cursor 和 Kiro 的预建技能。

因此，智能体是在一个纯文本文件中定义的，开发者可以阅读、比对（diff）并将其提交到 Git 中，没有专有的 DSL，也没有可视化构建器来绑架这一定义。同一个文件可以描述 Claude 智能体、Gemini 智能体或 AgentCore 智能体，它们之间的修改极少。虽然模型在基准测试上会继续相互超越，但 Markdown 配置正悄然成为它们之下通用的便携层，就像早在任何人同意之前，Dockerfile 就已经成为容器的构建单元一样。

## 这对当前的开发者选择意味着什么

对于今天选择智能体平台的开发者来说，一个实验室是否拥有托管智能体运行时已不再是决定性因素，因为谷歌、Anthropic 和 AWS 都提供这一功能。决定权转移到了那些枯燥的问题上：你的数据存在哪里、每会话小时的成本是多少、底层运行的是哪个模型，以及当其他地方有更好的新模型出现时，迁移有多困难。

坦率的反驳是，如今 Markdown 的便携性还比较浅。为 Gemini 编写的 `AGENTS.md` 仍然假设了 Gemini 的工具语义，而且将其移动到 Claude 也并非完全行不通。如果各大实验室故意对该格式进行分叉以使迁移变得痛苦，那么该标准在确立之前就会破裂。但其激励方向恰恰相反，因为让智能体最容易定义的厂商也让它们最容易被弃用，而眼下，他们每个人对开发者的渴望都超过了对厂商锁定的渴望。

配置文件是下一场标准之争的决定之地，因此这才是值得关注的焦点。