# 边缘人工智能：利用联邦学习提升性能

![边缘人工智能：利用联邦学习提升性能的特色图像](https://cdn.thenewstack.io/media/2025/04/3e0cdc23-ai-at-the-edge-2-1024x576.jpg)

经典的机器学习范式要求在中心位置聚合用户数据，数据科学家可以在此预处理数据、计算特征、调整模型和评估性能。这种方法的优点包括能够利用高性能硬件（如 GPU），以及数据科学团队进行深入数据分析以提高模型性能的范围。

然而，这种数据集中化以数据隐私为代价，并且可能违反数据主权法律。此外，集中式训练可能不适用于[物联网 (IoT) 和其他基于边缘的设备](https://thenewstack.io/edge-computing/)，例如手机、嵌入式系统和工厂中的机器人。这是因为网络连接可能不可靠，并且物联网设备的内存、存储和计算能力有限。

联邦学习由 Google 于 2016 年推出，最初被称为“[Federated Optimization](https://arxiv.org/abs/1610.02527v1)”，它提供了一种替代方案。其核心思想是，服务器不是将数据发送到服务器，而是将模型发送到客户端端点，而端点发送训练或模型更新。多个客户端在中央服务的协调下进行协作，以解决机器学习问题——在不共享数据的情况下迭代改进模型。

## 联邦学习的工作原理

联邦学习最常见的架构是每个设备首先从云中的数据中心下载模型，例如[基础模型](https://thenewstack.io/llm/)。他们在自己的私有数据上对其进行训练，然后总结并选择性地加密模型的新配置。

模型更新被发送回云端，中央协调器/聚合器在云端解密、平均或以其他方式使用某种计算来组合模型。聚合器将结果集成回集中式模型中，然后将其发送回参与客户端以进行进一步的改进。这种迭代的协作过程一直持续到模型完全训练完成。

架构上的变化可以增加分布量，例如，通过将客户端聚集到群组中，每个群组都有一个单独的协调器。

以这种方式工作可以提供一些数据隐私，因为不共享原始数据。也就是说，有时会共享整个模型。此外，模型参数可能会泄露信息；通过了解单个模型如何发散，可以推断出有关个人数据的很多信息。

为了限制模型更新过程中的这种泄漏，联邦学习可以与其他技术结合使用，例如[差分隐私](https://www.semanticscholar.org/paper/Differential-Privacy-:-A-Historical-Survey-Hilton-Cal/4c99097af05e8de39370dd287c74653b715c8f6a)和[安全聚合](https://research.google/pubs/practical-secure-aggregation-for-federated-learning-on-user-held-data/)。

例如，Google 的“[Deep Learning with Differential Privacy](https://arxiv.org/abs/1607.00133)”论文的作者描述了一种差分隐私随机梯度下降算法，该算法在梯度下降的每个步骤中应用裁剪和噪声。随机噪声使得难以反转训练示例，而裁剪则最大限度地减少了每个训练样本的贡献。

## 联邦学习的实际应用

也许令人惊讶的是，以这种方式进行模型训练对模型性能的降低非常小。根据 [Katharine Jarmul](https://www.linkedin.com/in/katharinejarmul/?originalSubdomain=de)（O’Reilly 图书“[Practical Data Privacy,](https://www.oreilly.com/library/view/practical-data-privacy/9781098129453/)”的作者，以及 [Thoughtworks Germany](https://www.thoughtworks.com/en-de) 的前首席数据科学家）的说法，联邦学习“越来越多地部署在非面向消费者的边缘系统中，例如学习工厂车间行为或预测性维护。”

与经典机器学习相比，联邦学习的收敛速度往往较慢。这意味着该技术最适用于模型相对简单的情况。

“当然，并非所有东西都是 Transformer 模型，或者需要在 70GB 的参数空间上进行训练，”Jarmul 告诉 The New Stack。“像 Cisco 这样的公司可能仍然会将执行非常快速分类的基本模型（例如决策树）放在边缘设备上进行恶意软件分析。”

联邦学习在消费类设备中同样有价值。虽然它仍然是一项成熟的技术，但该技术已被包括 [Apple](https://www.apple.com/) 和 Google 在内的许多科技巨头部署，因此已被数百万用户每天使用。
在 Google，联邦学习已被应用于训练机器学习模型，这些模型为移动键盘（Gboard）中的各种功能提供支持，包括下一个单词预测、智能撰写、即时重新评分和[表情符号建议](https://arxiv.org/abs/1906.04329)。

以 Gboard 为例，其中一个用例是改进对西班牙语和葡萄牙语等非英语语言的预测。为此，Google 会选择一部分设备，综合考虑设备设置和分析知识，优先选择较新的型号，以限制内存和 CPU 的约束。

数据科学团队会在本地运行多轮训练，并将梯度更新发送给聚合器，后者将所有梯度平均在一起。团队会持续训练，直到模型足够好，当过程停止时，每个人都会收到更新后的模型。

[联邦分析](https://research.google/blog/federated-analytics-collaborative-data-science-without-data-collection/)是与联邦学习密切相关的概念，后来由 Google 提出，作为“将数据科学方法应用于分析存储在用户设备本地的原始数据的实践”。
联邦学习和分析在医疗保健领域尤其令人兴奋。Google 将联邦分析用于 [Google 健康研究](https://blog.google/technology/health/google-health-studies-app/)。The New Stack [此前报道](https://thenewstack.io/how-rapidai-uses-edge-kubernetes-and-ai-to-boost-stroke-care/)了另一家公司 [RapidAI](https://www.rapidai.com/) 如何在边缘使用临床 AI，将理想的缺血性卒中治疗窗口从大约 6 小时延长到 24 小时。

可以想象，对于从肺部扫描到脑部 MRI 的任何事情，聚合医疗数据并大规模分析，可能会带来检测和治疗癌症和其他疾病的新方法，所有这些都无需共享机密的医疗记录。

Apple 的研究人员描述了他们如何将联邦学习应用于 [Photos 中的几个功能](https://machinelearning.apple.com/research/scenes-differential-privacy)。随着应用程序熟悉用户图库中的重要人物、地点和事件，它能够为 iOS 17 中的“回忆”和“地点”选择关键照片。

这家科技巨头还将联邦学习用于 [iOS 中的 Siri App Selection](https://arxiv.org/abs/2502.04565)。例如，当用户发出播放音乐的请求时，“App Selection”会分析用户的习惯，以确定最合适的应用程序。如果某个特定应用程序经常用于类似请求，即使没有明确提及，模型也会优先启动该应用程序。

Apple 移动设备中非常先进的芯片，加上更高水平的硬件标准化，可能会使 Apple 在长期内优于 Android。

“Apple Intelligence 中的许多新功能，以及 Apple 构建的硬件隐私功能，都表明该公司比 Android 先进得多，” Jarmul 告诉 The New Stack。“我们早就知道，最好的推荐系统是为单个用户设计的，但按人训练很难扩展。

“Apple 正在进行一些非常有趣的研究，研究他们如何训练模型并对其进行个性化设置，而不是对其进行聚合，因此您的设备只会学习您。”

其他几家大型企业也已在生产环境中[发布了联邦学习](https://github.com/aws-samples/federated-learning-greengrass-ecs)，包括 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 和 [NVIDIA](https://developer.nvidia.com/blog/federated-learning-clara/)。还有许多联邦学习开源库，其中最受欢迎的是 [Flower](https://flower.ai)，这是一个来自 AI 初创公司 [Flower Labs](https://flower.ai/) 的开源平台。

## 联邦学习对地球更好吗？

尽管人工智能的兴起令人兴奋，但目前它带来了相当大的碳成本：

[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 在 2024 年 5 月报告称，自 2020 年以来，其总碳排放量增加了近 30%，这主要是由于其数据中心的建设，以满足其对人工智能的推动。- 根据该公司自己的报告，自 2019 年以来，Google 的排放量激增了近 50%，2023 年同比增长了 13%。Google 将排放量激增归因于数据中心能源消耗和供应链排放的增加，这再次是由人工智能驱动的。
考虑到这一点，[剑桥大学计算机科学与技术系](https://www.cst.cam.ac.uk/)的 AI 研究人员开始研究更节能的 AI 模型训练方法。他们与[牛津大学](https://www.ox.ac.uk/)、[伦敦大学学院](https://www.ucl.ac.uk/)和[阿维尼翁大学](https://univ-avignon.fr/)的合作者合作，探索了联邦学习对环境的影响。

他们的论文《[联邦学习能拯救地球吗？](https://arxiv.org/abs/2010.06537)》以及后续的[期刊文章](https://www.jmlr.org/papers/v24/21-0445.html)研究了联邦学习与集中式训练相比的碳成本。

他们训练了一个模型来对大型图像数据集中的图像进行分类，发现法国的任何联邦学习设置排放的二氧化碳都比中国或美国的任何集中式设置要少。在训练语音识别模型时，联邦学习比任何国家的集中式训练都更有效。

我们应该注意到，这些观察结果与特定的模型和实验设置有关。[Nic Lane](https://www.cst.cam.ac.uk/people/ndl32)领导了这项研究，他告诉 The New Stack，“当我们关心碳排放和机器学习时，我们可以使用联邦学习方法通过让计算在特定地点和时间发生来控制开销。这在数据中心比在联邦环境中更难实现。”

这意味着联邦学习为我们提供了一种将碳感知计算方法应用于训练模型的方法，例如[需求转移和塑造](https://www.conissaunce.com/demand-shifting-and-shaping.html)。

Lane 的团队推测，在排放方面，联邦学习比集中式方法有三个主要优势——它不需要冷却，不需要移动数据，并且可以通过允许跨组织协作来减少浪费。

典型的数据中心电源使用效率 (PUE) 为 1.6，这意味着数据中心中使用的 60% 的能源用于冷却。即使对于像 Google 和 Meta 这样公司运营的最有效的数据中心，冷却仍然是一个重要的因素。当然，许多数据中心由大学和较小的组织运营，并且具有更高的 PUE。

解决数据中心冷却问题的一种方法是将废热用于其他目的，例如为家庭或市政游泳池供暖。您无法对 Amazon、Google 和 Microsoft 通常建造的大型设施执行此操作，因为您需要将便利设施放置在使用废物的地方附近。但是，欧洲有一些小型数据中心正在采用这种方法。

“[T.Loop](https://www.tloop.se) 是一家将能源浪费转化为热量的公司，还有其他公司，”Lane 告诉 The New Stack。“使用联邦学习，您可以将这些较小的设施组合起来并训练 LLM。”

当我们达到 GPU 基础设施的物理限制时，这开辟了一些有趣的可能性。

“全球只有非常有限数量的数据中心可以训练真正大规模的模型，例如 [Llama](https://thenewstack.io/llama-3-how-metas-new-open-llm-compares-to-llama-1-and-2/) 和 [ChatGPT](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/)，使用传统的需要在同一地点拥有所有 GPU 的范例，”Lane 说。他补充说，通过使用联邦学习来组合不同地点的 GPU 网络，“您可以训练这些模型的虚拟地点数量大大增加。”

对于大型组织来说，情况也是如此。“即使对于一家在全球拥有大约 10,000 个或更多 GPU 的公司，例如 Samsung，如果您在一个地方没有足够的 GPU，也无法训练大型 LLM，”Lane 说。“联邦学习将允许您更充分地利用您的资源。”

我们之前提到过，联邦学习往往是一个较慢的过程。然而，Lane 认为，尽管花费的时间更长，但这些优势可能意味着您最终可以更快地进行训练。“

当您目光短浅地关注大规模工作时的挂钟时间时，就会产生一种性能错觉，”他说。“许多公司都希望今天开始进行训练，但没有 GPU 可供他们使用，因此他们等待六个月。使用联邦学习，挂钟时间可能会慢 30%，但您可以今天开始并帮助环境。”

研究团队还指出，将数据从一个地方移动到另一个地方会产生相当大的成本。

“一次内存操作使用的能量是计算操作的一千倍，”Lane 说。
由于联邦学习不需要移动数据，因此这里存在潜在的效率提升。Lane 的团队已经展示了这项技术的强大示范；使用其构建在 Flower 之上的 [Photon system](https://arxiv.org/abs/2411.02908)，该团队率先展示了 7B 参数的 LLM，并且可以使用联邦学习训练更大的模型——这一结果后来被其他行业实验室和初创公司复制。

此外，联邦学习开启了跨组织协作的可能性。目前存在大量的冗余训练，因为多个组织构建非常相似的模型。理论上，联邦学习将为我们提供另一种在组织边界之间共享模型的机制。

德国和欧盟的其他国家/地区开始大力推动这一优势。

Jarmul 告诉我们：“我是由德国政府资助的 [Composite Learning](https://www.sprind.org/en/actions/challenges/composite-learning) 的评审团成员。“这个想法是，如果你想在像 LLM 这样的大规模模型上进行训练，你可以将其分散到多个数据中心和硬件提供商。”

Flower 和剑桥大学被选中并获得了该计划的资助，以构建 [a tool for large-scale federated learning](https://www.sprind.org/en/actions/challenges/composite-learning#anchor-teams)。

此外，Jarmul 告诉 TNS，“负责气候和经济的德国政府机构也刚刚宣布了一个名为 [8ra](https://www.8ra.com) 的欧盟项目，该项目旨在为边缘 AI 构建下一代云基础设施，并且本质上将是分布式或联邦式的。”“如果我们能够创建消除重复浪费的协作模型，那么对于行业来说将非常有趣。”

除了联邦学习之外，还有许多其他技术可以显着降低训练和推理的碳成本，其中大多数都植根于压缩。通过缩小模型尺寸，可以加快训练时间并提高其资源效率。

这是一个持续的研究领域，其中一些举措探索了诸如蒸馏、剪枝和量化等主题，作为压缩的一种手段。

除了这些方法之外，适用于机器学习的基本规则与适用于任何其他计算作业的规则相同：

- 使用可以安全执行作业的最小硬件配置。
- 在低碳电力充足且有可靠计划使电网更加清洁的地区运行计算。
- 使用来自在绿色地点拥有数据中心并提供良好工具以帮助减少碳足迹的提供商的云服务。
- 并应用碳感知计算技术，例如 [demand shifting and shaping](https://www.conissaunce.com/demand-shifting-and-shaping.html)，以进一步减少您的碳足迹。

我在 The New Stack 的电子书“[Sustainable Software: A Developer’s Guide to Green Computing](https://thenewstack.io/ebooks/cloud-infrastructure/developers-guide-to-cloud-infrastructure-efficiency-and-sustainability/)”中更深入地探讨了这些方法。

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)