# 我们能拥有美好的事物：升级到 Java 21 是值得的

![用于以下内容的特色图片：我们能拥有美好的事物：升级到 Java 21 是值得的](https://cdn.thenewstack.io/media/2024/02/a2feedba-update-java-21-nice-things-1024x576.jpg)

又是一年一度的时候了——New Relic 的年度“[Java 生态系统状况](https://newrelic.com/resources/report/2023-state-of-the-java-ecosystem)”调查结果出炉了，和往常一样，我对此进行了深入研究。虽然我认为这份报告做得很好，提出了很多好问题，但我对有多少 Java 开发人员使用过时的版本感到沮丧。

## 你在使用 Java 21 吗？你应该使用。

在我开始调查之前，作为一名 Java 爱好者，我想谈谈我对 Java 21 的一些喜爱之处。

首先，Java 虚拟机 (JVM) 上最流行的服务器端堆栈的当前版本 Spring Boot 3.x 至少需要 Java 17。根据调查，它不支持 Java 8，而 Java 8 是第二常用的版本。

我很高兴看到 Java 17 的采用速度相对较快，但你真的应该使用 Java 21。Java 21 在所有方面都比 Java 8 好得多。它在技术上更胜一筹。它更快、更安全、更易于操作、性能更高、内存效率更高。

它在道德上也更胜一筹。当你的孩子发现你在生产中使用 Java 8 时，你不会喜欢他们眼中流露出的羞愧和悲伤。

做正确的事，成为你想在世界上看到的改变：使用 Java 21。它只是[充满优点](https://thenewstack.io/java-21-is-nigh-whither-javaone/)，从本质上来说，自 Java 7 以来，它是一种全新的语言：

* Lambda
* 多行字符串
* 智能 switch 表达式
* var
* 模式匹配
* 命名元组（在 Java 中称为记录）

当然，还有虚拟线程这一壮举。虚拟线程是一个巨大的进步。它们提供了与 async/await 或挂起相同的好处，但没有其他语言中代码的冗长性。

是的，你没听错。Java 的虚拟线程提供了更好的解决方案，而且比其他语言的代码更少。

如果你不知道我在说什么，并且你使用那些其他语言，那么你现在一定很生气。Java？比你最喜欢的语言更简洁？不可能！但我没错。

## 为什么虚拟线程是一个大问题

要[了解虚拟线程](https://openjdk.org/jeps/444?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform)，你需要了解它们被创建来解决的问题。如果你还没有体验过虚拟线程，那么它们很难描述。我会尝试。

Java 具有阻塞操作——比如 Thread.sleep(long)、InputStream.read 和 OutputStream.write。如果你调用其中一个方法，程序将不会前进到下一行，直到这些方法完成它们正在做的事情并返回。

大多数网络服务都是 I/O 绑定的，这意味着它们大部分时间都花在输入和输出方法上，如 InputStream.read 和 OutputStream.write。

登录到线程池中没有更多线程的服务非常常见，但仍然无法返回响应，因为所有现有线程都在等待某些 I/O 操作发生，例如跨 HTTP 边界的 I/O、到数据库的 I/O 或到消息队列的 I/O。

有办法取消 I/O 阻塞。你可以使用 java.nio，它会引起焦虑的复杂性。你可以使用反应式编程，它在范式上有效，但对整个代码库进行了彻底的重构。

所以，思考是这样的：如果编译器知道你做了某些可能阻塞的事情（比如 InputStream.read）并重新排序代码的执行，那不是很好吗？因此，当你执行阻塞操作时，等待代码将从当前执行线程移走，直到阻塞操作完成，然后在它准备好恢复执行后将其放回另一个线程。

这样，你可以继续使用阻塞语义。第一行在第二行之前执行。这促进了可调试性和可扩展性。你不再会独占线程，只是在等待某事完成时浪费它们。它将是两全其美的：非阻塞 I/O 的可扩展性以及更简单的阻塞 I/O 的明显简单性、可调试性和可维护性。

许多其他语言，如 Rust、Python、C#、TypeScript 和 JavaScript，都支持 async/await。Kotlin 支持挂起。这些关键字提示运行时你将执行某些阻塞操作，并且它应该重新排序执行。以下是在 JavaScript 中的一个示例：

```javascript
async function myFunction() {
  const result = await fetch('https://example.com');
}
```

问题在于，要调用 async 函数，你也必须 *in* 一个 async 函数：

```javascript
(async () => {
  await myFunction();
})();
```

这个关键字是病毒式的。它会传播。最终，你的代码会陷入 async/await 的泥潭——因为为什么你不可以在任何地方使用 async/await 呢？因此，它比使用低级非阻塞 I/O 或反应式编程要好，但好不了多少。
**Java 提供了一种更好的方式**

只需为线程使用不同的工厂方法。

如果您使用 `ExecutorService` 创建新线程，请使用创建虚拟线程的新版本。
如果您直接在低级别创建线程，请使用新的工厂方法：

```java
Thread.ofVirtual().start();
```

您的大部分代码保持完全不变，但现在您获得了极大改进的可扩展性。如果您创建数百万个线程，运行时不会喘不过气来。我无法预测您的结果，但您很有可能不再需要运行几乎同样多的给定服务实例来处理负载。

如果您使用 [Spring Boot 3.2](https://tanzu.vmware.com/content/white-papers/spring-boot-3)（您使用，不是吗？），那么您甚至不需要执行任何这些操作。只需在 `application.properties` 中指定 `spring.threads.virtual.enabled=true` — 然后向您的管理层要求加薪，由大幅减少的云基础设施成本支付。

如果您未使用 Spring 3.2，请查看由我的 Spring 倡导者同事 DaShaun Carter 提供的这段 9 分钟视频，了解升级有多么容易。

并非每个应用程序在技术上都可以立即进行跳跃，但绝大多数应用程序可以并且应该进行跳跃。

## 莎士比亚式表达

最后，这让我回到了 New Relic 报告。别误会我：它做得很好，值得一读。就像莎士比亚悲剧一样，它写得很好，讲述了一个悲伤的故事。

有一整部分内容证实了显而易见的事实：天是蓝色的，到处都是云。在容器中部署工作负载似乎是占主导地位的模式，受访者报告称 70% 的 Java 工作负载使用容器。坦率地说，我惊讶它如此之低。

同样有趣的是转向多核而不是单核配置的趋势。根据调查，30% 的容器化应用程序正在使用 Java 9 的 `-XX:MaxRAMPercentage` 标志，该标志限制了 RAM 使用。G1 是使用最广泛的垃圾回收器。一切都很好。

当报告涉及 Java 版本时，它发生了悲剧性的转变。超过一半的应用程序（56%）在生产中使用 Java 11，高于 2022 年的 48%。Java 8（于 2014 年十年前发布）紧随其后，近 33% 的应用程序在生产中使用它。根据调查，三分之一的应用程序仍在使用与 Flappy Bird 游戏下架、冰桶挑战席卷 Vine 以及艾伦·德杰尼勒斯奥斯卡自拍照走红同一年推出的 Java 版本。

大多数用户使用亚马逊的 [OpenJDK](https://thenewstack.io/microsoft-releases-its-own-distro-of-java-21/) 发行版。报告表明，这是因为 [Oracle](https://developer.oracle.com/?utm_content=inline-mention) 暂时对其发行版引入了更严格的许可。但我很好奇，有多少只是因为该发行版是 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline-mention) 上 Java 工作负载的默认发行版，而 Amazon Web Services 是最多产的基础设施即服务 (IaaS) 供应商。自几年前首次亮相以来，该发行版已获得大量采用。2020 年，它占有 2.18% 的市场份额，而现在它占有 31%。哇！如果这么多人能够如此迅速地迁移到一个完全不同的发行版，那么他们应该能够使用同一发行版的新版本，不是吗？

我想，在 [趋势](https://thenewstack.io/java-usage-keeps-climbing-according-to-new-survey/) 中还是有一点希望。Java 17 用户采用率在一年的时间里增长了 430%。因此，也许我们会在 Java 21 中看到类似的数字——它 [已经发布](https://thenewstack.io/microsoft-releases-its-own-distro-of-java-21/) 近六个月了。

## 那么，您还在等什么？

正如我在 [Voxxed Days 上的演讲](https://youtu.be/8l0tv3_jFoY?si=itYItELoRw78VC-d&t=1) 中所说的，我相信现在是成为 Java 和 Spring Boot 开发人员的最佳时机。Java 和 Spring 开发人员拥有最好的玩具。我甚至还没有提到 GraalVM 原生镜像，它可以显著缩短启动时间并减少给定 Java 应用程序的内存占用。而且它已经可以完美地与 Java 21 配合使用。

这些东西就在这里，它们令人惊叹。我们必须做出改变。而且这并不难。试试看。

安装 [SDKMan](https://sdkman.io)，运行 `sdk install java 21.0.2-graalce`，然后运行 `sdk default java 21.0.2-graalce`。这将为您提供 Java 21 和 GraalVM 原生镜像编译器。访问 Spring Initializr，这是我在网上最喜欢的第二个地方（仅次于生产），网址为 [start.spring.io](https://start.spring.io)。配置一个新项目。选择 Java 21（当然！）。添加 GraalVM 原生支持。添加 Web。点击生成按钮并将其加载到您的 IDE 中。在 `application.properties` 中指定 `spring.threads.virtual.enabled=true`。创建一个简单的 HTTP 控制器：

```java
@RestController
public class MyController {

    @GetMapping("/")
    public String hello() {
        return "Hello, world!";
    }

}
```

将其编译成 GraalVM 原生镜像：

```
./gradlew nativeCompile
```

在 `build` 文件夹中运行二进制文件。
**现在，您拥有一个应用程序，它占用的 RAM 只是非 GraalVM 本机映像的一小部分，并且还可以扩展到每秒处理更多倍的请求。简单又惊人。**

## 进入生产从未如此简单

我们可以做到。让我们尝试在 New Relic 进行下一次报告时，让 Java 21（或 Java 22？）达到 99% 的采用率——谁支持我？

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。