
<!--
title: 使用领域特定Jenkins知识增强现有的LLM模型
cover: https://www.jenkins.io/images/post-images/2024/08/llm-landing-dark.png
-->

Google Summer of Code 2024  使用特定领域 Jenkins 知识增强现有 LLM 模型。

> 译自 [Enhancing an Existing LLM Model with Domain-specific Jenkins Knowledge](https://www.jenkins.io/blog/2024/08/25/gsoc-enhancing-llm/)，作者 Nour Ziad Almulhem。

## 关于项目

JenAI 是一款开创性的聊天机器人，经过专门训练可以回答用户关于 Jenkins 技术的查询，从而增强软件的可访问性和可用性。

我们的目标是为用户提供更快、更可靠的帮助。该模型与友好的用户界面集成，以确保更好的用户体验。

项目成果：

1. 从不同来源收集数据集，例如 [Jenkins 博客](https://www.jenkins.io/blog/)、[社区问题](https://community.jenkins.io/c/using-jenkins/7) 和其他外部来源
2. 预处理此数据集以确保其干净且不会混淆模型
3. 根据此数据微调 llama2 并提供一个新的开源微调模型
4. 创建一个带有一个小型服务器的用户界面来与模型交互
5. 提供所有已完成工作的文档和用户指南，以在您的机器上本地使用我们的聊天机器人

## 为什么会有 JenAI：

- Jenkins 目前没有 AI 驱动的辅助技术来帮助 Jenkins 新用户。
- 该项目将 Jenkins 知识与人工智能相结合，为所有用户提供 Jenkins 专家通常拥有的知识，提供完整的解决方案。
- 我们授权用户通过流畅的用户界面与这些知识进行交互，而不是到处寻找答案。

## 里程碑

该项目包括我们已经经历的几个阶段：

**阶段 #1：数据收集**

使用不同的来源来收集 Jenkins 知识，例如 [jenkins 文档和博客](https://www.jenkins.io/blog/)、[discource 社区问题](https://community.jenkins.io/c/using-jenkins/7) 以及许多外部来源，例如 [stack overflow](https://stackoverflow.com/)、[ask ubuntu](https://askubuntu.com/) 和 [stack exchange](https://stackexchange.com/)。

**阶段 #2：数据预处理和细化**

此阶段包括 3 个部分：

- 第一个是利用另一个大型语言模型来帮助我们从 Jenkins 文档中生成问答对。
- 第二个是使用堆栈交换查询来获取在 stack overflow 和许多其他平台上提出的问题和正确解决方案的数据集。我们可以为这些问题和答案定义一个分数阈值，以确保我们收集的数据集的可靠性。生成的数据集包含 HTML 标签，如段落代码和许多无用的块或 URL，因此进行了进一步处理以删除所有无用信息。
- 最后一部分是利用 Discourse 上提供的社区问题，我们可以使用 [discource api](https://docs.discourse.org/) 来修剪 Jenkins 帖子并检索具有已批准解决方案的帖子，然后我们可以执行另一个请求来检索这些帖子及其答案。

所有这些部分都是自动化的，并且用于创建数据集的笔记本在我们的存储库中提供。为此，我们设法收集了大约 4100 对；其中一部分用于微调我们的模型。

**阶段 #3：JenAI 作为一个系统**

此阶段是关于创建具有友好用户界面的软件作为该项目的一部分，以与模型进行交互。我们使用 ReactJs、Typescript 和 MUI 组件来帮助我们创建界面。

我们还使用 Flask 创建了一个只有一个端点的小型服务器，以便通过 Rest API 与模型交互并确保流畅的通信。

**阶段 #4：微调**

我们项目的核心，微调的工作是迭代的，并一直持续到我们确保其性能。这里进行了大量研究，以确保最佳参数和微调模型和获得准确结果的最佳方法。

我们使用 Colab 和 Kaggle 免费资源来微调我们的模型，因为它们提供了一个具有大约 16 GB VRAM 的 T4 GPU，这足以加载和微调我们的模型。

微调的详细信息、方法和参数在我们的 [最终文档](https://github.com/nouralmulhem/Enhancing-LLM-with-Jenkins-Knowledge/blob/main/JenAi%20Final%20Document.pdf) 中提供：

**阶段 #5：将模型转换为 GGML 格式和量化**

为了实现我们的目标，我们需要用户能够仅使用 CPU 在其本地机器上运行模型，而不是托管它。为此，我们使用 llama.cpp 将模型转换为 GGML 二进制格式（使用 `convert_hf_to_gguf.py` ），可以在 CPU 上加载和运行。
GGML 库的部分吸引力在于能够将这种二进制模型量化为更小的模型，从而可以更快地运行。Llama.cpp 存储库中有一个名为 `quantize` 的工具，可用于将模型转换为不同的量化级别。我们使用 `quantize` 工具将模型缩减为 `q8_0`。

## JenAI 作为一种系统

- 深色模式下的 JenAI 登录页

![](https://www.jenkins.io/images/post-images/2024/08/llm-landing-dark.png)

- 浅色模式下的 JenAI 登录页

![](https://www.jenkins.io/images/post-images/2024/08/llm-landing-white.png)

- JenAI 聊天页面

![](https://www.jenkins.io/images/post-images/2024/08/llm-chat-page.png)

## 后续步骤

这个想法可以进一步增强，并且提供了许多方法来实现相同的目标：

- 使用检索增强生成 (RAG)，它结合了数据库或传统信息检索系统的优势与大型语言模型的功能
- Llama3 已经过超过 15 万亿个标记的预训练，其训练数据集比 Llama2 使用的数据集大 7 倍，这使得它在针对 Jenkins 知识进行微调时可以胜过 Llama2。

## 致谢

我想借此机会向以下人员表示感谢：

- Google Summer of Code 组织了这次活动，他们的导师在整个项目中提供了帮助。
- Jenkins 和 GSoC 组织管理员让我为这个具有挑战性的问题做出贡献，并感谢您一路上的灵活性。
- 我的团队导师 [Kris Stern](https://www.jenkins.io/blog/authors/krisstern/)（首席导师）、[Bruno Verachten](https://www.jenkins.io/blog/authors/gounthar/)、[Harsh Pratap Singh](https://www.jenkins.io/blog/authors/harsh-ps-2003/) 和 [Shivay Lamba](https://www.jenkins.io/blog/authors/shivaylamba/)，感谢他们在整个项目中提供的持续支持和指导，回答我的问题并指出一些很棒的想法，这样我们就不会留下任何未完成的事情。他们是使这一切取得成功的伟大原因。
