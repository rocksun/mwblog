在正式发布六个月后，谷歌正推动 [Antigravity](https://antigravity.google/) 超越其作为编程环境的初衷。该公司将其重新定位为开发和管理[自主 AI 智能体](https://thenewstack.io/why-apis-are-the-missing-link-for-truly-autonomous-ai-agents/)团队的平台，并推出全新的桌面应用、[CLI](https://thenewstack.io/user-interfaces-in-agentic-cli-tools-what-developers-need/)、[SDK](https://thenewstack.io/openai-agents-sdk-sandboxes/) 以及[企业云集成](https://thenewstack.io/cloud-native/)来支持这一扩展。

“我们正在将 Antigravity 的功能从编程环境扩展，并将其转化为一个开发和管理自主 AI 智能体团队的平台，”Google DeepMind 首席技术官兼谷歌首席 AI 架构师 [Koray Kavukcuoglu](https://www.linkedin.com/in/koray-kavukcuoglu-0439a720/) 在本周 [Google I/O 2026](https://io.google/2026/) 前夕的新闻简报会上表示。该公司称已有数百万开发者正在使用该平台进行构建。

> “我们正在将 Antigravity 的功能从编程环境扩展，并将其转化为一个开发和管理自主 AI 智能体团队的平台。”

“Google Antigravity 是我们以智能体为中心的开发平台，旨在让开发者将想法转化为生产就绪的应用，”Google DeepMind 软件工程总监 [Varun Mohan](https://www.linkedin.com/in/varunkmohan/) 和 Google DeepMind 技术人员 [Logan Kilpatrick](https://www.linkedin.com/in/logankilpatrick/) 在[博客文章](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/)中写道。“今天，我们正在扩展 Antigravity 生态系统，以管理和部署可跨核心开发界面集成的智能体。”

## 平台的三种新形态

此次发布的核心是 Antigravity 2.0，这是一个独立的桌面应用程序，作为智能体编排的中心枢纽。开发者不再是让单个智能体执行单一任务，而是可以协调多个智能体同时工作——一个生成代码，另一个制作品牌资产，第三个处理产品架构规划。

对于更喜欢留在终端的开发者，谷歌推出了 Antigravity CLI，这是一个轻量级界面，用于在没有图形环境的情况下启动智能体。现有的 Gemini CLI 用户被鼓励进行迁移。

为了完善这一扩展，Antigravity SDK 为开发者提供了对驱动谷歌内部产品的同款智能体框架的编程访问权限。该 SDK 针对 Gemini 模型进行了协同优化，特别是 Gemini 3.5 Flash，谷歌称该模型是与 Antigravity 2.0 共同开发的，作为平台的主要主力模型。谷歌表示，它在几乎所有基准测试中都优于 Gemini 3.1 Pro，运行速度比竞争对手的尖端模型快四倍。

Gemini API 中的托管智能体将平台扩展到了云端。现在，只需一次 API 调用即可启动一个完整的智能体，它可以在持久、隔离的 [Linux](https://thenewstack.io/introduction-to-linux-operating-system) 环境中进行推理、使用工具并执行代码。状态和文件在后续调用中保持持久化，从而实现无需重新初始化的多轮会话。

企业层面通过 Antigravity 与 Gemini Enterprise Agent Platform 的集成得到解决，使 Google Cloud 客户能够直接连接到他们的云项目。该公司表示，全新的[每月 100 美元的 Google AI Ultra 订阅层级](https://thenewstack.io/google-ai-ultra-pricing/)在 Antigravity 中提供的用量限制是现有 Pro 计划的 5 倍。

![](https://cdn.thenewstack.io/media/2026/05/f1f7885d-52bde528-8ce8-4a0b-b219-9861b032b6a5-1024x768.jpg)

图片来源：*The New Stack*

早期企业采用者在发布中提供了验证。AirAsia Next 首席技术官 [Nikunj Shanti](https://app.aviation-festival.com/event/aviation-festival-asia-2025/person/RXZlbnRQZW9wbGVfMzYyODczNjQ=) 表示，公司目前有一半以上的生产就绪代码是通过 Antigravity 智能体工作流生成的。

德勤（Deloitte）美国 AI 与工程战略及服务负责人 [Faruk Muratovic](https://www.linkedin.com/in/farukmuratovic/) 提到，该平台能够运行符合德勤企业安全标准的受控自主工程工作流。普华永道（PwC）咨询首席技术官 [Vikas Agarwal](https://www.linkedin.com/in/vikas-agarwal-b5528a2/) 将这一转变描述为“从简单的 AI 代码补全迈向真正的智能体编排”。

“WPP 已将 Antigravity 集成到我们的智能体营销平台 WPP Open 中，以补充我们的产品开发生命周期，”WPP 工程负责人 [Callum Anderson](Callum%20Anderson) 在一份声明中表示。“利用 Gemini 的力量，它简化了工作流程，自动化了重复性任务，并使工程团队能够更快地为我们的客户提供高质量的解决方案。”

与此同时，另一项关键公告解决了一个谷歌自身参与产生的问题——随着智能体编写的代码越来越多，这些代码需要以与生成速度和规模同步的方式进行安全防护。

谷歌为其 [CodeMender](https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/) 增加了新功能——这是一个由 Google DeepMind 开发的 [AI 代码安全智能体](https://thenewstack.io/ai-security-agents-combat-ai-generated-code-risks/)，它不仅能发现漏洞，还能实际修复它们。

“CodeMender 是一个 AI 代码安全智能体，最初由 Google DeepMind 开发。利用智能体平台能力和先进的 Gemini 模型，CodeMender 可以自动识别代码中的漏洞，”Google Cloud 首席执行官 [Thomas Kurian](https://www.linkedin.com/in/thomas-kurian-469b6219/) 在一篇[博客文章](https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud)中写道。

“随后它会推荐精确的修复方案，对其进行安全测试，并可以在经您批准后，跨依赖系统应用补丁和必要的更改。这整个过程实现了安全部署的自动化，同时确保您的开发者保留控制权。”

利用 Gemini 模型的高级推理能力，它能够自主识别关键的代码缺陷，推荐精确的修复方案，在安全环境中进行测试，并跨依赖系统应用补丁——每一步都需要开发者的批准。

> “它展示了 AI 如何实际修复代码，而不仅仅是发现漏洞。”

“它展示了 AI 如何实际修复代码，而不仅仅是发现漏洞，”Kavukcuoglu 说道。

CodeMender 正作为 AI 威胁防御产品的一部分集成到谷歌的智能体平台中。目前正邀请选定的安全专家组测试 CodeMender API，随后将向更广泛的范围开放。

该工具使谷歌进入了一个初创公司活动频繁的市场细分领域。自主漏洞修复——而非探测，是修复——已成为企业安全领域竞争最激烈的空间之一，[Aikido Security](https://thenewstack.io/aikido-self-securing-software/) 和 [Mobb](https://thenewstack.io/ai-coding-tools-create-more-bugs-than-they-fix/) 等参与者已经提供了 AI 驱动修复模型的各种版本。CodeMender 是 Google DeepMind 进入该领域的切入点，依托 Gemini 的推理能力以及与智能体平台基础设施的原生集成。

谷歌今天还在智能体平台上推出了 AI 内容检测 API，使企业能够识别来自谷歌和第三方模型的 AI 生成内容——这表明合成媒体治理正与代码安全一样，成为平台层面的关注点。

## 它的意义

总而言之，Antigravity 的扩展和 CodeMender 的新闻代表了谷歌迄今为止对开发者基础设施发展方向最清晰的表态：摆脱单轮提示词，转向持久、协作、全天候运行的智能体系统。

“从单轮提示词到协作式、全天候运行的智能体的跨越，改变了开发者构建软件的方式，”Kavukcuoglu 表示。

该公司正在同步构建让智能体大规模编写代码的工具，以及管理这些智能体产出内容的安全基础设施。这是为企业量身定制的智能体化开发与智能体化修复的组合。