# 将 ChatGPT 用于 DevOps

在 ChatGPT 惊天动地地首次亮相时，我已经在 DevOps 和 SRE 领域工作了大约 5 年，它真正彻底改变了我的工作流程，但我稍后会深入探讨。

与我们中的许多人一样，我听说过 ChatGPT 能够从头开始编写完整应用程序的传闻，并且认为“它不可能真的那么好”决定亲自测试一下。

最初，我开始要求它用 Python 和 Bash 生成小脚本，只是为了让我的脚趾涉足 OpenAI/ChatGPT 水域。

![Leveraging OpenAI’s ChatGPT for Automation Scripting](/images/using-chatgpt-for-devops/p1.png)
*ChatGPT 编写了一个自动化的 Python 脚本来对 VM 执行内存检查。*

结果让我大吃一惊！ 🤯 它不仅生成了语法完美的代码，而且还向我解释了代码！

当时，我一直致力于通过 Terraform 使用 Helm 将 Airflow 部署到 EKS 集群，这个设置花了我大约 3-5 天的时间来整理和测试，所以我要求 ChatGPT 为此编写配置。

虽然它确实产生了良好的配置，但这并不是我一直在寻找或希望的，相反，我问了 OpenAI 的兄弟，Platform Playground 同样的问题。

![](/images/using-chatgpt-for-devops/p2.png)
*OpenAI 的 Platform Playground 工具生成的通过 Helm 为 Apache Airflow 部署的 Terraform 代码。*

OpenAI Platform Playground 工具改变了游戏规则！它生成的代码似乎可以访问互联网，而 ChatGPT 没有，因此可以提供更全面的配置。此处看到的由 Playground 工具输出的配置与我几天前手动配置的配置几乎相同，我花了几天时间，这个 AI 花了几秒钟。从这里开始，我开始将其纳入我的常规工作流程。

我试着向 ChatGPT 询问我当时正在处理的指标设置的具体基础设施设计和配置选项。 ChatGPT 能够在几秒钟内给出答案，完美地回答了我的问题，并就最佳实践提出了建议，而阅读 Thanos 文档和不同在线资源的时间无法给出明确的前进方向。

![](/images/using-chatgpt-for-devops/p3.png)
*向 ChatGPT 询问技术基础架构设计问题。*

在使用这两种工具简单地生成代码并回答基本问题几周后，我开始在我从事的另一个项目中遇到问题，所以我求助于 ChatGPT，看看它是否能为我提供答案：

![](/images/using-chatgpt-for-devops/p4.png)
*ChatGPT 提供有关如何对错误进行故障排除和分类的详细信息。*

虽然 ChatGPT 没有提供太多关于如何排除或解决我已经尝试过或在网上发现的错误的新信息，但它始终可以帮助提醒您检查可能遗漏或遗忘的内容。我敢肯定，对于不同的错误，它可能会给出更详细的响应，甚至可能会为给定的错误提供特定的解决方案。这为许多人打开了大门，尤其是更多的初级工程师，可以通过 ChatGPT 磨练他们的故障排除和分类技能。它还可能改变我们调查各种问题的整个流程，不仅是在 CI/CD 和基础设施中，甚至是调试代码。

这两个工具的结合，ChatGPT 和 OpenAI Playground，真正让我改进和优化了我的工作流程。在过去的两个月里，当我根本无法在 Google 上找到我需要的东西或只需要快速回答一个问题时，帮助我解除封锁。

## 充分利用 ChatGPT 进行 DevOps 的提示和技巧

* **指定版本**：如果您希望 ChatGPT 基于可能有多个版本的 Helm Chart（例如）生成配置，我发现默认情况下它并不总是采用最新版本。在请求中包含所需的配置版本可能有助于获得更准确的结果。
* **信任但验证**：正如引用所说的“信任但验证”，您可以相信 ChatGPT 给您的输出是好的并且没有错误，但是对于在线获得的任何代码，您应该始终自己通读并确保您在将其添加到您的项目之前了解它。永远不要假设 ChatGPT 生成的代码是可以开箱即用的，无论多么惊人或优秀。
* 如果 ChatGPT 没有给出您想要的响应，您也可以尝试使用 [**OpenAI 的 Playground**](https://platform.openai.com/playground)。重要的是要补充一点，这个产品线有免费试用，但试用结束后就变成付费的了。
* **举个例子**：当询问 ChatGPT 某事时，提供更多信息会很有帮助，这也可以通过举个例子的形式来完成。您可以说 regex to find an ip address in a string, for example, in a string 1.1.1.1:0000 the regex should match 1.1.1.1 ，而不是仅仅询问可能会产生的 regex to find an ip address in a string ，它可能会为您的查询生成更准确的响应。

![](/images/using-chatgpt-for-devops/p5.png)

最终，在当前版本的 ChatGPT 中，我认为 DevOps 工程师或 SRE 不会很快被取代。然而，ChatGPT 为工程师提供了大量的方法和机会来提高他们的生产力，并帮助他们以以前可能需要数天或多人协助的方式解除阻碍。

谢谢阅读 ：）。