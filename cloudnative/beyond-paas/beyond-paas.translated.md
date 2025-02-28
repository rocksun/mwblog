2025年2月28日

阅读时间：5分钟

每个工程团队的成功都取决于尽早做出正确的基础设施选择。

当资源紧张且速度至关重要时，选择正确的云基础设施方法可以决定团队的成败。

错误的选择可能会耗尽您的工程带宽数月；正确的选择可以成为快速、可持续发展的基础。

在云基础设施方面，团队通常面临三种主要方法，每种方法都有重要的权衡：

**传统PaaS (Heroku, Supabase, Firebase)**
- 快速启动，使用托管服务，但会将您锁定在其生态系统中
- 仅限于平台特定的附加组件，难以与其他云服务集成
- 对多个环境和本地开发的支持有限
- 最适合符合平台限制的更简单的应用程序

**基础设施即代码 (Terraform, Pulumi)**
- 最大限度的控制和云提供商访问权限
- 需要编写数千行配置代码（单个AWS ECS设置需要500多行）
- 需要专门的DevOps专业知识来维护
- 需要手动将服务连接在一起（VPC、安全组、IAM角色）
- 能够完全访问云提供商的功能

**部署平台 (Northflank, Fly, Railway)**
- 主要专注于容器部署和基本数据库（Northflank通过Kubernetes支持超越了这一点）
- 与云原生服务的集成通常有限（没有直接的AWS/GCP服务访问）
- 定价简单，但大规模情况下成本效益较低（Render每月最低收费7美元/服务）
- 监控和日志记录功能基本

我们在Encore努力解决的就是这种灵活性和简单性之间的权衡。

我们的方法是将一个[开源后端开发框架](https://github.com/encoredev/encore)与一个基于SaaS的云自动化平台([Encore Cloud](https://encore.cloud))结合起来。这种组合提供了类似PaaS的部署简单性和强大的开发者生产力功能，同时保持了在您自己的云帐户（AWS/GCP）中运行所有内容的灵活性。

这意味着Encore处于这些类别之间，提供了不同的功能组合：

- 像PaaS一样，它完全自动化基础设施和云部署。
- 像IaC一样，它允许您使用您自己的云提供商和强大的基础设施服务，如Kubernetes，但无需任何Terraform的手动开销和复杂性。
- 与上述任何一种方法不同，它与您的开发工作流程集成，以提供开发人员体验和生产力功能，例如内置API生成、服务发现、API文档和服务目录，以及具有分布式跟踪的[可观测性](可观测性)。
与传统的PaaS不同，Encore Cloud不会托管您的应用程序。您的基础设施保留在您自己的AWS或GCP帐户中，因此您永远不会失去控制。

Encore的开源CLI提供了将您的应用程序构建为Docker容器所需的工具，因此您可以将其部署到任何地方。

如果您选择使用[Encore Cloud](https://encore.cloud)来完全自动化您的基础设施和部署，您仍然可以使用您的AWS或GCP云帐户，因此您可以从第一天起就拥有您的基础设施和数据。

迁移离开Encore Cloud意味着您可以继续运行您的应用程序，只需要接管CI/CD和基础设施管理流程。

Encore的声明式基础设施框架是[开源的](https://github.com/encoredev/encore)，占用空间极小，99%的代码是普通的TypeScript或Go代码。这意味着开发人员不需要学习很多东西就可以开始使用Encore，并且您仍然可以使用您熟悉的工具和库。

从框架迁移也很简单，因为其占用空间仅限于应用程序的边缘。

例如，您可以通过使用`api`函数包装它来定义一个来自普通TypeScript函数的API端点：

```typescript
// Normal TypeScript function
export const getBlogPost =
async (req: { id: number }): Promise<BlogPost> => {
// ...
};
// API endpoint
export const getBlogPost = api({ method: "GET", path: "/blog/:id" },
async (req: { id: number }): Promise<BlogPost> => {
// ...
}
);
```

不需要复杂的Terraform脚本或Kubernetes清单，您可以编写普通的TypeScript或Go代码，并使用框架来包装您的函数以创建API，或者使用单行代码来定义您的基础设施，如数据库和Pub/Sub。

例如，您可以使用一行代码定义PostgreSQL数据库：

```typescript
import { SQLDatabase } from "encore.dev/storage/sqldb";
const db = new SQLDatabase("userdb", {migrations: "./migrations"});
// ... use db.query to query the database.
```

这就是Encore运行您的应用程序和基础设施进行本地开发以及自动化配置和云部署所需的一切。
它是通过解析您的代码并自动生成必要的基础设施定义，然后使用您的云提供商的API来配置和管理基础设施来工作的。

Encore Cloud负责设置所有底层基础设施的复杂性，包括：

- 安全组配置
- 网络路由和VPC设置
- IAM角色和权限
- 数据库连接池和凭证管理
- 以及更多

在本地开发中，Encore的开源CLI将自动启动使用本地等效项的基础设施服务，并将它们连接到您的应用程序。

与本次比较中的所有其他工具不同，Encore提供了生产型分布式系统开发所需的所有开发者平台工具，包括：

- 自动生成的API文档
- 服务目录
- 生成的架构图
- 分布式追踪
- 本地开发设置
- 每个拉取请求的预览环境

这将为您节省数月的设置时间以及雇用平台工程专业人员来维护您自己的自定义开发者平台的成本。

选择便利性和控制力之间的时代已经结束。使用Encore，我们的目标是为您提供现代云自动化的强大功能，同时保留对您基础设施的完全所有权。

如果您正在寻找一个新的工具来使云开发更快、更简单、更灵活，我们希望您能尝试一下Encore。

**想看看它是如何工作的吗？** 查看[文档](https://encore.dev/docs)，加入我们的[Discord](https://encore.dev/discord)提出问题，或[预约演示](https://encore.dev/book)进行一对一的介绍。

我们的故事

25年1月15日 / 阅读时间3分钟

为开发者设计工具也意味着为LLM设计工具

我们如何使用LLM为LLM生成构建Encore应用程序的指令。

发布周

24年12月13日 / 阅读时间3分钟

工作池——针对CPU密集型JavaScript工作负载的5倍性能

发布周第5天

发布周

24年12月12日 / 阅读时间3分钟

Encore.ts中的高级验证

发布周第4天