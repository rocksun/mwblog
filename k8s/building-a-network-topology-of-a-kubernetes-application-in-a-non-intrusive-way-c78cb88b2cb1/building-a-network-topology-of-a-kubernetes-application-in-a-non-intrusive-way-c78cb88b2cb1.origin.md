# Building a network topology of a Kubernetes application in a non-intrusive way
# Intro
An application in Kubernetes is logically split into two distinct parts: one is a computational resource (represented by pods) and the other exposes access to the application (represented by services). Application clients can access it by an abstract name without taking care of what pods actually handle requests. And since a single service may have multiple pods as a backend, it also plays a role of a load-balancer. In the default Kubernetes deployments this load-balancing feature is implemented pretty simple using
*iptables* or *Linux IPVS* — both work at L4 (e.g. TCP) and do a naïve random-based round-robin. Of course, cloud providers may also offer a more traditional load-balancing solutions to expose applications, but let’s start simple.
When we think about issues that can occur in applications deployed in Kubernetes, there is one group that requires a knowledge of a specific instance that handles a client request. For example: (1) one of application pods is deployed at a host which has worse network connectivity and establishing of a new connection takes longer than for others, or (2) there is a pod which performance degrades over the time while of others stays constant or (3) there is a specific client which requests affect application performance. Distributed tracing is usually one of approaches to get insights into such issues and, obviously, to trace client requests to the backend application. Traditionally, the distributed tracing requires some sort of instrumentation — it can vary from manual code additions to a fully automatic injection into runtime. But can the same be achieved without any manipulations with client code at all?
To debug the mentioned issues we basically need two features of a distributed tracing: (1) to collect metrics related to request latency and (2) to know exactly where every single request goes. The first feature can easily be implemented in a non-intrusive way by using one of large variety of tools powered by eBPF — a technology that allows to dynamically attach probes to kernel functions and, for example, to record which process establishes a new connection, get socket/connection related metrics, even check if there were retransmissions or evil connection resets. In
[openEuler](https://openeuler.org) ecosystem such tool is [gala-gopher](https://gitee.com/openeuler/gala-gopher/) which offers a large collection of different probes, including socket, TCP and L7/HTTP(s) probes. However the second feature (knowing where a single request goes) is much harder to achieve. In distributed tracing frameworks it is implemented by injecting a span/trace id into application payload and then correlating observations with the same span id from both client and backend sides. Being a non-intrusive to application code would mean that the same information needs to be injected a generic way, but doing this into application protocols is not feasible at all as it would require to intercept outgoing traffic, parse it, inject id, serialize it back and forward. Looks like we just re-invented a service mesh!
Before going further let’s first take a look at the data available from network monitoring. Here we assume that monitoring gets information from all nodes that host application pods and this data is then collected by e.g. Prometheus. In order to achieve this, we need some experiment environment.
# Experiment environment
First of all, we need a deployed multi-node Kubernetes cluster. In Huawei Cloud the corresponding service is called
[Cloud Container Engine (CCE)](https://www.huaweicloud.com/intl/en-us/product/cce.html).
Then we need a test application, for that purposes we will use a very simple
[Python program](https://gist.github.com/shakhat/059cc629803bbfbbde0975aee64c936b.js) that accepts an HTTP request with ability to make outgoing HTTP requests to the address specified in the original request. That way we can chain applications easily.
The applications will be called by Latin letters, A, B, etc. Application A is deployed as Deployment A and Service A, and so on. The very first application is also exposed externally, so it can be called from the outside.
Gala-gopher is deployed as a daemon set and runs on every Kubernetes node. It exposes metrics that are consumed by Prometheus and finally visualized with Grafana. Service topology is constructed based on metrics and visualized by
[NodeGraph](https://grafana.com/docs/plugins/yesoreyeram-infinity-datasource/latest/references/display-options/node-graph/) plugin.
# Observations
Let’s send a few requests to the application A with forwarding to the application B like this:
[root@debug-7d8bdd568c-5jrmf /]# curl http://a.app:8000/b.app:8000
..Hello from pod b-67b75c8557-698tr ip 10.0.0.76 at node 192.168.3.218
Hello from pod a-7954c595f7-tmnx8 ip 10.0.0.148 at node 192.168.3.14
[root@debug-7d8bdd568c-5jrmf /]# curl http://a.app:8000/b.app:8000
..Hello from pod b-67b75c8557-mzn6p ip 10.0.0.149 at node 192.168.3.14
Hello from pod a-7954c595f7-tmnx8 ip 10.0.0.148 at node 192.168.3.14
In the output we see that one of requests to the application B went to one pod and the other to the different. This is how the topology look in Grafana:
The top and the middle rows show that something sent requests to pods of application B and the bottom part shows that a pod of A sent a request to a virtual IP of a service B. But this doesn’t look like what we expected at all, right? We only see three groups of nodes and they don’t link to each other. IP addresses from 192.168.3.0/24 subnet are node addresses from cluster private network (VPC), 10.0.0.1/24 are addresses of pods except 10.0.0.129 which is again a node address for intra-node communications.
Now these metrics are collected at socket level, meaning that they are exactly what application processes can see. The collection is done by eBPF probes, so the first idea would be to check if OS kernel knows a bit more about application connections than is available in the sockets. The cluster is configured with the default CNI and Kubernetes services are implemented as iptables rules. Output of iptables-save reveals the configuration. Most interesting are these lines that actually configure load balancing:
-A KUBE-SERVICES -d 10.247.204.240/32 -p tcp -m comment
--comment "app/b:http-port cluster IP" -m tcp --dport 8000 -j KUBE-SVC-CELO6J2CXNI7KVVA
-A KUBE-SVC-CELO6J2CXNI7KVVA -d 10.247.204.240/32 -p tcp -m comment
--comment "app/b:http-port cluster IP" -m tcp --dport 8000 -j KUBE-MARK-MASQ
-A KUBE-SVC-CELO6J2CXNI7KVVA -m comment --comment "app/b:http-port -> 10.0.0.155:8000"
-m statistic --mode random --probability 0.50000000000 -j KUBE-SEP-VFBYZLZKPEFJ3QIZ
-A KUBE-SVC-CELO6J2CXNI7KVVA -m comment --comment "app/b:http-port -> 10.0.0.76:8000"
-j KUBE-SEP-SXF6FD423VYX6VFB
Load balancing is done on the same node where the client is. So if we map pods to nodes this looks like this:
Internally iptables (actually
[nftables](https://wiki.nftables.org/wiki-nftables/index.php/What_is_nftables%3F)) use conntrack module to understand that packets belong to the same connection and should be processed similar. Conntrack is also responsible for address translation, so the node with the client application should know where to send packets to. Let’s check this with conntrack CLI tool.
# node-1
# conntrack -L | grep 8000
tcp 6 82 TIME_WAIT src=10.0.0.164 dst=10.247.204.240 sport=51030 dport=8000 src=10.0.0.76 dst=192.168.3.14 sport=8000 dport=19554 [ASSURED] use=1
tcp 6 79 TIME_WAIT src=10.0.0.164 dst=10.247.204.240 sport=51014 dport=8000 src=10.0.0.155 dst=10.0.0.129 sport=8000 dport=56734 [ASSURED] use=1
# node-2
# conntrack -L | grep 8000
tcp 6 249 CLOSE_WAIT src=10.0.0.76 dst=192.168.3.14 sport=8000 dport=19554 [UNREPLIED] src=192.168.3.14 dst=10.0.0.76 sport=19554 dport=8000 use=1
Ok, we see that on the first node the address was translated from pod of application A and got address of node with some random port. At the second node the connection information is reversed because its own packets are actually a reply, but taking this into account we see that the request came from the first node and the same random port.
*Note that there are 2 requests at Node-1 because we sent 2 requests and they were handled by different pods: pod-b-1 at the same node and pod-b-2 at the other.*
Good news here is that it is
*possible* to know the actual request recipient right at the client node, but for a server side it requires *correlation* with the information collected at the client node. Like this:
When both client and server pods are at the same node the correlation becomes even more simple, but still with some assumptions regarding which addresses are true and which should be ignored:
Here OS has full view on NAT and can provide mapping between the real source and the real destination. It is
*possible* to reconstruct a full flow from 10.0.0.164 to 10.0.0.155.
To conclude this section, it should be possible to extend existing eBPF probe to include information from conntrack module about address translation. It is possible for a client to know where the request goes. But it is not always possible for a server to know who was the client
*directly without a centralized correlation* algorithm. To contrast, the distributed tracing approach gives both client and server information about peer **directly and immediately** from the communication data. So comes the FlowTracer! **The FlowTracer**
The idea is simple — to transfer data between peers right in the connection. It is not the first time such feature is needed, for example, HTTP load balancers insert X-Forwarded-For HTTP header to let back-end server know the client. The restriction here is that we want to stay at L4 and thus support any application level protocol. Such feature exists too and some L4 load balancers (e.g.
[this](https://www.tencentcloud.com/document/product/608/14429)) can inject original address as TCP header option and make it available to the server.
To sum up the requirements:
- Transfer peer address at L4.
- Be able to enable address injection dynamically (as easy as to deploy app in K8s).
- Non-intrusive and fast.
The most straight-forward approach seems to use a TCP header option (also known as TOA). The payload is IP address and port number (since they change during address translation). We can restrict to support IPv4 only since Huawei Kubernetes deployment supports only it. IPv4 address is 32 bits, plus we need 16 bits for a port number, in total this gives 6 bytes plus 1 byte for option kind and one more byte for option length. Here’s how a TCP header looks in
[spec](https://en.wikipedia.org/wiki/Transmission_Control_Protocol):
The header may contain multiple options of up to 40 bytes in total. Each option can have variable length and a type / kind.
Normally Linux TCP packets already have some options like MSS or Timestamp. But there’s still a room of approximately 20 bytes that can be used for our purposes.
Now when we know where to put the data the next question is where should the code be added? We want the solution to be as much generic as possible and work for any TCP connection. The ideal place is somewhere in the kernel in the network stack operating over a so-called socket buffer — a structure that represents network connection information — available from the top level down to the packets ready to be transferred over the network. From the implementation point-of-view the code should be an eBPF code (of course!), then address injection feature can be dynamically enabled.
The most obvious place for such code is TC, a traffic control module. There an eBPF program has access to already created packets, it can read and write data from packets. One of
*disadvantages* is the need to parse packet from scratch, i.e. even [ function provides a pointer to the beginning of L3 header, but the location of L4 still needs to be calculated manually. The most problematic though is inserting operation. There are 2 functions with promising names bpf_skb_load_bytes_relative](https://ebpf-docs.dylanreimerink.nl/linux/helper-function/bpf_skb_load_bytes_relative/) [bpf_skb_adjust_room](https://ebpf-docs.dylanreimerink.nl/linux/helper-function/bpf_skb_adjust_room/)and [bpf_skb_change_tail](https://ebpf-docs.dylanreimerink.nl/linux/helper-function/bpf_skb_change_tail/), but they allow to resize at most L3 packet and not L4. An alternative solution would be to check if existing TCP header contains some options and overwrite them, but let’s first check what an usual packet contains.
1514772378.301862 IP (tos 0x0, ttl 64, id 20960, offset 0, flags [DF], proto TCP (6), length 60)
192.168.3.14.28301 > 10.0.0.76.8000: Flags [S], cksum 0xbc03 (correct), seq 1849406961, win 64240, options [mss 1460,sackOK,TS val 142477455 ecr 0,nop,wscale 9], length 0
0x0000: 0000 0001 0006 fa16 3e22 3096 0000 0800 ........>"0.....
0x0010: 4500 003c 51e0 4000 4006 1ada c0a8 030e E..<Q.@.@.......
0x0020: 0a00 004c 6e8d 1f40 6e3b b5f1 0000 0000 ...Ln..@n;......
0x0030: a002 faf0 bc03 0000 0204 05b4 0402 080a ................
0x0040: 087e 088f 0000 0000 0103 0309 .~..........
This is a TCP SYN packet sent when the client establishes connection with the back-end application. The header contains multiple options: MSS used to specify maximum segment size, then selective acknowledgement, a Timestamp used in particular to ensure order of packets, a no-operation NOP probably used for word alignment and finally window scale used to tune window size. From this list the Timestamp option is the best candidate to be overwritten (the adoption is still ~40% according to Wikipedia) and that is what DeepFlow — one of leaders of non-intrusive eBPF tracing — does in their
[platform](https://zhuanlan.zhihu.com/p/641197123).
While this approach seems to be working it is still not a trivial to implement. TC program has access to an already translated address, meaning that the translation mapping should be somehow retrieved from conntrack module and stored. TC program is attached to network cards, so if a node has multiple of them then the deployment needs to correctly identify where to attach. The reading module will have to parse all packets in order to find TCP and then to iterate over headers to find where our header is. Is there another way?
While googling this question in August 2023, it was quite often to get to the bottom of a search result page telling no more results (hope this will change with this blog post!) The most useful reference was a link to a patch into Linux Kernel made by Facebook engineers back in 2020. This
[patch](https://lore.kernel.org/netdev/20200626175501.1459961-1-kafai@fb.com/) reveals what we were searching for:
The earlier effort in BPF-TCP-CC allows the TCP Congestion Control
algorithm to be written in BPF. It opens up opportunities to allow
a faster turnaround time in testing/releasing new congestion control
ideas to production environment.
The same flexibility can be extended to writing TCP header option.
It is not uncommon that people want to test new TCP header option
to improve the TCP performance. Another use case is for data-center
that has a more controlled environment and has more flexibility in
putting header options for internal traffic only.
And the grail are these functions:
[ and bpf_store_hdr_opt](https://ebpf-docs.dylanreimerink.nl/linux/helper-function/bpf_store_hdr_opt/) [bpf_load_hdr_opt](https://ebpf-docs.dylanreimerink.nl/linux/helper-function/bpf_load_hdr_opt/)! Both belong to a special type of [sock ops](https://ebpf-docs.dylanreimerink.nl/linux/program-type/BPF_PROG_TYPE_SOCK_OPS/)programs, both are available since kernel 5.10 meaning almost any distro after the year 2022. A sock ops program is a single function attached to cgroup v2, which allows to enable it only for some sockets (e.g. belonging to a specific container). The program receives a single operation, which is used to indicate current state of a socket. When we want to write a new header option we first need to enable writing for active or passive connections, then we need to tell the length of a new header and only then to write header payload. Reading is simpler, but too, we need to enable reading feature first and then to read the header option. TCP header callbacks are called when TCP packet is created. This happens *before address translation*, so we can just copy socket source address into a header option. The reader can easily extract value from a header option and store in BPF map so later the consumer can read and map from the observed remote address to the real one. The BPF part of the first running code is well under 100 lines. Quite impressive!
## Making the code production-ready
The evil is in details though. First of all, we need a way to delete old records from BPF map. The best time to do this is when conntrack module removes connection from its table. This
[post](http://arthurchiao.art/blog/conntrack-design-and-implementation/) from Arthur Chiao describes very well the internals of conntrack module and connection life cycle, so it is easy to find the right function in kernel sources — *nf_conntrack_destroy*. This function receives a conntrack entry right before it is removed from the internal table. And since this is the time when a connection officially ended we can also add a probe that will remove the connection from our mapping table too.
In sock ops program we do not specify into which packets to inject a new header option assuming it to work for all packets. And in fact it is, but reading works only when a connection is in established/confirmed state, meaning that a server side cannot read header option from an incoming SYN packet. SYN-ACKs are also handled before a regular TCP stack and it is not possible neither to inject header options, nor to read them. Effectively the feature works on both ends only when a connection fully operational with the first PSH (data packet). This is absolutely fine for working connections, but if connection attempt fails, then the client doesn’t know where it
*tried* to connect. This is quite a crucial miss; this information would be useful to debug network failures. As we learned, the Kubernetes load balancing is implemented at a client node, so we can extract information from conntrack and store it in the same format as data received through a flow. Conntrack function *__nf_conntrack_confirm* is here to help — it is called when a new connection is about to be confirmed, for active client (outgoing) TCP connections this happens right with the first sent SYN packet.
With all these additions the code becomes a bit fatter, but still well under 1000 lines in total. Full patch is available in
[this MR](https://gitee.com/openeuler/gala-gopher/pulls/778). Time to enable it in our experimental setup and check metrics and topology again!
Et voilà: