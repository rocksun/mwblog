# Gleam 简介，一种新的函数式编程语言

![Gleam，一种新的函数式编程语言的特色图片](https://cdn.thenewstack.io/media/2024/06/5af404eb-getty-images-n7fry417ibk-unsplash-1024x683.jpg)

当我的同事读完我的 [Virgil 帖子](https://thenewstack.io/introduction-to-virgil-a-new-language-by-wasms-co-creator/) 后，他立刻建议我看看 [Gleam](http://gleam.run)。它很酷且很新——版本 1 在今年 [3 月](https://gleam.run/news/gleam-version-1/) 发布——并且在编程生活的函数式方面表现得很出色。

Gleam 是一种类型安全的函数式编程语言，用于构建可扩展的并发系统。它编译为 [Erlang](https://thenewstack.io/past-present-future-erlang/) 和 [JavaScript](https://thenewstack.io/javascript/)，因此与其他“BEAM”语言（如 Erlang 和 Elixir）具有直接的互操作性。（BEAM 是在 Erlang 运行时系统中执行用户代码的虚拟机。我相信它的缩写是 *Bogdan’s Erlang Abstract Machine*。别问。）

Erlang 是一种早期的电信行业语言，非常注重并发性和容错性。它的做事方式仍然受到尊重，并且解释了 [Elixir](https://thenewstack.io/past-present-future-erlang/) 的流行。在这篇文章中，我不会假设你熟悉这些；实际上，Gleam 特别友好，因此它也没有做出太多假设。

让我们从 *hello world* 开始：

```
import gleam/io
pub fn main() {
  io.println("hello world!")
}
```

这与 [Zig](https://thenewstack.io/introduction-to-zig-a-potential-heir-to-c/) 中的相同内容非常相似。

有一个非常愉快的 [语言之旅](https://tour.gleam.run/)，它利用 Gleam 编译到 JavaScript 来提供动态检查。你还可以将其用作游乐场。[安装 Gleam](https://gleam.run/getting-started/installing/) 也意味着安装 Erlang。对于我的 Mac，我只使用了 Homebrew：

```
brew install gleam
```

Homebrew 会自动安装 Erlang。

Gleam 带有一个模板（或项目）生成器，很像 Rails。因此，要创建一个新的 *hello* 项目，我只需键入：

目前还没有节省时间，“hello world”风格的一行代码已经作为 **hello.gleam** 中的默认代码存在：

如果我运行整个项目：

请注意，这两个包仅在第一次运行时编译。

## 包管理

有两个 *.toml* 文件（显然是 *Tom’s Own Markup Language*。别问），它们充当配置。

由于它们应该很简单，我们可以快速浏览一下。在 **gleam.toml:** 中：

```
[dependencies]
gleam_stdlib = ">= 0.34.0 and < 2.0.0"
```

请注意，它们有一个 *版本约束*——提到最大版本以减少不兼容性。

下载和使用的实际版本在 **manifest.toml** 中提到。

如果我们 [遵循](https://gleam.run/writing-gleam/) 一个简单的示例，我们可以学习一些 Gleam 并使用包管理器。我们将添加几个包，并编写一些代码来打印环境变量。我将使用相同的 *hello* 项目模板，但插入了新代码。

首先，我们将添加新包以允许读取环境（ *envoy*）和读取命令行参数（ *argv*）——你可能希望它们是内置的，但可能反映系统差异。

因此，让我们用打印环境变量的代码替换 **hello.gleam** 中的代码：

```
import argv
import envoy
import gleam/io
import gleam/result
pub fn main() {
  case argv.load().arguments {
    ["get", name] -> get(name)
    _ -> io.println("Usage: get <name>")
  }
}
fn get(name: String) -> Nil {
  let value = envoy.get(name) |> result.unwrap("")
  io.println(format_pair(name, value))
}
fn format_pair(name: String, value: String) -> String {
  name <> "=" <> value
}
```

添加到公共 main 入口点，我们有两个函数。它们使用与我们在 Virgil 中看到完全相同的格式。事实证明，类型注释是可选的，但被认为是良好的实践。现在，我们变得有点函数化。

*argv* 加载执行你期望的操作，并拉入一个列表，该列表希望恰好包含两个字符串——第一个字符串等于“get”。这在 case 语句中使用。

简单说一下，Gleam case 比大多数非函数式语言中的更灵活。在这里，我们看到列表的内容正在被比较：

```
let result = case x {
  [] -> "Empty list"
  [1] -> "List of just 1"
  [4, ..] -> "List starting with 4"
  [_, _] -> "List of 2 elements"
  _ -> "Some other list"
}
```

因此， [模式可以在 case 语句中进行比较](https://tour.gleam.run/flow-control/list-patterns/)。下划线 _ 表示默认值，并且可能的情况被穷举检查。

回到我们的环境变量读取代码，如果模式 *不是* 两个字符串的列表，那么将显示帮助文本。否则，它将调用 *get* 函数。
我们看到了管道函数，它只是帮助使从左到右的长函数调用更具可读性。

|
1
|
let value = envoy.get(name) |> result.unwrap("")
这与以下内容相同：

|
1
|
let value = result.unwrap(envoy.get(name),"")
因为 Gleam 不会抛出异常，它使用内置的
[Result](https://tour.gleam.run/data-types/results/) 类型，而 *unwrap* 获取正确的路径值。

最后的奇点是：

|
1
|
name <> "=" <> value
…这只是字符串连接。

我在这里运行它，第二次使用必需的参数：

Gleam 没有
null、没有隐式转换，也没有异常。因此，如果它编译，那么你很好。此外，没有数字运算符重载，因此用于添加整数的代码与用于添加浮点数的代码不同：

|
1
2
|
io.debug(1 + 1) //ints
io.debug(1.0 +. 1.5) //floats
相等适用于任何类型。最好通过使用函数式语言一段时间来体验不变性的总体概念，因此我不会对此进行详细说明。它确实有助于消除一整套错误。

## 代数数据类型

最后，我们看到了
**代数数据类型** (ADT) 用于 [Virgil](https://thenewstack.io/introduction-to-virgil-a-new-language-by-wasms-co-creator/)，因此我热衷于了解 Gleam 中的等效项如何工作。事实上，我们已经看到了
case 语句的使用。

我们得到自定义类型，我们对其进行模式匹配。因此，我们已经完成了一部分：

|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
|
pub type Season {
Spring
Summer
Autumn
Winter
}
fn weather(season: Season) -> String {
case season {
Spring -> "Mild"
Summer -> "Hot"
Autumn -> "Windy"
Winter -> "Cold"
}
}
类型可以在
[记录](https://tour.gleam.run/data-types/records/) 中保存数据，这就是我们接近我的 Virgil 示例的方式：

|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
|
import gleam/io
pub type Travel {
Walk(hours: Int)
Cycle(hours: Int)
Drive(hours: Int, speed: Int)
}
pub fn main() {
let walking = Walk(1)
let cycling = Cycle(1)
let bus_trip = Drive(2, 50)
let trip = [walking, cycling, bus_trip]
io.debug(trip)
}
// [Walk(hours: 1), Cycle(hours: 1), Drive(hours: 2, speed: 50)]
我认为我无法在类型内部关联一个方法，但我可以访问记录值以获得与我们在 Virgil 中获得的结果类似的结果。我将把它留给更流利的用户作为练习！

对于像我这样不太使用函数式代码的人来说，Gleam 非常容易理解，并且不会立即用“柯里化”和其他函数式冲击之类的术语来让我不知所措。但是，如果你还没有成为拥护者，它应该是一种让你欣赏编程的不可变优势的好方法。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)