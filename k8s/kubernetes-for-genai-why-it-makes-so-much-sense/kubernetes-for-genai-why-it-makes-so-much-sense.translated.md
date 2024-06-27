# Kubernetes 与生成式 AI：为何如此契合

![Kubernetes 与生成式 AI：为何如此契合 的特色图片](https://cdn.thenewstack.io/media/2024/06/b26282f2-kubernetesforgenai-1024x576.jpg)

[生成式 AI（或 GenAI）](https://thenewstack.io/ai/) 正在迅速发展，成为许多组织不可或缺的一部分。它已超越简单的预测，通过代码补全、自动化、深度知识和专业知识来增强应用程序。无论您的用例是基于 Web 的聊天、客户服务、文档搜索、内容生成、图像处理、基础设施故障排除还是无数其他功能，GenAI 都承诺帮助我们成为更高效的解决问题者。

[Kubernetes](https://thenewstack.io/kubernetes/) 最近迎来了 [十周年纪念](https://www.dell.com/community/en/conversations/developer-blog/a-big-toast-celebrating-kubernetes-10th-birthday/6663114a1980ce7ac8c15e7e)，它为运行 GenAI 工作负载提供了宝贵的特性。多年来，Kubernetes 和云原生社区一直在改进、集成和自动化众多基础设施层，以简化管理员、开发人员和运维人员的工作。

GenAI 可以利用这些工作来构建在 Kubernetes 之上运行良好的框架。例如，[Operator Framework](https://operatorframework.io/) 已经被用于在 Kubernetes 中采用 GenAI，因为它允许以自动化和可扩展的方式构建应用程序。

让我们更深入地了解一下为什么 Kubernetes 是构建 GenAI 工作负载的理想选择。

## 为什么在 Kubernetes 上运行生成式 AI 很有意义

[Kubernetes](https://roadmap.sh/kubernetes) 为任何类型的应用程序提供了构建块。它提供了工作负载调度、自动化、[可观察性](https://thenewstack.io/10-ways-kubernetes-observability-boosts-productivity-cuts-costs/)、持久存储、安全、网络、高可用性、节点标签和其他对 GenAI 和其他应用程序至关重要的功能。

例如，将像 [Google](https://cloud.google.com/?utm_content=inline+mention) 的 Gemma 或 Meta 的 Llama2 这样的基础 GenAI 模型提供给具有图形处理单元 (GPU) 的工作节点。Kubernetes 的内置 [容器存储接口 (CSI)](https://thenewstack.io/how-the-container-storage-interface-csi-boosts-cloud-native-devops/) 驱动机制使为模型公开持久共享存储变得更加简单，以便推理引擎可以快速将其加载到 GPU 的核心内存中。

另一个例子是在 [检索增强生成 (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/) 管道中运行 [像 Chroma 这样的向量数据库](https://github.com/amikos-tech/chromadb-chart)。数据库通常需要保持高可用性，Kubernetes 的内置调度功能与 CSI 驱动程序相结合，可以使向量数据库迁移到 Kubernetes 集群中的不同工作节点。这在节点、网络、区域和其他故障的情况下至关重要，因为它可以使您的管道保持运行并访问嵌入。

无论您是在关注可观察性、网络还是更多其他方面，Kubernetes 都是 GenAI 应用程序的理想选择，因为它具有“自带电池”的架构。

## 在 Kubernetes 上启用 GPU

上游 Kubernetes 支持通过其 [设备插件框架](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) 管理 [Intel](https://www.granulate.io?utm_content=inline+mention)、[AMD](https://www.amd.com/en/products/processors/server/epyc/google-cloud.html?utm_content=inline+mention) [和 NVIDIA GPU](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)，只要管理员已将必要的硬件和驱动程序配置并安装到节点上。

这与通过插件和操作员进行的第三方集成相结合，为 Kubernetes 设置了启用 GenAI 工作负载所需的必要构建块。

供应商支持，例如 [Intel 设备插件操作员](https://operatorhub.io/operator/intel-device-plugins-operator) 和 [NVIDIA GPU 操作员](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html)，也可以帮助简化管理开销。例如，NVIDIA GPU 操作员有助于管理驱动程序、[CUDA](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/) 运行时和 [容器工具包](https://github.com/NVIDIA/nvidia-container-toolkit) 的安装和生命周期，而无需单独执行它们。

## 部署模型和推理引擎
在 Kubernetes 集群上启用 GPU 只是完整 GenAI 拼图中的一小部分。GPU 是在 Kubernetes 上运行 GenAI 模型所必需的；但是，完整的基础设施层还包括其他元素，例如共享存储、[推理](https://infohub.delltechnologies.com/en-us/l/design-guide-generative-ai-in-the-enterprise-inferencing/what-is-inferencing-1/)引擎、服务层、嵌入模型、Web 应用程序和批处理作业，这些都是运行 GenAI 应用程序所必需的。

一旦模型经过训练并可用，就需要将模型下载并拉取到 Kubernetes 环境中。许多基础模型可以从 [Hugging Face](https://huggingface.co/models) 下载，然后加载到服务层，服务层是推理服务器或引擎的一部分。

推理引擎或服务器，例如 [NVIDIA Triton 推理服务器](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/getting_started/quickstart.html) 和 [Hugging Face 文本生成接口](https://github.com/huggingface/text-generation-inference) (TGI)，由与预训练模型交互的软件组成。它加载和卸载模型，处理对模型的请求，返回结果，监控日志和版本等等。

推理引擎和服务层不必在 Kubernetes 上运行，但这里将重点介绍这一点。您可以通过 [Helm](https://thenewstack.io/get-started-with-the-helm-kubernetes-package-manager/) 将 Hugging Face TGI 部署到 Kubernetes，Helm 是一个 Kubernetes 应用程序包管理器。这个 [来自 Substratus AI 的 Helm 图表](https://github.com/substratusai/helm/tree/main/charts/text-generation-inference) 是一个示例，说明如何使用简单的配置文件来定义模型和 GPU 标记的节点，将 TGI 部署到 Kubernetes 环境并使其可用。

## 数据和存储
除了馈送到训练过程中的原始 [数据集](https://huggingface.co/datasets) 之外，运行模型和 GenAI 架构还需要几种类型的数据存储。

首先，在将 [大型语言模型 (LLM)](https://thenewstack.io/llm/) 下载到环境后，复制它们是不现实的，因为它们的大小可能从千兆字节到太字节不等。更好的方法是使用共享存储，例如高性能共享文件系统，如网络文件系统 (NFS)。这使得模型可以加载到共享存储中，并挂载到任何可能需要在可用 GPU 上加载和提供服务的节点。

数据存储的另一个潜在用例是运行 RAG 框架，以使用外部或更新的来源补充运行模型。RAG 框架通常使用矢量化数据和矢量数据库，而基于块存储的持久卷 (PV) 和持久卷声明 (PVC) 在 Kubernetes 中可以提高矢量数据库的可用性。

最后，利用模型的应用程序可能需要自己的持久性来存储用户数据、会话等等。这将高度依赖于应用程序及其数据存储需求。例如，聊天机器人可能会存储特定用户的最近提示查询，以保存历史记录以供回溯。

## RAG 框架
另一个部署场景是使用 [LlamaIndex](https://docs.llamaindex.ai/en/stable/) 或 [Langchain](https://python.langchain.com/v0.2/docs/tutorials/rag/) 等工具实现 RAG 或上下文增强框架。部署的基础模型通常在某个时间点对数据集进行训练，而 RAG 或上下文增强可以为 LLM 添加额外的上下文。这些框架在查询过程中添加了一个步骤，该步骤可以获取新来源的数据，并将该数据和用户查询馈送到 LLM。

例如，在公司文档上训练的模型可以实现 RAG 框架，以添加在模型训练后创建的新来源文档，为查询添加上下文。RAG 框架中的数据通常先加载，然后处理成更小的块（称为向量），并存储在 [嵌入](https://huggingface.co/blog/getting-started-with-embeddings) 中，这些嵌入位于 [矢量数据库](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/) 中，例如 [Chroma](https://github.com/amikos-tech/chromadb-chart)、[PGVector](https://github.com/pgvector/pgvector) 或 [Milvus](https://milvus.io/)。这些嵌入可以表示各种类型的数据，包括文本、音频和图像。

RAG 框架可以从嵌入中检索相关信息，模型可以使用这些信息作为其生成响应中的额外上下文。矢量数据通常比模型更紧凑，更小，但仍然可以从使用持久存储中受益。
使用 [Kubernetes 运行有状态工作负载](https://dok.community/community/) 并非新鲜事。现有项目，例如 Postgres，可以将 PGVector 扩展添加到 [通过 CloudNativePG 使用 PVC 部署的 Postgres 集群](https://github.com/cloudnative-pg/cloudnative-pg/blob/v1.23.1/docs/src/samples/cluster-pvc-template.yaml) 中。PVC 使数据库持久位置的高可用性成为可能，从而允许数据在 Kubernetes 集群中移动。这对于 RAG 框架在发生故障或 Pod 生命周期事件时的健康状况至关重要。

## 结论

Kubernetes 提供了一个 GenAI 工具箱，支持计算调度、第三方操作符、存储集成、GPU 支持、安全框架、监控和日志记录、应用程序生命周期管理等等。所有这些都是将 Kubernetes 作为 GenAI 平台的重大战术优势。

最终，将 Kubernetes 作为 GenAI 应用程序的平台，将它为运营商、工程师、DevOps 专业人员和应用程序开发人员提供的优势扩展到 GenAI 基础设施和应用程序的部署和可用性。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等等。