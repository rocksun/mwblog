
<!--
title: 流收集器：一种操作Java流的新方法
cover: ./cover.png
-->

Java 22 中 java.util.stream.Gatherers 接口中新的可定制流操作符的代码优先之旅。

> 译自 [Stream gatherers: A new way to manipulate Java streams](https://www.infoworld.com/article/3715621/stream-gatherers-a-new-way-to-manipulate-java-streams.html)，作者 Matthew Tyson。


## Java 22 引入流收集器

Java 22 引入了一种新的机制来操作数据流，称为流收集器(Stream gatherer)。流收集器是 [JEP 461](https://openjdk.org/jeps/461) 中交付的功能，允许开发人员创建自定义中间操作符，简化复杂操作。乍一看，流收集器似乎有点复杂和晦涩，你可能会想知道为什么要使用它们。但是，当你遇到需要某种流操作的情况时，收集器将成为 Stream API 中一个显而易见且受欢迎的补充。

## Stream API 和流收集器

Java 流模拟动态元素集合。正如 [规范](https://openjdk.org/jeps/461) 所说，“流是延迟计算的、可能是无界的数值序列。”

这意味着你可以无限地消费和操作数据流。把它想象成坐在河边，看着水流过去。你永远不会想到等待河流结束。对于流，你只需开始使用河流及其包含的所有内容。当你完成时，你就可以离开。

[Stream API](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html) 有几种内置方法用于处理数值序列中的元素。这些是 [函数式](https://www.infoworld.com/article/3613715/what-is-functional-programming-a-practical-guide.html) 操作符，例如 `filter` 和 `map`。

在 Stream API 中，流从事件源开始，`filter` 和 `map` 等操作被称为“中间”操作。每个中间操作都返回流，因此你可以将它们组合在一起。但是，使用 Stream API，Java 不会在流到达“终端”操作之前开始应用任何这些操作。这支持即使将许多操作符链接在一起也能实现高效处理。

Stream 的内置中间操作符功能强大，但它们无法涵盖所有可想象的要求。对于超出范围的情况，我们需要一种方法来定义自定义操作。收集器为我们提供了这种方法。

## 你可以使用流收集器做什么

假设你在河边，树叶上写着数字，漂浮而过。如果你想做一些简单的事情，比如创建一个包含所有偶数的数组，你可以使用内置的 `filter` 方法：

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
numbers.stream().filter(number -> number % 2 == 0).toArray()
// result: { 2, 4, 6 }
```

在上面的示例中，我们从一个整数数组（源）开始，然后将其转换为流，应用一个过滤器，该过滤器只返回那些除以二余数为零的数字。`toArray()` 调用是终端调用。这相当于检查每片树叶是否为偶数，如果通过则将其放在一边。

## 流收集器的内置方法

[java.util.stream.Gatherers](https://docs.oracle.com/en%2Fjava%2Fjavase%2F22%2Fdocs%2Fapi%2F%2F/java.base/java/util/stream/Gatherers.html) 接口带有一些内置函数，使你能够构建自定义中间操作。让我们看看每个函数的作用。

### windowFixed 方法

如果你想把所有漂浮的树叶收集容量为 2 的桶里，该怎么办？这对于使用内置函数操作符来说 [非常笨拙](https://blog.payara.fish/introducing-stream-gatherers-jep-461-for-enhanced-java-stream-operations)。它需要将一个单数字数组转换为一个数组数组。

`windowFixed` 方法是一种更简单的方法，可以将你的树叶收集到桶中：

```java
Stream.iterate(0, i -> i + 1)
  .gather(Gatherers.windowFixed(2))
  .limit(5)
  .collect(Collectors.toList());
```

这表示：给我一个基于整数按 1 递增的迭代的流。将每两个元素转换为一个新数组。重复五次。最后，将流转换为 `List`。结果是：

```java
[[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
```

窗口化就像在流上移动一个框架；它允许你拍摄快照。

### windowSliding 方法

另一个窗口化函数是 [windowSliding](https://docs.oracle.com/en%2Fjava%2Fjavase%2F22%2Fdocs%2Fapi%2F%2F/java.base/java/util/stream/Gatherers.html#windowSliding(int))，它与 `windowFixed()` 的工作方式相同，只是每个窗口从源数组中的下一个元素开始，而不是从最后一个窗口的末尾开始。以下是一个示例：

```java
Stream.iterate(0, i -> i + 1)
.gather(Gatherers.windowSliding(2))
.limit(5)
.collect(Collectors.toList());
```

输出是：

```java
[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
```

将 `windowSliding` 的输出与 `windowFixed` 的输出进行比较，你将看到区别。`windowSliding` 中的每个子数组都包含前一个子数组的最后一个元素，而 `windowFixed` 则没有。

### Gatherers.fold 方法

`Gatherers.fold` 就像 [Stream.reduce](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html#reduce-java.util.function.BinaryOperator-) 方法的精炼版本。`fold()` 在哪里比 `reduce()` 更方便，这一点有点微妙。[这篇文章](https://cr.openjdk.org/~vklang/Gatherers.html) 中有一个很好的讨论。以下是作者 Viktor Klang 对 `fold` 和 `reduce` 之间区别的看法：

> 折叠是归约的泛化。在归约中，结果类型与元素类型相同，组合器是关联的，初始值是组合器的标识。对于折叠，这些条件不是必需的，尽管我们放弃了并行化。

因此，我们看到 `reduce` 是一种 `fold`。归约接受一个流并将其转换为单个值。折叠也这样做，但它放宽了要求：1) 返回类型与流元素的类型相同；2) 组合器是关联的；3) `fold` 上的初始化器是一个实际的生成器函数，而不是一个静态值。

第二个要求与并行化相关，我将在稍后详细讨论。在流上调用 `Stream.parallel` 意味着引擎可以将工作分解成多个线程。这只有在运算符是关联的时才有效；也就是说，如果操作的顺序不影响结果，它才有效。

以下是一个简单的 `fold` 用法：

```
Stream.of("hello","world","how","are","you?")
  .gather(
    Gatherers.fold(() -> "", 
      (acc, element) -> acc.isEmpty() ? element : acc + "," + element
    )
   )
  .findFirst()
  .get();
```

此示例获取字符串集合并使用逗号将它们组合在一起。`reduce` 完成了相同的工作：

```
String result = Stream.of("hello", "world", "how", "are", "you?")
  .reduce("", (acc, element) -> acc.isEmpty() ? element : acc + "," + element);
```

您可以看到，使用 `fold`，您定义了一个函数 (`() -> “”`) 而不是一个初始值 (`“”`)。这意味着如果您需要更复杂的初始化器处理，可以使用 `closure` 函数。

现在让我们考虑一下 `fold` 在类型多样性方面的优势。假设我们有一个混合对象类型的流，我们想要统计出现次数：

```
var result = Stream.of(1,"hello", true).gather(Gatherers.fold(() -> 0, (acc, el) -> acc + 1));
// result.findFirst().get() = 3
```

`result var` 是 3。请注意，流包含一个数字、一个字符串和一个布尔值。使用 `reduce` 执行类似的操作很困难，因为累加器参数 (`acc`) 是强类型的：

```
// bad, throws exception:
var result = Stream.of(1, "hello", true).reduce(0, (acc, el) -> acc + 1);
// Error: bad operand types for binary operator '+'
```

我们可以使用 `collector` 来执行此工作：

```
var result2 = Stream.of("apple", "banana", "apple", "orange")
  .collect(Collectors.toMap(word -> word, word -> 1, Integer::sum, HashMap::new));
```

但是，如果我们需要更复杂的逻辑，我们就无法访问初始化器和折叠函数体。

### Gatherers.scan 方法

[Scan](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/util/stream/Gatherers.html#scan(java.util.function.Supplier,java.util.function.BiFunction)) 类似于 `windowFixed`，但它将元素累积到单个元素中，而不是数组中。同样，一个例子可以更清楚地说明（此示例来自 [Javadocs](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/util/stream/Gatherers.html#scan(java.util.function.Supplier,java.util.function.BiFunction))）：

```
Stream.of(1,2,3,4,5,6,7,8,9)
  .gather(
    Gatherers.scan(() -> "", (string, number) -> string + number)
  )
  .toList();
```

输出为：

```
["1", "12", "123", "1234", "12345", "123456", "1234567", "12345678", "123456789"]
```

因此，`scan` 允许我们遍历流元素并累积地将它们组合在一起。

### mapConcurrent 方法

使用 [mapConcurrent](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/util/stream/Gatherers.html#mapConcurrent(int,java.util.function.Function))，您可以指定在运行提供的 `map` 函数时并发使用的最大线程数。将使用虚拟线程。以下是一个简单的示例，它将并发限制为四个线程，同时对数字进行平方（请注意，对于如此简单的数据集，`mapConcurrent` 过于复杂）：

```
Stream.of(1,2,3,4,5).gather(Gatherers.mapConcurrent(4, x -> x * x)).collect(Collectors.toList());
// Result: [1, 4, 9, 16, 25]
```

除了线程最大值之外，`mapConcurrent` 的工作方式与标准 `map` 函数完全相同。

> 流式 API 允许使用 Stream.parallel 并行操作。在处理大型数据集时，这可以提高速度。只要遵守结合律，收集器即可使用此功能。仅在处理大型流时才需要并行操作。

## 结论

在流收集器被提升为一项功能之前，您仍然需要使用 `--enable-preview` 标志来访问 `Gatherer` 接口及其功能。使用 JShell 进行实验的一种简单方法是：`$ jshell --enable-preview`。

虽然它们不是日常需求，但流收集器填补了 Stream API 中一些长期存在的空白，并使开发人员更容易扩展和定制功能性 Java 程序。