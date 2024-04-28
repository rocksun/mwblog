
<!--
title: 提升AI代码助手的5个策略
cover: https://cdn.thenewstack.io/media/2024/04/474ac28b-rizelscarlett-2.jpg
-->

开发者倡导者 Rizel Scarlett 在本周的 InfoBip Shift 上分享了如何让 AI 编码助手更有效、更高效。

> 译自 [5 Strategies for Better Results from an AI Code Assistant](https://thenewstack.io/5-strategies-for-better-results-from-an-ai-code-assistant/)，作者 Loraine Lawson。

与所有 GenAI 一样，Copilot 也是非确定性的；这意味着它们的结果会有所不同。但根据 [Rizel Scarlett](https://www.linkedin.com/in/rizel-bobb-semple/) 的说法，在使用 AI 代码助手时，开发人员可以使用提示工程来优化和指导 AI，以获得更好的结果——Rizel Scarlett 是一位开发人员倡导者，最近还为 [GitHub Copilot](https://thenewstack.io/github-copilot-and-open-source-a-love-story-that-wont-end-well/) 工作。

Scarlett 现在是 [TBD](https://www.tbd.website/) 的一名员工开发人员倡导者，TBD 是 Block 旗下运营的一个业务部门，致力于构建用于在国际间兑换货币的开源平台和协议。在本周于迈阿密举行的 [InfoBip Shift 大会](https://shift.infobip.com/) 上，她分享了五种提高 Copilot 结果的策略。

首先，她设置了一个场景：她问观众，想象一下，一位名叫 Dawson 的开发人员患有轻微的冒名顶替综合征。对 Dawson 来说幸运的是，她有一位可以提供帮助的朋友——一位名叫 Phil 的开发人员和时间旅行者，来自迪士尼的 [Phil of The Future](https://www.imdb.com/title/tt0340281/)，只不过他已经长大了。

Dawson 有一个问题：她必须创建一个身份验证程序，但她不知道如何创建，也不确定如何真正利用 Copilot 来帮助她，Scarlett 说。Phil 来自 22 世纪，那时 [AI 助手](https://thenewstack.io/meet-the-star-member-of-the-it-team-the-ai-assistant/) 是常态。他用五种提示 Copilot 的策略帮助她启动了她的工作。

## 策略 1：提供高级概念

第一步是向 GPT 提供高级背景。在她的场景中，Phil 通过构建 Markdown 编辑器进行了演示。由于 Copilot 不知道上下文，他必须提供上下文，他通过带有分步说明的大提示注释来做到这一点。例如，他告诉 Copilot ，“确保我们支持加粗、斜体和项目符号”，以及“你能在 React markdown 包中使用反应吗？”该提示使 Copilot 能够创建一个功能齐全但尚未解决的 markdown 编辑器。

## 策略 2：提供详细信息

Scarlett 建议，接下来向 Copilot 提供具体详细信息。

“如果他写一列说从 [API](https://thenewstack.io/api-design-is-pretty-bad-heres-how-to-fix-it/) 获取数据，那么 GitHub  Copilot 可能知道或不知道他真正想做什么，并且可能无法获得最佳结果。它不知道他想从哪个 [数据](https://thenewstack.io/sir-tim-berners-lees-solid-protocol-puts-data-back-in-the-control-of-the-end-user/) 中获取数据，也不知道它应该返回什么，”Scarlett 说。“相反，你可以写一条更具体的注释，说明使用 JSON 占位符 API，传入用户 ID，并将用户作为 JSON 对象返回。这样，我们可以获得更优化的结果。”

## 策略 3：提供示例

Scarlett 说，在向 AI 提供示例时，有三个术语需要理解：

- 零次学习，模型有望对从未明确训练过的任务做出正确的预测。一个人的例子是在不玩视频游戏的情况下尝试击败它，但使用游戏玩家从之前的视频游戏中学到的策略。
- 一次学习，向 AI 提供一个示例。推论是，在游戏中玩一场比赛后，有望能够熟练地扮演任何角色并击败任何对手。
- 少次学习，向模型提供一组小示例。这就像在新游戏中执行两到五个任务，然后有望完全掌握游戏。

## 策略 4：保持几个标签页处于打开状态

这可能有点令人惊讶，但保持编辑器中打开一个或两个标签页允许 GitHub  Copilot 从标签页中获取上下文。她警告说，打开的标签页过多会降低 Copilot 建议的质量。

## 策略 5：使用 Copilot 聊天

我们的女主角 Dawson 喜欢这些建议和结果，但她实际上想获得代码反馈。Scarlett 说， Copilot 带有聊天功能，可用于执行修复错误、格式化日期、重构代码、测试代码和 [生成](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/) 测试等任务。她说，可以要求它识别任何错误，然后要求它提供一个简短的解释并提供解决方案。然后，她演示了要求 GitHub  Copilot 使用开源 JavaScript 测试框架 [Jest](https://thenewstack.io/jest-metas-javascript-testing-framework-joins-openjs/) 生成一个[测试](https://thenewstack.io/microsoft-one-ups-google-with-copilot-stack-for-developers/)。（[Microsoft 的 Copilot ](https://thenewstack.io/microsoft-one-ups-google-with-copilot-stack-for-developers/) 也提供聊天界面。）

Scarlett 补充说，通过使用 Copilot，开发者可以做到的不仅仅是提高工作效率。她表示，Copilot 还可以提升心理安全感，尤其对于[容易出现冒名顶替综合征的新手开发者或其他人](https://thenewstack.io/shameless-developers-how-to-manage-imposter-syndrome-within-your-team/)来说。“

遗憾的是，事实是心理安全感在工作中并不总是很常见，尤其是在历史悠久的公司里，对于少数群体尤其如此，”她说。“初学者可以通过 Copilot 获得安全感，因为它可以作为同伴，在初次使用新工具时为我们提供点子。
