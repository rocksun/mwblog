# 开源驱动十二要素现代化项目

![Featued image for: Open Source Drives the Twelve-Factor Modernization Project](https://cdn.thenewstack.io/media/2025/01/bb26f057-twelve-factor-open-source_modernization-1024x576.jpeg)

十二要素方法论是一套包含12个原则的体系，使公司能够以统一且高度可管理的方式创建、运行和维护企业级软件即服务 (SaaS) 应用程序。十二要素方法论不依赖于任何特定产品、技术或工具集。相反，它是一种软件开发理念，其驱动力是可移植性、弹性、稳定性和成本效益。

十二要素应用由Heroku联合创始人Adam Wiggins于2011年创建，因此已经存在一段时间了。多年来，[十二要素原则](https://thenewstack.io/learn-12-factor-apps-before-kubernetes/)帮助开发人员创建在云中运行的更具弹性、更易于扩展、管理和维护的应用程序。

十二要素方法论首次出现时，基于Web的应用程序和[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)仍处于起步阶段。从那时起发生了很多变化，但十二要素方法论在很大程度上保持不变。现在是将其现代化并使其与我们今天使用技术的方式保持一致的时候了，因此[十二要素方法论已开源](https://thenewstack.io/heroku-moved-twelve-factor-apps-to-open-source-whats-next/)。

在深入探讨十二要素方法论开源的目的和影响之前，我将首先介绍其背后的原则。

## 十二要素

以下是驱动十二要素的原则的简要回顾，包括每个原则的含义以及如何使用它们。

### 要素 1：代码库

**含义：**每个应用使用一个代码库，通过版本控制进行跟踪，并进行多次部署。这确保所有与应用程序相关的资产都在单个存储库中进行管理。

**应用方式：**通常，支持单个代码库意味着将项目的所有源代码和辅助工件保存在单个源代码存储库中，例如GitHub、BitBucket、AWS CodeCommit或[Google Cloud](https://cloud.google.com/?utm_content=inline+mention) Source Repositories。代码库不应散布在各种存储库中。

### 要素 2：依赖

**含义：**明确声明并隔离所有依赖项，以避免隐式依赖于系统工具或库。这使应用程序更易于预测和管理。

**应用方式：**支持依赖原则的关键是使用以受控方式存储独立库和包的存储库。应用程序应将自定义代码与独立开发的库分开，并在配置文件中列出这些库。然后，在运行应用程序时，独立库会在构建和运行时添加到项目中。库不与源代码一起存储，而是存储在由库开发者控制的单独存储库中。

一些此类存储库的示例包括[npm](https://www.npmjs.com/)（用于[Node.js](https://roadmap.sh/nodejs) 项目）、[PyPI](https://pypi.org/)（用于[Python](https://thenewstack.io/python/)）、[MVN Repository](https://mvnrepository.com/)（用于[Java](https://thenewstack.io/introduction-to-java-programming-language)）、[Chocolatey](https://chocolatey.org/)（用于.NET）和[RubyGems](https://rubygems.org/)（用于Ruby编程语言）。

### 要素 3：配置

**含义：**将不同部署之间变化的任何配置与代码分开存储。这允许您更轻松地进行更改，而无需修改代码库。

**应用方式：**将配置与代码分离已成为企业系统架构中的基本实践。有时，配置信息存储在清单文件中。Kubernetes等框架会自动将清单中声明的信息注入环境中。此外，配置更新是通过更改清单文件中的信息来执行的。框架会注意到更改并自动更新环境。

配置要素有一个开放的更新提案[(issue #4](https://github.com/twelve-factor/twelve-factor/issues/4))。

### 要素 4：后端服务

**含义：**将后端服务（如数据库、队列和内存缓存）视为附加资源，可以通过存储在配置中的URL或其他定位器进行访问。这使得服务易于互换。

**应用方式：**该原则要求通过标准协议（例如HTTP/HTTPS连接）进行资源访问。
理解使用库和命令行界面 (CLI) 工具的关键在于，这些技术是对实际资源的抽象。它们与资源之间没有紧密的绑定。程序员声明对资源的访问凭据以及要执行的操作。工具负责处理与资源交互的细节。

理论上，程序员应该能够以最小的影响从一个资源提供商切换到另一个资源提供商。但是，与任何技术一样，魔鬼总是隐藏在细节中。因此，程序员应该使用基于 TCP/IP 的资源。然后，代码将被构建为以通用的方式访问资源。

### 因素 5：构建、发布、运行
**含义：**严格分离部署过程的构建、发布和运行阶段。构建阶段编译代码，发布阶段添加特定于环境的配置，运行阶段执行应用程序。
**如何应用：**诸如 Jenkins 和 TeamCity 之类的综合 CI/CD 应用程序可用于支持构建、发布、运行原则。这些工具通常允许程序员定义应用程序的配置设置和源代码存储库。这些工具具有脚本，可以自动从指定的存储库获取源代码。然后，这些脚本构建应用程序并将配置设置应用于测试代码。（这些测试脚本与源代码一起存储在存储库中。）一旦构建的代码通过测试，脚本就会将构建的应用程序部署到指定的运行时环境。CI/CD 工具与构建、发布、运行原则结合使用，允许持续快速、准确且可观察地部署应用程序。

### 因素 6：进程
**含义：**将应用程序作为一个或多个无状态进程执行。持久性数据应存储在有状态后端服务中。这使得扩展更容易，并防止意外的副作用。
**如何应用：**无状态代码是基于 Web 的应用程序的基本原则。进程唯一应该做的是执行处理逻辑。应避免进程之间的副作用；进程不应影响应用程序的整体状态或应用程序中另一个进程的状态。要确定进程的状态，请检查独立的真相来源，该来源协调所有进程之间的活动。

### 因素 7：端口绑定
**含义：**使用端口绑定导出服务，使其自包含并可通过指定的端口访问。
**如何应用：**某些端口号已成为特定服务的象征。例如，非安全 Web 应用程序的默认端口是 80 端口。安全网站通过 443 端口上的 HTTPS 访问。Kafka 消息服务侦听 9092 端口上的客户端流量。MySQL 数据库的默认端口是 3306。一些公司会不遗余力地将产品的品牌标识与端口号关联起来。[Docker](https://www.docker.com/?utm_content=inline+mention) 和 [Kubernetes](https://thenewstack.io/kubernetes/) 使用端口声明来定义域内服务的访问点。在开发级别，程序员通常根据 localhost URL 在其机器上使用资源或服务，然后通过关联的端口号绑定到给定的资源或服务。

### 因素 8：并发
**含义：**扩展应用程序时，应通过添加更多进程来水平扩展，而不是垂直扩展单个进程。
**如何应用：**对按需水平扩展的支持已成为现代 Web 规模企业应用程序的关键功能。许多技术，包括 AWS Elastic Container Service (ECS)、Docker Swarm、Google Cloud Run、Heroku、[HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) Nomad 和 Kubernetes，都支持自动扩展。理解并发原则的关键在于，应用程序必须由离散的、独立的执行逻辑单元组成，这些单元可以冗余地和同时运行。运行的单元数量可以根据当前的流量需求进行扩展或缩减。

### 因素 9：可丢弃性
**含义：**确保快速启动和关闭时间，以最大限度地提高弹性和使系统更强大。
**如何应用：**十二要素原则的可丢弃性原则体现了现代分布式应用程序的短暂性。正如并发原则所指出的那样，应用程序将以冗余的方式启动资源以满足当时的需要。因此，组件总是“来来去去”以满足流量需求。
当资源终止时，必须快速且优雅地进行。这意味着确保没有操作以无定形状态终止。必须完成操作，必须关闭与外部资源的连接，并且必须安全地从内存中删除资源。组件终止后，应用程序的整体状态应保持一致。

### 因素 10：开发/生产环境一致性
**含义：**保持开发、登台和生产环境尽可能相似，以促进持续部署并减少开发和生产之间的差距。

**如何应用：**开发/生产环境一致性原则类似于构建、发布、运行原则，它将应用程序开发过程分解为离散的片段。但是，构建、发布、运行关注的是代码发布，而开发/生产环境一致性则关注跨升级开发环境的代码一致性。

通常，在软件开发的不同阶段执行不同的操作。在开发阶段，开发人员提交代码。该代码会进行代码分析和单元（可能还有性能）测试。如果一切顺利，它将被移至登台环境。在登台阶段，代码将接受更广泛的测试制度，其中可能包括集成测试和渗透测试以查找安全风险。如果应用程序将由人类使用，则登台环境也是代码进行可用性测试以确保满足人类需求的地方。最后，成功后，代码将在生产阶段发布。

关于开发/生产环境一致性的重要一点是，每个环境（开发、登台和生产）必须相同，并且在每个环境中执行自动化工作时必须使用相同的工具。此外，除非是紧急更新，否则升级过程必须是单向的：代码必须从开发环境移动到登台环境，再到生产环境。不能来回移动。并且，在紧急情况下，例如修补程序，当代码绕过开发环境并直接从开发人员的机器移动到登台环境时，一旦修补程序代码发布到生产环境，则必须更新开发环境以适应登台环境中的更改。

在一个运行良好的 IT 部门中，开发人员的习惯是在本地机器上开始编码会话之前，每天检查开发环境的更新。这确保了任何紧急“向后”更新（在修补程序的情况下，从登台环境到开发环境）都会返回到开发人员的机器。

开发/生产环境一致性的关键因素是每个环境中基础设施的统一性以及环境之间升级过程的可预测控制。

### 因素 11：日志
**含义：**将日志视为事件流，并让执行环境聚合它们。这简化了日志管理和调试。

**如何应用：**日志记录应通过将日志记录事件视为独立于任何特定技术的独立数据流来完成。通常的实现是将日志事件视为一条消息，该消息由数据流技术（例如 Kafka）使用。将日志发射与日志存储分离使应用程序的可移植性更容易。

将日志记录到数据流中会将存储和数据管理的责任放在流管理技术上。权衡是关于发出日志数据的机器和应用程序的信息变得不透明。因此，为了提高效率，使用标准化的消息格式至关重要。消息格式应包含有关事件、机器、应用程序以及与应用程序操作相关的任何其他环境信息。

将日志记录到事件流中有很多好处，但是您必须进行额外的规划以确保日志呈现准确、全面且有用的信息。

此因素有一个开放的提案，以扩展它以反映当前的可观察性实践，包括遥测（[issue #3](https://github.com/twelve-factor/twelve-factor/issues/3)）。

### 因素 12：管理流程
**含义：**将管理任务作为一次性流程运行，在与应用程序相同的代码库和版本控制系统中进行管理。这确保了一致性和易于执行。

**如何应用：**应用程序必须附带其自身的管理功能，例如仪表板。例如，Substack（一个面向作家、记者和其他内容创建者的在线出版平台）附带一个仪表板功能，允许内容创建者控制出版操作和读者访问。该平台还使内容创建者能够为付费访问细分某些内容，并配置资金的收取方式。
此管理功能是Substack的一部分。它不是一个单独的应用程序，其源代码也没有托管在单独的存储库中。通用应用程序和管理流程都是统一代码库的一部分。Substack是管理流程原则的一个例子。重要的是要理解，管理功能是作为应用程序的一部分进行管理的，而不是作为与应用程序分离的东西。

## 通过开源迈向更高水平
您可能会从每个因素的描述中注意到的一件事是，十二要素方法对用于支持其原则的技术是不可知的。

当十二要素应用在2011年推出时，这种方法论在技术领域是新思维。该原则的不可知性使得采用更容易，特别是对于像Heroku这样的公司，它提供[一个平台](https://blog.heroku.com/next-generation-heroku-platform)可以支持各种各样的工具和技术。然而，在接下来的几年里，各种各样的云提供商都采用了十二要素方法，并且通过使这种方法开源，Heroku正在鼓励社区帮助对其进行现代化改造。

正如Heroku首席营销官在一次采访中解释的那样：

>*“当Adam Wiggins在14年前编写它时，云计算仍然很新，Docker和Kubernetes还不存在。他正在为优秀的SaaS应该是什么样子制定路线。从那时起，许多事情都发生了变化，修订是必要的。但是，这不应该仅仅是Heroku的观点。许多云提供商和最终用户组织都采用了十二要素原则。每一个都带来了在云中大规模运行这些类型的应用程序和基础设施的不同经验。他们的想法和贡献需要被纳入，以将十二要素提升到一个新的水平。”*

正如Junod所指出的，推动十二要素的原则在当时是有意义的，但技术环境已经发生了巨大的变化。它必须现代化，以解决遥测、身份验证和服务到服务（S2S）通信等问题，现代开发人员和架构师每天都在处理这些问题，但它们不是原始方法论的一部分。

为了鼓励广泛参与十二要素的现代化，11月，[Heroku将其项目开源](https://www.youtube.com/watch?v=JG1nGgirkB4)，采用CC-BY-4.0许可证。该公司已将其十二要素的源代码从其[原始网站](https://github.com/heroku/12factor)迁移到一个新的开源[存储库](https://github.com/twelve-factor/twelve-factor)。

新的存储库为对十二要素的贡献提供了一个中心活动点。它包含更新版本的网站代码和文档，其中包含对这些因素更深入的描述。该存储库还包含来自各个组织的新思想和附加文档的链接，包括[O’Reilly](https://www.oreilly.com/library/view/beyond-the-twelve-factor/9781492042631/)、[Nginx](https://slidrio-decks.global.ssl.fastly.net/1020/original.pdf)和[IBM](https://www.ibm.com/blog/7-missing-factors-from-12-factor-applications/)。这些公司秉承了十二要素的精神，他们的观点对于使其在今天更实用非常宝贵。

开源的两个最重要的优点是透明度和促进基于社区的技术创新的机制。Heroku首席架构师兼十二要素存储库维护者在十二要素Discord服务器上的[最近讨论](https://discord.com/channels/@me/1315041275292155944/1315089927251300493)中表示，除了拓宽十二要素的范围外，这种创新有望激发基于该方法论创建应用程序的工具。

诀窍是使基于十二要素的应用程序开发成为一种全面统一的体验。开源该项目和推动十二要素的思想是朝着构建弹性、可扩展和可维护的、在网络规模上运行的应用程序迈出的重要一步。

## 参与其中
十二要素软件开发方法已经激发了十多年来的软件开发和架构。其原则定义了一种统一、可预测的方式，使企业系统更安全地部署和更容易维护。

但是，鉴于过去十年发生的巨大技术变革，十二要素需要不断发展以适应时代。希望通过将十二要素作为一个开源项目，更广泛的贡献者将带来各种各样的观点，这将有助于使十二要素在今天像2011年首次发布时一样有用。

了解您可以如何通过查看项目的存储库的[贡献页面](https://github.com/twelve-factor/twelve-factor/blob/next/CONTRIBUTING.md)来参与。
[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展日新月异，不要错过任何一期。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。