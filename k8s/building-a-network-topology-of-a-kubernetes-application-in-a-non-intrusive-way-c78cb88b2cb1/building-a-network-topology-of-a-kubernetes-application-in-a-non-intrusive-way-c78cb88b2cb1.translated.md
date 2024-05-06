## Building Network Topology of Kubernetes Applications Non-intrusively

### Introduction

Applications in Kubernetes are logically split into two distinct parts: one is the computational resources (represented by Pods), and the other is the exposure of the application (represented by Services). Application clients can access it via an abstract name, without having to care about which Pods actually handle the request. And since a single Service can have multiple Pods as its backend, it also plays the role of a load balancer. In the default Kubernetes deployment, this load balancing functionality is implemented using either *iptables* or *Linux IPVS* very simply — both work on L4 (e.g. TCP) and perform simple random-based round-robin. Of course, cloud providers can also offer more traditional load balancing solutions to expose applications, but let's start with the simple one.

When we think about possible issues in applications deployed in Kubernetes, there is a class of problems that require understanding which particular instance handled the client request. For example: (1) one of the application Pods is deployed on a host with poor network connectivity, and establishing new connections takes longer than on other Pods, or (2) there is a Pod whose performance degrades over time, while other Pods perform consistently, or (3) there is a particular client request that affects the application performance. Distributed tracing is usually one of the ways to get deep insights into such issues, and obviously, it can track client requests to the backend application. Traditionally, distributed tracing requires some form of instrumentation — it can vary from manual code additions to fully automated injection into the runtime. However, is it possible to achieve the same functionality without touching the client code in any way?

To debug the problems mentioned above, we basically need two features of distributed tracing: (1) collecting metrics related to request latency, and (2) knowing exactly where each request went. The first feature can be easily achieved non-intrusively using various tools powered by eBPF — a technology that allows to dynamically attach probes to kernel functions, e.g. to record which process established a new connection, get socket/connection related metrics, or even check for retransmissions or malicious connection resets. In the [openEuler](https://openeuler.org) ecosystem, such a tool is [gala-gopher](https://gitee.com/openeuler/gala-gopher/), which provides a bunch of different probes, including socket, TCP, and L7/HTTP(s) probes. However, the second feature (knowing where individual requests went) is harder to achieve. In distributed tracing frameworks, it is achieved by injecting span/trace IDs into the application payload, and then correlating observations from both client and backend sides that have the same span ID. Being non-intrusive to the application code means that the same information needs to be injected in a generic way, but injecting it into the application protocol is simply not feasible, as it would require intercepting the outgoing traffic, parsing it, injecting the ID, and then serializing it back and forwarding. It looks like we just reinvented a service mesh!

Before we proceed, let's first understand what data is available for network monitoring. Here we assume that monitoring collects information from all the nodes hosting application Pods, and then this data is collected by, for example, Prometheus. To achieve this, we need some test environment.

### Test Environment

First, we need a multi-node Kubernetes cluster deployed. In Huawei Cloud, the corresponding service is called [Cloud Container Engine (CCE)](https://www.huaweicloud.com/intl/en-us/product/cce.html).

Then we need a test application, and for this purpose, we will use a very simple [Python program](https://gist.github.com/shakhat/059cc629803bbfbbde0975aee64c936b.js) that accepts an HTTP request and is able to make an outgoing HTTP request to the address specified in the original request. This way we can easily chain applications.

Applications will be named with Latin letters A, B, etc. Application A is deployed as deployment A and service A, and so on. The first application is also exposed externally, so it can be called from outside.

Gala-gopher is deployed as a DaemonSet, and it runs on each Kubernetes node. It exposes metrics that are consumed by Prometheus, and ultimately visualized via Grafana. The service topology is built based on the metrics, and visualized via the [NodeGraph](https://grafana.com/docs/plugins/yesoreyeram-infinity-datasource/latest/references/display-options/node-graph/) plugin.

### Observations

Let's send a few requests to application A, and forward them to application B like this:

[root@debug-7d8bdd568c-5jrmf /]# curl http://a.app:8000/b.app:8000
..Hello from pod b-67b75c8557-698tr ip 10.0.0.76 at node 192.168.3.218
Hello from pod a-7954c595f7-tmnx8 ip 10.0.0.148 at node 192.168.3.14
[root@debug-7d8bdd568c-5jrmf /]# curl http://a.app:8000/b.app:8000
**来自 pod b-67b75c8557-mzn6p ip 10.0.0.149 的问候，位于节点 192.168.3.14**

**来自 pod a-7954c595f7-tmnx8 ip 10.0.0.148 的问候，位于节点 192.168.3.14**

在输出中，我们看到对应用程序 B 的其中一个请求发送到了一个 pod，而另一个请求发送到了另一个 pod。这是拓扑在 Grafana 中的显示方式：

顶部和中间行显示某些内容向应用程序 B 的 pod 发送了请求，而底部显示 A 的一个 pod 向服务 B 的虚拟 IP 发送了一个请求。但这看起来根本不像我们预期的那样，对吧？我们只看到三组节点，它们之间没有链接。来自 192.168.3.0/24 子网的 IP 地址是来自集群私有网络（VPC）的节点地址，10.0.0.1/24 是 pod 的地址，但 10.0.0.129 除外，它又是用于节点内通信的节点地址。

现在，这些指标是在套接字级别收集的，这意味着它们正是应用程序进程可以看到的内容。收集是通过 eBPF 探针完成的，因此第一个想法是检查操作系统内核是否比套接字中可用的信息更了解应用程序连接。该集群配置了默认 CNI，Kubernetes 服务作为 iptables 规则实现。iptables-save 的输出显示了配置。最有趣的是这些实际配置负载均衡的规则：

```
-A KUBE-SERVICES -d 10.247.204.240/32 -p tcp -m comment
--comment "app/b:http-port cluster IP" -m tcp --dport 8000 -j KUBE-SVC-CELO6J2CXNI7KVVA
-A KUBE-SVC-CELO6J2CXNI7KVVA -d 10.247.204.240/32 -p tcp -m comment
--comment "app/b:http-port cluster IP" -m tcp --dport 8000 -j KUBE-MARK-MASQ
-A KUBE-SVC-CELO6J2CXNI7KVVA -m comment --comment "app/b:http-port -> 10.0.0.155:8000"
-m statistic --mode random --probability 0.50000000000 -j KUBE-SEP-VFBYZLZKPEFJ3QIZ
-A KUBE-SVC-CELO6J2CXNI7KVVA -m comment --comment "app/b:http-port -> 10.0.0.76:8000"
-j KUBE-SEP-SXF6FD423VYX6VFB
```

负载均衡在客户端所在的同一节点上完成。因此，如果我们将 pod 映射到节点，则如下所示：

内部 iptables（实际上
[nftables](https://wiki.nftables.org/wiki-nftables/index.php/What_is_nftables%3F)）使用 conntrack 模块来理解数据包属于同一连接，并且应该以类似的方式进行处理。Conntrack 还负责地址转换，因此具有客户端应用程序的节点应该知道将数据包发送到何处。让我们使用 conntrack CLI 工具检查一下。

```
# node-1
# conntrack -L | grep 8000
tcp 6 82 TIME_WAIT src=10.0.0.164 dst=10.247.204.240 sport=51030 dport=8000 src=10.0.0.76 dst=192.168.3.14 sport=8000 dport=19554 [ASSURED] use=1
tcp 6 79 TIME_WAIT src=10.0.0.164 dst=10.247.204.240 sport=51014 dport=8000 src=10.0.0.155 dst=10.0.0.129 sport=8000 dport=56734 [ASSURED] use=1
# node-2
# conntrack -L | grep 8000
tcp 6 249 CLOSE_WAIT src=10.0.0.76 dst=192.168.3.14 sport=8000 dport=19554 [UNREPLIED] src=192.168.3.14 dst=10.0.0.76 sport=19554 dport=8000 use=1
```

好的，我们看到在第一个节点上，地址已从应用程序 A 的 pod 转换，并获得了具有某个随机端口的节点地址。在第二个节点上，连接信息被反转，因为其自身数据包实际上是回复，但考虑到这一点，我们看到请求来自第一个节点和相同的随机端口。

*请注意，Node-1 上有两个请求，因为我们发送了 2 个请求，并且它们由不同的 pod 处理：同一节点上的 pod-b-1 和另一个节点上的 pod-b-2。*

这里的好消息是，*有可能*在客户端节点上了解实际的请求接收者，但对于服务器端，它需要与客户端节点上收集的信息进行*关联*。像这样：

当客户端和服务器 pod 都在同一节点上时，关联变得更加简单，但仍然有一些关于哪些地址是真实的以及哪些应该被忽略的假设：

在这里，操作系统可以全面了解 NAT，并可以在真实源和真实目标之间提供映射。*有可能*从 10.0.0.164 重建到 10.0.0.155 的完整流。

为了总结本节，应该可以扩展现有的 eBPF 探针以包括来自 conntrack 模块有关地址转换的信息。客户端可以知道请求的去向。但服务器并不总是能够知道客户端是谁，*直接没有集中关联*算法。相比之下，分布式跟踪方法为客户端和服务器提供了有关对等方的信息，**直接且立即**来自通信数据。因此，FlowTracer 来了！**FlowTracer**

这个想法很简单——直接在连接中传输对等方之间的数据。这不是第一次需要这样的功能，例如，HTTP 负载均衡器插入 X-Forwarded-For HTTP 头，让后端服务器知道客户端。这里的限制是我们希望停留在 L4，从而支持任何应用程序级协议。这样的功能也存在，一些 L4 负载均衡器（例如

算法将以 BPF 编写。它开辟了机会，允许在测试/发布新的拥塞控制思想时缩短生产环境的周转时间。

同样的灵活性可以扩展到编写 TCP 头部选项。人们希望测试新的 TCP 头部选项以提高 TCP 性能的情况并不少见。另一个用例是对于具有更多受控环境和在仅针对内部流量放置头部选项方面具有更多灵活性的数据中心。

而圣杯是这些函数：

- [bpf_store_hdr_opt](https://ebpf-docs.dylanreimerink.nl/linux/helper-function/bpf_store_hdr_opt/)
- [bpf_load_hdr_opt](https://ebpf-docs.dylanreimerink.nl/linux/helper-function/bpf_load_hdr_opt/)

两者都属于一种特殊的 [sock ops](https://ebpf-docs.dylanreimerink.nl/linux/program-type/BPF_PROG_TYPE_SOCK_OPS/) 程序，两者自内核 5.10 起可用，这意味着几乎任何 2022 年之后的版本。sock ops 程序是附加到 cgroup v2 的单个函数，它允许仅针对某些套接字（例如属于特定容器）启用它。该程序接收单个操作，该操作用于指示套接字的当前状态。当我们想要编写新的头部选项时，我们首先需要为主动或被动连接启用写入，然后我们需要告知新的头部长度，然后才能写入头部负载。读取更简单，但我们也需要首先启用读取功能，然后才能读取头部选项。

当创建 TCP 数据包时，将调用 TCP 头部回调。这发生在 *地址转换之前*，因此我们可以将套接字源地址复制到头部选项中。读者可以轻松地从头部选项中提取值并存储在 BPF 映射中，以便稍后使用者可以读取并从观察到的远程地址映射到实际地址。第一个运行代码的 BPF 部分远少于 100 行。相当令人印象深刻！

## 使代码适合生产

不过，魔鬼藏在细节中。首先，我们需要一种从 BPF 映射中删除旧记录的方法。执行此操作的最佳时机是 conntrack 模块从其表中删除连接时。

Arthur Chiao 的这篇 [文章](http://arthurchiao.art/blog/conntrack-design-and-implementation/) 很好地描述了 conntrack 模块和连接生命周期的内部结构，因此很容易在内核源中找到正确的函数 — *nf_conntrack_destroy*。此函数在从内部表中删除 conntrack 条目之前接收该条目。由于这是连接正式结束的时间，因此我们还可以添加一个探针，该探针也将从我们的映射表中删除连接。

在 sock ops 程序中，我们没有指定将新的头部选项注入到哪些数据包中，假设它适用于所有数据包。事实上也确实如此，但只有在连接处于已建立/已确认状态时，读取才有效，这意味着服务器端无法从传入的 SYN 数据包中读取头部选项。SYN-ACK 也在常规 TCP 栈之前处理，并且既不能注入头部选项，也不能读取它们。实际上，该功能仅在连接完全使用第一个 PSH（数据包）运行时才在两端起作用。对于工作连接来说，这完全没问题，但如果连接尝试失败，则客户端不知道它 *尝试* 连接到哪里。这是一个至关重要的失误；此信息对于调试网络故障很有用。正如我们所了解的，Kubernetes 负载平衡是在客户端节点上实现的，因此我们可以从 conntrack 中提取信息，并以与通过流接收的数据相同的格式存储它。Conntrack 函数 *__nf_conntrack_confirm* 在这里提供帮助 — 它在新的连接即将确认时被调用，对于主动客户端（传出）TCP 连接，这发生在发送第一个 SYN 数据包时。

有了所有这些补充，代码变得有点臃肿，但总共仍然远少于 1000 行。完整补丁可在 [此 MR](https://gitee.com/openeuler/gala-gopher/pulls/778) 中获得。是时候在我们的实验设置中启用它并再次检查指标和拓扑了！

瞧：