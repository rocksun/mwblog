
<!--
title: AI编码工具Bolt：是神器还是鸡肋？
cover: https://cdn.thenewstack.io/media/2025/02/16baf448-alex-shuper-ilywf8exiem-unsplashb.jpg
-->

David Eastman 试用了新的 AI 编码工具 Bolt。他发现它在某些方面做得很好，但他渴望更精细的控制。

> 译自 [Introduction to Bolt: Does It Suit Professional Developers?](https://thenewstack.io/introduction-to-bolt-does-it-suit-professional-developers/)，作者 David Eastman。

作为一名开发者，我知道我的责任是创建或使用可维护的解决方案——我们通常认为这意味着以某种方式编写代码，以便将知识传递给其他人类开发者。这种立场不一定会改变，但尝试使用 LLM 以编程方式构建软件，无疑将在越来越多的案例中发挥开发工作流程的一部分作用。

考虑到这一点，我们可能需要习惯于使用乐高积木套件中的组件。所以我尝试了 [Bolt.new](https://Bolt.new)，它承诺“提示、运行、编辑和部署全栈 Web 应用程序”。我不确定我是否会获得“代理体验”，或者[这是否仍然被认为是编码工具](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/)。以下景观视图中的定义将 Bolt 定位为前者：

![](https://cdn.thenewstack.io/media/2025/02/372ba7b9-image-1024x576.png)

那么，让我们开始使用 Bolt 进行构建。使用 GitHub 登录后，起始页面非常醒目：

![](https://cdn.thenewstack.io/media/2025/02/38016efe-image-1-1024x843.png)

首先，让我们确定要构建的内容的一些要求。我想构建一个博客，首页显示我的最新条目。我想要一列缩略图，在右侧显示以前的条目。我假设我的导语（第一段）将用作带有缩略图图像的文本。每篇文章都将有一张“英雄”图片。这些都很标准。

我不确定我是否有“最喜欢的堆栈”，但这可能是学习新站点构建器的好方法。它实际上建议使用 Astro，它构建于 [Vite](https://vite.dev/) 之上——尽管现在博客的设计在任何地方都足够简单。

一旦我选择了 Astro，我们就会在左侧得到一个聊天框，在右侧得到代码和预览。Astro 开始设置：

![](https://cdn.thenewstack.io/media/2025/02/5c75cded-image-2-914x1024.png)

Bolt 从未告诉我我将在*哪里*工作——在云端还是本地？由于有一个聊天框，我询问了 Bolt，它澄清说：

![](https://cdn.thenewstack.io/media/2025/02/ccbea912-image-3.png)

这很好也很有趣。当然，这意味着实际上获取我的代码可能会存在问题或障碍。但目前，我假设我的兴趣是构建。

我在预览选项卡中看到了一个不错的 Astro 博客入门模板，在另一个选项卡中看到了代码。因此，很明显，我的体验将完全由 Bolt 调解——即使我位于 Astro 的页面上。

![](https://cdn.thenewstack.io/media/2025/02/2be82619-image-4-1024x276.png)

为了看看我们现在有什么，我点击了大的部署按钮，这在聊天框中得到了中继。这是与 Netlify 合作完成的，Netlify 为此与 Bolt 建立了合作伙伴关系。所以我得到了一个不错的个性化 URL 来检查当前的工作：

![](https://cdn.thenewstack.io/media/2025/02/40998457-image-5-750x1024.png)

现在我们将模板与我之前指定的内容进行比较。在博客页面上，缩略图的格式不太符合我的要求：

![](https://cdn.thenewstack.io/media/2025/02/50443c9e-image-6-1024x723.png)

我想使用导语作为主要视觉风格，以及带有日期的小得多的图像。没有标题。博客内容采用 Markdown 格式，标题、导语（命名描述）、日期和英雄图片放置在 front matter 中。

所以我们需要看看布局。

通过左侧窗格浏览文件，我遇到了 src/pages/blog/index.astro 中博客缩略图的描述：

![](https://cdn.thenewstack.io/media/2025/02/04cbe1dd-image-7.png)

当我开始编辑时，页面在我输入时不断向上滚动。当然，我问 AI 这种奇怪行为的原因是什么，但它没有帮助。

因为编辑器只是一个网页而不是 IDE，所以我真的没有太多控制权。我正在 MacBook 上使用 Chrome，所以这可能是问题所在。但至少我的页面有一个 URL，所以我可以立即尝试另一个浏览器：Safari。当然，我必须重新登录，让 Safari 向我显示弹出窗口，并重新验证。最终，我得到了这个，这非常具有讽刺意味：

![](https://cdn.thenewstack.io/media/2025/02/37bddc59-image-8-300x223.png)

因此，我用来检查错误的浏览器可能并不理想，而我离开的浏览器是推荐的。我的问题解决了吗？没有。大约从第 50 行开始，任何编辑尝试都会使代码向上滚动到我的光标上方。至少我可以关闭 Safari。

我没有找到任何关于此的参考，所以我认为这是一个最近的错误。

现在你可能会说，“当然，这个想法是用聊天来改变一切，而不是自己做”，你说的有道理。

首先，我要求 Bolt 更改每个博客的第一个导语，以便它们不都具有相同的 ipso lorem 拉丁文。它做到了：

![](https://cdn.thenewstack.io/media/2025/02/41cde5de-image-9-1024x582.png)

然后我要求将日期的颜色和字体与描述的颜色和字体交换。它做到了，但也颠倒了我对位置的其他更改并删除了标题：

![](https://cdn.thenewstack.io/media/2025/02/7eccf127-image-11-1024x825.png)

这里的结论不是与 LLM 进行细粒度的语言战斗，而是让 LLM 进行大的更改，同时稍后修复细节。我也在与滚动错误作斗争。但是滚动错误将由（人类）开发者修复。LLM 的态度无法由 Bolt 控制，因为他们不构建模型。
好的，我们可以轻松地调整日期位置和行距。

我希望它显示在一列中，并最终显示在一个页面上。Bolt 再次完成了这项工作，但在没有询问我的情况下更改了其他模板部分，尽管它告诉我它正在这样做：

![](https://cdn.thenewstack.io/media/2025/02/d0377879-image-12.png)

![](https://cdn.thenewstack.io/media/2025/02/48d7e2b2-image-13.png)

最后，我们希望博客在首页上，旧帖子列表显示在当前帖子的旁边。在提出这最后一个要求之后……

![](https://cdn.thenewstack.io/media/2025/02/289f3668-image-14.png)

……主要的更改完成了，在宽屏幕上显示的效果正是我想要的。

![](https://cdn.thenewstack.io/media/2025/02/151b0463-image-15-1024x726.png)

然后我可以恢复我的样式更改。

## 结论

现在，当我在与系统作斗争时——它显然无法读取我的想法——它尽了最大努力在保持博客看起来像*它认为*好看的博客网站的同时，进行我的更改。

这就是问题的关键；如果本质上你想让外部来源来维护整体外观，这将对你有效。如果你想要细粒度的控制，那么这种方法显然行不通。我认为混合方法会有效——但这显然需要更多的训练。

除了滚动错误之外，我认为 Bolt 操作 Astro 以完成我的任务的能力相当强大——它完成了繁重的工作。此外，Bolt 的布局允许我查看聊天结果、代码和预览，这非常好。总的来说，这是一个好的开始；现在的问题是如何以一致的方式整合人的角色。
