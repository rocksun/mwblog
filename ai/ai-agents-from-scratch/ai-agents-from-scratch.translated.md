# 如何在没有框架的情况下构建 AI Agent：分步指南

![博客预览](/_next/image?url=%2Fblog%2FBlogHeader_AiAgentsFromScratch.jpg&w=3840&q=75)

AI Agent 常常过于复杂。从本质上讲，它们只是具有使用工具和记住上下文能力的语言模型。虽然像 [LangChain](https://www.langchain.com/) 或 [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) 这样的框架可以帮助你快速入门，但它们增加了抽象层，这会让你更难理解实际发生的事情，也更难为特定用例定制你的 Agent。

在本教程中，我们将从头开始构建一个 AI Agent，直接调用 GPT-4o 的 API。你将学习如何创建一个可以查询 PostgreSQL 数据库、从 Wikipedia 获取信息并通过简单的数据库存储来维护对话上下文的 Agent。没有框架，只有干净的代码和清晰的概念。

目标是证明 AI Agent 不需要复杂的架构。我们将专注于基本组件：用于工具使用的提示工程、在 PostgreSQL 中存储对话历史记录以及管理 LLM 及其工具之间的交互流程。

最后，你将确切地知道什么是 Agent，它是如何工作的以及如何构建它们。如果你仍然决定使用框架 - 那也没关系。但是，你将更好地了解底层发生的事情。

让我们首先了解是什么使某个事物成为 AI Agent，然后逐步构建一个。

## 什么是 AI Agent？

AI Agent 从根本上来说只是一个可以执行以下操作的语言模型：

- 了解它有哪些可用的工具
- 决定何时使用这些工具
- 记住之前的互动
- 根据所有这些信息做出决定

### 什么是工具？

工具（有时称为“函数”或“能力”）只是 Agent 可以调用以与外部世界交互的函数。它们只是具有以下特征的 Python 函数：

- 对它们的功能的清晰描述
- 定义的输入参数
- 结构化输出

这是一个工具的具体示例：

当我们让我们的 Agent 访问此工具时，我们实际上是在告诉它：“你可以通过调用此函数来搜索 Wikipedia。” 然后，LLM 根据用户的问题，决定是否需要使用此工具来提供好的答案。当我们说“LLM 决定”时，我们的意思是，我们使用可用的工具提示 LLM，并要求它决定使用哪一个。然后，AI 模型只是返回一个带有工具名称的文本响应。

**工具的常见示例包括：**

- 数据库查询
- 网络搜索
- API 调用
- 文件操作
- 计算器函数
- 电子邮件发送功能

为了将 Agent 和工具的概念结合在一起，我们看到没有涉及任何魔法。这只是 AI 模型交互和一堆 python 函数。

将这些结合在一起，AI Agent 的伪代码可能如下所示：

这是 Agent 的核心概念。其他一切——复杂的规划、多次工具调用、复杂的内存系统——只是这个基本模式的扩展。

**关于 Agent 的常见误解：**

- 它们不需要复杂的编排框架
- 它们不需要自主运行（尽管它们可以）
- 它们不需要复杂的规划算法（尽管这些算法可以帮助完成复杂的任务）

**构建有效 Agent 的关键不在于你使用的框架，而在于：**

- 编写清晰的提示，帮助 LLM 了解其功能
- 实施 Agent 可以使用的可靠工具
- 通过某种形式的内存存储来维护相关上下文

在以下各节中，我们将使用真实代码来实现此模式，构建一个可以实际查询数据库和搜索 Wikipedia 的 Agent。你将看到复杂性来自你的用例的特定要求，而不是来自 Agent 架构本身。

## 为什么要构建没有框架的 Agent？

通常建议使用像 LangChain 和 AutoGPT 这样的框架来构建 AI Agent。虽然它们对于快速原型设计很有用，但有令人信服的理由可以避免使用它们：

### 了解真正发生了什么

无框架版本更加明确。你可以清楚地看到：

- LLM 被告知了什么
- 何时调用工具
- 如何做出决定

### 灵活性和控制

框架通常对以下方面做出假设：

- 工具应该如何构建
- 提示格式应该是什么
- 内存应该如何工作

当你需要自定义其中任何一个时，你最终会与框架作斗争，而不是与它合作。

### 更简单的调试

当框架出现问题时：

**注意：** 这或多或少是你应该在没有框架的情况下构建 Agent 的最重要原因。框架抽象掉了任何 AI Agent 的核心 - LLM 交互。在不添加额外基础设施的情况下，你不知道使用的确切提示、回复的特定 LLM 答案以及使用的工具。这使得调试成为一场噩梦。

### 更低的学习成本
构建 Agent 需要理解：

- LLM Prompt 工程
- 工具集成
- 内存管理

框架增加了另一层：

- 框架特定的概念
- 配置选项
- 集成模式

当您只需要基本原理时，为什么还要同时学习两者？

### 性能和资源

框架通常：

- 加载不必要的组件
- 添加网络调用
- 包含未使用的功能

直接实现让您：

- 只加载您需要的内容
- 优化关键路径
- 控制资源使用

**注意：** 可以说，原始性能对于 AI Agent 来说不是最重要的，因为 AI 模型的交互本身就很慢。 因此，加载一些额外的模块并不会增加太多。

### 何时使用框架

在以下情况下，框架是有意义的：

- 您正在构建一个快速原型
- 您需要预构建的工具
- 您最初正在学习 Agent 概念

但对于生产系统或当您需要完全控制时，直接实现通常更好。

让我们继续从头开始构建我们的 Agent，您将看到直接实现是多么的简单。

## 逐步构建 AI Agent

在我们深入研究代码之前，让我们了解一下我们将在第一步中构建什么。 我们将从定义我们的工具开始 - 我们想要赋予我们的 Agent 的能力。

### 步骤 1：定义工具

在此步骤中，我们将创建两个工具：

- 一个 PostgreSQL 查询工具，允许 Agent 查询您的数据库并搜索存储在数据库中的信息。
- 一个 Wikipedia 搜索工具，允许 Agent 在 Wikipedia 中查找信息。

我们可以看到这两个工具截然不同，因此根据用户的问题，Agent 应该能够决定使用其中一个工具。

在为 OpenAI 的函数调用定义工具时，我们需要每个工具的三个组件：

- 一个 schema，告诉 LLM 该工具的作用以及如何使用它。 这基本上只是 python 函数的 json 描述。 一旦你看到例子，它就会变得更清楚。
- 该工具的实际实现（Python 函数）
- 错误处理，以确保我们的 Agent 在出现问题时表现得体

schema 特别重要，因为它充当 LLM 的文档。 将其视为编写 API 文档 - 您描述工具的越好，LLM 就会越好地使用它们。 重要的是 `name`（应与函数名称匹配）、`description`（工具的作用）和 `parameters`（我们需要什么函数参数值）。

对于我们的数据库工具，我们将：

- 仅允许 SELECT 查询以确保安全
- 以 JSON 格式返回结果以便于解析
- 包括数据库连接问题的错误处理

对于 Wikipedia 工具，我们将：

- 将结果限制为三个句子，以保持响应简洁
- 处理消歧义页面和缺失的文章
- 在搜索失败时返回结构化的错误消息

以下是我们如何实现这些工具：

### 步骤 2：创建 Agent 类 - 详细设计

在实现代码之前，让我们准确地了解我们正在构建什么以及它是如何工作的：

#### 核心概念

AI Agent 本质上是一个循环：

- 接收用户输入
- 决定是否使用工具
- 如果需要，使用工具
- 制定响应

#### 关键组件设计

##### 1. 消息管理

- 我们需要将对话历史记录维护为消息列表
- 每条消息都有一个特定的角色：“用户”、“助手”或“工具”
- 历史记录为 LLM 做出更好的决策提供了上下文
- 将其视为聊天应用程序的状态管理

##### 2. 工具执行系统

- 像命令调度程序一样工作：
- LLM 决定使用一个工具
- 我们收到一个结构化的函数调用
- 我们将其映射到我们实际的 Python 函数
- 我们处理执行和任何错误
- 我们为 LLM 格式化结果

##### 3. 主要处理循环

#### 错误处理策略

我们需要三个层次的错误处理：

- 工具级别错误（例如，数据库连接失败）
- LLM 级别错误（例如，API 问题）
- 常规处理错误（例如，JSON 解析）

#### 消息流示例

这种设计允许：

- 关注点分离清晰
- 易于调试和监控
- 使用新工具进行灵活扩展
- 强大的错误处理
- 可维护的代码库

请注意，我们将通用 Agent 结构实现为一个循环的一部分。 这意味着我们将工具调用的结果发送回 LLM，然后 LLM 决定是制定最终答案还是调用另一个工具。

#### 实现

### （可选）步骤 3：向我们的 Agent 添加内存

**注意：** 请考虑您是否需要内存。 您的应用程序是否真的需要存储和检索对话历史记录？ 通常，答案是否定的！ 但是如果您确实需要内存，这里是如何添加它的。

AI Agent 中的内存通常过于复杂。 让我们了解我们实际想要实现的目标：

#### 什么是 Agent 内存？

Agent 内存的核心只是：

- 存储对话及其上下文
- 在需要时检索相关信息
- 总结过往的过长交互

#### 我们将要实现的记忆类型

**对话历史**
- 存储：用户输入、代理回复、工具使用结果
- 目的：跟踪当前的对话流程

**总结记忆**
- 内容：更长对话的周期性总结
- 原因：防止上下文窗口溢出
- 方法：在 X 条消息后或按需创建总结

### 数据库模式

#### 记忆流

#### AI 代理的记忆实现

在我们继续之前...

## 有兴趣了解如何训练你自己的大型语言模型吗？

我们准备了一份经过充分研究的指南，介绍如何使用开源技术的最新进展来微调你自己的 LLM。这有很多优点，例如：

- 成本控制
- 数据隐私
- 出色的性能 - 专门为你预期的用途进行调整

### 步骤 4：使用你的 AI 代理

完成所有设置后，使用代理非常简单。方法如下：

就是这样！代理将：

- 在需要时使用数据库
- 在适当时搜索维基百科
- 记住之前的上下文
- 自动创建总结
- 在幕后处理所有复杂性 - 但同时让我们能够直接进行调试

输出看起来干净自然：

## 增强的具有模式意识的数据库工具

可以说，上面的 PostgreSQL 数据库工具有点简单，不是吗？AI 模型应该从哪里知道哪些数据库列可用？你是对的 - 为了更清晰起见，我们省略了这个关键细节。我们将修改我们的数据库工具以包含模式信息，这有助于 LLM 了解哪些数据可用以及如何正确查询它：

主要改进：

- 工具描述中的模式信息
- 包括列类型和约束
- 错误时返回模式以实现更好的错误处理
- 具有列名称的详细结果结构

这有助于 LLM：

- 第一次尝试就编写正确的查询
- 了解可用数据
- 更好地处理错误
- 提供更详细的响应