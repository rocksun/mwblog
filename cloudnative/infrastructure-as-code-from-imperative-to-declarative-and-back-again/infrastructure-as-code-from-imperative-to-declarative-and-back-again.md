
<!--
title: 基础设施即代码：从命令式到声明式再回到命令式
cover: https://cdn.thenewstack.io/media/2025/01/9672deb8-kevin-ku-w7zyugynprq-unsplash-1-scaled.jpg
-->

向混合 IaC 模型转变是由开发者体验、效率以及对可扩展云原生解决方案的需求所驱动的。

> 译自 [Infrastructure as Code: From Imperative to Declarative and Back Again](https://thenewstack.io/infrastructure-as-code-from-imperative-to-declarative-and-back-again/)，作者 Arel Rabinowitz。

[基础设施即代码](https://thenewstack.io/introduction-to-infrastructure-as-code/)（IaC）这些年来经历了令人着迷的转变。基础设施管理的演变是一个不断迭代的故事，它受到扩展系统、速度和安全指标（如 [DORA](https://www.env0.com/blog/dora-metrics-an-infrastructure-as-code-perspective)）以及开发者生产力需求的影响。

从命令式方法（管理员编写详细的脚本来配置和设置基础设施）开始，行业转向声明式 [IaC](https://thenewstack.io/infrastructure-as-code-from-imperative-to-declarative-and-back-again)，这是由对可扩展性、可重复性和减少人为错误的需求所驱动的。Terraform 等声明式工具使得定义基础设施**应该**是什么样子，而不是指定**如何**创建它成为可能。这降低了复杂性并提高了可靠性。

在 2025 年，我们看到一种微妙但有意义的回归到命令式方法——尽管带有一些变化。让我们探讨一下行业如何在命令式和声明式方法之间转变，并融合到今天的混合模型。

## 早期：命令式配置管理

在 2000 年代初期，Chef 和 Puppet 等工具率先实现了基础设施配置自动化。Paul Hammond 和 John Allspaw 在 O'Reilly 的 Velocity 大会上发表了具有影响力的演讲 [10+ Deploys Per Day: Dev and Ops Cooperation at Flickr](https://www.youtube.com/watch?v=LdOe18KhtT4)，展示了现代工具如何改变工程实践。当时，每天实现 10+ 次部署似乎是科幻小说。

[Chef](https://www.chef.io/) 和 [Puppet](https://www.puppet.com/) 是早期最流行的配置管理平台，它们成为这种转变的支柱，引入了一种配置系统的新方法。然而，它们在命令式范例中运行，用户明确地概述了实现所需配置的步骤。

例如，安装软件需要指定每个命令，定义条件，并仔细控制操作顺序。

虽然功能强大，但命令式方法在可扩展性和维护方面存在不足。它们对这种范例的依赖使得脚本特定于环境且脆弱，需要大量的人工工作来适应不断发展的基础设施需求。

这导致了以下几个限制：

- **复杂性增加**： 随着基础设施的扩展，脚本变得笨拙。
- **容易出错**： 小错误经常导致不一致，尤其是在不同环境中。
- **重复逻辑（不 DRY – 不要重复自己）**： 脚本中重复的代码造成了巨大的维护负担。

## 转向混合声明式配置

随着行业认识到纯粹命令式方法的缺点，[Ansible](https://www.redhat.com/en/ansible-collaborative?intcmp=7015Y000003t7aWQAQ) 等工具应运而生，作为一种过渡解决方案，融合了命令式和声明式范例。毫不奇怪，Red Hat 在 Ansible 获得发展势头后迅速收购了它。凭借其基于 YAML 的 playbook，Ansible 允许用户定义他们的基础设施，而无需指定实现它的确切步骤。虽然在底层仍然按顺序执行任务，但 Ansible 接受了描述结果而非过程的声明式理念。

Ansible 的成功表明了对基础设施管理中更多抽象的需求，为完全声明式工具铺平了道路。

## 声明式革命和 IaC 的突破

这种转变随着 [Terraform](https://www.terraform.io/) 和 [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 等工具的出现而到来，它们采用了完全声明式模型。用户不再关注过程步骤，而是在配置文件中定义了他们期望的基础设施状态。

这些工具将这种状态与现实进行协调，自动执行实现结果所需的行动。Terraform 引入了状态文件来跟踪资源，从而实现增量更新和可扩展性，而 CloudFormation 利用 JSON 或 YAML 模板以声明方式管理 AWS 资源。两者都为命令式模型带来的挑战提供了独特的解决方案。

这种范式转变解决了命令式方法中固有的许多问题：

- **可扩展性**： 声明式 IaC 可以在不同环境中轻松扩展。
- **一致性**： 状态跟踪确保了部署的统一性。
- **效率**： 团队可以管理基础设施，而无需重复过程逻辑。

## 命令式复兴（某种程度上）

如今，像 [Terraform CDK](https://developer.hashicorp.com/terraform/cdktf) (TFCDK) 和 [Pulumi](https://www.pulumi.com/) 这样的工具已成为工程师的热门选择。这些工具允许开发人员使用熟悉的 [编程语言](https://thenewstack.io/programming-languages/)（如 Python、TypeScript 或 Go）编写 IaC。乍一看，这似乎是命令式 IaC 的回归。然而，在底层，它们仍然生成声明式配置（例如 Terraform 计划或 CloudFormation 模板），这些配置定义了基础设施的期望状态。

为什么命令式风格的接口会再次兴起？

答案在于提高开发者体验 (DX)、实现自助服务和增强可访问性这一更广泛的趋势。与我们在平台工程等领域看到的转变非常相似，这些工具旨在简化工作流程并使开发人员能够更有效地工作。

## 为什么是现在？

当前的格局代表了一种哲学的融合。虽然 IaC 工具在管理状态和资源方面仍然是根本上声明式的，但它们越来越多地结合类似命令式的接口来增强可用性。

转向命令式风格的接口并不是倒退。相反，它突显了一个更广泛的运动，即优先考虑开发人员的可访问性和生产力，与对简化工作流程和自助服务能力的强调相一致。

- **开发者熟悉度**： 许多开发人员更熟悉通用编程语言，而不是 YAML 或特定于领域的配置语言。使用熟悉的代码消除了陡峭的学习曲线。
- **代码重用**： 开发人员可以将现有的应用程序逻辑合并到他们的 IaC 配置中。例如，描述应用程序代理行为的代码可以重用于定义基础设施设置。
- **生产力提升**： 像 TFCDK 和 Pulumi 这样的工具使 IaC 更容易上手，从而实现了基础设施管理的民主化。开发人员无需切换上下文或学习全新的语言即可定义基础设施。
- **幕后的声明式能力**： 虽然开发人员以命令式方式编写配置，但底层操作仍然是声明式的。这确保了可扩展性、一致性和状态管理优势的保留。

即使在 CI/CD 等相邻领域，我们也看到了这种融合。像 Dagger 和 Buildkite 这样的工具让开发人员可以使用熟悉的编程语言来定义工作流程，从而创建更易于访问的体验，同时在底层保持声明式输出。

## 2024/5 年的完整循环

在许多方面，我们已经完成了一个完整的循环——但采用了熟悉的现代概念。推动更友好的开发者界面并不是要重新发明 IaC，而是要提高其可访问性和可用性。即使在收购了 Red Hat（以及扩展的 Ansible）之后，IBM 现在也准备收购 HashiCorp，这突显了 IaC 格局的发展程度。

声明式 IaC 仍然是核心，但较新的工具提供了类似命令式的接口，这些接口更好地与开发人员的工作流程保持一致，并强调灵活性、生产力和协作。这些创新降低了复杂性，支持协作可扩展性，并改进了基础设施管理。它们反映了 DevOps 和 [云原生开发](https://thenewstack.io/cloud-native/) 的趋势。

## 接下来是什么以及 IaC 的未来

随着命令式和声明式 IaC 之间的界限变得模糊，混合工具应运而生，结合了两者的优点。改进的状态管理、与应用程序逻辑的更紧密集成以及增强的多云支持正在 [推动 IaC 的未来朝着简单性和生产力发展](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/)。不同的 DevOps 平台（如 env0）正在帮助团队采用这些混合方法，以更少的投入获得更多成果。

这些模型提供了命令式风格编码的灵活性，同时保留了声明式 IaC 的可扩展性和一致性。目标不是选择一种范例而不是另一种范例，而是将它们的优势结合起来以满足不断变化的需求。随着工具的发展，平衡新旧方法仍将是 IaC 创新的核心。
