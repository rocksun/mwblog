# Rich Harris 谈论 SvelteKit 和 Svelte 的下一步

翻译自 [Rich Harris Talks SvelteKit and What’s Next for Svelte](https://thenewstack.io/rich-harris-talks-sveltekit-and-whats-next-for-svelte/) 。

Svelte 的创建者解释了为什么它会在今年进行大修，以及 SvelteKit 如何帮助部署前端框架。

![](https://cdn.thenewstack.io/media/2023/03/3b67966b-shutterstock_1942508920-1024x681.jpg)

根据前端框架 Svelte 的创始人 Rich Harris 的说法，第一次重大修订的工作正在进行中。此前，该团队发布了 SvelteKit，这是一个用于构建 Web 应用程序的全栈框架。

“现在 SvelteKit 已经发布，并且已经非常稳定且得到广泛使用，我们的注意力将转回到 Svelte 本身上，”Harris告诉 The New Stack。“目前我们正在开发 Svelte 4，它将现代化代码基。”

该团队正在将底层代码从 TypeScript 切换到 JavaScript。这样的更新将使团队能够在今年晚些时候实现 Svelte 5 的“重大创意”，他补充道。

Svelte是一个框架，但它也是一种用于描述用户界面的语言，Harris 表示。它被编译成 JavaScript，以便可以在任何地方运行。他说，这样做的优点是，在构建应用程序时，Svelte知道应用程序的哪些部分可能会发生变化，哪些部分不会发生变化。

“相比之下，[最初的]框架需要做很多工作来确定页面上需要更改的内容，而 Svelte 是第一个真正表明这是不必要的框架，通过尽可能地提前进行大量工作而不是在浏览器中进行，可以在性能和捆绑大小方面获得显着的收益，” Harris 表示。

## SvelteKit 为前端开发人员提供了什么

专注于 Svelte 意味着短期内将会减少对 SvelteKit 的关注。 SvelteKit 在去年 12 月发布了 1.0 版本，现在已经更新至 1.11 版本。 Harris 表示，它非常稳定。它与 Next.js 、 Gatsb y和 Nuxt 竞争。

“有时人们会问，‘我应该从 Svelte 还是 SvelteKit 开始’，好像它们是互斥的。我会这样描述，如果你熟悉像 React 和 Meta 框架、 Next 或 Remix 这样的框架，那么 Svelte 和 SvelteKit 就有类似的关系，” Harris 说道。

SvelteKit 是一个用户界面框架，用于创建自包含组件，将一些标记、行为和样式组合成可重用的组件，开发人员可以在其应用程序内使用它们，如导航栏、博客文章或聊天小部件，甚至是另一个组件内的组件，他补充道。它可以是开发人员想要的任何东西。

“在过去几年中，我们越来越多地看到框架团队意识到，我们需要为人们提供工具，以实际构建使用这些组件框架的应用程序，” Harris 说。“ Next 可能是这方面的第一次真正严肃尝试。它使 React 不再需要在自己的应用程序框架中拼凑起来。”

简而言之，如果开发人员正在使用 Svelte 构建应用程序， SvelteKit 支持并提供了最佳方法来实现这一点，他解释道。 Svelte 可以在两个不同的环境中运行——在服务器端或在浏览器中，它将操纵 DOM。 SvelteKit 使用 JavaScript 构建，并具有服务器/客户端分离的概念， Harris 说。

“一个是一次性生成 HTML，完成后就完成了，”他说。“另一个是你正在创建这个长期存在的、可能是交互式的东西，它可能会接收到新的数据，你可以点击按钮和创建事件、改变状态和所有这些事情，所以它必须有这个长的生命周期。”

尽管你只需编写一次组件，但你要面对两个非常不同的环境，他补充道。

“ SvelteKit 为您提供了一种非常简单的方法来弥合这个差距，”他说。“它将在服务器上协调初始渲染，然后将无缝地移交到浏览器上。”

## SvelteKit 方法的好处

这种方法的好处是能够更好地感知性能，因为页面的一部分会在 JavaScript 加载时运行，甚至在 JavaScript 无法加载时也会运行，Harris 说这种情况比开发者想象的要多。例如，当他在地铁上时就会遇到这个问题——连接断开了，JavaScript还没有加载。具有服务器端渲染可以使用户仍然能够查看内容。

“这对于搜索引擎优化、归档目的和可访问性等方面都更好，”他说。“这就是为什么我们有这种服务器/客户端思维模式，其中两者在应用程序中是平等的合作伙伴。”

但是，它的功能不仅限于服务器端渲染。SvelteKit 还具有从服务器获取数据的过程。如果页面需要在无需重新加载的情况下更新，它也可以从服务器获取数据，使开发者能够创建 API 端点，以便在同一应用程序中甚至第三方也可以使用数据，他说。

## 边缘渲染和 Svelte

边缘渲染是另一种服务器端渲染。在边缘使用 Svelte 引发了一些讨论，并且是两年前 Svelte 峰会的一个话题。Harris说，这种能力是前端框架的一种功能，而不是Svelte独有的。

“边缘函数的重大创新是不再运行 Node ；它们正在运行一种更轻量级的 JavaScript 运行时，在世界各地的许多不同数据中心都可以实现，” Harris 说。“我们正在看到的演变是从集中式、手动管理的服务器转向这些非常小的计算单元，它们可以在世界各地的任何地方运行。它可以是任何计算机，但在我们的情况下，它恰好是在呈现 HTML 。”

## Svelte Enterprise 准备好了吗？

Harris 承认以前 Svelte 可能不是大型公司的最佳选择。

他说：“如果你负责大公司的工程决策，那么你会考虑这样的事情：这个框架是否得到了主要公司的支持？有很多开发者在使用吗？长期以来，答案都是否定的。”

随着 [Vercel](https://thenewstack.io/vercel-and-svelte-a-perfect-match-for-web-developers/) 的支持，情况已经发生了变化，一些客户现在正在使用 Svelte 。 [Schneider Electric](https://www.se.com/ww/en/) 、 [Pudding](https://pudding.cool/) 和 [GitBook](https://www.gitbook.com/) 是使用 Svelte 的公司之一。

Harris 说：“越来越多的大公司的开发者开始使用它。一旦你知道有一家公司成功地使用了 Svelte ，其他公司通常会跟随。”