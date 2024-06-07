
<!--
title: 利用身份管理来提高收入
cover: ./cover.png
-->

初创公司 Userfront 解决了 SaaS 公司在发展过程中客户账户扩展的复杂性。

> 译自 [Banking on Identity Management to Boost Revenue](https://thenewstack.io/banking-on-identity-management-to-boost-revenue/)，作者 Susan Hall。

根据身份验证和身份管理初创公司 [Userfront](https://userfront.com/) 的首席执行官 [Tyler Warnock](https://www.linkedin.com/in/tylerwarnock/) 的说法，软件即服务 (SaaS) 公司通常从一系列相当小的帐户开始，这些帐户需要低摩擦登录功能，但随着他们的发展，当他们现有的身份管理解决方案不再满足他们的需求时，他们往往会感到停滞。

Userfront 提供了一个单一平台，可以从个人或免费增值帐户发展到定制的企业级别，帮助组织抓住可能错失的创收机会。

“我们内部已经讨论了很多关于过渡点的问题，因为我们正在与 SaaS 业务打交道，他们通常会在公司内部经历一些模式，”Warnock 说。“几年后，他们会遇到障碍……因为他们选择了一个无法扩展以满足他们需求的基本登录。因此，当他们这样做时，他们基本上有两个糟糕的选择：他们可以尝试扩展他们拥有的东西，而这些东西并不是为了做他们正在尝试做的事情而设计的，或者他们可以尝试迁移。而迁移过程尤其充满了许多不确定性。人们真的不知道如何去做；可能需要九个月到一年。”

这家总部位于加利福尼亚州圣何塞的公司特别专注于帮助 SasS 公司赢得客户，从而通过改进的身份管理来增加收入。它为客户提供了一条途径，可以逐步添加新功能，将客户升级到更高的帐户级别，并消除需要更高级别的安全性和合规性功能的大公司的流失。

## 消除复杂性

在 TNS，Mary Branscombe 解释了 [身份验证](https://thenewstack.io/how-do-authentication-and-authorization-differ/)（验证用户是否为他们声称的身份）和授权（确定该人在系统内部被允许做什么）之间的 [区别](https://thenewstack.io/how-do-authentication-and-authorization-differ/)。这两个原则是 [零信任安全](https://thenewstack.io/what-do-authentication-and-authorization-mean-in-zero-trust/) 的基础。

虽然 Auth0、OpenID Connect 和各种 [开源项目](https://thenewstack.io/kubernetes-authentication-solved-spiffe-spire-move-to-cncf-incubation/) 等解决方案一直在努力让开发人员更容易进行身份管理，但像 [Oso](https://thenewstack.io/oso-tackles-unbundling-security-authorization/) 和 [Stytch](https://thenewstack.io/stytchs-api-first-approach-to-passwordless-authentication/) 这样的初创公司也在关注此问题。

Userfront 诞生于与斯坦福大学相关的初创加速器 StartX。其团队在 2020 年花了三个月的时间与 150 名开发人员交谈，了解他们对身份管理的喜好和厌恶。他们发现开发人员不喜欢的一点是：复杂性。

因此，Userfront 建立在三个核心原则之上：

- 它应该具有所有主要功能
- 它应该默认安全
- 它应该易于使用，无需深入的领域知识

“目前大多数产品实际上都是关于一种新型小部件。我们希望更多地将其视为‘好的，小部件就像赌注一样。你如何真正将其转化为有用的东西？’”Warnock 说。“我们专门针对面向客户的软件进行了构建。因为扩展 SaaS 和达到增长指标真的很难，对吧？这可能是竞争最激烈的时刻。你必须真正了解你的客户关心什么。因此，Userfront 的成立是为了让软件公司在更好地服务于客户方面获得优势。

“除了所有基础知识——密码、无密码、使用 Google 登录、你知道的，MFA（多因素身份验证）、全功能身份验证、基于角色的访问控制、多租户……一旦你有了我们所做的基础，你就会关心两种极端情况，”他说。一种是快速入门，另一种是简化迁移。

[Heavybit](https://www.heavybit.com/press/heavybit-welcomes-new-member-userfront) 的普通合伙人 [Joseph Ruscio](https://www.linkedin.com/in/josephruscio/) 解释说：“从历史上看，你在这里有两个选择，要么为每种类型的客户构建一个内部解决方案，要么购买和管理跨多个产品的身份分割。Userfront 不仅通过采用现代前端框架，而且通过认识到现代 B2B 软件产品具有不同类别的最终用户，并使你能够在一个产品中满足所有客户的需求，从而将自己与该领域区分开来。你可以选择适合你的最终客户的服务，并为企业构建一套功能，这些功能可以针对 SMB 进行简化。”

Heavybit 领投了 Userfront 最近的 530 万美元种子基金轮。

他补充说，Userfront 是为基于组件的世界构建的：“第一代云原生 IAM 产品是为 15 年前主导应用程序开发的服务器端、全栈 Web 框架的世界构建和设计的，当时身份管理主要通过 API 在后端进行。随着应用程序开发转向复杂的前端框架，身份逻辑也随之转向，而使用粗粒度 API 在前端应用程序中拼接所有这些工作流变得越来越困难。”

## 从一行代码开始

沃诺克解释说，该系统建立在三层之上，并且只需一行 JavaScript 即可开始使用。

首先，有提供通过 JSON Web 令牌 (JWT) 访问的 API 层。它满足安全和合规性要求，包括 SOC 2、GDPR 和数据驻留。然后是 SDK 层。它的 [JavaScript SDK](https://userfront.com/docs/js) 是您可以添加到应用程序中的本机代码，该代码调用 Userfront API。最重要的是该公司称之为工具包层，它包括注册、登录和密码重置表单等内容——使用 SDK 调用 API 的用户界面组件。

![](https://cdn.thenewstack.io/media/2024/05/ea270e53-userfront-diagram.jpg)

“例如，我们可以为您提供一行代码，它会自动扩展为功能齐全的登录流程，”沃诺克说。“因此，您可以将其添加到您的网站，一行代码会带来您想要的样式。有了它，无论您配置了什么，它都会自动工作。因此，如果您说，‘我想通过链接选项使用 Google SSO 登录电子邮件。然后我想使用短信验证码作为第二个因素，’它们已经连接好以完成所有这些事情。您只需要在那里放置一行代码即可。”

它还提供 [Sidecar](https://www.npmjs.com/package/@userfront/sidecar-cli)，这是一种工具，可以使用户帐户迁移透明且安全，而无需重置密码。Sidecar 是后端的 TypeScript 抽象层，它模仿其他身份验证系统，以便通过最小的代码更改和不影响最终用户轻松迁移。
