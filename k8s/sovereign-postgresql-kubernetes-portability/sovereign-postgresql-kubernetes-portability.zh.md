多年来，围绕数字主权的争论一直集中在基础设施上。现在，焦点正在转向一个更有价值的企业层：数据库。地缘政治压力（尤其是在欧洲）正迫使像 [Amazon](https://www.reuters.com/business/retail-consumer/amazon-launches-new-europe-based-cloud-service-address-user-concerns-2026-01-15/) 和 [Microsoft](https://www.reuters.com/sustainability/boards-policy-regulation/microsoft-lays-out-data-protection-plans-european-cloud-customers-2025-06-16/) 这样的超大规模云厂商投入巨资以满足新的政策和法规，因为数据治理正迫使组织重新评估对托管云服务的依赖。越来越多的企业不再接受锁定，而是将 PostgreSQL 等资产视为一种可移植的、云中立的基础，在本地、私有云和公有云环境中的表现完全一致。这种转变激发了人们对一些工程师所称的[主权 DBaaS](https://www.enterprisedb.com/blog/beyond-dbaas-trap-claiming-operational-independence-postgresql)（Sovereign DBaaS）的兴趣：即在不向超大规模云厂商交出控制权的情况下，提供云级自动化的数据库平台。

这一变革的核心人物是 [Gabriele Bartolini](https://www.linkedin.com/in/gbartolini/)，他是 [EDB](https://www.enterprisedb.com/products/edb-postgres-ai) 的副总裁兼 Kubernetes 首席架构师。作为开源 PostgreSQL 社区的知名人物，Bartolini 为这一讨论带来了深厚的公信力。他联合创立了 2ndQuadrant，创办了意大利 PostgreSQL 用户组 (ITPUG) 和 PostgreSQL Europe，并且是 [CloudNativePG](https://cloudnative-pg.io/) Operator 的联合创始人兼活跃维护者。Bartolini 还是 Barman 的创造者，这是 Postgres 生态系统中最关键的灾难恢复工具之一。多年来，他的工作在确立 PostgreSQL 作为[云原生环境](https://www.enterprisedb.com/blog/kubecon-cloudnativecon-europe-2025-recap-kubernetes-all-grown)中一等公民的地位方面发挥了重要作用，包括领导了使 [EDB 成为首个针对 PostgreSQL 的 Kubernetes 认证服务提供商](https://www.enterprisedb.com/products/edb-postgres-ai-for-cloudnativepg)的倡议。

根据 Bartolini 的说法，这并不是一种妥协。这是在重新构思问题，以获得两全其美的效果：便利性和控制力。“真正的主权始于数据库。如果你的 PostgreSQL 不能跨环境迁移，你就没有真正控制你的技术栈，”他说道。确保跨环境的一致性允许企业标准化部署、执行策略，并充满信心地管理复杂且资源密集型的工作负载。Bartolini 强调，这种架构选择还直接增强了谈判筹码、监管合规性和长期战略灵活性。

* **诱人的捷径：** 虽然托管云服务承诺了速度和简单性，但 Bartolini 警告说，便利往往以牺牲控制为代价。“便利是云最大的捷径，但便利不等于主权。真正的控制意味着你可以将数据库迁移到任何地方，且其行为保持一致。”对于依赖混合环境一致行为的组织来说，Bartolini 的警告尤为重要，因为一个小失误就可能演变成运营或合规风险。
* **筹码之战：** 对于许多领导者来说，摆脱托管中心化服务的初衷在于长期筹码。Bartolini 将前期投资视为一种战略交换，旨在确保未来的自由和谈判权，并指出这种方法已经获得了足够的关注，超大规模云厂商也开始承认这一点。他提到 [最近一段 Microsoft 的视频](https://www.youtube.com/watch?v=KEApG5twaA4)，该视频鼓励客户在其 [Azure Kubernetes Service](https://blog.aks.azure.com/2025/11/10/announce-pgsql-howto) 上运行带有 CloudNativePG 的自托管 PostgreSQL，这标志着可移植性正在进入主流。“作为一个组织，你在面对超大规模云厂商时获得了巨大的筹码，因为他们知道你可以轻松离开，”Bartolini 解释道。“这种可移植性迫使他们提供更好的产品和更优惠的价格来留住你的业务。”

这种可移植性的关键推动力是 Operator 模式，这是一种通过扩展 Kubernetes 本身将数据库管理提升到简单容器化之上的架构。它的工作原理是将特定领域的专业知识编码到软件中，本质上是教 Kubernetes 如何管理像 PostgreSQL 这样有状态应用的整个生命周期。这种方法在 [CloudNativePG](https://www.enterprisedb.com/products/cloudnativepg) 中得到了体现，它支持[现代微服务数据库架构](https://www.enterprisedb.com/use-case/microservices-and-kubernetes)，并为高可用性、备份和自愈提供声明式 API，使用的是原生 PostgreSQL 流复制而非专有的云工具。

* **运营大脑：** Bartolini 断言，虽然 Kubernetes 提供了可移植性，但仅仅将数据库容器化是不够的。数据库本身必须编码运营智能，并与其集群一起有效地管理其生命周期。“通过将 DBA 的智能作为运营大脑嵌入到 Kubernetes 中，你打破了超大规模云厂商的‘运营墙’，创造了一个对开发者足够自动化、对企业足够主权的 DBaaS。”

但所有这些控制是否以牺牲性能为代价？Bartolini 认为恰恰相反——他有数据可以证明。他提到了即将发布的最新基准测试，这些测试展示了 CloudNativePG 在裸金属上运行的情况，在同步复制下达到了 30,000 TPS\*，而小型云部署可能仅产生 1,500 TPS。当考虑到[主权 AI](https://www.enterprisedb.com/what-is-sovereign-ai-data-sovereignty) 的需求时，这种级别的性能变得尤为宝贵。

* **AI 成本方程式：** “转向裸金属标志着回归 CAPEX（资本支出）模式。对于 AI，你需要可预测的成本。云支出的不可预测性已经是一个问题，而在 AI 领域，情况很容易失控。固定成本至关重要，”他指出。通过拥有硬件，组织可以更好地预测资源密集型 AI 工作负载的费用，避免云账单中隐藏的变动性，并让团队对性能和预算拥有更多控制权。
* **裸金属性能：** 摆脱虚拟机和云抽象不仅是一个技术选择，更有可能成为性能的倍增器。“如果你转向本地环境并能直接在裸金属上运行 Kubernetes，数据库的速度可以像传统的裸金属部署一样快。许多人认为需要虚拟机，但在配备本地存储的裸金属上部署可以获得巨大的吞吐量，并避免像多次复制块这样的低效操作。”对于构建资源密集型 AI 工作负载的企业，这种方法确保了速度和运营的可预测性，补充了使 AI 项目在财务上可管理的 CAPEX 驱动成本模式。

当然，技术只是成功的一半。要使这种模式运作，需要文化变革。Bartolini 回忆起他自己的 DBA 团队最初认为 Kubernetes 可能不会成熟到今天的地步。在他看来，解决方案是培养[“T型人才”](https://www.gabrielebartolini.it/articles/2024/08/the-urge-of-t-shaped-profiles-to-smooth-the-challenges-of-running-postgres-in-kubernetes/)，即 DBA 在其深厚的专业知识基础上补充对 Kubernetes 的横向理解，并指出这镜像了 21 世纪初 Instagram、Spotify 甚至 Skype 等创新者对 PostgreSQL 的历史性采用。Operator 的自定义资源定义 (CRD) 可以作为关键的推动因素，充当平台工程师和数据库专家之间的透明契约。

* **不断进化的 DBA：** “DBA 有两个选择：留在舒适区并假装 Kubernetes 不存在，或者开始学习。”这一选择反映了企业 IT 更广泛的转变，即基础设施和开发团队越来越多地期望数据库专家能够精通云原生环境，而不是孤立地运作。
* **直面挑战：** 他对 DBA 的适应速度持乐观态度，分享道在 EDB，“我们已经证明，通过大约一个月的学习，DBA 就可以获得 CKA 认证并建立那种 T 型人才画像，从而能够与开发者和基础设施团队进行明智的对话。”这种方法不仅加强了团队间的协作，还使 DBA 成为应用和基础设施工作流的积极架构师，而不仅仅是数据的被动管理者。

“数据库团队不能孤军奋战推动这一变革，否则这将是一场注定失败的‘形式化转型’。”构建他所称的“主权泡沫”通常涉及将其他关键层从特定供应商的服务中解耦，解决从[合规性](https://www.aidatapress.com/news/navigating-global-ai-compliance-challenges-son-u-michael-paik)到[灾难恢复](https://www.aidatapress.com/news/cloud-disaster-recovery-location-transparency-cyberquotient-prasanna-venkat)的一切问题。Bartolini 认为可观测性是影响企业团队的最大差距，并警告说：“如果你的日志和指标被困在供应商的专有工具中，你就不独立。变革需要流向整个基础设施已经前往的方向。”从他的角度来看，团队应将标准格式和技术作为首要原则，而不是依赖 CNCF 原生的可观测性技术栈，以避免被锁定在限制透明度、阻碍协作并约束组织独立扩展和创新能力的专有工具中。

\*吞吐量是使用 pgbench TPC-B 类模拟在未优化的开箱即用 CloudNativePG 安装上测得的；实际性能可能因模式、工作负载模式、复制设置和硬件配置而异。

*获取 O’Reilly 书籍的免费副本：* [*使用 PostgreSQL 构建数据和 AI 平台*](https://www.enterprisedb.com/resources/building-a-data-and-ai-platform-with-postgresql/?utm_source=adv&utm_medium=pa&utm_campaign=adv_ww_in_oreillybook-)