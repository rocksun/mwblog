几个月前，我们用不到 10 分钟构建了一个 [AI 聊天机器人](https://thenewstack.io/build-a-python-chatgpt-3-5-chatbot-in-10-minutes/)。今天，我们将直接在终端中构建一个类似的[聊天机器人](https://thenewstack.io/a-practical-guide-to-building-a-rag-powered-chatbot/)。在终端中构建类似的东西有什么价值？直接在终端中工作可以让你保持在开发流程中。它可以与你的本地文件、工具和系统交互。本质上，终端聊天机器人将 AI 直接带入你的环境。你可以向 [ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/) 提问，让它审查或生成代码，甚至运行命令，而无需任何上下文切换。

我们要构建的聊天机器人将比我们之前构建的更进一步。终端聊天机器人将包括相同的对话功能，但我们还将使其能够回复代码片段和 shell 命令。

*注意：在将 ChatGPT 或任何其他 AI 构建到你的系统中之前，请花时间阅读你使用的 AI 版本的训练数据和隐私政策，以便你可以安全地使用 AI。*

### 首先，让我们使用 OpenAI 进行设置

1.  转到 https://platform.openai.com/signup 并创建一个帐户。
2.  登录后，转到 <https://platform.openai.com/account/api-keys>。
3.  单击 Create new secret key（创建新的密钥）。
4.  复制密钥（以 sk-… 开头）。不要分享你的 API 密钥。

GPT-3.5 是免费的，但任何更高的版本（4.0 是我们现在使用的基本模型）仅适用于按需付费用户，不适用于免费帐户。以下教程使用 GPT-4.0。我支付了最低 10 美元的费用。也就是说，你可以使用 GPT-3.5 构建它。我将在代码中注明指定 3.5 的位置。

让我们转到终端。

## 基本设置

通过复制并粘贴以下代码来设置你的项目文件夹：

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | mkdir terminal-chatbot |
|   | cd terminal-chatbot |

在 [Gist](https://gist.github.com/JessicaWachtel/5ec29b2daee155a5748639a3cebb31b7) 上查看代码。

下一步是创建并激活一个虚拟 [Python](https://thenewstack.io/python/) 环境。我们想要创建一个虚拟环境，因为它提供了一个安全、隔离的工作区。它可以使所有内容井井有条、可预测且无冲突。我们没有设置虚拟环境，因为聊天机器人本身可能会导致问题。

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | python3 -m venv venv |
|   | source venv/bin/activate |

在 [Gist](https://gist.github.com/JessicaWachtel/0a1fcda01b0014dce74679f66c943dbe) 上查看代码。

在此代码之后，你应该在终端提示符中看到 (venv)。

现在是安装所需软件包的时候了。对于此项目，我们需要 `openai`，这是用于与 OpenAI 的 API 交互的官方 Python 客户端库。我们还需要 `python-dotenv`。`python-dotenv` 允许你的代码自动读取 `.env` 变量。

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | pip install openai python-dotenv |

在 [Gist](https://gist.github.com/JessicaWachtel/073c5672d3eea1bbd63b481a28cd0b83) 上查看代码。

让我们将我们的 API 密钥存储在 `.env` 文件中。为此，我们将使用 nano。

打开 nano。

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

在 [Gist](https://gist.github.com/JessicaWachtel/eb482b5dbdb61a17ac8e81e18ed0997c) 上查看代码。

将你的密钥粘贴到其中：

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | OPENAI\_API\_KEY=YOUR KEY HERE |

在 [Gist](https://gist.github.com/JessicaWachtel/16237ef842680b9065769ef5c16be1df) 上查看代码。

你可以使用以下命令保存并退出 nano：

*   `Ctrl + O`（字母，不是数字）保存。
*   `Enter` 确认。
*   `Ctrl + X` 退出。

## 创建聊天机器人脚本

我们将再次使用 nano 来创建代码文件。还有其他方法可以做到这一点，但我喜欢 nano。如果你喜欢文本文件或其他文件，请随时使用。

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

在 [Gist](https://gist.github.com/JessicaWachtel/19eb572cfe91b5ad3a27116d2c42b701) 上查看代码。

打开文件后，将接下来几个部分中的所有代码粘贴到文件中。我在这里将它们分开是为了解释每个块的作用，但它们都是同一个文件的一部分。

导入我们的依赖项：

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | # -\*- coding: utf-8 -\*- |
|   | import os |
|   | from openai import OpenAI |
|   | from dotenv import load\_dotenv |

在 [Gist](https://gist.github.com/JessicaWachtel/0f4114e0a0efba77acedd625b510640d) 上查看代码。

然后，我们想要加载我们的环境变量并创建 OpenAI API 客户端：

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | # load variables from .env file |
|   | load\_dotenv() |
|   |  |
|   | # create OpenAI API client |
|   | client = OpenAI(api\_key=os.getenv("OPENAI\_API\_KEY")) |

在 [Gist](https://gist.github.com/JessicaWachtel/1908502d8364509c32c0fb6fc757d390) 上查看代码。

现在我们准备好添加与 ChatGPT 的连接。函数 `connect_to_gpt` 会将当前的对话发送到 ChatGPT，并将 ChatGPT 的回复作为纯文本返回。这允许你进行一致的对话，其中它“记住”上下文和已共享的内容。

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | def connect\_to\_gpt(history): |
|   | response = client.chat.completions.create( |
|   | model="gpt-4", # Change to "gpt-3.5" if you have a free account |
|   | messages=history |
|   | ) |
|   | return response.choices[0].message.content |

在 [Gist](https://gist.github.com/JessicaWachtel/38b121bc4913bed7200f24703784a2a3) 上查看代码。

以下行表示“如果你直接运行此文件”（而不是将其作为模块导入），则运行以下代码。它会通过打印“Let’s get started! Type ‘exit’ to quit.\n”来让你知道聊天机器人何时准备就绪

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | def connect\_to\_gpt(history): |
|   | response = client.chat.completions.create( |
|   | model="gpt-4", # Change to "gpt-3.5" if you have a free account |
|   | messages=history |
|   | ) |
|   | return response.choices[0].message.content |

在 [Gist](https://gist.github.com/JessicaWachtel/342211d50c626c7ab5a05475ea15be9b) 上查看代码。

以下代码是驱动你的聊天会话的循环的一部分。它将对话初始化为一个名为 `chat_history` 的空列表。这就是存储对话并允许 ChatGPT 根据已讨论的内容获得上下文的原因。

无限循环 `while True` 会保持对话进行，直到他们退出。它还会读取用户输入并检查用户是否已退出。

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | chat\_history = [] # stores conversation history for normal chat |
|   |  |
|   | while True: |
|   | user\_input = input("You > ").strip() |
|   |  |
|   | if user\_input.lower() in {"exit", "quit"}: |
|   | print("Goodbye!") |
|   | break |

在 [Gist](https://gist.github.com/JessicaWachtel/6a128c1b25ebf646f385000713401f6a) 上查看代码。

下一段代码检查用户是否想要以代码形式获得答案。如果用户输入以 `/cmd` 或 `/code` 开头，则聊天机器人将使用代码回复。

系统消息是 AI 的指令。通过键入“You are a helpful assistant that ONLY responds with shell commands or code snippets. No explanations.”，你可以引导 AI 给出重点突出、简洁的答案。

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | #if user wants a reply in code |
|   | if user\_input.startswith("/code") or user\_input.startswith("/cmd"): |
|   | prompt = user\_input.split(" ", 1)[1] if " " in user\_input else "" |
|   | system\_message = { |
|   | "role": "system", |
|   | "content": "You are a helpful assistant that ONLY responds with shell commands or code snippets. No explanations." |
|   | } |

在 [Gist](https://gist.github.com/JessicaWachtel/e65c5bb4f34756f9dc402fcd36a1b28e) 上查看代码。

下一段代码构建要发送到 OpenAI 的请求并打印回复。

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | # prepare messages with system instructions + user prompt |
|   | messages = [ |
|   | system\_message, |
|   | {"role": "user", "content": prompt} |
|   | ] |
|   | reply = connect\_to\_gpt(messages) |
|   | print(f"Chatbot > {reply}\n") |

在 [Gist](https://gist.github.com/JessicaWachtel/fa61a93e4f15f175d13ddda1655b1f79) 上查看代码。

以下代码处理正常聊天模式，即用户不想要代码回复。

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | #regular conversation |
|   | else: |
|   | chat\_history.append({"role": "user", "content": user\_input}) |
|   | reply = connect\_to\_gpt(chat\_history) |
|   | print(f"Chatbot > {reply}\n") |
|   | chat\_history.append({"role": "assistant", "content": reply}) |

在 [Gist](https://gist.github.com/JessicaWachtel/a3d8518b967e0522d6c0dc8ccd1df536) 上查看代码。

你可以使用以下命令保存并退出 nano：

*   `Ctrl + O`（字母，不是数字）保存。
*   `Enter` 确认。
*   `Ctrl + X` 退出。

这是完整的代码文件：

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | # -\*- coding: utf-8 -\*- |
|   | import os |
|   | from openai import OpenAI |
|   | from dotenv import load\_dotenv |
|   |  |
|   | # load variables from .env file |
|   | load\_dotenv() |
|   |  |
|   | # create OpenAI API client |
|   | client = OpenAI(api\_key=os.getenv("OPENAI\_API\_KEY")) |
|   |  |
|   | def connect\_to\_gpt(history): |
|   | response = client.chat.completions.create( |
|   | model="gpt-4", # Change to "gpt-3.5" if you have a free account |
|   | messages=history |
|   | ) |
|   | return response.choices[0].message.content |
|   |  |
|   | if \_\_name\_\_ == "\_\_main\_\_": |
|   | print("Terminal Chatbot Ready! Type 'exit' to quit.\n") |
|   |  |
|   | chat\_history = [] # stores conversation history for normal chat |
|   |  |
|   | while True: |
|   | user\_input = input("You > ").strip() |
|   |  |
|   | if user\_input.lower() in {"exit", "quit"}: |
|   | print("Goodbye!") |
|   | break |
|   |  |
|   | if user\_input.startswith("/code") or user\_input.startswith("/cmd"): |
|   | prompt = user\_input.split(" ", 1)[1] if " " in user\_input else "" |
|   | system\_message = { |
|   | "role": "system", |
|   | "content": "You are a helpful assistant that ONLY responds with shell commands or code snippets. No explanations." |
|   | } |
|   |  |
|   | # prepare messages with system instructions + user prompt |
|   | messages = [ |
|   | system\_message, |
|   | {"role": "user", "content": prompt} |
|   | ] |
|   | reply = connect\_to\_gpt(messages) |
|   | print(f"Chatbot > {reply}\n") |
|   |  |
|   | #regular conversation |
|   | else: |
|   | chat\_history.append({"role": "user", "content": user\_input}) |
|   | reply = connect\_to\_gpt(chat\_history) |
|   | print(f"Chatbot > {reply}\n") |
|   | chat\_history.append({"role": "assistant", "content": reply}) |

在 [Gist](https://gist.github.com/JessicaWachtel/9e671a02c11f586d34ee9fc06e7d0245) 上查看代码。

你可以使用以下命令运行聊天机器人：

此文件包含隐藏的或双向的 Unicode 文本，这些文本可能会以不同于以下显示的方式进行解释或编译。要查看，请在显示隐藏 Unicode 字符的编辑器中打开该文件。
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)

在 [Gist](https://gist.github.com/JessicaWachtel/96633956a356f5b05dda6d13fb877e08) 上查看代码。

测试一下！尝试请求代码：/code bash command to list all .txt files recursively（/code bash 命令以递归方式列出所有 .txt 文件）。

或者只是用简单的英语问它一个问题。