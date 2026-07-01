专注于开发者的网络安全平台 [Aikido Security](https://www.aikido.dev/) 宣布已收购 [Root](https://www.root.io/)。该公司能将已知漏洞的补丁直接应用到团队正在使用的开源包版本中，而无需强迫用户升级到更新的版本。

这笔 7000 万美元的交易将 Root 的补丁技术整合进了一个名为“Aikido Libraries”的新产品中。同时，Aikido 还承诺，将为 [公司支持](https://www.npmjs.com/package/@aikidosec/safe-chain) 的所有生态系统（如 [npm](https://www.aikido.dev/protect/safe-chain)、PyPI 和 Maven）中的关键、活跃漏洞提供免费的反向移植（backport）补丁。

Aikido 成立于 2022 年，提供一个涵盖代码扫描、云安全、供应链恶意软件检测和 [AI 驱动的渗透测试](https://thenewstack.io/aikido-self-securing-software/) 的统一平台。这家比利时公司于今年 1 月达到独角兽地位，以 [10 亿美元的估值筹集了 6000 万美元](https://www.aikido.dev/blog/aikido-funding-series-b)。目前，该公司在 [一年多一点的时间里](https://www.aikido.dev/blog/allseek-and-haicker-are-joining-aikido) 已经进行了第四次 [收购](https://www.aikido.dev/blog/trag-is-now-part-of-aikido-secure-code-at-ai-speed)，旨在缩小漏洞发现与修复之间的差距。

Root 的前身是成立于 2021 年的 Slim.AI，该项目基于开源的 DockerSlim 项目构建。该公司在 [2022 年完成了 3100 万美元的 A 轮融资](https://www.insightpartners.com/ideas/slim-ai-closes-31-million-series-a-to-automate-best-practices-in-software-supply-chain-security-for-cloud-native-applications/)，随后更名为 Root，并将业务重心从容器优化转向了自动化漏洞修复。

## 解决紧迫缺陷的方案

Aikido 的免费反向移植承诺特别适用于 [CISA](https://www.cisa.gov/) 已知漏洞（[KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)）目录中的漏洞——这是一份相对较短的、被确认在现实中已被利用的漏洞清单。虽然这只是所有已披露漏洞的一小部分，但却是最有可能造成实际损害的部分。

这种承诺在收购成本需要辩护时也可能会消失。Aikido Security 的联合创始人兼首席增长官 Madeline Lawrence 告诉 *The New Stack*，这种情况不会发生，因为决定清单内容的是 CISA，而不是 Aikido。这些免费修复补丁与 Aikido 现有的付费产品并行，公司正押注于另一项增长趋势：企业在合规性方面面临越来越大的压力，要求清除常见的漏洞和披露（CVE），无论某个缺陷是否已经被武器化。

“这与我们的付费功能是分开的，付费功能涵盖了监管机构现在要求企业修复的长尾 CVE，而不仅仅是那些被活跃利用的漏洞，这方面的需求正在爆炸式增长，”Lawrence 说。“两者都出自同一个‘工厂’。没有单独的预算项目来削减免费修复的开支，因为产生这些补丁的工作与我们的付费客户所依赖的工作是一样的。”

> “该行业仍困在分诊（triage）阶段，拿着一长串 CVE 名单，争论首先修复哪一个。”

Root 的首席执行官 Ian Riopel 将行业一直回避的选择定义为：要么将修复方案锁定在供应商自己的生态系统中，要么将其交还给需要这些方案的项目手中。

“该行业仍困在分诊阶段，拿着一长串 CVE 名单，争论首先修复哪一个。或者更糟的是，告诉团队扔掉现有的镜像，用别人的从头开始，”Riopel 在一份声明中说。“我们构建 Root 是为了跳过这些争论，直接在原地解决问题。这是在封闭花园（walled gardens）和对开源的真正支持之间做选择。我们选择了开源。”

> “这是在封闭花园和对开源的真正支持之间做选择。我们选择了开源。”

## 安全领域的混战

此次收购正值 AI 和网络安全领域动荡不安之际。上周五，[Linux 基金会推出了 Akrites](https://thenewstack.io/akrites-open-source-vulnerability-coordination/)，这是一个由 Anthropic、Google、Microsoft 以及约 20 个组织支持的协调漏洞披露机构，其成立很大程度上是为了应对 AI 工具现在能以多快的速度在开源代码中发现缺陷。此前，Anthropic 特别经历了 [紧张的几周](https://thenewstack.io/anthropic-fable-mess-explained/)：美国政府在 6 月份因研究人员称发现利用模型辅助网络攻击的方法而 [暂停了对其 Fable 5 和 Mythos 5 模型的访问](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/)，随后在当月底恢复了对关键基础设施组织的访问。

Lawrence 表示，时间上的巧合是偶然的。她说，Root 的交易酝酿已久，建立在两家公司 [2025 年中期达成的现有合作关系](https://www.aikido.dev/blog/aikido-x-root-io-harden-your-containers-without-the-headaches) 基础之上，该合作将 Root 的强化容器镜像引入了 Aikido 现有的 Autofix 产品中。

尽管如此，Lawrence 并没有忽视 AI 给双方带来的更广泛压力。

“这个行业在发现漏洞方面已经非常擅长，但在修复方面却一直停滞不前，而 AI 是第一个让修复侧能够以同样速度前进的技术，”Lawrence 说。“先进的模型也使得发现和利用开源漏洞变得更容易、更便宜，这也是当前紧迫感的部分来源。读取代码以修复缺陷的同一能力同样可以读取代码来利用缺陷，这正是为什么每个补丁在发布前都经过人工验证的原因。”