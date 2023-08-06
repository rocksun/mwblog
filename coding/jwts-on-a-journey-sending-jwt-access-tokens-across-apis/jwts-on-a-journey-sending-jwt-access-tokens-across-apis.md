# JWT 的旅程 — 在API之间发送 JWT 访问令牌

在设计 JSON Web Tokens 时，必须彻底考虑令牌的最佳生命周期和所需数据。

翻译自 [JWTs on a Journey — Sending JWT Access Tokens across APIs](https://thenewstack.io/jwts-on-a-journey-sending-jwt-access-tokens-across-apis/) 。

![](https://cdn.thenewstack.io/media/2023/07/6bc12bce-token1-1024x683.jpg)
*图片来自 Shutterstock 的 [stocksolutions](https://www.shutterstock.com/g/stocksolutions)*

访问控制对于保护 APIs 至关重要。OAuth 实现了基于令牌的授权，其中访问控制要求满足特定要求的访问令牌。这种令牌通常以 [JSON Web Token（JWT）](https://thenewstack.io/jwts-connecting-the-dots-why-when-and-how/) 的形式存在，作为访问 APIs 的入场券。在进入系统时，存在于各个位置的访问控制，例如在 API 网关和每个微服务中。这种范式称为[零信任](https://thenewstack.io/what-is-zero-trust-security/)。在[应用零信任和基于令牌的授权时](https://curity.io/resources/learn/zero-trust-overview/)，JWT 不可避免地会在系统中传输，从一个端点到另一个端点。

![](https://cdn.thenewstack.io/media/2023/07/4343ab77-image1.png)

在令牌按流程进行时，JWT 会不断进行验证和核实。验证意味着检查令牌是否有效 — 即签名是否可信，令牌是否尚未过期。核实意味着令牌满足通过访问控制所需的要求，例如预期的发行者、受众、范围和声明值。因此，本文解决了 JWT 在旅程中面临的两个挑战：

- 设置令牌的生命周期。
- 在令牌中提供足够的数据。

## 令牌生命周期

安全最佳实践建议将 JWT 的生命周期保持短暂，最好仅为几分钟。然而，如果用户不得不一直登录以更新访问令牌，他们可能会感到沮丧。因此，OAuth 提供了一种流程，其中客户端应用程序可以使用刷新令牌进行访问，而无需与用户进行交互。然而，刷新令牌仅供客户端使用，而不是供 API 使用。因此，API 不能刷新访问令牌，但在收到过期令牌时最终会返回错误。

每当 API 因为过期或其他无效令牌而返回授权错误（HTTP 401）时，客户端应该使用新的访问令牌重试请求。然而，请求可能是异步的。在 JWT 过期之前，JWT 可能已经移到上游 API ，并且 API 可能无法在当前请求的一部分中向客户端返回错误。在这种情况下，必须有一个回调或通知机制，允许上游 API 通知任何下游 API ，最终通知客户端令牌已过期，以便客户端可以重新开始流程。为了最大程度减少这种回调，客户端可以在令牌过期之前[刷新访问令牌](https://curity.io/resources/learn/oauth-refresh/)，以便 JWT 在发送之前有足够的剩余生命周期。

## 隐私最小化

安全性涉及最小化。不仅令牌生命周期应该是可接受的最小值，JWT 还应该只包含访问控制所需的绝对必要数据。进一步说，尽管访问令牌是针对客户端发放的，但理想情况下，客户端不应该访问与访问令牌关联的任何数据。因此，JWT 的传递不应经过客户端，而应该是不透明的访问令牌。

如果客户端接收到不透明的访问令牌，则 JWT 的传递将从 API 网关开始。不透明的访问令牌不仅对客户端不透明，对 API 也是如此。因此，API 需要查找与此类令牌相关联的数据。这种流程称为内省。由于内省会影响性能，尤其是如果每个微服务都需要内省，则最好让 API 网关将不透明令牌转换为 JWT 并缓存结果。这种方法称为[幻象令牌模式](https://curity.io/resources/learn/phantom-token-pattern/)。通过这种方式，后端的 AP 仍然处理 JWT 。

![](https://cdn.thenewstack.io/media/2023/07/e444a42a-image2a.png)

## 令牌共享

如前所述，访问控制是由 API 执行的，因此它们是分散的。因此，API 需要在请求中包含一个访问令牌（JWT），以便基于其做出决策。基于令牌的授权允许以可验证和可审计的方式在 API 之间传输用户数据，将其放入 JWT 中。

### 令牌转发

在 API 和微服务之间共享 JWT 的最简单方法是将其简单地转发到上游 API 。然而，随着数百个不同的 API ，以及潜在的数百个不同的访问控制，向 JWT 提供所有潜在所需数据是不可行的。这是不可行的，因为可能事先根本不知道 JWT 将要走的路径以及要添加哪些数据。即使知道，添加所有数据和访问权限以覆盖所有可能的流程，违反了最小特权原则。例如，在这种情况下，访问令牌需要包括所有有效的范围值，以便任何 API 都能接受它，尽管单个 API 只需要一部分范围。目标应该是尽量减少数据，以涵盖最常见的情况。

![](https://cdn.thenewstack.io/media/2023/07/a79fec0a-image3.png)

### 令牌嵌入

在转发令牌时缩小 JWT 中的数据的一种方法是将一个令牌[嵌入到另一个令牌](https://curity.io/resources/learn/token-sharing/#embedding-a-token)中 - JWT 的一个声明包含另一个 JWT 。与使同一个 JWT 通过系统的方法不同，一个 API （或很可能是 API 网关）可以将一个嵌入的、更窄的 JWT 转发到上游 API 。因此，上游 API 接收定制的令牌，满足最小特权原则。嵌入令牌方法的缺点是它不仅增加了外部令牌的大小，而且在发放 JWT 时仍然需要知道所有数据。这并不总是如此。例如，如果在创建 JWT 时不知道新 API 的任何令牌，则 JWT 不会嵌入任何令牌。在这种情况下，新令牌将在 JWT 过期并得到更新时首次嵌入。

![](https://cdn.thenewstack.io/media/2023/07/3f738133-image4a.png)

### 令牌交换

最灵活的令牌共享方法是交换令牌。[令牌交换方法](https://curity.io/resources/learn/token-sharing/#exchanging-a-token)类似于刷新令牌流程，其中一个令牌被交换为另一个令牌。虽然刷新令牌流程是为客户端指定的，仅限于使用刷新令牌刷新（现有的）访问令牌，但令牌交换可以用于一系列令牌和其他用途。例如，它允许将访问令牌交换为具有不同范围和声明的新令牌。令牌交换不仅在共享同一用户的令牌时有用，还可以用于[实现委托和冒名顶替](https://curity.io/resources/learn/impersonation-flow-approaches/)用例，其中访问令牌的主题代表完全不同的用户。

因此，令牌交换使高度定制的令牌共享机制成为可能，API 或 API 网关可以根据需要请求上游 API 的新 JWT ，遵循最小特权原则。

![](https://cdn.thenewstack.io/media/2023/07/f59af710-image5.png)

## 结论

一旦 JWT 被发送出去，就无法更改。因此，在设计 JWT 时必须彻底考虑令牌生命周期和令牌数据。JWT 应该包含足够但最少的数据，以满足它们在途中遇到的挑战（即访问控制）。因此：

- 保持 JWT 生命周期短暂并处理过期。
- 保持 JWT 访问令牌私密，不要将其暴露给客户端。
- 使用令牌共享技术以满足 API 之间的安全要求。

有各种令牌共享方法可以帮助满足安全要求。令牌转发和令牌交换的组合可能足以满足复杂的云原生应用程序的要求，以确保JWT的安全传输。