
<!--
title: CSS布局：老派Div居中大法
cover: https://cdn.thenewstack.io/media/2025/12/fcfa36f5-1304-sa-bushwick-phetus88.jpg
summary: 互联网早期`<center>`标签易用但被弃用。现在主要用CSS和`<div>`实现网页内容居中和多列布局。早期方法繁琐，CSS Grid和Flexbox简化了问题，但旧代码仍在使用。
-->

互联网早期 `<center>` 标签易用但被弃用。现在主要用CSS和`<div>`实现网页内容居中和多列布局。早期方法繁琐，CSS Grid和Flexbox简化了问题，但旧代码仍在使用。

> 译自：[CSS Layout: How To 'Center a Div,' the Old School Way](https://thenewstack.io/css-layout-how-to-center-a-div-the-old-school-way/)
> 
> 作者：Joab Jackson

互联网早期，在网页上居中放置内容非常容易：只需在其上放置一个 `<center>` 标签。

然而，当 [World Wide Web Consortium](https://www.w3.org/about/) (W3C) [将 HTML](https://frontendinterviewquestions.medium.com/center-tag-in-html5-9b7ab0ff0a46) 修订到 4.0 版本时，它出于对[关注点分离](https://www.w3.org/TR/html-design-principles/)的热情，弃用了 center 标签。易用性为[架构纯粹性](https://www.w3schools.com/html/html_xhtml.asp)而牺牲。而内容居中不知何故成了 [层叠样式表](https://www.w3.org/Style/CSS/Overview.en.html)的领域。

这被证明是个问题，因为没有直接替代那个有效但架构不正确的 center 标签的东西。W3C 提供了一系列新的布局元素（*header*、*nav*、*aside*），但这些都无助于程序员在页面内部调整元素的比例。

“研究了网格布局之后，你可能会惊讶这一切看起来是多么复杂！”Mozilla 开发者页面在网络社区最初采用的现已过时的方法上[实际指出](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Legacy_Layout_Methods)。

公平地说，将内容放在网页的“中间”是一个哲学难题，因为 HTML 网页的画布实际上是无限的。它没有两侧，没有顶部或底部。因此，中间必须由开发者放置在页面上的任何画布来定义（如果他们 überhaupt 意识到自己应该这样做的话）。

> Divs “通过为项目指定大小并将它们推来推去，以使其看起来像网格一样对齐，”
>
> – Mozilla 开发者网络文档。

对于像网络这样号称民主的技术来说，这是一个很大的要求。它让许多网页设计师陷入了长达十多年的困惑之中，直到 [CSS Grid](https://thenewstack.io/get-grid-last-css-grid-template-markup/) 和 [CSS Flexbox](https://thenewstack.io/open-source-leaders-thomas-park-hops-easy-css-development-flexbox-froggy/) 的出现才简化了问题。

尽管如此，整整一代网站都是在没有 Grid 或 Flexbox 的情况下构建的，如今无疑仍有许多管理员不愿触碰用于居中定位的旧有且非常繁琐的代码，生怕一个多余或放错位置的标签就会破坏他们整个网站的设计。

因此，有一种使用 Grid 或 Flexbox 在网页上居中元素的方法，它是从社区生成的最佳实践中整合而来的。这一切都围绕着 HTML 的 *<div>* 标签展开。

## Div 的作用是进行分区

HTML *[<div>](https://www.w3schools.com/tags/tag_div.ASP)* 标签定义了网页文档中的一个节或一个分区。

在 HTML 文档的层级结构中，Div 元素紧随 *<body>* 之后，就像 *<body>* 紧随 *<head>* 之后并在层级上位于顶级 *<html>* 标签之下一样。

此文件包含隐藏或双向 Unicode 文本，其解释或编译方式可能与下面显示的不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

| | |
| --- | --- |
| | /\*插入到 HTML 文档的头部文件\*/ |
| | |
| | <head> |
| | <style> |
| | div { |
| | display: block; |
| | } |
| | </style> |
| | </head> |

你可以将每个 *<div> </div>* 组合视为一种容器，通过为 *<div>* 添加 **class** 或 **id** 属性，你可以用 CSS 对其进行样式设置（或用 JavaScript 进行操作）。[id](https://www.w3schools.com/html/html_id.asp) 属性指向网页中的一个特定 *<div>*；而 [class](https://www.bing.com/videos/riverview/relatedvideo?q=html+class+attribute&mid=AE045DAA6DEBA1D7C9F0AE045DAA6DEBA1D7C9F0&FORM=VAMTRV) 可以应用于多个 *<div>*。

因此，*<div>* 可以被赋予一个类名，浏览器将为该类的所有成员执行相应的操作。

此文件包含隐藏或双向 Unicode 文本，其解释或编译方式可能与下面显示的不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

| | |
| --- | --- |
| | <html> |
| | |
| | <head> |
| | <style> |
| | .red-text {background-color:red} |
| | </style> |
| | </head> |
| | |
| | <body> |
| | <div class="red-text">"Soul Kitchen"</div> |
| | </body> |
| | </html> |

**ID** 的工作方式类似，只是它们使用[井号而不是单个前导点作为标识符](https://gist.github.com/joabj/9f714841776afecde24daea061d58b27)。

因此，在页面上居中内容的最简单方法是使用 *<div>* 标签定义一个内容区域。

正如 Kevin Powell 在这个有用的视频中[解释](https://www.youtube.com/watch?v=ULVu2VNM_54)的那样，许多开发者实际上将这个 *<div>* 称为容器。使用 **class** 或 **id**，他们将该容器的**宽度**设置为该网页分配大小的 50%（一半）。随着浏览器窗口大小的变化，容器保持相应的 50%。

此文件包含隐藏或双向 Unicode 文本，其解释或编译方式可能与下面显示的不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

| | |
| --- | --- |
| | <html> |
| | |
| | <head> |
| | <style> |
| | .container {width: 50%; /\*Sets the size of the container as |
| | a percentage of overall page \*/ |
| | margin: 0 auto; /\*Margin above and below the content text set to 0; |
| | and left/right margin is claculated by the browser\*/ |
| | } |
| | </style> |
| | </head> |
| | |
| | <body> |
| | <div class="container">Tell me, O Muse, of the man of many devices, who wandered full many ways after he had sacked the sacred citadel of Troy. Many were the men whose cities he saw and whose mind he learned, aye, and many the woes he suffered in his heart upon the sea, seeking to win his own life and the return of his comrades. Yet even so he saved not his comrades, though he desired it sore, for through their own blind folly they perished—fools, who devoured the kine of Helios Hyperion; but he took from them the day of their returning. Of these things, goddess, daughter of Zeus, beginning where thou wilt, tell thou even unto us. Now all the rest, as many as had escaped sheer destruction, were at home, safe from both war and sea, but Odysseus alone, filled with longing for his return and for his wife, did the queenly nymph Calypso, that bright goddess, keep back in her hollow caves, yearning that she might have him to her husband.</div> |
| | </div> |
| | </body> |
| | |
| | </html> |

CSS 的 [**width**](https://www.w3schools.com/cssref/pr_dim_width.php) 属性也可以用像素的固定长度来设置（尽管在改变窗口本身大小时，固定长度可能会有问题）。

在上面的代码片段中，[**margin**](https://www.w3schools.com/css/css_margin.asp) 属性设置了文本与容器侧边之间的间距。第一个数字（“0”）设置文本的上下间距，第二个（此处设置为“auto”）是文本的左右外边距。如有必要，这些外边距可以用长度或百分比更精确地指定。

确保所有调用的类都使用直引号（“），而不是弯引号。

上述代码将示例文本居中显示在页面上：

[![网页上居中的文本。](https://cdn.thenewstack.io/media/2025/12/33aecbc3-div-center.jpg)](https://cdn.thenewstack.io/media/2025/12/33aecbc3-div-center.jpg)

令人难以置信的是，这是所有浏览器都能接受的，在网页上居中放置内容的*最简单方式*。

可惜的是，大多数网页设计师需要的居中方式远不止于此。

## 在浏览器窗口中平衡多列

不过，首先要绕道进入 [CSS float 属性](https://www.w3schools.com/css/css_float.asp)的世界。**float** 属性最初是为在盒子内定位图片而设计的。如果图片小于盒子，它应该向右、向左、向上还是向下对齐？

但绝望的网页开发者发现，**float** 却可以用来定位任何 HTML 元素。也就是说，它可以在容器 *<div>* 中定位较小的 *<div>*。

一个两列的网页可以由两个 div 组成，一个向左浮动，另一个向右浮动。它们需要在比例上保持平衡，以免大于容器，或者像太多猫围着一个食盆一样，它们不会互相挤压，导致你的网站变得不平衡。你需要自己计算这些数字。

此文件包含隐藏或双向 Unicode 文本，其解释或编译方式可能与下面显示的不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

| | |
| --- | --- |
| | <html> |
| | |
| | <head> |
| | <link rel="stylesheet" href="styles.css"> |
| | <style> |
| | .container {width: 90%; |
| | max-width: 700px; /\* A hard-limit maximum size for the container \*/} |
| | |
| | .left { |
| | width: 48%; /\*That's 48% of the 100% allocated to the container \*/ |
| | float: left; |
| | background-color: red; |
| | } |
| | |
| | .right { |
| | width: 48%; |
| | float: right; |
| | background-color: orange; |
| | } |
| | |
| | .clearfix { |
| | clear: both; |
| | } |
| | </style> |
| | </head> |
| | |
| | <body> |
| | <div class="container"> |
| | |
| | <div class="left"> |
| | <h2>First Column</h2> |
| | <p> |
| | Chicken |
| | </p> |
| | </div> |
| | |
| | |
| | <div class="right"> |
| | <h2>Second Column</h2> |
| | <p> |
| | Waffles |
| | </p> |
| | </div> |
| | |
| | <div class="clearfix"></div> |
| | |
| | </div> |
| | </body> |

在上述示例中，容器设置为浏览器窗口的 90%，两个 div 各占容器 *<div>* 分配的 100% 中的 48%。其中一个浮动到右侧，另一个浮动到左侧。

上述代码在页面上的渲染效果如下：

[![CSS 渲染的两列。](https://cdn.thenewstack.io/media/2025/12/d4da6c6e-two-columns.jpg)](https://cdn.thenewstack.io/media/2025/12/d4da6c6e-two-columns.jpg)

请注意，由于浏览器计算 *<div>* 大小的方式存在缺陷，应该添加一个名为 [Clear Fix](https://www.w3schools.com/howto/howto_css_clearfix.asp) 的补丁，同样也是一个 *<div>*。我不知道它是如何工作的，但这是 W3C 规定的。

那么三列布局呢，许多网站（包括 TNS 本身，在 [WordPress](https://thenewstack.io/wordpress-turmoil-and-the-fair-package-manager/) 的帮助下）都偏爱这种布局？最好的方法是调整 div 的属性，看看它们在浏览器窗口中如何堆叠。

此文件包含隐藏或双向 Unicode 文本，其解释或编译方式可能与下面显示的不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

| | |
| --- | --- |
| | |
| | <html> |
| | |
| | <head> |
| | <link rel="stylesheet" href="styles.css"> |
| | <style> |
| | .container { |
| | width: 90%; |
| | margin: 0 auto; |
| | } |
| | |
| | |
| | .column { /\*a class to set the attributes that will be applied to all the columns\*/ |
| | float: left; |
| | padding: 10px; /\* Padding will be added to the width \*/ |
| | box-sizing: border-box; /\*Needed for setting width with padding/border \*/ |
| | } |
| | |
| | .left { |
| | float: left; |
| | width: 25%; |
| | background-color: red; |
| | } |
| | |
| | .middle { |
| | width: 50%; |
| | background-color: white; |
| | } |
| | |
| | .right { |
| | float: right; |
| | width: 25%; |
| | background-color: blue; |
| | } |
| | |
| | .clearfix { |
| | clear: both; |
| | } |
| | </style> |
| | |
| | </head> |
| | <body> |
| | <div class="container"> |
| | |
| | |
| | <div class="left column"> |
| | <h2>First column</h2> |
| | <p> |
| | Navigation column |
| | </p> |
| | </div> |
| | |
| | |
| | <div class="middle column"> |
| | <h2>Second column</h2> |
| | <p> |
| | The Feature Well |
| | </p> |
| | </div> |
| | |
| | <div class="right column"> |
| | <h2>Third column</h2> |
| | <p> |
| | A column for ads. |
| | </p> |
| | </div> |
| | |
| | <div class="clearfix"></div> |
| | |
| | </div> <!--Wrapping up the container div--> |
| | |
| | </body> |

在上面的示例中，左右两列都赋予了 **float** 方向，分别将它们移动到右侧和左侧，而中间一列没有赋予 **float**，因此它位于中间。

上述代码中还有一个名为 column 的新类，它允许 *<dev>* 定义所有列都相同的属性。请注意每个元素如何由多个类定义（即“left column”实际上是两个类）。

上述代码将如下渲染：

[![一个三列布局的示例。](https://cdn.thenewstack.io/media/2025/12/15a9037a-three-columns.jpg)](https://cdn.thenewstack.io/media/2025/12/15a9037a-three-columns.jpg)

正如所指出的，如今使用 [Grid](https://www.w3schools.com/css/css_grid.asp) 和/或 [Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) 可以更轻松地渲染多列布局，我们将在未来的教程中介绍这些。不过，就目前而言，你可以为自己是少数真正了解如何居中 *<div>* 这一古老难题的开发者之一而感到自豪。