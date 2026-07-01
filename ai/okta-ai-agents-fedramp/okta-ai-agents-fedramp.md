<!--
title: Okta率先将AI智能体治理引入FedRAMP合规边界
cover: https://cdn.thenewstack.io/media/2026/06/f7840ee8-steve-a-johnson-8ugcqzkzcje-unsplash.jpg
summary: Okta推出了AI智能体治理平台，成为首个将AI智能体纳入FedRAMP和HIPAA合规管理边界的身份平台。该方案将AI智能体视为具备唯一身份的一等公民，通过全生命周期管理、最小权限控制及实时监控，有效解决了联邦机构及医疗组织面临的安全、审计和合规挑战。
-->

Okta推出了AI智能体治理平台，成为首个将AI智能体纳入FedRAMP和HIPAA合规管理边界的身份平台。该方案将AI智能体视为具备唯一身份的一等公民，通过全生命周期管理、最小权限控制及实时监控，有效解决了联邦机构及医疗组织面临的安全、审计和合规挑战。

> 译自：[Okta is the first to bring AI agent governance inside FedRAMP boundaries](https://thenewstack.io/okta-ai-agents-fedramp/)
> 
> 作者：Darryl K. Taft

# Okta率先将AI智能体治理引入FedRAMP合规边界

Okta已正式向受FedRAMP和HIPAA监管的环境开放其AI智能体治理平台，并声称这是首个将AI智能体生命周期管理扩展至联邦机构和医疗组织所信任的合规边界内的独立身份平台。

该产品 [Okta for AI Agents – Core](https://www.okta.com/en-au/newsroom/press-releases/okta-for-ai-agents-core-brings-lifecycle-governance-to-regulated-environments/) 将AI智能体提升为与人类和机器工作流并列的一等身份进行管理。这标志着一种转变，即不再将智能体视为静态服务账户或硬编码的API密钥。此次发布正值联邦机构面临近期关于AI创新与安全的行政命令带来的巨大压力，该命令指示各机构部署AI智能体并要求对其进行安全保护。

“给各机构的信息很明确：积极采用AI，但要在推进的同时确保其安全，”Okta联邦业务副总裁 [Amy Johanek](https://www.linkedin.com/in/amyjohanek/) 在一篇 [博客文章](https://www.okta.com/blog/ai/governing-fedramp-ai-agents/) 中写道，“这让身份处于使命的核心地位。”

> “这是目前增长最快，也最难被发现的一类非人类身份 (NHI)。”

Johanek 还写道，AI智能体是“目前增长最快，也最难被发现的一类非人类身份 (NHI)”。她说，任何人都可以启动一个智能体，智能体本身也可以衍生出其他智能体，且每一个智能体都在缺乏可见性的情况下跨应用、API、SaaS工具、MCP服务器和数据系统进行连接。

公司表示，对于那些负有强化系统及防御AI犯罪访问授权的组织而言，一个未经管理的智能体不仅是一个操作缺口，更像是一扇无人看守的门。

> “一个未经管理的智能体不仅是一个操作缺口，更像是一扇无人看守的门。”

Johanek 列出了运行未经治理智能体的机构所面临的四个具体风险：当智能体触及授权边界之外的数据时产生的合规违规；复合型违规风险（即单一被攻破的凭据授予的不仅仅是一个系统的访问权限，而是智能体在人类介入前所能触及的一切）；当智能体作为没有所有者或证据追踪的孤立账户运行时会导致审计失败；以及当延迟成为唯一合规选项时导致AI采用停滞。

此外，该平台的组织架构围绕三个治理问题展开：智能体在哪里运行、它们可以访问哪些资源，以及它们被授权采取哪些行动。Johanek 表示，智能体在组织受监管单元内的 [Okta Universal Directory](https://developer.okta.com/docs/concepts/universal-directory/) 中注册，每个智能体都被分配一个唯一身份和指定的负责人。无论该智能体来自第三方平台还是组织自己的开发人员，在环境内部，每个智能体都成为了一个已知、有归属的一等身份。

该平台用运行时强制执行的、作用域受限的短效令牌取代了静态凭据。授权服务器、第三方应用程序和MCP服务器均应用了最小权限原则。Johanek 指出，该治理层映射了现有的联邦劳动力身份控制机制：访问认证、权限审查、限时权限，以及一个完整的审计日志流，该流可以传输至SIEM平台以满足美国政府问责局的报告要求。

## 该产品还提供了一个“停用开关”

该产品还提供了一个“停用开关”。当智能体偏离其预期使命或意外访问敏感数据时，安全团队拥有一个实时机制，可以在风险升级为重大事件之前将其遏制。

Johanek 表示，她将此产品视为一种持续性手段而非全新的基础设施。各机构已经信任Okta来管理人类身份。[Okta Identity Governance](https://support.okta.com/help/s/article/Identity-Governance-FAQs?language=en_US) 在今年早些时候获得了FedRAMP High授权；她写道，将智能体纳入相同的身份架构是自然的下一步，而不是去构建和维护一个平行系统。

然而，有一个注意事项：Okta for AI Agents – Core 未在美军的Okta单元中获得授权。