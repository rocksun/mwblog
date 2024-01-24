<!--
title: 如何利用eBPF程序监控Kubernetes
cover: ./cover.png
-->

对 Kubernetes 集群进行监控对于确保容器化应用程序的健康、性能和可靠性至关重要。Kubernetes 提供了强大的监控工具套件和集成，但是当您需要深入内核和网络级别的复杂性时，eBPF(扩展的伯克利包过滤器)就成为了无价的资源。在本文中，我们将探索惊人的 eBPF 功能，以及如何利用它提升 Kubernetes 监控策略。

> 译自 [How to Use eBPF Capabilities to Navigate Kubernetes Monitoring](https://blog.devgenius.io/how-to-use-ebpf-capabilities-to-navigate-kubernetes-monitoring-2d63cc6510d0)。作者 Dev Genius 。

在 Kubernetes 的背景下，eBPF 在诸如容器网络监控(CNI 插件)、通过基于 eBPF 的网络策略加强安全性以及进行详细的性能分析等任务中发挥着关键作用。通过深入研究 eBPF 的功能，您可以对 Kubernetes 集群获得无与伦比的洞察，从而帮助您排查问题、优化性能并微调基础设施以达到峰值效率。

## 什么是 eBPF?

eBPF是一个强大的技术，它允许在不修改 Linux 内核源代码的情况下，动态地向 Linux 内核中插入自定义代码。这些代码可以用于各种目的，包括网络分析、跟踪和在 [eBPF Kubernetes](https://www.groundcover.com/ebpf/ebpf-kubernetes) 的背景下的可观察性。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/0*3tua7AmeLbFHOUmh)

[来源](https://www.groundcover.com/ebpf/ebpf-kubernetes)

Kubernetes 利用 eBPF 进行各种任务，例如容器网络监控(CNI 插件)、安全性(例如基于 eBPF 的网络策略)和性能分析。

## 设置环境和使用 eBPF 监控 Kubernetes

在我们深入研究基于 eBPF 的 Kubernetes 监控之前，让我们先设置环境。请确保您具备以下前提条件:

- 一个运行中的 Kubernetes 集群
- 安装了 [kubectl](https://kubernetes.io/docs/tasks/tools/) 命令行工具
- Docker 或其他容器运行时
- 基于 Linux 的系统(用于 eBPF 工具)

## 安装必需的工具

要开始，我们需要在您的系统上安装一些与 eBPF 相关的工具。这些工具将帮助您分析和跟踪内核级事件。

```bash
# Install BPF Compiler Collection (BCC)
sudo apt-get install bpfcc-tools
# Install BPFTrace
sudo apt-get install bpfcc-tools
```

## 观测 Pod 网络流量

eBPF 可以对 Pod 之间的网络流量提供深入的洞察。让我们创建一个简单的 eBPF 程序，用于跟踪两个特定 Pod 之间的网络流量。


```c
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>

BPF_TABLE("hash"， u64， u64， packet_count， 256);

int count_packets(struct __sk_buff *skb) {
  u64 *value;
  u64 key = 0;

  struct ethhdr *eth = bpf_hdr_pointer(skb);
  struct iphdr *ip = (struct iphdr *)(eth + 1);

  if (ip->protocol == IPPROTO_TCP) {
    key = ip->saddr;
    value = packet_count.lookup_or_init(&key， &key);
    (*value)++;
  }

  return 0;
}
```

将这段代码保存到一个文件中，例如 packet_count.c。您可以使用 clang 进行编译，并使用 bpftool 将其加载到内核中。

```
clang -O2 -target bpf -c packet_count.c -o packet_count.o
bpftool prog load packet_count.o /sys/fs/bpf/packet_count
```

现在，您可以使用容器 ID 将此 eBPF 程序附加到特定 pod 的网络接口上。

```
# Get the container ID of a pod
kubectl get pods -n <namespace> <pod-name> -o jsonpath=’{.status.containerID}’
# Attach the eBPF program to the container’s network interface
bpftool net attach container <container-id> /sys/fs/bpf/packet_count
```

然后您可以监控为指定 pod 计数的数据包。

## 使用 BPFTrace 进行动态跟踪

BPFTrace 是一个灵活的[动态跟踪](https://opensource.com/article/17/7/dynamic-tracing-linux-user-and-kernel-space)工具。让我们创建一个简单的 BPFTrace 脚本来监控特定 pod 所做的系统调用。

```
tracepoint:syscalls:sys_enter_* {
  if (str(args->comm) == "<pod-name>") {
    printf("%s called %s()\n"， args->comm， probefunc);
  }
}
```

将 `<pod-name>` 替换为您要监控的 pod 的名称。将此脚本保存到一个文件中，例如 syscall_trace.bt，并使用 BPFTrace 运行它。

```
bpftrace syscall_trace.bt
```

该脚本将实时显示指定 pod 所做的系统调用。

## 分析 Kubernetes 资源使用情况

eBPF 也可以帮助您深入了解 Kubernetes pod 和容器的资源使用情况。让我们创建一个 eBPF 程序来跟踪特定 pod 的 CPU 和内存使用情况。

```c
#include <linux/bpf.h>
#include <linux/perf_event.h>
#include <linux/sched.h>
BPF_HASH(pod_cpu, u64, u64);
BPF_HASH(pod_memory, u64, u64);
TRACEPOINT_PROBE(sched, sched_process_exit) {
 u64 pid = bpf_get_current_pid_tgid();
 u64 cpu_usage = bpf_perf_counter_value(pod_cpu, &pid);
 u64 memory_usage = bpf_perf_counter_value(pod_memory, &pid);
 printf(“Pod PID %lld — CPU Usage: %lld ns, Memory Usage: %lld bytes\n”, pid, cpu_usage, memory_usage);
}
```

像之前一样编译这个 eBPF 程序并将其加载到内核中。然后，将其附加到特定 pod 的进程上。

```bash
# Get the PID of a pod’s main process
kubectl exec -it -n <namespace> <pod-name> — pidof <process-name>
# Attach the eBPF program to the pod’s process
bpftool proc attach -p <pid> /sys/fs/bpf/pod_cpu
bpftool proc attach -p <pid> /sys/fs/bpf/pod_memory
```

现在，您可以实时监控指定 pod 的 CPU 和内存使用情况。

## 结论

在 Kubernetes 监控中利用 eBPF 功能可以深入了解内核级事件、网络流量和资源使用情况。通过创建自定义的 eBPF 程序和使用像 BPFTrace 这样的工具，您可以更好地理解集群的行为，排查问题，优化性能并分析资源利用率。

请记住，eBPF 是一个强大但底层的工具，所以要谨慎使用，并且在生产环境中运行自定义的 eBPF 程序时，始终要考虑安全隐患。进一步探索 eBPF 生态系统，发现更多提升 Kubernetes 监控和可观测性实践的方法。
