<!-- 
# 复杂性孕育了平台工程
https://cdn.thenewstack.io/media/2023/11/dabf0dc1-complexity-1-1024x576.jpg

 -->

KubeCon 在芝加哥举行，Release公司CEO Tommy McClung在会上谈到他们公司的工具致力于将复杂性简化。

译自 [How Platform Engineering Comes from Complexity](https://thenewstack.io/how-platform-engineering-comes-from-complexity/) 。

芝加哥 - [平台工程](https://thenewstack.io/platform-engineering-navigating-today-forecasting-tomorrow/)源于复杂性。

在[KubeCon + CloudNativeCon](https://www.cncf.io/kubecon-cloudnativecon-events/?utm_content=inline-mention)北美的这个星期，听到像[Release](https://release.com/?utm_content=inline-mention) CEO [Tommy McClung](https://www.linkedin.com/in/tmcclung/)这样的人讲话后，这似乎是个事实。

“我曾是一家上市公司的CTO，遇到了你刚才谈到的所有问题，”KubeCon这样的会议上，我们听到的有关复杂性程度的问题与任何其他问题一样多，因为如果你不了解[Kubernetes](https://thenewstack.io/kubernetes/)及其作为自定义世界释放的作用的深层复杂性，你还能怎么做？吸引了10，000人参会。

[Kubernetes](https://thenewstack.io/tim-hockin-kubernetes-needs-a-complexity-budget/)永远不会完全完成。谷歌的Tim Hockin上周在KubeCon的主题演讲中引用了他的一位同事的话，意思就是这个效果。

但是[平台工程](https://thenewstack.io/platform-engineering/)有助于让客户更接近与Kubernetes“足够好”特性相符的所需状态。企业架构也从未真正完成。[技术债务](https://thenewstack.io/how-frontend-devs-can-take-technical-debt-out-of-code/)和定制系统与企业天然契合。平台工程让开发者的工作更轻松。平台工程减轻了已经面临认知过载的开发者的负担。

## Spotify：定制系统无处不在

来看看Spotify面临的问题。它的开发人员代码编写速度惊人。但随后IPO来了，Ernst&Young的会计师说存在一些问题。

这家流媒体公司的代码库包含自定义脚本、各种API和通往生产环境的多种[CI/CD](https://thenewstack.io/ci-cd/)路径。(感谢[Corecursive: Coding Stories](https://corecursive.com/)对Spotify创建的内部开发者平台[Backstage](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/)起源所做的优秀[播客节目](https://corecursive.com/platform-takes-the-pain/)。)

Spotify代表了组织面临的混乱状态。定制系统无处不在。引用Hockin的主题演讲:

> 对于复杂性，@thockin说：...其结果是操作和概念上的复杂性增加......这就是“复杂性预算”的想法。很简单的想法。在一定时间内，我们可以吸收到项目中的复杂性数量是有限的。#KubeCon

## Release：驾驭复杂性

那么，Release如何适应Spotify所面临的这种情况呢？

“我们有遗留系统，”McClung说。“我们正在进行云迁移。我们引入了所有这些供应商。我们使用了一些云原生 Stuff。我们进行了容器迁移。这一切都很困难。

“所以我认为平台工程这一方面，如果你想走这条路，就是一个抽象化这种复杂性的努力。因此，开发人员不必处理它，这最终是无论你称之为环境即服务还是平台工程的目标。”

正是这种复杂性使开发人员难以获取资源。

“每个客户都有定制的性质，”McClung说。“如果你想做一些让开发人员轻松、一致地完成工作的事情，那么你就必须抽象化这种复杂性，这就是我们所做的事情的使命。

“我们希望开发人员可以访问那个定制生态系统，而不必担心其中的复杂性。在我们的世界里，这体现为环境。”

McClung说，Release提供预览开发人员环境。分期允许开发人员对他们构建的内容进行玩弄，并查看要交付的内容。

“我们的工作就是真的驾驭那种复杂性，”他说。“但这非常复杂。使非常复杂的事情变得简单是非常困难的。”

Release提供所谓的模板或蓝图。客户经常在踏上现代化之路后来找Release。他们已经制定了一些基础设施即代码做法。 Release消耗来自Helm Chart和[Docker](https://www.docker.com/?utm_content=inline-mention) Compose文件等所有信息 - 不管小块是什么。

McClung说，这是一个标准模板，定义了应用程序、其基础设施和重新生成它所需的工作流程。

“我们称之为基础设施即代码之上的一种抽象，”他说。“就是这样。它采用您现有的所有部分，然后能够重新生成全部内容。”

这是一个短暂的环境，它分析现有的报告、代码、配置和其他定制组件。它生成一个蓝图，重现客户的环境，考虑到所有定制组件。

环境按需启动，无需手动组装所有部分。 

没有复杂性就不会存在平台工程。这就是人们来KubeCon的原因。他们想要找到解决他们面临的复杂性的解决方案。现在，答案越来越多地体现在学习平台工程实践中。

“平台工程这一方面，如果你想走这条路，就是一个抽象这种复杂性的努力，”McClung说。“因此，开发人员不必处理它，这最终是无论你称之为环境即服务还是平台工程的目标。

“开发人员需要这些资源来完成工作。由于这种复杂性，让这些资源为他们服务是非常困难的。”
