
<!--
title: 新工具终结K8s中Java配置噩梦
cover: https://cdn.thenewstack.io/media/2025/08/16087190-sumaid-pal-singh-bakshi-cbrjixbfiga-unsplash-1.jpg
summary: Perforce 发布 JRebel Enterprise，旨在消除 Java 云开发中耗时的重新部署过程。它通过自动环境发现和连接，简化了配置，提高了开发效率。企业版支持多种 IDE 和云平台，适用于大型 Java 开发团队。
-->

Perforce 发布 JRebel Enterprise，旨在消除 Java 云开发中耗时的重新部署过程。它通过自动环境发现和连接，简化了配置，提高了开发效率。企业版支持多种 IDE 和云平台，适用于大型 Java 开发团队。

> 译自：[New Tool Ends Java Configuration Nightmare in K8s](https://thenewstack.io/new-tool-ends-java-configuration-nightmare-in-k8s/)
> 
> 作者：Darryl K. Taft

[Perforce](https://www.perforce.com/) 本周发布了 [JRebel Enterprise](https://www.jrebel.com/products/jrebel-enterprise)，这是一款旨在消除 [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 开发中最持久的痛点之一的新解决方案：耗时的重新部署过程，该过程可能会使现代云环境中的生产力停滞不前。

根据 [Perforce 的 2025 年 Java 开发者生产力报告](https://www.jrebel.com/blog/developer-report-highlights)，73% 的企业受访者现在使用基于云或远程的开发环境，这给传统工具难以处理的问题带来了新的摩擦点，Perforce 产品管理高级总监 [Jeff Michael](https://www.linkedin.com/in/jnmichael/) 告诉 The New Stack。

## 超越传统的热交换

[JRebel](https://www.jrebel.com/products/jrebel) 长期以来以其能够将类级别的更改推送到正在运行的 Java 应用程序而无需完全重建而闻名。但是 JRebel Enterprise 解决了一个更复杂的问题：在 [容器化](https://thenewstack.io/introduction-to-containers/)、[Kubernetes](https://thenewstack.io/kubernetes/)-驱动的环境中出现的配置难题，在这种环境中，开发容器会动态地启动和关闭，Michael 说道。

他说：“由于快速发展的业务需求，[DevOps](https://thenewstack.io/introduction-to-devops/) 环境正在快速成熟，这给开发和测试环境增加了显著的复杂性。” “JRebel Enterprise 为你的开发者管理这些复杂性，允许他们无缝地将代码更改推送到远程环境，而无需冗长的重建和重新部署。”

传统的 JRebel 方法要求开发人员在静态部署服务器上手动配置代理。Michael 说，在当今的动态环境中，当容器根据工作负载需求出现和消失，或者当开发人员需要启动环境来修复特定错误时，该模型就会崩溃。

## 自动环境发现

JRebel Enterprise 引入了该公司所谓的“主动连接”机制。当新的容器化环境启动时，它们会自动向中央 JRebel 代理注册。然后，该代理通过一个简单的下拉菜单直接在开发者的 IDE 中公开可用的环境，Michael 说。

其结果是大大减少了配置开销——从每个开发者每台服务器 3-5 分钟减少到整个 Java 开发团队一次性的 1-2 分钟设置。此外，开发人员不再需要跟踪哪些环境可用，也不需要在部署目标更改时手动重新配置其工具。

“作为一名开发人员，我不再需要知道我应该指向哪个环境。它会显示在我的 IDE 中。我可以在下拉列表中选择它，现在开发人员可以无缝地与所有动态环境进行交互，因为它们会启动和关闭，”Michael 解释道。

## 企业级采用

他说，JRebel 的吸引力范围从每年支付 595 美元的个人开发者到拥有 1,000 多名 Java 工程师的大型企业。

企业版目前支持 [IntelliJ IDEA](https://www.jetbrains.com/idea/)，并计划集成 [Eclipse](https://thenewstack.io/eclipse-theia-the-deepseek-of-ai-tooling/) IDE 和 [VS Code](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/)。它适用于所有主要的云提供商，包括 [AWS](https://aws.amazon.com/?utm_content=inline+mention)、Microsoft Azure 和 [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Platform，并支持 [Java 21](https://thenewstack.io/microsoft-releases-its-own-distro-of-java-21/) 及更高版本。

## 市场定位

虽然 JRebel 面临着来自热交换工具和其他开发效率解决方案的竞争，但 Perforce 认为其类级别更改检测和企业级动态环境管理使其脱颖而出，Michael 说。他指出，该公司自动处理复杂的 DevOps 管道而无需开发人员配置的能力代表了传统方法的演变。

对于在动态云环境中管理数百或数千名 Java 开发人员的 Java 商店来说，消除重新部署延迟和配置开销的承诺可以带来可观的生产力提升。

JRebel Enterprise 现已上市，有关详细信息和演示可通过 Perforce 的网站访问。