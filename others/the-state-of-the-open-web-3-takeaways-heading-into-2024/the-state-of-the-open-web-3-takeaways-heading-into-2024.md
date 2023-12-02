<!--
title:  开放Web2024三大趋势
cover: https://cdn.thenewstack.io/media/2023/11/e8e2ec0c-agatha-depine-_wf-ubkk9je-unsplash-1024x683.jpg
-->

在新的一年里开发者应关注三大开放Web趋势：社交Web复兴与Web组件。

> 译自 [The State of the Open Web: 3 Takeaways Heading into 2024](https://thenewstack.io/the-state-of-the-open-web-3-takeaways-heading-into-2024/)，作者 Richard MacManus 是 The New Stack 的高级编辑，他撰写有关Web和应用程序开发趋势的文章。此前，他于 2003 年创立了 ReadWriteWeb，并将其打造成世界上最有影响力的技术新闻网站之一。从早期......

在许多方面，开放Web比过去几年更加健康：由于 Mastodon 的持续改进和 Meta 承诺支持 Threads(这至关重要)，联邦宇宙现在具有强大动力；Web标准也在不断改进(仅举 WebAssembly 和 Web Components 为例)；如 Open Web Advocacy 这样的非营利集体也在大声疾呼，试图[限制谷歌和苹果等平台公司的权力](https://thenewstack.io/2023-web-tech-check-in-react-performance-pwas-ios-browsers/)。

尽管并不是所有事情都向好的方向发展 – 随着我们迈入 2024 年，大型科技公司操纵或直接控制开放Web的权力仍然令人担忧。 Google 掌握着这一代占主导地位的Web浏览器的钥匙，苹果和 Google 也控制着我们的移动设备，现在 Meta 有望成为联邦宇宙的主导力量。

考虑到这种背景，以下是 2023 年开放Web的三大发展趋势。

## 1. 联邦宇宙（Fediverse）是社交Web的复兴

2023年对社交媒体来说是汹涌澎湃的一年，这主要是因为埃隆·马斯克在 2023 年确立了他对推特的控制。2023 年 7 月底，马斯克将该应用程序的名称从 Twitter 更改为 X – 自那以后，该服务一直在持续退化。没有必要再浪费笔墨来讨论 X/Twitter，所以我将重点关注 2023 年和 2024 年社交媒体的亮点：联邦宇宙（Fediverse）。

[联邦宇宙](https://thenewstack.io/the-fediverse-points-to-our-social-media-future-post-musk/)是通过 ActivityPub(万维网联盟标准)互联的去中心化社交媒体服务的集合。联邦宇宙无疑是社交Web上的复兴，因为社交媒体有机会首次在十多年后真正去中心化。这对开发者有重大意义；自 2000 年代早期的博客圈以来，这可能是最好的开放平台机会。

Mastodon 是目前联邦宇宙中最大的应用程序。自 2017 年启动以来，Mastodon 经常因其糟糕的用户体验而受到批评(包括我的)，但在这方面它在今年取得了重大进步。5 月，该开源项目宣布改进了其新手引导体验，9 月它宣布了 Mastodon 4.2，其中包括更好的搜索和注册流程改进。用户界面也有明显的改进，“例如添加更多线程指示符，使文章预览更漂亮，并从图像预览中删除裁剪。”

4.2 中的关键更新是改进的搜索。首次，Mastodon 用户能够在整个Web中搜索全文帖子。但是，这里有一个问题 – 搜索引擎只包括明确选择加入的用户。目前还不清楚有多少 Mastodon 用户已经调整了他们的设置，但因为这是选择加入的，所以比例可能性很低。我看到的唯一数字来自一个名为 vmst.io 的小型实例，该实例[报告](https://vmst.io/@iostat/111336324983841020)截至 11 月 1 日，略高于 3% 的用户选择加入，超过 12% 的帖子现在可以搜索。

![](https://cdn.thenewstack.io/media/2023/11/162f6ffe-mastodon_search_optin.png)

尽管如此，Mastodon 比一年前有了更好的用户体验，在搜索方面也更加开放。但 Mastodon 仍然是......姑且这么说吧，一种需获得的品味。7 月，一个新的竞争对手出现，立即更受主流受众的欢迎:Threads。

Meta 主要推出 Threads 是为了挑战不堪重负的 Twitter。凭借与 Instagram 的巧妙集成(后者的用户可以使用现有的 Instagram 凭据登录 Threads)，它迅速获得了 1 亿用户。但当 [Threads 承诺](https://thenewstack.io/threads-adopting-activitypub-makes-sense-but-wont-be-easy/)通过支持 W3C ActivityPub 规范加入联邦宇宙时，情况变得非常有趣。

近五个月过去了，Threads 尚未实现 ActivityPub，但迹象表明它将在某个时候履行其诺言。这无疑对开放Web是有希望的，因为仅仅将 Mastodon 和 Threads 互连就会有好处 – 更不用说连接到已经表示将加入联邦宇宙的其他服务，比如 WordPress。

然而，存在风险：没有保证你的(例如)Mastodon 帖子会受到 Threads 算法的青睐。埃隆·马斯克今年的伎俩之一是限制没有为蓝色勾选标记付费的 X 用户的流量；本质上是一种“付费发挥作用”的策略，让人想起上一代流行音乐电台。因此，2024年有关社交媒体的一个大问题将是：Meta 在加入联邦宇宙后，将对 Threads 算法施加多大权力？让我们拭目以待。

## 2. Web 组件正在挑战 React 正统派

[Web Components](https://thenewstack.io/polymers-web-component-library-litelement-and-how-it-compares-to-react/) 正在经历繁荣时期。它们已经是上升的Web标准十多年了，但最近出现了一种称为“HTML Web 组件”的新模式，Web 开发人员正在越来越多地使用它。这种模式似乎是由杰里米·基思创造的，杰里米是一位受人尊敬的开发人员，他撰写了长期运行的 Adactio 博客。本月早些时候，基思[将 HTML Web 组件定义为](https://adactio.com/journal/20618)“使用自定义元素来扩展现有标记”。他明确将这种模式定位为 React 组件的替代方法:

“React 鼓励替换思维：“忘记浏览器可以做什么; 用 React 组件代替一切，即使你在重新创造轮子。”

HTML Web Components 鼓励增强思维。”

通过扩展 HTML 而不是绕过它的想法也得到了更现代框架的鼓励，包括 Eleventy、Remix 和 Astro。到 2023 年底，从常见的前端开发实践来看，React 仍然主导世界，但 Web Components 的不断发展正挑战这一世界观。

![](https://cdn.thenewstack.io/media/2023/11/70d2e3bb-html_web_components.png)

## 3. Web3 和元宇宙已成昨日黄花

2023 年是[人工智能工程](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/)的一年，这意味着前两年炒得火热的两大潮流在今年被毫不客气地甩到了路边：[Web3](https://thenewstack.io/web3-stack-what-web-2-0-developers-need-to-know/) 和[元宇宙](https://thenewstack.io/meta-metaverse-developers/)。

当然，2024 年情况可能会发生变化。尤其是对于元宇宙，因为我们正在等待[苹果 Vision Pro](https://thenewstack.io/vision-pro-for-devs-easy-to-start-but-ui-not-revolutionary/) 头显的发布(最新估计是 3 月)。但是，在多年来一再未能兑现[去中心化应用程序](https://thenewstack.io/web3-tools-and-tipping-points-a-chat-with-infura-co-founder/)(dApps)承诺之后，似乎基于区块链的 Web3 永远不会起飞了。

![](https://cdn.thenewstack.io/media/2023/06/857715d4-xcode_xros2.jpg)

*为 Apple Vision Pro 开发*

虽然我已经放弃了 Web3，但从长远来看，元宇宙对开放Web还是有意义的。[Metaverse Standards Forum](https://metaverse-standards.org/) 是一个行业联盟，拥有广泛的支持(尽管苹果不在其成员之列)，希望元宇宙与Web兼容。我在今年早些时候与其主席 Neil Trevett 进行了[交谈](https://thenewstack.io/the-slow-road-to-metaverse-standards-and-how-ai-fits-in/)，他将元宇宙定义为“Web的连接性与空间计算的沉浸性的组合”。

这是否会实现还有待观察，但 Meta 和苹果都表示他们将在其硬件和操作系统中支持Web。这些是开发人员明年会密切监视的承诺 – 我肯定会在这里报道它。
