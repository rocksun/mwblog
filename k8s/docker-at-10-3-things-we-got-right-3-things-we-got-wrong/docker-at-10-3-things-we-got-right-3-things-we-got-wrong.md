<!-- 
# Docker十岁了 - 我们做对了三件事，做错了三件事
https://cdn.thenewstack.io/media/2023/10/96740011-docker-logo-1024x683.jpg
Image from rafapress on Shutterstock.
 -->

Docker最近庆祝了10岁生日。回顾变革之路，你会看到自己做对的事情，也会看到自己做错的事情。

> 译自 [Docker at 10 — 3 Things We Got Right, 3 Things We Got Wrong](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/) 。作者是 [Sam Alba](https://thenewstack.io/author/sam-alba/)，Docker 的第一个员工，Docker 产品和工程团队的领导者。

Docker最近庆祝了10岁生日。我对Docker团队取得的所有成就感到无比自豪，今天的团队仍在不断创造奇迹。如果不是[容器](https://thenewstack.io/containers/)成为新的计算单元，我们现在看到的许多事物都不会存在，比如[基于微服务的架构](https://thenewstack.io/microservices/microservices-101/)、Kubernetes等等。当然，重大变革中也免不了会有做对和做错的地方。让我们来看看这些吧。

## 我们做对了的3件事

### 容器将改变世界

2010年，我[和Solomon Hykes](https://thenewstack.io/solomon-hykes-leader-open-source-world-needs/)一起建立了DotCloud(后改名为Docker)。很快我们意识到，如果仍然使用当时的工具，我们的愿景将无法实现。DotCloud是第一个支持任何语言的平台即服务(PaaS)，而当时Heroku等只支持单一语言。构建DotCloud时，我们立即遇到的瓶颈是当时基础设施的构建块仅有虚拟机(VM)这一选择。虽然虚拟机相比裸机服务器是一个巨大进步，但对我们实现云原生时代的敏捷性还是不够。我们需要更轻量级的东西，才能在一台机器上为客户提供隔离的计算、网络、存储资源，并容纳数百个开发者应用。这成为了微服务模式的开端。当时虚拟机仍是基础架构可重复使用的最新技术，容器技术还相当晦涩，只有少数爱好者在使用(还记得当时[LXC](https://linuxcontainers.org/lxc/introduction/)需要内核补丁才能连接运行中的容器吗？)，还有些人认为解决方案是让虚拟机瘦身（还记得JeOS吗？）。尽管困难重重，我们认为这项事业值得全力以赴。事实证明，我们的判断是正确的。几年后，我们从DotCloud平台中提取了一个核心组件：[容器运行时](https://thenewstack.io/choosing-an-operating-system-and-container-runtime-for-your-cloud-native-stack/)。我们对其进行重写并开源，这就是Docker的第一个版本。最初的目标是使Docker成为从DotCloud中提取的多个开放组件之一。容器编排器、网络层也将很快面世。但由于Docker在早期就获得了广泛关注，计划被迫做出调整。

### 开发者，开发者，开发者

Steve Ballmer是正确的。VMware主要专注于解决IT问题，而我们很早就意识到，改变世界的方法是关注全球的软件开发者。你必须改变软件的构建方式，而不仅仅是运维方式，这意味着要从开发者的需求出发。作为一个管理过数以千计开发者的人，我深知软件开发者每天面临的挑战。这可能是世上最激动人心的工作之一，不仅充满富有挑战性的问题，成功创造某些伟大事物也能带来满足感，但它也可能乏味重复、令人沮丧，有时候甚至让人恼火。基础设施和工具取得了巨大进步，但期望也在不断提高。Docker的指导方针是减少开发者的分心和额外开销，让开发者能保持高效协作。我们的首批收购(及成功的产品整合)之一就是一个名为“Fig”的产品，后来演变成Docker Compose，最初是由Ben Firshman开发的，他现在是Replicate的创始人，还有Anand Prasad。有趣的是，Fig实现的[YAML模型](https://roadmap.sh/videos/yaml-in-depth)(compose.yml)直接受到我们多年前构建的第一个DotCloud服务组合(dotcloud.yml)的启发。虽然我们已经取得很大进展，但在这方面还有更多工作要做，特别是要超越仅以容器作为单元，实现容器流水线的编排。这也是我们在2018年启动Dagger的原因之一，[它是一个可编程的CI/CD引擎](https://thenewstack.io/solomon-hykes-dagger-brings-the-promise-of-docker-to-ci-cd/)，使用容器运行流水线。

### 投资建立活跃社区

我们从一开始就致力于建立一个伟大的社区。从第一天起，我们就明白没能赢得广大群众的支持，我们单枪匹马无法达成目标。关键是要放手许多事情的所有权。DockerCon成为我们这个行业中众多顶尖人才的聚集地，一个人们因共同的变革愿景而团结一致、乐于付出的地方。在Docker初期，当我们考虑自己举办开发者会议时，这看起来像个遥不可及的梦想，因为这么做要么只适合大公司，要么需要成熟许多的开发者社区支持，比如PyCon。但当我们2014年6月在旧金山举办第一个DockerCon，聚集了一些天才开发者后，很明显这只是开始，未来会变得更大，并改变整个公司和行业。这种开创精神至今仍在我们看到的数十个(甚至数百个)开源项目和社区中强烈存在。云原生计算基金会现在托管其中许多项目，每天还在涌现更多新项目。

## 我们做错了三件事

### 采用与变现的矛盾

“社区至上”的另一面是我们花太长时间建立可持续的商业模式。我们的偏见是公开做所有事情，认真倾听社区需求，尽最大努力满足他们。这一策略的初衷是开源项目和商业专有解决方案可以很好地共存，并成为客户需求变化的一部分。我今天仍然相信这个模式，但平衡是很微妙的。首先，你必须接受一些开源贡献者和用户永远不会成为客户，只要他们参与建设强大的社区和品牌，这就是对商业市场的贡献。其次，产品架构必须能在核心开源基础上构建企业级功能。这通常需要复杂的支持和发布流程。在建立可靠的商业模式方面，我们显然可以更战略性一些。最终，我们做到了，但花了太长时间，过程中常感到担忧。

### 团队文化

我们没有及早定义团队文化和核心价值观。这些后来是由社区或后来加入公司的人定义的。这导致我们的团队文化从早期起变化剧烈，起初这并不明显。我们的文化反映了社区中人们的风格和价值观，而不是反过来影响社区。我们做错的一个具体例子是公司内有两组人——一组专注开源和社区，另一组专注商业。这是我最大的遗憾之一。它导致内部工具、产品和项目管理以及最重要的团队文化出现分裂。平衡这些竞争利益对任何人来说都是很难的，但当你分割角色时，你最终会遇到内部战斗、不一致并公开无法解决的辩论(从每个人的角度来看都是正确的)。许多最出色和最聪明的人都想在社区方面工作，在我们的许多协作中，对另一方常带明显的(或不那么明显的)判断。有时，感觉就像我们把“开源教徒”与“企业暴发户”对立起来。这并不高效。拥有活跃的社区和可持续的商业需要集成团队，每个人都努力平衡我们模式天然产生的固有紧张关系。这也能创造出更好的团队文化。无论在公司哪个部门工作，都只有一套目标值得关心。

### 以容器为宇宙的中心

当我退一步审视时，意识到我们过度依赖容器。我们开始把容器看作大多数问题的核心解决方案，这使我们盲目于开发链条的其他需求。Docker之所以诞生，是因为我们看到容器将为我们的行业带来一系列必要的变革，但随着事态发展，我们没有关注后续需求。由于未能解决这么多需求，我们给其他厂商进入这些领域创造了空间。一方面，这留下了巨大机会，但另一方面也意味着社区碎片化。Docker未能解决的一个挑战是软件供应链的整体自动化。我们在供应链末端解锁了巨大价值，但没有充分解决开发人员在编写代码和协作中的需求，如今CI/CD仍一团糟。但这是可以解决的烂摊子。与那个时代的许多其他人一样，Solomon Hykes, Andrea Luzzardi和我在反思Docker经历后，意识到我们的革命还未完成，于是找到了未来十年的使命。