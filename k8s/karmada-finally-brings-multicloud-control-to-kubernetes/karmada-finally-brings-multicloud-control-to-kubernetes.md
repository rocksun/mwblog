<!--
title:Karmada实现Kubernetes跨多云管控
cover: https://cdn.thenewstack.io/media/2023/12/c1ae8f68-karmada-1024x683.png
-->

鉴于KubeFed进展缓慢，一批主要来自亚洲的企业自主开发了开源多云集群管理系统Karmada，如今已经得到CNCF基金会的正式认可。

> 译自 [Karmada Finally Brings Multicloud Control to Kubernetes](https://thenewstack.io/karmada-finally-brings-multicloud-control-to-kubernetes/)，作者 Joab Jackson 是The New Stack的高级编辑，负责报道云原生计算和系统操作。他已经报道IT基础设施和开发25年，包括在IDG和Government Computer News的任期。在此之前，他是...... 

拥有来自60多个组织的500多名贡献者，[Karmada](https://karmada.io/)项目显示出人们对于使Kubernetes成为云提供商的事实标准化分布式工作负载编排器的浓厚兴趣。

本周，[云原生计算基金会](https://cncf.io/？utm_content=inline-mention)(CNCF)的[技术监督委员会](https://www.cncf.io/people/technical-oversight-committee/)(TOC)投票决定接受Karmada作为CNCF孵化项目。

Karmada通过一套Kubernetes原生API和高级调度功能，为在不同云提供商之间运行Kubernetes集群提供了一种方法。它不需要对应用程序本身进行任何更改。

Karmada的想法是让用户更容易地在不同的[云提供商](https://thenewstack.io/how-to-evaluate-kubernetes-cloud-providers/)之间切换工作负载。目前，主要的云提供商都有[稍微不同的方法](https://thenewstack.io/survey-shows-companies-moving-away-from-diy-kubernetes/)来提供[Kubernetes即服务](https://thenewstack.io/why-kubernetes-has-emerged-as-the-os-of-the-cloud/)。它将为身份验证、配置交付和服务管理提供单一访问点，同时减少[来自云供应商的潜在锁定](https://thenewstack.io/is-radius-just-another-microsoft-attempt-at-lock-in/)。

## KubeFed 的问题

[Nikhita Raghunath](https://www.linkedin.com/in/nikinath/？originalSubdomain=in)作为Karmada进入孵化阶段的TOC发起人在声明中表示：“Karmada在调度和编排多云和多集群Kubernetes环境的几个领域中填补了空白，这可以为分布式组织提供更好的性能和更低的成本。”

最初，多集群工作负载管理是[Kubernetes联邦](https://thenewstack.io/configuring-kubernetes-cluster-federation-to-create-a-global-deployment/)(KubeFed)项目的任务，尽管Karmada的许多参与者正在寻找更多功能，比如资源调度、故障迁移、自动扩缩容、服务发现、数据自动化和多平台集群生命周期管理。

此外，[KubeFed](https://thenewstack.io/living-with-kubernetes-multicluster-management/)没有提供Kubernetes原生API，这使得跨云迁移集群变得困难。

“所以我们决定开发Karmada来满足我们的需求，”[华为云](https://www.huaweicloud.com/)的Kevin Wang和[工商银行](https://www.icbc.com.cn/en/column/1438058319784067131.html)的Yifan Shen在一篇[介绍Karmada的博文中写道](https://karmada.io/blog/2022/03/22/multi-cluster-management-with-an-ocean-of-nodes)。

## Karmada的背后是谁？

Karmada于2021年启动，并在当年被接受为CNCF沙箱项目，它是一个由一些亚洲公司联合发起的项目，包括[中国一汽](http://www.faw.com/)、华为云、工商银行、[浦发银行](https://eng.spdb.com.cn/)、[VIPKid.com](https://www.vipkid.com/en-us/)翻译服务和[小红书](https://www.xiaohongshu.com/)媒体服务。

该项目目前在生产环境中拥有23家[公开采用](https://karmada.io/adopters/)Karmada的用户，包括Daocloud、携程集团、Vivo等。

携程使用Karmada构建了一个混合多云的控制平面，这使旅游公司即使在异构环境下也能降低架构迁移的成本。根据携程容器和混合云团队总监Honghui Yue的说法，故障隔离架构和多集群HorizontalPodAutoscaler也是该公司的卖点。

该[代码库](https://github.com/karmada-io/karmada/releases.)在GitHub上收到过3,500多次拉取请求，并在该服务上获得了3，600个星标。

## 什么是Karmada？

“Karmada源自社区和华为云在多云管理领域的深度积累，为企业提供从单集群到分布式云架构的平滑演进解决方案，”华为云CTO [Bruno Zhang](https://www.linkedin.com/in/bruno-zhang-16207678/?originalSubdomain=cn)在声明中解释道。

在架构上，Karmada由一组通过karmada-apiserver暴露和扩展的兼容Kubernetes的API运行。

一个独立的调度器(karmada-scheduler)根据故障域、集群资源、Kubernetes版本和集群中启用的插件来调度工作负载。它可以支持多维、多权重和多集群调度策略。

自定义控制器进程由karmada-controller-manager管理。每个集群都获取一个代理(karmada-agent)来从控制平面同步配置。

![](https://lh7-us.googleusercontent.com/S5s_8Cs3q4yo_AfR_hegDCh46nf00NIskixkqZECrp_sXm8G2RukZnRMhxW8zwVGvyuL4OcaZL1URK8WStrDECzOEbrJVACwuOZom-qoXTdgtZFLRnY5V-LC_HGxCVEs-bqJJc0sy9JwXly6idTtMZQ)

随着项目进入孵化状态，开发团队计划添加更多功能，并正在积极[添加新功能](https://github.com/karmada-io/karmada/blob/master/ROADMAP.md)，包括更细粒度的多集群安全性、用于降低延迟和提高稳定性的可扩展性功能、更好的可观测性和与其他云原生应用的更深入集成。
