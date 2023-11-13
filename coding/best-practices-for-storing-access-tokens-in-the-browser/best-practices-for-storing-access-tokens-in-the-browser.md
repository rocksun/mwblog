<!-- 
# 
https://cdn.thenewstack.io/media/2023/11/072bf6e2-browser-1024x683.jpg
 -->

浏览器提供了各种持久化数据的解决方案。当存储令牌时，您应该权衡存储选择与安全风险。

译自 [Best Practices for Storing Access Tokens in the Browser](https://thenewstack.io/best-practices-for-storing-access-tokens-in-the-browser/) 。

web应用程序不是静态站点，而是静态内容和动态内容的精心组合。 更常见的是，web应用程序逻辑在浏览器中运行。 与从服务器获取所有内容不同，应用程序在浏览器中运行JavaScript，从后端API获取数据，并相应地更新web应用程序呈现。

为了保护数据访问，组织应该采用OAuth 2.0。 通过OAuth 2.0，JavaScript应用程序需要在对API的每个请求中添加访问令牌。 出于可用性原因，JavaScript应用程序通常不会按需请求访问令牌，而是存储它。 问题是，如何在JavaScript中获取这样的访问令牌？当您获取一个令牌时，应用程序应该在哪里存储令牌，以便在需要时将其添加到请求中？

本文讨论了[浏览器](https://thenewstack.io/what-does-it-mean-for-web-browsers-to-have-a-baseline/)中可用的各种存储解决方案，并突出了与每种选择相关的安全风险。 在审查威胁之后，它描述了一种解决方案，以提供最佳的浏览器安全选项，用于必须与[OAuth保护的](https://thenewstack.io/5-steps-to-modernize-large-websites-using-oauth/)API集成的[JavaScript应用程序](https://thenewstack.io/beyond-browsers-the-longterm-future-of-javascript-standards/)。

## 获取访问令牌

在应用程序可以存储访问令牌之前，它需要先获取一个令牌。[当前的最佳实践](https://curity.io/resources/learn/spa-best-practices/#using-the-code-flow-with-spas)建议通过“授权码流”这一方式来获取访问令牌: 授权码流是一个两步流程，首先从用户那里收集一个授权许可——授权码，然后应用程序在后台通道中用授权码交换访问令牌。这个请求称为令牌请求，例子如下:

```js
const accessToken = await fetch(OAuthServerTokenEndpoint, {
method: "POST",
// token request with authorization code and PKCE
// submits data in as x-www-form-urlencoded encoded format
body: new URLSearchParams({
 client_id: "example-client",
grant_type: "authorization_code",
code: authorization_code,
 code_verifier: pkce_code_verifier
})
})
// server responds with JSON object
.then (response => response.json())
.then (tokenResponse => {
  // parse access token from response
  if (tokenResponse.accessToken) {
    return tokenResponse.accessToken;
  } // else handle error response
})
.catch( 
// handle network error
)
```

请注意，任何人都可以检查浏览器加载的资源，包括任何[JavaScript代码](https://roadmap.sh/guides/history-of-javascript)。因此，任何用JavaScript实现的OAuth客户端都被认为是一个公开客户端——一个无法保密的客户端，因此在令牌请求期间无法进行身份验证。然而，代码交换的证明密钥(Proof Key for Code Exchange， [PKCE](https://curity.io/resources/learn/oauth-pkce/))提供了一种方法来确保公开客户端的授权码流的安全性。为了减轻与授权码相关的风险，在使用授权码流时，始终应用PKCE。

## 浏览器威胁

### 跨站请求伪造(CSRF)

在[跨站请求伪造(CSRF)](https://owasp.org/www-community/attacks/csrf)攻击中，恶意行为者会欺骗用户通过浏览器无意中执行恶意请求。例如，攻击者可以在网站中嵌入精心设计的图像源字符串，以触发浏览器运行GET请求，或者在恶意网站上添加表单，以触发POST请求。在任何情况下，浏览器都可能会自动将cookie(包括单点登录cookie)添加到这样的请求中。

CSRF攻击也被称为“会话骑乘”，因为攻击者通常会利用用户的经过身份验证的会话来进行恶意请求。因此，攻击者可以默默地代表用户执行请求，并调用用户可以调用的任何端点。然而，攻击者无法读取响应，所以他们通常以一次性状态更改请求为目标，如更新用户的密码。

### 跨站脚本(XSS)

[跨站脚本(XSS)](https://owasp.org/www-community/attacks/xss/)漏洞允许攻击者将恶意的客户端代码注入到一个本来受信任的网站中。例如，如果用户输入生成的输出没有被适当清理，web应用程序的任何地方都可能存在漏洞。浏览器会自动在受信任的网站的上下文中运行恶意代码。

XSS攻击可用于窃取访问令牌和刷新令牌，或执行CSRF攻击。不过，XSS攻击有一个时间窗口，因为它们只能在有限的时间段内运行，如令牌的有效期内，或者打开的选项卡存在漏洞的时长。

即使在XSS无法用于检索访问令牌的情况下，攻击者也可以利用XSS漏洞通过会话骑乘向有保护的Web端点发送经过身份验证的请求。然后，攻击者可以伪装成用户，调用用户可以调用的任何后端端点，并造成严重损害。

## 浏览器中的存储解决方案

应用程序收到访问令牌后，需要存储该令牌以在API请求中使用它。浏览器中有多种方法可以持久化数据。应用程序可以使用专用API(如Web存储API或IndexedDB)来存储令牌。应用程序也可以简单地将令牌保存在内存中或将其放在cookie中。一些存储机制是持久的，另一些在一段时间后或页面关闭或刷新后会被清除。

一些解决方案跨选项卡共享数据，而其他解决方案仅限于当前选项卡。但是，本指南中介绍的大多数方法都针对每个源存储数据。因此，对于任何相关讨论来说，理解一些概念很有帮助:origin和site。

某个(Web)资源的origin是其URL的scheme、hostname和port。例如，`https://example.com/number/one`和`https://example.com:80/path/two`具有相同的origin，因为它们共享scheme(https)、hostname(example.com)和端口(默认端口)。它们的origin为`https://example.com`，与`https://example.com:8443`或`https://this.example.com`不同，因为它们在端口和主机名上有所不同。

相比之下，一个site比资源的origin要大。一个站点是为一组资源提供服务的Web应用程序的通用名称。简单地说，一个站点是scheme和domain name，如`https://example.com`。虽然`https://example.com`和`https://this.example.com:8443`有不同的origin(不同的主机名和端口)，但它们是相同的站点，因为它们托管在同一个域名(example.com)上并使用相同的scheme(https)。(从技术上讲，这个[定义还有细微差别](https://url.spec.whatwg.org/#host-registrable-domain)，但这个简化的说法有助于解释这个概念)。

### 本地存储

本地存储是通过Web存储API中的全局localStorage对象以JavaScript访问的。本地存储中的数据在浏览器选项卡和会话之间可用，也就是说它不会过期或在浏览器关闭时被删除。因此，通过localStorage存储的数据可以在应用程序的所有选项卡中访问。因此，在本地存储中存储令牌非常诱人。

```js
// Storing the access token
localStorage.setItem("token", accessToken);
// Loading the access token
let accessToken = localStorage.getItem("token");
```

每当应用程序调用API时，它都会从存储中获取令牌并手动添加到请求中。但是，由于本地存储可以通过JavaScript访问，这意味着该解决方案也容易受到跨站脚本(XSS)攻击。

如果您在本地存储中使用access token，并且攻击者设法在您的应用程序中运行外部JavaScript代码，那么攻击者可以窃取任何令牌并直接调用API。此外，XSS还允许攻击者操作应用程序中的本地存储数据，这意味着攻击者可以更改令牌。

请注意，本地存储中的数据会永久存储，这意味着存储在其中的任何令牌会驻留在用户的设备(笔记本电脑、电脑、手机或其他设备)的文件系统上，即使浏览器关闭后也可以被其他应用程序访问。因此，在使用localStorage时，请考虑终端安全性。考虑并防止浏览器之外的攻击向量，如恶意软件、被盗设备或磁盘。

根据上述讨论，请遵循以下建议:

- 不要在本地存储中存储敏感数据，如令牌。
- 不要信任本地存储中的数据(尤其是用于认证和授权的数据)。

### 会话存储

会话存储是Web存储API提供的另一种存储机制。与本地存储不同，使用sessionStorage对象存储的数据在选项卡或浏览器关闭时会被清除。此外，session存储中的数据在其他选项卡中不可访问。只有当前选项卡和origin中的JavaScript代码可以使用相同的会话存储进行读取和写入。

```js
// Storing the access token
sessionStorage.setItem("token", accessToken);
// Loading the access token
let accessToken = sessionStorage.getItem("token");
```

与本地存储相比，会话存储可以被认为更安全，因为浏览器会在窗口关闭时自动删除任何令牌。此外，由于会话存储不在选项卡之间共享，攻击者无法从另一个选项卡(或窗口)读取令牌，这减少了XSS攻击的影响。

在实践中，使用sessionStorage存储令牌的主要安全问题是XSS。如果您的应用程序容易受到XSS攻击，攻击者可以从存储中提取令牌并在API调用中重放它。因此，会话存储不适合存储敏感数据，如令牌。

### IndexedDB

IndexedDB是索引数据库API的缩写。它是一个用于在浏览器中异步存储大量数据的API。但是，在存储令牌时，这个浏览器API提供的功能和容量通常不是必需的。由于应用程序在每次API调用中都发送令牌，最好是使令牌的大小最小化。

与迄今为止讨论的其他客户端存储机制一样，使用索引数据库API存储的数据访问受到同源策略的限制。只有相同来源的资源和服务工作者才能访问数据。从安全角度来看，IndexedDB与本地存储相当:

- 令牌可能会通过文件系统泄露。
- 令牌可能会通过XSS攻击泄露。

因此，不要在IndexedDB中存储访问令牌或其他敏感数据。IndexedDB更适合用于应用程序脱机工作所需的数据，如图像。

### 内存

存储令牌的一个相当安全的方法是将其保存在内存中。与其他方法相比，令牌不存储在文件系统中，从而减轻了与设备文件系统相关的风险。

最佳实践建议在内存中存储令牌时将其保存在闭包中。例如，您可以定义一个单独的方法来使用令牌调用API。它不会向主应用程序(主线程)透露令牌。下面的摘录显示了如何在JavaScript中使用内存处理令牌的示例。

```js
function protectedCalls(tokenResponse) {
  const accessToken = tokenResponse.accessToken;
  return {
    // call API with access token
    getOrders: () => {
      const req = new Request("https://server.example/orders");
      req.headers.set("Authorization", accessToken);
   return fetch(req)
    }
  }
}
const apiClient = protectedCalls(tokenResponse);
// call protected API
apiClient.getOrders();
```

请注意，攻击者可能无法在获取令牌后直接访问令牌，因此可能无法直接使用令牌调用API。即便如此，通过持有令牌引用的apiClient，他们可以随时通过apiClient调用API。但是，任何此类攻击都限于选项卡打开并且接口提供的功能的时段。

除了与潜在的XSS漏洞相关的安全问题外，在内存中保持令牌的最大缺点是页面重载时令牌会丢失。然后，应用程序必须获取一个新令牌，这可能会触发新的用户身份验证。安全的设计应考虑到用户体验。

使用服务工作者的体系结构通过在独立的线程中运行令牌处理功能来减轻可用性问题，该线程与主网页分离。服务工作者实际上充当应用程序、浏览器和网络之间的代理。因此，它们可以拦截请求和响应，例如缓存数据和启用离线访问，或者获取和添加令牌。

在使用JavaScript闭包或服务工作者处理令牌和API请求时，XSS攻击可能会针对OAuth流程，如回调流或静默流来获取令牌。它们可以取消注册并绕过任何服务工作者，或者使用原型污染“实时读取令牌”通过覆盖诸如window.fetch之类的方法。因此，请出于方便而不是安全性考虑JavaScript闭包和服务工作者。

### Cookie

Cookie是存储在浏览器中的数据片段。由设计，浏览器会将cookie添加到对服务器的每个请求中。因此，应用程序必须谨慎使用cookie。如果未经仔细配置，浏览器可能会在跨站请求时追加cookie，并允许跨站请求伪造(CSRF)攻击。

Cookie具有控制其安全属性的属性。例如，SameSite属性可以帮助缓解CSRF攻击的风险。当一个cookie的SameSite属性设置为Strict时，浏览器只会将其添加到源自并目标与cookie的源站点相同的请求中。当请求嵌入在任何第三方网站中时，浏览器不会添加cookie，例如通过链接。

您可以通过JavaScript设置和检索cookie。但是，当使用JavaScript读取cookie时，应用程序会变得容易受到XSS攻击(除了CSRF之外)。因此，首选的选择是让后端组件设置cookie并将其标记为HttpOnly。该标志可以缓解通过XSS攻击泄露数据的问题，因为它指示浏览器cookie不能通过JavaScript访问。

为防止cookie通过中间人攻击泄露，这可能导致会话劫持，cookie应仅通过加密连接(HTTPS)发送。要指示浏览器仅在HTTPS请求中发送cookie，必须将Secure属性设置为cookie。

```
Set-Cookie:token=myvalue;SameSite=Strict;Secure;HttpOnly
```

与浏览器中的任何其他永久存储解决方案一样，cookie可能会驻留在文件系统中，即使浏览器已关闭(例如，cookie不必过期，或者浏览器可以将会话cookie作为恢复会话功能的一部分保留)。为了减轻从文件系统中窃取令牌的风险，只能在cookie中存储加密的令牌。因此，后端组件只能在Set-Cookie头中返回加密的令牌。

## 威胁矩阵

下表总结了浏览器中存储解决方案的威胁评估，主要威胁向量标记为红色。橙色威胁需要除Web技术之外的缓解措施。绿色威胁已经或可以通过适当的设置成功消除。

![威胁矩阵表格](https://cdn.thenewstack.io/media/2023/11/958bbae8-screenshot2.jpg)

无论攻击者何时设法窃取令牌，只要令牌有效，他们就可以独立于用户和应用程序使用访问令牌。如果攻击者设法窃取刷新令牌，他们可以显着延长攻击时间并增加损害，因为他们可以续新访问令牌。黑客甚至可以将攻击扩展到除JavaScript应用程序使用的API之外的其他API。例如，攻击者可以尝试重放访问令牌并利用不同API中的漏洞。

被盗的访问令牌可能会造成严重损害，XSS仍然是Web应用程序的主要问题。因此，避免在客户端代码可以访问的地方存储访问令牌。相反，将访问令牌存储在cookie中。当使用适当的属性配置cookie时，浏览器泄露访问令牌的风险为零。然后，XSS攻击与在同一站点上的会话劫持攻击相当。

## 使用Cookie的OAuth语义

Cookie仍然是传输令牌和充当API凭据的最佳选择，因为即使攻击者成功利用XSS漏洞，也无法从cookie中检索访问令牌。但是，为了做到这一点，cookie必须适当配置。

首先，将cookie标记为`HttpOnly`，以便它们不可通过JavaScript访问，以解决XSS攻击的风险。另一个关键属性是Secure标志，它确保cookie仅通过HTTPS发送，以减轻中间人攻击。

其次，颁发短暂的只在几分钟内有效的访问令牌。在最坏的情况下，具有最小有效期的访问令牌只能在可以接受的短时间内被滥用。通常认为15分钟的有效期是合适的。让cookie和令牌的过期时间大致相同。

第三，将令牌视为敏感数据。只在cookie中存储加密令牌。如果攻击者设法获取加密令牌，他们将无法从中解析任何数据。攻击者也无法将加密的令牌重放到任何其他API，因为其他API无法解密令牌。加密令牌只是限制了被盗令牌的影响。

第四，在发送API凭据时要限制性强。只向需要API凭据的资源发送cookie。这意味着确保浏览器只在实际需要访问令牌的API调用中添加cookie。为此，cookie需要有适当的设置，比如`SameSite=Strict`、指向API端点域的域属性和路径。

最后，在使用刷新令牌时，请确保将它们存储在自己的cookie中。没有必要在每个API请求中都发送它们，所以请确保不是这种情况。刷新令牌必须只在刷新过期的访问令牌时添加。这意味着包含刷新令牌的cookie与包含访问令牌的cookie有稍微不同的设置。

## 令牌处理程序模式

在JavaScript客户端中为OAuth提供最佳实践原则的设计模式是令牌处理程序模式。它遵循[OAuth 2.0 for Browser-Based Apps](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps#section-6.1)中描述的BFF(backend for frontend)方法。该模式引入了一个后端组件，能够发出带有加密令牌和上述必要属性的cookie。

后端组件的责任是:

- 作为OAuth客户端与授权服务器交互，启动用户认证并获取令牌。
- 管理JavaScript应用程序的令牌，使其不可访问。
- 代理和拦截所有API请求，以附加正确的访问令牌。

令牌处理程序模式定义了一个BFF，它为在浏览器中运行的应用程序抽象了OAuth。换句话说，令牌处理程序模式建议一个JavaScript应用程序可以用来认证用户并安全地调用API的API。为此，该模式使用cookie来存储和发送访问令牌。

令牌处理程序是一个后端组件，例如可以驻留在API网关中。它由两部分组成:

- OAuth代理，它处理OAuth流以从授权服务器获取令牌。
- OAuth代理，它拦截对API的所有请求并将cookie转换为令牌。

![](https://cdn.thenewstack.io/media/2023/11/ea383949-image1-6.jpg)

OAuth代理获取令牌后，它会发出带有以下属性的cookie:

- SameSite=Strict
- HttpOnly
- Secure
- API的路径

由于令牌处理程序是一个后端组件，所以OAuth代理是一个保密的客户端，可以向授权服务器进行身份验证(与公开的JavaScript客户端相比)。这意味着为了获得令牌，OAuth代理需要进行身份验证。因此，攻击者需要获取客户端凭据才能成功获取新令牌。在JavaScript中运行静默流而没有客户端凭据将失败。

为了令牌处理程序模式能够工作，JavaScript应用程序和令牌处理程序组件必须部署在同一站点上(换句话说，它们必须在同一域中运行)。否则，由于cookie上的同站限制，浏览器不会将令牌cookie添加到API请求中。

要获取数据，JavaScript应用程序只需通过OAuth代理调用API:

```js
// http://www.example.com/app.js
// Call to OAuth Proxy
const response = await fetch("https://api.example.com/orders", {
// Instruct the browser to add cookies to cross-origin requests
credentials: "include"
});
```

浏览器会自动将cookie添加到请求中。在上面的示例中，浏览器将cookie包含在跨域请求中。但是，由于cookie属性`SameSite=Strict`，浏览器只会将cookie添加到同一站点(同一域)的跨域请求中。

OAuth代理解密cookie并将令牌添加到上游API。cookie属性确保浏览器仅将cookie添加到HTTPS请求中，以确保它们在传输过程中是安全的。由于令牌是加密的，它们在休息时也是安全的。然后令牌用于安全访问API。

## 总结

使用OAuth和访问令牌可以最好地保护API访问。但是，JavaScript应用程序处于不利地位。浏览器中没有安全的令牌存储解决方案。所有可用的解决方案在某种程度上都容易受到XSS攻击。因此，确保任何应用程序安全的首要任务应该是防止XSS漏洞。

[令牌处理程序模式](https://curity.io/resources/learn/token-handler-overview/)通过在JavaScript无法访问的cookie中存储加密令牌来缓解XSS风险。它将Web关注点与API关注点分离，并提供指导，使用成熟的Web技术加固JavaScript应用程序，而不会破坏Web架构。[查看令牌处理程序模式的详细描述](https://curity.io/resources/learn/the-token-handler-pattern/)，并[探索各种示例](https://github.com/orgs/curityio/repositories?q=topic%3Atoken-handler)。