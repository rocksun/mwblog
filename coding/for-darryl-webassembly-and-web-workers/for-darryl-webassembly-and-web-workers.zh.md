我们都曾经历过网页冻结，然后是无休止的刷新、沮丧的叹息和偶尔的跺脚，却只看到旋转的加载图标。在许多情况下，这是由[JavaScript](https://thenewstack.io/introduction-to-javascript/)主线程的瓶颈引起的。

主线程是一条单行道，浏览器在此严格按顺序处理所有内容。它处理点击、管理滚动、渲染动画并执行你的逻辑。因为它一次只能做一件事，所以将大量计算加入其中会造成大规模的交通堵塞。当主线程过载时，整个用户界面就会停止响应。

[我们最近讨论了很多关于WebAssembly (Wasm) 的内容](https://thenewstack.io/when-should-javascript-devs-use-the-power-of-webassembly/)，所以Wasm在这里是一个很好的解决方案也就不足为奇了。通过将Wasm的原始能力与[Web Workers](https://thenewstack.io/leveraging-web-workers-to-safely-store-access-tokens/)结合起来，我们可以将那些繁重的计算转移到后台线程。这减轻了主线程的压力，让你的用户可以继续滚动和点击而不会中断。

为了展示使用C语言和Wasm进行计算相比JavaScript的优势，本教程将帮助你构建一个高性能的[斐波那契计算器](https://elementor.com/tools/fibonacci-calculator/)。然后我们将使用由Web Worker驱动的Wasm递归运行斐波那契数列，并使用JavaScript进行计算，这样你就可以看到两者的计时对比。

通过将密集的数学计算卸载到后台线程，我们将演示如何在处理器负载很重的情况下，仍能保持用户界面的功能性和流畅性。尽管递归斐波那契算法不适用于实际应用，但这个项目可以作为保持Web应用响应性的蓝图。

让我们开始吧。

首先，确保你有所需的一切。

创建你的项目结构。

在你的项目中打开一个终端，导航到`wasm-worker-demo`。进入该文件夹后，输入`ls`并确保你看到你的文件：`index.html`、`main.js`、`worker.js`、`compute.c`。确认你在正确的位置后，我们需要下载[Emscripten SDK](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/)。

Emscripten SDK将C/C++编译成Wasm。没有它，我们就无法进行下一步。在你的终端中，输入以下命令：

这将在此你的当前目录中添加一个名为`emsdk`的文件夹。

使用命令`cd emsdk`进入`emsdk`文件夹。

安装最新版本的Emscripten：`./emsdk install latest`

激活SDK，以便你的终端可以使用它：`./emsdk activate latest`

最后一步是为本次终端会话设置环境变量：`source ./emsdk_env.sh`

使用命令`emcc -v`确认设置准确。

回到终端中的主项目文件夹。

我们准备好开始构建文件了。

## 在C语言中构建Wasm计算逻辑

让我们从`compute.c`文件开始。我们将在本次演示中使用的算法是递归斐波那契数列。这会唤起所有编程学校毕业生的噩梦。尽管此算法对于生产级应用程序效率低下，但它非常适合本次演示。它会创建数十亿次函数调用，并将CPU推向极限。

## Emscripten：C到Wasm

Emscripten将我们的C代码编译成一个.wasm二进制文件和一个.js“胶水”文件。.wasm二进制文件是你C代码的编译版本。它包含浏览器可以以接近原生速度执行的底层指令。.js“胶水”文件充当语言之间的桥梁，提供加载二进制文件所需的代码，并允许JavaScript调用WebAssembly模块中的函数。

在你的终端中输入此命令以构建.wasm和.js文件。不到一分钟，你应该会在你的项目中看到它们。

我们使用这些文件标志是因为：

*   `-O3`：高级优化。它告诉编译器尽可能快地生成代码。
*   `-s MODULARIZE=1`：将输出包装成一个基于Promise的模块，使其更容易安全加载。
*   `-s EXPORTED_FUNCTIONS`：告诉Emscripten在优化期间不要移除我们的`calculate_fib`函数。

## Web Workers

Worker允许计算在主线程之外进行。我们不想在主线程上运行这个Wasm，因为这种量级的高速计算会占用浏览器的注意力，并导致UI冻结，直到任务完成。为了避免这种情况，我们使用Web Worker。Web Worker是一个专用的后台脚本，它在自己独立的线程中运行，完全独立于用户界面。

下面的代码通过加载Emscripten“胶水”脚本并等待WebAssembly模块完全准备好来初始化后台环境。一旦加载，它通过`cwrap`将基于C语言的`calculate_fib`函数映射到一个可用的JavaScript变量。然后它设置一个事件监听器，从主线程接收数字，独立执行计算，并将结果发送回去，而不会中断用户体验。

运行服务器

你可以使用命令`http-serve`运行服务器。导航到`http://localhost:8080/`，你将看到网页。在输入框中输入你的数字（从49以下的数字开始），并观察计算计时器。

## 将它们整合起来

当Worker处理数学计算时，`main.js`脚本充当指挥中心。它负责生成Worker，向其发送数据，并在结果准备好后更新屏幕。这使得用户界面保持活跃和响应，即使在后台几像素之外正在进行大规模计算。

下面的代码创建Worker实例并设置一个监听器来捕获最终结果。当你点击按钮时，它会记录开始时间并将输入值发布给Worker，然后等待响应来计算总执行时间。

## 将其带到浏览器

现在我们有了`index.html`代码。这是在浏览器中促进计算的基本HTML。

## 结果

对于小于25的小数字，JavaScript实际上更快，因为启动WASM引擎的少量启动成本对于如此快速的任务来说不值得。然而，一旦我们达到25，计算变得更加繁重时，WebAssembly的真正价值就开始显现。

当你达到50时，计算量如此之大，可能永远无法完成。但这里是最重要的部分：因为我们正在Web Worker上运行此任务，你的浏览器仍然保持活跃。你仍然可以点击按钮、滚动，甚至尝试运行JavaScript版本，直到应用程序最终达到其极限。这证明WASM不仅仅关乎原始速度。它关乎保持你的用户界面响应性。