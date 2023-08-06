# 如何正确集成社交登录

创建一个解决方案的指南，避免安全风险，能够很好地扩展到许多组件，易于扩展，并且只需要简单的代码。

翻译自 [How to Integrate Social Logins the Right Way](https://thenewstack.io/how-to-integrate-social-logins-the-right-way/) 。

![](https://cdn.thenewstack.io/media/2023/07/fe9ada74-social_media1-1024x654.jpg)
*图片来自 Shutterstock 的 [Lenka Horavova](https://www.shutterstock.com/g/lenkahoravova) 。*

提供数字服务的组织最常使用 [OAuth 2.0 和 OpenID Connect](https://curity.io/resources/learn/oauth-overview/) 来保护其应用程序和 API 。采用这种方法的一个好处是将用户凭据管理等复杂的安全操作从应用程序中外部化。

通常，开发人员在集成社交登录时[首次](https://thenewstack.io/getting-started-with-identity-and-access-management/)接触到 [OAuth](https://roadmap.sh/guides/oauth) 。这通常涉及将一个库插入应用程序中，然后编写几行代码将用户重定向到诸如 Google 或 Facebook 之类的 Provider ，之后令牌将返回到应用程序：

![](https://cdn.thenewstack.io/media/2023/07/98db8405-image1.jpg)

与旧的网站架构相比，这似乎是一个更有吸引力的选项，其中应用程序必须存储用户密码并实现密码恢复或密码策略功能。然而，简单的用户登录只是应用程序端到端安全生命周期的一小部分。

在使用社交登录时，存在一些架构和安全风险。因此，在本文中，我将指出最常见的问题。然后，我将展示如何以最佳方式实现社交登录解决方案。最终的结果将是一个能够很好地扩展到许多组件的解决方案，易于扩展，并且只需要简单的代码。

## 设计 API 凭据

在对用户进行身份验证后，下一个目标是与后端创建一个安全的会话。如今，前端通常调用后端 API ，因此需要一个 API 消息凭据。当开发人员初次接触 OAuth 时，他们通常期望使用从社交 Provider 收到的令牌之一。

收到的令牌通常是 ID 令牌、访问令牌和可选的刷新令牌。OpenID Connect 标准规定，ID 令牌始终处于 JSON Web Token（JWT） 格式。然而，[访问令牌和刷新令牌](https://curity.io/resources/learn/oauth-refresh)通常不是 JWT 。它们被设计用于从社交 Provider （如Facebook帖子）获取用户资源的访问。

因此，如果开发人员尝试使用将访问令牌发送到 API 的标准 OAuth 2.0 行为，可能无法确保请求的安全性。相反，缺乏经验的开发人员可能会尝试通过将 ID 令牌发送到 API 来解决这个问题。由于社交 Provider 提供了验证 ID 令牌的端点，如果 API 使用支持验证 JWT 的安全库，则可以成功实现以下流程：

![](https://cdn.thenewstack.io/media/2023/07/3f8a2ff1-image4a.jpg)



然而，不应该像这样使用 ID 令牌。在 OpenID Connect 中，ID 令牌代表认证事件的证明，并通知客户端应用程序认证是如何以及何时发生的。它应该由客户端存储，不应发送到任何远程端点。它不是用于 API 中的授权。

在这里缺少的关键因素是，用于保护 API 的访问令牌必须由提供 API 的同一组织颁发。这使得用户身份、范围和声明以及令牌生命周期可以被控制。然后，API 可以正确地授权对数据的请求。其他组织颁发的外部令牌，包括社交 Provider ，不应用于保护您的 API。

## 自定义令牌颁发

了解了这一点之后，下一步的实施可能是[验证 ID 令牌](https://curity.io/resources/learn/validating-an-id-token/)作为证明，然后在后端颁发自定义令牌，然后将其返回给 OAuth 客户端。这更接近标准 OAuth 和 OpenID Connect 的工作方式。自主实现可能被称为令牌服务，如下图所示。其角色将是向客户端颁发访问令牌，然后可以发送到组织的 API ：

![](https://cdn.thenewstack.io/media/2023/07/22d9487c-image2.jpg)

整体上，安全解决方案的形状现在走在更好的轨道上。然而，与完整的 OAuth 解决方案相比，存在一些限制。首先，每当集成新的认证方法（例如新的社交 Provider ）时，应用程序和令牌服务都必须进行更改，并且必须处理任何安全细微差别。随着架构的增长，这会增加相当大的复杂性，并且不太可能很好地应对诸如多因素认证（MFA）等方面。

其次，不太可能遵循安全最佳实践，导致弱点。快速的社交登录实现可能会使用一个公共客户端，该客户端接收没有 OAuth 客户端凭据的令牌，并将其暴露给浏览器。这与 OAuth 针对[基于浏览器的应用程序](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps)的最新建议不符。

在架构的 API 方面，应使用多种令牌类型。JWT 访问令牌仅设计用于在后端环境内使用。互联网客户端应该使用机密的、[不透明的访问令牌](https://curity.io/resources/learn/phantom-token-pattern/)作为隐私最佳实践。

另一个困难是，每个社交 Provider 将在其令牌的主题声明中为用户的身份发行不同的值。如果用户通过多种方式进行认证，存在风险会导致业务数据中出现重复的身份。大多数组织将难以正确管理这些 API 行为。

## 授权服务器

最初的 [OAuth 2.0 规范](https://datatracker.ietf.org/doc/html/rfc6749#section-1)在这个架构中引入了核心安全组件，即授权服务器。现代实现支持许多其他安全标准，包括 OpenID Connect 。使用授权服务器时，应用程序组件不再直接与社交登录 Provider 集成。

相反，每个应用程序实现一个[代码流](https://curity.io/resources/learn/openid-code-flow/)，只与授权服务器进行交互。该机制支持任何可能的身份验证类型，包括 MFA 和完全定制的方法。认证后，可以使用账户链接来确保 API 接收到的访问令牌中的一致身份。如何颁发令牌提供了对令牌格式、声明和生命周期的控制。还有一个内置的令牌签名密钥管理和更新解决方案：

![](https://cdn.thenewstack.io/media/2023/07/4c935bd3-image4a.jpg)

所有这些为在应用程序和 API 中实现安全性提供了一个完整的端到端解决方案。它最强大的特点是简单性和可扩展性。要集成对新的社交 Provider 的已测试支持，您只需要在授权服务器上进行配置更改。应用程序或 API 中不需要进行代码更改。

## 结论

社交 Provider 为管理许多类型应用的登录提供了用户友好的方式。每个用户使用他们不会忘记的熟悉凭证登录，这可以将用户无缝地引导到您的数字服务。然而，实施社交登录的方式可能不够优化。这个过程可能乍一看似乎很简单，但很快就会变得复杂并且会引发问题。

在设计这样的解决方案时，最好的方法是从 API 需要正确保护数据访问的角度进行思考。避免将社交 Provider 的 ID 令牌用作 API 凭据。

更重要的是，避免使用外部访问令牌来保护自己的数据。相反，颁发可以控制其格式、声明和生命周期的访问令牌。对于 API 和客户端都遵循安全最佳实践也很重要。

最后，考虑代码简洁性、未来的安全功能和架构可扩展性的观点。这将导致使用授权服务器集成社交登录。然后，您必须确保您选择的 Provider 支持您所需的行为。请参阅以下链接获取更多相关信息：

- [身份和访问管理入门](https://curity.io/resources/learn/iam-primer/)
- [API 安全最佳实践](https://curity.io/resources/learn/api-security-best-practices/)
- [帐户链接示例](https://curity.io/resources/learn/account-linking-recipes/)

