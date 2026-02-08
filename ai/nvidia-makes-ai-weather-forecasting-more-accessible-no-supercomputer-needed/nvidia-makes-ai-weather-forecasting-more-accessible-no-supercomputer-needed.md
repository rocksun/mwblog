<!--
title: 英伟达AI气象预测平民化，告别超级计算机
cover: https://cdn.thenewstack.io/media/2026/01/c2d88344-screenshot-2026-01-23-at-10.50.05-1024x610.png
summary: 英伟达发布开源AI天气预报模型，包括中期预报和短时预报，采用Transformer架构，可在单个GPU上运行，大幅降低超算需求，并推出数据同化工具，使企业级高分辨率天气预报更普及。
-->

英伟达发布开源AI天气预报模型，包括中期预报和短时预报，采用Transformer架构，可在单个GPU上运行，大幅降低超算需求，并推出数据同化工具，使企业级高分辨率天气预报更普及。

> 译自：[Nvidia makes AI weather forecasting more accessible, no supercomputer needed](https://thenewstack.io/nvidia-makes-ai-weather-forecasting-more-accessible-no-supercomputer-needed/)
> 
> 作者：Frederic Lardinois

除了极少数[例外情况](https://www.weathercompany.com/)，大规模天气预报一直是拥有大型超级计算机的政府机构的领域。但这种情况正在改变。

英伟达今天发布了两款开源天气预报模型：Earth-2 中期预报和 Earth-2 短时预报。此外，它还推出了一款工具，将显著加快这些模型起始条件的生成速度。

英伟达气候模拟总监[Mike Pritchard](https://www.linkedin.com/in/mikepritchard/)告诉《*The New Stack*》：“天气方面的风险再高不过了。”

“气候变化导致极端天气恶化，正在影响我们所有人以及现代生活的几乎每个方面。天气预报影响着我们所有人。它可以推动农业、能源、航空和应急响应的改进，但预报的科学正在发生变化。”Pritchard说。

Pritchard认为，人工智能引发了“天气预报领域的科学革命”，但研究人员一直在努力将这项工作从实验室推向实际解决方案。“我们需要降低准入门槛，让开发者能够在开放环境中构建工具。”

这并非英伟达首次涉足天气预报业务。作为其构建地球数字孪生项目Earth-2的一部分，它此前发布了两款其他模型。第一款是[Earth-2 CoreDiff](https://build.nvidia.com/nvidia/corrdiff)，一个能够将大陆尺度预测下采样到高分辨率局部预测的模型，速度比传统方法快500倍。第二款是[Earth-2 FourCastNet3](https://developer.nvidia.com/blog/fourcastnet-3-enables-fast-and-accurate-large-ensemble-weather-forecasting-with-scalable-geometric-ml/)，一款高效的全球预报模型，可在单个英伟达H100 GPU上运行。

准确的预报不仅仅是为了决定是否带伞。这些模型是航空公司、保险公司、能源供应商和农业的关键基础设施。

## 英伟达的新天气模型

此前的两款模型——以及大多数其他现有基于AI的预报模型——都使用[专业模型架构](https://arxiv.org/abs/2306.03838)，并且不采用现在已成为现代大型语言模型（LLM）默认方法的Transformer架构。对于新的中期预报和短时预报模型，英伟达正是采用了这种Transformer架构。毕竟，Transformer架构得到了几乎所有其他AI公司的性能和工程工具的支持。

Pritchard说：“从哲学上、科学上讲，这是一种回归简单。我们正在摆脱手工定制的利基AI架构，转向未来简单、可扩展的Transformer架构。”

中期预报模型，顾名思义，旨在提供未来长达15天的高精度预报。

![](https://cdn.thenewstack.io/media/2026/01/1be9e02a-nvidia-weather-model.gif)

*英伟达Earth-2 中期预报模型运行中。（图片来源：英伟达）*

英伟达尚未向《*The New Stack*》提供详细的基准测试数据，但Pritchard认为，中期预报模型在“超过70个气象变量”方面，包括温度、气压和湿度，都优于目前该领域的领导者DeepMind的GenCast。

短时预报模型可能更有趣：它能生成公里分辨率的国家级预报——对于任何现代模型来说，这都是一个非常高的分辨率。欧洲或北美的大多数天气预报模型分辨率为两公里或更高，而美国国家海洋和大气管理局（NOAA）的[GFS模型](https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast)，免费可用且通常是免费天气应用的默认模型，其分辨率为13公里（尽管NOAA最近也已开始[实施AI预报](https://www.noaa.gov/news-release/noaa-deploys-new-generation-of-ai-driven-global-weather-models)）。

以色列气象局计划今后使用短时预报模型，每天生成多达八次的高分辨率预报。该机构已经在使用英伟达较旧的CoreDiff模型。同样，天气公司（weather.com背后的公司）计划将短时预报用于局部恶劣天气应用。

## 无需超级计算机

中期预报模型有多个变体，参数范围从24亿到33亿不等，其训练是在32个80GB A100/H100 GPU上完成的。但要运行该模型，您只需26GB的GPU内存，单个A100 GPU即可运行覆盖6或12小时的单时间步预测。根据模型不同，GenCast模型仅需140秒，另外两个中期预报变体（分别命名为Atlas-SI和Atlas EDM）需要94秒和88秒，而Atlas-CRPS模型（具有额外的噪声条件，参数量稍大，为33亿）则在四秒内完成。

对于短时预报模型，每个6公里分辨率的模型仅需5GB GPU内存，可在单个H100 GPU上以最高精度在33秒内运行。“我们预计推理速度将通过蒸馏和/或降低精度等技术大大加快，”英伟达发言人告诉我们。

## 数据同化：问题的另一半

对于天气预报，模型开始生成预报的起始数据至关重要。这些数据可以是卫星图像、雷达数据、来自气象气球、飞机和浮标的传感器数据。所有这些数据都需要标准化和转换，以便模型能够对其进行处理。

气候科学家称此过程为“同化”。为了加速这个耗时数小时的过程，英伟达还推出了全球数据同化模型，该模型可在几秒钟内生成这些全球天气的初始快照。

Pritchard表示：“尽管AI社区和研究社区在过去五年中大量关注预测模型，但这种数据同化任务，这种状态估计任务，很大程度上仍未通过AI解决，然而它却消耗了传统天气[预报]总超级计算负荷的约50%。”

同化模型实际上相当小，参数量为3.3亿。使用一个H100 GPU，它可以在不到一秒的时间内运行完整的推理流程，同时使用的GPU内存不到20GB。

尽管如此，这些高效模型能否让业余爱好者很快开始创建自己的预测，仍然不太可能——但并非不可能。毕竟，仅仅获取和管理起始数据就是一个重大的数据问题。但对于拥有正确用例和资源的企业来说，这可能为创建本地预报打开大门，而无需访问超级计算集群。