<!--
title: Kubernetes 在企业中蓬勃发展，但如何才能成为主流？
cover: https://cdn.thenewstack.io/media/2025/06/16f616de-patrick-amoy-6dfebkqstia-unsplash-scaled.jpg
summary: Kubernetes采用率快速增长，主要驱动因素包括现代应用开发、灵活性需求和GenAI的普及。为使其成为主流，需加强教育培训，促进跨团队整合，尤其要重视安全和网络团队的参与。随着GenAI的部署，Kubernetes的使用将持续上升，安全解决方案也需同步发展。
-->

Kubernetes采用率快速增长，主要驱动因素包括现代应用开发、灵活性需求和GenAI的普及。为使其成为主流，需加强教育培训，促进跨团队整合，尤其要重视安全和网络团队的参与。随着GenAI的部署，Kubernetes的使用将持续上升，安全解决方案也需同步发展。

> 译自：[Kubernetes Surges in Enterprises, But What Can Take It Mainstream?](https://thenewstack.io/kubernetes-surges-in-enterprises-but-what-can-take-it-mainstream/)
> 
> 作者：Ratan Tipirneni

过去十年，Kubernetes 的采用经历了爆炸式增长。云原生计算基金会 (CNCF) 2024 年度调查中，93% 的受访者[报告](https://www.cncf.io/reports/cncf-annual-survey-2024/)他们要么在生产中使用 Kubernetes，要么正在试用/积极评估 Kubernetes。此外，Kubernetes 的生产使用率在 2024 年达到 80%，高于 2023 年的 66%。

在现代应用程序开发流程、生成式[人工智能开发](https://thenewstack.io/ai-for-developers-how-can-programmers-use-artificial-intelligence/)和部署的兴起，以及灵活性和可扩展性等优势的推动下，Kubernetes 正朝着主流方向发展。然而，在企业内部，平台和 DevOps 团队率先进行了迁移和采用，他们像一座“孤岛”一样，独立于技术团队中的其他成员，例如安全和网络从业者。为了简化 Kubernetes 的采用，需要更紧密的集成，并获得更广泛技术团队的支持。

## **Kubernetes 采用的主要驱动因素**

现代化和加速创新的驱动力促成了 Kubernetes 的采用。主要增长驱动因素包括：

* **现代应用程序开发流程：** 今天构建应用程序的开发人员使用在容器上运行的微服务架构，而 Kubernetes 是这些容器的默认编排系统。自 [Google 在 2015 年推出 Kubernetes](https://thenewstack.io/need-a-trillion-parameter-llm-google-cloud-is-for-you/) 1.0 版本以来，这一直是持续的增长驱动因素。
* **对灵活性的渴望：** 在本地和云之间，或在云中不同公共云提供商之间移动工作负载的灵活性是采用的催化剂。Kubernetes 的灵活性[避免了供应商锁定](https://thenewstack.io/opentelemetry-otel-is-key-to-avoiding-vendor-lock-in/)，赋予用户定价权 —— 这意味着如果他们没有从一个供应商那里获得他们想要的价格，他们可以很容易地转移到不同的供应商。
* **GenAI 的持续采用：** 自 OpenAI 在 2022 年发布 ChatGPT 以来，使 GenAI 的强大功能得到广泛应用，围绕这项技术的进步和势头是前所未有的。这推动了 Kubernetes 的使用，因为许多 GenAI 应用程序都在 Kubernetes 上运行。

## **Kubernetes 如何才能成为主流？**

显而易见的是，Kubernetes 在企业中的普及程度越来越高；业界不能再将 Kubernetes 视为仅供少数专家使用的独立实体。在过去的几年里，DevOps 和平台团队一直倡导 Kubernetes 的采用，这些用户在建立市场方面发挥了关键作用。但要使 Kubernetes 成为主流，它必须被相邻团队采用，并成为他们的第二天性。要实现这一目标，需要教育、培训和跨团队整合。

* **为非平台/DevOps 技术专业人员量身定制的教育计划：** 教育对于技术团队的广泛采用至关重要。教育工作必须从基础开始，并从基础知识入手：什么是容器和微服务？什么是 Kubernetes？这些技术和平台是如何工作的？安全影响是什么？发展这些基础知识使 Kubernetes 更容易被接受，并且是推动全组织范围采用的第一步。
* **专注的培训工作：** 在获得基础知识后，下一步是通过参与性的持续性培训课程将这些知识付诸实践。安全和网络专业人员必须踏上与 [平台和 DevOps 团队](https://thenewstack.io/platform-teams-win-over-devs-with-quick-wins/) 多年前完成的相同的培训“旅程”。需要有重点的培训工作来支持这一旅程，如今，许多 [Kubernetes 工程师都渴望帮助新用户](https://thenewstack.io/kubernetes-48-of-users-struggle-with-tool-choice/)。
* **更深入的跨团队集成：** 与企业基础设施和流程的其余部分集成是必要的。许多组织已经为网络和安全建立了流程和工具，而 Kubernetes 通常作为独立于这些框架的实体运行。集成到这些工具和流程中是释放更广泛增长和使用的必要条件。

## **Kubernetes 采用的未来之路**

随着 GenAI 部署的增加，Kubernetes 的使用量将继续上升，从而导致相应[安全解决方案](https://info.tigera.io/rs/805-GFH-732/images/ebook-Generative-AI-Security.pdf)的部署。为了使 Kubernetes 成为主流，优先考虑教育和培训、更深入的集成以及技术和安全团队之间的跨职能协作至关重要。

当前的 Kubernetes 工程师正在通过与新的和潜在的用户分享信息和最佳实践来帮助推动其使用。此外，[Kubernetes 的持续更新使其更容易使用](https://thenewstack.io/open-source-kubevirt-vm-management-with-kubernetes-is-a-work-in-progress/) —— 该系统正在从企业角度进行强化。这些努力共同简化了采用，并使相邻团队更容易使用该技术，从而迎来了 Kubernetes 主流使用的时代。