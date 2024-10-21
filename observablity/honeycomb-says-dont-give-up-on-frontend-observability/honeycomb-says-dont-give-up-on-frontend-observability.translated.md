# Honeycomb 呼吁不要放弃前端可观测性

![Featued image for: Honeycomb Says Don’t Give Up on Frontend Observability](https://cdn.thenewstack.io/media/2024/10/db65cc62-olivie-strauss-olllcdnwqrg-unsplash-1-1024x680.jpg)

[Honeycomb](https://www.honeycomb.io/?utm_content=inline+mention) 强调了前端可观测性缺失是不可接受的，并指出其解决方案很大程度上借鉴了 [OpenTelemetry](https://www.youtube.com/watch?v=I-dAQfzR2Vs&ab_channel=Honeycomb)，并发布了 [Honeycomb for Frontend Observability](https://www.honeycomb.io/frontend-observability) 的通用版本。

借助该工具，Honeycomb 工程师设计了用于调试核心 Web 指标 (CWV) 并精确定位原因的工具——Honeycomb 在一篇博文中声称，“无论它们出现在堆栈中的哪个位置”，都可以通过跟踪和其他数据来实现。Honeycomb 还表示，它提供“数千个”免费的自定义属性。

问题在于，实时用户监控 (RUM) 工具对于访问前端的 [遥测数据](https://thenewstack.io/exploring-telemetry-idf-2016/) 至关重要。但 [调试工具](https://thenewstack.io/debugging-software-using-generative-ai/) 通常缺乏。Honeycomb 表示，当涉及到实际调试 Web 应用程序中的问题时，您通常只能将浏览器开发者工具的输出拼凑在一起，并从客户支持工单中获取一些细节（如果您幸运的话），以便在本地复制问题，希望能够识别问题的根源。

Honeycomb 的高级产品经理 [Winston Hearn](https://www.linkedin.com/in/winston-hearn/) 之前曾在大型媒体公司担任工程师，负责调试 Web 性能问题。“我们经常遇到这个问题——所有现有的 RUM 工具都收集 CWV 指标，这有助于大致识别存在问题，但不会提供任何关于原因或所需修复的有效上下文，”Hearn 告诉 The New Stack。“在 Honeycomb，我们与客户的工程团队密切合作，确保他们拥有将问题归结到具体原因所需的数据，从而将调试时间从数小时或数天缩短到几分钟。”

如果没有合适的工具，调试核心 Web 指标 (CWV) 以提高分数可能会更糟糕。Honeycomb 表示，实际上任何资产或第三方服务都可能影响页面的性能，因此缩小影响指标范围是一个反复猜测和检查的过程。

## 更深入的分析和审查

虽然字段可以按任何一组标准进行划分，但确定哪些字段对于更深入的分析和审查至关重要。这是 Honeycomb for Frontend Observability 的一项关键功能。Honeycomb 在 [演示](https://www.youtube.com/watch?v=I-dAQfzR2Vs&ab_channel=Honeycomb) 中展示了，在检查累积布局偏移值较差的情况时，并选择 BubbleUp 后，Honeycomb 会分析所有三个字段并绘制图表，从差异最大的字段开始。黄色条表示结果较差，并且似乎在加载完成后出现。它们位于主页上，这是一个有用的信息。是什么元素导致了它们？Honeycomb 表示，可以通过任何属性进行进一步调查。

正如演示所揭示的那样，Honeycomb 提供的其他信息可能包括能够提出更多问题，例如：哪些后端请求最慢，更重要的是，为什么它们很慢？通过过滤到购物车页面并选择其中一个慢速请求，Honeycomb 会显示从前端到后端服务的分布式跟踪中的请求。此瀑布视图揭示了哪些内容很慢。似乎存在明显的网络延迟，但后端速度很快。跟踪显示了所有涉及的服务以及它们如何协同工作。Honeycomb 表示，由于它是从浏览器开始的分布式跟踪生成的，因此可以理解整个系统。

Honeycomb 传达了 Honeycomb for Frontend Observability 提供的其他功能，包括：

- Honeycomb 将前端连接到其背后的“所有内容”，提供用户体验的完整视图。借助 OpenTelemetry，可以揭示创建“丰富事件”所需的遥测数据。
- 访问所有字段和高基数值，涵盖应用程序开发。可以使用所有必要的上下文来监控指标，以改进它们。

除了标准的 OpenTelemetry 自动检测之外，还添加了数十个属性，包括 CWV 属性数据和用户交互数据（例如点击）。Honeycomb 表示，这使得能够清楚地了解影响用户体验的内容以及需要改进的地方。

Honeycomb 中的自定义属性是免费的。可以添加任何相关的自定义数据，例如用户身份验证状态、入口页面类型或流量来源。还可以整合来自 Fullstory 和 Amplitude 等其他工具的数据，提供来自相关数据的丰富见解，默认数据保留期为 60 天。
乍一看，Web Launchpad 类似于流行的 RUM 仪表板，提供诸如 CWV 之类的常见性能数据的可视化。

Honeycomb 具有两个主要组件：开源仪器包和 Web Launchpad。Honeycomb 网络仪器包是 OpenTelemetry 网络仪器的开源包装器，提供了一种与供应商无关的方式，可以在不到一小时的时间内对 Web 应用程序进行仪器化。根据 Honeycomb 文档，它允许将有关每个用户交互及其周围环境的实时数据直接发送到 Honeycomb。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。