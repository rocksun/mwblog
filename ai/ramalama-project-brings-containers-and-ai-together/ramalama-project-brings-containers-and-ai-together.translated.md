# RamaLama 项目将容器和 AI 结合在一起

![Featued image for: RamaLama Project Brings Containers and AI Together](https://cdn.thenewstack.io/media/2025/03/fb0b49d2-ramalama-1024x576.jpg)

[RamaLama 项目](https://github.com/containers/ramalama) 位于 AI 和 Linux 容器的交叉点，旨在简化在开发者桌面上开发和测试 AI 模型的过程。

随着 [RamaLama 网站](https://ramalama.ai/) 的最新发布以及公开邀请 [贡献](https://github.com/containers/ramalama/blob/main/CONTRIBUTING.md) 代码，我决定采访该项目的两位创始人 Eric Curtin 和 Dan Walsh。Dan 和 Eric 之前曾合作开发 Podman 容器管理工具，该工具最近被 Cloud Native Computing Foundation (CNCF) 接受为一个项目。

## RamaLama 如何启动

**Scott McCarty:** 您是如何参与 RamaLama 的？

**Eric Curtin, software engineer at Red Hat:** RamaLama 是我一直在研究的一个业余项目。我们开始尝试使用 [LLaMA.cpp](https://github.com/ggerganov/llama.cpp)，使其易于与云原生概念结合使用。我现在也是 LLaMA.cpp 的维护者。我在软件方面有各种各样的背景。

**Dan Walsh, senior distinguished engineer at Red Hat:** 我现在在 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) AI 团队工作。在过去的 15 年里，我一直致力于容器技术，包括创建 Podman，现在它是一个 CNCF 项目。在过去的一年左右，我一直在研究可引导容器，这促使我开始研究 Red Hat Enterprise Linux AI (RHEL AI)，它使用可引导容器来支持 AI 工具。我还参与了 [AI Lab Recipes](https://github.com/containers/ai-lab-recipes) 的开发，该项目使用容器来运行 AI 工作负载。几年前，我和 Eric 曾合作过一个独立的项目，所以我们一直保持联系。

**Scott:** RamaLama 项目是如何以及何时启动的？

**Dan:** Eric 编写了一些脚本，并在去年夏天演示了他的工具，当时我注意到了这项工作。我担心开源 AI 领域忽略了容器，并将 AI 开发人员困在特定的笔记本电脑硬件和操作系统中。更重要的是，将 [Linux](https://roadmap.sh/linux) 和 [Kubernetes](https://roadmap.sh/kubernetes) 排除在外。

**Eric:** RamaLama 最初的目标是使 AI 变得平平无奇（易于使用）并使用云原生概念。当时它被称为 podman-llm。当时我们计划了两个主要功能：将 AI 加速器运行时作为容器拉取，并支持多种传输协议（OCI、Hugging Face、Ollama）。今天在 [README.md](https://github.com/containers/ramalama/blob/main/README.md) 中的图表实际上没有改变。

**Dan:** 我开始建议进行更改，例如将其迁移到 [Python](https://thenewstack.io/what-is-python/)，以便于贡献者使用并与大多数 AI 软件保持一致。我们将项目重命名为“RamaLama”。我还建议我们将这些工具移动到 GitHub 上的 containers 组织中，我们在 2024 年 7 月 24 日在那里合并了我们的第一个 pull request。

**Scott:** 这个名字是怎么来的？

**Eric:** (laughs) 我想把这个问题留给 Dan 回答。

**Dan:** 许多开放 AI 内容都在使用某种形式的 Llama，由 [Meta 的 Llama2 AI 模型](https://thenewstack.io/metas-llama-2-is-not-open-source-and-thats-ok/) 率先推出。我们在 RamaLama 中的一些技术是基于 [Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)，并且我们在容器内部使用的主要引擎是 LLaMA.cpp。所以我们想以某种方式拥有一个“llama”的名字。我小时候想起的一首愚蠢的歌是“Rama Lama Ding Dong”，所以我们选择了 RamaLama 这个名字。

## RamaLama 的工作原理

**Scott:** 在桌面上使用容器镜像来运行 AI 模型有什么优势？

**Eric:** 我们已经使用 Open Container Image (OCI) 作为应用程序容器、[bootc](https://github.com/bootc-dev/bootc) 和 AI 运行时等事物的分发机制。OCI 注册表旨在传输大型数据，它是一种成熟的传输机制，已在许多地方可用。

**Dan:** 企业希望能够在他们的基础设施上存储他们的 AI 内容。许多企业不允许他们的软件直接从互联网上拉取。他们希望控制所使用的 AI 模型。他们希望他们的模型经过签名、版本控制并具有供应链安全数据。他们希望使用 Kubernetes 等工具来编排它们。因此，能够将 AI 模型和 AI 内容存储为 OCI 镜像和工件是完全有意义的。

**Scott:** RamaLama 是如何工作的？
**Eric：** RamaLama 尝试自动检测系统中的主要加速器；它会基于此拉取一个 AI 运行时。然后，它将使用或拉取一个基于指定模型名称的模型——例如，`ramalama run granite3-moe`——然后提供模型。这是最基本的使用方法；它具有 Kubernetes、Quadlet 和许多其他功能。

**Dan：** RamaLama 的另一个目标是帮助开发人员将其 AI 应用程序投入生产。RamaLama 可以轻松地将 AI 模型从任何传输方式转换为 OCI 内容，然后将模型推送到 OCI 注册表，例如 Docker Hub、Quay.io 或 Artifactory。RamaLama 不仅可以在本地提供模型，还会生成 Quadlet 和 Kubernetes 部署，以便在生产中轻松运行 AI 模型。

**Scott：** 为什么 RamaLama 很重要？

**Dan：** 我们可以让用户轻松地安装 RamaLama，并通过一个简单的命令启动并运行 AI 模型，将其作为聊天机器人或提供基于 AI 的服务，而无需用户下载和安装（在某些情况下还需要构建）AI 工具，然后才能将模型拉取到系统。RamaLama 的一个关键思想是在容器中运行模型，以保护用户免受模型或运行模型的软件对其主机的影响。用户运行随机模型是一个安全问题。

**Eric：** 它为社区提供了一个使用云原生概念进行 AI 推理的易于访问的项目。我们对推理运行时、传输机制、后端兼容性和硬件兼容性等方面的意见也较少，从而使开发人员可以在他们选择的系统上使用和构建 AI。

## RamaLama 对硬件和其他工具的支持

**Scott：** 你们能够支持替代硬件吗？

**Eric：** 这是 RamaLama 的一个不同之处。许多项目对硬件的支持有限，仅支持一种或两种类型的硬件，例如 Nvidia 或 [AMD](https://www.amd.com/en/products/processors/server/epyc/google-cloud.html?utm_content=inline+mention)。我们将与社区合作，尽最大努力启用替代硬件。

**Dan：** RamaLama 是用 Python 编写的，可能可以在任何支持 Python 的地方运行，并且支持 Podman 或 Docker 容器引擎。就加速器而言，我们目前有镜像来支持仅 CPU，以及 Vulkan、Cuda、Rocm、Asahi 和 Intel-GPU。其中许多是由社区贡献的，因此如果有人想贡献一个 containerfile (Dockerfile) 来构建对新 GPU 或其他加速器的支持，我们会将其添加到项目中。

**Scott：** RamaLama 还集成了哪些其他工具？

**Eric：** RamaLama 站在巨人的肩膀上，并使用了许多现有的技术。从容器的角度来看，我们与现有的工具（如 Podman、Docker、Kubernetes 和基于 Kubernetes 的工具）集成。从推理的角度来看，我们与 LLaMA.cpp 和 vLLM 集成，因此我们与可以与这些 API 集成的工具兼容。可能还有我们不知道的使用方式。

**Scott：** RamaLama 是否适用于新的 DeepSeek AI 模型？

**Eric：** 是的，我们在模型发布当天就与 DeepSeek 兼容。它是更令人印象深刻的模型之一；它展示其思维过程的方式很有趣。

**Dan：** 我们发现很少有它不适用的 [GGUF](https://huggingface.co/docs/hub/gguf)（GPT-Generated Unified Format）模型。当我们遇到这种情况时，我们会与 LLaMA.cpp 项目合作进行修复，并在几天内使它们正常工作。我们计划支持其他模型以与 vLLM 一起使用。

## AI 的未来展望

**Scott：** 对 RamaLama 或 AI 的未来有什么其他想法吗？

**Dan：** 我认为我们的 AI 冒险是一系列步骤。首先，我们玩耍并提供 AI 模型。RamaLama 现在可以做到这一点。我们希望通过添加其他使用 AI 模型的方式（如 Whisper）来增强这一点。接下来，我们正在积极帮助用户使用 Docling 和 Llama Stack 等开源工具将其静态文档转换为检索增强生成 ([RAG](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/)) 数据库。之后，我们添加了对运行和服务模型以及 RAG 数据的支持，以提高 AI 模型给出良好响应的能力。所有这些都将侧重于将 AI 数据容器化。

之后的下一步是支持 AI 代理。这些代理允许 AI 模型与互联网上的随机 API 和数据库进行交互。我们看到开源领域正在进行大量这方面的工作。我们希望让开发人员可以轻松地利用这些工具，并最终将它们投入生产。
**Eric:** 我们欢迎社区积极参与。我仍然认为 RamaLama 处于起步阶段。我们仅仅触及了 RAG、AI 代理、语音识别和 Stable Diffusion 等方面。我期待看到社区如何使用它。Podman 最初用于服务器之类的东西；现在我们看到更多创造性的用法，例如 [Podman Desktop](https://podman-desktop.io/)、toolbox 和 bootc。我期待看到 RamaLama 如何演变为前所未有的用例。

*要了解更多关于 Kubernetes 和云原生生态系统的信息，请参加 4 月 1 日至 4 日在伦敦举行的 *[KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)* 大会。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。