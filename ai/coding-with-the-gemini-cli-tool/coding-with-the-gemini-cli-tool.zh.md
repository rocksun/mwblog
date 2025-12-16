不久前，[谷歌](https://cloud.google.com/?utm_content=inline+mention)发布了令人印象深刻的 [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/)（命令行界面）工具。

与许多 [AI 工具](https://thenewstack.io/the-top-ai-tool-for-devs-isnt-github-copilot-new-report-finds/)不同，Gemini CLI 应用程序是本地安装的，因此你无需担心你的查询（或其结果）被用于任何恶意目的。

目前，Gemini CLI 的特点包括：

*   完全开源，允许用户检查代码并为其贡献。
*   由 Gemini 2.5 Pro 提供支持。
*   免费套餐允许个人谷歌账户每分钟发起 60 次请求，每天 1000 次请求。
*   包含谷歌搜索、文件操作和 Shell 命令工具，以增强功能。
*   支持自定义集成，并增强 AI 理解上下文的能力。

正如你可能从名字中猜测的那样，Gemini CLI 是一个纯命令行工具，没有图形用户界面（GUI）。如果你不习惯使用命令行，那么 Gemini CLI 可能不适合你。

另一方面，如果你在终端窗口中得心应手，Gemini CLI 很容易成为你编程旅程中的又一个工具。你可以使用 Gemini CLI 帮助你学习如何使用一门新的编程语言，如何提升你在特定语言方面的技能，等等。

让我们了解如何安装这个方便的工具，然后如何使用它来学习一些关于 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 的知识。

我们开始吧？

## 你需要什么

要实现此功能，你需要任何支持 [Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) 和 NPM 的操作系统。我将在 Zorin OS 上演示安装，它基于 [Ubuntu Linux](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)。在 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 上，你还需要一个具有 sudo 权限的用户。

我们开始动手吧。

## 安装先决条件

在安装 Gemini CLI 之前，你必须首先安装 [Node.js](http://node.js) 和 NPM。为此，我们将运行以下命令：

```
sudo apt-get install nodejs npm -y
```

完成这些后，你就可以安装 Gemini CLI 了。

## 安装 Gemini CLI

你可以使用一个命令安装 Gemini CLI：

```
sudo npm install -g @google/gemini-cli
```

这会花一两分钟完成，但应该会顺利进行。

你还没完成。

你必须使用你的个人谷歌账户验证 Gemini CLI。为此，请打开你的默认网络浏览器，并确保你已登录谷歌账户。完成此操作后，返回终端窗口并发出命令：

```
gemini
```

如果你收到错误，这意味着你的发行版安装了旧版本的 Node.js。要解决这个问题，请执行以下操作：

```
curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh
sudo -E bash nodesource_setup.sh
sudo apt-get install nodejs -y
```

完成此操作后，重新运行 `gemini` 命令。然后系统会提示你选择一种身份验证方法（**图 1**）。确保选择了“使用谷歌登录”并按下 Enter 键。

[![](https://cdn.thenewstack.io/media/2025/12/c0f5d803-geminicli1.jpg)](https://cdn.thenewstack.io/media/2025/12/c0f5d803-geminicli1.jpg)

**图 1：** 如果你愿意，可以使用 Gemini API 密钥或 Vertex AI 进行身份验证。

当你的默认网络浏览器打开时，如果你尚未登录谷歌账户，请立即登录。

当系统提示时，点击“登录”，你将被告知身份验证成功，届时你可以关闭浏览器，会发现 Gemini CLI 已准备好接收你的第一个查询。

暂时不要查询。

通过两次按下 Ctrl+c 组合键关闭 Gemini。

## 让我们学习一些关于 JavaScript 的知识

使用终端窗口，通过以下命令创建一个新的项目目录：

```
mkdir JS_PROJECT
```

使用以下命令进入该目录：

```
cd JS_PROJECT
```

现在，再次运行 `gemini` 命令。这次的不同之处在于你正在一个特定目录中工作（而不是你的主目录）。

从 Gemini 主窗口（图 2）中，我们发出以下查询：

```
How do I create a drop-down list in JavaScript?
```

![](https://cdn.thenewstack.io/media/2025/12/91827f73-gemini2.jpg)

**图 2：** Gemini CLI 已准备好进行你的首次查询。

按下 Enter 键，Gemini 将开始工作。

在它工作时，很可能会提示你同意某些任务，或者提示你允许它创建文件（**图 3**）。

[![](https://cdn.thenewstack.io/media/2025/12/a59fb739-gemini3.jpg)](https://cdn.thenewstack.io/media/2025/12/a59fb739-gemini3.jpg)

**图 3：** 反抗是徒劳的，所以请允许它创建文件。

继续允许 Gemini 执行它所需的操作，因为它正在执行我们要求它完成的工作。

几分钟后，Gemini 提示我用网络浏览器打开 index.html 文件，以查看下拉菜单的效果（**图 4**）。

[![](https://cdn.thenewstack.io/media/2025/12/e2cc7f31-gemini4.jpg)](https://cdn.thenewstack.io/media/2025/12/e2cc7f31-gemini4.jpg)

**图 4：** 我们的示例下拉菜单已成功创建。

好的，但我们如何从中学习呢？如果你回到你的 JS\_PROJECT 目录，你会看到三个文件：

```
index.html script.js style.css
```

或者，你可以像这样运行一个后续查询：

```
Explain to me what you did to create the dropdowns.
```

Gemini CLI 会详细解释它所做的一切（**图 5**）；否则，它会通知你已用完免费套餐的资源或服务过于繁忙。如果是这种情况，请再次运行查询，看看是否有效。

[![](https://cdn.thenewstack.io/media/2025/12/03c84e71-gemini5.jpg)](https://cdn.thenewstack.io/media/2025/12/03c84e71-gemini5.jpg)

**图 5：** 让 Gemini CLI 向你解释它是如何创建下拉菜单的。

很有趣。

我的朋友们，这就是如何安装和使用 Gemini CLI 工具来学习新知识或提升当前技能的方法。