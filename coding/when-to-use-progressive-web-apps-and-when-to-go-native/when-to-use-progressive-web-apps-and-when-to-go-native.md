
<!--
title: 何时使用渐进式Web应用，何时使用原生应用
cover: https://cdn.thenewstack.io/media/2025/05/06729690-getty-images-2okyxq7vlku-unsplashb.jpg
summary: PWA vs Native App？主流浏览器已支持 Service Worker，PWA 可离线运行、推送通知，提升用户体验。PWA 单代码库降低维护成本，SEO 友好。但 PWA 无法深度集成蓝牙、NFC 等原生 API。选型需考虑离线访问、推送策略、原生集成等因素。
-->

PWA vs Native App？主流浏览器已支持 Service Worker，PWA 可离线运行、推送通知，提升用户体验。PWA 单代码库降低维护成本，SEO 友好。但 PWA 无法深度集成蓝牙、NFC 等原生 API。选型需考虑离线访问、推送策略、原生集成等因素。

> 译自：[When To Use Progressive Web Apps and When To Go Native](https://thenewstack.io/when-to-use-progressive-web-apps-and-when-to-go-native/)
> 
> 作者：Alexander T Williams

还记得以前的 Web 应用很笨拙，只是在 App Store 中获得“真正”应用之前的临时替代品吗？现在已经不是这样了。今天的渐进式 Web 应用 (PWA) 可以离线运行、发送推送通知，并且加载速度非常快，几乎可以预测你想要什么。

一些公司已经完全放弃了他们的原生应用，发现 PWA 不仅满足了用户的期望，而且[实际上降低了维护开销](https://thenewstack.io/growth-of-progressive-web-apps/)、统一了技术栈并提高了参与度。那么，我们最终准备好让 PWA 占据中心舞台了吗？

## 浏览器已经成熟

过去 PWA 让人感觉像是一种妥协的原因之一，仅仅是因为浏览器支持不够。现在已经不是这样了。今天，[所有主流浏览器都支持 Service Worker](https://caniuse.com/serviceworkers)，这是支持离线功能、后台同步和推送通知的基本组件。随着 Cache Storage、IndexedDB 和 Fetch API 等 API 的标准化和广泛采用，PWA 体验可以真正像原生应用一样。

以流媒体内容为例。借助 Streams API，[开发人员可以在页面仍在加载时开始渲染页面](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API)，从而大大缩短了 Time to Interactive (TTI)。将其与延迟加载和细粒度的缓存控制相结合，你将获得一种感觉瞬间完成的体验——尤其是在重复访问时。

至于后台同步，它是一个沉默的强大功能。用户不必坐在那里等待上传或发送消息。通过定期后台同步，你的 PWA 可以悄悄地处理这些任务，即使在用户离线或切换选项卡时也是如此。

## 成本等式：一个代码库统管一切

从商业角度来看，PWA 最大的优势之一是简单性。你无需为 iOS、Android 和 Web 维护单独的代码库，而是构建和维护一个代码库。这意味着更小的开发团队、更少的错误和更紧密的反馈循环。对于电子商务网站或[任何涉足全渠道零售的品牌](https://feedonomics.com/blog/omnichannel-retail/)而言，产品更新、促销和数据提取都变得更加容易。

更新也更快、更可控。你无需等待 App Store 批准每个版本。你发布后，用户下次加载 PWA 时，它就是最新的。这种敏捷性对于在快速变化的市场中工作的团队[或那些积极进行 A/B 测试的团队](https://thenewstack.io/rethinking-testing-in-production/)来说是无价的。

然后是 SEO。与原生应用不同，PWA 存在于 Web 上——这意味着它们是可抓取和可索引的。这很重要，尤其是对于内容丰富的平台、电子商务网站和希望将可发现性融入其产品中的媒体品牌而言。

## 真实世界的转变：原生应用被取代

Pinterest 在 2017 年引起了轰动，[当时它推出了 PWA，并看到核心参与度指标飙升](https://medium.com/dev-channel/a-pinterest-progressive-web-app-performance-case-study-3bd6ed2e6154)。网站停留时间增加了 40%，用户生成的广告收入增长了 44% 以上。Flipkart Lite 是另一个有据可查的案例，它使跳出率降低了一半，并使网站停留时间增加了两倍。

它们不仅仅是小幅升级，它们表明，如果实施得当，PWA 可以完成以前为原生体验保留的繁重工作。更重要的是，它们强调用户并不关心平台，只要体验是无缝的。

较小的团队也从 PWA 中受益。预算有限的初创公司[以前不得不在 Android 和 iOS 开发之间做出选择](https://adapty.io/blog/android-vs-ios-development/)，现在可以构建一个高性能的 PWA。这意味着更快的部署、更简单的 QA 周期和更少的平台难题。

## PWA 的优势（以及劣势）

在某些情况下，PWA 具有明显的优势。如果你的用户在低连接环境中使用，PWA 可以缓存整个工作流程和资产以供离线使用。想想现场服务人员、奔波中的销售代表或使用间歇性 Wi-Fi 的学生。将其与[用于主屏幕安装体验的 Web App Manifest 结合使用](https://thenewstack.io/its-time-to-build-a-progressive-web-app-heres-how/)，你将获得类似于应用程序的东西——但没有 App Store 的把关。

PWA 还在保留和重新互动方面占据主导地位。推送通知可以将用户推回你的体验，就像原生应用一样。添加后台同步以处理更新或新内容交付，你就可以消除每一个环节的摩擦。这对于[本地化目的](https://localazy.com/features/webflow-localization)尤其有用，因为每个地区都会收到不同的通知。
也就是说，PWA 存在局限性。PWA 无法像原生应用那样，完全深入地利用特定于平台的 API，例如蓝牙、NFC 或生物识别身份验证。如果你的应用依赖于这些 API，或者你所在的垂直领域中，Apple 的 App Store 分发是不可协商的，那么原生应用可能仍然是正确的选择。此外，[虽然 iOS 在 PWA 支持方面取得了长足的进步](https://brainhub.eu/library/pwa-on-ios)，但某些功能仍然落后于 Android，尤其是在后台任务和通知支持方面。

## 构建决策框架

在深入 PWA 开发之前，请先问自己一些难题：

**你的用户是否需要离线访问？**如果你的产品需要在互联网连接不稳定或没有互联网连接的区域中使用，那么离线功能可能会带来变革性的影响，而 PWA 可以提供这种功能。这对于在途、现场或连接不稳定的地区的用户尤其重要。

**推送通知会成就或破坏你的参与策略吗？**如果及时的用户重新参与至关重要，例如在电子商务、社交应用或新闻平台中，那么[推送通知可能是高留存率和无声流失之间的区别](https://www.pugpig.com/2024/09/17/mobile-matters-guide-push-notifications/)。PWA 可以在 Android 上提供这些功能，在 iOS 上的支持程度稍逊，因此平台考虑因素在这里很重要。

**你是否可以在没有深度原生集成的情况下提供核心功能？**PWA 现在可以涵盖广泛的功能，但它们仍然无法取代深度操作系统级别的集成。如果你的产品严重依赖于原生支付、相机 API 或蓝牙等功能，那么原生应用可能仍然是更安全的选择。

**App Store 的可见性是必须的吗，或者你的营销策略可以在开放的网络上蓬勃发展？**如果 App Store 的发现为你的品牌带来了重要的用户获取，那么放弃原生应用可能会让你失去曝光机会。但是，如果你的受众是 Web 优先的，并且 SEO 在你的策略中起着重要作用，那么 PWA 可以开辟新的增长渠道。

如果答案倾向于 Web 优先的灵活性和平台独立性，那么 PWA 可能是正确的选择。

也就是说，你不需要立即全力投入。许多团队首先构建一个强大的 Web 应用，然后逐步使用 Service Worker 和其他 PWA 功能对其进行增强。这使你可以在进一步投入之前验证你的产品与市场的契合度以及用户体验。

## 准备好飞跃了吗？

渐进式 Web 应用不再只是一个聪明的名字，它们是原生开发的可行且通常更优越的替代方案。生态系统已经准备就绪。工具链很强大。用户的期望也已经赶上。如果你想要在不牺牲精致度的前提下扩大覆盖范围，并且在不分割代码库的情况下提高敏捷性，那么 PWA 值得在你的路线图上占有一席之地。

我们正处于一个转变的边缘，Web 不再是应用商店的配角。唯一剩下的真正问题是：你准备好为它构建了吗？