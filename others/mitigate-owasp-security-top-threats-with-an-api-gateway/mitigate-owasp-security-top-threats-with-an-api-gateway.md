<!--
title: 通过API网关缓解OWASP十大安全威胁
cover: https://cdn.thenewstack.io/media/2023/11/31e89923-security-1024x723.jpg
-->

API十大安全威胁解析及API网关的安全防护。

> 译自 [Mitigate OWASP Security Top Threats with an API Gateway](https://thenewstack.io/mitigate-owasp-security-top-threats-with-an-api-gateway/)，作者 David Sudia 是 Ambassador Labs 的高级开发者倡导者，该公司是 Emissary-Ingress 和 Telepresence 的创建者。他之前是 DevOps/平台工程师和 CNCF 最终用户。Dave 热衷于通过确保开发者做出最好的工作来支持其他开发者......

OWASP 每四年会发布一次 [OWASP Top 10](https://owasp.org/www-project-top-ten/)，其中描述了最关键的安全风险。这个列表是组织了解和缓解常见 Web 漏洞的起点。

自 2019 年以来，该组织还制定了一个针对 API 安全威胁的前 10 名，以提高人们对 API 安全的认识，并提供解决最紧迫威胁的指导。这些映射了一般安全威胁到 API 面临的具体问题。

随着越来越多的应用程序和平台提供 API 以方便集成、开发和自动化，与这些 API 关联的安全问题也在相应地上升。 API 常常扮演应用程序数据、业务逻辑和敏感功能的网关，这使得它们成为攻击者的诱人目标。如果未得到适当安全保护，它们可能被利用来泄露敏感信息、绕过安全控制或者甚至操纵基础系统。

OWASP API 安全项目在 7 月发布了新的前 [10 大 API 安全威胁](https://owasp.org/API-Security/editions/2023/en/0x00-header/)。让我们回顾这个列表的要点，以及 API 网关工具如何帮助减少这些漏洞。

## 最大的安全威胁：授权

损坏的[授权已经成为应用程序正在承受的最大 API 安全威胁](https://thenewstack.io/security-at-the-edge-authentication-and-authorization-for-apis/)。2023 年名单中前 10 大 API 安全威胁中有 3 个与授权相关:

- [损坏的对象级授权](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)：对象级授权确保用户只访问被允许的对象。接收对象 ID 的 API 必须验证用户对这些对象的操作权限。不足的检查可能导致未经授权的数据更改。
- [损坏的对象属性级授权](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)：API 常常暴露所有对象属性，特别是 REST API。检查 API 响应可以揭示敏感信息，而模糊测试可以检测隐藏属性。未经授权的属性访问可能导致数据泄露或账户被接管。
- [损坏的函数级授权](https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/)：攻击者通过匿名或普通用户身份访问不应访问的 API 端点来利用损坏的函数级授权。复杂的角色和用户层次结构使适当的授权检查变得艰巨。然而，API 的结构化特性使缺陷更容易被发现。这些漏洞允许未经授权的函数访问，冒着数据泄露或服务中断的风险。

## 永恒的安全威胁：认证

尽管随着服务提供商的认证服务向开发者开放，[损坏的认证](https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/)仍然是 API 安全威胁名单上的第 2 名。认证是验证试图访问您的 API 的用户或系统的身份。由于这些是您服务的“前门”，它们是攻击者的首要目标。

错误发生在开发人员尝试构建自己的认证系统时。对认证限制及其复杂实现的误解使漏洞很常见。攻击者可以劫持用户账户、访问个人数据并在真实用户无法区分的情况下执行敏感操作。

为了解决这个威胁，您会想要通过 API 网关为应用程序提供可靠的认证。使用使用 JSON Web 令牌(JWT)、OAuth 和其他[基于令牌的认证系统](https://roadmap.sh/guides/token-authentication)等认证机制的网关，以确保安全的用户体验。这些基于令牌的方法提供了一种可扩展和安全的方法来确认用户身份，而不需要不断交换敏感凭据。

无论您选择哪个 API 网关，请确保它可以根据经过身份验证的用户执行速率限制。这是一个关键功能，因为它可以通过限制用户可以提出的请求的频率来防止潜在的滥用。例如，通过将速率限制与特定的经过身份验证的配置文件相关联，Edge Stack 等选项可以确保系统资源不会过载，并抑制恶意尝试淹没系统的行为。这种特定于用户的速率限制对于具有不同用户角色的应用程序特别关键，它确保特权用户获得优先访问的同时保持系统的完整性和性能。

## 日益增长的安全威胁：不受限制的 API 访问

不受限制的 API 访问和增加暴露的 API(无适当控制)可能导致各种安全问题。

前 10 大 API 安全威胁中有 2 个与不受限制的访问相关:

- [不受限制的资源消耗](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)与分布式拒绝服务(DDoS)攻击相关。攻击者发起并发请求，过载流量并影响 API 响应性。如果 API 缺乏针对客户端交互或资源使用的限制，它们会不堪重负。精心设计的 API 请求，包括特定参数或批量操作，可以定位漏洞，响应指标可以进一步突出潜在的弱点。
- [不受限制地访问敏感业务流程](https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/)是利用 API 所依赖的业务模型，定位和破坏或利用敏感业务流程。一个例子是“程序化倒卖”，攻击者编写代码来操纵票务销售商的 API，在票务开售时购买许多票务以转售。与列表中的其他安全威胁不同，这不是一个技术威胁，而是一个业务威胁，妨碍真正的用户购买产品。

找到一个提供速率限制的工具，这是防止恶意或意外滥用系统资源的关键措施。通过这个，您可以确保系统服务不会被大量请求压垮。

根据特定端点或提出请求的用户类型，可以应用不同的速率限制，允许定制访问控制。这种细粒度的方法可以确保关键端点或特权用户获得优先访问，同时维持系统完整性和最佳的用户体验。

下面是一个例子，说明您的 API 网关工具可能如何应对 DDoS 攻击。当这种情况发生时，API 网关可以通过两种机制主动应对这些攻击：

- 开发人员可以设置请求阈值来检测潜在的 DDoS 攻击并缓解这些问题。
- 它采用缓存机制，在正常使用和遭到攻击期间减少后端负载，确保更快的响应并节省宝贵资源。

## 无处不在的安全威胁：数据验证

数据验证和清理在维持所处理信息的真实性和安全性方面发挥关键作用。

来自[服务器端请求伪造](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/)(SSRF)的 API 威胁是巨大的。这发生在 API 获取外部资源时没有验证用户提供的 URL。这使攻击者可以强制应用程序向意外目标发送定制请求，绕过防火墙或 VPN。OWASP 清楚地指出:

“更危险——现代技术如云提供商、Kubernetes 和 Docker 通过 HTTP 在可预测的、众所周知的路径上暴露管理和控制渠道。这些渠道很容易成为 SSRF 攻击的目标。”

完全消除 SSRF 风险具有挑战性。选择保护措施需要在业务风险与运营需求之间取得平衡。选择一个提供强大功能的网关，可以有效验证输入和输出数据，并识别和阻止恶意内容。

在网络威胁横行的时代，在系统被入侵之前过滤掉潜在有害数据的机制无价之宝。这种主动方法可以保护应用程序并确保更安全的用户体验。

## 外部安全威胁：第三方风险

依赖第三方软件或服务可能会引入未知的漏洞。[在不安全使用 API 时](https://owasp.org/API-Security/editions/2023/en/0xaa-unsafe-consumption-of-apis/)，开发人员不会验证他们正在将哪些端点集成到他们的应用程序中。这些第三方 API 可能缺乏保护我们上述威胁的安全配置，例如 TLS、认证和验证。

将 API 网关日志和数据[集成到例行安全评估中](https://thenewstack.io/5-best-practices-for-securing-your-api-gateway/)可以提供对系统当前状态和潜在弱点的整体视图。这些日志提供了关于流量模式、用户交互和潜在红旗的宝贵见解。

与此同时，应规定对 API 及其关联环境进行定期漏洞评估。这些评估深入研究基础架构，识别潜在风险和未打补丁的漏洞，并确保系统能够抵御不断发展的威胁。定期审核和漏洞评估可以建立一个强大的防线，不断加强和更新系统的安全态势。

## 被忽视的安全威胁：错误配置

[错误配置的系统](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/)通常会被忽视，可能会无意中暴露敏感数据或功能。攻击者侦察暴露的端点、缺乏安全补丁、缺乏标准(如 TLS 和 CORS)以及不安全的错误消息。正确的配置很重要，您的 API 网关工具应该承担这一责任:

1. **加密和数据保护**：例如，Edge Stack API 网关在所有 API 端点上实施 TLS，以确保传输中的数据免受拦截或窃听。它还确保静态数据被加密，为保护敏感信息添加了一个额外的安全层，即使在不主动传输时也是如此。
2. **错误处理和信息泄漏预防**：开发人员应该能够配置他们的工具来抑制可能为攻击者提供系统信息的详细错误消息。相反，它向用户返回通用错误消息，限制信息暴露并防止恶意行为者的潜在利用途径。
3. **持续更新和修补程序**：选择一个网关，它会不断更新以解决安全漏洞，并及时实现已知漏洞的修补程序，从而减少攻击者的机会窗口。
4. **日志记录和监控**：开发人员应该设置他们的网关来记录 API 请求和响应，维护一个全面记录，这在事件后分析或取证调查期间可能是无价之宝。您的 DevOps 团队可以主动监控这些日志，以检测可疑活动或异常情况，从而发出潜在安全威胁的信号。此外，您会想要一个与 SIEM 工具集成的工具。这统一了日志记录和监控，并利用 SIEM 解决方案提供的高级分析、关联规则和实时警报，确保一个知情的安全态势。

## 认真对待 API 安全

鉴于 API 的关键角色，API 安全在现代软件生态系统中至关重要。虽然 API 为集成和扩展打开了广阔的可能性，但它们也引入了一组必须精心解决的新安全挑战。只要您整合了某种类型的 API 网关，就不会出错，但这里有一些具体要考虑的事项:

- **它是**云原生的吗？[云原生和 Kubernetes API 网关](https://thenewstack.io/improving-cloud-native-devex-the-api-gateway-perspective/)是为在云原生和 Kubernetes 环境中蓬勃发展而特意构建的。它们了解并采用容器编排平台的动态特性。Kubernetes 原生 API 网关的一个例子是 [Edge Stack](https://www.getambassador.io/products/edge-stack/api-gateway)。
- **或者它是全面的吗？** 更通用的 API 网关，如 Kong 或 Gloo，功能多样，可以在各种环境中部署，包括 Kubernetes。但是，它们与 Kubernetes 的特定细微差别不固有地定制。它们需要更多的手动配置，但通常非常适应性强，并包括 API 开发生命周期中您可能会发现方便的其他套件工具。全面的解决方案可能不会提供与以 Kubernetes 为中心的对应物相同级别的自动服务发现、负载平衡和动态路由，这可能需要更多的手动管理。
- **开源还是商业？** 有各种开源选项可以尝试，包括 KrakenD 开源 API 网关、Emissary Ingress、Tyk 的开源选项或 Apache APISIX。开源选项非常适合试用，但不总是具有良好维护的商业选项的支持和可扩展性。

无论您选择哪种工具，请确保您获得的 API 网关工具都会细致地解决这些问题。认识到 API 所伴随的漏洞，并采用像 API 网关这样的工具来抵制潜在的威胁和加强防御变得至关重要。

通过优先考虑 API 安全，组织可以保护其数字资产并在用户基础中培育信任，确保可持续增长和技术创新。有关哪种 API 网关工具最适合您的团队的更多信息，请下载 [Ambassador Labs 的 API 购买指南](https://www.getambassador.io/resources/the-kubernetes-api-gateway-buyers-guide)。

