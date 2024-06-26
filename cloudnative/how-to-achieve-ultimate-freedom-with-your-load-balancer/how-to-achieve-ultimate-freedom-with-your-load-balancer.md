
<!--
title: 如何利用负载均衡器实现终极自由
cover: https://cdn.thenewstack.io/media/2024/06/5d015746-image1.png
-->

开源贡献、客户信任、行业认可和环境无关性是实现基础设施自由的关键要素。

> 译自 [How to Achieve Ultimate Freedom with Your Load Balancer](https://thenewstack.io/how-to-achieve-ultimate-freedom-with-your-load-balancer/)，作者 Tyler Charboneau; Floyd Smith。

开源软件的流行程度与云计算的使用增长同步飙升，包括多云和混合云基础设施。Pluralsight 的 2023 年云状况报告显示，[65% 的组织](https://learn.pluralsight.com/resource/offers/2023/state-of-cloud?utm_source=google&utm_medium=paid-search&utm_campaign=upskilling-and-reskilling&utm_term=b2b-na-dynamic&gad_source=1&gclid=CjwKCAjw48-vBhBbEiwAzqrZVA71VlE7k_ihXrG1CGgEha9viKRoB3xxKaKkHainxuj7DsVN0dQERBoCk00QAvD_BwE) 积极使用多云环境。

开源软件之所以受到青睐，部分原因在于它能够在组织的技术栈中实现自由选择，尤其是在复杂的部署环境中。这种选择的需求也延伸到负载均衡器，负载均衡器是不可或缺的基础设施组件，能够实现快速、可靠和安全的应用程序交付。

负载均衡软件处理各种功能，并与许多其他组件交互。负载均衡级别的灵活性有助于最大限度地提高整个应用程序基础设施中的选择自由度。

负载均衡器对于应用程序交付至关重要，而应用程序交付则由可扩展的分布式系统支持。当客户端请求到达时（例如，向用户显示产品页面），负载均衡器会根据指定的负载均衡算法将请求分配到后端服务器。这可以防止服务器过载，从而提高整体容量，并帮助应用程序以经济高效的方式扩展。

这只是传统负载均衡器所做的一切，但[现代负载均衡器已发展成为强大的应用程序交付解决方案](https://thenewstack.io/application-delivery-controllers-a-key-to-app-modernization/)，并具有以下附加功能：

- 高级请求路由
- 故障转移保护和运行状况检查，有助于确保高可用性
- 安全功能，包括下一代 Web 应用程序防火墙 (WAF) 功能和机器人管理
- 集中管理、监控和自动化，从而提高运营效率

组织需要一个功能丰富的负载均衡器，该负载均衡器能够无缝地集成到任何地方，将负载均衡器从简单的工具提升为现代应用程序环境中灵活的全能工作马。

![](https://cdn.thenewstack.io/media/2024/06/b293f2a2-image2-1024x512.png)

以下是一些关键特征，可以区分能够最大限度地提高技术栈自由度的现代负载均衡器：

## 开源基础

植根于社区参与和[开源贡献](https://thenewstack.io/open-source-contributions-on-the-rise-in-fintech-healthcare-and-government/) 的产品开发非常强大。虽然许多解决方案都是黑盒子，很少提供有关它们如何构建或运行的提示，但基于反馈构建的透明且可定制的解决方案将最适合用户。这种方法对用户需求更具响应性，并得到同行评审的支持。寻找具有社区代码贡献历史记录的健康且强大的开源项目。

## 随着时间的推移而广受欢迎

广泛的流行表明供应商长期以来一直支持客户需求，这使客户能够从信任的角度构建和创新。我们看到这种情况以两种方式发生。

首先，一个广泛使用且持久存在的项目会快速且持续地成熟和改进，因为它已经接触到大量挑战和不断变化的技术。

其次，流行的产品通常会拥有一个庞大而活跃的社区，可以帮助回答问题，提供关于利基实现的指南，并构建与其他工具和平台的集成。

## 广泛的技术支持

为了最大限度地提高自由度，负载均衡平台必须具有最大的灵活性。这包括在 OSI（开放系统互连）堆栈的第 4 层支持 TCP（传输控制协议）和 UDP（用户数据报协议），以及在第 7 层支持 HTTP。一些负载均衡器[在这方面表现出色](https://www.haproxy.com/blog/haproxy-protocol-support)，而另一些则停滞不前。

广泛的技术支持还解锁了趋势和新兴领域（例如 DevOps、MLOps、AIOPs 和[Kubernetes](https://www.haproxy.com/blog/haproxy-fusion-new-external-load-balancing-multi-cluster-routing-features)（仅举几例））中的众多用例可能性。

## 对环境和部署模型的全面支持

与基础设施无关的负载均衡器可以减轻决策压力，同时提供灵活性和一致性。例如，您需要能够跨[AWS](https://aws.amazon.com/?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention) Cloud、[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure 等运行工作负载。
一个功能强大的[负载均衡平台还必须提供对私有云、混合云、本地环境和边缘的特定支持](https://thenewstack.io/how-the-right-load-balancer-supports-a-video-saas-providers-ambitious-plans-for-kubernetes/)。灵活的部署选项——包括虚拟机、容器甚至设备——是关键。

您需要一个不会将您锁定在特定环境中的负载均衡器。您需要支持任何云提供商、VM 或容器，或本地部署，而不会造成技术妥协。这将使您的技术堆栈未来可期，从而实现更无缝的现代化，而不会造成不必要的摩擦或费用。

## 成本优化

成本是创新过程中最难克服的障碍，因为绝大多数组织都面临着预算限制。提供流行且广泛使用的开源途径的负载均衡供应商提供了一种解决方案。具有价格透明度、简单成本结构和直接销售实践的强大企业选项完善了这一画面。开源产品和付费产品及其用户社区之间的互动可以使每个人受益。

每美元的整体性能也是关键。高性能负载均衡器优化了后端服务器上的资源使用，并且运行给定工作负载所需的硬件更少，从而帮助您有效地扩展并降低总拥有成本。

## 实现终极自由

为了在 Web 应用程序和 API 传递中实现自由，您应该寻求创建、组装、许可（通过开源）和/或购买满足我们在此概述的要求的负载均衡平台。开源贡献、客户信任、行业认可和环境无关性是实现基础设施自由的关键要素。在 HAProxy，这些对我们来说一直非常重要。

如果您想了解更多信息，[请联系我们的团队](https://www.haproxy.com/contact-us) 开始对话。
