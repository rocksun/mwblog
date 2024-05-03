
<!--
title: Go 语言：如何使用 Go Install 命令
cover: https://cdn.thenewstack.io/media/2024/05/9e40387e-monitor-1307227_1280-1.jpg
-->

想要将 Go 程序作为完整的可执行二进制文件运行？Go install 命令会在工作区的 bin 目录中编译并安装应用程序。方法如下。

> 译自 [Golang: How To Use the Go Install Command](https://thenewstack.io/golang-how-to-use-the-go-install-command/)，作者 Jack Wallen。


[Go 语言](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/) 有一个特殊命令，用于将应用程序的二进制包编译并安装到应用程序用户可以访问的路径中。

让我用我们都能理解的方式来解释一下。

首先，我们来谈谈 PATH。PATH 是一个特殊的目录列表，它指示系统在何处查找运行命令所需的执行文件。例如：对于 Linux，运行命令...

```
echo $PATH
```

你可能会在输出中看到类似这样的内容：

```
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

从本质上讲，这意味着任何位于这些目录中的任何可执行文件都可以从文件系统层次结构中的任何位置运行。由于有了 PATH，你无需对 ls 等命令使用完整路径，该路径为：

```
/usr/bin/ls
```

相反，你可以简单地运行 ls 来使用该应用程序。

当你安装 Go 时，它假定 Go 的路径默认为特定位置。要找出该路径在哪里，请发出命令：

```
echo $GOPATH
```

你应该看到类似这样的内容：

```
/home/jack/go/
```

你可以使用以下命令设置此路径：

```
go env -w GOPATH=$HOME/go
```

**请注意** $HOME 等同于 */home/USER*（其中 *USER* 是你的 Linux 用户名）。你也可以在 .bash_profile 文件中进行设置。使用以下命令打开该文件进行编辑：

```
nano ~/.bash_profile
```

在该文件的底部，添加以下内容：

```
export GOPATH=$HOME/go
```

使用以下命令获取文件：

```
source ~/.bash_profile
```

如果你愿意，可以更改该路径，但最好始终保持原样（尤其是在刚开始时）。

好的，现在你已经了解了 GOPATH 是什么，它如何使用？

让我告诉你。

让我们编写一个程序来计算圆周率的近似值。此应用程序的工作原理如下：

1. 导入包  [fmt](https://pkg.go.dev/fmt)、[math](https://pkg.go.dev/math) 和 [math/rand](https://pkg.go.dev/math/rand#Rand)。
2. 设置随机数生成器种子，将   *totalPoints* 设置为 100 万，将 *pointsInsideCircle* 设置为 0。
3. 使用 for 循环迭代  *totalPoints*，将 x 和 y 都设置为随机浮点数 64，并使用这些数字（使用 *math.Sqrt* 函数）将 x*x 和 y*y 相乘。
4. 将  *piApprox* 设置为 *pointsInsideCircle* 和 *totalPoints* 的 float64 的 4 倍。
5. 最后，打印出该值。

以下是代码：

```go
package main

import (
        "fmt"
        "math"
        "math/rand"
)

func main() {
        rand.Seed(42)
        totalPoints := 1000000
        pointsInsideCircle := 0

        for i := 0; i &lt; totalPoints; i++ {
                x := rand.Float64()
                y := rand.Float64()

                distance := math.Sqrt(x*x + y*y)

                if distance &lt; 1 {
                        pointsInsideCircle++
                }
        }

        piApprox := 4 * float64(pointsInsideCircle) / float64(totalPoints)
        fmt.Printf("Using this method, our approximate value of π: %f\n", piApprox)

}
```

使用以下命令创建一个新的项目目录：

```
mkdir ~/randompi
```

使用以下命令切换到该目录：

```
cd randompi
```

使用以下命令初始化项目：

```
go mod init randompi
```

使用以下命令创建 main.go 文件：

```
nano main.go
```

将代码粘贴到该文件中并保存。

使用以下命令构建应用程序：

```
go build
```

你现在应该看到一个名为 *randompi* 的二进制可执行文件。你可以使用以下命令运行新的 Go 应用程序：

```
./randompi
```

太棒了。但是，如果你想能够从其他目录运行该命令怎么办？由于这是 Linux，你可以将它复制到
*/usr/local/bin* 目录，但 Go 已经提供了 GOPATH 可用于此目的。为此，你可以使用 go install，它会将该新二进制文件移动到你的 GOPATH 中。要执行此操作，请发出以下命令：

```
go install
```

如果你发出 ls 命令，你会发现 *randompi* 可执行文件现在已经消失了。它去哪了？Go 已将其移动到你的 GOPATH 中。请记住使用以下命令列出你的 GOPATH：

```
echo $GOPATH
```

这应该会打印出你的 GOPATH。这里的诀窍是 Go 不会仅仅将可执行文件复制到你的 GOPATH 的根目录。相反，它会将其复制到该路径中的 bin 目录。在 Linux 术语中，bin 是二进制文件的常见目录（bin = binary）。要验证可执行文件是否已复制到该路径，请发出以下命令：

```
ls $GOPATH/bin
```

你应该看到 *randompi* 已列出。

如果你[了解 Linux](https://thenewstack.io/tns-linux-sb00-1-intro-to-the-linux-skill-blocks-repository/)，你可能已经理解接下来会发生什么。即使你已经设置了 GOPATH，但这并不意味着它在你的 Linux PATH 中。即使有此警告，Go 也通过 run 命令为你提供了保障。如果你发出以下命令：

```
go run randompi
```

它将在 $GOPATH/bin 中找到二进制可执行文件并运行 randompi 应用程序，其输出将类似于：

```
Using this method, our approximate value of π: 3.139740
```

这里有一个小技巧。

当你使用 *go mod init randompi* 初始化应用程序时，它会创建一个 go.mod 文件，其中将包含类似以下内容：

```
module randompi

go 1.22.1
```

假设你想要将应用程序重命名为 gopi。你所要做的就是编辑 go.mod 文件并将 module randompi 更改为 module gopi。重新构建并重新安装应用程序，然后你可以使用以下命令运行应用程序：

```
go run gopi
```


这就是我的 [Go 朋友](https://thenewstack.io/how-golang-evolves-without-breaking-programs/)，这是使用 `go install` 命令的基础知识。随着您继续学习 [Go 语言](https://thenewstack.io/golang-variables-and-data-types-an-introduction/)，这将成为您的重要工具。

