# 谷歌与在线隐私的未来：超越第三方 Cookie

![Featued image for: Google and the Future of Online Privacy: Moving Beyond Third-Party Cookies](https://cdn.thenewstack.io/media/2024/07/fab213e0-chocolate-2599637_1280-1024x682.jpg)

**更新**: 我很喜欢这篇文章的最终效果，也很高兴能够从不同的角度来探讨第三方 Cookie 即将消亡的问题。然而，命运却另有安排——在我写完这篇文章几天后，谷歌[撤回了其决定](https://apnews.com/article/google-privacy-chrome-cookies-browser-bffdd0ca0af9ba7a94e95c2c7a11e4d2)（暂时）停止使用第三方 Cookie。

*我当时一边咒骂自己的运气，一边想着其他时间线，脑海中浮现出漫威剧集“假如…？”。这部剧集讲述了如果佩吉·卡特成为美国队长，或者如果奇异博士变得邪恶，或者如果复仇者联盟遭到僵尸攻击，等等会发生什么。*

*现在，我谦卑地过渡到下一个话题，并向您展示：“假如……开发者不得不在一个没有 Cookie 的世界中航行？”*

在网络的早期，如果您更改了网站上的设置或将商品放入购物车，刷新页面就意味着从头开始。网站将每个访问者都视为陌生人。为了根据过去的会话创建[更个性化的在线体验](https://thenewstack.io/dynamic-data-capture-sets-the-stage-for-extreme-personalization/)，Netscape[创建了浏览器 Cookie](https://montulli.blogspot.com/2013/05/the-reasoning-behind-web-cookies.html)，它将用户的偏好和浏览历史记录保存在他们的设备上。其他浏览器很快便采用了这种有用的功能。

虽然 Netscape 引入的第一方 Cookie 旨在通过记住偏好和设置来改善用户体验，但广告商很快开始实施第三方 Cookie 来跟踪用户的互联网活动，并根据他们之前访问过的网站向他们投放广告。多年来，第一方 Cookie 一直用于身份验证和登录网站，而第三方 Cookie 一直被用于定向广告、跨网站跟踪用户、数据收集和其他类型的监控。

出于这些隐私原因，[谷歌](https://cloud.google.com/?utm_content=inline+mention)计划效仿 Mozilla 和 Apple，它们已经在[Firefox](https://venturebeat.com/business/firefox-enhanced-tracking-protection-blocks-third-party-cookies-by-default/)和[Safari](https://www.zdnet.com/article/apple-blocks-third-party-cookies-in-safari/)中分别阻止了第三方 Cookie，并计划在 2025 年[默认情况下在 Chrome 和基于 Chromium 的浏览器中弃用第三方 Cookie](https://developers.google.com/privacy-sandbox/3pcd)。谷歌已经默认情况下限制了[1% 的 Chrome 用户](https://developers.google.com/privacy-sandbox/3pcd/prepare/prepare-for-phaseout)使用第三方 Cookie。该公司此后[撤回了这些计划](https://www.axios.com/2024/07/22/google-chrome-keeps-cookie-policy)。

虽然第三方 Cookie 的终结有其好处，但最终的证明将取决于实际效果——与任何重大变化一样，第三方 Cookie 的终结引发了许多问题。无论您对第三方 Cookie 的终结有何看法，您都必须认真思考这一变化对您的应用程序和项目意味着什么。当第三方 Cookie 消失时，某些用例将不再可能实现，您需要找到解决方案。

**平衡隐私和个性化**

谷歌表示，隐私是其计划停止在 Chrome 中支持第三方 Cookie 的主要驱动力。如果没有第三方 Cookie，个性化的再营销将无法实现。

如果第三方 Cookie 的终结按预期进行，我期待着不再看到烦人的弹出窗口，不再被在线跟踪，不再被投放我不希望看到的广告。然而，鉴于谷歌和其他许多公司依赖第三方 Cookie 来赚取数十亿美元，第三方 Cookie 不会在没有替代品的情况下消失。

在逐步淘汰第三方 Cookie 的同时，谷歌也在同时投资[隐私沙盒](https://privacysandbox.com/)，该沙盒旨在为任何需要为其业务提供内容和广告的人提供保护隐私的替代方案。隐私沙盒 API 将允许 Chrome 和任何采用它们的浏览器代表其设备在本地采取行动，以保护用户在浏览时的身份信息。例如，[主题 API](https://developers.google.com/privacy-sandbox/relevance/topics) 允许基于兴趣的广告，而无需跟踪单个用户访问的网站。

随着隐私沙盒的不断普及，开发者在创建应用程序和网站时将有一套新的网络标准需要遵守。这些标准将确保隐私，同时保持一定程度的个性化。

**为用户安全设定新标准**
For decades, Cookies have allowed developers to adopt suboptimal security practices for user authentication and tracking. Third-party Cookies were available, and they could store user authentication information and details. However, since these were third-party Cookies, no one could control who could use or access the data within them.

The potential end of third-party Cookies will bring security improvements, requiring developers to rethink their previous approaches and adopt new methods for securely handling user authentication and identification information. Consider the elimination of third-party Cookies as a forcing function to store this information more securely, such as using HTTPOnly and secure Cookies.

If you rely on third-party Cookies, you will need to find privacy-preserving authentication and identification methods. One possible solution is the [FedCM API](https://developer.mozilla.org/en-US/docs/Web/API/FedCM_API), which aims to allow identity providers to provide identity federation services on the web without the need for third-party Cookies and redirects. The FedCM API supports federated authentication for activities such as registration or login.

**Redefining the Developer Experience**
The end of third-party Cookies is an opportunity to fix mistakes or bad practices you may have followed when building your applications and websites years ago. This will help make your applications and websites more private and secure, but it is also an opportunity to reflect on the level of control you have over every aspect of your application or website.

As we move into a cookie-less world, how much time do you want to spend keeping up with these changes? You may want to [outsource some of the work](https://www.informationweek.com/software-services/applying-the-socratic-method-to-build-versus-buy) so that you don't have to be an expert on all things Cookies, but rather have a dedicated tool to track every change and update.

Perform a thorough audit to see where your applications and websites use third-party Cookies and develop solutions for those scenarios. For every process you build yourself that uses third-party Cookies, create a plan that outlines whether you will continue to build or use a third-party provider.

One solution is to reduce the use of third-party Cookies and adopt other mechanisms, such as session IDs, in areas where they cannot be reduced, such as authentication. I suspect many developers will move from third-party Cookies to first-party Cookies, which may drive other implementation changes, such as using custom domains or profile databases. If you already use a provider to handle third-party Cookies, check if they support migration to first-party Cookies.

[
YOUTUBE.COM/THENEWSTACK
Technology is moving fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)