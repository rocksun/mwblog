**企业 [Java](https://thenewstack.io/introduction-to-java-programming-language/) 公司 Azul** 于周三宣布推出 Azul Intelligence Cloud AI 助手。该技术的推出是为了应对全行业发出的警示：如今 AI 已成为威胁行为者的“力量倍增器”。

[Azul](https://www.azul.com/) 服务是一个自然语言查询接口，允许软件工程团队查看[安全风险](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/)和许可证侵权行为隐藏在其动态生产 Java 资产中的位置。该助手提供的答案“立足于实时运行时数据”，因此它取代了那些生成后一天比一天不准确的静态报告。

## 代码扫描报告过时的速度有多快？

Azul 表示，“大多数 IT 和工程团队”仍然使用静态 IT 和软件资产管理 (ITAM/SAM) 报告以及描述特定时间点的代码扫描报告来管理 Java 风险。该公司坚持认为，这些报告“在生成当天是准确的，之后则会越来越不准确”，这通常是因为 Java 虚拟机 (JVM) 在报告范围之外被启动、打补丁、漂移和退役。

Azul 联合创始人兼 CEO [Scott Sellers](https://www.azul.com/leadership/scott-sellers/) 表示：“多年来，企业一直通过构建仪表盘和报告来了解其 Java 资产中实际运行的内容，但当报告得到妥善总结和审查时，它所描述的风险往往已经发生了变化。过去，这是一个生产力问题。现在，AI 可以在几小时而不是几周内发现并利用漏洞，这就成了一个商业风险——涉及安全、合规性以及在审计中显现出来的许可证暴露问题。”

> “既然 AI 可以在几小时而不是几周内发现并利用漏洞，这就成了一个商业风险……”

Azul Intelligence Cloud AI 助手允许软件团队用通俗语言直接提出问题，并获得基于当时生产环境中实际运行情况的答案，同时还可以查询历史信息以进行进一步分析。

## 利用漏洞的鸿沟正在缩小

在企业将业务关键型工作负载与 AI 服务一起运行在 Java 上的地方，Azul 表示，其实际影响是：[常见漏洞和披露](https://thenewstack.io/how-linux-kernel-deals-with-tracking-cve-security-issues/) (CVE) 条目披露与其被利用之间的差距正在缩短。

该公司援引了 Anthropic 的 Mythos 和 OpenAI 的 Aardvark 等自主发现现实世界漏洞的 AI 模型，并指出云安全联盟 (Cloud Security Alliance) 2026 年 4 月的一份[白皮书](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_whitepaper_collapsing-exploit-window-ai-mtte_20260411-csa-styled.pdf)（被列为非官方 AI 辅助研究）表明：“虽然历史上组织平均需要 32 天来为已知漏洞应用补丁——这一窗口期曾经大致对应于攻击开始前可用的时间，但在 2025 年，平均利用时间窗口已骤降至约 5 天。”

Azul 重点介绍了其 Intelligence Cloud 服务，该服务为工程师提供了关于其 Java 资产的两条“持续更新”的记录：[JVM Inventory](https://www.azul.com/products/components/jvm-inventory/)（一个在任何地方——本地、云端或容器中运行的每个 JVM 实例的实时目录）和 [Code Inventory](https://www.azul.com/products/components/code-inventory/)（生产中实际执行的代码与仅配置的代码的运行时记录）。全新的 AI 助手在两者之上引入了一个利用 LLM 模型的对话层。

软件工程师可以提出以下问题：

* “哪些 JVM 运行的 Java 版本不是最新更新？”
* “现在生产环境中哪里在运行 Oracle Java？”
* “过去四个季度有哪些代码没有运行且可以安全移除？”

在其公告的 [FAQ](https://www.azul.com/newsroom/azul-launches-ai-assistant-that-tells-it-and-security-teams-where-java-licensing-and-security-risk-is-hiding/) 部分中，Azul 暗示迁移后的 JVM “漂移很常见”，这通常是由回滚、被遗忘的节点、影子部署或各种未更新的脚本和进程引起的，如果不引起安全风险，也会重新引入 Oracle Java 运行时，从而暴露出合规性和许可证风险。

## Java 运行时安全市场的格局

就哪些其他供应商在 Java 运行时分析和安全市场运营而言，有不止少数的常客。[Contrast Security](https://www.contrastsecurity.com/solutionbrief/contrast-agent-deployment) 以其 [JVM 代理](https://docs.contrastsecurity.com/en/agents.html)和应用内字节码插桩而闻名。[Dynatrace](https://docs.dynatrace.com/docs/secure/application-security/vulnerability-analytics) 提供运行时漏洞分析，作为其核心可观测性平台的延伸，该平台随附用于 Java 漏洞函数和 JVM 级字节码插桩代理的 OneAgent 监控。

通过被 HP、Micro Focus 以及现在的 [OpenText](https://www.opentext.com/products/cybersecurity-cloud) 收购，[Fortify](https://www.microfocus.com/en-gb/media/data-sheet/security-fortify-software-security-center-ds-a4.pdf) 依然以其静态和动态应用测试服务而闻名，包括旨在监控执行期间 Java 工作负载的运行时应用自我保护 (RASP) 代理 Fortify Application Defender。作为泰雷兹 (Thales) 的一部分，[Imperva](https://www.imperva.com/learn/application-security/runtime-security/) 针对 Java 和 .NET 应用的运行时安全跨越了从简单访问控制到复杂异常检测算法的范围，不过据报道 Imperva 已将其独立的 RASP 产品走上了停售路径。然后是 [Datadog](https://www.datadoghq.com/product/apm/)，其应用性能监控 (APM) 旨在从浏览器和移动应用到后端服务和数据库，提供代码级分布式追踪。

> “运行时上下文对于理解生产环境中的真实风险至关重要。”

这无疑是一个竞争激烈的市场，那么现在那些过时的静态报告究竟有多大问题？

Datadog 安全倡导负责人 [Andrew Krug](https://www.linkedin.com/in/andrewkrug/) 告诉 *The New Stack*，大多数时间点库存扫描的缺点在于它们“并不总是能代表”运行时环境。

Krug 表示：“运行时上下文对于理解生产环境中的真实风险至关重要。即使在最成熟的软件开发生命周期 (SDLC) 流程中，生成静态软件物料清单 (SBOMs) 的工具也可能会被绕过（即规避或颠覆），从而部署功能。此外，SDLC 之外的传统漏洞管理流程可能会在 CI/CD 流程之外更改版本，无意中加剧问题，并通过绕过已知良好的护栏（如依赖冷却期）引入额外风险。”

> “即使在最成熟的软件开发生命周期 (SDLC) 流程中，生成静态软件物料清单 (SBOMs) 的工具也可能会被绕过……从而部署功能。”

Krug 进一步建议称，Datadog 现在看到对已知漏洞的自动化随车攻击“呈不断上升趋势”，在许多情况下“特别是 Java”。

Krug 澄清说：“攻击过去会被专门或泛泛地添加到扫描器中，并且扫描是无差别地针对目标的。LLM 使得为新漏洞添加支持的成本变得更低。然而，这也使得个人研究人员/黑客更容易拥有自己的自定义规则集。”

> “LLM 使得为新漏洞添加支持的成本变得更低。”

他建议，这一事实使得趋势比“哦，有人在 FFUF 中为 CVE-2026-whatever 添加了支持”更难解读，因此今天许多攻击的目标没有改变。攻击者正在寻求进行横向移动、建立持久性，并且自动化通常会寻找凭据来利用以实现这一目标。

**注意：** ([Fuzz Faster U Fool](https://hackviser.com/tactics/tools/ffuf)) 是一个极其快速的 Web 应用程序模糊测试工具（用 Go 语言编写），安全测试人员用它来发现隐藏的文件、目录和端点。

## 死代码；这真的是个“大问题”

上述在 Azul 市场中运营的竞争对手名单（可以说）是真实存在的商业许可证和安全风险的实质性证据，这些风险存在于 Java 代码、冗余 JVM 和无根据（或者更有可能只是未被追踪的）Java 组件碎片被任其自由游荡的地方。Azul 本身指出，这里存在真正的维护开销需要解决，因为“未使用的死代码仍然会被调整、测试并通过每一次迁移携带”，通常是因为没有人能够评估将其删除是否安全。

Java 资产越大，暴露面显然就越大。但这同时也意味着，时间点报告在捕捉这些暴露面方面变得越来越不可信，无法在它们成为事件、审计发现或泄露之前将其拦截。

专职的合规官可能会喜欢这些工具的更广泛部署，尽管该角色本身现在可能属于 DevSecOps 或平台工程团队，或者两者兼而有之。

无论部署了哪个 JVM、来自哪个供应商、在其上运行的应用有多旧或多大，Azul Intelligence Cloud AI Assistant 都能正常工作。JVM Inventory 和 Code Inventory 随着时间的推移保留了组件和代码使用历史记录，因此 AI 助手可以根据当前和过去在生产中实际运行的代码、JVM 和应用进行推理。