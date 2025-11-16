<!--
title: Visual Studio 2026 首曝：演进而非颠覆
cover: https://cdn.thenewstack.io/media/2025/11/f07cdb96-johannes-plenio-awdgqexsxa0-unsplash.jpg
summary: Visual Studio 2026 Insider版发布，深度集成Copilot。UI改进有限，AI测试功能对代码覆盖率提升不大。兼容Win10，是渐进式更新而非革命。
-->

Visual Studio 2026 Insider版发布，深度集成Copilot。UI改进有限，AI测试功能对代码覆盖率提升不大。兼容Win10，是渐进式更新而非革命。

> 译自：[Visual Studio 2026 First Look: Evolution, Not Revolution](https://thenewstack.io/visual-studio-2026-first-look-evolution-not-revolution/)
> 
> 作者：David Eastman

我从未完全理解微软的路线图。我当然很喜欢使用 Visual Studio 2022 (VS 2022) 进行 C# 和 .NET 开发，但当它对 Mac 用户停止支持（取而代之的是 Mac 版 VS Code）时，我曾以为我们很快都会使用 Visual Studio Code——甚至在 PC 上也是如此。就目前而言，VS Code 很好用，但它感觉像一个需要你自己搭建的乐高解决方案。例如，它开箱即用时并没有一个简单的“构建”按钮。

我也不知道我是否有许可证——我想是有的，但也许那是 Office 的。或者可能是专业版。又或者我正在运行社区版。我不记得了。微软一直都懂得如何与他们众多的企业客户沟通，但与个人开发者的沟通则较少。

> 微软将这次深度集成 Copilot 的发布称为第一个**智能开发环境**（IDE），以应对人工智能的旋风。

我所知道的是，[Visual Studio 2026](https://visualstudio.microsoft.com/insiders/) 现在可以通过其测试版构建渠道“Insiders”获取了。我之前使用过 [Insiders](https://thenewstack.io/tutorial-set-up-an-mcp-server-with-net-and-github-copilot/)，它与我当前的旧版本并行安装，没有发生任何问题。对于像 Visual Studio 这样我们许多人赖以生存的关键工具，没有革命——只有演进。微软将这次深度集成 Copilot 的发布称为第一个**智能开发环境**（IDE），以应对人工智能的旋风。我在这里感受到了一丝戏谑；过去一年里，许多平台都借 AI 之名进行了大规模更名。

在这篇文章中，我将主要检查基础工作，让开发者有信心亲自尝试（或不尝试）它。但我期待它能更快，并与 Copilot 有更深度的 AI 集成（无论我是否需要）；此外，我还听说用户界面更清晰了。我还听说它能在“已死”的 Windows 10 上运行，而这正是我的当前 PC 开发环境所在——所以我很想验证这一点。

## 安装 Visual Studio 2026 Insider 构建版

所以我们将在我的 Windows 10 PC 上进行安装。值得注意的是，2022 和 2026 之间的图标设计略有不同，这样你就不会混淆这两个版本了。当我开始安装时，问题随之而来，但都很简短：

[![](https://cdn.thenewstack.io/media/2025/11/be6dd358-image.png)](https://cdn.thenewstack.io/media/2025/11/be6dd358-image.png)

他们明确表示会正确识别扩展，以及那些可能已停止支持的项目。我使用带有 Unity 扩展的 VS 2022，并且我确认它是社区版：

[![](https://cdn.thenewstack.io/media/2025/11/55db3363-image-1.png)](https://cdn.thenewstack.io/media/2025/11/55db3363-image-1.png)

我的电子邮件似乎足以让微软确认我的身份，但它也要求提供 GitHub（用于 Copilot），GitHub 强制执行完整的两步验证。这是它必须安装的内容：

[![](https://cdn.thenewstack.io/media/2025/11/c20a681a-image-2.png)](https://cdn.thenewstack.io/media/2025/11/c20a681a-image-2.png)

所以当我们最终启动应用程序，加载一个已知且受管理的项目时，屏幕看起来是这样的：

[![](https://cdn.thenewstack.io/media/2025/11/58706ad0-image-3-1024x568.png)](https://cdn.thenewstack.io/media/2025/11/58706ad0-image-3-1024x568.png)

首先，我使用深色主题，并且默认情况下我不会让 Copilot 显示在右侧窗格中。在我切换到 Unity 项目窗格之前，我问 Copilot：“如何设置深色模式？”它给出了很多答案。很快，我们就搞定了。虽然没有“直接做”的选项，但它确实提供了一个脚本。它还提供了 2026 版本的截图，所以至少它确定知道版本号。

## 用户界面增强功能一览

选择后，新文件很快就被加载到编辑器中。用户界面 (UI) 稍微清晰了一些——比较一下顶部窗格的新版本……

[![](https://cdn.thenewstack.io/media/2025/11/d1d32e9e-image-4.png)](https://cdn.thenewstack.io/media/2025/11/d1d32e9e-image-4.png)

……与下面的旧版本。布局相同，但旧版本使用实心文件夹。除此之外，差别不大。

[![](https://cdn.thenewstack.io/media/2025/11/a8194fcb-image-5.png)](https://cdn.thenewstack.io/media/2025/11/a8194fcb-image-5.png)

项目在大约 8.5 秒内构建完成，这可能是在没有缓存帮助的情况下完成的。

## 测试 Copilot 的 AI 功能

正如你所期望的，微软的 Copilot 是 VS 中默认的 AI 呈现方式。现在，VS 肯定不适用于**氛围编程**，但在最近使用了这么多优秀的 Agentic CLI 之后，ChatGPT 风格的帮助感觉有点过时了。

然而，代码补全是我日常编码中 AI 的主要用途。在 VS 2026 中，它们似乎更流畅了一些——也许行补全更快，建议的代码也稍微不那么强硬。但我需要更多时间来妥善评估这一点。

我在加载的项目中确实有糟糕的代码覆盖率 (49%)，所以我很乐意让 Copilot 创建额外的测试，看看它是否能提高覆盖率。我将选择一个我最近注入了更多功能的类区域：

[![](https://cdn.thenewstack.io/media/2025/11/7e584cc6-image-6-1024x26.png)](https://cdn.thenewstack.io/media/2025/11/7e584cc6-image-6-1024x26.png)

（对于那些无法猜测覆盖率报告中各列含义的人来说，有 138 行代码被覆盖，232 行未被覆盖，这给了我们 37% 的覆盖率。因此，虽然我不相信完全将测试交给大型语言模型，但我们可以让它提出建议。我还有一个 Mock 框架。

[![](https://cdn.thenewstack.io/media/2025/11/33bccad5-image-7.png)](https://cdn.thenewstack.io/media/2025/11/33bccad5-image-7.png)

正如它所说，这使用的是 GPT-5 mini。我本可以切换到 Claude Haiku。运行后，它创建了一个额外的测试夹具：

[![](https://cdn.thenewstack.io/media/2025/11/adcfca40-image-8.png)](https://cdn.thenewstack.io/media/2025/11/adcfca40-image-8.png)

我必须自己添加新的测试，这在使用为我完成此操作的代理工具之后，感觉有点令人失望。所使用的风格与我的相似，需要时会使用 Mocks。在这个例子中，唯一有点奇怪的是冗长的方法名：

```
[Test] public void FetchRoadPoint_ReturnsAssociatedRoadPoint() { 
  var locMock = new Mock<LightweightLocation>(); 
  var locObj = locMock.Object; var mp = new MapPosition(new System.Numerics.Vector2(0, 0), MapPosition.LocTypeCue.None); 
  mp.trackId = 1; 
  RoadPoint rp = ss.RegisterRoadPoint(mp, 0, 0); 
  ss.RegisterAssociation(rp, locObj); 
  RoadPoint found = ss.FetchRoadPoint(locObj); 

  Assert.AreEqual(rp, found); 
}
```

代码构建成功，所以我通过 Unity（这是预期的目标）运行测试。

新夹具中的所有测试都运行了：

[![](https://cdn.thenewstack.io/media/2025/11/ccef77ea-image-9.png)](https://cdn.thenewstack.io/media/2025/11/ccef77ea-image-9.png)

不幸的是，它们对代码覆盖率没有产生任何显著影响：

[![](https://cdn.thenewstack.io/media/2025/11/d090365d-image-10-1024x35.png)](https://cdn.thenewstack.io/media/2025/11/d090365d-image-10-1024x35.png)

所以它只覆盖了额外的三行！我完全承认，由于我是从 Unity 运行测试的，即使是代理运行任务也无法通过 Visual Studio 轻松改进这一点。它可能选择覆盖直接指向其他结构的方法，这无助于覆盖调用类。

也许对任务进行更好的分析（覆盖率报告是可以访问的）会有所帮助，但我们知道还有其他专门创建测试的应用程序。通过只创建代码模板，我可以添加我自己的测试；实际上，我会发现这更有用。

## 结论：向前迈出的进化一步

Visual Studio 还有很多我在这里没有提及的功能，例如 [使用 Copilot 进行性能分析](https://devblogs.microsoft.com/visualstudio/copilot-profiler-agent-visual-studio/)。我可以看到我对 Unity 的扩展得到了完全的尊重，并且我现有的项目立即顺利构建完成。如果你正在使用 Visual Studio 2022，那么几乎没有理由不尝试这个版本——但请期待演进，而非革命。