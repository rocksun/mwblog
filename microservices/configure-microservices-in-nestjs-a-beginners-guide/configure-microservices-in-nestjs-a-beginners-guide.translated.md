# 在 NestJS 中配置微服务：初学者指南

![Featued image for: Configure Microservices in NestJS: A Beginner’s Guide](https://cdn.thenewstack.io/media/2024/10/38d0b844-microservices-nestjs-configure-1024x576.jpg)

在 2011 年之前，单体架构是后端开发的主要方法。在这种模型中，整个应用程序被构建为一个单一的、统一的代码库，其中所有组件和服务紧密耦合，并作为一个模块一起部署。单体方法将所有业务逻辑、数据访问、用户界面 (UI) 和其他功能封装在一个可执行文件或应用程序中。

虽然 [单体方法](https://thenewstack.io/monolith-vs-microservice-architecture-for-software-delivery/) 在开发和部署方面提供了简单性，但它在应用程序扩展时带来了重大挑战。使用单个代码库，即使是微小的更改也需要重建和重新部署整个应用程序，从而导致更长的开发周期和更高的引入错误风险。此外，扩展单体应用程序通常效率低下，因为它通常需要扩展整个系统，即使只有单个组件的需求增加。组件之间的紧密耦合也会导致相互依赖，随着团队和代码库的增长，系统变得更加脆弱，更难维护。

然而，单体架构最关键的缺点是其广泛的故障影响，通常被称为“爆炸半径”。一个组件的故障会导致整个系统崩溃，从而导致重大停机。这种相互关联增加了广泛停机的风险，并使故障排除和恢复变得复杂。单个问题可能会级联到整个系统，使其难以隔离和解决，而不会影响其他部分。因此，组织经常面临长时间停机，这会对业务运营和整体用户体验产生严重影响。

尽管存在这些缺点，但由于其简单性和缺乏替代方案，单体方法多年来一直是标准。然而，[微服务](https://thenewstack.io/microservices/) 和其他新的架构范式提供了更灵活、更可扩展的解决方案。

## 什么是微服务？

在微服务架构中，应用程序由小型、独立的服务组成，这些服务通过定义明确的 API 相互通信。微服务将应用程序划分为不同的、松散耦合的服务。每个服务负责特定的功能；例如，在电子商务后端应用程序中，用户身份验证、支付处理、库存管理和其他服务可以独立开发、部署和扩展。这提供了许多优势，包括：

**可扩展性**: 微服务允许独立扩展单个服务。当一个服务遇到高需求时，它可以被扩展，而不会影响整个应用程序。这优化了资源利用率，提高了整体性能。

**技术灵活性**: 在微服务架构中，每个服务可以使用最适合其特定需求的技术、语言或框架进行开发。这种灵活性允许开发团队为每个任务选择最佳工具。

**故障隔离**: 由于微服务的独立性，一个服务的故障不太可能影响整个系统。这最大限度地减少了故障的影响，增强了系统弹性，减少了停机时间。

**开发和部署速度**: 微服务允许团队同时处理不同的服务，从而加快开发流程。持续集成和部署实践更容易实施，从而实现更快的更新和更频繁的改进。

**简化维护和更新**: 微服务的模块化结构使维护和更新应用程序更加直观。可以对单个服务进行更改，而不会影响其他服务，从而降低错误风险并简化测试过程。

**组织对齐**: 微服务促进了围绕特定业务能力组织团队。每个团队可以完全拥有一个服务，从开发到部署和支持，从而提高自主权、问责制和效率。

**增强敏捷性**: 微服务的模块化设计支持迭代开发，允许更灵活地适应不断变化的业务需求，并促进快速创新。

## 单体与微服务：结构差异

在单体应用程序中，所有客户端请求都由单个通用控制器处理。该控制器负责处理请求、执行必要的命令或操作并将响应返回给客户端。本质上，所有业务逻辑和请求处理都是集中式的，这简化了开发过程。
与之相反，微服务架构通过引入应用程序网关增加了额外的复杂性。应用程序网关在微服务设置中充当至关重要的中间层。以下是它的工作原理：

**请求处理**: 网关接收来自客户端的所有传入请求。**路由**: 然后，它根据其路由规则确定应该处理每个请求的适当微服务或控制器。**服务交互**: 选定的控制器与相应的微服务交互以处理请求。**响应聚合**: 微服务完成其任务后，它将结果发送回控制器，然后控制器将其转发到网关。**客户端响应**: 最后，网关将处理后的响应返回给客户端。

这种分层方法将请求路由和业务逻辑的关注点分离，使每个微服务能够专注于其特定功能，而网关则管理请求分发和响应聚合。如果这听起来很复杂，别担心 - 我将详细介绍每个组件，并解释它们如何协同工作。

## 使用 NestJS 实现微服务

[NestJS 是一个渐进式 Node.js 框架](https://thenewstack.io/implementing-iam-in-nestjs-the-essential-guide/)，它利用 [TypeScript](https://roadmap.sh/typescript)，提供了现代 [JavaScript](https://roadmap.sh/javascript) 功能、面向对象编程和函数式编程范式的强大组合。它旨在提供一个原生应用程序架构，帮助开发人员构建高度可测试、可扩展和可维护的应用程序。

在本教程中，我将向您展示如何使用 NestJS 作为主要技术、[NATS](https://nats.io/) 作为通信媒介、Prisma 作为对象关系映射 (ORM) 技术、MySQL 作为数据库以及最后使用 Postman 测试端点来实现微服务。

这种方法将演示如何有效地管理微服务，确保它们无缝通信、易于扩展，并且可以在生产环境中可靠地部署。在此过程中，我将介绍设置微服务架构、管理依赖项和保护部署的最佳实践，为构建健壮高效的分布式系统奠定坚实的基础。

### 设置基础 NestJS 应用程序

在开始之前，请确保已安装 Node.js。Node.js 对于在服务器端运行 JavaScript 代码和管理包至关重要。如果您尚未安装 Node.js，可以从 [官方 Node.js 网站](https://nodejs.org/) 下载。接下来，使用 npm（与 Node.js 捆绑在一起）安装 Nest 命令行界面 (CLI)，这是一个简化 NestJS 应用程序创建和管理的工具。

安装完 Nest CLI 后，设置您的基础 NestJS 应用程序作为您的网关，并将其命名为 `api-gateway`：

启动您喜欢的文本编辑器（例如，VS Code、Sublime Text）并打开 NestJS 应用程序的父目录（包含您基础应用程序父文件夹的目录）。导航到基础应用程序文件夹（即 `api-gateway`）并打开一个新的终端实例。大多数现代文本编辑器都具有内置的终端功能。对于 VS Code，您可以通过从顶部菜单中选择 `Terminal`，然后选择 `New Terminal` 来打开终端。对于 Sublime Text，您可能需要使用 Terminus 等插件在编辑器中打开终端。

### 构建后端应用程序

您的基础应用程序成功启动并运行后，下一步是为博客网站构建一个基础后端应用程序。您将在本教程中实现两个独立的服务：一个用于管理读者，另一个用于处理博客文章的创建、读取、更新和删除 (CRUD) 操作。如果您以前使用过 NestJS，那么项目结构将很熟悉且简单。但是，如果您不确定如何组织，我将简要概述一下结构。

当您构建一个新的 NestJS 项目时，默认结构通常包括：

1. **src**: 这是大多数应用程序代码所在的目录。

    * **app.module.ts**: 将应用程序的不同部分联系在一起的根模块。
    * **app.controller.ts**: 负责处理传入请求并返回响应的控制器。
    * **app.service.ts**: 包含业务逻辑的服务；可以注入到控制器中。
    * **main.ts**: 应用程序的入口点，在这里引导 NestJS 应用程序。
2. **test**: 此目录包含应用程序的测试文件。

    * **app.e2e-spec.ts**: 端到端测试文件。
    * **jest-e2e.json**: 使用 Jest 进行端到端测试的配置文件。
3. **node_modules**: 此目录包含项目的所有已安装依赖项。
4. **package.json**: 此文件列出了项目的依赖项和脚本。

5. **tsconfig.json**: TypeScript 配置文件。

6. **nest-cli.json**: NestJS CLI 的配置文件。

### 创建微服务和网关
下一步是创建两个额外的应用程序，它们将充当微服务，并分别命名为 `reader-mgt` 和 `article-mgt`。这些应用程序将在架构中充当独立的微服务。之后，安装 `@nestjs/microservices` 和 `nats` 库以启用服务之间的通信。然后配置这两个应用程序以通过 NATS 监听请求，确保它们能够相应地处理传入的消息。

因此，在同一个文件夹中，运行以下命令：

```bash
nest g application reader-mgt
nest g application article-mgt
```

现在，这两个服务已经搭建好了，配置您的网关来处理客户端请求并将它们路由到相应的服务。首先，安装 `@nestjs/microservices` 和 `nats` 依赖项。然后创建一个 NATS 模块，该模块将在 [API 网关](https://thenewstack.io/api-gateway-checklist-how-strong-is-your-apis-front-door/) 的应用程序模块中注册，以实现网关和微服务之间的正常通信：

如果您不在 `gateway` 文件夹中，请使用 `cd` 命令导航到该文件夹。到达那里后，转到 `src` 文件夹并创建一个名为 `nats-client` 的新目录，该目录将用作 NATS 客户端配置的位置。之后，在 `nats-client` 文件夹中创建一个名为 `nats.module.ts` 的文件，并添加以下代码：

```typescript
import { Module } from '@nestjs/common';
import { ClientsModule, Transport } from '@nestjs/microservices';

@Module({
  imports: [
    ClientsModule.register([
      {
        name: 'NATS_SERVICE',
        transport: Transport.NATS,
        options: {
          servers: ['nats://localhost:4222'],
        },
      },
    ]),
  ],
  exports: [ClientsModule],
})
export class NatsClientModule {}
```

此代码创建了一个 `NatsClientModule`，您将在稍后将其注册到 API 网关的应用程序模块中。首先，它从之前安装的 `@nestjs/microservices` 库中导入 `Module` 装饰器以及 `ClientsModule` 和 `Transport` 声明。接下来，它注册 `NATS_SERVICE` 并将传输指定为 `Transport.NATS`。NestJS 默认支持各种传输客户端，但对于本示例，请坚持使用 NATS。

然后它定义了一个 `options` 对象，该对象指定了 `servers` 属性并将 NATS 服务器地址设置为 `nats://localhost:4222`。最后，它导出注册的 NATS 客户端以使它们可供其他模块访问，如果您在网关中有多个模块，这将很有用。例如，您可能有一个用户模块、文章模块、读者模块等等。但是，本教程使用单个控制器和模块来处理读者和文章。

完成此操作后，您现在可以继续到 `app.module.ts` 文件并注册 `NatsClientModule`：

```typescript
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { NatsClientModule } from './nats-client/nats.module';

@Module({
  imports: [NatsClientModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

此时，您已经完成了大约 80% 的 API 网关配置。最后一步是在 `app.controller.ts` 文件中定义 API 路由。导航到该文件并添加以下代码：

```typescript
import { Controller, Get, Post, Body, Inject } from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';

@Controller('api')
export class AppController {
  constructor(@Inject('NATS_SERVICE') private readonly natsClient: ClientProxy) {}

  @Post('save-reader')
  async saveReader(@Body() reader: any) {
    return this.natsClient.send('save-reader', reader);
  }

  @Get('get-all-readers')
  async getAllReaders() {
    return this.natsClient.send('get-all-readers', {});
  }

  @Post('save-article')
  async saveArticle(@Body() article: any) {
    return this.natsClient.send('save-article', article);
  }

  @Get('get-all-articles')
  async getAllArticles() {
    return this.natsClient.send('get-all-articles', {});
  }

  @Post('delete-article')
  async deleteArticle(@Body() articleId: any) {
    return this.natsClient.send('delete-article', articleId);
  }
}
```

这定义了 API 路由，这些路由将处理传入的 HTTP 请求并将它们转发到 NATS 服务以进行处理。`AppController` 类使用 `@Controller` 装饰器来指定所有端点的基本路由，即 `'api/'`。在此控制器中，使用 `@Inject` 装饰器注入 NATS 客户端，将其与 `'NATS_SERVICE'` 令牌关联。控制器包含几个端点：`POST /save-reader` 和 `GET /get-all-readers` 用于管理读者，以及 `POST /save-article`、`GET /get-all-articles` 和 `POST /delete-article` 用于管理文章。每个端点方法都使用 `natsClient.send` 方法将命令发送到 NATS 服务，并将请求主体作为有效负载传递。此设置允许 API 网关通过 NATS 将客户端请求中继到相应的微服务。

最后，执行 `npm run start:dev` 命令启动 API 网关应用程序。这将验证应用程序是否顺利运行且没有任何错误。

![api-gateway 应用程序的屏幕截图](https://cdn.thenewstack.io/media/2024/10/11eb0f52-api-gateway_1-1024x640.png)
图 1：api-gateway 应用程序

### 配置通信服务
接下来，配置您的服务以处理来自正在运行的 API 网关的请求，处理它们并将响应发送回。但是，在继续之前，有一个重要的步骤：在本地设置 NATS 服务器。由于您将 NATS 服务器地址指定为 `nats://localhost:4222`，因此网关和服务都将期望在您的本地机器上运行 NATS 服务器。

出于开发目的，在本地安装 NATS 服务器。虽然您可以在 [Docker](https://www.docker.com/?utm_content=inline+mention) 容器中运行它，但为了简单起见，请使用本地设置。对于 Linux 和 macOS 用户，使用 `brew install nats-server` 安装 NATS 服务器，并运行 `nats-server` 启动服务。对于 Windows 用户，请使用 `choco install nats-server`。如果 `choco` 未被识别，请确保通过运行以下命令安装 Chocolatey：

```bash
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ProgramFiles%\Chocolatey\bin"
```

然后通过运行 `choco --version` 验证安装。如果您需要进一步的指导，请咨询 [NATS 文档](https://docs.nats.io/running-a-nats-service/introduction/installation)。
![图 2：本地运行的 NATS 服务器截图](https://cdn.thenewstack.io/media/2024/10/e589f8d3-nats-server_2-1024x192.png)
图 2：本地运行的 NATS 服务器

### 配置您的第一个服务
现在您可以配置您的第一个服务，`article-mgt`。转到 `main.ts` 文件，它是此服务的入口点，并将默认代码替换为：

```typescript
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { Transport } from '@nestjs/microservices';

async function bootstrap() {
  const app = await NestFactory.createMicroservice(AppModule, {
    transport: Transport.NATS,
    options: {
      url: 'nats://localhost:4222',
    },
  });
  await app.listen();
}
bootstrap();
```

此代码将 `article-mgt` 从一个独立的应用程序转换为一个 NestJS 微服务实例，并将其配置为使用 NATS 作为传输机制，指定服务器地址 (`nats://localhost:4222`) 连接到 NATS 服务器。

接下来，在 `src` 文件夹中创建一个名为 `dto` 的新目录，然后创建一个名为 `dto.ts` 的文件，该文件将包含预期的有效负载结构。DTO 代表数据传输对象，它们是用于在应用程序的不同层之间传输数据的简单对象，尤其是在网络请求期间。在这种情况下，DTO 有助于定义后端应用程序从客户端请求中期望的有效负载的结构和类型。如果需要，您可以使用 `class-validator` 依赖项实现进一步的验证。但是，为了使本文重点突出，我们不会在这里使用它。如果您有兴趣，可以在 NestJS 官方 [文档](https://docs.nestjs.com/techniques/validation) 中了解更多关于 `class-validator` 的信息。

```typescript
import { IsNotEmpty, IsString } from 'class-validator';

export class saveArticleDto {
  @IsNotEmpty()
  @IsString()
  title: string;

  @IsNotEmpty()
  @IsString()
  content: string;
}

export class deleteArticleDto {
  @IsNotEmpty()
  id: string;
}
```

此代码定义了两个 DTO 用于处理 `article-mgt` 服务中的数据。`saveArticleDto` 类指定了保存文章的结构，需要一个 `title` 和 `content`。而 `deleteArticleDto` 类定义了删除文章的结构，它需要一个 `id` 来标识要删除的文章。这些 DTO 有助于确保在应用程序的不同部分之间传递的数据定义明确、一致且符合预期类型。文章有三个路由，但只定义了两个 DTO 类。这是因为第三个路由，它检索所有文章，不需要任何有效负载。

现在转到 `app.controller.ts` 文件并修改代码。

```typescript
import { Controller } from '@nestjs/common';
import { MessagePattern } from '@nestjs/microservices';
import { AppService } from './app.service';
import { saveArticleDto } from './dto/dto';
import { deleteArticleDto } from './dto/dto';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @MessagePattern({ cmd: 'saveArticle' })
  async saveArticle(data: saveArticleDto) {
    return this.appService.saveArticle(data);
  }

  @MessagePattern({ cmd: 'getAllArticles' })
  async getAllArticles() {
    return this.appService.getAllArticles();
  }

  @MessagePattern({ cmd: 'deleteArticle' })
  async deleteArticle(data: deleteArticleDto) {
    return this.appService.deleteArticle(data.id);
  }
}
```

![图 3：app.controller.ts 中代码的截图](https://cdn.thenewstack.io/media/2024/10/27686622-app.controller-ts_3-1024x640.png)
图 3：`app.controller.ts` 中的代码

您可能会注意到控制器方法中函数名称下方的红色波浪线；这是因为您还没有在 `app.service.ts` 中定义这些函数。在解决这个问题之前，让我解释一下代码：它导入 DTO 以对有效负载执行类型检查，确保传递给函数的数据符合预期结构。`@MessagePattern` 装饰器指定了如何处理消息。它接受一个对象，其中 `cmd` 属性定义一个命令字符串。此字符串必须与之前在 API 网关中指定的命令匹配。API 网关使用此命令来确定对给定 API 请求调用哪个函数，在将请求转发之前将命令附加到请求中。

### 使用 Prisma 与您的数据库交互
要使用 Prisma 与您的数据库交互，请创建一个 Prisma 模块和服务，您可以在 `app.service.ts` 文件中使用它。首先，在 `src` 目录中创建一个名为 `prisma` 的文件夹。然后，在这个文件夹中，创建两个文件：`prisma.module.ts` 和 `prisma.service.ts`。`PrismaService` 在 `prisma.service.ts` 中扩展了 Prisma 的 `PrismaClient` 类，并通过使用 `DATABASE_URL` 环境变量配置数据库连接 URL 来定制 Prisma 客户端。`PrismaModule` 在 `prisma.module.ts` 中定义了一个提供 `PrismaService` 的模块，允许它被注入并在微服务的其他部分中用于数据库操作。

```typescript
// prisma.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient {
  constructor() {
    super({
      datasources: {
        db: {
          url: process.env.DATABASE_URL,
        },
      },
    });
  }

  async onModuleInit() {
    await this.$connect();
  }

  async onModuleDestroy() {
    await this.$disconnect();
  }
}

// prisma.module.ts
import { Module } from '@nestjs/common';
import { PrismaService } from './prisma.service';

@Module({
  providers: [PrismaService],
  exports: [PrismaService],
})
export class PrismaModule {}
```

现在，转到 `app.service.ts` 并添加下面的代码来定义必要的函数。简要解释一下：`saveArticle ` 函数以 `data` 作为参数，它必须是 `saveArticleDto` 类型，如前所述。该函数使用 try-catch 块来处理该过程。首先，它尝试将数据插入数据库。之后，它调用 `getAllArticles` 函数来检索更新后的文章列表。由于 `getAllArticles` 是一个异步函数，它使用 `await` 关键字。完成此操作后，该函数返回一个对象作为响应，其中包含 `HttpCode`，其中包括 `statusCode`、一条消息和一个字符串。此外，`getAllArticles` 函数从数据库返回所有文章，而 `deleteArticle` 函数根据提供的 ID 处理文章的删除。

```typescript
import { Injectable } from '@nestjs/common';
import { PrismaService } from './prisma/prisma.service';
import { saveArticleDto } from './dto/dto';
import { deleteArticleDto } from './dto/dto';

@Injectable()
export class AppService {
  constructor(private prisma: PrismaService) {}

  async saveArticle(data: saveArticleDto) {
    try {
      await this.prisma.article.create({
        data: {
          title: data.title,
          content: data.content,
        },
      });
      const articles = await this.getAllArticles();
      return {
        HttpCode: {
          statusCode: 201,
          message: 'Article saved successfully',
          data: articles,
        },
      };
    } catch (error) {
      return {
        HttpCode: {
          statusCode: 500,
          message: 'Failed to save article',
          data: error,
        },
      };
    }
  }

  async getAllArticles() {
    const articles = await this.prisma.article.findMany();
    return {
      HttpCode: {
        statusCode: 200,
        message: 'Articles retrieved successfully',
        data: articles,
      },
    };
  }

  async deleteArticle(id: string) {
    try {
      await this.prisma.article.delete({
        where: {
          id: id,
        },
      });
      const articles = await this.getAllArticles();
      return {
        HttpCode: {
          statusCode: 200,
          message: 'Article deleted successfully',
          data: articles,
        },
      };
    } catch (error) {
      return {
        HttpCode: {
          statusCode: 500,
          message: 'Failed to delete article',
          data: error,
        },
      };
    }
  }
}
```

### 启动您的第一个服务
完成这些操作后，您现在可以启动您的 `articles-mgt` 服务并检查它是否能顺利运行，没有任何错误。为此，只需执行命令 `'npm run start:dev'`。

![图 4：article-mgt 服务运行的截图](https://cdn.thenewstack.io/media/2024/10/65f501f0-article-mgt_4-1024x640.png)
图 4：`article-mgt` 服务

### 配置您的第二个服务
现在您已经完成了 `article-mgt` 微服务的配置，接下来配置 `reader-mgt` 服务。该服务将处理两个主要操作：注册读者和检索所有已注册读者。由于设置过程与我之前介绍的非常相似，为了节省时间，我将跳过详细的解释。实现本质上是相同的，只是在不同的服务上下文中。

要设置 `reader-mgt` 服务，首先导航到 `reader-mgt` 目录。由于此服务中的 `main.ts` 文件将与 `article-mgt` 服务中的代码相同，因此您可以简单地将 `article-mgt main.ts` 文件中的内容复制并粘贴到 `reader-mgt` 中的相应文件中。接下来，将 `article-mgt` 服务中的整个 `prisma` 目录复制到 `reader-mgt` 服务中。但是，这不会立即生效；您需要在 `reader-mgt` 服务中安装并初始化 Prisma。运行 `npm install Prisma @prisma/client` 来安装 Prisma，然后执行 `npx prisma generate` 来初始化它。此外，定义读者的模式并执行迁移。不要忘记从 `article-mgt` 中的 `.env` 文件中复制数据库连接字符串，因为没有它，`reader-mgt` 微服务将无法连接到数据库。

![图 5：读者和文章模型的截图](https://cdn.thenewstack.io/media/2024/10/ce5c42cf-reader-article-modules_5-1024x640.png)
图 5：读者和文章模型

定义读者模式后，运行 `npx prisma migrate dev` 将迁移应用到数据库，这将向 MySQL 数据库添加 `reader` 表。

最后一步是配置 `reader-mgt` 服务中的 `app.controller.ts` 和 `app.service.ts` 文件。此过程类似于您在 `article-mgt` 服务中所做的操作。在控制器中，定义路由，然后将这些路由映射到服务中的相应函数。您可以使用 `article-mgt` 微服务配置作为参考来指导您完成此过程。

### 运行您的微服务
配置完 `reader-mgt` 服务的 `app.service.ts`、`app.module.ts` 和 `app.controller.ts` 文件后，最后一步是运行微服务以确保一切正常运行且没有错误。这包括验证控制器中的路由是否正确映射到服务中的函数，以及微服务是否可以按预期处理请求。

确认所有配置到位后，您可以使用 `npm run start:dev` 命令启动 `reader-mgt` 服务。这将在开发模式下启动服务，允许您检查任何问题并确保服务无缝运行。

![图 6：reader-mgt 微服务运行的截图](https://cdn.thenewstack.io/media/2024/10/f428f8f6-reader-mgt_6-1024x640.png)
图 6：reader-mgt 微服务

### 测试您的应用程序
如果您已经完成了这一步，恭喜您！项目的编码部分已完成，您的 `api-gateway`、`reader-mgt` 和 `article-mgt` 服务已启动并运行，没有任何错误。下一步是使用 Postman 测试应用程序，并确保它按预期执行。使用 Postman 向 API 网关发送请求，并验证操作是否由微服务正确处理。这将有助于确认应用程序的所有部分都无缝地协同工作。

![图 7：显示 /save-reader 端点工作的截图](https://cdn.thenewstack.io/media/2024/10/393ac4e1-save-reader_7-1024x640.png)
图 7：`/save-reader` 端点

![图 8：显示 /get-all-readers 返回所有已注册读者的截图](https://cdn.thenewstack.io/media/2024/10/acdfdbfd-get-all-readers_8-1024x640.png)
图 8：`/get-all-readers`

该图像说明了 `save-reader` 和 `get-all-readers` 端点通过 API 网关到达 `reader-mgt` 微服务的流程。API 网关首先接收请求，识别正确的命令，并通过 NATS 将它们转发到 `reader-mgt` 服务。然后，`reader-mgt` 服务通过创建新读者或检索所有读者来处理请求。请求成功后，服务将返回相应的响应。

接下来，通过发送请求来创建、删除和检索文章来测试 `article-mgt` 端点。首先，向 `/save-article` 端点发送三个创建请求，以将三篇文章添加到数据库中，如图 9 所示。然后，向 `/delete-article` 端点发送一个请求，以删除 ID 为 2 的文章。最后，向 `/get-all-articles` 端点发出一个 GET 请求，以检索更新后的文章列表，确认删除成功，并且剩余的文章已正确列在数据库中。

![图 9：显示 /save-article 端点工作的截图](https://cdn.thenewstack.io/media/2024/10/393ac4e1-save-reader_7-1024x640.png)
图 9：`/save-article` 端点

![图 10：显示 /delete-article 端点工作的截图](https://cdn.thenewstack.io/media/2024/10/393ac4e1-save-reader_7-1024x640.png)
图 10：`/delete-article` 端点

![图 11：显示 /get-all-articles 端点工作的截图](https://cdn.thenewstack.io/media/2024/10/393ac4e1-save-reader_7-1024x640.png)
图 11：`/get-all-articles` 端点
## 图 9: `/save-article` 请求

## 图 10: `/delete-article` 请求

## 图 11: `/get-all-articles` 请求

## 结论

恭喜您完成了本篇全面设置指南！您已经成功地完成了使用 NestJS、Prisma、MySQL 和 NATS 配置健壮的微服务架构的复杂过程。虽然您已经成功地设置了功能性的微服务架构，但始终有改进的空间。

在继续开发应用程序时，请考虑实施其他功能，例如健壮的错误处理、安全措施和全面的日志记录。探索 Docker 进行容器化和 [Kubernetes](https://thenewstack.io/kubernetes/) 进行编排可以进一步简化您的开发和部署流程。

感谢您跟随本指南。您对掌握这些技术的奉献精神无疑将为创建复杂且有弹性的应用程序铺平道路。如果您需要本博文的代码，请在我的 [GitHub 仓库](https://github.com/RaymondZziwa/microservices) 中找到它。祝您编码愉快，并祝您在持续开发中一切顺利！

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等。