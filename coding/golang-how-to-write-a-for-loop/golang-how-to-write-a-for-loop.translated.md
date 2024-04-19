# Go 语言：如何编写 for 循环

![Go 语言：如何编写 for 循环的特色图片](https://cdn.thenewstack.io/media/2022/05/57bb2a1f-golang.png)

## 编程

[循环](https://thenewstack.io/how-to-use-loops-in-python/): 你了解它们，你喜爱它们。或者你并不了解它们，并且不确定它们对于几乎所有编程语言来说有多么重要。[Go 语言](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/) 也不例外，它使用 for 循环来重复一段代码块，直到满足给定的条件。for 循环实际上是 Go 语言中最基本的循环类型，但它是你经常会用到的循环类型。

你可能使用 [for 循环](https://thenewstack.io/golang-1-22-redefines-the-for-loop-for-easier-concurrency/) 的原因多种多样（取决于你的需求）。例如，你可能希望多次打印一条语句。你可以使用 for 循环来处理此过程，而不是一遍又一遍地编写相同的 *fmt.print()* 语句。

for 循环包含以下部分：

- 初始化 - 初始化或声明变量。
- 条件 - 用于评估条件。只要条件为真，循环就会执行。
- 更新 - 每次执行循环时都会更新初始化的值。
- 语句 - 执行的内容

for 循环的基本语法如下所示：

| 行数 | 语法 |
|---|---|
| 1 | `for 初始化; 条件; 更新 {` |
| 2 | 语句 |
| 3 | `}` |

还记得我们上面提到的打印示例吗？假设我们想打印 10 次 New Stack Rocks。是的，我们可以编写一个 Go 程序，它只需像这样使用 *fmt.Println()* 函数 10 次：

```go
package main

import "fmt"

func main() {
    fmt.Println("New Stack Rocks")
    fmt.Println("New Stack Rocks")
    fmt.Println("New Stack Rocks")
    fmt.Println("New Stack Rocks")
    fmt.Println("New Stack Rocks")
    fmt.Println("New Stack Rocks")
    fmt.Println("New Stack Rocks")
    fmt.Println("New Stack Rocks")
    fmt.Println("New Stack Rocks")
    fmt.Println("New Stack Rocks")
}
```

如果你运行以上代码，它实际上会打印以下内容：

```
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
*New Stack Rocks*
```

当然，你不想以这种方式做事。它不仅效率低下，而且也是引入错误的好方法，并且效率不高。相反，我们将使用 for 循环来完成相同的事情，如下所示：

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 10; i++ {
        fmt.Println("New Stack Rocks")
    }
}
```

你已经知道我们使用前两行调用 main 包并导入 fmt。下一行 *func main()* 初始化 main 包。然后使用以下内容创建我们的 for 循环：

- `i := 1` - 初始化，将 i 设置为 1。
- `i <= 10` - 条件，表示只要 i 小于或等于 10，就继续。
- `i++` - 更新，表示将 1 添加到 I 的前一个值。
- `fmt.Println(“New Stack Rocks”)` - 只要 i <= 10，就会执行我们的打印语句。

沿着这些相同的思路，你甚至可以创建一个无限循环。你为什么要使用无限循环？它们实际上有自己的用途。例如，你可能希望编写必须持续运行直到停止的应用程序代码，例如 Web 服务器或在应用程序手动停止之前需要持续用户输入的应用程序。

可以使用没有条件语句的 for 循环来完成无限循环。因此，for 循环可能如下所示：

```go
for {
    fmt.Println("New Stack Rocks")
}
```

整个应用程序可能如下所示：

```go
package main

import "fmt"

func main() {
    for {
        fmt.Println("New Stack Rocks")
    }
}
```

如果你运行以上代码，它将继续打印 New Stack Rocks，直到你使用 Ctrl+C 键盘快捷键之类的命令将其终止。

for 循环还有另一个非常酷的技巧，其中包括 range 关键字。range 关键字用于迭代数据结构中的元素。Range 可用于数组、切片、字符串、映射和通道。让我向你展示一个在 for 循环中使用 range 关键字迭代字符串的示例。

带有 range 关键字的 for 循环将如下所示：

```go
for i, ch := range "New Stack Rocks" {
    fmt.Printf("%#U starts a position %d\n", ch, i)
}
```

此 for 循环的作用是遍历字符串并打印字母和位置，直到完成。完整代码如下所示：

```go
package main

import "fmt"

func main() {
    for i, ch := range "New Stack Rocks" {
        fmt.Printf("%#U starts a position %d\n", ch, i)
    }
}
```

如果你运行此代码，输出将是：

```
*U+004E ‘N’ starts a position 0*
*U+0065 ‘e’ starts a position 1*
*U+0077 ‘w’ starts a position 2*
*U+0020 ‘ ‘ starts a position 3*
*U+0053 ‘S’ starts a position 4*
*U+0074 ‘t’ starts a position 5*
```
**U+0061 ‘a’** 开始位置 6
**U+0063 ‘c’** 开始位置 7
**U+006B ‘k’** 开始位置 8
**U+0020 ‘ ’** 开始位置 9
**U+0052 ‘R’** 开始位置 10
**U+006F ‘o’** 开始位置 11
**U+0063 ‘c’** 开始位置 12
**U+006B ‘k’** 开始位置 13
**U+0073 ‘s’** 开始位置 14

请注意，我们使用 `fmt.Printf()` 而不是 `fmt.Println()`. 原因是 `Printf` 允许你设置数字、变量和字符串的格式，而 `Println` 只是按原样打印行。如果你使用 `fmt.Println`，输出将是：`%#U 开始位置 %d 78 0`

显然，这是不正确的，所以我们必须使用 `fmt.Printf()`.

这就是在你最喜欢的编程语言中编写 for 循环的方法。现在你已经了解了它的工作原理，你准备好更进一步了吗？如果是，准备，开始，Go！

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等内容。