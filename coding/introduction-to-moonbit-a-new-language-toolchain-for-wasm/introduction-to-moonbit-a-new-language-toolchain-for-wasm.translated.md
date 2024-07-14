# MoonBit 简介：面向 Wasm 的新型语言工具链

![面向 Wasm 的新型语言工具链 MoonBit 的特色图片](https://cdn.thenewstack.io/media/2024/07/27dabd2f-john-ruddock-kefjvnqlr94-unsplash-1024x683.jpg)

[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) 将低级代码编程固有的效率与 Linux 容器中常见的组件可移植性相结合。在某些方面，它与 Docker 竞争。然而，浏览器内的密集工作强烈暗示着它在 AI 领域的未来。

碰巧的是，其他语言不一定能有效地编译成 Wasm，这在一定程度上抵消了拥有可以在浏览器中运行的程序的优势。这就是 **MoonBit** 的用武之地，尽管它

[也可以针对其他后端](https://thenewstack.io/moonbit-wasm-optimized-language-creates-less-code-than-rust/)，例如 JavaScript。通过针对 Wasm，MoonBit 在许多较小的专业设备上获得了免费的优势。

MoonBit 是一个由中国人领导的项目：这解释了它的一些美学，以及代码中偶尔出现的中文注释。如果适用，您应该在使用它之前检查您自己组织的治理系统。

正如 MoonBit 的创建者张洪波 [所说](https://thenewstack.io/moonbit-wasm-optimized-language-creates-less-code-than-rust/)，“我们决定采用容错类型系统的原因是，我们希望 IDE 与编译器共享相同的代码库。” 这使得您在 [Visual Studio Code](https://try.moonbitlang.com/) 中看到的 MoonBit 语言更像是一个一等公民。这就是类型系统很重要的原因——它越强大，IDE 在编译器接管之前就能完成更多有效的工作。

## 如何通过 MoonBit 运行 Wasm

但我们所说的“运行 Wasm”是什么意思？这一点很重要，因为您的操作系统还没有将它视为一个在您的文件系统中自由运行的应用程序。

在我们更深入地了解 MoonBit 之前，让我们确保我们了解如何运行 Wasm。在大多数情况下，我们需要一个 JavaScript 框架来加载和保存它。要在 JavaScript 中使用 WebAssembly，您首先需要将模块拉入内存，然后进行编译/实例化：

```
WebAssembly.instantiateStreaming(fetch("simple.wasm"), importObject).then( (results) => { // Do something with the results! }, );
```

将此与 MoonBit 数独画廊中的示例进行比较 [代码](https://www.moonbitlang.com/gallery/sudoku/)：

```
WebAssembly.instantiateStreaming( fetch("target/wasm/release/build/main/main.wasm"), importObject ).then((obj) => { 
  obj.instance.exports._start(); 
  assign = obj.instance.exports["sudoku/main::ij_assign"] 
  initValues = obj.instance.exports["sudoku/main::initValues"] 
  readValues = obj.instance.exports["sudoku/main::ij_read"] 
  solve = obj.instance.exports["sudoku/main::solveValues"] 
});
```

因此，我们这里需要了解一些事情。`WebAssemby.instantiateStreaming` 方法等待 Wasm 文件加载的 Response 对象（作为 promise）。然后访问 `obj` 实例成员，并调用包含的导出函数。导出清楚地描述了要在 Wasm 代码中调用的模块/方法。

好的，所以这让我们了解了通过 MoonBit 需要做什么；准备一个包含必要导出函数的 Wasm 文件。虽然我们可以在这个 [在线可视化代码网站](https://try.moonbitlang.com/) 中自由地使用 MoonBit 语言，但在本文中，我将重点介绍构建 Wasm 本身。

## 关于 MoonBit 及其 CLI 的更多信息

以下是一些解释：

- **Moon** 是 **MoonBit** 语言的构建系统。
- 您可以使用 **mooncakes.io** 构建第三方包，因此它是一个推测性的包管理系统。
- 如我所述，有一个 Visual Studio 代码插件用于 MoonBit。
- 术语 **module** 与项目同义。
- 为了创建我们看到的导出证据，我们需要 **外部函数接口**，我们将在本文末尾进行检查。

有了这些，让我们深入了解。

我们可以从 Visual Studio 代码开始，并安装 MoonBit 语言扩展。像往常一样，我在我那台可靠的 2015 年款 Macbook 上进行操作，它运行良好。

但我们将重点关注 [CLI 工具](https://www.moonbitlang.com/download/) 来 [管理项目](https://www.moonbitlang.com/docs/build-system-tutorial)。这是因为我想在我的脑海中巩固 Wasm 代码与在浏览器中公开它之间的联系。

打开 Warp，我下载了 CLI 工具：

```
> curl -fsSL https://cli.moonbitlang.com/install/unix.sh | bash
```

然后，我使用 `moon new` 命令创建了一个不错的默认“hello”模块：

该项目在磁盘上的设置显示了库和主包之间的关系：

JSON 包清单为每个包的构建器提供了提示。mod 文件描述了整个模块。第一行声明此模块名为“eastmad/hello”。

**hello.mbt** 文件包含我们熟悉的语言介绍：

```
123
```
```
pub fn hello() -> String { "Hello, world!" } 
这与现代语言中方法或函数的惯用语类似——例如，我们在 [Gleam](https://thenewstack.io/introduction-to-gleam-a-new-functional-programming-language/) 中看到了它。这将 main.mbt 代码保留在 main 包中，并负责将字符串发布到控制台：
```
fn main { println(@lib.hello()) } 
很明显，`@lib.hello()`
是对 **lib** 包的内部调用，该调用已在包描述中解析。
通过 CLI 运行它非常简单：

太棒了。但我想知道它产生了什么。有一个全新的 **target** 目录，所以让我们看一下：

（您可以看到对 [wasm-gc](https://developer.chrome.com/blog/wasmgc#traditional_methods_of_porting_languages_to_the_wasm_runtime) 的引用，它是 Wasm 的垃圾回收版本。本质上，这意味着谁以及如何解决“清理自身”的责任。）

因此，我们得到了承诺的 .**wasm 文件——**它是一个 285 字节长的二进制文件，其中包含可见的问候语，以及示例 javascript 调用开头引用的令牌“_start”——以及其他支持对象。我还没有看到任何像 JavaScript 框架顶部的“导出”的证据；我们所做的只是在内部打印到控制台。

## 与托管运行时交互
为了在嵌入到浏览器中时与托管运行时交互，MoonBit 引用了 [外部函数接口](https://www.moonbitlang.com/docs/ffi-and-wasm-host) (FFI)。让我们通过快速了解一下来结束我们的介绍。

要在 MoonBit 中声明一个外部函数，您可以这样做：

```
fn cos(d : Double) -> Double = "Math" "cos" 
```
实际函数本身（主体）已被推测的模块名称和函数名称替换。当我们从 JavaScript 调用它时，您将在下面看到它被重建。
然后，您可以在模块 **moon.pkg.json** 文件中描述关系：

```
{ "link": { "wasm-gc": { "exports": [ "add", "fib:test" ] }, "js": { "exports": [ "add", "fib:test" ], "format": "esm" } }} 
```
在此示例中，函数 `add`
和 `fib`
被导出，函数 `fib`
将以 `test`
的名称导出。
最后，对于我们的数学示例，JavaScript 调用框架看起来像这样：

```
WebAssembly.instantiateStreaming(fetch("xxx.wasm"), { Math: { cos: (d) => Math.cos(d), }, }); 
```
这让我们几乎回到了原点。大多数这些元素在 [数独](https://www.moonbitlang.com/gallery/sudoku/) 示例中可见。
虽然 MoonBit 几乎可以投入生产（查看 [此处状态](https://www.moonbitlang.com/docs/syntax)），但它已经描述了一种现代语言以及创建 Wasm 项目的工作流程。我预计小型 LLM 将在不久的将来有效地打包到 Wasm 格式中。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)
```