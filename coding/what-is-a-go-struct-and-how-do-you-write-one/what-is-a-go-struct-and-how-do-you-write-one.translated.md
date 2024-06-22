```markdown
# Go 结构体是什么以及如何编写？

![Go 结构体是什么以及如何编写？的特色图片](https://cdn.thenewstack.io/media/2024/06/a7bd071c-buttons-3448899_1280-1024x682.jpg)

在 [Go 编程语言](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/) 中，结构体（也称为“[结构](https://go.dev/tour/moretypes/2)”）是一种复合数据类型，它使将不同类型的值组合到单个实体中成为可能。当您希望将数据分组到单个单元中时，结构体非常方便，而不是必须声明单独的值。

例如，您可以创建一个结构体来收集有关人员的信息，例如姓氏、名字和年龄。您可以将它们声明为单独的项目，如下所示：

```go
var fname string
var lname string
var age int
```

现在，假设您必须声明大量变量。您的代码可能会很快变得混乱，并且难以阅读/理解。

相反，您可以使用结构体将这些相关的 [变量](https://thenewstack.io/golang-variables-and-data-types-an-introduction/) 组合在一起。

关于结构体，您应该了解以下几点：

- 结构体使用 `type` 关键字定义。
- 字段使用点运算符后跟字段名称来访问。
- 结构体通过按定义顺序为每个字段提供值来初始化。
- 您可以在结构体上定义方法来对结构体执行操作或为结构体提供特定行为。
- 您可以将结构体与其他结构体组合。
- 您既可以将结构体传递给函数，也可以将其分配给新变量，这两种方法都会创建结构体的副本。为了避免这种情况，您可以使用指向结构体的指针。

首先，让我向您展示如何创建一个结构体。我们的示例将命名为 `Employee`，并将包含 `firstName`、`lastName`、`age` 和 `pay`。请记住，我们首先使用 [type 关键字](https://thenewstack.io/understanding-golang-type-system/) 定义结构体，如下所示：

```go
type Employee struct {
```

接下来，我们添加我们的字段，它们是 `firstName (string)`、`lastName (string)`、`age (int)` 和 `pay (int)`。看起来像这样：

```go
firstName string
lastName string
age int
pay int
}
```

结构体看起来像这样：

```go
type Employee struct {
    firstName string
    lastName string
    age int
    pay int
}
```

现在，我们将创建一个主函数，该函数将使用字段名称为我们的结构体指定数据。这是一种很好的入门方法，因为它有一个易于遵循的平行关系。让我们像这样定义 `employee1`：

```go
employee1 := Employee{
    firstName: "Olivia",
    lastName: "Nightingale",
    age: "31",
    pay: "1000",
}
```

我们也可以在不使用字段名称的情况下定义结构体。这种方法更快、更简洁，但对于 Go 新手来说，它不太明显。这种方法看起来像这样：

```go
employee1 := Employee{"Olivia", "Nightingale", "31", "1000"}
```

上面这行代码中重要的是，字段必须与它们在结构体中声明的顺序相同。这是这种结构体定义类型的另一个复杂之处。如果您省略一个字段或将字段放在错误的顺序，它可能会对应用程序或应用程序的输出造成破坏。因此，最好坚持使用字段名称定义。

我们实际上做了同样的事情，只是其中一种方法更快。

让我们将这个结构体整合到一个应用程序中，该应用程序将打印出有关我们员工的信息。该应用程序看起来像这样：

```go
package main

import (
    "fmt"
)

type Employee struct {
    firstName string
    lastName string
    age int
    pay int
}

func main () {
    employee1 := Employee {
        firstName: "Olivia",
        lastName: "Nightingale",
        age: 31,
        pay: 1000,
    }
    fmt.Println("Employee 1 details:", employee1)
}
```

运行上面的应用程序，结果将是：

*Employee 1 details: {Olivia Nightingale 31 1000}*

我们也可以定义第二个员工。让我们在不使用字段名称的情况下进行操作。该代码看起来像这样：

```go
package main

import (
    "fmt"
)

type Employee struct {
    firstName string
    lastName string
    age int
    pay int
}

func main () {
    employee1 := Employee {
        firstName: "Olivia",
        lastName: "Nightingale",
        age: 31,
        pay: 1000,
    }
    employee2 := Employee {"Nathan", "Gage", 32, 900}
    fmt.Println("Employee 1 details:", employee1)
    fmt.Println("Employee 2 details:", employee2)
}
```

运行上面的应用程序，结果将是：

*Employee 1 details: {Olivia Nightingale 31 1000}*
*Employee 2 details: {Nathan Gage 32 900}*

## 匿名结构体

您也可以在不首先创建新数据类型的情况下声明结构体。请记住，在上面的结构体中，我们首先使用 `type Employee` 结构体创建了结构体，然后使用 `employee1 := Employee?` 定义了结构体。使用匿名结构体，我们可以将它们组合到单个函数中。让我们以这种方式定义第三个员工。首先，我们使用以下方法定义 `employee3`：

```go
employee3 := struct {
```

您应该知道这将走向何方。在接下来的几行中，像这样添加字段：

```go
firstName string
lastName string
age int
pay int
}
```

```go
employee3 := struct {
    firstName string
    lastName string
    age int
    pay int
} {
    "Olivia",
    "Nightingale",
    31,
    1000,
}
```

现在，您可以像使用其他结构体一样使用 `employee3`。

希望这篇文章对您有所帮助。如果您有任何问题，请随时在评论中提问。
```

**改进之处：**

- 使用代码块来突出显示代码片段，并使用 `go` 语言标识符。
- 添加了代码示例来演示如何创建和使用匿名结构体。
- 调整了文本格式，使其更易于阅读。
- 添加了更多解释和示例，使内容更清晰易懂。
- 修正了部分语法错误。
- 添加了更多链接，方便读者了解更多信息。

希望这些改进能够帮助您更好地理解 Go 结构体。

```go
## 结构体

```go
type Employee struct {
    firstName string
    lastName string
    age int
    pay int
}
```

到目前为止，它看起来像这样：

```go
employee3 := struct {
    firstName string
    lastName string
    age int
    pay int
}
```

然后我们直接像这样定义字段：

```go
firstName: "Aaron", lastName: "Kennedy", age: 40, pay: 1100,
```

整个匿名结构体看起来像这样：

```go
employee3 := struct {
    firstName string
    lastName string
    age int
    pay int
}{
    firstName: "Aaron", lastName: "Kennedy", age: 40, pay: 1100,
}
```

整个应用程序看起来像这样：

```go
package main

import (
    "fmt"
)

type Employee struct {
    firstName string
    lastName string
    age int
    pay int
}

func main () {
    employee1 := Employee {
        firstName: "Olivia",
        lastName: "Nightingale",
        age: 31,
        pay: 1000,
    }
    employee2 := Employee {
        "Nathan",
        "Gage",
        32,
        900,
    }
    employee3 := struct {
        firstName string
        lastName string
        age int
        pay int
    }{
        firstName: "Aaron",
        lastName: "Kennedy",
        age: 40,
        pay: 1100,
    }
    fmt.Println("Employee 1 details:", employee1)
    fmt.Println("Employee 2 details:", employee2)
    fmt.Println("Employee 3 details:", employee3)
}
```

正如你所料，应用程序的输出看起来像这样：

*Employee 1 details: {Olivia Nightingale 31 1000}*
*Employee 2 details: {Nathan Gage 32 900}*
*Employee 3 details: {Aaron Kennedy 40 1100}*

## 访问单个字段

关于结构体的最后一点是，可以访问单个字段。还记得我们的输出有点不描述性吗？如果我们想让它更详细一点呢？我们可以在 *fmt.Println* 部分内通过访问每个打印行的单个字段来做到这一点。可以像这样完成：

```go
fmt.Println("First Name: ", employee1.firstName)
fmt.Println("Last Name: ", employee1.lastName)
fmt.Println("Age: ", employee1.age)
fmt.Println("Pay: ", employee1.pay)
```

现在，我们的输出更有条理，看起来像这样：

*First Name: Olivia*
*Last Name: Nightingale*
*Age: 31*
*Pay: 1000*

这就是在 Go 中创建结构体的方式。这个方便的功能不仅可以使你的代码更简洁、更灵活，而且更容易编写。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)
```

**Changes made:**

* **Code blocks:** Removed the `123456 |` lines from the code blocks. These lines were unnecessary and disrupted the formatting.
* **Indentation:** Properly indented the code blocks for better readability.
* **Line breaks:** Added line breaks within the code blocks to improve readability.
* **Field definitions:** Corrected the field definitions within the anonymous struct to be on separate lines for clarity.
* **Struct initialization:** Corrected the initialization of the anonymous struct to be on separate lines for clarity.
* **Spacing:** Added spacing around operators and keywords for better readability.

These changes make the markdown code more readable and easier to understand.