
<!--
title: Nhost 在托管后端和开发平台之间开辟了一片天地
cover: https://cdn.thenewstack.io/media/2024/09/fb764f49-nhostlogo1.png
-->

提供后端即服务以及运行自定义代码和第三方服务的选择，以及新的 AI 工具。

> 译自 [Nhost Carves a Niche Between Managed Backend and Dev Platform](https://thenewstack.io/nhost-carves-a-niche-between-managed-backend-and-dev-platform/)，作者 Susan Hall。


# Nhost 在托管后端和开发平台之间开辟了一片天地

![Nhost 在托管后端和开发平台之间开辟了一片天地的专题图片](https://cdn.thenewstack.io/media/2024/09/fb764f49-nhostlogo1-1024x576.png)

在 [后端](https://thenewstack.io/why-backend-developers-should-fall-in-love-with-graphql-too/) 即服务的拥挤世界中，Nhost 决定——借用 [格林奇对谁村圣诞节的看法](https://docs.google.com/document/d/10yulrehQodGE7jqCt6AT0W_gclURWfo4q0HryBjTxVw/preview?hgd=1)——BaaS 应该“再多一点”。

“你要么是 BaaS，要么是 PaaS，像 Heroku、Render 或 Railway 这样的平台即服务。你必须在那里做出很多决定。你必须编写代码，你必须运行代码，对吧？”Nhost 联合创始人兼首席执行官 [Nuno Pato](https://github.com/nunopato) 说道。

通过添加其 Nhost Run 功能，该公司正专注于中间的某个地方。它还添加了 [AI 功能](https://thenewstack.io/ai/) 以简化开发。

[Nhost Run](https://nhost.io/blog/run) 旨在轻松扩展 Nhost 堆栈，以您选择的语言在同一个地方运行任何自定义和第三方开源解决方案。

“我们真正想要做的是提供像 Firebase 这样的预制或交钥匙解决方案的便利性——你创建项目，你在那里获得基础知识，然后使用 Run，你实际上可以扩展，所以你不需要去外面。[你]把所有东西都放在同一个保护伞下，”Pato 说。

您可以将 Redis、Memcached、Datadog Agents 或 MongoDB 等服务与您的 Nhost 后端集成。

## 后端以及扩展选项

居住在亚速尔群岛的 Pato 在 2020 年开始通过一个名为 Antler 的加速器项目开始研究 Nhost，在那里他遇到了最初在瑞典创立该公司的 [Johan Eliasson](https://github.com/elitan)。与许多公司一样，它的诞生源于创始人对一遍又一遍地构建相同基本后端服务的沮丧。

“每次我必须开始一个新项目时，我都必须一遍又一遍地做同样的事情：选择一个数据库，配置它，为 API、身份验证、存储编写代码……这些基本组件存在于大多数应用程序或项目中，”他说。

该公司构建为 Web 和移动应用程序的开源无服务器后端，它加入了为 [Google](https://cloud.google.com/?utm_content=inline+mention) 的 [Firebase](https://thenewstack.io/firebase-suite-google-fires-new-mobile-dev-powers/) 提供替代方案的领域。在底层，Nhost 提供：

- Postgres 数据库，您可以在其中将数据库视为电子表格或直接连接以编写原始 SQL 并对其进行完全控制。
- [Hasura](https://hasura.io/?utm_content=inline+mention) GraphQL 引擎，连接各种数据存储并自动生成 GraphQL API 的开源技术，用于全文搜索、事件触发器和实时订阅。它支持特定的行和列权限以实现协作，但具有控制权。
- 使用 FIDO 安全密钥或设备生物识别技术进行 Web 和移动应用程序授权，以实现无密码或多因素身份验证。
- Hasura 存储连接任何与 S3 兼容的存储服务。
- 无服务器函数，用于处理具有无限扩展性的 JavaScript 和 TypeScript 中的自定义代码。这些函数是为 AWS Lambda 构建的，并部署在与您的后端相同的 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 区域中。
- Nhost 还提供托管云。

Nhost 与主要的  前端框架集成，例如 React、Next.js 和 Vue。

“我们有一些客户在我们这里托管数据库和 API，但他们托管着自定义服务，例如用于机器学习或人工智能管道的 Python 服务。他们在不同的提供商（如 Render 或 Heroku）中托管这些服务，在某个时候，我们只是说，‘为什么我们不允许他们只在我们这里运行所有东西呢？’对吧？”Pato 在谈到 Run 功能时说道。

“因此，您创建项目，并使用我们为您提供的后端快速启动并运行——同样，存储、身份验证、API 和数据库——但我们也允许他们编写自己的服务，然后将这些服务置于同一个 Nhost 保护伞下。”

它在 Amazon EKS（AWS 的托管 Kubernetes 服务）上运行所有内容。

“后端显然有第一部分。我们只是清理容器。我们在我们拥有的每个集群中为每个用户或每个项目创建一个命名空间。我们的集群遍布各地。然后是 Run 部分。……您创建 Docker 文件，创建映像，将映像推送到我们自己的注册表，然后我们在仪表板中添加 UI，您可以在其中为要带来的服务设置配置，然后我们只需运行它。……我们试图让它变得非常非常容易，只需进行一些配置，”他说。

## 新的人工智能产品
最近，Nhost 使用开源 [Postgres 扩展](https://github.com/pgvector/pgvector) [pgvector](https://thenewstack.io/postgres-is-now-a-vector-database-too/) 为其 Postgres 产品添加了向量嵌入，用于相似性搜索。它还发布了 Auto-Embeddings，它使用 OpenAI 来支持自然语言查询，以及一种更简单的方法来保持嵌入的更新。当发生更改时，Auto-Embeddings 将重新生成嵌入并将新的嵌入存储在数据库中，因此用户无需编写该代码。

其 AI Assistants 使用 ChatGPT，它与表示为 GraphQL 查询、突变和/或 Webhook 的预定义访问一起，可用于涉及访问不同类型数据的过程，并严格执行对该数据的权限。您可以使用 Assistants 使用 Nhost 知识库构建 LLM。

它还发布了 [Graphite](https://nhost.io/blog/dev-assistant)，一个开发助手和编码伙伴。它了解您项目的数据库和 GraphQL 模式，以提供上下文感知的建议，使开发更容易。

在其由 Nauta Capital 领投的 300 万美元种子轮融资中，GitHub 创始人 Scott Chacon 和 Tom Preston-Werner 以及 Netlify 创始人 Christian Bach 和 Mathias Biilmann Christensen 也参与其中。

Firebase 虽然是启动项目的流行方式，但它是专有的，并且催生了许多开源 [替代方案](https://thenewstack.io/guide-serverless-technologies-functions-backends-service/)，包括 [Supabase](https://thenewstack.io/supabase-takes-aim-at-firebase-with-a-scalable-postgres-service/)、[AppWrite](https://thenewstack.io/appwrite-a-cloud-native-backend-as-a-service/)、Back4App、Parse、[Kinvey](https://thenewstack.io/introducing-kinvey-flex-industrys-first-unified-node-js-mbaas-platform/) 和 Kuzzle，以及无数其他专有产品，包括 [AWS Amplify](https://thenewstack.io/independent-baas-providers-should-be-worried/)。

据 Pato 说，Nhost 最初认为 Supabase 是其最接近的竞争对手，但他现在表示，他们过于专注于数据库，而 Nhost 正试图通过 Run、Graphite 等软件附加组件以及 [Dedicated Compute](https://nhost.io/blog/dedicated-compute) 和 [Service Replicas](https://nhost.io/blog/service-replicas) 等平台功能来开拓利基市场，这些功能允许您为 Nhost 堆栈上的每个服务分配 CPU 和 RAM，并在各种机器上部署同一服务的多个并发实例，以消除瓶颈并提高可用性和容错能力。

---

> **[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)**
>
> 技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等。