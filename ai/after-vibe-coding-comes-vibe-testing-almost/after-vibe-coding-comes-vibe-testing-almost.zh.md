[DevOps](https://thenewstack.io/devops/) 平台供应商 [Harness](https://www.harness.io/) 今天正式发布了其 [Harness AI Test Automation](https://www.harness.io/products/ai-test-automation) 工具，该公司称其为业界首个 AI 原生的端到端测试自动化解决方案。

Harness AI Test Automation 引入了“基于意图的测试”——一种革命性的方法，用户可以使用 [自然语言](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/) 描述他们想要测试的内容，而不是编写测试脚本。[AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 然后会计算出如何执行和验证测试，即使 UI 发生变化，Harness AI Test Automation 的业务负责人 [Sushil Kumar](https://www.linkedin.com/in/sushil-kumar-343780/) 告诉 The New Stack。

Kumar 表示，虽然像 [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 和 [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) 这样的 AI 工具已经极大地加速了代码生成，但测试仍然停留在 2012 年代的实践中。这造成了一个瓶颈，代码可以在几小时内生成，但由于缓慢的手动测试流程（尤其是端到端测试），需要数周或数月才能投入生产，他说。

Harness AI Test Automation 旨在满足现代 DevOps 所需的速度、规模和弹性。该工具使企业能够用无缝的、AI 驱动的解决方案取代过时的测试框架，从而在 [软件开发生命周期 (SDLC)](https://thenewstack.io/how-ai-is-reshaping-the-software-development-life-cycle/) 中实现更智能、更快速的测试。Kumar 表示，通过此产品，Harness 可以提供一个完全自动化的软件交付平台，用户可以使用 Harness 平台编写代码、构建、测试和部署应用程序。它消除了手动差距和工具链孤岛，并完善了 Harness 端到端 DevOps 平台，该平台被花旗、美国联合航空、精选酒店和家得宝等主要品牌使用。

## 代码编写快，测试慢？ 不再是这样

“生产力已经大幅提高，”Kumar 说。“不幸的是，你创建的代码无法尽快到达客户手中，因为现在测试已经成为瓶颈。”

Harness 工具使软件开发团队能够更快地交付高质量的软件。

“传统的测试方法难以跟上——它太手动、脆弱且缓慢。因此，我们用 AI 重新构想了测试，”Kumar 在一份声明中说。“基于意图的测试为自动化带来了更大的智能和适应性，并且它可以无缝集成到你的交付管道中。”

此外，Kumar 指出，[Google](https://cloud.google.com/?utm_content=inline+mention) 的 [2024 DORA 报告](https://dora.dev/research/2024/dora-report/) 发现，尽管 AI 提高了生产力，但软件交付实际上有所放缓，因为测试无法跟上，并且大约 70-80% 的组织仍然依赖手动测试方法，从而减慢了交付速度并引入了风险。

然而，通过在公司内部使用该工具，Harness 已经看到了显着的生产力提升，该产品的早期（beta）用户也是如此。

例如，一位没有质量保证 (QA) 背景的 Harness 项目经理在 2.5 周内构建了 55 个自动化测试——这通常需要一个专门的 QA 团队花费数月才能完成。[Rohan Gupta](https://www.linkedin.com/in/swarnendurohan-gupta/) 是 Harness 的首席产品经理，他在一份声明中说：“使用 AI Test Automation，我只是简单地编写并勾勒出所有测试用例，在大约 15 到 20 分钟内，我就能够完成一个测试。使用模板功能，我们能够在两周半的时间内从零开始创建一套 55 个测试。”

同时，通过使用 Harness AI Test Automation，Harness 的客户 [Siemens Healthineers](https://www.siemens-healthineers.com/) 减少了 QA 瓶颈，并将测试创建时间从几天缩短到几分钟。

[Amrita Majumder](https://www.linkedin.com/in/amritamajumder/?originalSubdomain=in) 是 Siemens Healthineers 的首席 QA 工程师，她在一份声明中说：“我们可以在浏览器中清楚地看到哪里出了问题，并直接编辑该步骤。这真的非常快速。”

Kumar 说：“他们将测试创建时间缩短了 90%，因为他们不必再编写脚本。他们只需编写提示即可。”

## 先是“氛围编码”，现在是“氛围测试”？

Kumar 说，用户无需编写脆弱的脚本，而是编写自然语言提示，例如“将 100 美元以下的运动鞋添加到购物车，以新用户身份结账”，AI 会处理执行、数据生成和结果验证。当 UI 更改破坏传统脚本时，此 AI 会自动适应。

Kumar 告诉 The New Stack：“你不再编写脚本。你只需告诉我们的 [agentic AI](https://thenewstack.io/agentic-ai-the-missing-piece-in-platform-engineering/) 平台工作流程是什么，然后你将完全按照你想要的方式描述它。电子商务网站用户可以编写‘转到店面，根据评分选择商品，添加到购物车，验证总计并结账’，即使 UI 发生变化，系统也会找出该怎么做。”

这听起来像氛围测试。

“我们实际上在想，‘嘿，我们应该称它为氛围测试吗？’ 我们可以接受，但我认为存在差异，”Kumar 说。

验证是测试的关键，因此氛围式方法的效果较差，Kumar 说。

事实上，这与“[氛围编码](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)”类似，开发人员表达的是高级意图，而不是详细的指令。Kumar 承认了概念上的相似性，但解释了他们为什么选择“基于意图的测试”，强调需要超越“氛围”的严格验证。

他说：“在基于意图的测试中，我们实际上会采取更精细的步骤。在每个步骤中，我们都会验证应用程序是否做出了响应。这是一个类似的想法，但如果你正在使用自然语言提示进行氛围编码，你需要像我们所说的基于意图的测试这样的技术来完成端到端流程。”

## AI 测试 AI

该工具的一个关键要素是使用 AI 来测试 AI 生成的代码。Harness 在内部使用该平台来测试其 DevOps 助手，该助手根据自然语言请求生成 YAML 管道代码。

Kumar 指出：“我们正在使用 AI 来测试 AI。编写确定性结果的传统方法不起作用，因为 AI 响应取决于上下文。”

该系统会自动调用 DevOps 助手，分析生成的 YAML 代码，并验证其是否执行了请求的功能——所有这些都无需人工干预。

## 主要特点

### **无需编写代码即可创建测试**

* 通过记录交互进行实时测试编写
* 自然语言测试用例（“登录是否成功？”）
* AI 在每个步骤后自动生成断言
* 通过类似人类的 AI 验证进行可视化测试

### **自我修复维护**

* AI 生成的选择器适应 UI 更改
* 测试维护减少高达 70%
* 智能选择器技术可在各种环境中工作

### **智能执行**

* AI 区分瞬时问题和真实错误
* 并行执行扩展到数千个测试
* 通过动态参数化进行数据驱动测试

## 它是如何开始的

Kumar 说，Harness AI Test Automation 的工作始于三年前的 [Relicx](https://relicx.ai/)，这是他创立的公司，[Harness 去年收购了该公司](https://relicx.ai/blogs/exciting-news-announcing-the-next-phase-of-our-journey)。该工具代表了在 agentic AI 开发方面的三年研发成果。

“…我们很高兴看到 Harness 和 Relicx 的综合优势将如何继续颠覆测试自动化领域，尤其是在生成式 AI 快速发展的情况下，”Kumar 在去年 8 月宣布收购的博客文章中写道。“我们相信，下一步将为你的开发流程带来显着价值，我们渴望继续在此过程中为你提供支持。”