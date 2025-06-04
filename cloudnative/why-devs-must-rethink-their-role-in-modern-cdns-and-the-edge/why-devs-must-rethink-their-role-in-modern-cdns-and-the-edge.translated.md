# 为什么开发者必须重新思考他们在现代 CDN 和边缘计算中的角色

![为什么开发者必须重新思考他们在现代 CDN 和边缘计算中的角色 的特色图片](https://cdn.thenewstack.io/media/2025/06/59c84e33-zyanya-citlalli-465kpeg2n-q-unsplashc-1024x576.jpg)

当 Web 首次扩展时，内容分发网络 (CDN) 成为处理不断增长的负载的一种方式。Akamai 被广泛认为是 1990 年代后期 CDN 技术的先驱，但可以说它现在已经被更年轻、更敏捷的 CDN 竞争对手所超越。至少这是 [Artur Bergman](https://www.linkedin.com/in/crucially/) 的观点，他是 Fastly 的联合创始人兼首席架构师，Fastly [于 2011 年作为 CDN 起家](https://thenewstack.io/glitch-fastly-developer-experience/)，但现在 [将自己定位](https://www.fastly.com/products) 为“边缘云平台”。

“Akamai 是第一个云服务，第一个多租户云服务，”Bergman 在接受 The New Stack 采访时说。“我认为如果他们对开发者友好，那么他们应该像 AWS 一样成为一个大型参与者，对吧？”

Akamai 可能不是第一个云服务，但它绝对是其中之一 —— 并且它的 CDN 在“[云计算](https://cybercultural.com/p/018-birth-of-cloud-computing/)”获得关注之前就已经首次亮相。同样值得注意的是，Akamai 最初的 CDN 架构是以硬件为中心的：数据中心里有很多盒子。今天的 CDN，包括 Fastly 和直接竞争对手如 Cloudflare 和 AWS CloudFront，都是以软件为中心的，因此更以开发者为中心。

Fastly 的关于页面当然强调了开发者，以典型的企业热情声称 Fastly 是“开发者梦想更大的地方”。

## 将边缘计算作为软件架构的一部分

在这次采访之前，Fastly 向我发送了一些关于谈话要点的想法。其中一个让我觉得实践开发者可能不会立即同意：“开发者不再与基础设施的复杂性隔绝，他们正在积极地塑造它。” 我请 Bergman 解释一下这句话。

> “…今天，应用程序的需求要求 […] 开发者真正思考 [软件] 架构如何正确使用基础设施。”
>
> – Artur Bergman, Fastly 首席架构师

“传统上，CDN 和边缘计算一直由 IT 或运维部门控制 —— 或者由安全部门控制，或者两者兼而有之。[…] 坦率地说，开发者不喜欢它，因为它只会让他们更难完成工作；它不是一种能够实现创新的东西。我认为今天，应用程序的需求要求 […] 开发者真正思考 […] [软件] 架构如何正确使用基础设施。现在，基础设施在操作上仍然应该是一种抽象 —— 他们实际上不必关心我们的 PoP [存在点 —— Fastly 的边缘节点] 在哪里。他们应该只关心它们是否快速。”

因此，当 Fastly 说开发者正在“积极塑造”基础设施时，这意味着开发者必须在其应用程序中规划诸如低延迟之类的事情。

“我认为，边缘计算应该是你架构的一部分，而不是事后才附加的东西，这种观念在过去 10 年里一直在改变，并且仍在改变，”Bergman 补充道。

## 开发者的负担

这很有道理，但它也增加了开发者的负担。即使没有边缘网络，开发者也有很多事情要做 —— 他们可能已经在使用像 Kubernetes 这样复杂的编排工具，许多前端框架“[复杂性的商人](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/)”，各种 DevOps 工具，以及现在的 AI 编码工具。

此外，Fastly 不仅仅是一个产品 —— 如果你查看 Fastly 的产品页面，你会看到有大量的产品。CDN 只是其中之一；它被归类在“网络服务”下（还有更多产品列表被归类在安全、计算和可观测性下）。

那么，Fastly 提供的产品数量是否会加剧近年来开发者一直在处理的日益增长的复杂性？

“我认为 AI 在很多方面都在帮助解决这个问题，”Bergman 说。“我认为我们的工作是将 [开发者] 从运营实施的复杂性中屏蔽出来。我确实认为今天开发者的生活非常复杂 —— […] 甚至包括非计算方面的事情，比如在欧盟工作。”

Bergman 说，开发者仍然需要意识到复杂性，但 Fastly 的目标是为他们抽象化它。

“我认为它真正有帮助的是 […] 我们消除了很多关于可靠性和性能的担忧 —— 这让工程团队 […] 能够更快地行动。”

## Matrix 中的小故障
不过，Fastly 偶尔也会从其产品套件中砍掉一些产品。上个月，Fastly [宣布关闭](https://blog.glitch.com/post/changes-are-coming-to-glitch/)了其最受欢迎的开发者产品之一：Glitch，这是一个 Fastly 在 2022 年收购的编码平台。三年前，当 [我采访 Fastly 联合创始人 Simon Wistow](https://thenewstack.io/glitch-fastly-developer-experience/) 时，我注意到 Glitch 是各种开发者的最喜欢的原型设计工具——从业余程序员到专业人士。

我问 Bergman，考虑到 Fastly 对开发者友好的关注，为什么这次收购没有成功。

“最终，由于人工智能的出现，世界已经发生了变化，”他回答说，“而 Glitch 平台并不是为人工智能帮助你生成代码、帮助你运行代码的世界而构建的。”

> “Glitch 平台并不是为人工智能帮助你生成代码的世界而构建的。”
>
> – Bergman

换句话说，AI“氛围编码”工具——比如 [Cursor](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance/) 和 [Bolt](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/)——已经抢了 Glitch 的午餐，至少在作为新应用程序的原型设计平台方面是这样。Bergman 将这种情况比作 StackOverflow 如何被 ChatGPT 和其他 AI 聊天工具取代。

## 与大型平台竞争

撇开 Glitch 关闭不谈，该公司似乎提供了除厨房水槽之外的一切互联网基础设施。在最近对边缘计算的深入分析中，我的同事 Mary Branscombe [描述了现代 CDN](https://thenewstack.io/the-modern-cdn-means-complex-decisions-for-developers/)，例如 Fastly 和 Cloudflare，是“计算基础设施的前门”。但我问道，这难道不是像 AWS、Google 和 Microsoft 这样的大型平台公司所做的事情吗？

“我们既竞争又合作，”他回答说。“至少，Amazon 和 Google 确实提供 CDN。我认为 Amazon 拥有其中最复杂的产品，但它更侧重于加速媒体、文件下载、图像——而对动态流量的关注较少。但在更高的层面上，客户对……如果你完全依赖 AWS 的前门，[...]你就不能用它来保护你的 GCP 实例，对吧？”

他的观点是，企业试图将这些世界分开，因为（用 Bergman 的话说）“如果你完全依赖一家供应商，随着时间的推移，你会被收取更多的费用。”

他说，Fastly 可以用作连接大型云提供商的一种渠道。

“通过把像我们这样的人放在前面，你可以 [...] 将流量发送给一个提供商，并将流量发送给另一个提供商。[而且]你知道，迁移变得容易得多。所有这些东西都被抽象掉了。”

## 现代 CDN：软件优先

回到开发者及其需求的话题。在采访快结束时，Bergman 指出，“仍然有很多开发者没有完全意识到”现代 CDN 的可能性。

“举个例子，当然 API 请求是 HTTP——取决于它们是什么，你可以缓存它们，你可以加速它们，你可以观察它们。但很大一部分移动 API 流量直接进入云，因为他们不认为它是 HTTP。比如，他们[开发者]知道图像应该来自边缘，但 API 调用呢？它们只是一些你做的神奇的事情，然后返回[到云]。当然，[API 调用]也受益于边缘。因此，仍然需要更多的教育；我认为，从我们提供商的角度来看，让开发者更容易使用它[Fastly]并看到好处。”

似乎我们在云计算中使用的一些术语——特别是 CDN 这个缩写——掩盖了像 Fastly 和 Cloudflare（谁知道，甚至可能是 Akamai？）这样的公司现在实际在做的事情。正如 Bergman 在我们谈话中的某个时刻所说，“[我们]更喜欢用软件而不是硬件来解决我们的问题。”

有一件事是肯定的：现代 CDN 不再只是一个靠近你的数据中心里的盒子。如今，有很多软件运行在该盒子之上。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)