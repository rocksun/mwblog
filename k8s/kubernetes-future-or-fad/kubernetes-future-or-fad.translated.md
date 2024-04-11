## Kubernetes 的崛起

开玩笑地说，在字典中查找容器编排时，你可能会找到同义词 Kubernetes，但 Kubernetes 花了大约十年的时间才走到今天。

Kubernetes 最初由 Google 基于 Borg（Google 的内部容器编排平台）的关键经验教训构建，于 2014 年 9 月发布。在 Kubernetes 发布时，Borg 本身已经超过十年了。到 2013 年，Borg 的许多原始团队成员开始研究下一步。Project 7 诞生了。

在发布时，Kubernetes 仍在底层使用 Docker。这种组合很可能有助于提升 Kubernetes 的普及度。Docker 当时非常流行，但人们在尝试组织和运行大量容器时开始发现不足。Kubernetes 即将解决这个问题。凭借其构建块的概念、独立部署和参与者（或代理），它易于扩展但仍然易于理解。此外，资源本质上是声明式的（以 JSON 或 YAML 文件编写），这使得这些定义能够进行版本控制。

自发布以来，Kubernetes 启用了越来越多的用例，因此越来越多的公司开始使用它。我认为采用的一大步是 2016 年 Helm 的发布，它简化了更复杂应用程序的部署过程，并实现了“开箱即用”的体验。现在 Kubernetes“容易”（不要引用我说的容易！）。

如今，每个云提供商及其母公司都提供托管的 Kubernetes 环境。由于一组标准接口，这些服务大多可以互换。Kubernetes 的一大好处。无论如何，它只是大部分。小的不一致和实现或性能差异可能会让你度过一生。但不是好的。但我们称之为“随处运行”，因为它大部分都是。

[Ferenc Hámori](https://www.linkedin.com/in/ferench) 在 [Kubernetes 的历史](https://blog.risingstack.com/the-history-of-kubernetes/) 中提供了 Kubernetes 完整历史的精彩概述，其中包括所有主要里程碑。

## Kubernetes，爱或恨

当我们深入了解社区时，人们对 Kubernetes 的看法分歧很大。许多人指出了 Kubernetes 的内部（但隐藏的）复杂性。随着新功能和附加功能（包括第三方）的添加，这种复杂性只会增加。这种复杂性是真实的，这就是像 [Kelsey Hightower](https://twitter.com/kelseyhightower) 或 [Abdelfettah Sghiouar](https://www.linkedin.com/in/sabdelfettah) 这样的人称 Kubernetes 为构建平台的平台（收听我们的 Cloud Commute [播客剧集与 Abdelfettah](https://www.simplyblock.io/cloud-commute-podcast/episode/225e0346/abdelfettah-sghiouar-from-google-cloud-commute-by-simplyblock)）的原因，这意味着它应该由云提供商（或公司内部私有云团队）用于构建容器部署平台，但它不应该由开发人员或每个人使用。然而，Kelsey 也声称 Kubernetes 是一个好的起点，而不是终点。

Kubernetes 已几乎成为容器编排的代名词，所有竞争要么被同化（或被重写为基于 Kubernetes，参见 Openshift），要么基本上消失在虚空中（抱歉 Nomad）。这是否意味着开发现在会放缓？还是更大规模的开始？也许 Kubernetes 正处于成为通用名称的边缘，就像 Kleenex，或者也许像“谷歌”这样的动词。

几年前，有人在面试中问我如何看待 Docker，以及我是否看到容器化的未来。当时我的回答快速而简单。首先，容器化并不是一个新概念。BSD、Solaris 以及其他系统已经使用了多年。它们对 Linux 来说是比较新的（至少在广泛使用方面），所以它们会继续存在。这是虚拟化的下一个合乎逻辑的进化步骤。然而，在我看来，Docker 是不同的。对于 Docker，我简单地回答“这是我们今天拥有的最好的工具，但我希望它不是我们能想出的最终解决方案。”虽然 Docker 已经扭转局面并即将回归，但我们今天使用的工具一致建立在开放容器计划 (OCI) 及其 OCI 镜像格式定义的规范之上。

那么 Kubernetes 的未来会怎样？它会继续存在还是会走向深渊，并且它会“只是另一个被其他东西取代的平台”，正如 [Michael Levan](https://www.linkedin.com/in/michaellevan/) 在 [Kubernetes 的未来](https://dev.to/thenjdevopsguy/the-future-of-kubernetes-2l0b) 中所写。
在光谱的另一端，有人将 Kubernetes 称为云领域的“操作系统”。由于其可扩展性和丰富的功能，他们可能并不算太离谱。现代操作系统的**主要工作**是抽象底层硬件及其功能。也就是说，Kubernetes 抽象了云基础设施的许多方面以及运行容器所需的运营流程。从这个意义上说，是的，Kubernetes 可能是一个云操作系统。特别是当我们开始看到 Kubernetes 在除 Linux 之外的其他操作系统上运行的实现时。微软，我说的就是你。

如果您有兴趣进一步了解 Kubernetes 作为云操作系统的理念，
来自 Robusta Dev 的 [Natan Yellin](https://www.linkedin.com/in/natanyellin/) 撰写了一篇非常有见地的文章，名为 [Kubernetes 将如何持续存在 50 年](https://platformengineering.org/blog/why-kubernetes-will-sustain-the-next-50-years)。

## 下一步是什么？

对于 Kubernetes 而言，最紧迫的问题是，下一步是什么？它将如何演变？我们是否接近终点？

回顾 Borg，十年后，Google 决定是时候重申编排并根据所吸取的教训进行构建了。Kubernetes 即将迎来其 10 周年纪念日。那么，这意味着是时候进行另一次迭代了吗？

Kubernetes 中的许多功能（例如机密）在 10 年前很好。今天我们知道，编码的“机密”肯定不够。临时用户帐户、OIDC 和类似技术可以并且已经集成到 Kubernetes 中，从而增加了其复杂性。

展望 Kubernetes，技术总是经历三个阶段：开始或采用阶段、每个人“必须”使用它的中间阶段以及公司开始逐步淘汰它的结束阶段。我个人认为，Kubernetes 目前正处于鼎盛时期，处于中间位置。

但这并不能让我们预测达到终点的时间表。目前看来，Kubernetes 将继续发展和壮大一段时间。它没有显示出任何放缓的迹象。

其他技术，如微型虚拟机，使用
[kata 容器](https://katacontainers.io/) 或 [Firecracker](https://firecracker-microvm.github.io/)，正变得越来越流行，提供更高的隔离性（因此更安全），但效率不高。然而，它们提供了一个重要的元素，即 CRI 兼容接口。这意味着它们可以用作 Kubernetes 下面的备用运行时。

在不久的将来，我看到 Kubernetes 提供多种运行时环境，就像它今天提供多种存储解决方案一样。启用在普通容器中运行简单服务，但将具有更高隔离需求的服务移动到微型虚拟机。

还有其他基于 Kubernetes 的有趣发展。Edgeless Systems 实施了一种机密计算解决方案，作为名为 Constellation 的 Kubernetes 发行版提供。机密计算利用 CPU 和 GPU 功能，帮助硬件加密内存，不仅适用于整个系统内存空间，还适用于每个虚拟机，甚至每个容器。这开启了一整套新的用例，为高度机密计算和数据处理提供端到端加密。虽然可以在 Kubernetes 之外使用它，但将这些计算运行在容器中的编排和操作优势使其易于部署和更新。如果您想了解更多有关 Constellation 的信息，我们不久前在我们的 [播客](https://www.simplyblock.io/cloud-commute-podcast/episode/2cfadcf6/moritz-eckert-from-edgeless-systems-cloud-commute-by-simplyblock) 中邀请了来自 Edgeless Systems 的 [Moritz Eckert](https://www.linkedin.com/in/eckert-moritz/)。

## 未来还是潮流？

那么，Kubernetes 是否拥有光明的前途，并将持续存在 50 年，还是我们很快就会意识到它不是我们正在寻找的东西？

如果今天有人问我如何看待 Kubernetes，我想我会回答得与我的 Docker 答案类似。它肯定是我们今天拥有的最好的工具，使其成为当今的容器编排工具。然而，它不断增加的复杂性使得很难在未来看到同样的情况。我认为有很多新的经验教训。现在可能是进行新迭代的时候了。不是今天，不是明天，而是在未来几年中的某个时候。

![Kubernetes：未来还是潮流？](https://static.wixstatic.com/media/a7fbb2_a151d1a2af9b48f3914b9ac74ce91466~mv2.jpg/v1/fill/w_147,h_77,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_auto/a7fbb2_a151d1a2af9b48f3914b9ac74ce91466~mv2.jpg)

也许这个新迭代不是一个全新的工具，而是 Kubernetes 2.0，谁知道呢——但有些东西必须改变。技术不会停滞不前，（容器）世界与 10 年前不同。
**如果你在集装箱化初期问某人，那都是关于容器必须是无状态的，而我们今天做什么？**

我们将数据库部署到 Kubernetes 中，我们喜欢它。云原生不再只是无状态的，但我认为今天三分之一的容器工作负载可能是状态化的（具有临时或持久状态），并且它将继续增加。编排、自动资源管理、自修复基础设施以及介于两者之间的所有内容的美妙之处在于，它太不可思议了，无法将其用于“所有内容”。

**无论如何，无论 Kubernetes 本身发生什么（也许它将成为 OCI 的编排扩展？！），我认为它将从用户的眼中消失。**

它（或其继任者）将成为构建容器运行时平台的平台。但要实现这一目标，需要提供调试功能。目前，您必须深入了解 Kubernetes 或代理日志才能找出并修复问题。现在可以举手的人，他从未发现过为什么 Let's Encrypt 证书没有更新。

**总之，Kubernetes 肯定不是一种潮流，但我强烈希望它也不是我们的未来。至少不是以其当前的形式。**