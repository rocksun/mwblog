我一直[喜欢 Markdown](https://thenewstack.io/obsidian-and-the-case-for-using-more-markdown/) 的清晰和简洁，现在会有更多的LLM代理也欣赏它。为了应对越来越多的LLM代理进行搜索，[Cloudflare 的网络现在支持实时 Markdown 转换](https://thenewstack.io/cloudflares-markdown-for-agents-automatically-make-websites-more-aifriendly/) [在源头](https://thenewstack.io/cloudflares-markdown-for-agents-automatically-make-websites-more-aifriendly/)。

让我们看一个比他们自己文档中建议的页面更不繁忙的页面，并用 `curl` 请求 Markdown。如果我们也要求详细模式，我们可以看到更多信息：

![](https://cdn.thenewstack.io/media/2026/02/27fb2f35-image-1024x74.png)

我们可以看到额外的头部信息，包括 `x-markdown-tokens:`

![](https://cdn.thenewstack.io/media/2026/02/acef2ec5-image-1-1024x364.png)

因此，假设所有LLM都以相同的方式定义令牌（我不认为它们是），那么我们知道吞噬以下数据将占用 297 个上下文窗口空间。

如果我们查看响应主体：

![](https://cdn.thenewstack.io/media/2026/02/65ebb53d-image-2-1024x339.png)

这是同一页面的 HTML 表示：

![](https://cdn.thenewstack.io/media/2026/02/ad12ba03-image-3-1024x393.png)

你可以清楚地看到两种表示形式中的四个链接。但你也可以看到右侧列的一些内容（例如，“这有帮助吗？”）已经进入了 Markdown。这并没有什么特别奇怪的——尽管我们认为“内容”只是中间列，但实际返回的内容是由页面配置决定的。但我们知道网页上的空间信息无法在 Markdown 中合理传输。而代理不需要这些空间信息。

Cloudflare 在这里做的事情是完全合理的，呼吁“网络必须对代理和人类都有效！”也是如此。但我们确实需要更清楚地了解网络目前是否 *真的* 对人类运行良好。

## 网络本身可能是问题所在

网络需要大量工作才能将其转变为具有金融功能的商店（它不是为此而建造的）或检查用户身份（同样，它不是为此而真正建造的）。随着实际网络使用严重偏离最初的愿景，平均网页变得越来越复杂。

关键是，现代网页被设计成一种视觉体验，其中存在许多相互竞争的张力；它不仅仅是带有固定、无关紧要视觉框架的文本内容，可以被跳过。如果“提取内容”是微不足道的，那么广告模式将比现在更容易被颠覆。

所以，虽然对于一个进行有限获取任务的AI代理来说，网站的大部分内容可能看起来像噪音，但读者，我不知道该怎么告诉你，那个网页对其他人来说也主要是噪音。

虽然保护LLM有限的上下文窗口是明智的，但这显然不是一个永久性问题。更大的问题在于将代理视为无法整体理解网站。

## 意图工程

最初，使用LLM是关于**提示**；然后是关于**上下文**；现在是关于[**意图**](https://natesnewsletter.substack.com/p/klarna-saved-60-million-and-broke)。因此，假设代理对网络只有提取需求是不正确的。随着LLM变得“更智能”，限制它们的操作方式不是一个好主意。正如我[用 Claude 和 GSD 演示的](https://thenewstack.io/beating-the-rot-and-getting-stuff-done/)，引导LLM的方法是设定一组好的目标，让它自己找出细节。

例如，LLM很有可能判断实际回答“此页面有帮助吗？”的查询将有助于其改进数据源的总体目标。为什么这只能是人类才能做的事情呢？

超市需要你导航到你需要的东西，而老式单柜台商店对用户来说容易得多。现在我们使用送货服务，我们又回到了让一个薪水过低的初级员工去取我们所有的购物商品。但超市模式最接近网站对所有用户的工作方式，并且在购买前浏览类似商品的能力也是代理可以受益的。与其给代理一个要购买的配料清单，不如直接告诉它你想烤一个披萨。换句话说——专注于意图。

## 你的网站也可以对代理和人类更友好

[渐进增强](https://www.gov.uk/service-manual/technology/using-progressive-enhancement)的世界（大约十年前流行）认识到 JavaScript 很好，只要在 JavaScript 不运行的情况下，一切都以相同的方式工作。人类喜欢一个响应悬停的按钮——但这些修饰不应该干扰导航。

虽然一些糟糕的网站会产生奇怪的字母数字谜语作为它们的 URL，但大多数网站确实使用简单且逻辑的结构，如 `/products/items`，这有助于人类和机器人导航。

如果你的网站说“致电获取报价”，我们已经知道 OpenClaw 会这样做。你不能再举手说：“从现在起，只欢迎人类。”所以也许现在是设计得更透明一些的时候了。

如果你发现你需要为机器人提供特定的端点以避免“UI 混乱”，那么最好先解决糟糕的 UI，然后再担心机器人。讽刺的是，大多数 LLM 可以很好地分析、解释和协助创建网站。

## 使用微数据获得有限的胜利

我真的没有注意到 [Schema.org](http://Schema.org) 标记的使用情况，并且为机器阅读器提供内容线索有点过时，因为 LLM 的内部结构本身就是一个庞大的语义关系网络。尽管如此，使用微数据并不昂贵。让我们看一个他们给出的早期电影目录示例：

从没有装饰的开始：

```
<div>
   <h1>Avatar</h1>
   <span>Director: James Cameron (born August 16, 1954)</span>
   <span>Science fiction</span>
   <a href="../movies/avatar-theatrical-trailer.html">Trailer</a>
</div>
```

这可以通过固定范围更好地定义：

```
<div itemscope itemtype="https://schema.org/Movie">
  <h1>Avatar</h1>
  <span>Director: James Cameron (born August 16, 1954)</span>
  <span>Science fiction</span>
  <a href="../movies/avatar-theatrical-trailer.html">Trailer</a>
</div>
```

我没有使用过需要这种帮助的 LLM，但它很可能提高搜索效率。

[Nate Jones](https://www.linkedin.com/in/natebjones/) [说得非常对](https://natesnewsletter.substack.com/p/klarna-saved-60-million-and-broke)：“提示工程告诉AI做什么。上下文工程告诉AI知道什么。意图工程告诉AI想要什么。”

不要将AI代理的网页浏览视为对网页的三角洲部队突袭，其任务是尽快走私信息。退一步，给代理有意义的目标。

另一方面，如果你的网站旨在迷惑用户，并且你担心代理会绕过它，请检查你的先验条件。