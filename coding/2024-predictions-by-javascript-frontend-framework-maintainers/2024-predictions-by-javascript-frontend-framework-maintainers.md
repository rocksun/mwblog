<!--
title: JavaScript前端框架2024年展望
cover: https://cdn.thenewstack.io/media/2023/12/90fe5532-year-forecast-1-1024x576.png
-->

Angular、Next.js、React和Solid的维护者和创作者们展望2024年，分享了他们计划中的改进。

> 译自 [2024 Predictions by JavaScript Frontend Framework Maintainers](https://thenewstack.io/2024-predictions-by-javascript-frontend-framework-maintainers/)，作者 Loraine Lawson。

由于水晶球破裂，The New Stack 采访了来自 Angular、Next.js、React 和 Solid 的创始人和维护者，询问他们对2024年的规划。以下概述了前端开发者可以期待的内容。

## Angular: 可选的 Zone.js

去年，Angular 的两个重大成就是[引入了细粒度的反应性 Signals](https://thenewstack.io/angular-qwik-creator-on-how-js-frameworks-handle-reactivity/) 和可延迟的视图，Google 的 Angular DevRel 技术负责人 [Minko Gechev](https://www.linkedin.com/in/mgechev/) 说。下一年将在此基础上继续专注于细粒度的反应性，并使 Zone.js 可选，他向 The New Stack 透露。

在 Angular 中，Zone 是跨异步任务持续存在的执行上下文。[Zones 在这个 GitHub 仓库中有详细解释](https://github.com/angular/angular/blob/main/packages/zone.js/lib/zone.ts)，但一个 zone 有五个职责，包括拦截异步任务调度和封装回调进行错误处理和跨异步操作的区域跟踪。Zone.js 可以创建跨异步操作持续存在的上下文，以及为[异步操作](https://angular.io/guide/zone#:~:text=lifecycle%20hookslink-,Zone.,lifecycle%20hooks%20for%20asynchronous%20operations)提供生命周期钩子。

“我们正在探索为现有项目启用可选的 Zone.js，开发人员应该能够通过重构现有应用来利用这个功能，” Gechev 说，“使用可选的 Zone.js，我们预期加载时间和首次渲染会有改进。在细粒度反应性的工作将其提升到另一个水平，使我们能够仅检测组件模板的一部分中的更改。”

这些特性将导致运行时更快，他说。

在另一项性能操作中，Angular正在考虑是否默认启用混合渲染。Gechev补充说，可以选择不使用混合渲染，因为它可能会增加托管需求和成本。

“我们看到 SSG(静态站点生成)和 SSR(服务器端渲染)的巨大价值，通过在 [v17 中奠定坚实的基础](https://thenewstack.io/deferable-views-page-load-improvements-coming-to-angular/)，我们正在努力完成最后的抛光工作，以从一开始就启用此体验，” Gechev说。

他补充说，优先事项之一是实现其 [Signals RFC](https://github.com/angular/angular/discussions/49685)。

开发者也可能会看到 Angular 文档的改进。根据开发者调查，开发者希望获得升级的学习体验，其中包括使 Angular.dev 成为该框架的新首页。开发人员还将首次加载时间列为优先事项，混合渲染、局部 hydration 和可选的 Zone.js 应该可以解决这一问题，他补充说，组件创作也是 Angular 计划进一步简化的事项。

“我们致力于迭代交付功能，并随着时间的推移逐步增强它们”，Gechev说，“开发者将能够在2024年受益于所有改进，并在未来几年获得更好的开发者体验和性能。”

## Next.js: 正在开发新的编译器

Next.js 在2023年引入了新应用服务器，旨在支持React服务器组件(RSC)和[Server Action](https://blog.logrocket.com/diving-into-server-actions-next-js-14)。它继续支持旧的应用服务器，其路由系统可以互换，Vercel产品负责人Lee Robinson说，该公司监督此框架。这种互操作性意味着开发人员可以慢慢地添加新特性。

“有些客户已经使用Next.js构建了5-6年，他们对这些较新的特性的采用也需要多年时间”，Robinson说，“我们希望尽可能顺利地让人们参与这个过程。”

在新一年，Next.js希望解决许多问题，但一个优先事项可能是简化缓存。就开发者体验而言，这可以更容易些，他说。

“通常，生态系统中的许多开发人员不得不引入大量额外的包或学习如何使用其他工具来进行获取、缓存和重新验证”，Robinson说，“Next.js现在已经内置了很多这些功能，这非常强大，但这也意味着需要学习的额外事项，初步反馈是，'这很棒，非常强大，但如果能简单一些就更好了'。”

Next.js团队也将继续关注性能改进，他称这是“我们的持续投资”。

这很可能以明年的新编译器的形式呈现，该编译器将加快在开发人员机器上启动Next.js的速度，他补充说。该编译器已经研发了大约一年，Vercel 一直在其产品和应用内部使用它。他说，这个由Rust提供动力的编译器即使不缓存也比之前的编译器缓存时快。

“我们距离推出它非常近了，每个人都可以默认启用它，而且它比现有的 Webpack 编译解决方案更快”，Robinson说，“开发人员希望他们的工具更快。如果它变得更快，他们永远不会抱怨。因此，有趣的是看到工具制造者，不是工具的用户，而是实际的工具开发人员转向诸如 Rust 之类的底层工具，以帮助获得这最后一英里的性能提升。”

第三个目标是继续为未来 10 年的 Next.js 奠定基础。

“这个新的路由系统，你知道，我们显然非常兴奋。我们认为这是未来的基础”，他说，“但这也需要时间。人们会试用，他们会有功能请求，并希望看到事情发生改变。我们将其视为未来 5 至 10 年的非常长期投资。”

他补充说，一个“某天”但可能不是今年的目标是以更好的方式处理 Next.js 中的内容。

“今天，它能够正常运行，你仍然可以连接到任何你想要的内容源，但有可能简化开发者体验的方法，”他补充说。“这更像是一种可有可无的东西，而不是一项必需品，这就是为什么我认为我们在2024年不会着手处理它的原因，但我希望将来能够对其进行一些处理。”

## React：2024预览

Meta的React工程经理Eli White说，React团队希望在新一年看到更多框架采用React服务器组件。

“对于大多数人来说，RSC已成为他们对React范围的看法的重大变化，从仅仅是一个UI层，到对您架构应用程序的方式有更多影响，以获得最佳的用户和开发人员体验，特别是对于单页应用程序(SPA)不够好的应用程序”，White说。

虽然他没有具体说明2024年的任何新发展，但White确实表示他们将发布和分享2023年一些启示的更多进展。例如，在React高级会议上，该团队向与会者展示了React Forget，这是React的自动记忆编译器。 White说，[React Forget将意味着开发人员不再需要使用useMemo和useCallback](https://dev.to/usulpro/how-react-forget-will-make-react-usememo-and-usecallback-hooks-absolutely-redundant-4l68)。

在React Native EU活动上，White补充说：“我们分享了消息，即我们将在0.73版本开始将Web开发人员熟悉的Chrome开发工具引入React Native。我们还初步展示了我们对Static Hermes的研究成果，这是我们用于JavaScript的本地编译器，它不仅有可能加速React Native应用程序，而且从根本上改变了JavaScript的有效用途。”

## Solid：专注于基本元素(Primitives)

Solid的创作者Ryan Carniato表示，Solid开发人员可以期待2024年推出的SolidStart 1.0和Solid.js 2.0。SolidStart是一个元框架，意味着它建立在Solid.js框架之上。他说，这与Svelte的SvelteKit相类似。

[SolidStart的文档](https://start.solidjs.com/getting-started/what-is-solidstart)这样解释：

“Web应用程序通常由许多组件组成：数据库、服务器、前端、打包工具、数据获取/变异、缓存和基础架构。协调这些组件具有挑战性，通常需要在应用程序堆栈中共享大量状态和冗余逻辑。这就是SolidStart的作用：提供一个在一个位置将所有这些部分组合在一起的平台。”

由于SolidStart仍处于测试阶段，Carniato有机会基本上使用生态系统中已有的东西来使其更好。

“其中一个重要的部分是，我们现在使用Nitro而不是编写自己的部署适配器，Nitro还支持Nuxt框架，这使你能够部署到所有不同的平台，” Carniato说。

另一个例子是任何Solid路由器都将在SolidStart中起作用。

“这意味着对路由器的基础部分进行了很多更新，以使它们可以共同工作，但我对最终结果感到非常满意，因为我们小团队的志愿者需要维护的代码量要少得多，并且它为开发人员提供了很多灵活性和控制，“他说。“他们不被迫采用单一的解决方案，这对我来说非常重要，因为每个人都有自己的需求。正如我所说，如果构建正确的组件并找出这些构建块是什么，人们可以做更多的事情。”

最终结果是一个“可互换”组件的元框架，不持有太多主观意见，他说。Solid团队一直在思考在越来越多的元框架决定开发人员使用什么的世界中，正确的基本元素对影响的问题。

“对我来说，一直都是关于基本元素的构建块，非常注重工程，我认为这也是它与众不同的原因之一，”他说。“我一直喜欢给予选择，并且我认为如果你拥有正确的基本元素，正确的构建块，你就可以构建出正确的解决方案。”

他表示，Solid 2.0预计将在2024年中晚期发布。目前，他们正在原型化它将如何处理异步系统。

“Solid 2.0也将是一个非常重要的发布版本，因为我们正在重新审视反应系统，并思考如何解决异步信号或异步系统的问题，” Carniato说。

他补充说，Solid试图在控制和性能之间取得平衡。

“我们的社区中有很多热情的人，非常关注性能的技术人员，关心控制的人，”他说。“我们吸引了许多真正想要控制构建的每个部分的人。”
