<!--
title: Cursor 20亿美元豪赌：IDE地位巨变，从默认走向备用
cover: https://cdn.thenewstack.io/media/2026/04/a0f52b0f-puzzle-creative-x0nz565wjq-unsplash-scaled.jpg
summary: Cursor 3将AI代码编辑器转变为代理管理控制台，使传统IDE退居次要地位。此举反映了AI辅助开发领域中代理编排日益重要的结构性转变。此番调整改变了模型选择、削弱了VS Code等传统IDE的优势，并重塑了工程师的工作流程，使之更像系统操作员，而非单纯的代码编写者。
-->

Cursor 3将AI代码编辑器转变为代理管理控制台，使传统IDE退居次要地位。此举反映了AI辅助开发领域中代理编排日益重要的结构性转变。此番调整改变了模型选择、削弱了VS Code等传统IDE的优势，并重塑了工程师的工作流程，使之更像系统操作员，而非单纯的代码编写者。

> 译自：[Cursor's $2 billion bet: The IDE is now a fallback, not the default](https://thenewstack.io/cursor-3-demotes-ide/)
> 
> 作者：Janakiram MSV

上周，该类别中收入增长最快的AI代码编辑器发布了一款*并非*代码编辑器的产品。

[Cursor 3](https://cursor.com/blog/cursor-3)以代号Glass从零开始构建，它将代理管理控制台作为主要界面，并将传统IDE推向次要地位。工程师仍然可以在其中编写代码。但该产品的设计假设他们将把大部分时间花在调度代理、审查输出以及决定发布哪些内容上。提示框位于文件树曾经的位置。

![](https://cdn.thenewstack.io/media/2026/04/dd333462-cursor-3-1024x538.png)

几个月以来，[编码工具已成为AI模型的“二等公民”](https://thenewstack.io/ide-vs-desktop-agent/)。当一家年收入达到20亿美元的公司认同这一论点，并将其整个产品界面押注于此，便产生了Cursor 3。这一转变反映了基础设施工程师已经经历过的转型。

云仪表板取代了SSH终端。Kubernetes控制器取代了手动服务器配置。现在，编排层正在取代代码编辑器成为主要界面。模式是相同的，但风险更高，因为这次被降级的是开发者使用了40年的抽象层。

## Cursor 3 的功能

Cursor于2022年作为VS Code的一个分支起步。现在，这个分支有了一个围绕代理从零开始构建的兄弟产品。Cursor表示，新界面是“从零开始，以代理为中心”构建的，它将传统IDE视为一个随时可以切换的备用选项。

工作区默认支持多仓库。代理和人类可以同时在不同的仓库中操作，每个本地和云代理都可以在统一的侧边栏中看到。该侧边栏从Cursor所接触的每个界面（包括从移动设备、网页客户端、Slack、GitHub和Linear启动的会话）中提取代理。云代理会生成其工作的演示和屏幕截图，因此工程师在审查输出时无需在本地拉取代码即可了解更改内容。

突出的功能是“云切换”（Cloud Handoff）。你可以在任务进行中将正在运行的代理会话从笔记本电脑转移到Cursor的云端，让它在你关闭机器时继续工作，并在准备在桌面进行编辑和测试时将其拉回本地。反之亦然。在云端开始某项工作，并在需要完全控制时将其带回本地。这种本地和云环境之间的会话可移植性是大多数竞争工具中的一个空白。

可以将其视为从管理单个服务器到通过控制平面管理整个服务器群的转变。你仍然可以在需要时通过SSH连接到服务器。但控制平面是决策发生的地方，工作负载分配的地方，以及你查看系统状态的地方。Cursor 3以同样的方式对待代理。IDE是SSH。Glass是控制平面。

## 转型背后的压力

Cursor 3的发布时机并非偶然。Cursor在过去六周内进行了一系列我称之为“加速产品攻势”的行动。3月下旬《财富》杂志[发表的一篇专题文章](https://fortune.com/2026/03/21/cursor-ceo-michael-truell-ai-coding-claude-anthropic-venture-capital/)将该公司的处境描述为创新者困境的典型案例，报道引发了强烈反响。据彭博社报道，Cursor的年化收入运行率在2026年2月[突破](https://www.bloomberg.com/news/articles/2026-03-02/cursor-recurring-revenue-doubles-in-three-months-to-2-billion)20亿美元，在三个月内翻了一番。

但据《财富》杂志报道，Anthropic公司不到一年前推出的终端优先编码代理Claude Code，已达到25亿美元的运行率，拥有超过30万商业客户。开发者公开表示离开Cursor转投Claude Code，一位Cursor投资者告诉《财富》杂志，他投资的几家初创公司正在与Cursor脱钩。3月份有报道称，Cursor正在寻求一轮约500亿美元估值的新融资，尽管其增长势头的故事正在出现裂痕。

Cursor迅速采取了三项重大举措。3月5日，该公司[推出](https://techcrunch.com/2026/03/05/cursor-is-rolling-out-a-new-system-for-agentic-coding/)了Automations，这是一个无需人工干预即可响应GitHub事件、Slack消息和定时器触发代理的系统。

3月19日，Cursor发布了Composer 2，这是其基于月之暗面（Moonshot AI）的开源模型Kimi K2.5构建的首个内部编码模型。Cursor声称Composer 2在其专有的CursorBench上获得了61.3分，领先于Claude Opus 4.6的58.2分，且代币成本大大降低。这些基准数字需要注意，因为CursorBench是Cursor自己的评估套件。同样在3月份，Cursor[启用](https://thenewstack.io/cursor-self-hosted-coding-agents/)了自托管云代理，允许《财富》500强公司在其自己的基础设施上运行Cursor的代理。

随后便是Cursor 3。在一个月内进行了三次产品发布和一次全面的界面重建。这种节奏表明该公司认为其所处类别正在围绕自身进行重新定义。

## 结构性转变

现在，AI辅助开发领域的每个主要参与者都同意代理需要一个专门的编排界面。他们分歧在于该界面应该存在于何处。这种分歧是当前开发者工具中最有趣的架构分歧。

Anthropic的Claude Code是终端优先的。完全没有IDE。CLI是编排层，开发者通过shell中的自然语言命令进行工作。Anthropic后来在claude.ai/code添加了一个基于浏览器的界面和一个桌面应用程序，但终端仍然是重心。编排层完全存在于编辑器之外。

OpenAI则走了不同的道路。[Codex](https://openai.com/index/introducing-the-codex-app/)现在涵盖了一个独立的桌面应用程序、一个CLI、VS Code及其分支的IDE扩展，以及chatgpt.com/codex上的云界面。桌面应用程序是用于管理并行代理、审查差异和跨项目运行工作的“指挥中心”。OpenAI的赌注是编排层应该无处不在，可从开发者可能使用的任何界面访问。

> “代码编辑器定义了软件如何构建长达四十年。Cursor 3的赌注是，监督代理将比编辑文件更重要。”

Google的方案最接近Cursor。在向Windsurf支付24亿美元[许可费](https://www.cnbc.com/2025/07/11/google-windsurf-ceo-varun-mohan-latest-ai-talent-deal-.html)并将其CEO和关键工程师招入DeepMind后，Google发布了[Antigravity](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/)，这是一个代理优先的IDE，具有两种不同的模式。编辑器视图提供了一个传统的编码环境。管理器界面允许你并行生成、编排和**可观测性**多个跨工作区的代理。代理编排和代码编辑存在于同一个应用程序中，但位于不同的视图中。

Cursor 3遵循了这种IDE内部的模式，但进一步推高了比例。Glass使代理控制台成为默认视图，编辑器成为备用。Google的Antigravity将两种视图视为同等重要。这种侧重点的差异很重要，因为它表明Cursor认为开发者的时间将实际花在哪里。

与云基础设施的类比有助于阐明这种分歧。当AWS推出其管理控制台时，没有人停止使用SSH。但SSH不再是做出基础设施决策的地方。控制台成为了控制平面，而SSH成为了你偶尔才会使用的调试工具。

Anthropic和OpenAI押注编排层可以作为一个独立的应用程序，与IDE分离。Cursor和Google押注它需要与编辑器共存，因为当代理出错时，开发者仍然会希望深入代码。业界同意代理编排是新的主要界面。但架构尚未达成一致。

## 这对开发者意味着什么

实际影响分为三个目前重要的领域。

### 1. 模型选择成为基础设施

Cursor将Composer 2作为默认模型，但仍允许开发者根据对话切换到Claude、GPT-5.4和Gemini。现在，为你的代理提供动力的模型是一个基础设施决策，类似于选择数据库或云区域。代币经济学在规模化时会产生复合效应。Cursor公布的Composer 2标准定价为每百万输入代币0.50美元，每百万输出代币2.50美元（截至2026年3月），远低于Anthropic和OpenAI的尖端模型定价。对于运行数十个并行代理的团队来说，这种数学计算在工具选择上的驱动力远超功能比较或UI偏好。

### 2. VS Code的护城河正在枯竭

Cursor通过分叉VS Code来继承其扩展生态系统并立即获得分发。通过Cursor 3，该公司正在脱离这一基础来创造差异化。如果代理优先的界面获胜，VS Code扩展的相关性就会降低。Microsoft应该密切关注。VS Code是开发者工具重心这一持续了近十年的假设正在削弱。JetBrains面临同样的压力。当主要交互界面从编辑文件转向管理代理时，传统IDE在代码智能和重构工具方面的竞争优势就会减弱。

### 3. 你的工作流程在你的职位头衔改变之前就改变了

使用Cursor 3的工程师将时间花在审查代理生成的差异、验证云代理产生的屏幕截图、决定哪些任务推送到云端以及哪些保留在本地，以及管理PR工作流。这与编写代码是不同的技能组合。它看起来更像工程经理或平台操作员的工作，而不是传统的软件开发者。软件工程师的角色正在与在应用层工作的系统操作员的角色趋于一致。

> “软件工程师的角色正在与恰好在应用层工作的系统操作员的角色趋于一致。”

Cursor自身的发展轨迹说明了这一转变。该公司在2025年12月[收购](https://fortune.com/2025/12/19/cursor-ai-coding-startup-graphite-competition-heats-up/)了代码审查平台Graphite，因为正如CEO Michael Truell所说，随着AI加速代码编写，代码审查正在成为瓶颈。Cursor 3进一步深化了这一逻辑。如果代理编写代码，Graphite审查代码，那么工程师的工作就是编排这两者。IDE变得次要。

## 接下来会发生什么

AI编码代理的编排层现在是一个产品类别。每个主要参与者都发布了相关的产品。开放的问题是架构。编排层是存在于IDE内部、外部，还是同时存在于所有界面？Anthropic和OpenAI押注独立工具。Cursor和Google押注IDE集成的控制台。答案将决定未来十年哪家公司能赢得开发者忠诚度，就像2010年代初期的云控制平面之争决定了谁拥有基础设施一样。

代码编辑器定义了软件如何构建长达四十年。Cursor 3的赌注是，监督代理将比编辑文件更重要。Cursor并没有杀死IDE。它只是“降级”了IDE。如果这项赌注成功，那么人们记住的最后一个代码编辑器将是由打造出最好编辑器的那家公司所构建。敬请期待。