ServiceNow 以自动化业务工作流闻名，但如今，该公司自称为“业务重塑的 AI 控制塔”。

这一主题在本周举行的 Knowledge 2026 大会上得到了充分展示。周三，ServiceNow 宣布了新的治理功能、面向所有客户免费开放其低代码应用管理工具、与第三方开发工具的新集成，以及其 [智能体构建工具](https://www.servicenow.com/docs/r/intelligent-experiences/ai-agent-studio.html) 的更新。

ServiceNow 在去年的活动中首次提出了“控制塔”的比喻，但自那以后，人们越来越清楚地认识到，企业（实际上是所有企业）将 AI 智能体投入生产所需的是更好的护栏和治理。同时，他们不想被锁定在一套今天可能是尖端、但几个月后就会过时的工具中。

[Jithin Bhasker](https://www.linkedin.com/in/jithinbhasker/) 是 ServiceNow 的 Creator Workflows 和 App Engine 集团副总裁兼总经理，他在接受 *The New Stack* 独家采访时表示，虽然该领域的每个人都在投资智能体构建器和以 AI 为中心的应用构建工具，但 ServiceNow 不仅希望提供这些工具，还希望提供管理它们的工具。

> “我们拥有自己的氛围编程产品，但我们考虑得更长远……我们如何确保当智能体和应用程序在我们的平台上构建时，[它们] 拥有正确的安全护栏和控制措施。”

“我们拥有自己的氛围编程产品，但我们考虑得更长远，”Bhasker 说道。“我认为下一个大阶段是……我们如何确保当智能体和应用程序在我们的平台上构建时，[它们] 拥有正确的安全护栏和控制措施。我们正在投资 Agent Studio，同时也确保正确的治理和控制真正结合在一起，这样首席信息官（CIO）就不必担心‘影子 AI’。”

ServiceNow 这种做法的核心是意识到开发者已不再有忠诚度。虽然 ServiceNow 可能提供自己的智能体和应用构建器，但员工会想使用 Claude Code、Codex、Cursor、Windsurf，以及一两个月后可能出现的任何下一波智能体编程工具。

> “我们从根本上相信，虽然 AI 智能体解决方案和氛围编程是入门的好方法，但真正的企业价值来自于实际的企业级控制。”  
> ——Jithin Bhasker

“这实际上造成了 AI 资产和智能体的扩张，它们正被部署在一些生产实例和环境中，”Bhasker 说道。“这就是为什么我们从根本上相信，虽然 AI 智能体解决方案和氛围编程是入门的好方法，但真正的企业价值来自于实际的企业级控制。”

## 开发者零忠诚度时代的 ServiceNow

在 Knowledge 大会上，ServiceNow 推出了与 Cursor、Windsurf 和 GitHub Copilot 等智能体优先 IDE 的新集成，此外还有一套独立的 MCP 客户端集成，涵盖 Figma、GitHub 和 Miro，让 Build Agent 能够直接从这些工具中提取设计规范、代码上下文和需求。正如该公司所指出的，重点是“无论开发者在哪里为 ServiceNow 进行构建，都能赋予他们扩展的技能和上下文”。

> “无论你是 GitHub Copilot 用户、Cursor [用户] 还是 Claude [用户]，都不重要，你可以使用我们的 SDK 技能在任何地方开始构建。”

“关键在于让任何工具都能轻松访问并能在 ServiceNow 平台上进行构建，”Bhasker 说道。“我们在那里获得了两个优势：第一，我们的用户画像成倍增加。过去，我们重金投资于自己的工作室和 IDE 等。现在，我们说无论你是 GitHub Copilot 用户、Cursor [用户] 还是 Claude [用户]，都不重要，你可以使用我们的 SDK 技能在任何地方开始构建。”

对于开发者来说，这意味着他们现在可以从 ServiceNow 的 Build Agent 中获取核心技能——在 ServiceNow Studio 内部，该工具目前由 Anthropic 的 Claude Opus 4.6 提供动力——并在他们首选的 IDE 中原生使用，而无需切换上下文。Build Agent 是 ServiceNow 的 AI 智能体，用于根据自然语言提示创建和更新 ServiceNow 应用程序，在此之前，它仅在 ServiceNow IDE 中可用。

## Build Agent 实现便携化

随着 Knowledge 2026 的发布，该公司还首次将 Build Agent 嵌入到 ServiceNow Studio 中，并新增了“全局范围”（Global Scope）模式，使 Build Agent 能够修改开箱即用的 ServiceNow 应用程序（如 ITSM、HRSD 和客户服务），而不仅仅是在自定义范围内生成全新的应用程序。最后一点比听起来更重要：企业在 ServiceNow 上的大部分支出都用于定制这些现有应用程序，而非从零开始的构建。

应用程序构建完成后，开发者可以将其构建的智能体和应用程序交由 ServiceNow 的应用引擎管理中心（AEMC）免费管理，这是该公司用于管理其平台上运行的应用程序全生命周期的服务。AEMC 还增加了一个自愈测试环路，它可以自动编写测试、诊断故障并修复损坏的构建，直到通过质量关卡；此外还有 Agent Packs，允许客户将自己的开发标准编码到 Build Agent 中。Bhasker 认为，通过向所有用户（无论持有何种 ServiceNow 许可证）开放 AEMC，公司消除了使用它的阻碍。

“我决定开放应用引擎管理中心的原因是，我觉得这是当务之急——因为有这么多应用程序和智能体正在被构建，我们感到有责任确保这些智能体和应用程序以正确的方式构建，并具备企业级治理控制和安全性，”Bhasker 解释道。

在实践中，这意味着开发者可以在 Claude Code 中编写一个应用程序，将其推送到 ServiceNow 实例中，然后 AEMC 将运行测试并扫描应用程序，以确保其已准备好在生产环境中运行。ServiceNow Studio 和重新设计的 AI Agent Studio（该公司用于 AI 智能体的对话式创建界面）现在也不再需要特殊许可证即可使用。

## 每个应用都将拥有一个智能体

这一切的一个有趣之处在于，未来每当在 ServiceNow 平台上构建应用程序时，ServiceNow 都会自动推荐一个可以存在于该应用程序内部的 AI 智能体。

“无论你是在财务部门，试图每天处理数百张发票并匹配收据。想象一下，你身边有一个智能化的、自主的专家，他正在协助你完成这些工作，”Bhasker 说道。“你可以在任何地方构建，在 ServiceNow 的平台上托管，现在该平台上构建的每个应用程序都将获得一个带有组件和控制措施的自主 AI 智能体专家的自动推荐。”

## ServiceNow 并非孤军奋战

在许多方面，这里的推介并不是 ServiceNow 独有的。Salesforce 在 2026 年 4 月的 TDX 大会上发布了 Agentforce Vibes 2.0 和 Headless 360，也采用了类似的“随处构建、此处部署”的框架。微软也通过 Copilot Studio 和 Power Platform 的托管环境提出了同样的观点。该公司认为，将 ServiceNow 的版本区别开来的是其现有的庞大业务版图。其服务已经运行了大多数财富 500 强企业内部的 IT、人力资源、法务和客户服务的工作流，这种跨部门的影响力是任何竞争对手从通常窄得多的起点出发都难以企及的。