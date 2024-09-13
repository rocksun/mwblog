```
Ctrl/Cmd + K

**Dom Del Nano**

*2024 年 9 月 9 日*  • 阅读时间：4 分钟

*Pixie 核心维护者*

eBPF 能够为网络、可观察性和安全用例重新编程内核，这是一种令人难以置信的超能力。但是，要开始使用该技术，您必须首先了解如何以及在何处挂钩到 Linux 内核。该技术提供了进入内核几乎任何部分的方法，但这种灵活性是有代价的——如果您不熟悉 Linux 源代码/内核 API，将其应用于新领域将令人生畏。

如今，许多可用的 eBPF 资源都在探讨如何为众所周知的钩子（系统调用、XDP 等）编写 eBPF 程序，并将未来的应用程序留给读者。虽然学习编写程序是成功的一半，但在不知道在哪里附加以及附加点可用的数据结构的情况下，您无法开始编写程序。因此，选择正确的探针对于解决新挑战至关重要，甚至可以帮助避免复杂性和不稳定的 API。

在这篇文章中，我们将探讨检查 Linux 源代码以编写 eBPF 程序的策略。这些策略将提供无所畏惧地浏览 Linux 所需的技能，并且最近被用来通过套接字的本地地址来补充 [Pixie](https://px.dev) 协议跟踪（[pixie#1989](https://github.com/pixie-io/pixie/pull/1989)）。

## Ftrace

Ftrace 是 Linux 的函数跟踪器。虽然它已经发展成为一套跟踪实用程序，但就我们的目的而言，它可以被认为是一种跟踪 Linux 中任何函数的进入和退出的方法。 这种动态跟踪由添加到每个内核函数开头的 nop 指令支持。禁用跟踪时，这些 nop 会保留在原位，并且内核保持高性能。当请求跟踪时，ftrace 会将这些 nop 转换为记录函数调用图的指令（请参阅 [Ftrace 简介](https://events.static.linuxfound.org/sites/events/files/slides/slides_0.pdf)）。

虽然 ftrace 的主要接口是通过 `/sys/kernel/debug/tracing` 目录，但使用 ftrace 前端（例如 [trace-cmd](https://man7.org/linux/man-pages/man1/trace-cmd.1.html)）通常更方便。Trace-cmd 可以轻松地为临时跟踪制作单行代码，因此它更适合我们的用例。典型的工作流程包括记录跟踪（[trace-cmd record](https://man7.org/linux/man-pages/man1/trace-cmd-record.1.html)），然后使用命令检查跟踪文件（[trace-cmd report](https://man7.org/linux/man-pages/man1/trace-cmd-report.1.html)）。

Ftrace 提供了丰富的配置选项。为了确定在何处添加 eBPF 程序，我们不会研究这些可能性，但我建议查看[内核文档和其他 ftrace 资源](/ebpf-probes-and-you/#ftrace-resources)以获取更多详细信息。

## 案例研究：使用 Ftrace 查找本地地址信息

[Pixie](https://px.dev) 是一款适用于 K8s 的可观察性工具，它提供微服务之间的协议跟踪（请求/响应跨度）。Pixie 通过套接字系统调用上的 eBPF 钩子捕获这些跨度。此跟踪中的一个空白是缺少连接的本地地址（IP 和端口）。考虑到这一点，让我们探讨 ftrace 如何识别正确的函数来探测以捕获此信息。
套接字系统调用 API 提供对连接远程详细信息的轻松访问。由于 eBPF 可以检查内核函数的参数，因此这些参数很容易访问，以及 Pixie 如何跟踪连接的远程端。不幸的是，连接的本地端是通过套接字文件描述符引用的。有一些用户空间 API 可以检查 fd（[getsockname](https://man7.org/linux/man-pages/man2/getsockname.2.html)、netlink [sock_diag](https://www.man7.org/linux/man-pages/man7/sock_diag.7.html)），但 BPF 受限环境中没有等效的接口。

```c
ssize_t sendto(int sockfd, const void buf[.len], size_t len, int flags,
conststruct sockaddr *dest_addr, socklen_t addrlen);
int connect(int sockfd, conststruct sockaddr *addr, socklen_t addrlen);
ssize_t sendmsg(int sockfd, const struct msghdr *msg, int flags);
#msg->msg_namecontains the struct sockaddr
```

调查的开始是在 ftrace 的函数图跟踪器下运行 curl 命令。这提供了为此命令提供服务的所有内核函数，并且是拦截本地地址和端口的潜在候选者。以下调用仅为 curl 命令启用 ftrace（`-F`
参数），因此已过滤掉对其他进程的任何内核处理。

```bash
sudo trace-cmd record -F -p function_graph curl http://google.com
```

由于内核代表我们执行许多复杂的操作，因此需要将结果跟踪过滤到套接字处理。为此，我们需要首先将跟踪过滤到系统调用。可以通过搜索任何带有 `_*x64_sys*` 前缀的函数来识别它们，如下所示：

```
<...>
    inet_csk_accept
    tcp_v6_syn_recv_sock create
    inet_csk_create
    inet_create_open
    __sys_socketcall
    do_syscall_64
    entry_SYSCALL_64_after_hwframe
<...>
```
```

- [ftrace：跟踪你的内核函数！](https://jvns.ca/blog/2017/03/19/getting-started-with-ftrace/) (2017 年 3 月，Julia Evans)
- [trace-cmd：Ftrace 的前端](https://lwn.net/Articles/410200/) (2010 年 10 月，Steven Rostedt)
- [使用 Ftrace 调试内核 - 第 1 部分](https://lwn.net/Articles/365835/) (2009 年 12 月，Steven Rostedt)
- [使用 Ftrace 调试内核 - 第 2 部分](https://lwn.net/Articles/366796/) (2009 年 12 月，Steven Rostedt)
- [内核文档](https://www.kernel.org/doc/html/v4.17/trace/ftrace.html)
- [通过 Ftrace 理解 Linux 内核](https://www.youtube.com/watch?v=2ff-7UTg5rE) - (2017 年，Steven Rostedt)
- 内联函数不会显示在此跟踪中。在这些情况下，可以使用最接近的非内联父函数。 [↩](/ebpf-probes-and-you/#fnref-1)
- [服务条款](https://www.linuxfoundation.org/terms) | [隐私政策](https://www.linuxfoundation.org/privacy)

我们是 [云原生计算基金会](https://cncf.io/) 的沙箱项目。

Pixie 最初由 [New Relic, Inc.](https://newrelic.com/) 创建和贡献。

版权所有 © 2018 - Pixie 作者。保留所有权利。| 根据 CC BY 4.0 分发的  内容

Linux 基金会已注册商标并使用商标。有关 Linux 基金会商标列表，请参阅我们的 [商标使用页面](https://www.linuxfoundation.org/trademark-usage)。

Pixie 最初由 [New Relic, Inc.](https://newrelic.com/) 创建和贡献。

本网站使用 Cookie 为您提供更好的用户体验。使用 Pixie，即表示您同意我们 [使用 Cookie](https://linuxfoundation.org/cookies/)。