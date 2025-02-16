# Deno 为 JavaScript 注册表项目创建董事会和章程

![Featued image for: Deno Creates Board, Charter for JavaScript Registry Project](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)

[JSR 是一个用于现代 JavaScript 和 TypeScript 的开源包注册表](https://jsr.io/)，[由 Deno 团队去年创建](https://deno.com/blog/jsr_open_beta)。但根据 Ryan Dahl, Luca Casonato 和 Leo Kettmeir 的一篇新文章，它从未打算成为一个 Deno 项目：它应该是一个[公开管理的 JavaScript/TypeScript 社区服务](https://deno.com/blog/jsr-open-governance-board)。

为了进一步实现这一目标，他们创建了一个新的独立理事会，并附带一份治理章程。

新的 JSR 董事会成员包括：

*   [Evan You](https://github.com/yyx990803)，[Vue.js 和 Vite 的创建者](https://thenewstack.io/vite-creator-launches-company-to-build-javascript-toolchain/)，VoidZero 的创始人；
*   [Isaac Schlueter](https://www.linkedin.com/in/isaacschlueter/)，npm 的创建者，vlt 的联合创始人；
*   [James Snell](https://github.com/jasnell)，Node.js TSC 成员，Cloudflare 的首席系统工程师；
*   [Luca Casonato](https://github.com/lucacasonato)，Deno 的软件工程师，TC39 代表；
*   [Ryan Dahl](https://github.com/ry)，Node.js 和 Deno 的创建者；

他们没有一个人*太*忙。嗯。

该团队还在文章中添加了完整的章程，供那些对此类事情感到好奇的人参考。公平地说，对[你最喜欢的开源产品会发生什么](https://thenewstack.io/open-source-is-at-a-crossroads/)感到好奇是明智的。

JSR 在某种程度上是不言自明的，但值得注意的是，每个包都有一个质量评分，该评分由许多因素决定——例如文档的完整性和用于快速类型检查的最佳类型声明。

## 3 个 Node.js 版本发布了 CVE

1 月，[Node 发布了三个主要的常见漏洞和暴露](https://nodejs.org/en/blog/vulnerability/upcoming-cve-for-eol-versions)（CVE）：

*   Node.js v17.x 或更早版本 CVE-2025-23087
*   Node.js v19.x CVE-2025-23088
*   Node.js v21.x CVE-2025-23089

该博客文章解释了如何迁移，但相关的消息是，如果您不能立即迁移，可以寻求帮助：[HeroDevs](https://www.herodevs.com/) 本周宣布，它将支持这三个版本的 [Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/)，作为其 [永不结束的支持](https://docs.herodevs.com/additional-information/consuming-packages) 计划的一部分。HeroDevs 是 [endoflife.date](https://endoflife.date/nodejs#:~:text=for%20Production%20use.-,Node.,HeroDevs%20Never%2DEnding%20Support%20initiative) 中列出的唯一选项。

HeroDevs 是 [The OpenJS Foundation 的生态系统可持续发展计划](https://www.linuxfoundation.org/press/the-openjs-foundation-announces-the-ecosystem-sustainability-program-with-herodevs-as-the-first-partner) 的创始合作伙伴，Node.js 是该计划的一部分。

## LinkedIn 关于更快 AI 原型设计的案例研究

LinkedIn 一直在（像我们大多数人一样）探索如何在众多产品中使用 AI。工程团队面临的一个挑战是[如何在仍然获得反馈的同时开发快速原型](https://www.linkedin.com/blog/engineering/product-design/building-collaborative-prompt-engineering-playgrounds-using-jupyter-notebook)，根据 LinkedIn 软件工程师 Ajay Prakash 和高级工程经理 Lukasz Karolewski 的说法。

“在执行提示工程时，仅仅孤立地测试提示是不够的，有时我们需要使用像 [LangChain](https://thenewstack.io/benchmark-llm-application-performance-with-langchain/) 这样的编排框架将多个提示链接在一起进行测试，”他们本周写道。

进入 [Jupyter Notebooks](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)。现在你们大多数人可能都很熟悉，但以防万一，Jupyter Notebooks 是交互式 Web 应用程序，允许用户创建和共享可以包含代码、方程式、可视化等内容的文档。

“为了有效地验证想法，需要一个非常紧密的反馈循环，以实现实时协作和迭代，”Prakash 和 Karolewski 写道。“为了实现这一点，我们采用了一种独特的提示工程流程，利用 Notebooks 打破了技术团队成员和非技术团队成员之间的障碍。”

在周四在该网站上发表的文章中，他们解释了 Jupyter Notebooks 如何成为一种可重用的解决方案，“允许工程师快速为他们的用例设置自定义提示工程试验场以及测试数据集。”

Jupyter Notebooks 也可供非技术用户访问，“使提示工程具有包容性和用户友好性，”他们写道。
工程师们还指出了 LinkedIn 在生产环境中部署大型语言模型时面临的挑战。

## 教程探讨使用 Angular 的微前端

[Angular](https://thenewstack.io/angular-documentary-debuts-with-star-studded-cast-of-devs/) 并非*正式*支持[微前端](https://thenewstack.io/4-lessons-learned-from-building-microfrontends/)，但本周，Angular 开发者、培训师和顾问 Manfred Steyer 撰写了一篇详细的文章，介绍了[如何使用 Native Federation 通过 Angular 实现微前端](https://blog.angular.dev/micro-frontends-with-angular-and-native-federation-7623cfc5f413)。

Steyer 创建了 Native Federation，这是一个建立在 Web 标准之上的社区项目，可与 Angular CLI 紧密集成。

“为了将 Federation 的概念与特定的打包器完全分离，我几年前启动了 Native Federation 项目，”Steyer 解释说。“[Native Federation](https://www.npmjs.com/package/@angular-architects/native-federation) 包装了任何打包器，并通过适配器与它们通信。”

他补充说，重点是可移植性和 ECMAScript 模块和 Import Maps 等标准。

他探讨了[如何将 Native Federation 与 Module Federation 结合使用](https://www.angulararchitects.io/blog/combining-native-federation-and-module-federation/)来创建一个“桥接解决方案”，该解决方案可用于集成使用 Angular 基于 Webpack 的构建器构建的 Micro Frontends。[Module Federation](https://module-federation.io/) 是一种支持延迟加载和依赖共享的解决方案，他解释说。

“Native Federation 以这些概念为基础，重点关注标准和可移植性，”Steyer 声明。“它提供了与 Angular CLI 及其高性能的基于 esbuild 的 ApplicationBuilder 的无缝集成，ApplicationBuilder 也是 SSR 和 hydration 等高级功能的基础。”

ApplicationBuilder 在 Angular 17 版本中引入，旨在提供更快、更简化的构建过程。

Steyer 实际上以对 Microfrontends 的优缺点的有用探索开始了这篇文章。

“微前端为企业级应用程序带来了显着的优势，例如增强的团队自主性和独立部署，”他写道。“这些优势使这种架构风格在多团队公司环境中特别有吸引力，在这些环境中，简化的沟通和快速的开发周期至关重要。”

但是，他补充说，存在一些权衡，例如不一致的 UI/UX、增加的加载时间和复杂的运行时集成。

“此外，[像 Angular 这样的框架](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/)，专为编译时优化而设计，在运行时集成场景中面临限制，”他警告说。“因此，Angular 团队建议使用其他替代方案，例如将应用程序拆分为在 monorepo 中管理的库，这更符合 Angular 在类型安全和高效编译方面的优势。”

*您有开发者新闻或故事创意要分享吗？请联系我们。*

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)