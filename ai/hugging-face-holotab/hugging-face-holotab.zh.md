大多数 AI 系统通过结构化路径（如 API、代码库或定义严密的工具集成）与软件交互。当系统是为自动化设计时，这种方案很有效，但人们日常依赖的大多数软件并非如此。内部仪表板、旧版工具和 Web 应用通常需要手动导航，AI 无法以干净的方式接入。

这种局限性正在激发人们对另一种方法的兴趣：让模型通过界面本身操作软件。模型不再是调用函数，而是像人类一样点击、打字并在应用程序中移动。这种方法通常被称为“计算机使用”（computer use），它建立在机器人流程自动化（[RPA](https://thenewstack.io/true-success-in-process-automation-requires-microservices/)）长期使用的理念之上，但现在是由模型负责决策，而非固定的脚本。

Hugging Face 是最新测试这一转变的公司，推出了 [HoloTab](https://chromewebstore.google.com/detail/holotab/hlaoiikljjgcjdhkakedfngifaopbcop?pli=1)，这是一款旨在直接在浏览器中运行智能体的 Chrome 扩展程序。该工具可以导航网站、执行动作并重复任务，而无需依赖特定站点的集成。

[周三宣布](https://huggingface.co/blog/Hcompany/holotab)的 HoloTab 基于 Hugging Face 最近发布的 [Holo3-35B-A3B](https://huggingface.co/Hcompany/Holo3-35B-A3B) 模型构建。该公司称该模型凭其在 [OSWorld-Verified](https://os-world.github.io/) 基准测试中的表现“突破了计算机使用领域的边界”。该基准测试是针对多步骤软件交互任务的公开测试。

> “HoloTab 是一款 Chrome 扩展程序，能像人类一样在网页上导航。” —— Hugging Face

## 无需集成的智能体

大多智能体系统依赖预定义的连接。模型可能会查询数据库、触发 API 或生成要在其他地方执行的代码。这些方法依赖于可预测的输入和输出，虽然更易管理，但限制了应用范围。

“计算机使用”采用了不同的路线。它不等待软件开放功能，而是直接利用屏幕上可用的任何内容。这包括点击菜单、填写表单以及在标签页或应用程序之间移动。

Anthropic 最近的发展也指向了类似方向。其 Claude Code 系统已[扩展到可以在用户的机器上操作](https://thenewstack.io/claude-computer-use/)，控制鼠标和键盘输入，并跨文件和应用程序执行任务。该公司还推出了允许这些会话[持久化并被远程访问](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/)的功能，这是向能够持续工作超过单次交互的长期运行智能体迈出的更广泛举措的一部分。

例如，开发者可能会要求 Claude 在模拟器中运行移动应用，操作没有命令行访问权限的桌面工具，或者执行仅存在于图形界面后的任务，系统在机器上直接处理这些交互，而开发者在任务运行时进行远程检查。

Anthropic 实际上早在 [2024 年就引入了计算机使用](https://www.anthropic.com/news/3-5-models-and-computer-use)作为其 Claude 3.5 更新的一部分，重点是让开发者能够访问可以解释屏幕并通过控制循环采取行动的模型。早期的版本需要更多配置，且很大程度上局限于基于 API 的实验。其最近的努力将其转向更多产品化设置，通过桌面应用和远程检查任务的能力，使同样的基础能力在日常工作中更易使用。

值得一提的是，HoloTab 采取了不同的方式，它在浏览器内部运行而非整个桌面，但它建立在相同的理念之上。它不需要集成，而是直接针对实时网站工作，允许用户移交任务，如查看和回复消息、填写表单，甚至在网上搜索人员并在 LinkedIn 等平台上发起联系。

![使用计算机进行专业社交](https://cdn.thenewstack.io/media/2026/04/5f3d8bca-gif1.gif)

***使用计算机进行专业社交***

## 计算机使用走向成熟？

随着 Hugging Face 进一步推进基于浏览器的智能体，Anthropic 继续扩展其桌面级能力，以及 Google 在其 [Gemini 家族中引入计算机使用模型](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)，显而易见的是，AI 系统正被设计为直接操作软件，而不依赖于集成。

许多业务流程涉及将多个无法顺畅沟通的工具拼接在一起。如果智能体可以直接操作这些工具，就能在不重建底层系统的情况下，实现更广泛任务的自动化。

这种方法与标准化 AI 如何连接软件的独立努力并存。例如，Anthropic 的[模型上下文协议](https://thenewstack.io/model-context-protocol-roadmap-2026/) (MCP) 旨在通过定义的接口为模型提供对工具的结构化访问。在 MCP 依赖于服务开放这些接口的地方，“计算机使用”通过直接针对 UI 工作彻底规避了这一要求。这两种方法反映了不同的赌注：一种是让软件适应 AI，另一种是让 AI 适应现有软件。

对于 Hugging Face 而言，HoloTab 是后一种方法的试验场，展示了其 Holo3 模型如何被用于导航实时网站并在无需集成的情况下执行任务。