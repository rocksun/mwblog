<!-- 
# 平台工程的六大支柱之二：CI/CD 和 VCS 流水线
https://cdn.thenewstack.io/media/2023/09/66573c34-pillar-capitals-2135682_1280-1024x492.jpg
Image via Pixabay.
-->

平台团队为将 CI/CD 和 VCS 流水线集成到其平台而制定的工作流程和清单。

译自 [The 6 Pillars of Platform Engineering: Part 2 — CI/CD & VCS Pipeline](https://thenewstack.io/the-6-pillars-of-platform-engineering-part-2-ci-cd-vcs-pipeline/) 。

*本指南概述了平台工程中开发者体验的六大主要技术领域的工作流程和步骤。该指南分为六个部分发布，第一部分介绍了该系列并关注了安全性。第二部分将介绍应用程序部署管道。指南的其他部分如下所列，您也可以下载[完整的 PDF 版本](https://www.hashicorp.com/on-demand/the-six-pillars-of-platform-engineering?utm_source=partner&utm_medium=email&utm_campaign=24Q3_WW_SIXPILLARSOFPLATFORMENGINEERING_WP&utm_content=&utm_offer=whitepaper)以获取完整的指导、大纲和清单。*

1. [安全性(包括简介)](https://yylives.cc/2023/09/24/the-6-pillars-of-platform-engineering-part-1-security/)
2. 流水线(VCS、CI/CD) 
3. Provisioning
4. 连接性
5. 编排
6. 可观测性(包括总结和下一步)

## 平台支柱之二：流水线

平台团队旅程的首要步骤之一是集成并可能重构软件交付流水线。这意味着详细查看组织的版本控制系统(VCS)和持续集成/持续交付(CI/CD)流水线。

许多组织在不同成熟阶段拥有多个 VCS 和 CI/CD 解决方案。这些平台也会随时间发展，因此建议采用基于组件的 API 平台或目录模型来支持未来的可扩展性，而不会损害功能或要求定期重构。

在云原生模型中，基础设施和配置以代码的形式进行管理，因此 VCS 对此核心功能是必需的。使用 VCS 和管理代码提供以下好处：

- 一致性和标准化
- 敏捷性和速度
- 可伸缩性和灵活性
- 配置即文档
- 复用性和共享
- 灾难恢复和重现性
- 调试性和审计性
- 合规性和安全性

VCS 和 CI/CD 使跨多个基础设施系统和平台的交互和工作流成为可能，这需要仔细评估下面列出的所有 VCS 和 CI/CD 要求。

## 工作流程：VCS 和 CI/CD

典型的 VCS 和 CI/CD 工作流程应遵循以下五个步骤：

1. **代码**：开发人员将代码提交到VCS，并自动向流水线提交任务。
2. **验证**：CI/CD 平台向 IdP 提交验证请求(AuthN 和 AuthZ)。
3. **响应**：如果成功，流水线触发任务(例如测试、构建、部署)。
4. **输出**：输出和/或工件在平台组件内共享或与外部系统共享以进行进一步处理。
5. **操作**：安全系统可能参与后运行任务，例如取消供应 provisioning 凭据。

![](https://cdn.thenewstack.io/media/2023/09/67322118-hashicorp-2-01.jpg)

*VCS 和 CI/CD 流水线流程*

### VCS 和 CI/CD 需求清单

成功的 VCS 和 CI/CD 解决方案应提供：

- 针对团队需求定制的开发人员体验和现代化效率
- 易于入门
- 温和的学习曲线，需要很少的辅助培训(利用行业标准工具)
- 完整且可访问的文档
- 支持流水线即代码
- 平台不可知(API 驱动)
- 内嵌预期的安全控制(RBAC、审计等)
- 支持自动化配置(基础设施即代码、运行手册)
- 支持机密管理、身份和授权平台集成
- 鼓励并支持大型合作伙伴生态系统，具有广泛的企业技术集成
- 扩展的服务范围，具有代理人和隔离控制跨度的运行程序
- 基于 SLA 的企业支持(例如 24/7/365)

**注意**：VCS 和 CI/CD 系统可能有这里未列出的更具体的要求。

随着平台团队选择和发展他们的 VCS 和 CI/CD 解决方案，他们需要考虑这种转变对现有/遗留供应实践、安全性和合规性的影响。团队应该假设构建新平台将影响现有惯例，并且他们应该努力识别、协作和协调业务中的变化。

平台团队也应具有前瞻性。VCS 和 CI/CD 平台正在迅速发展，以进一步从开发人员那里抽象出 CI/CD 过程的复杂性。HashiCorp 旨在通过为开发人员提供一致的方式来部署、管理和观察跨多个运行时(包括 Kubernetes 和无服务器环境)的应用程序，使用 HashiCorp Waypoint 来简化这些工作流程。

敬请期待我们关于平台工程第三支柱的文章：[provisioning](https://thenewstack.io/the-pillars-of-platform-engineering-part-3-provisioning/)。或者下载《[平台工程的六大支柱](https://www.hashicorp.com/on-demand/the-six-pillars-of-platform-engineering?utm_source=partner&utm_medium=email&utm_campaign=24Q3_WW_SIXPILLARSOFPLATFORMENGINEERING_WP&utm_content=&utm_offer=whitepaper)》的完整 PDF 版本，以获取完整的指导、大纲和清单。
