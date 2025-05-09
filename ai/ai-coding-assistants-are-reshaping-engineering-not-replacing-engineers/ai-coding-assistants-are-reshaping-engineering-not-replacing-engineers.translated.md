# AI 编码助手正在重塑工程，而不是取代工程师

![Featued image for: AI Coding Assistants Are Reshaping Engineering — Not Replacing Engineers](https://cdn.thenewstack.io/media/2025/03/184d8e33-fahim-muntashir-14joixmsoqa-unsplash-1024x683.jpg)

[Fahim Muntashir](https://unsplash.com/@f12r?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-man-using-a-laptop-computer-on-a-wooden-table-14JOIxmsOqA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

IntelliSense 是微软在编码辅助方面的早期创新之一，最初在 Visual Basic 5.0 (1996) 中引入，后来在 Visual Studio 97 中扩展。它可以帮助自动完成对象——例如，如果你有一个名为 steering wheel 的对象，它会建议相关的属性和方法，从而节省开发人员不断查找文档的时间。

编程语言、对象和 IDE 协同工作，因此程序员不必过多考虑语法。它只是按预期完成。这远早于像 Google Search 这样的工具使自动完成成为主流。因此，作为程序员，我们长期以来已经习惯了这种增强功能。AI 编码助手只是它的一个扩展。

**编码工具的演变**

像 Vi 和 Emacs 这样的文本编辑器已经存在了近 50 年，塑造了[开发人员编写和编辑代码的方式](https://thenewstack.io/developers-put-ai-bots-to-the-test-of-writing-code/)。例如，Vi 就像演奏乐器一样——如果你擅长它，你可以非常快速地移动代码。它允许你重复上一个动作 20 次，这对于使从 100 行中删除空格等繁琐的任务更有效率来说非常重要。

随着时间的推移，编辑器不断发展，以提高编程效率。Vi 和 Emacs 有其硬核的、键盘驱动的方法，后来，VS Code 通过更智能的自动完成命令行集成和 AI 驱动的辅助功能对其进行了扩展。一个关键的转变是引入了语言服务器协议 (LSP)，该协议标准化了编辑器如何在不同的编程语言中提供实时反馈和建议。

**当今 AI 编码助手的状态**

在 [TigerEye](https://www.tigereye.com/)，我们不将自己限制在单一的 AI 编码解决方案上，因为其中一个仍然令人印象深刻。没有明显的赢家。

我们已经研究了 GitHub Copilot、Cursor 和 Zed，很明显，它们之间的差异并不那么显着。它们都由类似的模型提供支持，真正的优势在于不同编辑器中的用户体验，而不是一个 AI 比其他 AI 更好。

为了进一步评估，TigerEye 团队还运行了本地模型来测试它们。这需要一台强大的机器，但它提供了一种私有且免费的方式来试验编码代理，而无需将代码发送到外部服务器。这种方法使我们能够更好地控制安全性、性能和定制，同时让我们评估这些模型在实际开发工作流程中的表现如何。

现在最大的问题是：哪一个进化最快？

使用传统的 IntelliSense，自动完成可以帮助你填写对象属性。使用 AI，可以自动完成更多内容，但仍然不足以完全信任。你必须审查所有内容。AI 还不能可靠地编写完整的、可用于生产的代码。现在的竞争是关于哪个编码助手将提供最干净、最佳调整的用户体验以及最有价值的 AI 增强功能。

**AI 编码助手擅长的地方**

AI 擅长以下几件事：

**编写单元测试**：这对开发人员来说是一个很大的痛苦。测试驱动的开发要求你先[编写测试用例](https://thenewstack.io/using-the-kyverno-cli-to-write-policy-test-cases/)，然后再编写实际代码，这完全是一种苦差事。使用 AI，你可以先[编写代码，然后让助手生成](https://thenewstack.io/how-generative-ai-coding-assistants-increase-developer-velocity/)测试用例。它可以节省数小时。
**生成样板代码**：当需要编写重复的代码块时，AI 可以很好地处理它。
**数学和算法实现**：假设我需要在红色和蓝色之间插值 100 个步骤的颜色。AI 可以快速准确地生成用于此目的的数学密集型逻辑。这种事情过去需要 50 多行代码，并且需要手动处理公式，但现在我可以直接询问 AI，它会在几秒钟内吐出一个高质量的实现。
**发现潜在的错误**：我不会取代正式的安全审计，但它可以充当一个弱的结对程序员或调试助手。一个有用的提示是，“*我认为这会泄漏内存。告诉我哪里泄漏了。*” AI 编码助手可以突出显示潜在的问题和值得调查的领域。
我们已经看到 AI 助手在[实际开发中表现良好](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/)。大约 50% 的 [DuckDB.dart](https://github.com/TigerEyeLabs/duckdb-dart) 单元测试是由 AI 编写的，并且所有 API 相关的代码注释都经过 AI 的校对或生成，以确保清晰度和一致性。这有助于标准化文档，同时节省重复测试编写的时间。

**AI 编码助手的不足之处**

**系统设计**：这是中高级开发人员的核心工作，而 AI 在这方面表现很差。

**重构代码**：AI 尚未具备分析完整代码库并有意义地改进现有代码的能力。

**理解超出单个文件的上下文**：虽然 AI 助手主要处理单个文件，但像 Cursor 的 Composer 功能和 Zed 即将推出的 Suggest Edit 功能等工具正开始通过允许程序员指定哪些文件是必不可少的来解决这个问题。然而，这仍然是手动 LLM 上下文管理，需要[工程师来指导 AI，而不是 AI 自行开发](https://thenewstack.io/developer-guide-to-the-crewai-agent-framework-for-python/)适当的系统范围的感知。它正在改进，但远非无缝。

最大的问题是什么？AI 缺乏直觉。

[大型语言模型](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/)无法以允许他们设计大型系统的方式进行思考。他们可以总结和重复已知的最佳实践，但当涉及到真实的、创造性的系统设计时……他们会失败。
这就像要求 AI 从头开始设计一家初创公司一样。它可以给你提供高层次的建议（因为有关于它的书籍和博客文章），但它无法完成实际的工作。

**安全和隐私**

TigerEye 不使用适用于我们整个代码库的 AI 工具。我们只使用零数据保留的 AI；我们输入的任何内容都不会被存储或用于模型训练。

这是我们的基本要求。除非我们明确控制其处理方式，否则我们不会将专有代码发送到外部模型。许多公司应该更加关注这一点。

**AI 驱动开发的未来**

[AI 编码助手的下一个重大飞跃](https://thenewstack.io/google-vaunts-new-gemini-code-assist-tool-at-cloud-next-2024/)将是当他们开始从开发人员的实时工作方式中学习时。

目前，AI 无法识别会话中的编码模式。如果我连续执行相同的操作 10 次，那么当前没有任何工具会问：“你想让我对接下来的 100 行执行此操作吗？” 但是 Vi 和 Emacs 在几十年前就通过宏和自动按键减少解决了这个问题。AI 编码助手甚至还没有赶上那个效率水平。

最终，AI 助手可能会变成基于插件的，因此[开发人员可以选择最适合他们首选编辑器的 AI 驱动功能](https://thenewstack.io/using-apis-with-low-code-tools-9-best-practices/)。深度集成的 IDE 体验可能会提供更多功能，但许多开发人员不想切换 IDE。

**AI 会取代开发人员吗？**

不会。

AI 将取代软件工程师的想法是无稽之谈，尤其是对于初级和中级职位。AI 将要做的是让优秀的工程师更快。它不会消除工作岗位；它会提高个人生产力。

这是根本性的转变：10 倍工程师不再是独角兽。

借助 AI，大多数中高级[工程师现在都可以成为 10 倍工程师](https://thenewstack.io/cadence-is-everything-10x-engineering-orgs-for-10x-engineers/)。

**最后的想法**

AI 编码助手具有潜力，但它们尚未改变游戏规则。目前，它们：

- 加速重复性编码任务（测试、样板代码、算法）
- 使学习更快（像 CS 教授一样解释概念）
- 在系统设计方面失败（没有实际的问题解决能力）
- 缺乏完整的项目上下文（仅处理单个文件）

今天最好的方法是在 AI 擅长的地方使用它，并在它薄弱的地方忽略它。

软件工程是一个快节奏的职业。语言、框架和技术来来去去，学习和适应的能力将那些蓬勃发展的人与那些落后的人区分开来。

AI 编码助手是这个周期中的另一次进化。它们不会取代工程师，但会改变工程的完成方式。关键不是抵制这些工具；而是学习如何正确使用它们，并对它们的能力和局限性保持好奇。

在这些工具改进之前，最好的工程师将是那些知道何时信任 AI、何时仔细检查其输出以及如何将其集成到他们的工作流程中而不依赖于它的人。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)