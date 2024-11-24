# Nue：一个挑战 Next.js 的新静态站点生成器

![Nue：一个挑战 Next.js 的新静态站点生成器](https://cdn.thenewstack.io/media/2024/11/fe236261-getty-images-fv_jinocbla-unsplashb-1024x576.jpg)

这场战争进展如何？这场对抗糟糕的缓存、缓慢的加载时间、安全漏洞、可扩展性问题、SEO，或者这个月我们在 Web 开发时被告知必须对抗的任何问题的战争。Web 开发是一个创新的跑步机，如果你想跟上，就永远无法真正离开。

回顾新的 Web 技术类似于回忆战争的时间线。我们在客户端有 HTML、CSS 和 Javascript。这很快，但很难开发。然后我们有了 [React](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)，它使操作文档对象模型 (DOM) 的可重用组件成为默认设置。我们被告知使用声明式方法比命令式方法更好。然后我们有了使用 React 构建的 [Next.js](https://nextjs.org/)（和 [Vue.js](https://vuejs.org/)），它默认使用服务器端渲染，但也允许使用客户端方法进行静态站点生成和 [JAMstack](https://thenewstack.io/jamstack-style-build-a-website-with-netlify-and-publii/)。诸如此类。

现在我们有了 [Nue](https://nuejs.org/blog/nue-release-candidate/)，它是一个“针对渐进增强进行优化的内容优先框架”。 正如我们[上周](https://thenewstack.io/angular-version-19-scheduled-to-release-tuesday/#nue)报道的那样，它已经发布了[候选版本一](https://nuejs.org/blog/nue-release-candidate/)。渐进增强在哪里适用？这是一条旧原则，即您的站点应该适用于所有浏览器，CSS 和 JavaScript 仅用于增强功能。 这最终意味着您的站点应该能够在没有 JavaScript 的情况下工作——但我怀疑这在今天是否是一个合理的期望。

现在，立即吸引我的地方是它似乎是 [markdown](https://thenewstack.io/obsidian-and-the-case-for-using-more-markdown/) 优先的。这确实鼓励了设计主导的方法。Nue“目前未在 Windows 下进行测试或开发”，这取决于你站在哪一边，这要么没问题，要么不严肃。我总是从我的 MacBook 开始，所以这对我来说没问题。

## 开始

好的，我愿意加入这场新的战斗。让我们开始[基础训练](https://nuejs.org/docs/installation.html)。

我不知道“Bun”是什么；显然它是一个组合的捆绑器和 JavaScript 运行时，Nue 推荐使用它。

所以首先安装 Bun。这很快：

```
# Installation command omitted as it was not provided in the original text
```

它礼貌地将自己添加到我的脚本中。因此，启动一个新的 [Warp](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) shell，我使用 Bun 安装 Nue 本身：

```
# Installation command omitted as it was not provided in the original text
```

…并创建模板项目：

```
# Project creation command omitted as it was not provided in the original text
```

最终，它启动了一个服务器，并将我带到了 [http://localhost:8083/](http://localhost:8083/) 的站点。

这个网站速度很快，设计也很漂亮。这个模板项目，一个博客，对大小变化的反应很灵敏：

![Responsive Blog Image](/path/to/image.png)  *(Placeholder for missing image)*

我很期待看到[这是如何组成的。](https://nuejs.org/docs/tutorial.html) 但让我们先看看项目结构。

如果我们剪切图像、CSS 和 JavaScript，只查看博客内容目录，我们就能了解其结构：

```
# Directory structure omitted as it was not provided in the original text
```

通常，我们得到一个 `*.dist*` 输出开发目录，显示 Markdown 文件 (.md) 被转换为 HTML 文件。我们还可以看到一些无疑包含元数据的 YAML 文件。另外，请注意 `*@global/layout.html*`。

事实上，`*site.yaml*` 似乎包含了非常具体的布局选项：

```yaml
navigation:
  header:
    - Emma Bennet: /
    - Contact: /contact/
  footer:
    - © Emma Bennet: /
    - image: /img/twitter.svg
      url: //x.com/tipiirai
      alt: Twitter (X) profile
      size: 22 x 22
    - image: /img/github.svg
      url: //github.com/nuejs/nue/
      alt: Github Projects
      size: 22 x 22
    - image: /img/linkedin.svg
      url: //linkedin.com/in/tipiirai
      alt: LinkedIn profile
      size: 22 x 22
```

页脚（我没有在上图中捕获）开始看起来像这样： *(Placeholder for missing image)*

我自然很想知道是否可以进行一个相当明显的更新。添加 BlueSky svg 后： *(No code provided)*

并编辑 site.yaml：

```yaml
# Updated site.yaml content omitted as it was not provided
```

这立即更新了页脚： *(Placeholder for missing image)*

不客气！这也为我们提供了 Nue 声明式性质的线索。

页眉和页脚是通过 `*@global/layout.html*` 和 `<navi>` 标签排列的：

```html
# HTML code omitted as it was not provided
```

它们读取 `*site.yaml*` 中的数据并从中创建这些页脚项。您已经可以看到 HTML 和 CSS 作为略微二等公民被隐藏在楼梯下。这很适合我，但可能会让更多代码优先的开发人员感到不安。

让我们深入了解更多内容细节。Nue 文档站点似乎没有搜索功能，因此您需要使用 Google 来深入了解详细信息。
Nue 以 Markdown 文件作为内容的主要形式；它支持标准的 Markdown，并在其基础上进行了大量的扩展。这意味着，如果您了解 Markdown（您应该了解），您只需要注意一些细微的差异即可。让我们看一下首页 *index.md*；请注意，我的 Warp shell 可以轻松打开 Markdown 文件并并排渲染：

我们看到三个短划线之间的“front matter”元数据和显然用作容器的“page-list”块标签。front matter 提到了“blog”内容集合。这对应于包含博客条目的 *blog* 文件夹。让我们看一下最新的条目：

front matter 用于在页面列表中为条目创建一个小的框，包含“thumb”图像和标题文本，我们在上面的网页上看到了这些内容。它在输出目录中创建了这个 *index.html* 文件：

```html
<li> <a href="/blog/class-naming-strategies.html"> <figure> <img src="/blog/img/dashboard-thumb.png" loading="lazy"> <figcaption> <time datetime="2024-03-13T00:00:00.000Z">March 13, 2024</time> <h2>CSS class naming strategies for scaleable dashboard design</h2> </figcaption> </figure> </a> </li></ul>
```

您可以在网页图片中的最后一个博客条目中看到结果。如果您点击进入，博客条目本身包含一个大的 hero 区域，我们可以看到：

这在可重用的 *blog/hero.html* 中指定；它有一些用于变量的模板：

```html
<header @name="pagehead"> <h1>{ title }</h1> <p> <pretty-date :date="pubDate"/> • Content by AI • Photo credits: <a href="//dribbble.com/{ credits }">{ credits }</a> </p> <img :src="og" width="1000" height="800" alt="Hero image for { title }">
```

您可以看到它从 Markdown front matter 中提取了“title”和“credits”的值。请注意 `:date` 和 `:src` 也是绑定。

## 岛屿（Islands）

Islands 的目的是作为动态组件位于原本静态的 HTML 中。Nue 允许混合使用服务器和客户端，并且可以使用[Web 组件](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/)。这些也被认为是集成 React 组件的理想方式，因此这可能是那些想要从其他服务器端项目迁移过来的人的起点。

## 结论

抛开文档略显夸张的写作方式，我确实喜欢 Markdown 优先的方法——即使这仅仅意味着将工作文件分开保存。还有很多其他的概念需要深入研究，但这种以设计为主导的方法可能是开发人员跳槽的唯一原因。然而，对于一个年轻的项目来说，这已经对 Web 开发有了新的看法。

[YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示以及更多内容。](https://youtube.com/thenewstack?sub_confirmation=1)