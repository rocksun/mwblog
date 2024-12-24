
<!--
title: 平台工程师为何拥抱用于无服务器的WebAssembly
cover: https://cdn.thenewstack.io/media/2024/10/85daa094-mohammad-rahmani-8qeb0fte9vw-unsplash-scaled.jpg
-->

从 AWS Lambda 到 SpinKube，WebAssembly 引入了服务器端无服务器计算的演变，具有无与伦比的启动速度和基础设施灵活性。

> 译自 [Why Platform Engineers Are Embracing WebAssembly for Serverless](https://thenewstack.io/why-platform-engineers-are-embracing-webassembly-for-serverless/)，作者 Matt Butcher。

近年来，对 WebAssembly ([Wasm](https://thenewstack.io/webassembly/)) 的热情不断高涨。虽然[一些 Wasm 的活力仍然存在于](https://thenewstack.io/step-by-step-guide-to-using-webassembly-for-faster-web-apps/)浏览器领域，但更多关注点集中在服务器端的 Wasm 上。

微软、Cloudflare、SUSE、Docker、Red Hat 等业界巨头都推出了 Wasm 产品或集成。多个开源项目正在通过 CNCF 的项目路径，开发者兴趣也激增。例如，用于构建无服务器应用程序的开源[Spin 工具包](https://www.fermyon.com/spin) 的下载量已超过 230,000 次。

这对平台工程意味着什么？我们将看到 Wasm 应用程序部署在哪里？

## 为何选择服务器端？

虚拟机定义了早期云计算。其价值主张清晰明了：将操作系统和应用程序打包到虚拟机中，并在其他人的硬件上安全地执行它们。十多年前，像 OpenStack 这样的开源平台加入了不断壮大的云提供商行列，使大小组织能够运行其基础设施，而无需拥有自己的硬件或租赁数据中心机架空间。

虚拟机虽然功能强大，但也有一些缺点，引起了开发人员和 DevOps 人员的强烈不满。机器映像构建、部署和启动速度慢，并且给负责构建 VM 映像的[团队](https://thenewstack.io/is-security-a-dev-devops-or-security-team-responsibility/)或个人带来了巨大的[安全和维护负担](https://thenewstack.io/is-security-a-dev-devops-or-security-team-responsibility/)。

对于那些重视经验和易用性的人来说，Docker 容器的迅速崛起并不令人意外。[Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) 使构建映像变得轻松且对开发人员具有吸引力。更高层次的抽象和更小的依赖项集减少了维护负担，并将其分散到相关责任方。容器的启动时间仅为十几秒，而不是几分钟。

然而，热情却过高了。容器技术的早期支持者声称这是虚拟机的丧钟。当 Kubernetes 出现时，事实证明恰恰相反：虚拟机和容器可以和谐共存。当今绝大多数 Kubernetes 集群都将虚拟机分配为节点，然后将这些虚拟机打包成容器。

尽管容器很有用，但它们并不能解决现代云计算的所有问题。它们非常适合预期寿命为数小时、数天或数月的长期运行进程。然而，随着一种名为“无服务器函数”的新开发模式越来越流行，容器的弱点也暴露无遗。

无服务器函数作为一种事件驱动型应用程序。无服务器函数不是启动处理其漫长生命周期内数十万（甚至更多）请求的长期运行守护进程，而是只处理一个事件——一个请求。它在收到事件时启动，执行所需的任何处理，返回响应，然后关闭。从操作角度来看，此模型的优点是，在不处理请求时，几乎不使用或根本不使用系统资源。理想情况下，无服务器函数更高效、更便宜且更易于管理。但这需要正确的运行时。第一代无服务器并没有做到这一点。

容器和虚拟机都针对长期运行的进程进行了优化。因此，如果它们的启动时间为一分钟或几十秒，则编排逻辑通常会吸收该成本。但是，对于无服务器函数来说，启动时间为几分钟甚至几秒钟都是不可接受的，尤其对于前线服务而言。用户根本不会等待响应。

已经尝试了许多方法来解决这些限制，最常见的是“预热”虚拟机或容器，以便它们空闲地排队等待请求。但这效率低下，导致无服务器函数的运营成本上升。

需要的是一个能够在毫秒内启动的隔离且安全的运行时。Wasm 正是这样一个运行时。

## 与您的容器一起

凭借亚毫秒级的启动时间和比容器更强大的安全模型，Wasm 成为沙盒化运行短生命周期进程（例如无服务器函数）的理想环境。许多开源工具（包括 Spin 和 Wasmtime）已发展到可在云环境中执行 Wasm 函数，这不足为奇。与 AWS Lambda 或 Azure Functions 等云特定解决方案相比，无服务器 Wasm 更高效、更经济。但是，没有理由将 Wasm 与容器对立起来——它们可以协同工作。

无服务器函数非常适合许多应用程序，但并非所有应用程序都适用。它们可以提供更便宜、更简单的微服务、Web 后端、API 服务器和批处理处理器。但是，许多服务需要始终运行，持续保持线程池工作。数据库、消息队列和遗留应用程序就是其中的例子。

容器为始终在线的服务器提供了极好的基础技术。为了兼顾无服务器和始终在线的使用案例，系统应该能够同时运行容器和 Wasm 工作负载。

我们已经拥有大量的容器环境，从本地端的 Rancher Desktop 和 Docker Desktop 到云端的 Kubernetes 和 Nomad。从另一个专门用于无服务器 Wasm 的编排器开始，将会在已经复杂的运行环境中引入更多操作复杂性。将 Wasm 运行器集成到这些现有环境中要容易得多。

在桌面上，Rancher Desktop 和 Docker Desktop 都支持运行 Wasm。SpinKube 将 Wasm 支持引入 Kubernetes，提供在同一 Pod 中并排运行容器和 Wasm 的功能。即使是企业级的 Nomad 也能将任务调度到 Wasm 运行时。无论您的基础设施投资如何，如果您正在运行容器，那么在相同的服务中运行 Wasm 也并非难事。

SpinKube 今年早些时候提交给 CNCF 沙盒项目，它集成了 Containerd shim、一些操作符和新的 CRD，以直接向 Kubernetes 添加 Wasm 支持。SpinKube 集群不仅没有引入性能开销，而且可以在一个 8 节点的 Kubernetes 集群上托管数千个 Wasm 应用程序，并每秒处理数十万次无服务器函数调用。

## 无服务器的演进

AWS 使用 Lambda 推出了第一波无服务器函数。十年后，是时候进行全面的技术升级了。借助基于 Wasm 的无服务器函数和 SpinKube 等项目，可以使用无服务器函数设计模式运行前沿 Web 应用程序。

由于 Wasm 的可移植性和 Wasm 平台的开源特性，不再存在云锁定。可以在任何运行 Kubernetes 的地方、任何运行容器的地方，甚至在像 Raspberry Pi 这样的小型裸机上运行它们。而 Wasm 超快的亚毫秒级冷启动时间意味着，不仅可以将您性能要求最高的 Frontend 工作负载作为 Wasm 运行，即使是您很少访问的应用程序也可以安装到 Kubernetes 集群中，而不会一直占用资源。

Wasm 吸引了许多服务器端开发人员的注意，因为其工具易于使用且运行简单。然而，Wasm 的运行时特性使其成为与当今现代云中的容器结合使用时的一项强大技术。
