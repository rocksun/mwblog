
<!--
title: Kubernetes上数据管理 (DoK)的四种解决方案
cover: https://cdn.thenewstack.io/media/2024/09/17276eb6-managing-data-on-kubernetes.jpg
-->

大约 97% 的组织在 Kubernetes 上运行数据密集型工作负载，但许多组织仍在努力解决持续存在的复杂性。

> 译自 [Managing Data on Kubernetes (DoK): 4 Solutions](https://thenewstack.io/managing-data-on-kubernetes-dok-solving-the-underlying-challenges/)，作者 Rajiv Thakkar。


在当今快速发展的数字环境中，保持领先需要敏捷性、灵活性和可扩展性。这正是 [在 Kubernetes 上管理数据 (data on Kubernetes,DoK)](https://community.cncf.io/data-on-kubernetes/) 成为企业游戏规则改变者的原因。随着行业继续 [拥抱 Kubernetes](https://roadmap.sh/kubernetes/)，利用 DoK 对于跟上现代需求至关重要。

最近由 Pure Storage 的 Portworx 委托进行的研究，总结在 [2024 年 Kubernetes 专家声音报告](https://portworx.com/resources/voice-of-kubernetes-expert-report/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand) 中，强调了 DoK 的变革性影响。该报告调查了来自大型组织的 500 多位 Kubernetes 专家，重点介绍了塑造企业 [数据管理](https://thenewstack.io/storage/) 未来的一些关键趋势和挑战。

## 在 Kubernetes 上管理数据的关键优势

在 Kubernetes 上管理数据 (DoK) 指的是现代企业中专门在 [Kubernetes](https://thenewstack.io/kubernetes/) 中运行有状态工作负载的趋势，这些企业工作负载被定义为以数据为中心、数据密集型或对组织业务至关重要的工作负载。由于这些关键工作负载在过去几十年中一直在虚拟机中运行，因此 DoK 的采用代表了 Kubernetes 在过去五年左右时间里快速获得的成熟度。

DoK 的优势显而易见：它提供了无与伦比的灵活性和可扩展性，以及成本效益。根据该报告，65% 的组织将更快的部署速度视为在 Kubernetes 上运行数据服务或工作负载的主要优势。

随着企业越来越多地 [采用云原生环境](https://thenewstack.io/enterprises-to-double-cloud-native-use-by-2029/)，它们通常从无状态工作负载开始，然后逐步发展到更复杂的有状态应用程序。这种演变——从最初的小项目到关键应用程序——反映了 Kubernetes 作为企业战略基石的作用日益重要。

![](https://cdn.thenewstack.io/media/2024/09/221b085d-dok-advantages_1-1024x394.png)

## 当前 DoK 趋势、工作负载类型和挑战

该报告显示，97% 的组织现在在 Kubernetes 上运行数据密集型工作负载。其中，72% 利用 Kubernetes 进行数据库管理，67% 用于分析，54% 用于 AI/ML 工作负载。这种广泛的采用标志着向云原生解决方案转变，以用于关键操作。

![](https://cdn.thenewstack.io/media/2024/09/5fbf6abe-dok-workload-types_2-1024x369.png)

然而，随着 Kubernetes 的不断成熟，与之相关的挑战也随之增加。高可用性和灾难恢复是 52% 的组织最关心的问题，而 46% 的组织则在高性能存储方面遇到了困难。此外，71% 的受访者表示需要一个 [集中式平台](https://thenewstack.io/execs-invest-in-platform-engineering-heres-why/) 来简化操作并有效地解决这些挑战。

![](https://cdn.thenewstack.io/media/2024/09/4fc191f7-dok-capabilities-needed_3-1024x412.png)

## 前进的道路

为了充分利用 DoK 的优势并减轻其复杂性，企业必须采用全面的容器数据管理平台。关键要求包括：

1. **高性能持久存储**：对于支持具有苛刻性能需求的现代应用程序至关重要。
2. **自动化存储流程**：通过自动化简化操作，并为开发人员提供自助服务体验。
3. **企业级业务连续性**：实施强大的数据保护和灾难恢复策略，以保护关键应用程序。
4. **统一数据平台**：一个集中式解决方案，简化跨混合云和多云环境的管理，并与现代数据库无缝集成。

企业需要考虑的问题不是是否在 Kubernetes 上运行数据，而是如何有效地解决相关挑战。通过投资正确的技术和策略，企业可以释放 DoK 的全部潜力，确保其基础设施能够随着未来需求的增长而扩展。

访问我们的网站或参加 Portworx [动手实验室](https://portworx.com/webinar/portworx-101-hands-on-labs-sep/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand)（面向平台工程师和 DevOps 从业人员），详细了解 Pure Storage 的 Portworx 如何帮助加速您的 Kubernetes 数据策略。

[立即下载一份《Kubernetes 专家声音报告》](https://portworx.com/resources/voice-of-kubernetes-expert-report/?utm_source=newstack&utm_medium=web&utm_campaign=px-brand) 了解有关该报告调查结果的更多信息！
