微软在上周的 [Build 2026](https://news.microsoft.com/build-2026/) 大会上宣布了对其旗舰级 [Visual Studio IDE](https://thenewstack.io/developers-test-visual-studio-2026s-ai-native-claims/) 的一系列更新。这些更新围绕着一个主题展开，即该公司所称的“参与开发而非仅在一旁辅助的智能体”，同时还推出了一项备受期待的举措：允许开发者将自己的 AI 模型和密钥带入 IDE 中。

这些发布涵盖了调试、性能剖析、测试、合并冲突解决、.NET 现代化，以及一项全新的模型灵活性选项。微软表示，这将为那些因环境限制而无法使用现有 AI 集成方案的团队敞开大门。

“从历史上看，Visual Studio 中的 AI 集成一直局限于一小部分经过批准的终点，”Visual Studio 首席产品经理 [Mads Kristensen](https://www.linkedin.com/in/madskvistkristensen/) 在配合此次发布的 [博客文章](https://devblogs.microsoft.com/visualstudio/whats-coming-next-in-visual-studio-our-microsoft-build-2026-announcements/) 中写道。“这适用于许多开发者，但它也冷落了真正的客户，包括那些环境要求做出不同选择的团队。”

## BYOK：企业级解锁

自带密钥（BYOK）的声明对企业级客户来说可能是最具意义的。微软正在转向一种新模式，允许开发者使用不同的 AI 模型——无论是在本地运行还是在云端运行——而不是被锁定在 Visual Studio 历史上支持的少数几个终点上。

> 微软乐意在灵活性上展开竞争，而不是假设开发者只会在雷德蒙德（微软总部）批准的任何 AI 技术栈内工作。

这对于那些因合规性要求、成本限制或数据主权顾虑而无法使用当前版本 Visual Studio AI 功能的团队来说至关重要。此举也表明，微软乐意在灵活性上展开竞争，而不是假设开发者只会在雷德蒙德批准的任何 AI 技术栈内工作。

除了 BYOK 之外，微软更大的架构推动力是将智能体直接嵌入到 IDE 的现有工具链中——包括调试器、性能剖析器和测试运行器——而不是将 AI 仅仅视为一个平行的聊天界面。

“这不是为了取代你已经依赖的工具，”Kristensen 写道。“而是为了更有效地将它们连接起来。”

这一实际应用场景主要针对在大型代码库中工作的企业级 [C#](https://thenewstack.io/c-compiler-lead-jared-parsons-on-20-years-at-microsoft/) 和 [C++](https://thenewstack.io/introduction-to-c-programming-language/) 开发者。正如 Kristensen 所说，在这些场景中，难题并不是“编写这个函数”，而是“找出这个东西在负载下为什么变慢”。这些智能体旨在帮助更快速地识别问题、解释正在发生的事情、提供修复建议并协助验证结果——所有这些都在现有调试器和性能剖析器的上下文中完成，而无需开发者频繁切换上下文到聊天窗口。

专门的 Build 专题分会——由 Kristensen 和微软首席软件工程师负责人 [Nik Karpinsky](https://www.linkedin.com/in/karpinsn/) 主持的 [“Visual Studio 中的 GitHub Copilot：能够进行调试、性能剖析和测试的智能体” (BRK207)](https://build.microsoft.com/en-US/sessions/BRK207)，提供了关于该主题的更多信息。

## 现代化升级迎来更大雄心

微软还在扩展其所谓的 [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 现代化升级，这是内置于 Visual Studio 中的智能体体验，用于将应用程序升级到最新的 .NET 技术栈。

今年夏天的新增功能：能够将 [Web Forms](https://learn.microsoft.com/en-us/aspnet/web-forms/what-is-web-forms) 应用程序迁移到 [Blazor](https://thenewstack.io/no-more-javascript-how-microsoft-blazor-uses-webassembly/)，并向现有应用程序中添加 [Aspire](https://thenewstack.io/microsofts-net-aspire-the-spring-boot-of-net-development/)，以实现面向云的 [可观测性](https://thenewstack.io/introduction-to-observability/) 和编排。该现代化升级智能体旨在评估项目、制定迁移计划并逐步执行升级。

这一方案主要针对那些因为彻底重写的经济效益不划算，而长期维持着老化 Web Forms 代码库的团队。智能体辅助的方法是否能真正改变这一权衡仍有待观察，但与通用的代码生成相比，这显然是一个更具体的应用场景。

## 值得注意的其他小改动

微软还推出了一个提升生活质量的修复方案，解决了一个大多数 Visual Studio 开发者都遇到过的场景：即便“错误列表”中已经显示了显而易见的问题，构建依然会运行，最后却因为早已显而易见的问题而宣告失败。Kristensen 写道，未来，Visual Studio 将在构建开始前检查错误和警告。

> Kristensen 写道，未来，Visual Studio 将在构建开始前检查错误和警告。

在协作方面，微软正在开发 AI 辅助的合并冲突解决功能——并非自动合并，而是帮助理解冲突并做出决策。即将推出的还有：微软编写的技能，这些技能会根据项目类型和上下文自动应用，从而减少了开发者需要知道如何编写提示词的需求。

## 底层原理

在这一切的底层，Visual Studio 正在转向以 GitHub Copilot SDK 作为其 AI 集成的基础。虽然这一改变不会在任何菜单中直接体现，但微软表示，这将使公司能够走得更快，并与更广泛的 Copilot 生态系统保持一致。

完整的公告内容可在 [Visual Studio 博客](https://devblogs.microsoft.com/visualstudio/)上查看。此外，Build 大会的分会内容也在 [build.microsoft.com](https://build.microsoft.com/en-US/home) 上提供免费的在线流媒体播放。