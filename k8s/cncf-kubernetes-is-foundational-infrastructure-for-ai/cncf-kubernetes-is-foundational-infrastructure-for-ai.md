<!--
title: CNCF：Kubernetes是AI的“基石”基础设施
cover: https://cdn.thenewstack.io/media/2026/01/aaa8c252-cncf.png
summary: CNCF报告指出，Kubernetes已成为AI基础设施的基石，尤其是在AI部署和推理方面。云原生技术采用率普遍，CI/CD和容器应用成熟。尽管Wasm等面临挑战，但AI推理被视为下一个重要的云原生工作负载。
-->

CNCF报告指出，Kubernetes已成为AI基础设施的基石，尤其是在AI部署和推理方面。云原生技术采用率普遍，CI/CD和容器应用成熟。尽管Wasm等面临挑战，但AI推理被视为下一个重要的云原生工作负载。

> 译自：[CNCF: Kubernetes is 'foundational' infrastructure for AI](https://thenewstack.io/cncf-kubernetes-is-foundational-infrastructure-for-ai/)
> 
> 作者：Steven J. Vaughan-Nichols

最新的[云原生计算基金会](https://cncf.io/?utm_content=inline+mention) (CNCF) [年度云原生调查报告](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/)已经发布，报告宣称，“82%的容器用户在生产环境中运行Kubernetes，云原生已跨越了一个决定性的门槛。”

“曾经的实验性技术现在已成为基础。”

或者，正如CNCF首席技术官Chris Aniszczyk所说，“[Kubernetes不再是小众工具](https://www.cncf.io/blog/2026/01/20/kubernetes-fuels-ai-growth-organizational-culture-remains-the-decisive-factor/)；它是一个核心基础设施层，支持规模、可靠性以及日益增长的AI系统。”他继续说道，“98%的受访组织现在已采用云原生技术，使其成为现代企业基础设施的近乎通用标准。”

这一切都不足为奇。有趣的是，AI正在推动Kubernetes的采用。你可能会问，AI难道不依赖于GPU、张量处理单元 (TPU) 和定制AI专用集成电路 (ASIC) 吗？这些在典型的云数据中心里并不常见。确实如此，但那些是用于训练AI，而不是使用AI。

正如CNCF执行董事Jonathan Bryce在《云原生报告》的引言中写道，“66%的组织已经在使用Kubernetes来托管他们的生成式AI工作负载。但真正的故事不在头条新闻中。这无关训练大型语言模型（LLM）。大多数企业不构建或训练自己的模型——他们是消费者。真正的挑战是部署。”

## 云原生用于开发

根据CNCF的统计，[59%的组织现在将云原生用于“大部分”或“几乎所有”开发。](https://www.cncf.io/wp-content/uploads/2026/01/CNCF_Annual_Survey_Report_final.pdf)

其细分情况大致如下。云原生采用有四个级别，从探索者 (8%)、采用者 (32%)、实践者 (34%)，到创新者 (25%)。CNCF在报告中将其描述为“一个可预测的渐进模型”，其中[GitOps](https://thenewstack.io/gitops-in-the-real-world-barriers-and-best-practices/)作为“北极星指标：没有一个探索者实施了它，而58%的创新者运行符合GitOps的部署。”

CNCF还指出，[持续集成/持续部署](https://thenewstack.io/ci-cd/) (CI/CD) 在高端用户中几乎普遍。这意味着91%的成熟组织在生产环境中使用CI/CD工具，而74%的创新者每天多次提交代码。

与此同时，正如你所预期的，[容器](https://thenewstack.io/containers/)也在稳步投入生产。生产环境中的应用程序容器已从2023年的41%上升到2025年的56%。与此同时，仅试点的容器部署已降至区区6%。人们不再只是试用容器；他们直接将其投入部署。

与此同步，其他已毕业的CNCF项目，如Helm、etcd、CoreDNS、Prometheus和containerd，现在被75%及以上的受访者使用。这些并非唯一被采用的项目。特别是，孵化中的项目如CNI (生产环境中使用率为52%)、OpenTelemetry (49%)、gRPC (44%) 和Keycloak (42%) 因其快速采用而脱颖而出。

## 前方的挑战

一些备受关注的技术在部署方面表现不佳。特别是，[WebAssembly (Wasm)](https://thenewstack.io/webassembly/webassembly-what-beginners-need-to-know/)未能达到预期。65%的受访者表示他们没有Wasm经验，只有5%已在生产环境中部署了它。

随着其普及，AI将带来其自身的用途。

随着那些千兆瓦AI数据中心工厂开始上线，“我们将需要大大降低服务AI工作负载的难度，同时大幅增加整个行业的推理能力。我相信这将是下一个重要的云原生工作负载。”

这是一个我们都能预见即将实现 Prediction 的预测。