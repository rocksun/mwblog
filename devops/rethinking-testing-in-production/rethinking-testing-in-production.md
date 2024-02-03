<!--
title: 在生产环境中重新思考测试
cover: https://cdn.thenewstack.io/media/2024/01/213bc145-leaf-8483401_1280-1024x682.jpg
-->

在生产环境中进行测试长期以来一直被认为是一项风险较大的尝试，经常在开发人员、测试人员和利益相关者之间引起争议。

> 译自 [Rethinking Testing in Production](https://thenewstack.io/rethinking-testing-in-production/)，作者 Ben Rometsch。

测试生产环境一直被认为是一项风险较大的尝试，通常在开发人员、测试人员和利益相关者之间存在争议。在部署到生产环境之前，在开发和暂存等受控环境中精细地测试软件的传统方法一直是常态。

[在实时的生产环境中进行测试](https://thenewstack.io/how-to-set-up-a-secure-test-environment-with-an-offsite-team/)的想法本身由于潜在的中断、不可预见的错误和损害用户体验的担忧而获得了不好的名声。然而，在软件开发中，这种传统观念正受到一种不同方法的日益挑战: 使用[功能标志](https://martinfowler.com/bliki/FeatureFlag.html)策略性地在生产中进行测试。

## 生产环境总是不同的

使用标志在生产中测试并不一定意味着放弃其他测试环境。

相反，它认识到维护相同的开发、暂存和生产环境的固有挑战。生产环境的快速增长和不断发展的本质 - 由用户交互和增加的数量推动 - 使准确地镜像这些环境变得几乎不可能，在经济上也不可行。

随着产品变得越来越互联，准确地在生产环境之外复制第三方 API 和集成几乎是不可能的。

[基于主线的开发](https://trunkbaseddevelopment.com/)，其重点是持续集成和交付，承认需要一个范式转变。功能标志作为这一转型中的传说中的阿基米德杠杆，提供了一种灵活且可控的在生产中测试方法。

开发人员现在可以逐步推出功能，而不会影响整个用户群，减轻与传统测试方法相关的风险。

功能[标志使开发人员能够](https://thenewstack.io/feature-flagging-and-logging-the-perfect-combination-for-developers/)在开发阶段的生产环境中为自己启用某个功能，使他们能够在向更广泛的测试受众公开之前对其进行精致地完善和完美化。

这种渐进式方法可以确保潜在问题能够在开发过程的早期就被识别和解决。随着功能的成熟，它可以为测试团队、工程组或特定用户细分市场选择性地启用，以促进每一步的彻底验证。

维护相同环境的后勤噩梦得到缓解，因为在[生产中测试成为开发工作流程的组成部分](https://thenewstack.io/achieving-production-parity-and-local-development-workflows-on-cloud-foundry-with-kubernetes/)。

此外，引入功能标志为在生产中进行 A/B 测试铺平了道路，通过比较不同功能变体在真实环境中的表现，实现基于数据的决策。

## 使用功能标志增强开发

使用 [Flagsmith](https://www.flagsmith.com/?utm_source=newstack&utm_medium=content&utm_campaign=testinginproduction&utm_id=thirdparty) 等功能标志工具，用户(标识)、细分市场(组)和标志的结构化层次为精心编排的功能发布奠定了基础。这种[故意的序列](https://docs.flagsmith.com/basic-features/managing-segments%23feature-flag-and-remote-config-precedence)允许您在不同级别覆盖功能。按优先顺序，这些是:

- 标识覆盖(用户)
- 细分市场覆盖(用户组)
- 环境默认设置(默认)

这种方法允许您拥有受控的发布流程，例如:

- 开发人员将功能包装在功能标志中，以便可以打开/关闭它。
- 然后，开发人员通过仅为自己启用功能来在生产中测试该功能(通过标识覆盖)。
- [开发人员通过为内部团队启用该功能来再次测试](https://thenewstack.io/how-to-enable-developer-teams-to-improve-container-security/)，而不影响任何用户(通过细分覆盖)。
- 该功能将逐步推出给越来越大的受众，直到到达所有用户，或者进行一些 A/B 测试来确定哪个功能版本应该是最终版本(通过环境默认设置)。

![缩放](https://cdn.thenewstack.io/media/2024/01/6227e2b9-wrapitinaflag.png)

如果您具有适当的工具，那么曾经受到谴责的在生产中测试的概念就不再合理。功能标志不仅与生产环境的动态特性保持一致，而且还可以显著增强开发过程。

引入它们赋予了开发人员和测试人员以增强的敏捷性迭代和精致地完善功能的能力，并且逐步将其推广到更广泛的受众。这种方法最大限度地减少了潜在的中断，增加了稳定性，并在软件开发快节奏的环境中促进了适应性。

## 为什么使用功能标志在生产中测试

在采用功能标志的同时，还有两个至关重要的要点浮出水面:

1. 功能标志释放了精简环境的潜力，甚至可能采用单环境设置。(如前所述，这是一个选项，而不是一个要求。)这种选择不仅代表了重大的节省成本的措施，而且还[优化了开发资源](https://thenewstack.io/deep-work-a-better-way-to-measure-developer-velocity/)。
2. 在功能标志的保护下，在生产中测试可以进行实验和优化，而不影响最终用户，最终有助于增加系统稳定性。

您应该记住，没有哪个银弹能解决所有问题。不言而喻的是(但是让我们强调一下!)，引入像功能标志这样的新东西意味着您完成了家庭作业，并了解了权衡、新的流程以及您将通过新技术引入的最佳实践。

但这是值得的！我们每天与开发人员交谈，他们可以证明使用上述方法在生产中进行测试的价值。

在生产中测试不是一个新话题，我们鼓励您阅读更多关于这个话题的内容。我们想向在我们之前写过这方面内容的人致敬。您可以在 The New Stack 上阅读其他观点!

- [Two Times Integration Testing in Production Has Gone Wrong](https://thenewstack.io/two-times-integration-testing-in-production-has-gone-wrong/)
- [Embracing Testing in Production](https://thenewstack.io/embracing-testing-in-production/)
- [Chaos Engineering Progressively Moves to Production](https://thenewstack.io/chaos-engineering-progressively-moves-to-production/)
- [Testing in Production: Will You Get Eaten Alive?](https://thenewstack.io/testing-in-production-will-you-get-eaten-alive/)
- [Honeycomb’s Charity Majors: Go Ahead, Test in Production](https://thenewstack.io/honeycombs-charity-majors-go-ahead-test-in-production/)

本文由解决方案架构师 Moreno Garcia 合著，他拥有 10 多年的解决方案架构经验。