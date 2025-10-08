<!--
title: 为Python数据科学家量身定制的云平台，告别繁琐运维
cover: https://cdn.thenewstack.io/media/2025/10/eea5c7ec-coiled-io.png
summary: Coiled.io简化数据科学家在云上运行Python的挑战。它倡导原生VMs，而非复杂K8s/Docker，提供更简便、更经济、更灵活的方案，让云体验更愉快。
-->

Coiled.io简化数据科学家在云上运行Python的挑战。它倡导原生VMs，而非复杂K8s/Docker，提供更简便、更经济、更灵活的方案，让云体验更愉快。

> 译自：[A Cloud Built for Python Data Scientists, Not Infrastructure Engineers](https://thenewstack.io/a-cloud-built-for-python-data-scientists-not-infrastructure-engineers/)
> 
> 作者：David Cassel

云计算非常有用——但如果你是一位热爱Python的数据科学家呢？

普遍的建议是，如果你想运行工业级的[Python](https://thenewstack.io/what-is-python/)，那么就把它运行在Kubernetes上。

“我们认为这完全是错误的，”Matthew Rocklin说。

2020年，Rocklin共同创立了[Coiled.io](https://coiled.io/)，旨在提供一种更简单的方式来释放云计算的潜力。“答案就是‘去使用原生的VMs[虚拟机]’，”Rocklin在[“Talk Python”播客](https://talkpython.fm/episodes/show/519/data-science-cloud-lessons-at-scale#transcript-section)上说。“如果你在它们周围做一些事情（比如配置正确的软件环境和适当的日志），它们实际上相当不错。”

2015年，Rocklin创建了[Dask](https://en.wikipedia.org/wiki/Dask_(software))，这是一个用于启动大量虚拟机来分析和操作数据的Python库。在多年为数据科学领域的Python项目（如Tools、Multiple Dispatch和SimPy）做出贡献后，Rocklin共同创立了Coiled.io，以使部署虚拟机创建软件变得更加容易。

[![](https://cdn.thenewstack.io/media/2025/10/88920bde-talkpython-300x225.png)](https://cdn.thenewstack.io/media/2025/10/88920bde-talkpython-300x225.png)

他上个月[在一个播客节目](https://www.youtube.com/live/omBibVGLzyo?si=Nmx6q00_j4A_i5ZH)中解释了他们的使命，该节目解释了“云规模Python的混乱真相”。播客主持人Michael Kennedy同意，当今许多云基础设施似乎都专注于Web和API开发人员。Kennedy认为，即使是为数据科学家准备的教程也没有强调[Docker](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/)和[Linux技能](https://thenewstack.io/introduction-to-linux-operating-system/)——尽管Rocklin看到了另一种可能的解决方案。“也许我们不应该通过教育人们来解决这个问题。

“也许我们应该通过构建更好的工具来解决它。”

这是一个来自Python社区核心的全新视角。在整个播客中，Rocklin指出数据科学家有他们自己独特的一系列顾虑。

而像Coiled这样面向虚拟机的解决方案可能是这项工作的正确工具。

## 为什么Docker和Kubernetes不适合数据科学家

他说，如果你让ChatGPT提供一些可以剪切粘贴以启动100台虚拟机的命令，“它会为你打字几分钟！而且这不是大多数只使用Python几年时间的数据科学家所能掌握的打字方式。”

“我实际上对这种相对常见的事情做起来竟然如此困难感到非常震惊。”

Rocklin承认Docker是一个很棒的工具，但它不一定适合数据科学家，因为它“非常专注于提供一个可以运行数十年的稳定系统”。然而，数据科学家需要“一个每五分钟就能改变的系统。像Docker、Kubernetes或Terraform这样的工具所做的选择，与你为这类受众构建中间件时所做的选择实际上大相径庭。”

“它是为云基础设施工程师设计的。”（虽然中间件确实存在，“但它不是为我们的用例设计的。”）

所以，“我们自己动手做了。”

在播客中，他两次从笔记本电脑上迅速启动了一个拥有1000个核心的EC2集群。

## 简单演示：使用Python装饰器启动集群

在演示过程中，播客主持人Kennedy惊叹于简单的Python语句中蕴含了如此多的功能。

```
vm\_type="g5.xlarge",  
keepalive="20 minutes"  
region="us-west-2",
```

在他们交谈时，Rocklin只通过输入一个字符（将带有ARM标志的装饰器语句改为注释）就关闭了ARM硬件。

```
# arm=True,
```


然后他开始启动一个新的集群。

Python的装饰器一直允许你扩展函数行为——所以这些语句扩展了Coiled定义的虚拟机函数（在导入Coiled库后可用）。“我们内部开玩笑说，我们的核心竞争力是开关虚拟机，”Rocklin说。“一旦你拥有了这项技术，围绕它编写API就相当便宜了。”

Rocklin还认为，如果将Docker推送周期放入数据科学工作周期中，“它会阻塞所有事情。人们最终就不会去做。”因此，Coiled的虚拟机不使用Docker，而是复制用户的环境。

这个演示的最终结果是什么？一千台机器，它们看起来就像用户原来的机器一样，“只是数量更多、更大、或带有GPU，或任何你想要的。”

Rocklin说，第一个1000台虚拟机的集群花费了1.39美元（并补充说第二个“到目前为止已经花了我45美分……”）。“云计算既比我预想的便宜得多，也贵得多，这取决于你是否正确操作。两者之间有几个数量级的差异。”

后来，Rocklin甚至给出了一个数字。“无服务器、Lambda和类似技术通常有4到5倍的成本溢价。它们也有局限性，比如你不能获得大型机器、不能获得GPU，你的软件环境必须达到一定大小。”

## 如何避免意外的云账单

Coiled的资深软件工程师Nat Tabris也参加了播客，他认为这是云计算的另一个难点：它缺乏防护措施，特别是对于不知道风险在哪里的人来说。

Rocklin笑了，回忆起自己还是研究生时使用[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)的免费套餐，创建了一些虚拟机，然后关闭了它们，“三个月后，我收到了一张400美元的账单。那不是虚拟机的费用，而是虚拟机附加的存储或一些遗留的网络资源——我对此一无所知。”

Kennedy补充说，还有“各种各样的小型其他服务”会让你意外付费（包括数据库和数据库存储）。“所以我们试图做的一部分工作，”Tabris说，“就是设置默认值，设置控制，这样你就不会意外地花那么多钱。”

具有讽刺意味的是，那段基本的计算时间“往往是成本中相当可预测的一部分”。令人惊讶的巨额账单来自“所有这些你甚至没有考虑到的其他东西——比如，‘如果我翻转这个设置，我现在会大量调用S3 API，结果是按API调用次数付费。’”

Tabris回忆起一个客户使用一个1000节点的集群，设置了调试级别的日志记录，这产生了“非常冗长的日志……我想那大概是15000美元的账单。”（尽管那个故事“有一个快乐的结局，因为我们和AWS谈了，他们最终为客户承担了这笔费用。”）Rocklin指出，这是处理这些突发意外账单的另一个好经验：如果你和AWS沟通，他们可以退款给你。

如果Coiled发现冗长的日志，现在会发出警告。

所以当Kennedy询问工作流程是怎样的，以确保他的2000台机器不会全天或不必要地运行，Rocklin指出Coiled会自动监控——并在机器不使用时将其关闭。

## 实验的自由

但当虚拟机变得容易创建时，会发生一些事情，Rocklin说：它赋予用户“很大的能力开始实验硬件。”（一位用户遍历了他们云中的每个区域，试图找到A100 GPU实例。）“我们经常看到人们玩转ARM、Intel和AMD，尝试各种GPU类型。”

你也可以实验不同的区域。例如，如果你的数据集存储在一个区域，Tabris说，“如果你离它近，下载速度会比离它远时快上几个数量级。”

Tabris来自Web开发领域，但他意识到对于数据科学家来说，“尝试不同的实例类型进行探索实际上是有意义的。‘这个GPU对我有什么用？’”不同的CPU也能带来差异——即使是像从ARMv8到ARMv7这样的小改变。“其中一些确实对数据科学工作负载产生了影响，因为它与那些宽指令有关。”

有些CPU有更好的内存——DDR5而不是DDR4。“这会影响我的工作负载吗？它能省钱吗？”这可能很难提前知道，但“尝试一下真的很容易。”

Rocklin后来称之为“这其中的乐趣……正是这种多样性实际上是云计算的核心部分”，称之为Coiled非常重视的一点。

## 让云计算变得有趣味性的理念

播客主持人Kennedy很欣赏这种额外的便利，因为多样性和实验性最终是数据科学精神的关键部分。“我们将进行实验，我们将探索，我们将玩耍。”

Rocklin也同意。“我认为Python之所以流行，很大程度上是因为它常常感觉像是在玩耍。我们得到这些既易于使用又功能强大的库。那感觉就像在玩耍。”

相比之下，在AWS中使用Boto库或在Kubernetes中编写YAML“感觉不像是在玩耍……但今天我们得以尝试创建2000个虚拟机——一半是ARM，一半是Intel。一半在美国东海岸，一半在美国西海岸……现在突然间，云计算就像在玩耍。

“当事情变得有趣时，你就会做不同的事情。你的行为也会不同。人们会玩得很开心。云计算是一个非常有趣的工具。一旦你克服了所有的痛苦。”

当被问及最后的想法时，Rocklin说云计算的伟大承诺——作为一个令人愉悦且强大的数据工具——并非总是能很好地实现。他敦促数据科学家不要满足于现状。

Kennedy承认，“它变得非常复杂——但它不一定非得如此。”Tabris补充说，“‘事情本应令人愉悦’的这个信息对我们很重要。”

Rocklin同意云计算“可以是一种愉悦的体验……我们都应该玩耍。如果你不想使用Coiled，那没关系。但还有其他做事的方式。去玩吧。”