<!--
title: Docker最不为人知的秘密：可观测性如何拯救开发者的理智
cover: https://cdn.thenewstack.io/media/2025/05/69904fc8-seo-galaxy-yushnkbhf3q-unsplash-1-scaled.jpg
summary: 告别盲盒式Debug！Docker容器可观测性最佳实践来袭！集成OpenTelemetry+Jaeger，实现分布式追踪，实时监控，告别MTTR过长。更有CI/CD集成、AI驱动的异常检测等高级技巧，助力云原生应用性能提升！
-->

告别盲盒式Debug！Docker容器可观测性最佳实践来袭！集成OpenTelemetry+Jaeger，实现分布式追踪，实时监控，告别MTTR过长。更有CI/CD集成、AI驱动的异常检测等高级技巧，助力云原生应用性能提升！

> 译自：[Docker’s Best-Kept Secret: How Observability Saves Developers’ Sanity](https://thenewstack.io/dockers-best-kept-secret-how-observability-saves-developers-sanity/)
> 
> 作者：Aditya Gupta

随着软件系统变得越来越复杂和分布式，开发人员和运维团队在理解大规模应用程序行为方面面临着严峻的挑战。虽然基于容器、微服务和云原生架构的技术使得交付软件更容易，但它们也增加了调试和监控流程的难度。如何有效地诊断问题、实时监控性能并确保服务之间的可靠性？

答案在于端到端的可观测性。可观测性超越了传统的监控，提供了对系统行为的深入洞察。通过在 Docker 容器中采用有效的追踪解决方案，例如 OpenTelemetry 和 Jaeger，开发人员现在可以主动检测性能问题、提高可靠性并显著减少停机时间。

![](https://cdn.thenewstack.io/media/2025/05/a122a40a-image1.png)

本指南概述了可观测性原则，[阐明了分布式追踪的作用](https://thenewstack.io/developer-relations-foundation-aims-to-clarify-role/)，并讨论了 Docker、OpenTelemetry 和 Jaeger 如何协同工作以增强运营智能并简化事件响应。

## 为什么可观测性比以往任何时候都重要

现代应用程序越来越多地以分布式系统的形式出现，这些系统由许多相互依赖的服务和应用程序编程接口 (API) 组成。虽然 Docker 使微服务的扩展和部署更容易，但其固有的[复杂性通常会导致不明确的性能问题](https://thenewstack.io/the-complexity-of-solving-performance-problems/)和扩展瓶颈。

主要的可观测性挑战包括：

* **分布式系统复杂性**：分布式系统中的挑战在于，在许多相互连接的微服务中查明错误或瓶颈的原因。
* **延迟和性能问题**：快速检测慢响应或资源争用。
* **实时洞察**：需要实时了解系统性能，而不是依赖于滞后的日志或传统监控工具。

如果没有完全的可观测性，故障排除既缓慢又费力，并且会大大增加平均修复时间 (MTTR)。

![](https://cdn.thenewstack.io/media/2025/05/a40fa2ce-image3.jpg)

根据我自己在一家大型云规模基础设施提供商处进行容器服务性能调试的经验，由于缺少分布式追踪，我们几乎完全依赖于日志关联和警报驱动的指标，这些指标在 70% 的情况下是成功的。剩下的就是猜测和漫长的作战室会议。通过在该等式中进行服务之间的跟踪传播，MTTR 急剧下降，调试变得更像是在时间线中导航，而不是在日志中搜索。

## 为什么基于 Docker 的环境需要可观测性

我记得在对一个部署进行故障排除时，该部署已经崩溃，其中一个前端应用程序中容器中运行的应用程序不断定期崩溃。CPU 和内存都很好，日志不透明，自动缩放隐藏了症状。我们不知道是身份验证服务在高并发流量期间超时，直到我们使用 OpenTelemetry 添加了跟踪上下文并在 Jaeger 中可视化了依赖关系。仅凭指标无法获得这种智能。Docker 和 Jaeger 在这里改变了游戏规则。

总的来说，Docker 通过实现可移植性、一致性和简单的扩展，彻底改变了软件部署领域。然而，容器的瞬态性质带来了一些挑战：

*   容器可以频繁启动和停止，从而使监控更加复杂。
*   容器共享资源，可能会掩盖性能问题。
*   微服务通常异步通信，从而模糊了跟踪和可见性。

在 Docker 环境中部署可观测性解决方案使开发人员和运维人员能够深入了解容器中运行的应用程序。

## OpenTelemetry 和 Jaeger 简介

![](https://cdn.thenewstack.io/media/2025/05/dfc2ba09-image2.png)

**OpenTelemetry**

OpenTelemetry 是一个开放的 CNCF 标准，专为云原生应用程序中的检测、跟踪和指标收集而设计。它可以轻松地在您的应用程序中提供一致的遥测数据，从而使可观测性更易于实施，数据分析更简单。

**Jaeger**

Jaeger 是一个开源的分布式跟踪系统，最初由 Uber 开发，在可视化和分析来自 OpenTelemetry 的跟踪数据方面非常有效。Jaeger 通过简单的仪表板提供实用的建议，从而帮助开发人员快速识别性能瓶颈和问题。

**Jaeger 的替代解决方案**
虽然 Jaeger 是一个强大的工具，但根据具体需求，可以考虑其他一些追踪工具：

- **Zipkin** 是一个优秀的替代方案，它具有类似的功能并且符合 OpenTelemetry 标准。
- **Elastic APM** 是一个完整的可观测性解决方案，原生支持追踪、指标和日志。
- **Datadog 和 New Relic** 是提供深度可观测性功能的专有软件。

然而，Jaeger 的开源特性以及与 Docker 的无缝集成使其特别适合需要经济实惠且灵活的解决方案的团队。

## 在 Docker 中设置 OpenTelemetry 和 Jaeger

**步骤 1：检测您的应用程序**

以 Node.js 微服务为例：

```javascript
// server.js
const express = require('express');
const { NodeTracerProvider } = require('@opentelemetry/sdk-node');
const { registerInstrumentations } = require('@opentelemetry/instrumentation');
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express');
const { JaegerExporter } = require('@opentelemetry/exporter-jaeger');

const provider = new NodeTracerProvider();
provider.addSpanProcessor(
  new (require('@opentelemetry/sdk-trace-base').SimpleSpanProcessor)(
    new JaegerExporter({ endpoint: 'http://jaeger:14268/api/traces' })
  )
);
provider.register();

registerInstrumentations({
  instrumentations: [new ExpressInstrumentation()],
});

const app = express();
app.get('/', (req, res) => res.send('Hello World'));
app.listen(3000);
```

**步骤 2：Dockerize 您的应用程序**

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

**步骤 3：使用 Docker Compose 部署**

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - jaeger
  jaeger:
    image: jaegertracing/all-in-one:1.55
    ports:
      - "16686:16686"
      - "14268:14268"
```

Run your environment with:

```bash
docker compose up
```

Access Jaeger UI at http://localhost:16686 to explore tracing data.

## 大规模实施的实际经验：

将此配置应用于高流量生产系统中的许多微服务，我们学到了重要的一课：可观测性不是事后才考虑的事情，而是基础设施不可或缺的一部分。借助提供可扩展性的容器编排，以及提供对系统巨大可见性的追踪，从基础设施团队到前端团队的每个团队都可以在解决边缘案例时依赖相同的追踪 ID；这种能力在早期使用断开连接的日志记录方法时是无法实现的。

**实际用例和行业示例**

Jaeger 被包括 Uber、Red Hat 和 Shopify 在内的主要技术公司大量使用，以实现实时可观测性。这些组织使用分布式追踪来实现：

- 快速检测微服务的性能下降
- 通过主动检测延迟问题来改善最终用户体验。
- 通过
  [及时检测和解决](https://thenewstack.io/how-we-slashed-detection-and-resolution-time-in-half/)事件来确保高可靠性。

## 高级可观测性技术

**分布式上下文传播**

利用 OpenTelemetry 自动 HTTP 标头传播来维护服务之间的追踪上下文。

**自定义 Span 创建**

```javascript
const axios = require('axios');

app.get('/fetch', async (req, res) => {
  const result = await axios.get('http://service-b/api');
  res.send(result.data);
});
```

通过手动定义 span，更深入地了解复杂的函数。

```javascript
const { trace } = require('@opentelemetry/api');

app.get('/compute', (req, res) => {
  const span = trace.getTracer('compute-task').startSpan('heavy-computation');
  // Compute-intensive task
  span.end();
  res.send('Done');
});
```

**将可观测性集成到 CI/CD 管道中**

将可观测性检查集成到持续集成和持续部署管道（例如 GitHub Actions）中非常重要，以确保代码更改满足可见性预期。

```yaml
name: CI Observability Check

on: [push]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Docker Compose
        run: docker compose up -d
      - name: Observability Verification
        run: curl --retry 5 --retry-delay 10 --retry-connrefused http://localhost:16686
```

## 可观测性的未来

![](https://cdn.thenewstack.io/media/2025/05/ab87a277-image4.png)

可观测性继续快速发展，尤其是在 AI 驱动的分析和预测监控功能方面。新兴趋势包括：

- 自动异常检测
- AI 辅助的
  [根本原因分析](https://thenewstack.io/machine-learning-for-automated-root-cause-analysis-promise-and-pain/)
- 改进的预测警报可以及早预防事件。

OpenTelemetry 和 Jaeger 是领先的技术，使组织能够在未来的部署中利用改进的可观测性。
随着越来越多的团队部署 AI/ML 服务，可观测性必须不断提高。我亲身经历过将 LLM 服务集成到容器管道中的过程，我发现模型行为变得多么不透明。OpenTelemetry 和类似技术现在开始填补这一空白，并且能够在同一时间线上看到推理、延迟和系统交互，这在 AI 原生世界中至关重要。

## 结论

OpenTelemetry 和 Jaeger 的集成用于显着增强 Docker 环境中的可观测性，从而提高[更有效地监控和管理分布式系统的能力](https://thenewstack.io/the-10-fundamental-principles-of-effective-monitoring/)。这些技术结合使用时，可产生实时的、可操作的情报，从而促进有效的故障排除，提高性能，并为团队保持高可用性。随着越来越多的组织采用容器化和微服务，理解可观测性的最佳实践已成为实现运营成功的关键组成部分。