<!--
title: Cycle.io：认识致力于取代Kubernetes的团队
cover: https://cdn.thenewstack.io/media/2023/11/f39c6f9c-cycleio-1024x768.png
-->

Kubernetes是由谷歌设计的，用于运营其庞大的业务属性，而我们中的许多人不需要那种规模。

> 译自 [Cycle.io: Meet the Team on a Mission to Replace Kubernetes](https://thenewstack.io/cycle-io-meet-the-team-on-a-mission-to-replace-kubernetes/)。作者Charles Humble是一位前软件工程师、架构师和CTO，曾在技术和内容组担任高级领导和执行官。他于2014-2020年担任InfoQ的总编辑，并于2020-2023年担任Container Solutions的首席编辑。他定期为The New Stack和其他出版物撰写文章，是一位高度资深的内容战略家，并在多个国际会议上发表过演讲，包括GOTO(主题演讲)、Devoxx、WTF is SRE和QCon。他的主要兴趣领域是我们如何更好地构建软件，包括可持续性和伦理、云计算、远程工作、多样性和包容性以及激励下一代开发者。Charles也是一位键盘手，并且是氛围科技乐队Twofish的一半。

当我们想到容器编排时，近十多年来，Kubernetes 一直是默认首选。但它不利于开发者使用，需要投入大量时间和精力才能部署、操作和故障排除。

组织内部专门的平台团队把大部分时间花在管理Kubernetes上已司空见惯，现在我们开始看到对此的反弹。

Kelsey Hightower，他与Kubernetes的兴起几乎划上等号，最近在[推特上说](https://twitter.com/kelseyhightower/status/1671582240026025986)：“如果你不需要Kubernetes，就不要使用它。”

但你还有什么其他选择呢？在我去年为The New Stack 撰写的[一篇文章中](https://thenewstack.io/can-you-live-without-kubernetes/)，我审视了更广阔的局面，其中包括使用大型云供应商的托管Kubernetes服务；像Red Hat的[OpenShift](https://www.openshift.com/try?utm_content=inline-mention)这样的Kubernetes发行版本；类似[HashiCorp](https://www.hashicorp.com/?utm_content=inline-mention)的Nomad这样的替代方案；以及采用Adrian Cockcroft称之为“[无服务器优先方法](https://blog.container-solutions.com/adrian-cockcroft-on-serverless-continuous-resilience)”的方式，直接使用FaaS产品(如[Azure](https://news.microsoft.com/?utm_content=inline-mention) Functions、[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline-mention)Lambda或谷歌云函数等)，完全绕过Kubernetes。

我还简要介绍了[cycle.io](http://cycle.io/)，它介于PaaS和编排器之间。该公司继续投入并改进他们的产品，我对深入研究该产品，并了解它对更广泛的编排器市场状况的看法很感兴趣。

Cycle将他们的平台描述为“[LowOps](https://cycle.io/blog/2022/12/cycle-is-the-lowops-approach-to-platform-engineering/)”，他们将其定义为抽象出应用程序管理的实现细节，“以便一个平台工程师——即使是有限的DevOps经验的人——能够描述他们想要的目标状态，而平台负责使其发生”。

虽然Kubernetes旨在提供[完全定制化](https://thenewstack.io/why-kubernetes-operators-will-unleash-your-developers-by-reducing-complexity/)及其带来的灵活性和复杂性，但Cycle希望在完全定制化和“开箱即用”之间找到一个平衡点。

归根结底，这里的目标是拥有一种管理容器和基础设施的方式，它提供类似Heroku的用户体验，并具有Apple的始终保持最新版本的方法。

## Cycle 的内部工作原理

要理解Cycle的核心是它组合了两件事——平台编排和基础设施管理——目标是简化两者。

从基础设施的角度来看，Cycle把重点放在容器上，之下的服务器作为分布式资源池出现。

支持的容器镜像源都是OCI兼容的或基于Docker的([Docker](https://www.docker.com/?utm_content=inline-mention) Hub、Docker Registry和Dockerfile)，但服务器可以存在于多个云提供商上。Cycle现成支持AWS、[Equinix Metal](https://metal.equinix.com/?utm_content=inline-mention)、GCP和Vultr，尽管Microsoft Azure计划支持但尚未可用。

此外，Cycle称之为基础架构抽象层(IAL)的组件，允许组织通过实现一个薄的基于REST的中间件来添加对另一个云提供商或内部部署基础设施的支持。值得注意的是，服务器需要基于x86(ARM尚不支持)，至少有4GB RAM和30GB+的磁盘空间。

在每个计算节点上，Cycle会自动安装自己的最小Linux派生操作系统CycleOS，它提供基本的网络、存储协议和运行在其上的容器层的插件。“它有意设计得尽可能简单，”Warner解释道。

从概念上说，CycleOS让人联想到[CoreOS](https://fedoraproject.org/coreos/)，但它采用了一种与部署基础设施完全不同的方法。每次服务器启动时，它都会连接到Cycle并拉取OS的副本，然后在RAM中运行——它从不安装到磁盘。这是Cycle能够管理基础设施的一部分。“它给我们的是基础架构标准化，我们可以保证每个服务器都运行完全相同版本的CycleOS和经过硬化的Cycle内核，而不管提供商的基本镜像，”Warner说。“这允许我们每两周推出一次更新，而不会引入不兼容或宕机时间。这使我们能够构建一个完全托管的平台，一个类似Heroku的用户体验，组织能够拥有他们的基础架构、网络和数据。”

在Cycle中，基础架构分组到集群中，应用程序隔离到环境中。集群提供了基础设施的隔离、资源管理和高可用性的途径。类似地，环境为容器到容器通信提供全局加密的私有网络，并可以跨越集群内的所有基础设施，而不管底层提供商。在环境内部，Cycle提供了许多内置的、完全托管的服务，包括：负载均衡、服务发现、VPN等。

深入研究环境，Cycle为每个环境配置一个全局二层网络，该网络内的所有流量都是加密的，并为环境内的所有容器配置一个相应的全局IP子网。该平台会自动处理设置此内容的细节。例如，在构建网络时，它会运行一系列测试，以查看节点是否需要带外连接，或者是否有Direct Connect可用；如果后者是一种选择，Cycle将默认使用它。

服务器被划分为命名的集群——例如，您可能有生产和开发集群——计算资源可以跨越不同的提供商(比如AWS、GCP和Vultr)，而无需用户做任何事情。

此外，有趣的是，尽管它需要计算节点之间合理的网络连接性，但该平台不对它们施加时延限制。由于它们各自的控制平面如何工作，Kubernetes和Docker Swarm实际上都施加了时延限制，这就是为什么我们通常看到所有内容都在单个区域运行。使用Cycle模型，客户不负责管理控制平面，这意味着Cycle作为一家公司可以在控制平面层管理时延。也就是说，您的应用程序可能有时延限制，您需要考虑这一点——通过可自定义的节点约束/标记，Cycle仍对这些要求友好。

## Cycle适合哪里？

当你花时间使用Cycle时，会变得明显的是设计和构建它的人们在基础设施上花费了大量时间，所以已经考虑过许多更小的细节和常见问题。

我们已经看到一个例子，即如何管理网络。该平台还内置了从一个云提供商迁移实例到另一个云提供商的机制；在此过程中，它会自动重新配置网络。此外，如果需要移动数据，它会通过流式传输来处理——将数据分成块，然后发送。如果你像我一样，当磁盘快满时，在不同机器之间移动数据会很头疼，那么你就会欣赏Cycle这种做法的好处。

此外，自动更新意味着任何运行在平台上的应用程序都将使用最新稳定版本的Cycle以及应用所有安全补丁，这对于运行Kubernetes的公司可能是一个挑战。

在高层次上，这种多云支持、设计周到的功能和易用性的组合非常吸引人。Warner告诉The New Stack，他们看到越来越多的客户从Kubernetes迁移到Cycle。事实上，他告诉我们，“今天迁移到Cycle的大多数公司正在摆脱Kubernetes。他们花时间采用并多年使用它，但意识到维护它的成本不值得它提供的价值。” 就规模而言，Warner告诉我们，移动到Cycle的平均公司有15到25名开发人员。

我个人的看法是，Cycle最适合认识到容器是将应用程序打包并部署到服务器的方式的价值的团队，但不一定坚持Kubernetes的方式，可能还没有建立DevOps或平台团队。我认为它的[定价](https://cycle.io/pricing/)通常在每月500至6000美元之间，提到了初创公司的折扣并非巧合。

Kubernetes是由[谷歌设计](https://thenewstack.io/google-learned-borg-container-management/)的，用于操作其庞大的业务属性，而我们中的许多人不需要那种规模。然而，我们通常不会质疑这一点，因为Kubernetes已经变得无处不在。我们可能会看到Cycle占据比我们以往想象的更大的市场份额。

声明：本文作者曾为cycle.io做过一些咨询工作。
