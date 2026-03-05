[Eclipse 基金会](https://www.eclipse.org/)本周宣布，作为基于[VS Code 扩展 API](https://code.visualstudio.com/api) 构建工具的开源扩展注册中心 [Open VSX，](https://open-vsx.org/)其每月下载量已突破3亿次。该组织表示，这一里程碑凸显了其作为全球开发者生态系统“基础架构”的作用。

这一数字发布之际，作为开源软件和协作的非营利性管理者，Eclipse 基金会正持续加强该注册中心的安全性和基础设施态势，以应对 AI原生和基于云的平台日益增长的需求。

Open VSX 每日峰值流量超过5000万次请求，拥有来自6500多家发布商的10000多个扩展，现已成为 [亚马逊 Kiro](https://thenewstack.io/kiro-is-awss-specs-centric-answer-to-windsurf-and-cursor/)、[谷歌 Antigravity](https://thenewstack.io/hands-on-with-antigravity-googles-newest-ai-coding-experiment/)、[Cursor](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/) 等工具以及其他 VS Code 兼容编辑器的运营路径中的关键组成部分。

财务支持也随之而来。去年[11月](https://eclipse-foundation.blog/2025/11/05/aws-invests-in-strengthening-open-source-infrastructure-at-the-eclipse-foundation/)消息称，亚马逊网络服务 (AWS) 将投资 Eclipse 基金会运营的开源基础设施，包括 Open VSX。

基金会现已向 *The New Stack* 证实，AWS 的承诺是一项“多年、七位数”的战略投资。Cursor，其专注于 AI 的编辑器为该注册中心带来了大量流量，现在也提供财务支持。

> “AWS 的承诺包括‘基础设施积分和运营协作’，专注于支持 Open VSX 和 Eclipse 基金会旗下的其他关键服务。”

AWS 的承诺包括“基础设施积分和运营协作”，专注于支持 Open VSX 和 Eclipse 基金会旗下的其他关键服务。

尽管 AWS 已经是 Eclipse 基金会的成员，但该组织强调成员资格和基础设施投资是分开的。会员费支持基金会更广泛的开源产品组合的治理和项目服务，并根据公司规模和类别分级。

参与 Open VSX 工作组需要每年支付4万欧元。相比之下，对 Open VSX 的基础设施支持是专门为随着需求扩大而加强注册中心的技术运营而设计的。

Eclipse 坚称，此项安排不会赋予对项目额外的决策权，正如 Eclipse 基金会首席营销官兼产品负责人 [Thabang Mashologu](https://www.linkedin.com/in/thabang-mash/) 告诉 *The New Stack* 的那样：

“这种支持不授予任何治理权利、否决权或特殊监督权，” Mashologu 说。“Open VSX 将继续在 Eclipse 基金会的供应商中立治理模式和 Open VSX 工作组既定流程下运作。”

## 市场的诞生

回顾一下，Open VSX 源于微软 Visual Studio Marketplace 的许可限制，该市场[规定扩展只能安装](https://cdn.vsassets.io/v/M264_20251020.18/_content/Microsoft-Visual-Studio-Marketplace-Terms-of-Use.pdf)并用于微软产品，如 Visual Studio、VS Code 和其他“适用产品”，使得开源分支和替代编辑器无法直接访问它。

Open VSX 作为一种开源替代方案应运而生：一个实现了相同 VS Code 扩展 API 但独立治理的注册中心。

该项目最初由 [TypeFox](https://www.typefox.io/) 开发，Open VSX 的第一个公共实例于2020年上线。此后不久，管理权开始向 Eclipse 基金会过渡，到2021年初，[该注册中心投入运营](https://thenewstack.io/eclipse-open-vsx-registry-offers-open-access-to-vs-code-extensions/)，隶属于基金会治理之下，为其提供了一个正式的非营利性归属并建立了开源监督机制。

随着时间的推移，越来越多的基于浏览器的 IDE、云开发环境和 AI原生编码工具采用 Open VSX 作为其默认或备用注册中心。正如 *The New Stack* [2023年](https://thenewstack.io/alternative-to-visual-studio-marketplace-gains-momentum/)报道的那样，这一增长促成了 Eclipse 基金会内部成立了一个专门的 Open VSX 工作组，由谷歌和 Salesforce 等公司提供支持，为注册中心的持续发展提供更结构化的支持和资金。

该注册中心的核心是为 VS Code 兼容扩展提供软件包分发服务，这些扩展涵盖了从语言服务器、linter 和调试器到测试工具和云连接器的一切功能。这一功能使其处于软件供应链的关键节点。受损的扩展可能会迅速传播到开发人员的机器和托管工作区，而冒充受信任发布商的情况在其他生态系统中已有记录。

在此背景下，Eclipse 正在通过[新的预发布验证框架](https://blogs.eclipse.org/post/christopher-guindon/strengthening-supply-chain-security-open-vsx)来加强注册中心，该框架在发布前扫描和审查扩展。它旨在在生命周期早期捕获某些类别的风险，包括命名空间冒充、扩展名欺骗、嵌入式凭证和已知恶意模式，可疑上传将被隔离以供审查。

虽然大多数提交通过自动化筛选，但那些发出危险信号的提交会升级进行更严格的审查，然后才允许进入注册中心。

“触发定义风险信号的扩展会自动隔离以供进一步审查，” Mashologu 说。“手动审查仅限于标记的案例或模糊的指标。我们还引入了内部报告和管理工具来支持监督。与大多数安全系统一样，某些实施细节故意不予披露，以降低规避风险。”

除了筛选发布内容，Eclipse 还在解决扩展的消费方式。注册中心正在实施有针对性的[速率限制](https://blogs.eclipse.org/post/christopher-guindon/scaling-open-vsx-registry-responsibly-rate-limiting)和流量控制，旨在处理持续、大容量的自动化请求，这种模式在 AI辅助和基于云的开发环境中更为常见，其中扩展是通过编程方式安装、更新或配置的。

在运营方面，Open VSX 也正在[转向混合模式](https://blogs.eclipse.org/post/denis-roy/hardening-open-vsx-registry-keeping-it-reliable-scale)。此前，生产工作负载托管在加拿大，混合了 Eclipse 基金会本地基础设施和云服务。主要生产现在在欧洲的 AWS 基础设施上运行，同时在加拿大将维护一个完全运行的本地部署作为由 Eclipse 基金会管理的独立辅助环境。

这种转变减少了对单一地理环境的依赖，并增强了弹性，因为自动化和 AI驱动的工作负载会产生更重、更持续的扩展流量。

## “共享基础设施”

亚马逊的投资引人注目，因为 Kiro（亚马逊基于 VS Code 构建的 [AI原生开发环境](https://thenewstack.io/aws-kiro-testing-an-ai-ide-with-a-spec-driven-approach/)）严重依赖扩展分发来提供[核心功能]。当这些工具安装或更新扩展时，请求通常会流经 Open VSX。

这种动态解释了为什么商业采用者会介入支持注册中心，以及在 AWS 的情况下，在欧洲托管 Open VSX 的主要生产环境。与此同时，Cursor 的财政支持反映了其 AI专注编辑器使用量的扩大，对其相同扩展管道的日益依赖。

> “Open VSX 已发展成为全球开发者生态系统的基础架构……来自领先商业采用者的支持，强化了 Open VSX 作为值得信赖的共享基础设施的地位。”

Eclipse 认为，正是这种共享依赖关系支撑着这些投资。

Eclipse 基金会执行董事 Mike Milinkovich 在一份声明中表示：“Open VSX 已发展成为全球开发者生态系统的基础架构。”“随着 AI原生和基于云的开发平台采用率的加速，我们正在投资，以确保注册中心保持安全、弹性且供应商中立。来自领先商业采用者的支持，强化了 Open VSX 作为值得信赖的共享基础设施的地位。”

对于构建和使用 AI原生编码工具的开发人员来说，这些变化大部分在日常工作中是不可见的。扩展将继续在后台安装和更新。

更具影响力的转变是结构性的：对发布内容的更严格控制、更清晰的流量管理策略以及旨在承受更大需求的混合部署模型。