
<!--
title: 垃圾回收日志记录是否会影响应用性能？
cover: https://cdn.thenewstack.io/media/2024/05/032fd6c0-garbage.jpg
-->

尽管性能成本极低，但垃圾回收日志提供了宝贵的见解，说明 JVM 如何在运行时动态管理内存。

> 译自 [Does Garbage Collection Logging Affect App Performance?](https://thenewstack.io/does-garbage-collection-logging-affect-app-performance/)，作者 Frank Delporte。

我们有时会遇到认为启用垃圾回收日志记录会对其性能指标产生重大影响的 Java 用户。让我们来研究一下事实和误区。

## 关于垃圾回收器

Java 垃圾回收器是 Java 虚拟机 (JVM) 的一个关键部分，它会影响应用程序的性能和可靠性。如果您想深入了解 [Java 运行时](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/) 中可用的不同类型的垃圾回收器及其工作原理，请查看这篇早期的博文：“[作为 Java 开发人员，我应该了解哪些有关垃圾回收的信息](https://www.azul.com/blog/what-should-i-know-about-garbage-collection-as-a-java-developer/)”。

## 什么是 GC 日志记录？

垃圾回收 (GC) 日志记录是 JVM 的一项功能，它提供有关垃圾回收过程的信息。借助生成的日志文件，您可以深入了解 [JVM 在运行时如何动态管理内存](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/)，方法是收集和处理程序不再需要的对象。当您想要监控 [Java 应用程序](https://thenewstack.io/java-adapts-to-cloud-native-computing/) 的性能、诊断内存泄漏和调整 JVM 的垃圾回收配置时，这非常有用。Azul 的销售工程师 Daniel Witkowski 指出：“我们的部分客户会追逐每一微秒来提高其应用程序的性能，但他们仍然会启用 GC 日志记录。”“因为它对应用程序性能的影响很小甚至没有影响，并且允许调试许多不同的问题，因此对于这些公司来说，在问题发生后始终能够检索 GC 日志至关重要。”

启用垃圾回收日志记录后，每当 JVM 执行垃圾回收时，以下信息都会存储在日志文件中：

- GC 事件类型
  - Minor GC：清理年轻代空间
  - Major GC：清理老年代空间
  - Full GC：清理整个堆空间
- *GC 事件开始的时间
- GC 事件的持续时间
- GC 事件前后每个内存池的内存量
- 每个池中的内存量

日志文件是人类可读的，内容如下所示：

```

[0.005s][info][gc] Using G1
[0.110s][info][safepoint] Safepoint "ICBufferFull", Time since last: 98355917 ns, Reaching safepoint: 2000 ns, Cleanup: 53416 ns, At safepoint: 7167 ns, Total: 62583 ns
[0.186s][info][safepoint] Safepoint "ICBufferFull", Time since last: 75998125 ns, Reaching safepoint: 1792 ns, Cleanup: 56000 ns, At safepoint: 4458 ns, Total: 62250 ns
[0.235s][info][safepoint] Safepoint "ICBufferFull", Time since last: 48961667 ns, Reaching safepoint: 2125 ns, Cleanup: 45208 ns, At safepoint: 4042 ns, Total: 51375 ns
[0.259s][info][gc       ] GC(0) Pause Young (Normal) (G1 Evacuation Pause) 49M->4M(1032M) 1.472ms
...
[2.290s][info][gc       ] GC(13) Pause Young (Concurrent Start) (Metadata GC Threshold) 120M->23M(560M) 2.647ms
[2.290s][info][gc       ] GC(14) Concurrent Mark Cycle
[2.290s][info][safepoint] Safepoint "CollectForMetadataAllocation", Time since last: 31224333 ns, Reaching safepoint: 1542 ns, Cleanup: 45042 ns, At safepoint: 2700833 ns, Total: 2747417 ns
[2.302s][info][gc       ] GC(14) Pause Remark 28M->28M(112M) 1.986ms
[2.302s][info][safepoint] Safepoint "G1PauseRemark", Time since last: 10354500 ns, Reaching safepoint: 1917 ns, Cleanup: 14125 ns, At safepoint: 2028625 ns, Total: 2044667 ns
[2.306s][info][gc       ] GC(14) Pause Cleanup 28M->28M(112M) 0.048ms
[2.306s][info][safepoint] Safepoint "G1PauseCleanup", Time since last: 3311666 ns, Reaching safepoint: 169500 ns, Cleanup: 11084 ns, At safepoint: 79583 ns, Total: 260167 ns
[2.306s][info][gc       ] GC(14) Concurrent Mark Cycle 16.086ms
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
[0.017s][info][logging] Log configuration fully initialized.
[0.017s][info][logging] Available log levels: off, trace, debug, info, warning, error
[0.017s][info][logging] Available log decorators: time (t), utctime (utc), uptime (u), timemillis (tm), uptimemillis (um),...
[0.017s][info][logging] Available log tags: add, age,... gc,...
[0.017s][info][logging] Described tag sets:
[0.017s][info][logging]  logging: Logging for the log framework itself
[0.019s][debug][logging] Available tag sets: , arguments, attach, cds, cds+class, cds+dynamic, cds+hashtables, cds+heap,...
[0.023s][info ][logging] Log output configuration:
[0.023s][info ][logging]  #0: stdout all=warning,logging=debug uptime,level,tags foldmultilines=false
[0.023s][info ][logging]  #1: stderr all=off uptime,level,tags foldmultilines=false
openjdk version "22" 2024-03-19
OpenJDK Runtime Environment Zulu22.28+91-CA (build 22+36)
OpenJDK 64-Bit Server VM Zulu22.28+91-CA (build 22+36, mixed mode, sharing)
```

## GC 日志记录的影响

在 Java 应用程序中启用 GC 日志记录通常会产生最小的性能影响，尤其是在使用现代 JVM 时。但是，具体影响可能因 JVM 版本、使用的 GC 算法、GC 日志记录的设置以及写入日志的系统的 I/O 性能而异。以下是一些您需要考虑的事实：

- **日志文件大小**：GC 日志文件的大小会随着时间的推移而增长，这可能会影响应用程序的性能。
- **日志文件轮换**：JVM 可以配置为定期轮换 GC 日志文件，以防止它们变得太大。
- **I/O 性能**：写入 GC 日志文件所需的 I/O 操作可能会影响应用程序的性能，尤其是在写入速度较慢的设备（如远程文件系统）时。
- **JVM 版本**：较新的 JVM 版本通常具有更有效的 GC 日志记录实现，这可能会减少对应用程序性能的影响。
- **GC 算法**：不同的 GC 算法具有不同的日志记录开销。例如，并发标记清除 (CMS) 算法比串行垃圾回收算法具有更高的日志记录开销。

Azul 公司的客户工作人员 Holger 说：“关于 GC 日志记录，实用性能主题用户应该考虑的是文件系统中的数据量。”“由于文件系统已满而造成的系统停止会产生非常糟糕的性能。对于 Zing，仅使用 -Xlog:gc:gc.log，对于 OpenJDK，仅使用 -Xlog:gc,safepoint:gc.log，即可获取所有必要的与性能相关的数据，而不会浪费太多空间。特别是对于 Zing，不需要 -XX:+PrintGCDetails、gc* 或 safepoint，因为它们不会在 GCLogAnalyzer 中添加更多图形。”

Azul 公司的首席软件工程师 Deepak Sreedhar 解释说：“GC 日志任务中的一个重要组成部分是将数据保存到日志文件中。用来存储这些文件的 I/O 类型可能会影响日志记录性能，而不会直接影响应用程序本身。” “因此，可能发生的某些问题与 GC 日志记录的性能无关，而与 I/O 速度有关。如果无法实时快速保存日志，OpenJDK 可以选择使用 Xlog:async 实现异步统一日志记录。

## 使用 Azul Zing 的 GC 日志记录

在使用 Azul Zing 时，您只需添加 -Xlog:gc:gc.log，即可指示 Zing 存储垃圾回收器日志文件。不需要 gc* 或 safepoint 等额外参数来增加详细级别，因为 Zing 始终会记录安全点暂停，甚至会记录 OpenJDK GC 日志中默认情况下看不到的其他信息，例如即时 (JIT) 编译器活动、CPU 和内存使用情况、Linux 页面缓存指标以及更多通常与系统性能分析相关的指标。

## 分析 GC 日志记录

用于分析 GC 日志文件内容有多种工具： 

- JVM 自带的 jstat 命令：此实用工具显示性能统计信息，可用于输出垃圾回收器统计信息。
- VisualVM：此工具提供了对不同 JVM 方面的多个视图，例如垃圾回收。它还提供了实时指标，这有助于实时分析问题。您可从 GitHub 下载此工具。
- Azul GC 日志分析器： 读取 GC 日志并将其形象化为一组随时间（主时钟和正常运行时间）变化的图表。它显示有关垃圾回收器、JIT 编译器、系统指标以及 ReadyNow 统计信息。此图形桌面应用程序在此处记录在案，并且此处提供了视频演练。

## 结论

虽然垃圾回收日志可能会带来最小的性能成本，但权衡通常是值得的，因为在调整垃圾回收和诊断内存问题时，日志通常是无价的。如果不启用 GC 日志记录，您可能会失去对 JVM 在运行时如何动态管理内存的了解。此信息对于监视 Java 应用程序的性能、诊断内存泄漏和调整 JVM 的垃圾回收配置非常有用。
