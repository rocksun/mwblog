<!--
title: 你的社交登录按钮依赖第三方 Cookie，而 FedCM 则不需要
cover: https://cdn.thenewstack.io/media/2026/07/12886340-philip-oroni-mtjfwskmra0-unsplash.jpg
summary: 本文探讨了传统社交登录依赖第三方 Cookie 的风险，并介绍了 FedCM 标准。FedCM 通过浏览器原生 API 实现身份验证与追踪脱钩，不仅提升了隐私安全性，还通过原生弹窗改善了用户体验，显著降低了注册流失率。
-->

本文探讨了传统社交登录依赖第三方 Cookie 的风险，并介绍了 FedCM 标准。FedCM 通过浏览器原生 API 实现身份验证与追踪脱钩，不仅提升了隐私安全性，还通过原生弹窗改善了用户体验，显著降低了注册流失率。

> 译自：[Your social login buttons run on third-party cookies. FedCM doesn't.](https://thenewstack.io/fedcm-federated-login-standard/)
> 
> 作者：Jeff Hickman

“使用 Google 登录”和“使用 Apple 继续”已进行联合登录（federated login）十多年了。它们消除了入门障碍，消除了密码疲劳，并将匿名流量转化为账户，这也是它们几乎出现在每个消费者注册页面上的原因。底层的机制才是问题所在。

这些按钮运行在第三方 Cookie 之上。传统的社交登录流程依赖的正是隐私监管机构多年来一直试图关闭的跨域机制。

> “传统的社交登录流程依赖的正是隐私监管机构多年来一直试图关闭的跨域机制。”

Safari 自 2020 年起默认阻止第三方 Cookie（智能防跟踪功能），Firefox 自 2019 年起（增强型跟踪保护），这已经使大约一半的网络处于无 Cookie 状态。

Chrome 的情况则更为混乱：Google 在 2024 年撤回了[其强制弃用计划](https://thenewstack.io/google-and-the-future-of-online-privacy-moving-beyond-third-party-cookies/)，转而采用用户选择模型，而不是直接切换开关，因此每个人都围绕其构建路线图的“Cookie 末日”期限实际上从未到来。不要将其解读为缓刑。两个主要的引擎默认被阻止；Chrome 的无痕模式默认被阻止；广告拦截器和同意疲劳感在不断上升；无论是否有人宣布死亡日期，Cookie 都在因损耗而侵蚀。任何建立在其之上的登录流程都只是借来的时间。

FedCM（联邦凭证管理）是为在这些机制消失后保持联合登录正常工作而构建的标准。W3C 和各大浏览器引擎将其开发为一种浏览器原生 API，可在没有跨站跟踪的情况下运行联合身份流程。

## 它是如何工作的

这种转变是架构上的。在传统流程中，点击社交按钮会触发隐藏的 iframe、重定向或弹窗，以便身份提供商（IdP）可以读取其自己的 Cookie 并确认你是谁。同一渠道也让 IdP 能够跨网络跟踪你。FedCM 将浏览器置于中间作为受信任的调解人。

网站通过一个明确的 API 调用 `navigator.credentials.get()` 请求身份令牌，浏览器负责运行其余部分：

1. 网站从浏览器请求身份令牌。
2. 浏览器从 IdP 托管的配置文件中获取账户详细信息，并将其与发出请求的网站隔离开来。
3. 浏览器显示原生登录提示，而不是弹窗。
4. 在获得明确用户同意后，浏览器将令牌传回网站后端以创建会话。

身份验证和被动跟踪被解耦了。（关于 API 的更多信息：FedCM 规范和 MDN 文档。）

它还解决了 NASCAR 问题。多年来添加的每一个可用的社交登录功能，导致注册页面上贴满了相互竞争的品牌按钮，这相当于在注册页面上贴满了赞助商贴纸的赛车。这就是[认知负荷](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/)，而认知负荷会影响转化率。

> “FedCM 跳过了按钮墙，并在一个原生提示中显示正确的账户。”

因为浏览器已经知道你上次使用了哪个提供商，FedCM 跳过了按钮墙，并在一个原生提示中显示正确的账户。

## 传统流程 vs. FedCM

| | **传统联合流程** | **FedCM** |
| --- | --- | --- |
| 机制 | 隐藏 iframe、重定向、弹窗 | 一个浏览器中介的 API 调用 |
| 隐私模型 | 依赖第三方 Cookie | 无第三方 Cookie；每次登录需明确同意 |
| 用户体验 | 重定向链、被拦截的弹窗、NASCAR 按钮墙 | 一键式原生浏览器提示 |
| 安全性 | 易受钓鱼攻击的重定向界面 | 页面无法伪造的浏览器隔离提示 |

实际的好处是转化率。每一次额外的点击和每一次中断的重定向都会导致部分尝试注册的用户流失，而且移动浏览器经常阻止传统流程所依赖的次级窗口。一个原生的提示消除了这种流失。

> “每一次额外的点击和每一次中断的重定向都会导致部分尝试注册的用户流失，而且移动浏览器经常阻止传统流程所依赖的次级窗口。”

还有一个维护角度：标准化的浏览器 UI 意味着你的团队不再需要构建和维护定制的登录组件，并且流程是通过浏览器版本更新而不是重构来升级的。

## 这在生产环境中是什么样子的

Axel Springer 在 Ory 上运行 FedCM，覆盖了数亿用户。其产品与收入总经理 Thomas Bergemann 明确表示：**“**我们看到注册量增加了超过 15 倍。”（[阅读案例研究](https://www.ory.com/case-studies/axel-springer)。）

Google 自己对浏览器中介登录的测试也显示了类似的结果：放弃令人不快的次级窗口步骤（移动设备经常阻止的步骤），减少了用户流失。

Shopify 在 Cookie 变更之前就转向了浏览器中介身份验证，并在严格的、以隐私为中心的移动浏览器（传统流程经常静默失败的环境）中保持了结账转化率的稳定。

## 开始使用 Ory

**第 1 步：将后端放在 CIAM 平台之后。** 不要自己手动构建。[Ory Kratos](https://www.ory.com/kratos) 原生处理 FedCM 的后端侧，将浏览器端的身份断言转化为安全的会话。（查看 [Ory FedCM 部署文档](https://www.ory.com/docs/kratos/social-signin/fedcm)。）

**第 2 步：配置你的社交登录提供商。** 在 Ory 控制台中，打开“社交登录”面板，选择你的 IdP，并输入其 FedCM 配置 URL。后台信任验证将为你处理。

**第 3 步：嵌入 JavaScript 触发器。** 在你的登录页面上放置一个轻量级片段，以检测支持并在不支持时优雅地回退：

```

if ('IdentityCredential' in window) {
  navigator.credentials.get({
    identity: {
      providers: [{
        configURL: 'https://auth.your-business.com/self-service/methods/oidc/fedcm/google',
        clientId: 'YOUR_CLIENT_ID',
      }]
    }
  }).then((credential) => {
    return fetch('/self-service/methods/oidc/fedcm/login', {
      method: 'POST',
      body: JSON.stringify({ token: credential.token })
    });
  }).catch((err) => {
    console.error('FedCM flow interrupted, fallback to traditional OIDC:', err);
  });
}

```

如果浏览器不支持 FedCM，流程会回退到标准的 OpenID Connect 重定向，因此没有人会在迁移过程中被锁在外面。想在连接真实的 IdP 之前进行测试吗？有一个[免费的 MockFedCM 网站](https://mockfedcm.com/)。

## 这让你处于什么位置

联合登录正在进入浏览器，隐私模型也随之改变。Safari 和 Firefox 已经默认阻止；Chrome 正在通过侧门泄漏 Cookie，而不是直接将其杀死。这两种路径都不会让你的社交登录保持原样。

现在正在审计其[认证栈](https://thenewstack.io/you-can-build-authentication-in-house-but-should-you/)的团队，将来就不会在别人的时间表下调试损坏的登录循环。最好按照自己的时间表而不是浏览器的要求做出改变。