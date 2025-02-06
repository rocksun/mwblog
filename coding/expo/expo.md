
<!--
title: 使用Expo进行跨平台移动开发
cover: https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F994c3d85-4d86-4933-be1e-b7710b32515b_1420x1070.png
-->

Expo已悄然成为最流行的跨平台开发工具之一。这是为什么，Expo又是如何工作的？深入了解Expo工程团队。

> 译自 [Cross-platform mobile development with Expo](https://newsletter.pragmaticengineer.com/p/expo)，作者 Gergely Orosz; Elin Nilsson。

React Native和Flutter是迄今为止最流行的跨平台开发技术，正如之前的深入探讨[跨平台移动开发](https://newsletter.pragmaticengineer.com/p/cross-platform-mobile-development)中所述。React Native（Meta出品）在美国和英国以及中大型公司中似乎更受欢迎，而Flutter（Google出品）则在全球范围内为更多应用程序提供支持。

但还有一家公司在跨平台移动技术的讨论中始终出现：Expo。当Bluesky团队分享他们的跨平台技术栈时，他们[提到](https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture)使用了React Native *和* Expo。同时，React Native的“入门”指南强烈建议从Expo开始开发，并称其为“生产级的React Native框架”。

那么，什么是Expo，为什么它对跨平台React Native开发如此重要？

一年前，我前往加利福尼亚州，参观了Expo在帕洛阿尔托的办公室，会见了团队成员以了解更多信息；几个月后，我又与他们取得联系，以了解Expo的工作原理以及它受欢迎的原因。本次深入探讨涵盖：

1. **为什么Expo受欢迎**？它在使React Native像今天一样普及方面发挥了重要作用，其开发者关注度也是一个重要因素。
2. **历史**。Expo起源于对开发和发布移动应用程序的笨拙的失望。今天，使移动开发像Web开发一样无缝的使命仍然激励着团队。
3. **React Native vs React Native框架**。Expo是一个React Native框架，并且是迄今为止*唯一*一个可用于生产的框架。
4. **Expo：开发者工具**。Expo提供的开源免费工具概述。
5. **使用EAS发布到生产环境**。Expo通过其Expo Application Services (EAS)产生收入：一项免费增值远程构建和提交服务。其广泛功能的概述。
6. **跨平台应用程序发布的替代方案**。Ionic Appflow, Shoebird, Fastlane, Bitrise, Codemagic。

*本次深入探讨得到了Expo联合创始人兼首席执行官Charlie Cheever，联合创始人兼首席技术官James Ide和工程经理Brent Vatne的贡献。感谢他们的参与！*

*与我们发布的每一次深入探讨一样，The Pragmatic Engineer与文中介绍的公司没有任何商业关联，也没有为此文章获得任何报酬。更多信息请参见我们的道德声明。*

## 1. 为什么Expo受欢迎？

Expo是一家位于加利福尼亚州帕洛阿尔托的初创公司，拥有32名员工，其中29名是开发人员——惊人的90%的比例。该公司在其关于页面上[列出了员工](https://expo.dev/about)。*像Meta、Google或Microsoft这样的大型软件公司，由于销售、支持以及许多其他支持职能团队的存在，其比例很少超过30-40%。*

如今，开源的Expo框架已用于超过100万个公共Github仓库，每周下载量超过80万次。该项目非常活跃：共有1300多名开发者参与贡献，截至发布时，Discord频道拥有5万多名成员。

**Expo可能是React Native之所以像Flutter一样流行的最大原因**。如今，当我听说一家公司使用React Native进行开发时，几乎总是意味着他们也使用Expo。这是因为它拥有开发者工具，即使是最好的跨平台框架，在iOS和Android原生平台上的开发也变得不那么笨拙。

对于Flutter，Google构建和维护的同样强大的开发者工具长期以来一直是一个差异化因素；这家搜索巨头构建了[复杂的工具](https://docs.flutter.dev/tools/devtools)来调试、分析和诊断Flutter应用程序。但是，Flutter的入门仍然需要[多步骤的开发环境设置](https://docs.flutter.dev/get-started/install/macos/mobile-ios)，而发布iOS和Android应用程序[是一个相当复杂的过程](https://docs.flutter.dev/deployment/android)，相比之下，使用React Native和Expo入门最简单的方法是：

只需打开网站 *snack.expo.dev*。

这个网站叫做“Expo Snack”，你可以在其中立即开始对在Android模拟器、iOS模拟器或Web视图上运行的React Native应用程序进行实时编辑：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86dd398f-6677-47a9-a13c-9e318d760966_1600x1110.png)

*一个在两分钟内无需安装任何东西即可构建的应用程序，运行在远程iOS模拟器上。图片：[Expo Snack](https://snack.expo.dev/)。*

您也可以通过扫描二维码并安装Expo Go应用程序在您的移动设备上运行该应用程序。我也这么做了——在我进行更改时，应用程序进行了实时更新。如此轻松，感觉就像魔法一样。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7f6ebe6-59f0-4910-b031-8faa11554cd2_1272x1128.png)

能够在无需任何本地开发工具的情况下实时编辑应用程序，即使在2025年，也感觉像是魔法。在进行原生iOS或Android开发时，无法在本地未安装任何工具的情况下进行开发。谷歌的云开发环境，[Project IDX](https://idx.google.com/)，非常接近，但速度不如它快。与此同时，Expo Snack只是Expo小型团队生产的众多开发者优先功能之一，其水平与苹果和谷歌的工具不相上下。*更多关于Expo开发工具的信息，请参见下面的“什么是Expo？”和“发布到生产环境”部分。*


为什么公司会转向Expo？我们询问了Bluesky工程团队，他们是React Native的重度用户——我们之前在深度文章[Inside Bluesky’s engineering culture](https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture)中介绍过他们。这是Paul Frazee（使用单个代码库构建了最初的Bluesky iOS、Android和Web应用程序的开发者）告诉我们的：

> “我们最初使用Xcode和Android Studio手动构建应用程序，然后上传构建版本。
>
> 我们最初关注Expo的原因是为了帮助我们进行部署。Expo拥有非常可靠的云构建基础设施（EAS Build）和无线更新系统（EAS Update）。我们查看了其他React Native云构建服务，但没有一个看起来构建得那么好，所以我们冒险尝试了Expo。我们发现自己迭代地采用了Expo模块，然后完全迁移到他们的框架。我唯一后悔的是我们没有一开始就使用它。我很少有如此积极的体验。
> 
> 我们在大约9个月的应用程序开发后，大约在2023年2月开始迁移到Expo。那时我们已经有了一个相当成熟的应用程序。这是一个迭代迁移，进行得相当顺利。”


## 2. 历史

如前所述，Expo的创立源于对构建移动应用程序所需时间的挫败感。2012年，Charlie Cheever是Quora的CTO，正在为该问答网站开发iOS和Android应用程序。作为一名经验丰富的Web开发者（他曾是Facebook的早期工程师），他认为最多只需要几周时间就能构建每个原生应用程序。然而，实际上每个平台都需要几个月的时间，并且在iOS和Android上都包含糟糕的开发者体验；至少，与Web相比是这样。由此产生了Expo的想法。Charlie总结了目标：

> “Web是一种相当不错的开发方式，而且功能非常强大。让我们采用Web和Web开发的所有优点，让移动开发领域变得更好。”

他和James Ide合作，开始尝试使用Web技术构建移动应用程序的方法，最终得到一个封装了移动原生组件的框架；基本上与React Native非常相似。他们即将发布时，React Native发布了，它是由Meta创建和使用的，大约有40人在开发它。相比之下，尚未发布的Expo框架是由两个人开发的。

**Expo并没有与React Native竞争，而是决定拥抱它**。Charlie和James明白，*编写*应用程序只是发布跨平台应用程序的众多部分之一。每个使用React Native的开发者仍然需要解决其他问题领域：
* 分发到iOS和Android应用商店
* 发布策略
* CI管道
* 改进开发者体验

**“Exponent”是团队发布的第一个产品**；一个位于React Native之上的React Native开发工具。该团队在2015年的一次名为React Rally的React会议上[宣布](https://www.youtube.com/watch?v=HaxZMDP6eDA)了它。它负责处理以下事项：
* 处理Xcode和Android Studio
* iOS配置文件
* 开发和部署证书
* 任何Objective-C、Swift和Java相关的事项

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45dad71a-502c-4c27-97f6-ee6ebb4309d8_1522x888.png)

*2015年用于引入指数的解释草图*

Exponent 工具集不断发展，两年后的 2017 年，名称改为 Expo，因为它更容易说和记住。从 2017 年开始，Expo 每年多次发布新的主要版本到 Expo SDK。当时，Expo 的 SDK 版本为 21；今天，它已经是 52 版本了。*公司维护着一个变更日志，其中列出了显著的更改以及详细的变更日志。*

## 3. React Native 与 React Native 框架
Expo 是一个使用 React Native (RN) 的框架和工具集，它简化了 RN 应用程序的开发。它恰好也是目前唯一被认为是生产级别的 React Native 框架。但是什么是“React Native 框架”？由于 React Native 建立在 React 之上，让我们看看 React 世界中的工作原理。

**React 与 React 框架**

**React：提供核心功能**。React 是一个用于构建 Web 用户界面的 JavaScript 库。
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff87f67fb-f5ab-48f9-9fdd-e3363d5ab4be_1600x725.png)

*使用名为 JSX 的标记的 React 代码，JSX 是 React 推广的一种 JavaScript 语法扩展，支持类似 HTML 的渲染逻辑。来源：*[React](https://react.dev/)

React 负责许多事情，例如：

* **高性能**: 使用虚拟 [DOM](https://en.wikipedia.org/wiki/Document_Object_Model)，React 创建 UI 的内存中数据结构缓存，计算结果差异，并仅在需要时更新浏览器的 DOM。此过程称为协调，并产生更好的性能
* **JSX**: 支持 JSX 语法扩展，允许在 JavaScript 中使用类似 HTML 的代码
* **可重用的 UI 组件**: React 的核心是可重用的组件。React 指定如何定义组件、它们的生存周期事件、嵌套、[组件间通信](https://react.dev/learn/passing-props-to-a-component)、基于[不同条件](https://react.dev/learn/conditional-rendering)的不同渲染以及[更多](https://react.dev/learn/your-first-component)功能
* **处理事件**: 例如点击、悬停、键盘输入、滑动[等](https://react.dev/learn/responding-to-events)。
* **UI 状态管理**: 一种管理状态的明确方法。React 不操作 UI 的各个部分，而是使用[声明式方法](https://react.dev/learn/reacting-to-input-with-state)
* **其他功能**: 例如[对 TypeScript 的支持](https://react.dev/learn/typescript)、[React Hooks](https://react.dev/reference/react/hooks)（从组件中使用 React 功能）以及对[服务器组件](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components)的支持等。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5cad761-bf99-4e9f-8f3c-ca3d9cbf3063_1600x814.png)

*最简单的 React 组件。React 框架指定了如何创建这些组件，并且甚至支持组件的复杂用例。来源：*[React](http://v)

**React 框架：提供生产级功能**。你仅使用 React 就可以构建 Web 应用程序。但是，应用程序越复杂越大，就必须构建更多附加功能，例如页面间的路由、多个文件间的代码分割、数据获取、将一些渲染移动到服务器等等。以下是 React 团队在[入门指南](https://react.dev/learn/start-a-new-react-project)中关于框架的说明：

> “您可以不使用框架而使用 React，但是我们发现大多数应用程序和网站最终都会构建针对常见问题的解决方案，例如代码分割、路由、数据获取和生成 HTML。这些问题对于所有 UI 库都是通用的，而不仅仅是 React。
>
> 通过从框架开始，您可以快速开始使用 React，并避免以后基本上构建自己的框架。”

React 团队列出了三个“生产级”框架，其定义如下：

* 支持在生产环境中部署和扩展应用程序所需的所有功能
* 开源
* 可以部署到个人服务器或托管提供商

满足这些条件并由 React 团队推荐的 React 框架：

- **Next.js:** Next.js 的 Pages 路由器是一个全栈 React 框架。它用途广泛，可用于创建任何规模的 React 应用，从静态博客到复杂的动态应用程序。由 Vercel 维护。
- **Remix**: 一个具有嵌套路由的全栈 React 框架。它允许您将应用程序分解成可以并行加载数据并响应用户操作进行刷新的嵌套部分。由 Shopify 维护。
- **Gatsby:** 一个用于快速构建基于 CMS 的网站的 React 框架。其丰富的插件生态系统和 GraphQL 数据层简化了将内容、API 和服务集成到一个网站的过程。由 Netlify 维护。

React 由 Meta 资助，但 React 框架由其他公司资助。Vercel 和 Netlify 是托管提供商，它们资助这些框架，因为这有助于推动其服务的采用。Remix 被 Shopify 收购，并且正在 [合并到](https://remix.run/blog/merging-remix-and-react-router#whats-happening-to-remix) React Router 中。

**React Native 与 React Native 框架**

考虑到 React 和 React 框架之间的区别，React Native 在“核心”React Native 功能和框架应提供的生产就绪功能之间存在类似的概念划分，这可能并不令人意外。

**React Native 提供构建原生应用的核心 API 和功能**。它是一个框架，允许使用 React 编程范式来构建原生 iOS 和 Android 应用程序，它提供：
* 一个用于 JavaScript 和 React 语法的运行时，并能够使用原生 iOS 和 Android 扩展来增强它
* 与纯原生应用程序足够相似的性能
* 持续支持现代 React 功能，例如
    * [Suspense](https://react.dev/blog/2022/03/29/react-v18#new-suspense-features)（声明式地指定组件树的加载部分）
    * [Transitions](https://react.dev/blog/2022/03/29/react-v18#new-feature-transitions)（区分紧急和非紧急更新）
    * [自动批处理](https://react.dev/blog/2022/03/29/react-v18#new-feature-automatic-batching)（将多个重新渲染分组到单个重新渲染以提高性能）和其他 API
* [调用](https://reactnative.dev/docs/next/turbo-native-modules-introduction)原生 iOS 或 Android API
* 热重载：在开发过程中，查看在代码中所做的更改如何在模拟器或设备上大约一秒钟内更新

**React Native 框架提供生产级功能：**React Native 团队遵循 RFC 方法进行讨论和提案。在 2024 年，该团队启动了一个 [关于 React Native 框架的 RFC](https://github.com/react-native-community/discussions-and-proposals/blob/main/proposals/0759-react-native-frameworks.md#what-do-we-recommend-to-react-native-library-developers)，并得出了以下关于 RN 框架的定义：

> “将原生应用交付到生产环境通常需要一套默认情况下未作为 React Native 的一部分提供的工具和库，但这些工具和库对于实现生产环境部署仍然至关重要。此类工具的示例包括：支持将应用程序发布到专用商店，或支持路由和导航机制。
>
> 当这些工具和库被收集起来形成一个构建在 React Native 之上的具有凝聚力的框架时，我们称之为 React Native 框架。>
> 
> Meta 内部如何使用 React Native 就是一个定制 React Native 框架的实际示例。我们确实有一套库、脚本和工具，可以使 React Native 与其使用的各种应用程序更容易集成。”

**Expo：目前唯一可用的生产级开源 RN 框架**。在发布时，React Native 团队仅推荐 Expo 作为生产级框架。这是一个非常强烈的推荐，因为同一个团队也 [写道](https://github.com/react-native-community/discussions-and-proposals/blob/main/proposals/0759-react-native-frameworks.md#what-do-we-recommend-to-react-native-library-developers) 关于 React Native 框架：

> “你要么正在使用 React Native 框架，要么正在构建你自己的 React Native 框架”

那么 Meta 为什么最终推荐 Expo 呢？解释如下：

> “我会稍微澄清一下这个建议：Meta 团队关于 React Native 的指导意见是，你需要使用某个框架才能构建任何实际的东西。如果你不选择现成的框架，你最终将不得不自己构建一个。
>
> 今天，Expo 是唯一一个非常成熟的 React Native 框架。但是，如果明天另一个团队出现并构建另一个真正优秀的 React Native 框架，每个人都会欢迎它。”

与 Meta 的合作始于早期，正如 Expo 的工程经理回忆的那样：

> 我们中的一些人从React Native最早的阶段，也就是2015年React Conf上的初始预览版本发布以来，就一直是它的贡献者。近10年的参与证明了我们对React Native成功的深度投入，并且可以信赖我们参与从会议演讲到开源项目中一些最大规模的倡议的所有工作。
>
> 例如，在过去的一年中，我们一直在与Meta的React Native团队紧密合作，以使[New Architecture for React Native](link-to-new-architecture)准备好向开源社区推出。我们通过迁移Expo的所有工具来帮助准备生态系统，使用依赖关系统计数据来确定影响最大的第三方库并帮助迁移它们，报告和/或修复我们在React Native中遇到的相关问题，教育社区，以及推出如此重大的变化所带来的许多其他项目。

Expo似乎以一种帮助Meta的方式填补了空白，使React Native更容易被外部开发者访问。Charlie：

> “Meta的重点主要在于使React Native在Meta内部运行良好，而我们的重点在于使其在Meta外部运行良好。Meta从使React Native开源中并没有直接受益，他们团队的大部分精力都集中在使其对他们自己运作良好上。因此，我们能够以一种双赢的方式自然地融合在一起！”

React Native本身并不支持部署和扩展生产级应用程序所需的工具。Meta拥有自己的生产级React Native框架，该框架是根据其自身需求及其[大量的自定义内部工具](https://newsletter.pragmaticengineer.com/p/facebook)量身定制的。因此，对于Meta来说，拥有一家公司构建更通用的生产框架来构建React Native应用程序是一件好事。

## 4. Expo：开发工具集合

Expo通过提供额外的抽象（如路由）和工具（如命令行）来加快应用程序的构建速度，从而简化了构建生产级React Native应用程序的过程。它在React Native之上构建，为React Native开发带来了这些附加功能：