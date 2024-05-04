## 主机平台工程：设计思维推动变革

![主机平台工程的特色图片：设计思维推动变革](https://cdn.thenewstack.io/media/2024/05/8cdcfe3d-project-impala-2-1024x576.jpg)

我们经常谈论 [在云原生复杂性面前的开发者体验](https://thenewstack.io/how-the-developer-experience-is-changing-with-cloud-native/)。然而，[71% 的财富 500 强公司](https://planetmainframe.com/2022/12/relevance-of-mainframe/) 仍在使用主机。我们如何实现主机工程师体验的现代化？

主机上的公司在快速增长时期面临不断变化的法规要求。此外， [主机开发人员的平均年龄](https://www.zippia.com/mainframe-systems-programmer-jobs/demographics/) 为 47 岁，这意味着有经验的人员即将退休——下一代需要入职。

Legal & General (L&G) 是全球最大的资产管理公司之一，拥有 1.7 万亿美元的资产和 10,000 名员工。在 4 月下旬的虚拟 [企业技术领导峰会](https://itrevolution.com/etls-eur24/) 上，L&G 的技术领导分享了他们的 [平台工程](https://thenewstack.io/platform-engineering/) 之旅，这使他们能够培养出色的开发者体验，而无需使用主机工具的工程师。

他们主机开发方法的这种转型是针对所有利益相关者的工具和同理心的社会技术融合。它弥合了时间和技术的差距。

### 设计思维实现主机的现代化

虚拟活动中的三位演讲者—— [Tariq Surty](https://www.linkedin.com/in/tariq-surty-8911101/)，零售业 IT 总监，[Jennifer Pickard](https://www.linkedin.com/in/jenniferpickard/)，工程主管，以及 [Bharghava Vamsi Krishna Bhogireddy](https://www.linkedin.com/in/bharghava-vamsi-krishna-bhogireddy-246543b/)，高级运营架构师——在 L&G 的养老金部门工作。2012 年，英国政府要求所有雇主必须提供养老金计划，员工必须选择退出，而不是加入。

由于这一要求，仅 L&G 的养老金部门就从 2012 年的 250,000 人增加到今天的 500 多万客户。英国养老金计划的最新监管变化使 L&G 预计未来几年将持续增长。

![变革案例：持续不断的变革量英国养老金行业的时间表，该行业经历了重大的监管变革。1998 年：个人养老金。2002 年：SERPS 被国家第二养老金计划或 S2P 取代。2004 年：《养老金法案》引入了养老金监管机构和养老金保护基金。2006 年：养老金简化引入。2010 年：国家养老金年龄开始变化。2011 年：三重锁定引入。2012 年：自动入职——可能是英国养老金中最大的举措。2014 年：大规模养老金改革。2015 年：养老金自由的开始。2016 年：引入新的固定费率、单层国家养老金。2018 年：女性国家养老金年龄提高到 65 岁。2019 年：自动入职缴款增加。2020 年：国家养老金年龄提高。2021 年：暂停三重锁定系统。2022 年：国家养老金增加](https://cdn.thenewstack.io/media/2024/05/5712d79a-legal-general-rate-of-change.jpeg)

此时间表说明了在过去 26 年中英国养老金制度的变革速度和复杂性。

2021 年，为了应对这种增长规模及其核心养老金管理系统预期的压力，L&G 问道：为什么不将主机现代化，而不是迁移到现代平台？目的是实现安全的系统开发生命周期和三个 3Q：变革的快速、质量和数量。

“为什么不加入 IT 革命，并带来所有 [DevSecOps](https://thenewstack.io/ebooks/devsecops/best-of-devsecops-trends-in-cloud-native-security-practices/) 和现代软件开发实践和工具所提供的优势？”Surty 在演讲中问道。“这样，我们不仅可以推动变革的数量，还可以推动变革的质量和速度。”

他补充说：“我想你们中的大多数人可能太年轻，无法像你们太年轻而无法记住雪佛兰 Impala 一样记住主机技术。但鉴于我们正在使用传统技术，并且希望推动更大的敏捷性、灵活性和速度，”他们将平台工程计划命名为 Project Impala。

许多企业希望通过 [大爆炸式云迁移](https://thenewstack.io/going-from-cobol-to-cloud-native/) 来驯服主机。相反，Legal & General 采用以同理心为导向的 [设计思维](https://blog.container-solutions.com/wtf-is-design-thinking) 方法来尝试了解与主机合作的不同群体及其痛点。
**同理心驱动的设计思维流程**

L&G 基于同理心的设计思维方法遵循以下流程：

- **同理心：**更好地理解人们的需求。
- **定义：**确定要解决的主要问题。
- **构思：**讨论可能会有用的解决方案。
- **实施或原型：**创建要测试的模型。
- **测试：**分享并获得反馈。

**教导大型机开发人员了解 DevOps**

很明显，大型机开发人员需要了解当代 DevOps 实践。

L&G 平台团队将主要学习内容归纳为：

- 工具
- 创建高质量数据所需的时间
- 手动步骤和交接的数量
- 环境争用

**“莱斯利”：现代大型机开发人员角色**

为了专注于他们理想的开发人员角色，L&G 的工程部门与 GitHub 的 Copilot 集思广益，询问生成式 AI 编码助手现代大型机开发人员是什么样子。

它提出了“莱斯利”，她既可以用 COBOL 也可以用 Python 编写代码，并且可以在绿屏和 GUI 之间切换。她可以轻松处理 TB 级数据，并且“不害怕遗留系统，而是将它们视为挑战和机遇”。

这种大型机工程师角色平衡了矛盾——新旧、可靠和创新、安全和敏捷。她可以使用现代云计算、AI 和 DevOps。
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

两份 Legal & General 员工证明，展示了统一开发人员体验的成功。

Legal & General 已被评为 [英国最受尊敬的公司](https://www.britainsmostadmired.com/winners/most-admired-companies/)，连续两年。Project Impala 最近获得了 IT 专业人士非营利组织 CMG 颁发的 [影响创新奖](https://www.cmg.org/2024/02/cmg-honors-legal-general-with-the-impact-innovation-award/)。
“对于我们来说，最暖心的是，年轻的莱斯利告诉我们，这和大型机开发有什么关系？我是基于云的开发人员，”博吉雷迪说。“但你不会发现我们创建的 DevOps 管道有任何区别，或者我们最资深的主流工程师最初不愿意踏上这段旅程，[现在]已经转变了。”

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。