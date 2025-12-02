<!--
title: KServe 携手 CNCF，共促 Kubernetes AI 模型服务标准化
cover: https://cdn.thenewstack.io/media/2025/11/62a45454-kubecon-kserve.png
summary: KServe成为CNCF孵化项目，提供Kubernetes上AI（预测和生成式）模型服务的可扩展开源平台。支持多框架、高级部署、自动扩缩及LLM优化。
-->

KServe成为CNCF孵化项目，提供Kubernetes上AI（预测和生成式）模型服务的可扩展开源平台。支持多框架、高级部署、自动扩缩及LLM优化。

> 译自：[KServe Joins CNCF To Standardize AI Model Serving on Kubernetes](https://thenewstack.io/kserve-joins-cncf-to-standardize-ai-model-serving-on-kubernetes/)
> 
> 作者：Joab Jackson

上个月在 [KubeCon+CloudNativeCon 北美](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) 大会上，[云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 接受开源 [KServe](https://kserve.github.io/website/) 软件作为孵化项目。

KServe 在 [云原生领域](https://thenewstack.io/cloud-native/) 的突出地位表明了 Kubernetes 已成为 AI 计算的基石，为企业运行自己的生成式 AI 和预测工作提供了 [可扩展的开源平台](https://thenewstack.io/kserve-a-robust-and-extensible-cloud-native-model-server/)。

TOC 发起人 Kevin Wang 在一份声明中表示：“现代 AI 工作负载日益增长的复杂性，迫切需要基于 Kubernetes 健壮且标准化的 [模型服务平台](https://thenewstack.io/model-server-the-critical-building-block-of-mlops/)。”“它对可扩展性的关注，特别是大型语言模型的多节点推理，是为云原生 AI 基础设施提供高效服务和部署解决方案的关键。”

根据 CNCF 的说法，KServe 开发团队将按照 [CNCF 毕业标准](https://github.com/cncf/toc/blob/main/process/graduation_criteria.md) 努力，目标是成为“一个完全抽象、弹性推理平台，用户只需关注模型和预/后处理，而 KServe 则负责编排、扩展、资源管理和部署。”

## KServe 的起源与演进

KServe 的作用是什么？它定义了模型在组织内部如何提供服务，提供了一个单一的 API 来访问。

Bloomberg 人工智能基础设施高级工程师 Alexa Griffith 在 KubeCon 的演示中解释道，它“为我们提供了一种标准化的可扩展方式，可以在本地运行自托管模型，并为每个模型提供一个网关可以通信的稳定内部端点。”

[Google](https://cloud.google.com/?utm_content=inline+mention)、[IBM](https://www.ibm.com/cloud?utm_content=inline+mention)、[Bloomberg](https://thenewstack.io/why-bloombergs-openapi-participation-is-important-for-the-financial-industry/)、[Nvidia](https://thenewstack.io/nvidias-ai-factories-and-agentic-software-development/) 和 Seldon Technologies LLC 共同创建了 KServe，于 2019 年最初在 [KubeFlow 项目](https://thenewstack.io/smooth-sailing-for-kubeflow-1-9-thanks-to-cncf-red-hat-support/) 下发布（当时名为“KFServing”）。

该项目随后于 2022 年捐赠给 LF AI and Data Foundation，并于去年九月提交给 CNCF。2022 年 9 月，该项目从 KFServing 更名为独立的 KServe，从 Kubeflow 中毕业。KServe 随后于 2025 年 9 月作为孵化项目加入 CNCF。

该软件最初是为预测推理而构建的，但在 [ChatGPT 激发了公众的想象力](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/) 后，扩展到 [基于 LLM](https://thenewstack.io/introduction-to-llms/) 的生成式 AI 用途。Griffith 说，Bloomberg 在运行 LLM 时遇到的每一个问题，都帮助 KServe 构建了对生成式 AI 工作的支持。

[![演示截图](https://cdn.thenewstack.io/media/2025/11/12686ed3-kubecon-kserve-griffith.png)](https://cdn.thenewstack.io/media/2025/11/12686ed3-kubecon-kserve-griffith.png)

尽管 KServe 是为预测推理而构建的，但该项目“为生成式 AI 创造了所有这些新功能”——Bloomberg 的 Alexa Griffith

## 理解 KServe 的核心组件

KServe 实际上有三个组件。其一是同名的 **KServe Kubernetes 控制器**，它协调定义 ML 资源和其他 Kubernetes 对象的 KServe 自定义资源定义（CRD）。InferenceService CRD 管理预测推理，而 LLMInferenceService CRD 则涵盖生成式 AI 用例。

[ModelMesh](https://kserve.github.io/website/docs/admin-guide/modelmesh) 是模型的管理和路由层，旨在快速切换模型用例。而 [开放推理协议](https://kserve.github.io/website/docs/concepts/architecture/data-plane/v2-protocol) 则通过 HTTP 或 [gRPC](https://thenewstack.io/grpc-a-deep-dive-into-the-communication-pattern/) 提供了一种标准方式，用于跨不同 ML 框架的服务运行时执行机器学习模型推理。

CNCF [技术监督委员会](https://www.cncf.io/people/technical-oversight-committee/) 发起人 Faseela K 在一份声明中解释说：“在技术方面，KServe 与 Envoy、Knative 和 Gateway API 的深度集成使其在 CNCF 生态系统中具有强大根基。”“社区的包容性使得新的贡献者和使用者很容易参与进来，这充分说明了它的健康和开放性。”

[![营销图表](https://cdn.thenewstack.io/media/2025/11/e8ec80e1-kserve_new.png)](https://cdn.thenewstack.io/media/2025/11/e8ec80e1-kserve_new.png)

## 预测和生成式 AI 的关键特性

对于预测建模任务，KServe 提供：

*   **多框架**支持，涵盖 [TensorFlow](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/)、Python 的 [PyTorch](https://thenewstack.io/why-pytorch-won/) 和 [scikit-learn](https://scikit-learn.org/stable/)、[XGBoost](https://xgboost.readthedocs.io/en/stable/)、[ONNX](https://thenewstack.io/why-the-frontend-should-run-ai-models-locally-with-onnx/) 等。
*   **智能路由**，了解预测器、转换器和解释器组件的路由需求，并进行自动流量管理。
*   用于 [金丝雀发布](https://thenewstack.io/primer-blue-green-deployments-and-canary-releases/)、推理管道和带有 [InferenceGraph](https://thenewstack.io/a-guide-to-model-composition/) 的集成模型的**高级部署模式**。
*   **自动扩缩**，包括缩容到零的能力。

对于 [生成式 AI](https://thenewstack.io/the-production-generative-ai-stack-architecture-and-components/)，该软件提供：

*   **LLM 优化**：与 OpenAI 兼容的推理协议，可与大型语言模型无缝集成。
*   **GPU 加速**：支持 GPU 的高性能服务，并为大型模型优化内存管理。
*   **模型缓存**：智能模型缓存，减少加载时间，提高常用模型的响应延迟。

目前，该项目有 19 位维护者，以及 300 多位贡献者。超过 30 家公司采用了该技术，并为项目做出了贡献或仅使用该技术。它已获得超过 [4,600 个 GitHub 星](https://github.com/kserve/kserve)。