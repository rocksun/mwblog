[红帽](https://www.redhat.com/en)在企业中部署AI已有一段时间。例如，[红帽企业版Linux (RHEL) 现在已具备AI工作能力](https://thenewstack.io/red-hat-enterprise-linux-10-an-ai-driven-quantum-ready-platform/)；[红帽拥有自己的推理引擎](https://thenewstack.io/red-hats-ai-platform-now-has-an-ai-inference-server/)；该公司还提供[AI驱动的系统管理员工具](https://thenewstack.io/red-hat-goes-all-in-on-ai-powered-lightspeed-system-admin-tools/)。

现在，红帽正将自己定位为全栈AI平台供应商。这家IBM旗下的Linux巨头通过新的[红帽AI企业版 (RHAE)](https://www.redhat.com/en/products/ai/enterprise)套件以及与NVIDIA联合工程的[红帽AI工厂](https://www.redhat.com/en/about/press-releases/red-hat-ai-factory-nvidia-accelerates-path-to-scalable-production-ai)来实现这一目标。

**红帽AI企业版**

RHAE是一个新的集成AI平台，旨在以RHEL和OpenShift为基础，在混合环境中部署和管理模型、智能体和应用程序。红帽将其宣传为一个“从裸机到智能体”的堆栈，它统一了AI生命周期，使IT部门能够像管理任何其他企业系统一样管理AI，而不是将其作为永远无法投入生产的孤立试点项目。

该平台捆绑了高性能推理、模型调优和定制、以及智能体部署和管理，并支持“任何模型、任何硬件、任何环境”，只要它能够部署在红帽的Linux和Kubernetes平台之上。红帽认为，这种方法提供了一个更一致、更安全强化的环境，用于大规模运行AI，并且使用企业围绕OpenShift已有的相同工具和流程。

这都是红帽一贯的集成堆栈方法的一部分。

除了AI企业版，红帽还推出了[红帽AI 3.3](https://www.redhat.com/en/about/press-releases/red-hat-launches-red-hat-ai-enterprise-deliver-unified-ai-platform-spans-metal-agents?intcmp=RHCTG0260000475259)。该版本通过OpenShift AI Catalog增加了Mistral-Large-3、Nemotron-Nano和Apertus-8B-Instruct等模型的压缩版、生产就绪版。它还支持Mistral 3和DeepSeek-V3.2等较新模型，以及多模态升级，包括更快的Whisper语音处理和增强的智能体工作流工具调用。

AI 3.3还引入了模型即服务的技术预览，通过API网关为内部用户提供对私有托管模型的自助访问，从而标准化了大型组织内AI的消费方式。

在硬件方面，红帽正在扩大支持范围，包括在英特尔CPU上为小型语言模型提供生成式AI支持，扩大对NVIDIA Blackwell Ultra GPU和AMD MI325X加速器的认证，并增加了内部GPU即服务功能，例如自动检查点，以防止长时间运行的任务丢失工作。

为了解决治理和软件供应链问题，红帽正在添加一个新的AI Python索引，作为一个可信存储库，其中包含关键AI工具的强化版本。这些工具包括Docling（一个IBM开发的开源工具包，用于将非结构化文档转换为机器可读格式以进行模型训练）和SDG Hub（一个用于构建合成数据生成管道的框架，用于微调大型语言模型）。

该公司还在加强AI可观测性和安全性，通过更详细的跨工作负载遥测数据，以及集成了NVIDIA NeMo Guardrails的技术预览版，以在AI交互中强制执行策略和保持一致性。

**红帽AI工厂**

现在也是介绍红帽与NVIDIA合作的红帽AI工厂的好时机。这是红帽最近[为NVIDIA Vera Rubin AI平台发布定制RHEL](https://thenewstack.io/red-hat-customizes-rhel-for-nvidias-vera-rubin-ai-platform/)的直接后续。这个新的联合工程软件平台将RHAE与NVIDIA AI Enterprise结合起来，创建了这些公司所称的为大规模部署而优化的端到端AI堆栈。

AI工厂直接面向那些试图从临时AI项目转向“工业级”生产系统的企业。它旨在帮助运营团队在统一管理下，同时管理传统基础设施和AI特定需求，从配置和GPU编排到模型性能和安全性。

这个联合平台专注于三个主要主题：价值实现时间、性能和成本、以及企业安全态势。为了加快部署，客户可以获得简化的工作流，并立即访问预配置模型，包括IBM经补偿的Granite系列以及通过NVIDIA NIM微服务交付的NVIDIA Nemotron和NVIDIA Cosmos开放模型，同时NVIDIA NeMo可用于企业数据调优。

在性能方面，AI工厂依赖于红帽的推理堆栈，该堆栈由流行的开源推理引擎vLLM以及NVIDIA的TensorRT-LLM、Dynamo和BlueField数据处理单元等技术提供支持。这与内置的**可观测性**相结合，旨在帮助组织满足严格的服务水平目标并降低AI总拥有成本。

红帽首席技术官 Chris Wright 将与NVIDIA合作的AI工厂描述为从AI实验向“工业级、企业级生产”更广泛转变的一部分，他认为以与核心IT平台相同的严谨性管理整个AI计算堆栈，现在对大型组织来说是必不可少的。在这两种情况下，红帽都认为其在混合云基础设施方面长期积累的专业知识，将使其在企业寻求在多个环境中标准化AI时获得优势。

红帽还在争取生态系统支持，Cisco、Dell、Lenovo、Supermicro、TD SYNNEX和WWT等公司都表示计划围绕AI企业版和AI工厂提供经过验证的基础设施和渠道产品。他们的作用是将红帽的软件与AI优化硬件和服务打包，以便客户可以将AI视为标准的企业工作负载，而不是一个定制的科学项目。所以，如果你喜欢主要基于NVIDIA硬件的单一AI软件堆栈理念，那么红帽非常乐意与你交流。