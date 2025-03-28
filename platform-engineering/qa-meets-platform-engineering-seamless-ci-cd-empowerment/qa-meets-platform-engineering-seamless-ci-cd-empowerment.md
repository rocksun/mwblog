
<!--
title: 质保团队与平台工程团队的融合：无缝 CI/CD 赋能
cover: https://cdn.thenewstack.io/media/2024/12/c979882e-qa.jpg
-->

本文探讨了挑战，并讨论了赋能 QA 团队的方法，从而实现更集成、更敏捷的软件交付方式。

> 译自 [QA Meets Platform Engineering: Seamless CI/CD Empowerment](https://thenewstack.io/qa-meets-platform-engineering-seamless-ci-cd-empowerment/)，作者 Bruno Lopes。


# QA 赋能平台工程：无缝 CI/CD 实践

![Featued image for: QA Meets Platform Engineering: Seamless CI/CD Empowerment](https://cdn.thenewstack.io/media/2024/12/c979882e-qa-1024x576.jpg)

鉴于当今快节奏的开发实践和左移趋势，质量保证 (QA) 的作用比以往任何时候都更加重要。为了快速发布高质量软件，必须将测试无缝集成到[CI/CD 管道](https://thenewstack.io/ci-cd/)中。

然而，尽管许多 QA 团队在编写和执行测试方面拥有专业知识，但他们面临的挑战却超出了测试本身的范围。他们经常发现自己要处理与基础设施相关的问题，需要 DevOps 或平台工程团队的支持才能充分实现其[测试工作流程](https://thenewstack.io/a-5-step-framework-for-test-execution/)。让我们探讨这些挑战，并讨论如何赋能 QA 团队，从而实现更集成、更敏捷的软件交付方法。

## CI/CD 环境下 QA 的挑战

质量保证专业人员是[理解软件功能](https://thenewstack.io/are-monolith-ci-cd-pipelines-killing-quality-in-your-software/)、边缘情况和用户行为的专家。他们设计全面的测试用例，分析结果并确保代码在进入生产环境之前符合质量标准。但在快速自动化部署成为常态的环境中，QA 工程师经常遇到与基础设施和平台管理相关的障碍，这些障碍超出了他们的传统技能范围。

### 1. 对平台工程 CI/CD 管道的依赖

CI/CD 管道是现代软件集成和部署的支柱，它提供了一种从代码提交到生产的自动化方式。对于 QA 团队而言，这些管道应该理想地在流程的每个步骤中促进测试执行。然而，在这些管道中构建、维护和扩展测试需要基础设施技能，而这些技能通常属于 DevOps 或平台工程的领域，而不是 QA 或测试人员。因此，QA 团队通常依赖这些团队来设置和管理管道，这可能会造成瓶颈和依赖关系，从而减慢测试过程。

### 2. 测试环境配置的挑战

理想情况下，测试环境应该稳定、一致，并且尽可能接近生产环境。然而，配置和维护此类环境并非易事。它需要强大的基础设施知识来处理容器编排、扩展、网络配置和其他技术复杂性，例如临时环境。如果没有这些环境随时可用，QA 团队很难进行彻底的测试，并且缺乏对环境管理的自主权会阻碍他们快速有效地工作。

### 3. 被测应用程序部署的复杂性

部署用于[测试的应用程序不仅仅是运行代码](https://thenewstack.io/stop-running-tests-with-your-ci-cd-tool/)。它需要管理依赖项、处理配置并确保部署是隔离的，以避免与其他工作流程发生干扰。对于许多 QA 工程师而言，部署管道的复杂性超出了他们的核心专业知识，这使得他们依赖 DevOps 团队来处理应用程序部署。这种依赖可能会导致延迟，尤其是在 DevOps 资源有限的情况下，从而减慢整体测试过程并影响产品发布。

## 未来方向：赋能 QA 团队自主工作

为了弥合这一差距，组织必须使 QA 团队能够更好地掌控其测试工作流程，并减少对平台工程的依赖。以下是一些可以考虑的方法：

### 1. 为测试环境实施自助服务平台

通过为 QA 团队提供自助服务平台，组织可以使他们能够按需配置和管理测试环境。Kubernetes 和 Docker 等容器化工具可以帮助简化此过程，使 QA 工程师能够启动隔离的环境，而无需 DevOps 的干预。自助服务平台可以定制为自动包含必要的配置，确保环境可靠、一致，并尽可能接近生产环境。

### 2. 将测试纳入自助服务平台

当平台工程师努力实施构建新组件和服务的自助服务方法时，这种方法也应该包括测试活动的必要模板和工作流程，包括：

- 使用 QA 团队选择的首选测试工具的函数测试和非函数测试模板。
- 将这些测试模板的执行集成到已配置的 CI/CD 管道中的配置。
- 用于排查测试失败和跟踪随时间推移的质量指标的工具和仪表板——根据需要集成到相应的开发者门户中。
### 3. 建立协作式 CI/CD 管道

通过让 QA 参与管道设计过程并为其提供简化的工具，平台工程可以促进更协作的管道管理方法。例如，允许 QA 控制测试参数、添加或修改测试阶段以及自定义测试工作流程的平台可以减少依赖性，并使 QA 能够更好地控制测试过程。

### 3. 自动化测试部署流程

[自动化测试环境部署](https://thenewstack.io/test-automation-tools-unite/) 可以最大限度地减少对 DevOps 的依赖，同时确保一致性。通过使用基础设施即代码 (IaC) 和模板化部署脚本，QA 团队可以自主触发测试环境部署，从而减少等待时间并提高测试效率。组织还可以考虑在测试环境中实施[蓝绿部署](https://testkube.io/learn/automating-blue-green-deployments-with-argo-rollouts-and-testkube) 或[金丝雀部署](https://testkube.io/learn/automate-canary-deployments-with-argo-rollouts-and-testkube)，允许 QA 团队在隔离的、类似生产的环境中测试应用程序的特定版本。

### 4. 投资培训和交叉技能培养

为了进一步赋能 QA，可以考虑投资培训，以增强他们对基础设施的了解，尤其是在 Kubernetes、IaC 和 CI/CD 工具等领域。跨职能团队方法也可以有所帮助，其中平台工程师和 QA 密切合作以共享知识和技能。随着时间的推移，QA 工程师可以建立他们管理基本基础设施任务所需的基础技能，从而使 DevOps 能够专注于更复杂或组织范围的问题。

## 通过 Testkube 弥合差距

在 Testkube，我们了解赋能 QA 团队克服基础设施挑战对于实现无缝、自动化的测试过程至关重要。我们的平台旨在简化 Kubernetes 环境中的测试编排，使 QA 团队能够管理测试、环境和工作流程，而无需广泛的基础设施知识。[Testkube](https://testkube.io) 与流行的 CI/CD 平台集成，使 QA 更容易自主部署、执行和监控测试，同时仍然可以与 DevOps 和平台工程团队有效协作。

## 培养协作、自主的测试文化

随着组织不断扩展并采用更快的开发周期，弥合 QA 和平台工程之间的差距变得至关重要。通过为 QA 团队提供处理基础设施相关挑战所需的工具、培训和自主权，组织可以创建一个更高效、更敏捷的测试流程。这反过来又会推动更快的发布、更高质量的软件和更协作的开发环境。

要了解有关 Testkube 如何为您的 QA 团队提供在 CI/CD 管道中简化测试所需的基础设施和工具的更多信息，请随时发送电子邮件至 [bruno@kubeshop.io](mailto:bruno@kubeshop.io) 或访问 [Testkube 的网站](http://testkube.io) 以[开始使用](https://www.testkube.io/get-started) 我们的测试控制平面。让我们一起重新定义测试如何集成到现代软件交付中。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)