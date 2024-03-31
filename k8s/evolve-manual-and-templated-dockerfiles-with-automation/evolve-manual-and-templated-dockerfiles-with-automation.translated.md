# 使用自动化改进手动和模板化 Dockerfile

![用于：使用自动化改进手动和模板化 Dockerfile 的特色图片](https://cdn.thenewstack.io/media/2024/03/365f0bb7-docker-1024x744.png)

[Docker](https://thenewstack.io/containers/how-to-deploy-a-container-with-docker/) 的可移植性让组织可以更轻松地将应用程序迁移到云端或采用混合云策略。应用程序可以在容器中进行本地开发，然后在不进行重大更改的情况下部署到云端。这种灵活性对于希望利用云的可扩展性和成本效益，同时保留一些本地资源的组织至关重要。

通过标准化应用程序运行的环境，Docker 减少了与为开发、测试和生产配置和维护不同环境相关的高昂成本。这种效率加快了开发周期并简化了部署流程，让团队可以更多地专注于开发，而减少对基础设施问题的关注。

问题在于，手动[制作和维护 Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) 对开发者来说提出了重大挑战。这些挑战包括编写和维护配置所花费的时间，以及针对各种项目类型和规模优化 Dockerfile 以实现高效构建的难度。

在决定手动创建 Dockerfile 还是使用抽象工具自动生成 Dockerfile 时，正确的选择取决于多个因素，包括项目的复杂性、团队对 Docker 的熟悉程度以及部署环境的特定要求。

## Dockerfile 困境

对于简单的项目，学习抽象工具的高昂成本可能是不合理的。对于基本的 node 应用程序，一个简单的 Dockerfile 可能如下所示。

```
FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]
```

虽然此 Dockerfile 对于单个应用程序来说很简单，但跨多个[微服务](https://thenewstack.io/microservices/) 管理类似的文件或更新它们以反映新的依赖项会变得越来越复杂且容易出错。

让我们来看一个失控的 Node.js 应用程序 Dockerfile 示例。这是一个夸张的示例，旨在说明随着项目规模的扩大而难以维护的常见缺陷。

```
FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install -g typescript ts-node nodemon

COPY . .

RUN npm install

RUN npm prune --production

CMD ["nodemon", "src/index.js"]
```

## 常见的 Docker 缺陷

虽然你可能不会同时遇到所有这些缺陷，但其中一些缺陷可能会随着时间的推移而出现。让我们看看此 Dockerfile 中的每个问题：

**低效分层**– 此 Dockerfile 创建了不必要的层，因为有多个`RUN`指令可以组合。此外，它低效地处理文件复制和依赖项安装。

**硬编码**– 此 Dockerfile 使用特定版本的 Node.js 镜像 (`node:14`)，而没有一种简单的方法来更新它。使用构建参数 (`ARG`) 来指定版本更具可扩展性，这样无需直接修改 Dockerfile 即可轻松更新。

**全局 NPM 包安装**– 安装全局包（TypeScript、ts-node、nodemon）会使镜像变大，并将构建绑定到这些工具的特定版本。最好将它们作为 dev 依赖项包含在 `package.json` 中并在本地使用它们，以确保跨环境的一致性。

**不必要的操作**– Dockerfile 包含增加构建时间和镜像大小的步骤，例如两次复制所有源文件并在复制源文件后安装不必要的包。此外，在安装所有依赖项后使用`npm prune --production`表明管理生产和开发依赖项的方法效率低下。

## 自动生成 Docker 镜像的案例

随着自动化创建和[管理 Docker 容器](https://thenewstack.io/fugue-security-config-checker-now-supports-cis-docker-benchmark-managed-containers/) 的复杂工具和框架的出现，有充分的理由使用这些技术来节省时间并减少人为错误的可能性。

使用 Jinja2、Mustache 或 EJS 等模板引擎可以帮助从模板生成 Dockerfile。这些模板可以定义 Dockerfile 的结构，并为可配置选项（如基础镜像、环境变量和依赖项）提供占位符。一个简单的脚本可以根据应用程序的要求或特定于环境的配置使用实际值填充这些模板。

### 我们能更进一步吗？

[Nitric](https://github.com/nitrictech/nitric) 等框架通过抽象云服务配置和部署的复杂性，为云应用程序开发带来了智能自动化，包括生成 Dockerfile。

## 如何自动化 Dockerfile 生成

云应用程序通常有多个 API 入口点，例如 `get`、`put`、`patch` 和
## 删除方法

这些应用程序还具有激活触发器的处理程序，例如监听事件主题或运行计划任务。应用程序中的每个入口点都可以使用 Docker 构建到其自己的容器中，然后部署到云容器运行时，例如 AWS Lambda、Google CloudRun 或 Azure Container Apps。

然后，我们可以根据项目的属性决定如何构建这些容器——例如，项目中使用的编程语言或对遥测的需求。在表面层面上，这的便利性似乎在于失去控制，但只要框架还包括内置的“逃生舱口”来保持控制，你仍然可以通过实现自定义 Dockerfile 模板来覆盖默认行为，以便在应用程序中的一些或所有服务中使用。

以下是一个 Docker 模板示例，取自 [Nitric 框架](https://github.com/nitrictech/nitric)，可以轻松覆盖。

## 自动化方法的优势

对于基于容器的部署，自动化框架可以根据应用程序的配置及其使用的服务生成 Dockerfile。这包括设置适当的运行时环境、处理依赖项以及配置应用程序在容器化环境中运行所需的构建步骤。

我们还获得了两个有用的增强功能：

**可移植性**——除了生成 Dockerfile 之外，自动化框架还可以简化部署过程以支持多个云提供商。这意味着应用程序可以部署到 [AWS](https://aws.amazon.com/?utm_content=inline-mention)、[Microsoft](https://news.microsoft.com/?utm_content=inline-mention)Azure，

**本地开发**——自动化框架可以通过模拟云环境来实现云原生应用程序的离线开发和测试。这意味着开发人员可以在与目标部署环境非常相似的免费环境中测试他们的应用程序，从而减少“在我的机器上运行！”综合症。

## 在你的项目中试用

虽然 Dockerfile 模板化可以为 Docker 镜像创建提供一定程度的自动化和标准化，但像 [Nitric](https://nitric.io) 这样的框架基于此概念，为应用程序部署和管理提供了更全面的方法。它们为常见任务提供了一个简化的、高级接口，并能够覆盖或扩展自动生成的 Dockerfile 和部署配置。

开发人员可以在部署前指定自定义 Dockerfile 指令、集成其他工具或服务，甚至手动调整生成的配置。这确保了团队可以实现所需的精确性能优化或功能集成，而不会受到框架自动化的限制。

使用 [Nitric](https://github.com/nitrictech/nitric) 创建概念验证，了解如何简化应用程序开发并自动生成在云中运行应用程序所需的样板。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。