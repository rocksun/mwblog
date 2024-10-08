
<!--
title: 好的代码冻结的4个步骤
cover: https://cdn.thenewstack.io/media/2024/08/ae29e662-freeze.jpg
-->

代码冻结期是专注于规划、文档和非部署任务的好时机。

> 译自 [4 Steps to a Good Code Freeze](https://thenewstack.io/4-steps-to-a-good-code-freeze/)，作者 Alex Quintana。

我仍然记得，就好像发生在昨天一样：我的工程经理粉碎了我的梦想。“我们一周内都无法部署。我们因为季度收益而处于代码冻结状态，”她再次告诉我。我计划用来超越 OKR（目标和关键成果）的 A/B 测试无法及时进行。

在季度收益或高峰流量季节等关键时期，代码冻结的概念在工程生态系统中是一种常见做法。实施代码冻结是为了防止在正常运行时间至关重要时发生事故并确保产品稳定性。但是，对于代码冻结是否是高峰时段的有效解决方案，以及开发团队是否仍然认为它们有用，目前还没有定论。

## 什么是代码冻结？

代码冻结是指 [软件开发团队](https://thenewstack.io/managing-software-development-team-dynamics-from-within/) 停止将新代码更改部署到生产环境的一段时间。这种做法有助于在业务的关键时期（例如高峰流量（例如零售业的黑色星期五）或重大事件（票务网站发布泰勒·斯威夫特的门票））确保系统稳定性。目标是 [最大程度地降低引入新错误](https://thenewstack.io/progressive-delivery-accelerate-app-releases-while-minimizing-bugs/) 或可能中断服务的风险。

在代码冻结期间，开发工作将仅限于部署到暂存环境，或者将限制为本地功能分支。这允许开发团队在仍然能够合并的情况下保持势头，只是不能合并到生产环境中。此外，代码冻结是专注于计划、文档和不可部署任务的好时机。有效的沟通和准备对于管理代码冻结之前、期间和之后的流程至关重要，确保平稳过渡并保持系统可靠性。

以下是帮助确保成功进行代码冻结的四个步骤：

## 1. 沟通是关键

围绕任何代码部署（以及任何代码冻结）要采取的第一步是有效沟通。不要像我得知我们的 A/B 测试无法发布时那样，让你的产品团队措手不及。这不仅仅是关于正在部署的代码或被冻结的部署，而是关于管理整个组织的期望。更改应该在内部传达，突出显示潜在的面向客户的影响，并与相关团队协调任何响应。

例如：

* **错误修复**：错误修复可能会解决某些用户的问题，但也可能会破坏其他团队或服务使用的解决方法。传达这些更改有助于团队有效地做好准备。
* **前端更新**：如果传达不当，小型部署（例如重新排序菜单选项）可能会造成混乱。这可能会导致支持请求和票证的涌入，给支持团队带来不必要的负担。
* **内部工具调整**：对内部工具的请求速率的更改可能会触发警报，从而导致混乱并给待命人员带来额外的工作。清晰的沟通可确保每个人都了解这些更改的背景，并可以做出适当的反应。

在内部可见的共享仪表板中传达更改可确保从工程师到支持人员的每个人都知道正在部署的内容、其目的及其潜在影响。这种整体方法有助于管理期望并在关键时期减少摩擦。

## 2. 实施冻结前后管理部署的策略

部署冻结之前的时期通常会出现急于进行更改的情况，而之后的时期则可能类似于交通堵塞。无论是否进行正式冻结，都会发生这种情况。为了有效地管理这些时期：

* **冻结前冲刺**：有一种趋势是在冻结之前尽可能多地推送更改。这可能会导致仓促的决定和测试不足，从而增加发生事故的风险。重要的是确定关键更新的优先级，并确保在任何代码冻结之前对其进行彻底测试，以避免不必要的事故。
* **冻结后交通堵塞**：冻结后，Backlog 的更改可能会使系统以及开发团队不堪重负。此期间需要仔细协调以错开部署并密切监控其影响。

交错的休假时间表可能会产生类似的问题。通过识别和规划这些模式，组织可以更好地管理工作流程并保持稳定性。

## 3. 将冻结期用于非部署工作

即使部署冻结被用来阻止工程师负担过多，但这并不意味着开发团队什么都不应该做。这段时间可用于执行不需要立即部署的任务，例如：

* **规划和协调**：制定详细的计划并协调即将进行的项目。此项准备工作可以简化未来的部署并提高整体效率。
* **工具开发**：专注于构建和增强内部工具（例如支持流程和提高生产率的内部开发者平台）。
* **文档和培训**：更新文档并提供培训课程以提升团队成员的技能。这确保每个人都已为未来的挑战和变化做好准备。

这种方法有助于在不影响系统稳定性的情况下维持生产力，并确保即使部署已暂停，团队仍可继续提供价值。

## 4. 进行冻结后审查

冻结期结束后，对所采取的方法进行审查至关重要。这包括：

*   **收集反馈**: 与值班工程师、支持人员、流程组织者甚至客户交流他们的体验。了解他们的观点有助于确定痛点和需要改进的领域。
*   **评估有效性**: 评估哪些方面做得好，哪些方面做得不好。冻结期间是否发生过任何事件？它们是如何处理的？哪些方面可以做得更好？
*   **实施变更**: 根据反馈和评估，引入变更，使流程更加顺畅，并在下一个关键时期更加有效。

这种持续改进循环确保组织从每次经验中学习，并随着时间的推移改进其方法。

## 为事件做好准备

无论是否进行部署冻结，事件都会发生。做好准备是有效管理事件的关键：

* **制定事件备忘单**: 准备一份包含值班时间表、事件处理流程和备份计划的综合指南。这确保每个人都知道在发生事件时该做什么以及联系谁。
* **实施培训和演练**: 定期进行培训和事件响应演练。这有助于团队保持敏锐，并为实际事件做好准备。
* **建立支持系统**: 确保建立了强大的支持系统。这包括拥有足够的资源和工具来有效管理事件并减少停机时间。

请记住，[事件提供了宝贵的学习机会](https://thenewstack.io/3-strategies-to-turn-incidents-into-learning-opportunities/)。它们促进了团队合作，提高了解决问题的能力，并带来了更好的系统和流程。通过做好充分的准备，组织可以将事件转化为成长和改进的机会。

通过采取上述每个步骤，组织可以顺利度过关键时期，并在 [业务需求](https://thenewstack.io/5-signs-your-business-needs-an-operations-intervention/) 与员工福祉之间取得平衡。
