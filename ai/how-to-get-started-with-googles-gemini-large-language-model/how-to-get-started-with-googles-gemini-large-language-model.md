<!--
title: 谷歌Gemini语言模型入门指南
cover: https://cdn.thenewstack.io/media/2024/02/d04bd01d-12photostory-ndiecok1nq-unsplash-1024x684.jpg
-->

本文向您介绍两种访问谷歌Gemini语言模型的途径:Vertex AI和Google AI Studio，并详细阐述每种方法的使用入门指南。

> 译自 [How to Get Started with Google’s Gemini Large Language Model](https://thenewstack.io/how-to-get-started-with-googles-gemini-large-language-model/)，作者 Janakiram MSV。


在我之前的文章中，我介绍了谷歌的多模态生成 AI 模型 Gemini 的[关键功能](https://yylives.cc/2024/02/21/gemini-all-you-need-to-know-about-googles-multimodal-ai/)。在这篇文章中，我将带领大家了解如何访问这个模型。

有两种方式可以访问 Gemini:[Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview) 和 [Google AI Studio](https://aistudio.google.com/app/)。前者面向熟悉 [Google Cloud](https://thenewstack.io/generative-ai-cloud-services-aws-azure-or-google-cloud/) 的开发者，而后者面向利用 Google Cloud 构建 Web 和移动应用的开发者。

让我们来看看这两种方法。

## 通过 Vertex AI 访问 Gemini

假设您已经拥有一个启用了计费的活跃项目，以下是从本地工作站访问 API 的步骤。

创建一个 [Python 虚拟环境](https://thenewstack.io/set-up-python-on-fedora-linux-4-steps/)并安装所需的模块。

```bash
$ python -m venv venv
$ source venv/bin/activate
```

由于我们需要通过 Google Cloud 进行身份验证，让我们运行以下命令来缓存凭据。这将被 Google Cloud SDK 在调用 API 端点时使用。这种方法会在您的开发工作站的 $HOME/.config/gcloud/application_default_credentials.json 中创建应用默认凭据(ADC)。

```bash
$ gcloud init
$ gcloud auth application-default login
```

您会看到浏览器窗口弹出，要求您的谷歌凭据来完成认证过程。完成此操作后，继续执行下一步安装 Python 模块。

```bash
$ pip install -U google-cloud-aiplatform
$ pip install -U jupyter
```

启动 Jupyter Lab，并从您喜欢的浏览器访问它。


```bash
$ jupyter notebook --ip='0.0.0.0' --no-browser --NotebookApp.token='' --NotebookApp.password=''
```

首先导入模块，然后初始化模型。

```bash
from google.cloud import aiplatform   
import vertexai
from vertexai.preview.generative_models import GenerativeModel， Part
```

vertexai.preview 模块提供了访问 Vertex AI 中可用的基础模型的功能。请检查文档获取最新版本和更新的 API。

```bash
vertexai.init()
model = GenerativeModel("gemini-pro")
```

与其他语言模型一样，Gemini 有两种 API:文本生成和聊天补全。

我们先试试文本生成 API。

```bash
response = model.generate_content("I have a Python in the backyard. What should I do?")
print(response.text)
```

![](https://cdn.thenewstack.io/media/2024/02/4b8a9103-gemini-api-1-1024x470.jpg)

接下来，让我们探索聊天补全 API。文本生成和聊天补全的关键区别在于能够在历史记录列表中维护对话历史。传递历史记录列表可以自动为模型提供上下文。它甚至可以保存到本地磁盘并加载以接上同一线程。

```bash
chat = model.start_chat(history=[])  
response = chat.send_message("In one sentence， explain how a computer works to a young child.")
response.text
```

```bas
response = chat.send_message("Okay， how about a more detailed explanation to a high schooler?")
response.text
```

您可以访问历史记录列表以查看整个对话。

## 通过 Google AI Studio 访问 Gemini

Google AI Studio 是一个探索谷歌提供的生成式 AI 模型的游乐场。任何拥有谷歌账户的人都可以登录进行模型实验。然而，对于生产环境的使用，您仍然需要在 Google Cloud 上拥有一个活跃的项目。

创建一个 API 密钥并初始化一个环境变量。

![](https://cdn.thenewstack.io/media/2024/02/9bee271c-gemini-api-3.jpg)


```bash
$ export GOOGLE_API_KEY=YOUR_API_KEY
```

您需要一个不同的 Python 模块通过 AI Studio 访问模型。  

```bash
$ pip install -U google-generativeai
```

导入模块并查看是否可以列出可用的模型。

```py
import os
import google.generativeai as genai
```

```py
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
```

```py
models=genai.list_models()
for m in models:
    print(m.name)
```

![](https://cdn.thenewstack.io/media/2024/02/d4f1792d-gemini-api-4.jpg)

如您所见，我们可以访问 Gemini Pro 多模态模型。让我们初始化该模型。

```py
model = genai.GenerativeModel('gemini-pro')
```

现在我们重复执行文本生成和聊天补全的步骤。

```py
response = model.generate_content("I have a Python in the backyard. What should I do?")
print(response.text)
```

![](https://cdn.thenewstack.io/media/2024/02/29b50d79-gemini-api-2-1024x772.jpg)

```py
chat = model.start_chat(history=[])
response = chat.send_message("In one sentence， explain how a computer works to a young child.")  
print(response.text)
response = chat.send_message("Okay， how about a more detailed explanation to a high schooler?")
print(response.text)
```

![](https://cdn.thenewstack.io/media/2024/02/e67434a9-gemini-api-1a-1024x550.jpg)

## 计算令牌数以估计成本

根据谷歌的说法，文本输入的费用是根据输入(提示 prompt)的每个 1，000 个字符和输出(响应 response)的每个 1，000 个字符收取的。字符由 UTF-8 代码点计数，空格不包括在内。API 有方法提供令牌数 `token counts`，帮助我们估计成本。下面的代码使用 count_tokens 方法和 `usage_metadata` 属性将提示和 LLM 响应转换成可计费令牌。

```py
import vertexai
from google.cloud import aiplatform 
from vertexai.preview.generative_models import GenerativeModel， Part

vertexai.init()
model = GenerativeModel("gemini-pro")

vertexai.init()  
model = GenerativeModel("gemini-pro")

print(len(prompt))
# 43

print(model.count_tokens(prompt)) 
# total_tokens: 11
# total_billable_characters: 34

response = model.generate_content(prompt)
print(response.text)

print(response._raw_response.usage_metadata) 
# prompt_token_count: 11
# candidates_token_count: 129
# total_token_count: 140
```

在本教程系列的下一部分，我们将探索使用 Gemini 的 prompt engineering 的基础知识。敬请期待。
