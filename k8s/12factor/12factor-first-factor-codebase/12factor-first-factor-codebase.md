<!-- 
# 12 factor 微服务应用 - 基于Kubernetes
TODO
 -->

12 factor 方法已广泛用于构建现代、可伸缩、易维护的应用程序。虽然这些原则有大量的相关知识，但常常缺乏在微服务上下文中实施它们的实际指导。本文旨在填补这一空白。我们将探讨如何利用 12 factor方法来设计微服务，工具选择以及如何在 Kubernetes 上引导 12 factor微服务应用程序。

译自 [12 factor Microservice applications — on Kubernetes](https://itnext.io/12-factor-microservice-applications-on-kubernetes-db913008b018) 。

## 挑战和目标

我们的目标明确但具有挑战性：我们的目标是启动一个带有仪表板的 12 factor 微服务应用程序，并确定执行此任务所需的最精简工具集。所选工具应符合 12 factor方法的原则。

## 第一因素：代码基

> 一个代码基，多次部署。

12 factor 方法的第一因素规定要求“版本控制跟踪一个代码基，多次部署”。

为了管理我们的代码库，我们需要一个版本控制系统（VCS）！版本控制系统对于任何现代软件开发过程都是至关重要的。它们帮助团队随着时间的推移管理源代码的更改，允许多人协作，跟踪修改，并在必要时还原更改。

在选择合适的 VCS 时，有几个要考虑的因素，其中主要的因素包括：

- **分支**：这是版本控制系统的核心功能之一，允许开发人员从主要开发线路分叉，并创建独立的环境以处理功能或修复错误。每个分支代表一个独立的开发线路，不会影响其他分支，允许多个开发人员同时处理不同的功能。
- **Action 和 Workflow**：将分支与策略（如 Action 和/或 Workflow ）相结合时，分支变得更加强大。这些策略定义了代码库提交时执行哪些步骤方法以及如何执行它们。
- 其他因素：易用性、社区支持以及集成。

为此，我们将使用 Git（Hub），结合 Git Actions 和 Git Workflows。

## Git 在我们的设计中的角色

在我们的设计中，后端和前端开发人员将使用 Git，并将其扩展使用。

**后端**开发人员将在应用程序中编写业务逻辑，可以使用任何喜欢的编程语言进行编码。开发过程将包括

- 在“特性（feature）”环境中创建应用程序的框架，
- 首先编写测试（一种称为测试驱动开发或 TDD 的实践），
- 编写业务逻辑（business logic, BL），然后
- 最后提交拉取请求（Pull Request, PR）。

**前端**开发人员将遵循类似的模式，使用应用程序提供的 API 编写前端业务逻辑。与后端一样，前端应用程序可以使用任何语言进行编码，需要创建框架，并遵循类似的分支和提升标准。

我们将为每个微服务和前端应用程序创建一个 Git 存储库。这允许我们在开发拓扑中使用像 development、staging 和 main（或必要时的 feature 分支）等分支。每个微服务将拥有“部署清单”，除了实际源代码之外还需要这些清单，以便将应用程序部署到 **Kubernetes**。

## Docker 和 Docker 镜像仓库

在这里需要做一个必要的绕行，先说一下 Docker 及其用于托管应用程序镜像的镜像仓库！

**Docker** 是一个旨在自动化应用程序的部署、扩展和管理的开源平台。它使用容器化技术，将应用程序及其依赖项封装到标准化的软件开发单元中，并确保应用程序能够在任何环境中无缝运行，无论是本地计算机、私有数据中心还是公共云。

Docker 通过使用轻量级容器运行时来实现这一目标，将应用程序的进程与系统的其他部分隔离开来。每个 Docker 容器都能独立运行，并包含运行应用程序所需的一切：代码、运行时、系统工具、库和设置。

Docker 镜像仓库是用于存储和分发命名 Docker 镜像的存储和分发系统。这些镜像是 Docker 容器的构建块。它们包含了应用程序、其依赖项以及描述容器运行时应执行何种操作的一些元数据。

任何 **Docker 镜像仓库**的关键功能包括：

- **版本控制**：每次将镜像推送到仓库时，都会创建一个新版本。这允许您在需要时还原到早期版本。
- **访问控制**：您可以控制谁有权读取或写入仓库，以及他们可以执行什么操作。
- **集成**：Docker 镜像仓库可以与您的 CI/CD 流水线集成，确保用于部署的镜像始终保持最新。

如果 Docker 镜像是软件打包的手段，那么下一个自然的问题是，如何部署 Docker 镜像？它们将在多个环境中运行，比如 stage、qa、production，怎么做呢？

如果没有一种部署 Docker 镜像的方法（以容器形式运行它们），那么镜像本身就没有用处。那么“部署 Docker 镜像的方法”是什么意思呢？

**“部署 Docker 镜像的方法”的要求**

- 一种指定在哪里运行 Docker 镜像的方法——将 Docker 镜像部署到的虚拟机集合
- 一种指定如何运行 Docker 镜像的方法——运行镜像所需的资源（例如内存/CPU/GPU、磁盘等）
- 一种将流量路由到 Docker 容器的方法（nginx-ingress）
- 一种监视 Docker 容器是否健康的方法（健康检查）
- 一种在 Docker 容器失败或崩溃时重新启动它的方法（滚动升级、重启）
- 一种维护容器的一组所需副本的方法

以上所有功能都是成功部署 Docker 镜像的最低要求。这个“部署 Docker 镜像的方法”称为**容器编排**，我们使用 **Kubernetes** 来实现这一切。

## 拥抱 Kubernetes

在我们的设计中，我们选择了 Kubernetes 作为我们的微服务编排平台。[Kubernetes](https://kubernetes.io/) 是一种用于自动化部署、扩展和管理容器化应用程序的开源系统。它提供了一个平台，可以弹性地运行分布式系统，根据需要扩展和恢复应用程序。

## 声明性指令

我们的应用程序清单是声明性的 YAML 文件，包含了有关我们的微服务的所有有用信息，包括：

- **应用程序元数据（名称、端口）**：帮助识别来自池中的特定微服务。
- **规格（副本、镜像、资源限制等）**：提供了大小和扩展信息。
- **Ingress 规则**：建立路由信息，以将传入请求定向到正确的 API 或前端应用程序。

我们将托管我们的应用程序清单在一个单独的 Git 存储库中。这种方法允许我们将包含实际源代码的存储库与包含基础设施的存储库关联起来，提供了明确的关注分离。

我们的自定义清单的目录结构如下：

```
~/manifests-index develop > tree -L 1 infra/k8s
infra/k8s
├── auth
├── auth-mongo
├── ingress
├── kafka
├── posts
└── posts-mongo
```

## 深入清单

在每个专为每个微服务（或其相关数据库）指定的文件夹中，我们将保留所有命名环境的自定义清单，包括 development, staging 或其他环境。

设计决策：使用 Kustomize 构建清单

我们选择使用 Kustomize 来“构建”我们的清单，这提供了一种无需模板的方式来自定义应用程序配置。它允许我们创建一组基本资源并根据每个环境的需要应用一组自定义项。

这是我们的 Kustomize 目录结构：

```
~/manifests-index develop > tree -L 4 infra/k8s/auth
infra/k8s/auth
├── README.md
├── base
│   ├── deployment.yaml
│   ├── kustomization.yaml
│   └── service.yaml
└── overlays
    └── development
        ├── build-version-patch.yaml
```

和 deployment, service 以及应用 kustomization！

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: auth-depl
spec:
  replicas: 1
  selector:
    matchLabels:
      app: auth
  template:
    metadata:
      labels:
        app: auth
    spec:
      containers:
        - name: auth
          image: xx-xxx-docker.pkg.dev/labs-xxxxx/auth/auth:development
          env:
            - name: API_VERSION
              value: 'v1'
            - name: MONGO_URI
              value: 'mongodb://auth-mongo-srv:27017/auth'
            - name: JWT_KEY
              valueFrom:
                secretKeyRef:
                  name: jwt-secret
                  key: JWT_KEY
```
```yaml
apiVersion: v1
kind: Service
metadata:
  name: auth-srv
spec:
  selector:
    app: auth
  ports:
  - name: auth
    protocol: TCP
    port: 3000
    targetPort: 3000

```

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
  - ../../base

namespace: development

patchesStrategicMerge:
  - build-version-patch.yaml
```

实际上，Kustomize build 应该为我们获取特定目标环境中的某个微服务的所有部署清单。

```bash
kustomize build infra/k8s/<microservice>/overlays/<overlay>
```

```bash
kustomize build infra/k8s/auth/overlays/development
```

为什么会有 build-version-patch.yaml？稍后会更多解释…

## 为什么需要 Ingress 和 Kafka 的清单？

我们将 `Ingress` 视为一个应用程序，提供细粒度的路由控制，允许我们为任何给定的分支或命名空间自定义路由规则。

将 `Kafka` 视为一个应用程序允许我们在每个命名空间中启动 Kafka 的一个实例（使用 [Strimzi](https://strimzi.io/)，后续会发布一篇文章介绍）。这种方法提供了一个可伸缩的、分布式的事件流平台，供我们的微服务用于通信。但请注意，根据命名空间托管 Kafka 可能会变得昂贵，因此较大的团队可能更喜欢使用一个集中的开发 Kafka 实例。

Ingress 和其基础！

```
~/_workspace/manifests-index develop > tree -L 3  infra/k8s/ingress
infra/k8s/ingress
├── README.md
├── argo
│   ├── base
│   │   ├── application.yaml
│   │   └── kustomization.yaml
│   └── overlays
│       └── development
├── base
│   ├── ingress-srv.yaml
│   └── kustomization.yaml
└── overlays
    └── development
        └── kustomization.yaml
```

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-service
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/use-regex: "true"
spec:
  rules:
    - host: dev.xxxx.io
      http:
        paths:
          - path: /api/v1/users/?(.*)
            pathType: Prefix
            backend:
              service:
                name: auth-srv
                port:
                  number: 3000
          - path: /api/v1/posts/?(.*)
            pathType: Prefix
            backend:
              service:
                name: posts-srv
                port:
                  number: 3000
          - path: /?(.*)
            pathType: Prefix
            backend:
              service:
                name: dashboard
                port:
                  number: 80
```

Kafka 和其基础！

```
~/_workspace/manifests-index develop > tree -L 3  infra/k8s/kafka
infra/k8s/kafka
├── argo
│   ├── README.md
│   ├── base
│   │   ├── application.yaml
│   │   └── kustomization.yaml
│   └── overlays
│       └── development
├── base
│   ├── deployment.yaml
│   ├── kustomization.yaml
│   └── topics.yaml
└── overlays
    └── development
        └── kustomization.yaml
```

```yaml
apiVersion: kafka.strimzi.io/v1beta2
kind: Kafka
metadata:
  name: kafka-cluster
spec:
  kafka:
    version: 3.3.1
    replicas: 1
    listeners:
      - name: plain
        port: 9092
        type: internal
        tls: false
      - name: tls
        port: 9093
        type: internal
        tls: true
    config:
      offsets.topic.replication.factor: 1
      transaction.state.log.replication.factor: 1
      transaction.state.log.min.isr: 1
      default.replication.factor: 1
      min.insync.replicas: 1
      inter.broker.protocol.version: "3.3"
    storage:
      type: ephemeral
  zookeeper:
    replicas: 3
    storage:
      type: ephemeral
  entityOperator:
    topicOperator: {}
    userOperator: {}
```

因为我们在每个命名空间中使用 Strimzi 作为我们的 Kafka 编排器，所以它带来的一个好处是我们可以根据开发者的需求拥有独特的主题！

```
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaTopic
metadata:
  name: comment
  labels:
    strimzi.io/cluster: kafka-cluster
spec:
  partitions: 1
  replicas: 1
  config:
    retention.ms: 900000
    segment.bytes: 1073741824
---
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaTopic
metadata:
  name: post
  labels:
    strimzi.io/cluster: kafka-cluster
spec:
  partitions: 1
  replicas: 1
  config:
    retention.ms: 900000
    segment.bytes: 1073741824
```


## 索引存储库概述

看起来是这样的…

```
~/manifests-index develop > tree -L 1
.
├── README.md
├── auth
├── infra
├── npm-commons
├── posts
├── frontend
├── .gitignore
└── skaffold.yaml
```

- auth 和 posts 目录是专门为认证和发布微服务而创建的存储库。
- npm-commons 是一个共享的 Node.js 通用库，包括共享中间件、事件、错误等。
- 还有前端应用程序
- 和 skaffold 中的脚手架指令
- 一个 .gitignore 文件，除了 infra 和 skaffold 之外，排除了所有内容

如果有足够多的投票，可以对这部分进行详细的解释！

## 使用 Skaffold 进行脚手架

在我们的设计中，开发人员（无论是后端还是前端）将使用 Skaffold 来为他们的工作创建环境。Skaffold 是一个命令行工具，用于简化 Kubernetes 应用程序的持续开发。

以下是我们的 Skaffold 配置示例：


apiVersion: skaffold/v2beta29
kind: Config
deploy:
  kubectl:
    manifests:
      - ./infra/k8s/auth/overlays/"{{.IMAGE_TAG}}"
      - ./infra/k8s/posts/overlays/"{{.IMAGE_TAG}}"
build:
    tagPolicy:
      envTemplate

:
        template: "{{.GIT_COMMIT}}"
        env: COMMIT_SHA along with the code in main.go, this uses a template to inject the latest Git commit hash.
  artifacts:
    - image: auth-service
      context: ./auth
      docker:
        dockerfile: Dockerfile.dev
      sync:
        manual:
          - src: "..."
            dest: "..."
    - image: posts-service
      context: ./posts
      docker:
        dockerfile: Dockerfile.dev
      sync:
        manual:
          - src: "..."
            dest: "..."
profiles:
  - name: dev
    deploy:
      kubectl:
        flags:
          - --filename=./infra/k8s/ingress/base/ingress-srv.yaml
          - --filename=./infra/k8s/kafka/base/
        namespace: development
        defaults:
          wait: false
        patches:
          - target:
              version: v1
              kind: ConfigMap
              name: kube-dns
            patch: |-
              [
                {
                  "op": "add",
                  "path": "/data/name.conf",
                  "value": "nameserver kube-dns.kube I… and their leader and look no more for this.
      - name: production
        deploy:
          kubectl:
            flags:
              - --filename=./infra/k8s/ingress/base/ingress-srv.yaml
              - --filename=./infra/k8s/kafka/base/
            namespace: production
            defaults:
              wait: false
            patches:
              - target:
                  version: v1
                  kind: ConfigMap
                  name: kube-dns
              patch: |-
                [
                  {
                    "op": "add",
                    "path": "/data/name.conf",
                    "value": "nameserver kube-dns.kubelet.svc.cluster.local\n"
                  }
                ]


这一配置允许 Skaffold 使用 Dockerfile.dev 生成 Docker 镜像，并将应用程序清单推送到 Kubernetes。

存储库内的任何更改都会自动触发 Skaffold 重新构建和部署，以便开发人员可以专注于编写代码而不是手动构建和部署。

还有开发和生产两个配置文件，允许我们在不同的环境中部署相同的应用程序清单。

部署至 Kubernetes
这是从我们的 skaffold.yaml 中的 profiles 部分获取的。

Skaffold 将根据我们的配置，将 k8s 文件传递给 kubectl 命令，用于部署应用程序的清单。下面是一个示例：

skaffold dev -p dev
使用这个命令，我们可以在开发模式下运行应用程序，这会将我们的应用程序清单部署到 development 命名空间。我们可以使用不同的配置文件进行生产部署。

CI/CD 工作流
Skaffold 与持续集成/持续交付（CI/CD）工作流程集成得很好。我们的 CI/CD 工作流程主要由 Git Actions 驱动，但也可以使用其他 CI/CD 工具，如 Jenkins、CircleCI 或 Travis。

当开发人员推送更改时，CI/CD 工作流程会触发，然后会构建、测试和部署应用程序。下面是一个基本的 Git Actions 工作流程示例：

name: Build and Deploy

on:
  push:
    branches:
      - main

jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Docker
        uses: actions/setup-docker@v2

      - name: Build the Docker image
        run: |
          docker build -t myapp:$GITHUB_SHA .
          docker tag myapp:$GITHUB_SHA myapp:latest
        env:
          GITHUB_SHA: ${{ github.sha }}

      - name: Push the Docker image
        run: |
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login docker.pkg.github.com -u ${{ github.actor }} --password-stdin
          docker push myapp:$GITHUB_SHA
          docker push myapp:latest
        env:
          GITHUB_SHA: ${{ github.sha }}

  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Set up kubectl
        uses: azure/setup-kubectl@v1

      - name: Deploy to Kubernetes
        run: kubectl apply -f infra/k8s/

使用 Git Actions，我们可以自动构建 Docker 镜像、将其推送到 Docker 仓库，然后使用 kubectl 部署到 Kubernetes。

集群监视和日志记录
在 Kubernetes 上运行微服务时，监视和日志记录非常重要。我们使用各种工具来实现这些目标：

Prometheus：用于指标收集和警报的开源系统。
Grafana：用于可视化指标和创建仪表板的开源工具。
Loki：一个开源的日志聚合系统。
Fluentd：用于日志收集和传输的开源数据收集代理。
Elasticsearch：用于存储和检索日志数据的开源搜索和分析引擎。
Kibana：用于可视化和分析 Elasticsearch 中的日志数据的开源工具。
集群监视和日志记录是确保微服务应用程序运行正常并及时检测问题的关键组成部分。

自动缩放和负载均衡
Kubernetes 提供了内置的自动缩放和负载均衡功能，这些功能使微服务应用程序能够根据负载的需求自动扩展和调整。

Horizontal Pod Autoscaling（HPA）：HPA 允许您根据 CPU 使用率或自定义指标自动扩展 Pod 的副本数。
Service 之后的负载均衡：Kubernetes Service 提供了负载均衡 Pod 的机制，确保流量分布均匀。
Istio：Istio 是一个开源的服务网格平台，提供流量管理、安全性、连接性等功能，可用于微服务应用程序。
Kubernetes 本身具有强大的自动化功能，可确保微服务应用程序按需扩展以应对不断变化的流

量和负载。

自动故障处理
Kubernetes 具有自动恢复机制，可确保在 Pod 失败或崩溃时自动重新启动它们。这有助于减少应用程序中断并提高可用性。

Readiness 和 Liveness 探针：Kubernetes 允许您定义 Pod 的就绪性和存活性检查，以确保它们在出现问题时能够自动重启。
滚动升级：Kubernetes 具有内置的滚动升级机制，可确保在部署新版本时不会中断现有流量。
Probes 和滚动升级是 Kubernetes 强大的功能，有助于自动处理应用程序的故障和更新。

安全性
在微服务应用程序中，安全性至关重要。Kubernetes 提供了多层次的安全性保护，包括：

命名空间隔离：使用命名空间将不同的微服务分开，确保它们之间的隔离。
网络策略：使用网络策略定义哪些 Pod 可以与其他 Pod 通信，实现网络隔离。
服务帐户和角色：Kubernetes 提供服务帐户和角色的概念，可用于授权和认证微服务。
RBAC（基于角色的访问控制）：使用 RBAC 规则来定义谁可以执行哪些操作，以限制权限。
机密管理：Kubernetes 提供机密对象，可用于存储敏感信息，如 API 密钥和证书。
Kubernetes 的安全性功能使您能够实施多层次的安全策略，以保护微服务应用程序的安全性和完整性。

总结
在设计和部署微服务应用程序时，Kubernetes 是一个功能强大的容器编排平台，提供了多种功能，用于管理、扩展和监视微服务。通过结合使用 Docker 镜像和 Kubernetes，您可以创建高度可伸缩、弹性和可维护的微服务应用程序。

本文提供了关于如何使用 Kubernetes 来部署和管理微服务的概述，包括如何创建应用程序清单、使用 Skaffold 进行本地开发和自动化部署、CI/CD 工作流、监视和日志记录、自动缩放和负载均衡、自动故障处理以及安全性。希望这些信息能帮助您更好地理解如何在 Kubernetes 上构建和运行微服务应用程序。