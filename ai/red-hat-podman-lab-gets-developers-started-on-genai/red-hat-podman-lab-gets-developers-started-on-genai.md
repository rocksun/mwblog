
<!--
title: Podman Lab帮助开发者开启GenAI
cover: https://cdn.thenewstack.io/media/2024/05/051f11ac-podmanai-summit.jpg
-->

与许多用于构建生成式 AI 应用程序的工具不同，Podman AI Lab 是专门为开发者而非数据科学家构建的。

> 译自 [Red Hat Podman 'Lab' Gets Developers Started on GenAI](https://thenewstack.io/red-hat-podman-lab-gets-developers-started-on-genai/)，作者 Joab Jackson。

Podman，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 [桌面工具](https://thenewstack.io/red-hat-podman-container-engine-gets-a-desktop-interface/)，用于 [管理容器 Pod](https://thenewstack.io/check-out-podman-red-hats-daemon-less-docker-alternative/)，已获得扩展职责，即为开发者提供一个工作空间来构建基于生成式 AI 的应用程序。

与许多用于构建生成式 AI 工具的工具不同，Red Hat 断言，此工具是专门为开发者构建的，而不是为数据科学家构建的。这里对训练模型的支持不多。相反，用户需要围绕已通过 API 提供并打包为 [微服务](https://thenewstack.io/microservices/) 的开源模型构建代码。

[Podman AI 实验室](https://github.com/containers/podman-desktop-extension-ai-lab) 为开发者提供了在本地计算机上构建生成式 AI 应用程序的能力，并在准备就绪后将其发送到 [OpenShift](https://www.openshift.com/try?utm_content=inline+mention)/ [Kubernetes](https://thenewstack.io/kubernetes/) 在一组[容器](https://thenewstack.io/containers/)中部署。

Red Hat 首席技术官办公室的数据科学家 [Michael Clifford](https://www.linkedin.com/in/jamesmichaelclifford/) 上周在丹佛举行的红帽峰会上的一次会议上表示：“能够在自己的笔记本电脑上构建和测试应用程序，‘让您作为一名开发者拥有速度、自由和安全性，可以立即开始破解一些东西’”。AI 实验室“让事情非常容易地适应人们已经熟悉的现有开发范例。并且让将事物放入云中变得更加容易”。

与 [Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) 类似，[Podman](https://podman.io/) 本身提供了一种方法，可以轻松地将代码从本地开发环境（例如 VS Code）移到 Kubernetes/OpenShift 操作环境中。因此，对于 Red Hat 来说，这是一个推出 AI 应用程序的自然平台。

为了让开发人员的工作变得更加轻松，AI 实验室有一个示例应用程序的配方目录，其中包括：

- 聊天机器人
- 文本摘要
- 代码生成器
- 对象检测
- 音频转文本转录

这些都是功能非常强大的模板，尽管它们并非设计为按原样使用。源代码可用于检查和针对其进行自定义。每个配方都是从现有模型构建的，并具有用于交互的 API。Red Hat 希望围绕这些配方形成一个社区，并且随着时间的推移会创建更多配方。

该项目源于客户要求，即为开发目的找到一种在台式机上运行 LLM 的方法。

Clifford 解释说，过去几年中的一项不错的 AI 进步是，您不再需要为某些特定用途训练自己的模型。相反，您可以在通用模型周围构建应用程序。

当然，有流行的商业模型，例如 [OpenAI](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/)，但也有越来越多的开源模型（Clifford 在最近的统计中统计了超过 90,000 个 [公开可用的语言模型](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)）。

![](https://cdn.thenewstack.io/media/2024/05/a7b1a03f-stevan_lemeur-1024x686.jpg)

*Stevan Le Meur 解释了开发人员 AI 工作流以及它如何与 Podman 配合使用。*

## 开始使用 Podman AI 实验室

Podman AI 实验室界面提供了一个开源模型目录供下载，其中包括大多数开源模型，例如 [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)、[Pytorch](https://pytorch.org/) 或 [Tensorflow](https://www.tensorflow.org/)。用户还可以导入自己的模型。

![](https://cdn.thenewstack.io/media/2024/05/ee20814f-download-model.gif)

*在 Podman 中下载模型。*

这些模型不包含在容器中。相反，它们在运行时通过单独挂载存储卷来添加。这允许您在运行时交换模型。

Red Hat 首席产品经理 [Stevan Le Meur](https://www.linkedin.com/in/stevanlemeur/?originalSubdomain=fr) 在自己的峰会演讲中解释说，所有这些构思和原型制作都需要一些工作，“我需要找到合适的模型来完成我的应用程序”，“哪种模型最适合我的用例？”

一旦选择了一个模型，用户就可以在自己的计算机上启动一个推理服务器。所有模型服务器都构建在 Linux 通用基础映像（[UBI](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image)）为基础，以实现最大的兼容性。许多服务都包含了对硬件加速器的支持，例如 [Llama.cpp](https://python.langchain.com/v0.1/docs/integrations/llms/llamacpp/)、Nvidia 和 AMD。

![](https://cdn.thenewstack.io/media/2024/05/a4ba0b90-start-inference-server.gif)

该扩展还提供了一个测试不同模型的游乐场，允许开发人员在不同任务上尝试不同的模型。

![](https://cdn.thenewstack.io/media/2024/05/8fc8c615-playground.gif)

这些食谱展示了可以从这些模型中整理出什么样的功能。“我们尝试提供一些示例，激发你对在自己的应用程序中可以做什么的灵感，”Le Meur 说。

## 人工智能的未来

人工智能实验室是 Podman Desktop 的众多扩展之一，它本身基于 [符合 OCI](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/) 的 Podman 容器引擎。还有用于在本地运行 K8s 的 [minikube](https://thenewstack.io/install-minikube-on-ubuntu-linux-for-easy-kubernetes-development/) 副本、OpenShift 的本地主机以及用于制作 [可引导容器](https://thenewstack.io/red-hat-rethinks-the-linux-distro-for-the-container-age/) 的扩展。

然而，Podman AI 与红帽的整体人工智能战略非常契合，该战略旨在支持构建人工智能应用程序的各种方法。

人工智能的未来“不会由单一供应商使用单一模型构建。它将是开源的，” 红帽首席执行官 [Matt Hicks](https://www.redhat.com/en/about/company/leadership/matt-hicks) 在峰会上发表主题演讲时 [说](https://twitter.com/Joab_Jackson/status/1787849813851017720)。
