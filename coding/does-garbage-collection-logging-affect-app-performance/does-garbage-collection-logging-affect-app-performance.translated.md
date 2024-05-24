# 垃圾回收日志记录是否会影响应用性能？
![垃圾回收日志记录是否会影响应用性能？的特色图片](https://cdn.thenewstack.io/media/2024/05/032fd6c0-garbage-1024x625.jpg)

我们有时会遇到认为启用垃圾回收日志记录会对其性能指标产生重大影响的 Java 用户。让我们来研究一下事实和误区。

## 关于垃圾回收器

Java 垃圾回收器是 Java 虚拟机 (JVM) 的一个关键部分，它会影响应用程序的性能和可靠性。如果您想深入了解 [Java 运行时](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/) 中可用的不同类型的垃圾回收器及其工作原理，请查看这篇早期的博文：“[作为 Java 开发人员，我应该了解哪些有关垃圾回收的信息](https://www.azul.com/blog/what-should-i-know-about-garbage-collection-as-a-java-developer/)”。

## 什么是 GC 日志记录？

垃圾回收 (GC) 日志记录是 JVM 的一项功能，它提供有关垃圾回收过程的信息。借助生成的日志文件，您可以深入了解 [JVM 在运行时如何动态管理内存](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/)，方法是收集和处理程序不再需要的对象。当您想要监控 [Java 应用程序](https://thenewstack.io/java-adapts-to-cloud-native-computing/) 的性能、诊断内存泄漏和调整 JVM 的垃圾回收配置时，这非常有用。Azul 的销售工程师 Daniel Witkowski 指出：“我们的部分客户会追逐每一微秒来提高其应用程序的性能，但他们仍然会启用 GC 日志记录。”“因为它对应用程序性能的影响很小甚至没有影响，并且允许调试许多不同的问题，因此对于这些公司来说，在问题发生后始终能够检索 GC 日志至关重要。”

启用垃圾回收日志记录后，每当 JVM 执行垃圾回收时，以下信息都会存储在日志文件中：

- **类型**的 GC 事件
  - 次要 GC：清理年轻代空间
  - 主要 GC：清理老年代空间
  - 完全 GC：清理整个堆空间
- **时间**GC 事件开始的时间
- **持续时间**GC 事件的持续时间
- **内存量**GC 事件前后每个内存池的内存量
- **总可用内存**每个池中的内存量

日志文件是人类可读的，内容如下所示：

```
[GC (Allocation Failure) [PSYoungGen: 512K->256K(9216K)] 512K->256K(19456K), 0.0010233 secs] [Times: user=0.00 ms, sys=0.00 ms, real=0.00 secs]
[GC (Allocation Failure) [PSYoungGen: 256K->0K(9216K)] 256K->0K(19456K), 0.0004686 secs] [Times: user=0.00 ms, sys=0.00 ms, real=0.00 secs]
```

存储的信息和格式可能因您使用的 JVM 和 GC 算法而异。

## 启用 GC 日志记录

GC 日志记录通过 Java 命令行参数启用 `-Xlog`。自 Java 9 起，这已成为可能，这要归功于 [JEP 158 “统一 JVM 日志记录”](https://openjdk.org/jeps/158)：

- `-Xlog:gc,safepoint:gc.log` 启用对所有安全点暂停（包括重要垃圾回收事件）的默认日志记录。
- `-Xlog:gc*,safepoint:gc.log` 启用更详细的日志记录，包括所有安全点暂停以及通常不会记录的较小的垃圾回收器事件和阶段。对于 OpenJDK，这通常是必需的；否则，将不会记录一些 Java 堆内存指标，并且不会跟踪所有暂停。在 Zing 上，这是不需要的，因为所有必要的数据在默认情况下已经由 `gc` 记录。
- `-Xlog:gc,safepoint` 将日志数据写入 `stdout`，这在容器中避免存储本地日志文件时很有用。
- `-Xlog:gc,safepoint:gc.log::filecount=10,filesize=100M` 将默认日志轮换从每个 20MB 的 5 个文件更改为每个 100MB 的 10 个文件。
- `-Xlog:gc,safepoint:gc.log::filecount=0` 禁用日志文件轮换，这对于快速测试运行或经常重新启动的进程很有用。请注意双冒号。

您甚至可以重复 `-Xlog` 参数并使用它同时指定不同的输出——例如，以下内容会将其写入 `stdout` 和本地文件：

```
$ java -Xlog:gc,safepoint -Xlog:gc,safepoint:/opt/log/gc.log -jar myApp.jar
```

当您运行以下命令时，统一日志记录系统提供了更多选项，如下所示：

```
$ java -Xlog:gc,safepoint:file=gc.log,tags:gc
```

## GC 日志记录的影响

在 Java 应用程序中启用 GC 日志记录通常会产生最小的性能影响，尤其是在使用现代 JVM 时。但是，具体影响可能因 JVM 版本、使用的 GC 算法、GC 日志记录的设置以及写入日志的系统的 I/O 性能而异。以下是一些您需要考虑的事实：

- **日志文件大小：**GC 日志文件的大小会随着时间的推移而增长，这可能会影响应用程序的性能。
- **日志文件轮换：**JVM 可以配置为定期轮换 GC 日志文件，以防止它们变得太大。
- **I/O 性能：**写入 GC 日志文件所需的 I/O 操作可能会影响应用程序的性能，尤其是在写入速度较慢的设备（如远程文件系统）时。
- **JVM 版本：**较新的 JVM 版本通常具有更有效的 GC 日志记录实现，这可能会减少对应用程序性能的影响。
- **GC 算法：**不同的 GC 算法具有不同的日志记录开销。例如，并发标记清除 (CMS) 算法比串行垃圾回收算法具有更高的日志记录开销。

总体而言，在 Java 应用程序中启用 GC 日志记录通常不会对性能产生重大影响。但是，在启用 GC 日志记录之前，了解潜在影响非常重要，以便您可以做出明智的决定。
**文件系统填满的风险**

将文件系统填满至 100% 或接近 100% 是与日志记录相关的最常见的实际性能影响，需要避免这种情况。默认情况下，Java 9 及更高版本已启用日志文件轮换，并且只会写入五个大小为 20MB 的日志片段。

**I/O 操作**

GC 日志直接写入磁盘。这会创建 I/O 操作，因此如果磁盘速度较慢或磁盘使用率较高，则可能会降低应用程序的速度。

**内存缓冲**

现代 JVM 通常为 GC 日志使用内存缓冲区。当缓冲区已满时，日志会转到磁盘以减少 I/O 影响。但是，缓冲区会占用应用程序原本可以使用的内存。

**详细的 GC 日志**

如果启用了详细的 GC 日志，例如记录每个线程的时间或对象统计信息的日志，则性能影响可能会变得明显，因为需要记录和处理此数据，这可能会消耗 CPU 资源。

**安全点**

所有 GC 日志记录活动都发生在应用程序执行中的“安全点”，这意味着它不会导致比 GC 活动本身自然发生的更多“停止世界”暂停。

**Azul 的建议**

Azul 的客户员工工程师 Holger 说：“用户在考虑 GC 日志记录时应考虑的实际性能主题是文件系统中的数据量”。“由于文件系统已满而导致系统停止将导致非常糟糕的性能。仅使用 -Xlog:gc:gc.log（适用于 Zing）或 -Xlog:gc,safepoint:gc.log（适用于 OpenJDK）时，您将获得所有必要的与性能相关的指标，而不会浪费太多空间。尤其是在 Zing 上，不需要 -XX:+PrintGCDetails、gc* 或 safepoint，因为它们不会在 GCLogAnalyzer 中添加更多图表。”

Azul 的首席软件工程师 Deepak Sreedhar 解释说：“GC 日志任务很大一部分是将数据保存到日志文件中。用于存储这些文件 I/O 的类型可能会影响日志记录性能，而不是直接影响应用程序本身。”“因此，可能发生的一些问题与 GC 日志记录的性能无关，而是与 I/O 速度有关。如果无法实时快速保存日志，OpenJDK 可以选择使用异步统一日志记录，方法是使用 Xlog:async。

## 使用 Azul Zing 的 GC 日志记录

在使用 Azul Zing 时，您只需添加 -Xlog:gc:gc.log，即可指示 Zing 存储垃圾回收器日志文件。不需要 gc* 或 safepoint 等额外参数来增加详细级别，因为 Zing 始终会记录安全点暂停，甚至会记录 OpenJDK GC 日志中默认情况下看不到的其他信息，例如即时 (JIT) 编译器活动、CPU 和内存使用情况、Linux 页面缓存指标以及更多通常与系统性能分析相关的指标。

## 分析 GC 日志记录

有各种工具可用于分析 GC 日志文件的内容：

**JVM 的内置工具**

* jstat 命令：此实用程序显示性能统计信息，可用于输出垃圾回收器统计信息。

**VisualVM**

此工具提供了对不同 JVM 方面（如垃圾回收）的多个视图。它还提供实时指标，这有助于实时分析问题。您可以从 [GitHub](https://visualvm.github.io/) 下载此工具。

**Azul GC 日志分析器**

读取 GC 日志并将其可视化为一段时间（时钟时间和正常运行时间）的图表集。它显示有关垃圾回收器、JIT 编译器、系统指标和 ReadyNow 统计信息的信息。此图形桌面应用程序在此处[记录](https://docs.azul.com/prime/GC-Log-Analyzer)，并且此处提供视频演练 [（https://www.azul.com/tutorial/garbage-collection-log-analyzer/）。

## 结论

虽然垃圾回收日志可能会带来最小的性能成本，但权衡通常是值得的，因为在调整垃圾回收和诊断内存问题时，日志通常是无价的。如果不启用 GC 日志记录，您可能会失去对 JVM 在运行时如何动态管理内存的了解。此信息对于监视 Java 应用程序的性能、诊断内存泄漏和调整 JVM 的垃圾回收配置非常有用。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)