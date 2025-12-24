<!--
title: 云原生全链路可观测框架
cover: https://cdn.thenewstack.io/media/2025/12/351875d0-observabiity.jpg
summary: 本文强调端到端可观测性对云原生系统至关重要，涵盖应用追踪、Kubernetes和CI/CD。通过OpenTelemetry、日志、指标与AI，实现快速故障排除和系统健康。
-->

本文强调端到端可观测性对云原生系统至关重要，涵盖应用追踪、Kubernetes和CI/CD。通过OpenTelemetry、日志、指标与AI，实现快速故障排除和系统健康。

> 译自：[An End-to-End Cloud Native Observability Framework](https://thenewstack.io/an-end-to-end-cloud-native-observability-framework/)
> 
> 作者：Khushboo Nigam

可观测性对于理解我们的系统性能以及何时出现问题至关重要，这一点已经毋庸置疑。在我与采用可观测性服务来支持其关键云原生工作负载的企业合作过程中，我看到可观测性是孤立地被采用的。请求常常是分离的：侧重于应用程序跟踪，或仅关注Kubernetes指标/日志，或仅关注CI/CD[管道遥测](https://thenewstack.io/the-case-for-telemetry-pipelines/)。

然而，我的方法是从第一天起就考虑端到端的可观测性，而不是将其视为事后附加。

这里展示了一个端到端的[可观测性](https://thenewstack.io/introduction-to-observability/)框架，它使用一个简单的双微服务应用程序，通过CI/CD管道构建/部署在托管的Kubernetes集群上。它侧重于可以从每个层——应用程序、[Kubernetes](https://thenewstack.io/kubernetes/)和[CI/CD](https://thenewstack.io/introduction-to-ci-cd/)——收集的遥测数据，以及每个层如何有助于更快的故障排除和更好的系统健康状况。

## **应用程序和可观测性架构**

图1展示了包括遥测数据收集在内的架构。演示应用程序包括两个微服务——retail-web和retail-api——运行在云环境中的托管Kubernetes集群上。对于此应用程序，可观测性通过以下策略覆盖：

*   应用程序的跟踪数据使用[OpenTelemetry 收集器](https://opentelemetry.io/docs/collector/)进行收集，它提供了一种与供应商无关的方式来接收、处理和导出遥测数据。
*   Kubernetes集群的日志使用[fluentd](https://www.fluentd.org/) daemonset（每个节点一个日志收集Pod）进行收集。
*   Kubernetes基础设施指标使用云平台专有代理进行收集。这也可以使用Prometheus Node Exporter来完成。

由于此应用程序运行在云平台上，因此从CI/CD管道、计算节点和Kubernetes控制平面等云原生组件收集的遥测数据通过平台的[可观测性]服务收集。

此演示零售应用程序专注于一个功能：结账请求。[用户的结账请求到达负载均衡器](https://thenewstack.io/stop-losing-users-the-load-balancing-fix-your-website-needs/)，并由调用API后端的web前端处理。API后端随后执行三个关键操作——检查库存、收取付款和创建订单，然后所有这三个操作都会访问数据库。出于演示目的，API后端使用SQLite；在生产环境中，这将是托管数据库服务。无论底层数据库如何，可观测性模式仍然适用。

**注意**：托管Kubernetes环境还包括其他几个云管理组件，例如[网络和负载均衡](https://thenewstack.io/zero-trust-for-legacy-apps-load-balancer-layer-can-be-a-solution/)。同样重要的是要启用并监控它们的遥测数据，因为这些服务直接影响Kubernetes工作负载的可靠性。

[![](https://cdn.thenewstack.io/media/2025/12/5c123218-image8.png)](https://cdn.thenewstack.io/media/2025/12/5c123218-image8.png)

*图1*

## **使用OpenTelemetry捕获应用程序跟踪**

跟踪捕获单个用户请求的端到端旅程。单个跟踪由多个跨度组成，具体取决于请求如何遍历分布式系统。在我的应用程序中，单个用户请求从用户点击UI上的“Checkout”（结账）按钮开始，然后移至后端和SQLite数据库。跟踪此请求的单个跟踪将有多个跨度，在此示例中，各个跨度将捕获每个HTTP请求和操作，例如“verifying inventory”（验证库存）、“executing payment”（执行支付）和“create order”（创建订单），如图2所示。

[![Trace = Collection of Spans](https://cdn.thenewstack.io/media/2025/12/45f35491-image10.png)](https://cdn.thenewstack.io/media/2025/12/45f35491-image10.png)

*图2*

该应用程序结合使用了OpenTelemetry的自动插桩（用于Flask和HTTP调用）和手动跨度（围绕业务逻辑阶段），所有跨度都通过OpenTelemetry (OTel) Collector导出，OTel Collector在将其发送到云原生应用程序性能服务之前，会用Kubernetes元数据丰富它们。

图3显示了我的遥测模块中的一段代码，其中我定义了一个自定义的`bootstrap()`函数。该函数通过设置`service.name`、`service.namespace`和`deployment.environment`等资源属性来配置我的服务的OpenTelemetry。这些属性成为每个跨度的一部分。

在同一个函数内部，我初始化了一个OpenTelemetry TracerProvider并附加了一个OTLP (OpenTelemetry Protocol) span exporter，这是负责将跨度发送到管道中下一个目标（在本例中是OTel Collector）的组件。

[![](https://cdn.thenewstack.io/media/2025/12/445f4526-image9.png)](https://cdn.thenewstack.io/media/2025/12/445f4526-image9.png)

*图3*

### **如果您不熟悉OpenTelemetry：**

OpenTelemetry Protocol (OTLP) 是遥测信号（跟踪、日志、指标）在组件之间传输的标准方式。OTLP span exporter将跨度发送到配置的任何OTLP端点。

尽管OTLP span exporter可以直接将跟踪发送到应用程序性能监控 (APM) 后端，但我有意将其发送到OTel Collector。原因有两点：

1.  **供应商中立性和面向未来。**
    当收集器位于应用程序和APM后端之间时，我可以将相同的跟踪路由到任何后端（Grafana Tempo、Jaeger、[云原生APM](https://thenewstack.io/streamlined-apm-integration-in-cloud-native-buildpacks/)服务等），而无需修改应用程序代码。
2.  **跨度丰富和处理。**
    我使用收集器将Kubernetes元数据（Pod名称、节点名称、部署等）注入到跨度中。如果需要，收集器还可以执行批处理、采样、转换和路由。

图4显示了一段代码，其中`bootstrap()`内部有一个自动插桩部分。在这里，我为以下组件启用了OpenTelemetry的插桩库：

1.  **Requests** (Python的HTTP客户端) 用于在应用程序进行出站HTTP调用（例如`retail-web`调用`retail-api`）时自动创建客户端跨度。
2.  **Flask** 用于在应用程序接收入站HTTP请求时自动创建服务器端跨度。

如果没有`RequestsInstrumentor`，下游API调用将不会显示为同一个跟踪的一部分，并且分布式父子关系将丢失。Flask插桩处理入站流量，而requests插桩处理出站调用。由于微服务通常会相互调用，因此两者都必不可少以维护完整的分布式跟踪。

[![](https://cdn.thenewstack.io/media/2025/12/e15ecf5f-image12.png)](https://cdn.thenewstack.io/media/2025/12/e15ecf5f-image12.png)

*图4*

图5显示了应用程序文件 (app.py) 中的一段代码片段，其中在创建Flask应用程序实例后立即调用了`bootstrap()`函数。这就是激活运行服务的自动插桩并应用先前定义的资源属性的过程。

[![](https://cdn.thenewstack.io/media/2025/12/7212aca8-image11.png)](https://cdn.thenewstack.io/media/2025/12/7212aca8-image11.png)

*图5*

手动插桩意味着在应用程序代码中明确创建跨度，以捕获业务逻辑、数据库操作或任何自动插桩无法推断的工作。

在retail-web服务中，当`/checkout/execute`处理程序运行时，Flask自动插桩已经为HTTP请求创建了一个SERVER跨度。在处理程序中，我使用`trace.get_current_span()`获取该跨度，然后添加一个名为`Process_Checkout_Flow`的手动父跨度，其中包含三个子跨度：`Verify_Inventory_Status`、`Execute_Payment_Charge`和`Create_Order_Record`。`Process_Checkout_Flow`位于HTTP级别的SERVER跨度与这些业务步骤之间。这些跨度直接映射到我的业务步骤，我附加了`retail.flow`和`retail.stage`等属性，以便以后可以按流程和阶段过滤跟踪。

下面的图6是显示验证库存步骤的手动父跨度和业务跨度的代码。

[![](https://cdn.thenewstack.io/media/2025/12/d587aec6-image14.png)](https://cdn.thenewstack.io/media/2025/12/d587aec6-image14.png)

*图6*

下面的图7显示了一个结账请求的完整跨度树。第一个跨度，`retail-web: POST /checkout/execute`，是Flask自动插桩自动创建的入口点服务器跨度。接下来的跨度，`retail-web: Process_Checkout_Flow`及其下面的嵌套跨度（库存检查、支付费用和订单创建）是手动插桩的。这些手动跨度来自图6中所示的代码级插桩。

[![](https://cdn.thenewstack.io/media/2025/12/e3a92efa-image13.png)](https://cdn.thenewstack.io/media/2025/12/e3a92efa-image13.png)

*图7*

自动插桩和手动插桩的跨度服务于不同的目的。如果延迟来自自动插桩的跨度，则可能归因于网络连接问题等开销进程；而如果延迟来自手动插桩的跨度，则主要是由于应用程序逻辑（例如低效的循环）造成的。

OpenTelemetry 生成三种类型的跨度：

*   **服务器跨度**——当服务接收到传入的HTTP请求时创建（例如retail-web接收`POST /checkout/execute`，retail-api接收`GET /inventory/check`）。
*   **客户端跨度**——当服务发出传出的HTTP调用时创建（例如retail-web调用retail-api）。这些显示了往返的传出部分。
*   **内部跨度**——在服务内部创建的跨度，表示内部工作单元。所有手动跨度（例如`Process_Checkout_Flow`、`Verify_Inventory_Status`、`Execute_Payment_Charge`、数据库操作）都属于此类，因为它们表示在服务内部执行的代码级操作，并且我没有明确将跨度类型设置为任何其他类型。下面的图8显示了跨度树中不同类型的跨度。

[![](https://cdn.thenewstack.io/media/2025/12/3a83c00c-image16.png)](https://cdn.thenewstack.io/media/2025/12/3a83c00c-image16.png)

*图8*

我使用OTel Collector来丰富带有Kubernetes上下文的跨度。图9展示了我如何配置OTel Collector来提取Kubernetes元数据。

[![](https://cdn.thenewstack.io/media/2025/12/42f0256a-image15.png)](https://cdn.thenewstack.io/media/2025/12/42f0256a-image15.png)

*图9*

一旦应用此配置，通过收集器发送的每个跨度都将包含Kubernetes属性，如图10所示。这种丰富在故障排除性能问题时变得极其有价值。如果一个跨度变慢，我可以立即看到是哪个Pod和节点执行了代码。

[![](https://cdn.thenewstack.io/media/2025/12/0a284913-image19.png)](https://cdn.thenewstack.io/media/2025/12/0a284913-image19.png)

*图10*

## **托管Kubernetes环境的可观测性**

在云平台上的托管Kubernetes环境中，存在一个共享责任模型。云提供商管理Kubernetes控制平面组件，例如API服务器、etcd、调度器、控制器管理器、节点供应，并且仅暴露平台选择提供的控制平面日志或指标。节点内部运行的一切（Pod、容器、应用程序进程）完全由用户管理，用户需要拥有自己的可观测性设置。

本质上，虽然所有主要的托管平台（Oracle、Google、Amazon、Azure）都为其托管Kubernetes暴露控制平面指标，但用户通常必须选择加入或使用提供商的原生监控解决方案来消费它们。基本的控制平面指标包括API服务器请求、API服务器请求延迟和etcd延迟，以了解控制平面的性能，并在发现意外行为时向云提供商提出服务工单。

**节点健康** – 了解节点健康状况很重要，因为节点是应用程序工作负载运行的基础。一个好的起点是关注节点级指标，因为它们是资源耗尽的早期预警系统。图11显示了属于Kubernetes集群的3个节点的CPU利用率。我们在这里看到三个节点之间的均匀分布，这是健康的。如果一条指标线在10%而另一条在95%，那将表明一个节点过载而另一个节点利用不足。

[![](https://cdn.thenewstack.io/media/2025/12/e5871842-image17.png)](https://cdn.thenewstack.io/media/2025/12/e5871842-image17.png)

*图11*

日志也能提供洞察力。日志有助于故障排除，但它们也能提供很好的概述，例如图12所示的节点健康摘要。通过这个小部件，我突出显示了每个节点的三个压力值，这些值有助于节点托管Pod的就绪状态。这些条件直接来自kubelet，并在节点状态中显示。

[![](https://cdn.thenewstack.io/media/2025/12/dae63044-image18.png)](https://cdn.thenewstack.io/media/2025/12/dae63044-image18.png)

*图12*

节点与Pod的关联性很重要，它提供了运行在节点上的Pod的状态。图13展示了一个基于机器学习的可视化，它将多个维度结合在一起：节点、命名空间、Pod状态和Pod数量。这使得很容易发现模式，例如Pod放置不均匀、Pod卡在Pending/Failed状态或节点持续托管有问题的工作负载。这就是可观测性的真正力量：能够看到关系而不是孤立的指标。

[![](https://cdn.thenewstack.io/media/2025/12/0b75a7d2-image21.png)](https://cdn.thenewstack.io/media/2025/12/0b75a7d2-image21.png)

*图13*

**Pod健康**

Pod的日志可以用于提供快照，如图14所示，其中显示了所有运行中Pod的详细信息，包括命名空间、位置、控制器和控制器类型。

[![](https://cdn.thenewstack.io/media/2025/12/106f08fb-image22.png)](https://cdn.thenewstack.io/media/2025/12/106f08fb-image22.png)

*图14*

但要理解Pod健康状况，仅仅知道Pod阶段（Running / Pending / Succeeded / Failed / Unknown）是不够的。Pod可能显示Running阶段，但实际上仍然不健康，因为阶段仅反映生命周期状态，而不是容器是否可达或正常运行。

图15就是一个很好的例子。突出显示的Pod阶段是running，但当我将其与Kubernetes事件关联时，我发现了“readiness probe failure”（就绪探针失败）。这种关联揭示了实际情况：Pod状态不等于Pod健康。健康取决于就绪性、活跃性、重启次数和探针失败等信号。这些很少单独在高层阶段中显示。这就是可观测性通过将Pod日志、事件和指标连接起来，使“真实”健康状况可见的方式。

[![](https://cdn.thenewstack.io/media/2025/12/4c315567-image23.png)](https://cdn.thenewstack.io/media/2025/12/4c315567-image23.png)

*图15*

## **从CI/CD管道可观测性中获取洞察**

在CI/CD设置中，指标和日志为开发人员提供了反馈循环，从而提高了可靠性并加速了代码交付。在这里，我使用云原生DevOps遥测技术，重点关注retail-web和retail-api微服务的构建和部署管道的[可观测性]信号。

### **构建管道趋势**

图16和图17显示了零售微服务的成功和失败构建趋势的指标图。

对于成功构建，我们希望看到这条线保持健康水平，但如果成功构建线相对于预期构建数量下降，它会告诉我们关于正在合并的代码质量或测试环境稳定性的重要信息。

[![](https://cdn.thenewstack.io/media/2025/12/cb22aa80-image24.png)](https://cdn.thenewstack.io/media/2025/12/cb22aa80-image24.png)

*图16*

失败构建图是开发人员挫折感的时间线。立即引人注目的是浅蓝色线的巨大峰值，代表了retail-api管道。这立即促使DevOps工程师提问：“在此之前提交了什么？我们是否引入了破坏性更改、不兼容的依赖项或配置错误？”

[![](https://cdn.thenewstack.io/media/2025/12/06cde2c4-image26.png)](https://cdn.thenewstack.io/media/2025/12/06cde2c4-image26.png)

*图17*

### **构建运行持续时间 (P95)**

接下来，我们来看看P95构建运行持续时间，它告诉我们代码通过构建和测试过程所需的时间。

什么是P95？P95构建持续时间告诉我们95%的构建需要多长时间，这比平均值有用得多。

图18和图19显示了一个一致的模式，即失败的构建比成功的构建花费的时间明显更长。这表明在本例中，故障发生较晚，在漫长的测试运行之后。

[![](https://cdn.thenewstack.io/media/2025/12/1f7e2ee3-image27.png)](https://cdn.thenewstack.io/media/2025/12/1f7e2ee3-image27.png)

*图18*

[![](https://cdn.thenewstack.io/media/2025/12/9a795148-image28.png)](https://cdn.thenewstack.io/media/2025/12/9a795148-image28.png)

*图19*

解决方案是“左移”：提早增加验证，以便构建快速失败，从而节省计算时间并改善开发人员体验。

### **部署管道趋势**

图20显示了retail-web和retail-api管道每小时的部署失败计数。

请注意，retail-web管道（深蓝色）显示出持续的失败水平，并带有明显的峰值。这告诉我们问题不一定出在代码本身，因为它通过了构建。这表明存在环境或配置问题，例如镜像拉取错误、网络超时、缺少密钥或Kubernetes API限流。

[![](https://cdn.thenewstack.io/media/2025/12/9a54c6d0-image29.png)](https://cdn.thenewstack.io/media/2025/12/9a54c6d0-image29.png)

*图20*

观察部署失败有助于将代码级问题与集群级问题区分开来，这使得[开发人员在DevOps团队调试实际瓶颈时保持专注](https://thenenewstack.io/2-ways-to-reduce-bottlenecks-with-the-theory-of-constraints/)。

### **部署执行时间 (P95)**

两种服务的P95部署持续时间都显示出高方差，如图21和图22所示，带有剧烈的峰值。我们看到的是高而剧烈的峰值和下降，而不是一条平坦、稳定的线条。

部署代码所需的时间非常不可预测。有一天可能需要一分钟，而另一天部署可能需要超过11分钟。

调查CI/CD系统的日志有助于确定是注册表、网络、集群API还是回滚策略导致了减速。

[![](https://cdn.thenewstack.io/media/2025/12/be01c203-image4.png)](https://cdn.thenewstack.io/media/2025/12/be01c203-image4.png)

*图21*

[![](https://cdn.thenewstack.io/media/2025/12/a928e156-image5.png)](https://cdn.thenewstack.io/media/2025/12/a928e156-image5.png)

*图22*

## **从原始日志到AI智能洞察**

我们已经跟踪了构建和部署失败，但从数千行日志中诊断它们是痛苦的。这就是日志聚类成为真正加速器的原因。平台应用基于机器学习的聚类来自动将相似的日志模式分组在一起。

在图23中，来自retail-web构建管道的3000多条原始日志条目被简化为仅52个集群，立即突出显示了重复出现的问题和异常情况。

现在我们可以专注于大局：发现重复出现的失败特征或配置错误，这些错误否则可能会被噪音淹没。

[![](https://cdn.thenewstack.io/media/2025/12/dfe7d73c-image6.png)](https://cdn.thenewstack.io/media/2025/12/dfe7d73c-image6.png)

*图23*

更进一步，图24展示了AI助手如何用通俗的语言总结这些集群。通过关联52个集群中的日志，它可以揭示反复出现的错误背后可能的原因，例如为什么会出现“BUILD_EXECUTION Failed”或者它是否与认证问题、缺失依赖项或拉取速率限制重叠。

这并不能取代工程师的专业知识。相反，它充当了一个副驾驶，加速了推理，突出了日志模式之间的关系，并缩短了查找根本原因的时间。

[![](https://cdn.thenewstack.io/media/2025/12/65dddd84-image7.png)](https://cdn.thenewstack.io/media/2025/12/65dddd84-image7.png)

*图24*

**结论**

通过本文，我的目标是为读者提供一个实际的、端到端的可观测性视图，涵盖您的应用程序、Kubernetes环境和交付管道。我希望这些经验教训能帮助您以可观测性作为一流设计原则来构建系统。