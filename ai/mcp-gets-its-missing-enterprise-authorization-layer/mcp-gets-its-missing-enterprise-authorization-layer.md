<!--
title: MCP 补全了缺失的企业级授权层
cover: https://cdn.thenewstack.io/media/2026/06/d9501232-hj-project-jnkwgfzkamk-unsplash-scaled.jpg
summary: MCP 协议推出企业级授权扩展，支持通过身份提供商（如 Okta）统一管理 AI 代理访问权限。该方案消除了个人手动授权的繁琐，增强了企业的审计、合规管控及安全性。
-->

MCP 协议推出企业级授权扩展，支持通过身份提供商（如 Okta）统一管理 AI 代理访问权限。该方案消除了个人手动授权的繁琐，增强了企业的审计、合规管控及安全性。

> 译自：[MCP gets its missing enterprise authorization layer](https://thenewstack.io/mcp-gets-its-missing-enterprise-authorization-layer/)
> 
> 作者：Frederic Lardinois

几乎每家企业都在尝试采用 [模型上下文协议 (MCP)](https://thenewstack.io/why-the-model-context-protocol-won/) 将其 AI 代理连接到各种工具。但到目前为止，授权这些连接意味着员工必须为每个服务器点击 OAuth 提示。一段时间以来，MCP 项目一直致力于开发 [“企业管理授权”](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization) 扩展，目标是允许企业通过其现有的身份提供商集中控制 MCP 服务器访问权限。

该扩展现已[达到稳定版本](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/)，Anthropic 和 Microsoft 是首批在其客户端（包括 Claude、Claude Code、Claude Cowork 和 Visual Studio Code）中支持该扩展的公司，Okta 则是首个支持该扩展的身份提供商。

MCP 发布后迅速有机增长，但正如往常一样，[最初的规范并非为企业用例设计](https://thenewstack.io/model-context-protocol-roadmap-2026/)。标准 MCP 授权模型是为个人构建的。即使在今天，授权服务器也意味着需要手动连接一个又一个服务，这意味着安全团队无法执行一致的策略或保留单一的审计追踪——而且员工将个人账户连接到工作工具的风险始终存在。

“只需登录一次，所有的 MCP 连接器就会自动设置好，这真的很神奇，” Linear 的工程主管 Tom Moor 在今天的公告中说道。

## 令牌切换

“企业管理授权”使身份提供商成为客户端可以访问哪些服务器的决策者。管理员只需设置一次策略，员工即可使用他们已有的公司身份登录。

与 OAuth 不同，该交换过程无需确认界面。在单点登录期间，客户端从身份提供商处获得一份已签名的断言，该断言既证明了用户身份，也证明了请求访问的应用程序身份。随后，它将该断言呈现给 MCP 服务器自身的授权服务器，后者返回一个作用域访问令牌，客户端随后可以使用该令牌进行调用。

该断言实际上是一个名为 [身份断言 JWT 授权授予 (Identity Assertion JWT Authorization Grant)](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/) 的新兴 OAuth 扩展，简称 ID-JAG，目前是 IETF 的草案。Okta 的品牌版本是 [跨应用访问 (Cross App Access)](https://www.okta.com/identity-101/cross-app-access-securing-ai-agent-and-app-to-app-connections/)。由于 ID-JAG 是一个开放标准，任何身份提供商都可以实现它，尽管目前只有 Okta 发布了支持。

## 将控制权交还给 IT 部门

![](https://cdn.thenewstack.io/media/2026/06/9dbbb5d9-ema-comparison-1024x563.png)

图片来源：MCP

对于 IT 团队来说，这理想地意味着结束不可避免的个人审批蔓延。现在，管理员可以为整个组织（或特定团队，甚至个人）启用服务器，员工及其代理将继承对其的访问权限，并限定在他们已有的组和角色范围内。

控制和审计转移到了身份提供商的控制台。访问决策在每个连接器中留下一条路径，撤销权限的操作流程也与其他一切保持一致，因此禁用用户将同时切断他们的 MCP 访问权限。

由于企业 IT 部门现在控制着此连接，混合使用个人和工作账户——无论是无意还是有意——都变得困难得多。

在实践中，这看起来像 Anthropic 和 Okta 的实现，这意味着 Claude Managed Agents 现在也可以导入到企业目录中，并作为具有人类所有者的身份来对待，同时合规性界面会将休眠代理或配置错误的账户等风险信号反馈给安全团队。

## 身份，而非授权

在今天的公告中，Okta 身份标准总监 Aaron Parecki 将此结果称为使身份提供商成为 MCP 访问的“集中式治理平面”。该治理平面决定了谁连接到什么。不过，它并不决定是否允许执行特定操作。

值得注意的是，该扩展移交的权限范围很广。某个代理是否应被允许在特定时刻对特定资源执行特定操作，是由通常位于代理及其调用的工具之间的[策略引擎和网关](https://thenewstack.io/why-the-model-context-protocol-won/)来管理的决策。

## 未来展望

除了 Anthropic、Okta 和 Microsoft，Asana、Atlassian、Canva、Figma、Granola、Linear 和 Supabase 等公司现在也支持该扩展。Slack 和其他许多公司也将很快加入支持。

Okta 还将把对该协议的原生支持引入其 [Auth0 开发者平台](https://auth0.com/)，让开发者无需从零开始实现即可公开其 MCP 服务器。