[OpenClaw](https://openclaw.ai/)、[NanoClaw](https://nanoclaw.net/) 以及当前备受追捧的各种个人AI代理，都能快速消耗数百万AI令牌。它们之所以变得经济实惠，是因为Anthropic或OpenAI每月20美元的固定费率最基础的计划，允许你使用它们的编程代理，并提供相对慷慨的令牌限制，所有这些都无需使用按需付费的API密钥。

然而，Anthropic最近[更新了其Claude Code文档](https://code.claude.com/docs/en/legal-and-compliance#authentication-and-credential-use)，指出在“任何其他产品、工具或服务”中使用这些账户的OAuth令牌将“违反其服务条款”。然而，这正是NanoClaw等产品运行其入职流程的方式。

更新还指出，正在构建“与Claude功能交互的产品或服务”的开发者应该使用API密钥。“Anthropic不允许第三方开发者提供Claude.ai登录，也不允许代表其用户通过免费、专业或最大计划的凭据路由请求，”该文档现在写道。

可以理解，这在[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1r88vbs/claude_code_policy_clear_up_from_anthropic/)、[X/Twitter](https://x.com/robzolkos/status/2024125323755884919) 和其他论坛的Claude社区中引起了不小的轰动。为这一切提供支持的 [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) 不仅让人们能够使用这些新的个人代理，还能使用各种编程工具。事实上，Agent SDK旨在让用户以Claude Code为核心构建AI代理。

虽然可以理解Anthropic不希望开发者实质上“钻系统空子”，在不支付API费用的情况下构建完全依赖专业版和最大版计划的服务，但此举似乎阻碍了许多个人使用场景以及目前推动整个行业前进的许多实验。

但请不要担心，Anthropic认为这一切都只是一个误解。

*The New Stack* 向Anthropic的公关团队寻求澄清，并被指引到[X上的一篇帖子](https://x.com/trq212/status/2024212378402095389)，其中在Anthropic从事Claude Code工作的Thariq Shihipar写道：“抱歉，这是一次文档清理工作，导致了一些混淆。您使用Agent SDK和MAX订阅的方式没有改变！”

此外，他后来澄清说，Anthropic希望鼓励实验，但“如果您正在Agent SDK之上构建业务，则应该使用API密钥。”

当我们向该公司进一步询问（以及用户是否应该担心Anthropic会取消他们的账户，例如如果他们使用OpenClaw）时，我们收到了以下声明，这与Shihipar的措辞相呼应：“客户使用其账户的方式没有任何改变，Anthropic不会取消账户。此次更新是对我们文档中现有语言的澄清，以使其在各页面之间保持一致。”

![](https://cdn.thenewstack.io/media/2026/02/9592537d-screenshot-2026-02-18-at-1.48.13-pm.png)

雪上加霜的是，Anthropic要求Clawdbot的创始人Peter Steinberger更改其项目的名称。因此，“Claudebot”现在被称为OpenClaw。这可能出于法律必要性，但这个过程并没有让Anthropic赢得社区的好感。Peter Steinberger现在已加入OpenAI。几周前，Anthropic还[禁止OpenCode等开发者工具](https://gist.github.com/R44VC0RP/bd391f6a23185c0fed6c6b5fb2bac50e)使用其OAuth系统。

对于许多用户来说，长期以来都觉得这些订阅服务，无论提供商是谁，都得到了那些使用更昂贵的API的人的补贴。许多用户预计“好得不像真的”AI服务时代即将结束，这可能不足为奇，许多人将此政策更新视为未来趋势的信号。