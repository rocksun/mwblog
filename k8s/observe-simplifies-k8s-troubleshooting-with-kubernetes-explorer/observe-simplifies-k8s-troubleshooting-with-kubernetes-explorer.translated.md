# Observe 简化 Kubernetes 排错：Kubernetes Explorer

![Featued image for: Observe Simplifies K8s Troubleshooting With Kubernetes Explorer](https://cdn.thenewstack.io/media/2024/11/dd5153c8-k8s_explorer-1-1024x589.webp)

在上周的[KubeCon + CloudNativeCon 北美 2024](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/?utm_source=google&utm_medium=paid-search&utm_campaign=kubecon-na-2024&utm_term=events-kubecon-na-2024-cncf&utm_content=kubecon-na_rsa&campaignid=21541954784&adgroupid=166431838780&creative=708046449585&matchtype=e&network=g&device=c&keyword=kubecon%20cloudnativecon%20north%20america%202024&utm_term=kubecon%20cloudnativecon%20north%20america%202024&utm_campaign=Events+-+KubeCon+NA+2024+-+CNCF&utm_source=google&utm_medium=ppc&hsa_acc=8666746580&hsa_cam=21541954784&hsa_grp=166431838780&hsa_ad=708046449585&hsa_src=g&hsa_tgt=kwd-2561250744672&hsa_kw=kubecon%20cloudnativecon%20north%20america%202024&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwmt24BhDPARIsAJFYKk0G62Qijiv1aoyNQIChsEyNhUj7RwDyhsafk9KdMQeRfE0F6z8rYhEaAh5aEALw_wcB) 大会上，[Observe, Inc.](https://www.observeinc.com/) 推出了 Kubernetes Explorer，这是该公司可观测性平台的一个新增功能，旨在简化云原生环境的可视化和故障排除。

借助这种全新、专为可观测性设计的体验，[DevOps 团队](https://thenewstack.io/kubernetes-job-market-platform-engineers-earn-20-more-than-devops-engineers/)、[SRE](https://thenewstack.io/what-platform-engineering-meant-for-adidass-sres/) 和工程师可以获得复合[Kubernetes (K8s) 环境](https://thenewstack.io/kubernetes/) 的全局视图，从而更快、更轻松地识别和解决健康和性能异常。

## K8s 热潮中的一个受欢迎的补充

近年来，K8s 的采用率快速增长，这主要得益于[边缘计算的新趋势](https://lfedge.org/kubernetes-is-paving-the-path-for-edge-computing-adoption/) 和[爆炸式增长的 AI/ML 工作负载](https://analyticsindiamag.com/ai-origins-evolution/how-generative-ai-is-fueling-demand-for-kubernetes/)。展望未来，专家预计这种快速增长将持续下去；事实上，[Gartner 的一份最新报告](https://globalitresearch.com/wp-content/uploads/2024/10/69157-Google%20-%20Q4%202024%20-%20GCP%20-%20Startup%20Greenfield%20-%20Lead%20Gen%20-%20ABM%20Enterprise%20%28MFG%29%20PSA/Gartner%20Reprint%20Container.pdf) 预测，到 2027 年，超过 75% 的所有 AI 部署将“使用容器技术作为底层计算环境”。这比今天的水平增加了 25% 以上。

随着 K8s 采用的持续增长，管理 K8s 环境的复杂性也在增加。这给 DevOps 团队、SRE 和工程师带来了更大的挑战，因为他们试图在 K8s 平台和云原生基础设施中保持可见性，观察分布式应用程序，并获得对 K8s 部署的工作负载的健康状况和性能的可行见解。更大的问题是，K8s 部署的分布式应用程序日益增长的复杂性已成为一个顽固的障碍，威胁到进一步的容器采用。

但 Observe 承诺改变现状。借助 Kubernetes Explorer，这家 SaaS 可观测性公司提供了与传统监控工具不同的东西，首次为工程师提供了 K8s 的可视化统一界面。

## 终于，一款展现全局视图的监控工具

Kubernetes Explorer 统一了指标、跟踪和日志中的碎片化数据，以提供跨应用程序、K8s 平台和云原生基础设施的上下文洞察。Observe 表示，反过来，这种增强的可见性将使 DevOps 团队、SRE 和工程师能够更好地理解不同的 K8s 组件，以便他们能够比以往更快、更轻松地识别、诊断和纠正问题。

值得注意的是，Kubernetes Explorer 集成了 Observe 的[AI](https://www.observeinc.com/blog/observe-inc-introduces-ai-powered-observability-closes-series-b-funding-of-145m/)[调查员](https://www.observeinc.com/blog/observe-inc-introduces-ai-powered-observability-closes-series-b-funding-of-145m/)，这是其“Project Voyager”[2024 年 9 月宣布的产品更新](https://www.prnewswire.com/news-releases/observe-inc-introduces-ai-powered-observability-closes-series-b-funding-of-145m-302259523.html) 的一部分，以及该公司 1.45 亿美元 B 轮融资。Kubernetes Explorer 与这种智能 AI 方法相结合，可以创建自定义的、特定于事件的可视化效果，充当事实上的 K8s 助手，以支持值班工程师的故障排除工作。其他功能包括 Kubernetes Hindsight（提供历史可见性）、资源描述符（提供对 K8s 资源完整 YAML 配置的可见性）和集群优化（提供跨 K8s 集群的工作负载分布的可视化地图）。
总而言之，这对于传统监控工具无法全面了解应用程序性能的工程和DevOps团队来说，可能是一个巨大的胜利。

据Observe首席执行官Jeremy Burton所说，大多数其他监控K8s部署的应用程序和基础设施的工具只提供有限的历史上下文；换句话说，虽然它们可以为团队提供对K8s部署当前状态的洞察，但它们缺乏更深入的历史可见性。“这使得团队难以有效地诊断和解决问题，”他解释道。此外，典型的监控工具通常难以集成碎片化的数据类型（例如，指标、跟踪和日志），进一步抑制了团队充分监控应用程序和排查健康和性能问题的能力。

相比之下，Kubernetes Explorer有效地将指标、跟踪和日志中的孤立数据整合在一起，提供对所有K8s组件（当前运行的和以前终止的）的全面可见性，使团队更容易理解组件之间的相互依赖关系，以便他们能够更快地检测、诊断和解决问题——即使是追溯性地。然后，AI Investigator可以介入并提供故障排除建议。通过Kubernetes Explorer为Kubernetes AI代理提供工件（如自定义可视化、OPAL和遥测数据），使代理能够推理、确定根本原因并提供解决方案建议。

## 可见性的一步，行业的一大飞跃

凭借AI功能和自动化可视化，Kubernetes Explorer承诺为混乱的K8s环境带来一些急需的简便性——或者用Burton的话说，它将“消除Kubernetes的复杂性”。

鉴于K8s的快速增长和K8s以及云原生环境日益增长的复杂性，Burton将Observe的新增功能称为“云原生环境可观察性的一大进步”是有道理的。他还将Observe的代理AI方法应用于K8s故障排除称为行业中的“独特”方法，并肯定它是唯一能够解决DevOps团队、SRE和长期以来难以有效监控K8s部署应用程序的工程师的难题的工具：“工程师需要当前的可观察性产品无法提供的可操作的见解。”

为了提供这些见解，Observe表示他们正在简化这一过程。作为公司提供全面可观察性解决方案且无隐藏费用的使命的一部分，Kubernetes Explorer现在可供所有Observe客户免费使用。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。