<!--
title: 你的容器能跑起来，但别让周边环境成为你的负担
cover: https://cdn.thenewstack.io/media/2026/08/9bac07c4-zyanya-citlalli-xtsvy5rarpy-unsplash.jpg
summary: 本文介绍了 Amazon ECS Express Mode，旨在简化容器化应用的部署流程。它通过单一接口提供负载均衡、自动扩缩容、灰度发布等功能，让开发者无需管理复杂的基础设施配置，即可实现高效、可扩展的生产级服务部署。
-->

本文介绍了 Amazon ECS Express Mode，旨在简化容器化应用的部署流程。它通过单一接口提供负载均衡、自动扩缩容、灰度发布等功能，让开发者无需管理复杂的基础设施配置，即可实现高效、可扩展的生产级服务部署。

> 译自：[Your container runs. Everything around it shouldn't be your problem.](https://thenewstack.io/amazon-ecs-express-mode/)
> 
> 作者：Satej Sawant

容器的承诺很简单：如果它在你的本地机器上能运行，那么在生产环境中也能运行。这个承诺确实兑现了——你的容器确实能跑起来。但这需要付出代价：你需要配置容器周围的一切。为了连接到你的容器，你需要一个负载均衡器来路由流量，以及处理可变流量的扩展策略。接着还有网络组件和最小范围的访问角色。在清单的某个地方，别忘了安全配置；除非你想从合规团队那里听到关于它的投诉。在某个时刻，你可能会想，为什么不能直接回到开发工作中去呢？

> “你提供一个容器镜像。你得到一个生产服务。当你的工作负载超出了单个容器的承载能力时，你也不会超出 Amazon ECS Express Mode 的能力范围。”

听起来耳熟吗？你并不孤单。大多数团队在有信心将容器部署到生产环境之前，都会耗费大量时间。这些时间本该用于路线图上的任务，却被消耗在那些无法让你业务产生差异化的决策上。在第三个 Terraform 模块和第二个 [IAM 策略审查](https://thenewstack.io/how-iam-missteps-cause-data-breaches/) 之间，你已经失去了容器本应赋予你的速度。

Amazon Elastic Container Service (ECS) 是 AWS 上一些最大生产工作负载背后的容器编排引擎。但直到现在，使用它意味着在部署任何东西之前，你必须了解负载均衡器、网络、IAM 角色和扩展策略。

我们试图改变这种状况，让你更容易上手，并让你在 [发布 Amazon ECS Express Mode](https://aws.amazon.com/about-aws/whats-new/2025/11/announcing-amazon-ecs-express-mode/) 后专注于开发。Express Mode 是连接同一引擎的一个新接口。你并没有为了简单而牺牲性能。你获得的是通往已经过实战检验的基础设施的更快捷的通道。愿景很明确：保持简单但可扩展。你提供一个容器镜像和两个 IAM 角色；你就能在 Fargate 上获得一个运行 HTTPS 服务的环境，包含负载均衡器、TLS 证书、自动扩缩容和金丝雀部署。哦，所有这些资源都运行在你的账户中，你拥有完全的控制权。

```
 // Sample Terraform Code
 resource "aws_ecs_express_gateway_service" "frontend_service" {
   execution_role_arn = aws_iam_role.execution.arn
   infrastructure_role_arn = aws_iam_role.infrastructure.arn
 
   primary_container {
     image = "111122223333.dkr.ecr.us-east-1.amazonaws.com/my-service:1.4.2"
   }
 }
```

## Amazon ECS Express Mode 包含什么？

在这一步部署的背后，你得到的是：

* **无资源蔓延** – 每个服务都位于应用负载均衡器（ALB）之后，但并不占用专属的 ALB。一个 VPC 内最多 25 个 Express Mode 服务共享一个 ALB。Express Mode 仅在需要时添加负载均衡器，并在服务删除时移除它们。无需担心产生悬空资源。
* **更安全的发布** – 开箱即用，每次部署都是一次金丝雀发布，即 5% 的流量被路由到新版本并停留 3 分钟，之后转移剩余流量。如果你的 4xx/5xx 错误率超过 1%，我们为你创建的报警器将触发自动回滚。
* **扩展性** – 每个服务都配有自动扩展策略，默认目标为 60% 的 CPU 利用率，任务数量从 1 个扩展到最多 20 个。如果你的工作负载需要基于内存或请求数进行扩展，你也可以进行配置。
* **支持基础设施即代码 (IaC)** – 通过 CloudFormation、CDK、Terraform 或 GitHub Actions 创建和管理 Express 服务。
* **完全所有权** – 集群、负载均衡器、目标组、日志组和其他资源都位于你的 AWS 账户中。你可以检查它们、审计事件，并在需要时直接修改它们。没有任何黑盒。

### 那我的 Sidecar 怎么办？我的工作负载没那么简单。

迟早，随着应用的演进，工作负载将不仅仅是一个容器。一个可观测性代理需要在应用旁边运行，将追踪数据发布到你的监控解决方案中。基础镜像会被替换为安全团队维护的加固镜像。凭证会从环境变量转移到 Secrets Manager 中。这就是扩展性发挥作用的地方。

为此，[Express Mode 现在支持](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-express-mode-custom-task-def/) 提供标准的 ECS 任务定义——即描述你的容器、资源限制以及它们如何连接的规范。你的 Sidecar、镜像和凭证都可以直接嵌入其中。如果你的团队目前正在运行 ECS，这就是你已经在编写的规范。如果不是，Express Mode 会在你的账户中生成一个任务定义，当有需求时，你可以获取该工作规范，添加你需要的内容，并交回 ARN。一旦你将任务定义与 Express Mode 服务关联，你可以继续通过任务定义更新或直接通过 Express Mode 管理你的应用，任君选择。

```
// Sample CDK snippet
const taskDef = new ecs.FargateTaskDefinition(this, 'TaskDef', {
  cpu: 1024,
  memoryLimitMiB: 2048,
  executionRole,
  taskRole,
});
 
taskDef.addContainer('Main', {
image:
ecs.ContainerImage.fromRegistry('111122223333.dkr.ecr.us-east-1.amaz
onaws.com/my-service:1.4.2'),
  essential: true,
  portMappings: [{ containerPort: 8080, name: 'main' }],
});
 
taskDef.addContainer('otel-collector', {
image:
ecs.ContainerImage.fromRegistry('public. ecr.aws/aws-observability/aw
s-otel-collector:latest'),
  essential: false,
  memoryReservationMiB: 256,
  command: ['--config=/etc/ecs/ecs-default-config.yaml'],
});
 
new ecs.CfnExpressGatewayService(this, 'FrontendService', {
  infrastructureRoleArn: infrastructureRole.roleArn,
  taskDefinitionArn: taskDef.taskDefinitionArn,
});
```

## 等等，我会因为这个被锁定吗？

不会。Express Mode 是 Amazon ECS 的一个接口，而不是封闭的围墙。它创建的每个资源都是你账户中的标准 AWS 资源，可以通过 ARN 寻址。如有需要，你可以通过控制台、CLI 或 SDK 对应的 AWS API 直接修改它们。

> “Express Mode 是 Amazon ECS 的一个接口，而不是封闭的围墙。”

如果你更改了扩展策略、更新了安全组规则或替换了任务定义，Express 会在下一次更新时遵循这些修改。它不会覆盖你所做的更改。这意味着你可以从今天开始使用 Express 的默认设置，并随着需求的发展自定义单个资源，而无需迁移出 Express 或重建服务。

Express 还通过 Describe API 以及作为 CloudFormation/CDK 输出，公开了它所管理的所有内容的 ARN——包括负载均衡器、目标组、安全组和报警器。你可以在自己的堆栈中引用它们，或将它们交给现有的构建模块。

## 为什么我们将其设计为单一操作？

我们刻意将 Express Mode 设计为单一 API 调用，而不是多步骤工作流。一个输入（你的镜像或任务定义 ARN），一个操作，一个结果。

这种设计选择产生了叠加效应。你的 IaC 代码不到十行。你的 [CI/CD 流水线](https://thenewstack.io/cicd-pipeline-front-line/) 不需要自定义步骤。一个氛围编程代理可以代表你进行部署和迭代，因为整个界面就是一个定义明确的规范，它已经知道如何读取和修改。

但也有工程上的原因。因为 Express Mode 拥有它所创建资源的全生命周期管理权，它可以清理它所设置的内容。删除一个服务，目标组、[扩展策略](https://thenewstack.io/beyond-magic-scaling-myth/) 和报警器也会随之删除。没有孤立的基础设施。而且因为你没有手动连接这些资源，一个服务的部署不会意外触碰到另一个服务。

### 总结

随着我们继续在 ECS Express Mode 上进行构建，我们的优先级很简单——为客户消除不具差异化的繁重工作。Amazon ECS Express Mode 是我们实现这一承诺的尝试：指向一个镜像，得到一个生产服务：包含负载均衡器、TLS、自动扩缩容、金丝雀部署，所有这些都运行在你的账户中，你可以随时查看并修改。

> “配置随需求增长，而运营负担不会。”

当你的工作负载超出单个容器的承载能力时，你也不会超出 Express Mode 的能力。带上你自己的任务定义：Sidecar、加固镜像、密钥，继续将基础设施交给我们就行。配置随需求增长，而运营负担不会。

从 AWS 控制台、Terraform、CloudFormation、CDK 或 GitHub Actions 尝试它——或者直接问你的 AI 助手。