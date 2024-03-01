<!--
title: 简化Kubernetes开发：你的工具指南
cover: ./cover.png
-->

随着 Kubernetes 在应用开发中的日益普及，高效的本地开发工具需求变得至关重要。在过去几年中，用于开发人员与 Kubernetes 协作的工具得到了改进。这些工具帮助开发人员简化工作流程，加速迭代周期，并创建真实的开发环境。本文将全面分析和比较六种流行的现代 Kubernetes 本地开发工具。通过阅读本文，您将获得足够的信息，从而做出明智的选择，并提升 Kubernetes 开发体验。

> 译自 [Simplifying Kubernetes Development: Your Go-To Tools Guide](https://semaphoreci.com/blog/kubernetes-development-tools)，作者 。

## Skaffold

[Skaffold](https://github.com/GoogleContainerTools/skaffold) 是一个强大的工具，可自动化 Kubernetes 应用的开发工作流程。Skaffold 提供了全面的解决方案，满足本地开发需求和 CI/CD 工作流。它通过自动化镜像构建、部署和监视源代码的变化，使开发人员能够快速迭代。Skaffold 支持多种构建工具，并与本地 Kubernetes 集群无缝集成。其声明性配置和直观的命令行界面使其受到开发人员的欢迎。

Skaffold 配置文件通常命名为 skaffold.yaml，它是一个 YAML 文件，定义了应用程序的构建、测试和部署方式。它充当 Skaffold 的中心配置中心，允许您指定各种设置和选项，以满足特定项目的需求。

```yaml
apiVersion: skaffold/v2beta15
kind: Config

build:
  artifacts:
    - image: my-app
      context: ./app
      docker:
        dockerfile: Dockerfile

deploy:
  kubectl:
    manifests:
      - k8s/deployment.yaml
      - k8s/service.yaml
```

### 优点

Skaffold 具有模块化的架构，允许您选择与特定 CI/CD 需求对齐的工具。它类似于一个通用的瑞士军刀，在各种场景中都能发挥作用。通过图像管理功能，它可以在每次构建图像时自动创建图像标签。此外，Google 的 Cloud Code 插件使用 Skaffold 提供了与几种流行的 IDE 无缝的本地和远程 Kubernetes 开发工作流。值得注意的是，Skaffold 通过其配置文件功能提供了为每个环境维护不同配置的优势。

### 限制

根据我的经验，使用 Skaffold 时，当处理大量资源密集型微服务时，您可能会遇到在本地运行所有实例时遇到困难。因此，开发人员可能会采用模拟某些服务的方式，导致与实际生产行为有所偏差。

## Tilt

[Tilt](https://github.com/tilt-dev/tilt) 是一个增强 Kubernetes 开发体验的开源工具。Tilt 使用称为 Starlark 的 Python 方言的 Tiltfile 进行配置。Tiltfile 是 Tilt 使用的配置文件，用于定义在开发过程中如何构建、部署和管理应用程序。您可以在此处探索 Tilt API 参考。以下是一个 Tiltfile 的示例：

```
# Sample Tiltfile

# Define the Docker build for the application
docker_build(
    './app',
    dockerfile='Dockerfile',
    image='my-app'
)

# Define the Kubernetes deployment manifests
k8s_yaml('k8s/deployment.yaml')
k8s_yaml('k8s/service.yaml')
```

当您使用此 Tiltfile 运行 Tilt 时，它将基于指定的 Dockerfile 构建 Docker 镜像，并使用提供的 Kubernetes 清单将应用程序部署到 Kubernetes 集群中。Tilt 还会监视源代码的更改，并自动触发重建和重新部署，确保流畅高效的开发体验。

### 优点

与其他 Kubernetes 开发工具不同，Tilt 不仅是一个命令行工具。它还提供了一个用户友好的 UI，使您可以轻松监视每个服务的健康状态、构建进度和运行时日志。Tilt 还提供了一个 Web UI，可视化显示运行服务的状态。根据我的经验，Tilt UI 仪表板提供了当前状态的优秀概述，在处理多个系统时非常有用。虽然 Tilt 在提供流畅的开发体验方面表现出色，但对于更复杂的部署，可能需要额外的设置。

### 限制

采用 Tilt 可能需要额外的学习，特别是对于不熟悉 Starlark Python 方言的开发人员。了解并编写 Tiltfile 可能对于没有这种语言经验的人来说有挑战性。由于 Tilt 使用 Starlark 作为其配置语言，它可能不提供与使用广泛采用的 YAML 等广泛采用的配置格式的其他工具相同的灵活性和广泛的语言支持。

## Telepresence

[Telepresence](https://github.com/telepresenceio/telepresence) 由 Ambassador Labs 开发，被认可为云原生计算基金会沙箱项目，旨在提升 Kubernetes 开发体验。使用 Telepresence，您可以在本地运行单个服务，同时无缝连接到远程 Kubernetes 集群。该过程消除了在集群中连续发布和部署新工件的需要，与 Skaffold 不同，后者依赖于本地 Kubernetes 集群。通过在远程集群中为应用程序运行占位符 pod，Telepresence 将传入的流量路由到本地工作站上的容器。它将立即反映开发人员在远程集群中对应用程序代码所做的任何更改，而无需部署新容器。

要使用 Telepresence 调试应用程序，您首先需要使用 `telepresence connect` 命令将本地开发环境连接到远程集群。

然后，您可以使用 `telepresence intercept` 命令开始拦截流量。例如，您想要使用 `telepresence intercept order-service --port 8080` 命令拦截正在本地运行的服务名称 order-service 的流量。

一旦拦截激活，所有发往远程服务的流量都将路由到您本地运行的实例。您可以使用类似 curl 的工具将请求发送到远程服务。Telepresence 将这些请求路由到您的本地服务。

### 优点

Telepresence 通过最小资源利用，从您的笔记本电脑实现远程开发能力，证明了其价值。它消除了设置和运行单独的本地 Kubernetes 集群（如 minikube 或 Docker Desktop）的需要。在处理分布式系统和微服务架构时，Telepresence 特别有用。Telepresence 简化了流程，并确保您的开发环境与生产行为紧密相符。

### 限制

Telepresence 依赖于远程 Kubernetes 集群来代理到和从本地开发环境的请求。如果远程集群的可用性或连接性存在问题，则可能会中断开发工作流程。根据我的经验，Telepresence 在网络或防火墙限制严格的环境中可能还需要额外的设置。

## Okteto

[Okteto](https://github.com/okteto/okteto) 有效地消除了与本地开发设置相关的挑战，以及单个工程组织中可能出现的各种变化，以及常常伴随这种复杂性的问题解决。其主要优势在于将内部开发循环转移到集群而不是在本地工作站上自动化它。通过在 okteto.yaml YAML 清单文件中定义开发环境，并利用像 okteto init 和 okteto up 这样的命令，开发人员可以快速在集群上建立他们的开发环境。

```
# Sample okteto.yaml

# Define the development environment
environment:
  name: my-dev-env
  namespace: my-namespace
  image: my-app:latest

# Specify the services to sync with the remote cluster
sync:
  - local_path: ./app
    remote_path: /app

# Specify the services to forward ports for local access
port_forwarding:
  - service: my-app
    local_port: 8080
    remote_port: 80
```

okteto.yaml 文件由 Okteto 用于定义开发环境以及应该如何同步和转发到远程 Kubernetes 集群的本地文件和端口。

当您使用此 okteto.yaml 文件运行 okteto up 时，Okteto 将在指定的命名空间中创建指定的开发环境，并将 my-app Docker 镜像部署到远程集群。它还将本地 ./app 目录与集群中的 /app 目录同步，确保立即在远程集群中反映本地进行的任何更改。此外，文件中指定的端口转发允许您访问在集群中运行的 my-app 服务，就像它在本地的端口 8080 上运行一样。

okteto.yaml 文件提供了一种简单的方法来配置您的 Okteto 开发环境，并将本地开发与远程 Kubernetes 集群同步。它提供了一种无缝的开发体验，允许您将远程集群视为本地开发环境。

### 优点

Okteto 是一种良好的解决方案，可轻松地在本地和远程 Kubernetes 集群之间同步文件。其单个二进制文件与各种操作系统完全兼容，并在容器开发环境中具有出色的远程终端。具有卓越的热代码重载功能以实现更快的迭代和双向端口转发以实现本地和远程服务之间的顺畅通信，Okteto 对于所有开发人员来说都是绝对必备的工具。它与本地和远程 Kubernetes 集群、Helm 和无服务器函数无缝集成，消除了在开发过程中构建、推送或部署的必要性。此外，它高效、方便地消除了特定运行时安装的必要性，使其成为所有开发人员的最佳选择。

### 限制

Okteto 在开发方面严重依赖于远程 Kubernetes 集群。如果远程集群的可用性或连接性存在问题，则可能会中断开发工作流程。由于 Okteto 将开发循环移到集群，因此可能会消耗额外的资源，导致成本增加并与集群上的其他工作负载争用。根据我的经验，这可能还会影响开发环境的性能和响应速度。

## Docker Compose

尽管 [Docker Compose](https://github.com/docker/compose) 并非专门为 Kubernetes 设计，但它被广泛用于定义和运行多容器应用程序。它允许开发人员在声明性的 YAML 文件中定义服务、网络和卷，从而轻松设置复杂的开发环境。借助 Docker 的 Kubernetes 集成，我们可以使用 Compose 文件将应用程序部署到 Kubernetes 集群。要使用 Docker Compose，必须在工作站上安装 Docker。但是，

重要的是要注意，虽然 Docker Compose 可能让开发人员感觉他们的应用程序在类似 minikube 的 Kubernetes 环境中运行，但它与实际的 Kubernetes 集群有根本的区别。因此，在 Docker Compose 上顺利运行的应用程序的行为可能在部署到 Kubernetes 生产集群时不会表现得类似。

以下是一个简单的 Java 应用程序的 Docker Compose 文件示例：

```
version: '3'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    volumes:
      - ./src/main/resources:/app/config
```

services 部分定义了构成应用程序的服务。在本例中，我们有一个名为 app 的单个服务

build 指定了构建上下文和用于构建 app 服务镜像的 Dockerfile。

context 是包含 Dockerfile 和应用程序源代码的目录的路径。

dockerfile 是要使用的 Dockerfile 的文件名。ports "8080:8080" 将主机上的端口 8080 映射到容器中的端口 8080，允许您在 http://localhost:8080 上访问在容器中运行的 Java 应用程序。

`volumes` 创建了一个绑定挂载，将主机上的 src/main/resources 目录挂载到容器中的 /app/config，允许在主机上对配置文件进行更改，以便在容器中反映。

要使用此 Docker Compose 配置，导航到包含 docker-compose.yml 文件的目录，并运行以下命令：

```bash
docker-compose up
```

### 优点

使用 Docker Compose，您可以在单个文件中概述应用程序的服务、配置和依赖关系。根据我的经验，我觉得 Docker Compose 遵循 KISS（保持简单、愚蠢）设计原则。它简化了监视和部署由众多容器组成的复杂应用程序。它非常适合在单个主机或机器上运行的应用程序，使其成为开发和测试环境的绝佳选择。Docker Compose 允许在开发过程中快速迭代，因为您可以快速重建和重新部署容器。学习曲线通常比 Kubernetes 小，使其适用于对容器编排新手的开发人员。

### 限制

虽然容器有效地解决了“在我的机器上可以运行”的问题，但 Docker Compose 引入了一个新的挑战 - “在我的 Docker Compose 设置上可以运行”。使用 Docker Compose 作为简化云应用程序内部开发循环的替代方案可能很诱人。但是，正如之前解释的那样，本地和生产环境之间的差异可能使调试变得具有挑战性。

## Garden

Garden 是一个全面的 Kubernetes 本地开发环境，旨在在不同的开发阶段提供一致和可重复的体验。它是一个云原生应用程序开发、测试和部署的平台。它通过利用 Docker 和 Kubernetes，提供了对容器化开发的一种偏爱的方法。Garden 与流行的 IDE 集成良好，并提供诸如热重载和无缝服务发现之类的功能。它通过称为 garden.yml 的配置文件概述了应用程序的构建和部署过程。

要将 Garden.io 集成到您的项目中，请执行以下命令以启动设置：

```bash
garden init
```

然后，您可以通过将以下示例添加到 'garden.yml' 文件中来配置您的项目。此文件定义了服务、任务、测试等：

```yaml
services:
  web:
    build: .
    ports:
      - target: 3000
        published: 3000
        protocol: tcp
```

在您的项目中配置 Garden.io 之后，通过导航到您的项目目录并运行 garden start 命令启动它。一旦设置和配置了 Garden.io 并且正在运行，工具将启动项目，为 'garden.yml' 文件中指定的每个服务生成容器。要将测试纳入 Garden.io 设置中，请向 garden.yml 文件添加 'tests' 部分。

```bash
tests:
  my-tests:
    service: web
    command: mvn test
```

随后，运行以下 garden test 命令将执行测试套件。最后，您可以通过向 garden.yml 文件添加目标环境部分来将应用程序部署到不同的云提供商和 Kubernetes 集群。

```bash
target:
  name: my-kubernetes-cluster
  provider: kubernetes
```

在这里，我们指示目标环境是名为 my-kubernetes-cluster 的 Kubernetes 集群。然后，执行 garden deploy 命令以启动部署。此外，garden deploy 将自动将应用程序部署到指定的 Kubernetes 本地开发环境，处理图像构建、Kubernetes 编排和同步等任务，并为开发和测试提供无缝环境。

### 优点

其主要优势之一在于其简化云原生开发环境设置的能力。通过抽象出创建 Kubernetes 配置和其他部署相关任务的复杂性，Garden 大大简化了初始设置过程，使开发人员能够专注于编写和测试应用程序，而不是与复杂配置进行挣扎。这种设置的简易性可以显着加快对 Kubernetes 生态系统中有经验的开发人员和新手的入职速度，使他们能够更快地投入到有效的工作中。

### 限制

根据我的经验，我发现 Garden 的设置比其他工具更为复杂，需要一些

学习曲线。尽管 Garden 的目标是简化 Kubernetes 应用程序的本地开发，但它的配置仍然需要一定的了解和技能，特别是对于那些对容器编排和云原生技术不太熟悉的人来说。虽然 Garden 为开发人员提供了丰富的功能和强大的控制力，但这也可能使其对初学者来说有点过于复杂。

## 结论

在现代 Kubernetes 生态系统中，有多种工具可用于本地开发环境设置。每个工具都有其独特的优势和适用场景。选择正确的工具取决于您的特定需求、团队的技能水平以及项目的规模和复杂性。在选择工具时，您应该考虑到与您的团队和工作流程最匹配的解决方案，以及您希望实现的开发体验。无论您选择哪种工具，重要的是确保它能够满足您的需求，并与您的工作流程无缝集成。通过选择适当的工具，您可以加速开发周期，提高生产力，并确保您的应用程序在生产环境中具有高可靠性和性能。