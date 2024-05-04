
<!--
title: 大机平台工程：设计思维推动变革
cover: https://cdn.thenewstack.io/media/2024/05/8cdcfe3d-project-impala-2.jpg
-->

法律与通用工程师带我们了解 Project Impala，这是一项旨在改变大型机开发人员体验以更快地交付更高质量的努力。

> 译自 [Platform Engineering for a Mainframe: Design Thinking Drives Change](https://thenewstack.io/platform-engineering-for-a-mainframe-design-thinking-drives-change/)，作者 Jennifer Riggins。

我们经常谈论 [在云原生复杂性面前的开发者体验](https://thenewstack.io/how-the-developer-experience-is-changing-with-cloud-native/)。然而，[71% 的财富 500 强公司](https://planetmainframe.com/2022/12/relevance-of-mainframe/) 仍在使用主机。我们如何实现主机工程师体验的现代化？

主机上的公司在快速增长时期面临不断变化的法规要求。此外， [主机开发人员的平均年龄](https://www.zippia.com/mainframe-systems-programmer-jobs/demographics/) 为 47 岁，这意味着有经验的人员即将退休——下一代需要入职。

Legal & General (L&G) 是全球最大的资产管理公司之一，拥有 1.7 万亿美元的资产和 10,000 名员工。在 4 月下旬的虚拟 [企业技术领导峰会](https://itrevolution.com/etls-eur24/) 上，L&G 的技术领导分享了他们的 [平台工程](https://thenewstack.io/platform-engineering/) 之旅，这使他们能够培养出色的开发者体验，而无需使用主机工具的工程师。

他们主机开发方法的这种转型是针对所有利益相关者的工具和同理心的社会技术融合。它弥合了时间和技术的差距。

### 设计思维实现主机的现代化

虚拟活动中的三位演讲者—— [Tariq Surty](https://www.linkedin.com/in/tariq-surty-8911101/)，零售业 IT 总监，[Jennifer Pickard](https://www.linkedin.com/in/jenniferpickard/)，工程主管，以及 [Bharghava Vamsi Krishna Bhogireddy](https://www.linkedin.com/in/bharghava-vamsi-krishna-bhogireddy-246543b/)，高级运营架构师——在 L&G 的养老金部门工作。2012 年，英国政府要求所有雇主必须提供养老金计划，员工必须选择退出，而不是加入。

由于这一要求，仅 L&G 的养老金部门就从 2012 年的 250,000 人增加到今天的 500 多万客户。英国养老金计划的最新监管变化使 L&G 预计未来几年将持续增长。

![变革案例：持续不断的变革量英国养老金行业的时间表，该行业经历了重大的监管变革。1998 年：个人养老金。2002 年：SERPS 被国家第二养老金计划或 S2P 取代。2004 年：《养老金法案》引入了养老金监管机构和养老金保护基金。2006 年：养老金简化引入。2010 年：国家养老金年龄开始变化。2011 年：三重锁定引入。2012 年：自动入职——可能是英国养老金中最大的举措。2014 年：大规模养老金改革。2015 年：养老金自由的开始。2016 年：引入新的固定费率、单层国家养老金。2018 年：女性国家养老金年龄提高到 65 岁。2019 年：自动入职缴款增加。2020 年：国家养老金年龄提高。2021 年：暂停三重锁定系统。2022 年：国家养老金增加](https://cdn.thenewstack.io/media/2024/05/5712d79a-legal-general-rate-of-change.jpeg)

*此时间表说明了在过去 26 年中英国养老金制度的变革速度和复杂性。*

2021 年，为了应对这种增长规模及其核心养老金管理系统预期的压力，L&G 问道：为什么不将主机现代化，而不是迁移到现代平台？目的是实现安全的系统开发生命周期和三个 3Q：变革的快速、质量和数量。

“为什么不加入 IT 革命，并带来所有 [DevSecOps](https://thenewstack.io/ebooks/devsecops/best-of-devsecops-trends-in-cloud-native-security-practices/) 和现代软件开发实践和工具所提供的优势？”Surty 在演讲中问道。“这样，我们不仅可以推动变革的数量，还可以推动变革的质量和速度。”

他补充说：“我想你们中的大多数人可能太年轻，无法像你们太年轻而无法记住雪佛兰 Impala 一样记住主机技术。但鉴于我们正在使用传统技术，并且希望推动更大的敏捷性、灵活性和速度，”他们将平台工程计划命名为 Project Impala。

许多企业希望通过 [大爆炸式云迁移](https://thenewstack.io/going-from-cobol-to-cloud-native/) 来驯服主机。相反，Legal & General 采用以同理心为导向的 [设计思维](https://blog.container-solutions.com/wtf-is-design-thinking) 方法来尝试了解与主机合作的不同群体及其痛点。

“我们只是认为花时间听取与大型机交互的人员的意见并确保我们倾听这些问题，并且我们必须反复迭代其中一些解决方案和选项非常重要，” Pickard 说。

平台团队运行着一些会话，在这些会话中，他们倾听了不同开发人员组、质量工程师以及任何与大型机交互的人员的意见。她说，大约两个月后，在产生了大量便利贴的想法之后，Project Impala 的领导团队对不同的团队、其工作流和交接有了深刻的理解。

L&G 基于同理心的设计思维方法遵循以下流程：

1. **同理心**：更好地理解人们的需求。
2. **定义**：确定要解决的主要问题。
3. **构思**：讨论可能会有用的解决方案。
4. **实施或原型**：创建要测试的模型。
5. **测试**：分享并获得反馈。

Pickard 指出：“团队发现，在不同的点子中表达自己的问题和担忧非常有效，但同样地，他们也开始结合他们自己的观点，思考如何改善事物以及他们所观察到的问题。”“同样地，当涉及工具和选项时，人们对此知之甚少。”

## 教导大机开发人员了解 DevOps

很明显，大型机开发人员需要了解当代 [DevOps](https://thenewstack.io/devops/) 实践。

L&G 平台团队将主要学习内容归纳为：

- 工具
- 创建高质量数据所需的时间
- 手动步骤和交接的数量
- 环境争用

环境争用，Pickard 表示，这种情况发生在大型产品主机“当月底处理时间达到高峰时”。容量会被分配到生产系统，而较低环境的容量则会变低。在某些情况下，这些系统会极度缓慢并或多或少变得对开发团队不可用。

团队意识到，所有这些问题都不会通过“大爆炸”云迁移来解决。

“我们得小心谨慎，逐步引入这些更改，并了解团队对此的解决办法。”皮卡德表示，“但我们还希望解决下一代问题，并为他们提供工具功能，这意味着他们可以成为下一代继续支持、维护和提升大型机能力的人。”

产生的问题包括：

- 我们如何在大机上获得 CI/CD？
- 我们如何在云端获取大型机？
- 在虚拟化环境中，当只有足够的容量来运行某些工作负载时，我们如何才能解决该工作流程争用？
- 我们如何鼓励平台采用？
- 我们如何鼓励下一代大机工程师？

“我们如何确保它被采用，被使用，人们保持好奇，我们吸引下一代”，皮卡德问道，呼应了所有平台工程计划的开发商重点。

平台团队继续通过展示和讲解会议鼓励与大型机利益相关者进行公开沟通。然后他们招募了一位初级工程师，他“作为一个新视角，对有哪些选择以及哪些是可行的进行了评估，但也意味着他们可以验证一些初始工具”。

Legal & General 还为发现漏洞的团队成员引入了一个小漏洞奖励，作为培养持续反馈而不受指责的文化的一种方式。

## “Leslie”：现代大机开发人员角色

为了始终专注于理想的开发人员角色，L&G 的工程部门与 [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 集思广益，询问生成式 AI 编码助手，了解现代大型机开发人员是什么样子。

它提出了“Leslie”这个角色，她既能用 COBOL 编码，也能用 Python 编码，并且可以在绿色屏幕和 GUI 之间切换。她可以轻松处理数TB的数据，而且是“一个不害怕旧系统的人，而是将它们视为挑战和机遇”。

这种大机工程师角色平衡了旧与新、可靠与创新、安全与敏捷之间的矛盾。而且她可以使用现代云计算、Al 和 DevOps。

那么，平台团队是如何达成那个角色的？通过采用并改编面向大型机的 DevOps 流程。

“从一开始就非常明显，我们必须为大型机开发生命周期采用 CI/CD 流程，”Bhogireddy 说，以便在这项新旧技术中提供统一的开发者体验。

但这还不够。团队必须使用一个测试数据集，该数据集代表了为 500 万客户提供服务的 14 个工程团队。

“除了提供不可变的大型机环境之外，想象一下启动并关闭一个物理大型机，你会像其他所有组织或经受时间考验的传统应用程序或产品一样获得不可变性，”Bhogireddy 补充道。

工程团队不能再依赖于同行的 25 年养老金制度的机构知识。如果他们继续这样做，随着那些对大型机有第一手经验的人退休，他们就会遇到问题。

Bhogireddy 补充说，随着最初的主机开发人员年龄的增长，“关于如何配置这些环境，如何进行这些更改的知识的人员依赖关系”也必须被设计出来。

换句话说：养老金制度工程师的“英雄文化”必须被设计出来。

平台团队检查了开发人员每天花费超过 30 至 40 分钟的任何内容，希望通过将所有内容自动化为代码来消除繁琐的工作。

Bhogireddy 表示，这涉及采用一系列企业工具。然后，将这些工具嵌入到 L&G 的大型机开发生命周期中，“以便我们的 Leslies 可以将链开发并交付到生产环境中，该链在物理大型机上停留的时间不到两周。那就是梦想。那是我们的目标。

”所有测试均应在生产前在虚拟、不可变的大型机上继续进行，该大型机由 PopUp 按需大型机提供，该大型机位于 Microsoft Azure 云环境之上并利用 Delphix 的持续

## 追求统一的开发人员体验

平台团队已经解决了环境和数据问题，但仍然必须想办法提供统一的开发人员体验，从年轻的 Java 开发人员到最资深的主机开发人员，后者不熟悉当代的 [云原生开发](https://thenewstack.io/cloud-native/)。

平台团队克隆了所有代码，包括 GitHub 中的 80,000 个模块，这使他们能够使用非主机集成开发环境来执行应用程序开发。镜像使用 Broadcom 的 [Endevor Bridge for Git](https://techdocs.broadcom.com/us/en/ca-mainframe-software/devops/ca-mainframe-application-tuner/12-0/using/performance-testing-with-ca-mat-in-devops-ci-cd-pipelines/build-performance-testing-ci-cd-pipeline/install-the-pipeline-tools/install-and-configure-ca-endevor-bridge-for-git.html) 创建和维护。

“然后奇迹发生了：当最资深开发人员看到年轻的 Leslies 能取得什么成就时，”Bhogireddy 说。“他们可以看到只需点击一个按钮即可将代码推送到预生产环境，而不是在黑绿屏幕上键入 25 到 30 个命令。”

这是另一个迹象，表明平台团队以同理心为导向的方法来协调 Leslie 的平台体验正在发挥作用。尽管如此，团队仍然必须让每个人都参与到这种新的主机开发人员体验中。

“这不会是一个大爆炸的故事。那是我们希望开发人员达到的最终状态，但有过渡期，”Bhogireddy 说。

“总的来说，Leslies 现在处于不同的过渡状态。每个过渡状态都产生了价值。”

他说，这项工作还没有结束：该平台仍然必须向其理想的开发人员角色展示该价值。“我们可以有最好的意图。我们可以拥有最好的技术解决方案，”但如果没有团队、高级管理人员和七个生态系统合作伙伴的参与，采用就不会成功。

但它成功了。现在，养老金系统开发人员可以在不到四小时的时间内将更改交付到预生产环境。他们可以在几分钟内创建环境。他们可以使用自动单元测试，该测试突出显示 COBOL 代码以显示哪些代码已测试或未测试。漏洞在管道中较早被扫描出来。

Bhogireddy 将 Project Impala 的成功很大程度上归功于在整个转型过程中不断寻求反馈。

![年轻的 Leslie 引用说：“我不知道主机开发有什么大惊小怪的？”我是一名训练有素的云 DevOps 工程师，并且没有发现与主机 DevOps 管道有任何区别。”资深主机工程师说，“我认为在云中进行主机开发是不可能的，但当我看到正在做的事情时，我开始相信。”](https://cdn.thenewstack.io/media/2024/05/5b3cbde5-mainframe-vs-cloud.jpeg)

*两份 Legal & General 员工证明，展示了统一开发人员体验的成功。*

Legal & General 已被评为 [英国最受尊敬的公司](https://www.britainsmostadmired.com/winners/most-admired-companies/)，连续两年。Project Impala 最近获得了 IT 专业人士非营利组织 CMG 颁发的 [影响创新奖](https://www.cmg.org/2024/02/cmg-honors-legal-general-with-the-impact-innovation-award/)。

“对于我们来说，最暖心的是，年轻的 Leslies 告诉我们，这和大型机开发有什么关系？我是基于云的开发人员，”Bhogireddy 说。“但你不会发现我们创建的 DevOps 管道有任何区别，或者我们最资深的主流工程师最初不愿意踏上这段旅程，[现在]已经转变了。”
