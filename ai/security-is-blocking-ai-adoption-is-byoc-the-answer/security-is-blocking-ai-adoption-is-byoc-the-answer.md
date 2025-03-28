
<!--
title: 安全问题阻碍AI普及：自带云(BYOC)是解决方案吗？
cover: https://cdn.thenewstack.io/media/2025/02/defe521b-cloud.jpg
-->

自带云架构如何帮助监管行业部署 AI 解决方案，同时保持安全和合规标准。

> 译自 [Security Is Blocking AI Adoption: Is BYOC the Answer?](https://thenewstack.io/security-is-blocking-ai-adoption-is-byoc-the-answer/)，作者 Jiang Chen。

自从 ChatGPT 首次亮相以来的 18 个月里，[人工智能采用](https://thenewstack.io/ai/)的格局发生了巨大的变化。根据 [麦肯锡 2024 年人工智能全球调查](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai?t)，组织对人工智能的采用率从 50% 飙升至 72%，其中一半的受访组织在多个业务职能部门实施人工智能，高于 2023 年的不到三分之一。

然而，这股人工智能采用浪潮给金融和医疗保健等受监管行业带来了独特的挑战。虽然这些行业认识到人工智能在提高生产力和保持竞争优势方面的变革潜力，但在大规模实施人工智能解决方案方面面临着重大障碍。

挑战不仅仅在于采用技术，而在于在保持严格的安全和[合规标准](https://thenewstack.io/compliance/)的同时做到这一点。例如，由于数据隐私和安全问题，[49% 的医疗保健组织完全限制使用生成式人工智能](https://www.liminal.ai/case-studies-foundational-papers/generative-ai-adoption-report)。

## 人工智能实施困境

想象一下在受监管行业的会议室中出现的典型场景：一位首席信息官 (CIO) 展示了他们的人工智能试点项目的结果。当他们展示他们的原型人工智能系统如何在提高准确性的同时将客户服务响应时间缩短 40% 时，兴奋之情显而易见。董事会成员印象深刻，首席执行官 (CEO) 渴望在整个组织中推广该解决方案。然后出现了关键问题：“我们多久才能在生产环境中部署它？”

这就是热情碰壁的地方。首席信息官解释说，从原型到生产不仅仅是扩大规模的问题，而是要应对安全要求、合规法规和运营限制的复杂迷宫。可用的前进道路都存在重大缺陷。

## 公共 SaaS 困境

一个看似简单的选择是采用公共 SaaS 人工智能解决方案，例如用于[嵌入模型](https://zilliz.com/ai-models?utm_source=vendor&utm_medium=referral&utm_campaign=2025-02-11_blog_byoc-security_tns)、大型语言模型 (LLM) 和完全托管的[向量数据库](https://zilliz.com/learn/what-is-vector-database?utm_source=vendor&utm_medium=referral&utm_campaign=2025-02-11_blog_byoc-security_tns)的公共 API 服务。这些平台提供强大的开箱即用功能，并为用户提供最低的运营开销。

然而，缺点也很明显：数据驻留在供应商的云帐户中，而不是客户的云帐户中，并且与公共 API 服务的通信必须通过公共网络。对于受监管的行业来说，这种选择通常是不可行的。安全团队会标记客户数据通过公共网络传输的问题，合规官会担心数据驻留要求，风险管理人员会强调在依赖第三方服务时维护审计跟踪和问责制的困难。

## 本地部署的挑战

另一种选择是使用[开源软件](https://thenewstack.io/is-community-backed-open-source-software-worth-the-risk/)在本地部署所有内容。如果执行正确，这种方法有望实现完全控制和合规性，但它也带来了一系列挑战。

首先，它需要在专门的 DevOps 团队中进行大量投资，以管理本地部署、解决问题和处理持续维护。运营开销可能令人望而却步，并且与依赖专家管理的服务相比，中断的风险更高。随着人工智能技术以惊人的速度发展，对于内部团队来说，跟上软件更新和新模型发布几乎是不可能的。此外，组织在遇到生产问题时，可能会因缺乏专门的支持而面临延误和中断。

一位医疗保健首席技术官 (CTO) 将此描述为“人工智能炼狱”。各组织发现自己陷入了有希望的原型和生产部署之间，眼睁睁地看着其他人竞相实施人工智能。人工智能的商业案例很明确，技术也已得到验证，但安全合规部署的道路仍然令人沮丧地遥不可及。

## 人工智能部署中的关键安全挑战

企业在规模化采用人工智能方面面临着独特的障碍。敏感数据必须保留在安全、受控的环境中，避免使用公共网络或共享基础设施。传统的 SaaS 模型通常无法满足这些严格的数据主权和合规性要求。

除此之外，组织还需要精细的控制、全面的审计和完全的透明度，以追踪每一个AI决策和数据访问。这确保了未经明确批准和记录，供应商无法与敏感数据交互。这些未被满足的需求造成了巨大的差距，阻碍了受监管行业在保持合规性和安全性的前提下部署AI解决方案。

## BYOC：第三条前进的道路

自带云（BYOC）的概念并不新鲜。它作为传统SaaS和本地部署之间的一种折衷方案出现，承诺结合两者的优点：托管服务的便利性和本地基础设施的控制和安全性。然而，它在行业中的历史既有成功，也有警示。

早期的BYOC实施通常未能兑现其承诺。一些供应商只是将他们的软件部署到客户的云账户中，而没有进行适当的架构规划，导致实际上是远程管理的本地环境。此外，仅将数据托管在客户的云账户中并不能保证安全。供应商仍然需要登录到客户的账户进行故障排除，这可能会打破很多假设。在BYOC中实现真正的安全性是一项独特的挑战。正如一位行业资深人士恰如其分地描述的那样，这种方法变成了“[an architectural dead end](https://jack-vanlightly.com/blog/2023/9/25/on-the-future-of-cloud-services-and-byoc)”——起初看起来很有希望，但最终却制造了比解决的问题更多的问题。

## 为AI工作负载重新构想BYOC

BYOC的故事并没有就此结束。企业AI工作负载的兴起创造了一个新的背景，在这种背景下，经过深思熟虑的BYOC提供了独特的价值。新一代的BYOC架构通过清晰地分离控制平面和数据平面，有效地解决了以前的安全问题。在这种模式下，所有业务逻辑和数据处理都保留在客户的私有网络中，而供应商的控制平面管理资源调度和系统升级等操作任务，而无需访问敏感数据。这种方法远远超出了简单地将软件部署在客户的VPC（虚拟私有云）中。一个设计良好的BYOC实现通常包括以下关键特征：

*   **客户网络内的数据主权**：所有数据处理和流动都严格保留在客户的VPC内，确保完全的数据控制。
*   **安全至上的架构**：整个控制流程的架构都以安全性为基本原则，而不是将安全性改造到现有设计中。
*   **有限的、受控的供应商访问**：供应商访问严格限制在客户批准的即时操作上，并对所有操作进行全面日志记录。
*   **完全的操作可见性**：系统维护控制平面和数据平面之间所有交互的详细审计跟踪，尤其是在故障排除期间。

**Zilliz的BYOC方法**

[Zilliz](https://zilliz.com/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-02-11_blog_byoc-security_tns)开发了一种[BYOC](https://zilliz.com/bring-your-own-cloud?utm_source=vendor&utm_medium=referral&utm_campaign=2025-02-11_blog_byoc-security_tns)解决方案，专为向量搜索而设计，以满足企业级的安全性。该架构将系统操作分为两个不同的区域：控制和数据。每个区域都有特定的用途，同时保持安全边界。

![](https://cdn.thenewstack.io/media/2025/02/4cd6eaef-image2-1024x627.png)

**清晰地分离管理和数据**

由Zilliz管理的控制平面充当管理层，处理资源调度和系统升级等任务。可以把它想象成一个监督者，监控系统的健康状况并管理基础设施，但从不与实际数据交互。数据平面完全在客户的VPC和云账户中运行，确保客户的应用程序服务器和向量数据库之间的通信包含在客户的VPC中。所有数据都受到行业标准加密的保护，无论是在传输过程中还是在静态存储时。

**企业级网络安全**

为了满足企业网络安全要求，管理流量是加密的，并且仅从数据平面到控制平面的出站流量，从而防止供应商直接访问客户的VPC。AWS PrivateLink支持确保控制平面和数据平面之间的安全通信，而无需将其暴露于公共互联网。该连接使用TLS 1.2+ over port 443/HTTPS，并且默认情况下只能从客户的数据平面启动。

**细粒度的访问控制**

精细的权限设置确保对控制平面的最小权限访问。授予用于管理客户云账户内集群的跨账户 IAM 角色的每个权限都经过精心策划和审查，以坚持最小权限原则。访问权限还被限制于特定的资源名称或客户定义的资源标签，从而防止暴露客户云账户中的其他数据。

**即时供应商访问和审计日志记录**

供应商对数据平面的访问（用于故障排除）取决于客户的同意，并且受到严格控制。所有访问方面——包括身份验证详细信息、执行的操作、授权、上下文信息、所做的更改以及任何异常或可疑活动——都会被彻底记录并持续监控。Zilliz 的安全团队会定期进行审计和风险审查，以确保符合安全标准并快速解决任何潜在问题。

这种方法使组织能够继续进行具有生产就绪的向量搜索功能的 AI 创新，而不会影响满足严格合规性要求所需的控制和[安全性](https://thenewstack.io/master-difficult-user-authentication-requirements-with-oauth/)。

## 展望未来

虽然没有适用于所有 AI 部署的万能解决方案，但 BYOC 提供了一个实用的中间地带。它允许企业利用托管的 AI 服务，同时保留受监管行业中合规性所需的控制和安全性。随着 AI 采用在各个领域持续加速，像 BYOC 这样的方法对于努力在创新与严格的安全性和合规性需求之间取得平衡的组织至关重要。如果您有兴趣将具有企业级安全性的向量数据库引入您的应用程序，请考虑查看 Zilliz Cloud BYOC [文档](https://docs.zilliz.com/docs/byoc/byoc-intro#how-it-works?utm_source=vendor&utm_medium=referral&utm_campaign=2025-02-11_blog_byoc-security_tns)以获取更多详细信息。

