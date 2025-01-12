# 开始使用CodeGate，LLM开发人员的中间件

![Featued image for: Getting Started With CodeGate, an Intermediary for LLM Devs](https://cdn.thenewstack.io/media/2025/01/f814f7a3-kent-tupas-u7scebzs57q-unsplashb-1024x576.jpg)

我认为充当远程LLM和最终用户之间的中间件本身就是一个强大的想法，这就是为什么我认为[查看CodeGate](https://thenewstack.io/codegate-open-source-tool-secures-ai-coding-assistants/)无论您当前的AI编码计划如何，都将很有价值。[CodeGate](https://codegate.ai/)是一个安全解决方案，根据其主页，“它会加密提示中的密钥以保护您的隐私，并使用最新的风险洞察来增强LLM的知识库以保护您的代码”。

您可以从人们查询的内容和方式中明显看出很多信息——这就是为什么谷歌总是会成功。开发人员可以从他们的“输出”中泄露大量信息，其中包括他们的公共查询。这并不意味着有人正在积极查看这些信息，但养成过滤输出的习惯是明智的。

许多事情对组织来说可能是敏感的，例如内部供应商的名称、内部项目名称以及密钥和密码等显而易见的事情。并非所有这些都一定对开发团队显而易见。

## 本地防御

[CodeGate](https://codegate.ai/)是一个开源框架，它提供了一个“本地提示网关”，并且随着时间的推移，它将显然拥有更多内容和策略选项——可以把它想象成一个刚刚开始的在线服务游戏。

来自[https://docs.codegate.ai/#what-is-codegate](https://docs.codegate.ai/#what-is-codegate)

因此，这并非一个现成且完整的解决方案。我想象CodeGate最终会位于团队的前面，而不是单个计算机（就目前而言）。CodeGate目前寻找的两个操作是：远程LLM代码示例中不安全的包建议，以及通过AI助手暴露内部信息。我将在本文后面查看第二个示例。

## 设置

我将遵循[示例](https://docs.codegate.ai/quickstart)，该示例使用GitHub Copilot和Visual Studio。您可以通过[Continue](https://www.continue.dev/)使用其他几种组合，所有这些配置都将随着时间的推移和社区的使用而完善。在我们深入研究之前，以下是我们将要做的工作，以便您可以检查它是否在您的开发舒适区内：

- GitHub Copilot。您需要一个GitHub帐户才能使用Copilot。
- Visual Studio Code。作为[GitHub Copilot在Visual Studio Code中是免费的](https://code.visualstudio.com/docs/copilot/overview)(VS Code)，这个示例路径很好，即使现在有很多IDE + AI组合。（我想看看Zed AI和CodeGate）。我假设您知道如何在系统上调用命令面板。
- Docker：我们将本地在Docker上托管CodeGate，这意味着将提示发送到Docker，Codegate将增强的代码发送到（在本例中）Copilot。
- 证书：鉴于这是一个安全解决方案，我们希望确保我们正在与之通信的对象。

## 开始

我在我的MacBook M4上进行此操作。首先，让我们确保我们有一个准备好Copilot的VS Code。

我将在一个空项目中启动一个VS Code：

然后我将安装GitHub Copilot扩展并登录：

然后确保Docker Desktop正在运行。

现在我们将使用CodeGate的签名安装行：

```bash
docker run --name codegate -d -p 8989:8989 -p 9090:9090 -p 8990:8990 --mount type=volume,src=codegate-volume,dst=/app/codegate_volume --restart unless-stopped ghcr.io/stacklok/codegate:latest
```

这有点冗长。这将从注册表中提取最新的CodeGate镜像并在后台启动它。有一些端口转发。然后脚本启动一个卷用于持久数据存储。

现在我们需要添加一个证书。为什么我们需要这个？由于我们故意将CodeGate设置为[“中间人”](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)，我们最好确保我们确实正在与正确的人交谈。通过端口转发，Docker容器已将您的本地网站提供在[http://localhost:9090](http://localhost:9090)上，因此请转到那里下载您的证书。

然后我按照Mac的说明通过MacBook的UI将证书添加到我的链中：

打开钥匙串访问中登录钥匙串中新添加的证书，并确保两个条目“SSL”和“X.509”都为“始终信任”：

它现在应该像这样出现在证书列表中：

是的，当然您可以使用以下命令从终端添加它：

```bash
security add-trusted-cert -r trustRoot -k ~/Library/Keychains/login.keychain ~/Downloads/codegate.crt
```

好的，现在我们只需要通知VS Code与我们的中间件通信。使用命令面板，打开**“首选项：打开用户设置(JSON)”**。
添加以下设置：

```json
{
  // ... other settings ...
  "codegate.endpoint": "http://localhost:8989",
  "codegate.cert": "/path/to/your/codegate.crt"
}
```

"http.proxy": "https://localhost:8990", "http.proxyStrictSSL": true, "http.proxySupport": "on", "http.systemCertificates": true, "github.copilot.advanced": { "debug.useNodeFetcher": true, "debug.useElectronFetcher": true, "debug.testOverrideProxyUrl": "https://localhost:8990", "debug.overrideProxyUrl": "https://localhost:8990" }

由于我们刚刚重新设计了底层的代理管道，您需要重新启动 VS Code。

现在让我们使用 Codegate 的仓库示例。让我们将它们克隆到我们的项目文件夹中：

这些是用 Python 编写的，而我使用的是 C#，但这现在无关紧要。

如果我们查看 `conf.ini` 文件，您可以看到其中包含密钥和机密。

现在，如果我们打开了 Copilot 窗口，它已经加载了 `conf.ini` 用于上下文，我们可以天真地准备询问有关此文件的问题。开发人员只是向 LLM 询问键值对的含义，可能是因为他们一段时间没有使用 AWS 了。

问题是，当向 GPT-4 提问我们为什么使用它时，您不希望将您的私钥直接发送给 Sam Altman。如果它们最终成为训练数据，那将是令人尴尬的。

因此，虽然 CoPilot 看起来按预期回答了这个问题，但如果您仔细观察，您可以看到 CodeGate 干预时留下的注释：

如果我们转到 CodeGate 面板，我们可以看到实际发生了什么。

（事实上，CodeGate 在这里的时间安排有点不清楚，而且也没有完全正确地引用。由于时间以分钟为单位，我不太确定顺序。触发标题也不一致——您可能已经注意到了这些。从技术上讲，它应该屏蔽所有三行。）

首先，CodeGate 检测到其中一个密钥是 `AWS_ACCESS_KEY_ID`，屏蔽原始值并用加密值代替：

然后，当它从 Copilot 返回数据时，它会解密密钥：

显然，为了彻底检查这一点，我们需要运行我们自己的 LLM 并查看收到的内容。

虽然触发器的日志记录标签不太准确（在您阅读本文时可能会修复——如果没有，请在他们的 Discord 上询问他们），但操作周期正在运行。我认为这只是此 CodeGate 版本的当前输出。

## 结论

当 LLM 提供商必须做出决定时，将会出现一个有趣的时刻。标准的生态系统策略意味着（即使是匿名地），了解最终用户正在做什么会增加提供商平台的价值——问问亚马逊就知道了。当用户告诉 LLM 提供商的内容被隐藏时，不可避免地，平台的价值会略微降低。因此，提供商要么会为用户提供他们自己的中间件版本，要么会转向压制它。

所以现在是时候提高您对中间件可以为您和您的安全做什么的理解了。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以串流收听我们所有的播客、访谈、演示等等。