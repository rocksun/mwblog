# Go 变量和数据类型：简介

![Go 变量和数据类型：简介的特色图片](https://cdn.thenewstack.io/media/2024/04/786e8015-cat-7928232_1280-1024x703.png)

既然你已经
[尝鲜](https://thenewstack.io/learn-the-go-programming-language-start-here/) 了 [Go 语言的工作原理](https://thenewstack.io/import-and-use-a-third-party-package-in-golang/)，现在我们退一步来讨论变量和数据类型。如果你曾经使用过任何 [其他编程语言](https://thenewstack.io/best-practices-for-naming-variables-what-the-research-shows/)，你应该已经 [熟悉这些概念](https://thenewstack.io/python-for-beginners-data-types/)。但是，如果 [Go](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/) 是你的第一门语言，那么理解变量和数据类型的目的以及它们如何发挥作用非常重要。

如果不了解变量和数据类型，你将很难快速掌握 Go（或任何语言）。但别担心，变量和数据类型都不是复杂的概念。事实上，变量非常简单。至于数据类型，你只需要知道类型及其工作原理即可。

## 变量

一个典型的变量以键值对的形式工作，如下所示：

键 = 值

非常简单。

在 Go 中，你可以声明一个变量，定义它的数据类型，然后给它一个值。语法如下所示：

```go
var 变量名 数据类型
```

我们用 `var` 声明变量，用
*变量名* 给变量命名，用 *数据类型* 定义数据类型。假设我们正在为名字创建一个变量

```go
var fname string
```

我们所做的是声明一个名为
*fname*（表示名字）的变量，类型为字符串。我们使用字符串，因为名字将由字符 a/A-z/Z 组成（稍后详细介绍数据类型）。

我们还可以在同一行中用一个值初始化该变量（如果我们愿意），如下所示：

```go
var fname string = New
```

让我们在一段代码块中使用它，同时为姓氏也创建一个变量。请记住（从我们之前的教程中），我们必须使用以下命令调用主包：

```go
package main
```

接下来，我们必须使用以下行从 main 中导入“fmt”：

```go
import ("fmt")
```

现在，我们将创建一个函数来定义我们的变量并打印名字和姓氏。该函数如下所示：

```go
func main() {
    var fname string = "New"
    var lname string = "Stack"
    fmt.Println(fname,lname)
}
```

我们的整个应用程序（名为 vars.go）如下所示：

```go
package main

import ("fmt")

func main() {
    var fname string = "New"
    var lname string = "Stack"
    fmt.Println(fname,lname)
}
```

我们使用以下命令运行应用程序：

```go
go run vars.go
```

输出将是：

```
New Stack
```

简单有效。

但是，如何使用用户输入的数据初始化变量？这是一个很酷的技巧。我们将坚持上面的示例。为此，我们将使用
*fmt.Scan* 函数从主包中。在调用 *main* 和 *fmt* 之后，我们首先要做的（在我们的函数中）是用以下命令声明我们的变量：

```go
var fname string
var lname string
```

接下来，我们写四行代码：

- 指示用户输入他们的名字。
- 接受名字的输入。
- 指示用户输入他们的姓氏。
- 接受姓氏的输入。

此部分如下所示：

```go
fmt.Println("Enter your first name:")
fmt.Scan(&fname)
fmt.Println("Enter your last name:")
fmt.Scan(&lname)
```

最后，我们写一行来打印所有内容，如下所示：

```go
fmt.Println("Your name is:", fname, lname)
```

整个代码如下所示：

```go
package main

import ("fmt")

func main() {
    var fname string
    var lname string
    fmt.Println("Enter your first name:")
    fmt.Scan(&fname)
    fmt.Println("Enter your last name:")
    fmt.Scan(&lname)
    fmt.Println("Your name is:", fname, lname)
}
```

当你运行应用程序时，它会询问名字，然后询问姓氏，并打印出这两个名字。

## 数据类型

Go 有许多包含的数据类型，分为三类：

- 基本类型（bool、int、float64、complex128、string）
- 聚合类型（数组、切片、结构）
- 引用类型（指针、通道、映射、接口）

基本类型很明显，定义如下：

- `var boolean bool = true`
- `var integer int = 100`
- `var float float64 = 100.09`
- `var comp complex128 = 1 + 3i`
- `var st string = “New Stack”`

它们分解如下：

- 布尔值为 true/false
- int 是一个整数
- float64 是一个小数
- complext128 是所有复数的集合，具有浮点数和虚数分量
- string 是一个字符串

接下来，我们有聚合类型，它可以采用以下形式：

- `someArray := [10]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}`
- `var slice []int = someArray[0:5]`

结构聚合类型有点复杂，因为它可以包含自定义字段。你像这样声明一个结构：

```go
type Box struct {
    X int
    Y int
}
```

然后你可以像这样初始化这些值：

```go
b := Box{1,2}
```

最后，还有引用类型，例如指针，它包含它们所基于的变量的内存地址。指针使用 * 字符，如下所示：

```go
var p *int
```

然后我们可以声明如下内容：

```go
myInteger := 100
```

然后我们像这样从变量创建指针：

```go
p = &myInteger
```
我们稍后将深入探讨这些概念，但了解 Go 中包含的基本类型非常重要。

恭喜您在 Go 语言中又迈进了一步。它可能不如 [Python 简单](https://thenewstack.io/an-introduction-to-python-for-non-programmers/)，但它远没有 C、C++ 或类似编程语言那么复杂。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。