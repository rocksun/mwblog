任何实际规模的后端项目最终都会有两个描述相同系统的代码库。你有TypeScript或Go编写的应用程序代码，然后在其他地方，通常是`terraform/`目录或一个完全独立的仓库，你有用于配置数据库、消息队列、IAM角色的HCL代码。它们用不同的语言编写，在单独的PR中进行评审，通过不同的管道部署。没有人能很好地解决如何保持它们同步的问题。

代码即基础设施（IFC）消除了第二个代码库。你可以直接在应用程序代码中声明你的基础设施（数据库、Pub/Sub主题、cron作业），然后框架会读取这些声明来配置实际的云资源。所有东西都在一个PR中发布，基础设施不会偏离应用程序，因为它是由应用程序派生的，你也不再需要维护那些与你的代码已知信息镜像的Terraform模块。

除了简化日常工作流程，IFC还改变了AI代理与你的代码库交互的方式，这正是有趣之处。在介绍完基础知识后，我们将对此进行更多探讨。

```
1import { api, SQLDatabase }
2import { Topic }
3
4const db = new SQLDatabase("orders")
5const topic = new Topic("order-created")
6
7export const create = api({
8method: "POST", path: "/orders"
9}, async (req) => {
10await db.insert(req)
11await topic.publish(req)
12})
```

代码即基础设施管道

代码 → 编译 → 部署。IFC管道分三步。

需要PostgreSQL数据库和[Pub/Sub主题](/blog/event-driven-architecture)的服务会在使用它们的地方直接声明：

```


import { api } from "encore.dev/api";
import { SQLDatabase } from "encore.dev/storage/sqldb";
import { Topic } from "encore.dev/pubsub";


const db = new SQLDatabase("orders", { migrations: "./migrations" });


const orderCreated = new Topic<OrderEvent>("order-created", {
  deliveryGuarantee: "at-least-once",
});


export const createOrder = api(
  { expose: true, auth: true, method: "POST", path: "/orders" },
  async (req: CreateOrderRequest): Promise<Order> => {
    const order = await db.queryRow`
      INSERT INTO orders (customer_id, total)
      VALUES (${req.customerId}, ${req.total})
      RETURNING *`;
    await orderCreated.publish({ orderId: order!.id, total: order!.total });
    return order!;
  }
);


```

在本地，该框架通过Docker配置一个真实的PostgreSQL实例，并运行具有等效内存语义的Pub/Sub。在生产环境中，像[Encore Cloud](https://encore.cloud)这样的平台会读取相同的声明，并在你的云账户中，在AWS上配置RDS + SNS/SQS，或者在GCP上配置Cloud SQL + GCP Pub/Sub。加密、备份、最小权限IAM都由基础设施团队一次性设置的[环境级配置](/docs/platform/infrastructure/configuration)来处理。

同样的模式适用于cron作业、对象存储、缓存和密钥。每个都根据你部署的位置映射到不同的云资源：

SQL数据库

Pub/Sub

Cron作业

对象存储

缓存

密钥

SQL数据库

声明

`new SQLDatabase("orders", {
migrations: "./migrations"
})`

通过Docker的本地PostgreSQL

awsRDS

gcpCloud SQL

相同的代码 → 每个环境不同的基础设施

点击一个基本元素，查看它如何在不同环境中映射。

代码即基础设施（IFC）并非新概念。[Encore](https://encore.dev)在当前AI编码工具浪潮之前就推出了这种方法，而从应用程序代码中派生基础设施的想法甚至更早。它之所以获得发展势头，是因为AI代理改变了工作量。

当一个代理在一个下午生成十个新端点时，没有人会去编写十个匹配的Terraform模块。应用程序代码在几分钟内就准备好了，但实际运行所需的基础设施工作却需要一整天。[DORA的研究](https://dora.dev/research/)发现，用AI更快地编写代码并不能加快交付速度，除非周围的工作流程也发生变化，而基础设施配置是大多数团队尚未改变的工作流程。

每月

22个功能等待基础设施

AI加速代码生成。基础设施配置速度保持不变。

还存在一个上下文问题。当基础设施内联声明时，AI代理可以读取单个服务文件，并理解它使用PostgreSQL数据库，发布到至少一次交付的主题，并公开一个经过认证的POST端点。这足以生成一个查询相同数据库的新端点，或者一个处理相同主题事件的订阅者。使用Terraform，基础设施上下文存在于不同的仓库（或使用不同语言的不同目录）中，代理无法将应用程序逻辑与其所依赖的资源连接起来。

使用IFC框架，代理编写的应用程序代码声明了其基础设施需求，并且输出可以通过`git push`进行部署。没有单独的基础设施PR，没有计划/应用周期，并且代理编写的内容与实际运行的内容相符。Encore的[MCP服务器](/blog/mcp-server)通过让代理了解整个应用程序中现有的服务、API和Schema，从而进一步发展，使生成的代码遵循项目现有的模式。

Terraform使基础设施可复现且版本受控，这相对于通过云控制台点击操作来说是一个真正的改进。它还在应用程序代码和基础设施代码之间创建了一种永久性的分离，团队已经与这种分离共存了十年。（我们在[《告别Terraform CDK》](/blog/terraform-cdk-alternative)中更详细地介绍了这一转变。）

这是两种端到端部署工作流的样子：

宽度 = 耗时。实线 = 活跃工作。虚线 = 等待评审或验证。

传统IaC与代码即基础设施部署工作流对比。

最明显的区别是漂移。当基础设施从应用程序代码派生时，两者不可能出现分歧。不会出现应用程序期望一个Terraform忘记创建的Pub/Sub主题，或者数据库迁移引用了一个尚未配置的表的情况。基础设施始终是代码的函数。

Terraform状态也消失了。锁定冲突、损坏的状态、状态文件中的敏感数据，以及每个团队配置略有不同的远程后端。IFC平台内部管理状态，因此你无需处理这些问题。

计划/应用周期是为基础设施每周变化几次的世界设计的。当你每天部署多次，或者AI代理持续生成服务时，它就变成了瓶颈。使用IFC，部署基础设施更改与部署应用程序代码是相同的操作。

也没有语言切换。基础设施以TypeScript或Go声明，与应用程序编写的语言相同。你无需在HCL和应用程序语言之间进行上下文切换，也无需在业务逻辑旁边维护YAML配置。

本地开发是差异最明显的地方。使用Terraform，你通常会设置Docker Compose或模拟服务来模拟你的云环境。使用IFC，`encore run`为你提供真实的PostgreSQL、真实的Pub/Sub语义，以及一个包含分布式追踪、API浏览器和数据库浏览器的[本地仪表盘](/docs/ts/observability/dev-dash)。无需配置。

文件结构反映了这一切：

使用Terraform的代理输出

使用Encore的代理输出

`security-groups.tf28 lines`

`docker-compose.yml32 lines`

`1_create_tables.up.sql8 lines`

相同的系统，不同的项目结构。

我们在[《Terraform的最后一年》](/blog/last-year-of-terraform)中更详细地介绍了这一转变。

IFC并非没有限制。采用它意味着：

**你使用框架的模式。** 基础设施声明遵循框架的约定：`new SQLDatabase()`、`new Topic()`等。你的业务逻辑是标准的TypeScript或Go（约占代码的99%），但基础设施层面使用框架的API。你可以使用`encore build docker`[生成Docker镜像](/docs/ts/self-host/build)并部署到任何地方，因此你不会被锁定到特定的托管平台。

**语言限制。** [Encore](https://encore.dev)支持TypeScript和Go，这是目前大多数后端开发所使用的语言，但如果你的团队使用Python、Ruby或Java，那么当前的IFC选项会更受限制。

**对单个资源的控制粒度较低。** Terraform允许你配置每个资源的每个参数。IFC抽象了资源级别的细节，平台根据环境设置处理配置。对于大多数团队来说，这是一个特性（出错的地方更少）。有些团队需要对特定资源进行精细控制，可能会觉得这种抽象过于不透明。

作为回报，你将获得：无需管理状态文件，应用程序与基础设施之间没有漂移，没有计划/应用周期，没有模拟生产环境的Docker Compose文件，以及应用程序开发人员和平台工程师之间更少的协调开销。

当应用程序代码和基础设施代码都由人类以相似的速度编写时，两者的分离是有意义的，但现在越来越多的应用程序代码是由AI生成的，而基础设施层决定了这些代码是实际运行还是等待某人编写Terraform。

我们发布了一份白皮书[《后端开发 3.0》](https://encore.cloud/library/backend-development-3-0)，深入探讨了这一转变背后的数据：DORA关于AI采用的发现、基础设施成熟度模型以及团队从Terraform迁移的过渡路径。

对于已经使用AI编写应用程序代码的团队来说，基础设施工作流程通常是尚未跟上的环节。IFC是弥合这一差距的一种方式。

**想亲身体验吗？**
我们很乐意向你展示Encore如何与你选择的AI工具协同工作。[预约一对一介绍](https://encore.cloud/book)，没有压力，只是一次对话。