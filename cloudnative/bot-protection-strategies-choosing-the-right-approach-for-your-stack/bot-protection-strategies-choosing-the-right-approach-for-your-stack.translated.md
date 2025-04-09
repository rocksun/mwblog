# 一种用于防御恶意机器人的云原生方法

![用于：一种用于防御恶意机器人的云原生方法的特色图片](https://cdn.thenewstack.io/media/2025/04/b913ec79-bots12-1024x576.png)

[机器人流量](https://thenewstack.io/can-you-bot-proof-your-applications-and-apis/)分为有益机器人和恶意机器人。有益机器人，如搜索引擎爬虫、正常运行时间监控器和存档服务，通常遵守站点策略并贡献价值。恶意机器人从事数据抓取、凭据填充、DDoS 攻击和垃圾邮件活动，通常忽略传统的访问控制，如 `robots.txt`。

最近的报告显示，大约[一半的网络流量是机器人](https://securitybrief.co.uk/story/half-of-online-traffic-in-2024-generated-by-bots-report-finds)，并且“坏”机器人占[越来越高的比例](https://www.statista.com/statistics/1264226/human-and-bot-web-traffic-share/)。AI 机器人是这一流量中不断增长的一部分，一些公司的数据显示，高达[90% 的 AI 机器人流量](https://www.haproxy.com/blog/nearly-90-of-our-ai-crawler-traffic-is-from-tiktok-parent-bytedance-lessons-learned)来自单一来源。这些爬虫通常通过模仿合法用户来绕过现有的保护措施，需要更高级的解决方案，将流量分析与[机器人检测](https://www.haproxy.com/blog/bot-protection-with-haproxy)算法相结合，以实现准确识别。

基础设施的多样性增加了挑战。组织在裸机服务器、Kubernetes 集群和无服务器平台上运行工作负载——每个平台都有自己的安全约束和要求。这造成了“多-多”问题：多个工具保护多个堆栈，跨越多个环境，每个环境都有不同的需求。根据 [OWASP 自动化威胁项目](https://owasp.org/www-project-automated-threats-to-web-applications/)，这种异构的格局使得基于独立服务的方法越来越无效。

这个问题很复杂，但我们可以分三个层次来管理它：流量管理，用于控制入口点的请求；策略驱动的安全，用于大规模管理安全；以及边缘保护，用于在威胁到达内部系统之前阻止它们。一种[云原生方法](https://thenewstack.io/cloud-native/10-key-attributes-of-cloud-native-applications/)统一了这些层，确保了适应性强、可扩展的安全，并随着新兴威胁的发展而发展。

## 流量管理

对于那些在流量管理中寻求更大控制和性能的人来说，开源代理是一个标准的解决方案。与第三方服务相比，代理级别的实现增加了最小的延迟，但提供了强大的机器人缓解。这些技术使用多种防御机制来识别和阻止恶意流量模式，包括高级速率限制系统、[访问控制列表](https://thenewstack.io/a-guide-to-linux-access-control-lists/) (ACL) 和灵活的响应策略，以应对不断演变的机器人威胁。

拥有一个有效的速率限制系统至关重要，该系统可以有效地缓解不断演变的机器人威胁，同时保持最小的资源开销和误报。有效的系统将灵活的算法与多种识别方法相结合——跟踪 IP 地址、浏览器指纹、会话 cookie、请求的 URL 和自定义标头作为复合键。这种方法应包括允许/拒绝列表、基于地理位置的限制和自适应速率限制规则，这些规则可以检测各种攻击向量的模式，包括暴力破解尝试、网络抓取和会话劫持。

根据特定的威胁配置文件，可以部署滑动窗口和固定窗口速率限制。由于攻击者不断修改他们的技术，系统必须保持适应性，同时不牺牲性能。进一步的增强包括跨集群的分布式速率限制和基于历史分析的动态阈值计算。

例如，代理使用诸如 [stick tables](https://docs.haproxy.org/3.1/intro.html#3.4.5) 在 [HAProxy](https://www.haproxy.com/?utm_content=inline+mention) 或 [shared memory zones](http://nginx.org/en/docs/dev/development_guide.html#shared_memory) 在 [NGINX](https://www.nginx.com?utm_content=inline+mention) 等技术来实现对请求模式的实时监控，并帮助检测恶意活动，如 DDoS 攻击、凭据填充和网络抓取。

响应策略选项可能包括使用 CAPTCHA（可见或不可见）挑战请求、限制响应带宽或将请求定向到蜜罐。此外，如果后端过载，基于优先级的排队可以优先处理某些请求（例如登录用户）而不是其他请求。
当使用自定义资源定义 (CRD) 来启用声明式流量策略配置时，流量管理将变得更加强大。团队可以将复杂的机器人防护规则定义为[原生 Kubernetes 资源](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)，使用 GitOps 工作流程并在集群中标准化策略管理。与云原生安全模型的集成可确保一致的、可扩展的保护。

## 策略驱动的安全

为了解决“多重”问题，组织需要一个统一的策略，将流量管理与平台级的策略驱动的安全集成在一起。这种方法可以实现细粒度的流量控制、[策略执行和实时可观测性](https://thenewstack.io/real-time-policy-enforcement-with-governance-as-code/)。

云原生技术实现了关注点分离：集中的[控制平面](https://www.haproxy.com/glossary/what-is-a-control-plane)管理安全策略，而分布式的[数据平面](https://www.haproxy.com/glossary/what-is-a-data-plane)在流量处理层执行这些策略。这种架构允许团队根据上下文调整保护级别，而无需重复工作，从而确保在不同环境中实现一致的安全（和合规性）。

与机器人防护提供商通常提供的独立安全控制平面相比，统一的控制平面架构可以提供显著的优势。这些优势包括减少延迟、简化操作以及集成其他原生交付和安全功能的能力。此外，统一的控制平面可以通过自动将较低级别的安全构建块与以威胁为中心的缓解策略相结合，从而简化实施多层安全策略的复杂性。

可观测性完善了这个反馈循环，将被动安全转变为主动实践。[OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver) 检测使团队能够跟踪可疑的请求模式，而 [Prometheus](https://prometheus.io/blog/2015/04/24/prometheus-monitring-spreads-through-the-internet/#using-prometheus) 指标提供实时异常检测。实时可见性使团队能够通过调整速率限制、IP 信誉评分和有针对性的对策来不断改进其防御。

## 边缘保护

边缘层安全通过过滤高风险流量来提高性能并减少攻击面。精心设计的边缘网络不仅可以加强安全性并改善用户体验，还可以通过卸载机器人缓解和优化资源消耗来降低基础设施成本。

边缘的 AI 驱动检测至关重要，它使用实际的流量模式来动态地改进机器人缓解策略。机器学习模型不断适应新兴威胁，确保防御在规模上保持有效。系统应该定期使用机器学习分析整个网络的流量，而不是对每个请求执行资源密集型分析，以识别新的威胁和模式，然后实时更新过滤算法，以保持效率而不增加延迟。

虽然托管边缘服务简化了操作，但构建您[自己的云原生边缘网络](https://www.haproxy.com/user-spotlight-series/how-oui-sncf-built-its-cdn-with-haproxy)可以提供更大的控制、成本效益和灵活性。云原生方法使用相同的工具来实现这一点，这些工具为流量管理和平台级编排提供支持，从而确保无缝集成和可扩展性。自我管理的边缘提供定制的安全策略，减少对第三方服务的依赖，并启用统一的堆栈，该堆栈在所有层应用相同的云原生原则，以实现一致的、可扩展的安全性。

## 设计您的方法

机器人防护策略的选择取决于组织环境，包括技术专长、可扩展性需求和合规义务。机器人防护应从代理级别的控制开始，在数据平面上实施速率限制和访问策略，以减轻直接威胁。

在规模上，策略驱动的安全和统一的控制平面解决方案可确保在分布式环境中实现一致的执行。组织应采用云原生解决方案，以统一内部和外部保护，从而实现长期的安全一致性。Kubernetes 和 GitOps 工作流程支持可扩展的、自动化的安全执行，该执行随着新兴威胁而发展。

边缘安全为外部流量提供了一条扩展的防线，在恶意请求到达内部基础设施之前对其进行过滤。这种方法最大限度地减少了攻击面暴露，同时保持了合法用户的性能。
通过分层应用这些方法，组织可以实施自适应、可扩展的机器人缓解措施，确保其基础设施保持安全，同时不影响效率和简易性。

*要了解更多关于 Kubernetes 和云原生生态系统的信息，请于 4 月 1 日至 4 日在伦敦加入我们的 KubeCon + CloudNativeCon 欧洲会议。*

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)