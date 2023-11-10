<!-- 
# Kubernetes的安全性不能仅仅依赖于eBPF
https://cdn.thenewstack.io/media/2023/11/db2978cb-growtika-gsieeohcntq-unsplash-e1699539849298-1024x576.jpg
 -->
 
不建议在没有适当的服务提供商和第三方工具的情况下使用eBPF。

译自 [Don’t Rely on eBPF Alone for Kubernetes](https://thenewstack.io/dont-rely-on-ebpf-alone-for-kubernetes/) 。

[eBPF](https://thenewstack.io/linux-technology-for-the-new-year-ebpf/)在安全性、监控、可观测性等方面广为关注。的确，通过扩展钩子来实现安全性和可观测性的功能，这无疑使eBPF成为Kubernetes最好的基石选择(详见下文)。特别是结合使用CNI或单一API时尤其如此。

但是，正如一辆F1赛车需要丰富的驾驶技巧和适当的工具来备战一样，在没有适当的服务提供商和第三方工具支撑的情况下使用eBPF并不可取。换言之，在您可能会融入基础设施的生产环境中，单独依靠eBPF是不明智的。

事实上，根据[Gartner](https://www.gartner.com/en/documents/4597499)的说法，大多数企业都缺乏构建和集成基于eBPF功能所需的专业知识和技能。然而，Gartner也建议组织: “当规模、性能、可见性和安全至关重要时，谨慎评估基于eBPF的Kubernetes CNI(容器网络接口)解决方案。” 

[ARMO](https://thenewstack.io/armo-misconfiguration-is-number-1-kubernetes-security-risk/)公司CTO兼联合创始人[Benyamin Hirschberg](https://il.linkedin.com/in/ben-hirschberg-66141890)评论道: “Gartner在这一点上是正确的。” 实践中，Kubernetes集群中的基于eBPF的分组路由要比标准的Linux分组路由更有效，后者在Kubernetes和容器化环境下非常复杂。例如，[Cilium](https://thenewstack.io/cilium-cncf-graduation-could-mean-better-observability-security-with-ebpf/)通过eBPF添加了Kubernetes CNI特定的分组路由逻辑，跳过了部分路由层从而提高了效率，Hirschberg说。

[Isovalent](https://isovalent.com/)，也就是[创造Cilium的公司](https://thenewstack.io/ebpf-tools-an-overview-of-falco-inspektor-gadget-hubble-and-cilium/)，CTO兼联合创始人[Thomas Graf](https://www.linkedin.com/in/thomas-graf-73104547/?originalSubdomain=ch)说: “eBPF不是面向终端用户的技术，它也不是被设计来直接面向终端用户。它的接口是针对内核开发者设计的。” “尽管它在一定程度上降低了入门门槛，相比直接编写内核源代码，它能验证程序从而变得更安全，但该技术仍主要服务于内核开发者和高端系统工程师。eBPF就像一个Android SDK: 它赋予了在广泛设备上开发和运行沙盒应用的能力，但大多数终端用户即使在技术上可以做到，也不会开发自己的应用。”

## 现有的eBPF安全解决方案

eBPF的核心功能是能够在内核中运行并扩展到各种堆栈，包括Kubernetes节点和集群中的运行时环境，都在封闭或沙箱环境中。eBPF在高度分布式的Kubernetes环境中的可扩展性，使其非常适合云原生安全工具和平台。但要合理利用eBPF进行安全防护(以及监控和可观测性)，就需要适当的工具和平台。换句话说，在实验室中测试eBPF功能可能很有趣，但强烈建议不要依赖自己开发的或未经测试的工具来保障组织安全。 

然而，正如Kubernetes一样，eBPF是一个基础性的技术层面，企业管理联盟分析师Torsten Volk说。eBPF通过在Linux内核级操作，具有保障快速变化的分布式环境安全的潜力。“但权力越大，责任越大，这意味着如果你自主开发eBPF平台并犯了配置错误，或者没有及时响应新发现的安全漏洞，那么你可能已经允许恶意行为者不仅入侵一个虚拟机，而是所有分布式应用集群。或者也许是你自己的开发人员无意中通过eBPF运行了新的代码，导致Kubernetes集群速度大幅下降。” Volk说，“因此，我建议使用现有的、经过良好维护和支持的基于eBPF的工具，而不是采用自主开发的方法。”

## 谨慎选择

存在许多eBPF安全工具。其中许多甚至大多数可能会以过多的“假阳性”或对漏洞严重性缺乏足够指导，压垮安全和DevOps团队。Torsten Volk说，这可能发生在依赖像[Nginx](https://www.nginx.com/?utm_content=inline-mention)、Elasticsearch、[Kafka](https://thenewstack.io/apache-kafka-primer/)等云原生资源的许多公共镜像时。

Volk说，存在大量商业Kubernetes安全态势管理工具，包括谷歌的GKE安全态势控制板，以及Tigera的跨集群跨云容器联网平台。然而，他说市场上仍有空间容纳一个将安全性直接嵌入Kubernetes集群API的开源项目。

虽然某些工具的扫描器肯定能识别出大多数已知漏洞，但如果CVR文件中有成百上千条警报，那么这些信息就不太有价值，因为镜像中的漏洞不意味着它能被利用。

在本周芝加哥举行的[KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)上，ARMO公司的Hirschberg在演讲中描述了容器镜像是Kubernetes安装中许多漏洞的来源，但严重程度不同。他分享了ARMO的研究结果，显示大量漏洞实际上没有被加载到内存中，因此不会对环境立即造成风险。然后他描述了开源KubeScape提供的不同评分系统，这些系统从严重性和威胁级别对漏洞进行了特征化。这使安全团队能首先解决那些对环境构成直接威胁的漏洞，并降低对那些更为良性的通常是“假阳性”漏洞的优先级，否则这些漏洞会成为耗费资源的干扰。Hirschberg解释ARMO的可达性功能如何提供与[利用预测评分系统(EPSS)](https://www.first.org/epss/)一致的结果。他还展示ARMO如何利用eBPF的“可达性”功能，以便用户可以根据漏洞构成的威胁程度对其进行优先级排序，从而让他们能够优先修复最紧迫的漏洞。

在演讲中，Hirschberg展示了如何自动对漏洞进行优先级排序，这样你可能只需要立即修复几十个漏洞，而不是在成千上万个漏洞中不知该先修复哪些。他说，可达性是“描述漏洞影响和打分的一种方式，这样你就知道该采取什么行动了。”

的确，Graf说，eBPF应该能改善“噪音与信号”的问题。“安全工具在无噪音环境下表现良好，但真实世界充满了导致假阳性的微妙差异。eBPF在提供安全可观察性方面具有非凡的能力，提供了几年前还难以想象的丰富上下文，” Graf说，“虽然这不能神奇消除假阳性，但它通过更多上下文改善了信号质量，随着我们利用额外上下文提高模式准确性，信噪比也会提高。”

减少安全噪音和假阳性是eBPF最初用于性能基准测试和故障排除(如bcc和[bpftrace](https://thenewstack.io/ebpf-tools-an-overview-of-falco-inspektor-gadget-hubble-and-cilium/))的自然效益，Graf说。他说，使用这些工具面临类似需要更多上下文来准确定位性能瓶颈的挑战。

使用eBPF的合适平台应该能让DevOps团队监控Kubernetes集群中应运行的内容，并在违反策略或检测到安全威胁时提供可操作的结果。

Hirschberg说，许多缺点阻碍了扫描程序在Kubernetes安全中应用。他说: “它们包含几乎无穷无尽的错误配置和漏洞，导致警报疲劳，因为此类工具可能产生大量假阳性。”

但是，通过应用eBPF提供的运行时洞察，然后将该上下文反馈到扫描程序，可以提高安全扫描结果的优先级准确性，Hirschberg说。有了它，DevOps团队就能知道需要修复什么来积极影响安全态势。Hirschberg说: “此外，风险验收更多地基于事实，而不是直觉。” “这本身就培养了DevOps团队和安全团队之间更好的合作文化。”

eBPF在Kubernetes安全方面的发展也体现在工具和平台与云原生需求的更好匹配上。Graf说: “Kubernetes和云原生市场进化非常迅速，最初开发的工具主要面向早期用户‘构建、定制和结束’，不太适合新的‘安装和使用’的市场现实。这还是早期，有许多Kubernetes发行版、安装程序和大量重叠的项目，非常让我想起了无数个Linux发行版的日子，每个人都在编译自己的Linux内核。” “我们已经转向一个希望消费开源解决方案而不仅仅是开源代码的社区。eBPF并不能神奇地解决这个问题——它提供了构建解决方案的惊人功能，但这取决于云原生供应商和社区将技术及其潜力发展成成熟的解决方案。”
