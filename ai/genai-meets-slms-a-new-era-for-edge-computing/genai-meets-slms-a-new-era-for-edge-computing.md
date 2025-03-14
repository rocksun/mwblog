
<!--
title: GenAI遇上SLM：边缘计算的新纪元
cover: https://cdn.thenewstack.io/media/2025/02/2bcf4a85-nathan-shipps-ke2-wbtxini-unsplash-scaled.jpg
-->

小型语言模型（SLM）在效率、隐私和适应性之间实现了卓越的平衡，使其成为各种应用的理想选择。

> 译自 [GenAI Meets SLMs: A New Era for Edge Computing](https://thenewstack.io/genai-meets-slms-a-new-era-for-edge-computing/)，作者 Pankaj Mendki。

让我们想象一个场景：一家医院的患者拥有自己的医疗记录。医院希望在其个人监控设备上安装支持 AI 的医疗保健助手，以便医疗保健专业人员可以监控和分析数据，并提供实时反馈，以确保常规和紧急药物治疗，但该系统必须符合区域医疗法规。在这种情况下，边缘计算方法对于准确性和数据安全性是可靠的——并且可以在本地工作；不需要云。

现在，想象一下当边缘计算由 [GenAI](https://www.talentica.com/blogs/generative-ai-transforming-decision-making-edge-computing/) 提供支持时的可能性。这种融合不仅使解决方案更智能，而且使解决方案更具自主性，并为开发个性化的智能医疗保健开辟了新的可能性。但边缘计算的影响不仅限于医疗保健领域。它还可以改变投资等行业，在这些行业中，实时数据处理对于交易决策至关重要，并加强网络安全，以防止数据落入坏人之手。

如今，[开发人员主要使用大型语言模型](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) (LLM) 来开发 GenAI 应用程序，因为它们具有明显的优势。但 LLM 的规模和复杂性使其对资源受限的边缘设备提出了挑战。SLM 接受针对特定案例的文献训练，与 LLM 相比，它们可以更快、更高效地做出实时决策。

作为新兴技术主管，我和我的团队已经多次测试了 SLM。本文探讨了在边缘计算系统中使用 SLM 的一些挑战和潜在策略。

## 用 SLM 替换 LLM 用于边缘应用

切换到 SLM 在医疗保健领域具有显着优势，在该领域，个人设备的使用很普遍。由于性能限制，个人设备通常缺乏有效运行 LLM 所需的资源。由于 SLM 针对特定案例，因此它们提供了一个解决这些限制的理想解决方案。

使用模型蒸馏、参数剪枝和量化等技术可以轻松地将 LLM 转换为 SLM。模型蒸馏涉及训练一个更小的模型来模拟更大的模型，从而保留原始模型的大部分性能。参数剪枝消除了模型中不必要的权重和连接，以简化其架构，而不会牺牲准确性。量化通过降低权重数值表示的精度来压缩模型，从而产生更小的占用空间和更快的推理时间。

现在，让我们重新审视医院的例子。不同组的患者可能需要持续监测，并针对神经内科、肾脏内科、心血管内科、自身免疫性疾病、传染病甚至事故相关的疾病和病症采取立即行动。可以针对这些医疗状况分别训练 SLM。他们可以[实时分析这些患者的数据](https://thenewstack.io/how-open-source-and-time-series-data-fit-together/)，并启动所需的治疗或提醒医疗保健专业人员及时采取行动。

根据开发人员的需求，他们可以从头开始构建 SLM，也可以使用预训练模型作为其项目的基础工具，并加快开发过程。开放市场（例如 GitHub Models 和 Hugging Face）拥有预训练的 SLM。这些工具还有助于在边缘更广泛地采用生成式 AI。SLM 的上下文功能可以改变多个行业。在智慧城市中，SLM 可以构建更好的支持边缘的物联网设备，以提供针对拥堵或道路封闭等情况量身定制的上下文相关方向。这种组合可以提高效率，最大限度地减少延误，并改善整体城市交通体验。

## 解决平台多样性和资源需求

边缘设备之间的平台异构性可能会使部署 SLM 具有挑战性。个人监控设备可以在多个平台上运行，例如 iOS 和 Android。但是，诸如 Open Neural Network Exchange (ONNX)、MediaPipe、WASI-NN、Rust 和 WebAssembly 之类的堆栈和框架可以帮助构建一个边缘应用程序生态系统，以使用 SLM。它们支持各种硬件和操作系统，并确保跨平台支持和资源优化的应用程序。

诸如开放神经网络交换 (ONNX) 运行时之类的框架提供了一个抽象层，简化了跨多个平台对 SLM 的支持，从而缓解了这个问题。开发人员可以使用 ONNX 工具包针对特定硬件目标优化模型，以确保无论底层设备架构如何，都能实现高效的性能。MediaPipe 框架简化了将 SLM 迁移到轻量级边缘设备（包括移动平台）的过程。其模块化框架和高效的硬件加速器支持预优化的跨平台解决方案，并简化了在资源受限环境中部署复杂的 AI 模型。

此外，WebAssembly 可以利用包括 GPU 在内的底层硬件功能来优化性能并加速推理任务。由于它将轻量级执行与强大的计算资源相结合，因此非常适合 SLM 应用程序。它还有助于可持续发展计划，通过支持在功耗和发热量较低的边缘设备上开发强大的 AI 解决方案。WASI-NN 为 WebAssembly 提供机器学习推理 API。它支持利用 SLM 功能的 WebAssembly 多语言[开发](https://thenewstack.io/webassembly-users-a-mix-of-backend-and-full-stack-developers/)应用程序。

[Rust 编程语言](https://thenewstack.io/the-rust-c-bridge-a-new-path-forward/)堆栈进一步增强了这个生态系统。与 [ML 环境中使用的 Python 堆栈](https://thenewstack.io/why-every-python-dev-needs-virtual-environments-now/)不同，Rust 支持小至 30 MB 的应用程序运行时，从而实现适用于资源受限边缘环境的轻量级、高性能应用程序。

## 通过增强的安全性在边缘进行协作学习

医疗保健和许多其他领域都在隐私敏感的环境中运作。然而，与边缘应用程序进行受控的[数据共享可以帮助建立](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/)知识库，以使用 SLM 和其他医疗保健服务改进治疗程序。在这种情况下，联邦学习等技术可以确保在多个设备上对 SLM 进行训练和微调。使用联邦学习，维护数据隐私和安全性更加简单。这种方法有助于[模型从本地化数据中学习](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/)，而无需共享敏感信息。

让我们回到医院的例子。医院已决定加入与其他医院的合作计划，旨在建立一个更复杂的模型，以根据来自各种医疗记录的见解来改善预测和护理结果。但有一个问题：医院不能公开这些文件，因为法规指定患者为其数据的所有者。

这就是联邦学习与 SLM 结合可以改变游戏规则的地方。每家医院都可以使用其患者记录来训练自己的 SLM。然后，它只能将学习到的参数上传到共享数据库，从而使所有贡献者受益，同时保持隐私。然后，服务器根据收到的更新构建全局模型，而无需访问单个文件。

同样的原则适用于所有涉及敏感数据的情况。例如，在客户数据需要严格安全性的投资领域，来自投资模式共享参数的见解可以帮助银行业开发更有效的计划。联邦学习促进了贡献者（无论是个人、设备还是组织）之间的协作。它通过提供数据而不损害数据隐私来改进模型。该技术还确保符合隐私法规。

开发人员可以使用开源项目进行联邦学习，例如 Flower、Substra、NVFlare 等。这些框架实施数据安全，并通过差异隐私、同态加密和机密计算等技术确保隐私。

## 结论

小型语言模型 (SLM) 在效率、隐私和适应性之间实现了出色的平衡，使其成为各种应用的理想选择。在医疗保健领域，快速的设备上症状诊断也可能成为远程医疗（一个新兴的医疗保健子领域）的差异化因素。

工业物联网、国防和金融科技等行业可以利用 SLM 进行实时分析、增强安全性和定制解决方案。这些行业可以进一步受益于其对多语言和多模式输入的适应性。例如，金融科技行业可以使用 SLM 进行多语言客户支持和用于各种数据集的本地化模型。由于 SLM 在本地部署，因此它们更安全且更易于解释，这在监管合规性是优先事项的领域提供了透明度。
