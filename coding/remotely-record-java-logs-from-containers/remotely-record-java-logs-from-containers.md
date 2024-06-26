
<!--
title: 从容器中远程记录 Java 日志的方法
cover: https://cdn.thenewstack.io/media/2024/06/20a8222a-remotely-record-java-logs-from-containers.jpg
-->

即使无法访问 JVM 的命令行，也可以访问 Java Flight Recorder 指标来检查应用程序的运行状况。

> 译自 [How to Remotely Record Java Logs from Containers](https://thenewstack.io/remotely-record-java-logs-from-containers/)，作者 Matt Van Order。

[Java Flight Recorder](https://thenewstack.io/your-guide-to-navigating-openjdk-in-2023/) (JFR) 是用于记录和查看 [Java 虚拟机 (JVM)](https://thenewstack.io/how-to-avoid-overprovisioning-java-resources/) 和系统指标的首选技术。JFR 日志揭示了有关正在运行的应用程序、JVM 的运行状况和系统稳定性的许多信息。您可以通过进入命令行或终端并输入一些命令来访问 JFR 日志。

但是，如果您没有直接访问运行 JVM 的系统上的命令行或终端，例如当 JVM 在 [容器](https://thenewstack.io/containers/) 中运行时，该怎么办？

幸运的是，您可以使用 JVM 的 Java 管理扩展 (JMX) 连接器和用于分析 JVM 基于应用程序的工具，无需太多配置即可获取 JFR 日志。您需要具备 JVM、JFR 和 JFR 日志的工作知识才能完成本教程。

## 在您的 JVM 上设置 JMX

在您可以在命令行或终端之外访问 JVM 之前，您必须设置 JVM 以便通过远程连接进行发现和访问。您可以通过简单地启用 JVM 的 JMX 连接器来实现这一点。使用以下 VM 参数配置您的 Java 应用程序：

* `-Dcom.sun.management.jmxremote`：启用 JMX/JMXRMI（Java 管理扩展远程管理接口）连接。
* `-Dcom.sun.management.jmxremote.host=<IP/Hostname>`：设置 JMX 连接的地址。使用运行 Java 程序的计算机或容器的外部 IP 地址或主机名。
* `-Dcom.sun.management.jmxremote.port=<port>`：设置 JMX 连接的 TCP 端口。
* `-Djava.rmi.server.hostname=<IP/hostname>`：设置 JMXRMI 连接的地址。使用与 JMX 连接相同的 IP/主机名。
* `-Dcom.sun.management.jmxremote.rmi.port=<port>`：设置 JMXRMI 连接的 TCP 端口。使用与 JMX 连接相同的 TCP 端口。
* `-Dcom.sun.management.jmxremote.local.only=false`：如果您要从另一台机器连接到 JVM，则必须从 localhost 解绑端口。

此外，您可能希望使用以下方法启用 JMX 身份验证/SSL：

* `-Dcom.sun.management.jmxremote.authenticate=true`
* `-Dcom.sun.management.jmxremote.ssl=true`

例如：

```
-Dcom.sun.management.jmxremote \
-Dcom.sun.management.jmxremote.host=192.168.0.166 \
-Dcom.sun.management.jmxremote.port=7091 \
-Djava.rmi.server.hostname=192.168.0.166 \
-Dcom.sun.management.jmxremote.rmi.port=7091 \
-Dcom.sun.management.jmxremote.local.only=false \
-Dcom.sun.management.jmxremote.authenticate=false \
-Dcom.sun.management.jmxremote.ssl=false
```

## 使用 Azul Mission Control 连接到远程 JVM

首先，您需要一个用于分析 JVM 基于应用程序的工具。为了演示目的，我将使用 Azul Mission Control，它是免费下载的。如果您没有 Azul Mission Control，请访问 [Azul Mission Control 下载页面](https://www.azul.com/products/components/azul-mission-control/#downloads)。

其他类似的工具包括 [Oracle](https://developer.oracle.com/?utm_content=inline+mention) JDK Mission Control、VisualVM、JProfiler、YourKit Java Profiler、AppDynamics for Java、Dynatrace、New Relic APM、Glowroot 和 Java Flight Recorder (JFR)。

在 Azul Mission Control 中，转到 **JVM 浏览器** 并单击 **添加 JVM 连接** 按钮以创建新的自定义 JVM 连接。

![](https://cdn.thenewstack.io/media/2024/06/1126eb4e-jvmbrowserconnectbutton_1.png)

指定远程系统的 hostname/IP 地址和 JMX 端口号。

如果启用了 JMX 身份验证，请输入用户名和密码。

单击 **Test Connection** 以确保您的远程 JVM 可访问，然后单击 **完成**。

![](https://cdn.thenewstack.io/media/2024/06/ff78b43e-newconnection_2.png)

您的远程 JVM 现在将显示在 JVM 浏览器中。

![](https://cdn.thenewstack.io/media/2024/06/c465e987-jvmbrowserconnectionsuccess_3.png)

根据您的网络和容器设置，可能需要设置端口转发。如果您需要有关 [端口转发](https://thenewstack.io/linux-create-encrypted-tunnels-with-ssh-port-forwarding/) 的帮助，请联系您的网络管理员。

## 从您的远程 JVM 记录 JFR

现在您已远程连接到 JVM，是时候进行 JFR 记录了。

在 Azul Mission Control 中，转到 JDK 浏览器，右键单击您的远程 JVM 连接并选择 **Start Flight Recording**。

![](https://cdn.thenewstack.io/media/2024/06/cd103a98-startnewfrdropbox_4.png)

根据 JFR 日志的大小和/或年龄，选择您喜欢的选项和时间间隔（固定时间记录或连续记录），然后单击 **Finish**。

![](https://cdn.thenewstack.io/media/2024/06/d3dae2e8-startnewfr_5.png)

您的远程 JFR 记录已开始。您快完成了！

通过在 JVM 浏览器中展开远程 JVM 连接来检查记录的进度。

![](https://cdn.thenewstack.io/media/2024/06/c6e0caf4-recordingprogress_6.png)

录制完成后，您的 JFR 日志将在 Azul Mission Control 中自动打开。现在您可以查看 **Outline** 选项卡，更深入地了解您的 JVM 的 [性能](https://thenewstack.io/does-garbage-collection-logging-affect-app-performance/) 概况。