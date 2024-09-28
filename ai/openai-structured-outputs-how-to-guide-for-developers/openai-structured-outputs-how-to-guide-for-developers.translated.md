# OpenAI 结构化输出：开发者操作指南

![OpenAI 结构化输出：开发者操作指南的特色图片](https://cdn.thenewstack.io/media/2024/09/60870d89-openai-structured-outputs-1024x576.jpg)

OpenAI 新的[结构化输出](https://thenewstack.io/openais-chatgpt-now-formats-output-to-developer-queries/)功能旨在确保模型生成的输出与您提供的 JSON 模式完全匹配。此功能对于需要一致且结构化数据格式的开发人员特别有用，无论是用于 API 集成、数据处理还是应用程序开发。

我将指导您开始使用结构化输出，包括设置环境、定义 [JSON](https://thenewstack.io/how-to-use-json-in-your-python-code/) 模式以及使用 OpenAI API 生成符合您规范的模型输出。

## 结构化输出简介

结构化输出允许您通过定义模型输出必须遵循的 JSON 模式来强制执行特定的数据格式。这确保了模型生成的数据既可预测又可靠，可以无缝地融入您现有的数据工作流程。结构化输出可以通过两种主要方式实现：通过[函数调用](https://thenewstack.io/getting-started-with-function-calling-in-llms/)和使用带有新 **json_schema** 选项的 **response_format** 参数。

### 为什么使用结构化输出？

当您需要以下内容时，结构化输出非常有用：

- 与需要特定格式数据的其他 API 集成。
- 确保模型返回的数据一致性，减少对额外验证或格式化的需求。
- 简化在依赖结构化数据的应用程序（例如数据库或 Web 服务）中使用 [大型语言模型 (LLM)](https://thenewstack.io/llm/) 的过程。

## 入门

### 先决条件

在深入研究结构化输出之前，请确保您具备以下条件：

- 在您的机器上安装了 [Python](https://roadmap.sh/python)。
- 一个 [OpenAI API 密钥](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)。
- **dotenv**库，用于管理环境变量。您可以[使用 pip](https://thenewstack.io/how-to-use-python-pip-and-why-you-need-to/)安装必要的库：

```bash
pip install openai python-dotenv
```

### 设置您的环境

首先在您的项目目录中创建一个 **.env** 文件，以安全地存储您的 OpenAI API 密钥：

```
OPENAI_API_KEY=your_openai_api_key
```

接下来，在您的 Python 脚本中加载此 API 密钥以与 OpenAI API 交互：

## 在 OpenAI API 中使用结构化输出

让我们逐步介绍如何在实践中使用结构化输出，重点关注函数调用和 **response_format** 参数。

### 1. 定义 JSON 模式

首先，定义一个模型输出应符合的 JSON 模式。对于此示例，我假设您正在使用一个简单的用户配置文件数据模式。

此模式指定输出必须是一个包含三个字段的对象：`name`、`age` 和 `email`。**name** 字段是一个字符串，**age** 是一个整数，**email** 必须遵循电子邮件格式。

### 2. 设置 API 请求

接下来，设置一个 API 请求，指示模型生成与此模式匹配的数据。使用带有 **json_schema** 选项的 **response_format** 参数来强制执行结构。

### 3. 将函数调用与结构化输出一起使用

利用结构化输出的另一种方法是通过函数调用。这种方法允许您根据提供的模式定义模型可以调用的特定函数。以下是实现方法：

#### a. 定义函数

#### b. 向 OpenAI 注册函数

您需要将函数注册为模型可以调用的工具。

#### c. 生成输出

现在，您可以通过 API 调用函数来生成输出。

#### d. 验证输出

获得输出后，务必根据模式对其进行验证，以确保其满足所有指定的要求。尽管 API 尝试符合模式，但最好添加额外的验证层。

## 处理错误和异常

使用结构化输出时，如果模型的输出与定义的模式不匹配，则可能会遇到错误。优雅地处理这些错误对于构建强大的应用程序至关重要。

## 结论

结构化输出是一个强大的功能，使开发人员能够使用 JSON 模式在模型输出中强制执行特定的数据格式。无论是通过函数调用还是 **response_format** 参数，此功能都可确保模型生成的输出是可预测的、一致的，并且可以与其他系统集成。
按照本指南中概述的步骤，您可以开始在自己的项目中使用结构化输出，从而提高 AI 应用程序的可靠性和实用性。无论您是与 API 集成、使用数据库还是构建数据驱动的应用程序，结构化输出都可以帮助您维护数据的完整性并减少对后处理的需求。

立即开始尝试结构化输出，了解此功能如何简化您的工作流程并增强应用程序的功能。

***

> 您是否正在计划自己的 AI 项目？阅读《技术领导者 AI 入门指南》，了解如何最好地将 AI 用于您的业务和用例。

[YOUTUBE.COM/THENEWSTACK
技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等内容。](https://youtube.com/thenewstack?sub_confirmation=1)