# Tailwind CSS 辩论：又一款被网络纯粹主义者贬低的酷工具

就像 React 一样，CSS 工具 Tailwind 经常在 Web 开发者圈子中进行辩论。它非常受欢迎，但也有它的反对者。

翻译自 [Tailwind CSS Debate: Another Cool Tool Dissed by Web Purists](https://thenewstack.io/tailwind-css-debate-another-cool-tool-dissed-by-web-purists/) 。

![](https://cdn.thenewstack.io/media/2023/08/93ef3e5a-portrait-3373374_1280-1024x806.jpg)
*图片来自 Pixabay*

本周早些时候，Matt Rickard 写了一篇题为“[为什么 Tailwind CSS 胜出](https://matt-rickard.com/why-tailwind-css-won)”的文章，该文章登上了 [Hacker News](https://news.ycombinator.com/item?id=37143837) 的首页。不可避免地，这引发了关于一种受欢迎的 Web 开发工具的社交媒体上的最新一轮两极分化的意见。令人惊讶的是，一些人喜欢 Tailwind，而另一些人讨厌它。

每一方的理由也都很熟悉：喜欢它的开发者认为 Tailwind CSS 节省了他们的时间，易于学习，而不喜欢 Tailwind 的开发者则认为它“不尊重” Web 平台。将 Tailwind 替换为 React，或者几乎是当今任何其他流行的基于 JavaScript 的工具，你都会得到相似的相反意见。

## 争议点在哪里？

作为开发者的框架，[Tailwind CSS](https://tailwindcss.com/) 相当容易理解。基本上，它允许你将 CSS 样式代码嵌入到你的 HTML 代码中，正如 Tailwind 的口号所说：“在不离开 HTML 的情况下快速构建现代网站。”因此，它使开发者不必从 HTML 切换到 CSS 样式表。

[Tailwind 自己的文档](https://tailwindcss.com/docs/utility-first)指出了对这种方法的常见反对意见：“这不就是内联样式吗？”那些来自 20 世纪 90 S年代的人会记得，在 CSS 革命兴起之前，必须向 HTML 文件添加样式标记。但根据 Tailwind 的说法，它的“实用类”方法提供了比内联样式更多的功能，包括响应式设计（适用于移动友好设计）。

因此，易于使用（特别是与编写和维护 CSS 文件相比）以及在 HTML 中进行样式设置的能力是许多开发者喜欢 Tailwind 的主要原因。在他的文章中，Matt Rickard 还将“可复制粘贴”、“更少的依赖关系，更小的表面”和“可重用性”作为该框架的关键优点。

至于批评者，他们对 Tailwind 的不喜欢的总体主题是，它以某种方式“不尊重所依赖的平台”，正如 [Jared White 最近](https://thathtml.blog/2023/08/tailwind-death-of-craftsmanship/)在[一篇文章](https://www.spicyweb.dev/why-tailwind-isnt-for-me/)中所说的那样。当我向他询问时，他把我引导到了他早些时候的一篇文章，概述了他的具体批评意见。简要总结一下：他认为 Tailwind “推广了丑陋的 HTML”，他不喜欢为 Tailwind 构建的“CSS 文件是非标准的（也就是专有的）并且与所有其他 CSS 框架和工具基本不兼容”，他认为“Tailwind 忽略了 Web 组件的存在”，最后，他认为它“鼓励了div/span 标签的混合”。

简而言之，**Tailwind 具有丑陋的标记并且是非标准的**，这似乎是 Jared White 和其他 Tailwind 批评者的核心抱怨。Jeff Sandberg 在他最近的博客文章中提到了类似的抱怨，[反对 Tailwind](https://pdx.su/blog/2023-07-26-tailwind-and-the-death-of-craftsmanship/#the-death-of-craftsmanship)。Sandberg 在文章中提到了关于 Tailwind 兴起以牺牲直接编写 CSS 的更大问题：“Tailwind 是我认为在开发中更大问题的症状。开发中的自豪感迅速恶化。”

## 那么，谁是对的...

Tailwind的创作者 Adam Wathan 毫无疑问多次在像 X/Twitter 这样的平台上与人辩论。我浏览了一些最近的帖子，但他发布的这张 Macho Man Randy Savage 的 GIF 似乎总结了他的立场：

![（GIF显示了Macho Man Randy Savage的表情）](https://cdn.thenewstack.io/media/2023/08/cf673ccc-tailwind_savage.jpg)

很诱人地把这场关于 Tailwind 的辩论看作是又一场“酷工具与网络纯粹主义者”的争论（通常意味着双方永远不会对对方说的任何话达成一致）。

一方面，我不会责怪任何实际的 Web 开发者想要使用最简单的可用工具，并且一个可以与其他工具很好地集成的工具，例如，Tailwind 可以[与 Next.js 一起使用](https://tailwindcss.com/docs/guides/nextjs)。这是对 Web 开发的实用主义方法；而且在某些情况下，如果项目已经使用了 Tailwind，他们刚刚加入团队，开发者甚至可能没有选择的机会。

另一方面，偏离现有的 Web 标准（不管多么微妙）可能会在今后成为问题。如果你不再直接使用 CSS 文件，而是使用[类似 Tailwind 的抽象层](https://thenewstack.io/css-frameworks-in-vogue-but-dont-forget-style-fundamentals/)，那么这是否意味着你不太可能理解底层技术？

我认为 Google 的 Una Kravets 在最近的 X/Twitter 关于 Tailwind 的辩论中恰如其分地总结了这一点。“Tailwind 可以是一个很好的解决方案，”她在六月份[发推文](https://twitter.com/Una/status/1664752942526742531)说。“问题出现在人们认为如果他们学会了 Tailwind，他们就不需要学习 CSS，这最终会限制他们。”

## 将 Tailwind 辩论与 React 之争进行比较

与过去几年一直存在的[关于 React 的争论不同](https://thenewstack.io/2023-web-tech-check-in-react-performance-pwas-ios-browsers/)，Tailwind 的争论略有不同。有足够的证据表明，React 实际上对 Web 有害，主要是因为它对浏览器的负载很大，这可能导致许多用户的性能问题。

由于 React 导致网页中不必要的 JavaScript 数量，这甚至可以被视为一种伦理问题。来自微软 Edge 团队的 Alex Russell [去年底写道](https://infrequently.org/2022/12/performance-baseline-2023/)，“网站继续发送比 80% 以上的世界用户合理的脚本更多的脚本，拉大了富人和穷人之间的差距。”

然而，在 Tailwind 的情况下，似乎没有对最终用户造成任何损害。Tailwind 的批评者抱怨的部分是审美问题（“丑陋的标记”），部分是 Tailwind 据称对 Web 开发工艺所做的事情（非标准方法）。

当我询问 Web 开发者 Paul Scanlon 有关这场辩论时，他对 Tailwind 的批评者进行了简短的回应。“我已经写了将近 20 年的 CSS，它很糟糕，总是难以维护，你的也是一样，”他说。“至少 Tailwind 标准化了糟糕的东西。”

我可以证明处理 CSS 文件的困难——最近，我正在研究我的 Web 2.0 技术博客 ReadWriteWeb 的多个CSS文件，并惊讶于那些文件有多么复杂。但那是大约 15 年前的事了，CSS 从那时起已经改进了。或者至少，Jeff Sandberg 认为是这样。“我看到其他工程师，不论级别如何，都陷入了糟糕的 CSS 中，所以对他们来说，也许 Tailwind 看起来像是一种救星，”他在他的文章中写道。“但是 CSS 现在更好了。它不是完美的，但比以往任何时候都要好，比 Tailwind 更好。”

Sandberg 恳请开发者再次尝试 CSS。也许他们会在完成了使用 Next.js 和 Tailwind 这些酷工具的一天的有偿工作之后这样做。
