<!-- 
# Kubernetes之后的Moby项目: 2023年有3个新版本
https://cdn.thenewstack.io/media/2023/10/d2c35253-mobyprojectphoto-1024x591.png
 -->


*Docker工程师Sebastiaan van Stijn(左)和Bjorn Neergaard就Moby项目进行演讲。图片来源:Loraine Lawson。*

译自 [The Moby Project Post-Kubernetes: 3 New Releases in 2023](https://thenewstack.io/the-moby-project-post-kubernetes-3-new-releases-in-2023/) 。Moby 项目继承了 Docker 的运行时部分，也在不断的进步。

开源Moby项目的最后一个主要版本发布于2020年，但根据两名Moby项目贡献者透露，今年将会有3个主要版本发布。

[Moby项目](https://github.com/moby/moby)是一个组件集合，可以用来构建基于容器的系统，包括容器运行时、[容器镜像仓库](https://thenewstack.io/trow-a-container-registry-to-run-inside-a-kubernetes-cluster/)、容器构建工具、编排工具以及网络、日志和监控工具。这些组件可以用于构建基于容器的系统，如云原生应用程序、[微服务架构](https://thenewstack.io/in-the-great-microservices-debate-value-eats-size-for-lunch/)、[CI/CD流水线](https://thenewstack.io/kubernetes-ci-cd-pipelines-explained/)以及内部容器平台。

Moby项目维护者[Bjorn Neergaard](https://github.com/neersighted)是Docker的高级软件工程师。技术指导委员会成员[Sebastiaan van Stijn](https://github.com/thaJeztah)也是Docker的软件工程师，他们本月早些时候在[DockerCon](https://thenewstack.io/docker-launches-genai-stack-and-ai-assistant-at-dockercon/)上就Moby项目进行了演讲，详细介绍了2023年的主要版本发布计划以及未来规划。

## Moby项目前史

Neergaard和van Stijn从Moby作为开源项目的简史开始他们在DockerCon的演讲。根据van Stijn介绍，其历史可以追溯到开发者第一次将容器作为轻量级虚拟机使用的时期，这些虚拟机使用起来非常困难，且非常小众。

“它并未被广泛使用，因为过于复杂。” van Stijn说，“保持各组件同步很困难；也没有镜像发布或类似机制。”

后来dotCloud公司，一个小型平台即服务供应商，推出了服务。但是，真正吸引技术人员的是dotCloud在后台所做的工作: 他们在部署基于Python的技术容器，需要大量脚本才能让容器工作，van Stijn解释说。dotCloud决定开源他们内部使用的技术。

2013年，Docker创始人Solomon Hykes在PyCon上进行闪电演讲，首次介绍了Linux容器。

van Stijn说: “他的演讲只有5分钟，但在业内引起了相当大的反响，因为在那5分钟里，他第一次演示了docker run命令。”“Docker run命令完成了他原本需要通过LXC完成的许多工作，但只需要单个命令。”

当时Docker还只是LXC的封装，是LXC完成了繁重工作。它提供了易用的用户体验，也提供了镜像格式——这是重大进步，因为开发者现在可以使用镜像而不是为容器创建自己的文件系统。当时还没有构建功能。它还提供了API，让开发者可以做“很酷的事情”，他补充说。

“它对市场产生了重大影响，因为第一次将Linux容器变成现实，到达开发者手中。”他说。

LXC可以工作，但Docker决定重写运行时，在Docker引擎中创建一个本地运行时，van Stijn说这对后来添加更多功能(如网络)非常重要。容器开始普及，但每个容器只执行单一任务，这意味着开发者需要多个容器。这导致了早期的编排尝试，后来演变为Compose，允许定义[YAML](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/)文件。

Docker收购了Fig，成为Docker Compose。然后Docker启动了Swarm，1.0版本允许开发者在机器集群上运行容器。后来Kubernetes出现，决定使用Docker作为运行时，因为它已成为运行容器的事实标准，van Stijn说。这带来一个小问题，因为越来越多的人请求明显超出项目范围的功能，他补充说。

“Kubernetes不需要Docker的网络栈或我们提供的其他功能，但他们仍在使用运行时，有时会遇到挑战。” 他说，“作为一个庞大的引擎变得越来越成问题。”

此外，虽然Docker是事实上的标准，但是没有正式的容器镜像规范或运行时应有的行为规范，他说。

“实现就成了规范，这并不总是理想的。”

Docker决定将实际运行时拆分出来。与此同时，OCI标准组织启动。Docker捐献了它一直在使用的镜像分发和运行时规范以及镜像规范。

“这使得不仅仅是Docker，其他人也可以实现运行时、镜像和注册表。”

Docker还与合作伙伴从零开始重写了运行时，这导致了containerd(发音为“container D”)，这是Docker运行时部分的完全重写。

## Moby项目的诞生

当Docker决定进一步拆分项目，使其成多个组件时，Moby项目启动，因为人们想使用containerd和Docker引擎的其他部分，van Stijn向听众表示。这导致了构建套件用于构建，Swarm Kit用于编排，以及Docker引擎。CLI成为独立项目的一部分，集成到Docker产品中，他补充说。运行时本身成为了Moby项目。

“这可以让其他人在其上构建、参与，也使接受可能不直接使Docker产品受益但可能被其他人使用的更改变得更容易——反之亦然。” 他说。

Docker自己也转型，企业产品转移到Mirantis，Docker回归开发者导向的产品。Docker专注于桌面产品，Moby项目进展放缓，直到过去18-24个月，当Mirantis和Microsoft的维护者加入努力时，情况有所改善，他补充说。

Neergaard解释说:“困扰人的是，大家所知道的开源Docker代码发生了什么变化。” “但这也有助于解释，项目的利益相关方不仅仅是Docker公司，还有更多参与其中的人——不仅仅是参与者。”

除Mirantis和Microsoft外，[Nvidia](https://thenewstack.io/nvidia-uses-openstack-swift-storage-as-part-of-its-ai-ml-process/)最近也为容器设备接口贡献了支持，Neergaard补充说。

## 当前进展

Neergaard说:“最近一段时间里，我们看到项目中出现了许多活动。” “这以各种形式呈现，但交流可能还不够理想。”

![Moby项目最近的进展](https://cdn.thenewstack.io/media/2023/10/3481529d-moby-recent-activity.png)

*Moby项目最近的活动*

Docker引擎的最后一个主要版本发布于2020年。从那时到现在，有大量代码和改进从未发布。他补充说。

今年已经有两个主要版本——23.0和24.0版本，主要特性是:

- BuildKit默认启用(不再需要设置DOCKER_BUILDKIT=1)。Neergaard说，BuildKit重写了构建器。“BuildKit的原始任务是取代Docker引擎中的旧构建器，提供更丰富、更灵活的构建平台，仍保持Docker构建的简单性。” 因此，BuildKit现在默认启用。
- 在Swarm中启用了CSI(容器存储接口)
- 可选的containerd shims:
  - [gVisor](https://thenewstack.io/how-to-implement-secure-containers-using-googles-gvisor/)
  - [Kata容器](https://thenewstack.io/the-road-to-kata-containers-2-0/)
  - [WebAssembly](https://thenewstack.io/what-is-webassembly-wasm/)
- 容器

Neergaard说，可选的[shims](https://stackoverflow.com/questions/2116142/what-is-a-shim)“可能看起来无聊”，但为各种可能性开启了大门，“特别是为了以新的方式运行容器或类容器，如WebAssembly”。

团队希望在DockerCon之前发布第三个版本25.0，但没有实现。根据演示，预计它将很快发布。该版本将包含：

- CDI(容器设备接口)
- 将OTEL([OpenTelemetry](https://thenewstack.io/what-is-opentelemetry/))集成到引擎中
- “平稳”运行状况检查，具有health-start-interval，Neergaard说这一直是一个让人头疼的问题。

“我认为我们今年会发布引擎的3个版本，但每次发布仍然是一个巨大的挑战；我们每次都在进步。” Neergaard说。

“另一件有趣且让人惊讶的事情是，Docker Swarm中仍在添加新功能。” 他说Swarm是Docker对Kubernetes的响应。

“现在我会说，Kubernetes无疑已经成为编排的事实标准，除非你有很好的理由，否则不应该选择Kubernetes之外的方案。” Neergaard说。“有一小部分但仍然非常喜欢使用Swarm的用户，希望Swarm能做更多事情，甚至与Kubernetes的各种插件和扩展兼容。”

Moby项目的未来计划还包括在containerd中添加多个快照器和原生多架构支持，重新设计CLI，以及网络错误修复和新功能，将协调器逻辑从Compose移动到守护进程以实现声明式Docker等，两人补充说。
