<!--
title: 通过Kratix掌握平台工程
cover: https://www.infracloud.io/assets/img/Blog/mastering-platform-engineering-with-kratix/how-does-kratix-work.png
-->

[DevOps向平台工程的演变](https://www.infracloud.io/blogs/devops-to-platform-engineering-how-we-got-here/)，是当前技术领域一个有趣的转型。[平台工程](https://www.infracloud.io/blogs/platform-engineering-101/)包括创建创新工程解决方案，帮助开发者减少基础设施部署等非开发活动的时间投入，使他们可以专注于应用程序开发和交付。

> 译自 [Mastering Platform Engineering with Kratix](https://www.infracloud.io/blogs/mastering-platform-engineering-with-kratix/)。作者 
Nitin Naidu 。

各种工程解决方案的采用，例如内部开发平台(IDP)- 比如Backstage，都支持平台工程的采用。这些工具中一些致力于为开发者创建一个中心控制台，而一些则帮助平台工程师构建平台即服务，这可能与通过运行单个命令来帮助设置开发环境一样简单。

本文我们将探索Kratix，这是一个使您能够构建和交付平台即服务的工具。

## 什么是Kratix？

[Kratix](https://kratix.io/)是一个开源框架，为平台工程师提供将平台交付为产品的功能。Kratix通过利用Kubernetes和GitOps的力量来提升平台构建能力，同时提供在服务中也包含业务逻辑的方式。

与其他框架和工具不同，其他工具专注于应用程序开发人员的体验，Kratix则专注于使平台工程师能够构建更好的平台。随着团队采用平台工程技术，如果您的平台团队正在寻找将日常平台任务交付为开发人员的自助服务，那么Kratix可能会成为平台团队的帮助，因为它可以省去满足开发人员各种要求的时间。当然，Kratix是一个灵活的工具，也可以与其他工具一起使用，支持广泛的使用场景。

要直观理解Kratix的使用，可以考虑这样一种情况:您的QA团队希望在特定环境中测试一个应用程序。这个环境可能需要数据库和Kubernetes集群等资源。可能需要特定版本来部署数据库和Kubernetes。

### 没有Kratix

在典型业务环境下，这需要提出一个工单，然后指派给平台团队，由平台团队接手任务并交付。平台工程师需要抓紧时间组装环境，运行脚本等完成部署，以赶上交付的最后期限。

### 使用Kratix

使用Kratix，可以创建一个Promise，它包含满足类似环境创建请求所需的配置。这个Promise可以满足开发人员对环境创建的任何请求。通过开发人员提供的几项输入，Promise可以在Kubernetes集群中运行并创建环境。在后台，Promise可以使用Terraform CRD(自定义资源定义)、流水线等来交付任务。我们在下面会进一步讨论它的工作方式。

虽然这只是一个简单的使用场景，但可以利用这个工具交付一个全面的平台即服务产品，包括合规性、业务逻辑等。

## Kratix的特性

### Promise

Promise是平台团队和应用团队之间达成的透明协议，通过定义和实现明确的抽象概念来形成，这些概念在YAML文档中定义，由平台团队创建。Promise安装在Kubernetes集群上以满足开发人员或任何利益相关者的要求。

Promise包含什么？

![Kratix promise](https://www.infracloud.io/assets/img/Blog/mastering-platform-engineering-with-kratix/kratix-promise.png)

1. API

应用程序开发人员用来请求Kratix Promise资源的API(在Kubernetes中，是CRD)，它定义用户在请求Promise时可以配置的选项。

2. 依赖项

依赖项是任何地方创建资源所需的先决条件，必须预先在任何地方安装。例如Jenkins CRD(自定义资源定义)和用于部署Jenkins的operator。

3. 工作流

工作流允许定义在资源创建、维护或更新时要运行的流水线。流水线可以包含将用户输入转换为operator预期格式等步骤。还可以帮助执行Kubernetes集群外的任务，如部署失败时发送Slack警报。

可以查看用于[部署PostgreSQL资源的YAML配置中的Promise](https://github.com/infracloudio/promise-postgresql/blob/main/promise.yaml)，以了解API、依赖项和工作流程是如何组合形成Promise的。

### 复合Promise

[复合Promise](https://kratix.io/docs/main/guides/compound-promises)是Promise中的Promise依赖项，可以用来从应用到数据库部署整个堆栈，打包为一个。考虑业务环境，复合Promise不仅可以部署单个资源。

它可以在主集群中安装Promise，在工作集群中安装依赖项如CRD，创建黄金路径等。它可以包含诸如设置环境时处理安全、网络、存储、合规性、部署等任务的Promise。

### Kratix市场

[Kratix市场](https://kratix.io/marketplace)是一个可以找到社区和Kratix团队创建的Promise的地方。这意味着可能不需要从零开始创建Promise，可以重用现有的Promise。如果现有的不完全符合要求，可以基于它进行自定义。这里可以找到用于部署监控堆栈(Prometheus和Grafana)、设置RabbitMQ或Kafka等的多个预构建Promise。

## 与其他工具的集成

Kratix 与 [Backstage](https://www.infracloud.io/blogs/starting-platform-engineering-journey-backstage/)、[Kubernetes operator](https://www.infracloud.io/kubernetes-school/writing-k8s-operator-kluster/) 和 Terraform 等其他工具互补。例如，使用 Kratix 您可以创建一个 Promise，它可以部署 Backstage 视图。这将是将视图作为 Kratix 中的配置进行编码。您可以根据需要部署这些视图，可以部署任意次数。

Kratix 可以与 Terraform operator 一起使用。可以通过 Promise 来部署云资源。开发人员只需通过请求资源来请求创建虚拟机，Promise 将通过利用 Terraform CRD 在云上创建资源来提供服务。

## Kratix 如何工作？

Kratix 建立在 Kubernetes 之上。如前所述，Kratix 的工作原理围绕 Promise 进行。包含服务请求所需资源的 Promise 将在 Kubernetes 集群上服务任何请求。Kratix 允许在单集群或多集群架构中实现。在单集群中，满足资源创建请求的 Promise 将部署在任何传入的资源创建请求也发生的同一集群中。而在多集群中，您可以拥有一个平台集群，其中 Promise 将被部署，任何传入的资源创建请求都将由 Promise 在单独的工作集群中创建。Kratix 运行的简单可视化如下图所示。

![Kratix 如何工作](https://www.infracloud.io/assets/img/Blog/mastering-platform-engineering-with-kratix/how-does-kratix-work.png)

## 实现 Kratix

为了理解如何实现 Kratix，我们将安装一个满足 PostgreSQL 资源创建请求的 Promise。Promise 将部署在名为平台集群的单个 kind 集群上。在此示例中，您可以将工作集群和平台集群视为一个。此 Promise 由 Kratix 提供的基本 Promise 组成。此 Promise 接受用户的某些输入，并根据输入创建 PostgreSQL 资源。基本 Promise 已更新为接受一个新字段“deployedBy”，用户在请求时也可以输入此字段。此字段将作为标签添加到将创建的 PostgreSQL 资源中。

请求者可以传递的基本输入参数包括数据库名称、部署资源的超级用户名称、部署的命名空间以及标签“deployedBy”。

PostgreSQL 的 Promise 预先配置了 PostgreSQL pod 的 CPU 和内存限制等值。平台工程师可以更进一步，还可以配置细粒度的访问级别(读取器、写入器和所有者)、节点亲和性等根据其业务需求的具体配置。这有助于平台工程师摆脱每次 PostgreSQL 部署中的干预。同时，开发人员只需运行一个带有基本输入的命令即可启动并运行 PostgreSQL，而无需担心开发人员不需要决定的其他与数据库相关的配置。所有这些都可以由平台工程师在 Promise 中预先配置。

以下是执行所述用例的步骤:

### 先决条件

1. 应安装 [Docker](https://docs.docker.com/engine/install/)
2. 应安装 Kind([了解如何安装 Kind](https://kind.sigs.k8s.io/#installation-and-usage))

### 步骤

1. Kratix 安装

您可以按照[官方文档](https://kratix.io/docs/main/guides/installing-kratix/single-cluster)作为单集群设置安装 Kratix。

2. 获取 PostgreSQL Promise。

克隆来自 Kratix 的基本 Promise 的 PostgreSQL Promise，已更新为具有新的输入参数 - 'deployed by:'。查看 [promise.yaml](https://github.com/infracloudio/promise-postgresql/blob/main/promise.yaml) 和 [resource-request.yaml](https://github.com/infracloudio/promise-postgresql/blob/main/resource-request.yaml)。promise.yaml 包含通常由平台团队设置的 Promise 配置。resource-request.yaml 是用户通过在文件中添加所需输入来请求 PostgreSQL 资源创建的文件。

```bash
$ git clone https://github.com/infracloudio/promise-postgresql.git
```

3. 创建流水线镜像。

我们用例中的 Kratix Promise 中的流水线会根据用户输入的任何时间用户请求资源来创建清单文件。Postgres Operator 需要清单来创建 Postgres 实例。该流水线由获取输入和输出 [minimal-postgres-manifest.yaml](https://github.com/infracloudio/promise-postgresql/blob/main/internal/configure-pipeline/resources/minimal-postgres-manifest.yaml) 的 bash 脚本组成，我们将使用 [Dockerfile](https://github.com/infracloudio/promise-postgresql/blob/main/internal/configure-pipeline/Dockerfile) 将其转换为 Docker 镜像，在后续步骤中我们将使用该镜像。这种方法的基本原理是一旦将流水线转换为镜像，就可以重复使用流水线。一旦以 Docker 镜像的形式封装，流水线就可以轻松地在不同的 Promise 之间重复使用。

```bash
 $ cd promise-postgresql/internal/configure-pipeline

 $ docker build . --tag kratix-workshop/postgres-configure-pipeline:dev
 [+] Building 0.2s (10/10) FINISHED
 docker:default
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 399B
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/library/alpine:latest
 => [1/5] FROM docker.io/library/alpine
 => [internal] load build context
 => => transferring context: 127B
 => CACHED [2/5] RUN [ "mkdir", "/tmp/transfer" ]
 => CACHED [3/5] RUN apk update && apk add --no-cache yq
 => CACHED [4/5] ADD resources/* /tmp/transfer/
 => CACHED [5/5] ADD execute-pipeline execute-pipeline
 => exporting to image
 => => exporting layers
 => => writing image sha256:XX
 => => naming to docker.io/kratix-workshop/postgres-configure-pipeline:dev

```

4. 将您的流水线镜像提供给 kind 集群 - 'platform'。

```bash
 $ kind load docker-image kratix-workshop/postgres-configure-pipeline:dev --name platform
 Image: "kratix-workshop/postgres-configure-pipeline:dev" with ID "sha256:XXXXX"
```

5. 在平台集群上安装 Postgres Promise 并进行验证。

运行以下命令时，请确保您位于 promise-postgresql 文件夹中。

```bash
nitin@NITIN-NAIDU:~/kratix/Promise-postgresql$ kubectl apply
--filename Promise.yaml
Promise.platform.kratix.io/postgresql created

nitin@NITIN-NAIDU:~/kratix/Promise-postgresql$ kubectl get crds
NAME                                   CREATED AT
bucketstatestores.platform.kratix.io   2023-10-17T12:48:08Z
certificaterequests.cert-manager.io    2023-10-17T12:47:14Z
certificates.cert-manager.io           2023-10-17T12:47:14Z
challenges.acme.cert-manager.io        2023-10-17T12:47:14Z
clusterissuers.cert-manager.io         2023-10-17T12:47:14Z
destinations.platform.kratix.io        2023-10-17T12:48:08Z
gitstatestores.platform.kratix.io      2023-10-17T12:48:08Z
issuers.cert-manager.io                2023-10-17T12:47:14Z
orders.acme.cert-manager.io            2023-10-17T12:47:14Z
postgresqls.marketplace.kratix.io      2023-10-17T12:50:31Z
Promises.platform.kratix.io            2023-10-17T12:48:08Z
workplacements.platform.kratix.io      2023-10-17T12:48:08Z
works.platform.kratix.io               2023-10-17T12:48:08Z

nitin@NITIN-NAIDU:~/kratix/Promise-postgresql$ kubectl --namespace default get pods
NAME                                 READY   STATUS      RESTARTS   AGE
minio-create-bucket-pzjsr            0/1     Completed   0          22m
postgres-operator-64cbcd6fdf-2dpkk   1/1     Running     0          14m
```

6. 验证您的 Kratix Promise 是否可以实现。

```bash
nitin@NITIN-NAIDU:~/kratix/Promise-postgresql$ kubectl apply
--filename resource-request.yaml
postgresql.marketplace.kratix.io/example created

nitin@NITIN-NAIDU:~/kratix/Promise-postgresql$ kubectl get pods
NAME                                        READY   STATUS      RESTARTS   AGE
acid-example-postgresql-0                   1/1     Running     0          29m
configure-pipeline-postgresql-8b724-nx2ct   0/1     Completed   0          30m
minio-create-bucket-pzjsr                   0/1     Completed   0          53m
postgres-operator-64cbcd6fdf-2dpkk          1/1     Running     0          45m

nitin@NITIN-NAIDU:~/kratix/Promise-postgresql$ kubectl get pods --selector deployedBy=InfraCloud
NAME                        READY   STATUS    RESTARTS   AGE
acid-example-postgresql-0   1/1     Running   0          30m
```

瞧！我们刚刚部署了一个定制的 Kratix Promise，它帮助满足了在 Kubernetes 集群中安装带有标签 deployedBy 和用户在创建过程中提供的其他输入的 PostgreSQL 的请求。我们作为开发人员/用户运行了一个命令来请求资源，该资源已成功提供服务。

接下来，您可以按照[官方文档创建自己的 Kratix Promise](https://kratix.io/docs/main/guides/writing-a-promise)，其中包含特定于业务的要求。

## 总结

随着平台工程的发展，利用像 Kratix 这样的工具会有利于以服务的形式呈现您的平台，从而减轻平台工程师和开发人员的负载。

[Kratix 市场](https://kratix.io/marketplace)是一个很好的地方，您可以直接使用社区开发的 Promise。虽然一些 Promise 可能立即满足您的需求，但其他 Promise 可能需要定制以更好地满足您的特定需求。

简而言之，Kratix 是一个 Kubernetes 原生的灵活工具，可用于为开发人员创建非开发活动的抽象，并作为平台工程师的便利工具来创建平台工程任务的抽象。

欢迎随时联系我们的[平台工程咨询](https://www.infracloud.io/platform-engineering-consulting/)团队，采用像 Kratix 这样的工具，并支持您的组织采用平台工程。您可以在[LinkedIn](https://www.linkedin.com/in/nitin-naidu-4b86a7129/)上联系我，就本博文开始讨论。

## 参考资料

* [Kratix 官方文档](https://kratix.io/docs/main/intro)
