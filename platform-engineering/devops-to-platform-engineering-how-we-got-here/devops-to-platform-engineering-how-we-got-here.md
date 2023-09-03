# DevOps 到平台工程：我们的前行之路

翻译自 [DevOps to Platform Engineering: How We Got Here?](https://www.infracloud.io/blogs/devops-to-platform-engineering-how-we-got-here/) 。

在 2000 年代，软件行业发生了许多重要事件。丰田的精益生产运动已经在汽车生产中证明了其巨大价值。许多行业，不仅包括制造业，显然软件行业也注意到了他们的领域与“精益”之间的相似之处。软件行业的早期创新者也在尝试“持续集成”的想法，可以从诸如 [CruiseControl（2001）](https://en.wikipedia.org/wiki/CruiseControl) 和 [Hudson（2005）](https://en.wikipedia.org/wiki/Hudson_(software)) 等工具的诞生中看出，而 Hudson 的一个分支被命名为 [Jenkins（2011）](https://en.wikipedia.org/wiki/Jenkins_(software))，被开源社区采用，并成为[实施 CI/CD](https://www.infracloud.io/ci-cd-consulting) 的最受欢迎的工具之一！2009 年，正式提出了 “DevOps” 的术语，是在 O'Reilly Velocity Conference 上，Flickr 的工程师们呈现了他们著名的演讲：“[10+ Deploys per Day: Dev and Ops Cooperation at Flickr](https://www.youtube.com/watch?v=LdOe18KhtT4)”，并且形成了 DevOpsDays 会议。

![](https://d33wubrfki0l68.cloudfront.net/e0d70fb73f6d3794434734f4a0c5220ccbf1f5bd/169e6/assets/img/blog/devops-to-platform-engineering-how-we-got-here/star-trek-meme-devops-to-platform-engineering-how-we-got-here.png)
*([来自著名的演讲 “10+ Deploys per Day: Dev and Ops Cooperation at Flickr”](https://www.youtube.com/watch?v=LdOe18KhtT4))*

DevOps 的基本思想是将“开发”和“运维”团队对齐，以实现更高速度的软件交付目标。虽然技术、流程和人员的对齐花费了 2010 年代很大一部分时间！

![DevOps 对齐](https://d33wubrfki0l68.cloudfront.net/253845135da4686a97cfbba242d731b999a5f67d/b699e/assets/img/blog/devops-to-platform-engineering-how-we-got-here/devops-illustration.png)

## 云计算、规模和复杂性的增长：2010 年代

2010 年代见证了云计算、SaaS 和容器等技术的巨大增长。只需了解一下增长情况，AWS 从 2010 年的 10 万客户增长到 2015 年的 100 万客户，或者 Docker 于 2013 年推出，2014 年已有 10 万家公司在使用/评估，而在一年后的 2015 年，以 Docker 形式使用容器的公司达到了 100 万家！

![](https://d33wubrfki0l68.cloudfront.net/63588ec4a11c99c010eb40f80a8f1a1259546d4a/70ab2/assets/img/blog/devops-to-platform-engineering-how-we-got-here/docker-adoption-behavior.png)
*[（来源：Datadog 的 Docker 采用研究）](https://www.datadoghq.com/docker-adoption-2017/)*

云计算和技术的增长改变了一些事情，例如：

* 一系列新工具应运而生，用于构建、运营和扩展软件。例如，Terraform 是一种用 HCL 定义基础设施的方式。或者一旦 Docker 成为主流，编排就成为创新的新领域，最终导致了 Kubernetes 及其周边大规模生态系统的诞生，被称为 Cloud Native Technologies。

![编排器的使用](https://d33wubrfki0l68.cloudfront.net/38bff67f988b1804a98590c0e9901ec269e7db19/9414e/assets/img/blog/devops-to-platform-engineering-how-we-got-here/usage-of-orchestrators.png)
*早年的编排器增长，例如 Mesos、Docker Swarm、Kubernetes 或 Rancher Cattle。来源：[Datadog 2017 的 Docker 采用研究](https://www.datadoghq.com/docker-adoption-2017/)*

* SaaS - 许多新业务现在以 SaaS 形式通过互联网交付。这意味着您现在可以通过 SaaS 提供商交付应用程序的大部分需求，同时可以专注于业务的核心。在这个过程中，运营的问题不仅仅是部署和管理基础架构。运营现在包括更高可靠性的构建，或者以安全性为重点的构建，因为您的服务正在跨越组织的网络边界！

> 随着 SaaS 变得更加主流，可靠性、安全性和成本等问题都成为主要关注点。运营的范围比以前扩展得多！

## ShiftLeft + “You Build It, You Run It” (YBYRI)

尽管运营的范围扩展得更广泛，但开发方面的事情也同样增加。许多与安全性或可靠性相关的问题正在“编码”中定义。因此，开发人员必须对这些事物有所了解，即使是表面层次的了解。向左移动也是由敏捷运动推动的，以便修复尽可能靠近开发人员的内部开发，而不是将代码完全推向需要更改的阶段，然后再通过整个流程流动。

一些大型组织也尝试了 YBYRI - 你建立它，你运行它！这意味着开发团队必须了解除编写代码之外的许多其他事情。开发团队可能需要负责从与业务相关的代码更改到可靠性、安全性等方面的所有事情。

## Development+++: 定义与混淆！

因此，DevOps 运动始于伟大的初衷，并解决了许多问题。然而，云计算、SaaS 和应用程序的复杂性的增长迅速模糊了边界，导致几乎每个人的认知负担增加！

![YBYRI无法扩展](https://d33wubrfki0l68.cloudfront.net/1c0ed44278866cc792d210c793b1ed9ce3dadc99/a77c7/assets/img/blog/devops-to-platform-engineering-how-we-got-here/ybyri-does-not-scale.png)
*（[图片来源](https://www.slideshare.net/grabnerandi/kcd-munich-cloud-native-platform-dilemma-turning-it-into-an-opportunity)）*

那么，除了编写代码，开发人员还应该知道 Terraform 如何提供一切，或者如何为 Kubernetes 编写所有清单和图表吗？同样，运营团队是否需要编写代码，如果是的话，边界在哪里？这不是要建立壁垒的问题，但毫无疑问，让每个人承担如此多的事情的认知负担是不具生产力的。因此，如果我们回到最初的 Dev 对齐 Ops 的图表，现在它是与更多功能（如安全性、可靠性、成本以及当然是 Dev 和 Ops）之间的对齐！

![开发人员认知负担](https://d33wubrfki0l68.cloudfront.net/e782c33346bd5a1ca5a2d05de20b5a167176ea3a/618c7/assets/img/blog/devops-to-platform-engineering-how-we-got-here/developer-cognitive-load.png)

## 平台工程的崛起

所有这些事情导致了重新思考团队结构，以减少认知负担，增加流程状态和更快的反馈循环。一些快速扩张并且是 DevOps 领先采用者的组织迅速识别了这一模式，并改进了团队结构、工具和流程，以构建出能够支持开发人员的平台。

那么，什么是平台工程？组织内部平台工程的目标是使交付团队能够获取所需的内容并快速移动，同时专注于应用程序。随着应用程序经历的复杂性和广度的增加，开发人员不可能深入了解一切。这就是平台的作用，使他们可以对他们想要快速推进的事物使用明智的默认值，而后根据需要进行更改。随着时间的推移，平台将成为一个完整的产品，用于支持软件的交付，但这不一定是最初的目标。

这就是全部内容！我们将很快在另一篇文章中介绍“什么是平台工程”，所以敬请期待（或者您可以订阅我们的新闻通讯，每周获取云原生知识的一小部分）。