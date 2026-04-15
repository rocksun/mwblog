<!--
title: 超越 VPN：Cloudflare Mesh 为 AI 智能体时代构建私有网络
cover: https://cdn.thenewstack.io/media/2026/04/1462502c-evelina-mitev-wpkl7xvf4d0-unsplash-scaled.jpg
summary: Cloudflare 推出 Mesh 服务，将多云环境整合为统一的安全架构。该服务专为 AI 智能体、代码和人类设计，通过身份驱动的私有连接取代传统 VPN，在不暴露公网的情况下实现跨云安全互联。
-->

Cloudflare 推出 Mesh 服务，将多云环境整合为统一的安全架构。该服务专为 AI 智能体、代码和人类设计，通过身份驱动的私有连接取代传统 VPN，在不暴露公网的情况下实现跨云安全互联。

> 译自：[Beyond the VPN: Cloudflare Mesh builds a private network for the age of AI agents](https://thenewstack.io/cloudflare-mesh-agent-networking/)
> 
> 作者：Adrian Bridgwater

长期以来，云连接一直是 DevOps 团队手动操作、碎片化的难题。周二，Cloudflare 推出了 Cloudflare Mesh，旨在弥补这一差距。这是一款私有网络服务，旨在将多云环境统一为一个安全架构，供人类、智能体和代码共同使用。

[Cloudflare 旨在实现这一目标](https://www.cloudflare.com/en-gb/)，希望为人类、智能体和代码之间的云连接提供一个新的融合点。为全球约 20% 的网页提供服务的 Cloudflare 在周二发布了与其同名的 Cloudflare Mesh，这是一种私有网络服务，旨在将[多云基础设施](https://thenewstack.io/reasons-to-opt-for-a-multicloud-strategy/)对齐为统一的安全织网。

## 私有网络：一个定义

要理解 Mesh，首先必须定义 Cloudflare 特定风格的“私有网络”。与传统的私有云不同，这种模式将内部资源（包括服务器、数据库和开发工具环境）连接到更广泛的网络世界，而无需在公司的防火墙上打开端口。

> “随着自主智能体变得越来越普遍，企业必须重新思考访问模式，否则就会面临‘新类别客户端’访问内部资源时使用不安全变通方案的风险。” —— Christian Reilly，Cloudflare。

从本质上讲，Cloudflare Mesh 帮助软件开发人员和运维团队加密每个连接点，而无需将内部基础设施和数据暴露给公共互联网。

该公司表示，生产级智能体的出现是对其技术的核心验证。由于 AI 智能体需要深度访问公司私有数据库、内部 API 和“[预发布环境](https://www.techtarget.com/searchsoftwarequality/definition/staging-environment)”（应用程序、数据集或服务的部署前实例，智能体需要访问这些环境进行安全学习练习），因此它们需要连接通道。

## 危险的隧道，遗留的连接

Cloudflare 欧洲、中东和非洲地区（EMEA）现场首席技术官 [Christian Reilly](https://www.linkedin.com/in/reillychristian/) 告诉 *The New Stack*，通过使用传统的 VPN 或[手动隧道](https://www.twingate.com/blog/glossary/tunnel)来授予智能体访问权限是缓慢且具有内在风险的。

他强调，如今许多团队被迫在两者之间做出选择：要么通过限制访问来束缚他们的智能体，要么为了使其正常工作而可能将私有基础设施暴露在公共互联网中。

“随着自主智能体变得越来越普遍，企业必须重新思考访问模式，否则将面临不安全变通方案的风险，”Reilly 说道，“这意味着组织必须重新思考访问模式。Cloudflare Mesh 通过确保每个智能体都有经过验证的身份，并将所有流量引导通过我们的全球网络来解决这个问题，在不同地区和云之间提供一致的性能，而无需退回到公共互联网。”

由于每个数据包都经过 Cloudflare 的安全栈，Reilly 坚持认为身份和安全性是设计内置的，而不是作为一个单独的层添加的。

## 被以人为中心的网络模型所束缚

Cloudflare 联合创始人兼首席执行官 [Matthew Prince](https://www.linkedin.com/in/mprince/) 进一步强调了 AI 智能体在现代开发工作流中遇到的问题。他表示，它们正受到专为人类设计的“网络模型”的“限制”。面对[复杂且笨拙的 VPN](https://thenewstack.io/2-8-million-reasons-why-you-cant-trust-your-vpn/) 或将私有基础设施暴露于开放网络的危险捷径，Prince 声称 Cloudflare Mesh 消除了这种权衡。

“我们正在为智能体和基础设施之间提供一座安全的桥梁——无论这些智能体是在 Cloudflare 上运行，还是在私有数据中心或其他公有云中运行，”Prince 说道。

## 为每个智能体提供身份

Cloudflare Mesh 运行在连接、安全和身份管理这三个领域之间，被定位为智能体身份的基础。在 Mesh 环境中，每个智能体——就像每个员工一样——都携带一个独特的身份。

这种身份的存在允许安全团队编写粒度策略：例如，允许编码智能体或沙盒读取预发布数据库，同时严格防止其访问包含公司敏感数据、个人身份信息或两者兼有的实时生产财务记录。

通过将 Cloudflare Mesh 与 Cloudflare 开发人员平台（包括该组织的 Workers 产品（一种无服务器边缘计算代码服务）、Workers VPC（用于虚拟私有云）及其智能体 SDK）相结合，Cloudflare 表示它为 AI 智能体提供了端到端的生命周期支持。

## 工作的围墙花园

Cloudflare Mesh 承诺消除跨云网络的复杂性，允许开发人员将笔记本电脑、办公硬件和多云环境（AWS、GCP）桥接成一个统一的私有架构。

该公司表示，其技术使团队能够创建一个与公共互联网完全隔绝的内聚网络。通过 Cloudflare 的全球网络路由私有 IP，敏感数据（从云基础设施到分布式设备和 AI 工具）保持加密状态，且对外部威胁不可见。

这项新服务允许在 Cloudflare Workers 上运行的 AI 智能体通过 Workers VPC 绑定访问整个私有网络。开发人员现在可以通过该公司定义的简单代码命令，授予智能体对私有 API 和数据库的范围限制访问权限。

随着全球范围内对代理型 AI 创建和控制权的争夺战仍在继续，现在似乎出现了相应水平的平台和工具开发，旨在锁定（或至少在更细粒度的水平上控制和管理）整个现代栈中的智能体行为。