## 开发新闻：AI 编码代理、Nue Glows 和新的 Android Beta 版

![Dev News: AI Coding Agent, Nue Glows, and New Android Beta 的特色图片](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)

上周，[CodiumAI](https://www.codium.ai/) 发布了一款新的 AI 编码代理，旨在与代码补全工具配合使用。除了该代理外，CodiumAI 还发布了*其自己的*代码补全工具。

该 AI 工具称为 Codiumate Agent，可免费下载，适用于

- [JetBrains IDE](https://plugins.jetbrains.com/plugin/21206-codiumate--code-test-and-review-with-confidence--by-codiumai)
- [Codiumate for VS Code](https://marketplace.visualstudio.com/items?itemName=Codium.codium)

它会建议相关测试、起草文档、提供最佳实践指导，并主动识别代码重复项。

该公司在其新闻稿中指出：“此公告建立在 CodiumAI 最近成功的 [AlphaCodium 研究](https://github.com/Codium-ai/AlphaCodium) 的基础上，该研究提出了一种通过 LLM 进行代码生成的新方法，该方法建立在基于测试的多阶段迭代流程之上，以解决代码问题。”“AlphaCodium 在 CodeContest 基准测试中的表现表明，其性能将 GPT-4 的准确性从 19% 提高到了 44%。”

## Nue 提供 Glow 进行语法高亮

[Nue.js](https://nuejs.org/blog/introducing-glow) 的开发者发布了 Glow，Nue 创建者兼前端开发者 [Tero Piirainen](https://www.linkedin.com/in/tipiirai/?originalSubdomain=fi) 称其为“语法高亮的全新演绎”。

Glow 仅关注美观——以及你的代码外观。它通过调整少数 CSS 变量，使所有语言都能与你的品牌颜色相匹配。Piirainen 称，它的体积也非常小。

他写道：“Glow 的数量级比主流替代品小得多。”“我们说的是 5K，而不是 5M。它迄今为止是最小的可用实现。”

它旨在与 Shiki 等竞争。

他补充说，[Nue](https://thenewstack.io/dev-news-a-nue-frontend-dev-tool-panda-and-bun-updates/) 当然内置了对 Glow 的支持，尽管 Glow 也可用作独立库。

## JetBrains 推出企业 IDE 服务

JetBrains 宣布推出新的 [企业 IDE 服务套件](https://www.jetbrains.com/ide-services/)，该套件将五种产品和服务组合在一起，可单独或作为捆绑包提供。其中包括：

- IDE Provisioner，一种集中且简化的 IDE 管理工具，用于向整个组织的开发者推送适当的版本、设置和 IDE 插件，以降低与未经批准或过时的版本相关的风险；
- AI Enterprise，为开发者提供基于 AI 的生产力功能，并让公司控制安全性、支出、选择一流的 LLM 提供商和效率措施；
- License Vault，一种工具，可 [自动分发 JetBrains IDE](https://thenewstack.io/gitpod-brings-automated-environments-to-jetbrains-ides/) 许可证；
- Code With Me Enterprise，支持“注重安全的组织”进行实时协作编程；
- CodeCanvas，一种自托管远程开发环境编排器。

![Jetbrains IDE 服务仪表盘](https://cdn.thenewstack.io/media/2024/04/00bf51e5-jetbrainsideservices.png)

图片由 JetBrains 提供

JetBrains IDE 服务产品主管 Ernst Haagsman 在一份准备好的声明中表示：“JetBrains IDE 服务提供了一个简洁的控制面板，简化了开发者工具的管理，同时对开发者来说几乎是不可见的。”

Haagsman 补充说，该公司预计“在不久的将来”推出托管云平台。

## 发布 Android 15 首个 Beta 版

星期四，[Android 15 首个 Beta 版](https://developer.android.com/about/versions/15/overview#pixel) 发布，向开发者和早期采用者开放，为未来某个时间点的消费者版本做准备。

更新内容包括：在 Android 15 设备上，应用默认以端到端方式显示，这意味着开发者不再需要显式调用 Window.setDecorFitsSystemWindows(false) 或 enableEdgeToEdge() 来在系统栏后面显示其内容。也就是说，Google 确实建议继续调用 enableEdgeToEdge() 以在较早的操作系统版本上获得端到端体验。此外，为了帮助实现端到端，许多 Material 3 [可组合项处理内边距](https://developer.android.com/develop/ui/compose/layouts/insets#inset-handling)，具体取决于可组合项在应用中的放置方式，符合 Material 规范，Google 指出。
## Android 15

Android 15 包含了改进，通过加入对应用存档和解存档的操作系统级支持来简化性能，以便用户可以从不常使用的应用中释放设备空间，同时保留其数据。此测试版还通过提供用于联系人密钥的端到端加密的操作系统级 API 来优先考虑隐私和安全性，以便用户可以安全地管理和验证其他人的联系信息。

最后，Android TalkBack 现在将支持通过 USB 和蓝牙使用人机界面设备的盲文显示器，以提高可访问性。

Google 补充说，任何 Pixel 设备都可以下载 Android 15，并通过无线方式获取未来的 Android 15 Beta 版和功能更新。还有一个 [Android 模拟器](https://developer.android.com/about/versions/15/get)，开发人员可以使用它在 Android 15 上测试应用。

## Astro 4.6 版本

[Astro 4.6 已发布](https://astro.build/blog/astro-460/) 星期四，并带有用于国际化的全新手动路由策略。

[Astro](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/) 团队写道：“此新策略允许你完全控制国际化 Astro 网站的路由，以满足默认路由策略无法满足你的需求的情况。”

他们补充说，作为一种替代方案，可以使用 astro:i18n 中的新中间件函数导入 Astro 自身的中间件逻辑，以构建在默认路由策略之上。文章中提供了代码示例。

新版本还允许 [开发人员将](https://thenewstack.io/tips-for-developers-moving-sectors-in-the-software-industry/) 开发工具栏移动到屏幕底部的不同位置。其他更改：

- 此版本增加了对 CSRF 保护的实验性部分支持，尽管这可能会在未来版本中发生变化；
- Cookie 改进，因为 Astro 用于删除 Cookie 的帮助程序现在允许设置更多 Cookie 属性，而不仅仅是路径和域属性；以及
- 弃用对低于 18.17.1 的 [Node.js](https://thenewstack.io/dev-news-django-updates-storybook-7-6-and-node-js-20-beta/) 版本、Node.js 19 和低于 20.3.0 的 Node.js 20 版本的支持。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。