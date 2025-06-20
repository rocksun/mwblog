你是否已经开始了你的编程之旅？或者你只是最近才开始，并且发现学习你的第一门 [编程语言](https://thenewstack.io/programming-languages/) （或一门新的编程语言）比你想象的更具挑战性。

你读过书，研究过在线教程，甚至向其他人寻求帮助，但似乎没有任何东西能让你掌握。

如果还有另一种方法呢？如果有一种方法不仅可以帮助你理解概念，甚至可以向你展示你想要做的具体例子呢？

那就是 AI。

我知道，我知道……你可能对使用 AI 来编写代码的想法感到摇头，因为这感觉像作弊。但如果不是呢？如果你不只是用它来为你做工作，而是用它作为一种工具来帮助你快速掌握可能是一项艰巨的任务呢？

我写过很多关于 AI 的文章，并且对此有一些非常强烈的感受。我坚信 AI 不应该被用于创造的目的，但是当 AI 被用于研究或作为学习工具时，我完全赞成。

我测试了几种不同的 AI 解决方案用于这些目的，当涉及到学习编码时，有一个解决方案比其他解决方案更胜一筹，那就是 [Warp Terminal](https://www.warp.dev/) 中的 AI。

## 为什么选择 Warp Terminal？

首先，[Warp 是一个终端应用程序](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/)，因此它已经具有优势，因为它专为那些几乎在任何事情上都使用终端应用程序的人而开发。而且它内置的 AI 还可以帮助你学习 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 命令（因为它允许你输入人类可读的语言，然后将该语言转换为命令），这使其比其他 AI 解决方案更具优势。

关于 Warp Terminal 的另一件事是，它不仅仅是编写你要求的代码。使用 Warp Terminal，你可以查询 AI 来创建一个程序，并将其代码保存到文件中。然后它会向你展示如何（如果需要）编译和运行该程序。

它真的就是这么好用和简单。

让我用一个用 [C++](https://thenewstack.io/introduction-to-c-programming-language/) 编写的简单的 Hello, World 应用程序来演示一下。

## 如何使用 Warp Terminal 编写你的第一段代码

在你安装 Warp Terminal（适用于 Linux 和 Windows）之后，从你的桌面菜单打开该应用程序，你应该会看到一个非常简单的提示符。但是，当你输入以下内容时会发生什么：

突然之间，事情发生了变化，Warp 开始工作。它最终会向你展示该应用程序的代码（图 1）。

![](https://cdn.thenewstack.io/media/2025/06/96a7a20f-warpapp1.jpg)

图 1. 由 Warp Terminal 创建的基本 C++ 应用程序。

你还应该看到一排选项，用于取消（Ctrl+C）、细化（R）、编辑（E）和应用更改（Enter）。如果你点击 Enter，Warp 将使用它创建的代码并创建一个文件（恰如其分地命名为 hello\_world.cpp）。完成后，它将向你展示编译命令 (g++ hello\_world.cpp) 和运行命令 (./hello\_world)。

如果你查看当前工作目录，你将看到编译和运行代码所需的所有文件，而你所要做的就是告诉 Warp 创建它。

但是，如果你不理解代码是如何工作的会怎么样？Warp 的 AI 也可以帮助你。

让我们看一下 Warp 创建的 Hello, World 文件，它看起来像这样：

如果你是 C++ 的新手，并且不知道上面的内容是什么意思呢？让我们询问 Warp 的 AI。例如：

响应如下所示：

它继续进行描述，但你已经明白了。

然后你可以逐行询问每段代码的作用，以便你更好地了解 C++ Hello, World 应用程序是如何工作的。

你也可以采取更具挑战性的路线。

这一次，我要求 Warp 在 C++ 中为 Warp Terminal 创建一个图形用户界面 (GUI) 应用程序。几乎立即，Warp 发现我没有安装必要的 GUI 工具包，而是选择了一条不同的路线：– X11（而不是 gtk4 库）。然后 Warp 呈现了必要的代码。我点击 Enter 以应用更改（由于 Warp 发现并解决了一些问题，因此必须多次执行此操作），然后 Warp 向我展示了下一步，其中包括安装 libgtk-3-dev，然后是编译和运行命令。

它奏效了。

我还可以打开 Warp 为该应用程序创建的文件，并要求它解释每一行的作用，以便我可以开始更好地了解 C++ 的工作原理。

这几乎可以用于任何编程语言，例如 [Python](https://thenewstack.io/python/)、[JavaScript](https://thenewstack.io/javascript/)、[Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/)、[Go](https://thenewstack.io/introduction-to-go-programming-language/)…… 你能想到的都可以。

虽然让 AI 为你做工作这个想法让我感到不舒服，但是为了能够快速掌握一门语言，以便我可以正确地完成工作，我完全赞成。AI 是一种非常有价值的工具，可以用于好的方面，而且在我看来，让它帮助你学习编程艺术就属于这一类。