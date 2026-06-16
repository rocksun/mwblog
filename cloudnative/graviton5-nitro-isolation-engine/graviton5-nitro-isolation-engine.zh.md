周三，AWS 宣布其 Graviton5 处理器现已正式商用，并为两款新的 Amazon EC2 实例提供支持：用于通用工作负载的 M9g 和用于需要高速本地存储工作负载的 M9gd。这是自 AWS [在 re:Invent 2025 上预览这些芯片](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2)以来，首批推出的 Graviton5 实例。

新芯片将 Graviton4 的核心数量从 96 个翻倍至 192 个，AWS 表示，与上一代相比，这些新实例将提供高达 25% 的计算性能提升。

> AWS 表示，与上一代相比，这些新实例将提供高达 25% 的计算性能提升。

然而，更有趣的是，这些新实例运行在第六代 Nitro 系统上，该系统现在引入了 Nitro 隔离引擎 (Nitro Isolation Engine, NIE)，这是一个经过形式化验证的新型安全组件，AWS 将其描述为“一个专门用于将虚拟机相互隔离的分离内核”。

## 一个唯一职责就是隔离的内核

[分离内核 (separation kernel)](https://en.wikipedia.org/wiki/Separation_kernel) 的概念已经存在很长时间了。[John Rushby 在 1981 年提出了这个术语](https://dl.acm.org/doi/10.1145/800216.806586)。他的核心观点是，即使在当时，标准的操作系统内核也变得太庞大，无法进行形式化验证。然而，一个更小、更专业的隔离内核由于其相对有限的复杂性，仍然可以进行形式化验证。

AWS 于 2017 年推出了其 [Nitro 系统和 hypervisor](https://aws.amazon.com/ec2/nitro/)，并从那时起一直在 EC2 中实施隔离。但 Nitro 同时也处理大量的业务逻辑，并管理设备驱动程序和其他 AWS 特有功能，这意味着它从一开始就不是为形式化验证而设计的。

有了这个新系统，Nitro hypervisor 仍然负责处理策略，包括虚拟机创建、资源分配、迁移和调度，但它现在被剥离了部分特权，必须请求 Nitro 隔离引擎 (NIE) 来执行任何涉及访客状态的操作，且隔离引擎会在采取行动前检查每个请求。

“将 hypervisor 的关键安全隔离逻辑提炼成一个最小化组件（即 NIE），使其足够小以便于验证和审计，从而为客户提供了前所未有的关于如何实施隔离的可见性，”AWS 的 Dominic Mulligan 和 Nathan Chong 写道。“我们还使用 Rust 编写了 NIE，这是一种更自然地适合形式化验证的语言。”

## 我们是如何走到这一步的

该领域的一些早期工作包括哥伦比亚大学的 [SeKVM 项目](https://www.cs.columbia.edu/~rgu/publications/oakland21-li.pdf)，它是 2021 年首个经过形式化验证的商用级 hypervisor。但看起来这主要是一个从未在商业云中运行的研究项目。

AWS 本身将其归功于 [seL4](https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf)，这是一个证明了操作系统验证是可行性的项目。

为了证明内核的行为是正确的，AWS 使用了 [Isabelle/HOL 证明助手](https://www.amazon.science/blog/isabelle-hol-the-proof-assistant-behind-the-nitro-isolation-engine)。AWS 表示，该模型和证明“包含了 33 万行经过机器检查的数学代码”，使其可以与 seL4 项目相媲美。“然而，与 seL4 不同的是，NIE 是为商业云环境设计的，并作为 Graviton5 用户的常驻功能在生产硬件上发布，”AWS 在其公告中写道。

## 192 个核心：一次实质性的重构

芯片本身经历了实质性的重构。Graviton5 从台积电 (TSMC) 的 4nm 工艺转向 3nm，虽然 Graviton4 将所有 96 个核心放在单个小芯片 (chiplet) 上，并将 PCIe 和 DDR 控制器放在各自的小芯片上，但 Graviton5 将其 192 个核心划分为四个小芯片，每个小芯片都有自己的控制器，这使得内存控制器更靠近核心。

AWS 声称，结合更快的内存芯片，这将使 Web 应用程序的运行速度比 Graviton4 快 35%，机器学习推理速度也提升 35%。

## Graviton 与代理式 AI

AWS 将 Graviton5 定位为专为代理式 AI 构建的产品。这种策略与 Google 对其 ARM 处理器采取的策略并无太大不同，而且似乎正在奏效。Meta 在 4 月份签署了一项 [数十亿美元的协议](https://www.aboutamazon.com/news/aws/meta-aws-graviton-ai-partnership)，为其代理式 AI 工作部署数千万个 Graviton 核心，Snowflake 在 5 月份 [承诺在五年内投入 60 亿美元](https://www.snowflake.com/en/news/press-releases/snowflake-expands-aws-collaboration-with-6b-commitment-to-accelerate-enterprise-agentic-ai-adoption/)。AWS 表示，Uber 也在为代理式工作负载部署 Graviton。

总的来说，AWS 表示目前有超过 12 万家客户使用 Graviton，并且在过去三年中，AWS 新增的 CPU 容量中超过一半是 Graviton。

AWS 在这里可能拥有一定的先发优势。Microsoft 的 [Cobalt 200](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/announcing-cobalt-200-azure%E2%80%99s-next-cloud-native-cpu/4469807) 仍处于预览阶段，Google 最新的 [Axion](https://cloud.google.com/blog/products/compute/axion-based-n4a-vms-now-in-preview) 芯片直到 1 月份才正式商用，而 NVIDIA 的 [Vera](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/)——可能是所有这些芯片中最受炒作的——将在今年下半年面世。