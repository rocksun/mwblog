<!--
title:  eBPF：更强大的钩子，更多WebAssembly和可观测性
cover: https://cdn.thenewstack.io/media/2021/02/659cbe3d-telescope-4806386_1280-1024x681.jpg
-->

尽管大多数企业目前还没有直接运用eBPF的专业知识，今年可以选择配置了eBPF和功能扩展层的工具，这方面会有更多帮助。

> 译自 [eBPF: Meaner Hooks， More WebAssembly and Observability Due](https://thenewstack.io/ebpf-meaner-hooks-more-webassembly-and-observability-due/)，作者 B. Cameron Gain 是ReveCom Media的创始人和首席分析师。 他对计算机的痴迷始于20世纪80年代初，当时他黑客攻击了太空侵略者控制台，以每天25美分的价格在当地视频游戏厅连续玩游戏。

[eBPF](https://ebpf.io/) 无疑已经实现了它在2023年的宣传效果，在2024年，我们将看到更多有趣的发展。这主要是因为[eBPF已经证明了](https://thenewstack.io/what-is-ebpf/)它的适用性，随着它在监控、可观测性、网络和安全方面的继续采用，以及开源社区的不懈努力。

它都始于Berkeley Packet Filter在2010年与Linux内核合并，之后在2014年成为“扩展”并称为eBPF。如今，eBPF已经展示了它可以通过钩子提供的各种日志、指标、追踪和其他信息的价值。这些钩子来自于底层支持着开发者、运维团队和SRE的应用、基础设施工具、[CI/CD](https://thenewstack.io/ci-cd/)和部署的Linux内核。

也就是说，它要发挥其全部潜力还存在一些挑战。

让我们看看2024年有什么值得期待的。

## 更多的努力

关于开源工作，去年或者说2023年有许多进展。其中亮点包括Kubernetes和面向云原生的eBPF项目(如[Cilium](https://thenewstack.io/cilium-cncf-graduation-could-mean-better-observability-security-with-ebpf/))从CNCF毕业。此外，通过诸如[Kubescape](https://www.armosec.io/kubescape/)、[Inspektor Gadget](https://www.inspektor-gadget.io/)、[Hubble](https://cilium.io/blog/2019/11/19/announcing-hubble/)、[Tetragon](https://tetragon.io/)和[Falco](https://falco.org/tags/ebpf/)等工具，eBPF的适用性和采用率持续提升。另外，正如Gartner所指出，值得注意的是这些开源开发利用了eBPF，而这些工具正助力组织满足业务和安全可观测性需求。

Gartner建议大多数企业缺乏直接利用eBPF的专业知识，应该选择配置了eBPF及功能扩展层的工具。

Gartner分析师[Tony Harvey](https://www.linkedin.com/in/tony-harvey/)和[Jason Donham](https://www.linkedin.com/in/jason-donham/)在“[2023年计算能力炒作周期](https://www.gartner.com/en/documents/4546999)”中写道: “虽然对技术供应商和超大规模公司来说这很现实，但大多数企业缺乏构建和集成基于eBPF功能所需的专业知识和技能。”

换句话说，在沙箱环境中使用eBPF可能很有趣，但在没有信任成熟可靠的eBPF工具和流程来确保组织的安全策略前，不要轻易尝试。

与此同时，解决方案将取决于主要支持eBPF发展的开源项目如何不断改进和交付。

[企业管理协会(EMA)](https://www.enterprisemanagement.com/)分析师[Torsten Volk](https://www.linkedin.com/in/torstenvolk)表示: “目前，eBPF主要是一个‘被动’技术，它直接从操作系统内核监听相关系统数据。例如，这种被动特性限制了基于eBPF的可观测性平台可以提供的自动检测程度。”“如果eBPF允许这些可观测性平台通过系统调用和网络请求自动检测过程传递上下文数据，那么自动检测就可以变得更加开箱即用，因为这些数据可以用来关联内核和应用程序。”

Volk表示，这种自动检测可以自动编译到应用程序代码中，而无需应用程序开发团队进行任何代码变更。“然而，尽管我将这种级别的自动检测描述为‘可观测性的圣杯’，允许应用程序对内核级别的系统数据进行更改可能会成为一个非常棘手的问题，因为这些更改对系统安全性、稳定性和整体性能的潜在影响。”Volk说。“另一方面，内核级别的自动检测甚至可以提高应用性能，因为eBPF代码编译和运行速度比解释代码快。”

## 组织将对安全“相关性”有更明智的认识

eBPF在很大程度上归功于它独特的能力，不仅可以为漏洞和攻击检测提供可观测性，还可以识别和修复漏洞。此外，它在区分和提供脆弱性上下文方面发挥着关键作用，这些脆弱性可以从需要立即补救的攻击中区分出来，或是发生在CI/CD过程中的代码中的次要配置错误。

正如[Isovalent](https://isovalent.com/)的首席开源官[Liz Rice](https://uk.linkedin.com/in/lizrice)在《[学习eBPF:为增强的可观测性、网络和安全编程Linux内核](https://www.oreilly.com/library/view/learning-ebpf/9781098135119/)》一书中写道:“安全工具与报告事件的可观测性工具之间的区别在于，安全工具需要区分正常情况下预期的事件和表明潜在恶意活动的事件。” Rice强调，eBPF作为核心技术，支持创建工具“在事件检测的基础上构建，产生能够检测甚至防止恶意活动的基于eBPF的安全工具。” 通过这种方式，Liz总结说eBPF使安全性有别于其他形式的可观测性。

## 更多集成

我们预计会有更多eBPF工具和项目的集成。例如，Isovalent创建的Cilium将与各种工具和流程进行广泛集成。例如扩展Cilium的边界网关协议(BGP)功能，允许[Kubernetes](https://thenewstack.io/kubernetes/)工作负载无缝连接传统服务/工作负载;以及将[Tetragon的安全事件](https://thenewstack.io/tetragon-1-0-promises-a-new-era-of-kubernetes-security-and-observability/)报告与SIEM集成，为安全团队提供详细的取证来调查恶意事件，Rice在接受The New Stack采访时表示。

此外，还将增加与其他技术的集成，例如[WebAssembly](https://thenewstack.io/webassembly-4-predictions-for-2024/)尽管未像eBPF那样稳定采用，但具有前景。这种集成将利用WebAssembly将应用程序分发到连接端点的通道中的能力，eBPF帮助维持封闭环路。

Rice说:“我们可以将WebAssembly视为用户空间沙箱，将eBPF视为内核沙箱，每个都允许在各自领域进行自定义处理。”“因此，合理预期的是基础设施工具可能会结合两者的功能以互补的方式。这个集成的一个示例是Wasm Envoy插件中的自定义高级L7处理，结合用eBPF实现的Cilium网络”，Rice说，“以创建高级和动态的网络功能，满足组织的定制需求。”

最终可能会将eBPF代码编译成WebAssembly，自动向应用容器注入可观测性，可能还有自动检测，“无论它们在哪里运行”，Volk说。“eBPF与WebAssembly的集成确实令人振奋”，Volk说。“从安全角度来看，由于eBPF在内核中运行，而WebAssembly在Linux操作系统的用户空间中运行，将两者结合可以为完整的应用堆栈提供增强的隔离。”

## 人工智能的关联

毫无疑问，人工智能在未来几个月和几年内不仅对社会会产生深远的影响。观察人工智能如何应用于或与eBPF结合使用将非常有趣。这仍是一个非常笼统的预测，因为实际应用尚不明确。对eBPF将如何体现或人工智能将如何与eBPF集成进行推测纯属猜测。

与此同时，看看网络，特别是如何与eBPF结合使用，而不是仅仅依赖类似ChatGPT等LLM进行网络安全，这一点很有趣。观察这种动态在2024年如何发展将很有趣。“我预期的一个例子是由AI创建的网络策略，并由Cilium执行”，Rice说。“我们在这方面看到了一些实验，像大多数ChatGPT应用一样，还不够可靠到依赖它，但我预计这会有改进。”

此外，Volk说，使用eBPF从操作系统的用户空间添加内核级数据到当前的遥测数据流中，为LLM提供重要的上下文，以便做出更好的决策，并向人类安全工程师推荐更具体的补救行动。“进一步说，eBPF与LLM的集成可以允许LLM基于它们在系统级的影响来实施和评估安全策略”，Volk说。“这就是事情变得非常技术化的地方。”

## eBPF被黑

eBPF旨在提供网络范围内的自定义功能，从内核或跨运行时扩展，尤其是用于Kubernetes。然而，由于eBPF与Linux内核集成，这对一些人来说可能会引发安全问题。毕竟，除了攻击者外，没有人想要具有直接访问操作系统和CPU权限的恶意代码。

为了解决这个eBPF安全问题，[eBPF验证器](https://docs.kernel.org/bpf/verifier.html)会检查代码，只在验证程序在GPL许可下时才授予eBPF写权限。当然，没有什么是完全防患于未然的。正如Rice指出的，验证器检查程序是否安全运行，但无法保证程序不是恶意的。“例如，我可能会编写一个eBPF程序，因为某个地址是恶意流量的来源而丢弃其数据包，或者我作为黑客出于某些不轨目的编写程序以阻止某个地址”，Rice说。“验证器无法区分这两者。”

正如上面所提到的，自己内部不要自定义eBPF工具，而要依赖经过适当审核的供应商同样重要。Rice说:“因此，只能从您信任的供应商加载和运行eBPF程序非常重要。” 内核中正在进行工作，以帮助用户验证eBPF程序的来源(很像应用程序的供应链安全检查)。

我参与这些事情实际上是为了乐趣，当它能推动善意时。因此，我预计并希望在2024年会披露一个漏洞，不仅为了乐趣，也为了进一步加固eBPF进行网络加密。

但是，正如Rice指出的:“eBPF可以大量自定义网络功能，但更典型的做法是依靠其他内核加密实现(如Wireguard)，而不是在自定义的eBPF程序中进行加密。”

此外，从定义上讲，当您增加应用层与内核层交互的能力时，系统的攻击面也会增加，Volk指出。“这很直观，因为这也是最初创建Linux时将内核与应用程序分离的原因，” Volk说。“然而，自Linux最初创建以来已经过去了这么多年，我们现在可能已经有了一种方法，允许应用程序有条件地访问内核而不会冒全部农场受损的风险。”
