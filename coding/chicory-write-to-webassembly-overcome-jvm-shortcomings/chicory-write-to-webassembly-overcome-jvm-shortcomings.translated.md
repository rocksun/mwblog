# Chicory：编写 WebAssembly，克服 JVM 缺陷

![Chicory：编写 WebAssembly，克服 JVM 缺陷的特色图片](https://cdn.thenewstack.io/media/2024/07/2d1fbb61-wyxina-tresse-h9lxuk5eamy-unsplash-1024x683.jpg)

[Java 虚拟机 (JVM)](https://thenewstack.io/how-do-javas-virtual-threads-help-your-business/) 和 [WebAssembly](https://thenewstack.io/webassembly/) 都有其固有的能力。JVM 经过数十年的考验和信赖，用于运行 [Java 代码](https://thenewstack.io/trash-pandas-love-enterprise-java-code/) 和应用程序。作为在云、移动、本地或任何运行 Java 的地方运行 Java 应用程序的固有组成部分，JVM 已在大多数行业中得到广泛使用，包括金融、制造、银行和金融。安全和监控得到提供，并且通过 [即时 (JIT)](https://thenewstack.io/how-to-reduce-cloud-waste/) 编译器，JVM 经过多年的发展，可以在各种设备和端点上执行 Java 代码，包括边缘设备、服务器、移动环境和 PC。

另一方面，WebAssembly（也称为 Wasm）最近出现，它是一种将您选择的应用程序（用您选择的语言编写）捆绑在一起并同时部署到任何主机环境（从边缘到云）的方法，只要存在与 Wasm 兼容的 [CPU 指令集](https://thenewstack.io/webassembly-isnt-software-its-a-computer/)。与 JVM 一样，Wasm 也被（正确或错误地）与“一次编写，随处运行”联系在一起，尽管语言兼容性难以最终确定一个标准组件模型来标准化端点分发，并且其他挑战仍然存在。同样，JVM 也只在存在 JVM 端点的地方才能一次编写，随处运行，这与 WebAssembly 模块不同，理论上 WebAssembly 模块应该能够在任何能够运行 CPU 指令集的设备上运行。

同时，[Chicory](https://github.com/dylibso/chicory) 的创建是为了将 Wasm 的一些优势带到原生 JVM。考虑到 WebAssembly 的安全性、隧道和沙箱方面，它就像虚拟机中的虚拟机。通过 JVM 提供的额外封闭模块，用户可以从双重沙箱中受益。

正如 [Chicory 在 GitHub 上的 readme.md 文件](https://github.com/dylibso/chicory/blob/main/README.md) 中所述，Chicory 是一个 JVM 原生 WebAssembly 运行时。它的创建是为了让 WebAssembly 程序能够在没有原生依赖项或 [Java 本地接口 (JNI)](https://docs.oracle.com/javase/8/docs/technotes/guides/jni/) 的情况下运行。“Chicory 可以在 JVM 可以运行的任何地方运行 Wasm。它在设计时考虑了简单性和安全性，”其创建者写道。

## Wasm 帮助
Chicory 的联合创始人兼 [Dylibso](https://dylibso.com/) 的 CTO 和联合创始人 [Benjamin Eckel](https://www.linkedin.com/in/benjamin-eckel-b025831a3/) 解释说，Wasm 本身什么也做不了，只能计算。—— 它制作了 [Extism](https://thenewstack.io/extism-v1-run-webassembly-in-your-app/)，这是一个旨在让软件最终用户能够使用 Wasm 增强现有应用程序的框架。Eckel 说，理论上，它无法影响外部世界，WebAssembly 看起来可能是一个弱点，但这实际上是 Wasm 最大的优势。

默认情况下，程序是沙箱化的，没有任何功能。如果程序需要功能，则必须提供功能。这将开发人员置于操作系统的角色。模块可以通过在字节码格式中列出“导入”函数来请求功能。此导入可以使用用 Java 编写的宿主函数来实现。无论模块的语言是什么，模块都可以在需要时调用此 Java 函数。宿主函数可以被认为是系统调用或语言的标准库，但宿主函数是在 Java 中确定和实现的，Eckel 说。

Eckel 指出，如果链接到 JVM 中的原生对象，则必须将该对象与应用程序或库一起提供。使用 JVM 的主要原因之一是它编译成平台无关的字节码，这是为 JVM 编写应用程序的主要优势。但是，这会产生为需要交付的每个操作系统、体系结构和 libc 编译的问题，他说。

在运行时方面，为了与某些共享对象通信，大多数系统都需要使用外部函数接口。在 Java 中，对此有几个不同的名称，但概念大致相同。当执行离开 JVM 的安全性和可观察性时，会存在很大的复杂性和许多问题，Eckel 说。
如果停留在 JVM 范围内，根据 Eckel 的说法，保证的内存安全一直是可靠的功能。还提供了故障隔离，这意味着如果 Wasm 程序类似于 JVM 字节码，它不会使 JVM 崩溃，这对许多应用程序来说是一个主要优势。此外，还提供了一个超级先进的 JIT。当使用外部函数接口 (FFI) 时，来自 JVM 的 JIT 将程序视为一系列漏洞，进进出出。但是，如果一切都只是一条连续的 JVM 字节码流，那么好处会更大，他说。

内存漏洞越来越令人担忧，美国政府已发出信号，他们将开始 [强制使用内存安全语言](https://thenewstack.io/white-house-warns-against-using-memory-unsafe-languages/)，Eckel 在电子邮件回复中说。同时，默认情况下，Java 代码是内存安全的，只需要检查 JVM 的实现。“但是，如果你调用本机代码，你就离开了 JVM 的安全范围，”Eckel 说。“这给了攻击者更多机会，也给了错误更多机会。”

## 灵感

![](https://cdn.thenewstack.io/media/2024/07/86c0bad4-capture-decran-2024-07-18-170609-1024x450.png)
Red Hat 首席软件工程师 Andrea Peruffo 解释了如何开始使用 Chicory。

开源项目 [Wazero](https://wazero.io/) 启发了 Chicory。借助它，运行时执行 WebAssembly 模块，这些模块通常是带有 .wasm 扩展名的二进制文件，根据 Wazero 的文档。目前，Wazero 也是一个用 Go 编写的零依赖 WebAssembly 运行时。因此，与 Chicory 一样，Wazero 的创建是为了帮助简化用不同语言（C++、Go、Java、Rust 等）编写运行时。

Chicory 最有趣的用例之一是用于身份管理软件，[Andrea Peruffo](https://www.linkedin.com/in/andrea-peruffo-32269178/?original_referer=https%3A%2F%2Fwww%2Egoogle%2Ecom%2F&originalSubdomain=pt)，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的首席软件工程师，在 2023 年 Linux 基金会 [Wasm I/0 大会](https://www.youtube.com/watch?v=00LYdZS0YlI&ab_channel=WASMI%2FO) 上的“Chicory：创建语言原生 Wasm 运行时”演讲中讨论了这一点。他描述了 [Keycloak](https://thenewstack.io/how-to-integrate-openshift-with-keycloak/) 是一款非常流行的身份管理软件，它支持单点登录和其他相关操作。但是，可能鲜为人知的是，它包含复杂的意大利面条式代码，旨在与任何类型的遗留系统集成。Active Directory 可以位于一侧，[LDAP](https://thenewstack.io/deploy-the-ldap-directory-system-to-an-ubuntu-server/)，然后是 Kerberos，等等。虽然用 Rust 重写这些集成似乎很有吸引力，但实际上并不现实。这就是 Java 强大的地方。Peruffo 指出，像这样的企业应用程序不容易替换，因此目标是赋予它们权力，使它们的使用更加灵活。

在 Keycloak 中，如果需要自定义操作，例如根据不同的提供商检查用户的身份或插入自定义业务规则，通常需要编写 Java 插件，Peruffo 继续说道。但为什么要将开发限制在 Java 上？通过导入 JVM 库，可以使用任何编译成 WebAssembly 的语言（如 Rust、C、Go、JavaScript 等）编写插件。通过导入 JVM 库，在短短两个小时内就创建了一个初始概念验证。这种方法使企业应用程序（通常很重且复杂）能够轻松地使用轻量级系统进行扩展。它只需导入一个库，并使应用程序能够加载和运行 Wasm 代码。Peruffo 说，这种功能非常有用。

## 运行起来

与其他语言相比，Chicory 无法克服 Java 的固有缓慢性，但它仍然可能出于上述原因而实用。尽管如此，Chicory 还是一个新项目，还有很多工作要做。到目前为止，它可以（根据文档）：

引导字节码解释器和测试套件以及功能：

- Wasm
[二进制解析器。](https://github.com/dylibso/chicory/blob/main/wasm) - 简单的字节码解释器
- 建立基本的编码和测试模式
- 从
[wasm 测试套件](https://github.com/dylibso/chicory/tree/main/test-gen-plugin)
生成 JUnit 测试。
#### 到今年夏天结束时，它应该能够：
- 使用解释器使所有测试变为绿色（对正确性很重要）。
- 实现验证逻辑（对安全性很重要）。
- v1.0 API 草案（对稳定性和 dx 很重要）。
项目 readme.md 中的其他新路线图更新包括：

- 完成大约 30,000 个测试以确保满足 Wasm 规范。
- 字节码验证已完成 95%。
- 项目创建者表示，提前编译已投入生产，并且已被证明比解释器模式快得多。

## 设置
虽然我还没有能够在我的 Windows 笔记本电脑上加载和运行 Chicory，但请继续关注有关如何设置和运行它的评论。Chicory 的 readme.md 提供了可靠的设置说明，以便开始使用，在此期间：

将 `com.dylibso.chicory:runtime` 依赖项添加到依赖项管理系统以使用运行时：

```xml
<dependency>
  <groupId>com.dylibso.chicory</groupId>
  <artifactId>runtime</artifactId>
  <version>0.0.10</version>
</dependency>
```

实现：

```
'com.dylibso.chicory:runtime:0.0.10'
```

Java 生成器 CLI 可在 Maven 上的以下链接下载：

```
https://repo1.maven.org/maven2/com/dylibso/chicory/cli/<version>/cli-<version>.sh
```

有关项目和如何贡献的更多信息，请访问 [专门的 Zulip 频道](https://chicory.zulipchat.com/join/g4gqsxoys6orfxlrk6hn4cyp/)。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)