
<!--
title: eBPF探针与你：寻踪内核源头
cover: https://blog.px.dev/static/51737f5fbe33debfd2e62bdd9c7ade08/a6d66/probe-investigation-overview.png
-->

eBPF 能够为网络、可观测性和安全用例重新编程内核，这是一种令人难以置信的超能力。但是，要开始使用该技术，您必须首先了解如何以及在何处挂钩到 Linux 内核。该技术提供了进入内核几乎任何部分的方法，但这种灵活性是有代价的——如果您不熟悉 Linux 源代码/内核 API，将其应用于新领域将令人生畏。

> 译自 [eBPF TLS tracing: The Past, Present and Future](https://blog.px.dev/ebpf-tls-tracing-past-present-future/)，作者 None。

如今，许多可用的 eBPF 资源都在探讨如何为众所周知的钩子（系统调用、XDP 等）编写 eBPF 程序，并将未来的应用程序留给读者。虽然学习编写程序是成功的一半，但在不知道在哪里附加以及附加点可用的数据结构的情况下，您无法开始编写程序。因此，选择正确的探针对于解决新挑战至关重要，甚至可以帮助避免复杂性和不稳定的 API。

在这篇文章中，我们将探讨检查 Linux 源代码以编写 eBPF 程序的策略。这些策略将提供无所畏惧地浏览 Linux 所需的技能，并且最近被用来通过套接字的本地地址来补充 [Pixie](https://px.dev) 协议跟踪（[pixie#1989](https://github.com/pixie-io/pixie/pull/1989)）。

## ftrace 简介：Linux 函数追踪器

Ftrace 是 Linux 的函数跟踪器。虽然它已经发展成为一套跟踪实用程序，但就我们的目的而言，它可以被认为是一种跟踪 Linux 中任何函数的进入和退出的方法。 这种动态跟踪由添加到每个内核函数开头的 nop 指令支持。禁用跟踪时，这些 nop 会保留在原位，并且内核保持高性能。当请求跟踪时，ftrace 会将这些 nop 转换为记录函数调用图的指令（请参阅 [Ftrace 简介](https://events.static.linuxfound.org/sites/events/files/slides/slides_0.pdf)）。

虽然 ftrace 的主要接口是通过 `/sys/kernel/debug/tracing` 目录，但使用 ftrace 前端（例如 [trace-cmd](https://man7.org/linux/man-pages/man1/trace-cmd.1.html)）通常更方便。Trace-cmd 可以轻松地为临时跟踪制作单行代码，因此它更适合我们的用例。典型的工作流程包括记录跟踪（[trace-cmd record](https://man7.org/linux/man-pages/man1/trace-cmd-record.1.html)），然后使用命令检查跟踪文件（[trace-cmd report](https://man7.org/linux/man-pages/man1/trace-cmd-report.1.html)）。

Ftrace 提供了丰富的配置选项。为了确定在何处添加 eBPF 程序，我们不会研究这些可能性，但我建议查看[内核文档和其他 ftrace 资源](/ebpf-probes-and-you/#ftrace-resources)以获取更多详细信息。

## 通过 eBPF 捕获套接字的本地地址

[Pixie](https://px.dev) 是一款适用于 K8s 的可观测性工具，它提供微服务之间的协议跟踪（请求/响应跨度）。Pixie 通过套接字系统调用上的 eBPF 钩子捕获这些跨度。此跟踪中的一个空白是缺少连接的本地地址（IP 和端口）。考虑到这一点，让我们探讨 ftrace 如何识别正确的函数来探测以捕获此信息。

套接字系统调用 API 提供对连接远程详细信息的轻松访问。由于 eBPF 可以检查内核函数的参数，因此这些参数很容易访问，以及 Pixie 如何跟踪连接的远程端。不幸的是，连接的本地端是通过套接字文件描述符引用的。有一些用户空间 API 可以检查 fd（[getsockname](https://man7.org/linux/man-pages/man2/getsockname.2.html)、netlink [sock_diag](https://www.man7.org/linux/man-pages/man7/sock_diag.7.html)），但 BPF 受限环境中没有等效的接口。

```c
ssize_t sendto(int sockfd, const void buf[.len], size_t len, int flags,
              const struct sockaddr *dest_addr, socklen_t addrlen);

int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);

ssize_t sendmsg(int sockfd, const struct msghdr *msg, int flags);
# msg->msg_name contains the struct sockaddr
```

*各种带参数的 Linux 套接字系统调用函数，这些参数存储了连接的远程端。*

调查的开始是在 ftrace 的函数图跟踪器下运行 curl 命令。这提供了为此命令提供服务的所有内核函数，并且是拦截本地地址和端口的潜在候选者。以下调用仅为 curl 命令启用 ftrace（`-F` 参数），因此已过滤掉对其他进程的任何内核处理。

```bash
sudo trace-cmd record -F -p function_graph curl http://google.com
```

由于内核代表我们执行许多复杂的操作，因此需要将结果跟踪过滤到套接字处理。为此，我们需要首先将跟踪过滤到系统调用。可以通过搜索任何带有 `_*x64_sys*` 前缀的函数来识别它们，如下所示：

```
curl-965264 [003] 856720.850841: funcgraph_entry:                   |  __x64_sys_sendto() {
curl-965264 [003] 856720.850841: funcgraph_entry:                   |    x64_sys_call() {
curl-965264 [003] 856720.850841: funcgraph_entry:                   |      __sys_sendto() {
curl-965264 [003] 856720.850842: funcgraph_entry:                   |        sockfd_lookup_light() {
curl-965264 [003] 856720.850842: funcgraph_entry:        0.301 us   |          __fdget();
curl-965264 [003] 856720.850843: funcgraph_exit:         0.794 us   |        }
curl-965264 [003] 856720.850843: funcgraph_entry:                   |        security_socket_sendmsg() {
curl-965264 [003] 856720.850843: funcgraph_entry:                   |          apparmor_socket_sendmsg() {
curl-965264 [003] 856720.850843: funcgraph_entry:                   |            aa_inet_msg_perm() {
curl-965264 [003] 856720.850844: funcgraph_entry:                   |              __cond_resched() {
curl-965264 [003] 856720.850844: funcgraph_entry:        0.267 us   |                rcu_all_qs();
curl-965264 [003] 856720.850844: funcgraph_exit:         0.736 us   |              }
curl-965264 [003] 856720.850845: funcgraph_exit:         1.276 us   |            }
curl-965264 [003] 856720.850845: funcgraph_exit:         1.793 us   |          }
curl-965264 [003] 856720.850845: funcgraph_exit:         2.326 us   |        }
```

从这里，我们开始调查套接字发送系统调用的子功能（`sendto`、`sendmsg`、`sendmmsg`）。由于这些系统调用包含到套接字的完整传输，因此如果探测到子功能，则可以避免额外的状态管理。例如，可以从套接字系统调用中捕获本地地址，然而，正确实现这可能会很复杂。已知 Web 服务器具有预分叉线程模型，这些模型会从不同的线程发出套接字和 sendto/sendmsg/sendmmsg 系统调用。虽然此架构对客户端不太了解，但从单个系统调用中捕获数据会限制任何潜在的未知因素。

![](https://blog.px.dev/static/51737f5fbe33debfd2e62bdd9c7ade08/44d59/probe-investigation-overview.png)

*说明了这个新的预期探测器如何工作的图表*

随着我们发现相关函数，它们交叉引用 https://elixir.bootlin.com/ 来识别某个函数是否可行。理想的函数应包含套接字数据结构作为参数或返回值（eBPF 接口可访问），并且是一个稳定的内核接口。在查看多种选项后，tcp_v4_connect 和 tcp_v6_connect 显然成为当之无愧的选择。这些函数的第一个参数包含 sock 结构，其中包含本地地址。从稳定性的角度来看，这些函数在 tcp_prot 和 tcpv6_prot 结构内进行定义。在 C 编程中，使用包含函数指针的结构来定义 OOP 之类的接口很常见——这意味着这些函数比随机的内核函数更可能是稳定的。在不同内核版本中检查此函数原型验证了该假设。

根据我们之前处理这些套接字跟踪用例的经验，我们知道此功能将不足以解决问题。我们检查的 curl 命令会创建一个新的 TCP 连接，但对于正在传输中拾取的连接（长期存在的 TCP 连接）又该如何？

利用研究这些内核功能的流程，让我们将该流程重新应用于正在传输的连接。

为了模拟这种情况，我们使用 netcat 作为服务器端，使用 telnet 作为客户端。在 telnet 连接后附加 Ftrace，以限制跟踪范围至正在发送的消息。

```c
(term1) $ nc -l 8000 -v & 
(term1) $ telnet localhost 8000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.

(term2) sudo trace-cmd record -P ${pid_of_telnet} -p function_graph

# tcp_v4_connect was missed as expected
(term2) sudo trace-cmd report | grep tcp_v4_connect

(term2) sudo trace-cmd report | grep tcp_sendmsg
   telnet-1554313 [004] 1183569.050034: funcgraph_entry: | tcp_sendmsg() {
```

在查看跟踪报告后，识别出 tcp_sendmsg 函数。该函数也存在于 tcp_prot 和 tcpv6_prot 中，这增强了我们对其稳定性的信心。通过新的连接和中间流情况的涵盖，这结束了捕获本地地址的调查！

20 行 eBPF 代码之后，Pixie 就能够捕获 tcp 套接字的本地地址！虽然更改本身很小，但了解内核的 TCP 状态机并通过 ftrace 浏览源代码对于实施至关重要。我们发现 ftrace 是 eBPF 编程的宝贵工具，并建议您将其添加到您的工具库中！

## 附录

Ftrace 资源

- [ftrace：跟踪你的内核函数！](https://jvns.ca/blog/2017/03/19/getting-started-with-ftrace/) (2017 年 3 月，Julia Evans)
- [trace-cmd：Ftrace 的前端](https://lwn.net/Articles/410200/) (2010 年 10 月，Steven Rostedt)
- [使用 Ftrace 调试内核 - 第 1 部分](https://lwn.net/Articles/365835/) (2009 年 12 月，Steven Rostedt)
- [使用 Ftrace 调试内核 - 第 2 部分](https://lwn.net/Articles/366796/) (2009 年 12 月，Steven Rostedt)
- [内核文档](https://www.kernel.org/doc/html/v4.17/trace/ftrace.html)

Ftrace 深度剖析

- [通过 Ftrace 理解 Linux 内核](https://www.youtube.com/watch?v=2ff-7UTg5rE) - (2017 年，Steven Rostedt)