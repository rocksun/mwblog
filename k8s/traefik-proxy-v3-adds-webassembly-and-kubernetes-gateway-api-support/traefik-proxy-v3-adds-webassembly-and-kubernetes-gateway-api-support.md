<!--
title: Traefik Proxy v3 重磅发布：支持 WebAssembly 和 Kubernetes Gateway API
cover: https://cdn.thenewstack.io/media/2024/02/7652637d-traffic-traefik-1024x576.jpg
-->

开源 Traefik Proxy v3 发布，新增 WebAssembly、Kubernetes Gateway API 和 OpenTelemetry 支持！

> 译自 [Traefik Proxy v3 Adds WebAssembly and Kubernetes Gateway API Support](https://thenewstack.io/traefik-proxy-v3-adds-webassembly-and-kubernetes-gateway-api-support/)，作者 Steven J. Vaughan-Nichols 是一位资深的科技作家，自 CP/M-80 时代起就开始撰写有关技术和技术业务的文章。

领先的开源反向代理和负载均衡器 [Traefik Proxy](https://traefik.io/traefik/) 正在增加更多[云原生](https://thenewstack.io/cloud-native/what-is-cloud-native-and-why-does-it-matter/)支持。

自一切都是用 Linux、Apache、MySQL、Perl/PHP/[Python](https://thenewstack.io/python/) (LAMP) 堆栈编写的时候起，反向代理和负载平衡软件对于将后端服务与前端接口连接起来至关重要。

然后，云原生计算来了，事情变得更加复杂。正如 Traefik 的创建者 [Emile Vauge](https://github.com/emilevauge) 之前在新兴技术栈中所说，“传统的反向代理不适合这些动态环境。”现在，开源 Traefik Proxy 已经成功解决了这个问题将近十年，它正在进一步扩展其云原生支持。

周三，该项目的母公司 Traefik Labs 推出了 Traefik Proxy v3 的第一个候选版本。这个新版本现在支持 [WebAssembly (Wasm)](https://thenewstack.io/webassembly/)、[OpenTelemetry](https://thenewstack.io/opentelemetry-and-observability-looking-forward/) 和 [Kubernetes Gateway API](https://thenewstack.io/kubernetes-api-gateway-1-0-goes-live-as-maintainers-plan-for-the-future/)。

## WebAssembly 的游戏规则改变者？

WebAssembly 支持的加入可能会改变游戏规则。除了为无服务器和容器化应用程序提供高性能、语言无关的功能之外，Traefik 的支持还为 Wasm 提供了更大的潜在市场。

“这对于 Traefik 来说是一个迈向低摩擦可扩展性的重要步骤，因为它将其更广泛的插件纳入了其不断增长的生态系统，同时为开发人员提供了出色的体验。插件可以用不同的语言编写并直接编译成 Wasm，”[开放全球应用安全项目](https://owasp.org/) (OWASP) [Coraza](https://coraza.io/) 项目（Web 应用程序防火墙）的联合负责人 [Jose Carlos Chavez](https://github.com/jcchavezs) 在一份声明中说。

集成 OpenTelemetry 将为用户提供更好的应用程序可见性。 OpenTelemetry 是一种用于标准化日志记录、指标和跟踪格式的协议。它可以通过 [OpenTelemetry 协议](https://opentelemetry.io/docs/specs/otel/protocol/) (OTLP) 进行传输。

由于 [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) 还支持 [Prometheus](https://www.cncf.io/projects/prometheus/) 和 [Zipkin](https://zipkin.io/) 等较旧的数据收集程序，这也将是 Traefik 扩展其可用性的方式。 当然，这将有助于网络管理员和开发人员进行故障排除和性能优化。

“我们公司已经在许多 [Kubernetes](https://thenewstack.io/kubernetes/) 生产部署中广泛使用 Traefik，”芬兰电信公司 [Elisa](https://elisa.com/) 的云架构师 [Jesse Haka](https://github.com/zetaab) 在一份声明中说。Haka 是一位 Traefik Wasm 和 OpenTelemetry 开源贡献者。

“我们渴望部署 Traefik 的这个新版本，以解锁 Wasm 和 OpenTelemetry 支持，这些都是为我们打开新可能性的关键技术。”

## Kubernetes Gateway API 支持

最后，Traefik Proxy 对 [Kubernetes Gateway API](https://thenewstack.io/how-the-kubernetes-gateway-api-beats-network-ingress/) 的新支持代表了简化 Kubernetes 环境中路由管理和配置的重大举措。 添加的 Gateway API 支持提供了一种标准化的方法来管理和配置第 4 层和第 7 层 Kubernetes 路由。

即使没有这些改进，Traefik Proxy 仍然是云原生 API 网关领域的基石，迄今为止已下载 30 亿次。

对于已经使用 Traefik 的用户来说，一个好消息是 Traefik Labs 优先考虑从 Traefik Proxy v2 到 v3 的平滑过渡。这确保了向后兼容性，并为新语法提供渐进式采用路径。

Traefik Labs 首席技术官 Vauge 在一份声明中强调了应用程序代理在当今云原生世界中的重要性：“应用程序代理对于管理网络流量、确保高可用性和安全性至关重要。借助 v3，Traefik Proxy 成为云原生应用程序堆栈中更加重要的组件，提供无与伦比的易用性和强大功能。”
