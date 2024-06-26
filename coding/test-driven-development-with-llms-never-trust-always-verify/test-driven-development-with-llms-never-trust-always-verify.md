# 使用 LLM 进行测试驱动开发：永不相信，始终验证

Jon Udell 发现,先编写测试可以帮助保持 LLM 助手的进度，随着他在软件开发中继续探索 LLM，他得出了这个结论。

译自 [Test-Driven Development with LLMs: Never Trust, Always Verify](https://thenewstack.io/test-driven-development-with-llms-never-trust-always-verify/) 。

![](https://cdn.thenewstack.io/media/2023/08/565425b0-arseny-togulev-meckpokjyjm-unsplash-1024x576.jpg)
*图片来自 Unsplash*

作为 [Steampipe](https://steampipe.io/) 的社区负责人，我一直想要一种更好的方式来可视化项目活动。自从我大约两年前加入以来，[插件](https://hub.steampipe.io/plugins)套件已经从 42 个增长到 136 个，现有的插件也在不断地使用新的表、增强功能和错误修复进行更新。所有这些更新都出现在社区 Slack 频道和社交媒体上，但我一直想要每月或每季度自动总结这些变更。原始信息存在于 GitHub 变更日志中，日志采用一致的样式编写，因此从理论上讲，从日志中提取结构化数据应该很简单——但是像往常一样，魔鬼藏在细节中。编写正则表达式以匹配日志中的模式是一项艰巨的任务，我一直在拖延。由于 LLM 在本质上是模式匹配器，我认为它们可以帮助我更轻松快捷地完成这项工作。

为了这个练习，我从一个[详细的提示](https://gist.github.com/judell/3a58ae45f50f9cf03219258718f2f3f0)开始，其中包含样本数据，指定要在数据中识别的模式，并提供可以在测试中使用的样本输出，这些测试将证明脚本的工作符合预期。提示以这个雄心勃勃的目标结束:

> 编写一个脚本来处理 sample_data.py 中的数据，并编写测试以证明它生成这些输出。

这过于雄心勃勃了。尽管我听说基于详细规范的成功的整程序合成的故事，但我还没能实现它。ChatGPT、Sourcegraph Cody、GitHub Copilot Chat 和我第一次试用的 [smol developer](https://github.com/smol-ai/developer) 都提出了有用的引导解决方案，然后这个练习变成了现在已熟悉的(并且有用的!)[与橡皮鸭的对话](https://blog.jonudell.net/2023/05/24/when-the-rubber-duck-talks-back/)。我自己编写了测试，出现的解决方案能够通过测试，而且确实比没有 LLM 辅助来得更容易。但我对代码不满意，也不觉得我已经充分利用了 LLM，所以我重新开始，采用不同的策略:

> 编写测试，要求 LLM 编写通过测试的函数。

我不确定我们为什么甚至期望 LLM 将详细的规范作为输入，并在一次操作中生成整个程序作为输出。人类程序员不会这样工作。即使 LLM 可以，我们会想要它们这样做吗？毕竟，目标不仅是创建可以工作的软件(可证明)，还可以被参与创建它的人机合作理解、维护和发展的软件。保持人类在循环中的最佳方法是什么？

对于重新启动，我专注于问题的最棘手部分：正则表达式。对于每个模式(添加新表、增强功能、错误修复、贡献者)，我想要一个可以匹配该模式并通过针对样本数据的测试的函数。长期以来，我的做法是将复杂的正则表达式分解为更简单的步骤，这样我可以单独理解和测试它们。这是一种可靠的方法，但它缓慢和笨拙。如果机器可以快速编写复杂的正则表达式并通过测试，我很乐意外包这项任务 —— 尤其是如果它们可以解释自己的工作。这里是匹配“增强功能”或“错误修复”部分的正则表达式之一。

```python
rf"{re.escape(section_name)}\s*\n((?:-\s[^\n]*(?:\n(?!\s*-).*)*\n)+)"
```

以下是一系列解释。

![LLM 对复杂正则表达式的合唱式解释](https://cdn.thenewstack.io/media/2023/08/eb38369c-choral-regex-explanations-1024x807.png)

我不会想深入研究这个正则表达式，但如果需要，我会感谢这些解释，并考虑所有解释。

LLM 能够产生更简单的正则表达式，使我更易于理解和修改，而仍然通过测试吗？我给了它们很大压力，但到目前为止，没有一个给出了一个更简单的工作版本。因此，目前我愿意接受一个权衡：开发我难以理解的正则表达式的速度更快，但我可以对其进行测试。总感觉掌握正则表达式是外星智慧的工作，现在我们有了它们，我很高兴能把人类智慧用在其他地方。

## 迭代的测试驱动开发

配备代码解释器插件的 ChatGPT 目前是迭代生成受测试约束的函数的黄金标准。在“[大型语言模型如何协助网站改版](https://thenewstack.io/how-large-language-models-assisted-a-website-makeover/)”一文中，我报告了代码解释器的首次成功使用。我的语气可能有点过于事实，我对 LLM 宣传的反击很敏感，我的目标是这里采取中立的立场和关键的客观性。但让我们现实点：能够在目标导向的自主循环中运行 LLM 是一项惊人的突破——仍处于初级阶段，但可能是使 LLM 可靠再现地用于编程的一种方式。

到目前为止，我还没有成功地试图用 Cody 和 Copilot 来模拟这种效果。我可以要求它们编写一个通过测试的函数，给它们通过的测试，并将测试失败反馈给它们，但用这种方法我还没有得到一个成功的结果。这真的是个遗憾，因为与 ChatGPT 相比，Cody和 Copilot 有一个关键优势：它们是本地的，可以看到你的文件，而且你可以以不需要将所有内容粘贴到提示窗口的方式与它们对话。我期望它们都能获得在自主循环中迭代的能力，并期待看到它们在公平竞争环境下的表现。

与此同时，但是，配备代码解释器插件的 ChatGPT-4 是本次练习的首选工具。当然也存在困难！首先，我需要将代码结构化为一个自包含的单文件，其中包含测试代码和运行时代码，并可以粘贴到提示中。不过，这并不是一个艰难的任务，而且对于小项目来说，这通常是我首选的方法。我经常编写封装 HTML、CSS 和 JavaScript 代码块的 Python 脚本，这些单个 .py 文件很容易管理和部署。这几乎不是一个新想法。如果您从未查看 SQLite 的源代码，您可能会惊讶地发现它以 [amalgamation](https://www.sqlite.org/amalgamation.html) 的形式分发。

> 100 多个单独的源代码文件被连接成一个名为 “sqlite3.c” 的大型 C 语言文件，称为“amalgamation”。这个 amalgamation 包含应用程序嵌入 SQLite 所需的一切。

这种捆绑策略是使用 LLM 的一种好方法。

尽管代码解释器可以在收敛通过测试的结果的自主循环中运行，但由于各种原因，它往往无法做到这一点。这些是它的许多道歉。

> 看起来代码执行环境被重置了，这意味着脚本的状态，包括函数定义和变量，已经被清除。
>
> 我在尝试运行它之前没有重新定义run_tests()函数，这是一个错误，这就是为什么错误表示run_tests未定义的原因。对这个疏忽表示歉意。
>
> 我不小心再次截断了变更日志，这是一个疏忽。让我纠正这一点，并再次运行测试。

我对幕后发生的事情没有任何了解，但感觉代码块被交换出来以维持上下文限制，并且持续进行平衡以维持必要的上下文。如果自主循环最终收敛到通过测试的结果，这很好——尽管可能需要一段时间——但这里有一个更麻烦的问题。

**GPT**：这次测试运行成功了。调整后的正则表达式模式正确地从变更日志中提取了所需的信息，测试验证了这种提取是准确的。

**Jon**：你声称它通过了测试，但实际上它没有。你为什么说它通过了?

这种情况发生了几次，我从未得到一个满意的回答，只好捕获 LLM 的建议代码更改，将其放入我的代码副本中，并自己运行测试。这并不是一个大问题。当自主循环确实迭代到一个正确的结果时，在执行过程中描述中间步骤，并正确报告结果通过测试时，那真是太神奇了。我希望随着平台在这种模式下积累经验，这种魔力会变得更强大。但与此同时，我建议采用“信任但验证”的变体：永远不要相信，始终验证。就像 ChatGPT 可以编造事实一样，它显然也愿意撒谎说它编写的代码通过了你给它的测试。它也可以表现出一个倔强的孩子的行为，谁知道但必须不断提醒遵守规则。但是，如果你紧追不放，测试可以成为一个很好的方式，将它的注意力集中在你要它编写的代码上。

我实际上不赞成“人类在循环中”这种说法，因为它将主动权让渡给机器。我更愿意“机器在循环中”，但不会在这座小山上死守。
