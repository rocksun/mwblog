
<!--
title: 新一代同步引擎如何解决前端问题
cover: https://cdn.thenewstack.io/media/2025/01/776ff0d3-alex-shuper-ehko-zsjnoi-unsplashb.jpg
-->

Zero 是一个现代同步引擎的例子。它使应用程序开发人员能够执行 SQL 查询，指示他们想要同步的内容。

> 译自 [How a New Breed of Sync Engines Solves Frontend Problems](https://thenewstack.io/how-a-new-breed-of-sync-engines-solves-frontend-problems/)，作者 Loraine Lawson。

大多数现代软件都构建在标准的三层架构上——有时被称为 [REST](https://thenewstack.io/happened-rest-world-containers-data-streaming/) 架构——由客户端、暴露客户端调用的 API 的 [API](https://thenewstack.io/apis-are-quickly-becoming-the-latest-security-battleground-and-nightmare/) 服务器和 [数据库](https://thenewstack.io/database-trends-a-2024-review-and-a-look-ahead/) 组成。但一些 Web 开发人员正在转向 [新一代同步引擎](https://thenewstack.io/the-vintage-technology-that-speeds-up-modern-web-apps/) 作为替代方案。

在三层架构下，更改会触发客户端向 API 服务器发送请求，API 服务器将请求存储在 [数据库](https://thenewstack.io/database-trends-a-2024-review-and-a-look-ahead/) 中。 [Aaron Boodman](https://www.linkedin.com/in/aaron-boodman/) 解释说，如果另一个客户端调用并发出请求，API 服务器会从数据库中取出并发送响应。Aaron Boodman 是构建开发者工具的小型合伙企业 [Rocicorp](https://rocicorp.dev/) 的 CEO、创始人和合伙人。

Boodman 是一名软件工程师，曾帮助构建 Google Chrome。他的整个职业生涯都在从事同步引擎的工作。

他说：“在最低层发生的所有事情是 [that] 这些请求从客户端发送，要求服务器做一些事情，服务器回复答案。这些请求是完全无状态的，”他说。“每个请求都与其他请求完全分离，这是一个非常简单的架构。但对于人们试图构建的东西来说，它太简单了。如果你希望 UI 速度快，你需要数据在用户请求之前就位于客户端上。”

> “如果你希望 UI 速度快，你需要数据在用户请求之前就位于客户端上。”
>
> – Aaron Boodman, Rocicorp 首席执行官兼同步引擎开发人员

同步引擎提供了一种替代方法。同步引擎是旨在同步多个设备或服务之间的数据的软件。同步引擎的一部分驻留在客户端，一部分驻留在服务器上。同步引擎在客户端和服务器之间提供长期连接。

Boodman 解释说，它的速度之所以快，是因为服务器在客户端请求之前将信息发送到客户端，以便在客户端需要时可用。

## 同步引擎的问题

同步引擎以前没有被广泛部署的一个原因是市场上没有通用的同步引擎。[Replicache](https://replicache.dev/) 是 Rocicorp 五年前开始的，是市场上最早的通用同步引擎之一，Boodman 说。它被前端云提供商 [Vercel](https://thenewstack.io/introduction-to-vercel-frontend-as-a-service-for-developers/) 和部署工具 SST 使用。

但他补充说，将 Replicache 集成到产品中很困难。启动它需要巨大的设置成本。多年来他们看到的另一个问题是它不够通用。

他说：“当前的同步引擎，包括 [Replicache](https://replicache.dev/)，从根本上受到以下事实的限制……它们提前将数据同步到客户端。”“你可以尝试使网络通信尽可能快。但是，客户端和服务器相距遥远。它们通常位于不同的洲，你知道，数据需要时间才能传播。”

他说，为了获得比这更快的速度，你必须提前将数据发送到客户端，以便客户端已经拥有它需要的东西。然后问题就变成了开发人员应该发送*哪些*数据。

“我们不能将所有数据都发送到客户端。通常，有太多的数据要发送到客户端；它甚至无法容纳在客户端上，”他说。此外，发送数据需要时间，这会减慢应用程序的启动速度，他补充说。

还有授权问题：显然，你不能将其他人的数据发送到客户端。开发人员必须尝试仅发送应用程序需要的数据。

Boodman 说：“在这种有趣的权衡中，标准架构，REST 架构，……它只下载你请求的数据，所以它永远不会过度下载。”“但是，由于在下载数据之前你看不到数据，所以一切都很慢。同步引擎会下载所有内容。[…] 因此，一切都很快，但它仅适用于数据量小的应用程序，在这些应用程序中，下载所有内容是合理的。”

他说，这是同步引擎的一个根本问题，多年来一直阻碍着它们的发展。

## 一种新型同步引擎

借助 [Zero](https://zero.rocicorp.dev/)，该公司最新的开源同步引擎，Boodman 和他的团队正试图解决这一挑战。
“它建立在一个新的基础上。我们称之为查询驱动同步，”他说。

应用程序开发者无需下载用户有权访问的所有数据，也无需尝试分割数据，而是执行一个普通的 SQL 查询，表明他们想要同步的内容。该查询可以针对一个丰富的数据集。虽然开发者今天可以使用 REST 架构做到这一点，但不同之处在于 Zero 会同步该查询，使其能够实时更新。

> Zero 是“建立在一个新的基础上。我们称之为查询驱动同步。”
> 
> – Boodman

“应用程序可以显示结果，然后如果它更改查询，数据将自动返回到客户端，并且 UI 将自动显示新数据，而无需开发人员做任何事情，”他说。“他们不必编写任何代码来执行这些实时更新。它只是神奇地发生了。”

但它更进一步。一旦数据被下载到设备中，并且在 Zero 中与查询同步，如果开发人员执行一个新的查询，该查询可以通过设备上已有的数据来回答，Zero 将自动使用设备上已有的数据来回答该查询，而无需向服务器发送新的请求，他解释说。

他说，如果在原始数据中找不到答案，那么它会回退到服务器并获取结果。

“这提供了一个非常好的框架，开发人员可以使用查询来构建应用程序，这是他们通常使用的方式，”他说。“他们可以使用查询来描述可能需要的数据，但他们不受此限制。用户 [...] 仍然可以访问整个应用程序中的所有数据，并且不必提前同步。因此，它实现了同步引擎的所有优势，同步引擎的所有 UX 优势，以及同步引擎的 DX 优势，开发人员的生产力优势，但它不需要预先下载所有数据。”

Zero 是一个[新一代通用同步引擎](https://gist.github.com/pesterhazy/3e039677f2e314cb77ffe3497ebca07b)的例子，Boodman 说。其他新产品包括 [Power Sync](https://www.powersync.com/), [Electric SQL](https://electric-sql.com/), [Convex](https://www.convex.dev/sync) 和 [Jazz Tools](https://jazz.tools/)。

目前，Zero 提供 alpha 版本，该版本于 2024 年底发布。Boodman 说，它更适合爱好者。预计今年晚些时候将推出 Zero 的 beta 版本，该版本专为更广泛的采用而设计。
