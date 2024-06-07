
<!--
title: 使用LangChain和Gemini构建AI应用程序
cover: https://cdn.thenewstack.io/media/2024/05/0786331e-rocket.png
-->

借助这些先进技术，您可以生成文本、分析图像并实现多模态 AI 交互。

> 译自 [LangChain and Google Gemini API for AI Apps: A Quickstart Guide](https://thenewstack.io/langchain-and-google-gemini-api-for-ai-apps-a-quickstart-guide/)，作者 Oladimeji Sowole。

整合文本、图像、音频和视频等多种方式对于创建复杂且引人入胜的 AI 应用程序变得越来越重要。[LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 和 Google 的 [Gemini API](https://thenewstack.io/exploring-the-api-of-googles-gemini-language-model/) 被证明是开发人员的完美搭档，提供了一套强大的工具包来帮助构建高级多模态 AI 解决方案。

## LangChain 和 Google 的 Gemini API 是什么？

### LangChain：构建 AI 应用程序的弹性框架

LangChain 是一个强大且灵活的框架，可以简化 AI 应用程序的开发。它提供了一种模块化且可组合的方法，允许技术人员组合各种工具（例如语言模型、知识库和数据源）来创建复杂的 AI 系统。借助 LangChain，开发人员可以利用最先进的自然语言处理 (NLP) 模型，集成外部数据源，并构建针对特定用例量身定制的自定义代理。

### Google 的 Gemini API：释放多模态 AI 的潜力

Google 的 Gemini API 是一个尖端的 AI 多模态平台，使开发人员能够构建可以同时理解和处理多种方式的应用程序。此 API 使用 Google 的高级机器学习模型和计算机视觉功能来分析和解释文本、图像、音频和视频数据。借助 Gemini，开发人员可以创建智能应用程序，以更类似于人类的方式感知和理解世界。

## 设置和安装

为了确保你的 Python 环境已准备好与 LangChain 和 Google 的 Gemini 协同工作，请使用 pip 安装必要的包：

```
pip install -q langchain-google-genai
pip install --upgrade -q langchain-google-genai
pip show langchain-google-genai
pip install -q google-generativeai
```

这些命令处理安装和升级专为 Google 的 Gemini 和 Gemini API 客户端库定制的 LangChain 包。

## 配置

要使用[Google 的 Gemini API](https://ai.google.dev/)，你需要一个 API 密钥。出于安全性和易于访问性的考虑，将此密钥存储在 `.env` 文件中：

```
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
```

如果 API 密钥未设置在你的环境变量中，以下脚本将提示你手动输入它：

```

import getpass
import os
if 'GOOGLE_API_KEY' not in os.environ:
    os.environ['GOOGLE_API_KEY'] = getpass.getpass('Provide your Google API Key: ')
```

## 探索可用模型

在深入了解具体功能之前，了解哪些模型可用很有用：

```
import google.generativeai as genai
for model in genai.list_models():
    print(model.name)
```

此代码段列出了可通过 Gemini API 访问的所有模型，允许你为你的任务选择合适的模型。

## 将 Gemini 与 LangChain 集成

### 基本设置

LangChain 简化了与 Gemini 模型的交互。以下是设置基本聊天界面的方法：

```
from langchain_google_genai import ChatGoogleGenerativeAI

# Create an instance of the LLM, using the 'gemini-pro' model with a specified creativity level
llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.9)

# Send a creative prompt to the LLM
response = llm.invoke('Write a paragraph about life on Mars in year 2100.')
print(response.content)
```

此代码使用 Gemini-pro 模型初始化 LangChain LLM 实例，并发送有关 2100 年火星生活的创意提示。

### 使用模板和链条的高级用法

LangChain 还支持更高级的模板和链式机制：

```
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set up a prompt template
prompt = PromptTemplate.from_template('You are a content creator. Write me a tweet about {topic}')

# Create a chain that utilizes both the LLM and the prompt template
chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
topic = 'Why will AI change the world'
response = chain.invoke(input=topic)
print(response)
```

此设置支持更结构化的交互，其中链条根据输入动态构建和发送提示。

## 系统提示和流式传输

### 系统提示

处理提示中的特定指令对于控制你的 AI 应用程序的行为至关重要：

```
from langchain_core.messages import HumanMessage, SystemMessage

# Setup with system message conversion
llm = ChatGoogleGenerativeAI(model='gemini-pro', convert_system_message_to_human=True)
output = llm.invoke([
    SystemMessage(content='Answer only YES or NO in French.'),
    HumanMessage(content='Is fish a mammal?')
])
print(output.content)
```

此方法对于创建结构化、受控的对话很有用，其中 AI 系统严格遵守给定的指令。

### 流式传输响应

对于较长的输出，流式传输至关重要：

```
# Send a prompt requiring detailed, continuous output
prompt = 'Write a scientific paper outlining the mathematical foundation of our universe.'
for chunk in llm.stream(prompt):
    print(chunk.content)
    print('-' * 100)
```

流式传输允许 API 更有效地处理较大的输出，将它们发送为可管理的块。

## 使用 Gemini Pro Vision 的多模态 AI

### 处理图像

Gemini Pro Vision 将功能扩展到图像分析：

```
from PIL import Image
img = Image.open('match.jpg') #change this with your image

# Setup for image analysis
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model='gemini-pro-vision')
prompt = 'What is in this image?'
message = HumanMessage(
  content=[
    {'type': 'text', 'text': prompt},
    {'type': 'image_url', 'image_url': img}
  ]
)
response = llm.invoke([message])
print(response.content)
```

此示例演示如何提示 AI 系统询问有关图像的问题并描述其内容。

## 结论

使用 LangChain 和 Gemini 的功能，你可以生成文本、分析图像并实现多模态 AI 交互。

集成这些先进技术使开发人员能够开发更智能、响应性更高且能够轻松处理复杂任务的 AI 系统。

无论你的目标是增强用户交互、自动响应还是分析视觉内容，你都可以将这些强大的工具整合到你的项目中。

开始实验并探索LangChain和Google的Gemini的潜力，将您的应用程序转化为更强大、更有创造力的平台。
