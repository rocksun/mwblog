# Docker Model Runner 将本地 LLM 带到您的桌面

![Docker Model Runner 将本地 LLM 带到您的桌面的特色图片](https://cdn.thenewstack.io/media/2025/04/a94b6455-hu-chen-jazlbmkqf0u-unsplash-1024x684.jpg)

[Docker](https://www.docker.com/) 通过让每个人都能访问容器而声名鹊起。现在，这家与容器化开发同义的[公司](https://www.docker.com/?utm_content=inline+mention)正试图通过让开发者能够在他们的 PC 上运行和测试 [AI 大型语言模型](https://thenewstack.io/LLM/) (LLM) 来获得更多声誉，并推出了 [Docker Model Runner](https://www.docker.com/blog/introducing-docker-model-runner/)。

Docker Model Runner 是 [Docker Desktop 4.40](https://www.docker.com/blog/docker-desktop-4-40/) 中一个新的 beta 功能，适用于 Apple silicon 驱动的 Mac。此功能使开发者能够在他们的 PC 上运行 LLM 和其他 AI 模型。您可以直接从命令行访问它。它还可以无缝集成到 [Docker 生态系统](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)的其余部分。

为什么要本地运行？除了能够将其直接集成到您的工作流程中之外，Docker Model Runner 还消除了调用外部云应用程序编程接口 (API) 的需要。反过来，这确保了数据隐私，减少了延迟并降低了成本。

使用 Docker Model Runner，您的 LLM 被打包为 [开放容器计划](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/) (OCI) Artifacts。这使您能够从 Docker Hub 或其他注册表中提取模型，并使用熟悉的工具将其集成到 CI/CD 管道中。例如，您可以使用熟悉的 Docker CLI 命令（例如“docker model pull”、“docker model run”和“docker model list”）来处理模型。换句话说，AI 模型是 Docker 工作流程中的“一等公民”，就像容器和镜像一样。

在本地机器上运行 LLM 长期以来一直是一个挑战，受到零散的工具、硬件兼容性问题和断开连接的工作流程的阻碍。开发者经常需要处理多个工具，配置复杂的环境，并在其容器化设置之外管理模型，从而导致摩擦和不断上升的云推理成本。

为了实现这个技巧，Docker Model Runner 使用 [llama.cpp](https://github.com/ggml-org/llama.cpp)。这是一个开源 C++ 库，可以无需 GPU 即可高效部署和推理 LLM。[Chris Wellons](https://nullprogram.com/about/) 是一位著名的软件工程师，他报告说他已成功地将 [llama.cpp 移植到 Windows XP](https://nullprogram.com/blog/2024/11/10/) 并在 2008 年的笔记本电脑上运行了 [一个 360M 模型](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct)。简而言之，您可以使用这些模型在您的工作 PC 上完成实际工作。

顾名思义，Llama.cpp 可以很好地与 Meta AI 的 LLaMA LLM 配合使用。但是，它不限于 LLaMA 模型。由于它使用了与 OpenAI 兼容的 API，因此它可以与其他模型一起使用。Docker 已经提供了一个精选的列表，其中包含最适合本地用例的最流行的 LLM。开始使用的最简单方法是查看 [Docker Hub 的 AI 存储库](https://hub.docker.com/u/ai)。

目前只有十几个 LLM，但还有更多正在开发中。Docker 正在与 Google、HuggingFace、Qualcomm、Spring AI、VMware Tanzu 和 Dagger 等 AI 领导者合作。这些合作将各种高质量、优化的模型和工具直接引入 Docker 工作流程，使开发者可以更轻松地在本地试验和构建 AI 驱动的应用程序。

展望未来，Docker 计划将支持扩展到更多平台，包括具有 GPU 加速的 Windows。此外，该计划还使开发者能够发布自定义模型，并更深入地集成到更广泛的 AI 生态系统中。该公司设想的未来是，运行、共享和部署 AI 模型就像今天使用容器一样无缝和标准化。

但是，等等！还有更多。

## 模型上下文协议

Docker 还在集成 [模型上下文协议](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/) (MCP)。这是一个[开放标准](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)，旨在简化 AI 代理与数据源、工具和应用程序环境之间的连接。
最初由 [Anthropic](https://www.anthropic.com/) 开发，MCP 迅速成为事实上的标准——有时被描述为“ [AI 的 USB-C](https://modelcontextprotocol.io/introduction)”——用于将 AI 助手连接到各种资源，包括数据库、API、云服务和本地文件系统。通过提供通用协议，MCP 消除了为每个新工具或数据源定制连接器的需求，从而使开发人员能够更轻松地构建、部署和扩展 AI 代理，这些代理可以在不同的环境中执行有意义的、上下文丰富的任务。

Docker 正在通过 [Docker MCP Catalog](https://www.docker.com/blog/introducing-docker-mcp-catalog-and-toolkit/) 引入它。此 Docker Hub 目录提供了一种集中方式来发现、运行和管理来自领先提供商的 100 多个 MCP 服务器，包括 Grafana Labs、[Kong](https://konghq.com/?utm_content=inline+mention), Neo4j, Pulumi, [Heroku](https://www.heroku.com/?utm_content=inline+mention), 和 Elasticsearch。现在，开发人员可以像启动传统的容器化服务一样轻松地浏览和启动支持 MCP 的工具。

该公司还提供 Docker MCP Toolkit，它为 MCP 工作流程带来了企业级管理和安全性。它包括注册表和镜像访问管理、密钥处理和 OAuth 集成等功能，使团队可以更轻松地在其现有的 Docker 环境中安全地发布、管理和连接 MCP 服务器。

根据 [new Docker President](https://www.globenewswire.com/news-release/2025/03/05/3037425/0/en/Docker-Appoints-Mark-Cavage-as-President-and-Chief-Operating-Officer-to-Accelerate-Next-Phase-of-Growth.html) 和 COO [Mark Cavage](https://www.linkedin.com/in/mcavage/) 的一份声明，所有这一切的意义在于“构建功能性 AI 应用程序不应与构建任何其他应用程序有根本的不同。开发人员希望将 AI 集成到他们现有的工作流程中——在本地构建、测试并充满信心地交付到生产环境。随着代理工具开始表现得像成熟的软件系统一样，打包、版本控制和身份验证的旧挑战会迅速回归。Docker MCP Catalog 将所有这些整合在一个地方，这是一个受信任的、对开发人员友好的 Docker Hub 体验，其中的工具经过验证、安全且易于运行。”

因此，如果您想让 AI 成为您工作流程的一部分，而无需付出太多努力，并且您已经在使用 Docker 进行开发工作流程，那么这套新的 AI 工具看起来肯定会成功。

[YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)