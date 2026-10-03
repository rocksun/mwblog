<!--
title: “可以把它看作智能体的Kubernetes”：OpenClaw携手英伟达与红帽进军企业级市场
cover: https://cdn.thenewstack.io/media/2026/09/1506ac27-feat.png
summary: 开源AI智能体项目OpenClaw推出企业级平台OpenClaw Enterprise (OCE)，旨在通过提供类似Kubernetes的中心化控制面来解决企业IT对智能体安全的担忧，获得英伟达和红帽等公司的支持。
-->

开源AI智能体项目OpenClaw推出企业级平台OpenClaw Enterprise (OCE)，旨在通过提供类似Kubernetes的中心化控制面来解决企业IT对智能体安全的担忧，获得英伟达和红帽等公司的支持。

> 译自：["Think of it as Kubernetes for agents": OpenClaw lands in the enterprise with Nvidia and Red Hat on board](https://thenewstack.io/openclaw-enterprise-kubernetes-agents/)
> 
> 作者：Paul Sawers

“可以把它看作智能体的Kubernetes”：OpenClaw携手英伟达与红帽进军企业级市场

自从不到一年前作为病毒式的周末项目崭露头角以来，OpenClaw已经走过了漫长的道路。这个自托管的AI智能体由奥地利开发者 [Peter Steinberger](https://www.linkedin.com/in/steipete/) 于 2025 年底创建，其受欢迎程度呈爆炸式增长，到 2月份——当时 [OpenAI 聘用了 Steinberger](https://www.reuters.com/business/openclaw-founder-steinberger-joins-openai-open-source-bot-becomes-foundation-2026-02-15/) 时——它在 GitHub 上就已经获得了超过 10 万颗星。

在此后的几个月里，OpenClaw 采取了重大举措为该项目带来更多严谨性，收紧了[其持久化智能体架构](https://thenewstack.io/openclaw-persistent-agent-architecture/)，大力投资于安全性，添加了新的[智能体 harness 选项](https://thenewstack.io/openclaw-hermes-agent-harness/)，并[成立了](https://thenewstack.io/openclaw-foundation-nonprofit-status/)独立的 OpenClaw 基金会来监督该项目。这包括 OpenAI、Nvidia、Red Hat 和 GitHub 等赞助商，以及承诺贡献资源的其他一大批知名公司。

现在，它正通过 [OpenClaw Enterprise](https://docs-enterprise.openclaw.org/) (OCE) 迈出迄今为止进军严肃商业领域的最大一步，这是一个用于管理智能体的开源、“厂商中立”的平台。

## OpenClaw 获得企业级控制平面

赋予持久化智能体访问代码库、凭据、插件、消息通道和其他公司系统的权限，给企业 IT 带来了显而易见的问题：这些智能体变得越有用，其权限和操作的影响就越大。

在周二发布的一篇[博客文章](https://openclaw.ai/blog/openclaw-enterprise)中，OpenAI 领导 OCE 工作的技术人员 [Kevin Lin](https://www.linkedin.com/in/kevinslin-nimbus/) 论证说，许多公司仍然认为智能体平台难以进行集中管控，从而将禁止作为默认选择。

> “大多数组织中 IT 部门的默认立场是彻底禁止 OpenClaw 等智能体平台。”

“我们从组织听到主要反馈是，在完全采用智能体之前，需要有更强的通用安全、安全保障和治理标准，”Lin 写道。“因此，大多数组织中 IT 部门的默认立场是彻底禁止 OpenClaw 等智能体平台。”

OpenClaw Enterprise 仍处于萌芽阶段。Lin 表示，该项目目前“在今年晚些时候发布 1.0 版本之前正在公开开发中”，并补充说它目前仅适用于内部试点项目。

因此，在 OCE 可以被合理地视为成熟的企业平台之前，还有一段路要走。但其预期的轮廓已经清晰可见。

OCE 的核心是 OpenClaw 控制平面（OCC），它为管理员提供了一个中心化场所来部署智能体、将它们隔离到不同的命名空间中、管理配置和凭据、设置权限，并保留通过平台所做更改的记录。智能体活动本身是单独进行的：网关接收消息，而 harness 处理智能体轮次、模型调用和工具执行。

归根结底，OCE 的构建是为了适应多个智能体、用户和团队可能共享相同底层基础架构的环境，并对谁可以访问什么内容以及如何将单个智能体部署彼此隔离进行控制。

在差距方面，OpenClaw 的[架构文档](https://docs-enterprise.openclaw.org/)称其 API、控制台、持久化 worker、PostgreSQL 后端和 Kubernetes 打包已经实现，而包括外部网关准入、工作负载向 OCC 的身份验证以及某些模型身份验证方法在内的领域仍未完成。

> “OCE 专为在您自己的基础架构上运行而构建，并且对任何组织始终免费使用。”

这种未完成的状态至少部分是 OpenClaw 如此早地将 OCE 作为开源项目发布的原因。这个想法是让公司自己检查和调整软件，同时为外部开发者提供在正式发布之前塑造项目的机会。该代码[已经在 GitHub 上可用](https://github.com/openclaw/openclaw-enterprise)，并带有用于在本地运行或在组织内部部署的[入门指南](https://docs-enterprise.openclaw.org/#getting-started)。

“OCE 专为在您自己的基础架构上运行而构建，并且对任何组织始终免费使用，”Lin 指出。

## 应用于智能体的 Kubernetes 玩法

OpenClaw Enterprise 有着有趣的出身。在公司将项目移交给 OpenClaw 基金会之前，OpenAI 是它的最初诞生地。此后，Red Hat 和 Nvidia 一直为其开发做出贡献，而 OpenAI 和 Red Hat 已经在内部测试该软件。

> “把它想象成智能体的 Kubernetes。”

项目中还贯穿着一个相当明确的受 Kubernetes 启发的理念：OpenClaw 希望 OCE 为跨不同环境管理智能体提供一个通用层。“把它想象成智能体的 Kubernetes，”该项目的官方[文档](https://docs-enterprise.openclaw.org/)指出。

这种比较延续到了 OCE 的实际部署方式上。其完整的本地开发环境在 Kubernetes 集群内部运行控制平面、PostgreSQL 和智能体工作负载，同时公司可以将 OCE 安装到他们已经运营的 Kubernetes 基础架构中。该文档确实包含 Docker 或 Podman Compose 选项，尽管目前该选项仅限于控制平面预览，无法通过 OCC 部署智能体。

在 LinkedIn 上，Lin 也进行了清晰的 Kubernetes (K8) 比较，反映了 OpenClaw 对该项目的长期雄心。

> “类似于 K8 成为云中部署容器的标准，我们希望 OCE 成为智能体的标准。”

“类似于 K8 成为云中部署容器的标准，我们希望 OCE 成为智能体的标准，”Lin [写道](https://www.linkedin.com/feed/update/urn:li:activity:7510806587981344768/)。

就 Red Hat 而言，它以类似的视角看待企业智能体的崛起。在周二发布的另一篇[博客文章](https://www.redhat.com/en/blog/why-red-hat-building-open-foundation-enterprise-agents-openclaw-enterprise)中，Red Hat AI 业务单元副总裁兼总经理 [Joe Fernandes](https://www.linkedin.com/in/joefernandes1/) 划出了一条路线：从摆脱专有 Unix 系统转向 Linux，通过容器和 Kubernetes 的兴起，到现在走向智能体。他的论点是，Red Hat 可以将在帮助将这些早期技术引入企业环境中所学到的知识应用到新一代软件中。

“在 Red Hat 的历史中，企业计算的一些最大变革是由应用程序构建和运营方式的根本转变所驱动的，”Fernandes 写道。“Red Hat 的工程师已经在为 OpenClaw 做贡献，我们正在以 Linux、Kubernetes、分布式系统、安全性和企业基础架构方面的专业知识来扩大这一投资。”

安全仍然是 OpenClaw 表示正在集中精力的主要领域。该项目正在将受信任和不受信任的工作负载之间的隔离与沙箱、精细权限和 LLM 辅助审查相结合，并表示计划发布参考架构，展示这些部分如何在实践中组合在一起。

就目前而言，OCE 仍然是一个进行中的项目。控制平面正在成形，但许多工作尚未完成，OpenClaw 仍在邀请开发者、运维人员和安全团队在 1.0 版本之前帮助影响该项目的未来形态。

“我们还处于早期阶段，前方还有更多工作要做，”Lin 补充道。