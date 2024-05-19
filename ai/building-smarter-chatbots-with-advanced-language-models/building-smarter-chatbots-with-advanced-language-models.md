
<!--
title: 利用高级语言模型构建更智能的聊天机器人
cover: https://cdn.thenewstack.io/media/2024/05/0673cbee-ai-chatbots-featured-image.png
-->

使用 LangChain 社区、Mixtral 8-7B 和 ChromaDB，利用向量数据库检索和语义搜索开发一个功能强大、直观的聊天机器人。

> 译自 [Building Smarter Chatbots With Advanced Language Models](https://thenewstack.io/building-smarter-chatbots-with-advanced-language-models/)，作者 Mikhail Khlystun。

聊天机器人的发展正在迅速演变，新的工具和框架让构建复杂系统变得更加容易和高效。但当前的 [大型语言模型 (LLM)](https://thenewstack.io/llm/) 存在局限性：它们缺乏当前知识，无法访问特定领域的知识，例如公司的知识库内容。[检索增强生成 (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/) 可以通过查找 LLM 训练数据之外的知识，然后将该信息传递给 LLM 来解决此问题。

在这篇技术文章中，我将解释如何利用 LangChain Community、Mixtral 8-7B 和 ChromaDB 创建一个高级聊天机器人，该机器人能够处理各种文件类型，以便从向量数据库中检索信息，通过语义搜索进行搜索，并通过直观界面与用户交互。

## 聊天机器人技术的发展

用于聊天机器人开发的工具和流程发展得非常快。它们正在扩展聊天机器人的功能，并改变它们与用户交互和处理信息的方式。我确定了五个我认为特别重要的功能，我将在本教程中使用它们。

- **过渡到 LangChain Community 和 Mixtral 8-7B**：从 LangChain 和 Mistral 过渡到它们更高级的对应版本 LangChain Community 和 Mixtral 8-7B，标志着聊天机器人开发的重大演变。这些工具扩展了聊天机器人的应用范围，支持文档处理，并增强了跨各种领域的自然语言理解。
- **从图数据库过渡到 ChromaDB**：ChromaDB 支持存储和查询大规模、高维数据。这使得 ChromaDB 成为管理各种应用程序中复杂数据类型和结构的理想选择。
- **使用会话检索链**：虽然 RAG 通过允许访问 LLM 训练数据集之外的外部数据来增强聊天机器人的响应，但会话检索链通过在会话期间从向量数据库动态检索信息来构建此功能。这种转变保留了 RAG 的优点，同时还通过高级语言模型集成实时、特定于上下文的检索来提高聊天机器人的交互性和相关性。
- **高级文件处理和处理**：新场景扩展了处理的文件类型，包括 PDF、M4A、CSV、Excel 和 EML，并引入了高级处理技术。这涉及使用 ChromaDB 存储和查询提取的信息，以及为音频文件集成语音识别，从而扩展了聊天机器人处理各种数据源的能力。
- **使用 Gradio 界面进行部署**：Gradio 为测试和部署 AI 模型（包括聊天机器人）提供了一个交互式且用户友好的界面。这使用户可以更轻松地实时与系统交互。

我将在本教程中使用这些工具。但首先，为不熟悉 RAG 的人提供一个说明。

## 了解 RAG

RAG 在增强 LLM 的功能方面发挥着至关重要的作用。RAG 促进 LLM 访问外部数据，使它们能够生成具有附加上下文的信息。结果是一个为最终用户提供卓越的下一代 LLM 体验的应用程序。使用 RAG，您的 LLM 更加有用和有效。

RAG 通过一系列四个关键步骤进行操作：

1. **加载编码文档**：该过程从将文档加载到已编码为机器可读格式的向量数据库开始。
2. **查询编码**：使用句子转换器将用户的查询转换为向量。查询的这种向量化格式使其与数据库中的编码文档兼容。
3. **上下文检索**：将编码查询用于从向量数据库中检索相关上下文。此上下文包含生成适当解决用户查询的响应所需的信息。
4. **提示 LLM**：检索到的上下文和查询用于提示 LLM。LLM 生成一个在上下文上适当且信息丰富的响应。

## 展示 RAG 的影响

为了说明 RAG 在增强聊天机器人功能方面的有效性，我准备了比较模型在使用和不使用 RAG 的情况下提供的答案的屏幕截图：

### 不使用 RAG

该模型无法访问最新的定价信息，因为它不属于训练数据集的一部分。此限制导致响应无法反映当前公司数据。

![](https://cdn.thenewstack.io/media/2024/05/27e91aac-model_without_rag-1024x432.png)

### 使用 RAG

在将[定价页面](https://gcore.com/pricing/cloud)保存为 PDF 文件并将其用作 RAG 的额外内容后，该模型有效地解析并利用了该文件，准确地回答了有关最新定价的问题。这展示了 RAG 通过集成动态外部信息来增强聊天机器人性能的能力。

![](https://cdn.thenewstack.io/media/2024/05/8e8bdd10-model_with_rag-1024x435.png)

## 系统要求和性能

为了确保我们的聊天机器人系统的最佳性能，我在配备 4x GeForce GTX 1080 Ti GPU 的虚拟机上测试了该设置。这些资源的平均利用率对于维持聊天机器人的高要求进程至关重要。

![](https://cdn.thenewstack.io/media/2024/05/f213f44a-4xgpu_load-1024x528.png)

通过实施命令 `export CUDA_VISIBLE_DEVICES=0`，我限制系统仅使用一个 GPU。此调整显著改变了 GPU 资源利用率，该模型占用约 6GB 的 GPU 内存来高效处理请求。

![](https://cdn.thenewstack.io/media/2024/05/002127c3-1xgpu_load-1024x461.png)

## 如何运行代码

此设置过程为您提供了所有必要的工具和依赖项，这些工具和依赖项已正确配置，以便高效地运行和与聊天机器人交互。您需要的代码可在 GitHub 中获得，因此我避免在此处全部编写。我使用 Ubuntu 22.04 运行了该模型，但它可以在任何最新的
[Linux 操作系统](https://thenewstack.io/linux/) 上运行。

### 创建虚拟环境

初始化一个新的 [Python](https://roadmap.sh/python) 虚拟环境来管理依赖项：

```
python3 -m venv chatbot-env
```

### 激活虚拟环境

激活创建的环境以将其用于以下步骤：

```
source chatbot-env/bin/activate
```

### 克隆存储库

从我们的 GitHub 存储库下载项目代码：

```
git clone https://github.com/G-Core/ai-code-examples.git
```

### 安装依赖项：

从提供的需求文件中安装所有必需的库：

```

pip install -r requirements.txt
```

### 运行推理脚本：

使用 Python 启动聊天机器人应用程序：

```
python chat_bot.py
```

### 访问聊天机器人

**本地机器**

如果您在本地机器上运行聊天机器人，请打开网络浏览器并导航到本地服务器 URL：

```    
http://127.0.0.1:5050
```

您将看到此屏幕出现：

![](https://cdn.thenewstack.io/media/2024/05/10538727-login-gcore-1024x345.png)

**远程机器**

如果您在远程机器（例如云中）上运行聊天机器人，则需要使用端口转发技术。要使机器人可用于所有网络接口，请通过将 127.0.0.1 更改为 0.0.0.0 来修改代码中的服务器配置：

```
demo.launch(server_name="0.0.0.0", server_port=5050, auth=("user", "password")).queue().launch(root_path="/")
```

注意：在公共接口上公开机器人可能会带来安全风险，因此请确保您已采取适当的[安全措施](https://thenewstack.io/how-a-popular-combo-provides-ddos-protection/)。

## 结论

我在这里分享的开发过程为创建更知识渊博、响应更迅速且更有用的聊天机器人打开了大门，这些聊天机器人可以通过访问更新的信息并提供基于对上传文档的全面理解的答案来超越传统限制。这次聊天机器人开发之旅强调了整合新技术的重要性，以及定期更新开发策略以适应和纳入新进步以创建更智能、更高效和更用户友好的聊天机器人应用程序的必要性。

随着技术的不断进步，聊天机器人作为信息检索、客户参与和个性化协助工具的潜力仅受开发人员的创造力和创新力的限制。
