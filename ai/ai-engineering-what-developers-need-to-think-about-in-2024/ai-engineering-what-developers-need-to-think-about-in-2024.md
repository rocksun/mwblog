<!--
title: 2024年开发者人工智能技术思考指南
cover: https://cdn.thenewstack.io/media/2023/12/90fe5532-year-forecast-1-1024x576.png
-->

展望2024年，人工智能技术仍将引领热点。以下几个方面将影响开发者的人工智能工程实践。

> 译自 [AI Engineering: What Developers Need to Think About in 2024](https://thenewstack.io/ai-engineering-what-developers-need-to-think-about-in-2024/)，作者 David Eastman 是伦敦的专业软件开发人员，在甲骨文公司和英国电信任职，并作为顾问帮助团队以更敏捷的方式工作。他写了一本关于UI设计的书，从那时起一直在撰写技术文章......

过去一年，许多[大型语言模型(LLM)](https://thenewstack.io/what-is-a-large-language-model/)项目快速从研究领域冒出。对即将到来的一年，我们要关注的不再是追随趋势，而是首先发现哪些潜望镜会首先抬起。并非一切都与人工智能有关，但至少在未来一年，通常的嫌疑人仍将抢占头条。

我列出了可能通过参与或服务使用影响开发者的下一个项目的领域。其中大多数只是下一个问题领域，或者利益自然碰撞的地方。

## 加快速度，缩小大小和人工智能自生成数据

我们现在已经进入了人工智能的“让成千上万个大型语言模型绽放”时期，数据访问的问题和许多小型运营的大小限制也将随之绽放。

[Wayve](https://wayve.ai/thinking/scaling-gaia-1/)对自动驾驶的解决方案是将视觉信息反馈到模型中，然后可以生成驾驶视频，这些视频然后可以用作训练或预测数据。这是有道理的，因为即使有行车记录仪，对深度学习来说视频源可能还是不够的。但[这需要大量计算](https://thenewstack.io/meeting-the-operational-challenges-of-training-llms/)。

Wayves的系统不是使用词为标记，而是使用图像作为输入标记，就像预测下一个词一样，这里系统预测下一个图像。

正如图所示，该系统查看视觉输入(`image encoder`)和汽车正在做什么(`action encoder`)以帮助通过内部 `world model` 预测下一步:

![放大](https://cdn.thenewstack.io/media/2023/12/68988680-untitled-1024x408.png)

*[那是一只鸡在过马路吗？](https://wayve.ai/thinking/scaling-gaia-1)*

使用更小、更高效的模型是摆脱不断升级大小战争的唯一途径，[另一场芯片短缺](https://thenewstack.io/no-immediate-end-to-chip-shortage-but-hope-for-the-long-run/)可能会加剧这一趋势。另一个角度是，当然，将更小的模型置于移动设备上。因此，预计这一领域的工作将继续进行。

## 更多使您自己的数据可供人工智能使用的应用程序

如果您还记得几年前的“[自我量化](https://thenewstack.io/wearable-silence-suit-helps-create-the-perfect-meditation-experience/)”趋势，您就会明白为何让人工智能利用您的个人数据可能很有价值。这可能只是将聊天界面连接到您的日记，但在健康和生活日志领域可能会出现更智能的协作。

能够就像“本月我比上月睡了多少个小时?”这样的问题询问您的睡眠追踪器，这真的可以帮助您在不盯着图表的情况下做出更好的生活选择。像“我的通勤路线中哪条会受道路施工最少影响?”这样更具体的查询，是让解决方案保持围绕您需要的集中，而不是围绕不断变化的环境。

对于已经拥有您数据的公司来说，这是一个更容易提供的选择。在某些情况下，[ChatGPT趋势](https://thenewstack.io/openais-gpt-4-can-analyze-visual-images-pass-bar-exam/)是一个很好的方式，悄悄暴露他们已经可以这样做，并且一段时间以来就可以做到这一点。

## 自治代理仍将遇到安全和隐私障碍

“代理”一词在人工智能计算中被过度使用。在这里，我使用它来表示使用大型语言模型理解目标、生成任务并尝试完成任务的程序。

但是它们面临的问题与多年来联邦数据所面临的问题相同: 我控制的代理如何获得使用其他人数据的许可？

我不认为代理将取得重大进展，因为它们的[法律和安全边界还没有得到解决](https://thenewstack.io/an-ai-safety-institute-benefits-big-tech-but-little-else/)。更重要的是，尽管我尊重那些努力利用大型语言模型的公司，但他们似乎明显对法律框架不感兴趣。

这可能意味着解决这个问题存在一个利基机会，但经验告诉我，现在还没有人真正有兴趣去解决这个问题。同样，拥有或窃取尽可能多的数据仍然是更好的选择。我们稍后会再次谈到这个问题。

## 人工智能帮助实现边缘的实时监控

英国最近爆出的丑闻之一是流氓水务公司非法向英国河流[排放未经处理的污水](https://www.theguardian.com/environment/ng-interactive/2023/sep/12/unacceptable-how-raw-sewage-has-affected-rivers-in-england-and-wales-in-maps)。检测这种有毒袭击并不需要复杂的设备，但对河流水质的实时监测兴趣明显增加了。

为了控制碳排放和提高效率，我们担心对阳光进行测量以供太阳能电池板使用、城市空气污染和全球各地的交通量等，情况也是如此。

更传统类型的专家系统可以帮助过滤这些数据，但使用[机器学习](https://thenewstack.io/the-ultimate-guide-to-machine-learning-frameworks/)来[自主洞察](https://www.loginradius.com/blog/engineering/ai-and-iot-the-perfect-match/)或改变检测参数可以帮助解决问题。这也推动了数字孪生的增加，它可以实时检测和响应环境。

## 边缘计算和将工作负载放在不同的地方

与前面的两点有些关联，将计算放在离处理数据更近的地方，从而允许在数据实际收集的地方进行计算，这是建立“[边缘人工智能](https://thenewstack.io/edge-ai-how-to-make-the-magic-happen-with-kubernetes/)”中可能开始相当重要的效率优化之一。

这可能是允许更好的移动查询响应的关键。它意味着可以占用更少功耗、延迟更低并且以某种方式最大限度地减少带宽的更小、更紧凑的机器学习模型。

如果您想知道这是否会增加黑客的攻击面——好吧，是的。所以[安全风险](https://thenewstack.io/security/)必须小心翼翼地织入这些集成平台中。

## 首席数据官的更多工作

突然之间，您组织的数据不仅仅具有模糊的战略重要性；它现在可能在未经许可的情况下供电大型语言模型。无论你对[伊隆·马斯克](https://thenewstack.io/vivatech-the-secret-of-elon-musks-success-crystal-meth/)(Elon Musk)的看法如何，他关于如何管理社交媒体平台的决策通常令人困惑的逻辑在这一点上是正确的。其他人[也正在发现这一点](https://arstechnica.com/tech-policy/2023/12/ny-times-sues-open-ai-microsoft-over-copyright-infringement/)。

首席数据官(或等效角色)现在需要制定逃跑或战斗策略，而不仅仅是另一个生态系统游戏。在他们考虑使客户的数据更有价值之前，他们必须确保它不会飞走，如我前面所提到的。这要么涉及锁定数据，要么提供竞争服务。最终，会有法律追索，但对大多数小型组织来说，这会来得太晚。

重要的是，大型语言模型将使用您宝贵的数据。因此，它也可以是您控制的大型语言模型。

## 灭世论者让步

随着人工智能的实际产品并未完全达到炒作的效果，好的一面是[存在风险马戏团](https://thenewstack.io/bryan-cantrill-on-ai-doomerism-intelligence-is-not-enough/)将放慢脚步。通过说某件事有多危险来提高媒体兴趣，让我想起儿童游乐场，而不是真正为人类福祉而努力的严肃事业。

就像Golgafrinchams一样，[道格拉斯·亚当斯](https://www.enotes.com/topics/hitchhikers-guide-galaxy/critical-essays)(Douglas Adams)在他的小说中指出，人类灭绝仍然更有可能是由脏电话传染的瘟疫引起的。在此，我祝您新年快乐。
