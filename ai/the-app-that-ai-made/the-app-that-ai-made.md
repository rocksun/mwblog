
<!--
title: 用AI制作应用
cover: https://alexredmon.com/api/og?post=the-app-that-ai-made&title=The%20app%20that%20A.I.%20made
-->

我用一种我不熟悉的语言和框架制作了多模态多功能移动应用程序 [CrayEye](https://www.crayeye.com)，我依靠现代大语言模型来编写代码，而不仅仅是代码片段，而是全部代码。虽然我后来手动进行了一些微小的调整（例如更改元素颜色或交换元素位置），但 LLM 完成了所有早期和繁重的工作。

> 译自 [The app that A.I. made | blog | alexandria redmon](https://alexredmon.com/blog/the-app-that-ai-made)，作者 alexandria redmon

为了完成这项练习，我通过网络 UI 使用了向我提供的最新最先进的模型：

- OpenAI 的 [GPT-4](https://cdn.openai.com/papers/GPTV_System_Card.pdf)
- Anthropic 的 [Claude 3 Opus](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)
- Google 的 [Gemini Advanced](https://support.google.com/gemini/answer/14517446?hl=en&co=GENIE.Platform%3DAndroid)

## 如何开始

自 [GPT-4V](https://openai.com/research/gpt-4v-system-card) 的早期预发布演示以来，人们的想象力就开始活跃起来，我们能够用它构建哪些神奇的新事物。该技术对基于视觉的用户体验的影响不容小觑 - 曾经需要一个专门的专家团队花费大量时间和资源的事情，现在可以通过对多模态 LLM 的简单调用以更高的熟练度和细节来完成。我想探索它们的能力，而无需为每个想法启动 create-react-app 或 create-next-app 前端，并真正探索 [Ethan Mollick](https://www.oneusefulthing.org/) 所说的[锯齿状前沿](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)即这项技术能够和不能够做什么之间的界限，即使在看似相邻或可比较的领域和任务中，这种界限也可能迅速发生变化）。

## 多功能工具

我的要求主要有：

- 用于捕获输入的快速界面
- 能够以最小的摩擦使用所有摄像头
- 可以编辑和共享的可配置提示
- 将车载传感器数据（例如位置）纳入提示

我决定创建一个应用程序。自从我创建原生应用程序以来已经有一段时间了，我一直想再次尝试一下，而这种多模态多功能工具的用例提供了绝佳的机会。

自从我上次尝试制作原生应用程序以来，[Flutter](https://flutter.dev/) 的受欢迎程度有所提高，所以我决定尝试一下，尽管我之前没有使用过 [Dart](https://dart.dev/)。我对这门语言的不熟悉实际上在这里很有用，因为我想涉足的另一件事是测试当今 LLM 在整体开发方面的能力。

## 轮胎路面相遇

我按照 [Flutter 文档](https://flutter.dev/learn) 设置 [iOS 的 Flutter 开发工具](https://docs.flutter.dev/get-started/install/macos/mobile-ios?tab=download) 并启动 flutter create 来开始。此时，样板应用程序的核心逻辑完全包含在 lib/main.dart 中 - 这使得立即开始工作变得特别容易。我开始提示添加简单的功能 - 相机预览、远程 HTTP 请求以通过 GPT 分析图像，并且应用程序的功能（和代码行）开始迅速增长。我的提示主要依赖于请求：

> “在这些更改后，完整修改的文件，没有截断”
> "the complete modified files after these changes with no truncation"

这一点至关重要，因为我想减少 LLM 和磁盘之间传输响应的摩擦，并确保它在生成响应时完全明确地考虑了与代码其余部分相关的上下文中的更改区域。我的证据纯粹是轶事，但它通常似乎比让它传递对文件部分部分的补丁更新产生更高质量的结果，并且回归问题更少。

![](https://www.alexandriaredmon.com/img/blog/the-app-that-ai-made/claude-1.jpg)

在我对一个最小功能 POC 的 [初始提交 (76841ef)](https://github.com/alexdredmon/crayeye/commit/76841ef2a105817d7062baf5055147bd8842a27c) 之后不久，我让 LLM 执行 [模块化重构 (6247975)](https://github.com/alexdredmon/crayeye/commit/624797532388cd24e46041f97914378fcc15bcf2) 以将内容拆分为单独的文件。从最佳实践和工作流性能的角度来看，这很有帮助，因为我无需等待它输出更模块化拆分的文件的较小块。

现在，当将代码库传递给 LLM 时，由于内容位于单独的模块中，我需要区分不同的文件/模块。此时，我在每个文件开头添加了包含其名称的注释，并在末尾添加了 // eof 注释。我的提示看起来像这样：

```
You are a software development team. Ask for the codebase if not provided, and base all your changes around this codebase. When provided with the codebase, reply only with "I'm in" unless a new feature has been requested.

The user will ask for features - respond first with the files that need to be changed followed by a brief summary of the changes. Only output files that require changes to implement the current feature. When you output the files, begin with the filename of the file being updated and then output the entire un-truncated file after modifications. Do not remove any comments. Ensure that the first line of each file is "// FILENAME" where "FILENAME" is the file's name, and that the last line of each file is "// eof" - and most importantly, make sure to surround each file with triple backticks "```" so that they will be entirely formatted as code.

Here's my codebase:
```

在 lib 目录中将提示文本另存为带有前缀 _（具体而言为 lib/_autodev_prompt.txt）以确保它浮动在文件排序列表顶部，我可以轻松使用 cat lib/* | pbcopy 将提示文本与我的整个代码库放在一起，通过文件名标识符分隔，以便粘贴到我选择的 LLM 中。正在运行的是：

- OpenAI 的 [GPT-4](https://cdn.openai.com/papers/GPTV_System_Card.pdf)
- Anthropic 的 [Claude 3 Opus](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)
- Google 的 [Gemini Advanced](https://support.google.com/gemini/answer/14517446?hl=en&co=GENIE.Platform%3DAndroid)

### 烘培

我发现各个提供商在不同方面表现出色。Anthropic's Claude 完全适用于复制粘贴工作流，会自动将一大段粘贴内容压缩成附件样式的界面。ChatGPT 和 Gemnini 在输入代码时既不会压缩也不会自动格式化代码，这会导致用户界面一开始就有点混乱：

![](https://www.alexandriaredmon.com/img/blog/the-app-that-ai-made/gpt4-1.jpg)

Gemini 的渲染几乎完全相同，尽管它最终也遇到了大约 31,000 个字符的字符计数限制。一旦应用程序发布，这将非常局限。

![](https://www.alexandriaredmon.com/img/blog/the-app-that-ai-made/gemini-1.jpg)

Gemini 似乎总是热衷于在尚未提出任何功能需求之前就建议更改，尽管稍加调整提示可以避免这种情况。

![](https://www.alexandriaredmon.com/img/blog/the-app-that-ai-made/gemini-2.jpg)

Claude 通常会在给定提示的情况下尽最大努力完成更改，而不会引入回归问题，并且在开始时会正确地回答“我在”，而不是进行未请求的更改。代码库越大，这种情况就越少见 - 我最终在以后的请求中在我的提示末尾添加了另一个提醒：

![](https://www.alexandriaredmon.com/img/blog/the-app-that-ai-made/claude-2.jpg)

我经常开始撞上 Claude 消息限制，它每隔大约 8 小时会重置一次 - 这成了我的主要瓶颈，因为这些功能积累起来且代码库在不断增长。事实证明，Claude 3 Opus 无疑是冠军，能够持续产生完整的文件和修改，很少或没有错误或退步。

最终，代码库增长到足以让 Claude Opus 在任何功能被描述之前就开始提出修改建议，就像 Gemini 所做的那样。这似乎是上下文窗口或至少是提示的大小，因为这会在超过一定行/字符计数时持续发生。

在 autodev 的 prompt 调整 (5539cfb) 中，我终于将 prompt 分成了两部分——在代码库前后加入提示。这似乎解决了在功能被请求之前就提出更改的问题，并且确保了更一致地遵守“在这些更改后完整该文件，但不截断”的规则。

有了三明治提示，我又出发了——快速迭代再次变得轻松，功能请求也很快变成了代码。

## 最小可行产品 

### 优点 

MVP 使我能够添加/编辑提示，并插入位置数据，结果非常可用且有用：

![](https://www.alexandriaredmon.com/img/blog/the-app-that-ai-made/iphone-triple.jpg?v=3)


我启动了 Flutter 模拟器，并尝试在 Android 模拟器上运行我的应用。结果不行 - 事实证明，我使用的几个软件包与我的目标 Android SDK 版本不兼容。在多次尝试让 LLM 正确解决问题后，我终于找到了一个解决方案，包括 [删除一个依赖项 (f18c8b2)](https://github.com/alexdredmon/crayeye/commit/f18c8b2e276f12b21f7e586f46d7581e34ceb1ed)（这样做后，支持提示中的 `{location.orientation}` 插值值）。

该工具支持使用标记 {location.lat}、{location.long} 和 {location.orienation} 插值用户的位置值，以表示他们在执行提示时的当前纬度、经度和北/南/东/西方向。我最初认为我可能需要像在 WhatsMyHood 中那样使用 API 调用来根据用户的纬度/经度来解释用户的街区，但事实证明，仅向 LLM 提供原始值就足够了 - 它能够像 Google 地图的 API 一样判断您所在街区.

有一些需要改进的地方，例如改进局促的“添加/编辑提示”对话框，但我可以轻松地管理和分享我的提示并在现场对其进行测试 - 甚至保存我的常用回复。

### 缺点

我已经准备好了分享我的应用程序。我准备在 Android 上进行测试并将其提交到 Google Play 商店和 Apple App Store。那时我第一次遇到第一个重大挫折 - 在设置 [Android 开发工具](https://docs.flutter.dev/get-started/install/macos/mobile-android?tab=download)后，我启动了 Flutter 模拟器并尝试在我的安卓模拟器上运行我的应用。这不行 - 结果证明我使用的几个软件包与我的目标 Android SDK 版本不兼容，经过几次尝试让 LLM 正确解决后，我终于找到了一个解决方案，涉及[删除一个依赖项 (f18c8b2)](https://github.com/alexdredmon/crayeye/commit/f18c8b2e276f12b21f7e586f46d7581e34ceb1ed) （这样做会移除提示中对 {location.orientation} 插值值的支持）。

## 总结

**优势**

- 得益于现代 LLM 的力量倍增器，我能够快速制作一个功能完备的跨平台 MVP，而无需付出太多努力/投入 - 初始 MVP 花费了大约 10 小时的人工工作/投入。
- 对于我的目的，Claude Opus 3 始终如一地生成功能代码，且没有回归，做得最好

**限制**

- Gemini 只能构建大约 31k 字符（包括所有提示）的应用
- ChatGPT 最容易引入回归错误或忽略指令，输出不完整、未截断的文件
- 业务限制超过了技术限制（即 Anthropic 消息节流、最初的 App Store 拒绝）

**需要改进的地方**

- 该工作流程显然可以进一步自动化，特别是使用自主代理（例如 Autogen）来编写和测试更改，而人类仅参与需求输入和验收标准验证。
- 对于大型项目来说，代码搜索以及映射/使用代码映射或文档的功能非常理想
- 虽然 MVP 花费了大约 10 小时的动手输入/工作，但由于 Claude 3 Opus 的消息上限，这些工作分散在多天/周末。通过使用 API 而不是 Web UI 或以其他方式规避消息上限，可以缩短交付时间表。

**更高级的语言**

大语言模型在用于生成代码时，可以被概念化为用于开发的最新高级语言 - 就像 Python 的存在并没有取代所有 C 语言开发一样，LLM 也不一定能完全消除低级语言开发 - 即使它不可否认地加速了在所述低级开发中执行的能力。

然而，它们确实占据了很大一部分 - 现代基础 LLM 可以独家处理惊人地大且不断增长的用例百分比，*今天*这个数字只会上升。
