# Markwhen介绍：面向开发者的Markdown时间线工具

![Markwhen介绍：面向开发者的Markdown时间线工具的特色图片](https://cdn.thenewstack.io/media/2024/12/a9f3d4a6-diana-light-fpbtaoqvi-k-unsplashb-1024x576.jpg)

作为一名开发者，[我喜欢Markdown](https://thenewstack.io/obsidian-and-the-case-for-using-more-markdown/)。有人反对使用它，理由是其格式并非强制执行——例如，它允许存在不同的版本和名称相似的模式。然而，它的弱点也是它的优势。这就引出了[Markwhen](https://www.notion.so/Markwhen-152ba3b27486804f8093c832a18cafc6?pvs=21)，它自称是一个“文本到时间线工具，你可以编写类似Markdown的文本，它会将其转换为美观的级联时间线或其他可视化效果”。

因此，Markwhen既是一种时间格式，也是一个显示甘特图式时间序列或级联时间线的编辑器。它还有一个Obsidian插件，我稍后会尝试使用。服务设计师在研究Markwhen时，也可以深入了解处理时间表示的复杂性。

## 一个事件
表达的基本单位是*事件*，它由日期范围和冒号分隔的描述组成。然而，相当多的内容都可以作为“日期”运行。所有这些对于Markwhen来说都是可接受的事件：

- “12/2012: 世界末日”
- “1961: 1960年之后的一年”
- “2020-02-22T12:13:14Z-now: 疫情持续了多久？”
- “1892/2021-08-12: EDTF日期范围示例”

这相当宽松，所以我们需要更仔细地看看发生了什么。

## 让我们把它变成日期
Markwhen处理的是*日期范围*，但如果我们只提及一个日期，它会查看粒度并将边缘标记为范围。因此，对于“1961”，定义的范围是1961年1月1日至1961年12月31日。

Markwhen理解常用的易于阅读的日期格式：

- “04/1776” 将是1776年4月
- “11/11/2024-12/12/2024” 将是11月11日至12月12日。

我们稍后可以处理是否使用美国月份/日期/年份格式。

由于我们将要查看日期，让我们熟悉一下[扩展日期/时间格式(EDTF)](https://www.loc.gov/standards/datetime/)，Markwhen也使用它。

这些内容指的是日期：

- “1985-04-12” 指的是1985年4月12日的日历日期。
- “1985-04-12T23:20:30” 指的是1985年4月12日23:20:30的本地时间。
- “1964/2008” 是一个44年的范围。
- “2004-02-01/2005-02” 是一个以日期开始但以月份结束的时间间隔。因此，这是一个比你想象中模糊得多的时期定义。
- “2004-02-01/2005” 同样以日期开始，但以年份结束。

Markwhen也理解“now”和相对日期。幸运的是，有一个[playground](https://docs.markwhen.com/parser/playground.html)可以输出JSON，所以我们可以检查不同的事件。

因此，对于事件“12/2012: 世界末日”，你可以从JSON中获得几个有用的片段：

```
123456789101112131415
"firstLine": { "full": "12/2012: End of the world", "datePart": "12/2012", "rest": " End of the world", "restTrimmed": "End of the world" }, ... "metadata": { "earliestTime": "2012-12-01T00:00:00.000Z", "latestTime": "2013-01-01T00:00:00.000Z", "maxDurationDays": 31, ... }
```

这是一个相对日期，当我刚才询问“1 year: When is this”时，输出结果清楚地说明了它的含义，即星期五下午6点12月。

```
123456789101112131415
"firstLine": { "full": "1 year: When is this", "datePart": "1 year", "rest": " When is this", "restTrimmed": "When is this" }, ... "metadata": { "earliestTime": "2024-12-06T13:26:19.958+00:00", "latestTime": "2025-12-06T13:26:19.958+00:00", "maxDurationDays": 365, ... }
```

所以它显然是从现在开始的一年。

## 前置 matter
正如你所想象的，向这个工具提供一些关于预期格式的提示会有所帮助。幸运的是，Markwhen可以读取[前置 matter](https://gohugo.io/content-management/front-matter/)，它在许多Markdown文档的开头。因此，为了修复欧洲格式，我们可以使用：

```
12345
---
title: My Timeline
dateFormat: d/M/y
#Travel: blue
---
```

第三个条目是一个*标签*，在前置matter中，你可以表达你希望任何可视化效果在表达该事件时使用的颜色。只需将标签放在事件的末尾即可应用它。

## 最后一些可视化效果
虽然我们可以在首页[app](https://markwhen.com/)上试用Markwhen的格式、输出和可视化效果，但我们真正想要使用的是专业编辑器[Meridiem](https://docs.markwhen.com/interface/overview.html)来展示更多内容。我下载了这个应用程序，但它也[在这里](https://meridiem.markwhen.com/example)可以在网上使用。

这个例子中唯一额外的东西是*部分和组*，它们是不言自明的可视化组织者。当你点击日期范围时，日历就会弹出。

## Obsidian
因此，我们最终会在现有应用程序中使用这项技术——毕竟，这是它能够在现实世界中运行的最终证明。记住，唯一可移植的数据是 Markwhen 代码；目前，您受到支持它的应用程序数量的限制。幸运的是，Obsidian 就是其中之一。

在我的 1.7.7 版本 Obsidian 中，通过设置，我打开了社区插件并关闭了受限模式：

由此，我可以浏览最近更新的 Markwhen：

侧边栏显示 Markwhen 图标，我们可以从中开始一个新文件。

我一启动前置 matter，它就提供了一个不错的助手。

这项相当简单的努力……

……产生了这张图表：

（当然，这只是为了说明目的）时间跨度都可以像您预期的那样进行操作。


## 如果不是现在，是什么时候？

这最近才由公开发布，所以它的发展方向和应用场景还有待观察。例如，有一个 VS Code 扩展程序。网络应用程序编辑器不是开源的，但其余部分似乎是开源的。

显然，这需要发展成为一个拥有足够解决方案的生态系统，才能站稳脚跟。提到正在开发一个使用该格式组织帖子条目的博客应用程序。他还提到了 iCal 集成，这将是一个好主意。在 Markwhen 能够普及之前，开发者需要准备好现成的附加组件，以便他们可以使用这些附加组件来增强自己的产品。

为了完全成功，Markwhen 必须自下而上地与库一起工作，也必须自上而下地与应用程序一起工作。无论哪个方向首先出现，都已经提供了时间轴的优势。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)