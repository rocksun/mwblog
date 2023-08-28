# Python 的演变方式

未来可能会带来更快速、更高性能的 Python，而正是这个充满激情和执着的用户社区将帮助实现这一目标...

![](https://cdn.thenewstack.io/media/2023/08/87533201-motorbike-1827482_1280-1024x682.jpg)
*图片来自 Pixabay 的 Christel SAGNIEZ*

[Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) 是如何演变的？Stack Overflow 在其播客中[探讨了这个问题](https://stackoverflow.blog/2023/07/25/how-the-python-team-is-adapting-the-language-for-an-ai-future-ep-593/)，邀请了 [Pablo Galindo Salgado](https://www.linkedin.com/in/pablo-galindo-salgado-4996b4139/) —— Python 核心开发人员之一，也是 Python 指导委员会的五位成员之一。

Salgado 还是最近两个重要版本（Python 3.10 于 2021 年 10 月和 3.11 于 2022 年 10 月发布）的发布经理，他在播客中开玩笑说“听起来非常花哨，但实际上只是负责按下按钮发布二进制文件的人，这可能不是最时尚的工作，但总需要有人来做，有时候也很有趣…

“有一次我们实际上弄崩了 GitHub。”

在谈话中表现出来的是对 Python 的热情，这种热情在多个层面上都有体现。它始于开发人员和委员会，他们为忠实的社区维护和拓展这门语言。然而，这个社区不仅通过将 Python 应用于新的问题领域来帮助推动语言的发展，还通过在开放过程中合作，以确定最需要的新功能。 Python 正在为数据科学和人工智能应用微调语言，并寻找避免 Python 的全局解释器锁带来性能损失的方法。

但是，尽管未来可能会带来更快速、更高性能的 Python ，正是这个充满激情和承诺的用户社区将帮助实现这一目标…

## 变革与兼容性

变革一直在发生。作为核心开发人员，Salgado 帮助实现了 Python 的新解析器和 Python 编译器。Python 3.12 版本包括了针对 Python 格式化字符串字面量（或“[f-strings](https://realpython.com/python-f-strings/)”，即带有变量的特殊字符串，在运行时被值替换的字符串）的[改进](https://realpython.com/python312-f-strings/#f-strings-had-some-limitations-before-python-312)。而且 Salgado 在[一月份告诉 Dice.com](https://www.dice.com/career-advice/developer-qa-pablo-galindo-talks-pythons-speedy-future)，长期目标包括 WebAssembly 兼容性以及改进 Python 的类型系统、用户界面和错误消息。

但另一个长期目标是保持向后兼容性。在早些时候的 [Stack Overflow 播客中](https://the-stack-overflow-podcast.simplecast.com/episodes/what-its-like-to-be-on-the-python-steering-council)，Salgado 承认仍在使用 Python 2 的人数“不是零……但我很高兴地说，非常非常少。我认为可能只有几十个…”

Python 在向后兼容性方面的断裂与 Python 2 仍然是一个悬而未决的记忆，仍然影响着他们努力改变 Python 的全局解释器锁。Salgado 在采访中后来说：“我们知道从 Python 2 到 Python 3 发生了什么。”“我们已经吸取了那个教训，我们不想再次重复，即使是微小的部分，这对我们来说非常重要。”

## 与人工智能的接口

Galindo 被问及是否有公司有兴趣应用生成式人工智能和大型语言模型，以及他是否认为这会导致新的 Python 框架或语言特性。但他对核心团队的看法是坦率的。“我们在预测 Python 中的新事物方面表现得确实很差。”无论是网站开发和 Django 网络框架，数据科学，还是（现在的）生成式人工智能，“我们总是稍微落后。”

Salgado 表示，Python 部分是通过关注灵活性来回应的。“我们努力使所有可能的工作流程，或尽可能多的工作流程，都可以通过 Python 实现。”作为一个例子，Salgado 说他见过使用 Rust、C++ 或 Swift 等快速编译语言编写的 AI 框架，但仍然在顶部有一层 Python 进行交互。正是这种灵活性“让你可以继续前进，作为开发人员，这给你带来了动力”，当然，顶部的 Python 层允许快速迭代和解释语言的轻松交互。“你运行一个小实验，然后会发生一些事情，你可以立即获得反馈，然后你可以移动事物，而不需要等待编译等。”

Salgado 认为，正在开发具有大型代码库的 AI 社区欣赏 Python 的可选“提示”语法以指示变量类型（以及它使类型检查工具能够发挥作用的方式）。他在播客中提到，物理学家喜欢语法修改，这使他们可以向类型检查工具警告有关使用奇异形状的多维数组的情况。

Salgado 还回顾了 Python 添加矩阵乘法运算符的时候。这是一个独立的 @ 符号，表示一种[常见的数学运算](https://en.wikipedia.org/wiki/Matrix_multiplication)，在这种运算中，一个矩阵的列的值与另一个矩阵的行的值相乘，最终创建出第三个矩阵。Salgado 将这个时刻记为一个“我们实际上为帮助这些社区改变了语言的时刻……主要是为了数据科学人员”，在这种操作中经常使用。

在与 Dice.com 的[一月份采访中](https://www.dice.com/career-advice/developer-qa-pablo-galindo-talks-pythons-speedy-future)，Salgado 以矩阵乘法操作符为例，说明了语言如何演变。正如 Salgado [在 2021](https://www.dice.com/career-advice/python-luminary-pablo-galindo-talks-programming-languages-future) 年所说，“Python 是在公开环境中开发的，主要由志愿者完成。因此，任何问题都必须通过社区、核心开发团队和 Python 指导委员会之间的合作来解决。

“有时候这会使事情变得更具挑战性，因为在处理这些挑战时没有协调的努力。另一方面，核心开发团队的许多成员和广大的 Python 社区对这些问题都很感兴趣，并积极探索不同的解决方案……

“事实上，开发是在公开环境中完成的，主要由志愿者完成，这带来了一些挑战，但也允许任何人提供意见并参与。这通常会产生比由一组非常有控制力的开发人员达成的解决方案更好得多的解决方案，而这些开发人员都有相似的背景。”

## 关于全局解释器锁

播客主持人不得不问有关 Python 讨厌的全局解释器锁，这会阻止并行处理（因此，最多只能够在线程之间切换，但不能同时运行两个线程的 Python 代码。）但是 Python 核心开发人员正在解决这个问题——他们正在探索一种[可选的线程限制锁](https://discuss.python.org/t/a-steering-council-notice-about-pep-703-making-the-global-interpreter-lock-optional-in-cpython/30474)，特别是因为他们[从其用户社区中感受到了这种需求](https://thenewstack.io/python-to-drop-the-global-lock-for-greater-parallelism/)。“现在，我们感觉在数据科学世界，尤其是在人工智能领域，底层有所有这些超级并行的 C++ 库，但由于这种限制，它们实际上无法充分利用这些库的全部功能。”因此，对于AI/数据科学社区，“它将使它们能够在没有很多线程之间的通信，或者在利用 C++ 库的实际原始功能时，充分利用这些并行工作流程。”

人们已经尝试解决这个问题，但这很困难。（“显然你可以解决它，但这意味着现在 Python 的长度会增加一倍，所以这可能是不可接受的。”）但是，去年 Meta AI 的软件工程师 [Sam Gross](https://github.com/colesbury) 实际上实现了一个没有全局解释器锁的 Python CPython 参考语言的[概念验证版本](https://github.com/colesbury/nogil)， Salgado 说，“在性能上没有太大影响。”

Salgado 将这种可能性描述为“一个非常有影响力的事情……尤其是在从事人工智能和数据科学的人，因为它将使他们能够在没有很多线程之间的通信，或者在利用 C++ 库的实际原始功能时，充分利用这些并行工作流程。”

当被问及 Python 如何跟上趋势和活动（除了添加新功能之外），Salgado 说他们更注重于维护开发人员的生产力——“现在，我认为对我们来说更重要的是，Python 不会成为障碍。”他承认全局解释器锁是一个例外，“不幸的是，它确实是……”

## 令人振奋的未来

因此，当采访者在结束时问起 Python 未来的令人兴奋之处时，Salgado 重新提到了改变全局解释器锁的可能性。“我想，这实际上可能发生在一个世界里，因为这一直阻碍了许多可能的工作流程。”

但这不是加速 Python 的唯一努力。Salgado 还对 Microsoft 的 Guido von Rossum 团队以及他们在加速 Python 的 CPython 参考实现（默认和最广泛使用的实现）方面的工作感到兴奋。“它不会像 C++ 那样快，所以如果有人认为会这样，这将是一个现实检验……但免费的速度很重要……你什么都不需要做，然后你就会得到免费的速度！”

很久以前，Python 的基本原则之一是“应该有一种——最好只有一种——明显的方法来做。”所以采访者问，这是否为语言的指导社区创造了紧张氛围，或者是否担心引入多种做事的方式？

Salgado 坦白承认，Python 最明显地违反了这个规则，尤其是在流格式化方面。“我认为我们有六种方法来做这件事！”但他补充说，在现实世界中，“不可能无所不知，知道最佳方式。”因此，当努力追求一种方法时，Salgado 有一个准备好的回应。

“我会修改这句话，说应该有一种非常好的方法来做。”
