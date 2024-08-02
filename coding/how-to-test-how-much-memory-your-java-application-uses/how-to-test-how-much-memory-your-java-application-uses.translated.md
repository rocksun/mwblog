# 测试和优化 Java 应用程序的内存使用

![测试和优化 Java 应用程序的内存使用](https://cdn.thenewstack.io/media/2024/07/7977d1b8-trash1a-1024x601.jpg)

确定运行 Java 应用程序的 [理想内存大小](https://thenewstack.io/how-to-avoid-overprovisioning-java-resources/) 可能非常困难。但随着云实例成本和生态影响的不断上升，正确地调整机器尺寸以处理预期负载而不过度调整非常重要，这样可以最大程度地降低机器成本，同时减少其生态影响。了解应用程序的内存大小需求对于以最低运营成本实现最高性能至关重要。

我将向您展示如何使用垃圾收集器 (GC) 日志文件来确定应用程序所需的内存大小。借助 [Java](https://roadmap.sh/java/developer-skills) 运行时，我们可以依靠 GC 来清理不再使用的内存，并尽可能降低总内存量。在此过程中，GC 可以输出包含大量信息的日志文件，这些信息可以帮助我们找到代码中的问题并为我们的服务器或虚拟环境定义 [正确的尺寸](https://thenewstack.io/how-to-reduce-cloud-waste/)。

## 如何测试您的应用程序

对您的应用程序进行现实世界测试中最难但最重要的部分是拥有可重复的负载模拟，该模拟类似于应用程序的实际使用情况。这是开发和部署应用程序的重要步骤，需要您的开发和 DevOps 团队之间的合作。

您希望从这样的测试中了解一些重要的结果：定义应用程序所需的内存量并测试最大吞吐量。以下是一些实现此目标的指南：

**慢慢来**: 当执行 Java 应用程序时，JVM 会将最常用的字节码（类文件）重新编译为本地代码。此过程需要一些时间（称为预热时间），因此您需要等待应用程序在您期望的典型负载下运行足够长的时间。这意味着所有执行的代码都已由施加在应用程序上的负载调用。**注意本地测试**: 一些测试可以轻松地在您自己的机器上执行，但请注意测试本身的负载。在运行应用程序的同一台机器上执行负载测试会导致 CPU 和/或内存过载，从而 [影响](https://thenewstack.io/does-garbage-collection-logging-affect-app-performance/) 测试中应用程序的性能。**使用现实世界测试**: 只有当您可以在类似于生产系统的环境中模拟预期负载时，测试才有效。**在生产环境中测试**: GC 日志对系统性能的影响很小。在许多情况下，与设置完整的测试环境相比，这将是获取真实日志结果的更轻松、更便宜的解决方案。

## 使用 Spring PetClinic 进行实验

我使用 Spring PetClinic 应用程序来收集本文的测试结果。源代码可在 GitHub 上获得，其中包括 JMeter 测试脚本。

## 运行测试应用程序

要遵循此方法，请获取源代码，编译应用程序并使用以下命令启动它：

```bash
java -Xms1g -Xmx1g -XX:+UseG1GC -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintGCApplicationConcurrentTime -XX:+PrintGCApplicationStoppedTime -XX:+PrintHeapAtGC -Xlog:gc*:gc.log -jar target/spring-petclinic-2.5.8.BUILD-SNAPSHOT.jar
```

您的应用程序现在已配置为将垃圾收集日志存储在一个文件中。此设置非常适合此测试。但在生产环境中启用 GC 日志时，您应该使用滚动文件以防止文件变得太大并填满存储空间。例如，使用 `-Xlog:gc,safepoint:gc.log::filecount=10,filesize=100M` 将日志轮换设置为最多 10 个文件，每个文件 100MB。当您未定义文件数量和文件大小时，默认值为 5 个文件，每个文件 20MB，因此 GC 日志不会使用超过 100MB 的空间。

## 关于 JMeter

Spring PetClinic 项目包含一个 JMeter 测试。可以使用 Apache JMeter 执行此类测试，Apache JMeter 是一个 100% 纯开源 Java 应用程序，旨在对功能行为进行负载测试并衡量性能。它最初是为测试 Web 应用程序而设计的，但后来扩展到其他测试功能。查看最新版本（在 [jmeter.apache.org/download_jmeter.cgi](https://jmeter.apache.org/download_jmeter.cgi) 上）并下载它。

JMeter 测试可以使用 GUI 应用程序执行，但不建议这样做，因为它会带来 GUI 影响测试性能的风险。GUI 仅应用于创建测试或运行测试以验证其配置。

## 使用 JMeter GUI 创建测试

启动 Apache JMeter GUI 应用程序：

`$ java -jar ~/Downloads/apache-jmeter-5.6.3/bin/ApacheJMeter.jar`

- 在 UI 中，单击文件 > 打开，然后选择文件 `spring-petclinic/src/test/jmeter/petclinic_test_plan.jmx`。
- 您可以通过点击开始按钮来执行测试以验证配置，这将启动线程来模拟 500 个用户。
- 运行测试直到测试完成。活动线程数将从 500 降至 0。
## 使用 JMeter 在无头模式下运行负载测试

对于实际测试，我们将以无头模式执行 JMeter。在我的情况下，我在运行应用程序的同一台机器上执行测试，因为它有足够的内存和 CPU 来处理两者。使用相同方法时，您需要确保这对于您的测试有效。

让我们运行一个测试并使用以下选项生成报告：

**-n**: 在无头模式下运行（无 GUI）**-t**: 要执行的 `.jmx` 测试脚本的路径**-l**: 用于存储原始结果的 `.jtl` 文件的路径**-o**: 负载测试后生成报告仪表板的输出文件夹的路径，该文件夹必须为空目录**-e**: 负载测试后生成报告仪表板
`$ java -jar ApacheJMeter.jar -n -t spring-petclinic/src/test/jmeter/petclinic_test_plan.jmx -l jmeter.jtl -o jmeter-report/ -e`
当您不添加 -e 选项时，您仍然可以根据测试运行期间创建的 `.jtl` 文件稍后生成 HTML 报告。

**-g**: 测试期间生成的 `.jtl` 文件的路径**-o**: 用于存储 HTML 报告的文件夹
`$ java -jar ApacheJMeter.jar -g jmeter.jtl -o jmeter-report/`
由于每个新的 Java 运行时版本都带来了性能改进，因此了解您的生产系统使用哪个版本非常重要。我使用 Azul Zulu Builds of OpenJDK 版本 21.0.3 执行了我的测试。

## 阅读 JMeter 报告

在 JMeter HTML 报告目录（在我的情况下为 `jmeter-report/`，如 -o 参数指定）中，您可以找到包含 JMeter 测试结果的网页。您不会在这里找到任何与内存相关的信息，但会找到 JMeter 测试文件中定义的测试结果。例如：响应时间百分位数、每秒命中数的吞吐量等。

## 检查 GC 日志结果

`gc.log` 文件是了解应用程序内存使用情况的“最佳位置”。使用 Azul GC Log Analyzer，我们可以读取此文件并可视化一段时间（挂钟时间和正常运行时间）内的一组图表，以检查垃圾收集器、JIT（即时）编译器、系统指标等。以下图表显示，垃圾收集器暂停持续时间在初始负载后保持在 10 毫秒以下，垃圾收集后的堆大小保持在 64MB 左右。我们建议您使用该值的双倍来确定系统尺寸。因此，在这种情况下，应用程序将能够处理与测试期间生成的相同负载，内存为 128MB。

您可以对您的应用程序遵循相同的原则，并在更改 Java 运行时的 `–Xmx` 设置或虚拟环境的内存配置后重新检查暂停持续时间和堆使用情况。

## Azul Zing 和 Zulu Builds of OpenJDK 之间的 GC 日志差异

通过不同的内部基准测试，我们创建了一些额外的日志文件来演示 Azul Zulu 和 Zing Builds of OpenJDK 版本 17 提供的不同结果。

### 使用 Zulu 的结果

当我们使用 Zulu（OpenJDK 的一个版本）生成 GC 日志时，我们在日志文件中获得与大多数其他发行版相同的数据。以下图表显示，垃圾收集器暂停持续时间保持在 80 毫秒以下，垃圾收集后堆利用率保持在旧一代的 1GB 左右（用于长期对象）和新一代的 2GB 左右（用于临时对象）。

在这个特定的测试用例中，总共 `-Xmx4G` 足够并且实际上被使用，但通常标准建议是将 `-Xmx` 设置为观察到的堆利用率的两倍；在这里，它将是 `-Xmx6G`。

### 使用 Zing 的结果

我们使用 Zing 重复了相同的测试，Zing 是一种基于 OpenJDK 的替代 Java 运行时，但它具有更好的 JIT 编译器（Falcon）和额外的垃圾收集器（C4，持续并发压缩收集器）。

由于 C4 垃圾收集器提供的额外信息，图表看起来略有不同。使用并发 GC 时，GC 在与应用程序并行活动时的并发持续时间是一个更重要的指标。它不会暂停应用程序，但会消耗一些 CPU 时间。100% 并不意味着它消耗了所有 CPU 时间的 100%，因为基准 100% 是 GC 线程的总数，这少于 CPU 内核的数量。但应通过增加堆大小来避免长时间保持在 100%。大多数时间通常由 GC 用于处理临时对象。在这里，在这个特定的测试用例中，与具有相同 `-Xmx4G` 的 Zulu 相比，应用程序性能在 Zing 中仍然更好。

对于一般大小调整，Zing 的 Live Set 图表也很重要，因为它显示了活动对象的数量，例如，不包括未引用的对象，也称为垃圾。

## 结论
垃圾收集器日志提供了检查应用程序需要多少内存的正确指标。能够在与生产系统相同的环境中，以类似的负载测试应用程序至关重要。也许“在生产环境中测试”可能是实现这一目标的最简单方法。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等。