
<!--
title: 亚马逊黑五备战：大数据预测
cover: https://cdn.thenewstack.io/media/2025/11/8b294ee9-puzzle-creative-v4ncwsb6a_u-unsplash.jpg
summary: 亚马逊工程师在Kubecon会议上提出，在处理全球性服务时，仅靠反应式扩展不足以应对流量激增。他们采用预测建模，结合平均流量时间（MTT）和突破点TPS（每秒事务数）等指标，提前规划容量以平衡成本和服务可用性。内部系统CloudTune能实时更新预测，应对突发事件。
-->

亚马逊工程师在Kubecon会议上提出，在处理全球性服务时，仅靠反应式扩展不足以应对流量激增。他们采用预测建模，结合平均流量时间（MTT）和突破点TPS（每秒事务数）等指标，提前规划容量以平衡成本和服务可用性。内部系统CloudTune能实时更新预测，应对突发事件。

> 译自：[How Amazon Prepares for Black Friday: Predictive Modeling](https://thenewstack.io/how-amazon-prepares-for-black-friday/)
> 
> 作者：Joab Jackson

亚特兰大 — 在亚马逊工程师们于上周在亚特兰大举行的 [Kubecon + CloudNativeCon NA](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) 会议上，两位工程师建议，在运行面向全球的服务时，对需求的增长做出反应意味着你已经落后了。

这两位亚马逊工程师在主题演讲中描述了该公司如何在不打破预算或导致服务不佳的情况下，为应对客户流量的大幅激增做好准备。

随着 [黑色星期五](https://thenewstack.io/sre-tips-to-prepare-for-black-friday/) 即将到来，他们的建议可以帮助其他电商零售商确保即使在极端压力下也能保持上线和运行。

[![](https://cdn.thenewstack.io/media/2025/11/d9fa8caf-kubecon25-artur_souza-chunpeng_wang-300x225.jpg)](https://cdn.thenewstack.io/media/2025/11/d9fa8caf-kubecon25-artur_souza-chunpeng_wang-300x225.jpg)

*Kubecon 25：亚马逊的 Artur Souza 和 Chunpeng Wang（右）。图片：TNS*

简而言之，反应式扩展（即在负载接近容量时增加服务器的标准做法）对于这些流量高峰期是必需的，但却不足够。

亚马逊首席工程师 [Artur Souza](https://www.linkedin.com/in/barbalho/) 解释说：“这还不够。当你的监控系统检测到 CPU 使用率过高并触发扩展操作时，你已经落后了，并且你的大部分客户已经受到影响。”

因此，这家零售巨头转向了预测建模。

## 准备应对黑色星期五等高峰流量事件

每年，该公司都会经历几次周期性的流量高峰，其中最引人注目的是黑色星期五，每年工程师都会估计这些高峰的规模。在美国，黑色星期五是感恩节后的第一天，很多人不上班，渴望开始为即将到来的假期购物季购物。

黑色星期五的购物实际上从星期四晚上就开始了，届时该公司看到了流量的立即增长。流量会在夜间有所回落，但第二天会再次回升。周末流量会趋于平稳，但周一（通常称为黑色星期一）会再次飙升。

[![](https://cdn.thenewstack.io/media/2025/11/40ae891c-amazon-peak-traffic.png)](https://cdn.thenewstack.io/media/2025/11/40ae891c-amazon-peak-traffic.png)

*上面图表中显示的初始峰值太陡峭，仅靠反应式扩展是不够的。*

在这些情况下，亚马逊学会了预先运行备用容量。

工程师们解释说，这些事件具有“**巨大的峰均比**”，这意味着用户数量的峰值远远高于平均数量。

而所有这些用户都是潜在的付费客户。因此，当如此多的用户如此迅速地涌来时，亚马逊希望能够容纳所有人，以免损失收入。

## 醒醒，宝贝：新的亚马逊性能指标已发布

该公司的一个有用指标是**平均流量时间** (MTT)，它基本上是指通过 [容器](https://thenewstack.io/containers/) 或 [无服务器](https://thenewstack.io/serverless/) 启动一项新服务实例以开始接受用户所需的平均时间。MTT 用于反应式扩展，以根据每个实例的 CPU 使用率来确定何时需要下一个实例。

主动扩展需要另一个重要指标：**突破点 TPS**（每秒事务数），即一项服务实例在违反其 [服务水平协议](https://thenewstack.io/slo-vs-sla-whats-the-difference-and-how-does-sli-relate/) (SLA) 之前的可处理事务数。SLA 是由业务所有者预先定义的满意性能阈值（例如，将商品添加到购物车的耗时）。

[![](https://cdn.thenewstack.io/media/2025/11/d8ef592e-amazon-breaking_tps.png)](https://cdn.thenewstack.io/media/2025/11/d8ef592e-amazon-breaking_tps.png)

Souza 说：“所以我们希望在那个极限点准确地喊出我们的突破点，即使服务没有崩溃，或者即使错误率没有增加。”

TPS 与预期的流量业务预测相结合。每个服务所有者还可以使用其他独立变量来修改预测。

Souza 说：“所有这些都提前计算好了，所以你知道你需要什么样的容量。”

[![一张描述扩展选项的幻灯片](https://cdn.thenewstack.io/media/2025/11/07c9b48e-amazon-scaling-options.png)](https://cdn.thenewstack.io/media/2025/11/07c9b48e-amazon-scaling-options.png)

即使是无服务器函数也有 MTT，在这种情况下，它是响应你需求的时间。 [亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention) 甚至为用户创建了一个选项，让他们可以 [预热他们的 DynamoDB](https://aws.amazon.com/blogs/database/pre-warming-amazon-dynamodb-tables-with-warm-throughput/) 表，以便它们能够应对突然的流量需求。

## CloudTune：亚马逊的预测流量系统

亚马逊高级应用科学家 [Chunpeng Wang](https://www.linkedin.com/in/chunpeng-claude-wang/) 解释说，这些高峰时段预期流量的预测“指导着我们所做的一切”。他介绍了该讲座的模型预测部分。

这些预测不仅用于估算待命的服务数量，而且从长远来看，甚至用于估算未来数据中心的容量以及何时应该建造它们。

通常，基础设施团队会在预期的激增事件发生前大约一个月准备好额外的容量。然后，他们会对额外的实例进行压力测试，以检查其准备情况，识别出可能运行过热的服务。还会准备一个备用容量池。

[![显示预测的聊天](https://cdn.thenewstack.io/media/2025/11/4ff5e243-amazon-scaling-forecasts.png)](https://cdn.thenewstack.io/media/2025/11/4ff5e243-amazon-scaling-forecasts.png)

## 平衡基础设施成本和服务可用性

Wang 表示，对于这些事件，亚马逊必须确定基础设施成本和服务可用性风险之间的最佳平衡点。

它可以为这些高峰事件提供所有可用的容量，这将是有效的，但非常昂贵。但如果它没有准备足够的基础设施，那么服务缓慢甚至中断可能会发生。

Wang 说：“我们花在基础设施上的钱越多，客户影响就越小；我们花的钱越少，客户受影响的风险就越高。就是这么简单。”

这正是预测发挥作用的地方。每年，该公司都会为今年的流量制定一个统计范围，而不仅仅是一个单一的估计。然后，它会选择一个百分位数，例如第 90 百分位数，作为风险与成本权衡点，然后根据该估计来配置容量。

## 扩展复杂的互联服务

考虑到亚马逊的客户交易涉及多个服务，服务可用性的估算可能特别棘手。当潜在客户开始购物时，他们会使用搜索服务，当他们找到喜欢的东西时，就会调用购物车服务。如果一切顺利，那么各种支付和物流服务就会启动。

这些服务中的每一个可能反过来调用其他服务（如数据库）来获得支持。

每项服务都有其自身的性能特征和潜在瓶颈。因此，该公司还必须确定扩展级别的一致性，或者一组相互关联的服务启动所需的时间。这被称为**扇出比**。亚马逊也在其预测模型中使用此比率，并在服务修改导致这些比率发生变化时进行更新。

## 在现场活动期间实时调整预测

2015 年，亚马逊工程师根据亚马逊中央经济学团队的指导方针，构建了预测未来流量模式的软件，称之为 [CloudTune Forecasting](https://www.amazon.science/news-and-features/how-cloudtune-generates-amazon-store-forecasts-for-prime-day-black-friday-cyber-monday)。

这个亚马逊内部系统可以提前一年预测使用模式或“高峰计算负载预测”。每周的预测提前两周进行，甚至未来几个月每分钟的预测也会进行。

来自机器人和其他异常流量模式的访问会被过滤掉。

亚马逊内部数百个产品团队都使用这些结果，它们都希望预测自己将承担哪些支持流量需求的责任。一些团队甚至创建了流程，通过 Amazon Elastic Compute Cloud 将预期使用量转换为服务器的容量订单。

## 预测未来，一秒一秒地

在活动期间，亚马逊会继续监控使用情况，并将这些实时数据反馈到其预测中。

Wang 指出，预测模型总会存在差异。用户今年可能会进行更多搜索，而明年可能会进行更少。

Wang 说：“我们在活动剩余时间里实时更新我们的预测，以便获得最新的扩展指导，并有足够的时间来做出响应。”

Wang 说，即使是最周密的模型也会受到世界事件的干扰。他回忆起 2022 年，巴西和塞尔维亚争夺 FIFA 世界杯冠军，那一天恰好是黑色星期五。但巴西业务团队警告量化人员说，只要比赛还在进行，来自巴西的流量就不会很大。因此，他们能够“以外科手术般的精度”对基础设施进行调整。

当然，大多数企业的规模都不及亚马逊。但这些工程师不知疲倦的工作表明，总有更多的方法可以优化我们的工作负载，以实现成本效益和客户满意度。