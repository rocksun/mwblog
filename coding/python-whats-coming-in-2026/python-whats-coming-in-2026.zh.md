如果2025年是Python的“类型检查和语言服务器协议之年”，那么2026年会是类型服务器协议之年吗？据称，像自由线程这样的“变革性”发展，以及能提高[Python](https://thenewstack.io/what-is-python/)模块性能的“惰性”导入，都将在2026年登陆Python。我们（希望）也将看到改进后的Python代理框架。

但2026年甚至可能迎来变化本身的变化——Python提出变更的方式将有所改变。

上个月，七位嘉宾进行了一次富有启发性的对话——其中包括三位Python核心开发者，其中两位也是[Python指导委员会](https://discuss.python.org/t/steering-council-election-results-2026-term/105296)的成员。2025年即将结束之际，这些知名嘉宾齐聚一堂，参加了[“Talk Python to Me”播客的年终回顾特别节目](https://www.youtube.com/live/PfRCbeOrUd8?si=x5MVtWW6nu7zGgY)，讨论了他们在2025年看到的趋势，以及他们对Python及其开发者社区未来一年的展望。

## 运行Python的工具

从一开始，播客就表明Python仍然是一个基础广泛的全球社区。来自温哥华的[Brett Cannon](https://www.linkedin.com/in/drbrettcannon/)，自[2003年](https://opensource.snarky.ca/About+Me/Frequently+Asked+Questions%20)起就担任Python核心开发者，并已在微软担任首席软件工程师超过10年。Cannon在2025年看到的是人们使用工具运行Python代码方面的进步。

以前你需要安装Python解释器，然后安装所有必需的依赖项，最后在虚拟环境中启动所有东西，而“现在我们有了能将所有这些压缩成一个运行命令的工具！”像[Hatch](https://hatch.pypa.io/latest/)、[BDM](https://www.scalefree.com/portfolio/development-of-the-business-data-modeler-using-python/)和[uv](https://github.com/astral-sh/uv)等越来越多的工具[“相互借鉴，……慢慢建立起这种工具方法的体系。”](https://python-poetry.org/)

这引起了Python核心开发者的关注。“这些工具几乎把Python当作一个实现细节，”Cannon说。Python解释器“只是它们用来运行你的代码的一个东西”，渐渐地隐入幕后。

参与通话的还有[Barry Warsaw](https://www.linkedin.com/in/barry-warsaw/)，他担任Python核心开发者已超过30年。他告诉Cannon：“我认为你确实发现了一些重要的东西。”Warsaw也是2026年Python指导委员会的成员（目前在Nvidia从事Python相关工作），他将这视为一个更大的趋势——“重新关注用户体验”。

对于新用户来说，仅仅安装带有Python解释器的二进制文件可能就很复杂，但[2024年](https://discuss.python.org/t/how-would-you-like-to-declare-runtime-dependencies-and-python-requirements-for-pep-723/40418/82)Python[增加了在Python脚本中嵌入元数据的格式](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata)，以帮助IDE、启动器和其他外部工具。因此，在2025年的世界里，编写由Python运行的代码变得更加容易。“你可以把uv放在脚本的shebang行中——这样你就不用考虑任何事情了。Hatch也可以用同样的方式为开发者服务。”

这得到了计算机科学副教授[Gregory Kapfhammer](https://allegheny.edu/about/campus-department-resources/faculty-and-staff-directory/gregory-kapfhammer/)的积极赞同。Kapfhammer从匹兹堡打来电话（他已经在Allegheny学院的课程中使用了uv），他说uv极大地简化了学生的学习，这让他感到惊讶。“我不用教他们Docker容器，也不用告诉他们如何用包管理器安装Python。”

来自柏林的[Jodie Burchell](https://www.linkedin.com/in/jodieburchell/)也表示赞同，她是一位拥有10年经验的数据科学家（现在是JetBrains的开发者倡导者，负责PyCharm）。Burchell说他们甚至正在讨论是否在数据科学指导社区[Humble Data](https://humbledata.org/)（她是该社区的组织者之一）中使用uv。“它确实抽象掉了所有这些细节。我的争论是，它是不是太‘魔法’了？”作为JetBrains的开发者倡导者，“这也是我们在PyCharm中争论的问题。你在多大程度上‘魔法般地’隐藏了基础知识，而不是让人稍微思考一下？”

这引发了关于Python未来可能发展的讨论。核心开发者Cannon说，对于排查问题的人——甚至只是好奇的人——“我希望这种‘魔法’能够分解。你应该能够通过更细分的步骤来解释这条‘魔法’路径，使用工具一直深入到工具在幕后实际做了什么。”这对他来说不仅仅是假设。“我一直在深入思考这个问题，”Cannon说，因为“我正在考虑让Python启动器做更多的事情。”

毕竟，uv仍然是由一家公司（名为[Astral](https://astral.sh/about)）制造的，“他们随时都有可能消失的风险。”目前已经投入大量工作来为这类打包创建标准，包括[元数据添加](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata)。

## 惰性导入和自由线程Python

2026年还将带来提高性能的“惰性导入”，它将模块的导入推迟到首次使用时进行，从而加快启动时间。“它已经被接受了，而且会非常棒，”核心开发者[Thomas Wouters](https://github.com/yhg1s)说。Wouters从阿姆斯特丹打来电话，他曾在[Google](https://cloud.google.com/?utm_content=inline+mention)内部部署Python，在那里工作了17年，之后才转到Meta。他曾是Python软件基金会的董事会成员——甚至在2025年获得了他们的[杰出服务奖](https://pyfound.blogspot.com/2025/03/dsa-thomas-wouters.html)——并且是[2026年Python指导委员会的现任成员](https://discuss.python.org/t/steering-council-election-results-2026-term/105296)。

Wouters对Python在增加并行处理能力方面的进展感到更加兴奋。考虑到Python的全局解释器锁（Global Interpreter Lock）通过强制单线程处理而臭名昭著地降低了性能，Wouters不加修饰地将这一发展称为“全局解释器锁即将消失！我将其作为一个事实来陈述——虽然它还不是一个事实，那是因为指导委员会尚未意识到这个事实。”

Wouters之所以这么说，是因为他曾是指导委员会的成员，该委员会接受了自由线程作为一项实验性功能，现在对于Python 3.14，“它已获得官方支持。性能非常棒……在MacOS上基本保持了相同的速度……这是ARM硬件和*clang*专业化优化的结合……而在Linux上的最新GCCs上，速度大约慢了百分之几。”

Wouters说，2026年将重点关注社区采纳，“让第三方包更新其扩展模块以适应新的API”，以及“以良好的方式支持自由线程”。但对于Python代码，“事实证明，要使其在自由线程下良好运行，需要进行的更改非常少。”

更重要的是，“我们已经看到了许多非常有前景、高度并行的示例，它们现在可以加速10倍甚至更多。这在未来将非常令人兴奋。”

## 改进增强提案？

最大的变化可能是Barry Warsaw提出的。作为Python增强提案（改变语言的程序）的创建者，Warsaw在说“我们必须重新思考我们如何演进Python——以及我们如何向Python提出变更，以及我们如何在社区中讨论这些变更”时，具有真正的可信度。

当前的流程已有超过四分之一世纪的历史，虽然开发者社区“有所扩大”，但Warsaw说，“使用Python并对其感兴趣的人数”呈指数级增长。但更重要的是，“我一次又一次听到的其中一件事是，编写Python增强提案极其困难，并且耗费精力。它是一个时间黑洞，而在discuss.Python.org上领导这些讨论……有时会充满毒性，而且非常困难。”

最终结果呢？“演进语言、标准库和解释器变得异常困难……我们需要思考如何让人们更容易做到这一点，同时又不失去用户的声音。”

当谈到Python社区时，Warsaw说，留在discuss.python.org上的评论“只是冰山一角”。“世界上有数百万计的用户，例如，惰性导入将*影响*他们——自由线程将*影响*他们。然而他们甚至不知道自己*有*发言权。”Warsaw希望“以一种更具协作性和积极性的方式”代表他们。

因此，Warsaw说，在2026年，“我认为这将是我将花时间思考的事情——你知道的，和人们讨论——如何让这变得对每个人都更容易。”

Warsaw分享了对我们现状的一个有趣观察。“Python已经发生了一些本应是PEP的改变。但它们不是因为……核心开发者不想经历这场苦战！”

“但那也不好，因为那样，你知道的，我们就没有达到适当的考虑水平。”

## 当类型遇到工具

Kapfhammer分享了一个重要的提示，指出“如果你能教你的AI代理使用类型检查器和LSP，它也会为你生成更好的代码。”这为大型语言模型（LLM）提供了更多有用的信息和上下文——而业界也开始注意到这一点。Kapfhammer说，Meta的类型检查器背后的团队正在与[Pydantic AI](https://ai.pydantic.dev/)直接合作，以创建互操作性，“这样当你使用Pydantic AI构建AI代理时，当你使用Pyrefly作为类型检查器时，你也可以获得更好的保障。”

事实上，对于Kapfhammer来说，2025年是“类型检查和语言服务器协议之年”。他使用静态类型检查器[Mypy](https://mypy-lang.org/)以及像[Pyright](https://github.com/microsoft/pyright)或PyLance这样的语言服务器协议。但2025年也带来了Meta的[Pyrefly](https://pyrefly.org/)类型检查器/LSP、Astral的[ty](https://docs.astral.sh/ty/)以及一个名为[Zuban](https://zubanls.com/blog/open-source/)的新类型检查器/LSP。他指出这些2025年的工具都用Rust实现——并且“显著更快”，这改变了他使用工具的方式和频率。“它帮助我将可能需要几十秒或几百秒的事情，通常缩短到不到一秒。”

Cannon指出，“编写Rust代码比编写Python代码需要更多的工作，”并赞扬了工具制造商愿意承担额外的努力，为“社区带来全面的胜利”。

但Cannon似乎也对2026年我们将看到的东西抱有很高的期望。“Pylance实际上正在与Pyrefly团队合作[定义一个类型服务器协议](https://github.com/microsoft/pylance-release/discussions/7180)[TSP]，这样许多类型服务器就可以将类型信息提供给更高级别的LSP，并让该LSP处理像符号重命名之类的所有事情。”

播客由居住在波特兰的Python爱好者和教育家[Michael Kennedy](https://www.linkedin.com/in/mkennedy/)主持，他为这场84分钟的对话——以及未来的一年——做出了完美的总结。

“我仍然认为，作为一名开发者或数据科学家，现在是一个极其激动人心的时代。外面有如此多的机会……每一天都比前一天稍微更令人惊叹……我热爱它。”

视频