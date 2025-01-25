# TikTok 算法为何如此有效？

![TikTok 算法为何如此有效的特色图片](https://cdn.thenewstack.io/media/2025/01/beed1e48-tiktok-1024x768.png)

周二，新当选的美国总统唐纳德·特朗普[签署](https://www.nytimes.com/2025/01/22/us/politics/what-is-an-executive-order.html)了一项[行政命令](https://www.whitehouse.gov/presidential-actions/2025/01/application-of-protecting-americans-from-foreign-adversary-controlled-applications-act-to-tiktok/)，给予TikTok [75 天的缓刑期](https://www.nytimes.com/2025/01/20/technology/trump-tiktok-ban-delay-executive-order.html)，使其免于被美国司法部关闭，这让狂热的TikTok用户欣喜不已。

但在签署仪式上，总统明确表示[他的意图](https://x.com/Acyn/status/1881510272529240260)：TikTok必须[将其一半股份出售给美国](https://www.theregister.com/2025/01/20/trump_tiktok_nationalization_idea/)，通过某种美国拥有的实体，才能继续在美国运营。

这位注重交易的总统随后补充道：“每个富人都给我打过关于TikTok的电话。”

然而，一半可能很棘手。你想要确保你得到正确的一半。否则，你最终会得到一个媒体服务的空壳，就像[Friendster](https://www.therunway.ventures/p/friendster)一样。

该公司目前在美国拥有约 1.7 亿用户。但这个受众群体可能会迅速消失。你想要的是能让用户持续登录的部分。有价值的部分是运行推荐服务的算法。

TikTok 巨大的用户群证明了其令人上瘾的特性。保持用户参与的关键？强大的算法。这些算法驱动推荐系统，不断为用户提供与其兴趣相符的内容流。

正如苏黎世大学研究人员 Maximilian Boeker 和 Aleksandra Urman 在他们的研究“[对 TikTok 个人化因素的实证调查](https://www.researchgate.net/publication/358233121_An_Empirical_Investigation_of_Personalization_Factors_on_TikTok)”中指出的那样，该平台的推荐系统可以说是其最重要的成功驱动因素。

[TikTok](https://www.tiktok.com/en/)及其母公司，位于北京的[字节跳动](https://www.bytedance.com/en/)，在为用户提供内容的算法的设计和运行方面一直保持沉默。

那些愿意深入研究字节跳动工程师和其他研究人员撰写的研究论文的人可能会发现一些线索，了解TikTok 如何让用户不断回归。

## 揭开整体架构的神秘面纱
这篇发表在 2022 年 ACM 推荐系统会议 (RecSys) 上的论文“[Monolith：具有无碰撞嵌入表的实时推荐系统](https://arxiv.org/pdf/2209.07663)”提供了宝贵的见解。虽然没有声称描述 TikTok 的确切算法，但它揭示了字节跳动工程师设计高效推荐系统的方法。

该论文详细介绍了研究人员做出的“非正统”权衡，这些权衡带来了显著的性能改进，从而产生了一个名为“Monolith”的推荐系统，该系统在研究人员的断言中始终优于具有相同内存使用量的其他系统。

前 TikTok 工程师 [Arman Khondker](https://armankhondker.com/) 指出这篇论文是[理解 TikTok 方法的基础](https://x.com/armankhon/status/1880860565889040428)。Khondker [盛赞](https://x.com/armankhon/status/1880860565889040428) TikTok 算法“领先竞争对手数年”，“毫无疑问，这是现存最有价值的软件”。埃隆·马斯克本人对这一说法作出了简洁的回应：“目前是这样”。

## TikTok 算法的目标
2021 年《纽约时报》[获得的一份 TikTok 内部文件](https://www.nytimes.com/2021/12/05/business/media/tiktok-algorithm.html) 揭示了该公司算法的四个主要目标：用户价值、长期用户价值、创作者价值和平台价值。从本质上讲，TikTok 优先考虑让用户参与并花费时间在平台上。

该算法考虑各种因素，包括点赞、评论和视频观看时间，以确定向用户展示哪些内容。它还旨在使推荐多样化，以防止用户感到厌倦并失去兴趣。

对于熟悉用户留存率的分析师来说，这一切看起来都像是相当常规的事情。“完全合理，但很传统，”加州大学圣地亚哥分校计算机科学教授 Julian McAuley 俏皮地说。

因此，TikTok 算法的真正力量可能不仅来自用户分析，还来自[其相当快的执行速度](https://thenewstack.io/tiktok-to-open-source-cloud-neutralizing-edge-accelerator/)。

## 实时反馈的力量
“整体式”论文强调了构建推荐系统以跟上用户快速变化的偏好的挑战。

简而言之，推荐引擎的工作是利用最新的交互作为训练模型的主要输入来预测用户的兴趣和未来行为。

为此，传统系统通常依赖于难以快速适应新数据的复杂模型。构建此类系统的传统方法是为每个任务维护单独的模型。“预测点击”将获得一个模型，“预测观看时间”将获得另一个模型。分析通常通过批处理完成，从而降低了系统了解用户的速度。模型无法实时与客户反馈互动。

用户使用TikTok的频率越高，“算法就越准确”。

—— 赵郑伟，中山大学

像[Pytorch](https://thenewstack.io/why-pytorch-gets-all-the-love/)和[TensorFlow](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/)这样的深度学习框架，虽然是为通用用途而构建的，但并不真正适合在线推荐的紧急生产需求。Tensorflow将训练与推理分开，这使得模型与来自用户的最新输入脱节。因此，任何具有竞争力的系统设计都必须构建各种变通方法，才能将这些[批处理框架](https://thenewstack.io/real-time-ai-apps-using-apache-flink-for-model-inference/)整合到[实时系统](https://thenewstack.io/data-streaming/)中。

另一方面，“整体式”利用单个模型完成所有任务，并通过在线训练整合实时反馈。这允许系统快速学习并适应用户不断变化的兴趣。

论文描述了如何使用[Kafka](https://thenewstack.io/confluent-wants-to-make-batch-processing-a-thing-of-the-past/)记录用户的行为，以及并行记录特征。一个[Apache Flink](https://thenewstack.io/a-developers-guide-to-getting-started-with-apache-flink/)作业“将来自用户行为的特征与标签连接起来，并生成训练示例，然后将其写入Kafka队列。训练示例的队列由在线训练和批量训练同时使用。”

- 整体式架构强调更快的在线训练。

## “无尽浏览”和表格大小

推荐系统的另一个挑战是处理“稀疏特征”和“概念漂移”。稀疏特征意味着用户只对一小部分内容感兴趣，而概念漂移是指用户在浏览无尽的视频流时，其兴趣随着时间的推移而变化的趋势。

论文指出：“对某个主题感兴趣的同一用户，可能下一分钟就会转移他们的热情。”

如果将所有内容都放入嵌入表中，它将太大而无法放入内存。传统的固定大小模型不喜欢被放大，而随着新用户的加入，它们将不得不不断地被放大。

“整体式”通过以下方式解决了这些问题：

- 快速将用户反馈纳入训练过程。
- 通过“无冲突哈希表”和高级特征逐出机制来保持数据表可管理。

实现这些目标确保系统能够跟上用户不断变化的偏好，而不会被海量数据淹没。

为了将各种稀疏特征整合到计算机内存中，研究人员提倡使用[Cuckoo Hashmap](https://en.wikipedia.org/wiki/Cuckoo_hashing)设计，该设计最大限度地减少了冲突，或者两个键无意中占据了相同的空间。

为了进一步减少内存使用，很少使用的ID会被删除。

## 快速个性化内容

本质上，“整体式”代表着从构建系统的[传统微服务方法](https://thenewstack.io/microservices/)转向更[统一的整体式架构](https://thenewstack.io/return-of-the-monolith-amazon-dumps-microservices-for-video-monitoring/)。

虽然字节跳动尚未确认“整体式”架构是否用于TikTok（或其中文版本抖音），但这些服务以闪电般的速度提供个性化内容的能力是不可否认的。（整体式架构已正式用于[BytePlus Recommend](https://www.byteplus.com/en/product/recommend)，这是该公司的托管推荐引擎服务）。

在TikTok上，用户几乎不需要任何操作就能找到引人入胜的内容，中国中山大学的研究员赵郑伟观察到。用户开始滑动的那一刻，应用程序就开始学习。

用户使用TikTok的频率越高，“算法就越准确”。
科技发展日新月异，不要错过任何一期。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等：[https://youtube.com/thenewstack?sub_confirmation=1](https://youtube.com/thenewstack?sub_confirmation=1)