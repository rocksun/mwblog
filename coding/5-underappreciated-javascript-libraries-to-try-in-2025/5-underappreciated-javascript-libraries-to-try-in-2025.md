
<!--
title: 2025年，5个不应被忽视的JavaScript库
cover: https://cdn.thenewstack.io/media/2025/07/e5be971a-allison-saeng-dss28vqcxaa-unsplashb.jpg
summary: 文章介绍了五个值得关注的 JavaScript 库：Valtio (简化状态管理), Htmx (无需 JS 的动态界面), Tippy.js (tooltip 库), Day.js (轻量级日期处理), Comlink (简化 Web Workers)。它们专注解决特定问题，提高生产力。
-->

文章介绍了五个值得关注的 JavaScript 库：Valtio (简化状态管理), Htmx (无需 JS 的动态界面), Tippy.js (tooltip 库), Day.js (轻量级日期处理), Comlink (简化 Web Workers)。它们专注解决特定问题，提高生产力。

> 译自：[5 Underappreciated JavaScript Libraries To Try in 2025](https://thenewstack.io/5-underappreciated-javascript-libraries-to-try-in-2025/)
> 
> 作者：Alexander T. Williams

JavaScript [不仅仅是关于框架了](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/)。虽然 React、Vue 和 Svelte 占据了头条，但生态系统悄然涌现出一些小型、精巧的工具，专门解决非常具体的问题——而且通常比那些庞然大物做得更好。这些库可能不会在 X 上成为热门话题，也不会出现在贵公司的技术雷达中，但它们可以显著提高你的生产力、代码质量和心智健全。

这不是你常见的那些半死不活的 npm 包列表。这些都是经过深思熟虑精心设计的库，它们把一件事做到了极致，你会后悔没有早点发现它们。

让我们深入了解一下 2025 年值得你关注的五个未被充分赏识的 JavaScript 库。

## 1. Valtio：简化的 React 状态管理

React 中的状态管理一直是一个战场。在 Redux 的样板代码、context 的滥用以及 MobX 的复杂性之间，开发者们渴望更精简的东西。Valtio 由此应运而生。

Valtio 是一个基于 Proxy 的状态管理器，它允许你使用普通的 JavaScript 对象作为状态。无需将状态包装在 reducer、action 或 provider 中，你只需像在原生 JS 中那样修改状态——Valtio 使其具有响应性。

```js
import { proxy, useSnapshot } from 'valtio';


const state = proxy({ count: 0 });


function Counter() {
  const snap = useSnapshot(state);
  return (
    <div>
      <p>{snap.count}</p>
      <button onClick={() => ++state.count}>Increment</button>
    </div>
  );
}
```

这开箱即用，无需任何仪式。在底层，Valtio [使用 ES6 的 Proxy 来跟踪更改](https://thenewstack.io/mastering-javascript-proxies-and-reflect-for-real-world-use/)，并且只有访问这些属性的组件才会重新渲染。没有选择器，没有 action，也没有 reducer 的狗血剧情。

Valtio 脱颖而出，不仅因为它优雅的设计，还因为它与不断发展的 React 生态系统保持一致。随着 React 过渡到 [服务端组件](https://thenewstack.io/react-server-components-in-a-nutshell/) 并采用更简单、更直接的思维模型，Valtio 提供了一个干净的抽象层，为未来做好准备。它可以与其他现代工具干净地集成，并且可以很好地与 Suspense、并发渲染甚至 [服务端渲染 (SSR)](https://thenewstack.io/web-development-trends-in-2024-a-shift-back-to-simplicity/) 场景配合使用。

## 2. Htmx：重新构想前端，摆脱 JavaScript 臃肿

在一个痴迷于 SPA 的世界里，htmx 悄然地 [对 JavaScript 的过度使用发起了战争](https://news.ycombinator.com/item?id=40015612)。它的前提优雅而激进：[HTML 已经足够了](https://thenewstack.io/htmx-html-approach-to-interactivity-in-a-javascript-world/)。

Htmx 让你仅使用 HTML 属性即可创建 [动态、响应式的界面](https://docs.ckan.org/en/latest/theming/htmx.html)。你可以发出 Ajax 请求、渲染局部内容、交换内容，甚至处理 WebSockets —— 所有这些都无需编写一行 JavaScript 代码。

```html
<button hx-get="/clicked" hx-target="#result" hx-swap="innerHTML">
  Click me
</button>
<div id="result"></div>
```

服务器返回一个 HTML 片段，htmx 会精准地替换你所需要的部分。结果感觉就像一个实时的 SPA，但你避免了 hydration 问题、巨大的 JS 包或状态同步的噩梦。

htmx 更加令人兴奋的是它与 2025 年的架构趋势的契合程度。[随着边缘渲染的兴起](https://thenewstack.io/why-devs-must-rethink-their-role-in-modern-cdns-and-the-edge/)，服务端逻辑正在卷土重来。开发人员希望构建快速、可缓存且易于维护的应用程序，而无需将整个前端 [交给一个复杂的框架](https://latitude.so/blog/expressjs-react-server-side-cache/)。Htmx 让你拥有这种控制权，让服务器掌控一切。

另一个引人注目的用例是升级遗留应用程序。与其用 React 或 Angular 重写整个前端，不如逐步增强应用程序的各个部分。这使得 htmx 成为现代化旧系统的理想选择，[尤其是在将页面拆分为模块化、服务器渲染的组件时](https://docs.apryse.com/web/guides/features/manipulation/split)，这些组件可以独立更新。引入 htmx，添加一些属性，突然之间，你的旧表单无需完全刷新页面即可重新加载。这就像让你的后端应用程序重获新生，而无需冒着完全重写的风险。

## 3. Tippy.js：你希望自己编写的 Tooltip 库

[Tooltips](https://en.wikipedia.org/wiki/Tooltip)（当用户将鼠标悬停在网页上的元素上时显示的简短消息）具有欺骗性的复杂性。定位、可访问性、过渡、视口感知 —— 它们都很麻烦。[Tippy.js](https://atomiks.github.io/tippyjs/) 将所有这些抽象成一个健壮、优雅且开箱即用的软件包。

Tippy 构建在 Popper.js 之上，只需最少的配置和最高的润色，即可轻松添加 tooltips、下拉菜单和 popovers。

```js
tippy('#button', {
  content: 'Tooltip content',
});
```

它支持从交互式内容和延迟渲染到动态放置、动画甚至用于完全控制的无头模式的所有内容。该 API 直观，并且即使没有额外的 CSS 争论，输出看起来也很专业。

Tippy.js 不仅仅是一个实用程序，它还是一个用于经常被忽略的界面细节的框架。你可以定义自定义主题，在 tooltip 中嵌入表单或小部件，并以编程方式控制显示/隐藏行为。它确保跨设备的无缝 UX，具有键盘导航、焦点锁定 [和预先配置的 ARIA 角色](https://atomiks.github.io/tippyjs/v6/all-props/)。

随着企业团队现在优先考虑可访问性和设计系统，Tippy.js 几乎已成为必需品。它足够强大，可以用于生产环境，但又足够轻量级，可以用于业余项目。简而言之，它是你在开始使用之前都不知道自己需要的 tooltip 解决方案。

## 4. Day.js：Moment.js，减去累赘

Moment.js 可能已经统治日期/时间领域多年，但现在是 2025 年，你应该拥有更好的选择。[Day.js](https://day.js.org/) 正是如此。它 [模仿 Moment 的 API](https://corner.buka.sh/mastering-day-js-a-comprehensive-guide-to-effortless-date-and-time-management/)（但 gzip 压缩后只有 2KB），并且它是不可变的和可链式的。

Day.js 的精妙之处在于对现代化的熟悉。如果你编写过 Moment.js 代码，则可以在几分钟内迁移：

```
dayjs().add(1, 'day').format('YYYY-MM-DD');
```

它支持用于时区处理、高级格式化、持续时间解析和相对时间的插件。你只需包含你需要的内容，这可以保持包的精简。

Day.js 已成为微服务、serverless 函数甚至 Jamstack 站点的首选。它对 ISO 字符串、Unix 时间戳和自定义解析逻辑的支持使其在后端和前端都非常有用。

与 Moment 不同，Day.js 拥抱 tree-shaking 和现代导入策略。虽然 [Luxon](https://moment.github.io/luxon/) 是一个有效的替代方案，但 Day.js 在简单性和大小方面胜出。

在一个性能至关重要且日期逻辑不可避免的 Web 中，Day.js 是 [你工具箱中的明智之举](https://www.geeksforgeeks.org/javascript/how-to-use-the-dayjs-library-to-work-with-date-time-in-javascript/)。无论你是在记录事件、安排任务还是构建完整的日历视图，Day.js 都能让你保持敏捷和高性能。

## 5. Comlink：让 Web Workers 再次可用

Web Workers 功能强大但未被充分利用 —— 不是因为它们无关紧要，而是因为 API 很痛苦。[Comlink](https://github.com/GoogleChromeLabs/comlink) 改变了这一点。

Comlink 由 Google 创建，它抽象了 postMessage 的样板代码，并将 [workers 转换为异步函数调用](https://github.com/GoogleChromeLabs/comlink/issues/635)。你可以编写感觉同步的代码，即使它在单独的线程中运行。

```js
// main.js
import { wrap } from 'comlink';
const worker = new Worker('worker.js');
const api = wrap(worker);


const result = await api.heavyComputation();
// worker.js
import { expose } from 'comlink';


const heavyComputation = () => {
  // expensive operation
  return 42;
};


expose({ heavyComputation });
```

这使得多线程变得易于访问，无需回调或状态体操。对于处理图像处理、实时计算或大数据转换的应用程序，Comlink 将 [痛苦的工程转化为简单的函数调用](https://thenewstack.io/javascript-kung-fu-elegant-techniques-to-master-the-language/)。

在 2025 年，当高分辨率画布图形、AI 模型推理和密集型音频/视频处理迁移到浏览器时，Comlink 充当了一条生命线。它让前端开发人员可以使用多核硬件，而无需成为并发专家。

## 重要的弱者

在一个充斥着热门观点和过度炒作框架的 JavaScript 世界中，这些库代表了一场更安静的革命。它们没有重新发明轮子，而是完善了它。无论你是在构建创业公司的 MVP 还是在优化企业巨头，这些工具都可以节省你开发周期中的时间并减少精神负担。

2025 年将成为专注于做好一件事的极简库的一年。这五个库非常符合这一要求。不要只是将它们添加到书签，而是要使用它们。未来的你会感谢你的。