<!-- 
# HTTP/2 带来快速重置的痛苦
https://cdn.thenewstack.io/media/2023/10/42705762-action-16892_1280-1024x682.jpg

 -->

由于HTTP/2网络协议本身的设计缺陷，我们在未来很多年内都不得不面对其中的一个严重漏洞带来的安全风险。

译自 [HTTP/2 Brings Rapid Reset Misery](https://thenewstack.io/http-2-brings-rapid-reset-misery/) 。

安全漏洞层出不穷，每周都会出现新漏洞，但大多数漏洞可以通过软件更新来修复。但是，HTTP/2中的这个漏洞与软件无关，它存在于互联网基础协议本身，这使问题变得极为严峻。

我指的是HTTP/2中的“快速重置”漏洞(也称[CVE-2023-44487](https://www.cloudflare.com/h2))，它导致了迄今为止最大规模的DDoS分布式拒绝服务攻击。虽然像[Amazon Web Services](https://aws.amazon.com/?utm_content=inline-mention) (AWS)、Cloudflare、谷歌云等大型互联网公司能够抵御这类攻击，但对于许多规模较小的网站和服务来说，同样的攻击力度将难以招架。

问题的根源在于，HTTP/2中的这个漏洞不是某个特定软件组件的问题，而是源自HTTP/2[网络协议](https://thenewstack.io/oracle-open-sources-a-network-protocol-for-machine-learning-models-graphpipe/)本身的设计缺陷。HTTP/2约在[8年前](https://thenewstack.io/take-advantage-http2-speed-web-sites-apps/)由互联网工程任务组(IETF)设计开发，目的是作为传统HTTP协议的更快更高效的继任者。它在移动应用中的广泛采用确立了其在现代互联网基础设施中的关键地位。然而不幸的是，其设计缺陷也埋下了安全隐患。

要理解为何如此，必须首先了解HTTP/2与前身HTTP/1之间的区别。Cloudflare在其报告"HTTP/2 Rapid Reset: deconstructing the record-breaking attack"中详细解释了这一点。

简单来说，所有版本的HTTP都共享相同的HTTP语义结构。也就是总体架构、术语和协议等方面都是相同的，例如请求和响应消息，方法，状态码，header和trailer字段，消息内容等等。每个HTTP版本定义了如何将这些语义内容转换成在互联网上传输的“线路格式”。

HTTP/1使用非常简单的线路格式，它通过可靠的传输层(通常是TCP)发送ASCII字符的序列化流。请求和响应消息进行交换。尽管[单个TCP连接可以交换多个请求和响应](https://thenewstack.io/nvm-manage-multiple-versions-of-node-js-on-a-single-system/)，但在HTTP/1中，每个消息都必须作为一个整体按严格顺序发送。这意味着这些消息是顺序地串行发送的，不能多路复用。

## HTTP/2的复杂性

HTTP/2要复杂得多。在HTTP/2中，每个HTTP消息都会序列化为一组HTTP/2帧。这些帧标识了每条消息的类型、长度、标志、流标识符和有效载荷。流标识符明确指出哪些字节属于哪条消息。通过这种方式，可以在保持并发的同时安全地对消息进行多路复用，以提高速度。为了进一步[提高性能](https://thenewstack.io/neo4j-5-hits-ga-with-major-performance-scalability-improvements/)，在HTTP/2中，流也是双向的。

但是，这种[性能提升](https://thenewstack.io/how-to-boost-mastodon-server-performance-with-redis/)是有代价的。可以用多个HTTP请求轻易淹没服务器。为了防止这种情况发生，可以使用SETTINGS_MAX_CONCURRENT_STREAMS设置来设置最大的活动并发流数。HTTP/2流在理论上也具有生命周期，可以帮助防止HTTP/2遭受DDoS攻击。

然而，HTTP/2也使客户端更容易取消在途请求。也就是“嘿，亚马逊，我其实不需要看自动猫砂盆的页面了”。与其终止整个连接，客户端可以为单个流发送RST_STREAM帧。当服务器收到此消息时，它会停止处理请求并中止响应。结果是服务器资源负载减少，没有浪费带宽。

但是，如果你一个接一个地发送多个HTTP/2取消请求会怎么样？如果你发送那么多请求以至于淹没服务器呢？那么，我的朋友，这就是DDoS攻击的开始。

例如，如果你在服务器或服务的前面部署了HTTP/2代理或负载均衡器(大多数重要的服务器或服务都是这样)，那么用快速重置轻易就能把它压垮。

即使服务器或代理有并发请求数限制，恶意客户端也可以用高请求率把它淹没。而且，由于客户端倾向于速度，它们不会等待服务器设置。结果就是发生竞争条件。这就是发生的事情。结果，用户看到HTTP 502错误网关错误消息和HTTP 499客户端关闭错误。DDoS攻击开始了。

对Cloudflare来说，他们异常坦诚地公开了问题所在，意味着当一个客户端连接到Cloudflare发送HTTPS流量时，它首先会到达他们的TLS解密代理: 该服务解密TLS流量，处理流量，然后将其转发到他们的“业务逻辑”代理。当然，这应该是会发生的事情。

该代理加载所有客户设置，然后将请求路由到适当的上游服务。在攻击下，代理不仅被淹没，而且无法正确报告所发生的事情。更糟糕的是，网络连接本身也被过量流量淹没。

Cloudflare目前通过各种不同的技术手段进行了缓解。这包括设置更高的SETTINGS_MAX_CONCURRENT_STREAMS值;监控连接对RST_STREAM帧的滥用并阻止它们；以及调整“IP监狱”功能，以便将用于此类攻击的IP地址被阻止，不仅针对目标网站，还阻止它们对任何其他Cloudflare保护的域使用HTTP/2。

那么问题现在解决了吗？哦，不。我希望如此。正如Cloudflare所说，“因为这种攻击滥用了HTTP/2协议中的一个根本弱点，我们认为任何实现了HTTP/2的供应商都将受到攻击。这包括每一个现代Web服务器。”

让我强调最后一句话: “每一个现代Web服务器”。这不仅仅是适当的Web服务器。任何提供Web服务的东西都是如此。例如，您还可以在使用Microsoft .NET 8.0 RC1、.NET 7.0和.NET 6.0构建的程序中找到它；Kubernetes API服务器；NodeJS；以及许多其他服务器和程序。

## 更多DDoS在路上

好消息是，HTTP/2快速重置漏洞只能实现DDoS攻击。您不能使用HTTP/2快速重置来接管服务器或窃取数据。坏消息是进行这些哥斯拉级攻击所需的简单性和[所需机器](https://thenewstack.io/how-machine-learning-pipelines-work-and-what-needs-improving/)数量很低。Cloudflare估计其遭受的每秒2.01亿请求的攻击，几乎是其记录中前一次最大攻击的3倍，仅需要2万台机器就生成了。

是的，我们距离安全还远着呢。将会有许多更多的HTTP/2快速重置攻击。而且，我预计许多攻击会比这第一波更成功。很少有公司拥有像亚马逊、Cloudflare和谷歌这样的资源来对付这样的攻击。

这个星期的您的工作是，如果您还没有开始的话，检查整个基础架构，寻找任何提供Web服务的内容，然后将它们[更新](https://thenewstack.io/linkerd-service-mesh-update-addresses-more-demanding-user-base/)为较新、更安全的程序。如果您无法获取补丁，那么就该考虑像将其与互联网隔离等激进的解决方案，直到您能够防御这些攻击。

祝您好运。我们都会需要它。