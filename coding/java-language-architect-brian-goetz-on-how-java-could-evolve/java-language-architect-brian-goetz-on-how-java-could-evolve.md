
<!--
title: Java语言架构师Brian Goetz谈Java的未来发展
cover: https://cdn.thenewstack.io/media/2025/09/a3c50315-brian-goetz-java-language-architect-at-2025-jvm-summit-shh-1.png
summary: Java架构师Brian Goetz在JVM峰会上展望Java的未来，重点在于通过“见证者”概念，使Java更具可成长性和可扩展性，并提出了新的数字类、数学运算符、集合表达式和创建表达式等潜在新特性。
-->

Java架构师Brian Goetz在JVM峰会上展望Java的未来，重点在于通过“见证者”概念，使Java更具可成长性和可扩展性，并提出了新的数字类、数学运算符、集合表达式和创建表达式等潜在新特性。

> 译自：[Java Language Architect Brian Goetz on How Java Could Evolve](https://thenewstack.io/java-language-architect-brian-goetz-on-how-java-could-evolve/)
> 
> 作者：David Cassel

Java 语言架构师 [Brian Goetz](https://inside.java/u/BrianGoetz/) 上个月在 JVM 峰会上发表了[一次展望 Java 未来的演讲](https://www.youtube.com/watch?v=Gz7Or9C0TpM)。

Goetz 讨论的不是[我们现在拥有的 Java](https://thenewstack.io/introduction-to-java-programming-language/)，而是一种假设的“一组特性，这些特性的设计目的不是作为一种编写更好程序的方式单独使用，而是作为一种使语言更具可成长性和可扩展性的机制。”

简而言之，Goetz 解释了他如何看待 Java 语言的演变。

“我花了很多时间研究其他语言的做法，”Goetz 说，“我们觉得现在已经到了一个地步，我们对我们想要的发展方向有了一个很好的想法。”

在 Reddit 上，Goetz 将他的演讲描述为“[对未来可能方向的声明](https://www.reddit.com/r/java/comments/1mwaba5/growing_the_java_language_jvmls_by_brian_goetz/na320i0/)”。目前还没有正式的 Java 增强提案，“这确实是我们第一次如此详细地谈论它。总要从某个地方开始。”

但这是一个绝佳的机会，不仅能看到一种编程语言是如何变化的，还能看到推动这些决策的深思熟虑的理念。

## “可成长”语言的理念

在演讲开始时，Goetz 强调他不是在谈论“我们计划立即交付的特性”。相反，他将着眼于长期的“更具*激励性*的例子”。Goetz 将他的演讲命名为“发展 Java 语言”——这是有原因的。Goetz 记得 Sun Microsystems 计算机科学家 [Guy Steele](https://en.wikipedia.org/wiki/Guy_L._Steele_Jr.) 在 1998 年发表的一篇著名论文（[以及演讲](https://youtu.be/uXLtyhNUleg?si=o8oX2H2P8gjxVIbD)），题为“发展一种语言”。

Goetz 说 Steele “呼吁语言设计者将可成长性视为编程语言设计的一个维度。”

虽然许多语言允许用户通过用户创建的库来扩展“词汇”，但 Steele 指出，如果这个新词汇看起来与语言自身的本质“原语”不同，那就更难了。Goetz 说，“在许多方面，这篇论文是 Valhalla 项目的发令枪”——这是一个始于 2014 年的 OpenJDK 项目，旨在孵化新的 Java 语言特性，由 Goetz 领导。

因此，Goetz 想描述的不仅仅是一个新的 Java 特性，还有一种语言演化理念，该理念在添加新的 [Java 特性](https://thenewstack.io/frontend-gets-smarter-ais-javascript-revolution/) 时优先考虑可扩展性，以及实现它的机制。“有些人会说这太过分了，”Goetz 幻灯片上的一个要点说。“有些人会说这还不够。”

“这就是我们知道我们……正好处在中间的位置。”

## 引入“见证者”：Java 的一个新概念

那么，新想法是什么？Java 的方法定义接口被称为“[行为的蓝图](https://www.geeksforgeeks.org/java/interfaces-in-java/)”。Goetz 建议，现在“我们想做接口所做的一切——获取一组命名的行为，并将它们分组到一个命名的包中，你可以声明这种类型符合，或者这组类型符合（并允许编译器进行类型检查）。”

因此，这里有一个关键的区别。Java 语言设计团队希望它是关于类型，而不是类型的实例。

“我们想把这种行为转移到一个第三方的*见证者*对象中，”一张幻灯片解释说。

所提出的是一个简单、直接的关键字——一个见证者字面量（以及“召唤”见证者的能力，Goetz 说，“仅仅通过说出它的类型”）。

所以……

`public static final Comparator` COMPARATOR =

变为……

`public static final witness Comparator COMPARATOR =`

稍后，Goetz 详细地告诉听众，“我们可以通过向语言中添加相对较少的东西来向 Java 添加类型类——一种*发布*见证者的机制，以及一种*查找*见证者的机制——我们可以利用现有的语言结构，如接口、字段和方法。”

为什么不直接定义具有所有所需方法的接口，然后让类实现该接口呢？事实证明，这并不总是抽象的一个有用场所，Goetz 说，这让语言设计者面临着许多棘手的角落情况和“陷阱”。

Goetz 的下一张幻灯片解释说，这“实际上是在使用错误的工具”。

“我们需要一些与接口相似但不完全相同的东西。”Haskell 有类型*类*（“抽象类型，而不是类型的行为”），而 C# 和 Kotlin 都在“经历他们自己对它的探索”。C# 社区提出了一个类似的东西，称为 [shapes and extensions](https://github.com/dotnet/csharplang/discussions/164)。

“所有这些都在围绕着同一个难题跳舞。那就是：我如何抽象类型的行为，而不让它成为类型定义的一部分？”

## 增长的机会：潜在的 Java 新特性

Goetz 说，这个想法经历了许多迭代，但“我们已经把它提炼成一种比我们以前的一些想法更干净地融入 Java 的东西。”

“这是关于发展语言的，”一张幻灯片上写道。Goetz 看到了“可成长性”的巨大潜力——并提出了几个潜在的新特性：

* **新的数字类，**但“具有原语的运行时行为”——例如 16 位浮点数。
* **数学运算符。**Goetz 说，为你的 Float16 变量使用标准的加号“会非常好”，而不是使用单独的方法。其他语言已经尝试过这种所谓的“运算符重载”——根据所涉及的变量类型，将符号与多个操作相关联。Goetz 说，这是一个“有点语言学上的雷区……许多语言都孵化了各种运算符重载的灾难”。
* **集合表达式**“用于构建类似序列的结构”，类似于 [C#](https://developers.redhat.com/articles/2024/04/22/c-12-collection-expressions-and-primary-constructors#collection_expressions) 中可用的结构。“这处于‘你为什么不’的规范水平。但似乎有一条可行的路径可以到达那里，就像 Java 7 时代提出的提案不是一条可行的路径一样。”
* **创建表达式。**今天在创建一个数组时，其元素的默认值始终为“null”或零。如果有一个见证者可以指示何时存在（以及何时不存在）有效的“空白”值呢？在 Valhalla 项目中，Goetz 说，在初始化数组时添加有效性检查“是我们一直有点犹豫的特性”，因为他们不想将其添加到 Java 的虚拟机 (VM) 中。但是“这是一种将该特性保留在语言中的方法，但允许给定的类根据他们是否做了一些额外的工作来参与该特性。所以这意味着我们可以将这种行为放在正确的位置，这是一种很好的感觉。”

一种多用途的语言添加并不是没有先例的。Goetz 展示了两个早期的“旨在可由库扩展的语言特性的著名示例”——*foreach* 循环和 *try*。开发人员可以通过实现 *Iterable* 类来使用 *foreach* 特性。（Goetz 说 JDK 的开发人员随后“进行了改造，使许多类实现了 iterable”——其他 Java 开发人员也是如此。）但最重要的是，它只是“看起来是内置的”。

Goetz 很高兴 [Java](https://thenewstack.io/azul-cto-java-at-30-still-rules-enterprise-dev/) 没有将该特性限制为仅用于少数明显的用例（如 *list*、*map* 和 *set*）。“我真的很高兴有人站出来说，‘不，不，除了这些少数几个魔法类之外，其他类也能够参与其中，这真的很重要。’”

Goetz 说他想继续保持这种传统。

## Java 演变的未来路线图

在结束演讲时，Goetz 说这不仅展示了见证者的想法，还勾勒出了“我们将如何使用它来实现四个让我们困扰了相当一段时间的潜在特性”。

展望未来，Goetz 认为见证者“使您能够设计更好的特性、更丰富的特性、用户可以更多地使用的特性，并且最终也许我们将来不必设计那么多的语言特性。……希望从长远来看，我们将能够使用它来构建更丰富的通用库和条件行为以及这些东西。

“但在短期内，我们可以使用它来交付可成长的语言特性，包括人们已经要求了相当一段时间的特性。”

一位 Reddit 评论员甚至在[稍后开玩笑说](https://www.reddit.com/r/java/comments/1mwaba5/comment/n9wg1ke/)，Goetz 的演讲让他们想起了“龙与地下城”的法术。“在某个时刻，我确实觉得 Brian 就要施放魔法飞弹了。”

[![](https://cdn.thenewstack.io/media/2025/09/9cbca623-brian-goetz-java-language-architect-reddit-comment-about-2025-jvm-summit-talk-on-witnesses.png)](https://cdn.thenewstack.io/media/2025/09/9cbca623-brian-goetz-java-language-architect-reddit-comment-about-2025-jvm-summit-talk-on-witnesses.png)

这位 Reddit 评论员后来补充说：“这是一次很好的、有趣的演讲。我希望这些特性能够实现。”但 Goetz 的最后一张幻灯片清楚地解释了我们所处的位置。“前几张幻灯片中的示例不是设计，而是想法。”

[![](https://cdn.thenewstack.io/media/2025/09/7fd2db3f-brian-goetz-java-language-architect-reddit-comment-about-complexity-and-2025-jvm-summit-talk-on-witnesses.png)](https://cdn.thenewstack.io/media/2025/09/7fd2db3f-brian-goetz-java-language-architect-reddit-comment-about-complexity-and-2025-jvm-summit-talk-on-witnesses.png)

尽管如此，在[另一条 Reddit 评论](https://www.reddit.com/r/java/comments/1mwaba5/comment/na311aa/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) 中，Goetz 说 Java 的设计团队现在有一个他们“满意”的故事，“所以我们准备分享它。但请注意，它仍然是一个*故事*，并且还有很多其他的 Valhalla 内容需要先完成。”

Goetz 在他的演讲后赢得了热烈的掌声——然后开始接受听众的提问。第一位提问者承认他们已经看到了这个想法的很多价值，称 Goetz 的演讲是“一个以相当小的语法变化包装的非常大的提案”。

Goetz 的回应是什么？“嘘，别告诉他们！”