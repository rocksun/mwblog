在过去几年里，构建应用程序变得越来越容易，这已不是什么秘密。而[氛围编程](https://thenewstack.io/vibe-coding-agentic-engineering/)只会让它变得更容易。但是，如果一个人甚至不知道全栈应用程序需要文件路由系统、服务器函数、流式SSR和类型安全处理这些元素，他究竟如何才能构建一个全栈应用程序呢？

欢迎来到[TanStack Start](https://tanstack.com/start/latest)。TanStack并不是同类中唯一的全栈框架，但它绝对是初学者最容易上手的框架之一。与[Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/)或[Remix](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/)不同，它们也提供服务器端渲染和全栈功能，TanStack Start强调类型安全路由、服务器函数和最少的样板代码。这使得用户无需配置多种工具，就能快速获得一个可用的应用程序。

TanStack Start专为那些希望获得全栈框架的强大功能，同时又不想承担繁重配置开销或牺牲类型安全性的开发者设计。或者，就本教程而言，它也为那些不完全了解全栈应用程序所需但仍想创造一些酷东西的新手开发者而构建。

*TanStack Start使用Typescript。*

是什么让TanStack Start适合进行氛围编程？

*   **默认类型安全**：与其他一些框架不同，TanStack Start确保您的路由、服务器函数和数据获取都是完全类型化的，从而减少运行时错误。这对氛围编程非常有用，因为您可以在快速迭代的同时，无需担心在实验过程中破坏应用程序。
*   **基于文件的路由**：添加新页面就像创建一个新文件一样简单。无需手动配置复杂的路由。对于氛围编程来说，这意味着您可以即时启动新想法，并在浏览器中看到它们，而无需为设置烦恼。
*   **服务器函数**：您可以直接在应用程序中运行安全的服务器端逻辑，而无需创建单独的API。这让您可以快速进行全栈功能的氛围编程，无需停下来构建外部后端。
*   **流式SSR**：您的页面渲染速度更快，因为TanStack Start可以有效地将内容从服务器流式传输到客户端。对于氛围编程来说，这确保了您的原型即使在添加更多功能时也能感觉流畅和响应迅速。
*   **灵活轻量**：虽然在精神上与Next.js相似，但TanStack Start更小、更易于定制，并与TanStack生态系统紧密集成。这让您可以在氛围编程时无需与框架“对抗”，赋予您构建所需内容的创作自由。

您只需要安装[Node.js](http://node.js)和npm。我们将在项目本身中安装TanStack Start。

让我们一起回顾TanStack Start的基础知识，以便您能够熟练地在此框架之上构建应用程序。

## TanStack Start 基础

这些是TanStack Start构建所基于的基本原则。

*   **根(root)**：将其视为每个页面的“父级”。在TanStack中，`root.tsx`是全局包装器。无论您导航到哪个页面，它都会保持在屏幕上。您可以在此处放置导航栏、页脚和全局样式，这样就无需为每个页面重复编写它们。
*   **索引(index)**：通常被称为`index.tsx`是默认入口点。将其视为首页。当有人访问您的网站时，它会自动加载。
*   **页面(pages)**：这些是您的关于、产品、联系等页面。它们由独立的路由文件组成，TanStack Start会将其转换为可点击的链接和浏览器地址。使用TanStack Start，您无需编写复杂的路由表，只需添加一个文件，TanStack Start就会提供页面自动添加到您的站点所需的所有样板代码。

## 创建一个新的TanStack Start应用

在您的项目终端中，您可以使用以下代码创建一个新应用：

```

npm create @tanstack/start@latest
```

然后会出现一些提示。您可以这样回答：

*   **项目名称**：为您的项目命名
*   **工具链**：ESLint
*   **是否需要演示页面？** 否
*   **附加组件？** 无

然后我们就可以安装依赖项了

```

cd your project name
npm install
```

## 启动开发服务器

下一步是运行开发服务器。这看起来可能是在这个过程的相当早的阶段进行，确实如此。但这就是使用TanStack Start的好处。您的应用程序已经安装了所有的基础组件。安装后我们就可以立即运行。

```

npm run dev
```

在浏览器中导航到`http://localhost:3000`，您将看到TanStack Start的默认页面。

一旦您通过在浏览器中看到样板应用程序确认设置正常工作，我们回到IDE的文件树，这样我们就可以准确地看到我们正在处理的文件。

您的项目结构应如下所示：

```

src/
├── routes/
│   ├── __root.tsx
│   └── index.tsx
├── components/
├── routeTree.gen.ts
├── router.tsx
├── vite.config.ts
└── package.json
```

`__root.tsx`

您可以在`src/routes/__root.tsx`中找到此文件。

理解根布局有助于您了解单个页面如何适应整个应用程序结构。这是您应用程序的基础。它设置HTML结构、加载必要的脚本，并为每个页面提供一致的包装器。没有它，您的页面将无法正常显示，您的JavaScript将无法运行，并且像页眉或页脚这样的共享元素将难以管理。

此文件包装了您的所有页面。关键部分是：

*   `<Outlet />` – 渲染当前页面（例如，`index.tsx`）
*   `<HeadContent />` – 管理`<title>`和`<meta>`
*   `<Scripts />` – 注入JS以使页面具有交互性

以下是TanStack Start的样板代码：

```

import { HeadContent, Scripts, Outlet, createRootRoute } from '@tanstack/react-router'

export const Route = createRootRoute({
  component: RootComponent,
})

function RootComponent() {
  return (
      
      
        
        
        
      
    
  )
}
```

## `index.tsx`

这是您应用程序的主页。它是用户获得的第一印象。这是一个很好的开始氛围编程的地方，因为您可以几乎立即看到代码的添加和更改。使用TanStack Start，您可以构建的东西没有限制。所有样板代码都只是一个起点。

需要注意的一些重要部分：

*   `createFileRoute('/')`将此文件映射到URL /，因此当用户访问您的主页时，会显示此组件。
*   `HomePage`是此路由显示的React组件。

以下是样板代码：

```

import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({
  component: HomePage,
})

function HomePage() {
  return
```

# 欢迎使用 TanStack Start！

}

## `src/routes/about.tsx`

您也可以在此处进行自定义。`src/routes`文件夹中已经包含了一个附加页面。`about.tsx`已包含在内。如果您在浏览器中导航到`http://localhost:3000/about`，您将看到样板“关于”页面。

这是我最喜欢TanStack Start的部分。如果您想添加一个新页面，您只需将相同的样板代码复制/粘贴到routes文件夹中的一个新文件中。这也是氛围编程使其变得更容易的地方。

为`about`页面提供的样板代码如下所示：

```

import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/about')({
  component: AboutPage,
})

function AboutPage() {
  return
```

# 关于此应用

}

添加新页面非常容易。在下一个示例中，我们将创建一个联系页面。首先，在routes文件夹中添加一个`contact.tsx`文件。我使用AI来帮助我。我将`about.tsx`文件粘贴到一个AI工具中，并要求它将其转换为联系页面。它返回了以下代码来启动我的联系页面：

```

import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/contact')({
  component: ContactPage,
})

function ContactPage() {
  return (
```

# 联系我们

) }

TanStack Start还有更多值得探索的地方，但这些是主要的基石。本教程最重要的收获是，在网络上获得一个可运行的原型是多么容易。TanStack Start帮助您氛围编程实时应用程序，而无需考虑架构、路由或任何其他可能让您绊倒并使您无法专注于更令人兴奋的业务逻辑的元素。