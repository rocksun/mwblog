# 如何精通 JavaScript 性能优化

![关于如何精通 JavaScript 性能优化的特色图片](https://cdn.thenewstack.io/media/2024/07/7e117b67-vaibhav-nagare-tyorfzqokxg-unsplash-1024x576.jpg)

JavaScript 是现代 Web 应用程序的基石，为从动态内容到交互式功能的一切提供支持。然而，随着应用程序变得越来越复杂，确保 JavaScript 能够高效运行变得至关重要。

随着用户对更快、更具响应性的应用程序的需求不断增长，开发人员必须优先考虑 JavaScript 优化以满足这些期望。从减少加载时间到提高交互性，[优化您的 JavaScript](https://developer.mozilla.org/en-US/docs/Learn/Performance/JavaScript) 可以显著提高 Web 应用程序的整体性能。

## 为什么优化 JavaScript 的性能

正确理解网站的性能是优化 JavaScript 代码的第一步。

考虑到这一点，衡量您的网站或应用程序的性能至关重要，因为它可以帮助您识别影响下载时间、渲染速度和整体用户体验的瓶颈。

如果没有[对性能进行适当的衡量](https://thenewstack.io/4-ways-to-measure-your-software-delivery-performance/)，您可能会浪费时间应用优化，而这些优化并不能解决您的网站所面临的实际问题。

### 分析性能数据

有几种工具可以帮助您有效地衡量性能。内置的浏览器工具，例如 Chrome DevTools，[提供关于网络活动、加载时间和 CPU 使用率的全面而有价值的见解](https://developer.chrome.com/docs/devtools/console/understand-messages)。

收集完性能数据后，下一步是确定哪些优化是必要的。

这些工具可以让您看到页面中哪些部分加载时间最长，以及哪些脚本可能会减慢网站速度。除此之外，性能 API 还可以提供更复杂的数据，用于深入分析。

收集完性能数据后，下一步是确定哪些优化是必要的。并非每种技术都适合每个项目，因此根据您网站的具体需求进行优先排序非常重要。

例如，如果您的分析表明事件处理程序会导致延迟，您可以专注于改进事件管理。类似地，如果大型 JavaScript 文件会减慢加载时间，缩小和异步加载可能是正确的解决方案。

此外，它还可以帮助您[遵守 GDPR](https://upsun.com/blog/gdpr-compliance-everywhere/)，或与您的网站或应用程序相关的欧盟、美国或其他地方的任何数据保护法规。优化您的 JavaScript 有助于提高性能，同时确保您的数据处理实践符合标准。

正确管理的代码可以帮助最大限度地减少不必要数据的收集，从而简化尝试遵守和遵循重要监管要求的过程。

## 优化 JavaScript 性能的挑战

我们都经历过：如果您的代码没有得到妥善管理，JavaScript 有时会成为一个真正的头痛问题。

您可能遇到的[一些常见问题](https://thenewstack.io/too-much-javascript-why-the-frontend-needs-to-build-better/)包括质量较差的事件处理，这会导致深层调用堆栈和更慢的性能。无序的代码是另一个大问题，会导致资源分配效率低下，并使浏览器更难快速执行脚本。

代码拆分允许您将 JavaScript 代码分解成更小、更易于管理的块。

然后是[过度依赖的问题](https://thenewstack.io/a-guide-to-software-dependencies/)，这会减慢应用程序的速度，通常会显著减慢速度，尤其是对于带宽有限的移动用户而言——而且不要忘记，低效的迭代会不必要地拖延处理时间。

### 理解和实现代码拆分

代码拆分允许您将 JavaScript 代码分解成更小、更易于管理的块——这在您的应用程序变得越来越复杂时至关重要，有助于减少加载时间并提高用户的初始渲染速度。

那么，如何进行代码拆分呢？一种常用的方法是使用动态导入，它允许您[仅在需要时加载 JavaScript 模块](https://thenewstack.io/5-ways-javascript-is-improving-modules-for-developers/)，而不是一次性将整个应用程序加载到用户身上。这就像只为周末旅行打包必需品，而不是打包整个衣橱。
根据最近的调查统计，[48.9% 的开发人员已采用动态导入按需加载模块](https://marketsplash.com/javascript-statistics/)，[45.7% 的开发人员正在使用服务工作者](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers) 来增强离线用户体验。

同样，对于 JS 库也是如此，允许进行各种应用内操作，例如[在 React 应用中查看文档](http://apryse.com/blog/webviewer/how-view-documents-in-a-react-app)，动态[在实时分析仪表板中渲染图表](https://stackoverflow.com/questions/44248930/how-to-get-realtime-data)，或加载交互式地图以用于基于位置的服务。然后是 webpack，一个工具，一旦你掌握了它，就会感觉有点像魔法；它可以[自动将你的代码拆分成更小的块](https://thenewstack.io/airbnb-moves-from-webpack-to-metro-enjoys-shorter-build-times/)，按需加载它们。

### 如何实现代码拆分
-
**动态导入**: 使用`import()`
函数在需要时加载模块。例如：
```javascript
import('./module.js').then(module => {
  module.doSomething();
});
```
**Webpack 配置**: 配置 webpack 使用`SplitChunksPlugin`
和`optimization.splitChunksoptions`
自动将代码拆分成更小的块。
.**React.lazy**: 在 React 应用中，使用`React.lazy`
进行组件级代码拆分：
```javascript
const MyComponent = React.lazy(() => import('./MyComponent'));
```
### 实现延迟加载以提高性能
延迟加载是一种很棒的技术，可以通过延迟加载非必要资源来提高 Web 应用的性能，直到它们真正需要时才加载。

简而言之，延迟加载允许这些[元素仅在进入用户的视野时加载](https://www.hotjar.com/blog/importance-of-lazy-loading-content/)，而不是让用户等待每个图像、视频或媒体文件预先加载。

延迟加载最常见的用例包括图像、视频和其他媒体密集型内容等元素。使用延迟加载可以大幅减少初始加载时间，从而增强网站或应用的整体用户体验。

实现延迟加载的一种流行方法是通过 Intersection Observer API。这个特定的 API 允许你[检测元素何时进入或退出视窗](https://stackoverflow.com/questions/53306419/intersection-observer-when-element-leaves-the-viewport)，因此你可以在内容即将对用户可见时才加载它。它效率高且设置起来相对容易。

### 如何实现延迟加载
**Intersection Observer API**: 检测元素何时进入视窗并动态加载内容：
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      loadImage(entry.target);
      observer.unobserve(entry.target);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => observer.observe(img));
```
- 对于 React 开发人员，
`React.lazy`
函数是延迟加载组件的强大工具。使用`React.lazy`
，你可以[在组件级别拆分代码](https://legacy.reactjs.org/docs/code-splitting.html)，以便仅在需要时加载应用的必要部分。
### 利用 Web Workers 卸载繁重的计算
Web Workers 是现代 Web 开发中的一项强大功能，旨在帮助处理繁重的计算，而不会减慢用户界面。

Web Workers [从主线程卸载密集型任务](https://web.dev/learn/performance/web-worker-overview)，通过在后台线程中运行脚本，提供流畅且响应迅速的用户体验。

Web Workers 通过启用并行执行来显著提高性能；因此，当主线程处理用户交互和渲染时，Web Workers [负责后台的资源密集型操作](https://thenewstack.io/leveraging-web-workers-to-safely-store-access-tokens/)，例如数据处理和计算。这可以防止 UI 由于长时间运行的脚本而变得无响应。

使用 Web Workers 的一些更实际的示例包括卸载基本数据处理任务。例如，当处理需要排序、过滤或复杂计算的大型数据集时，Web Worker 可以管理这些操作，而不会冻结主 UI 线程。

### 如何利用 Web Workers
**创建 Web Worker**: 为工作者创建一个单独的 JavaScript 文件：
```javascript
// worker.js
self.onmessage = (e) => {
  const result = computeHeavyTask(e.data);
  postMessage(result);
};
```
**使用 Web Worker**: 从主线程实例化并与工作者通信：
```javascript
const worker = new Worker('worker.js');

worker.onmessage = (e) => {
  console.log('Result from worker:', e.data);
};

worker.postMessage(data);
```
## JavaScript 优化的其他技术

### EDITOR'S RESPONSE
优化 JavaScript 不仅仅是代码分割和延迟加载，还有其他一些技术可以显著提高应用程序的性能。

异步加载允许脚本与其他资源并行获取。

一种重要的方法是 [压缩和压缩 JavaScript 文件](https://thenewstack.io/the-architects-guide-to-data-and-file-formats/)，这涉及从代码中删除不必要的字符和空格，而不会改变其功能。像 UglifyJS 这样的工具可以帮助完成此过程，使用 gzip 或 Brotli 压缩可以进一步减小文件大小，从而加快加载时间。

另一方面，异步加载允许脚本 [与其他资源并行获取](https://stackoverflow.com/questions/47344897/what-does-synchronous-vs-asynchronous-loading-mean)，防止它们阻塞页面的渲染。HTML 中的 `async` 属性通常用于此目的。

使用 `defer` 属性延迟脚本，确保 [代码在初始 HTML 解析后执行](https://stackoverflow.com/questions/51092203/how-to-execute-javascript-after-html-and-javascript-has-been-parsed-but-not-any)，这提高了用户与网站交互的速度。

利用 HTTP/2 和 JavaScript CDN 可以进一步提高网站或应用程序的性能。

HTTP/2 引入了多路复用等功能，允许多个请求同时通过单个连接发送，从而减少延迟。使用 [内容交付网络 (CDN) 为您的 JavaScript 文件提供服务](https://stackoverflow.com/questions/59182642/how-to-choose-a-cdn-to-load-javascript-css-libraries) 可以保证它们从更靠近用户的位置提供服务，从而加快交付速度。

## 提升您的 JavaScript 水平
代码分割、延迟加载、使用 Web Workers、压缩文件和利用异步加载等技术并不完全是秘密，但开发人员并没有充分利用它们——远非如此。

每种方法都可以提高应用程序的速度和响应能力，将它们纳入开发工作流程将提供更流畅的用户体验，并使您的应用程序保持领先地位。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)