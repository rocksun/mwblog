Dragonfly 项目，一个开源的对等（P2P）镜像和文件分发系统，[已从](https://www.cncf.io/announcements/2026/01/14/cloud-native-computing-foundation-announces-dragonflys-graduation/) [云原生计算基金会](https://cncf.io/?utm_content=inline+mention)孵化新云原生技术的项目中毕业。

据该组织称，这项[开源技术](https://github.com/dragonflyoss/dragonfly)自[2018年](https://www.cncf.io/projects/dragonfly/)起在CNCF的支持下，已证明其在生产环境中可行，能够大规模地在网络中复制容器和大型AI模型。它被构建为运行在 [Kubernetes](https://thenewstack.io/kubernetes/) 上，已被管理大规模AI工作负载的组织所采用，并在其他环境中也找到了用武之地，包括 [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) 和 [边缘计算](https://thenewstack.io/edge-computing/)。

CNCF [Dragonfly](https://d7y.io/) 最初由 [阿里云](https://www.alibabacloud.com/) 内部开发，为[组织提供了一种](https://thenewstack.io/dragonfly-brings-peer-to-peer-image-sharing-to-kubernetes/)在网络中分发镜像的方式。它能几乎同时将容器镜像复制到数千个节点。

它也适用于文件、缓存和日志。

总体而言，来自130家公司的271位个人为该项目贡献了26,000次提交。

Dragonfly 创始人兼名誉维护者 Zuozheng Hu 在一份声明中表示：“回顾过去八年的历程，每一步都体现了开源精神和众多贡献者不懈的努力。”

## P2P 的力量

对等文件共享机制有助于云原生部署更快地在集群中分发新的和更新的容器镜像，并减少对上游网络的压力。

P2P 最早由 Napster 等音乐共享程序在二十多年前推广，它能充分利用集群带宽，同时消除单个服务器响应所有新镜像请求可能造成的瓶颈。

在P2P网络中，每个节点或“对等点”可以相互共享文件，而不是所有节点都通过下载单个镜像的相同副本而使镜像服务器的带宽饱和。

Dragonfly 并非纯粹的P2P技术；它仍然需要一个超级节点来调度和控制对等网络内的分发。每个节点上的代理，`dfget`，下载文件块。另一个组件，`dfdaemon` 代理，拦截来自容器引擎到 `dfget` 的镜像下载请求。

## Dragonfly 强大的支持堆栈

作为一个CNCF项目，开发团队在过去十年中建立了一个强大的支持堆栈。Dragonfly 可以通过 [Helm](https://artifacthub.io/packages/helm/dragonfly/dragonfly) 安装，并使用 [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) 和 [OpenTelemetry](https://thenewstack.io/can-opentelemetry-save-observability-in-2026/) 进行监控。

为了加快传输速度，它可以在 [gRPC](https://thenewstack.io/grpc-a-deep-dive-into-the-communication-pattern/) 协议上运行。镜像可以通过 [Harbor 开源注册中心](https://goharbor.io/docs/2.12.0/working-with-projects/working-with-images/preheat-images/) 进行“[预热](https://goharbor.io/docs/2.12.0/working-with-projects/working-with-images/preheat-images/)”以实现更快的共享。

Dragonfly 还支持CNCF的 [ModelPack 规范](https://github.com/modelpack/model-spec)，以实现更整洁的AI模型分发。

Dragonfly 的一个子项目，名为 [Nydus](https://nydus.dev/)，通过进一步加速模型分发，为该软件带来了可观的价值。

Nydus 维护者 Jiang Liu 在一份声明中表示：“Dragonfly 和 Nydus 的结合大大缩短了容器镜像和AI模型的启动时间，提高了系统的弹性和效率。”

## Dragonfly 的用例

Dragonfly 已在一些最具创新性的 [云原生服务](https://thenewstack.io/cloud-native/) 中找到了用武之地，其中许多位于亚洲。CNCF 提供了一些关键示例。

它已成为阿里巴巴容器镜像和数据分发系统的核心组件，为一年一度的双11（光棍节）购物节提供支持，并在模型数据分发和缓存加速方面发挥着持续作用。

它为亚洲金融公司 [蚂蚁集团](https://www.antgroup.com/en/home) 的10,000个 Kubernetes 节点节省了大量传输带宽。特别是 Nydus 帮助该组织将镜像拉取时间缩短到接近零，并且该技术也用于大型语言模型的移动。

对于 [Datadog](https://thenewstack.io/is-datadog-becoming-a-platform-engineering-company/) 可观测性公司，Dragonfly 与 Nydus 的结合将节点守护程序集启动时间缩短到几秒钟内，而此前镜像拉取会使该时间延长到五分钟。

中国移动技术公司 [滴滴](https://web.didiglobal.com/) 使用 Dragonfly 进行企业级大规模文件同步和镜像分发。

而容器注册服务 [快手](https://www.cncf.io/case-studies/kuaishou-technology/) 即将使用 Dragonfly 来支持数万个服务和数十万台服务器的镜像分发能力。