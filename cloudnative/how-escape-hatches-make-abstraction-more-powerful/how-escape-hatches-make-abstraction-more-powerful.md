
<!--
title: 逃生舱如何让抽象更强大
cover: https://cdn.thenewstack.io/media/2024/03/f8c82ab7-escape123.jpg
-->

无论您是喜欢还是讨厌抽象，它们在云开发中无处不在。选择那些带有逃生舱的，让您的生活更轻松。

> 译自 [How Escape Hatches Make Abstraction More Powerful](https://thenewstack.io/how-escape-hatches-make-abstraction-more-powerful/)，作者 Rak Siva。

软件社区热衷于就抽象的话题展开争论；在某个地方，某人被锁定而无法理解，实际上有精心设计的抽象能够满足应用程序开发的独特性质。与此同时，我们的整个行业建立在层层抽象之上。

例如，API 网关抽象了 API 端点的路由、安全性和可扩展性，使开发人员能够高效地管理其 API，而无需深入了解底层基础设施。同样，Amazon S3 提供了一个抽象的可扩展存储解决方案，使用户能够存储和检索任意数量的数据，而无需管理物理存储系统。

这些抽象被如此无缝地集成到云应用程序开发的结构中，以至于对使用它们的开发人员来说几乎是不可见的。然而，它们是基础性的，通过在简单界面背后处理复杂细节，实现应用程序的快速开发、部署和扩展。

逃生舱是一项至关重要的功能，可确保开发人员不会被锁定在特定技术中，尤其是在涉及抽象时。它们提供了一条直接访问和使用底层云服务以及使用现有资源或工具集的途径。此外，它们允许你利用框架的优势，同时提供在云原生环境中构建复杂、高性能和定制应用程序所需的灵活性和控制力。

## 为什么逃生舱对云抽象至关重要

虽然抽象层旨在涵盖常见和基础用例，但它们有目的地构建为避免公开可用的每个配置或设置。逃生舱允许对云服务进行更细粒度的控制，从而实现性能优化和定制。

没有有目的地引入逃生舱的抽象层更难信任和更难使用。然而，许多抽象框架很容易认识到对逃生舱的需求，并预期可以对任何集成进行更改。曾经被烧伤过一两次的工程师可能会发现这些框架更容易信任。

## 良好逃生舱的示例

了解什么构成了一个好的逃生舱的最佳方法是看一些示例。之前，我提到大多数软件都是建立在抽象层之上的，所以我将从项目中最常见的抽象之一开始：数据库。

### 示例 1：Prisma

[Prisma](https://www.prisma.io/) 是一个开源数据库工具包，可简化 Node.js 和 TypeScript 应用程序中的数据访问和管理。它提供了一个 ORM（对象关系映射）层，使开发人员能够通过高级 API 与其数据库进行交互。

尽管有抽象，但 Prisma 认识到在某些情况下需要直接访问数据库，因此它为开发人员需要更多控制或需要执行 Prisma 的 API 未涵盖的数据库操作时提供了逃生舱。

Prisma 提供的最重要的逃生舱之一是直接对数据库执行原始 SQL 查询的能力。此功能对于 Prisma Client API 不支持特定数据库操作或优化需要直接 SQL 以提高效率的情况至关重要。

以下是如何使用 `$queryRaw` 执行复杂 `SELECT` 查询的一个简单示例，该查询无法通过 Prisma 生成的客户端 API 轻松表示：

```js
const result = await prisma.$queryRaw`
  SELECT
    *
  FROM
    users
  WHERE
    name = ${name}
`;
```

注意：Prisma 通过为 `$queryRaw` 提供标记模板文字语法来减轻 SQL 注入等风险，该语法通过允许变量绑定来帮助防止 SQL 注入。

### 示例 2：Pulumi

[Pulumi](https://www.pulumi.com/) 是一个基础设施即代码工具，允许开发人员使用 TypeScript、Python、Go 和 C# 等编程语言定义、部署和管理云服务。它支持多个云提供商，包括 [AWS](https://aws.amazon.com/?utm_content=inline-mention)、[Microsoft](https://news.microsoft.com/?utm_content=inline-mention) Azure，
自动化 API 封装了各种云提供商的 API，允许开发人员以一致且符合习惯的方式跨不同云与云资源进行交互。为了访问 Pulumi 的抽象尚未完全支持的即将推出的或实验性功能，逃生舱为开发人员提供了内置的灵活性和可扩展性。

Pulumi 的动态提供程序允许你在现有提供程序无法满足你的需求时定义自定义资源。通过实现四种方法——创建、读取、更新和删除——你可以将任何外部服务或 API 集成到 Pulumi 应用程序中。

**以下代码段可在详细的**[Pulumi 动态提供程序](https://www.pulumi.com/docs/concepts/resources/dynamic-providers/) 指南中进行扩展：

```js
import * as pulumi from "@pulumi/pulumi";

class MyResourceProvider implements pulumi.dynamic.ResourceProvider {
    public async create(inputs: any) {
        // Custom create logic here
        return { id: "resource-id", outs: {} };
    }

    // TODO: Implement read, update, and delete 
}

const myResource = new pulumi.dynamic.Resource("myResource", {}, { provider: new MyResourceProvider() });
```

这种方法让开发人员能够将最新的云功能纳入其代码即基础设施中，即使这些功能尚未封装在 Pulumi 的资源提供程序中。

### 示例 3：Nitric

[Nitric](https://nitric.io) 是一个框架，旨在利用 Pulumi、Terraform 和云 SDK，通过提供一组可跨不同云提供程序工作的抽象 API 来简化云原生应用程序的开发。这种抽象允许开发人员编写不太依赖于任何单个云提供程序的特定服务和 API 的代码，从而更容易跨多个云部署应用程序或在需要时切换提供程序。

Nitric 提供程序处理云应用程序的预配和运行时操作。通过扩展提供程序，开发人员可以获得一个逃生舱口来覆盖或扩展抽象资源的配置。这包括调整性能设置、安全规则或其他未通过框架的标准 API 公开的特定于提供程序的配置。

以下是如何部署对存储桶资源的请求的示例，开发人员可以轻松修改或扩展该示例：

```py

// Bucket - Implements deployments of Nitric Buckets using AWS S3
func (a *NitricAwsPulumiProvider) Bucket(ctx *pulumi.Context, parent pulumi.Resource, name string, config *deploymentspb.Bucket) error {
	opts := []pulumi.ResourceOption{pulumi.Parent(parent)}

	bucket, err := s3.NewBucket(ctx, name, &s3.BucketArgs{
		Tags: pulumi.ToStringMap(common.Tags(a.stackId, name, resources.Bucket)),
	}, opts...)
	if err != nil {
		return err
	}

	a.buckets[name] = bucket

	if len(config.Listeners) > 0 {
		notificationName := fmt.Sprintf("notification-%s", name)
		notification, err := createNotification(ctx, notificationName, &S3NotificationArgs{
			StackID:   a.stackId,
			Location:  a.region,
			Bucket:    bucket,
			Lambdas:   a.lambdas,
			Listeners: config.Listeners,
		}, opts...)
		if err != nil {
			return err
		}

		a.bucketNotifications[name] = notification
	}

	return nil
}
```

这种方法意味着，当开发人员需要使用 Nitric 当前未抽象的特定 AWS 服务功能时，他们可以退回到底层抽象技术来实现其目标。

## 利用带有逃生舱口的抽象

良好的逃生舱口意味着使用抽象框架并不等于被其限制所束缚。当您需要跳出抽象的界限以满足应用程序的特定需求时，它们提供了一种安全的方式，无论是为了优化、访问新功能还是与旧系统集成。

抽象的便利性和逃生舱口提供的灵活性之间的平衡确保了开发人员可以享受两全其美的优势。我们在 [Nitric](https://nitric.io) 思考并致力于解决这个问题。来与我们聊天吧！
