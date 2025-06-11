# 打造成功的内部开发者门户的五大策略

![打造成功的内部开发者门户的精选图片](https://cdn.thenewstack.io/media/2025/06/a8e6ff5d-clint-patterson-jnaoptm2_ay-unsplash-1024x684.jpg)

[Clint Patterson](https://unsplash.com/@cbpsc1?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)在Unsplash上发布。

随着平台工程的兴起，内部开发者门户已成为减轻软件开发者负担的关键。根据Gartner的预测，到今年年底，预计75%拥有平台团队的组织将实施自助服务开发者门户。

许多开发者门户都是使用开源框架构建的，其中Backstage在受欢迎程度上遥遥领先。但是，如果没有正确的方法，这些门户可能无法获得交付其预期价值所需的吸引力。根据我们社区中工程领导者分享的见解，以下是确保您的开发者门户蓬勃发展的五个关键实践。

**1. 优先考虑自助服务体验**

开发者门户的核心目的是通过简化对整个软件开发生命周期（SDLC）中所需的工具和资源的访问来增强开发者体验。自助服务是这项任务的基石。开发者应该能够毫不费力地找到他们需要的东西，无论是设置基础设施、启动管道、添加可观测性功能还是运行测试。

为了实现这一目标，请创建一个组织良好的服务和文档目录，并将操作与开发者只需点击几下即可部署的模板配对。您应该优先考虑用户友好的界面，并包括常见用例的参考实现。真正的魔力发生在可发现性鼓励开发者[探索不熟悉的工具或服务](https://thenewstack.io/solocon-explore-service-mesh-api-gateways-graphql-ebpf/)时，从而激发创新并提高其工作流程的效率。

例如，我们的一位客户采用了Harness IDP来简化他们的开发者入职流程，并且效果立竿见影。由于预构建的模板和自动化，开发者可以进行自助服务，而无需依赖手动交接，从而将典型的入职时间从5-10天缩短到几个小时。

**2. 利用自动化消除重复性工作**

强大的开发者门户通过将自动化嵌入到日常流程中，使开发者从繁琐的重复性任务中解放出来。诸如[启动暂存环境](https://thenewstack.io/orca-security-launches-first-k8s-testing-staging-environment/)或将代码通过构建、测试和部署阶段之类的活动应需要最少的手动操作。

诸如基础设施即代码（IaC）之类的工具在这里至关重要，使开发者无需深入了解[管理当今复杂环境](https://thenewstack.io/managing-kubernetes-complexity-in-multicloud-environments/)的专业知识。为了减少辛苦的工作，您的组织应集成[IaC以配置环境并提供预构建的CI/CD管道](https://thenewstack.io/questions-to-ask-about-the-iac-in-your-ci-cd-pipeline/)。

这使他们可以将更多的精力投入到编码和交付业务价值上。为了保持质量，请使用记分卡自动执行扫描和验证检查，这些记分卡[根据性能或安全风险等指标评估代码](https://thenewstack.io/how-to-assess-integration-security-risks-when-evaluating-saas-vendors/)，从而为开发者提供护栏，以便他们可以自信地进行部署，而无需担心中断。

对于客户，我们看到他们的CI/CD流程通常涉及分散的脚本、多种工具且没有集中控制。一旦迁移到使用我们的开发者门户工具，他们现在就可以使用标准化的管道和记分卡来及早发现问题。这意味着开发者无需依赖DevOps专家来执行例行任务，而是可以在考虑策略和治理的情况下自行启动、测试和部署。

**3. 无缝连接生态系统**

开发者通常对经过多年实践磨练的工具和工作流程有根深蒂固的偏好。由于IDP旨在改善他们的体验，因此您的IDP应该与他们已经使用的工具集成，而不是强迫他们彻底修改工具包。

除此之外，开发工具经常与更广泛的系统交互，例如IT服务管理平台（例如，ServiceNow）、协作工具（例如，Slack）、代码存储库（例如，Git）或知识库。为了使开发者门户大放异彩，它必须与第三方和内部工具顺畅集成，使开发者能够以他们喜欢的方式高效工作。

为了使这种集成无缝衔接，您的组织应绘制出您的开发工具链并连接顶级工作流程，使用插件或API引入外部工具，并使常见操作（例如，创建存储库）成为一键式任务。
灵活性是我们大多数客户的关键，特别是那些运行混合模型的客户，在这种模型中，Harness 管理控制平面并将[操作](https://thenewstack.io/linux-run-a-single-command-across-multiple-servers-with-ssh/)委派到另一个环境（例如，AWS）。这种类型的设置为开发人员提供了对敏感数据的安全性和控制，同时仍然允许灵活、可扩展的 CI/CD 操作——所有这些都通过内部开发者门户进行协调。这样，开发人员可以留在他们熟悉的工具中，但可以从统一的可观测性中受益。

**4. 建立强大的治理和监督**

工程领导者必须保持对其开发门户的权威，以确保正确使用并最大限度地降低风险。这需要实施治理策略，以维护最佳实践并保护整个 SDLC 的安全性。

为了维护治理，您的组织应整合身份和访问管理 (IAM)，以根据角色限制对功能的访问，确保只有授权的开发人员才能使用特定功能。此外，定义一个强大的[安全策略来保护敏感数据](https://thenewstack.io/llm-integration-pitfalls-protecting-sensitive-data-in-the-ai-age/)并遵守 GDPR 等法规，使组织保持稳固的基础。

**5. 使用专门构建的解决方案进行简化**

或者，选择像 Harness 这样现成的企业级平台可以简化流程。通过绕过从头开始构建 IDP 的需要，开发人员可以专注于编写和运行软件。

对于我们的一位客户来说，与我们合作的决定是基于战略一致性。该团队正在寻找一个以平台为中心的[方法，该方法可以统一 CI/CD](https://thenewstack.io/ai-generated-code-requires-a-trust-and-verify-approach/)、改进治理并增强开发人员体验。我们的产品满足了这些要求，使组织能够在减少人工工作和入职时间的同时扩展标准化。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)