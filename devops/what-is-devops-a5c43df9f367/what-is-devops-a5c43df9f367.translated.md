## DevOps 是什么？
## 系统工程师的历程和观点
[Florian Olivo](https://unsplash.com/@florianolv?utm_source=medium&utm_medium=referral)在 [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral) **引言**
DevOps 是什么？这是我在进入特定 IT 领域并真正理解答案之前一直问自己的一个问题。

我记得在澳大利亚墨尔本参加 VMware 用户大会时的情景。我与许多其他 VMware 爱好者同处一室，渴望更多地了解 VMware 及其赞助商一直在开发的一些令人兴奋的产品。当时进行演示的那位先生有一个非常吸引人的名字，让我忍俊不禁：KevOps。

作为当时的系统工程师，我将 DevOps 视为下一个前沿。从高层次上来说，我知道它与代码有关，而我在这方面很差。但它的本质让我望而生畏，坦率地说，让我感到害怕。我最初的理解是，你需要成为一名优秀的开发人员，拥有丰富的编码经验。这是我所不擅长的，我从未想过有可能弥补这一差距。但随着我深入了解，我发现的越多。最终，正如我将解释的那样，我发现自己正在从事那项似乎是不可逾越的高山的工作。

**DevOps 的简史**

在我们了解 DevOps 是什么之前，让我们先回顾一下一个问题陈述。

对于非 IT 读者：

* 运维：构建应用程序运行的服务器，例如网站。
* 开发人员：构建在这些服务器上运行的应用程序。

大约是 2007 年，整个行业中开发和运维团队的协作方式出现了问题。他们通常彼此孤立，并且对下一个里程碑的目标不一致。由于运维人员有许多竞争优先事项来照顾服务器群，因此开发人员无法及时部署。在这个模型中，没有人“获胜”。

这就是 DevOps 一词的由来，我们开始对这场运动产生兴趣，在我看来，这场运动已经彻底改变了 IT 行业的部分领域，这些领域需要对一个相当大的问题进行急需的解决。

**那么，** *DevOps 是什么？*is*DevOps?

首先，DevOps 无法用一个句子或陈述来描述。事实上，它是一个包含多个元素或方面的概念。你所看到的定义取决于你所使用的视角。

DevOps 可以描述为：

* 一种文化
* 一个框架
* 一种技术方法
* 一种工程师

根据你的观点和专业知识，每个要点都有一个定义。这类似于敏捷或 ITIL 等其他概念，其中你对这些主题的理解实际上归结为你的角色和职责，以及这些框架如何融入其中。

就像一所房子，DevOps 在进行结构和收尾工作之前，会建立在坚实的基础之上。下图有助于说明 DevOps 如何从文化层面开始，并构建为生动鲜活的技术：

**DevOps 作为一种文化**

由于生成式人工智能目前是一个热门话题，我们大多数人都会熟悉大型语言模型 (LLM)，例如 ChatGPT 或 Gemini。如果你问 ChatGPT DevOps 是什么，你将得到大致如下答复：

“DevOps”是一种协作式的软件开发和 IT 运维方法，旨在提高交付软件产品和服务的的速度、效率和质量。它强调打破开发和运维团队之间的孤岛，培养协作、自动化和持续改进的文化。

这个定义是总结 DevOps 文化方面的完美方式。它的目标是打破开发和运维团队之间的障碍，并将他们推到一起，以实现互利共赢的关系。

DevOps 作为一种文化所追求的一些准则是：

* 我们摒弃手动和繁琐的任务。
* 我们促进自动化，进而有助于提高效率和敏捷性。
* 我们使用可重复的模式来保持一致性。
* 我们促进协作以增强能力和熟练程度。
* 我们以简单而非复杂的眼光学习和适应新挑战。

让我们看看遵循 DevOps 模型和**不**遵循 DevOps 模型的文化的一些示例。

## 遵循 DevOps 模型

*运维团队：*

* 手动执行任务，例如安装软件更新。
* 重复性工作不会自动化。
* 手动处理新基础设施的请求。
* 手动部署开发人员为专有应用程序编写的代码。
* 在每月周期内完成活动存在竞争优先事项。
* 任务不遵循线性流程，并且容易出现人为错误。

*开发团队：*
## DevOps：文化、框架和技术方法

### DevOps 作为文化

- 由于严重依赖运营团队，导致专有应用程序的部署出现重大延迟。
- 无法及时测试某些部署。
- 不了解基础设施，或者即使了解，也无法访问基础设施。
- 运营团队提供反馈的循环繁琐且笨拙，无法突出显示部署问题。

为了真正理解 DevOps 解决的问题，我们需要了解一个糟糕的环境是什么样的。别误会我的意思，这种情况今天仍然存在，实施 DevOps 无法解决所有问题。然而，在上述示例中，它将极大地帮助缩短时间线并提高交付速度。

**遵循** DevOps 模型 *DevOps 团队：*

- 具备跨基础设施、代码、自动化和构建技术的技能组合。
- 审查问题并找出最佳解决方法，然后使用自动化一次性解决问题，然后依靠该自动化在未来进行自我修复和纠正。
- 遵循严格的流程，使用基于模式的方法将更改引入环境。
- 使用尽可能少的手动任务。
- 更改很小且是增量的。
- 反馈循环很牢固，有助于建立与团队成员的融洽关系。

当我们将这两个示例并排放置时，改进是显而易见的。只有当你接触到这种思维方式时，你才能真正欣赏 DevOps 可以提供什么以及你可以从使用它中获得什么。

对于我们的非 DevOps 示例，主要关键字应该是明确的；手动。DevOps 的本质是尽可能多地实现自动化。但是，需要牢记的一点是，你
*不能* 自动化所有内容。DevOps 是一段旅程。这意味着你必须明确划分适合 DevOps 方法的环境和**不**适合 DevOps 方法的环境。

对于向 DevOps 过渡，我们
*必须* 正确处理的第一个要素是文化。我们需要接受它并全心全意地拥抱它。没有文化，我们就无法团结一致，也无法找到共同的基础。DevOps 是关于协作和理解，成功的不是个人，而是团队。你以前听说过这样一句话“一条链条的强度取决于它最薄弱的环节”。这句话充分说明了 DevOps 的含义及其方法论向我们展示的内容。

在达成文化共识后，其余部分就会很容易地到位，因为已经制定了基本规则。

### DevOps 作为框架

当我们将 DevOps 视为一个框架时，我们更多地考虑工作方式。这包括：

- DevOps 对我们的团队意味着什么？
- 需要理解的 DevOps 的子概念是什么？
- 我们如何确保团队中的每个人都为成功做好准备？

这些是我们问自己的众多问题中的几个示例。该框架使我们能够定义实现成功的途径，并提供切实的好处，带来有形的成果。

让我们快速列出 DevOps 的每一侧的专业领域：

对于非 IT 读者：很抱歉地说，这只是我们在 IT 中使用的一些技术术语和概念。我建议研究你不理解并有兴趣了解更多信息的主题。

这是 DevOps 框架中一些关键概念的另一个示例。还有其他概念，但这里的目的是简单说明主要概念。就像在我们的 DevOps 作为文化部分中一样，你可能会开始识别一些互惠互利的专业领域。

从本质上讲，DevOps 作为框架旨在汇集这些不同的专业领域，以部署、管理和维护你的基础设施解决方案和应用程序。它通过以下方式实现此目的：

- 结合 SCM 和 CI/CD 流程来构建和部署基于基础设施的解决方案。这通常称为 GitOps 模型。
- 自动化定期重复的手动任务。
- 利用无状态架构的概念，该架构具有容错能力，并且可以根据需求进行扩展。
- 创建对应用程序中的更改做出反应的事件驱动架构。
- 重用众所周知的模式以提高敏捷性和交付速度。

### DevOps 作为一种技术方法

在我们深入了解 DevOps 的更多技术细节和技术元素之前，我想回到我亲身经历的一个真实场景。

对于非 IT 读者：

- Windows — 我相信大多数人都熟悉笔记本电脑/PC 上的 Windows。还有可用于构建应用程序的服务器版本。
- VMware — 这是一个虚拟化平台，允许你在数据中心中的单个物理服务器上运行多个虚拟服务器。
- SCCM — Windows 服务器的一个特定产品，用于安装应用程序和操作系统更新（补丁）

回想一下 2017 年的一个特定环境，我记得执行的手动任务类似于 DevOps 中作为文化部分中提到的任务，该任务
**不遵循 DevOps 模型**

环境以 Windows 为主，并使用 VMware 作为其虚拟环境。服务器使用 SCCM 手动修补。此过程包括：

- 运营团队的每个成员从列表中获取少量服务器
- 使用管理访问权限登录到这些服务器
- 启动 SCCM 客户端
- 安装更新
- 执行重新启动

这是一个繁琐的过程，特别是考虑到有几台服务器必须以这种方式修补。最糟糕的是什么？这是每月都会发生的事情。

此示例有助于说明在运营方面 DevOps 出现之前的生活是什么样的。这也是为了维护环境和“保持灯亮”而定期需要执行的众多任务之一，正如俗话所说。当您意识到 DevOps 可以提供什么时，定期执行手动任务会感觉像是在浪费大量精力，而投资回报率却很低。

**关于 DevOps 作为一种技术方法**

我们现在开始深入了解用于执行各种操作和任务的实际工具。

以下是您可能熟悉的一些概念和一些相应应用程序的列表：

**对于非 IT 读者：**更多技术术语和概念！随时进行自己的研究。

这只是为了说明目的而进行的另一个抽样。

通过使用这些工具的组合来运行我们的环境，我们可以构建与平台相关的（在大规模环境中支持平台）或特定于应用程序的解决方案。此图表显示了我们如何将这些概念和应用程序应用到实际场景中：

**要点 1 — 代码存储在 GitHub 中**

这确保我们可以：

- 妥善维护整个团队将使用的可靠事实来源。
- 创建代码库版本，以便将分阶段且受控的部署部署到各种环境中，例如开发 > 测试 > 生产。
- 通过接受同行审查和审批流程，审查并批准提议引入代码库的更改。
- 与 Buildkite 集成以进行自动部署。

**要点 2 — 将 Terraform 用于 IaC**

Terraform 用于在 AWS 上创建/替换/更新/删除 (CRUD) 资源。通过将 Terraform 与 Github 和 Buildkite 结合使用，我们正在使用所谓的 GitOps 模型，该模型可以代表我们执行部署。它还确保：

- 使用一致且简化的方式部署资源。
- 此过程没有偏差，因为只有 Buildkite 被授予使用 Terraform 执行部署的权限。
- 可以反复重用代码以推广“不要重复自己 (DRY)”模型，您只需要增强功能，而无需每次都从头开始。

**要点 3 — 将 Buildkite 用于 CI/CD**

Buildkite 用作 CI/CD 平台来执行验证、规划和部署。Buildkite 将使用 GitHub 作为其来源，以确保我们保持一致性。

**要点 4 — 部署前验证代码（CI/CD 的 CI）**

在任何部署之前运行验证和规划管道，以便我们知道会发生什么。

您还可以选择增强此步骤并在开发环境中执行模拟部署。这可以进一步突出不可预见的问题，并导致您重新考虑自己的方法并进行调整。

**要点 5 — 拉取请求同行评审**

一旦收集到足够的证据，我们就可以要求同事审查我们的拉取请求，如果一切正常，则继续合并。

协作至上，正如在 DevOps 的文化方面提到的，根据同事的想法，总有更多的东西可以学习和调整。

**要点 6 — 拉取请求合并和部署（CI/CD 的 CD 部分）**

一旦拉取请求获得批准并合并，自动化将接管，并且资源将被部署。

通过利用此 GitOps 模型，沿途的每一步都受到控制，并且应该有相对预见的操作。它可以反复使用，以持续将更改引入您的环境。

DevOps 的全部意义在于通过您拥有的工具找到让生活更轻松的方法。

## DevOps 作为一种工程师

随着前几层的舒适就位，我们发现自己处于 DevOps 房屋的顶点；工程。对于 DevOps 工程师来说，较低层为我们提供了坚实的基础，使我们能够提笔写字，并完成整个模型。

但以一种相当违反直觉的方式，被贴上 DevOps 工程师的标签并不是业界整齐划一的事情。例如，将 DevOps 模型应用于内部部署环境没有问题。概述的大多数概念工具都有内部部署等效项。即使没有，您仍然可以使用基于软件即服务 (SaaS) 的产品在内部部署设置中执行部署。
## DevOps：定义、工具和挑战

**引言**

DevOps 通常被认为仅适用于公有云，但事实并非如此。虽然 DevOps 模型可以轻松应用于公有云，但仍有一些边缘案例场景，您可以在其中将其应用于本地环境。这使得很难将某人定义为 DevOps 工程师。

**技术方法**

在技术方法部分，我们涵盖了 IaC 和 CI/CD 等概念。基于这些概念构建的工具将以不同的形式出现在整个行业中。这是因为使用这些概念作为基础的工具数量（在某些意义上）是巨大的。例如：

* 在公司 A 中，作为一名 DevOps 工程师，您可能会使用 GitHub（SCM）、GitHub Actions（CI/CD）和 Terraform（IaC）等工具。
* 但作为公司 B 中的 DevOps 工程师，您可能会使用 BitBucket（SCM）、Bamboo（CI/CD）和 CloudFormation（适用于 AWS 的 IaC）。

所说明的重点是，工程层面的 DevOps 在整个行业中没有一致性。就我个人而言，我现在已经使用 DevOps 模型在多个环境中工作过，并且没有一个环境使用完全相同的工具。虽然有很多相似之处，但它们并不完全相同。

另一个很好的例子是将 DevOps 模型应用于公有云空间时。虽然它们都具有相似的概念，但它们在所使用的术语以及如何将这些概念应用于实际操作方面仍然存在差异。

**定义 DevOps 工程师**

这使得很难将某人定义为 DevOps 工程师。现实情况下，当您看到 DevOps 工程师的职位时，它将针对该特定公司和该特定环境。有人可能会争辩说，当您开始讨论多云和多种不同的技术堆栈时，平台工程师可能会进入等式。尽管如此，DevOps 工程师这个术语将继续存在，并且假设它会带来一定程度的歧义。

**结论**

我希望现在在阅读完本文后，您对以下这个非常复杂的问题有一些见解：

* 什么是 DevOps？

DevOps 的妙处在于它有许多不同的兔子洞可供探索，并且将来会继续发生变化。许多组织仍在努力实现其最终版本的 DevOps，这为渴望动手并实施一些复杂解决方案的工程师提供了大量机会。

DevOps 是一种高级模型，不容易理解。我告诉那些我提供建议或指导的人，作为一名 DevOps 工程师，您不需要完全理解所有内容。相反，您需要能够相对快速地找到答案，并开始将您的 DevOps 逻辑应用于这种情况。鉴于 DevOps 的本质以及两个主要 IT 领域的融合，需要多年的奉献和持续的技能提升才能磨练一个人的能力和潜力。

如果您正在探索 DevOps 或只是好奇，最好的学习方法就是动手实践。技术方法部分涵盖了一些您可以使用的出色应用程序。其中一些甚至可以在个人环境中免费使用，让您能够试验和练习自己的实验室和设置。

感谢您的阅读！如果您觉得此内容有吸引力，请告诉我，以便我继续创建此类内容。