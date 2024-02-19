<!--
title:  AI时代的软件交付难题
cover: https://cdn.thenewstack.io/media/2024/01/755a4c47-ai-generated-8252068_1280-1024x682.jpg
-->

尽管潜力巨大，人工智能的发展面临着一个重大挑战：将其实际应用到产品中。

> 译自 [The Future Is AI, but AI Has a Software Delivery Problem](https://thenewstack.io/the-future-is-ai-but-ai-has-a-software-delivery-problem/)，作者 Jim Rose 是 CircleCI 的首席执行官，该公司是全球最优秀的工程团队使用的持续集成和交付平台。Jim 通过收购 Distiller 公司加入了 CircleCI，Distiller 是一家专注于 iOS 的持续集成服务公司。他是 Distiller 的联合创始人和首席执行官...。

在变革性技术史上，几乎没有什么能比得上[人工智能](https://thenewstack.io/ai-for-developers-how-can-programmers-use-artificial-intelligence/)（AI）的颠覆潜力。就像互联网和移动技术的兴起一样，AI已经被证明是创新的下一个前沿。

然而，尽管潜力巨大，但AI的发展面临着重大挑战：如何将其真正应用到产品中。

回想一下互联网的黎明时期——那是一个充满了被过度吹捧的承诺，但却为那些能够利用这项新技术的人带来了改变游戏规则的现实。如今，工程团队正面临着类似的抉择，他们需要在AI的压力下对抗着从何处开始的不确定性。

通过阅读 Sequoia Capital 的文章《[生成式AI的第二幕](https://www.sequoiacap.com/article/generative-ai-act-two/)》，读者们可能会得出结论，即 GenAI 的下一章即将到来。2023年上半年，第一幕是一场从零开始构建基础模型的竞赛，而第二幕则是关于如何将现有模型整合到更全面的解决方案中。

但第二幕之后呢？随着越来越多的开发者开始熟悉构建以AI为动力的软件，第三幕将引发一场新的竞赛：能够大规模构建、部署和管理以AI为动力的软件的能力，这需要在前所未有的水平上进行持续监控和验证。

这就是为什么关键的 DevOps 实践，如持续集成和[持续交付](https://thenewstack.io/a-primer-continuous-integration-and-continuous-delivery-ci-cd/)（CI/CD），将在提供强大框架方面发挥核心作用，帮助工程领导者应对交付以AI为动力的软件的复杂性，从而将这些技术挑战转化为创新和竞争优势的机会。

## 从是/否到无限灰：AI的测试迷宫

就像软件团队已经完善了在规模上安全快速地将可靠、可观察、可用的应用程序交付给客户的实践一样，以AI为动力的软件再次在演变这些方法。我们正在经历从我们建立软件开发实践的确定性结果到一个具有概率结果的世界的[范式转变](https://thenewstack.io/how-ai-is-shifting-developer-culture-and-work-at-github/)。

这种复杂性给传统的是/否逻辑带来了困难，而这种逻辑一直是我们测试软件基础的基石，需要开发人员应对各种主观结果。手动测试这种系统变得费时费力，因为它不仅需要验证大量潜在的交互，还需要评估AI所做决策的主观质量。

如今，验证高质量答案的工作通常由专业领域的专家完成，但为了扩展规模，团队将需要寻求与[评估平台无缝集成的](https://thenewstack.io/garden-the-configure-once-kubernetes-platform-for-seamless-dev-prod-integration/) CI/CD 工具来自动化此过程。这凸显了在测试和验证人工智能方面需要创新方法的必要性，借鉴了我们在 CI/CD 方面[学到的一切](https://thenewstack.io/the-machine-learning-building-blocks-developers-require-to-do-mlops/)以及在这个新世界有效安全地向客户交付应用程序所需的条件。

## 利用今天的 CI/CD 流水线来交付AI的第三幕

CI/CD 在帮助团队管理开发人工智能软件的复杂性方面起着至关重要的作用。这些方法论提供了一个结构化的、自动化的流水线，涵盖了从构建和测试到训练和部署AI应用程序的各个环节。

将其视为增强的交付，确保计算资源既可扩展又高效。自动化测试和快速反馈循环可以快速识别问题，[降低](https://thenewstack.io/mitigate-risk-beyond-the-supply-chain-with-runtime-monitoring/)了模型漂移等与AI相关的挑战的风险。

CI/CD 增强了团队协作，加快了开发时间表，并通过[流程自动化提高了以人工智能为动力的软件质量](https://thenewstack.io/3-steps-for-automating-software-release-management/)。这种自动化最小化了手动错误，增强了可重现性，使团队能够[迅速自信地交付可靠的人工智能驱动的应用程序](https://thenewstack.io/3-must-have-modernization-competencies-for-application-teams/)。通过将[AI软件开发与自动化测试](https://thenewstack.io/no-time-for-test-automation/)和持续部署相结合，CI/CD 流水线促进了一个无缝的工作流，其中任何变更都在持续地构建、训练、测试、部署和监控。

该系统充当着一个质量门卫的角色，确保只有符合严格标准的AI应用程序才能投入生产。此外，如果由于模型漂移导致性能下降，流水线可以安全地回滚、重新训练和重新部署更新后的AI应用程序，确保部署的AI/ML应用程序随着时间的推移保持强大和功能齐全。

## 将AI和ML项目与业务目标对齐

在投资于以AI为动力的软件时，战略业务对齐至关重要，远远超出了工程团队的视野。这需要一种协同的努力，各部门的利益相关者 —— 如产品管理、营销、销售和客户服务 —— 齐心协力，定义AI可以实现的明确目标。

关键在于确保AI倡议与核心业务目标紧密联系，例如增强客户体验、简化运营或开启新的收入来源。这种跨职能的对齐确保了AI项目在技术上可行且具有商业战略性，最大限度地提高了投资回报率，并确保技术服务于更广泛的业务目标，而不是孤立存在。

## 加速您基于AI的创新，赢得明天的市场

未来确实可能属于AI，但实现其全部潜力取决于我们解决软件交付难题的能力。这需要战略业务对齐、技术准备以及正确的工具和流程的结合。

通过将人工智能与强大的 CI/CD 实践相结合，工程领导者可以应对交付以 AI 为动力的软件的复杂性，将潜力转化为业绩，将愿景变为现实。随着 AI 重塑着景观，愿意演变和适应软件交付实践的准备将会把先驱者与其他人区分开来，在不断发展的技术竞技场上确保竞争优势。
