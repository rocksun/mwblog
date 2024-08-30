# eBPF 安全力量与不足

![eBPF 安全力量与不足的特色图片](https://cdn.thenewstack.io/media/2024/08/3d7f4b59-enis-can-ceyhan-xmrvdstiyay-unsplash-1024x576.jpg)

每个声称提供全面安全的安全工具和平台都应该至少包含一些 [eBPF](https://thenewstack.io/what-is-ebpf/) 的方面。但是，对于组织的安全态势，eBPF 不应该也不可能涵盖当今 [DevOps](https://thenewstack.io/devops/) 和平台工程实践中所要求的、日益紧迫的全部安全用例范围。

但我们不妨说 eBPF 是安全领域必不可少的元素。它确实有其局限性，这些局限性要么需要扩展，要么需要在安全产品中加以考虑，或者在某些情况下需要单独解决。

一个充分利用 eBPF 的安全提供商也会在其功能的基础上构建一个全面的平台。即使如此，也很难找到一个安全提供商平台，它不需要在充分利用 eBPF 的基础上添加补充工具。

[Ben Hirschberg](https://il.linkedin.com/in/ben-hirschberg-66141890)，安全提供商 [ARMO](https://www.armosec.io/homepage-new-lp-2/?utm_term=kubescape&utm_campaign=brand-kubescape-us_t1-cpc&utm_source=google&utm_medium=cpc&utm_content=armosec&hsa_acc=5055384472&hsa_cam=17941524163&hsa_grp=142744593834&hsa_ad=708348387730&hsa_src=g&hsa_tgt=kwd-1016805388690&hsa_kw=armosec&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjwoJa2BhBPEiwA0l0ImCWwGC5TjjCbLdHR2f0Hang_OqLa6IQoP8jJ8oV4Ck9VpkaI_uYR9BoCgaAQAvD_BwE) 的 CTO 以及 [CNCF](https://cncf.io/?utm_content=inline+mention) 开源项目 [Kubescape](https://thenewstack.io/kubescape-3-0-the-result-of-lessons-learned-with-ebpf-for-security/) 的创建者对此表示同意和不同意。“我认为没有多少人认为 eBPF 旨在解决所有问题。这就像说有人认为锤子是万能工具一样，”Hirschberg 说。“理论上，可以证明锤子不能砍倒树木，但斧头总是更适合砍树。没有人认为 eBPF 是解决所有安全需求的单一工具/技术。”

也就是说，如果组织想要确保他们正在使用 eBPF，那么提供商至关重要。根据 Gartner 的说法，大多数企业缺乏构建和集成基于 eBPF 的功能所需的专业知识和技能。但是，Gartner 还建议组织“在规模、性能、可见性和安全性至关重要的前提下，寻求基于 eBPF 的 Kubernetes CNI [容器网络接口] 解决方案。”

[Utpal Bhatt](https://www.linkedin.com/in/ubhatt)，[Tigera](https://www.tigera.io/) 的 CMO 表示，大多数安全平台使用 eBPF 来监控和分析网络流量、系统调用和其他内核级活动，从而能够实时检测可疑行为或异常。“但是，全面的安全方法应该整合预防和风险缓解策略，”他说。

例如，相当一部分攻击来自已知的恶意攻击者，一个简单的 IDS/IPS 系统与威胁情报集成可以防止这些攻击“从一开始就发生，”Bhatt 说。

像 MISP（恶意软件信息共享平台）这样的来源存储、收集和共享威胁情报和入侵指标（IOC），例如文件哈希，Bhatt 说。“有效的安全策略将是阻止此类恶意软件执行。此外，大多数系统应该假设它们会被攻击，并且应该能够访问快速风险缓解工具，”他说。

例如，在 Kubernetes 的情况下，部署缓解网络控制可以减少攻击的爆炸半径，Bhatt 说。“eBPF 是威胁检测方面最重要的创新之一，”他说。“但是，它可能无法检测到所有内容，在攻击者和防御者之间的猫鼠游戏中，预防和风险缓解同样重要。”

## 工作原理

正如 [Liz Rice](https://www.linkedin.com/in/lizrice/) 在 [“学习 eBPF”](https://www.oreilly.com/library/view/learning-ebpf/9781098135119/) 中所定义的那样，系统调用或系统调用是用户空间应用程序和内核之间的接口：“如果你限制了应用程序可以执行的系统调用集，那么就会限制应用程序能够执行的操作。如果你一直在使用 [Docker](https://www.docker.com/?utm_content=inline+mention) 或 Kubernetes，那么你很有可能已经使用过一个使用 BPF 来限制系统调用的工具：[seccomp](https://en.wikipedia.org/wiki/Seccomp)，”正如 Rice 所写。Seccomp 在容器世界中被广泛使用（以默认的 Docker seccomp 配置文件形式），但这只是今天基于 eBPF 的安全工具的第一步，Rice 说。
使用 [seccomp BPF](https://www.kernel.org/doc/html/v4.19/userspace-api/seccomp_filter.html)，加载一组 BPF 指令作为过滤器，Rice 写道。每次调用系统调用时，都会触发过滤器。过滤器代码可以访问传递给系统调用的参数，允许它根据系统调用本身以及传递给它的参数做出决策。Rice 说，结果可能包括允许系统调用继续执行、向用户应用程序空间返回错误代码、终止线程或通知用户空间应用程序等操作。

使用 eBPF，可以实现更多强大的选项和功能。Rice 说，seccomp 仅限于系统调用接口，而 eBPF 程序现在可以附加到操作系统的几乎任何部分。“与预定义的过滤器程序不同，eBPF 程序员可以灵活地编写自定义和定制代码，”Rice 说。

例如，Rice 说，eBPF 程序可以附加到每次打开文件或接收网络数据包时触发的内核事件。该程序可以将有关该事件的信息报告给用户空间以用于 [可观察性](https://thenewstack.io/observability/) 目的，或者它甚至可以修改内核对该事件的响应方式。Rice 说，在网络安全中，eBPF 程序可用于丢弃数据包以遵守防火墙规则或防止 DDoS 攻击。

eBPF 正在广泛的应用程序中使用，并已成为许多成功商业项目的基石。它在推动安全方面的进步方面尤其有影响力。曾经限制 eBPF 采用的挑战现在已经克服；例如，早期版本的 eBPF 限制为 4096 条指令，但在内核 5.2 中，该限制已提升至一百万条指令，并且现在可以通过将 eBPF 程序与 [eBPF 尾调用](https://thenewstack.io/what-is-ebpf/) 链接在一起等方式实现更多复杂性，从而导致开发了各种工具和平台，这些工具和平台不仅解决了这些障碍，而且还提高了安全、可观察性、网络等领域的效率。

## 开源构建
许多旨在利用 eBPF 的公司或组织可能缺乏直接充分利用 eBPF 好处的资源或专业知识。有效地使用这些功能需要深入的 Linux 知识，这就是大多数企业不自己编写基于 eBPF 的工具的原因。这就是 eBPF 工具和平台提供商发挥关键作用的地方。他们对 Linux（和 Unix）的深刻理解使他们能够在 eBPF 代码中创建高级功能。

“确实，eBPF 需要大多数组织缺乏的深入理解和技能。能够开发和维护 eBPF 代码的工程师数量非常有限，”Hirschberg 说。“因此，拥有能够为普通用户提供 eBPF 能力的优秀供应商（开源或商业）非常重要。”

Falco 是一个很好的例子，它说明了 eBPF 的强大功能和局限性，尽管它的局限性很小。单独使用时，它用于许多任务，尤其是在为分布式 Kubernetes 和云原生基础设施配置时。

Falco 涵盖了广泛的工作负载和基础设施，当然也扩展到内核，因为 eBPF 在这方面做得很好。它是获得大量关注的开源项目之一。

但是，它并没有涵盖清单上的所有安全方面，这为其他安全提供商提供了机会，让他们使用 Falco 构建安全解决方案，或提供不与 eBPF 绑定的单独功能。

有趣的是，Falco 最初是在 2016 年底首次发布时使用内核模块创建的，没有涉及或集成 eBPF。当 [Sysdig](https://thenewstack.io/sysdig-prioritizing-risk-with-risk-spotlight/) 将 Falco 贡献给 CNCF 时，它于 2018 年被接受为云原生项目。但是，直到 2021 年，Falco 的创建者才开始将 eBPF 探测器和库作为 Falco 组织的子项目，正如 [Loris Degioanni](https://www.linkedin.com/in/degio) 和 [Leonardo Grasso](https://www.linkedin.com/in/leonardograsso/?originalSubdomain=it) 在他们的书“使用 Falco 进行实用的云原生安全”中所述。

Rice 说，许多企业不愿使用内核模块，因为内核中的错误会导致整个机器崩溃，而且内核模块不会像内核本身那样经过相同级别的测试和现场强化，因此遇到此类错误的可能性可能是一个不可接受的风险。Rice 说，eBPF 相对于内核模块的优势在于 [eBPF 验证器](https://docs.kernel.org/bpf/verifier.html)，它在加载程序时会分析程序，以确保它们不会使内核崩溃，从而消除了这种担忧。
“放弃内核模块是一个重要的里程碑。我们今天在 eBPF 中实现的所有东西，过去都可以在内核模块中实现，”Hirschberg 说。“然而，内核模块有破坏内核的倾向，它们的不稳定性让基于它们的工具的采用非常有限。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。