<!--
title: 皮克斯 CTO：Vision Pro 的未来和 USD Web Tools
cover: https://cdn.thenewstack.io/media/2024/02/d484fee7-coco-usd-1024x576.jpg
-->

我们采访了皮克斯 CTO Steve May，了解了 USD 的最新发展。USD 是一种开放的 3D 内容标准，正在被 Apple、Meta、Nvidia 等公司使用。

> 译自 [Pixar CTO on OpenUSD, Vision Pro Future, and USD Web Tools](https://thenewstack.io/pixar-cto-on-openusd-vision-pro-future-and-usd-web-tools/)，作者 Richard MacManus 是 The New Stack 的高级编辑，专门撰写有关 Web 和应用程序开发趋势的文章。他于 2003 年创立了 ReadWriteWeb，并将其建设成为全球最具影响力的科技新闻网站之一。从早期...

皮克斯在 2016 年开源了其 3D 图形技术[通用场景描述](https://openusd.org/) (USD)，这距其为自身电影制作目的创建该技术几年后。USD 现已被苹果、Meta 和 Nvidia 等行业巨头采用。**有人将 USD [比作 Photoshop 格式 psd](https://thenewstack.io/the-slow-road-to-metaverse-standards-and-how-ai-fits-in/)**，希望它最终会成为 3D 互联网的默认语言，类似于 HTML 之于万维网的地位。

为了了解 USD 如何在当今使用以及它在“[元宇宙](https://thenewstack.io/openusd-could-enable-a-real-metaverse/)”和“[空间计算](https://thenewstack.io/vision-pro-for-devs-easy-to-start-but-ui-not-revolutionary/)”成为主要流行语的时代如何进一步发展，我采访了皮克斯首席技术官兼非营利性[开放 USD 联盟](https://aousd.org/) (AOUSD) 主席 [Steve May](https://www.linkedin.com/in/stevemay2/)。

## 什么是 USD？它如何使用？

在 AOUSD 今天发布的 [May 个人简介](https://aousd.org/blog/meet-the-visionary-steve-may/)中，USD 被定义为“数字场景中所有元素的通用语言——角色、环境、照明和摄像机运动。”

当我问 May 关于 USD 如何在皮克斯内部使用时，他承认这是一项复杂的技术——但也非常强大和灵活。

“我们不会将所有数据都放入一个单独的实体、一个单独的资产中，”他解释道。“它实际上拥有一张完整的资产网。因此，您可能有一个代表我们一部电影中整个场景的资产，但它有这些触角——这些指向其他资产的指针，例如每个角色的资产、场景设置的资产以及设置中每个道具的资产。”

数字艺术家或开发人员使用 USD 时，他们可以处理特定片段的 3D 内容，然后将其与其他资产连接。

![](https://cdn.thenewstack.io/media/2024/02/b4d1f636-pixar-production-process-1024x740.png)

*Pixar 的生产流程，来自 pixar*

“角色本身也有资产，”May 继续说道，“因为角色可能拥有身体 […] 但它们可能也有单独的 USD 文件用于服装、头发、描述皮肤反射光线的方式。所有不同部分实际上都由数百个 [USD 文件] 组成。”

这意味着皮克斯电影中的单个场景可能拥有数千甚至数百万个单独的 USD 文件。

“因此，USD 的真正强大之处之一，”May 说，“不仅仅在于描述对象的几何形状或决定其外观的材质属性，还在于它可以将所有这些资产以一种连贯的方式组装和连接在一起，并让您轻松编辑各个部分。”

根据 May 的说法，USD 也非常适合构建大型虚拟世界或复杂的 3D 工业应用程序，因为这类产品中“许多事情同时发生和改变”，并且需要大量协作。

“它远不止是描述东西，”他说，指的是 USD 格式。“它还能以一种高效的方式编辑、组装和管理这些非常复杂的资产网络。”

## USD 远远不只是电影制作：苹果、Meta和其他

USD 在 2016 年开源后是如何演变的，皮克斯是否仍然引领开发？

“自從开源后，它的技术也在不断发展，”May 说（他确认皮克斯仍领导开发工作）。“它不是一项成熟的技术。即使它已经相当成熟，我们已经使用了很长时间——它实际上是基于我们在皮克斯几十年来所做工作的——它仍在不断发展。”

May 指出，USD 也在 “使用它和对它感兴趣的人群” 方面发生变化。USD最初开源的想法是允许电影行业的其他公司与皮克斯的管道连接。或者正如 May 所说，USD 是开源的，“这样我们就可以访问新的工具，它们可以理解 USD，然后就可以与其他所有东西一起工作——我们所有在皮克斯的专有工具。”

然而，最终发生的是其他行业也希望采用 USD——从 [Nvidia 的工业 3D 产品](https://thenewstack.io/omniverse-kit-nvidia-metaverse-sdk/)，到 Apple 的[混合现实产品](https://thenewstack.io/apple-lays-foundation-for-mixed-reality-headset-at-wwdc22/)，再到 Meta 建立 3D “元宇宙”的[宏伟愿景](https://thenewstack.io/meta-metaverse-developers/)。

“令我们有点惊讶的是，一些电影行业以外的公司对它的兴趣来得如此之快，”May 说。“其中两个早期参与者，也是开放 USD 联盟创始成员的最大支持者是 Apple 和 Nvidia。他们很早就参与进来，是为了解决完全不同的问题。”

这些不同的公司聚集在 AOUSD，这是一个与 Linux 基金会合作的非营利组织。Adobe 和 AutoDesk 是其他创始成员，但该组织现在也包括 Meta、Epic Games、宜家和其他多个对构建 3D 互联网感兴趣的公司。

## Vision Pro 和使用 Pixar 3D 内容的潜力

今年 3D 内容领域的最大新闻当然是苹果 Vision Pro 头显的发布。我问 May 是否已经试用过它。他回答说他只玩过一点，但已经对其潜力印象深刻。

“我认为它有一些方面确实令人震惊，”他说，“每个人都知道，这只是个开始。对我来说，它让你看到了未来，它会让你重新思考你的工作方式和计算方式。”

他补充说，Vision Pro 可能比之前采用“娱乐作为游戏设备”方法的 VR 设备提供更多功能。

我问皮克斯是否计划为 Vision Pro 开发任何应用程序，甚至将来在 Meta 的 3D 互联网平台上开发应用程序。

“我们是一家工作室，我们非常专注于制作电影——这就是我们的工作，”他回答，“我们制作电影，然后我们是迪士尼这个大公司的一部分，他们帮助我们发行这些电影，并利用这些电影制作主题公园的游乐设施、吸引人的消费产品等等。所以我们目前没有专门的任务去做交互式 AR 或 VR 内容，但我们会使用这些工具来制作电影——例如，我们会使用 VR 进行实地考察。”

然而，他确实承认，皮克斯的母公司迪士尼非常适合为 Vision Pro 等设备制作 3D 内容。他指出，迪士尼首席执行官鲍勃·伊格尔 (Bob Iger) 出席了 Vision Pro 发布活动，展示了迪士尼的互动内容。

“我认为，在讲述故事和让观众以新的方式体验皮克斯角色和皮克斯电影方面，存在着巨大的潜力，”May 说。

## USD 和网络

去年 12 月，AOUSD 制定了最终确定规范的[路线图](https://aousd.org/news/alliance-for-openusd-unveils-roadmap-for-core-usd-specification-and-ecosystem-collaborations/)。其中大部分重点都放在定义核心规范上，但也有一些其他领域正在探索。我特别问到的是网络支持。

“我们正在努力的一件事是让它 [USD] 适用于网络使用，”May 说。“已经有一些示例和原型。事实上，如果你访问苹果的产品网站并查看 Apple Watch，他们有一个功能可以让您从网站上通过 AR 查看它。那实际上是一个你可以在手机上查看的 USD 资产。所以，目前已经有一些功能，但要真正为网络启用它还需要做很多工作。但这正是联盟中的许多人感兴趣支持的事情。”

相关的是，人们还在努力使 USD 创作变得更加简单——就像 1990 年代出现的 HTML 编辑器让编写 HTML 变得更加容易一样。

“你可以直接在文本编辑器中输入 USD，但我们不建议这样做，因为它相当复杂，”May 说。“所以它通常通过编程 API 完成。我没有理由相信我们不会有好的工具来创建这些资产并使它们在网络上可用。我们的目标是，无论是在网络上、在 Apple 的 Vision Pro 等设备上，还是在台式电脑或工作站上，相同的 USD 资产都应该能够在任何这些不同的平台上使用。”
