<!--
title: OpenTelemetry与可观测性：展望未来
cover: https://cdn.thenewstack.io/media/2023/12/77697d44-globe-1024x557.jpg
-->

让我们探索一些令人兴奋的趋势，回顾我们目睹的一些情况，并考虑到我们对2024年的期望，看看可观测性领域正在发展的情况。

> 译自 [OpenTelemetry and Observability: Looking Forward](https://thenewstack.io/opentelemetry-and-observability-looking-forward/)，作者 Ken Hamric 是一位有着 35 年开发经验的开发者，创办了多个科技初创公司，包括 CrossBrowserTesting.com，后被 SmartBear 收购并加入其强大的测试组合，最近是 Tracetest，一个开源项目，允许用户...

随着年底的临近，这是一个很好的时机来暂停并反思。2023 年对 OpenTelemetry 来说是一个里程碑，因为它的三种基本信号 tracing、metrics 和 logging 都达到了稳定版本。这一成就标志着 [OpenTelemetry](https://thenewstack.io/opentelemetry-gaining-traction-from-companies-and-vendors/) 最初提出的提供一个标准化框架来检测和收集可观测性数据的愿景的实现。

让我们借此机会来探索我们所见证的一些激动人心的趋势，深入研究创新产品和使用案例，仔细考虑可观测性不断发展的景观，以期待 2024 年会带来什么。

## 指标(Metrics)独树一帜

尽管 OpenTelemetry 的指标规范在 2022 年 5 月宣布稳定，但今年看到了采用的传播。这里有一些从业者的文章:

- VMware 的 Matthew Kocher 和 Carson Long 的“体验报告: [在 Cloud Foundry 中采用 OpenTelemetry 进行指标检测](https://opentelemetry.io/blog/2023/cloud-foundry/)”。
- 我们自己的 Matheus Nogueira 的“[在您的 Go 应用程序中添加 OpenTelemetry 指标](https://tracetest.io/blog/adding-opentelemetry-metrics-in-your-go-app)”。

展望 2024 年，预计会看到 logs 有相同的运动和采用。

## 关注在负载测试中使用分布式跟踪

两款领先的负载测试工具 [Grafana k6](https://k6.io/) 和 [Artillery.io](https://artillery.io/) 在 2023 年增加了对 OpenTelemetry 的支持。

- Grafana k6 [引入了跟踪](https://github.com/grafana/xk6-distributed-tracing)功能，使性能工程师能够在[负载测试](https://thenewstack.io/trace-based-testing-the-next-step-in-observability/)期间识别系统瓶颈或故障。
- Artillery.io 紧随其后，[添加了指标和分布式跟踪](https://www.artillery.io/blog/introducing-opentelemetry-support)，为系统性能提供了更详细的分析。

Tracetest 利用 k6 测试提供的能力，实现[基于跟踪的负载测试](https://docs.tracetest.io/tools-and-integrations/k6)，允许在运行测试时进行深度断言。我们已经看到像 [Sigma Software](https://tracetest.io/case-studies/how-sigma-software-built-load-testing-for-their-microservices-with-k6-tracetest) 这样的客户广泛使用了这项功能。在 2024 年，Tracetest 团队将考虑将这一能力添加到 [Artillery.io](http://artillery.io/) 和其他负载测试工具中。

## OpenTelemetry 的支持和用例不断扩展

越来越多的供应商正在采用 OpenTelemetry 标准，以支持超出典型但非常重要的遥测数据分析角色之外的操作。

- 像 Tyk 这样的公司[正在对其 API 网关进行仪表化，使其原生支持 OpenTelemetry](https://opentelemetry.io/blog/2023/tyk-api-gateway/)。
- 最终用户正在为 OpenTelemetry 找到新的用例，例如[使用分布式跟踪观察您的 CI/CD 流水线](https://thenewstack.io/how-to-observe-your-ci-cd-pipelines-with-opentelemetry/)。
- [Tracetest](https://tracetest.io/) 利用分布式跟踪数据进行集成和端到端测试。

## 强调 OpenTelemetry Collector

[OpenTelemetry Collector](https://thenewstack.io/how-adobe-uses-opentelemetry-collector/) 位于 OpenTelemetry 世界的中心，接收来自应用程序的信号，对其进行处理和转换，然后将其导出到任意数量的后端系统。随着对 OpenTelemetry 的[集成](https://opentelemetry.io/ecosystem/integrations/)和[供应商](https://opentelemetry.io/ecosystem/vendors/)支持的扩展，对这个集中Collector的需求和要求也在增加。

在 2023 年引入的 OpenTelemetry Transformation Language (OTTL) 增强了 OpenTelemetry Collector处理和转换传入信号的能力。

在 Tracetest，我们能够[利用在过滤处理器中使用 OTTL 的能力](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/filterprocessor/README.md)，改进了我们从输出大量遥测数据的生产环境中收集跟踪数据的方式。这对于在高负载环境中运行测试，包括生产环境，使 Tracetest 变得更加合适。

## 普及可观测性

在最近的讨论中，我们发现客户中有一种向“普及可观测性”的趋势。这超越了其传统用途，不仅由站点可靠性工程师和 DevOps 使用，而且公司中的每个人，包括开发人员和测试人员，都参与到可观测性中。这一转变重新定义了可观测性，使其从生产问题的一种反应性工具变成了在开发和测试中有益的一种主动工具。

[Honeycomb](https://www.honeycomb.io/) 强调[在开发过程中使用可观测性](https://www.honeycomb.io/blog/observability-driven-development)，而 [Digma.ai](http://digma.ai/) 和 Tracetest 等工具正在推动这一进程。

## 浏览器

OpenTelemetry 的主要作用一直局限于为后端系统进行仪表化，而[基于开放标准的浏览器仪表化](https://opentelemetry.io/docs/instrumentation/js/getting-started/browser/)仍处于试验阶段并且进展较慢。目前正在努力改进和标准化这方面的仪表化。

- 在这方面，[Uzufly](https://tracetest.io/case-studies/how-uzufly-built-end-to-end-testing-serverless-web-app-with-distributed-traces) 独树一帜。它使用现有的客户端仪表化来构建测试。展望未来，它的雄心是将基于跟踪的测试扩展到覆盖浏览器中由前端操作引发的测试。

这将使得在前端和后端之间进行完整的端到端测试成为可能。请在 2024 年关注这个话题的更多进展！

## 2023 年已经是‘上一年’

告别 2023，我们怀着热情迎来 2024。OpenTelemetry 在标准支持和广泛采用的推动下，势头强劲，助力其增长。新的一年将迎来激动人心的发展，围绕 OpenTelemetry 出现创新的产品和用例。我迫不及待地期待着 2024 年将揭示的进步和创新。愿 OpenTelemetry 长存！
