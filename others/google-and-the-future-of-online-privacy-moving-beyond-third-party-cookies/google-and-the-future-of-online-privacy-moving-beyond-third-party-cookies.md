
<!--
title: 谷歌与在线隐私的未来：超越第三方Cookie
cover: https://cdn.thenewstack.io/media/2024/07/fab213e0-chocolate-2599637_1280.jpg
-->

无论您采取什么措施来为无 Cookie 的世界做准备，都要从小处着手，先进行测试。

> 译自 [Google and the Future of Online Privacy: Moving Beyond Third-Party Cookies](https://thenewstack.io/google-and-the-future-of-online-privacy-moving-beyond-third-party-cookies/)，作者 Gilad Shriki。


**更新**: 我很喜欢这篇文章的最终效果，也很高兴能够从不同的角度来探讨第三方 Cookie 即将消亡的问题。然而，命运却另有安排——在我写完这篇文章几天后，谷歌[撤回了其](https://apnews.com/article/google-privacy-chrome-cookies-browser-bffdd0ca0af9ba7a94e95c2c7a11e4d2)（暂时）停止使用第三方 Cookie 的决定。

*我当时一边咒骂自己的运气，一边想着其他时间线，脑海中浮现出漫威剧集“假如…？”。这部剧集讲述了如果佩吉·卡特成为美国队长，或者如果奇异博士变得邪恶，或者如果复仇者联盟遭到僵尸攻击，等等会发生什么。*

*现在，我谦卑地过渡到下一个话题，并向您展示：“假如……开发者不得不在一个没有 Cookie 的世界中航行？”*

在网络的早期，如果您更改了网站上的设置或将商品放入购物车，刷新页面就意味着从头开始。网站将每个访问者都视为陌生人。为了根据过去的会话创建[更个性化的在线体验](https://thenewstack.io/dynamic-data-capture-sets-the-stage-for-extreme-personalization/)，Netscape[创建了浏览器 Cookie](https://montulli.blogspot.com/2013/05/the-reasoning-behind-web-cookies.html)，它将用户的偏好和浏览历史记录保存在他们的设备上。其他浏览器很快便采用了这种有用的功能。

虽然 Netscape 引入的第一方 Cookie 旨在通过记住偏好和设置来改善用户体验，但广告商很快开始实施第三方 Cookie 来跟踪用户的互联网活动，并根据他们之前访问过的网站向他们投放广告。多年来，第一方 Cookie 一直用于身份验证和登录网站，而第三方 Cookie 一直被用于定向广告、跨网站跟踪用户、数据收集和其他类型的监控。

出于这些隐私原因，[谷歌](https://cloud.google.com/?utm_content=inline+mention)计划效仿 Mozilla 和 Apple，它们已经在[Firefox](https://venturebeat.com/business/firefox-enhanced-tracking-protection-blocks-third-party-cookies-by-default/)和[Safari](https://www.zdnet.com/article/apple-blocks-third-party-cookies-in-safari/)中分别阻止了第三方 Cookie，并计划在 2025 年[默认情况下在 Chrome 和基于 Chromium 的浏览器中弃用第三方 Cookie](https://developers.google.com/privacy-sandbox/3pcd)。谷歌已经默认情况下限制了[1% 的 Chrome 用户](https://developers.google.com/privacy-sandbox/3pcd/prepare/prepare-for-phaseout)使用第三方 Cookie。该公司此后[撤回了这些计划](https://www.axios.com/2024/07/22/google-chrome-keeps-cookie-policy)。

虽然第三方 Cookie 的终结有其好处，但最终的证明将取决于实际效果——与任何重大变化一样，第三方 Cookie 的终结引发了许多问题。无论您对第三方 Cookie 的终结有何看法，您都必须认真思考这一变化对您的应用程序和项目意味着什么。当第三方 Cookie 消失时，某些用例将不再可能实现，您需要找到解决方案。

## 平衡隐私和个性化

谷歌表示，隐私是其计划停止在 Chrome 中支持第三方 Cookie 的主要驱动力。如果没有第三方 Cookie，个性化的再营销将无法实现。

如果第三方 Cookie 的终结按预期进行，我期待着不再看到烦人的弹出窗口，不再被在线跟踪，不再被投放我不希望看到的广告。然而，鉴于谷歌和其他许多公司依赖第三方 Cookie 来赚取数十亿美元，第三方 Cookie 不会在没有替代品的情况下消失。

在逐步淘汰第三方 Cookie 的同时，谷歌也在同时投资[隐私沙盒](https://privacysandbox.com/)，该沙盒旨在为任何需要为其业务提供内容和广告的人提供保护隐私的替代方案。隐私沙盒 API 将允许 Chrome 和任何采用它们的浏览器代表其设备在本地采取行动，以保护用户在浏览时的身份信息。例如，[主题 API](https://developers.google.com/privacy-sandbox/relevance/topics) 允许基于兴趣的广告，而无需跟踪单个用户访问的网站。

随着隐私沙盒的不断普及，开发者在创建应用程序和网站时将有一套新的网络标准需要遵守。这些标准将确保隐私，同时保持一定程度的个性化。

## 为用户安全设定新标准

几十年来，cookie 向开发者允许了采用劣质安全实践进行用户验证和追踪。第三方 cookie 是可用的，并且他们可以存储用户身份验证信息和详细信息。然而，因为这些是第三方 cookie，任何人都不能控制谁能够使用或访问其中数据。

第三方 cookie 的潜在末日将带来安全改进，要求开发者们重新思考他们的以往方法，并采用新方式来安全地处理用户身份验证和身份信息。可以将第三方 cookie 消除当作一个强制功能，用于更加安全地存储那些信息，比如伴随 HTTPOnly 和安全 Cookie。

如果您依赖第三方 cookie，您将需要找到一种保护隐私的身份验证和识别方法。一个潜在的解决方案是 FedCM API，它被设计为让身份提供者在网络上提供身份联合服务，无需第三方 cookie 和重定向。FedCM API 能够进行联合身份验证，以进行诸如注册或登录之类的活动。

## 重新定义开发者体验第三方 

Cookie 即将走到尽头，这是修正多年来在你构建应用和网站时可能遵循的错误或不良做法的一个契机。它本应让你的应用和网站变得更加私密和安全，但这也是一次反思的机会，思考你究竟需要在多大程度上控制应用或网站的方方面面。

在进入无 Cookie 时代之际，你希望在跟进这些方面变化上花费多少时间？你可能希望将这方面的一些工作外包出去，这样一来你就不必成为 Cookie 领域的专家，而可以拥有一个专门的工具来跟踪每个变化和更新。

对你的应用程序和网站使用第三方 Cookie 的情况进行彻底审计，并为这些场景制定解决方案。对于你自行构建的每个使用第三方 Cookie 的流程，制定一个游戏计划，确定你将继续自行构建还是采用第三方提供商。

一种解决方案是减少第三方 Cookie 的使用，并在诸如身份验证等无法减少的领域采用会话 ID 等其他机制。我怀疑许多开发人员会从第三方 Cookie 转向第一方 Cookie，这可能会推动其他实现更改，例如使用自定义域或配置文件数据库。如果你已采用供应商来处理第三方 Cookie，请检查他们是否支持迁移到第一方 Cookie。
