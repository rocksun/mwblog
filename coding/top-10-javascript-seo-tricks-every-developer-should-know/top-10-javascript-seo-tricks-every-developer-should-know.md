
<!--
title: 每个开发人员都应该知道的10个JavaScript SEO技巧
cover: https://cdn.thenewstack.io/media/2024/11/af4b4d35-getty-images-6dnmfeeaht0-unsplashd.jpg
-->

前端开发人员应该了解的十个 JavaScript SEO 技巧，包括代码示例和实用指南。

> 译自 [Top 10 JavaScript SEO Tricks Every Developer Should Know](https://thenewstack.io/top-10-javascript-seo-tricks-every-developer-should-know/)，作者 Alexander T Williams。

JavaScript SEO 对于确保你的网络应用程序在提供丰富的用户体验的同时，被搜索引擎 [发现](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) 至关重要。

虽然 [JavaScript 框架](https://thenewstack.io/javascript-framework-maintainers-on-unification-potential/) 提供了动态功能，但如果搜索引擎无法正确解释你的 JS 内容，你就有可能失去可见性和流量。Google 等搜索引擎可以在一定程度上执行 JavaScript——尽管如此，仅仅依赖它们的能力是有风险的。

因此，你需要确保你的网站在利用 JavaScript 获得最佳用户体验的同时，仍然保持对 SEO 的友好性。以下是每个开发者都应该了解的十个 JavaScript SEO 技巧，并附有代码示例和实用指南。

## 1. 服务器端渲染 (SSR) 和静态渲染

JavaScript 密集型网站经常面临挑战，[因为搜索引擎难以有效执行客户端 JavaScript](https://seobase.com/java-script-seo-challenges-and-solutions-for-indexing-and-ranking)。当内容严重依赖于客户端 JavaScript 时，抓取器可能看不到最终呈现的页面，从而导致索引不完整或不正确。[SSR 和静态渲染可以通过预渲染内容来提高搜索引擎抓取器索引页面的能力](https://stackoverflow.com/questions/67789864/what-does-rendering-mean-in-the-context-of-server-side-rendering)。

服务器端渲染是指在将网页发送给客户端之前在服务器上渲染网页，[而静态渲染涉及在构建时生成 HTML](https://stackoverflow.com/questions/75457090/static-site-generation-ssg-vs-server-side-rendering-vs-client-side-rendering)。这两种方法都使内容在不依赖于客户端 JavaScript 执行的情况下立即可供搜索引擎使用。

**Next.js 示例：**

```
// pages/index.js
import React from 'react';
 
const Home = ({ data }) => (
  <div>
    <h1>{data.title}</h1>
    <p>{data.description}</p>
  </div>
);
 
export async function getServerSideProps() {
  // Fetch data at runtime
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
 
  return { props: { data } };
}
 
export default Home;
```

在这个示例中，Next.js 在运行时获取数据并在服务器上预渲染页面，使搜索引擎更容易抓取内容。SSR 确保将完整的 HTML 发送给客户端，从而显著改善 SEO——尤其是对于内容繁重的网站。

## 2. 使用 rel=”canonical” 来防止重复内容问题

JavaScript 框架[有时会生成同一页面的多个版本](https://softwareengineering.stackexchange.com/questions/142313/support-multiple-frameworks-in-a-javascript-library)，这可能会让搜索引擎感到困惑。当 URL 因参数、过滤器或用户导航状态而异时，这种情况尤其常见。重复的页面会导致排名信号稀释，其中一个页面的多个版本在搜索结果中相互竞争。

为了避免这种情况，请使用 rel="canonical" 标签[来指示页面的首选版本](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)。这有助于合并所有信号，并告诉搜索引擎在搜索结果中优先考虑哪个版本。

**示例：**

```
<head>
  <link rel="canonical" href="https://www.example.com/original-page" />
</head>
```

添加此标签有助于[将重复的 URL 合并到一个权威页面中](https://stackoverflow.com/questions/71770978/consolidate-duplicate-urls)，确保你不会因为错误的重复信号而分散页面之间的排名信号。如果不这样做，你建立的任何高权威反向链接都将因错误的重复信号而徒劳无功。因此，你必须始终查看你的 JavaScript 驱动的 URL，以识别任何潜在的重复项并相应地设置规范标签。

## 3. 谨慎处理客户端路由

React Router 等客户端路由框架便于创建动态[单页应用程序](https://thenewstack.io/spas-and-react-you-dont-always-need-server-side-rendering/) (SPA)。但是，不正确的实现会导致抓取问题。如果未使用正确的链接或内容加载不正确，搜索引擎可能会难以处理客户端路由。

在处理客户端路由时，确保可以通过内部链接访问内容，并且 history.pushState() 是[用于更新 URL 而无需重新加载整个页面](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState)确保使用适当的链接元素有助于搜索引擎正确理解和索引内容。

**使用 React 路由的解决方案：**

```ts
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
 
function App() {
  return (
    <Router>
      <nav>
        <Link to="/about">About Us</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <Route path="/about" component={About} />
      <Route path="/contact" component={Contact} />
    </Router>
  );
}
```

确保内部链接始终是 Link 组件[而不是通过 JavaScript 操作的动态生成的 <a> 标签](https://stackoverflow.com/questions/71543906/how-to-select-and-manipulate-the-dynamically-created-html-element-with-javascrip)。这可确保搜索引擎可以抓取和索引您的内容，而不会出现问题。

## 4. 明智地使用延迟加载

延迟加载是一种出色的技术，可以通过推迟加载非必要内容，直到需要时才加载，从而
[提高页面加载速度和整体性能](https://thenewstack.io/how-to-master-javascript-performance-optimization/)。但是，如果延迟加载未正确实施，则会对 SEO 产生负面影响。如果加载得太晚或搜索引擎无法触发加载它的必需 JavaScript，则搜索引擎可能无法索引重要内容。

为了确保索引关键内容，您应始终优先考虑视口上方内容，并考虑为延迟加载的元素提供后备。使用 Intersection Observer API 有助于高效加载图像，同时不影响 SEO。

**使用 Intersection Observer 的示例：**

```
// Lazy loading images
const images = document.querySelectorAll('img[data-src]');
 
const imgObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      observer.unobserve(img);
    }
  });
});
 
images.forEach(img => {
  imgObserver.observe(img);
});
```

确保关键图像（如视口上方图像）立即加载，并测试实施以确认所有基本内容对搜索引擎可见。

## 5. 为重要页面预渲染 JavaScript

预渲染是一种有效的解决方案，可确保搜索引擎可以访问 JavaScript 密集型页面。当内容隐藏在复杂的 JavaScript 交互或登录屏幕后面时，预渲染服务可以提供一个静态 HTML 快照，搜索引擎可以轻松地对其进行索引。

使用 Prerender.io 或 Rendertron 等服务可以帮助使您的 JavaScript 内容更适合搜索引擎。这些服务充当中间件，为抓取器生成静态 HTML 页面，同时仍为用户提供动态体验。

**使用 Express 设置：**

```
const express = require('express');
const prerender = require('prerender-node');
 
const app = express();
app.use(prerender.set('prerenderToken', 'YOUR_TOKEN_HERE'));
 
app.get('/', (req, res) => {
  res.send('Hello World!');
});
 
app.listen(3000);
```

此设置会为搜索引擎预渲染您的 JavaScript 页面，确保它们可以在不执行 JavaScript 的情况下索引内容。对于通过正常抓取无法轻松访问其基本内容的页面，应考虑预渲染。

## 6. 动态使用元标记进行社交分享和 SEO

标题和描述等元标记[在 SEO 和社交分享中扮演着重要角色](https://www.conductor.com/academy/what-are-meta-tags/)。它们帮助搜索引擎理解页面内容，并且当页面出现在搜索结果中时，它们可以影响点击率。对于 JavaScript 驱动的网站，必须动态呈现这些标记以反映内容。

在使用[人工智能进行潜在客户生成](https://www.artisan.co/blog/ai-lead-generation)或实施任何其他类型的自动化时，这一点尤其重要。

使用 react-helmet 等工具[使开发人员能够根据内容动态更新元标记](https://www.freecodecamp.org/news/react-helmet-examples/)。这可确保搜索引擎和社交媒体平台接收准确且经过优化的元数据，从而获得更好的排名和提高分享率。

**使用 React Helmet 的动态元标记：**

```
import { Helmet } from 'react-helmet';

function BlogPost({ title, description }) {
  return (
    <div>
      <Helmet>
        <title>{title}</title>
        <meta name="description" content={description} />
      </Helmet>
      <h1>{title}</h1>
      <p>{description}</p>
    </div>
  );
}
```

使用 react-helmet 允许您动态设置元数据，这有助于搜索引擎和社交平台理解您的页面内容。为了最大化 SEO 收益，请确保所有页面都有适当且唯一的标题和描述。

## 7. 避免使用 robots.txt 阻止 JavaScript

在 robots.txt 中阻止 JavaScript 文件[阻止搜索引擎抓取器访问这些脚本](https://support.google.com/webmasters/thread/198126075/js-file-blocked-by-robots-txt?hl=en)，这会严重损害您网站的可见性。搜索引擎需要访问您的 JavaScript，以了解您的网页如何构建以及内容如何呈现。

不要阻止 JavaScript 资源，而应使用配置良好的 robots.txt 文件，确保限制敏感区域，同时让抓取器可以访问基本资源。

**安全的 robots.txt 配置示例：**

```
User-agent: *
Disallow: /private/
Allow: /js/
```

通过允许访问 JavaScript 目录，您可以[确保搜索引擎可以正确呈现您的网页](https://www.conductor.com/academy/javascript-seo/)。定期审核您的 robots.txt，以验证重要的资源不会被无意中阻止。

## 8. 实施面包屑导航以提高可抓取性

面包屑导航[通过提供清晰的链接路径来改善用户和搜索引擎的导航](https://yoast.com/breadcrumbs-seo/)。Google 在搜索结果中显示面包屑导航，这可以通过为用户提供更多上下文来提高点击率。

实施结构化数据（例如 JSON-LD）[有助于搜索引擎解释您的面包屑导航](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)并提高其在 SERP 中的可见性。

**JSON-LD 示例：**

```js
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://www.example.com/blog"
    }
  ]
}
</script>
```

添加 JSON-LD 等结构化数据有助于 Google 了解您网站的内容层次结构（[以及 AI API](https://thenewstack.io/better-llm-integration-with-content-centric-knowledge-graphs/)），使其更易于索引并增强整体用户体验。面包屑导航还可以通过让用户轻松浏览您的网站来降低跳出率。

## 9. 通过最小化 JavaScript 复杂性来管理抓取预算

抓取预算是指搜索引擎在给定时间范围内将在您的网站上抓取的页面数。繁重的 JavaScript 和不必要的脚本会消耗您的抓取预算，导致抓取和索引的页面减少。

要[提高抓取效率](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget)，请最小化 JavaScript 的复杂性，并在页面加载期间避免不必要的外部 API 调用。保持 JavaScript 占用空间较小，以确保页面加载更快，以便搜索引擎可以抓取更多内容。

**提示：** 

- [在初始页面上最小化 API 调用](https://softwareengineering.stackexchange.com/questions/188881/how-to-optimize-calls-to-multiple-apis-at-once-and-return-as-one-set)加载以避免延迟。
- 使用关键 CSS 和内联基本 JS 来减少依赖并提高加载速度。
- 使用 Lighthouse 等工具审核您的 JavaScript，以识别和修复可能阻碍抓取器的性能问题。

示例：在页面加载期间删除不必要的 API 调用

```js
function loadData() {
  if (!sessionStorage.getItem('dataLoaded')) {
	fetch('https://api.example.com/data')
  	.then(response => response.json())
  	.then(data => {
    	// Process data
    	console.log(data);
    	sessionStorage.setItem('dataLoaded', true);
  	})
  	.catch(error => console.error('Error fetching data:', error));
  }
}
 
document.addEventListener('DOMContentLoaded', loadData);
```

在此示例中，通过使用 sessionStorage 在页面重新加载之间存储数据，将不必要的 API 调用最小化。这种方法减少了在初始页面加载期间进行的 API 调用次数，从而优化了抓取预算并提高了页面加载速度。

## 10. 使用 window.history.replaceState() 保持 URL 清晰

SPA 可能会导致带有查询字符串或片段 (#) 的 URL，这可能不太利于 SEO。使用 window.history.replaceState()[允许您维护清晰、有意义的 URL](https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState)，而无需触发全页面重新加载。

清晰的 URL 更容易让用户记住和分享，它们还有助于搜索引擎更好地理解页面内容。使用
replaceState() 确保 URL 反映内容，使搜索引擎更容易正确抓取和索引。

**示例：**

```js
// Clean up URL after loading dynamic content
window.history.replaceState(null, 'New Page Title', '/new-url-path');
```

此函数在不重新加载页面的情况下更新地址栏中的 URL，使您的 URL 更易于用户使用，并确保它们与显示的内容保持一致。

## 结论

JS 的力量应该以不妨碍搜索引擎访问和索引您的内容的方式加以利用。通过我们概述的这些 JS SEO 技巧，您将增强内容的可发现性，确保您的应用程序对爬虫友好，并最终提高搜索引擎排名。

无论您是在优化客户端渲染、管理抓取预算还是确保元标记设置正确，这些技巧中的每一个都是 JavaScript SEO 拼图的关键部分。关键是要确保搜索引擎和用户都可以轻松访问您网站的宝贵内容。没有必要忽视其中一个或另一个，对吧？