**[Red Hat](https://thenewstack.io/red-hat-introduces-its-first-out-and-out-ai-platform/) 本周发布了 Red Hat AI 3.5**，此举旨在让软件工程团队能够以与企业级应用同等的运维严谨度在[关键任务](https://thenewstack.io/smarter-ai-for-critical-operations-why-data-matters/)基础设施上运行 AI。

呼应了科技行业中普遍存在的“从试点走向生产”以及“基础设施、模型和代理的单一控制平面”这一论调，Red Hat 的核心举措似乎在于扩展其平台能力，为 AI 服务提供商运行增强的多租户环境。

至关重要的是，该新版 AI 平台旨在运行需要彻底的软硬件隔离（当 AI 工作负载必须处理[敏感数据](https://thenewstack.io/protect-sensitive-data-and-prevent-bad-practices-in-apache-kafka/)、专有模型和受监管信息时必不可少）的 AI 用例，并通过在共享 [GPU 基础设施](https://thenewstack.io/vultr-nvidia-ai-infrastructure/)上的原生多租户能力处理[优先级感知的服务请求](https://arxiv.org/pdf/2503.09304?)（即关键任务工作负载优先于低等级任务执行）。

Red Hat AI 产品高级总监 Tushar Katarki 向 *The New Stack* 表示，在没有安全控制的情况下运行企业 AI 实际上“就像蒙着眼睛驾驶超级跑车”。

“通过 [Red Hat AI 3.5](https://www.redhat.com/en/products/ai?sc_cid=RHCTE0250000437915&gclsrc=aw.ds&gad_source=1&gad_campaignid=22183537126&gbraid=0AAAAADsbVMShE5A5QHDrbm3iw5ib9zxpu&gclid=Cj0KCQjwh4TVBhCWARIsAG0czmpCwai8R3s0h7IB0SYbOJOQwdBghMJyUvUtl7Wil74eCImlFT54elIaAhyTEALw_wcB)，我们提供了将 AI 作为关键任务服务而非不可预测的实验来运行所需的运维护栏、可验证的信任和多租户控制，” Katarki 说道。“你无法衡量就无法扩展，更不应该部署你无法验证的东西。通过统一预部署安全基准测试、实时可观测性和 GPU 资源管理，我们正在赋予平台团队将孤立的 AI 试点转变为完全受管的企业架构的能力。”

## 每个 GPU 请求现在都变成了一个优先级决策

应用数学家、数据科学家兼兼职 CMO Joshua Estrin 博士告诉 *The New Stack*，Red Hat 的工作正当其时；主要是因为“每个 GPU 请求现在都变成了一个优先级决策”，所以开发人员的内部实验不能与财务结算任务享有同等的紧迫性。

“审视目前 AI 基础设施厂商的现状，Red Hat 显然已经意识到，优先级感知的多租户技术可以让企业更高效地使用昂贵的计算资源，但没有隔离的高效率只是一种更快制造安全和可靠性危机的手段，” Estrin 说道。

> “每个 GPU 请求现在都变成了一个优先级决策。”

他认为，该市场的赢家（他提到的常规候选者包括 [Nvidia](https://thenewstack.io/palantir-nvidia-sovereign-ai/)、[Nutanix](https://thenewstack.io/how-nutanix-is-taming-operational-complexity/)、采用 [Rancher](https://thenewstack.io/can-rancher-deliver-on-making-kubernetes-easy/) 的 [Suse](https://thenewstack.io/suse-ai-infrastructure-kubernetes/)、[HPE Ezmeral](https://www.hpe.com/uk/en/products/software/ezmeral-unified-analytics.html) 和 [Broadcom](https://thenewstack.io/broadcom-vcf-kubernetes-platform/) 旗下的 [VMware Cloud Foundation](https://thenewstack.io/vmware-cloud-foundation-is-now-an-ai-native-platform/)）将是那些能够在实时生产环境中“既共享容量，又能证明发生了什么以及在哪里发生”的组织。

“这意味着要证明是谁的工作负载实际执行和运行了，谁有权访问，成本是多少，以及需求激增时会发生什么。这些答案很少来自基础设施图表；它们是在董事会会议室中解决的，通常是在某人的关键工作流变慢之后，但无论如何，这总结了目前 AI 基础设施所处的阶段，” Estrin 补充道。

## 什么是提升多租户的痛点？

为了剖析这里发生的事情，让我们提醒自己，GPU 很昂贵。随着组织转向智能体 AI 的实时生产用例，他们将希望最大化其 GPU 状态为跨多个团队、多个客户、多个应用等提供服务的能力。

这意味着 AI 基础设施效率的广度成为新的智能体瓶颈。

上述用于共享 GPU 基础设施上的原生多租户的优先级感知服务在当前很重要；此功能根据工作负载优先级动态分配 GPU 容量。当低优先级工作负载可以在闲置（或更便宜）的容量上运行时（而不是必须为较小的任务额外配置 GPU 资源），那么每个人周五都可以更早下班。

> “AI 基础设施效率的广度成为新的智能体瓶颈。”

但这并不是这里需要权衡的全部内容；Red Hat 也提到了隔离，这是一个同时具有挑战性的复杂 AI 基础设施学科。通过隔离技术管理的 GPU 计算资源使 AI 服务能够在不访问或干扰其他服务的数据、模型或计算环境的情况下运行。

换句话说，这结合了硬件整合与强大的租户隔离。

## Red Hat 提供了哪些新技术？

Red Hat 表示，此版本允许开发人员通过 [EvalHub](https://github.com/eval-hub) 在部署前验证模型，从而实现以风险为重点的安全基准测试和监管合规认证。

新的可观测性仪表板为平台团队提供了关于推理健康状况、GPU 利用率和 AI 模型性能的实时视图。非管理员用户可以访问用于每用户代币消耗展示（Token 跟踪的另一种说法）和分布式推理工作负载的仪表板。

此外还有用于多租户推理的共享 GPU 控制。所谓的“公平份额 GPU 调度”管理跨租户的资源分配，而优先级感知服务提供准入控制和基于优先级的请求路由，以保护实时推理。如上所述，它还允许后台工作负载使用可用容量。

Nutanix 产品管理副总裁 Anindo Sengupta 向 *The New Stack* 表示，大规模运行多租户 AI 确实需要安全的租户隔离。

“必要的隔离最好通过虚拟化来实现，” Sengupta 说道。“对于专业的大规模 AI 工作负载，选择可能是运行在裸机上的 Kubernetes。在此之上，为了创造真正的价值，智能体需要访问运行在容器上的大语言模型（LLM）以及运行在传统基础设施上的企业系统（数据库、业务系统等）。为了高效运行混合 AI，平台必须以高性能的方式管理这两个环境，并具有通用的操作模型。”

## 可观测性与模型即服务（MaaS）展示

Red Hat 最新版本中内置的可观测性和 MaaS 展示功能旨在提供每用户代币计量、模型和智能体的性能仪表板、MLflow 可视化智能体追踪，以及用于运维和使用透明度的 GPU 利用率仪表板。

为了实现高效的 GPU 内存管理，CPU 卸载的正式发布以及存储卸载的开发者预览版允许模型处理更长的对话和更大的文档，而无需额外的 GPU 硬件。

Red Hat AI Hub 还引入了智能体模板和入门套件，其中包含针对常见企业模式的预配置参考实现，包括代码审查、文档处理和研究工作流。

> Red Hat 希望其 Red Hat AI 3.5 版本能让我们达到一个状态，即基于 GPU 的 AI 资源被视为一种受策略控制的基础设施池。

## 没有互联带宽的算力是拙劣的。

随着企业 AI 试点取得成功并初步显示出一些回报，IT 团队必须着手解决大规模交付的需求。但在整个业务中扩展 AI 需要与任何关键任务基础设施相同的运维严谨性：部署前验证安全、跨共享 GPU 环境的精确资源控制、受管的智能体行为和透明的使用指标。

主权 AI 边缘云提供商 [Zadara](https://www.zadara.com/) 的首席执行官 Yoram Novick 此前曾就这一话题[明确表态](https://www.itpro.com/infrastructure/networking/why-networking-is-just-as-important-as-compute-in-ai-data-centers)。他曾表示，当团队需要扩展 AI 时，“仅仅增加更多的 GPU 而不确保足够的互联带宽，在现代 AI 时代可能会导致收益递减”。

总的来说，凭借其指导优先级感知推理、租户隔离、容量共享和可观测性的能力，Red Hat 希望其 Red Hat AI 3.5 版本能让我们达到一个状态，即基于 GPU 的 AI 资源被视为一种受策略控制的基础设施池。