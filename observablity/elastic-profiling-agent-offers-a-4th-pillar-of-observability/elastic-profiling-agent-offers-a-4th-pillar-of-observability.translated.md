# 弹性分析代理提供第四个可观察性支柱

![Featued image for: Elastic Profiling Agent Offers a 4th Pillar of Observability](https://cdn.thenewstack.io/media/2024/06/eda61053-ahmed-vblx61xdb2m-unsplash-1-1024x683.jpg)

[Elastic 的持续分析代理](https://github.com/open-telemetry/community/issues/1918) 被 [OpenTelemetry](https://thenewstack.io/opentelemetry-gaining-traction-from-companies-and-vendors/) 分析社区接受，这可以说是一种形式，但它将为实现分析代理的可能性奠定基础。由于它提供的信号功能，该代理可以为所谓的第四个 [可观察性](https://thenewstack.io/observability/) 支柱奠定基础，与 [跟踪、日志和指标](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/) 并列。

[Honeycomb](https://www.honeycomb.io/?utm_content=inline+mention) 的开源总监 [Austin Parker](https://www.linkedin.com/in/austinlparker/) 解释说，OpenTelemetry 的分析代理应该对用户很有用，因为它通过扩展到代码级别提供了更深入的可观察性分析。它通过扩展统一流中收集的遥测数据来对指标、跟踪和日志进行更深入的分析，这些数据扩展到整个网络中应用程序的代码级别。Parker 说，代码被分析和存储。

“OpenTelemetry 的持续分析在某种程度上已经向公众开放了六年多，”Parker 说。“随着分析代理添加到 OpenTelemetry，我们预计持续生产分析将成为主流。”

实际上，这意味着当出现问题时，或者当查看可观察性数据流提供的某些性能方面时——例如当 CPU 运行缓慢或最终用户的数据请求花费太长时间时——配置文件会识别出有问题的代码，Parker 说。“有了合适的可观察性附加工具，应该可以更快地提供修复，因为用户可以通过他们的查询更轻松地查明问题代码，”他说。

[持续分析](https://thenewstack.io/grafana-shows-new-observability-projects-at-observabilitycon/) 是一种通过收集有关软件应用程序执行情况随时间推移的信息来了解其行为的技术，OpenTelemetry 的创建者和贡献者 [Bahubali Shetti](https://www.linkedin.com/in/billshetti/)（Elastic）、[Alexander Wert](https://www.linkedin.com/in/alexanderwert/)（Elastic）、[Morgan McLean](https://www.linkedin.com/in/morganmclean/)（Splunk）和 [Ryan Perry](https://www.linkedin.com/in/ryanaperry/)（Grafana）在一篇 [博客文章](https://opentelemetry.io/blog/2024/profiling/) 中解释道。他们写道，通过这种方式，持续分析涵盖了跟踪函数调用的持续时间、内存使用情况、CPU 使用情况和其他系统资源以及相关元数据。
“这一贡献不仅促进了可观察性持续分析的标准化，而且还加速了其作为 OpenTelemetry 中关键信号的采用，”OpenTelemetry 项目创建者和贡献者写道。“客户受益于一种与现有信号（如跟踪、指标和日志）相关的收集分析数据的供应商无关方法，为可观察性洞察和更有效的故障排除体验开辟了新的可能性。”

[Abhishek Singh](https://www.linkedin.com/in/abhiksingh/)，Elastic 的可观察性总经理说，捐赠不仅仅是一种形式。这是因为“这里贡献了大量的代码和 IP，它们以与语言无关的方式工作，以分析整个系统。它是市场上最全面的，并在企业中部署，”Singh 说。

例如，Elastic 的一个大型客户意识到，其供应商部署的代理消耗的资源比预期多，“导致其整个机群浪费了数百万美元的计算资源，”Singh 说。“OpenTelemetry 没有能力分析应用程序之外的任何进程，即使这些能力也是有限的，”Singh 说。

Parker 说，Elastic 分析代理之所以引人注目，是因为它是一款可用于生产的产品，我们可以将其集成到我们现有的工具生态系统中。“这加快了我们向用户提供分析、将其与现有信号集成以及获得有关如何改进的关键反馈的能力，”Parker 说。
Elastic 的捐赠填补了 OpenTelemetry 项目的探查器之前缺少的空白。这就是 [eBPF](https://thenewstack.io/what-is-ebpf/) 的作用所在——Elastic 的探查器使用它——因为 eBPF 允许直接从 [Linux 内核](https://thenewstack.io/rust-in-the-linux-kernel/) 抓取遥测数据，并且可以扩展到整个网络。eBPF 有助于消除对第三方和专有代码检测（运行时/字节码）、重新编译或服务重启的需求。据项目创建者称，开销很低，在生产环境中 CPU 占用率不到 1%，内存使用率也很低。

总而言之，Elastic 的贡献很重要，因为 Elastic 使用 eBPF 提供“全系统探查”，Singh 说，“这不仅允许用户探查其应用程序进程，还可以探查所有正在运行的进程。”“这很重要，因为用户可以将代码更改与性能下降联系起来，并查看系统上运行的其他内容是否会影响性能，例如第三方代理。”

该项目的创建者强调了持续探查代理为 OpenTelemetry 带来的具体好处：

**提供详细的见解**: 持续探查数据通过提供有关服务行为的详细和代码级见解来补充现有信号（跟踪、指标和日志）。**提高保真度和深度**: 与其他 OpenTelemetry 信号（如跟踪）无缝关联，从而提高保真度和调查深度。**预测环境影响**: 将探查数据与 OpenTelemetry 的资源信息（即资源属性）相结合，使团队能够深入了解服务的碳足迹。
通过详细分解服务的资源利用率，探查数据提供了有关性能优化机会的可操作信息。

根据该项目的文档，持续探查代理支持各种运行时和语言，例如：

- C/C++
- Rust
- Zig
- Go
- Java
- Python
- Ruby
- PHP
- Node.js / V8
- Perl
- .NET

## 重大工作
OpenTelemetry 贡献者将继续共同努力，完成其中一个更具活力的开源项目。公司贡献者包括 Datadog、Grafana、Honeycomb、New Relic、Splunk 等。

Parker 说：“OpenTelemetry 作为一个项目，之所以取得成功，是因为我们社区的贡献，无论他们隶属于哪个机构。我们非常感谢来自世界各地和许多不同供应商的工程师每个月为该项目付出的努力。”“构建一个与供应商无关的云原生可观察性框架，比任何一家公司都重要，很高兴看到社区对此做出了如此积极的回应。”

Datadog 是 OpenTelemetry 探查器和 OpenTelemetry 项目开发的主要贡献者。该公司将继续为探查器的功能以及 OpenTelemetry 项目的其他方面做出贡献，并为使用 Datadog 时改善可观察性体验做出贡献。

Datadog 的产品负责人 [Yrieix Garnier](https://www.linkedin.com/in/yrieixgarnier/fr) 说：“使用这个统一的代理，您可以决定将数据发送到哪里，从而在您的监控和可观察性策略中提供灵活性和完整性。”“您必须并行运行以创建收集器，然后创建导出器到数据后端。现在，就像使用一个工具将所有内容推送到内部，无论格式如何。”


[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)