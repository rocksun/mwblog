<!--
title:  基础设施即代码终极指南
cover: https://cdn.thenewstack.io/media/2024/01/984f4092-jon-tyson-dzjtzdl7dwo-unsplash-1024x659.jpg
-->

IaC 可以通过机器或者直接到机器的代码来部署、管理和扩展基础设施。

> 译自 [Infrastructure as Code: The Ultimate Guide](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/)，作者 B. Cameron Gain 是 ReveCom Media 的创始人和首席分析师。他对计算机的痴迷始于 20 世纪 80 年代初，当时他破解了太空侵略者控制台，以每天 25 美分的价格在当地视频游戏厅玩了一整天。

什么是基础设施即代码(IaC)，为什么它正在获得普及？

随着 IaC 的兴起，DevOps 中对于与机器直接通信的需求日益增长，这使得开发人员和运维人员能够使用共享语言来实现和管理基础设施。

这消除了不必要的软件接口层，促进了更清晰的方法。同时也存在着减少复杂性、远离软件接口中的“臃肿”的趋势。

人们似乎更喜欢直接交互，有时通过[大型语言模型(LLM)](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)接口以近乎自然语言的方式交互，然后显示用于基础设施的代码。

IaC 允许通过机器或机器直接代码来部署、管理和扩展基础设施。

鉴于 IaC 倾向于提供一种直接配置、部署和管理基础设施的方式，它非常适合版本控制以及版本控制 [DevOps](https://thenewstack.io/thinking-in-systems-a-sociotechnical-approach-to-devops/) 或 [GitOps](https://thenewstack.io/achieve-gitops-on-day-one-with-iac-automation/) 的扩展，从这个角度来看，它也提供了扩展机会。

“IaC 的重要意义在于它为您提供了一种自动化基础架构层部署清单的方式，与其位置和规模无关，”“GitOps” 一词的创造者 [Alexis Richardson](https://uk.linkedin.com/in/richardsonalexis) 对 The New Stack 表示。

## IaC 的原则是什么？

IaC 通过机器或直接到机器的代码实现基础设施的部署、管理和扩展。这与传统的通过接口和额外软件层进行操作的方法形成对比。由于其直接的方法，IaC 有利于版本控制，并扩展到 DevOps 或 GitOps，提供扩展机会。

IaC 的流行开源配置包括 HashiCorp Terraform(及其开源等价物 OpenTofu)、[Nitric](https://nitric.io/?utm_content=inline-mention)、Pulumi 和 [Red Hat Ansible](https://www.openshift.com/try?utm_content=inline-mention)。

## IaC 如何应用于持续集成/持续交付(CI/CD)？

通过命令行一致高效地在各种环境中进行基础设施供应和部署的 IaC 使用非常适合 CI/CD。

当 IaC 应用于生产流水线时，组织报告说生产力和资源节省有所提高。但是，并非所有的 IaC 解决方案都效果相同。潜在的 IaC 用户应该仔细审视某个特定解决方案是否以及如何能够真正改善 CI/CD 流程。

IaC 解决方案应为 CI/CD 提供:

- 自动化供应
- 不变的版本控制，因此使用单一仓库创建和删除基础设施
- 贯穿 CI/CD 的测试功能
- 设置策略的能力
- 管理安全的能力

IaC 为 CI/CD 提供的不变性“至关重要”，[企业管理协会(EMA)](https://www.enterprisemanagement.com/)分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk/) 对 The New Stack 表示。他说，之所以如此，是因为它“确保一致性、便于回滚的清晰审计轨迹、对安全性和合规性的统一控制，以及整体效率”。

## IaC 如何用于设置策略和管理安全？

IaC 提供了一种统一的方法来处理和定义各种配置的策略。其优势不仅限于声明式方法，还影响到基于工具选择和 IaC 方法论的安全管理。

在 Pulumi 年度用户大会 PulumiUP 上题为“一家银行如何通过基础设施即代码自动化现代化其软件工程”的演讲中，华盛顿信托银行的 DevOps 工程师 [Dennis Sauvé](https://www.linkedin.com/in/dengsauve/) 提供了一个关于 IaC 在银行策略和安全方面的角色的小案例研究。

他指出他如何与开发人员“合作理解他们的云基础设施需求，并协调如何最好地使用我的团队和信息安全部门的资源来部署这些资源。”

根据 Sauvé 的说法: “与我们的开发团队合作有时会具有挑战性。我们的开发团队遵循敏捷框架进行调度，而基础设施则遵循更多看板分类框架进行工作，毕竟这是 IT 运维。这意味着有时候我有大量带宽来协助开发目标，而其他时候我在基础设施上的职责必须优先。”

华盛顿信托银行采用 IaC 的总体目标是“消除基础设施可用性成为瓶颈，并以预制的基础设施即代码资源和组件的形式将大量开发环境脚手架放在开发人员手中”，Sauvé 说。自动化部署极大地减轻了基础设施团队的大量手动部署负担，并“为未来项目创建可重复使用和可重用的组件”，Sauvé 说。

在华盛顿信托银行决定在其部署流水线中采用 IaC 之前，联邦存款保险公司(FDIC)关于保护客户个人数据的严格规定影响了这一决定，Sauvé 说。

正如 Sauvé 所描述的:“数据泄露对组织的客户有可怕的影响，所有托付给我们的数据都必须视为机密。这是因为这是正确的事情，也是因为 FDIC 强制要求这样做。鉴于必须保护客户数据，使用基础设施即代码构建云资源提供了一个可以[由信息安全部门](https://thenewstack.io/how-to-enable-developer-teams-to-improve-container-security/)和基础设施团队审查和改进的蓝图。”

## 基础设施即代码的一个例子是什么？

IaC 涉及使用 Ansible 等工具来管理和自动化 IT 基础设施。Ansible 需要安装其软件并随后执行命令。初始步骤涉及创建 Ansible playbook，它由指导 Ansible 执行各种任务的 YAML 指令组成，跨越部署、网络、服务管理以及[安全和策略配置](https://thenewstack.io/tutorial-create-a-kubernetes-pod-security-policy/)。

以下是配置 Ansible playbook 的 YAML 指令示例:

![Zoom](https://cdn.thenewstack.io/media/2024/01/cfa5dda0-capture-decran-2024-01-16-144453-1024x250.png)

*来源:Ansible 项目贡献者。*

设置 playbook 后，使用此命令运行 playbook:

![Zoom](https://cdn.thenewstack.io/media/2024/01/c89276ff-capture-decran-2024-01-16-144808-1024x54.png)

*来源:Ansible 项目贡献者。*

输出如下所示:

![Zoom](https://cdn.thenewstack.io/media/2024/01/c37d7780-capture-decran-2024-01-16-145028-1024x234.png)

*来源:Ansible 项目贡献者。*

## IaC 有哪些局限性？

IaC 确实存在局限性 —— 即，它旨在自动化并避免在创建和管理基础设施时进行手动流程。

仅使用基本的开源替代方案或工具，比如 Terraform 会有局限性。因此，自动化这些工具，提供更直接的基础设施供应方式，或使其简化会大有裨益。

这对开发人员尤为重要。例如，对于提供基础设施工作流程自动化的工具，IaC 可以帮助开发人员在代码文件中更加声明式地[配置和管理云基础设施](https://thenewstack.io/how-much-of-cloud-native-incidents-should-developers-manage/)。

其想法是为开发人员在[云中设置基础设施](https://thenewstack.io/3-tips-to-secure-your-cloud-infrastructure-and-workloads/)时降低错误概率并提高不变性。提供执行 IaC 的同时简化该流程的能力 —— 并提供更易于使用的模板，例如用于 Terraform、Ansible 或任何其他工具 —— 有助于实现这一目标。

## 如何自动化或改进 IaC？

出现了许多替代方案，它们要么添加层以提升自动化并添加类似 Terraform 或 Ansible 的附加功能，要么寻求替换这些解决方案。就 Terraform 对手 Pulumi 而言，虽然 Terraform 的市场份额几乎是 Pulumi 的 10 倍，但根据企业管理协会(EMA)的数据，Pulumi 的份额增长率是 Terraform 的 2-3 倍。这些解决方案(包括 Nitric 和 Pulumi)旨在为 IaC 提供自动化目标。

Pulumi CEO 兼创始人 [Joe Duffy](https://www.linkedin.com/in/joejduffy/) 在 Pulumi 年度用户大会 PulumiUP 上的主旨演讲中表示，Pulumi 提供的编程语言选择的灵活性至关重要。“例如，许多用户今天不幸仅限于使用 YAML 进行部署，这不应该是这种情况;开发人员不应该仅限于一种语言，”Duffy 说。

另一方面，Pulumi 声明支持所有主流编程语言，从而为持续集成/持续交付(CI/CD)和一般情况下的基础设施配置提供更多的选择自由和更直接的方法。

“Pulumi 是您最喜欢的语言中的基础设施即代码 —— 熟悉基础设施即代码的人可能使用过其他工具，这些工具使用特定域语言甚至标记语言如 YAML 或 JSON，这在开始时通常就足够了。但尤其是当我们扩展到现代云架构时，缺陷开始显现，”Duffy说。

“因此，Pulumi 的方法真的是采取不同的方法:携带您最喜欢的编程语言，无论是 JavaScript 还是 TypeScript，Python，Go。Pulumi 在其核心是多语言的。这意味着您可以利用编程语言的所有丰富功能来表达您的基础设施即代码。”

## 基础设施即代码如何与 GitOps 集成？

首先，让我们描述一下 [GitOps 是什么](https://thenewstack.io/gitops-git-push-all-the-things/)，以及它如何用来自动化和简化持续集成/持续交付的基础设施部署，以及在复杂的环境(如 Kubernetes)中。

云原生计算基金会应用程序交付特别兴趣小组下的 GitOps 工作组 [OpenGitOps](https://opengitops.dev/) 已经发布了关于 GitOps 的精确且以共识为导向的描述。它由一组开源标准、最佳实践和面向社区的教育组成，以帮助组织采用结构化、标准化的方法来实施 GitOps。它将 GitOps 原则描述为:

- **声明式**: 由 GitOps 管理的系统必须声明式地表达所需状态。
- **版本化和不变性**: 所需状态以强制不变性和版本控制的方式存储，并保留完整的版本历史记录。  
- **自动拉取**: 软件代理自动从源中拉取所需的状态声明。
- **持续协调**: 软件代理持续观察实际系统状态，并尝试应用所需状态。

“目标是改善云原生部署的可访问性和可管理性，简化与 Kubernetes 相关的复杂性，并促进更顺畅的运营，”Alexis Richardson说。“这些改进将通过正在进行的努力和 GitOps 的进步实现，在很大程度上由开源社区和类似 [Flux](https://thenewstack.io/argo-cd-and-flux-are-cncf-grads-but-what-now/) 的项目推动，”他说。

可以说，基础设施即代码就是 GitOps —— 或者至少，它是 GitOps 工作方式的一个组成部分。在开发人员方面，无论是仅使用拉取请求，还是在概念上通过 Flux 或 Argo 将应用程序放在存储库上，开发团队都使用基础设施即代码命令来完成这项工作，使用模板或 API。

当应用程序部署时，例如，运维人员更新和部署实际基础设施时，不变性方面就是基础设施即代码角色发挥作用的地方。

根据 Richardson 的解释，与此同时，您也得到了自动化，这是 GitOps 的一个关键方面。一组标准代码模板用于作为持续集成/持续交付领域的 GitOps 的一部分创建、部署等应用程序。这反映了基础设施即代码的自动化部分。当然，这个自动化与 GitOps 同时发生。

Richardson 说，GitOps 和基础设施即代码包括三个不同的用例:基础设施即代码、持续集成/持续交付(特别是持续交付)和[平台工程](https://thenewstack.io/year-in-review-platform-engineering-still-run-by-spreadsheet/)。

“这三个元素汇聚形成一种协调方法，用于自动化如何管理整个技术栈:最佳实践要求使用这些工具的组合来协调正确的部署，管理流水线、交付、机群和规模，”Richardson说。“随着规模的扩大，您会发现需要采用新技术来处理规模，因为对于 1000 个集群有 1000 个 Git 仓库是不实际的。理想情况下，您要么需要一个 Git 仓库，要么最多只需要一小部分。”
