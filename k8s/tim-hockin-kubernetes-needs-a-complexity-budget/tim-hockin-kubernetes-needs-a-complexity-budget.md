<!-- 
# Kubernetes 需要控制复杂度
https://cdn.thenewstack.io/media/2023/11/86e09c28-kubecon-hockin-03.png
 -->

Kubernetes 的核心维护者在考虑新增功能时，应该权衡其带来的好处和额外复杂度。Kubernetes 的联合创始人在今年的 KubeCon 大会上提出了这个建议。

译自 [Tim Hockin: Kubernetes Needs a Complexity Budget](https://thenewstack.io/tim-hockin-kubernetes-needs-a-complexity-budget/) 。

芝加哥 —— Kubernetes 的高级工程师们达成共识: K8s 正变得过于复杂，不仅对终端用户，可能连核心维护者自己都难以掌控。是时候给复杂度设定一个预算了。

在本周 [Kubecon+CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 大会的主题演讲中，Kubernetes 的联合创始人、Google 杰出软件工程师 [Tim Hockin](https://thenewstack.io/kubernetes-co-founder-tim-hockin-extensibility-ecosystem/) 回顾了 Kubernetes 前九年半的发展历程，并展望了其未来发展方向。Kubernetes 起初主要用于支持高度可扩展的 Web 应用，但现在它越来越多地被用于更复杂的任务，比如[机器学习推理](https://thenewstack.io/tensorflow-model-deployment-and-inferencing-with-kubeflow/)。这意味着扩展 Kubernetes 以支持更多用例的压力正在大幅增加。

为准备演讲，Hockin 询问了云原生社区的其他人员，他们认为 Kubernetes 当前面临的最大挑战是什么。一个反复出现的主题是应对部署和维护容器编排引擎[日益复杂的困难](https://thenewstack.io/how-to-fight-kubernetes-complexity-fatigue/)。

有人甚至认为这是 Kubernetes 最大的“生存威胁”。

![](https://cdn.thenewstack.io/media/2023/11/8177f0f0-kubecon-hockin-04.png)

“必须做出妥协，” Hockin 说，“项目在一定时间内可以吸收的复杂度是有限的。” 他指出，复杂度越高，核心维护者未来进行变更的敏捷性就越低。

与此同时，软件越复杂，用户阻力也越大。

Kubernetes 周边的软件是由社区推动的: 迄今为止，项目已经吸引了超过[74，000名贡献者](https://www.cncf.io/reports/kubernetes-project-journey-report/)。这第一代用户对 Kubernetes 感兴趣，其中许多致力于使其变得更好。

但是随着新用户不断加入，他们必然会越来越不关心 Kubernetes 的内部工作机制。所以维护者有责任使其更易于使用，这一点 Hockin 强调了。

“我们添加的功能越复杂，就消耗越多的‘复杂度预算’。当预算用尽时，会带来坏结果，” 他说，创新停滞，用户流向其他解决方案。

因此，Kubernetes 的项目管理者需要考虑复杂度是一个有限的资源，是一个“复杂度预算”。

Hockin 承认他不知道如何量化软件的复杂度，也不知道用户容忍复杂软件的程度。

但是他指出，工程师通常知道自己何时“透支”。所以在考虑新增功能时，必须问自己: 复杂度预算还能不能承受？这是应该在有限预算中投入的吗？

工程师的工作就是权衡任何决策的利弊，新增功能带来的复杂度增长也应该是要评估的因素之一。

某些代码改动可能让软件性能提升5%，但如果给维护者带来更多内部复杂度，那是否值得？如果 API 改动只是为了满足小众用例，这是否应该加重所有其他用户的负担？

“提高门槛需要我们愿意说不，对我们真正想要的也说不，对看似容易实现的也说不，对公司要求的也说不，” 他说。

![](https://cdn.thenewstack.io/media/2023/11/82799366-kubecon-hockin-02.png)

通过对某些提议说“不”，就为未来更重要的项目留出了复杂度预算。

“我们必须现在就对某些事说‘不’，这样才能实现更有意义的创新，” Hockin 说。

Kubernetes 还有许多工作要做，但这并不意味着全部都需要立即完成。我们习惯了“更多就是更好”，但对 Kubernetes 来说，眼下“少就是多”可能更恰当，Hockin 说。

正如有人向 Hockin 建议的: 为保持活力，Kubernetes 应该保持未。

![](https://cdn.thenewstack.io/media/2023/11/a43fc14a-kubecon-imperfecta.png)

