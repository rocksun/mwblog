
<!--
title: Knative 正式毕业，荣膺 CNCF 毕业项目
cover: https://cdn.thenewstack.io/media/2025/11/bb820809-md-duran-1vqhrwxcccw-unsplash.jpg
summary: Knative 已从 CNCF 毕业，成为无服务器和事件驱动应用的开源 Kubernetes 原生平台。它简化了 Kubernetes 的部署和管理，支持 Serving 和 Eventing 组件，并已集成 CloudEvents、Buildpacks 和 Tekton。Knative 现已支持 Kubernetes Gateway API，并转向 OpenTelemetry。该平台已被多家云提供商采用，并在 AI 领域展现出潜力。Knative 被视为 AWS Lambda 和 Azure Functions 的有力竞争者，为用户提供了供应商中立性和跨云部署能力。
-->

Knative 已从 CNCF 毕业，成为无服务器和事件驱动应用的开源 Kubernetes 原生平台。它简化了 Kubernetes 的部署和管理，支持 Serving 和 Eventing 组件，并已集成 CloudEvents、Buildpacks 和 Tekton。Knative 现已支持 Kubernetes Gateway API，并转向 OpenTelemetry。该平台已被多家云提供商采用，并在 AI 领域展现出潜力。Knative 被视为 AWS Lambda 和 Azure Functions 的有力竞争者，为用户提供了供应商中立性和跨云部署能力。

> 译自：[Knative Has Finally Graduated From the CNCF](https://thenewstack.io/knative-has-finally-graduated-from-the-cncf/)
> 
> 作者：Steven J. Vaughan-Nichols

亚特兰大 — [Knative](https://knative.dev/) 是一个用于构建、部署和运行无服务器及事件驱动型应用的开源 [Kubernetes](https://thenewstack.io/kubernetes/) 原生平台，现已[正式从](https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/) [云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 毕业。这花费了七年多的时间，但它终于实现了。

大家一致认为，Knative 的目标是简化 Kubernetes 上现代工作负载的部署和管理，通过抽象掉自动扩缩、路由和事件交付等基础设施复杂性。这是一个很好的目标。这使得开发人员能够专注于业务逻辑和应用程序架构，而不是迷失在 Kubernetes 的复杂细节中。

正如 Knative 联合创始人 Evan Anderson 在 Knative 发布时的新闻稿中所说：“Knative 填补了云原生生态系统中的一些空白，成为进入 Kubernetes 的一个简单入口，而 Knative 的事件处理机制则充当了连接事件到响应的缺失骨架。”

## Serving 和 Eventing

具体来说，Knative 的核心组件 Serving 和 Eventing 使开发人员能够部署容器化应用程序，这些应用程序在不使用时自动扩缩到零，从而降低基础设施成本并提高效率。Eventing 提供了一种通过事件连接应用程序的统一方式，使得构建事件驱动型架构更加容易。Knative 集成了 [CloudEvents 规范](https://cloudevents.io/)，并支持云原生 [Buildpacks](https://buildpacks.io/) 和 [Tekton](https://tekton.dev/)，后者是用于创建 [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) 流水线的开源框架。

此外，Eventing 现在集成了 [Apache Camel Kamelets](https://camel.apache.org/camel-k/2.8.x/kamelets/kamelets.html) — 将新的事件源引入生态系统。对于 Serving，Knative 正在采用 [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) 来简化网络堆栈，并引入更安全的容器设置为默认值以提高安全态势。该项目还已从 [OpenCensus](https://opencensus.io/) 切换到更受欢迎的 [OpenTelemetry](https://opentelemetry.io/) 用于指标和跟踪。

包括阿里云、Scaleway 和 Gojek 在内的主要云提供商和企业，已经采用 Knative 来支持其无服务器函数、AI 推理模型和可扩缩自动化平台。该平台处理从 AI 到金融等各种工作负载的能力也使其成为一个有吸引力的选择。

正如 CNCF 首席技术官 Chris Aniszczyk 在 KubeCon 上所说：“Knative 的毕业反映了 Kubernetes 和 CNCF 生态系统中无服务器技术的成熟。Knative 已经建立了强大的贡献者基础，赢得了最终用户的信任，并继续通过集成来满足从新型 AI 工作负载到互操作性的各种需求。”

考虑到 AI，[红帽 (Red Hat)](https://www.openshift.com/try?utm_content=inline+mention) 特别致力于如何将 [Knative Functions](https://knative.dev/docs/functions/) 与 [Llama Stack](https://github.com/llamastack/llama-stack) 结合使用，后者是一个用于[构建生成式 AI (GenAI) 应用程序](https://knative.dev/blog/articles/ai_functions_llama_stack/)的开源框架。红帽也参与了[将大型语言模型 (LLMs) 作为代理与 Knative 集成](https://knative.dev/blog/articles/llm-agents-overview/)的工作。最后，红帽还在[使用 Knative 开发复杂的 AI 代理系统](https://knative.dev/blog/articles/knative-eventing-eda-agents/)。

## 更激烈的竞争

在 KubeCon 上，几位不愿透露姓名的人告诉我，他们预计，在 CNCF 的认可下，Knative 将被视为 [AWS](https://aws.amazon.com/?utm_content=inline+mention) [Lambda](https://aws.amazon.com/lambda/) 和 [Azure Functions](https://azure.microsoft.com/en-us/products/functions) 更强大的竞争对手。

尽管它们在[架构、用例和操作理念上存在显著差异](https://developers.redhat.com/articles/2023/10/19/knative-versus-aws-lambda-and-azure-functions)，但它们都提供了无服务器和事件驱动功能，允许开发人员在自动扩缩的情况下运行代码，而无需管理底层服务器资源。

当然，[AWS](https://aws.amazon.com/?utm_content=inline+mention) Lambda 和 Azure Functions 与各自的云基础设施紧密结合，而 Knative 是一个运行在 Kubernetes 之上的开源项目。这意味着使用 Knative 的公司可以保持供应商中立。它还赋予了他们在任何 Kubernetes 运行的地方运行无服务器工作负载的能力，包括多云或本地环境。

这是否足以推动 Knative 达到 [Market Intelo](https://marketintelo.com/) 预测的到 2033 年将达到[32 亿美元市场规模](https://marketintelo.com/report/managed-knative-services-market)，同时以 24.8% 的强劲复合年增长率 (CAGR) 增长？敬请关注。我们拭目以待。