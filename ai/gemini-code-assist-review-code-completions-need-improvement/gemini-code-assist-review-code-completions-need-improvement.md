
<!--
title: Gemini代码助手审查：代码补全需要改进
cover: https://cdn.thenewstack.io/media/2025/03/69600efb-joshua-aragon-eab4ml7c7fe-unsplashb.jpg
-->

> 译自：[Gemini Code Assist Review: Code Completions Need Improvement](https://thenewstack.io/gemini-code-assist-review-code-completions-need-improvement/)
> 
> 作者：David Eastman

资深工程师David Eastman试用了谷歌最新的Gemini 代码助手，并将其输出结果与GitHub Copilot和Augment Code进行了比较。

谷歌进军代码辅助领域只是时间问题，而[Gemini](https://codeassist.google/) 就是其成果。其宣传重点是[平台上免费提供的补全次数](https://thenewstack.io/google-ai-coding-tool-now-free-with-90x-copilots-output/)——是 GitHub Copilot 的 90 倍——这背后体现了谷歌擅长规模化运作。这与 Gmail 在 2004 年推出时为每个用户提供比竞争对手多得多的存储空间如出一辙。

Gemini 代码助手声称支持 20 多种语言，这在规模上也是一项强大的功能。但由于谷歌没有提供自己的 IDE，因此在许多情况下，它们可能依赖于微软的 Visual Studio Code (VS Code)。我开始怀疑，正因为这个原因，JetBrains 等替代方案是否正在获得巨大的提升。然而，默认似乎是 VS Code：

![](https://cdn.thenewstack.io/media/2025/02/bf7376d1-image-1024x618.png)

你可能已经看到我如何将代码助手从 Copilot 切换到[Augment](https://thenewstack.io/augment-code-an-ai-coding-tool-for-real-development-work/)，我现在也会这样做——但这次是从 Augment 切换到 Gemini 代码助手，以便对其进行检查。

我在我的 MacBook M4 上打开了 VS Code，并立即搜索了当天新发布的扩展程序：

![](https://cdn.thenewstack.io/media/2025/02/8e92ea53-image-1-1024x431.png)

加载扩展程序似乎需要一些时间，尽管 VS Code 上没有进度指示器。当然，第一天新版本上线，服务器肯定承受了巨大的压力。

有一个欢迎页面，但没有关于设置的信息。由于我甚至没有登录 Google，它不太可能真正准备好。左侧边栏有 Gemini 图标，选择它确实会在边栏中填充登录请求。但这只是强调了我之前说过的话：在 VS Code 中，扩展程序加载代码助手的用户体验很差。

我被跳转到一个网页登录，然后返回我的 IDE，现在看到以下内容：

![](https://cdn.thenewstack.io/media/2025/02/11212858-image-2.png)

虽然侧边栏由 Gemini 控制，但我仍然不知道谁在控制代码补全。底部工具栏似乎表明它可能与 Augment 共存：

![](https://cdn.thenewstack.io/media/2025/02/631b8da9-image-3-300x33.png)

（我的 Copilot 菜单已移至顶部，即使 copilot 扩展本身表示需要重新启动。）

我禁用了 Augment 扩展程序以允许 Gemini 单独控制。但这需要微软来解决这个问题。

与此同时，谷歌需要在其扩展程序上添加警告，就像 Augment 一样。

![](https://cdn.thenewstack.io/media/2025/02/9ca850e6-image-4-1024x310.png)

和以前一样，我将对我的项目进行实际更改，并查看代码补全的行为。我的游戏项目使用随机数，但我需要从列表中获取它们，以便能够就地生成它们，或者使用预先准备好的数字集进行测试。由于在开发过程中获取数字的调用顺序可能会发生变化，我需要确保每次调用都从列表中获取固定的索引，此外还要检查我是否不会意外地两次获取相同的数字。但是，这在循环中很难管理，所以我返回一个数字块。

我发现 Gemini 做了一些糟糕的补全。它倾向于在理解上下文之前就跳转，例如：

```
...
private RN[] randomNumbers = new RN[MAXRN]; 
... 
for(short i; i < MAXRN; i++) { 
 float rnd = UnityEngine.Random.value; 
 short converted = (short)(rnd * 100); 
 randomNumbers[i] = new RN(converted, false); 
 TagDebug.Log($"We set number {i} to {rnd}"); //Line suggested by Gemini 
}
```

在上面的示例中，Gemini 建议了一行打印索引和值的日志行，但忽略了我的列表直接使用的转换为“converted”的部分。我经常发现，当我更新我的解决方案并删除旧代码时，Gemini 会建议将已删除的行放回原处。这让我想知道 Gemini 在敏捷开发中进行了多少测试，在敏捷开发中重构非常重要。

（在某个阶段，Augment 自动重新启动，卸载扩展程序也没有任何作用。只有在退出并重新打开后，Augment 才完全消失。现在，我非常清楚，我审查不同助手的情况使我更容易遇到助手冲突，但我担心，虽然审查应该关于 Gemini，但我对 VS Code 完全无法控制冲突的扩展程序感到印象深刻。）

Gemini 明智地强调使用 **command-i** 的“智能操作”，它介于代码补全和尝试为你编写大量代码之间：

![](https://cdn.thenewstack.io/media/2025/02/6a8914ea-image-5-1024x515.png)

我首先要求 Gemini 对选定的方法进行“解释”，也就是请求随机数块的地方。它大约花了 10 秒钟（相当长）才生成输出：

*“`RequestNewIndexedBlock` 方法旨在为游戏的不同部分提供一种方式，以请求并‘预留’来自 `RandomNumber` 系统的预先生成或随机生成的特定数字块。它充当这些块分配的管理器。”*

这是一个很好的总结。关键在于它使用术语“预留”识别了预留模式，而这并非基于我在代码中留下的任何提示。它还理解了“游戏的不同部分”的含义，以及数字可能是预先生成的。它还提供了一个可能过于详细的“代码分解”。

虽然该方法和整个类都能工作，但您可以看到我应该使用 `ushort`（无符号短整型）作为 `storeindex`，因为负索引没有意义。所以我尝试了第二个智能操作“修复”以查看它是否提出了这个建议：

![](https://cdn.thenewstack.io/media/2025/02/e4f7f1ba-image-6-1024x105.png)

告诉我们在现阶段要谨慎对待生成的代码，这有点像告诉爱丽丝，沿着兔子洞进入仙境可能会产生不可预测的结果！

按照惯例，它创建了一个临时差异文件。结果表明对块进行了多余的检查，虽然从技术上讲是正确的，但依赖于对另一个类的内部结构的假设。如果有什么不同的话，它确实让我减少了对 `RNBlock` 的访问，所以这间接地是好的。令人费解的是，由于临时文件不是项目的一部分，Copilot 试图提出建议！我之前关于 VS Code 如何处理扩展的评论涵盖了这一点。

最后，我让它尝试对该方法进行最终的智能操作“生成单元测试”。我在项目中有一个单独的程序集，其中包含测试和模拟库 (Moq)，尽管我没有为此类编写任何测试——而且我不确定 Gemini 是否可以看到这些。浏览代码，您可以看到有两个案例需要测试，因为我为它们抛出了异常。

它在预先准备好的集合和生成的随机集合中都很好地创建了设置和拆卸。对于主要的正常路径，测试足够合理：

```
[Test] public void RequestNewIndexedBlock_ValidIndex_ReturnsBlockAndMarksAsTaken() 
{ 
  // Arrange 
  RandomNumber rng = RandomNumber.GetActiveRandomNumber(); 
  short validIndex = 5; 
 
  // Act 
  RandomNumber.RNBlock block = rng.RequestNewIndexedBlock(validIndex);
 
  // Assert 
  Assert.IsNotNull(block); 
  Assert.AreEqual(validIndex, block.storeindex); 
  Assert.IsTrue(block.taken); 
}
```

**结论**

我已经非常清楚地表达了我对 VS Code 无法处理多个扩展争用相同 LLM 功能的担忧，但 Gemini Code Assist 必须在帮助用户禁用以前的扩展方面做得更好。

关于 Gemini Code Assist，唯一让我担心的是代码完成的速度，有时会稍微迟缓一些。在代码重构期间，任何[代码助手](https://thenewstack.io/top-dev-tools-and-web-developer-trends-of-2024/)都不能确定哪些代码部分不再是新解决方案的一部分。但我总体感觉 Gemini 跟不上我的节奏——尽管代码解释很精确。

代码完成的质量总体还可以——尽管在我最近的测试中，Copilot 和 Augment 给我的结果更好。但您的里程可能会有所不同，我毫不怀疑扩展足够的处理时间可能是一个问题。此外，如果有一件事我们知道，那就是 LLM 输出只会随着时间的推移而改进。
