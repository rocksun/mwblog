
<!--
title: 面向未来的AI：重蹈覆辙还是从历史中学习？
cover: https://cdn.thenewstack.io/media/2025/05/f044c2ab-future-proofing-ai.jpg
summary: AI时代，科技巨头狂砸基础设施！但别重蹈覆辙！吸取云计算、容器化教训，警惕安全漏洞和资源浪费。用Rust重构Xen等虚拟机监控程序，在内核级实现安全隔离，提升GPU利用率。拥抱云原生，构建安全、高效的AI基础设施， Kubernetes等技术别忽视！
-->

AI时代，科技巨头狂砸基础设施！但别重蹈覆辙！吸取云计算、容器化教训，警惕安全漏洞和资源浪费。用Rust重构Xen等虚拟机监控程序，在内核级实现安全隔离，提升GPU利用率。拥抱云原生，构建安全、高效的AI基础设施， Kubernetes等技术别忽视！

> 译自：[Future-Proofing AI: Repeating Mistakes or Learning From the Past?](https://thenewstack.io/future-proofing-ai-repeating-mistakes-or-learning-from-the-past/)
> 
> 作者：Alex Zenla

在硅谷的中心地带，科技巨头们正在掀起一场前所未有的 AI 基础设施支出狂潮，仅 2025 年就高达 3200 亿美元。亚马逊计划投入 1000 亿美元的资本支出，比去年的 770 亿美元投资有了显著的飞跃。与此同时，[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention) 和 [Meta](https://about.meta.meta/?utm_content=inline+mention) 的基础设施投资总额与 2024 年相比增长了 30%。我们以前看过这部电影——但它并不总是有美好的结局。

作为一名 25 岁的自学成才的软件工程师，我沉浸在多次计算革命的技术中，我研究了范式转变时出现的模式。从本地软件到虚拟化的过渡，从虚拟机 (VM) 到云原生 [containers](https://thenewstack.io/introduction-to-containers/)，再到现在的 [AI era](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)，这个周期是毋庸置疑的。历史总是重演：速度胜过安全，效率低下被认为是创新的代价，技术债务悄无声息地累积，直到变得难以承受。

## 过去数字化转型的教训

还记得云计算的热潮吗？各组织整体迁移工作负载，通常没有针对 [cloud native](https://thenewstack.io/cloud-native/) 效率进行重新设计。以 Netflix 迁移到 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 为例，该迁移始于 2008 年，但耗时近八年才完成。其最初的“直接迁移”方法导致了重大中断，包括 2012 年圣诞节前夕影响数百万客户的中断。只有在采用云原生原则并开发像 [Chaos Monkey](https://thenewstack.io/chaos-engineering-business-value/) 弹性测试系统这样的工具后，AWS 才实现了云所承诺的可靠性和效率。

然后是容器化——一种变革性的方法，承诺更高的效率和可移植性。然而，许多组织在现有基础设施之上实施容器，而没有解决根本的安全和性能问题。Target 在其容器采用过程中亲身[experienced](https://www.ciodive.com/news/target-cloud-migration/628448/)了这一点，发现其传统的安全工具无法充分保护容器化的工作负载，导致可见性差距和潜在漏洞。X（前身为 Twitter）著名的且令人尴尬的频繁“[Fail Whale](https://www.wired.com/2013/11/qa-with-chris-fry/)”是试图运行一个设计不佳的故障处理的单体 Ruby 应用程序的后果。该行业逐渐成熟，开发了像 [Kubernetes](https://thenewstack.io/kubernetes/) 这样的编排平台和标准化的安全实践，但在此之前，由于适当的规划本可以避免的代价高昂的错误。

每个过渡都遵循类似的轨迹：最初的兴高采烈、仓促的实施、事后才考虑的安全、低效的资源利用，以及最终，一种在创新与企业需求之间取得平衡的更成熟的方法。

## 从过去中学习，以拯救未来的创新

今天的 AI 繁荣有陷入这些相同陷阱的风险——只是风险更高。据报道，仅 OpenAI 的 GPT-4 的训练就花费了 [over $100 million](https://www.wired.com/story/openai-ceo-sam-altman-the-age-of-giant-ai-models-is-already-over/) 的计算资源。现代 AI 的计算需求是巨大的，像微软这样的公司正在构建专门的超级计算机来训练这些模型。部署 AI 应用程序的竞赛使各组织接受了这些工作负载运行方式的巨大低效率。

AI 淘金热自然也产生了相应的效果，即引入的 AI 项目激增。[GitHub’s Octoverse 2024 report](https://github.blog/news-insights/octoverse/octoverse-2024/) 引用了 GitHub 上托管的 137,000 个生成式 AI (GenAI) 项目，比 2023 年同比增长 98%。如果我们从过去几年的软件供应链安全攻击中学到任何东西，那就是从安全角度来看，开源项目的资源严重不足。

急于部署新的开源 AI 项目的企业是否采取了必要的安全措施，将其与基础设施的其余部分隔离？或者他们是否无视最近的开源安全历史，并默认信任它们？
令人担忧的是，还有报告称，位于中国、朝鲜和俄罗斯的网络犯罪团伙正在积极瞄准物理和 AI 基础设施，同时利用 AI 生成的恶意软件更有效地利用漏洞。微软 2024 年的一项[研究](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/new-innovations-in-container-security-with-unified-visibility-investigations-and/4298593)发现，包括 AI 系统在内的基于容器的工作负载面临着越来越多的威胁，预计到 2024 年，容器的采用率将达到 52%，同时安全挑战也在不断增加。

然而，我们有理由感到乐观。以往技术变革的经验可以为 AI 基础设施提供更好的方法——这种方法既能提供企业所需的敏捷性，又能从一开始就建立安全、高效的基础。

## 容器难题：强大但并不完美

虽然容器彻底改变了应用程序的部署，但当应用于 AI 工作负载时，它们会带来重大的挑战。

**资源效率低下**

标准的容器化通常会导致资源浪费。例如，Uber 的工程团队[发现](https://www.uber.com/blog/scaling-ai-ml-infrastructure-at-uber/)，其容器化的机器学习 (ML) 服务仅利用了 20-30% 的已分配 GPU 资源，从而有效地浪费了其昂贵的 AI 基础设施的 70-80%。这种效率低下与 AI 工作负载相结合，而 AI 工作负载本身就非常消耗资源。

**安全漏洞**

容器安全仍然是一个持续的挑战。容器共享主机的操作系统 (OS) 内核，从而创建了传统安全工具无法解决的独特攻击媒介。容器的短暂性使得安全监控特别困难，正如微软[指出](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/new-innovations-in-container-security-with-unified-visibility-investigations-and/4298593)的那样，安全团队很难确定哪些容器在任何给定时间运行，并查明易受攻击的容器。

**性能瓶颈**

容器引入的开销对于 AI 工作负载来说尤其成问题。Netflix 的工程团队[记录](https://www.linkedin.com/pulse/navigating-network-challenges-case-study-netflixs-traffic-gogte-xlotf/)了其 ML 推理服务在容器化时如何因容器架构固有的网络和 I/O 瓶颈而面临延迟问题。对于实时 AI 应用程序，这些性能损失是不可接受的。

**运营复杂性**

容器化环境的动态特性带来了显著的运营复杂性。根据 [Flexential 的 2024 年 AI 基础设施状况报告](https://www.flexential.com/system/files/file/2024-07/flexential-state-of-ai-infrastructure-report-2024-hvc.pdf)，82% 的组织在过去 12 个月中遇到了 AI 工作负载的性能问题，这通常源于管理容器化环境的运营挑战。

## 构建面向未来的 AI 基础设施

解决当前基础设施挑战的方案不是放弃容器或放慢创新，而是应用经过时间考验的原则，同时针对 AI 的独特需求进行调整。一种周全的方法是将成熟技术的可靠性与现代开发团队所需的敏捷性相结合。

**重新构想 AI 时代的虚拟化**

二十年前彻底改变计算的虚拟化技术从根本上来说仍然是可靠的，但我们看到了改进这项已有数十年历史的技术的机会，以满足现代计算的需求和差距。在内存安全语言（如 [Rust](https://thenewstack.io/rust-programming-language/)）中重新实现 Xen 等虚拟机监控程序技术，可提供传统虚拟化的经过实战检验的安全隔离，并显著提高性能和资源效率。

这种现代化的虚拟化不是采用传统的一刀切的容器方法，而是根据实际的 AI 工作负载需求动态分配资源，从而消除了困扰标准容器化的过度配置问题。

**设计时就考虑安全性，而不是事后诸葛亮**

面向未来的基础设施不是将安全性附加到固有脆弱的系统上，而是在基础层面构建安全性。通过使用现代化的虚拟机监控程序技术在内核级别实现真正的隔离，组织可以从一开始就创建安全的多租户——这是处理敏感数据的 AI 工作负载的关键要求。

**性能不打折扣**

下一代 AI 基础设施不应受到因使用当今解决方案创建真正的、安全的多租户环境而产生的性能损失的束缚。通过将裸机性能的最佳方面与类似容器的部署模型相结合，组织可以构建既能提供速度又能提供便利的系统。例如，Edera 的技术不需要硬件，对于实际工作负载，它比 Kata Containers（仅有的依赖硬件的替代方法之一）[快 41%](https://arxiv.org/abs/2501.04580)。

这种架构保留了开发者喜爱的容器的部署优势，同时消除了使容器化 AI 工作负载难以处理的性能瓶颈。

**简化复杂性的统一管理**

最成功的 AI 基础设施方法是与现有系统无缝集成，而不是创建孤立的孤岛。通过统一传统工作负载和 AI 工作负载的管理，组织可以保持一致的安全性、治理和运营实践。

平台团队获得了他们需要的可见性和控制力，而开发人员保持了他们需要的速度——证明了当基础设施设计正确时，安全性和速度并非相互排斥。

## 前进的道路

我们正在经历的 AI 革命并非凭空而来。在我十几岁的时候，我学习了过时的计算范式——深入研究虚拟机监控程序，阅读 Xen 和 KVM 背后的架构决策，并探索 20 世纪 70 年代和 80 年代的操作系统设计原则——并且我开始欣赏技术历史如何为我们最紧迫的挑战提供解决方案。

当我第一次通过 Xen 等项目接触到虚拟化时，我震惊于它如何优雅地解决了边缘设备面临的资源共享和安全隔离问题。设计这些系统的计算机科学家正在解决超越特定技术趋势的根本问题。他们的解决方案，针对现代硬件进行了更新，并以内存安全语言（如 Rust）实现，仍然是满足 AI 基础设施需求的强大工具。

如果我们忽视过去的智慧，我们就无法建设稳固的未来。计算安全、资源管理和运营效率的基础是几十年前由那些必须让每个 CPU 周期和内存字节都发挥作用的先驱者奠定的。当我们构建消耗前所未有的计算资源的系统时，他们的经验教训比以往任何时候都更加重要。

在 AI 时代能够生存下来的组织不一定是那些拥有最大基础设施投资或最流行的技术堆栈的组织。领导者将是那些认识到回顾过去有时是前进的最佳方式，在拥抱现代 AI 工作负载的特定需求的同时，调整经过时间考验的原则。

作为一名研究过计算过去成功与失败的人，我深信我们最好的前进道路是将昨天的智慧深思熟虑地应用于明天的挑战。对于我们这些愿意学习的人来说，这些经验教训就在那里。