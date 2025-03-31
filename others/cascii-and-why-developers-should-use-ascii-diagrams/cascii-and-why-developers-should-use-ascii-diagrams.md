<!--
title: Cascii和开发者应该使用ASCII图的原因
cover: https://cdn.thenewstack.io/media/2025/03/55b2e003-viktor-forgacs-iv72ujcnptw-unsplashb.jpg
summary: 这款爆火 ASCII 图表编辑器 Cascii，让开发者重拾代码注释和文档编写的效率！基于原生 JavaScript，支持 Unicode 和纯 ASCII 切换，轻松绘制流程图。通过 URL 分享，复制粘贴无缝衔接，告别 Visio 等复杂工具，拥抱轻量级 ASCII 艺术，提升云原生时代开发体验！
-->

这款爆火 ASCII 图表编辑器 Cascii，让开发者重拾代码注释和文档编写的效率！基于原生 JavaScript，支持 Unicode 和纯 ASCII 切换，轻松绘制流程图。通过 URL 分享，复制粘贴无缝衔接，告别 Visio 等复杂工具，拥抱轻量级 ASCII 艺术，提升云原生时代开发体验！

> 译自：[Cascii and Why Developers Should Use ASCII Diagrams](https://thenewstack.io/cascii-and-why-developers-should-use-ascii-diagrams/)
> 
> 作者：David Eastman

“开发人员经常使用 ASCII 图表吗？”

这篇文章是对这个编辑挑战的回应。起因是听说了 [Cascii 应用](https://cascii.app/)，并反思了这样一个事实：开发社区仍然没有一种非常有效的方式来制作和分享简单的图表。

Cascii 本身是一个非常简洁的美国信息交换标准代码 (ASCII) 编辑器，或者，[正如该项目本身所描述的](https://github.com/casparwylie/cascii-core)，**“一个用原生 JavaScript 编写的基于 Web 的 ASCII 和 Unicode 图表构建器。”** 它没有依赖项、打包或库。

你可以直接访问 [托管应用](https://cascii.app/)，或者通过下载 HTML 并在浏览器中打开来运行你自己的本地版本：

![](https://cdn.thenewstack.io/media/2025/03/413a3567-image-2-1024x207.png)

这将使你开始使用浅色主题版本，该版本使用 Unicode。在“设置”中，你可以更改为深色模式并切换到纯 ASCII。

关于 Unicode 与 ASCII 的说明：Unicode 是一种通用的、可变长度的编码，它包含了大多数语言——你会注意到当该模式开启时，会出现一些更漂亮的箭头和虚线效果。虽然 Unicode 为你提供了更多的符号可供使用，但它远不如标准化且更古老的 ASCII 那样可靠。

Cascii 的托管版本允许你保存绘图并通过 URL 分享它们——你可以在你复制的图表的底部看到这些 URL。

![](https://cdn.thenewstack.io/media/2025/03/d575c4d4-screenshot-2025-03-28-at-14.39.05-1024x496.png)

如果你最近使用过图像编辑器，那么使用 Cascii 应该没有任何问题。你可以创建形状组件、线条连接器和文本。你可以选择、然后调整大小、复制和移动这些组件（但是，我无法移动菱形）。你可以将组件移到后面或前面，尽管我无法想象有什么需要这样做。

一个简单的流程图可以用正方形、菱形、线条和文本很快完成。真正的启示来自于当你点击“导出”按钮时，Cascii 会将你的图表复制到你的粘贴缓冲区中。瞧。

我将我的第一次尝试复制到我的 Warp 终端中，只是为了证明它只是 ASCII 艺术：

![](https://cdn.thenewstack.io/media/2025/03/9c395d05-image-1024x617.png)

你可以直接访问显示的 URL 并加载它。但是我的图表有点笨拙，所以我制作了一个更小的版本用作艺术。在我们开始使用它之前，让我们看看你可能实际遇到过 ASCII 图表或艺术的地方。

## 开发者在哪里使用 ASCII？

如果你查看 [Cascii GitHub README.md 页面](https://raw.githubusercontent.com/casparwylie/cascii-core/refs/heads/main/README.md) 的原始 markdown，你将看到它们在三个反引号之间的结构图
，这是 GitHub Markdown 方言，用于将文本格式化为它自己独特的块。我也可以在 WordPress 中做到：

```
                                   ┌╶╶╶╶╶╶╶╶╶╶╶╶╶╶┐
                                   │ GroupManager │ 
                                   └╶╶╶╶╶╶╶╶╶╶╶╶╶╶┘
               ┌─────────────┐    /                  ┌─────────────┐
               │EventManager │   /           ┌───────│SquareLayer  │
               └─────────────┘  /            │       │─────────────│        ┌───────────────┐
                      \        /             │───────│CircleLayer  │   ┌────│SwitchLineLayer│
                       \      /              │       │─────────────│   │    │───────────────│
                        ┏━━━━━━━━━━━━┓       │───────│BaseLineLayer│◀──┐────│FreeLineLayer  │
                        ┃LayerManager┃◀──────┘       │─────────────│   │    │───────────────│
                        ┗━━━━━━━━━━━━┛       │───────│DiamondLayer │   └────│StepLineLayer  │
        ┌────────────┐ /      /       \      │       │─────────────│        └───────────────┘
        │CharManager │/      /         \     │───────│FreeLayer    │
        └────────────┘      /           \    │       │─────────────│
                           /             \   └───────│TableLayer   │
                     ┌────────────┐       \          └─────────────┘            Pixels!
                     │ ModeMaster │        •
                     └────────────┘      •   •                                     ▲
                                       •       •                                   │
                                     •           •                                 │
                                   •   CanvasCom   ────────────────────────────────┘
                                     •           •
                                       •       •
                                         •   •
                                           •
Edit/view: https://cascii.app/7c24a
```

当然，也有一些常见的表情包以 ASCII 艺术的形式出现。所以，我可以用 ASCII 艺术做一个 git check out 笔记。也许“掀桌子”这个梗就是从这里来的：

# (╯°□°）╯︵ ┻━┻

基本的图表经常出现在代码注释中——通常是系统流程图或网络图。在使用 VIM 的开发者中，或者至少在使用 Courier 等等距（固定间距）字体的 IDE 中，这些都很容易辨认。

在过去，即使是简单的图像渲染也需要配备好的显卡的机器，ASCII 艺术代表了一种易于分享的默认方式。只有像样的字体控制以及最终的表情符号才逐渐侵蚀了它的使用。最终，开发人员可以使用 Microsoft Visio 等工具，这是一种图表和矢量图形应用程序，几乎无处不在。虽然 Visio 仍然存在，但它是一种更复杂的工具，更受架构师和营销人员的青睐。

## Cascii：适合绘制图表

让我们回到我的流程图示例的更简单版本：

```
                  +                       
                /   \                       
+---------+   /       \           +--------+
|         | /           \         |        |
|  Start! |+   Continue? +--------|  Done! |
|         | \           /         |        |
+---------+   \       /           +--------+
                \   /                       
                  +                         
                  |                         
                  |                         
                  |       +---------+       
                  |       |         |      
                  +-------| Cancel  |       
                          |         |       
                          +---------+       
 
Edit/view: https://cascii.app/02e0e
```
现在你可以复制这段文字并直接粘贴到 Cascii 中。差不多了。当你最终在浏览器上看到这段文字时，它已经被处理过很多次，可能与原始版本略有不同，也许会丢失一个重要的换行符。但是，如果你把它放到像 Warp 这样的终端程序中，然后再粘贴到 Cascii 中，你可能会看到这个图表：

![](https://cdn.thenewstack.io/media/2025/03/8f174c04-screenshot-2025-03-28-at-14.03.16-1024x531.png)

还有一些其他的工具可以将图像转换为 ASCII 格式，或者更大的东西，比如 [playscii](https://jp.itch.io/playscii)，它们更专注于完整的艺术创作。但 Cascii 似乎在简单绘制图表方面独树一帜。

## 为什么开发者应该使用 ASCII

虽然借助像 Cascii 这样的工具，创建、共享和重新编辑 ASCII 图像仍然相对容易，但敌人是媒体在我们在消息、社交媒体和文档形式中移动文本时经常经历的快速格式转换。此外，如果不遵循行尾和定位的命运，就很难保证固定宽度、多行 ASCII 的效果，否则它很容易被破坏。

优势在于完整循环的灵活性，从创建图表到通过复制和在需要时重新编辑进行共享。所有这些步骤都不需要任何工具——在文本可以存在的任何地方进行多次小的更新更改才能发挥它们的真正效率。如果 ASCII 图表绘制在代码上方并与代码一起存储，那么它更容易与代码“共存”。

因此，本文开头提出的问题的真正答案是，开发人员可以并且应该使用 ASCII 图表，但要获得完全的灵活性，他们可能需要在具有类似工具的团队中工作。在这种情况下，他们不妨同意使用相同的现代图表工具。只是碰巧没有真正简单的图表工具是开发人员都认可的，因此像 Cascii 这样的工具可以填补易于维护的轻量级案例的角色。

┳━┳ ヽ(ಠل͜ಠ)ﾉ