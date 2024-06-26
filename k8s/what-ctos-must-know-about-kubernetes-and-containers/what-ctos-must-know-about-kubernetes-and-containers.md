# 分析报告：CTO 必须了解的 Kubernetes 和容器知识

翻译自 [Analyst Report: What CTOs Must Know about Kubernetes and Containers](https://thenewstack.io/analyst-report-what-ctos-must-know-about-kubernetes-and-containers/) 。查看原文可以看到更多的链接。

![](https://cdn.thenewstack.io/media/2023/02/43de1e90-art-2-1024x682.jpg)

为了成功部署和健康的投资回报，组织应该确保正确的应用程序和人员到位。

云原生应用程序和微服务对于任何现代企业的有效运行都是必不可少的。但技术主管不能在没有计划的情况下购买现成的解决方案或将遗留基础设施提升并转移到云原生架构中。

工程师需要合适的工具、团队和技能，但很难知道要购买、实施哪些工具以及如何计算投资回报 (ROI)。

Gartner 报告“CTO 的容器和 Kubernetes 指南——回答十大常见问题解答”指出，容器和 Kubernetes 已成为构建云原生应用程序和实现遗留工作负载现代化的重要平台技术。到 2027 年，超过 90% 的全球组织将在生产中运行容器化应用程序，与 2021 年的不到 40% 相比有了显着增长。

作者还写道，“企业在准确衡量其云原生投资的投资回报率以及创建合适的组织结构以使其蓬勃发展方面面临挑战。”

以下是企业应了解的有关容器和 Kubernetes 的知识、它们的主要用例以及它们如何帮助运行云原生架构。

## 什么是容器、Kubernetes 及其用例？

容器是捆绑在一起的应用程序代码包。 Kubernetes 是一个帮助管理容器的平台。

这些技术通常用于微服务、应用程序可移植性和降低锁定风险。它们还支持 DevOps 工作流和遗留应用程序现代化。任何决定采用云原生或升级其基础架构的公司都必须同时使用容器和 Kubernetes。

根据 Gartner 的说法，容器和 Kubernetes 的理想应用程序具有：

* 对外部应用程序的依赖程度低。
* 支持应用程序基础设施和平台技术的容器镜像。
* 快速的弹性需求和频繁的代码更改。
* 适用于任何商业现成 (COTS) 应用程序部署的供应商支持的镜像。

## 行业对这些选项的支持程度如何？

大多数容器镜像都基于开源软件。容器镜像是静态文件，其中包含用于在计算系统中创建容器的所有可执行代码。

Gartner 报告指出，与容器支持已经司空见惯的开源软件相比，COTS 应用程序容器支持的增长速度要慢得多，并且因供应商而异。

“虽然一些 COTS ISV [独立软件供应商] 在战略上为 Kubernetes 提供强大支持，例如 IBM，但许多 COTS ISV 尚未提供支持——尤其是在基于 Windows 或企业业务应用程序中。你应该审查容器支持策略和他们的战略 COTS ISV 的路线图，”作者写道。

尽管如此，Gartner 指出，越来越多的供应商正在开发容器支持，而且“越来越多的 ISV 正在实现与容器/Kubernetes 的更深入集成，而不仅仅是提供容器镜像。”

该报告强调，截至 2022 年 2 月，AWS Marketplace for Containers 有 524 个与容器相关的条目，比 2020 年 2 月的 320 个条目增长了 64%。

围绕 Kubernetes 和容器出现的行业趋势包括 VM 融合、有状态应用程序支持、边缘计算、无服务器融合和应用程序工作流自动化。

Kubernetes 和容器的开源和 COTS 应用程序的组合为组织提供了多种部署选项：

![](https://cdn.thenewstack.io/media/2023/02/878fb91e-image1.png)

## 容器和 Kubernetes 有好处吗？

容器为专门运行云原生架构的组织提供了多种好处。它们提供敏捷的应用程序开发和部署、环境一致性和不变性。

由于 Kubernetes 在容器软件之上运行，因此它提供了灵活性和选择。

“Kubernetes 得到了由云提供商、ISV 和 IHV [独立硬件供应商] 组成的庞大生态系统的支持。这种 API 和跨平台一致性、开源创新和行业支持为 CTO 提供了很大程度的灵活性，”Gartner 作者表示。

### Kubernetes 的技术局限是什么？

平台复杂性绝对是 CTO 和 IT 经理必须承认的事情，尤其是容器和 Kubernetes 并非对所有可能的用例都是最佳选择。这些技术最适用于动态、可扩展的环境，如果工程师试图使用它们来管理静态的 COTS 应用程序，则会增加复杂性。

### 成功部署 Kubernetes 需要哪些技能？

成功实施容器和 Kubernetes 的很​​大一部分是确保拥有适当的团队和技能组合来管理和运行该技术。组织应投资于各种核心和次要角色，包括安全、平台运营、可靠性工程以及构建和发布工程。这些指定有助于确保 Kubernetes 部署是安全、可靠的，并且是为组织大规模开发的。

### Gartner 概述了运行 Kubernetes 环境的团队的角色和职责

开发团队应承担编码、应用程序设计、实施和测试以及源代码管理的任务。

平台工程团队负责监督平台选择、安装、配置和管理。成员还应该能够维护基础镜像、集成 DevOps 管道、为开发人员启用自助服务功能、自动化容器配置以及提供容量规划和工作负载隔离。

可靠性工程师负责安全、监控和性能方面的工作。他们应该关注应用程序的弹性；能够调试和记录生产问题；并负责事件管理和响应。

最后，构建和发布工程团队选择 CI/CD 部署管道，为新服务开发模板，培训开发团队，并创建仪表板来衡量效率和生产力。

### 组织如何衡量容器的投资回报率？

“通过构建全面的业务案例来确保投资回报率对于验证您是否纯粹因为容器和 Kubernetes 是一项闪亮的新技术而进行投资非常重要。组织需要对产生的成本和潜在收益采取现实的看法，”报告作者写道。

组织可以衡量的容器的好处包括开发人员的生产力、敏捷的 CI/CD 环境、基础设施效率的提高和运营开销的减少。

可能削减收益的潜在成本是容器即服务/平台即服务 (CaaS/PaaS) 许可费；用于安全、自动化和监控工具的附加软件许可证；基础设施投资成本；雇用新员工来进行此类部署；和专业的实施服务，让一切都在线并顺利运行。

### Gartner 向技术领导者推荐了哪些步骤？

Gartner 作者建议技术领导者：

* 在致力于和扩展 Kubernetes 平台环境之前，确保存在强大的业务案例、确定合适的用例并建立 DevOps 文化。
* 创建一个平台团队来管理平台选择，推动 DevOps 功能的标准化和自动化，并与开发人员协作以培育云原生架构。
* 为集成不同技术组件的生产部署选择打包软件发行版或云托管服务，简化该堆栈的生命周期管理并提供多云管理，而不是采用 DIY 方法。
* 准确衡量和传达收益，包括软件速度、发布成功和运营效率提升等技术指标，以及收入增长和客户满意度等业务指标。

容器和 Kubernetes 为想要运行云原生架构并将遗留应用程序带入 21 世纪的组织和 IT 领导者提供了清晰的技术基础。为了成功部署和健康的投资回报率，组织应该确保正确的应用程序和人员到位。

[下载完整报告](https://go.chronosphere.io/gartner-cto-guide.html)，了解容器和 Kubernetes 如何对云原生应用至关重要。