
<!--
title: 后端开发效率：缓存的关键作用
cover: https://cdn.thenewstack.io/media/2024/06/8b5e4e0a-caching.jpg
-->

其简化操作、提升可扩展性和提高应用程序可靠性的能力，突显了其作为后端架构基础支柱的地位。

> 译自 [Backend Development Efficiency: The Critical Role of Caching](https://thenewstack.io/backend-development-efficiency-the-critical-role-of-caching/)，作者 Zziwa Raymond。

毫无疑问，我们许多人都有过完成一个项目后才发现我们的应用程序在从后端获取数据时可以做得更好的挫败感。这不仅会阻碍我们应用程序的效率，还会赶走用户，迫使他们寻找替代方案。因此，一个出色的应用程序创意可能会变得不可靠且不可用。但有一个解决方案可以解决这些挑战。

缓存是 [提高应用程序性能](https://thenewstack.io/why-http-caching-matters-for-apis/) 的关键。如果实施得当，它可以通过简化性能来显著提升用户体验。让我们探讨缓存的基本原理。

从本质上讲，缓存涉及临时存储从数据库中检索的数据。当对相同数据发出后续请求时，后端应用程序会无缝地传递缓存数据，而不是等待 API 再次检索它。

我将使用一个由 Nest.js、Redis、Redis-commander、npm、Docker 和 Postman 组成的综合堆栈来说明这个概念。Nest.js 是一个基于 Node.js 构建并利用 [TypeScript](https://thenewstack.io/typescript-vs-javascript/) 的强大后端框架，它将作为我们的基础。以其高速性能而闻名的 Redis 将充当我们的缓存数据库，而 npm 则促进包管理。Docker 将使我们能够将 Redis 数据库容器化，从而提高可扩展性和部署效率。此外，Redis-commander 将为监视我们的缓存数据库提供一个用户友好的界面。最后，Postman 是一个用于 [API 测试](https://thenewstack.io/api-management/) 和请求处理的多功能工具，它将发挥关键作用。

首先，打开终端并使用 Nest CLI 创建一个新的 Nest.js 应用程序。应用程序成功构建后，导航到项目文件夹并使用 VS Code 或任何其他首选代码编辑器将其打开。

```
npm install -g @nestjs/cli //command to install the nest-cli
nest new caching-demo //command to scaffold my nestjs application
cd caching-demo //navigate to the root folder of the application
code . //open the application directory with vs code
npm run start:dev //start the application
```

接下来，安装一些将帮助我们实现目标的包。需要注意的是，我们不会使用许多后端框架提供的内存缓存技术。虽然内存缓存有其优点，例如速度，但它也有明显的缺点。最重要的是，数据存储在 RAM 中，这可能不理想，尤其是当您的服务器或托管机器资源有限时。

![](https://cdn.thenewstack.io/media/2024/06/896aadd0-image4.png)

在代码编辑器中，我们将打开一个新终端并通过运行以下命令来安装依赖项：

```
npm install @nestjs/cache-manager cache-manager //command to install the cache-manager
npm install -D @types/cache-manager //command to install cache-manager types so as typescript doesnt throw errors as we work through our code
npm install cache-manager-redis-yet //command to install the redis-store
```

首先，我们将导航到 `src` 文件夹并打开 `app.module.ts` 文件，然后导入并注册 `CacheModule`。此外，我们将通过传递一个参数对象来配置模块。这些参数将使我们的应用程序能够连接到 Redis 数据库，我们稍后会将其 Docker 化。

![](https://cdn.thenewstack.io/media/2024/06/53c25c4a-image2.png)

正如 `app.module.ts` 文件中所证明的，`CacheModule` 已成功导入并注册。此外，我们初始化了一个参数对象来配置我们的缓存存储。这些参数包括：

- `store`：定义要使用的缓存存储。
- `host`：指定我们的 Redis 数据库将运行的服务器。
- `port`：指示访问 Redis 的端口。
- `username` 和 `password`：出于我们的目的而留空。
- 还可以根据需要添加其他值得注意的属性，例如 `ttl`（生存时间），它确定数据在数据库中缓存的持续时间。但是，对于本文的范围，我们不会包含它，因为它对我们的演示并不重要。

为了与缓存数据库交互，我们需要将 `CACHE_MANAGER` 实例注入到我们的控制器中。此实例充当我们的应用程序控制器和缓存数据库之间通信的中介，因此需要在控制器级别执行检查。如果数据已经存在于缓存数据库中，则服务不会参与该过程。

![](https://cdn.thenewstack.io/media/2024/06/8920ba22-image9-1024x685.png)

在注入缓存管理器之后，我们在控制器中定义了一个名为 `getSampleData` 的函数。此函数负责返回一个包含属性的对象，例如 `id`（字符串）、`items`（数字数组）和 `users`（字符串数组）。在内部，此函数调用另一个方法，`getSampleData`，它位于 `app.service.ts` 文件中定义的 `AppService` 类中。

此外，我们将 `AppService` 注入到控制器中，从而授予对其成员的访问权限。我们控制器的路由已配置为 `/api/test/cache`，用作测试我们的缓存配置的端点。

![](https://cdn.thenewstack.io/media/2024/06/9bc5d207-image11.png)

现在，让我们深入了解令人兴奋的部分！`cache_manager` 提供了各种方法，但我们将重点关注其中四到五个方法。

首先，我们有 `get(key)` 方法，它接受一个键作为输入，从缓存数据库中检索相应的数据并返回它。

接下来是 `set(key, value)` 方法。与 `get` 方法类似，它接受两个参数：一个键和一个值。此方法将指定的值存储在缓存数据库中，与键相关联。

接下来，我们介绍一下 del(key) 方法。当调用该函数时，此函数将从缓存数据库中删除与此键关联的数据。

最后，我们研究一下 reset() 方法。这个强大的函数将清空整个缓存数据库，使它保持为空状态，并可容纳新数据。

借助这些方法，我们就可以高效地管理缓存数据库并优化应用程序的性能。在理解了上述功能后，我们来增强控制器中的 getSampleData 函数。当接收到一个请求时，控制器首先会检查缓存数据库。如果存在缓存数据，控制器会立即将数据返回给用户，而不用调用服务。但是，如果没有找到缓存数据，控制器会调用服务以获取数据。一旦检索到数据，它将被缓存以供将来请求使用，然后返回给用户。这种方法可以通过最小化对服务的不必要的调用来优化性能。

![](https://cdn.thenewstack.io/media/2024/06/51dff372-image1.png)

接下来详细解释控制器中所做的更改：

我们把 getSampleData() 函数改成了异步函数，表示它会返回一个 promise。因此，该函数的返回类型已更新为一个 promise，用来解决包含预定义属性的对象。

收到请求后，控制器首先检查是否存在与键 "UD" 对应的缓存数据。如果存在这样的数据（使用 if (cachedData) 检查），则将它作为 JSON 响应返回给用户。

在未找到缓存数据的情况下，控制器继续调用 AppService 的 getSampleData 方法。在检索到数据后，将其转换为字符串并使用 this.cacheManager.set('UD', JSON.stringify(fetchedSampleData)) 以键“UD”存储在缓存数据库中。随后，将数据返回给用户。

为了确保无缝执行，app.service.ts 模块中的 getSampleData 函数也已修改为异步。这允许在控制器中调用函数时使用 await 关键字，从而防止出现未定义值的问题。

![](https://cdn.thenewstack.io/media/2024/06/1a964e04-image3.png)

下一步涉及创建 docker-compose.yml 文件。此文件有助于提取 Redis 和 Redis-commander 镜像，使我们能够轻松运行容器。有了 Docker Compose，我们将定义项目所需的服务，包括用于缓存数据库的 Redis 和用于用户友好界面的 Redis-commander。配置后，Docker Compose 将编制安装，确保容器正常运行。

![](https://cdn.thenewstack.io/media/2024/06/f6f582db-image10.png)

为了提供一个简洁的概述，version 指令被设置为“3.8”，表示正在使用的 Docker Compose 文件格式的版本。随后，我们定义要执行的服务，即 Redis 和 redis-commander。每项服务都会与一个镜像相关联，Docker 会检索该镜像来实例化各自的容器。

关于 Ports 配置，它指定容器将在其上操作的端口。然后将映射这些端口以启用外部访问。

要详细了解 redis-commander 中的特定变量，环境变量有助于指定 Redis-commander 连接的 Redis 位置。此外，container_name 属性指定容器的名称，而主机名表示分配给容器的主机名。虽然容器名称和主机名有点不言而喻，但它们是容器管理的基本组成部分。现在，我们返回终端执行 Docker Compose 文件，启动我们服务的构建和启动过程。在运行以下命令之前，请确保系统中已安装 Docker Desktop。如果没有，您可以从 Docker 官网下载。否则，如果没有安装 Docker Desktop 就尝试执行命令会导致出错。

```
docker-compose up --build //command to build and start our redis and redis-commander containers
```

![](https://cdn.thenewstack.io/media/2024/06/b0f5a6f7-image7.png)

在两个容器平稳运行且无错误后，我们可以继续启动 Postman。接下来，我们将从中开始发送请求以亲身体验缓存。此外，我们将导航到 http://127.0.0.1:8081 来访问 Redis-commander 界面。此界面将允许我们监控和管理 Redis 数据库的内容，提供对其操作的有价值的见解。

![](https://cdn.thenewstack.io/media/2024/06/5dff60ad-image8.png)

![](https://cdn.thenewstack.io/media/2024/06/0c6e8936-image6.png)

实现 52 毫秒的 API 响应时间当然非常令人满意。在验证 Redis-commander 时，我们可以确认成功保存了“UD”键下的数据。现在，让我们发起另一个请求来探索缓存功能。这将使我们能够直接看到缓存如何优化响应时间，从而提高我们应用程序的整体效率。

![](https://cdn.thenewstack.io/media/2024/06/235d3faf-image5.png)

瞧！由于缓存的魔力，我们的 API 响应时间已大幅下降至仅 9 毫秒。这甚至不到初始请求返回响应时间的一半。这突显了缓存对后端开发不可或缺的作用。

缓存不仅仅是一种技术；它是一个改变游戏规则的技术。它显著提高了性能，提升了用户体验并优化了资源利用率。通过智能地存储经常访问的数据，缓存最大限度地减少了冗余计算和数据库查询，从而实现了闪电般的响应和更流畅的用户交互。

在速度至上且用户期望不断提高的 Web 开发动态世界中，缓存成为效率的灯塔。总之，我们对缓存领域的探索阐明了其在优化后端性能方面的变革力量。从显著减少 API 响应时间到提升整体用户体验，缓存已成为现代 Web 开发中的基石技术。

通过智能地存储和检索数据，缓存最大限度地减少了计算开销和数据库负载，从而实现了更快、更具响应性的应用程序。通过我们的探索，我们亲眼目睹了缓存如何彻底改变应用程序性能，确保更流畅的用户交互和更高的效率。

随着我们驾驭不断发展的 Web 开发领域，很明显，缓存仍然是我们武器库中的一个重要工具。它简化操作、提高可扩展性和提升应用程序可靠性的能力突显了其作为后端架构基础支柱的地位。

在追求卓越的过程中，让我们将缓存作为一项基本原则，利用其功能打造卓越的数字体验，给用户留下持久的印象。让我们共同继续释放缓存的全部潜力，并将我们的应用程序推向性能和创新的新高度。

有兴趣了解更多有关如何驾驭数据的信息吗？数据驱动的组织在盈利能力上可以比竞争对手高出 6%，在生产力上可以高出 5%。成为数据驱动的意味着什么？作为领导者，您如何驾驭数据？[查看我们的指南](https://www.andela.com/resources/navigating-data-driven-leadership?utm_medium=contentmarketing&utm_source=ebook&utm_campaign=client-global-2024-06-13-thenewstack&utm_content=data-driven%20guide&utm_term=ebook)
