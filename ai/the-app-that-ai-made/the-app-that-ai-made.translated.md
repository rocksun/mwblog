**我用一种我不熟悉的语言和框架制作了多模态多功能移动应用程序 [CrayEye](https://www.crayeye.com)，我依靠现代大型语言模型来编写代码，而不仅仅是代码片段，而是全部代码。虽然我后来手动进行了一些微小的调整（例如更改元素颜色或交换元素位置），但 LLM 完成了所有早期和繁重的工作。**

**为了完成这项练习，我通过网络 UI 使用了向我提供的最新最先进的模型：**

- OpenAI 的 [GPT-4](https://cdn.openai.com/papers/GPTV_System_Card.pdf)
- Anthropic 的 [Claude 3 Opus](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)
- Google 的 [Gemini Advanced](https://support.google.com/gemini/answer/14517446?hl=en&co=GENIE.Platform%3DAndroid)

**自 [GPT-4V](https://openai.com/research/gpt-4v-system-card) 的早期预发布演示以来，人们的想象力就开始活跃起来，我们能够用它构建哪些神奇的新事物。该技术对基于视觉的用户体验的影响不容小觑 - 曾经需要一个专门的专家团队花费大量时间和资源的事情，现在可以通过对多模态 LLM 的简单调用以更高的熟练度和细节来完成。我想探索它们的能力，而无需为每个想法启动 create-react-app 或 create-next-app 前端，并真正探索 [Ethan Mollick](https://www.oneusefulthing.org/) 所说的 [锯齿状前沿](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)（即这项技术能够和不能够做什么之间的界限，即使在看似相邻或可比较的领域和任务中，这种界限也可能迅速发生变化）。**

**我的要求主要有：**

- 用于捕获输入的快速界面
- 能够以最小的摩擦使用所有摄像头
- 可以编辑和共享的可配置提示
- 将车载传感器数据（例如位置）纳入提示

**我决定创建一个应用程序。自从我创建原生应用程序以来已经有一段时间了，我一直想再次尝试一下，而这种多模态多功能工具的用例提供了绝佳的机会。**

**自从我上次尝试制作原生应用程序以来，[Flutter](https://flutter.dev/) 的受欢迎程度有所提高，所以我决定尝试一下，尽管我之前没有使用过 [Dart](https://dart.dev/)。我对这门语言的不熟悉实际上在这里很有用，因为我想涉足的另一件事是测试当今 LLM 在整体开发方面的能力。**

**我按照 [Flutter 文档](https://flutter.dev/learn) 设置 [iOS 的 Flutter 开发工具](https://docs.flutter.dev/get-started/install/macos/mobile-ios?tab=download) 并启动 flutter create 来开始。**

**此时，样板应用程序的核心逻辑完全包含在 lib/main.dart 中 - 这使得立即开始工作变得特别容易。我开始提示添加简单的功能 - 相机预览、远程 HTTP 请求以通过 GPT 分析图像，并且应用程序的功能（和代码行）开始迅速增长。我的提示主要依赖于请求：**

“在这些更改后，完整修改的文件，没有截断”

**这一点至关重要，因为我想减少 LLM 和磁盘之间传输响应的摩擦，并确保它在生成响应时完全明确地考虑了与代码其余部分相关的上下文中的更改区域。我的证据纯粹是轶事，但它通常似乎比让它传递对文件部分部分的补丁更新产生更高质量的结果，并且回归问题更少。**

**在我对一个最小功能 POC 的 [初始提交 (76841ef)](https://github.com/alexdredmon/crayeye/commit/76841ef2a105817d7062baf5055147bd8842a27c) 之后不久，我让 LLM 执行 [模块化重构 (6247975)](https://github.com/alexdredmon/crayeye/commit/624797532388cd24e46041f97914378fcc15bcf2) 以将内容拆分为单独的文件。从最佳实践和工作流性能的角度来看，这很有帮助，因为我无需等待它输出更模块化拆分的文件的较小块。**

**现在，当将代码库传递给 LLM 时，由于内容位于单独的模块中，我需要区分不同的文件/模块。此时，我在每个文件开头添加了包含其名称的注释，并在末尾添加了 // eof 注释。我的提示看起来像这样：**

您是一个软件开发团队。如果没有提供代码库，请索要代码库，并围绕此代码库进行所有更改。在提供代码库时，除非请求了新功能，否则仅回复“我已进入”。
// FILENAME

// User will request a feature - first respond with the file(s) that need to change, then a brief summary of the changes. Only output the files that need to change in order to implement the current feature. When you output a file, first output the filename of the file you are updating, then output the entire file, untruncated, after the edit. Do not remove any comments. Make sure the first line of each file is "// FILENAME" where "FILENAME" is the filename of the file, and the last line of each file is "// eof" - most importantly, make sure to wrap each file in three backticks "```" so that they will be fully formatted as code.

Here is my codebase:
By keeping the prompt in the lib directory, and starting it with an underscore (specifically lib/_autodev_prompt.txt) to ensure it floats to the top of the sorted file list, I can easily cat lib/* | pbcopy and use my prompt with my entire codebase, separated by filename identifiers, for pasting into my LLM of choice. The ones I have been running are:
- OpenAI's [GPT-4](https://cdn.openai.com/papers/GPTV_System_Card.pdf)
- Anthropic's [Claude Opus](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)
- Google's [Gemini Advanced](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/#gemini-15)
I have found that different providers are better at different things. Anthropic's Claude is great for copy-paste workflows, automatically collapsing large pastes into an attachment-style interface. ChatGPT and Gemnini neither collapse nor automatically format code inputs, resulting in a UX that is a bit messy to start with:
Gemini renders almost identically, though it also eventually hits a character count limit of around 31,000 characters. Once the app gets going, this will be very limiting.
Gemini also seems to be very eager to suggest changes before any feature has been requested, though this can be somewhat mitigated by tweaking the prompt.
Claude generally seems to be the most compliant with the prompt I give it, able to produce complete changes without introducing regressions, and correctly responding to "I add" at the beginning without diving into unrequested changes. This seems to be less true the larger the codebase gets - I ended up adding another reminder to the end of my prompt in later requests:
I often start to hit Claude's message throttling, which resets every ~8 hours - this became my primary bottleneck as features accumulated and the codebase grew. Claude 3 Opus proved to be the absolute champ at consistently generating complete, untruncated files and changes, with few to no errors or regressions.
Eventually, the codebase got large enough that even Claude Opus would start suggesting changes before any feature had been described, just like Gemini did. The context window or at least the size of the prompt seems to be the culprit here, as it always happens above a certain line/character count.
In [autodev prompt tweaks (5539cfb)](https://github.com/alexdredmon/crayeye/commit/5539cfb428770785779f3ba78599ed5972cb1e93), I ended up splitting the prompt into two parts - a [before](https://github.com/alexdredmon/crayeye/blob/5539cfb428770785779f3ba78599ed5972cb1e93/flutter/lib/_autodev_prompt.txt) prompt and an [after](https://github.com/alexdredmon/crayeye/blob/5539cfb428770785779f3ba78599ed5972cb1e93/flutter/lib/z_autodev_prompt_end.txt) prompt, with the codebase sandwiched in the middle. This seems to have solved the problem of suggested changes before a feature is requested, and ensures that the "complete the file after these changes, no truncation" rule is followed more consistently.
With the sandwich prompt in place, it was off to the races again - rapid iteration became easy once more, and feature requests were quickly turning into code.
The MVP allowed me to add/edit prompts for inserting location data, and the results were very usable and useful:
It supports interpolating the user's location values using the tokens {location.lat}, {location.long}, and {location.orienation} to represent their current latitude, longitude, and north/south/east/west orientation at the time the prompt was executed.
I initially thought I might need to use an API call to interpret the user's neighborhood based on their lat/long, like I do for [WhatsMyHood](https://whatsmyhood.com/), but it turns out that just providing the raw values to the LLM is enough - it is able to determine what neighborhood you are in just as well as Google Maps' API.
There is room for improvement, such as improving the cramped "add/edit prompt" dialog, but I can easily manage and share my prompts and test them in the field - even saving my favorite responses.
I am ready to share my app. I prepared to test on Android and submit to the Google Play Store and Apple App Store. That's when I hit my first major roadblock - in setting
[Android 开发工具](https://docs.flutter.dev/get-started/install/macos/mobile-android?tab=download)

我启动了 Flutter 模拟器，并尝试在 Android 模拟器上运行我的应用。结果不行 - 事实证明，我使用的几个软件包与我的目标 Android SDK 版本不兼容。在多次尝试让 LLM 正确解决问题后，我终于找到了一个解决方案，包括 [删除一个依赖项 (f18c8b2)](https://github.com/alexdredmon/crayeye/commit/f18c8b2e276f12b21f7e586f46d7581e34ceb1ed)（这样做后，支持提示中的 `{location.orientation}` 插值值）。

- 得益于现代 LLM 的力量倍增器，我能够快速制作一个功能完备的跨平台 MVP，而无需付出太多努力/投入 - 初始 MVP 花费了大约 10 小时的人工工作/投入。
- 对于我的目的，Claude Opus 3 始终如一地生成功能代码，且没有回归，做得最好
- Gemini 只能构建大约 31k 字符（包括所有提示）的应用
- ChatGPT 最容易引入回归错误或忽略指令，输出不完整、未截断的文件
- 业务限制超过了技术限制（即 Anthropic 消息节流、最初的 App Store 拒绝）
- 该工作流程显然可以进一步自动化，特别是使用自主代理（例如 Autogen）来编写和测试更改，而人类仅参与需求输入和验收标准验证。
- 对于大型项目来说，代码搜索以及映射/使用代码映射或文档的功能非常理想
- 虽然 MVP 花费了大约 10 小时的动手输入/工作，但由于 Claude 3 Opus 的消息上限，这些工作分散在多天/周末。通过使用 API 而不是 Web UI 或以其他方式规避消息上限，可以缩短交付时间表。

大型语言模型在用于生成代码时，可以被概念化为用于开发的最新高级语言 - 就像 Python 的存在并没有取代所有 C 语言开发一样，LLM 也不一定能完全消除低级语言开发 - 即使它不可否认地加速了在所述低级开发中执行的能力。

然而，它们确实占据了很大一部分 - 现代基础 LLM 可以独家处理惊人地大且不断增长的用例百分比，*今天*这个数字只会上升。

关注我：