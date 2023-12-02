<!--
title: 如何使用OpenTelemetry监控你的CI/CD流水线
cover: https://cdn.thenewstack.io/media/2023/11/1a3dc57a-cat_magnifying-glass_1-1024x834.png
-->

使CI/CD流水线具备可观测能力有助于提高故障排除、开发敏捷性和效率。

> 译自 [How to Observe Your CI/CD Pipelines with OpenTelemetry](https://thenewstack.io/how-to-observe-your-ci-cd-pipelines-with-opentelemetry/)，作者 Adriana Villela 和 Reese Lee。

今天的软件比 20 多年前的软件复杂了数个数量级，这给我们调试代码带来了新的挑战。幸运的是，通过在系统中实现可观测性，我们已经相当远程地理解了我们的应用程序正在执行什么以及问题正在发生在哪里。

然而，不仅仅是软件发生了进化——创造和开发它的过程也发生了改变。[DevOps](https://roadmap.sh/devops) 引入了 [CI/CD 的概念](https://thenewstack.io/a-primer-continuous-integration-and-continuous-delivery-ci-cd/)。随着交付周期从月度到季度再到现在的周度甚至一天多次缩短，我们正在沿着软件交付流水线采用自动化。

不幸的是，与应用程序软件相比，CI/CD 流水线的可观测性没有取得太大进展。考虑到这些流水线是软件交付过程的支柱，这令人惊讶：如果你没有可视性，那么当出现问题时如何排除故障并使软件投入生产？

这就是我们在本文中将要关注的内容：CI/CD 流水线的可观测性。首先，我们将定义一些事物；然后，我们将深入探讨观测流水线的重要性以及如何使其可观测；最后，我们将通过讨论一些剩余的挑战来结束。

## 关键概念

以下是一些需要了解的定义:

### 可观测性

有关可观测性存在多种定义，因此我们将缩小范围，选择我们最喜欢的一种：

> 可观测性，或称 o11y(发音为“奥利”)，可以通过让你提出问题而不需要知道该系统的内部工作原理，从外部理解一个系统。有趣的事实："o11y" 中的 11 代表了单词“observability” 中“o”和“y”之间字符的个数。

这意味着即使你不了解一个系统所有复杂的底层业务逻辑，该系统也会发出足够的信息让你跟踪线索来回答："这是为什么发生的？"。但是，如果你的系统不发出信息，你就无法实现可观测性。如何获取那些信息呢？一种方法是使用 OpenTelemetry。

### OpenTelemetry

[OpenTelemetry(OTel)](https://thenewstack.io/introducing-opentelemetry-in-your-organization-3-steps/)是一个用于生成、收集、转换和导出遥测数据的开源可观测框架。它提供了一组 API、软件开发工具包(SDK)、仪器化库和工具来帮助你完成这些工作。自 2019 年正式推出以来，它已成为应用程序仪器化和遥测生成和收集的事实标准，[eBay](https://innovation.ebayinc.com/tech/engineering/why-and-how-ebay-pivoted-to-opentelemetry/) 和 [Skyscanner](https://www.infoq.com/presentations/opentelemetry-observability/) 等公司都在使用它。

它最大的好处之一是摆脱了供应商锁定。你可以对你的应用程序进行一次仪器化，然后将你的遥测数据发送到最适合你的任何后端。它还提供了一些非常酷的工具，例如 Collector。

Collector 是一个中立的供应商服务，用于摄取、转换和导出数据到一个或多个可观测性后端。

![](https://cdn.thenewstack.io/media/2023/11/55f49024-pipeline_2.png)

Collector 由四个主要组件组成，这些组件可以访问遥测数据:

- **Receiver**摄入数据，无论是来自你的应用程序代码还是你的基础设施。
- **Processor**转换你的数据。Processor可以做诸如模糊你的数据，添加属性，删除属性或过滤数据等事情。
- **Exporter**将你的数据转换为与你选择的可观测性后端兼容的格式。
- **Connector**允许你连接两个流水线。

你可以将 OTel Collector 视为一个数据流水线。

## CI/CD 流水线

CI/CD 是一种自动化的软件交付方法，它借鉴了两种关键实践:

- 持续集成(CI)是在每次代码更改时构建、打包和测试你的软件。
- 持续交付(CD)是将该软件包部署到生产环境。

![](https://cdn.thenewstack.io/media/2023/11/cd1d6a74-tacocicdpipeline.gif)

自动化流水线通过允许你更快地将任何新功能、错误修复和一般更新推送给客户来实现快速的产品迭代。它们消除了手动错误的风险，并将反馈循环标准化为对开发人员的反馈。

## 为什么 CI/CD 流水线的可观测性很重要

当你的流水线运行良好时，你的团队可以连续编写、构建、测试和部署代码和配置更改到生产中。你还可以改进或实现开发敏捷性，这意味着你可以更改你的操作并最大限度地减少确定这些修改对你的应用程序运行状况是否有积极或消极影响所需的时间。

相反，当你的流水线不健康时，你可能会遇到以下一个或多个问题:

- **慢速部署**：错误修复可能不够快以缓解用户的不满，问题可能变得紧急。
- **测试问题**：等待测试完成，或者没有足够的时间测试不同配置，可能导致延迟的部署，以及难以实现足够的应用性能覆盖用户群体。
- **技术债**：难以确定潜在问题可能导致技术债。

![](https://cdn.thenewstack.io/media/2023/11/7b183a15-this-is-fine_4.png)

### 流水线是 DevOps 工程师的生产系统

尽管流水线可能不是外部用户互动的生产环境，但它们绝对是内部用户（例如，软件工程师和[站点可靠性工程师s](https://thenewstack.io/our-2023-site-reliability-engineering-wish-list/)（SREs））互动的生产环境。能够观测您的生产环境意味着：

- 防止不必要的长周期时间，或者更改的交付时间，这会影响提交到生产的时间。
- 减少推出新功能和错误修复的任何延迟。
- 减少用户等待时间。

### 代码可能会失败

CI/CD 管道由定义其工作方式的代码运行，尽管您付出最大的努力和细心，代码仍可能失败。使应用程序代码可观测有助于在遇到生产问题时理清事情。同样，了解流水线的情况可以帮助您在其失败时理解发生了什么。

### 故障排除更容易

具有可观测的流水线有助于回答诸如：

- 发生了什么问题？
- 为什么会失败？
- 这之前是否曾经失败过？
- 最常发生的故障是什么？
- 流水线的正常运行时间是多久？
- 是否存在瓶颈？如果存在，是什么瓶颈？
- 您能缩短修复流水线问题的交付时间吗？
- 想要收集什么样的数据？

### 你希望收集哪类数据？

为了回答这些问题，您需要收集关于您的流水线的信息。但应该收集什么信息呢？捕获以下信息：

- 分支名称。
- 提交的安全哈希算法（SHA）。
- 机器 IP。
- 运行类型（定时运行，由合并/推送触发）。
- 失败的步骤。
- 步骤持续时间。
- 构建编号。
- 如何观测流水线

## 如何观测流水线

回顾一下，当系统发出足够的信息来回答问题：“为什么会发生这种情况？”时，系统是可观测的。首先，您需要一种发出信息的方式；然后，您需要将其发送到一个地方；最后，您需要分析它并找出需要修复的问题。

这就是 OpenTelemetry 发挥作用的地方。您可以在系统中实现 OpenTelemetry，以发出您需要实现系统可观测性所需的信息。就像您用于应用程序一样，您也可以用于 CI/CD 流水线！您仍然需要将生成的遥测发送到后端进行分析，但我们将重点放在第一部分上，即仪器化。

### 使用 OpenTelemetry

对于为流水线提供仪器化，OpenTelemetry是一个非常合理的选择，因为许多人已经用它为应用程序提供仪器化；在过去的几年中，采用和实施逐渐增加。

### 一些选项是什么？

目前，有点杂。包括：

- 商业 SaaS 监控解决方案，例如 [Datadog](https://www.datadoghq.com/product/ci-cd-monitoring/) 和 [Splunk](https://www.splunk.com/en_us/blog/learn/ci-cd-devops-analytics.html)。
- 供应商创建的工具，您可以将其插入现有的 CI/CD 工具中，以帮助实现 CI/CD 的可观测性（例如 [Honeycomb buildevents](https://github.com/honeycombio/buildevents)）。
- 自制的 GitHub actions（参见[这里](https://github.com/inception-health/otel-export-trace-action)、[这里](https://words.boten.ca/GitHub-Action-to-OTLP/)和[这里](https://cloud-native.slack.com/archives/C0598R66XAP/p1698393723861129)的示例）以在 CI/CD 流水线中启用可观测性。
- 自制的 [CircleCI webhook](https://github.com/DavidS/circleci-hook) 用于 OTel。
- 自制的 [Drone CI webhook](https://cloud-native.slack.com/archives/C0598R66XAP/p1698408390701199) 用于 OTel。
- 原生 OpenTelemetry 集成到 [Jenkins](https://plugins.jenkins.io/opentelemetry/) 和 [Tekton](https://github.com/tektoncd/community/blob/main/teps/0124-distributed-tracing-for-tasks-and-pipelines.md) 中。

您还可以将这些工具集成到您的 CI/CD 流水线中；它们会发出 OpenTelemetry 信号，从而帮助使您的流水线可观测：

- [Maven build OTel extension](https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/maven-extension/README.md) 发出 Java 构建的分布式跟踪。
- [Ansible OpenTelemetry 回调跟踪](https://docs.ansible.com/ansible/latest/collections/community/general/opentelemetry_callback.html) Ansible playbooks。
-[ Dynatrace 的 JUnit Jupiter OpenTelemetry Extension](https://github.com/dynatrace-oss/junit-jupiter-open-telemetry-extension) 是通过 OpenTelemetry 收集 JUnit 测试执行数据的 Gradle 插件。还有一个 [Maven 版本](https://github.com/dynatrace-oss/junit-jupiter-open-telemetry-extension/packages/1061205)。
- [pytest-otel](https://pypi.org/project/pytest-otel/) 记录执行的 Python 测试的分布式跟踪。
- [otel-cli](https://github.com/equinix-labs/otel-cli) 是用 Go 编写的命令行接口（CLI）工具，使 shell 脚本能够发出跟踪。
- [Filelog receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/filelogreceiver)（OTel Collector）尾随并解析文件中的日志。
- [Git Provider receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/gitproviderreceiver)（OTel Collector）从 Git 供应商中抓取数据。
- 可观测的流水线示例

## 可观测性流水线示例

此图显示如何使用上述一些工具实现流水线的可观测性。假设您正在构建和部署一个 Java 应用程序。您使用 Jenkins 来编排构建和部署。

![](https://cdn.thenewstack.io/media/2023/11/ecd38734-otel-jenkins-pipline_5.png)

1. Jenkins CI/CD 管道可以通过 [Jenkins OTel 插件](https://plugins.jenkins.io/opentelemetry/)发出遥测信号。
2. 在构建阶段：
   - 您可以使用 [Maven OTel 扩展](https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/maven-extension/README.md)发出 Java 构建的分布式跟踪。
   - 如果您的构建包含 shell 脚本，您可以使用 [otel-cli](https://github.com/equinix-labs/otel-cli) 工具使您的 shell 脚本能够发出跟踪。
3. 在测试阶段，Maven 的 [JUnit Jupiter 插件](https://github.com/dynatrace-oss/junit-jupiter-open-telemetry-extension/packages/1061205)允许您通过 OpenTelemetry 收集 JUnit 测试执行的数据。
4. 在打包阶段，使用 Artifactory 打包应用程序时，您可以通过 [Filelog 接收器](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/filelogreceiver/README.md)将其日志发送到 OTel Collector，该接收器尾随并解析文件中的日志。
5. 在部署阶段，使用 Ansible 编排部署时，[Ansible OpenTelemetry 回调](https://docs.ansible.com/ansible/latest/collections/community/general/opentelemetry_callback.html)会向 Ansible playbooks 添加跟踪。如果您的 Ansible playbook 还使用了 shell 脚本，它可以利用 [otel-cli](https://github.com/equinix-labs/otel-cli) 工具，使您的 shell 脚本能够发出附加的跟踪数据。
6. 各种插件发出的信号被 OTel Collector 所摄取。数据可以使用标准的 [OTLP 接收器](https://github.com/open-telemetry/opentelemetry-collector/tree/main/receiver/otlpreceiver)来摄取遥测数据，还有 [Git Provider 接收器](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/gitproviderreceiver)和 [Filelog 接收器](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/filelogreceiver/README.md)。然后 Collector 将遥测信号发送到可观测性后端。
7 一旦您的数据到达可观测性后端，您可以查看和查询数据，设置警报等。

## 实现可观测流水线的挑战

尽管使用 OpenTelemetry 实现 CI/CD 流水线的可观测性是有道理的，但缺乏标准化，工具生态相对混乱。

OpenTelemetry 并未内置在大多数 CI/CD 工具中。虽然有将观测能力添加到 GitLab 和 GitHub Actions 等 CI/CD 工具的愿望，但这些倡议进展缓慢。例如，尽管在[ GitLab 的有关使用 OTel 进行流水线可观测性的请求](https://gitlab.com/gitlab-org/gitlab/-/issues/338943)上已经有了活动，但该请求已经开放了两年。关于 [CI/CD 流水线可观测性的 OTel 提案](https://github.com/open-telemetry/oteps/pull/223)于 2023 年 1 月提出，但截至 2023 年 11 月，自 7 月以来没有活动。

因此，如果您想使用那些工具，您要取决于个人和组织，他们自己创造了这些工具。如果他们决定不再维护这些工具，会发生什么？

## 了解更多

使您的 CI/CD 流水线可观测有助于更有效地排除问题，实现开发敏捷性，并深入了解其内部运作，以便您可以调整它们以帮助它们更高效地运行。

健康的流水线意味着您可以持续编写、构建、测试和部署新代码。相反，不健康的流水线可能意味着部署速度较慢、测试问题和技术债务。

您可以使用 OpenTelemetry 向您的流水线添加可观测性；虽然目前选择有限，但事情正朝着正确的方向发展，我们对 CI/CD 未来的展望充满期待！

进一步阅读：

- [Fighting Slow and Flaky CI/CD Pipelines starts with Observability](https://logz.io/learn/cicd-observability-jenkins)
- [Leveraging OpenTelemetry to Enhance Ansible with Jaeger Tracing](https://www.linkedin.com/pulse/leveraging-opentelemetry-enhance-ansible-jaeger-tracing-infralovers)
- [CI/CD Pipeline Monitoring: An Introduction](https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html)
- 在 [CNCF Slack](https://communityinviter.com/apps/cloud-native/cncf) 上查看 [cicd-o11y](https://cloud-native.slack.com/archives/C0598R66XAP) 频道

