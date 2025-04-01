<!--
title: 为什么Copilot路径是软件测试的一个有缺陷的策略
cover: https://cdn.thenewstack.io/media/2025/03/1bc7eb25-christopher-gower-m_hrflhgabo-unsplash-1-scaled.jpg
summary: AI驱动的软件测试并非万能药！Copilot式AI助手虽能加速测试创建，但难解测试维护难题。需利用NLP等AI技术，实现动态上下文理解和实时验证，摆脱对脚本和对象定位器的依赖，实现测试的“Democratization”，解放测试人员，关注更有价值的工作，解决软件测试的根本问题。
-->

AI驱动的软件测试并非万能药！Copilot式AI助手虽能加速测试创建，但难解测试维护难题。需利用NLP等AI技术，实现动态上下文理解和实时验证，摆脱对脚本和对象定位器的依赖，实现测试的“Democratization”，解放测试人员，关注更有价值的工作，解决软件测试的根本问题。

> 译自：[Why the Copilot Route Is a Flawed Strategy for Software Testing](https://thenewstack.io/why-the-copilot-route-is-a-flawed-strategy-for-software-testing/)
> 
> 作者：Stephen Feloney

我花了超过 25 年的时间开发软件测试产品并将其推向市场。在此期间，我们见证了重大变化——自动化测试、持续测试、低代码/无代码平台、卓越中心和左移方法。然而，尽管取得了这些进步，但有一件事始终不变：测试仍然是软件开发生命周期中耗时、低效的[瓶颈](https://thenewstack.io/how-to-find-and-solve-engineering-bottlenecks/)。

虽然多年来测试的瓶颈效应有所减弱，但我们从未真正实现无缝验证。如今，人工智能处于我们测试产品发展的最前沿（与其他许多供应商一样），但关键问题仍然存在：它会使测试更有效率吗？那么人的因素呢？人工智能会减少单调的任务，还是会像过去的“进步”一样，只是增加另一层复杂性？

## 下一代自动化测试

许多供应商已经开始将人工智能融入其测试平台。许多人选择使用 AI 助手来辅助测试创建，但这只是解决方案的一部分。随着人工智能的快速发展，我们必须超越助手，专注于更有意义的准确性、效率和速度的提升。

虽然助手可以加速测试创建，但它们并不能[解决测试的一些更重大的挑战](https://thenewstack.io/solving-3-pervasive-enterprise-continuous-testing-challenges/)。用户的反馈褒贬不一。一些开发人员觉得助手很有帮助，但许多人报告说，它们有时会生成不正确的测试，或者创建更多需要持续维护的测试。助手非但没有解决核心问题，反而有加剧这些问题的风险，只是在已经崩溃的流程上叠加了人工智能。

## 为什么测试仍然存在问题

为了理解原因，让我们看看自动化软件测试的演变。该行业已经开发了各种技术来识别屏幕上的对象，从而使[测试能够运行](https://thenewstack.io/why-shift-testing-left-part-2-qa-does-more-after-devs-run-tests/)。虽然有些方法比其他方法更好，但事实仍然是，UI 或应用程序的更改会破坏测试，从而需要持续维护——估计占测试人员时间的 30-40%。

以回归测试为例：每当进行更改时，都必须重新运行回归套件以检测新问题。在大型应用程序中，这些测试可能有数千个，但据估计，回归套件中只有 20% 的测试是有效的。许多这些测试会产生错误，需要耗时的分析来验证其真实性。难怪一些企业仍然依赖手动测试，即使他们知道无法实现完整的测试覆盖率。

## 一种新的测试方法

在讨论如何改进 Web、移动和性能测试套件时，人们意识到，虽然[助手可以帮助编写测试](https://thenewstack.io/testing-copilot-and-chatgpt-as-coding-assistants-what-we-found/)脚本，但它们并没有解决用户最主要的痛点：测试维护和分析。这就是为什么最好专注于可以交付价值的领域，从测试验证开始。

我们[需要重新思考如何进行测试](https://thenewstack.io/we-need-a-new-approach-to-testing-microservices/)。是否可以消除对脚本编写和基于对象的定位器的需求？

## 一种更智能的方法

自动化测试的下一个演进不仅仅是可视化屏幕上的内容，而是使用 AI 在上下文中和动态地理解它。通过利用[自然语言处理](https://thenewstack.io/what-temperature-means-in-natural-language-processing-and-ai/)，用户可以提出简单的问题，系统可以相应地分析和验证测试，而无需依赖对象或代码，甚至不需要了解应用程序的底层技术。结果是什么？实时验证，可在任何平台上运行，并且可供技术和非技术团队成员使用。它还可以在不进行人工干预的情况下，在代码发生大规模[更改](https://thenewstack.io/root-out-vulnerabilities-in-github-as-you-merge-code-changes/)后继续有效。
虽然 AI 驱动的测试验证带来的直接好处显而易见，但真正的价值来自于实践经验和真实用户的反馈。例如，金融机构已经使用这种方法来验证他们以前无法验证的数据，例如检查屏幕上的图表是否与底层表格匹配。零售商现在可以确保产品描述与产品图像匹配。这种 AI 驱动的验证可以无缝工作，即使应用程序不断发展，也无需手动调整。

## 超越验证

但测试验证仅仅是个开始。要真正改变测试，我们[必须关注 AI 如何将测试人员和开发人员从日常任务中解放出来](https://thenewstack.io/data-dignity-developers-must-solve-the-ai-attribution-problem/)，使他们能够专注于更有价值的工作。 目标是[普及测试——使其对每个人都可访问](https://thenewstack.io/breaking-barriers-democratizing-access-to-vector-databases/)且高效。 我不太喜欢“普及”这个词，但如果使用得当，这确实是 AI 将实现的目标。

软件测试的未来不是为了应用 AI 而应用 AI，也不是为了采用短期修复方案。 而是要利用计算领域最重大的进步来解决现实世界的问题，并最终修复多年来困扰软件测试的那些有缺陷的流程。