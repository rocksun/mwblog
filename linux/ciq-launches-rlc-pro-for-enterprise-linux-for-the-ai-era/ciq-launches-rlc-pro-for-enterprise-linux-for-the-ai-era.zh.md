构建了流行 [Rocky Linux](https://thenewstack.io/how-almalinux-and-rocky-linux-have-diverged-since-centos/) 发行版的公司 [CIQ](https://ciq.com/)，推出了 [RLC Pro](https://ciq.com/products/rocky-linux/pro/)，这是一种新的商业支持企业级 Linux 发行版，它将合规性、长期支持和工程修复捆绑到单一订阅中。

RLC Pro 定位为面向人工智能 (AI)、高性能计算 (HPC) 和受监管行业等工作负载的下一代平台，提供长期支持 (LTS)、对其加密功能进行 FIPS 140-3 验证、赔偿以及来自 CIQ 的直接工程支持。

## 一价全包，无附加组件

该公司表示，这些功能在传统企业产品中通常只能作为昂贵的附加组件提供，但在 RLC Pro 中却是标配。

CIQ 首席执行官兼 Rocky Linux 创始人 Gregory Kurtzer 在一份声明中表示：“AI 正在推动企业基础设施的真正拐点。RLC Pro 将组织所需的基础设施能力整合到一个‘随处可用’的模型中，优先考虑效率、安全性和可用性。当您遇到 bug 时，我们会修复它。”

据 CIQ 称，RLC Pro 解决了企业级 Linux 生态系统中的一个长期挑战：开源灵活性和商业级可靠性之间的权衡。使用社区发行版的组织通常会投入大量的内部工程资源来管理补丁和合规性。与此同时，商业平台的用户可能面临不断上涨的订阅成本，以获取与开源平台提供的类似功能。

RLC Pro 将这两种模式整合到单一订阅中。它包括：

*   **捆绑长期支持 (LTS)：** 3-5 年的稳定生命周期管理，无需强制升级。
*   **FIPS 140-3 验证：** 适用于政府、国防、金融和医疗保健环境的合规性就绪软件包。
*   **直接的 Bug 和安全修复：** CIQ 工程师根据客户反馈提供的响应式问题解决。
*   **企业许可协议 (ELA)：** 覆盖核心、云和边缘基础设施的混合部署。

## RLC Pro 对比竞争对手

您可能会问，“RLC Pro 和 Red Hat Enterprise Linux (RHEL) 有什么区别？” RLC Pro 本质上将自己定位为“RHEL 式的默认捆绑包”，而 RHEL 则提供相同类别的功能，但将其划分为多个附加组件和层级。

深入来看，RLC Pro 的基本订阅模式提供三到五年的支持周期，没有强制性的点版本升级。而 RHEL 订阅，每个主要版本（完整 + 维护 + 扩展生命周期阶段）都有一个标准的 10 年生命周期，并在此期间有 9 个或更多的小点版本发布。

另一个想到的比较对象是 [AlmaLinux OS](https://almalinux.org/)。与 CIQ 的 Rocky Linux 类似，Alma 的出现是为了回应 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) [终止 CentOS Linux](https://thenewstack.io/red-hat-deprecates-linux-centos-in-favor-of-a-streaming-edition/)。

这里，区别在于 RLC Pro 将什么捆绑到单一订阅中。AlmaLinux 将其分为免费的社区操作系统和来自 [TuxCare](https://tuxcare.com/) 的商业选项（FIPS、扩展生命周期、实时补丁、企业支持）。使用 AlmaLinux，您仍然使用社区发行版，并根据需要选择商业附加组件。而 RLC Pro，“企业级”层是默认产品，这些功能被定位为基线而非附加组件。

CIQ 和 AlmaLinux/TuxCare 都没有公布其许可费用。

Rocky Linux 仍然是部署最广泛的企业级 Linux 发行版之一，CIQ 引用来自 [Extra Packages for Enterprise Linux (EPEL)](https://docs.fedoraproject.org/en-US/epel/) 的遥测数据显示，全球有超过 275 万个活跃实例。该公司表示，RLC Pro 建立在这一社区势头之上，为需要商业问责制、生命周期保证和合规性保障的企业提供了一条路径。

CIQ 总裁 Bjorn Hovland 表示：“真正的变革在于这能让企业做些什么。组织可以立即在受监管的环境中部署，自信地规划基础设施，并让开发人员专注于创新而不是操作系统维护。”

RLC Pro 现已通过 CIQ 和云市场（包括 AWS、Microsoft Azure 和 Google Cloud）提供。RLC Pro 将于今年晚些时候添加到 [CIQ Portal](https://ciq.com/blog/manage-your-ciq-account-and-software-with-ciq-portal/)。