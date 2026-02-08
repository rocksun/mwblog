[Whamm](https://thenewstack.io/meet-whamm-the-webassembly-instrumentation-framework/) 旨在允许用户使用[编程语言](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/)或代码对其 [WebAssembly](https://thenewstack.io/webassembly/) (或 Wasm) 应用程序进行插桩，或者让他们直接在模块中编程其 WebAssembly 应用程序。有了它，他们可以在 WebAssembly 模块中调试和监控其应用程序。

如果您已经安装了 [Homebrew](https://thenewstack.io/install-homebrew-on-macos-for-more-dev-tool-options/)，那么在安装 Whamm 时，更新将自动安装。此命令会下载并安装 Homebrew：

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

从发布页面下载适用于您平台的最新版本。

克隆 Whamm 仓库：

```
git clone https://github.com/ejrgilbert/whamm.git
```

需要 [Rust](https://thenewstack.io/rust-programming-language-guide/)，即使您对 Rust 不太了解——我当然也不——一旦安装好，您就可以开始使用 Whamm 了。我通过此可信站点使用此命令（我强烈推荐这样做）在我的 Mac 上下载并安装了 Rust：

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

然后我运行了这些命令，以确保 Rust 在所有终端会话中都可用。这是必要的，因为 Rust 使用起来非常复杂，或者极其逻辑化，或者两者兼而有之：

```
grep -q ".cargo/env" ~/.zshrc 2&gt;/dev/null || echo 'source "$HOME/.cargo/env"' &gt;&gt; ~/.zshrc &amp;&amp; echo "Added to ~/.zshrc - will work in new terminals"
```

构建源代码：

```
cargo build --release
```

当我第一次提示 Whamm 构建源代码时，我收到了一条错误消息：

[![](https://cdn.thenewstack.io/media/2026/01/dd8b42a5-screenshot-2026-01-13-at-8.29.19-pm.png)](https://cdn.thenewstack.io/media/2026/01/dd8b42a5-screenshot-2026-01-13-at-8.29.19-pm.png)

我没有安装 WebAssembly 目标是错误的原因。因此，我安装了 WebAssembly 目标作为修复：

```
cd ~/whamm &amp;&amp; rustup target add wasm32-wasip1
```

我再次尝试构建源代码：

```
cargo build --release
```

成功了！

[![](https://cdn.thenewstack.io/media/2026/01/f4ee857a-screenshot-2026-01-13-at-8.37.20-pm.png)](https://cdn.thenewstack.io/media/2026/01/f4ee857a-screenshot-2026-01-13-at-8.37.20-pm.png)

将构建好的二进制文件添加到您的 PATH。此二进制文件应位于：

```
target/release/whamm
```

完成此操作后，您可以使用 Whamm 和 Wasm 完成的巧妙操作会整齐地列出。您可以按照指示使用命令行界面 (CLI) 作为所有可用命令的参考。这些命令包括——如所示——监控或操纵程序的执行。我在这里不会深入探讨应用程序监控的含义，但它是为 Wasm 应用程序添加更多**可观测性**的开始。使用 Whamm 进行此操作通常用于调试、收集和分析应用程序运行时的日志和指标，而不仅仅是静态地进行。

一旦找到错误源，所谓的“操纵执行”允许您通过改变“动态行为”来修复错误，换句话说，就是修复错误。正如文档所述，您可以通过“操纵应用程序的动态行为”来改变应用程序状态。

## 基本测试

您可以运行一个基本测试，通过运行以下命令来确保 Whamm 二进制文件在您的路径中并按预期工作：

```
whamm --help
```

您应该会看到以下内容：

[![](https://cdn.thenewstack.io/media/2026/01/d6b227ef-screenshot-2026-01-13-at-9.08.47-pm-1024x157.png)](https://cdn.thenewstack.io/media/2026/01/d6b227ef-screenshot-2026-01-13-at-9.08.47-pm-1024x157.png)

由于我尚不清楚的原因，我最初对 Whamm 功能的测试并未奏效，如上所示。但随后我回顾了以上所有命令，包括重新安装 Rust 目标，并重新构建或重新安装 WebAssembly 目标，以及重新安装 Rust 的 Cargo 以确保其在所有终端中都可用。因此这很可能是一个 Rust 问题，尽管我不确定。无论如何，我执行了大部分上述命令并最终成功了。

现在您已准备好开始您的 Whamm 之旅，进行代码的插桩、重新构建、纠错、监控和调试。向该项目的创建者——以及现在，我猜想是主要维护者——卡内基梅隆大学的博士生 Elizabeth Gilbert 致敬，感谢她带来了这个出色的项目。

尽管我认为这看起来很简单且相对易于使用，但它是一个了不起的构建，代表了大量的辛勤工作和工程奉献。这无疑是 WebAssembly 社区的又一次胜利，也为**可观测性**、调试以及使用 Wasm 动态更新应用程序的能力带来了胜利。