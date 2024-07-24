# 如何在边缘运行小型语言模型

![边缘运行小型语言模型的特色图片](https://cdn.thenewstack.io/media/2024/07/6ecf3e41-getty-images-zyyrzizlmao-unsplash-1024x702.jpg)

在我之前的文章中，我介绍了[联邦语言模型](https://thenewstack.io/federated-language-models-slms-at-the-edge-plus-cloud-llms/)的概念，它利用了运行在云端的[大型语言模型](https://thenewstack.io/llm/) (LLM) 和运行在边缘的[小型语言模型](https://thenewstack.io/the-rise-of-small-language-models/) (SLM)。

我的目标是在边缘运行一个 SLM，它可以根据本地工具提供的上下文来响应用户查询。[英伟达 Jetson Orin 开发套件](https://developer.nvidia.com/embedded/learn/get-started-jetson-agx-orin-devkit) 是这种用例的理想选择之一，它运行着像[微软 Phi-3](https://azure.microsoft.com/en-us/products/phi-3) 这样的 SLM。

在本教程中，我将引导您完成在 Jetson Orin 开发套件上配置[Ollama](https://ollama.com/)（一个轻量级模型服务器）的步骤，该服务器利用 GPU 加速来加快 Phi-3 的推理速度。这是配置跨越云和边缘的联邦语言模型的关键步骤之一。

## 什么是英伟达 Jetson AGX Orin 开发套件？

NVIDIA Jetson AGX Orin 开发套件代表了边缘 AI 和机器人计算的重大进步。这款强大的套件包含一个高性能的 Jetson AGX Orin 模块，能够提供高达 275 TOPS 的 AI 性能，并且比其前身 Jetson AGX Xavier 的功能提升了八倍。开发套件旨在模拟所有 Jetson Orin 模块的性能和功耗特性，使其成为开发人员在各个行业开发高级机器人和边缘 AI 应用的极其通用的工具。

开发套件的核心是 Jetson AGX Orin 模块，它配备了英伟达 Ampere 架构 GPU，拥有 2048 个 CUDA 内核和 64 个张量内核，以及一个 12 核 Arm Cortex-A78AE CPU。该套件配备了一个参考载板，该载板公开了许多标准硬件接口，从而能够快速进行原型设计和开发。Jetson AGX Orin 开发套件提供 32GB 或 64GB 内存选项，支持多个并发 AI 推理管道，以及 15W 到 50W 的功耗配置，为开发人员提供了一个灵活且强大的平台，用于在制造、物流、医疗保健和智慧城市等领域创建尖端的 AI 解决方案。

另请参阅：我们之前关于

[使用 Jetson Orin 运行实时目标检测] 的教程。

对于这种情况，我使用的是配备 32GB RAM 和 64GB eMMC 存储的 Jetson AGX Orin 开发套件。它运行着最新版本的 Jetpack 6.0，其中包含各种工具，包括 CUDA 运行时。

Jetpack 中最重要的组件是 Docker 和 Nvidia 容器工具包。

## 在 Jetson AGX Orin 开发套件上运行 Ollama

Ollama 是一个以 Docker 为模型的开发人员友好的 LLM 基础设施。它已经针对 Jetson 设备进行了优化。

与 Docker 类似，Ollama 也有两个组件：服务器和客户端。我们将首先安装客户端，它带有一个可以与推理引擎通信的 CLI。

```bash
wget https://github.com/ollama/ollama/releases/download/v0.2.8/ollama-linux-arm64
chmod +x ./ollama-linux-arm64
sudo mv ollama-linux-arm64 /usr/local/bin/ollama
```

上面的命令下载并安装了 Ollama 客户端。

使用以下命令验证客户端：

```bash
ollama --version
```

现在，我们将通过 Docker 容器运行 Ollama 推理服务器。这可以避免您在访问 GPU 时遇到的任何问题。

```bash
docker run -d \
--runtime nvidia \
--name ollama \
--network=host \
-v ~/models:/models \
-e OLLAMA_MODELS=/models \
dustynv/ollama:r36.2.0 ollama serve
```

此命令在主机网络上启动 Ollama 服务器，使客户端能够直接与引擎通信。服务器监听端口 11434，该端口公开了一个与 OpenAI 兼容的 REST 端点。

运行命令 `ollama ps`

显示一个空列表，因为我们还没有下载模型。

## 在 Ollama 上提供微软 Phi-3 SLM

微软的 Phi-3 代表了小型语言模型 (SLM) 的重大进步，它以紧凑的封装提供了令人印象深刻的功能。Phi-3 家族包括从 38 亿到 140 亿个参数的模型，其中 Phi-3-mini (38 亿) 已经可用，而更大的版本，如 Phi-3-small (70 亿) 和 Phi-3-medium (140 亿) 即将推出。
Phi-3 模型旨在提高效率和可访问性，使其适合部署在资源受限的边缘设备和智能手机上。它们采用 Transformer 解码器架构，默认上下文长度为 4K 个令牌，长上下文版本（Phi-3-mini-128K）扩展到 128K 个令牌。

在本教程中，我们将运行模型的 4K 版本，即 [Phi-3 mini](https://ollama.com/library/phi3:instruct)。

在 Ollama 容器运行且客户端安装后，我们可以使用以下命令拉取镜像：

```
ollama run phi3:mini
```

使用命令 `ollama ls` 检查模型。

## 从 Jupyter Notebook 访问 Phi-3
由于 Ollama 公开了与 OpenAI 兼容的 API 端点，因此我们可以使用标准 OpenAI Python 客户端与模型进行交互。

```
pip install openai
```

通过将 URL 替换为 Jetson Orin 的 IP 地址，尝试以下代码片段。

```python
from openai import OpenAI

OLLAMA_URL = "YOUR_JETSON_IP::11434/v1/"
client = OpenAI(base_url=OLLAMA_URL, api_key='ollama')
prompt = "When was Mahatma Gandhi born? Answer in the most concise form."
model = "phi3:mini"
response = client.chat.completions.create(
    model=model,
    max_tokens=50,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)
print(response.choices[0].message.content.strip())
```

在 Jetson 设备上，可以使用 `jtop` 命令监控 GPU 的使用情况。

本教程介绍了在 Nvidia Jetson Orin 边缘设备上运行 Microsoft Phi-3 SLM 所需的基本步骤。在本系列的下一部分中，我们将继续构建联邦 LM 应用程序，利用此模型。敬请关注。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)