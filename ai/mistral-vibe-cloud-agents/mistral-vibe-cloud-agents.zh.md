无数公司正在利用 AI 热潮牟利，构建从[编程助手](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/)到客户服务机器人的各种应用。但只有少数几家公司在构建基础 AI 模型本身——即驱动这一切的底层系统。

这个群体主要由 OpenAI、Anthropic 和 Google 占据，而像 [Mistral AI](https://mistral.ai/) 这样的公司则处于这个精英圈层之外。Mistral 于 2023 年在巴黎成立，已从包括 [Microsoft](https://techcrunch.com/2024/02/27/microsoft-made-a-16-million-investment-in-mistral-ai/) 和 [Nvidia](https://mistral.ai/news/mistral-ai-and-nvidia-partner-to-accelerate-open-frontier-models) 在内的知名投资者手中筹集了数十亿美元，同时一直推动更加开放的方法——发布开源权重模型，并让开发者对如何运行这些模型拥有更多控制权。

> 周三，Mistral 推出了新模型 Mistral Medium 3.5，以及一个允许其编程智能体在云端运行的系统。

现在，该公司正在向其一些更大对手的领地进军。周三，Mistral [首次展示](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5)了新模型 [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04)，以及一个允许其编程智能体在云端运行的系统，在那里它们可以在后台继续工作，而开发者则可以去处理其他事情。

此外，Mistral 正在为其类似 ChatGPT 的界面 [Le Chat](https://chat.mistral.ai/chat) 添加“工作模式”，该模式可以通过并行调用工具来承担更长的工作，因为它希望超越聊天，进入处理实际工作的领域。

## 传送至云端

Mistral 的编程助手 [Vibe](https://mistral.ai/products/vibe)（支持[氛围编程](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5)）到目前为止主要存在于终端中，开发者可以在命令行中要求它读取仓库、编辑文件、运行命令、修复错误或编写测试。通过这次更新，Mistral 正在将其推向一种不同的模式——你可以在云端启动多个智能体，让它们在隔离的沙盒环境中独立完成任务，然后再回来查看它们的成果。

会话可以从 CLI 或 Le Chat 本地启动，并在任务中途“传送”到云端，同时保留完整的上下文——包括任务本身、之前的步骤以及到目前为止所做的任何更改。从那里开始，智能体将远程继续运行，而不会被束缚在开发者的机器上。

![传送至云端](https://cdn.thenewstack.io/media/2026/05/0036b09b-teleport.gif)

*传送至云端*

因此，开发者不再需要坐在那里循环提示和检查结果，而是可以将大块工作移交出去，并允许它们在后台运行。这些任务可能包括编写新功能、更新代码，或准备更改作为草稿拉取请求（pull requests）供以后审查。

用户还可以直接从 Le Chat 启动 Vibe。例如，他们可以要求它构建一个销售仪表板，它将在远程设置中运行任务，然后返回完成的分支或草稿拉取请求。

![从 Le Chat 启动 Vibe](https://cdn.thenewstack.io/media/2026/05/ea4865c7-launchvibefromlechat.gif)

***从 Le Chat 启动 Vibe***

最重要的是，Mistral 在 Le Chat 中添加了“工作模式”，用户可以设置更广泛的任务——例如整理会议简报或更新文档——并让系统使用连接的工具来完成这些任务。

![工作模式](https://cdn.thenewstack.io/media/2026/05/d21a7658-workmodegif.gif)

*工作模式*

在 Mistral 产品团队工作的 [Pini Wietchner](https://www.linkedin.com/in/pini-wietchner-45224513a/) 在一次[在线讨论](https://www.youtube.com/watch?v=KaMbzM9dsTc)中表示，公司一直在内部对其最新的发布进行 Vibe 的“吃螃蟹”（dogfooding）测试，其大部分拉取请求都是远程处理的。

“我们在内部看到 Vibe 非常有效，”Wietchner 在那段公司制作的 YouTube 视频中说道。“我们的客户希望在本地和远程都能使用智能体。本地智能体非常适合在 IDE 或终端处理编程任务的开发者。远程智能体则允许他们使用我们的沙盒设置，以安全的方式并行运行多个智能体。”

> “我们的客户希望在本地和远程都能使用智能体。本地智能体非常适合在 IDE 或终端处理编程任务的开发者。远程智能体则允许他们并行运行多个智能体。”

## 模型表现

支撑这一切的是 Mistral Medium 3.5，这是一个拥有 128B 参数和 256k 上下文窗口的模型，旨在处理更长、更复杂的任务，而不是快速提示。

Mistral 将 Medium 3.5 与已用于类似工作负载的模型进行对比——包括 Claude Sonnet、Kimi K2.5、GLM 5.1 和 Qwen 3.5，如其报告的结果所示。在衡量模型解决真实 GitHub 问题能力的 SWE-bench Verified 等标准测试中，该公司报告了具有竞争力的分数，以及在电信、零售和银行等特定领域任务中的结果。这些数据来自 Mistral 自己的评估，在不同的设置或条件下可能会有所不同。

![智能体基准测试对比竞争模型](https://cdn.thenewstack.io/media/2026/05/8f19cc18-frame-2147228534-1024x750.png)

*智能体基准测试对比竞争模型*

对于那些全身心投入 Mistral 技术栈的人来说，一个更相关的比较或许是与其早期的模型进行对比。根据该公司报告的 Swe-Bench Verified 结果，以此衡量，Medium 3.5 比之前的编程专注版本（如 [Devstral 2](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512)）有了显著提升。

![智能体基准测试对比之前的 Mistral 模型](https://cdn.thenewstack.io/media/2026/05/ef08fa34-frame-2147228532-1024x607.png)

*智能体基准测试对比之前的 Mistral 模型*

## 构建拼图

Mistral 自成立以来几乎一直在为此而努力。2024 年，该公司发布了 [Codestral](https://huggingface.co/mistralai/Codestral-22B-v0.1)，这是其[首个专用编程模型](https://mistral.ai/news/codestral)，专注于代码补全和生成等日常开发者任务。最近，它又推出了 [Leanstral](https://thenewstack.io/leanstral-formal-verification-code/)，解决了更难的问题——使用形式验证来检查代码是否真正正确。

因此，Mistral 并没有直接跳向完全自主的智能体，而是一直在构建这些拼图：可以编写代码的模型、可以检查代码的模型，以及现在尝试在后台运行这些工作的系统。

这也是该公司开始与更大的竞争对手产生更直接交集的地方。例如，Anthropic 一直在通过 Claude Code 推动类似的想法，包括允许开发者运行更长的编程任务并在不同会话中保持任务进行的工具，无论是在[浏览器、移动设备](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/)上，还是通过[远程访问本地环境](https://code.claude.com/docs/en/remote-control)。

Mistral 的不同之处在于它如何包装这些想法。它的模型通常以开源权重发布，现在像 Vibe 这样的工具可以在本地或云端运行，让开发者对它们的使用拥有更多控制权。

这并不能保证它会胜出——远非如此。但它确实给 Mistral 带来了一些独特的视角——尤其是在欧洲，Mistral 将自己定位为替代主导市场的美国实验室的本土选择。

然而，似乎各方达成一致的是，人们越来越渴望将 AI 从一种必须不断引导的东西，转变为一种能够独立处理大块工作的工具。