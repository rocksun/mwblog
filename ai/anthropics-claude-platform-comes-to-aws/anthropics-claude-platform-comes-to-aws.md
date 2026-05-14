<!--
title: Anthropic 的 Claude Platform 正式登陆 AWS
cover: https://cdn.thenewstack.io/media/2026/05/2f95a795-img_3509-scaled.jpg
summary: Anthropic 与 AWS 合作将 Claude Platform 引入 AWS。开发者现可利用 AWS 凭据访问原生 API 和工具，支持 CloudTrail 审计，但数据处理位于 AWS 安全边界之外。
-->

Anthropic 与 AWS 合作将 Claude Platform 引入 AWS。开发者现可利用 AWS 凭据访问原生 API 和工具，支持 CloudTrail 审计，但数据处理位于 AWS 安全边界之外。

> 译自：[Anthropic’s Claude Platform comes to AWS](https://thenewstack.io/anthropics-claude-platform-comes-to-aws/)
> 
> 作者：Frederic Lardinois

作为 Anthropic 与 AWS 扩展合作的一部分（两家公司已于[4 月份宣布](https://www.anthropic.com/news/anthropic-amazon-compute)），Anthropic 表示将把其开发者工具和 API 集 [Claude Platform](https://platform.claude.com/docs/en/home) 引入 AWS。仅在几周后，AWS 于周一[宣布](https://aws.amazon.com/about-aws/whats-new/2026/05/claude-platform-aws/) [Claude Platform on AWS](https://aws.amazon.com/claude-platform/) 正式上线。

现在，开发者可以直接在 AWS 上使用其 AWS 凭据，访问之前仅能通过 Anthropic 获取的相同 API 和功能。这也使 AWS 成为第一家提供原生 Claude Platform 体验访问权限的云服务提供商。

支持的体验包括消息 API、Claude 托管代理（测试版）、建议工具（测试版）、网页搜索与网页获取、MCP 连接器（测试版）、代理技能（测试版）、代码执行以及文件 API（测试版）。

![](https://cdn.thenewstack.io/media/2026/05/e21f87d7-figure4-claude-code.gif)

有趣的是，底层的 Claude Platform 实际上仍由 Anthropic 运营，而 AWS 特别指出，请求和数据将在“AWS 安全边界之外”进行处理。

正如 AWS 在公告中所写，“这使其非常适合没有特定区域数据驻留要求的团队，并且是对 Amazon Bedrock 上 Claude 模型的补充，因此你可以通过最适合你需求的方式访问 Claude。”换句话说：如果你有数据驻留要求，那么这可能不是你正在寻找的 Claude Platform。

顺便说一下，这与在 Amazon Bedrock 上使用 Claude 不同。在 Bedrock 上，当你通过 AWS 访问 Claude 模型时，所有数据都保留在 AWS 边界内。

AWS 上的定价与[通过 Anthropic 使用 Claude Platform](https://platform.claude.com/docs/en/about-claude/pricing) 的定价相同。

当 Anthropic 和 AWS 首次宣布合作时，Anthropic 特别提到，AWS 上的 Claude Platform 将允许组织在“满足其现有治理和合规性要求”的同时使用 Claude。

不过，与其他 AWS 服务一样，身份验证和计费将由 AWS 处理。Claude Platform 用户在 AWS 上获得的一个额外功能是内置的 AWS CloudTrail 支持，用于监控和审计 AI 使用情况。

整体合作伙伴协议与 Anthropic 最近达成的其他协议一样，将为其近期的算力短缺问题提供一些缓解。Anthropic 承诺在未来 10 年内购买超过 1000 亿美元的 AWS 计算容量，并获得 AWS 的 Trainium 芯片以及高达 5GW 的电力供应。

虽然这不属于协议的一部分，但 Amazon 的开发者[最近也获得了 Claude Code 的访问权限](https://thenewstack.io/amazon-coding-agents-developers/)——此外还有 AWS 自有的 Kiro 编程工具。