Anthropic 在周三[发布了](https://claude.com/blog/claude-managed-agents) [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) 的公开测试版，这是一项新服务，允许企业在其平台上快速构建和部署云端智能体（agents）。

在此之前，Anthropic 主要专注于为用户提供构建智能体的模型，但除了 Claude Code 和 Cowork 之外，它尚未提供运行这些智能体的自有基础设施。正如其名，通过 Claude Managed Agents，用户可以定义他们想要运行的智能体——通过自然语言描述或 YAML 文件——定义其护栏（guardrails），并在 Anthropic 的平台上运行它们，所有的基础设施都被抽象化了。

正如 Anthropic 团队在今天的公告中所指出的，“发布一个生产级智能体需要沙箱代码执行、检查点设置、凭证管理、限定范围的权限以及端到端追踪。在用户看到任何东西之前，这需要数月的底层架构工作。”

团队承诺，Managed Agents 将这一过程缩短了 10 倍，部分原因是该服务提供了一整套用于智能体沙箱化、处理身份验证和工具执行的工具。

![](https://cdn.thenewstack.io/media/2026/04/00ee9869-claude-managed-agents-demo-video.gif)

该公司表示，智能体可以运行数小时，并且与第三方服务的连接通过 [MCP 服务器](https://platform.claude.com/docs/en/managed-agents/mcp-connector)处理。

然而，Managed Agents 的某些功能仍处于有限的研究预览阶段。这些功能包括高级记忆工具、多智能体编排，以及智能体自我评估和迭代直到达到预定结果的能力。

Anthropic 还强调，它正在提供治理工具，这是阻碍许多企业在生产环境中采用智能体的一个因素。该公司表示，该平台将处理限定范围的权限、身份管理和执行跟踪。

![](https://cdn.thenewstack.io/media/2026/04/53795e13-69d53a1b570fa207204f0111_claude-blog-managed-agents-diagram-noborder-1024x1024.png)

*图片来源：Anthropic。*

新服务的[定价](https://platform.claude.com/docs/en/about-claude/pricing)非常直观。用户根据 Anthropic 的标准 API 定价支付模型的 Token 使用费，此外，对于活动运行时间（以毫秒计算），每会话小时额外支付 0.08 美元。空闲时间——当智能体等待您的下一个输入或工具时——不计入此运行时间。当智能体执行网络搜索时，Anthropic 每 1,000 次搜索额外收费 10 美元。

显而易见，这是 Anthropic 的一个重要里程碑。通过 Claude Code，它围绕其模型和编码套件构建了一个庞大的开发者生态系统，但现在它正在进入智能体基础设施层。这是一个非常不同的市场，但与任何竞争对手相比，Anthropic 都更加关注企业用户。Managed Agents 解决了许多企业在尝试将智能体投入生产时面临的明显痛点，无论是用于内部使用还是交付给客户。