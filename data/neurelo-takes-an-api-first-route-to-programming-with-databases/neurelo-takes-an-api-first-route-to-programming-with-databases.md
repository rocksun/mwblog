<!--
title: Neurelo 采用API优先的方式进行数据库编程
cover: https://cdn.thenewstack.io/media/2024/01/70cf3e2e-data-1024x576.jpg
-->

如果每次软件对数据库的读取和写入都变成为对应数据模型定制的标准 API，将会如何？

> 译自 [Neurelo Takes an API-First Route to Programming with Databases](https://thenewstack.io/neurelo-takes-an-api-first-route-to-programming-with-databases/)，作者 Susan Hall 是 The New Stack 的赞助商编辑。她的工作是帮助赞助商为其提供的内容获得尽可能广泛的读者。

在云原生计算中，计算、网络和存储的抽象化在很多方面使开发者的工作变得更容易。但是对于数据呢？情况并非如此。

开发者仍然需要织造出各种方式来定义、集成、编程、监控、扩展和保护数据。根据 [MongoDB 2022 年的数据与创新报告](https://www.mongodb.com/collateral/report-on-data-and-innovation-en)，在受访的 2000 名 IT 专业人士中，有 73% 的人表示构建应用程序最困难的部分是处理数据。

“这整个层面都是一个复杂性和挑战的冰山，”创业公司 [Neurelo](https://www.neurelo.com/) 的联合创始人兼 CEO [Chirag Shah](https://www.linkedin.com/in/chisha/) 说，该公司采用 [API 优先的方法](https://thenewstack.io/creating-an-api-first-culture-and-company-part-1/)来简化这一过程。

Neurelo 旨在为使用 PostgreSQL、MongoDB 和 MySQL 构建应用程序的人们带来一个单一的抽象层，抽象应用程序与数据库之间的复杂依赖关系。

## 面向您的数据模型构建的 API

来自数据库背景的联合创始人 Shah 和 [Guru Kamat](https://www.linkedin.com/in/gkamat/) 在与客户合作中亲身见证了这个“冰山”。

Shah 之前是 [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline-mention) 的产品副总裁，领导 [VMware](https://tanzu.vmware.com/?utm_content=inline-mention)、惠普企业等公司的产品和市场职能。Kamat 是 Stripe 安全基础的工程主管，并曾任 [Palo Alto Networks](https://www.paloaltonetworks.com/cloud-security?utm_content=inline-mention) Prisma Cloud 的工程副总裁。

正是这些经验促使他们大约一年半前在加利福尼亚州洛斯阿尔托斯创建了 Neurelo。展望未来，他们决定其以 API 为先，并自问道: “如果您的软件与数据库之间的每个读取和每个写入都成为针对您的数据模型定制的标准 API，会怎么样？在几分钟内，而不是几天或几周内。现在，开发者一开始就可以......他们可以在一分钟内开始编写程序。”

![放大镜](https://cdn.thenewstack.io/media/2024/01/4f3db260-neureloart2.png)

随着 1.0 版云数据 API 平台的发布，Neurelo 正在提供根据您的数据模型自动生成的自定义 API，消除了对驱动程序、驱动程序查询语言、对象关系映射(ORM)或用于 MongoDB 的基于 Node.js 的对象数据建模(ODM)的依赖。它还会自动为 API 创建文档，并根据应用程序的需求处理版本控制、更改代码和模式。

“API 本身就是一个巨大的开发者速度提升，因为所有与数据库编程、查询语言、驱动程序等相关的准备阶段都被完全中和了。他们可以直接暴露数据模型并在一分钟内开始工作，”Shah 说。

在[使用 Neurelo 早期访问版本的经历中](https://dev.to/seanrreid/resurrecting-a-dead-app-neurelo-to-the-rescue-1io7)，软件开发者和编码讲师 [Sean R. Reid](https://www.linkedin.com/in/sean-r-reid-7ba999a8/) 写道，至少需要 6-7 个步骤来设置 Express 或 Django API，更可能是其两倍，如果他喜欢后端工作，这可能并不令人生畏。但事实并非如此。

“我的‘舒适区’是前端，React、Remix、Next、Vue等......构建 API 就像那些你一直把推到待办事项底部的琐事......”

他详细叙述了一个拼写错误导致的长期不活跃的项目 BOOMKARKS 的复苏:

“Neurelo 有许多优点，但我们首先要提的是最大的一点: 我将数据库添加为数据源，然后 BOOM ，我有了一个 API!

“说真的，这就是运行 BoomKarks API 所需的一切。Neurelo 读取我的模式，为我的所有主要表生成了 `GET`、`POST`、`PUT` 和 `DELETE` 路由。在几分钟内，我就可以抛出一些 `fetch()` 查询，并能执行所有基本的 CRUD 操作。不需要 Node、Python 或 PHP，只需将数据源指向我的 PostgreSQL 服务器，切换开关，然后 BOOMKARKS 活了过来!”

API 以 REST 和 GraphQL 格式生成，可以处理跨单个表或集合的各种创建、读取、更新和删除(CRUD)操作，以及跨数据库中多个实体的 JOIN 查询。Shah 将这些 API 描述为与 Stripe 或 Twilio 的技术非常相似，它们存储在完全托管的云平台上。

## 自定义复杂查询等

Neurelo 还可以使用自然语言提示自动生成自定义复杂查询。此版本基于 OpenAI 技术，尽管该公司一直在试验 Bard 和其他 AI 模型。它一直在所有的数据库特定语法和语义上训练大型语言模型，因此您只需提出问题，它就会根据特定数据库的需要以 SQL(结构化查询语言)或 MQL(Mongo 查询语言)生成优化的查询，从数据模型中获取应用程序的上下文。

虽然抽象会带来一定的不透明性，但 Neurelo 旨在展示通过 API 发生的每次读取和写入的过程。

“当行业在查询级监控上失误时。每个数据库供应商都给你这个，对吧？但真正的理解是‘给我我的数据访问模式。我的读取是什么？我的热点是什么？哪列正在获取 90% 的读取流量？’这样的事情[是]深刻的，它改变了你在生产中做很多事情的方式，”他说，解释说，如果一个特定列正在获取大量流量，例如，这可以确定你的扩展方式。

Neurelo 的可观测性可以在不同的环境(开发、测试、生产)中设置，以跟踪 API 和数据库查询性能。

Neurelo 还提供了 Schema-as-Code 功能，可以像源代码一样对待数据库模式，以版本控制跟踪更改。它提供了一个规范化的存储库——真理的中心源——用于跨数据库所有方面的元数据的自动收集和管理，帮助一致地执行标准并改善团队成员之间的协作。

它已经为 TypeScript、Go、Java、PHP 和 Python 发布了 SDK，尽管 Shah 表示 Neurelo 可与任何语言配合使用。

“如果您是前端开发人员，正在构建应用程序，比如说，[HTMX](https://thenewstack.io/htmx-html-approach-to-interactivity-in-a-javascript-world/)......您可以通过我们直接开始向数据库发出 restful 调用，甚至不需要担心数据库驱动程序不支持这些语言，”他说。

该技术本身是[用 Rust 构建的](https://thenewstack.io/microsoft-rust-is-the-industrys-best-chance-at-safe-systems-programming/)。创始软件工程师 [James Shockley](https://www.linkedin.com/in/shockleyje/) 在这个视频中解释了他们为什么选择 Rust:

分析师 Torsten Volk，企业管理协会(EMA)的管理研究总监，对 Neurelo 的安全性方面发表了评论。

“集中管理的访问令牌与能够白名单指定IP和IP范围的功能相结合，使Neurelo的安全措施与其他托管数据服务(如MongoDB或AWS DynamoDB)保持一致。此外，Neurelo允许组织在内部托管其运行程序——负责数据检索和操作的专用代理。这种内部托管选项使组织能够应用‘最低权限’安全原则，有效地缩小运行程序的权限，最大限度地降低安全漏洞的风险和影响，”他说。

与组织网络的微分段一起使用时，Neurelo的方法通过隔离工作负载来提供额外的安全性，这限制了系统内威胁的横向移动。Neurelo托管的控制平面与本地管理的执行代理(运行程序)之间的这种架构分离解决了广泛的安全问题，他解释道。

“随着现代分布式微服务应用越来越多地依赖于应用中心的安全策略，而不仅仅依赖于基础设施强化，Neurelo 的云托管控制平面与内部托管代理的模型非常适合安全集成到企业环境中。然而，值得注意的是，某些用例，特别是那些有严格法规要求的用例，可能与基于云的控制平面不兼容。尽管如此，这些用例只占企业应用的相对较小的一部分，这表明 Neurelo 的平台可能适用于和安全适用于绝大多数(可能高达 90%)的企业工作负载。“

## 面向企业的路线图

“数据库编程可能是一项艰巨的任务，尤其对于刚接触该领域的人员而言。理解数据类型、约束、索引和事务的复杂性是构建高效可靠的数据库应用程序的先决条件。即使[经验丰富的开发人员也可能花费数小时甚至数天的时间](https://www.neurelo.com/post/simplifying-database-programming-with-neurelo)调试和优化查询以达到所需的性能，”根据该公司的白皮书。

一些公司针对这个问题投入了很多不同的工具——为每个数据库找到5个或更多工具并不罕见——而少数几个科技巨头像 PayPal、X(原 Twitter)和 Facebook 构建了自己的抽象层，这些项目的构建和维护成本高昂。

这个版本只是 Neurelo 路线图上的第一个里程碑。它正在努力实现更多企业级功能，如字段标记、对敏感信息的其他访问控制以及与缓存、搜索和其他系统的即插即用集成。还计划开发一个本地版本。

“API的利用是开发生命周期中的关键部分，使Neurelo能够快速创建、修改和增强功能。这种方法加速了开发人员的生产力，并作为创新的催化剂，”Futurum Group的分析师Paul Nashawaty在电子邮件中说。

“…Neurelo的API抽象层在简化与数据库管理相关的复杂性方面发挥作用。开发人员可以通过明确定义的API端点与底层数据库系统进行交互，减少了传统上与直接数据库操作相关的复杂性。这个抽象层提高了开发人员的理解能力，并优化了整个开发过程。此外，通过利用托管的云服务，Neurelo确保其API的安全性和可靠性，提供强大且可扩展的环境。这种战略性的整合不仅导致更快的生产时间，而且提供了更好的控制、可预测性和成本效益，最终为Neurelo在市场上的技术进步和竞争优势做出了贡献。”
