# 生产中的 Backstage：平台团队需考虑的要点

从零开始构建一个生产级别 Backstage开发者门户网站的指导意见。

翻译自 [Backstage in Production: Considerations for Platform Teams](https://thenewstack.io/backstage-in-production-considerations-for-platform-teams/) 。

![](https://cdn.thenewstack.io/media/2023/09/4a290222-backstage-1024x534.jpg)
*图片来自 Shutterstock 的 Skreidzeleu*

开发者门户网站是大多数平台的一个突出方面，因为它是您与用户之间特权的互动点。开发者门户网站通过一个集中的UI反映了平台的功能，这意味着它们必须定制化以适应您的开发者和您想要提供的功能。

这就是 Backstage 的闪光点：可定制化。您可以用 Backstage 创建您梦想中的开发者门户网站，这可能包括用您组织的设计系统替换 UI 或引入您自己的数据消费机制。这是可能的，因为 Backstage 不是一个[现成的开发者门户](https://roadie.io/backstage-spotify/)网站，而是一个提供构建该网站的构建块的框架。

然而，开发者门户网站都是 web 应用程序。因此，当您从零开始采用和扩展 Backstage 时，您将承担它的全栈后果。因此，[Gartner](https://www.gartner.com/en/documents/4010078) 和其他机构报告说，自己设置和维护 Backstage 可能具有挑战性，但对许多公司来说，这样做的价值是巨大的。

也就是说，采用 Backstage 没有一刀切的方式。当您着手自己搭建 Backstage 时，您将遇到一些采纳这个框架时没人告诉您的常见任务。在本文中，我将带您了解在规划团队工作时需考虑的一些要点。

## 初始设置和部署

Backstage 通过其[命令行界面(CLI)](https://backstage.io/docs/local-dev/cli-overview/)提供了 `create-app` 命令来帮助您开始使用新实例。结果将在您的机器上运行良好，但从这一点上，您仍有一些工作要做，以使其成为生产就绪的开发者门户网站。

我对 Backstage 概念验证的建议是首先实现一个有意义的集成，如 GitHub。这将让您经历从 React 和 Node 配置到部署的所有接触点。

您的开发者门户网站很可能需要通过集成从各种源连接数据。因此，您需要实施一个 secret 管理策略，该策略允许您将 secrets 注入到将运行 Backstage 的容器中。

在部署方面，Backstage 团队建议使用您通常会为类似应用程序使用的部署方式。因此，您可以从将标准 CI/CD 实践应用于您的开发者门户网站中受益。

就 Roadie 管理的 Backstage 实例而言，所有这些考虑因素都内置于产品中，因此您不必投入时间在其中任何一个上。

## 身份验证和安全性

您的开发者门户网站是一个集成 GitHub、Argo CD 或 PagerDuty 等第三方服务的一站式商店。开发者门户网站将允许用户通过其[自助服务或黄金路径](https://thenewstack.io/new-to-platform-engineering-try-a-thin-self-service-layer/)功能请求基础设施。因此，确保 Backstage 实例的[安全性](https://thenewstack.io/secure-your-software-supply-chain-through-backstage/)非常重要。

首先，您需要安装和设置一个身份验证机制。值得庆幸的是，Backstage 提供了从 Okta 到 Google IAP 的 [13 个 provider](https://backstage.io/docs/auth/) 的开源集成。

接下来，您需要使用 Backstage 自带的权限框架。默认情况下，Backstage 的后端路由不受身份验证保护，因为开发者门户网站有开放性的假设。

另外，我建议您设置 scaffolder 在短暂的环境中执行任务。Roadie 一开始就这样做防止了[去年 Backstage 远程代码执行漏洞](https://roadie.io/blog/roadie-customers-are-not-affected-by-backstages-rce-vulnerability/)影响到任何客户。

请务必关注 Backstage 团队发布的安全补丁，并且经常升级您的实例。

## 升级和维护

Backstage 团队每个月从许多贡献者那里合并大约 300 个拉取请求，每两周发布次要版本。这个过程为框架提供了令人印象深刻的功能和错误修复流。

我建议定期将升级添加到您的计划中。Backstage 的升级过程目前涉及一些手动步骤，每个版本的复杂程度各不相同。

要注意的是，一些改进作为您需要挂钩到开发者门户网站的额外 API 或一组可以改进实例的新的 UI 组件。

最重要的是，跟上新功能是很有用的，因为有时即使在升级 Backstage 之后，您也必须选择加入它们。我撰写了 [Backstage 每周通讯](https://roadie.io/backstage-weekly/)，所以您不必自己查看代码库。欢迎订阅。

## 使用插件

Backstage 生态系统中有 100 多个可用插件，并鼓励您构建自己的插件将您独特的开发需求集成到 Backstage 中。

插件通常在后端、前端和通用三个包中实现。插件也可以提供扩展点，以便根据不同情况进行自定义或适配。

Backstage 社区正致力于[简化安装和升级插件的过程](https://github.com/backstage/backstage/issues/18390)，但目前它仍然需要一些手动工作，并且需要您重新部署实例。

在编写插件时，请注意 Backstage 正在整合一个具有简化 API 的[新后端系统](https://backstage.io/docs/plugins/new-backend-system/)，所以值得一看。

## Backstage 实例只是第一步

或者也许是第二步？您首先需要确定开发者门户网站要解决什么问题。然后，一旦您建立了一个实例，您将进入一个更长期的旅程，在学习开发者的同时，继续添加更多用例并对开发者门户网站进行迭代。

如果您想采用 Backstage 但不想拥有其实现或维护，[Roadie.io](http://roadie.io/) 提供托管和管理的 Backstage 实例。 Roadie 提供无代码 Backstage 体验和更精致的功能，同时与开源软件框架完全兼容。 此外，Roadie 提供完整的记分卡来测量组织内的软件质量和成熟度。

如果您有兴趣了解托管生产级 Backstage 实例与自托管实例的优势和权衡，请[查看我们的白皮书](https://roadie.io/whitepapers/managed-vs-self-hosted-backstage/)。
