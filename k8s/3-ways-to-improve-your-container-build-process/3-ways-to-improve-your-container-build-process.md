
<!--
title: 优化容器构建流程的3种方法
cover: https://cdn.thenewstack.io/media/2024/07/5fffaf8c-lego-708087_1280.jpg
-->

在中央注册表上替换图像层并使所有正在运行的图像更新各个层是一个方便的协议。

> 译自 [3 Ways To Improve Your Container Build Process](https://thenewstack.io/3-ways-to-improve-your-container-build-process/)，作者 Sylvain Kalache。

随着 [Kubernetes](https://thenewstack.io/kubernetes/) 最近 [庆祝其 10 周年](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/)，容器镜像已成为现代基础设施的核心。这些容器镜像往往变得更加复杂和庞大；一份报告发现，受访者报告称，从 2020 年到 2021 年，构建时间 [增加了 15.9%](https://www.incredibuild.com/survey-report-2022#item_7490)。

在本文中，我将探讨良好管理容器带来的收益，这将使我们能够构建更轻量级的镜像，速度更快。其中两个技巧将针对 [Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)，而最后一个技巧将使用 [Pack](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/)，这是一个支持使用 [buildpacks](https://thenewstack.io/streamlined-apm-integration-in-cloud-native-buildpacks/) 的 CLI 工具。

## 步骤排序

在编写 Dockerfile 时，步骤的顺序很重要。Docker 具有一个内置的缓存机制——称为层缓存——在您构建容器镜像时缓存文件中的每个步骤。因此，下次您从同一个 Dockerfile 构建镜像时，它将重用缓存的层。

但是，只要步骤发生变化并且缓存无法使用——例如，因为应用程序代码已更改——所有后续步骤也需要重新运行。

让我们看一下 Python 应用程序 Dockerfile 的一部分。在这里，我们从 Ubuntu 基础镜像开始，复制应用程序代码，然后安装系统包。

```dockerfile
FROM ubuntu:22.04
 
# Copy the current directory contents into the container at /app
COPY . /app
 
# Install Python and pip
RUN apt-get update &amp;&amp; apt-get install -y python3-pip python3-dev
```

此排序问题在于，每次应用程序代码发生更改时，Docker 都无法为包安装部分使用其缓存，并且需要再次下载和安装包。原本只需要不到一秒钟的操作，最终可能需要几分钟。

因此，这里正确的排序应该是简单地翻转指令：

```dockerfile
FROM ubuntu:22.04
 
# Install Python and pip
RUN apt-get update &amp;&amp; apt-get install -y python3-pip python3-dev
 
# Copy the current directory contents into the container at /app
COPY . /app
```

我在一台内存为 16G、4 个 vCore 的普通服务器上运行了一个示例，使用以下 [Python 应用程序](https://github.com/sylvainkalache/sample-web-apps/tree/buildpack_pack_rebase_benchmark/python)。为了模拟企业应用程序的大小，我添加了 numpy、scipy 和 pandas 作为依赖项。

当使用具有 [错误排序](https://github.com/sylvainkalache/sample-web-apps/blob/buildpack_pack_rebase_benchmark/python/wrongDockerfileOrder) 的 Dockerfile 时——当应用程序代码在安装 Python 包之前被复制时——在代码更改后重建镜像平均需要 1.7 分钟。

当使用具有 [正确排序](https://github.com/sylvainkalache/sample-web-apps/blob/buildpack_pack_rebase_benchmark/python/Dockerfile) 的 Dockerfile 时——当应用程序代码在安装 Python 包之前被复制时——在代码更改后重建镜像平均需要 0.3 秒，速度提高了 99%。

因此，不要忘记 Dockerfile 的经验法则，将不太可能更改的内容放在 Dockerfile 的顶部，将更可能更改的内容放在底部。

## 使用多阶段构建

Dockerfile 中的多阶段构建通过允许在同一个 Dockerfile 中使用多个 FROM 语句来优化构建镜像的过程。此功能有助于创建更小、更高效的 Docker 镜像。例如，它可以用于将构建环境与运行时环境分离。

同样，我运行了一个示例来查看我们可以期待哪些改进。这次，我们使用一个带有 Spring、Spark 和 Kafka 作为依赖项的示例 Java 应用程序。

以下是使用多阶段构建的 Dockerfile：

```dockerfile
# Multi-Stage Dockerfile
 
## Stage 1: Build Stage
FROM maven:3.8.1-openjdk-16 AS build
 
# Set working directory
WORKDIR /app
 
# Copy the application source code and pom.xml
COPY pom.xml .
COPY src ./src
 
# Build the application
RUN mvn clean package
 
## Stage 2: Runtime Stage
FROM openjdk:16-jdk-slim
 
# Set working directory
WORKDIR /app
```

如您所见，我有两个 FROM 语句，一个用于构建我的 jar，另一个用于构建我的镜像。

当使用 [没有多阶段构建](https://github.com/sylvainkalache/sample-web-apps/blob/buildpack_pack_rebase_benchmark/java/nonMultiStageDockerfile) 的 Dockerfile 时——当编译和容器安装是同一个阶段的一部分时——镜像大小最终为 1Gb。

当使用 Dockerfile [包含多阶段构建](https://github.com/sylvainkalache/sample-web-apps/blob/buildpack_pack_rebase_benchmark/java/Dockerfile) 时 - 当编译和容器安装属于同一阶段时 - 镜像大小最终减少了 500MB 或 50%。根据需要加载此镜像的容器实例数量，这可以显著提高部署时间，尤其是在地理分布式基础设施中。

## 只重新绑定特定层

最后一个技巧不像我们讨论的其他两个技巧那么出名。在这里，我们将使用一个额外的工具 - [pack CLI](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/) - 它基于云原生构建包的实现。

由于使用构建包生成镜像的方式，[rebase](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/cli/pack_rebase/) 功能允许您将容器镜像的 OS 层（运行镜像）替换为运行镜像的更新版本，而无需重新构建整个容器。

要重新绑定镜像，命令如下：

```
pack rebase name-of-container-image
```

同样，我使用一个简单的 Python 应用程序和 Dockerfile 进行了 [实验](https://github.com/sylvainkalache/sample-web-apps/blob/buildpack_pack_rebase_benchmark/python/benchmark.py)。当使用 docker build 重新构建新的容器镜像时，我从 Ubuntu 22.04 升级到最新版本，在撰写本文时为 24.04。使用最新 OS 版本重新构建镜像平均需要 2 分钟 26 秒。

当使用 pack CLI 的 rebase 功能时，使用最新 OS 版本重新构建容器镜像平均需要 43 秒，速度提高了 70%。

这在您必须紧急将 OS 安全补丁应用于镜像时尤其有用，对于拥有数千甚至数十万个镜像需要打补丁的公司来说，这一点尤其重要。

## 结论

所有这些在本地作为开发人员运行时可能无关紧要；但是，构建速度在使用开发管道时很重要。当规模较小时，看似微不足道的收益在规模化时将变得重要。当您在一个拥有许多管道的工程组织中工作时 - 特别是在微服务激增的情况下 - 构建和重建速度对于保持高交付速度至关重要。这可能意味着将开发周期从数小时缩短到数分钟。

更小的镜像将提供存储、网络和吞吐量性能提升，并在规模化运行时降低成本。

最后，当组织在生产中使用大量容器时，更快的更新时间很重要。能够在中央注册表中替换镜像层并让所有正在运行的镜像更新各个层是一个方便的协议，尤其是在需要单独构建和重新部署镜像的情况下。
