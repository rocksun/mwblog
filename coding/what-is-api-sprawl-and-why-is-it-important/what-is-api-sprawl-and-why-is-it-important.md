<!--
title: API蔓延：重要性及应对之策
cover: https://cdn.thenewstack.io/media/2024/02/70c37e43-puzzle-1024x576.jpg
-->

未经控制的API增长可能会导致严重后果，进而加剧不安全的编码实践。

> 译自 [What Is API Sprawl and Why Is It Important?](https://thenewstack.io/what-is-api-sprawl-and-why-is-it-important/)，作者 Bill Doerrfeld 是一位技术记者和 API 思想领袖。他是 Nordic APIs 博客的主编，这是一个致力于使世界更具可编程性的全球 API 社区。

API 在我们的日常生活中扮演着核心的角色，但随着 API 的快速增长，蔓延问题开始浮现。

越来越多的微服务被开发出来，以实现 Gartner 所称的[可组合企业](https://www.gartner.com/smarterwithgartner/gartner-keynote-the-future-of-business-is-composable)。例如，Rapid 在其 [2022 年的 API 状况报告](https://stateofapis.com/)中发现，拥有 10,000 名或更多员工的大公司往往拥有超过 250 个内部 API。API 对于新的 SaaS 产品和合作伙伴生态系统也至关重要。然而，并非所有这些集成接触点都受到精心管理。

最近，OWASP 的基础性 API [安全风险前十名](https://curity.io/resources/learn/owasp-top-ten/)列表中新增了两个新风险，即不当的库存管理和不安全的 API 使用。对我而言，这反映了在维护组织 API 足迹的准确概览方面面临的越来越大的挑战，以及在盲目集成第三方 API 中日益增加的风险。而且，如果不得当地管理，生成 AI 相关工具和 API 的突然增长可能会[加剧现有的技术债务](https://devops.com/will-the-rise-of-generative-ai-increase-technical-debt/)。

解决 API 蔓延问题至关重要，因为缺乏一致性可能会减缓开发时间表。此外，如果没有治理和对其生命周期的可见性，[API 就更容易存在访问控制风险](https://thenewstack.io/with-auth0-purchase-okta-will-boost-access-apis-for-developers/)，或者变成僵尸端点。让我们探讨一下 API 蔓延是什么，以及为什么解决它很重要。我还将为技术领导者提供一些建议，指导他们如何在开发文化中避免这种情况。

## 定义 API 蔓延

[EON 咨询](https://eonconsulting.net/blog/ydjge72222w4eun6c37sxx9mdpqe4i-fkf79-tkwx9)将技术蔓延描述为 "组织内各种技术（无论是软件、硬件还是云服务）的不受控制的扩展。" 在一定程度上，由于对数字技术的日益依赖，技术债务是不可避免的。但是，当增长真正开始失控时，您会开始遇到不利影响。这就是蔓延。

就 API 而言，我将蔓延视为对 API 优先策略的盲目采用，而没有适当地采用行业标准，或者没有对这些接口在长期支持方面有所考虑。许多大型组织正在处理一个不断膨胀的 API 组合，由各种开发协议和设计风格组成。他们可能还在处理不同版本和不同的发布和弃用时间表。这可能会产生一个杂乱无章的集成网络，往往容易出现故障。

导致蔓延的主要原因只是正在开发的 API 数量庞大——F5 估计今天已经存在近 [2 亿个 API](https://www.f5.com/pdf/reports/f5-office-of-the-cto-report-continuous-api-sprawl.pdf)。另一个因素是，并非所有的 API 都有文档记录。事实上，根据[企业管理协会](https://www.scmagazine.com/news/it-organizations-document-apis) 2023 年的报告，只有 10% 的组织完全记录了他们的 API。这意味着随着开发人员的流失，部落知识往往会随之流失。

## API 蔓延的负面影响

不适当地监管您的 API 库存可能会给您带来麻烦。例如，它可能会降低可发现性并阻碍技术的可重用性。缺乏文档和设计前瞻性可能会限制可用性。缺乏治理可能会导致更严重的安全后果，例如被遗忘的、未维护的端点。

### 降低开发者体验

API 之间的不一致可能会阻碍开发者在集成方面的体验。例如，现代 API 开发中使用了许多不同的设计范式，包括 SOAP、REST、gRPC 等以及更多的异步格式，如 Webhooks 或 Kafka 流。一个组织可能同时采用各种风格。

使用[各种 API 风格](https://nordicapis.com/top-architectural-styles-for-apis-in-2023/)为手头的任务提供了最佳选择。尽管如此，风格不一致可能会使得单个开发者在没有指导的情况下难以导航分散的组件。如果您正在将 API 外部化给合作伙伴或将其作为公共服务产品化，那么缺乏[文档尤其糟糕](https://thenewstack.io/bad-documentation-bad-documentation/)。[优质的开发者体验](https://nordicapis.com/what-is-developer-experience/)不仅是技术市场上的竞争优势，而且正在迅速成为一种期望。

### 安全漏洞

正如网络安全专家经常说的那样，您无法保护您不了解的东西。在技术蔓延中，您可能不会意识到每天开发和使用的数以百计，甚至数以千计的 API。没有库存管理，API 可能会被忽视并陷入混乱之中。

API 蔓延也可能导致不安全的编码实践。Escape 公司的安全研究人员最近在对网络进行扫描后发现了 [18,000 个高风险的与 API 相关的机密信息和令牌](https://escape.tech/blog/how-we-discovered-over-18-000-api-secret-tokens/)。将这些凭据暴露出去的风险在于它们可能被用于对企业系统的定向攻击，这可能导致数据泄露，降低消费者信心并产生高昂的罚款。

### 生命周期管理不佳

生命周期管理在蔓延情况下也可能受到影响。如果 API 版本控制和下线计划没有得到有效的传达，就很容易导致客户端的破坏性更改。当多个 API 互相依赖时，这可能会产生连锁反应，导致生态系统的破碎化。

总的来说，API 蔓延可能会导致更加混乱的开发文化。而且，这不仅仅是 IT 的问题。API 蔓延也可能伤害业务。例如，匆忙获取的暗影 API 可能不符合更广泛的 IT 战略。在低效设计或重复性工作中可能存在隐藏成本。破碎的客户端可能意味着丧失了最终用户功能，导致收入下降。

## 管理 API 蔓延的思路

API 蔓延可能会导致许多潜在的不利后果。那么，我们该如何避免这种混乱呢？以下是一些技术，开发人员、架构师和首席技术官可以在其中达成一致，使他们的 API 战略更安全、更精简、更易用：

- **保持文档更新**。强调 API 文档的重要性。所有内部开发的 API 应该被充分记录。理想情况下，这些文档包括易于理解的描述和示例代码，以帮助他人理解其内部工作原理。
- **维护所有 API 的清单**。除了单独记录每个 API 外，审查您的表面区域并创建一个包含您的组织已构建或从第三方使用的所有 API 的目录。这些信息可以添加到现有的[内部开发者平台](https://nordicapis.com/the-role-of-apis-in-platform-engineering/) (IDP) 中，例如。
- **围绕 OpenAPI 规范进行整合**。[OpenAPI 规范](https://www.openapis.org/)（原 Swagger）已成为描述 Web API 的事实行业标准规范。采用基于规范的 API 开发可以解决上述许多问题。
- **制定内部 API 设计风格指南**。就像编辑团队有书面文稿的风格指南一样，软件开发也会受益于一个概述内部 API 约定的风格指南。为内部开发标准设定保护栏可以消除 [API 设计](https://thenewstack.io/what-are-the-core-principles-of-good-api-design/)的猜测工作，并使消费 API 的过程更加容易。查看 [API Stylebook](https://apistylebook.com/) 获取一些具体示例。
- **遵循安全最佳实践**。从第一天开始为所有 API 开发加入适当的[安全控制](https://thenewstack.io/5-software-security-goals-all-ctos-should-prioritize/)。这包括使用 API 网关、采用 OAuth 和 OpenID Connect、应用多因素身份验证以及遵循安全的令牌处理实践等 API 安全最佳实践。采用零信任模型并在分配 API 访问范围时遵循最小特权原则也是一个好主意。
- **尽可能自动化治理**。设计审查很繁琐，IT 治理不应该妨碍创新。自动化测试可以被采用来将这个过程向左移动，实现最好的两个世界。例如，API 管理供应商已经为评估 API 规范的设计和安全性创建了许多免费工具，如 [RateMyOpenAPI](https://ratemyopenapi.com/)、[API Insights](https://apiinsights.io/) 和 [OpenAPI.security](https://openapi.security/)。 [Spectral](https://github.com/stoplightio/spectral) 还是一个独特的开源工具，可以根据自定义规则对 OpenAPI 定义文件进行 lint。
- **考虑其他机器可读的规范**。OpenAPI 对于文档和 SDK 生成等方面很有帮助。但是，它省略了一些有价值的业务数据。[APIs.json](https://apisjson.org/) 是一个有趣的新兴标准，可以帮助改善 API 操作和元数据的可发现性。

## 采取长期的 API 平台视角

API 的采用正在显著增长，许多公司希望参与蓬勃发展的 API 生态系统。毫无疑问，[持续的人工智能浪潮](https://nordicapis.com/how-ai-is-transforming-the-future-of-apis/)将为市场带来新的 API，为所有工程师带来一些令人兴奋的可能性。与此同时，API 不再是业余项目。它们值得认真对待。

未加控制的 API 蔓延可能会带来负面后果，可能会加剧不安全的编码实践。因此，对 API 蔓延做出响应将至关重要，方法是保持对所有服务的清单，并建立更多的以文档为驱动的文化。API-first 的理念不会很快消失，因此应该为长期制定内部标准——希望在事态失控之前能够做到这一点。

另外值得一提的是，新的[平台工程倡议](https://devops.com/strategies-to-consider-when-adopting-platform-engineering/)将如何考虑 API 的作用将是一个有趣的观察点。有一段时间以来，开发人员被期望不仅负责编程，还负责软件的部署和维护。在技术蔓延之后，行业似乎正在向稍微更加集中化的控制方向转变。这为恢复标准并为常见的开发人员工作流程设立“铺好的道路”，包括 API 设计和管理，提供了一个机会。
