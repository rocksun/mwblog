<!--
title: 几分钟搭建你的AI终端聊天机器人
cover: https://cdn.thenewstack.io/media/2025/07/6d541ee5-mohamed-nohassi-2iurk025cec-unsplash.jpg
summary: 本文介绍了如何在终端中构建一个 AI 聊天机器人，包括设置 OpenAI API 密钥、创建 Python 虚拟环境、安装所需软件包，以及编写聊天机器人脚本。该聊天机器人可以回复代码片段和 shell 命令。
-->

本文介绍了如何在终端中构建一个 AI 聊天机器人，包括设置 OpenAI API 密钥、创建 Python 虚拟环境、安装所需软件包，以及编写聊天机器人脚本。该聊天机器人可以回复代码片段和 shell 命令。

> 译自：[Build Your Own AI Terminal Chatbot in Minutes](https://thenewstack.io/build-your-own-ai-terminal-chatbot-in-minutes/)
> 
> 作者：Jessica Wachtel

几个月前，我们用不到 10 分钟构建了一个 [AI 聊天机器人](https://thenewstack.io/build-a-python-chatgpt-3-5-chatbot-in-10-minutes/)。今天，我们将直接在终端中构建一个类似的[聊天机器人](https://thenewstack.io/a-practical-guide-to-building-a-rag-powered-chatbot/)。在终端中构建类似的东西有什么价值？直接在终端中工作可以让你保持在开发流程中。它可以与你的本地文件、工具和系统交互。本质上，终端聊天机器人将 AI 直接带入你的环境。你可以向 [ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/) 提问，让它审查或生成代码，甚至运行命令，而无需任何上下文切换。

我们要构建的聊天机器人将比我们之前构建的更进一步。终端聊天机器人将包括相同的对话功能，但我们还将使其能够回复代码片段和 shell 命令。

*注意：在将 ChatGPT 或任何其他 AI 构建到你的系统中之前，请花时间阅读你使用的 AI 版本的训练数据和隐私政策，以便你可以安全地使用 AI。*

## 首先，让我们使用 OpenAI 进行设置

1.  转到 https://platform.openai.com/signup 并创建一个帐户。
2.  登录后，转到 <https://platform.openai.com/account/api-keys>。
3.  单击 Create new secret key（创建新的密钥）。
4.  复制密钥（以 sk-… 开头）。不要分享你的 API 密钥。

GPT-3.5 是免费的，但任何更高的版本（4.0 是我们现在使用的基本模型）仅适用于按需付费用户，不适用于免费帐户。以下教程使用 GPT-4.0。我支付了最低 10 美元的费用。也就是说，你可以使用 GPT-3.5 构建它。我将在代码中注明指定 3.5 的位置。

让我们转到终端。

## 基本设置

通过复制并粘贴以下代码来设置你的项目文件夹：


```shell
mkdir terminal-chatbot
cd terminal-chatbot
```

下一步是创建并激活一个虚拟 [Python](https://thenewstack.io/python/) 环境。我们想要创建一个虚拟环境，因为它提供了一个安全、隔离的工作区。它可以使所有内容井井有条、可预测且无冲突。我们没有设置虚拟环境，因为聊天机器人本身可能会导致问题。

```shell
python3 -m venv venv
source venv/bin/activate
```

在此代码之后，你应该在终端提示符中看到 (venv)。

现在是安装所需软件包的时候了。对于此项目，我们需要 `openai`，这是用于与 OpenAI 的 API 交互的官方 Python 客户端库。我们还需要 `python-dotenv`。`python-dotenv` 允许你的代码自动读取 `.env` 变量。

```shell
pip install openai python-dotenv
```

让我们将我们的 API 密钥存储在 `.env` 文件中。为此，我们将使用 nano。

打开 nano。

```shell
nano .env
```

在将你的密钥粘贴到其中：

```shell
OPENAI_API_KEY=YOUR KEY HERE
```

你可以使用以下命令保存并退出 nano：

*   `Ctrl + O`（字母，不是数字）保存。
*   `Enter` 确认。
*   `Ctrl + X` 退出。

## 创建聊天机器人脚本

我们将再次使用 nano 来创建代码文件。还有其他方法可以做到这一点，但我喜欢 nano。如果你喜欢文本文件或其他文件，请随时使用。

```shell
nano chatbot.py
```

打开文件后，将接下来几个部分中的所有代码粘贴到文件中。我在这里将它们分开是为了解释每个块的作用，但它们都是同一个文件的一部分。

导入我们的依赖项：

```py
# -*- coding: utf-8 -*-
import os
from openai import OpenAI
from dotenv import load_dotenv
```

然后，我们想要加载我们的环境变量并创建 OpenAI API 客户端：

```py
# load variables from .env file
load_dotenv()

# create OpenAI API client 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

现在我们准备好添加与 ChatGPT 的连接。函数 `connect_to_gpt` 会将当前的对话发送到 ChatGPT，并将 ChatGPT 的回复作为纯文本返回。这允许你进行一致的对话，其中它“记住”上下文和已共享的内容。

```py
def connect_to_gpt(history):
    response = client.chat.completions.create(
        model="gpt-4",  # Change to "gpt-3.5" if you have a free account
        messages=history
    )
    return response.choices[0].message.content
```

以下行表示“如果你直接运行此文件”（而不是将其作为模块导入），则运行以下代码。它会通过打印“Let’s get started! Type ‘exit’ to quit.\n”来让你知道聊天机器人何时准备就绪

```py
def connect_to_gpt(history):
    response = client.chat.completions.create(
        model="gpt-4",  # Change to "gpt-3.5" if you have a free account
        messages=history
    )
    return response.choices[0].message.content
```

以下代码是驱动你的聊天会话的循环的一部分。它将对话初始化为一个名为 `chat_history` 的空列表。这就是存储对话并允许 ChatGPT 根据已讨论的内容获得上下文的原因。

无限循环 `while True` 会保持对话进行，直到他们退出。它还会读取用户输入并检查用户是否已退出。

```py
    chat_history = []  # stores conversation history for normal chat

    while True:
        user_input = input("You > ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
```

下一段代码检查用户是否想要以代码形式获得答案。如果用户输入以 `/cmd` 或 `/code` 开头，则聊天机器人将使用代码回复。

系统消息是 AI 的指令。通过键入“You are a helpful assistant that ONLY responds with shell commands or code snippets. No explanations.”，你可以引导 AI 给出重点突出、简洁的答案。

```py

      #if user wants a reply in code  
      if user_input.startswith("/code") or user_input.startswith("/cmd"):
            prompt = user_input.split(" ", 1)[1] if " " in user_input else ""
            system_message = {
                "role": "system",
                "content": "You are a helpful assistant that ONLY responds with shell commands or code snippets. No explanations."
            }
```

下一段代码构建要发送到 OpenAI 的请求并打印回复。

```py
            # prepare messages with system instructions + user prompt
            messages = [
                system_message,
                {"role": "user", "content": prompt}
            ]
            reply = connect_to_gpt(messages)
            print(f"Chatbot > {reply}\n")
```

以下代码处理正常聊天模式，即用户不想要代码回复。

```py
            #regular conversation
        else:
            chat_history.append({"role": "user", "content": user_input})
            reply = connect_to_gpt(chat_history)
            print(f"Chatbot > {reply}\n")
            chat_history.append({"role": "assistant", "content": reply})
```

你可以使用以下命令保存并退出 nano：

*   `Ctrl + O`（字母，不是数字）保存。
*   `Enter` 确认。
*   `Ctrl + X` 退出。

这是完整的代码文件：

```py
# -*- coding: utf-8 -*-
import os
from openai import OpenAI
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()

# create OpenAI API client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def connect_to_gpt(history):
    response = client.chat.completions.create(
        model="gpt-4",  # Change to "gpt-3.5" if you have a free account
        messages=history
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Terminal Chatbot Ready! Type 'exit' to quit.\n")

    chat_history = []  # stores conversation history for normal chat

    while True:
        user_input = input("You > ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if user_input.startswith("/code") or user_input.startswith("/cmd"):
            prompt = user_input.split(" ", 1)[1] if " " in user_input else ""
            system_message = {
                "role": "system",
                "content": "You are a helpful assistant that ONLY responds with shell commands or code snippets. No explanations."
            }

            # prepare messages with system instructions + user prompt
            messages = [
                system_message,
                {"role": "user", "content": prompt}
            ]
            reply = connect_to_gpt(messages)
            print(f"Chatbot > {reply}\n")

        #regular conversation
        else:
            chat_history.append({"role": "user", "content": user_input})
            reply = connect_to_gpt(chat_history)
            print(f"Chatbot > {reply}\n")
            chat_history.append({"role": "assistant", "content": reply})
```

你可以使用以下命令运行聊天机器人：

```shell
python3 chatbot.py
```

测试一下！尝试请求代码：/code bash command to list all .txt files recursively（/code bash 命令以递归方式列出所有 .txt 文件）。

或者只是用简单的英语问它一个问题。