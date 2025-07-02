<!--
title: Java语言的文艺复兴
cover: https://cdn.thenewstack.io/media/2025/06/c37fab79-java.jpg
summary: Java 正在经历复兴，变得更加有趣和现代化。通过 OpenJDK 和 Project Amber 等项目，Java 在语言表达性、面向数据编程和简化学习方面取得了显著进展。六个月的发布节奏也使得 Java 能够更快地适应现代架构和程序类型。
-->

Java 正在经历复兴，变得更加有趣和现代化。通过 OpenJDK 和 Project Amber 等项目，Java 在语言表达性、面向数据编程和简化学习方面取得了显著进展。六个月的发布节奏也使得 Java 能够更快地适应现代架构和程序类型。

> 译自：[Inside Java's Language Renaissance](https://thenewstack.io/inside-javas-language-renaissance/)
> 
> 作者：Chad Arimura

“Java 太老了，太枯燥了，而且太企业级了！” 当时我和我的联合创始人 Travis Reeder 在萨克拉门托河和圣华金河三角洲上乘船颠簸时，他对着风大喊大叫，当时我们正处于企业倦怠和中年编码危机的某个阶段。“我想重新享受编写代码的乐趣！”

这就是为什么我们在 2009 年用 Ruby 创办咨询公司的原因。2011 年，我们将我们的下一个创业项目 Iron.io 切换到 Go——并在 go-nuts 邮件列表中发布了可能是史上第一份 Go 的招聘信息。

快进 15 年，[Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 正在经历一场[全面的复兴](https://thenewstack.io/java-modernizes-new-tools-for-ai-and-quantum-age/)。它又变得有趣起来，而且奇怪的是，我正在成为促成此事的一员。

## **哎呀！成功了。**

我理解 Travis 的想法。2005 年，当 Ruby on Rails 的创建者 David Heinemeier Hansson 在第一次演示 Rails 脚手架时，[说出他的那句名言](https://www.youtube.com/watch?v=Gzj723LkRJY)——“哎呀！成功了。我们已经启动并运行了。”——时，Travis 可能正在使用 Java 1.4。不仅没有 record 类、switch 表达式或模式匹配——而且还没有 lambda 函数、流或泛型，而 J2EE 才是当时流行的框架，并且完全支持 SOAP 和 WSDL。而 DHH 正在舞台上，在 16 分钟内从头开始构建一个可以正常运行的博客，并且从未说过“企业”或“bean”这个词。这太棒了。

因此，我接下来的十年都花在了编写 Ruby 和 Go 上，对 Java 的 тихо 并且快速的进步保持着不感兴趣和不了解的状态，直到一系列事件导致了我们公司被收购，并且我加入了 Oracle 的 Java 平台组。

## **发布节奏**

我们最近在 JavaOne 2025 上发布了 [Java 24](https://blogs.oracle.com/java/post/the-arrival-of-java-24?source=:ex:pw:::::TNS_Java_Renaissance_A&SC=:ex:pw:::::TNS_Java_Renaissance_A&pcode=)。新版本的 Java 每六个月发布一次，就像时钟一样，在 ISO 周的第 12 周和第 38 周的星期二发布，并且已经持续了七年多。这种[基于时间的发布模式](https://www.java.com/releases/)与以前基于功能的模式相比是一个很大的变化，在以前的模式中，发布会与一个特定的功能绑定，而这个功能通常需要三年多的时间才能完成。

这种可预测的六个月发布节奏带来了许多好处，例如更快地将新功能交付给开发人员，将大型概念（例如模式匹配）分解为较小的增量更改（用于 `instanceof` 的模式匹配），为依赖 Java 的公司建立可预测性，以及启用一个预览功能流程，该流程可以收集真实世界的反馈并在最终确定之前进行更改。六个月的发布节奏也意味着不必急于在准备就绪之前包含某些内容——因为如果某个功能需要更多时间，那么另一趟列车很快就会到来。

在这种节奏下，大量的功能被添加到 Java 中：records、模式匹配、虚拟线程、外部函数和内存 API 以及超低延迟垃圾收集器，仅举几例。我将介绍这项工作的一些主题，但首先让我们讨论一下所有这些的推动者：OpenJDK。

## **OpenJDK**

[OpenJDK](https://openjdk.org/) 于 2006 年启动，旨在协作开发 Java 的开源实现，如今，许多公司和个人通过 OpenJDK 为 Java 做出贡献。请在此处查看 JDK 24 的 OpenJDK 贡献图 [here](https://blogs.oracle.com/java/post/the-arrival-of-java-24?source=:ex:pw:::::TNS_Java_Renaissance_A&SC=:ex:pw:::::TNS_Java_Renaissance_A&pcode=)。

请注意，我说 OpenJDK 是一个“地方”，而不是一个“事物”。OpenJDK 拥有项目、小组、成员、邮件列表、维基、JDK 增强提案 (JEP) 以及诸如源代码甚至 Java 吉祥物 Duke 的图像等工件。OpenJDK 不是“Java 的构建版本”，可以下载并用于运行其应用程序。除了管理和贡献 OpenJDK 的大部分工作外，Oracle 还构建发行版，包括一些在 GPLv2（带有 Classpath Exception）下获得许可的发行版，一些在 Oracle“无费用条款和条件”许可下获得许可的发行版，以及其他在 Oracle 的商业许可下获得长期支持的发行版。

## **Java 的语言复兴**

由 Oracle 首席语言架构师 Brian Goetz 领导的 Project Amber 是推动 Java 当前语言演变的主要力量。该项目在三个方面取得了重大改进：首先，使 Java 语言更具表现力（从而更简洁）；其次，使其更“面向数据”；第三，简化新学习者和小程序的使用——所有这些都使该语言保持可读性、可维护性和兼容性。这是一个很高的要求，但通过精心的演变，它已成为一项成功的尝试。

表达性在 Amber 的所有功能中都很明显。例如，文本块和局部变量类型推断将如下代码：

```java
String html = "<html>\n" +
              "    <body>\n" +
              "        <p>Hello, world</p>\n" +
              "    </body>\n" +
              "</html>\n";
```

变成这样：

```java
var html = """
           <html>
               <body>
                   <p>Hello, world</p>
               </body>
           </html>
           """;
```

Record 类将我们编写的成百上千行的“数据载体”类变成这样：

```java
record Person(String name) { }
```

模式匹配允许使用简单的类型模式，例如带有 `instanceof` 的示例：

```java
if (obj instanceof Person p) {
	System.out.println(p.name());
}
```

...以及带有 record 模式的对象解构用例：

```java
if (obj instanceof Person(String name)) {
	System.out.println(name);
}
```

我们可以将以上所有内容组合成 `switch` 的模式：

```java
switch(o) {
	case Person(String name) && !name.isEmpty() -> "Person: " + name
	case Vehicle(String plate) && !plate.isEmpty() -> "Vehicle: " + plate
}
```

这可能是最常见的模式匹配形式。

这不仅减少了代码量，而且减少了容易出错的代码，并且当您开始一起解开这些功能的强大功能时，它会变得更具表现力和强大。

但不仅仅是细节在发生变化；人们正在编写的程序类型也在发生变化。现在许多程序本质上是来自/去往外部来源的数据的接收者、处理器和发送者：数据库、API、大型语言模型 (LLM) 等。

举个例子：Slack 机器人从您的某个客户那里获取支持请求，然后调用您的 CRM API，然后要求 LLM 使用所有这些信息来构建对客户的回复。与其使用类来模拟业务实体和流程（这对于较大的复杂应用程序来说传统上是一个好主意），现在您可以使用类来简单地模拟数据本身。您可以使用 record 来模拟 JSON API 响应，使用模式来解构数据，使用密封类进行详尽的分析，并使用文本块来形成 LLM 提示。我们讨论过的这些功能使您可以编写结构精美的面向数据的程序。

最后，对于解决现代问题的专业开发人员来说，该语言不仅变得更好、更漂亮，而且对于学习者和小型程序来说也变得更简单。“Paving the On-Ramp”是 Project Amber 的一部分，致力于简化此过程。简而言之，第一个 Java 程序已从以下形式：

```java
public class HelloWorld {
	public static void main(String[] args) {
		System.out.println("Hello, World!");
	}
}
```

...变为以下形式：

```java
void main() {
	IO.println("Hello, World!");
} 
```

Java 是团队构建大型程序的绝佳平台，但对于学生和学习者来说，第一个 Java 程序的示例给人的印象是复杂和冗长，尤其是在一种多语言的世界中，其他语言只是简单地提供 `print()` 作为唯一的代码行。

还有更多的工作要做。例如，单/多文件源代码引入了使用 Java 启动器启动源代码程序的能力，而无需首先显式编译源代码。还有一个新的 shebang 构造，允许您的 Java 文件像脚本一样启动。采用以下源文件：

```java
#!/path/to/bin/java --source 24 --enable-preview
 
void main() {
  IO.println("Hello, World!");
}
```

...并使其可执行：

```shell
chmod +x myscript
```

您现在可以运行它：

```shell
$ ./myscript
Hello, World!
```

这仅仅是现代 Java 的可能性的开始，它再次变得有趣，仍然向后兼容，易于维护，甚至更易于阅读。我们甚至还没有触及其他创新领域，如新的 API、更好的性能、更清晰的**可观测性**、更好runtime ergonomics等等。

因此，下次我带 Travis 出海时，我们应该有很多话要说，因为 Java 在六个月的发布节奏下已经发生了很大的变化，以适应现代架构、风格和程序类型。他真的没有理由不在 Java 中开始他的下一个项目。

在本三部分系列的下一篇文章中，我们将讨论 Java 的平台复兴，在第三部分中，我们将讨论 Java 的人工智能复兴。

敬请关注！

*要了解有关 Java 语言发展方向的更多信息，请观看来自 JavaOne 的 [Brian Goetz 的演讲](https://www.youtube.com/watch?v=1dY57CDxR14)。*