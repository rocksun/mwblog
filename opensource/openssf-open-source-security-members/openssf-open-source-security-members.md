<!--
title: “道德上的卑劣与短视”：为何开源安全领袖要求企业停止对维护者的“白嫖”行为
cover: https://cdn.thenewstack.io/media/2026/05/15523400-erone-stuff-pzn8n1raiqi-unsplash-scaled.jpg
summary: OpenSSF 迎来 ActiveState 等新成员，旨在应对日益严苛的安全标准。专家严厉批评企业仅利用开源获利而不回馈社区的“吃白食”行为，并强调安全重心应转向开发流程。
-->

OpenSSF 迎来 ActiveState 等新成员，旨在应对日益严苛的安全标准。专家严厉批评企业仅利用开源获利而不回馈社区的“吃白食”行为，并强调安全重心应转向开发流程。

> 译自：["Morally repugnant shortsightedness": Why open source security leaders say companies must stop freeloading on maintainers](https://thenewstack.io/openssf-open-source-security-members/)
> 
> 作者：Adrian Bridgwater

[开源软件安全基金会](https://openssf.org/)（OpenSSF）是 [Linux 基金会](https://thenewstack.io/the-linux-foundation-in-the-age-of-ai/)发起的一项跨行业倡议，致力于实现开源软件的可持续安全。该基金会于周四宣布，已有五名新成员加入。

新加入 OpenSSF 的成员包括 ActiveState、Aikido、Minimus 和 TuxCare，它们以普通成员身份加入。此外，FreeBSD 基金会也以准成员身份加入。

吸引这些新成员加入的动力源于 OpenSSF 所定义的软件生态系统中“两种汇聚的压力”：日益强制化的安全标准，以及将组织和国家统一在这些标准背后的需求。

## 维护全球网络标准

OpenSSF 持续承诺向其成员提供实用资源，帮助他们应对复杂的要求，例如[欧盟《网络韧性法案》](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)及其全球同等法案，包括[《美国国家网络安全战略》](https://bidenwhitehouse.archives.gov/wp-content/uploads/2023/03/National-Cybersecurity-Strategy-2023.pdf)。

[OpenSSF](https://thenewstack.io/openssf-brings-sbom-and-sdpx-to-python/) 总经理 Steve Fernandez 表示：“随着软件供应链的威胁环境变得愈发复杂，对社区驱动的安全标准的需求从未像现在这样迫切。”

Steve Fernandez 指出，OpenSSF 成员的增长以及像 OSS-CRS 这样项目的出现，表明安全是“所有人的重要优先级”，而 OpenSSF 本身正在为开发人员构建更具韧性的软件提供所需的实用工具和指导。

加入的组织将参与工作组和技术倡议，帮助推动 OpenSSF 的战略方向。通过在中立的论坛中协作，所有成员共同支持[开源生态系统](https://thenewstack.io/power-community-open-source/)的长期可持续性。

## 告别看板前的犹豫不决

[Aikido Security](https://www.aikido.dev/) 的创始人兼首席执行官 [Willem Delbare](https://www.linkedin.com/in/willemdelbare/) 告诉 *The New Stack*，软件安全的未来不会在仪表盘（看板）上赢得。相反，Willem Delbare 认为，这场胜利将在代码仓库、包管理器和开发人员工具内部实现。

“攻击者已经意识到，进入生产环境最快的方式是通过软件供应链，”Willem Delbare 说道，“威胁行为者越来越擅长污染依赖项、接管维护者账户、交付恶意提交、暴露凭据，并在深埋于基础设施代码中的地方制造细微变化。”

他指出，Aikido 的重点是将安全控制直接推送到开发人员已经操作的地方：终端、CI/CD 流水线、Git 工作流、容器构建以及最难监控但在被攻破时最危险的底层代码路径。

“这包括 Safe Chain、Zen Firewall、OpenGrep 和 BetterLeaks 等项目，其目标不仅是可见性，而是主动防御，”Willem Delbare 澄清道，“对于在内核、沙箱层或运行时基础设施附近工作的维护者和工程师来说，安全工具必须成为运营基础设施，而不仅仅是另一个合规性检查框。OpenSSF 是少数几个公司可以公开协作解决该问题并建立开发人员真正愿意采纳的标准的地方之一。”

> “许多公司拒绝积极参与他们用来致富的项目的支持或维护……这不仅在道德上令人厌恶，而且是短视的，也是糟糕的商业行为。”
> —— Kat Cosgrove，Minimus 开发者关系负责人。

## 道德上的卑劣与短视

云容器安全保护专家 [Minimus](https://www.minimus.io/) 的开发者关系负责人 [Kat Cosgrove](https://www.linkedin.com/in/katcosgrove/) 告诉 *The New Stack*，尽管开源安全领域已经付出了最大的努力，但外界仍存在很多杂音。她强调这一观点，并认为开源软件是当今我们所构建的几乎所有东西的基石，“这已不再是夸大其词”。

“尽管如此，许多公司仍拒绝积极参与他们用来致富的项目的支持或维护，”Kat Cosgrove 说道，“他们让开源维护者替他们构建和加固产品，却漫不经心地让自己的工程师在缺乏填补空白所需的标准或工具的情况下负责运行。这不仅在道德上令人厌恶，而且是短视的，也是糟糕的商业行为。”

Kat Cosgrove 显然并不害怕点名那些落后者和“吸血者”，她对自己的组织在行业中的“存在意义”非常坚定：即对用户负有“做正确的事”的义务。

她表示：“必须确保开源维护者拥有必要的工具来保护他们的项目，这样你的开发人员才能在生产环境中安全地实施这些项目。”

## 重新夺回仓库责任

将重点转向软件应用程序代码仓库（repo）是目前一个极其重要的主题。[ActiveState](https://www.activestate.com/) 负责人工智能与安全的现场工程经理 [Leslie Pascual](https://www.linkedin.com/in/lesliepascual/) 强调了这一事实，并告诉 *The New Stack*，这不是什么高深学问，即安全必须体现在工程师实际工作的地方。

“简而言之，这意味着安全要出现在代码仓库、构建过程、包工作流、容器、沙箱和命令行中，”Leslie Pascual 说道，“对于内核级和系统工程师来说，这些环节恰好处于现代基础设施的信任边界。在 ActiveState，我们专注于帮助团队实现信任的运营化，无论是通过安全构建、来源证明，还是 BOM 和 VEX 详情。”

Leslie Pascual 和其他人的共同感受是，目前正有一种扎实、切实的努力在进行，旨在构建软件工程师真正能用的工作流。这一真诚的承诺也得到了 [TuxCare](https://tuxcare.com/) 首席执行官 Igor Seletskiy 的回应。TuxCare 以[无需重启的漏洞补丁](https://tuxcare.com/blog/rebootless-patching-explained/)、符合合规要求的 Linux 安全、漏洞情报和长期安全服务而闻名。

Igor Seletskiy 告诉 *The New Stack*，漏洞和供应链攻击改变了依赖开源的含义，而人工智能正在加速这两个渠道的风险。

“开发人员现在拉取的每一个包都带有一个悬而未决的问题：是谁构建了它、里面有什么，以及它是否值得信任，”Igor Seletskiy 说道，“回答这个问题需要整个生态系统的协同工作，没有任何一家公司能单独完成。这就是我们加入 OpenSSF 的原因。”

作为 [FreeBSD 基金会](https://freebsdfoundation.org/)的执行董事，[Deb Goodkin](https://www.linkedin.com/in/deb-goodkin-b282924a/) 坚持该组织的使命，即通过研究和教育支持 [FreeBSD](https://www.freebsd.org/) 开源操作系统。

配合此次强调的新成员身份，她表示：“作为全球数字基础设施的关键组成部分，我们相信 FreeBSD 必须参与到塑造开源未来的安全讨论中。加入 OpenSSF 将使我们能够与他人合作，共同保护世界所依赖的软件。”

## 值得信赖的运营基石

在相关公告中，OpenSSF 还在本周于明尼阿波利斯举行的 [OpenSSF 北美社区日](https://events.linuxfoundation.org/openssf-community-day-north-america/)期间指出了其他技术资源，包括 Python 安全编码、首批 OpenSSF 大使，以及加入基金会沙箱的新项目（如 OSS-CRS）。

OpenSSF 广泛宣称，其努力通过解决现代网络安全中的技术、法律和人为因素，确保开源始终是数字创新的可信基础。