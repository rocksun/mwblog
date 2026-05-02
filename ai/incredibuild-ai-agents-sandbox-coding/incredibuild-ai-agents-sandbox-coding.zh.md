某处，一位开发者正半开着笔记本电脑走来走去，以免他的 AI 编码智能体关机。

这就是 2026 年企业 AI 开发的现状——而 [Incredibuild](https://www.incredibuild.com/) 正试图通过 Islo 来解决这个问题，这是一个为每个智能体提供独立、持久且隔离的云环境的沙箱。

该公司以其被 Microsoft、Take-Two 和 Nintendo 使用的[构建加速平台](https://www.incredibuild.com/glossary/build-acceleration)而闻名，现已发布了 Islo，这是一个专为[AI 编码智能体](https://thenewstack.io/ai-coding-agents-level-up-from-helpers-to-team-players/)打造的沙箱。

其目标是为每个智能体提供专用的、隔离的云环境，由明确的策略进行管理，这样工程团队就可以持续运行智能体，而无需担心在开发者机器或非托管基础设施上放任它们所带来的安全和治理难题。

## 智能体不适用于“一名开发者，一台机器”的模式

“编码智能体现在已经能够完成实际工作，但它们都在开发者的笔记本电脑上运行，”Incredibuild 产品工程总监 [Adam Gold](https://www.linkedin.com/in/adamgold7/) 在新闻稿中表示。“这意味着当盖子关闭时，它们就会消失，而且它们拥有访问机器上所有内容的权限。

“我们构建 Islo 是因为我们相信每个 AI 智能体都需要自己的计算机——不是短暂的容器，而是具有自身运行服务、作用域凭据且生命周期不依赖于人工监管的长期运行开发环境。”

> “我们构建 Islo 是因为我们相信每个 AI 智能体都需要自己的计算机”

这种“每个智能体都需要自己的计算机”的说法不仅仅是一个口号。当前的行业模式是“一名开发者，一台机器”——这之所以有效，是因为开发者是一个受监管的单一行动者，他们坐下来工作，第二天再回来。

然而，该公司表示，智能体在三个特定方面打破了这一模式。它们的生命周期与人类不匹配——据报道，人们为了让智能体持续运行而半开着笔记本电脑走来走去，该公司直截了当地将其描述为“非正常工作流”。它们具有巨大的爆炸半径，继承了开发者积累的所有凭据——SSH 密钥、AWS 配置文件、浏览器 Cookie——但在何时不使用这些凭据方面完全缺乏判断力。而且它们需要带有运行服务、数据库和构建缓存的热持久环境，而短暂的容器在每次运行时都会将其丢弃。

## 既不是 Codespaces，也不是容器

Incredibuild 正在构建的是为每个智能体提供一台持久的、可寻址的机器——拥有自己的作用域凭据，且生命周期不会因为人类去吃晚餐而结束。

该公司表示，这种区别也将 Islo 与目前最接近的替代方案区分开来。像 [GitHub Codespaces](https://thenewstack.io/codeanywhere-founders-take-on-github-codespaces-with-daytona/)、[Daytona](https://thenewstack.io/codeanywhere-founders-take-on-github-codespaces-with-daytona/) 和 [Coder](https://thenewstack.io/self-hosted-cdes-preferred-to-saas-in-large-orgs-says-coder/) 这样的云开发环境是为人类构建的——它们假设连接了 IDE，会自动空闲超时，并且其安全前提是开发者是值得信赖的。

该公司表示，短暂沙箱针对亚秒级的冷启动进行了优化，旨在被销毁。Islo 是基于相反的假设构建的：智能体是主要用户，会话是持久的且没有会话上限，并且在智能体与沙箱外的一切之间有一个策略层。

## 控制点，而非策略语言

这个策略层值得详细了解，因为 Incredibuild 表示，“细粒度的策略控制”几乎可以意味着任何事情。在 Islo 的案例中，它并不意味着像 [Open Policy Agent](https://www.openpolicyagent.org/) 或 [Cedar](https://thenewstack.io/all-about-cedar-an-open-source-solution-for-fine-tuning-kubernetes-authorization/) 这样的策略语言——它意味着在特定的、明确定义的控制点进行强制执行。

网络网关位于 [VM](https://thenewstack.io/the-future-of-vms-on-kubernetes-building-on-kubevirt/) 之外，处理智能体发出的每一个出站调用。企业配置主机、端口和方法的允许列表，智能体无法绕过它，因为网关在其控制之外。文件系统边界强制执行每个路径的读写规则——智能体可能被允许写入 `/workspace`，但被阻止读取 `~/.ssh` 或 `~/.aws`。审计日志记录每一个 shell 命令、文件更改、网络调用和凭据使用情况。

这些控制点是独立的，因此团队可以根据特定智能体正在执行的操作，在运行开放的网络策略的同时运行严格的文件系统策略。

## 设计之初即为凭据盲视

凭据处理遵循类似的逻辑，即将强制执行保持在智能体无法触及的范围之外。凭据永远不会存在于沙箱中——不在 VM 镜像中，不在环境变量中，也不在智能体的文件系统中。

沙箱被 Incredibuild 称为“凭据盲视（credential-blind）”。相反，一个主机侧代理位于 VM 之外，并根据智能体的身份和每个沙箱的策略在网络边界注入凭据。智能体在没有凭据的情况下进行 API 调用；Islo 网关会为每个请求附加凭据。

“我们多年来一直致力于帮助团队快速交付，”Incredibuild 首席执行官 [Shimon Hason](https://www.linkedin.com/in/shimon-hason/) 在新闻稿中表示。“Islo 正在确保 AI 能够安全地交付。我们正在引入堆栈中缺失的一层：一个功能强大的沙箱，它提供了组织将 AI 智能体安全地作为实际生产工作流一部分运行所需的基础设施。”

## 定价与可用性

虽然 Islo 可以独立运行，但 Incredibuild 将其与现有的加速技术并置，以加快构建、测试和 [CI/CD](https://thenewstack.io/ci-cd/) 工作流中计算密集型的步骤。该公司还通过与 [Harbor Framework](https://www.harborframework.com/) 社区（一个用于编写和执行智能体基准测试及评估的开源基础设施项目）合作，瞄准了 AI 研究工作流。

Islo 推出了三个层级：支持多达五个并发沙箱的免费计划；团队（Team）计划价格为每 CPU 小时 0.07 美元和每 GB 小时 0.04 美元，支持多达 50 个并发沙箱；以及带有定制套餐的企业（Enterprise）层级。该公司表示，目前正通过私人测试版与一小部分设计合作伙伴合作。

Islo 现已在 islo.dev 上线。Incredibuild 在其平台上服务于 600 多家客户。市场是否准备好迎接堆栈中缺失的那一层，私人测试版将开始给出答案。