几年前，我在一次工程会议上抛出了可访问性问题，我眼睁睁地看着房间里的活力消失殆尽。有人咕哝着关于家庭作业的事情，几个人翻了白眼，我确信其余的人只是默默地希望我会忘记这件事。

并不是[工程师不想构建可访问的产品](https://thenewstack.io/entrepreneurship-for-engineers-how-to-build-products-customers-love/)。可访问性往往会在潜在客户要求一种叫做 VPAT 的东西时才出现。我们都可以想象到那位引用 WCAG 标准的“可访问性顾问”，它立即让我们想起那位将 OWASP 指南作为安全“要求”提出的安全顾问。 唉。

但现在是 2025 年，可访问性是基本要求。

可访问性不仅仅是一个复选框或法律术语。它也不是合规拥护者的支线任务。相反，它对于构建弹性、用户友好和面向未来的软件越来越重要。如果您的产品恰好涉及文档（PDF、表格、报告），那么风险会显着提高。

在 Nutrient，我们构建的工具可以帮助用户与文档交互，而不仅仅是 UI。这意味着可访问性不仅仅是一个前端问题，它还融入到我们呈现、预览和操作的内容中。我们已经深刻地认识到，如果您的 PDF 是一个既不能被开发人员也不能被最终用户管理的未标记内容的迷宫，那么仅通过在几个按钮上贴上 aria-label 来修复可访问性是行不通的。

本文面向[工程师及其周围的生产团队](https://thenewstack.io/why-successful-platform-engineering-teams-need-a-product-manager/)，他们已准备好停止对该话题翻白眼，而是开始解决问题。我们将保持简单，跳过冗余，专注于重要的事情：为什么可访问性现在应该引起您的注意，以及如何在不精疲力尽的情况下取得有意义的进展。

## 双层问题：UI 与以用户为中心的可访问性

对于大多数产品团队来说，可访问性始于 UI 并止于 UI：用户是否看到了正确的内容？他们能否点击、键盘 Tab 键或滑动浏览？标签是否清晰、颜色是否可读、焦点指示器是否可见？

这些都是好问题。但它们忽略了更重要的一点。

可访问性不是关于 UI，而是关于用户。无论用户角色卡片如何建议，用户都不会以可预测的理想化状态出现。有时他们使用屏幕阅读器。有时他们完全通过键盘导航。有时他们只是暂时受损——手腕骨折、偏头痛，或者只是用一只胳膊抱着婴儿，同时用另一只胳膊使用您的应用程序。

这就是为什么可访问性很重要。它与一致性级别、标准和满足法律部门无关。而是要确保人们（真实的、多样的和不可预测的）能够与我们构建的内容进行交互。

这就是游戏规则正在改变的地方：界面不再是固定的。人工智能可以动态生成 UI，并为最终用户进行个性化设置。应用程序越来越多地将来自 API、Markdown、文档和用户输入的部分拼接在一起。

仅仅设计一个漂亮的 UI 并确保它可以以可访问的方式使用是不够的。我们必须确保构建块（组件、内容、文档，尤其是 AI 生成的模块）默认情况下是可访问的。如果您在应用程序中预览 PDF 或动态呈现结构化内容，则可访问性不是可以在之后添加的东西。

在 Nutrient，我们看到了文档中的这种表现。但是，这个教训可以广泛应用：在一个 UI 越来越流动的世界中，可访问性必须从基础开始。不仅在于它的外观，还在于它的行为、声音和适应方式。

这不是一个极端情况。这就是软件的发展方向。

## 2025 年的法规如何使可访问性成为基本要求

如果可访问性一直感觉像一项“总有一天”的任务——在发布后清理或委托给 QA 的事情——那么 2025 年将改变这一点。

《欧洲可访问性法案》（EAA）于 2025 年 6 月 28 日生效。它规定，在欧盟向消费者提供的任何数字产品或服务（从银行应用程序到电子商务平台）都必须对所有用户都可访问。这包括网站、移动应用程序，是的，还有文档。

在大西洋彼岸，美国正在迎头赶上。根据更新后的《美国残疾人法案》（ADA）规定，州和地方政府必须在 2026 年和 2027 年之前使其数字体验符合 WCAG 2.1 AA 级标准。私营公司紧随其后。

诉讼呢？它们已经开始了。可访问性诉讼正在增加，采购团队开始以与对待安全性相同的方式看待可访问性——作为交易的决定因素，而不是功能请求。

但是——再说一遍——这不仅仅是法律压力。

可访问性正在成为现代软件基础设施的重要组成部分。随着 AI、个性化和响应式[设计创造出更动态的界面](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/)，确保包容性的唯一方法是将可访问性作为构建事物不可或缺的一部分，而不是以后添加的附加物。

可访问性是否会出现在您的待办事项列表中已不再是一个问题。而是什么时候。或者它可能已经在那里了。这也取决于您是否准备好在截止日期之前或发生紧急情况之后处理它。

## 不需要可访问性专家的实用工程步骤

说实话：可访问性会让人感到不知所措。这些标准很密集，工具不一致，并且这些指南有时读起来好像是专门为合规官员而不是交付代码的人编写的。

但这里有个好消息：您不必把所有的事情都做完。您只需要停止忽视火灾。

从基础开始——真正帮助实际用户并且几乎出现在每个标准和审计中的事情：

* 使用语义 HTML。<button> 每次都比 <div onclick> 好。好像有人必须告诉您这一点。
* 标记您的控件。每个输入都需要一个标签。除非纯粹是装饰性的，否则每个图像都需要替代文本。不要过度；用户不希望屏幕阅读器解释小插曲。
* 支持键盘导航。Tab 键顺序应该有意义。焦点不应消失。跳过链接不是老式的——它们是必要的。
* 检查您的对比度。这不仅仅是美学。糟糕的对比度会使您的应用程序对某些用户来说无法阅读。

这些不是奇特的做法。它们只是合理的默认值。

然后，引入工具：

* 使用 Axe、Lighthouse 或 WAVE 等自动化检查器来发现容易解决的问题。
* 偶尔使用真实的辅助技术进行测试——屏幕阅读器、降低的运动设置或高对比度模式。
* 将可访问性检查纳入您的 CI 管道。像对待性能预算或测试覆盖率一样对待它：可见、自动化且不容协商。

如果您的产品涉及[动态内容或文档](https://thenewstack.io/how-to-use-llms-for-dynamic-documentation/)，也要考虑该输出的可访问性。问：屏幕阅读器可以理解吗？有人可以在没有鼠标的情况下填写它吗？您不需要成为 PDF/UA 专家，但您确实需要关心它。

您并不孤单。许多开源库、设计系统和框架现在都将可访问性放在首位。使用它们。扩展它们。当它们不足时，提交问题。

进步并不意味着完美。这意味着决定不发布可避免的障碍。

## 从复选框心态到核心工程实践

可访问性不是您可以一次性勾选的功能。它是一个持续的实践，就像测试、安全或性能一样。它并不总是赢得冲刺积分。它并不总是出现在用户反馈中。但是当它缺失时，某些人根本无法使用您构建的东西。

当这种情况发生时，这不仅仅是一个技术故障。这是一种将人们拒之门外的体验。

您不需要一夜之间成为专家。但您可以开始。您可以修复您知道已损坏的内容。但更好的是，您可以[建立可在您的团队中扩展的习惯](https://thenewstack.io/high-performing-devops-teams-build-self-service-platforms/)、您的产品以及您甚至尚未想到的未来界面。

因为当 UI 消失时——当 AI 完全接管布局的生成，或者当您的应用程序适应语音、屏幕阅读器或未知输入时——唯一能确保可用性的就是您的组件、您的内容和您的代码尊重用户现实的程度。

这就是**可观测性**。不是一个复选框，而是一个良好的软件基础。

如果您是一名工程师，那么这个基础就是您要构建的。拥有它。让人们感到自豪。