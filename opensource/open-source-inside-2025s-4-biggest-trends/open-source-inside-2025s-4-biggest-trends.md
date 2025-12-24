<!--
title: 开源风向标：2025年四大趋势深度剖析
cover: https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1.png
summary: 2025年开源：AI主流化，许可争议引分叉。项目资金匮乏，供应链安全风险增。需企业资助与强化安全。
-->

2025年开源：AI主流化，许可争议引分叉。项目资金匮乏，供应链安全风险增。需企业资助与强化安全。

> 译自：[Open Source: Inside 2025's 4 Biggest Trends](https://thenewstack.io/open-source-inside-2025s-4-biggest-trends/)
> 
> 作者：Steven J. Vaughan-Nichols

人工智能在2025年大放异彩，但同时也有许多其他发展和担忧。

2025年最重大的开源故事围绕着人工智能、许可/治理、安全以及“商业开源”商业模式的转变。我们开始吧，好吗？

## 1. 开源人工智能走向主流

尽管大部分资金流向了专有模型，但开源人工智能数据集、编排框架、评估工具和安全防护栈都取得了进展。

[Common Corpus](https://huggingface.co/blog/Pclanglais/common-corpus) 等开源人工智能项目，以及由 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) 的人工智能与数据组托管的 [数十个 AI 项目](https://lfaidata.foundation/projects/)，使我们能够使用社区基础设施进行生成式人工智能，而不是仅仅依赖专有API，从而使开放人工智能栈成为企业和用户的严肃选择。

尽管 [开源人工智能的定义仍有争议](https://thenewstack.io/what-is-open-source-ai-anyway/)，并且很少有 AI 项目能完全符合 [开放源代码促进会 (OSI) AI 定义](https://thenewstack.io/the-open-source-ai-definition-is-out/) 的严格要求，但 [人工智能仍然建立在开源软件的基础之上](https://www.zdnet.com/article/why-open-source-is-the-cradle-of-artificial-intelligence/)。关于开放权重、数据和训练代码的争论将继续，但即使是最专有的 [大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms/) 也不可能没有开源程序而存在。

[Agentic AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/)，完全归功于开源。为了编排我们最新一代的 AI 代理，我们正在使用多个程序。

在游戏的早期阶段，其中最重要的似乎是 [模型上下文协议 (MCP)](https://modelcontextprotocol.io/)。这是一个开放标准和开源实现，用于将代理统一连接到工具、文件、数据库和其他系统。

MCP 正日益成为许多代理和 IDE 助手的“底层管道”，并且有 [大量的开源 MCP 服务器和工具包](https://thenewstack.io/10-mcp-servers-for-frontend-developers/)，允许任何兼容的代理框架接入相同的工具。

MCP 并非唯一正在加速发展的 Agentic AI 中间件：

## 2. 关于“开放”与“源代码可用”许可的争论持续激烈

[Linux 基金会八月发布的一份报告](https://www.linuxfoundation.org/research/2025-state-of-commercial-open-source) 显示，在过去25年里，获得风险投资支持的商业开源公司表现优于同类闭源供应商。

这份报告，连同 [OSI 四月调查](https://opensource.org/blog/key-insights-from-the-2025-state-of-open-source-report) 中96%的组织维持或增加开源软件使用的数据，巩固了商业开源作为构建软件的默认方式的地位。

这些报告共同推动了更多资金、更多并购以及围绕关键开源项目的更多“开放核心加服务”策略。

当然，我们知道这一点。毕竟，2024年哈佛商学院的一项研究已经表明，[96%的商业程序都依赖开源](https://www.library.hbs.edu/working-knowledge/open-source-software-the-nine-trillion-resource-companies-take-for-granted)，并且开源代码的总价值高达8.8万亿美元。但这仍然无法阻止那些 [将开源作为软件开发模型与商业模式混淆](https://opensourcewatch.beehiiv.com/p/open-source-not-business-model-never) 的公司；它从来都不是商业模式，也永远不会是。

因此，在2025年，我们看到更多公司从 [开源转向“假开源”](https://www.theregister.com/2024/04/12/linux_foundation_opinion/)。例如，[ScyllaDB](https://www.scylladb.com/?utm_content=inline+mention) 团队于2024年12月宣布将 [转向单一的“ScyllaDB Enterprise”](https://www.scylladb.com/2024/12/18/why-were-moving-to-a-source-available-license/) 版本，并采用源代码可用许可。

在库层面，也出现了一些之前宽松许可的项目悄然转向源代码可用、付费商业使用条款的高调案例，例如 [Fluent Assertions .NET 测试库](https://devclass.com/2025/01/16/another-open-source-project-shifts-to-restrictive-license-fluent-assertions-following-xceed-partnership/) 在今年一月从 Apache-2.0 转向了专有的源代码可用许可，并按开发者收费。

然后，还有 DevOps 程序 [Puppet](https://puppet.com/?utm_content=inline+mention)。尽管 Puppet 的核心代码库仍采用 Apache 2.0 开源许可，但其商业母公司 [Perforce](https://www.perforce.com/) 改变了官方构建版本的发布和许可方式。

变化在于，由 [Puppet/Perforce 构建的新版“强化”二进制文件和软件包现在从私有仓库发布](https://www.puppet.com/blog/open-source-puppet-updates-2025/)。[Puppet Core 最终用户许可协议 (EULA)](https://forge.puppet.com/eula) 提供了一个最多25个节点的免费层级，超出此范围则需要商业许可。这实际上使 Puppet 成为一个源代码可用程序，尽管代码在技术上仍然是开放的。

Puppet 的结果与我们看到其他此类尝试关闭曾是开源的项目一样：不满的程序员分叉了该项目。这个 [分叉被称为 OpenVox](https://thenewstack.io/openvox-the-community-driven-fork-of-puppet-has-arrived/)。

这些分叉项目，包括带有其分叉 [OpenSearch](https://thenewstack.io/opensearch-how-the-project-went-from-fork-to-foundation) 的 Elasticsearch，带有 [Valkey](https://thenewstack.io/navigating-the-path-from-redis-to-valkey) 分叉的 [Redis](https://redis.com/?utm_content=inline+mention)，以及带有 [OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next) 分叉的 Terraform，[都取得了一定的成功](https://thenewstack.io/what-happens-to-relicensed-open-source-projects-and-their-forks/)。这四个分叉都获得了可观的关注，但规模和对“成功”的定义各不相同。

[OpenSearch 似乎是最成功的](https://www.linuxfoundation.org/press/opensearch-software-foundation-marks-1-year-anniversary-with-community-growth-agentic-ai-and-hybrid-search-enhancements/)。它报告了强劲的增长，包括两位数、同比增长78%的下载量，以及 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)、Canonical、[SAP](https://www.sap.com/index.html?utm_content=inline+mention) 和 Uber 等主要成员的名单。

[Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") 也被证明很受欢迎。[最新版本 Valkey 9](https://thenewstack.io/valkey-9-0-debuts-multidatabase-clustering-for-massive-scale-workloads/) 据报道比最新版本的 Redis 快得多。特别是，Valkey 用户报告称，它在原始吞吐量方面始终领先于可比较的 Redis 版本，尤其是在 Valkey 的多线程 I/O 和缓存预取发挥作用的更大、内存密集型工作负载上。

虽然 OpenSearch 和 Valkey 都已超越其母项目，但 Terraform 与 OpenTofu 则另当别论。人们仍然认为 [OpenTofu 和 Terraform 仅在许可上有所不同](https://infisical.com/blog/terraform-vs-opentofu/)。然而，在过去的几个月里，这种情况正在发生变化，因为 OpenTofu 于四月 [加入了](https://thenewstack.io/opentofu-joins-cncf-new-home-for-open-source-iac-project/) [云原生计算基金会](https://cncf.io/?utm_content=inline+mention)，并正在更多地走自己的道路。[最新版本现在包括状态加密](https://spacelift.io/blog/opentofu-vs-terraform#differences-between-opentofu-and-terraform)，这是 Terraform 社区多年来一直想要的功能，以及早期变量评估。

最后，OpenVox 继续将自己定位为“软分叉”。其董事希望它与 Puppet 保持100%兼容，以便它可以作为 Puppet 部署的直接替代品。然而，这似乎已不再可能，正如 OpenVox 的领导者 Gene Liverman 所写，“[我们无法再保证我们的模块能与 Puppet Core](https://www.linkedin.com/pulse/unsupportable-path-gene-liverman-wngje/) 或 Puppet Enterprise 兼容。”

从项目维护者的角度来看，Perforce 正在破坏兼容性。然而，目前 OpenVox 本质上是一个健康的、社区驱动的救生艇，而不是一个全面的 Puppet 替代舰。

## 3. 开源项目资金匮乏

尽管我们都依赖开源，但太多项目仍资金不足。还有一些项目，例如 [NET 6，仍然很受欢迎](https://thenewstack.io/herodevs-throws-net-6-users-a-post-deprecation-lifeline/)，但其维护者已停止支持它们。用户该怎么办？

这不是一个新问题。早在2021年，一家安全公司 [Tidelift](https://tidelift.com/?utm_content=inline+mention)，也为开源维护者提供资金支持，发现 [46%的开源项目维护者根本没有报酬](https://www.zdnet.com/article/hard-work-and-poor-pay-stresses-out-open-source-maintainers/)。同样糟糕的是，即使那些获得报酬的人，也只有26%的人每年工作收入超过1000美元。

情况并未改善。事实上，它们变得更糟了。在2024年，Tidelift 的最新结果显示，现在 [60%的开源维护者是无偿的](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/)。

正如 [由10个开源基金会签署](https://openssf.org/blog/2025/09/23/open-infrastructure-is-not-free-a-joint-statement-on-sustainable-stewardship/) 并于9月发表的一封公开信所指出的，“这些 [开源] 系统中的大多数都在一个危险脆弱的前提下运行：它们通常以依赖善意而非将责任与使用对齐的机制来维护、运营和资助。”

因此，根据公开信，“少数组织承担了大部分基础设施成本，而绝大多数大规模用户，包括产生需求并获取经济价值的商业实体，在不为其可持续性做出贡献的情况下消费这些服务。”

我一直在报道的一个具体例子是，[所有通过互联网观看视频的人都在使用的 FFMpeg，其资金状况非常糟糕](https://thenewstack.io/ffmpeg-to-google-fund-us-or-stop-sending-bugs/)，即使亚马逊、谷歌和 Netflix 等大公司都依赖它的代码。还有许多其他类似的项目。这种情况不能继续下去。

答案是，公司必须——必须——开始为关键任务的开源项目提供资金支持。与这些项目停摆或遭受重大安全问题所造成的损害相比，这样做的成本微乎其微。

## 4. 开源供应链比以往任何时候都更脆弱

2024年，xz 数据压缩库代码 [被恶意软件故意感染](https://thenewstack.io/malicious-code-in-linux-xz-libraries-endangers-ssh/)，差点在 [Fedora](https://www.fedoraproject.org/)，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的社区 Linux 中植入后门。如果成功，它可能会最终出现在 Red Hat Enterprise Linux (RHEL) 及其克隆版本中。

这将导致迄今为止最大的 Linux 安全灾难。我们躲过了一劫。

不幸的是，开源软件供应链安全正受到持续、大规模的攻击，以 npm 和 PyPI 为目标的攻击活动正在升级。

2025年的几项高影响活动集中在破坏开源包生态系统，尤其是 npm。

11月，Wiz、Aikido 和其他研究人员详细描述了“Shai-Hulud 2.0”恶意 npm 包的浪潮，这些包从使用与主要 SaaS 和云工具相关的流行库的环境中窃取了开发者和 CI/CD 凭证。

作为攻击活动的一部分，数万个恶意仓库被创建。[GitLab](https://about.gitlab.com/?utm_content=inline+mention) 的漏洞研究团队还报告了另一起广泛的 [npm 供应链攻击，该攻击窃取了](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/) GitHub、npm 和主要云的凭证，并通过感染受害者拥有的其他软件包进行传播。

这些并非孤立事件。2025年的行业威胁报告描述了软件供应链攻击的全面激增，10月份创下月度新高，开源生态系统在目标中占据突出位置。

[Palo Alto Networks](https://www.paloaltonetworks.com/cloud-security?utm_content=inline+mention) 的 [Unit 42](https://unit42.paloaltonetworks.com/) 和其他研究团队的分析指出，攻击者越来越倾向于通过破坏维护者账户和发布管道而不是核心源代码仓库，因为这种方式可以大规模地悄悄地毒害受信任的软件包。

[ReversingLabs 在3月份发布的一项研究](https://www.reversinglabs.com/sscs-report) 报告称，虽然观察到的开源恶意软件包有所下降，但风险已转向泄露的开发者密钥和构建时暴露。

研究人员在检查流行的 npm、PyPI 和 RubyGems 组件时，继续在企业中广泛使用的二进制文件中发现硬编码凭证、弱应用程序加固和暴露的数据。这种错误在80年代我首次在生产软件中遇到时就很愚蠢，而今天更是不可原谅。

更糟糕的是，[JFrog](https://jfrog.com/?utm_content=inline+mention) 和 [Veracode](https://www.veracode.com/) 等安全公司报告称，爆炸式的依赖关系图、更快的发布周期以及对开源库的大量重用意味着一个恶意或脆弱的软件包可以在几天内波及数千个下游应用程序。

这种密集的互联性使得2025年以 npm 为重点的攻击活动的影响范围比许多早期开源事件要大得多，尤其是当目标库出现在20%到30%的扫描云环境中时。

我们能做些什么呢？我们必须更广泛地采用 [软件物料清单 (SBOM)](https://thenewstack.io/sboms-sboms-everywhere/)、[软件工件供应链级别 (SLSA)](https://thenewstack.io/enhance-your-sbom-success-with-slsa/) 风格的证明，以及来自开放源代码软件基金会生态系统的工具来跟踪开源组件的来源和完整性。

OpenSSF 及其合作伙伴强调了诸如用于无密钥签名的 [Sigstore](https://thenewstack.io/need-to-sign-your-code-and-havent-a-clue-sigstore-can-help/)、用于自动化项目风险评估的 [Scorecard](https://openssf.org/projects/scorecard/) 和 [开源项目安全基线](https://baseline.openssf.org/) 等举措，这些旨在为维护者和消费者提供更清晰的安全预期。

每年，我都会告诉人们，他们必须更认真地对待安全问题。最近，随着开源供应链违规行为变得越来越普遍，我一直在说，你必须确保供应链中的代码既安全又由值得信赖的人编写。

展望未来，我只能加倍强调这些警告。我们过去几年已经发生了严重的安全漏洞。你还记得：[Solarwinds](https://thenewstack.io/solarwinds-the-worlds-biggest-security-failure-and-open-sources-better-answer/)、JetBrains [TeamCity](https://www.wiz.io/blog/jetbrains-teamcity-authentication-bypass-vulnerabilities-cve-2024-27198-cve-2024-27199) 和 [Apache Log4j](https://thenewstack.io/one-year-of-log4j/) 都应该迅速浮现在脑海中。尽管它们很糟糕，但如果我们不更认真地对待开源供应链安全问题，更糟糕的安全灾难还在前方。