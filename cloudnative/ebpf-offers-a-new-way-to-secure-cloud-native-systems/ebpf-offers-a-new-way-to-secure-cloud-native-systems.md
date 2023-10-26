<!--
# eBPF 为云原生系统提供了新的安全方法
https://cdn.thenewstack.io/media/2023/10/9684f4fc-lin_sun-1024x768.jpg
Feature image by B. Cameron Gain.
-->

安全提供商正在利用 eBPF 的可观测性来预防攻击，检测和修复高优先级漏洞(并区分严重和不那么严重的漏洞)，检测可疑活动等。

译自 [eBPF Offers a New Way to Secure Cloud Native Systems](https://thenewstack.io/ebpf-offers-a-new-way-to-secure-cloud-native-systems/) 。

eBPF(extended Berkeley packet filter)正在被用于解决云原生环境中的几个安全问题，不仅仅是其最初的网络监控用途。

从Linux内核中延伸(在Windows中的程度较小)，跨网络或环境中的运行时，使其成为Gartner分析师[Simon Richard](https://www.gartner.com/analyst/45057)在Gartner的“[2023年计算炒作周期](https://cloudsoft.io/blog/gartner-hype-cycle-infrastructure-orchestration)”中所说的Linux操作系统的“增强”。

eBPF允许组织在不更改内核源代码或需要内核模块的情况下向Linux添加功能，Richard写道。

专门针对安全性，eBPF提供了监控的非常详细的方式，并提供了监控不同潜在可疑系统活动和代码的跟踪。所有这些都适用于其通道中的就地处理或处理速度。

一个关键方面是安全[提供商正在利用 eBPF 的可观测性](https://thenewstack.io/cilium-cncf-graduation-could-mean-better-observability-security-with-ebpf/)来预防攻击，检测和修复高优先级漏洞(并区分严重和不那么严重的漏洞)，检测可疑活动等。当然，这种扩展还包括分析事件、发出和接收有关漏洞和事件的警报，以及分析或发现潜在的危险漏洞和攻击轨道。 正是可观测性方面的[利用 eBPF 来监控和检测](https://thenewstack.io/what-ebpf-means-for-container-threat-detection/)可疑活动，并帮助确定哪些漏洞有可能被利用。

## 内核时间

[安全提供商Kubescape创始公司ARMO](https://www.armosec.io/)的[Shauli Rozen](https://il.linkedin.com/in/shaulirozen)说: "eBPF的采用率确实正在改变安全公司的游戏规则，使它们能够访问关键数据而无需更改内核。然而，我们确实看到一些公司正在努力增加eBFP解决方案所需的额外资源，主要集中[在eBPF的数据跟踪](https://thenewstack.io/ebpf-put-the-kubernetes-data-plane-in-the-kernel/)所需的CPU消耗和网络流量以及对这些数据进行分析。"

eBPF的神奇之处在于它如何在不直接更改内核代码的情况下[从内核中工作](https://thenewstack.io/greg-kroah-hartman-lessons-for-developers-from-20-years-of-linux-kernel-work/)。

由于eBPF在一个封闭的沙箱环境中运行，所以它的运行时相对不侵入性，有助于防止它与内核直接交互，同时也发源自内核内部。因此，它可以用于检测和确定漏洞的相关性和威胁级别，并确保内核中可能发生的潜在安全问题。

从内核一直到[跨网络的运行时环境](https://thenewstack.io/identifying-solving-issues-containerized-production-environments/)的这种监控和可观测性，包括高度分布式的Kubernetes环境、节点和容器等。换句话说，[eBPF的可观测性](https://thenewstack.io/groundcover-simplifying-observability-with-ebpf/)扩展超出了单台机器，它在分布式系统中很有用。

[Vandana Salve](https://www.linkedin.com/in/vandana-salve-31b0586/)，Micron Technology的独立软件架构师和软件架构师，在9月关于使用eBPF保护Linux内核的Open Source Summit Europe演讲中说，eBPF“允许开发人员编写可在运行时加载到内核中的代码。”

它还可以帮助更改内核代码或[添加你希望作为安全实施的一部分的逻辑](https://thenewstack.io/how-paybase-overcame-default-kubernetes-security-settings-for-pci-dss-compliance/)。” eBPF框架由指令集组成。它可以被视为在隔离的沙箱环境中运行[eBPF程序](https://thenewstack.io/how-io_uring-and-ebpf-will-revolutionize-programming-in-linux/)的虚拟机。这是通过执行eBPF字节码来实现的。验证器确保程序加载的字节码保持完整性。验证器执行所有必要的检查。

[eBPF程序](https://thenewstack.io/this-week-in-programming-ebpf-coming-to-a-windows-near-you/)是事件驱动的，并在内核或应用程序达到某个挂钩点时运行。预定义的挂钩点包括:

- 系统调用
- 函数入口/出口
- 内核跟踪点 
- 网络事件
- 其他事件，例如调度算法

大规模来看，生成的[Linux安全](https://thenewstack.io/design-system-can-update-greg-kroah-hartman-linux-security/)模块(LSM) eBPF程序允许特权用户在运行时检测LSM挂钩，使用eBPF实现系统范围的强制[访问控制](https://thenewstack.io/tns-tutorial-friday-arcadia-data-redefining-security-apache-hadoop/)(MAC)和审计。它们提供了:

- 适当的LSM挂钩
- 使用eBPF辅助程序和访问结构字段
- 与用户空间共享变量
- 访问或拒绝函数和操作

本质上，这使您能够实现MAC和内核[控制策略](https://thenewstack.io/open-policy-agent-the-top-5-kubernetes-admission-control-policies/)，Salve说。

## 快速修补

eBPF有时被错误地描述为能够直接更改或修改内核代码。实际上这种说法是不准确的，eBPF直接从内核内运行。这使它能够解决在内核中发现漏洞时，对运行中的Linux机器应用修补程序的一个[关键安全挑战](https://thenewstack.io/devops-security-overcome-cultural-challenges-transform-true-devsecops/)。这在零日漏洞的情况下特别有用，在这种情况下，可以修改Linux内核的行为，而无需更改[Linux内核](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/)代码本身。如果可以应用与版本和分发无关的热修补程序，[安全团队](https://thenewstack.io/why-your-successful-cloud-journey-starts-with-building-the-right-security-team/)就可以快速修复这些漏洞。否则，Linux代码修复需要几个月的时间进行审查、测试、分发和安装。

solo.io高级总监、Istio TOC成员和CNCF大使[Lin Sun](https://www.linkedin.com/in/lin-sun-a9b7a81/)在其主持的“Developing Portable eBPF Applications”研讨会上说:“我记得听说将PR([拉取请求](https://thenewstack.io/week-programming-documentation-amalgamation-comes-mozilla/))合并到Linux内核可能非常具有挑战性，因为维护者对及时合并新功能保持了很高的标准。”

“这就是eBPF发挥关键作用的地方——它允许您在无需等待PR合并到内核或经历冗长等待的情况下，扩展内核之外的功能。”Sun说，“不管您喜欢哪种[Linux发行版](https://thenewstack.io/linux-distributions-can-teach-rolling-releases/)，eBPF在设计上非常注重安全性。代码在加载时会由内核验证，以确保其不会危害或破坏内核。这就是它在沙箱环境中运行的原因。”

## 多内核

eBPF程序直接在内核中运行并与内核结构交互，这可能限制了它在[多版本](https://thenewstack.io/linux-manage-multiple-versions-of-node-js-with-the-nvm-manager/)内核上的可移植性。但是，安全工具提供商通过创建方法使eBPF以一种方式编写，使相同的eBPF程序可以在多个内核版本上运行，[以解决此缺点](https://thenewstack.io/be-careful-what-you-ask-for-webmobile-edition/)。

例如，由开源Kubescape驱动的[Kubernetes企业安全平台](https://thenewstack.io/aporetos-kubernetes-security-platform-now-offers-multiregion-cluster-support-service-mesh-integration/)ARMO利用了eBPF的“一次编译，处处运行”(CO-RE)特性。CO-RE允许eBPF程序[跨多个内核版本在多个内核上](https://thenewstack.io/britive-just-in-time-access-across-multiple-clouds/)运行和部署。

此特性的重要意义在于，它使得基于[eBPF的技术的开发和部署更容易](https://thenewstack.io/week-programming-developers-help-harvey-typescript-gets-update/)，这将带来更广泛的采用。

“这非常重要，这也是[安全采用](https://thenewstack.io/why-third-party-security-adoption-must-get-better/)的主要障碍之一，在过去内核代理的‘旧’时代，互操作性和覆盖范围也是最难掌握的领域之一。” Rozen说。“这些功能可以更有效地实现更大的覆盖范围和互操作性。”
