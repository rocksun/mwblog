## CI/CD 可观测性：OpenTelemetry 的全新丰富机遇

![CI/CD 可观测性：OpenTelemetry 的全新丰富机遇的特色图片](https://cdn.thenewstack.io/media/2024/04/203ec45b-animals-3337027_1280-1024x682.jpg)

持续集成和持续部署 (CI/CD) 是现代软件交付的支柱，但对其流程的可见性仍然有限。以下是 OpenTelemetry (OTel) 如何改变这一现状，以及这些改变为何如此令人兴奋。

根据询问对象的不同，CI/CD 有不同的定义，但一致的部分是它具有持续性——一个永无止境的反馈循环，其全部内容都是减少手动流程、生成可部署软件并在问题到达生产环境之前将其根除。

该实践已成为减少手动流程、生成可部署软件和提高软件交付流程信心的必要条件，但我们缺乏防止其变得不稳定的工具。

对 CI 系统的可观测性仍处于早期阶段——现在，由于多种因素的结合，这一机会成为可能。让我们仔细了解历史上不可观察的 CI/CD 管道方面，OpenTelemetry 及相关工作如何实现 CI 可观测性，以及未来开发者生产力提升的高上限。

### 仍有很大的空间可以向左移动

CI 和警报传统上被用作具有共同目标的解决方案。它们作为持续自动化监控的基本组件紧密协作。持续集成是早期阶段的保护者：它检测更改、维护构建运行状况并持续监控系统信号。警报往往用于后期阶段。它识别出 CI 遗漏的问题。因此，CI 奠定了基础，而警报对威胁做出响应——持续协作以解决同一问题。

但从历史上看，可观测性的重点一直放在事物的“运行”部分，而忽略了构建、测试和部署等早期阶段的宝贵见解，以及 CI 管道早期阶段的其他关键机会领域。

我们部署事物，我们看到事物着火，然后我们尝试扑灭大火。

但如果我们只观察开发和部署周期的最后阶段，那就太晚了。我们不知道在构建阶段或测试阶段发生了什么，或者我们在根本原因分析或平均恢复时间增加方面遇到困难，也错失了优化机会。我们知道我们的 CI 管道运行时间很长，但如果我们想让它们运行得更快，我们不知道该改进什么。

如果我们将可观测性重点向左移动，我们可以在问题升级之前解决问题，通过在流程中减少问题来提高效率，提高测试的稳健性和完整性，并最大程度地减少与部署后和停机相关的成本和开支。

### 使用 OpenTelemetry 拥有自己的 CI 数据

OpenTelemetry 成为云原生计算基金会 (CNCF) 中最活跃的项目之一（从技术上讲，“第二大速度项目”）是有原因的。它一直是定义语义约定和统一日志、指标和跟踪（可观测性的“三大支柱”）以及分析和其他新兴信号类型的信号类型的出色协议。

在为开放标准和曾经是黑匣子的领域的共同基础增加广泛支持后，我们看到 OTel 在去年掀起了波澜。曾经高度专有的可观测性领域，如数据库、云提供商、查询语言和日志文件格式，已经通过一个定义明确的协议被破解，该协议有效，并且支持我们现代多语言世界中的几乎所有流行编程语言。

CI/CD 供应商工具领域有其自己的黑匣子。每个开发团队都使用 CI 系统，大多数团队使用多个 CI 系统。“拥有自己的 CI 数据”的概念今天得到了更多用户的关注，这些用户厌倦了复杂的解决方法，无法在他们自己理解良好的后端架构中获取该数据，但正在努力进行上下文切换和专有后端。

这就是当 OTel CI/CD 工作组首次提出引入新的 CI/CD 可观测性语义约定时，随后又提出了一个新的专门兴趣小组 (SIG)，专门针对 CI/CD 可观测性时，引起了如此大的兴奋。
**可观测性数据未来的样子**

拥有自己的数据意味着您可以决定数据的去向以及如何存储数据。通过在我们的 CI 系统和我们选择的目的地之间运行 OpenTelemetry，OpenTelemetry 会负责将其转换为我们想要的数据库和架构，这意味着基于以前孤立的 CI 数据的大量创新现在正在引入可观测性工具领域。

例如，我们构建了一个 [OpenTelemetry Collector 分发](https://github.com/grafana/grafana-ci-otel-collector)——一个二进制文件，其接收器、处理器和导出器从 Drone 中提取 CI 数据，将其转换为您需要的格式，然后将该数据发送到数据库。[Jenkins 有一个插件](https://plugins.jenkins.io/opentelemetry/)，可通过 OpenTelemetry 协议 (OTLP) 导出数据。

对于可观测性社区来说，这是一个非常激动人心的时刻。通过从我们的 CI 中获取数据并将其与可观测性系统集成，我们可以追溯到构建中的日志，并从我们的 CI 中查看重要信息——例如首次出现故障的时间。从那里，我们可以找出产生错误的原因，这种方式可以更准确地查明错误的发生时间。

CI/CD 领域为可观测性系统解锁了大量预犯罪数据。从构建中获取遥测数据可以让您构建部署分支的时间线，并深入了解发生的故障，解决各种不稳定的测试问题，轻松查找和重现问题根源，并对 CI/CD 管道性能和持续时间进行故障排除。

随着可观测性继续向 CI 管道中更靠左的方向发展，我们可以在问题升级之前解决问题，通过从流程中消除问题来提高效率，提高测试的健壮性和完整性，并最大程度地减少与部署后和停机相关的成本和开支。

在 OpenTelemetry 的推动下，我们预计 CI/CD 领域将成为可观测性最热门的演进领域之一，加入基础设施监控和应用程序性能监控等其他主要可观测性用例的行列。

CI/CD 是每个现代生产系统的基础——通常也是先决条件，因此我们应该通过对其应用我们用于生产服务的最佳实践来强调其重要性。

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。