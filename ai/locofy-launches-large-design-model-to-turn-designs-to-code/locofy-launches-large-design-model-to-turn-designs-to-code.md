<!--
title: Locofy发布设计转代码的“大设计模型”，
cover: https://cdn.thenewstack.io/media/2024/01/0288569c-arthur-mazi-fexeynymo2y-unsplash-1024x683.jpg
-->

Locofy全新“大设计模型”（LDM）让用户通过轻松点击按钮将网页设计转化为前端代码。我们采访了创始人。

> 译自 [Locofy Launches ‘Large Design Model’ to Turn Designs to Code](https://thenewstack.io/locofy-launches-large-design-model-to-turn-designs-to-code/)，作者 Richard MacManus 是 The New Stack 的高级编辑，撰写关于 web 和应用程序开发趋势的文章。此前，他于2003年创立了 ReadWriteWeb，并将其建设成为世界上最有影响力的科技新闻网站之一。从早期...

Locofy是一款专为前端开发人员设计的工具，通过一个Figma插件主要将设计转换为代码。这家总部位于新加坡的公司刚刚宣布了一款名为Locofy Lightning的新产品，该产品基于一种包含自定义技术的堆栈，称为“大设计模型”（LDM）。据该公司称，LDM使用户能够在仅需一次点击的情况下将Web设计转换为前端代码。

为了弄清楚LDM究竟是什么以及[Locofy](https://www.locofy.ai/)如何帮助前端工程师，我采访了两位联合创始人，[Honey Mittal](https://www.linkedin.com/in/honeymittal/)（首席执行官）和 [Sohaib Muhammad](https://www.linkedin.com/in/msohaib/)（首席技术官）。

Mittal解释说，公司成立于2021年，其产品的第一个版本，现在称为“Locofy Classic”，是一个多步骤的过程，需要“学习曲线”。但是，使用新产品Lightning，将设计转换为代码只需一次点击，尽管在产品推出后不久仍然需要一些微调。

“通过Lightning，我们只是想让它变得非常简单，无论某人的背景或资历如何，获得前端代码80%的准备工作应该只是一次点击的事情，”Mittal说道。

这对创始人向我展示了Lightning的演示。示例是一个类似Airbnb的Figma构建的用户界面，显示了伴随着图片的属性列表。当点击魔术的Lightning按钮时，模型被转换为一个完全响应式的网站（此过程大约需要40-50秒）。转换后，Lightning允许您检查生成的代码的任何元素，以便根据需要进行调整。

![](https://cdn.thenewstack.io/media/2024/01/b6f4cc8c-locofy2-1024x433.jpg)

*Locofy设计到代码的过程。*

## LDM 是什么以及是否使用 LLM？

从用户角度来看，将一个简单的 Figma 设计转变为响应迅速的网站，不到一分钟的时间，令人印象深刻。但是这是如何实现的，Locofy 的 "Large Design Model" 又在哪里发挥作用呢？

“它的运作方式是，在后台运行各种 AI 模型，” Mittal 说道。他随后澄清说，它的功能远不止与[现有的 LLM](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/) 互动那么简单。

“我们对LLM的使用不到5%，” 他继续说道。“因为我们关注的不是文本，而是视觉。因此，我们必须构建自己的 'large design models'，利用数百万设计、数百万网站、数百万由我们自己创建的自动设计，来理解和选择合适的模型。”

Mittal 补充说，他们仅在几周前将 LLM 引入 Lightning 栈中，用于一些小型用例，例如帮助命名设计中的图层。对于这类小事情，他们使用了 LLM 的混合：Mistral、OpenAI 和 LLaMA。

但是转换的繁重工作是由 Locofy 的定制 LDM 完成的。这需要机器学习工程师数月的工作来创建，每个工程师都处理设计到代码流程的不同部分。

“在我们的 LDM 中，我们基本上使用了七到八种不同的技术，”Mittal 说道。“流程的每个部分都使用了不同的技术。我们花了七到八个月的时间来研究哪种技术在哪里起作用。我们将继续投资。我们推出的 LDM（大设计模型）是起点。”

因此，LDM 是通过混合图像识别、语义分析和其他 AI 技术创建的。

## LDM 如何创建响应式网站

我看到的演示是将 Figma 设计转换为完全响应式的网站。Lightning 还可以处理 Adobe XD 设计，Mittal 补充说，对其他工具的支持，如 Penpot 和 Canva，正在计划中。他表示，Penpot 整合肯定会在今年实现，但 Canva 还没有最终确定。

我询问是否可以将使用单一图像格式（如 PDF 或 JPG）的模型转换为网站。Mittal 表示这是可能的，尽管这“需要一些工作”。然而，总体而言，这种转换并不是 Locofy 关注的重点。

![Zoom](https://cdn.thenewstack.io/media/2024/01/c3879ea9-locofy1-1024x497.jpg)

*Locofy 展示。*

“一些公司过去尝试过这样的转换，” 他在后续的电子邮件中解释说，“但目前看起来可能是一个稍微较小的问题，因为设计师现在可以轻松制作高保真模型。我知道有些公司这样做，但这可能迎合的是由设计师阻塞的设计师和非设计师。目前我们的重点是设计师与开发者之间的桥梁，从金钱的角度来看，这是一个更痛苦/昂贵/耗时的过程。”

假设您正在使用 Figma 或 Adobe XD 设计，将设计转换为代码的第一步之一是审查结构。

“设计师可以以任何方式构建他们的设计，”首席技术官 Sohaib Muhammad 告诉我。“因为当您查看设计时，它看起来是完美的 - 但在幕后，可能有许多冗余的图层、许多不必要的帧或组。因此，我们使用我们的 AI 模型，以开发者理解的方式重新组织一切。”

Mittal 表示，LDM 还可以识别某个元素是什么类型，即使（例如）它只是设计中的一个矩形框 - 它可能是表单的输入框，也可能是一个按钮。LDM “可以区分看起来相似的项目，它们本质上只是带有文本和图标的矩形”，他说。

除了找出元素，LDM 的另一个重要任务是将设计转换为完全响应式的网站。

## Locofy 与 Vercel 的 v0 之间的区别

将设计到代码转换背后的引擎命名为“LDM”是一种巧妙的营销手段，考虑到当前的人工智能热潮。但我注意到有些公司似乎走得更远，通过帮助开发人员仅通过描述以文本创建用户界面。其中一个明显的例子是 [Vercel 的 v0](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/)，它使用了一个几乎同样出色的营销术语（“[Generative UI](https://vercel.com/blog/announcing-v0-generative-ui)”）。我问 Locofy 与那种类型的人工智能产品有何不同。

Mittal首先指出，你可以将Vercel用作使用Locofy创建的网站或应用的部署平台，因此在这方面是互补的。至于v0，他认为它适用于“简单的仪表板[在那里]你甚至不需要设计师，你只需指定某些尺寸，它将自动为你生成按钮的最基本版本，或者输入的最基本版本。”

他希望Locofy专注于已经制作好模型的设计的前端代码。

“我们说，无论您是使用设计师还是AI进行设计，我们都不在乎。我们关心的是，您给我们一个设计，我们将完成前端工程师的80%的工作。”
