# 4 个 API 安全最佳实践

![Featued image for: 4 API Security Best Practices](https://cdn.thenewstack.io/media/2024/07/dcb99323-token-1024x576.jpg)

API 是现代数字解决方案的支柱。因此，API 安全应该成为首要的业务关注点。然而，与发展中的企业一样，在 API 安全方面总是有可以改进的地方。因此，不要将本文视为一个全面的指南，而是一个关于从哪里开始的启发。如果您考虑以下两个要点，您将为您的 API 安全奠定良好的基础：

- 使用 API 网关。
- 使用访问令牌进行授权。

让我详细说明它们的优势，并展示如何发展您的 API 安全。

## 1. 使用 API 网关

当上线并公开 API 时，在 API 前面放置一个 API 网关。然后，API 网关充当您 API（或 API）的单一入口点。因此，您可以使用它来强制执行通用策略。例如，您可以确保所有公开可用的端点都支持 HTTPS。

HTTPS 使用加密的通信通道（TLS）。但是，TLS 不限于 HTTPS。我建议将 TLS 用于在 TCP 上运行的任何协议。这样，您可以加密传输中的数据，保护它免受窃听，从而避免（某些）对您通过 API 公开的数据的未经授权的访问。

HTTPS 仅仅是保护 API 的最低限度。您还应该考虑实施 [身份验证和授权](https://curity.io/resources/learn/authentication-vs-authorization/)。为此，请使用 [OAuth](https://curity.io/resources/learn/oauth-overview/) 或 [OpenID Connect](https://curity.io/resources/learn/openid-connect-overview/) 等协议。这两种协议都允许您在 [访问令牌](https://thenewstack.io/jwts-on-a-journey-sending-jwt-access-tokens-across-apis/) 的帮助下委托对 API 的访问，同时保持信任管理集中。

## 2. 使用访问令牌进行授权

实际上，访问令牌通常意味着 JSON Web 令牌 (JWT) 格式。从本质上讲，JWT 是 [一个签名的 JSON 对象](https://curity.io/resources/learn/self-contained-jwts/)，它以可验证的方式传达有关访问授予的信息。在 OAuth 中，[授权服务器](https://curity.io/product/) 负责处理和传达该授权。授权服务器有责任向 [访问令牌](https://thenewstack.io/the-data-your-access-token-reveals-and-how-to-secure-it/) 添加准确的 [数据] 并对其进行签名。

### 仔细设计 JWT

JWT 是 API 授权的便捷工具。它们可以承载 API 及其微服务应用访问规则并授予或拒绝请求所需的所有必要信息。您应该花时间做的一件事是勾勒出您的 API 规则需要哪些信息。此练习称为 [令牌设计](https://curity.io/resources/learn/scopes-claims-tokens-and-all-the-things-in-between/)。在设计令牌时，请确保使用非对称签名算法。

非对称签名提供不可否认性，这意味着只有授权服务器才能颁发访问令牌，因为它是有权访问所需密钥的唯一机构。使用非对称签名，您可以确保授权服务器颁发了访问令牌，而不是任何其他方。这就是您如何在技术层面上建立信任的方式。

### 验证 JWT

一旦您知道从访问令牌中期待什么，您就可以准备集成。使用 API 网关进行粗粒度访问控制。它应该拒绝任何明显格式错误的请求，例如缺少访问令牌或包含无效令牌时。无效令牌也可以是 [范围](https://curity.io/resources/learn/scopes-and-how-they-relate-to-claims/) 不适合请求的令牌。[JWT 安全最佳实践](https://curity.io/resources/learn/jwt-best-practices/) 包括以下内容：

- 始终验证访问令牌。
- 指定并检查以下内容的预期值：
    - 签名算法
    - 颁发者（授权服务器的标识符）
    - 受众（您 API 的标识符）
- 验证基于时间的要求，例如：
    - 过期
    - 颁发时间
    - 不早于
- 不要信任 JWT 标头参数中的值。
如果您依赖 JWT 标头参数来加载密钥材料，请谨慎。例如，仅从受信任的来源（例如配置的 URL（JSON Web 密钥集 URI，jwks_uri））加载 kid 参数引用的密钥，或者使用 OpenID Connect Discovery 等发现机制。如前所述，密钥对于建立信任至关重要，因此您必须小心。验证完 JWT 的语法后，您可以验证签名，如果成功，则可以使用声明来处理访问规则。

## 3. 避免常见风险
使用 API 网关和访问令牌进行授权，可以避免常见的 API 安全风险。例如，在 [OWASP 十大](https://curity.io/resources/learn/owasp-top-ten/) 中，您可以找到以下项目：

- 对象级授权漏洞 (BOLA)
- 用户身份验证漏洞 (BUA)
- 对象属性级授权漏洞 (BOPLA)
- 资源消耗不受限制
- 对敏感业务流程的访问不受限制

您可以在 API 网关中配置速率限制，从而避免资源消耗不受限制。此外，API 网关可以默认要求所有请求都使用访问令牌。结合 API 在每个请求上验证访问令牌并根据令牌中的声明进行访问控制，您可以避免对象级授权漏洞和对象属性级授权漏洞。

使用 OAuth，授权服务器承担了重要且困难的安全工作。其中包括对用户进行身份验证，这可以最大程度地减少由于专有实现中的缺陷而导致的用户身份验证漏洞。您可以在授权服务器上启用 [多因素身份验证](https://curity.io/resources/learn/introduction-to-mfa/)，以降低对敏感业务流程的访问不受限制的风险。

## 4. 提升 API 安全性

通过添加 API 网关并使用 [OAuth 或 OpenID Connect 基于访问令牌进行授权](https://thenewstack.io/supply-chain-attacks-how-to-mitigate-oauth-token-theft/)，您可以缓解许多主要的 API 安全风险。此外，您可以以可扩展的方式发展您的架构。例如，实施和结合最佳实践模式，例如保护隐私的 [幽灵令牌模式](https://curity.io/resources/learn/phantom-token-pattern/) 或 [令牌处理程序模式](https://curity.io/resources/learn/the-token-handler-pattern/)，用于基于浏览器的应用程序。您只需要一个 API 网关和访问令牌进行授权即可开始。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。