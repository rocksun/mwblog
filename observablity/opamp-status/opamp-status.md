<!-- 

# 开放代理管理协议(OpAMP)2023年状态报告

 -->

作者：Jacob Aronoff (Lightstep)、Evan Bradley (Dynatrace)、Michael Hausenblas(AWS)、Andy Keller(observIQ公司)、Tigran Najaryan(Splunk)

译自 [Open Agent Management Protocol (OpAMP) State of the Nation 2023](https://opentelemetry.io/blog/2023/opamp-status/) 。

[开放代理管理协议(Open Agent Management Protocol, OpAMP)](https://opentelemetry.io/docs/collector/management/)是管理大规模遥测代理集群的新兴开放标准。2022年，Splunk 将 OpAMP 捐赠给 OpenTelemetry(OTel)项目，最初的反馈来自 observIQ，基于 observIQ 在 BindPlane 中使用的定制协议。[OpAMP 规范](https://github.com/open-telemetry/opamp-spec/blob/main/specification.md)定义了远程管理代理集群的网络协议。这些代理可以是任何东西，从遥测代理(如 [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/))到 [Fluent Bit](https://fluentbit.io/) 再到您环境中可能使用的定制代理。

在 OpAMP 中，我们区分服务器端，通常托管在控制平面，和客户端，在您要管理的各个代理中实现。例如，使用 OpAMP 来管理 OpenTelemetry Collector 集群，可能如下所示:

![](https://opentelemetry.io/blog/2023/opamp-status/opamp-concept.svg)


Collector 报告其状态并从 OpAMP 控制平面接收配置。OpAMP 协议与供应商无关，通用(不特定于 OTel)，因此 OpAMP 服务器可以远程监控和管理不同代理的集群。OpAMP 当前支持的功能包括:

- 代理(如 OpenTelemetry Collector)可以将其属性(如类型和版本)或主机操作系统详细信息报告给服务器(OpAMP 控制平面)。
- 服务器可以将配置推送到代理，并确保应用配置，例如通过重载代理。
- 您可以将代理自己的遥测(日志和指标)引入符合 OTLP 标准的可观察性后端。
- 用于升级和降级代理的安全自动更新功能。
- 内置连接凭据管理，包括客户端 TLS 证书吊销和轮换。

现在我们对 OpAMP 的概况以及它支持的功能有了一个粗略的了解，让我们看看它如何在 OpenTelemetry Collector 中实现。

在与 OTel 最终用户和 Collector 贡献者的讨论中，我们发现他们希望将 OpAMP 既作为收集器扩展(具有有限功能)使用，也作为(收集器外部的)监督程序来实现更广泛的 OpAMP 功能集。

> 注意: 如果您希望这里深入探讨，我们建议您阅读 [OpAMP for OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/cmd/opampsupervisor/specification) 文档，其中描述了如何实现这两种选项而最小化代码重复。

支持这两种模式的主要思想是在收集器中实现具有最小 OpAMP 功能集的扩展。此收集器扩展本身可以使用，也可以用来创建外部的监督程序，该监督程序使用扩展作为助手，并在扩展实现的基础上实现 OpAMP 的其余功能:

![](https://opentelemetry.io/blog/2023/opamp-status/opamp-supervisor.png)

让我们先详细了解一下收集器 OpAMP 扩展，然后再讨论 OpAMP 监督程序。

## OpAMP 扩展

[OpenTelemetry Collector OpAMP 扩展](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/16594)将在收集器内部实现 OpAMP 客户端，并将在独立模式和受监督模式下用于通过 OpAMP 管理收集器实例。与监督程序一起使用时 OpAMP 扩展的功能已在监督程序的设计文档中定义，其中扩展在很大程度上负责向监督程序提供引导信息并与之沟通收集器的有效配置。

## OpAMP 监督程序

OpAMP 监督程序将作为一个独立的二进制文件存在，它运行 OpenTelemetry Collector 实例并实现 OpAMP 客户端，通过将远程和本地配置源合并为收集器可以在启动时使用的文件，将配置从 OpAMP 服务器中继到收集器。 通过 OpAMP 协议管理收集器的受监督模式还将允许下载其他二进制文件，允许下载其他文件以及更新收集器。

此外，如果 OpAMP 服务器向监督程序发送“坏”配置，导致收集器无法启动，由于它作为一个独立的进程运行，监督程序可以与 OpAMP 服务器通信以通知此情况。 在实现 OpAMP 客户端的基础上，监督程序还将实现 OpAMP 服务器，在其中它将与收集器中的 OpAMP 扩展通信以接收关于收集器的信息。 我们在[设计文档](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/cmd/opampsupervisor/specification)中定义了监督程序的功能，并根据它向 [opentelemetry-collector-contrib 存储库](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/cmd/opampsupervisor)贡献了初始实现，并创建了问题回日志以指导进一步开发。

## Kubernetes 中的 OpAMP

在 OTel 中，我们通过 [OpenTelemetry Operator for Kubernetes](https://opentelemetry.io/docs/kubernetes/operator/) 专门支持 Kubernetes 作为计算平台。 在此背景下，我们也正在努力在 Kubernetes 中支持 OpAMP，这将通过部署到 OpenTelemetry Operator 的[桥接组件](https://docs.google.com/document/d/1M8VLNe_sv1MIfu5bUR5OV_vrMBnAI7IJN-7-IAr37JY/)提供:

![OpAMP 桥接组件在 OTel Operator 中](https://opentelemetry.io/blog/2023/opamp-status/opamp-kubernetes-bridge.png)

> 注意: 目前，我们不支持通过 Helm chart 进行部署，但是，如果您愿意贡献此功能，欢迎您贡献。

OpAMP 桥接组件是 OTel [SIG Kubernetes Operator](https://docs.google.com/document/d/1Unbs2qp_j5kp8FfL_lRH-ld7i5EOQpsq0I4djkOOSL4/) 开发的二进制文件，负责在 Kubernetes 集群中维护 OpenTelemetry Collector 资源池。 桥接组件充当 OpAMP operator 服务器的客户端，报告收集器池的有效配置，并启用远程配置收集器池。 未来，桥接组件将通过增强的状态和改进的运行状况检查报告 Kubernetes 中运行的收集器池的更丰富信息。 您还可以扩展桥接组件以支持 Instrumentation 资源的远程配置。 桥接组件的镜像已经与 OpenTelemetry Operator 一起构建和发布。 此外，我们正在开发方便的[自定义资源定义(CRD)](https://github.com/open-telemetry/opentelemetry-operator/blob/main/apis/v1alpha1/opentelemetrycollector_types.go)，这将使您能够轻松地将桥接组件部署到 Kubernetes 集群中。

## 接下来是什么？

社区已经在 OpAMP 上工作了一年多，用户对它带来的机会感到兴奋。 如果您在 11 月 6 日至 9 日在美国芝加哥参加 [KubeCon NA](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)，请考虑访问我们在 OpenTelemetry 维护者展台，或者参加任何与可观察性相关的活动，例如 [Observability Day](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/observability-day/)。 我们非常渴望从您了解非 OTel 收集器用例和需求。 目前，如果您是供应商并实现 OpAMP 规范，请提供反馈，作为最终用户，您可能希望按照 [OTel 文档中的 OpAMP 条目](https://opentelemetry.io/docs/collector/management/)中的步骤尝试参考实现 Server、Supervisor 和简单 UI，或者深入研究 [Supervisor 代码(用 Go 编写)](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/cmd/opampsupervisor)在 OTel 收集器中。

