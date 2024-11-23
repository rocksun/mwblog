最后更新：2024年11月12日

服务器端渲染 (SSR) 已经存在一段时间了，但它值得进一步探索。这项技术可以使您的 Web 应用更快、更利于 SEO。

本指南将解释 SSR，为什么您可能想要使用它，以及如何在不费力的情况下实现它。我们将介绍基础知识，将其与客户端渲染进行比较，并讨论一些实际示例。

从根本上说，SSR 是指在服务器上而不是在浏览器上渲染您的网页。当用户请求页面时，服务器会完成所有繁重的工作并将完全渲染的页面发送到客户端。然后，客户端 JavaScript 接管以使其具有交互性。

服务器在厨房里做准备工作，浏览器只需摆盘和上菜。

这是一个最小的 Express.js 示例：

```javascript
const express = require('express');
const React = require('react');
const ReactDOMServer = require('react-dom/server');
const App = require('./App');
const app = express();
app.get('/', (req, res) => {
  const html = ReactDOMServer.renderToString(<App />);
  res.send(`
<!DOCTYPE html>
<html>
<body>
<div id="root">${html}</div>
<script src="client.js"></script>
</body>
</html>
`);
});
app.listen(3000, () => console.log('Server running on port 3000'));
```

当我们谈到 SSR 提供“完全渲染的页面”时，重要的是要理解这实际上意味着什么。让我们分解一下：

完全渲染的页面是一个 HTML 文档，其中包含用户首次加载页面时将获得的所有内容。这包括：

- 完整的 DOM 结构
- 所有文本内容
- 图片占位符和其他媒体元素
- 初始样式

这是一个基本示例：

```html
<!DOCTYPE html>
<html>
<head>
<title>My SSR Page</title>
<style>
/* Initial styles */
</style>
</head>
<body>
<header>
<h1>Welcome to My Site</h1>
<nav><!-- Fully populated navigation --></nav>
</header>
<main>
<article>
<h2>Article Title</h2>
<p>This is the full content of the article...</p>
</article>
</main>
<footer><!-- Fully populated footer --></footer>
<script src="hydration.js"></script>
</body>
</html>
```

相比之下，客户端渲染 (CSR) 的初始 HTML 可能如下所示：

```html
<!DOCTYPE html>
<html>
<head>
<title>My CSR Page</title>
</head>
<body>
<div id="root"></div>
<script src="bundle.js"></script>
</body>
</html>
```

CSR 页面完全依赖 JavaScript 来填充内容。

**更快的初始绘制**: 浏览器可以立即开始渲染内容。**更好的 SEO**: 搜索引擎无需执行 JavaScript 即可读取所有内容。**改进的辅助功能**: 屏幕阅读器和其他辅助技术可以立即访问内容。**弹性**: 即使 JavaScript 无法加载，基本内容也可以使用。

发送完全渲染的 HTML 后，SSR 应用程序通常会经历一个称为[水合](https://www.builder.io/blog/hydration-is-pure-overhead)的过程：

- 服务器发送完全渲染的 HTML。
- 浏览器立即显示此 HTML。
- JavaScript 加载并*水合*页面，添加交互性。

```javascript
// Simplified React hydration example
import { hydrateRoot } from 'react-dom/client';
import App from './App';
const domNode = document.getElementById('root');
hydrateRoot(domNode, <App />);
```

此过程允许快速初始加载，同时仍提供现代 Web 应用的丰富交互性。

请记住，虽然 SSR 提供了这些完全渲染的页面，但它并非没有权衡。服务器的工作量更大，您需要仔细处理服务器和客户端之间的状态。但是，对于许多应用程序而言，完全渲染页面的好处使 SSR 成为一个引人注目的选择。

客户端渲染 (CSR) 和服务器端渲染 (SSR) 是渲染网页的两种不同方法。以下是它们主要区别的细分：

| 特性          | 客户端渲染 (CSR)                                     | 服务器端渲染 (SSR)                                     |
|---------------|------------------------------------------------------|------------------------------------------------------|
| 服务器发送     | 包含 JavaScript 包的最小 HTML 文件                    | 完整的 HTML 内容                                       |
| 浏览器行为     | 下载并运行 JavaScript，创建页面内容并使其具有交互性 | 快速接收并显示预渲染的 HTML，然后加载 JavaScript 以使页面完全具有交互性 |
| 优点           | 初始加载后的流畅交互；需要更少的服务器资源           | 初始页面加载速度更快；更利于 SEO；在速度较慢的设备上运行良好 |
| 缺点           | 初始页面加载速度较慢；潜在的 SEO 挑战                 | 设置可能更复杂；可能使用更多服务器资源             |


这是一个简单的视觉比较：

本质上，CSR 在浏览器中运行更多，而 SSR 在服务器上运行更多。它们之间的选择取决于项目的特定需求，平衡初始加载时间、SEO 要求和服务器资源等因素。

服务器端渲染会对搜索引擎查看您网站的方式产生重大影响。让我们分解一下：

- 更快的索引

**框架无关性**: Builder.io 支持各种支持 SSR 和 SSG 的框架。**自动优化**: Builder 会优化您的内容性能，包括代码分割和屏幕外组件的延迟加载。**动态渲染**: 您可以根据用户属性或[A/B 测试](https://www.builder.io/c/docs/abtesting)渲染不同的内容，同时保持[SEO 优势](https://www.builder.io/m/explainers/seo-core-web-vitals)。**轻松集成**: Builder 提供[SDK 和文档](https://www.builder.io/c/docs/sdk-comparison)，以便无缝集成您的现有项目。

以下是如何使用[Builder 和 Next.js](https://www.builder.io/c/docs/custom-components-ssr-ssg)在服务器端获取和渲染内容的基本示例：

```javascript
import { builder, BuilderComponent } from '@builder.io/react'
builder.init('YOUR_API_KEY')
export async function getStaticProps({ params }) {
  const page = await builder
    .get('page', {
      userAttributes: {
        urlPath: '/' + (params?.page?.join('/') || '')
      }
    })
    .toPromise()
  return {
    props: {
      page: page || null,
    },
    revalidate: 5
  }
}
export default function Page({ page }) {
  return (
    <BuilderComponent
      model="page"
      content={page}
    />
  )
}
```

- 确保您正在使用支持 SSR 或 SSG 的框架。
- 集成 Builder 页面或区块时，请遵循框架的服务器端数据获取指南。
- 有关处理服务器端数据的更多信息，请参阅`getAsyncProps`自述文件。

通过利用 Builder 进行 SSR，您可以将[无头 CMS](https://www.builder.io/headless-cms) 的灵活性和服务器端渲染的性能优势相结合，同时保持易于使用的[可视化编辑](https://www.builder.io/m/knowledge-center/visual-editing)体验。

服务器端渲染 (SSR) 是一种强大的 Web 开发方法，可以显著提高应用程序的性能、SEO 和用户体验。在本文中，我们探讨了 SSR 的含义、它与客户端渲染的不同之处、它对搜索引擎的影响以及使用[Next.js](https://www.builder.io/m/nextjs-cms) 等流行框架的实际实施策略。

我们还讨论了完全渲染页面的概念，并检查了不同生态系统中的各种 SSR 解决方案。虽然 SSR 提供了许多好处，但在决定是否实施它时，务必考虑项目的具体需求。

**问：SSR 如何影响我的开发工作流程？**
答：SSR 可能会使开发变得更加复杂，因为您需要同时考虑服务器和客户端环境。您可能需要调整构建过程并注意特定于浏览器的 API。

**问：SSR 如何影响我网站的交互时间 (TTI)？**
答：虽然 SSR 可以提高初始内容可见性，但它可能会稍微延迟 TTI，因为浏览器需要在收到初始 HTML 后加载和水化 JavaScript。

**问：SSR 有哪些特定的安全注意事项？**
答：是的，使用 SSR 时，您需要更加小心地保护服务器端敏感数据或 API。始终清理用户输入，并注意在初始渲染中包含哪些数据。

**问：SSR 如何与身份验证和个性化内容一起使用？**
答：SSR 可以与身份验证一起使用，但这需要仔细处理。您可能需要实现 JWT 令牌或服务器端会话等技术来管理经过身份验证的 SSR 请求。