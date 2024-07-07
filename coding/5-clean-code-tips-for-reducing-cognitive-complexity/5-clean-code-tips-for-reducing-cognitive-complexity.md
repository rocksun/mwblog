
<!--
title: 降低认知复杂度的5个整洁代码技巧
cover: https://cdn.thenewstack.io/media/2024/07/6f4145ce-scrubbing.jpg
-->

降低认知复杂度是帮助您编写安全、可维护和可靠代码的关键，这将使开发人员（包括您自己）更快乐。

> 译自 [5 Clean Code Tips for Reducing Cognitive Complexity](https://thenewstack.io/5-clean-code-tips-for-reducing-cognitive-complexity/)，作者 John Clifton。

你可能理解试图理解别人旧代码（甚至是你自己的代码）带来的挫败感。时间流逝让你记忆模糊，现在你已经无法理解代码的逻辑。

创建你和其他人可以理解的代码至关重要。降低认知复杂度是帮助你编写安全、可维护和可靠的 [干净代码](https://www.sonarsource.com/solutions/clean-code/) 的关键，这将使其他开发人员（包括你自己）在长期内更快乐。以下是如何采取纪律性方法。

## 1. 编写团队会感谢你的代码

[软件开发非常像团队运动](https://thenewstack.io/managing-software-development-team-dynamics-from-within/)。理解你编写的代码如何融入整体项目以及其他需要阅读代码的开发人员如何理解它至关重要。

圈复杂度(Cyclomatic complexity)最初被引入作为一种衡量模块控制流测试和维护难易程度的方法。这个公式可以帮助根据代码中分支的数量来评估需要多少测试。它不会很好地反映出你或你的队友将来理解和维护代码的难度。

## 2. 生活并非一帆风顺

线性代码是你的朋友。如果所有代码都是一个接一个的命令链 - 没有循环或曲折 - 你就不会有任何问题在脑海中理清所有事情。在代码中添加循环和分支会使理解和处理代码变得越来越困难。

每次这样做都会使代码的认知复杂度逐渐增加。问题是开发人员需要能够 [编写循环和分支的代码](https://thenewstack.io/bad-code-stalls-developer-velocity/)，包括使用 if/else 语句的代码，来创建软件。这里关键的是专注。了解你正在使用什么，并清楚地知道你的代码是否做得太多。如果是，请考虑重构。了解代码的认知复杂度可以帮助你确定何时何地需要简化。

## 3. 嵌套会很快造成混乱

例如，嵌套代码（循环嵌套在循环中）难以理解。你嵌套代码越深，理清头绪并理解你正在处理的每一部分代码就需要付出更多努力。

查看你的代码，看看哪些嵌套组件导致了最大的头痛。然后，找到另一种编写代码的方法。了解每个组件带来的认知复杂度将帮助你走上正确的道路。

## 4. 有用的东西不会增加复杂度

存在许多结构可以使代码更清晰、更容易理解。switch 语句是一种很好的方法，可以帮助消除一系列嵌套的 if 或 if/else 语句，这些语句使代码变得模糊不清，并且不会增加代码的认知复杂度。帮助你跳出循环的 continue 或 break 语句也可以帮助你编写更清晰的代码，并且同样不会增加复杂度。这些只是可以帮助降低认知复杂度的不同类型结构中的一部分。

## 5. 使用正确的工具并编写干净代码

像 [SonarLint、SonarQube 和 SonarCloud](https://www.sonarsource.com/lp/products/all/) 这样的工具具有内置的认知复杂度测量功能，可以帮助你编写不仅运行良好，而且易于理解和构建的代码。它们可以帮助你更好地、更仔细地查看你的代码，以便你了解你在哪些地方使代码变得比必要时更复杂。专注于编写易于理解的代码，你的团队和未来的你都会感谢你！

开发人员应该始终专注于编写 [干净代码](https://www.sonarsource.com/solutions/clean-code/) - 安全、可靠、可读和可维护的代码，为所有使用它的人节省软件项目中的重大头痛。有了正确的思维方式和工具，你可以确保你的代码对 [软件质量](https://thenewstack.io/5-takeaways-from-smartbears-state-of-software-quality-report/) 有帮助，而不是阻碍。
