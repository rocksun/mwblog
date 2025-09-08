
<!--
title: 局域网内连接本地 Ollama AI 实例
cover: https://cdn.thenewstack.io/media/2025/09/a6aefacd-a-c-_0a1prorvoo-unsplash-ollama.jpg
summary: 本文介绍了如何在服务器上安装和配置 Ollama，并通过终端或 GUI (Msty) 从远程连接到 Ollama 实例。这样可以避免本地资源消耗，提高运行速度和可靠性。
-->

本文介绍了如何在服务器上安装和配置 Ollama，并通过终端或 GUI (Msty) 从远程连接到 Ollama 实例。这样可以避免本地资源消耗，提高运行速度和可靠性。

> 译自：[Connect to a Local Ollama AI Instance From Within Your LAN](https://thenewstack.io/connect-to-a-local-ollama-ai-instance-from-within-your-lan/)
> 
> 作者：Jack Wallen

我非常喜欢使用本地安装的 [Ollama AI](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) 实例，这个工具可以在你自己的电脑上运行大型语言模型（LLM）。部分原因是当通过标准方法使用AI时，它会[消耗大量能源](https://thenewstack.io/ai-consumes-lots-of-energy-can-it-ever-be-sustainable/)。

有一段时间，我一直在我的台式机上使用 [Ollama](https://ollama.com/)，但我发现有一些原因导致这种方式并不理想。首先，Ollama 消耗了太多的资源，导致我的台式机速度变慢。其次，我只能在我的台式机上使用 Ollama —— 除非我想 [SSH 进入我的台式机](https://thenewstack.io/linux-ssh-and-key-based-authentication/) 并从那里启动 AI。

然后，我发现了一种更好的方法：我可以将 Ollama 安装在服务器上，然后从我网络上的任何机器连接到它。

我想向你展示两种不同的方法来实现这一点，一种是从命令行，另一种是通过图形用户界面（GUI）。这比你想象的要容易得多，只需要在服务器端进行最少的配置。

话不多说，让我们开始吧。

## 安装 Ollama

你必须做的第一件事是在服务器上安装 Ollama。我建议为此部署一个 Ubuntu Server 实例，因为我在 Ubuntu 上运行 Ollama 的体验非常好。

也就是说，登录到你的 Ubuntu Server 实例并运行以下命令来安装 Ollama：

```
curl -fsSL https://ollama.com/install.sh | sh
```

安装完成后，Ollama 就已成功安装。然后，你可以使用如下命令将 LLM 拉取到你的本地机器：

```
ollama pull llama3.2
```

或者，如果你想要 gpt-oss 模型：

```
ollama pull gpt-oss
```

完成上述操作后，你就可以配置 Ollama 以接受远程连接了。

## 配置 Ollama 以进行远程连接

使用以下命令打开 Ollama systemd 配置文件：

```
sudo nano /etc/systemd/system/ollama.service
```

在 [service] 部分下，添加以下内容：

```
Environment="OLLAMA_HOST=0.0.0.0"
```

保存并关闭文件。

上面的行将 Ollama 开放给来自任何位置的连接。请记住，你需要确保你的局域网是安全的；否则，一些不良行为者可能会潜入你的局域网并使用 Ollama 做一些事情。

如果你希望能够从局域网外部访问你的 Ollama 实例，你需要配置你的路由器，将端口 11434 上的传入流量定向到托管服务器。

使用以下命令重新加载 systemctl 守护程序：

```
sudo systemctl daemon-reload
```

使用以下命令重启 Ollama：

```
sudo systemctl restart ollama
```

你现在可以从你的局域网连接了。

## 通过终端连接

在你想要连接到 Ollama 服务器的本地机器上打开一个终端窗口。在该机器上，输入以下命令：

```
OLLAMA_HOST=IP_ADDERES ollama run llama3.2:latest
```

其中 IP\_ADDRESS 是 Ollama 服务器的 IP 地址。

你应该会看到 Ollama 文本提示符，你可以在其中开始运行你自己的查询。完成后，使用以下命令退出 Ollama 提示符：

```
/bye
```

这将不仅结束你的 Ollama 会话，还会结束远程连接。

## 通过 GUI 连接到你的远程 Ollama 实例

我们现在将通过 GUI 连接到我们的远程 Ollama 实例。这里使用的 GUI 是 Msty，因为它使这项操作变得非常容易。你应该可以通过官方 GUI 连接到远程 Ollama 实例，但我尚未成功实现这一点。

相反，我们将使用 Msty，它无论如何都是一个更出色的 GUI。Msty 具有大量功能，可以在所有三个主要平台（Linux、macOS 和 Windows）上运行，并且可以免费使用。

如果你尚未安装 Msty，请前往 [官方网站](https://msty.ai) 并下载适用于你操作系统的版本。安装 Msty 相当简单，因此你不应该遇到任何问题。

安装 Msty 后，打开 GUI 应用程序。从主窗口中，单击左侧边栏中的 Remote Model Providers 图标，然后单击 Add Remote Model Provider。在出现的窗口（图 1）中，按如下方式填写信息：

* Provider：从下拉列表中选择 Ollama Remote。
* 给远程模型起一个容易记住的名字。
* 以 http://SERVER\_IP:PORT 的形式输入服务器端点，其中 SERVER\_IP 是 Ollama 托管服务器的 IP 地址，PORT 是你配置的端口（默认为 11434）。

[![Screenshot](https://cdn.thenewstack.io/media/2025/09/7ad7facf-ollamaremote.png)](https://cdn.thenewstack.io/media/2025/09/7ad7facf-ollamaremote.png) 图 1：配置远程 Ollama 服务器非常简单。

出现提示时，单击 Fetch Models，从 Model 下拉列表中选择你想要的模型，然后单击 Add。

## 将远程实例与 Msty 结合使用

回到 Msty 主窗口，开始一个新的聊天。从 Model 下拉列表中（图 2），你现在应该会看到一个 Remote 部分，其中包含你添加的模型。

[![Screenshot](https://cdn.thenewstack.io/media/2025/09/20f5b4df-ollamamenu.png)](https://cdn.thenewstack.io/media/2025/09/20f5b4df-ollamamenu.png) 图 2：选择新添加的远程 Ollama 实例。

选择该条目并键入你的查询。这一次，查询将由 Ollama 的远程实例回答。因为你在服务器上运行 Ollama，所以你的查询响应应该比直接从你的桌面运行它们时更快。

我现在已经开始严格使用这种类型的设置来使用 Ollama，以避免我的台式 PC 上的 CPU/RAM 瓶颈。我发现远程使用 Ollama 更快、更可靠。