
<!--
title: 无需GPU运行AI的情况：一个“Farm Fresh”案例研究
cover: https://cdn.thenewstack.io/media/2024/09/37fe0ae7-vmware-explore-ruby-bradley.jpg
-->

最新一代支持英特尔 AMX 的至强处理器如何为许多以前只能用 GPU 完成的 AI 任务提供动力。

> 译自 [When You Don't Need GPUs to Run AI: A 'Farm Fresh' Case Study](https://thenewstack.io/when-you-dont-need-gpus-to-run-ai-a-farm-fresh-case-study/)，作者 Joab Jackson。

虽然英伟达在公司加速其 AI 项目时享受着 [前所未有的 GPU 需求](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/)，但英特尔和其他芯片制造商的悄然进步减少了对 GPU 的需求，至少允许一些工作负载完全无需图形处理单元即可运行。

这是上周在拉斯维加斯举行的 [VMware Explore](https://tanzu.vmware.com?utm_content=inline+mention) 大会上的一次演讲的结论。

演讲来自位于安大略的 Nature Fresh Farms。这家位于安大略的农业公司在美国和加拿大拥有 250 英亩的温室，全年种植 160 万株植物：甜椒、西红柿、黄瓜和草莓。

生长周期的所有方面都由 AI 管理。通过少量服务器，植物生命的所有方面都得到监控和控制：水、光（外部和温室产生的）、温度、二氧化碳水平、湿度和土壤中的营养。

使用的 GPU 数量？零。

![](https://cdn.thenewstack.io/media/2024/09/4caf2adb-nature_fresh-01-1024x558.png)

## Nature Fresh Farms

Bradley 和他的团队从一个简单的三节点 Kubernetes 集群开始，以及英特尔的 [OpenVINO](https://github.com/openvinotoolkit/openvino)，这是一个用于运行 [推理](https://thenewstack.io/5-open-llm-inference-platforms-for-your-next-ai-application/) 和其他 AI 任务的开源框架。

该系统不仅从温室传感器中获取信息，还从视频和照片中获取信息，以及从附近的氣象站获取信息。这使得系统能够微调操作，例如，只有在阳光明媚的时候才给植物浇水，或者在外面阴天的时候开启人工照明。

“我们已经了解到，就像人类一样，如果你在我们饿的时候给我们食物，我们会做得更好，”[Keith Bradley](https://www.linkedin.com/in/keith-bradley-76105049)，[Nature Fresh Farms](https://www.naturefresh.ca/) 的 IT 和安全副总裁。

总的来说，该公司为每株植物的整个生命周期收集约 12MB 的数据，或每年为整个运营收集 23TB 的数据。

“我们分析所有数据，并使用 AI ML 来改进每天的生长，以获得更优化的结果，”Bradley 说。

所有这些数据不仅用于优化作物的健康状况，还用于向销售团队提供销售预测。

“AI 帮助我们进行预测，因为有很多你看不到的变量，”Bradley 说。

AI 还用于扫描箱子，以确保所有农产品都已准备好出售，识别腐烂的农产品，防止其污染整个箱子。

由于 AI，该公司在连续几年中产量增长了 2-3%，并且增加了少量人员可以完成的耕作量。

令人惊讶的是，Nature Fresh 规模相对较小。“我们不是一家可以为 AI 农场建立平台的数十亿美元公司，”Bradley 说。

Nature Fresh 使用 [OneAPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html) 在不同的 CPU 上运行工作负载，因此 IT 团队不必担心将特定工作负载写入特定的 CPU 或硬件加速器。该公司与 Kubernetes 一起使用 OneAPI 来优化工作负载，确保实时决策的实时数据优先于不太紧急的分析作业。

Bradley 说，由于 OneAPI 是跨平台的，因此 Nature Fresh 能够在没有大量最新硬件资金的情况下扩展 AI 操作。

[OpenVINO 网站](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.htm) 是一个了解哪些 AI 任务可以由 CPU 单独完成的好地方，事实证明，这些任务相当多。它包括一套强大的基于 [Jupyter Notebook](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/) 的教程，用于启动各种 AI 任务，包括聊天机器人、LLM、文本图像生成、视频分析、图像着色、降噪、手势检测、物体识别和分类、人脸识别、手写文字转文本、下一个词建议、医学图像分析、声音分类、注视检测、缺陷识别。

## GPU 或 CPU

GPU 只做一件事：矩阵数学。

GPU 的优势在于它们可以非常快地并行地对矩阵进行数学运算。虽然它们最初是为渲染图形而设计的，但并行数学运算对于 [AI](https://thenewstack.io/ai/) 也很有用。

![](https://cdn.thenewstack.io/media/2024/09/75402b19-matrix-math-ruby.png)

但 GPU 并非唯一能够进行矩阵运算的芯片。AMD 在其最新的 [EPYC 系列](https://www.amd.com/en/products/processors/server/epyc.html) 处理器中增强了矩阵功能，并且越来越多的 [硬件加速器](https://thenewstack.io/developers-can-now-access-the-worlds-fastest-ai-chip/) 正在上市。

在最新的英特尔至强第四代（“Sapphire Rapids”）和第五代（“Emerald Rapids”）[CPU](https://www.intel.com/content/www/us/en/products/details/processors/xeon/scalable.html) 中，英特尔包含了 [高级矩阵扩展](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html) (AMX)，它将一些矩阵运算指令放入 CPU 的每个核心。

英特尔估计 AMX 可以将 Pytorch 性能提高 10 倍，并且可以与 TensorFlow 和 OpenVINO（以及 VMware 的 [vSphere 8](https://core.vmware.com/resource/whats-new-vsphere-8) 虚拟机平台）开箱即用。

![](https://cdn.thenewstack.io/media/2024/09/a71bdb71-ruby-amx-02-1024x565.png)

Broadcom 的研发首席工程师 [Earl Ruby](https://earlruby.org/tag/broadcom/) 在本次会议上发言时表示，AMX 于 2023 年推出，引入了“称为 tile 的二维寄存器，加速器可以在其上执行操作”。

他说：“它旨在成为一个可扩展的架构。因此，第一个实现的加速器被称为矩阵乘法单元，或 TMOL，数据直接进入 tile，同时主机向前跳跃并调度 tile 的加载。TMOL 在数据准备好的那一刻就开始操作。”

“在每次乘法回合结束时，该 tile 会移动缓存并进行一些并行处理，从而能够使用单个指令处理多个数据。软件方面的目标是确保主机和 AMX 单元同时运行，从而最大限度地提高吞吐量和性能。”

![](https://cdn.thenewstack.io/media/2024/09/9bb5568f-ruby-amx-01-1024x565.png)

## 演示，请

Ruby 说，有了这种新的硬件和支持软件，许多 AI 工作负载可以运行，与普遍看法相反，无需 GPU。

作为示例，Ruby 运行了一个演示。他在一个旧的“Ice Lake”——第三代英特尔至强服务器处理器的集群上打开了 [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 70 亿参数模型，并将该初始化的速度与在基于 AMX 的处理器集群上的相同启动速度进行了比较。

Ice Lake 芯片的性能充其量只能说是缓慢。

Ruby 说：“这就是为什么人们会想，‘哦，你必须要有 GPU，因为如果你想做这种事情，CPU 的性能就不是那么好。’”

相比之下，在 Sapphire Lake 处理器上启动 Hugging Face 非常快。

Ruby 说：“它足够响应，可以完成实际工作。”

然后，Ruby 展示了使用大约 17,000 个金融问题微调 Hugging Face 模型的示例，AMX 集群能够在大约 3.5 小时内完成这项工作。

Ruby 说：“所以，如果你在数据中心有 AMX，并且想在晚上进行一些微调，你可以做到。你不需要 GPU。”

Ruby 还使用该模型在单个第四代至强上运行了三个聊天机器人：

![](https://cdn.thenewstack.io/media/2024/09/e69ab883-ruby-chatbot-1024x515.png)

Ruby 说，仍然有一些情况需要 GPU：需要低延迟或即时响应、微调大型模型或从头创建模型。

但越来越多的情况下，最新的 CPU 可以正常工作：批处理 ML 工作负载、轻量级推理，或者在降低运营成本和 [功耗](https://thenewstack.io/how-amazon-matches-power-needs-to-green-energy-sources/) 时，Ruby 说。

Ruby 说：“你不需要使用 GPU。CPU 将涵盖 [许多] 用例。如果你想入门，并且不想为了入门而购买一堆硬件，你今天就可以用你现有的硬件入门。”

Bradley 补充说：“我们不需要一直立即响应。三到四分钟的延迟不会影响我们。但一旦我们达到那个点，很高兴知道我们可以开始转换。”

“我不知道我们什么时候会达到那个点，但很高兴知道我们一直在构建平台并使用我们现有的东西。”

你可以在这里观看整个演讲 [here](https://www.vmware.com/explore/video-library/video/6360760637112)。

*披露：Broadcom 为记者支付了参加此次会议的旅行/住宿费用。*

