# OAuth 2.0：名义上的标准？

![OAuth 2.0：名义上的标准？特色图片](https://cdn.thenewstack.io/media/2024/12/04250612-1587430004271.jpeg)

[Belinda Fewings](https://unsplash.com/@bel2000a?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)  发表于 [Unsplash](https://unsplash.com/photos/brown-and-grey-padlock--RdoPEdnfnw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

作为一家集成平台公司的CTO，我花费了无数时间分析数百个SaaS应用程序中的[OAuth 2.0](https://thenewstack.io/master-difficult-user-authentication-requirements-with-oauth/)实现。虽然OAuth 2.0经常被吹捧为标准，但现实情况远比这复杂和支离破碎。

OAuth 2.0于2012年出现，作为OAuth 1.0的继任者，旨在[简化](https://thenewstack.io/the-cedar-programming-language-authorization-simplified/)网络和移动应用程序的授权流程。其目标是崇高的：

- 强制使用SSL以增强安全性
- 简化OAuth 1.0中所需的复杂签名过程
- 更好地支持快速普及的移动设备

理论上，OAuth 2.0将为应用程序提供一种统一的方式来请求对其他系统上用户帐户的有限访问权限，而无需共享密码。这将使集成更安全，并[更易于用户和开发人员管理](https://thenewstack.io/zeroops-helps-developers-manage-operational-complexity/)。

**支离破碎的景象**

然而，OAuth 2.0实现的现实情况远非标准化。OAuth 1.0规范的作者Eran Hammer，他在OAuth 2.0发布期间[著名的辞职](https://www.wired.com/2012/07/developer-quits-oauth-2-0-spec-calls-it-a-bad-protocol/)，被引用说——“几乎任何东西都可以很容易地被称为符合OAuth 2.0标准”。

以下是一些关键问题：

**过度灵活：**OAuth 2.0规范包含许多可选组件和流程。虽然出发点很好，但这导致了实现方式的巨大差异。**复杂性：**OAuth 2.0核心规范长达81页，但要完全理解它，需要阅读20多个附加RFC中的数千页内容。这种复杂性使得[开发人员难以](https://thenewstack.io/how-ddev-can-help-solve-local-web-development-challenges/)正确且一致地实现。**实现不一致：**主要平台经常偏离核心规范或以独特的方式实现特定的RFC。例如：

- Microsoft Azure需要用于令牌刷新的重定向URI，这不是标准规范的一部分。
- Wix有自己的“OAuth 2解决方案”，具有非标准的“基本”和“高级”流程。要刷新高级选项，必须发送client_id和secret、访问令牌和刷新令牌，这很不寻常。

**安全问题：**某些OAuth 2.0流程，例如资源所有者密码凭据授权，本质上是不安全的，但规范仍然允许。

**案例研究：签名的回归**

具有讽刺意味的是，从OAuth 1.0迁移到2.0的主要原因之一是消除对复杂签名的需求。然而，安全问题导致引入了代码交换证明密钥（PKCE），在RFC 7636中指定。PKCE重新引入了一种类似签名的机制来防止特定攻击，尤其是在移动环境中。这一发展突显了OAuth 2.0生态系统如何不得不发展以解决安全漏洞，有时是通过重新引入它最初试图消除的概念。

一个很好的例子是Pleo，一家位于欧洲的费用管理公司。RFC 7636于2015年发布，Pleo是我见到的第一家使用它的公司。他们针对此用例的API是在2022年创建的。他们对OAuth 2.0的其余遵守情况非常好。他们遵循所有“建议”，因为他们已经实现了PKCE。他们可能符合OAuth 2.1标准，但稍后再详细介绍。

**什么构成了一个好的标准？**

一个好的标准在特异性、灵活性和简单性之间取得微妙的平衡。特异性至关重要，它通过诸如“必须”和“必需”之类的词语提供精确的要求。然而，灵活性同样重要，以确保在各种实现中得到广泛采用。关键在于找到适当的平衡点，避免过度选择性，这可能导致实现不一致。
简洁性是另一个关键因素——一个好的标准应该简洁易懂。例如，OAuth 1.0 的 81 页规范与 OAuth 2.0 散布在多个 RFC 中的数千页形成鲜明对比，突出了复杂性如何成为一个重大缺点。最终，一个有效的标准提供了精确的强制性要求，同时允许必要的灵活性，所有这些都在一个易于理解的框架内，不会因过多的文档而使实施者不知所措。

**前进的道路：OAuth 2.1 及其未来**

认识到这些挑战，OAuth 社区正在开发 OAuth 2.1。此修订旨在：

- 将最佳实践和多个 RFC 合并到单个综合文档中
- 要求所有客户端都使用 PKCE，从而全面增强安全性
- 删除有问题的授权
- 统一处理公共客户端和私有客户端
- 强制限制刷新令牌和安全重定向

虽然 OAuth 2.1 有望解决许多当前的痛点，但它也引发了关于向后兼容性和采用时间表的问题。

**对开发者和企业的影响**

对于开发者和[构建集成的企业](https://thenewstack.io/building-an-integrated-infrastructure-for-real-time-business/)，当前的 OAuth 2.0“标准”带来了一些挑战：

* **开发时间增加：**每个 OAuth 实现可能需要自定义代码，从而增加开发和维护成本。
* **安全风险：**如果不仔细管理，不一致的实现会导致安全漏洞。
* **用户体验影响：**OAuth 流程的变化可能会混淆最终用户，并可能影响集成服务的采用。
* **合规性问题：**对于受监管行业的企业而言，确保每个 OAuth 实现都符合安全和隐私标准可能很复杂。

**结论：OAuth 2.0 是否过于灵活而无法成为标准**

虽然 OAuth 2.0 提供了一个授权框架，但其当前状态远非一个合适的标准。过度的灵活性和碎片化导致了一个生态系统，其中“符合 OAuth 2.0”在实践中可能意味着截然不同的东西。

当我们展望 OAuth 2.1 和像 Grant Negotiation and Authorization Protocol (GNAP) 这样的潜在替代方案时，很明显，对真正标准化、安全且对开发者友好的授权协议的追求仍在继续。与此同时，开发者和企业必须保持警惕，仔细评估他们遇到的每个 OAuth 实现，并构建强大的系统来处理各种变化。

这节课的意义超越了 OAuth：在设计标准时，平衡灵活性和特异性至关重要。过多的灵活性会导致碎片化，而过多的僵化会阻碍采用。随着我们继续构建和连接数字系统，找到这种平衡将是创建真正有效标准的关键。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以串流收听我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)