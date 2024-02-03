<!--
title: 使用Docker构建云加速Docker构建
cover: https://cdn.thenewstack.io/media/2024/01/1a35455a-docker_build-1024x747.png
-->

这是 Docker 构建远程服务的一个分支，称为 Docker 构建云，是一个完全托管的服务，可将构建时间提速高达 39 倍。

> 译自 [Docker Build Cloud Promises to Speed Docker Builds](https://thenewstack.io/docker-build-cloud-promises-to-speed-docker-builds/)，作者 Steven J. Vaughan-Nichols 又名 sjvn，自 CP/M-80 是前沿的个人电脑操作系统，300bps 是快速的互联网连接，WordStar 是当时最先进的文字处理器的时候，他就一直在撰写关于技术和技术业务的文章，而我们喜欢它。

即使它只能提供其母公司承诺的性能的一小部分，Docker 构建云对于开发人员来说仍然是非常值得的。

[Docker](https://www.docker.com/?utm_content=inline-mention) 长期以来一直是一个家喻户晓的名字 —— 至少在程序员的家庭中是这样 —— 但 Docker 构建时间却一直在不断延长。根据一项 [Incredibuild](https://www.incredibuild.com/) 调查，自 2020 年以来，[平均构建时间增加了 15.9%](https://www.incredibuild.com/survey-report-2022#item_7490)。这让很多程序员感到沮丧，但现在 Docker 有了一个解决方案：[Docker构建云（Docker Build Cloud）](https://www.docker.com/products/build-cloud/)。

这是 [Docker 构建](https://docs.docker.com/engine/reference/commandline/image_build/)远程构建服务的一个衍生产品，Docker 构建云是一个完全托管的服务，弥合了在本地编程和远程为 linux/amd64 或 linux/arm64 平台进行构建之间的差距，或者您可以使用该服务同时构建两者。

结果呢？Docker 声称这项新服务将使您的构建时间加速高达 39 倍。

例如，Docker 表示其客户之一能够将构建时间从平均 15-20 分钟减少到不到 2 分钟，使用了 Docker 构建云。虽然不是 39 倍更快，但也不可忽视！我真希望我在工作中也能看到这样的性能提升。

## Docker 构建云的工作原理

Docker 构建云通过提供比本地计算机更快的计算资源来实现这一点。其云架构还使您能够利用服务的多个核心和 GPU。

通过为团队的所有构建提供一个共享缓存，Docker 构建云还能够加速构建时间。使用 Docker 云构建时，当一个团队成员启动一个构建时，缓存的结果立即对其他人可用，从而消除不必要的构建，加快开发周期。您无需等待每个构建独立完成。

除了速度之外，公司声称使用 Docker 构建云，可扩展性不再是一个问题。开发人员不再需要担心本地计算机的限制或管理自己的构建服务器。Docker 构建云可以根据需求动态分配资源，确保构建不仅快速而且高效。

另一个关键的改进是 Docker 构建云为构建过程带来了一致性。通过标准化构建发生的环境，Docker 构建云确保了“在我的机器上可以运行”的问题已经成为过去。这种一致性对于团队来说是无价的，确保每个成员都在使用相同的工具和环境。

所有这些都无需您更改现有的工具和工作流程。您不应该改变或迁移您的工作流程。无论您是在本地构建还是在持续集成（CI）流水线中构建，您都可以采用 Docker 构建云，而无需彻底改变当前的流程。Docker 构建云的混合本地/云方法使您能够利用熟悉的本地开发工具进行诸如代码编辑和调试等任务，同时可以扩展到云资源以处理资源密集型的工作负载、部署或协作。该服务还为自动化和与其他云服务集成提供了新的可能性，进一步增强了开发工作流程。

## Docker 构建云的费用是多少？

要使用 Docker 构建云，您首先必须像往常一样[创建一个 Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)。然后，您可以将其推送到基于云的存储库，例如 [GitHub](https://thenewstack.io/github-developer-productivity-at-30-billion-messages-per-day/) 或 [Docker Hub](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/)。接下来，您需要创建一个云构建配置文件。此文件告诉云构建如何构建您的镜像。配置文件必须指定 Dockerfile 的位置和目标镜像名称。

最后，您需要启动一个构建。您可以使用 Cloud Build 控制台、Cloud Build API 或 [Google Cloud（gcloud](https://cloud.google.com/sdk/gcloud)）命令行工具来完成这一操作。构建完成后，您的镜像将被推送到 Google Container Registry。从那里，您可以将镜像部署到任何 Kubernetes 集群。

当前 Docker 用户可以立即尝试 Docker 构建云。您将[根据您的订阅等级获得 Docker 构建云分钟数](https://www.docker.com/products/build-cloud/#pricing)：Docker 个人版，50 分钟/月（M/M）；专业版，100 M/M；团队版，400 M/M；企业版，800 M/M。需要更多吗？您还可以购买 Docker 构建云计划。这些计划从每月每用户 $5 起，提供 200 分钟/月。额外分钟费用从每分钟五美分开始。
