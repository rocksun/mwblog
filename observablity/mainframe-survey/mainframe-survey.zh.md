# 探索 OpenTelemetry 在大型机上的优先级——来自调查回应的见解

作者

**Ruediger Schulze (IBM)**

|

2025 年 10 月 10 日，星期五

用户认为哪些 [OpenTelemetry](/) 功能对于增强大型机的可观测性最为重要？今年早些时候，[OpenTelemetry 大型机特别兴趣小组](https://github.com/open-telemetry/community/?tab=readme-ov-file#sig-mainframes)（SIG）和 [开放大型机项目](https://openmainframeproject.org/)进行了一项[调查](/blog/2025/otel-mainframe-priorities-survey/)以解决这个问题。本博客详细介绍了此次调查的结果。

## 背景和目的

OpenTelemetry 项目旨在通过提供高质量、可移植的遥测数据，使其能够从任何来源发送到任何目标，从而实现有效的可观测性。该项目目前在 [GitHub 上](https://github.com/open-telemetry/)托管了 90 个存储库，涵盖规范和实现。当 OpenTelemetry 大型机 SIG 成立时，它的任务是为大型机启用最重要的 OpenTelemetry 组件，并专注于三个关键领域：语义约定、编程语言 SDK 以及 OpenTelemetry Collector 的增强。考虑到 OpenTelemetry 项目的广泛范围和大型机复杂的架构，很快就显而易见，深入了解用户优先级对于在大型机上充分利用 OpenTelemetry 功能至关重要。现在调查结果已出，SIG 将优先并实施有针对性的活动，以加速 OpenTelemetry 在大型机平台上的采用。

## 主要见解

以下是确定大型机 SIG 活动优先级的关键见解：

1.  增强大型机社区内的 OpenTelemetry 专业知识。在 26 位 OpenTelemetry 初学者中，有 21 位拥有十年以上的大型机经验，但仍有 11 位表示对 OpenTelemetry 功能一无所知。
2.  优先处理系统性能指标的语义约定，其次是作业处理、数据库和应用程序。在受访者中，30 人希望 OpenTelemetry 首先关注指标，当被问及指标类别时，约 32 人强调系统指标是主要优先级。
3.  优先为 z/OS 提供 Java 和 Python SDK，并开发 COBOL SDK。所有希望获得 Java (25) 和 Python (20) SDK 的受访者也需要用于 z/OS 的 OpenTelemetry SDK。COBOL SDK 有 26 人提出要求，其重要性与 Java SDK 类似。
4.  评估使用 OpenTelemetry Collector 收集系统性能和平台指标的方法。根据回应，30 名参与者表示有兴趣让 OpenTelemetry Collector 在作为代理部署时收集系统性能和平台指标。28 人将大型机运维确定为主要用户，27 人认为 OpenTelemetry 格式的系统性能指标对其组织最重要。

## 贡献方式

我们邀请贡献者和组织加入 [OpenTelemetry 大型机 SIG](https://github.com/open-telemetry/community/?tab=readme-ov-file#sig-mainframes)。主导一项调查优先级，成为 OpenTelemetry 项目的贡献者。例如，参与我们的代码检测和移植计划：

*   支持集成用于 linux/s390x 的自托管 GitHub action runners，以实现持续集成和交付，以及 OpenTelemetry 组件在 s390x 平台上的自动化验证。
*   扩展 zos/s390x 和 linux/s390x 上 SDK 的社区支持：确保选定的 OpenTelemetry SDK 在 z/OS 和 s390x 上的 Linux 上得到全面支持和维护。
*   为 s390x 平台实施 SDK 优化：为性能和兼容性改进做出贡献，充分释放 OpenTelemetry 在大型机上的潜力。
*   为 COBOL 启用 OpenTelemetry 支持：协作开发强大的 COBOL SDK，赋予传统应用程序现代化的可观测性能力。

## 方法论

本次调查分为两个部分。第一部分收集了关于受访者角色和背景的输入。第二部分收集了受访者组织在大型机上启用 OpenTelemetry 的优先级。受访者总共被要求回答 20 个问题。调查从 1 月中旬开始开放了两个月，并通过 OpenTelemetry 和开放大型机项目的博客以及大型机会议进行推广。调查收到了 45 份回应。所有回应都纳入结果。仅进行了最少的数据清洗。由于只有 45 份回应，样本量过小，不足以得出具有统计代表性的结果。组织不应以此为基础做出决策。不过，本次调查提供了关于优先级的一些初步见解，大型机 SIG 将利用这些见解来指导其上述的一些活动。

## 综合回应

### 问题 1：您在组织中的主要角色是什么？

收到了来自不同角色的回应。超过一半的回应（26 份）来自经理、IT 和软件架构师以及系统程序员（包括表示多个角色的回应）。他们中的大多数（22 份）拥有 10 年以上的大型机工作经验。

![组织内的主要角色](/blog/2025/mainframe-survey/q1.png)

### 问题 2：您拥有多少年大型机系统工作经验？

大多数受访者（33 人）拥有 10 年以上的大型机工作经验。其中只有四人声称拥有 OpenTelemetry 专家或高级知识。相反，在六位大型机经验不足四年的受访者中，有四人自认为是 OpenTelemetry 的专家或高级从业者。总的来说，绝大多数回应表明，调查参与者具有大型机背景。

![大型机系统工作经验年限](/blog/2025/mainframe-survey/q2.png)

### 问题 3：您组织所属的主要行业是什么？

绝大多数受访者来自金融服务业（45 份总回应中的 22 份）。一小部分来自不同的物流业（总计 8 份）。13 名受访者主要从事软件和 IT 相关领域，例如软件开发、独立软件供应商 (ISV)、服务提供商、IBM zStack Software、可观测性和信息技术 (IT)。

![组织所属主要行业](/blog/2025/mainframe-survey/q3.png)

### 问题 4：您使用以下哪些大型机平台？

除了一个（专注于 IBM Z 上的 Linux）之外，所有受访者都使用 z/OS 作为大型机操作系统。大约三分之一的受访者（17 人）使用 IBM Z 上的 Linux。八名受访者使用 z/VM 作为虚拟化平台。一名受访者声称使用所有操作系统，包括 z/VSE 和 zTPF。

![使用中的大型机平台](/blog/2025/mainframe-survey/q4.png)

### 问题 5：您使用哪些 z/OS 系统软件？

大多数受访者（38 人）使用 CICS 或 IMS 或两者之一的事务处理系统。39 名调查参与者使用 Db2，31 名使用 VSAM，而一小部分受访者也使用 ADABAS、IDMS、DVM 或 Datacom 作为数据后端。

![使用中的 z/OS 系统软件](/blog/2025/mainframe-survey/q5.png)

### 问题 6：您对 OpenTelemetry 的熟悉程度如何？

OpenTelemetry 采用的初学者（26 人）在受访者中占比最大。其中 15 人不熟悉任何 OpenTelemetry 功能或组件。只有三人自认为是专家，而所有具有中级知识的参与者也声称熟悉 OpenTelemetry Collector。

![对 OpenTelemetry 的熟悉程度](/blog/2025/mainframe-survey/q6.png)

### 问题 7：您熟悉 OpenTelemetry 的哪些功能和组件？

大约一半的调查参与者熟悉 OpenTelemetry 指标 (24) 和 OpenTelemetry Collector (22)。在信号类型方面，虽然指标在受访者熟悉度中领先，但日志 (20) 和分布式追踪 (17) 紧随其后。上下文传播和采样作为与分布式追踪相关的补充技术，知名度略低。代码检测（零代码和手动）仅被大约四分之一的受访者了解。语义约定和 API 规范也同样如此。只有少数参与者表现出对 Kubernetes Operator 和开放代理管理协议的熟悉度，并且这些参与者自认为是至少具有 OpenTelemetry 中级知识，如果不是高级或专家级别的话。

![对 OpenTelemetry 功能和组件的熟悉程度](/blog/2025/mainframe-survey/q7.png)

四分之三的受访者声称使用可观测性或性能监控工具（35 人）。大多数用户对大型机平台具有可见性（30 人）。在使用分布式和大型机平台工具的受访者组（19 人）中，三分之二声称花费超过 20% 的时间进行可观测性和监控活动（13 人），其中五人几乎全职从事这些活动（超过 80% 的时间）。

![可观测性或性能监控工具的使用情况](/blog/2025/mainframe-survey/q8.png)

### 问题 9：您花费多少时间进行可观测性或性能监控活动？

大约四分之一的受访者（11 人）将超过 60% 的时间投入到可观测性和性能监控活动中。大多数调查参与者（19 人）参与这些活动的时间少于 20%，这可以归因于他们工作角色的性质。其中 12 人声称对 OpenTelemetry 的熟悉程度高于初学者水平。

![用于可观测性或性能监控活动的时间](/blog/2025/mainframe-survey/q9.png)

### 问题 10：您组织可观测性策略的关键特征是什么？

实时分析 (35) 和端到端可见性 (33) 是受访者组织的主要目标，其次是开放标准 (26) 及其实现的能力：上下文和关联 (22)、工具选择的灵活性 (19) 和统一数据处理 (19)。碳核算由一位受访者明确添加。

![组织可观测性策略的关键特征](/blog/2025/mainframe-survey/q10.png)

### 问题 11：您首先需要 OpenTelemetry 格式在大型机上支持哪种信号类型？

在调查参与者中，指标是 OpenTelemetry 在大型机上支持的最重要的信号类型（30 人），其次是日志（20 人）和追踪（18 人）。

![信号类型优先级](/blog/2025/mainframe-survey/q11.png)

### 问题 12：在您的组织中，谁将是 OpenTelemetry 格式大型机遥测数据的主要用户？

受访者认为大型机运维是 OpenTelemetry 格式大型机遥测数据的主要用户。在将大型机运维置于优先地位的受访者群体中，80% 的人拥有七年以上的大型机工作经验。值得注意的是，22 人拥有十年以上的工作经验，这表明即使在那些经验丰富的平台用户中，也强烈倾向于简化大型机遥测数据的消费方式。SRE (21) 和应用程序开发人员 (19) 构成了预计将从 OpenTelemetry 格式大型机遥测数据中受益的第二组用户，其次是组织各个领域的其他角色。

![组织中的主要用户](/blog/2025/mainframe-survey/q12.png)

### 问题 13：对您的组织来说，哪类指标以 OpenTelemetry 格式发出最为重要？

对于大多数受访者来说，OpenTelemetry 对系统性能指标（32 个）的支持，结合各种其他工作负载和基础设施相关指标，最为重要。作业和批处理（27 个）、数据库（27 个）和应用程序（27 个）指标被调查参与者认为同等重要，其次是网络（24 个）、I/O（21 个）、存储（20 个）和容量规划（19 个）的基础设施指标。虽然其他指标领域收到的选择较少，但结果突出表明了对支持这些领域也存在相当大的兴趣。例如，多名受访者表示对 DevOps 和 CI/CD 指标以及环境、能源和可持续性指标感兴趣。

![按类别划分的指标重要性](/blog/2025/mainframe-survey/q13.png)

### 问题 14：在您的组织中，以 OpenTelemetry 格式导出大型机遥测数据的主要用例是什么？

在端到端可见性已被确定为组织可观测性策略的重要目标之后，受访者在列出 OpenTelemetry 支持大型机遥测数据的用例时再次证实了这一点。跨着陆区的端到端可见性 (28) 和改进的事件管理 (28) 被视为主要用例。列出的其他用例对至少四分之一的调查参与者来说很重要，其中一些用例，例如优化应用程序性能 (22) 和主动问题发现和预测分析 (21)，甚至与近一半的受访者相关。碳核算获得了一票，因为它被一位受访者添加为重要用例。

![主要用例](/blog/2025/mainframe-survey/q14.png)

### 问题 15：对于哪种应用程序部署模型，您最需要使用 OpenTelemetry 进行检测？

调查参与者希望 OpenTelemetry 检测优先用于在线事务处理 (30)，其次是批处理 (23)、以数据库为中心的应用程序 (19) 和其他应用程序部署模型。分析和 AI 工作负载 (10) 以及云原生、容器化工作负载 (7) 的检测是一些受访者关注的焦点，这突显了大型机上新应用程序部署模型日益增长的使用。

![按应用程序部署模型划分的优先级](/blog/2025/mainframe-survey/q15.png)

### 问题 16：您的组织需要 OpenTelemetry 现有哪些 SDK 支持大型机？

Java (25) 和 Python (20) 是在大型机平台上实现 OpenTelemetry SDK 支持的优先级最高的两种编程语言。20% 的受访者希望 C++ 的 SDK 也能在大型机平台上使用。

![OpenTelemetry SDK 的优先级](/blog/2025/mainframe-survey/q16.png)

### 问题 17：您的组织还需要 OpenTelemetry 支持哪些其他语言的 SDK？

COBOL 是大多数受访者（26 人）希望为大型机开发 OpenTelemetry SDK 的编程语言。COBOL 的 SDK 主要由拥有七年以上大型机经验的调查参与者提出，但也由五位经验不足三年的受访者提出。超过 40% 的受访者在调查回应中要求提供 REXX 和 JCL 的 SDK。超过四分之一的调查参与者要求提供 HLASM 的 OpenTelemetry SDK，20% 的人要求提供 PL/1 和 C 的 SDK。三人表示对 Metal C 的 SDK 感兴趣。

![对大型机语言支持的需求](/blog/2025/mainframe-survey/q17.png)

### 问题 18：您的组织需要 OpenTelemetry SDK 支持哪些大型机操作系统？

根据受访者使用的操作系统，他们表示对这些相应平台的 OpenTelemetry SDK 感兴趣。z/OS 作为 OpenTelemetry SDK 的支持平台对受访者来说最重要 (35)，其次是 IBM Z 上的 Linux (13)，以及一个针对 zTPF 的单一选择。

![支持 OpenTelemetry SDK 的操作系统优先级](/blog/2025/mainframe-survey/q18.png)

### 问题 19：OpenTelemetry Collector 的哪些功能对您的组织启用大型机遥测数据的处理和分发最感兴趣？

OpenTelemetry Collector 的数据收集功能对调查参与者来说最重要。在回应中，使用 Collector 以代理部署方式进行源本地收集 (20) 和使用接收器从任何系统收集 (19) 的得分最高。此外，指标的数据聚合是受访者高度重视的功能 (20)。数据处理 (15) 和导出 (16)、追踪采样 (14) 和网关部署 (14) 也引起了超过 30% 受访者的兴趣。基于硬件的压缩和加密对九位调查参与者来说很重要。

![OpenTelemetry Collector 功能的优先级](/blog/2025/mainframe-survey/q19.png)

### 问题 20：您设想 OpenTelemetry Collector 在大型机上的系统级遥测数据收集和处理有哪些用例？

在评估 OpenTelemetry Collector 时，受访者将系统性能和平台指标的收集列为最重要的用例（30）。大约一半的调查参与者认为系统日志的收集和大型机对资源检测的支持很重要。部分受访者关注来自 Kubernetes 和容器运行时的数据收集，并且他们对将 OpenTelemetry Collector 用于这些用例很感兴趣。

![OpenTelemetry Collector 遥测数据收集按类别划分的优先级](/blog/2025/mainframe-survey/q20.png)

### 总结

调查结果显示，大多数大型机从业者对 OpenTelemetry 尚不熟悉，并优先考虑系统性能指标的采用。此外，对 Java、Python 和 COBOL SDK 以及 Collector 支持有需求。这些发现强调了教育、语义约定以及将 OpenTelemetry 组件移植到大型机平台的有针对性工作的重要性。

加入 OpenTelemetry 大型机 SIG，为语言 SDK、检测和社区专业知识做出贡献，这将加速 OpenTelemetry 在大型机上的采用。通过 Slack 频道 [#otel-mainframes](https://cloud-native.slack.com/archives/C05PXDFTCPJ) 或太平洋时间周三上午 10:00 的 [SIG 会议](https://github.com/open-telemetry/community/?tab=readme-ov-file#sig-mainframes)与 SIG 成员联系。

*本文的一个版本[最初发布](https://openmainframeproject.org/blog/exploring-opentelemetry-priorities-for-mainframes-insights-from-survey-responses/)在开放大型机项目博客上。*