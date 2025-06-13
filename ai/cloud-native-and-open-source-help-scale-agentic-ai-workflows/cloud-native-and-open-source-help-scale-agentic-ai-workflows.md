
<!--
title: 云原生和开源助力扩展Agentic AI工作流
cover: https://cdn.thenewstack.io/media/2025/06/43fddf20-business.png
summary: Agentic AI爆火！云原生+开源才是王道！用 Kubernetes、Knative 搞定 SLM 部署，成本暴降！OCI、FaaS 加持，实时客户支持、DevOps 自动化、金融服务不在话下！Prometheus、Istio 监控优化，速来抄作业！
-->

Agentic AI爆火！云原生+开源才是王道！用 Kubernetes、Knative 搞定 SLM 部署，成本暴降！OCI、FaaS 加持，实时客户支持、DevOps 自动化、金融服务不在话下！Prometheus、Istio 监控优化，速来抄作业！

> 译自：[Cloud Native and Open Source Help Scale Agentic AI Workflows](https://thenewstack.io/cloud-native-and-open-source-help-scale-agentic-ai-workflows/)
> 
> 作者：Sanjay Basu

企业自动化越来越多地利用由 AI 驱动的智能代理工作流，这些应用通常依赖于大型语言模型（LLM）。虽然 LLM 可以解决许多通用用例，但这些模型的部署和编排会增加显著的复杂性和高昂的运营成本。

为了解决企业特定的用例，各组织已经开始看到较小模型的优势。因此，[小型语言模型（SLM）](https://thenewstack.io/the-rise-of-small-language-models/) 与现代云原生平台（如 [Kubernetes](https://thenewstack.io/kubernetes/) 和 [函数即服务（FaaS）](https://thenewstack.io/serverless/)）相结合，已成为解决 [agentic AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/) 用例的替代方案。

让我们探讨如何有效地使用云原生范例来部署和扩展基于 SLM 的 agentic 工作流。具体来说，如何使用 Kubernetes、Knative 和 serverless 平台来帮助动态管理推理工作负载、优化资源利用率并加速代理驱动的 AI 应用的创新。

## 为什么选择小型语言模型？

虽然 LLM 因其令人印象深刻的功能而广受欢迎，但它们的高计算要求和巨大的基础设施开销通常限制了它们的大规模实际部署。SLM 通常具有较少的参数和更精简的计算需求，可以在响应性、可扩展性和成本效益至关重要的场景中提供显著优势。

[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 的 [Phi-3-mini](https://thenewstack.io/how-to-get-started-running-small-language-models-at-the-edge/) 就是 SLM 的一个例子。它相对较少的参数（38 亿）转化为更小的内存占用和更快的处理时间。SLM 的其他例子包括 [Mistral 7B](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/)、[Llama 3.2](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/) 和 [Google](https://cloud.google.com/?utm_content=inline+mention) [Gemma 2B](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/)，它们非常适合在较小的 GPU 和 CPU 上运行。这些模型专为效率而设计，并且都可以在各种设置中部署，包括笔记本电脑等边缘设备。

对于许多 agentic 工作流，例如实时客户互动、DevOps 自动化、异常检测和数据丰富，SLM 往往能够提供足够的准确性并显著降低延迟。它们较小的占用空间使它们成为云原生架构的理想选择，强调敏捷性和成本效益。

## 云原生架构：Kubernetes 和 FaaS

云原生计算基金会（CNCF）生态系统提供了强大的工具，可以实现高效且可扩展的 AI 部署。核心是 Kubernetes，这是一个容器编排平台，以自动化应用程序部署、扩展和管理而闻名。Kubernetes 促进了容器化部署，从而实现了高效的资源分配和无缝的可扩展性。

一个丰富的 CNCF 项目生态系统补充了 Kubernetes，包括 Knative。这个 FaaS 平台为开发人员和 MLOps 团队提供了在 Kubernetes 上部署 serverless 工作负载的关键构建块，从而可以根据需求自动扩展，并通过动态管理容器生命周期来帮助降低运营开销。

将这些技术结合使用可以帮助组织快速部署基于 SLM 的代理，在不同的工作负载下无缝扩展并保持成本效益。

## 实际应用

为了创建以下实现，我们正在 [OCI Kubernetes Engine](https://www.oracle.com/cloud/cloud-native/kubernetes-engine/?source=:ex:pw:::::TNS_ScalingSLMS_May25&SC=:ex:pw:::::TNS_ScalingSLMS_May25&pcode=) (OKE) on [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/?source=:ex:pw:::::TNS_ScalingSLMs_May25_B&SC=:ex:pw:::::TNS_ScalingSLMS_May25_B&pcode=) (OCI). OKE 提供了一个完全托管的 Kubernetes 环境，简化了生产级 Kubernetes 集群的设置和操作。它符合 CNCF 的开源 Kubernetes，下面的示例也应该可以使用。此外，将 Knative 集成到 OKE 中可以为 SLM 部署创建一个强大的 serverless 基础设施。

**架构蓝图**

一个有效的云原生架构，利用 OCI、Kubernetes 和 FaaS 进行 SLM 部署，由几个关键组件组成，如下所列：

- **Oracle Kubernetes Engine (OKE)**: 管理 Kubernetes 集群，自动化编排、安全和扩展。
- **Knative Serving**: 提供 Serverless 功能，根据推理请求自动扩展 SLM 容器。
- **OCI object storage**: 存储模型工件和配置文件，方便部署和更新。
- **Prometheus and Grafana**: 通过 CNCF 工具集成；它们监控性能指标、资源利用率和扩展行为。
- **Istio service mesh**: 提供高级流量管理、安全和可观测性。

**分步部署指南**

**1. 准备您的 Kubernetes 集群**

使用 OCI 的托管 Kubernetes 服务来配置 Kubernetes 集群。 这简化了集群管理，让您可以自由地专注于部署细节：

```
oci ce cluster create --name my-oke-cluster --kubernetes-version v1.29.0
```

**2. 安装 Knative Serving**

使用 YAML 清单部署 Knative Serving，从而启用 Serverless 功能：

```
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.14.3/serving-crds.yaml
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.14.3/serving-core.yaml
```

**3. 容器化小型语言模型**

使用 Docker 或符合 OCI 标准的容器注册表，使用轻量级运行时环境（如 FastAPI 或 Flask）打包您的 SLM：

```dockerfile
FROM python:3.11-slim
COPY ./model ./model
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
```

**4. 通过 Knative 部署 Serverless SLM**

创建 Knative Service YAML 清单：

```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: slm-agent
spec:
  template:
    spec:
      containers:
        - image: oci-container-registry/my-slm-agent:v1.0
          resources:
            requests:
              cpu: 500m
              memory: 512Mi
```

应用清单以将您的模型部署为 Knative 服务：

```
kubectl apply -f slm-agent.yaml
```

Knative 会根据传入的请求自动扩展您的 SLM 代理，根据需要启动和关闭容器，从而优化资源使用和成本。

**5. 监控和优化**

使用通过 Helm chart 部署的 Prometheus 和 Grafana 等工具，监控 SLM 代理的性能、延迟和资源利用率：

```
helm install prometheus prometheus-community/kube-prometheus-stack
```

配置 Istio service mesh 以进行详细的流量管理和安全。

## 解决行业特定用例

**实时客户支持**

部署 SLM 代理以提供实时聊天支持可以通过显著减少响应延迟来帮助提高客户交互效率。云原生代理可以动态扩展以满足波动的需求，从而减少高峰使用期间的延迟。组织可以从运营成本降低中受益，因为 serverless 基础设施无需始终开启的配置，从而可以无缝扩展资源以精确匹配需求。

**DevOps 自动化**

将 SLM 代理与 Kubernetes 和 Knative 集成到 CI/CD 管道中，可以实现高效的自动化故障排除和主动异常检测。代理可以快速解释构建日志和测试输出，监控警报，诊断问题并提出立即修复建议。这有助于提高运营效率，减少停机时间，并通过帮助快速识别和解决管道瓶颈来简化 DevOps 流程。

**金融服务**

金融机构可以部署轻量级 SLM 代理，以更快地分析实时市场数据，从而在没有大型模型通常带来的繁重计算开销的情况下，实现快速且明智的决策。这些敏捷、可扩展的部署可以更有效地帮助处理大量并发查询，为交易员和金融分析师提供即时见解、趋势预测和风险评估，这对于知情的交易策略和解决法规遵从性至关重要。

## 结论

各组织正在努力了解 Agentic AI 提供的新范例，以提高运营效率。通过将 SLM 与 Kubernetes 和 FaaS 集成，企业可以使用可扩展、高效且响应迅速的基于代理的解决方案来帮助解决他们的用例。像 Oracle 的 OKE 这样的云原生解决方案，辅以 Knative、Prometheus 和 Istio 等 CNCF 工具，可以帮助简化运营，用于降低开销，并使组织能够快速且经济地交付创新的 AI 驱动的解决方案。 采用这种[云原生方法](https://thenewstack.io/cloud-native/10-key-attributes-of-cloud-native-applications/)使企业能够在日益敏捷和竞争激烈的环境中蓬勃发展。