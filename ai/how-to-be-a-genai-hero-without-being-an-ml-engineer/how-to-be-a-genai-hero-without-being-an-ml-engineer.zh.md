*Vishnu Kammari 也对本文有所贡献。*

生成式 AI (GenAI) 正在迅速成为现代商业战略的基石，许多组织积极地将 AI 功能集成到他们的软件和工作流程中。 虽然企业正在积极推进概念验证 (PoC)，但通常需要专业的知识才能将这些转化为生产工作负载，这在超越初始实施方面造成了障碍。

## 选择 AI 栈：令人难以承受、耗时

AI 的快速发展——由新技术、改进的模型、尖端的 GPU 和开源创新驱动——增加了另一层复杂性。 组织必须不断重新评估其 AI 栈，以避免依赖过时的技术。 例如，Meta 频繁发布 [Llama 模型](https://thenewstack.io/get-started-with-metas-llama-stack-using-conda-and-ollama/)，这既为创新提供了机会，也为在评估和微调期间跟上最新版本带来了挑战。

除了模型选择之外，组织还面临着有效管理高成本 GPU 计算资源的艰巨任务。围绕购买、扩展和优化这些资产的决策已成为驾驭 GenAI 格局的关键。 在这些因素的影响下，组织必须不断完善其战略，以平衡创新与实用性。

组织采用 AI 的方式存在明显的差异，从运营 1-10 个裸金属实例的小规模用户，到运行大规模 GPU 集群以开发下一代 [大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/) 的企业。

管理大型集群并训练尖端 LLM 的组织往往走在行业进步的前沿，通过对工具和技术的战略投资来有效地优化基础设施。 最重要的是，他们拥有专注于 GenAI 方法的专业机器学习 (ML) 工程师。 另一方面，希望将 GenAI 应用于实际用例（例如使用现有 LLM）的企业，通常会寻求云提供商或系统集成商的指导，以了解最佳实践、高效技术和基础步骤。

例如，一家大型保险提供商正在进行一个由 AI 驱动的客户服务聊天机器人的 PoC。 通过利用历史客户互动，他们旨在缩短解决时间并提高支持质量。 然而，确定正确的微调方法、选择理想的模型、与 MLOps 管道集成以及优化 GPU 使用提出了复杂的挑战，需要仔细考虑和数月的研究才能开始。 即使是[选择最适合此场景和未来增长的 GPU 类型](https://thenewstack.io/ebooks/cloud-infrastructure/developers-guide-to-cloud-infrastructure-efficiency-and-sustainability/)的决策，以及对如何扩展和管理此基础设施的担忧，也增加了数月的时间，从而减慢了项目速度。

诸如此类的场景在各个行业都很常见，这促使我们转向 [开源世界](https://thenewstack.io/open-source/)，以构建一种新的解决方案来帮助简化不同用例的部署过程。

## 开源解决方案如何缩短部署时间

经过几个月的工作，确定了 GenAI 应用程序的几种场景、重复出现的用例和模式后，我们发布了 [OCI AI Blueprints](http://www.oracle.com/application-development/ai-blueprints/?source=:ex:pw:::::TNS_OCIAIBlueprints_C&SC=:ex:pw:::::TNS_OCIAIBlueprints_C&pcode=)。 这个免费使用的无代码部署平台构建于 Kubernetes 之上，将 Oracle 最佳实践、默认基础设施和 ML 应用程序层配置打包为单个部署清单文件。

每个蓝图清单都针对一个常见的 GenAI 实施场景量身定制。 无需手动将传统的 [Terraform](https://thenewstack.io/how-to-use-terraforms-for_each-with-examples/) 用于基础设施和 Kubernetes YAML 清单用于软件配置，同时在库之间进行选择，使用蓝图可以将您在几分钟内启动并运行所需的元素，只需在平台内单击一下即可。

但是，在 GPU 上启动新的 AI 应用程序只是第一步。 有效地管理基础设施依赖项可能会带来压力，尤其是在新工作负载意外扩展时。 这需要端到端**可观测性**和集群管理功能，以将软件栈配置和基础设施依赖项决策整合到单个控制平面中。

OCI AI Blueprints 部署的控制平面是一个提供程序集，它了解与 Prometheus、KEDA 和 KubeRay 等多个开源软件组件相关的配置，以及构成部署清单文件的与 OCI 相关的基础设施配置，例如文件存储服务 (FSS)。 开发人员不再需要手动将 FSS 作为其 ML 应用程序部署的一部分，因为控制平面具有无需接触 OCI 控制台即可理解和创建一个 FSS 的逻辑。

例如，LLM 服务，涉及部署预训练的语言模型来处理生产环境中的推理请求，是聊天机器人的日常用例。 研究要选择的软件平台、什么硬件是最佳的、需要什么 [Kubernetes](https://thenewstack.io/kubernetes/) 配置等等，可能需要数周的评估。 以下 OCI AI Blueprint 部署清单具有基础设施组件、使用 KEDA 的复制设置和基于 Prometheus 的扩展设置、vLLM 代码和 LLM 推理服务器集成以及 LLM。 所有这些都在一个部署清单中，使其变得简单明了。

我们有一位客户使用此推理配方来快速启动 GPU 节点，并为其业务流程管理平台部署用于文档和图像批量处理用例的多模态 LLM。 以前，该过程需要数周的时间，但一个开源的无代码解决方案使其团队能够完全自动化整个过程并在几天内取得成功。 此外，通过此蓝图部署和管理的自动扩展和共享存储，针对此批量推理场景优化了 GPU 资源利用率。

感谢开源工具，您无需成为 ML 工程师或拥有专业知识即可启动并运行这些蓝图。 这些蓝图经过打包和简化，可以通过专用的 OCI AI Blueprints 平台进行部署，但对于开发人员使用基于 API 的部署来说，它也足够灵活。

*了解更多关于 [OCI AI Blueprints](http://www.oracle.com/application-development/ai-blueprints/?source=:ex:pw:::::TNS_OCIAIBlueprints_C&SC=:ex:pw:::::TNS_OCIAIBlueprints_C&pcode=) 的信息，或访问 [GitHub 仓库](https://github.com/oracle-quickstart/oci-ai-blueprints) 以开始使用。*