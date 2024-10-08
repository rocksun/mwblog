# Python 3.13：性能和规模的全新突破

![Python 3.13：性能和规模的全新突破的特色图片](https://cdn.thenewstack.io/media/2024/10/48878a39-kyle-glenn-hn2xf1sk_y4-unsplash-1-1024x683.jpg)

[Python 3.13](https://docs.python.org/3.13/whatsnew/3.13.html) [预计将于今天发布](https://peps.python.org/pep-0719/)，代表着 [Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) 编程语言的重大进步，特别是在性能和开发人员体验方面，实验性的自由线程模式和 [即时 (JIT) 编译器](https://thenewstack.io/why-python-is-so-slow-and-what-is-being-done-about-it/) 为未来的改进奠定了基础。

[最初计划于 10 月 1 日发布](https://www.phoronix.com/news/Python-3.13-rc3-Released)，新版本因性能回归而推迟，Python 最新稳定版本的发布时间已改为 10 月 7 日。

如上所述，Python 的一些主要变化包括一个新的 [交互式解释器](https://docs.python.org/3.13/whatsnew/3.13.html#whatsnew313-better-interactive-interpreter)，以及对在 [自由线程模式](https://docs.python.org/3.13/whatsnew/3.13.html#whatsnew313-free-threaded-cpython) 下运行和 [JIT 编译器](https://docs.python.org/3.13/whatsnew/3.13.html#whatsnew313-jit-compiler) 的实验性支持。

## 自由线程

实验性的自由线程 [CPython](https://thenewstack.io/how-python-is-evolving/) 功能允许在禁用 [全局解释器锁 (GIL)](https://thenewstack.io/why-python-is-so-slow-and-what-is-being-done-about-it/) 的情况下运行。它需要一个单独的可执行文件，可以通过官方的 Windows 和 macOS 安装程序安装，也可以从源代码构建。它可以充分利用多核处理器。目前，它在单线程操作中会造成性能损失。

“自由线程试图从 CPython 中移除 [全局解释器锁](https://realpython.com/python-gil/)，而全局解释器锁一直是实现 [基于线程的](https://realpython.com/intro-to-python-threading/) 并行性的最大障碍，尤其是在执行 [CPU 密集型](https://en.wikipedia.org/wiki/CPU-bound) 任务时，”Real Python 的内容创作者 [Bartosz Zaczyński](https://www.linkedin.com/in/bzaczynski/?originalSubdomain=pl) [在一篇文章中写道](https://realpython.com/python313-free-threading-jit/)。“简而言之，GIL 允许在任何给定时间只运行一个执行线程，无论你的 CPU 配备了多少个核心。这阻止了 Python 有效地利用可用的计算能力。”

历史上，Python 的 GIL 阻止了线程的真正并发执行，[Stanley Seibert](https://www.linkedin.com/in/stanleyseibert/)，[Anaconda](https://thenewstack.io/faster-python-easier-access-to-llms-anacondas-ai-roadmap/) 的社区创新高级总监，告诉 The New Stack。然而，Python 3.13 中的新实验性功能允许并发执行纯 Python 代码。该功能旨在更好地利用多核处理器，而不会牺牲单线程性能。由于其实验性，该功能在本版本中默认关闭。该功能由 Meta 工程师开发，并获得了 Python 指导委员会的批准。Seibert 说，Anaconda 正在为社区开发测试包，以便他们尝试使用此功能。

## JIT 编译器

与此同时，“到目前为止，你只能通过外部工具和库来利用 Python 的各种 JIT 编译器，”Zaczyński 写道。“其中一些，比如 [PyPy](https://pypy.org/) 和 [Pyjion](https://pypi.org/project/pyjion/)，提供了或多或少通用的 JIT 编译器，而另一些，比如 [Numba](https://numba.pydata.org/)，则专注于特定的用例，比如数值计算。”

Python 3.13 中新的实验性 JIT 编译器使用了一种名为 [复制和修补](https://en.wikipedia.org/wiki/Copy-and-patch) 的相当新的算法，他写道。

“这种编译技术的核心思想是找到一个适合目标 CPU 的预编译机器代码模板，并用缺失的信息（例如变量的内存地址）填充它，”他在文章中指出。

Zaczyński 补充说，长远计划是将 Python 的 JIT 提升到一个程度，使其在代码执行性能方面真正产生显著差异，而不会占用太多额外的内存。

Omdia 的分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 将 JIT 编译器称为“一件大事”，因为它使 Python 在与 Java 等久负盛名且面向企业的基于 JIT 的语言相比时处于更平等的地位。
“更重要的是，这种 JIT 实现比传统的 JIT 架构带来了性能提升，”他告诉 The New Stack。“与在创建机器代码之前将代码遍历中间语言相比，这可能非常慢，Python 13.3 的实现使用了一种复制和修补方法，不需要在 Python 运行时内运行完整的 JIT。”

[Andrew Cornwall](https://www.linkedin.com/in/acornwall/)，Forrester Research 的分析师，同意 Python 3.13 中两个最重要的运行时更改是实验性的，“因此日常 CPython 用户目前不会看到太大区别，”他告诉 The New Stack。然而，Python 正在为在多个处理器上更快地运行代码奠定基础。
“一旦启用，JIT 编译器应该让 CPython 对于每个人来说都运行得更快，但 Python 现在正在保持谨慎，默认情况下将其关闭，”Cornwall 说。然而，“禁用全局解释器锁的能力可能会更具破坏性，因为它允许 Python 库利用更多核心，如果这些库可以支持多线程。那些开发 C 库的人需要调查禁用 GIL 的影响。但是，对于日常用户来说，这些变化还很遥远——它们目前在单独的 python3.13t 二进制文件中。”

免费线程是关于尝试使用更多核心。然而，“JIT 编译是关于尝试通过使解释器更高效来从单个核心获得更多收益，”Seibert 告诉 The New Stack。“此版本将包含该 JIT 编译器的第一个版本，并且该目标只是让它无形地使一切都更快。”

事实上，Seibert 说，Python 多年来一直专注于速度。“我知道历史上 Python 比其他一些语言更慢，但更容易编程。这个 [JIT 编译器] 某种程度上将它带入了像 C 或 C++ 这样的领域，”他说。

## 交互式解释器改进
同时，改进的交互式解释器功能包括多行编辑，带有历史记录保存，直接支持 read-eval-print loop (REPL) 特定命令，包括 help、exit 和 quit，默认情况下启用颜色的提示和回溯，交互式帮助浏览（F1 键），历史记录浏览（F2 键）和“粘贴模式”以更轻松地粘贴代码（F3 键）。

“有一个新的交互式解释器，它添加了一些生活质量的东西，比如颜色和能够同时编辑多行 Python 代码——这些东西你可以在 [IPython](https://ipython.org/) 中完成，但现在它内置在解释器中，”Seibert 说。

Python 的新 [交互式](https://docs.python.org/3.13/glossary.html#term-interactive) shell，默认情况下可用，基于 [PyPy 项目](https://pypy.org/) 的代码。

## 其他关键更改
此外，Python 3.13 具有增量 [垃圾收集器](https://thenewstack.io/time-to-get-the-garbage-out-of-webassembly/) 实现，可以减少清理分配内存时的长时间暂停，Cornwall 说。

此外，“平台支持现在包括移动设备（iOS 和 Android 都处于第 3 层，这意味着至少有一位核心开发人员参与）。并且 [Wasm](https://thenewstack.io/what-makes-wasm-different/) 支持已从 [emscripten](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/) 迁移到 [WASI](https://thenewstack.io/wasi-0-2-unlocking-webassemblys-promise-outside-the-browser/),”他说。

## 更多幕后改进
此外，“有一些已弃用的库——例如，如果您使用的是 [cgi](https://docs.python.org/3/library/cgi.html) 或 [crypt](https://docs.python.org/3/library/crypt.html)，您需要找到替代方案，”Cornwall 告诉 The New Stack。“语言更改不太可能影响大多数用户。以前关于 locals() 的未定义语义现在已定义，但这对于大多数开发人员来说都是小事。在这个版本中，大多数开发人员会注意到新的油漆工作，但不会注意到幕后的重大变化。”

一位注意到幕后变化的开发人员是 [Tom Tang](https://github.com/xmader)，[Distributive](https://distributive.network/) 的工程师，[PythonMonkey](https://pythonmonkey.io/) 项目的创建者。Tang 是 [PythonMonkey 项目](https://thenewstack.io/python-meets-javascript-wasm-with-the-magic-of-pythonmonkey/) 的核心开发人员，目前正在努力将 Python 3.13 支持引入 PythonMonkey。

## API 稳定性：PythonMonkey 示例
Tang 说，他作为一名系统开发人员，深入研究 Python 的底层部分，因此 Python 3.13 中 C API 稳定性的变化值得注意。

在 3.13 版本之前，Python 的 C API 在每个次要版本中都会频繁更改，并且有很多未记录的内部 API 在每个下一个 Python 版本中都被破坏或删除，Tang 告诉 The New Stack。
这给 PythonMonkey 的开发带来了一些麻烦，因为 PythonMonkey 承诺支持多个 Python 版本，这非常复杂。在 Python 3.13 中，CPython 核心维护者采取了 [措施来解决 API 不稳定性](https://github.com/python/cpython/issues/106320) 问题，只提供稳定的公共 API 供使用。大多数未记录的“私有”API 在 Python 3.13 中被移除，剩下的几个现在已记录并提升为稳定 API。

此举对 Python 扩展开发人员很重要，因为它让您能够使用经过良好记录的 API，并迫使您在处理 Python 的底层部分时真正考虑向前和向后兼容性，Tang 说。

“另一方面，在 PythonMonkey 的情况下，由于我们正在处理 CPython 解释器中非常利基的实现细节，以使 PythonMonkey 尽可能快且高效，隐藏“内部 API”或实现细节可能会阻碍我们进一步优化 PythonMonkey 以实现更快的跨语言运行时，”他说。

此外，“如果有一个更正式的 API 用于访问内部，即使这些 API 成为“不稳定”API 的一部分，对像 PythonMonkey 这样的深度集成产品也会有所帮助，”Tang 说。

## 全面做好
总的来说，Python 3.13 中的更改“是不错的补充，本身将进一步巩固 Python 在现有用例中的“首选”语言地位，特别是对于数据、AI 和 IT 工程师，”Shimmin 说。“然而，对我来说，这个版本的决定性因素是速度和规模。”

Python 社区对性能和效率的关注当然会解决 Python 目前在性能方面的一些增长烦恼。Python 3.13 中的更新“也将更好地巩固 Python 作为一种在更广泛的用例中‘无所不能，精益求精’的语言的声誉，”Shimmin 说。

[YOUTUBE.COM/THENEWSTACK 科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)