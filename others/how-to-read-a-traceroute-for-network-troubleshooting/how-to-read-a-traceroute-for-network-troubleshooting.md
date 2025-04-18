
<!--
title: 如何阅读Traceroute以进行网络故障排除
cover: https://cdn.thenewstack.io/media/2025/04/861e0b4c-route.png
summary: 网络故障排查利器！详解 traceroute 原理及应用，助你快速定位网络瓶颈。掌握 Windows、macOS 和 Linux 下 traceroute 命令，解读 RTT、跃点信息，识别超时等问题。更有高级 Traceroute InSession 和 Pietrasanta Traceroute 方案，穿透防火墙，精准诊断现代网络。
-->

网络故障排查利器！详解 `traceroute` 原理及应用，助你快速定位网络瓶颈。掌握 Windows、macOS 和 Linux 下 `traceroute` 命令，解读 `RTT`、跃点信息，识别超时等问题。更有高级 `Traceroute InSession` 和 `Pietrasanta Traceroute` 方案，穿透防火墙，精准诊断现代网络。

> 译自：[How To Read a Traceroute for Network Troubleshooting](https://thenewstack.io/how-to-read-a-traceroute-for-network-troubleshooting/)
> 
> 作者：Alessandro Improta

traceroute 工具是可用于[网络](https://thenewstack.io/networking/)故障排除的最有价值但最直接的诊断实用程序之一。traceroute 内置于几乎每个操作系统中，它运行从一台计算机到另一台设备的连接测试，显示数据在网络设备之间采用的每个“跃点”。

本综合指南将帮助您了解 traceroute 的工作原理、解释其结果并识别它可以揭示的常见网络问题。

## Traceroute：了解它的作用

要了解 traceroute 的实际应用，我们可以从一个简单的示例开始，即从您的计算机到 Catchpoint 的服务器运行 traceroute。每个人的具体结果会有所不同。但是，在大多数情况下，结果会显示数据包从您的计算机到达 Catchpoint 的服务器并返回大约 4 到 20 个“跃点”。第一个很可能是您的本地路由器，从那里，数据将通过您的内部网络进行多次“跃点”，并通过您的互联网服务提供商 (ISP) 并通过互联网，最终到达 Catchpoint 的服务器。

图 1 显示了您在 Windows 计算机的命令提示符下可能看到的内容示例。

![图 1：traceroute 命令和生成的结果的图像。](https://cdn.thenewstack.io/media/2025/04/e659ca9c-figure-1-1021x1024.png)

*图 1：traceroute 命令和生成的结果的图像。*

了解如何运行此工具以及运行 traceroute 命令时显示的不同信息意味着将帮助您[排除各种类型的问题](https://thenewstack.io/devops-as-a-graph-for-real-time-troubleshooting/)。

## Traceroute 的剖析

Traceroute 通常与密切相关的 ping 工具相关联。因此，人们通常认为，像 ping 一样，它在所有平台上都是标准化的。然而，事实并非如此。

**Windows traceroute** 专门使用 Internet 控制消息协议 (ICMP)（与 ping 相同的协议）。**macOS 和 Linux** 通常默认使用用户数据报协议 (UDP) 进行 traceroute，但也可以配置为使用 ICMP 或传输控制协议 (TCP)。

尽管存在这些差异，traceroute 的核心功能（向您显示源和目标之间的每个跃点）保持不变。

## 如何运行 Traceroute 并解释结果

运行 traceroute 非常简单。首先，在您的计算机上调出命令提示符。对于 Windows 10，单击“开始”按钮并键入 CMD 以调出“命令提示符”选项，然后单击“命令提示符”应用以将其打开。

![图 2：Windows 10 中的命令提示符选项。](https://cdn.thenewstack.io/media/2025/04/45107265-image2.png)

*图 2：Windows 10 中的命令提示符选项。*

加载命令提示符后，键入命令 `tracert` 后跟您要测试的目标。例如，要在 catchpoint.com 上运行测试，您将键入 `tracert catchpoint.com` 然后按 Enter。（对于 [Linux](https://www.linux.com/news/cli-magic-introduction-traceroute/) 和 [macOS](https://macreports.com/how-to-run-traceroute-on-macos/) 设备，您将键入 `traceroute catchpoint.com` 代替。）

当您查看 traceroute 结果时，您会看到以类似表格格式组织的几个关键信息：

| 跃点数 | RTT 尝试 1 | RTT 尝试 2 | RTT 尝试 3 | 跃点详细信息 |
|---|---|---|---|---|
| 1 | 2ms | 1ms | 1ms | 10.0.0.1 |
| 2 | 10ms | 10ms | 10ms | 96.120.40.245 |
| 3 | 10ms | 11ms | 12ms | 96.110.175.85 |

*表 1：traceroute 结果的表示。*

**跃点数：** 数据通过的每个设备都被视为一个跃点。这可以是路由器、交换机、服务器或计算机。

**往返时间 (RTT)：** 您通常会看到三次尝试（三个 RTT 列）。每个条目显示数据到达该跃点并返回到您所花费的时间。显着差异可能表明存在问题或间歇性延迟。

**跃点详细信息：** 您可以在此处看到 IP 地址，或者在某些情况下，可以看到域名。某些设备会显示额外信息，或者可能配置为不显示任何内容（以星号表示）。

## 使用 Traceroute 发现的常见网络问题

您可以使用此命令查找各种网络问题，以根据显示的结果确定可能存在的问题类型。

**各个点的星号（超时）**

您在使用 traceroute 时会看到的最常见问题是超时响应，它由星号 (*) 表示。这些情况经常发生，并且有多种不同的原因。在以下示例中，您可以看到尝试对 google.com 运行 traceroute 时，多个跃点都有星号。

![图 3：traceroute 到 Google 的示例输出。](https://cdn.thenewstack.io/media/2025/04/d1c21c02-figure-3-1024x678.png)

*图 3：traceroute 到 Google 的示例输出。*

当您看到星号时，它将表示以下情况之一：

- **跃点上的单个星号：** 这表示请求在三次尝试中的一次超时。这可能表明该跃点存在间歇性问题。
- **三个星号，然后失败：** 如果您看到一个跃点的所有三次尝试都显示星号，然后 traceroute 报错，则表示该跃点已完全关闭。
- **三个星号，然后成功：** 如果您看到一个跃点的三次尝试都失败了，但之后 traceroute 的其余部分继续进行而没有问题，那么这实际上根本不是问题。这仅仅意味着（如前所述）该跃点上的设备配置为不响应 ping 或 traceroute，因此尝试超时。

**一个跃点后延迟升高**

如果一切看起来都很好，但随后响应时间在一个点上显着跃升，并且之后的每个跃点都保持很高，则可能意味着该跃点或其与前一个跃点之间的连接存在问题。由于从您到每个连续跃点的连接都必须经过该跃点，因此它们都会受到它引起的延迟的影响。

如果您可以确定该跃点的位置，则可以与该连接的所有者合作来解决问题。问题通常出在他们的数据电路上。

如果您不知道该连接的所有者并且此延迟导致严重问题，您或许可以与您的 ISP 合作，让您的流量绕过该点。

**一个跃点的延迟升高**

如果您看到一个跃点的响应时间升高，但之后其余跃点恢复正常，则无需担心。这仅仅意味着该跃点上的设备配置为使响应 traceroute 的优先级较低，这会导致这种类型的延迟。虽然 traceroute 上可能存在延迟，但这种缓慢不会影响正常的互联网流量。

## Windows、macOS 和 Linux 上的 Traceroute 比较

所有主要的[操作系统](https://thenewstack.io/choosing-an-operating-system-and-container-runtime-for-your-cloud-native-stack/)——Windows、macOS 和 Linux——都内置了 traceroute，但它们的语法、协议和自定义选项有所不同。

下表重点介绍了 Windows、macOS 和 Linux 操作系统上 traceroute 实现之间的一些主要区别：

| 功能         | Windows             | macOS               | Linux               |
|--------------|---------------------|---------------------|---------------------|
| 命令名称     | tracert             | traceroute          | traceroute          |
| 默认协议     | ICMP Echo Requests  | UDP                 | UDP                 |
| 更改协议     | 不适用（仅 ICMP）   | -I 用于 ICMP，-T 用于 TCP SYN | -I 用于 ICMP，-T 用于 TCP SYN |
| 每个跃点的探测次数 | 3（固定）          | 默认 3，可以使用 -q 更改 | 默认 3，可以使用 -q 更改 |
| 最大跃点数的默认值 | 30                  | 30                  | 30                  |
| 选项         | 有限 (-d, -h, -w)   | 广泛 (-m, -q, -p, etc.) | 广泛 (-m, -q, -p, etc.) |
| 连续跟踪     | 否                  | 否                  | 否                  |
| 输出格式     | 简化，包含基本信息  | 详细，包含数据包大小、TTL 等 | 详细，包含数据包大小、TTL 等 |
| 安装         | 内置（命令提示符/PowerShell） | 内置（终端）        | 通常内置，如果缺少则可安装 |
| 可自定义的超时 | 是，使用 -w（以毫秒为单位） | 是，使用 -W（以秒为单位） | 是，使用 -w 或 -W（以秒为单位） |
| 解析主机名     | 默认                | 默认，可以使用 -n 禁用 | 默认，可以使用 -n 禁用 |
| IPv4/IPv6 支持 | 两者都支持，使用 -4 或 -6 强制 | 两者都支持，使用 -4 或 -6 强制 | 两者都支持，使用 -4 或 -6 强制 |
| 数据包大小     | 固定（无法更改）    | 可使用 -q 调整      | 可使用 -q 调整      |

有关 macOS 和 Linux 环境中 traceroute 的更多信息，请访问以下链接：

## 传统 Traceroute 实现的局限性

在许多网络配置和功能场景中，可能会干扰传统的 traceroute 实现。因此，traceroute 的结果可能会产生误导。

**防火墙和安全设备**

现代防火墙通常会过滤掉或降低 ICMP 和 UDP 探测的优先级，从而导致路径不完整和数据包丢失严重。这种过滤会误导用户认为网络存在问题，而实际上可能只是安全配置导致了中断。

**负载均衡**

负载均衡是一种网络设计技术，允许数据通过多个路径遍历网络，从而最大限度地利用可用基础设施的带宽。负载均衡可以沿着不同的路径路由数据包，从而进一步扭曲 traceroute 显示的结果。

**网络地址转换 (NAT)**

NAT（网络地址转换）会在数据包通过路由器时修改数据包头中的 IP 地址，从而使 traceroute 难以准确映射网络路径。IP 地址的更改可能导致误导性的 traceroute 结果，因为表面上的源或目标 IP 地址可能无法反映真实的网路路径。

**Traceroute 的其他障碍**

虽然这些是可能干扰 traceroute 的最常见的网络服务和功能，但仍然存在其他因素，包括：

- 非对称路由，数据包采用不同的路径往返于目的地。
- ICMP 速率限制或节流可能会导致 ICMP 响应延迟或丢弃，从而导致高延迟或数据包丢失的错误指示。
- 服务质量 (QoS) 策略用于优先处理或降低某些类型的流量的优先级。traceroute 使用的数据包的优先级可能会低于其他流量类型，从而导致延迟和数据包丢失的测量不准确。
- 在虚拟化环境或云网络中，物理网络路径可能与 traceroute 看到的虚拟化网络路径不直接对应。此外，云提供商基础设施内部的内部路由可能对用户不完全可见，从而导致 traceroute 结果失真。

## 适用于现代网络的高级 Traceroute 解决方案

Catchpoint 提供了具有增强功能的 traceroute 工具，用于诊断网络路径和性能问题，包括 [Traceroute InSession](https://www.catchpoint.com/blog/traceroute-insession-a-traceroute-tool-for-modern-networks)，它在进行 traceroute 之前建立完整的 TCP 会话，帮助它通过防火墙和安全过滤器，以及 [Pietrasanta Traceroute](https://www.catchpoint.com/blog/install-pietrasanta-traceroute-on-windows-11)，它支持多种协议（UDP、TCP、QUIC），并包括 TCP InSession 等功能来模拟实际应用程序流量。

查看以下资源，了解有关这些工具如何帮助您精确诊断网络问题并优化性能的更多信息。

- 要试用 Pietrasanta Traceroute 程序，请访问 [Catchpoint 的 GitHub 页面。](https://github.com/catchpoint/Pietrasanta-traceroute)
- 要了解 Catchpoint 的工程师 Luca Sani 关于 Pietrasanta Traceroute 的信息，请观看他的 [在 RIPE 87, Rome 2023 上的演讲](https://ripe87.ripe.net/archives/video/1171/)。
- 要了解更多关于使用 Pietrasanta Traceroute 检测显式拥塞通知 (ECN) 漂白的信息，请观看 Sani 的 [在 RIPE 88, Krakow 2024 上的演讲](https://ripe88.ripe.net/archives/video/1298/)。