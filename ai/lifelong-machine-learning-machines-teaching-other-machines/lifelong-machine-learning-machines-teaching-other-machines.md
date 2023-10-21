<!--
# 智能机器终身学习: 机器教机器
https://cdn.thenewstack.io/media/2023/09/e78954c9-pexels-pixabay-159775.jpg
 -->

针对机器学习的一个分支——终身学习(Lifelong Learning，LL)的新研究表明，机器确实具备人类式的学习能力。

译自 [Lifelong Machine Learning: Machines Teaching Other Machines](https://thenewstack.io/lifelong-machine-learning-machines-teaching-other-machines/) 。

对人类来说，学习是终身的过程。我们在生活中不断获取、分享和发展新的技能，并持续将这些技能运用到新的场景中。相比之下，我们通常不会认为机器能够像人类那样，以协作的方式进行长期的学习。然而，针对[终身学习](https://www.cs.uic.edu/~liub/lifelong-machine-learning.html)(LL)这一[机器学习](https://thenewstack.io/how-machine-learning-works-an-overview/)分支的新研究表明，机器确实具备这种人类式的学习能力，也就是说它们能够随着时间的推移不断积累知识，并在此基础上建立新知识，以适应新的场景。

现在，南加州大学的Laurent Itti和研究生Yunhao Ge带领的一个研究团队，开发了一种工具，可以让人工智能代理进行这种持续的集体学习。在最近发表的题为 [Lightweight Learner for Shared Knowledge Lifelong Learning](https://openreview.net/pdf?id=Jjl2c8kWUc) 的论文中，研究人员描述了他们的共享知识终身学习(Shared Knowledge Lifelong Learning， SKILL)工具是如何帮助AI代理最初各自学习102个不同的图像识别任务，然后通过分散式通信网络与其他代理分享知识。这种集体知识传播最终让所有代理最终掌握了所有102项任务，同时仍保持对各自最初被分配任务的知识。

Ge在[声明](https://www.eurekalert.org/news-releases/996134)中解释说：“这有点像每个机器人都在讲授自己最拿手的课题，其他所有机器人都是专心的学生。它们通过一个数字网络相互连接，分享知识，有点像它们自己的内部互联网。实际上，任何需要广泛、多样化知识或处理复杂系统的职业都能显著受益于这种SKILL技术。”

## 避免“灾难性遗忘”

终身学习是机器学习的一个相对较新的领域，AI代理在遇到新任务时会持续学习。LL的目标是使代理在获取新任务知识的同时不忘记如何执行之前的任务。这种方法不同于典型的“训练后部署”机器学习，后者在学习新信息时会发生“[灾难性干扰](https://codelabsacademy.com/blog/catastrophic-forgetting-in-machine-learning)”(也称“[灾难性遗忘](https://en.wikipedia.org/wiki/Catastrophic_interference)”)，导致AI忘记大量先前学习的信息。

据该团队介绍，他们的工作可能代表了终身机器学习领域的一个新方向，因为目前的LL研究都是让单个AI代理顺序学习多个任务。

相比之下，SKILL涉及大量AI代理同时以并行的方式学习，从而显著加速了学习过程。该团队的研究结果表明，使用SKILL后，学习所有102项任务的时间缩短了101.5倍之多，这对于AI的自主学习和实际部署来说可能是一个巨大的优势。

“当前的LL研究大多假设单个代理会顺序地从自身行动和周围环境中学习，这种设计本身就不可并行化。”该团队解释道。

“在现实世界中，不同的任务可能发生在不同的地点......SKILL具有以下优点：通过并行学习加速训练过程;可以同时从不同地点学习;由于没有使用中央服务器，因此具有容错能力;代理之间可能存在协同效应，一个代理学到的东西可帮助其他代理以后学习。”

## “通用神经网络骨干”

为了创建SKILL，研究人员从[神经科学中获取启发](https://thenewstack.io/stronger-artificial-intelligence-needs-neuroscience-inspiration/)，特别关注“[祖母细胞](https://www.bionity.com/en/encyclopedia/Grandmother_cell.html)”或认知神经元理论，这种假设的神经元可以表示某个复杂但特定的概念或对象。当人感知或思考这个特定实体时，该神经元就会激活。

对研究人员来说，祖母细胞理论启发他们设计了轻量级终身学习(LLL)代理，这些代理具有一个通用的、预先训练的神经网络“骨干”，能处理基于图像的任务。正如该团队指出的，这种方法支持“分布式去中心化学习，因为各个代理可以独立地学习自己的任务”。由于以并行的方式进行，这种技术还使得加速和可扩展的终身学习成为可能。

![](https://cdn.thenewstack.io/media/2023/09/21f55783-lifelong-learning-skill.jpg)

*图片显示了SKILL算法的设计。*

“各个代理使用一个通用的固定骨干，只为每个任务训练一个紧凑的任务相关‘头’模块，然后在代理之间共享。”该团队澄清道，“这使得训练和共享的成本非常低。头模块仅包括操作在固定骨干之上的分类层，以及一组有益的偏差，它们为骨干提供轻量级的特定任务调优，以弥合骨干与每个新任务的数据分布之间可能存在的鸿沟。”

研究人员表示，SKILL类似于众包，一群人分享各自的技能和知识来共同解决问题。他们认为机器也可以使用类似的方法来辅助人类专业人员，成为各个领域如医学的“全面助手”。结合其他新兴研究领域如[AI的社会智能](https://thenewstack.io/social-intelligence-is-the-next-big-step-for-ai/)，其他专家也指出终身机器学习[对开发通用人工智能(AGI)至关重要](https://www.cs.uic.edu/~liub/lifelong-machine-learning.html)。

更多信息请阅读该团队的[论文](https://openreview.net/pdf?id=Jjl2c8kWUc)。
