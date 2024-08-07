# 绕过 eBPF 来保护 Kubernetes 应用中的运行时

![绕过 eBPF 来保护 Kubernetes 应用中的运行时](https://cdn.thenewstack.io/media/2024/08/54c24441-bypassing-ebpf-to-protect-runtimes-in-kubernetes-apps-2-1024x576.jpg)

西雅图 - Kubernetes 非常适合运行生成式 AI 应用所需的规模。但 GenAI 带来了一种安全问题，需要新的方法来[保护 Kubernetes 应用中的运行时](https://thenewstack.io/the-top-5-kubernetes-security-mistakes-youre-probably-making/)。

如果说有什么不同的话，[CloudNativeSecurityCon](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america) 在今年夏天早些时候展示了随着 GenAI 的出现，新的攻击向量如何使问题变得更加复杂。

Operant 提出了一种解决该问题的新方法，Operant 是一家运行时应用平台提供商，由来自 Apple、Arm、[Google](https://cloud.google.com/?utm_content=inline+mention)、Juniper、Transposit 和 [VMware](https://tanzu.vmware.com?utm_content=inline+mention) 的资深团队共同创立。

[Operant](https://www.operant.ai/) 在应用的每一层都保护 Kubernetes 应用的运行时。Operant 的联合创始人兼 CMO [Ashley Roof](https://www.linkedin.com/in/ashleyroof/) 表示，它为服务和 API 强制执行安全策略，包括 Kubernetes 集群中的所有内容。

Roof 表示，客户安装 Operant 后，就可以看到其 Kubernetes 应用在所有网络层上的蓝图。Operant 的方法与云原生安全领域的一些趋势背道而驰，特别是关于扩展伯克利数据包过滤器或 [eBPF](https://thenewstack.io/what-is-ebpf/)，这是一种 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 技术。

“我们确实有一个 eBPF 组件来处理进程级的东西，但我们所做的大部分工作与它无关，”Roof 说。“因此，这使我们能够减少很多噪音，并获得独特的运行时洞察，然后我们能够对其进行优先排序，并让人们对关键性有强烈的认识。”

Operant 首席执行官 [Vrajesh Bhavsar](https://www.linkedin.com/in/vrajeshio/) 表示，他的公司希望支持想要使用 eBPF 的用户。但他认为，与从 [eBPF 对 Linux 内核的可观察性](https://thenewstack.io/ebpf-meaner-hooks-more-webassembly-and-observability-due/) 中过滤数据洪流相比，还有更好的方法。

他说，eBPF 是一项强大的技术，许多供应商试图以多种不同的方式将其产品化。Operant 构建了一个不依赖于 eBPF 的解决方案，该公司认为这使得其解决方案具有更好的可扩展性，避免了与 eBPF 相关的固有风险，并允许更好的上下文性。

## 数据太多，“噪音”太多

Bhavsar 表示，eBPF 不可扩展，因为数据太多。这就像打开泄洪闸；eBPF 运行来自内核的所有系统数据。

“想想所有短暂的服务，它们只运行几分钟然后消失，”Bhavsar 说。“当您有很多信号来自 eBPF 传感器时，您就会严重依赖于该层发生的事情，而没有了解整个 Kubernetes 堆栈中所有其他层发生的事情。尤其是在 Kubernetes 中，这是一个特别困难且重要的难题。”

他说，对于 Kubernetes，您需要考虑的不仅仅是进程级活动。您还需要查看其他 Pod、容器和服务的行为。它们如何在不同的网络之间通信？入口和出口呢？API 如何在内部和外部相互通信？

“这就是我们推向市场的方法，团队不必筛选来自 eBPF 的噪音，”Bhavsar 说。

但是其他所有层呢？如何在如此庞大的数据堆栈中找到针？

Bhavsar 说，将数据洪流发送到某个地方进行分析没有意义。如何理解系统在操作系统和内核级别发生的事情？如何理解所有其他层发生的事情？

他说，许多现有的 eBPF 解决方案都需要编写过滤器。但这不是 Operant 的方法：“我是一名内核工程师。我不想编写内核级过滤器，也不想让客户编写这些过滤器。”

Bhavsar 在 Apple 工作，负责 iOS 和 macOS，构建数据保护系统、动态跟踪和公司的安全 enclave 技术。他的背景使他能够将安全性和机器学习结合起来，并认识到为什么生成式 AI 会带来如此巨大的风险，需要一种侧重于运行时行为的上下文方法。
各种商业大型语言模型都可以在像[Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/)这样的网站上找到。所有这些模型都以容器的形式交付。这些容器连接到 API 和服务。容器可移植性和生成式 AI 的结合是一种强大的组合，可能导致数据泄露。采用 AI 的公司现在必须重新思考其整个安全计划。这不仅仅是代码扫描、身份管理或配置正确。

Bhavsar 说，这更多地是关于运行时发生了什么。应用程序在做什么？

“这些容器在相互通信时在做什么？” Bhavsar 说。“所有这些不同系统之间移动的数据有效负载是什么？在我的环境之外，通过这些 AI API 发生了什么？以及这些新型风险和攻击在哪里？

## 随着世界采用 Kubernetes
每个人都在向 Kubernetes 迁移，尤其是在 GenAI 方面，并采用模型和参考。

“我们希望世界做好准备来保护这些环境，”Bhavsar 说。但他补充说，“网络应用程序防火墙或 API 网关不再足够了。”

所有这些应用程序都有深层的根源和依赖关系，这些依赖关系绕过外围，访问个人私密信息，例如信用卡数据。

Bhavsar 说，这就像一个全新的黑洞，你无法手动管理它。存在太多动态性和短暂性。

在旧世界中，你可以手动创建基于 IP 的规则集。在 Kubernetes 中，没有 IP 地址。因此，工程师必须重新考虑要创建哪些类型的端点以及要建立哪些分段策略。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。