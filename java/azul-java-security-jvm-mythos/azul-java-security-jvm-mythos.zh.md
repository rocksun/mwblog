[Azul Systems](azul.com) 正在提供一项免费的 [Java 虚拟机 (JVM)](https://thenewstack.io/how-do-javas-virtual-threads-help-your-business/) 漏洞风险评估，旨在 AI 辅助的攻击者破解系统之前揭示 Java 运行时的暴露风险。不过，该公司对于威胁的描述在很大程度上依赖于 Anthropic 尚未公开验证的 [Mythos](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) 模型作为其核心论据。

Azul 是一家总部位于加利福尼亚州桑尼维尔的 Java 运行时供应商，该风险评估工具主要针对那些对其 Java 资产缺乏全面[可观测性](https://thenewstack.io/devops/)的 [DevOps](https://thenewstack.io/devops/) 和 [SecOps](https://thenewstack.io/how-azure-copilots-new-agents-automate-devops-and-secops/) 团队。其工作原理如下：该工具通过扫描网络来识别 JVM 实例——包括标准资产发现工具通常会遗漏的嵌入式和非托管运行时。据该公司称，扫描完成后，它会返回一份基于 CISA 已知被利用漏洞 (KEV) 目录和美国国家漏洞数据库进行交叉引用的优先级修复路线图。

当然，Azul 自身也制造 JVM 并出售相关支持服务，而这项免费扫描本质上是一种潜在客户挖掘策略，旨在将用户转化为 Azul Core 订阅用户。

这种策略主要针对 Azul 仅含安全修复的“关键补丁更新”(CPU)，Azul 产品管理高级总监 Eric Costlow 向 *The New Stack* 表示，这是唯一的 OpenJDK 发行版，它只包含安全修复，不包含任何新功能或捆绑的错误补丁，而 [AWS Corretto](https://www.theserverside.com/news/252452738/Amazon-Corretto-extends-OpenJDK-support) 或 [Eclipse Temurin](https://thenewstack.io/why-bloomberg-chose-vendor-neutral-java-over-big-tech/) 并非如此。他认为，对于客户而言，其价值主张在于更新长期运行的 Java 资产时，系统崩溃的风险更低。

“人们长时间不更新 JVM 的原因之一是担心搞坏系统，”Costlow 说，“所以他们会想，‘没坏就别动它’。Core 提供的是一个只包含安全补丁的 Java 版本——它的作用仅是修复安全漏洞。应用这种仅含安全补丁的版本导致应用程序崩溃的风险非常低，因为它只修复安全漏洞。”

这就是其区别于 Corretto、Eclipse Temurin 和其他 OpenJDK 发行版的宣传点。

“如果你使用 Corretto 或 Eclipse JVM，他们做得很好，”Costlow 说，“但他们的构建中包含了所有东西。任何变化都会包含在内。假设有 1% 的概率导致崩溃——你更新了 100 个应用程序，其中一个就会崩溃。我们的崩溃率可能只有 0.1% 左右，因为我们不做那些额外改动。”

## AI 威胁论点

核心安全论点在于，AI 工具已将漏洞利用的平均时间从几个月缩短到几天甚至几小时，使得未打补丁的 Java 资产比 18 个月前危险得多。Costlow 将其描述为 AI 降低了发现漏洞和武器化的门槛。

“你可以构建爬虫来寻找较旧的 Java 版本，因为你可以通过许多特征来识别它们，”他说，“而且对于漏洞利用——过去你可能会说，‘我有一个针对特定版本 [Spring](https://thenewstack.io/production-worthy-ai-with-spring-ai-1-0/) 的漏洞，但它只能在特定场景下工作’——AI 已经让这些漏洞的泛化变得容易多了。这些东西更容易被发现，也更容易被攻击。很遗憾。”

在[一篇博文](https://www.azul.com/blog/get-your-java-estate-ready-for-the-growing-agentic-ai-threat/)中，Platform Core 产品营销总监 Dana Crane 提供了研究来支持这一观点。一份 [2024 年伊利诺伊大学厄巴纳-香槟分校的研究](https://arxiv.org/pdf/2404.08144)发现，在给定适当的基架的情况下，GPT-4 能够自主利用 87% 的已知高危 CVE，且无需人工干预，平均每次成功利用成本约为 8.80 美元。该小组的后续研究显示，AI 代理团队在攻击零日漏洞时的成功率为 53%。最近，一个名为 ARTEMIS 的 AI 系统在一个包含 8,000 台主机的真实企业网络中，在与人类渗透测试人员的对抗中获得了第二名，其发现有效漏洞的成本为每小时 18 美元，而其胜过的人类测试员成本为每小时 60 美元。

更难评估的是 Azul 的核心主张，即极度依赖 Anthropic 的 Mythos 模型——这是一个尚未公开发布的前沿 AI 系统，Anthropic 仅将其限制在少数受信任的组织内。

Azul 的新闻稿指出：“Anthropic 的 Claude Mythos 表明 AI 可以自主发现以前未知的漏洞，并大规模生成可执行的漏洞利用路径。”

此外，Azul 首席执行官 Scott Sellers 在一份声明中表示：“Anthropic 的 Mythos 表明，AI 现在可以自主发现并武器化漏洞——包括那些在人类审查下存活了数十年的缺陷。”

Azul 的常见问题解答进一步指出，“Mythos 级能力迅速脱离其预期限制”是加速打补丁的原因。然而，当在简报中被问及公司是否真正使用 Mythos 测试过 JVM 漏洞时，Costlow 指出他无法访问该模型。“这受到了许多政府层面限制的保护，”他告诉 *The New Stack*，“它现在仅供特定组织使用。”

换句话说，Azul 正在使用一个它并未测试过，且除少数经过审查的组织外没有人使用过的模型，作为其威胁叙事的核心。

## 评估工具实际发现的内容

该工具本身是一个网络扫描器，Azul 称其运行只需几天时间，且不会产生性能影响。它可以识别整个堆栈中的 JVM 版本和时长，包括应用服务器、无服务器容器和数据库。

输出包包括一个按风险等级、发布者和 Java 版本细分的仪表板；与真实世界威胁数据交叉引用的 KEV 和 CVE 暴露分析；生命周期结束的运行时识别（生产环境中 Java 5、6 和 7 实例，Crane 指出这“比大多数 IT 领导者想象的要普遍得多”）；以及一份补丁时效性差距报告，显示已部署实例距离当前的 CPU 基准有多远。

监管层面则针对 PCI-DSS、SOX、HIPAA、DORA、NERC CIP 和 FedRAMP。这些框架要求对已部署的软件版本有明确的可见性，并记录补丁历史。

“PCI DSS 领域中的许多人本应修补他们的 JVM，但却没有，”Costlow 说，“如果你八年没打补丁，它真的会累积起来。我称之为 CDE 海啸。”

与此同时，Crane 表示：“典型的评估揭示出，少数几个 Java 版本——通常只有两三个——占据了企业资产中大部分的风险。这使得缓解措施比最初看起来要容易处理得多。”

该评估可通过 Azul 及其选定合作伙伴免费获取，网址为 azul.com/jvm-vulnerability-risk-assessment。