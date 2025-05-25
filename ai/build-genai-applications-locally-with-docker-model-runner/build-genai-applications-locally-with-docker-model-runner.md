<!--
title: 使用Docker Model Runner在本地构建GenAI应用程序
cover: https://cdn.thenewstack.io/media/2024/09/b152c34d-docker.png
summary: 告别繁琐！Docker Model Runner 让你在本地轻松玩转 GenAI 应用。无需复杂配置，直接在 Docker Desktop 拉取、运行和管理 AI 模型，支持 llama.cpp 和 Hugging Face 模型。通过 OpenAI 兼容 API，加速 Gemma LLM 和嵌入模型开发，体验 Apple 芯片 GPU 加速！
-->

告别繁琐！Docker Model Runner 让你在本地轻松玩转 GenAI 应用。无需复杂配置，直接在 Docker Desktop 拉取、运行和管理 AI 模型，支持 llama.cpp 和 Hugging Face 模型。通过 OpenAI 兼容 API，加速 Gemma LLM 和嵌入模型开发，体验 Apple 芯片 GPU 加速！

> 译自：[Build GenAI Applications Locally With Docker Model Runner](https://thenewstack.io/build-genai-applications-locally-with-docker-model-runner/)
> 
> 作者：Janakiram MSV

[Docker Model Runner](https://docs.docker.com/model-runner/) 是 [Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) 的一项新功能，旨在简化在 [Docker 生态系统](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) 中本地运行和测试 AI 模型的过程。它解决了开发人员在将生成式 AI 和大型语言模型集成到其工作流程中时面临的长期挑战，例如工具碎片化、复杂的环境设置和不一致的模型管理。

通过将主机原生推理引擎直接嵌入到 [Docker Desktop](https://docs.docker.com/desktop/) 中，Model Runner 无需容器化每个 AI 工作负载，这不仅提高了性能，还简化了用户体验。该推理引擎目前构建在 [llama.cpp](https://github.com/ggml-org/llama.cpp) 之上，作为主机上的原生进程运行。这种方法确保了模型权重被有效地加载，并且系统可以充分利用本地硬件，包括 Apple 芯片系统上的直接 GPU 加速。这种原生执行绕过了在容器或虚拟机内部运行模型的传统开销，从而实现了更快的推理和更流畅的开发周期。

## Docker Model Runner 的先决条件

要运行 Docker Model Runner，您需要满足与 Docker 环境和硬件相关的几个先决条件。首先，您必须安装 Docker Desktop 4.41 或更高版本。Docker Model Runner 作为 Docker Desktop 中的一项功能集成，因此早期版本不支持它。如果您计划将 Model Runner 与多容器应用程序或 Compose 文件一起使用，则还需要 Docker Compose 2.35 或更高版本。

硬件兼容性至关重要。在 Mac 上，Docker Model Runner 需要 Apple 芯片（M1、M2 或更新版本）。在 Windows 上，您需要一个带有 NVIDIA GPU 的系统才能利用本地推理加速。该功能目前不适用于 Linux 或基于 Intel 的 Mac。

## 启用 Model Runner

如果您运行的是最新版本的 Docker Desktop，则可以访问 Dashboard 设置以启用 Model Runner。

从命令行，运行以下命令以启用相同的功能：

```
docker desktop enable model-runner --tcp 12434
```

现在，您已经在 macOS 上运行了一个 llama.cpp 推理引擎。您可以使用以下命令验证它：

```
docker model status
```

启用后，您可以按照熟悉的命令来拉取和运行模型。与 `docker images list` 命令类似，您可以运行 `docker model list` 来列出所有已下载的模型。

## 拉取和运行 Gemma LLM

与容器注册表类似，Docker 也有一个用于生成式 AI 模型的注册表，可以在 [hub.docker.com/u/ai](https://hub.docker.com/u/ai) 访问。模型以与容器镜像相同的 OCI 格式存储。

让我们在本地拉取并运行 [Gemma3](https://blog.google/technology/developers/gemma-3/) 模型。

```
docker model pull ai/gemma3
```

模型下载完成后，您可以使用以下命令确认其可用性：

```
docker model list
```

我们现在可以使用 [cURL 命令](https://thenewstack.io/curl-fights-a-flood-of-ai-generated-bug-reports-from-hackerone/) 通过与 OpenAI 兼容的 API 端点访问该模型。

```
curl http://localhost:12434/engines/llama.cpp/v1/chat/completions \
 -H "Content-Type: application/json" \
 -d '{
  "model": "ai/gemma3",
  "messages": [
   {
    "role": "system",
    "content": "You are a helpful assistant."
   },
   {
    "role": "user",
    "content": "Who was the captain of the Indian cricket team during the 1983 World Cup?"
   }
  ]
 }'
```

## 从 Hugging Face 拉取和运行嵌入模型

Docker Model Runner 支持直接从 Hugging Face [模型存储库](https://huggingface.co/models) 拉取模型，前提是这些模型与 llama.cpp 兼容。在此示例中，我将从 Hugging Face 拉取 [mxbai-embed-large-v1](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1) 嵌入模型。

```
docker model pull hf.co/mixedbread-ai/mxbai-embed-large-v1
```

由于这具有针对 CPU 优化的 [GGUF](https://huggingface.co/docs/hub/en/gguf) 风格的模型，并且与 llama.cpp 引擎完全兼容，因此 Docker 成功下载了该模型。
您可以使用下面显示的命令对其进行测试。

```
curl http://localhost:12434/engines/llama.cpp/v1/embeddings \
 -H "Content-Type: application/json" \
 -d '{
  "model": "hf.co/mixedbread-ai/mxbai-embed-large-v1",
  "input": "Embeddings made easy"
 }'
```

您还可以在 Docker Desktop 仪表板中看到下载的模型。
有了在本地运行的文本嵌入模型和LLM，我们可以在我们的开发机器上开发RAG和agentic应用程序，而无需使用远程推理引擎或端点。

Docker Model Runner标志着本地AI开发的重大进步，它使AI开发变得快速、简单并集成到Docker生态系统中。它使开发人员能够直接在他们的机器上拉取、运行和管理AI模型，而无需传统基础设施设置的复杂性或容器化推理的开销。通过利用主机原生推理引擎并支持直接GPU加速，尤其是在Apple silicon上，Model Runner提供了高性能和高效的资源使用。模型作为OCI工件分发，从而可以实现标准化打包、版本控制以及与现有Docker工作流程的无缝集成。使用OpenAI兼容的API可确保轻松采用并与现有应用程序兼容。