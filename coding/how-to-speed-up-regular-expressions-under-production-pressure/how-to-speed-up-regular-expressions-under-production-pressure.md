
<!--
title: 如何在生产压力下加速正则表达式
cover: https://cdn.thenewstack.io/media/2024/04/33320028-getty-images-g6d6uvrvmmq-unsplash.jpg
-->

如果你能分离正则表达式方法并使用基准测试来检查比较，那么如果你真的需要的话，你可以加速正则表达式。

> 译自 [How to Speed up Regular Expressions under Production Pressure](https://thenewstack.io/how-to-speed-up-regular-expressions-under-production-pressure/)，作者 David Eastman。

在指出使用[正则表达式](https://thenewstack.io/taming-text-search-with-the-power-of-regular-expressions/)的优势时，我感到有些内疚，因为我在[多篇](https://thenewstack.io/regular-expressions-and-solving-the-food-taster-dilemma/)[文章](https://thenewstack.io/magic-regexp-a-javascript-package-for-regular-expressions/)中提到了它的优势，却从未提及它的运行速度可能很慢。

在许多应用案例中，正则表达式的速度并不是问题。它只是通过表单捕获一些问题。但是，当速度很重要时，你突然会变成一名侦探，寻找时间杀手。这会迫使你找出哪些代码片段效率低下，但在生产压力下不得不加快速度是一种高难度行为。

我将使用 C# 示例，但最重要的是，你通常必须注意如何在任何你使用的语言中使用正则表达式，并且编译正则表达式等选项可能会有所帮助。

在我比较执行速度时，我必须使用某种基准工具来进行有效的比较。幸运的是，[BenchmarkDotNet](https://benchmarkdotnet.org/articles/overview.html) 已经存在。它适用于控制台应用程序，这正是我们所需要的。

我将继续使用 Visual Studio Code，因为它更适合创建和显示项目，而无需解决方案。为了加快速度，我将使用模板。

打开 [Warp](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)，我首先运行以下步骤：

![](https://cdn.thenewstack.io/media/2024/04/6c6ae404-untitled-1024x185.png)

![](https://cdn.thenewstack.io/media/2024/04/94ea416a-untitled-1-1024x326.png)

![](https://cdn.thenewstack.io/media/2024/04/a877aff3-untitled-2-1024x277.png)

这只是使用可用的 **benchmark template** 为我们设置一个名为 `BenchmarkRegex` 的项目，以设置合适的项目框架。我们可以看到生成的位于目录中的文件：

![](https://cdn.thenewstack.io/media/2024/04/0a6ce7e9-untitled-3-1024x220.png)

然后，我们可以使用 `code .` 命令启动 VS Code.

但首先，让我们考虑一下我在之前的文章中运行的一些正则表达式任务。我们使用了一个[棘手的模式](https://thenewstack.io/regular-expressions-and-solving-the-food-taster-dilemma/)，它使用交替和 **环视(lookaround)** 来证明 *“i before e except after c”* 在英语中经常被打破：

![](https://cdn.thenewstack.io/media/2024/04/f0e4e2d4-untitled-5.png)

上面的模式通过查找不带 “c” 的 “cie” 或 “ei” 来查找破坏性示例。请注意，环视是正则表达式中可能在不同实现中表现不同的函数之一，应谨慎使用。在这种情况下，我们使用否定后顾 (?<!c) 来确认 “ei” 前面没有 “c”，但不会消耗该 “c”。阅读文章了解更多详情。

我们可以将此示例文本和模式直接放入我们的新模板文件 *Benchmark.cs* 中：

```cs
using System; 
using System.Text.RegularExpressions; 
using BenchmarkDotNet; 
using BenchmarkDotNet.Attributes; 
namespace BenchmarkRegex 
{ 
   public class Benchmarks 
   { 
      private const string Pattern = @"(cie|(?<!c)ei)"; 
      private const string GoodText = "Good: ceiling, receipt, deceive, chief, field, believe."; 
      private const string BadText = "Bad: species, science, sufficient, seize, vein, weird."; 
      static bool printMeOnce = false; 
 
     [Benchmark] 
      public void Scenario1() 
      { 
         // Implement your benchmark here var 
         f = Regex.IsMatch(GoodText + BadText, Pattern); 
         if (!printMeOnce) foreach (Match match in Regex.Matches(GoodText+BadText, Pattern, RegexOptions.None)) 
            Console.WriteLine("Found '{0}' at position {1}", match.Value, match.Index); 
         printMeOnce = true; 
      } 
   } 
}
```

首先，我们检查匹配是否有效，以及它是否捕获了六个案例。

我们只能对发布模式下的控制台应用程序进行基准测试，这很好，因此我们可以在 Warp 命令行中运行  `dotnet run -C Release`。很快，在日志中，我们得到了六个案例被捕获的确认：

![](https://cdn.thenewstack.io/media/2024/04/eff28054-untitled-7.png)

最后，我们得到了基准：

![](https://cdn.thenewstack.io/media/2024/04/f7884eaa-untitled-8-1024x535.png)

好的，太棒了。当然，我们现在需要回到我们的主题，即加速正则表达式。因此，第一个也是相当明显的方法就是使模式 **静态化**。既然我们已经确认了模式有效，我们就可以放弃打印输出，毕竟，这使得基准测试非常慢！


```cs
.. 
private const string Pattern = @"(cie|(?<!c)ei)"; 
private static readonly string StaticPattern = @"(cie|(?<!c)ei)"; 
.. 
[Benchmark] public void Scenario1() 
{ 
  // Implement your benchmark here 
  Regex.Matches(GoodText+BadText, Pattern, RegexOptions.None); 
} 
 
[Benchmark] public void Scenario2() 
{ 
  // Implement your benchmark here 
  Regex.Matches(GoodText+BadText, StaticPattern, RegexOptions.None); 
} 
..
```

因此，我们大致期望第二个场景会快一些。事实确实如此：

![](https://cdn.thenewstack.io/media/2024/04/d9d28b6d-untitled-9-1024x244.png)

（是的，在不打印的情况下，我们处于纳秒级范围。）

现在我们已经测试了基准测试，我们可以测试编译选项：

```cs
private const string Pattern = @"(cie|(?<!c)ei)"; 
private static readonly string StaticPattern = @"(cie|(?<!c)ei)"; 
private static readonly Regex CompiledRegex = new(Pattern, RegexOptions.Compiled); 
.. 
[Benchmark] public void Scenario3() 
{ 
   CompiledRegex.Matches(GoodText+BadText); 
} 
..
```


那么，这个基准测试如何？

![](https://cdn.thenewstack.io/media/2024/04/fc8aeb11-untitled-10.png)

嗯，大约一半。但这并不是一个明确的结论。在其中和周围发生着许多事情，你需要了解。

当你第一次开始使用 C# 时，你可能还记得了解到它被转换为**中间语言**（IL 或 MSIL），然后通过**即时**（JIT）编译编译成操作系统的本机格式。（在 C# 于 2000 年发布时，这似乎有点无关紧要，因为 Microsoft 与 Windows 紧密绑定。）

![](https://cdn.thenewstack.io/media/2024/04/a1abb0af-untitled-11.png)

然而，Regex 会生成自己的节点、**解析树**和操作，然后将其转换为 IL。请记住，Regex 是比 .NET 更古老的技术——大约早了半个世纪。这在一定程度上解释了为什么在处理它时有特殊规则。

如果没有 Compile 标志，则会将实例化的 Regex 对象解释为上述一组内部操作。当调用对象上的方法（如*Match*）时，才会将这些操作代码转换为 IL，以便 JIT 编译器可以执行它们。如果进行的 Regex 调用很少，这是可以的。如果 Regex 定义是**静态的**，则操作代码会得到**缓存**。默认情况下，最近使用的 15 个操作代码会被缓存。如果你确实使用了许多模式，可以使用**Regex.CacheSize**属性来更改此设置。

如果使用了 Compile 标志，预编译的正则表达式会增加启动时间，但执行单个模式匹配方法的速度会更快。如果你反复使用某些模式，这是有用的。

你可以创建一个 Regex 对象和模式，对其进行编译，然后将其保存到**独立程序集**中。你可以调用**Regex.CompileToAssembly**方法来编译并保存它。但是，在设计时考虑这一点是有意义的，因为你要将应用程序切分成单独的程序集。

总之，明智的认识是，Regex 根本不应在时间关键区域中使用。如果你运行的表达式很少，最好以通常的解释方式完成。如果你经常运行相同的模式，请使用 Compile 标志或将它们放在单独的程序集中。最终，如果你可以隔离 Regex 方法并使用基准测试来检查比较，你就可以在行动中抓住时间杀手。
