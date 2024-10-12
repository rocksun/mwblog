
<!--
title: 我如何构建我的博客
cover: https://www.joshwcomeau.com/images/og-how-i-built-my-blog-v2.png
-->

我最近发布了这个博客的全新版本，在这篇文章中，我将分享它的构建方式！我们将考察技术栈，看看所有部分是如何组合在一起的，并深入了解一些细节，看看它们是如何工作的。

> 译自 [How I Built My Blog • Josh W. Comeau](https://www.joshwcomeau.com/blog/how-i-built-my-blog-v2/)，作者 Josh W Comeau。


在过去的几个月里，我一直致力于这个博客的全新版本。几周前，我终于把它上线了！以下是新旧版本的对比：

![](https://www.joshwcomeau.com/images/how-i-built-my-blog-v2/blog-home-new-light.webp)

从设计角度来看，变化并不大；我认为它更加精致，但总体理念保持一致。大多数“有趣”的改变都在幕后，或者隐藏在细节中。在这篇博文中，我想分享一下新架构的构成，并深入探讨一些细节！

多年来，我的博客已经成为一个出乎意料的复杂应用程序。它包含超过*100,000行代码*，还不包括内容。迁移所有内容是一个大工程，但也非常有教育意义。我将分享我对这个博客中使用的所有新技术的真实想法。

如果你正在计划自己创建一个博客，或者正在考虑使用我正在使用的某些技术，希望这篇文章对你有所帮助！

## 技术栈

让我们先快速列出我的博客使用的主要技术：

- [Next.js](https://nextjs.org/) v15.0.0 (beta)
- [React](https://react.dev/) v19.0.0 (beta)
- [MDX](https://mdxjs.com/) v3.0.1
- [Linaria](https://linaria.dev/) v6.1.0
- [Shiki](https://shiki.style/) v1.17.7
- [Sandpack](https://sandpack.codesandbox.io/) v2.13.8
- [React Spring](https://react-spring.io/) v9.7.3
- [Framer Motion](https://www.framer.com/motion/) v11.2.10
- [MongoDB](https://www.mongodb.com/) v6.5.0
- [TypeScript](https://www.typescriptlang.org/) v5.6.2
- [PartyKit](https://www.partykit.io/) v0.0.108

这个列表看起来可能对一个博客来说有点过分，有些人问我为什么不选择更“轻量级”的替代方案。原因有几个：

1. 我所有的博文都是用 MDX 编写的，所以我需要一流的 MDX 支持。
2. 我的另一个主要项目，我的课程平台，使用 Next.js。我希望尽可能减少上下文切换的摩擦。
3. 我想更多地体验最新的 React 功能，比如服务器组件和操作。

如果不是因为原因 2 和 3，我可能会尝试一下 [Astro](https://astro.build/)。我一直对 [Remix](https://remix.run/) 感兴趣！我认为两者都是非常棒的选择。

> **Pages Router vs. App Router**
> 正如你所了解的，Next.js 最近推出了一款全新的路由系统：应用路由器。它彻底改变了 React 中的路由和渲染方式，这是由 React 和 Next.js 核心团队历经多年努力的结果。
> 
> 此博客的旧版本也是使用 Next.js 构建的，但它使用的是旧的页面路由器。而对于我的新博客，我专门使用了应用路由器。
> 
> 比较和对比这两种方法非常有趣。在这篇文章的后面，我将分享我对这个新方向的看法，以及在什么情况下迁移是有必要的。

## 内容管理

我使用 MDX 编写博文。对我来说，这可能是技术栈中最关键的部分。

如果你不熟悉 MDX，它本质上是 Markdown 和 JSX 的结合。你可以把它看作是 Markdown 的超集，它提供了一个额外的超能力：能够在内容中包含自定义 React 元素。

使用 MDX，我可以创建交互式小部件，并将它们直接放在博文中间，就像这样：

> JS 组件

这种能力对于我创建的内容类型至关重要。我不想被标准的 Markdown 元素集（链接、表格、列表……）所限制。使用 MDX，我可以*创建自己的元素*！它感觉比传统的 Markdown 或存储在 CMS 中的富文本内容强大得多。

你可能想知道：为什么不完全使用 React，而完全跳过 Markdown 部分？当我构建这个博客的第一个版本时，早在 2017 年，我正是这么做的。每篇博文都是一个 React 组件。这样做有两个问题：

1. 写作体验很糟糕。例如，必须将每个段落都用 `<p>` 包裹起来，很快就让人厌烦了。 
2. 无法将内容作为数据访问。例如，我无法获取最近更新的 10 篇博文的列表，因为每篇博文都是一段代码，而不是数据库记录或 JSON 对象。

MDX 解决这两个问题，而且没有真正牺牲任何东西。在编写博文时，我仍然拥有 React 的全部功能！

在工作流程方面，我直接在 VS Code 中编辑我的 MDX 文件，并将它们作为代码提交。文章元数据（例如标题、发布时间）在文件顶部的 frontmatter 中设置。这种方法有一些缺点（例如，我必须重新部署整个应用程序才能修复一个错别字），但我发现它对我来说是最简单的选择。

使用 MDX 和 Next.js 有多种方法。我使用的是 [next-mdx-remote](https://github.com/hashicorp/next-mdx-remote)，主要是因为我在我的课程平台上使用它，并且希望这两个项目尽可能相似。如果您使用 Next.js 构建一个全新的博客，那么可能值得尝试一下 [内置的 MDX 支持](https://nextjs.org/docs/pages/building-your-application/configuring/mdx)；它看起来更加直观。


> **从 MDX v1 迁移到 v3** 
> 
> 此博客的旧版本也使用 MDX，但它使用的是版本 1。作为博客重建的一部分，我借此机会更新到了最新版本 v3。
> 
> 老实说，迁移有时相当令人沮丧😅。在 v1 中“即可运行”的内容在 v2/v3 中不再受支持。在某些情况下，我能够通过安装 remark/rehype 插件来还原旧行为，但大多数时候我必须自己动手构建解决方案，或手动编辑 MDX 以匹配新格式。
> 
> 这最终成为一项相当艰巨的任务，有时还令人沮丧，因为我觉得新版本并没有改进。我更喜欢 v1 中做出的权衡。😬 
> 
> 也就是说，新版本中某些事情肯定更好，而我的大多数抱怨都是主观的/口味问题。MDX 仍然是我所知道的最适合创建交互式内容的解决方案。如果我现在启动一个全新的项目，我仍然会选择 MDX v3.*


## 样式和 CSS

我的旧博客使用 styled-components，这是一个 CSS-in-JS 库。正如我之前写过的，styled-components [与 React Server Components 不完全兼容](/react/css-in-rsc/)。因此，对于这个新博客，我已切换到 [Linaria](https://github.com/callstack/linaria)，通过 [next-with-linaria 集成](https://github.com/dlehmhus/next-with-linaria/)。

以下是它的样子：

```js
import { styled } from '@linaria/react';

const Wrapper = styled.div`
  background: red;
`;
```

Linaria 是一个很棒的工具。它提供了一个熟悉的 `styled`
API，但它不是在运行时发挥作用，而是 *编译成 CSS 模块*。这意味着没有 JS 运行时参与，因此它与 React Server Components 完全兼容！

现在，让 Linaria 与 Next 协同工作一直是一场艰苦的战斗。我遇到了一些奇怪的问题。例如，当我在一个文件中导入 React 但没有实际 *使用* 它时，我得到了这个令人费解的错误：


```bash
**EvalError: TextEncoder is not defined**
/node_modules/.pnpm/@wyw-in-js+transform@0.4.1_typescript@5.4.5/node_modules/@wyw-in-js/transform/lib/module.js:223
throw new EvalError(e.message, this.callstack.join('\n| '));
```

错误消息/堆栈跟踪并没有真正帮助，所以我通过向后遍历我的更改和/或删除随机内容来解决大多数问题，直到错误消失。幸运的是，我发现的所有问题都是一致且可预测的；它不是那种 *有时* 发生错误，或者只在生产环境中发生的事情。

一旦我了解了它的所有特性，它就变得非常顺利，尽管仍然存在一个重大问题。而且它与 Linaria 完全无关，它与 Next.js 处理 CSS 模块的方式有关。

这篇文章篇幅有限，无法详细介绍，但简单概括一下：Next.js “乐观地” 捆绑了来自无关路由的大量 CSS，以提高后续导航速度并保证正确的 CSS 顺序。例如，这篇博文加载了 245kb 的 CSS，但它只使用了 47kb。这两个数字都是完整的未压缩值。实际通过网络发送的数据量更小。有一个 [关于此问题的 Github 上的活跃讨论](https://github.com/vercel/next.js/discussions/70168)，听起来一些即将推出的配置选项可以改善这种情况。

**鉴于所有这些，我无法真正推荐 Linaria。** 它是一个很棒的工具，但它还没有经过足够的实战检验，对于大多数人/团队来说，它不是一个明智的选择。
我目前最兴奋的是 [Pigment CSS](https://mui.com/blog/introducing-pigment-css/)，这是一个由 Material UI 团队开发的零运行时 CSS-in-JS 工具。将来，它将成为他们流行的 MUI 组件库中使用的 CSS 库，这意味着它将很快成为最经过实战检验的 CSS 库之一。

现在还处于早期阶段，但一旦他们发布了 1.0 版本，我计划尝试切换。希望到那时，Next.js 已经修复了 CSS 模块的捆绑问题。🤞

> **为什么不用 Tailwind？**
> 
> 过去几年里，Tailwind 已经成为 React 应用程序中最流行的样式工具。当然，我可以通过切换到 Tailwind 来避免所有这些令人困惑的问题？
> 
> 有几个原因，说明这对我来说并不是一个正确的解决方案： 
> 
> - 我有大约 1500 个样式化组件，因此我需要一个提供简单迁移路径的工具。我不会手动重写数千行 CSS。
> - Tailwind 完全不支持代码拆分，这意味着你的整个应用使用了一个 CSS 文件，在每个路由中加载。因为每个声明都是其自己的重复使用类，这并不是大多数项目的巨大问题，但这取决于你如何使用 CSS。我倾向于对 CSS 变量进行大量自定义操作，这可能会造成问题。
> - 对我来说，使用 Tailwind 是一种令人沮丧的体验，我希望我参与的项目是有趣的。Tailwind 并不是我的菜。

[链接到此标题](#code-snippets-4)代码片段
由于自定义设计的语法主题，代码片段在新博客上的外观非常不同！以下是前后对比：

## 代码片段

在新的博客上，由于自定义设计的语法主题，代码片段看起来截然不同！这是一个对比：

如果您想在您的 IDE 中使用此主题，您可以下载 JSON 文件 ([dark](/themes/dark.json)，[light](/themes/light.json))。我还没有测试过，但它使用与 VSCode 和其他编辑器相同的语法，所以它 *应该* 可以工作。

[链接到此标题](#the-magic-of-static-5)静态的魔力
我使用的是 [Shiki](https://shiki.style) 来管理语法高亮。虽然不是专门为 React 构建的，但 Shiki 旨在在编译时工作，使其非常适合 React Server Components。*这令人惊讶地令人兴奋。*

在我的旧博客中，我使用的是 Prism，一个典型的客户端语法高亮库。由于所有代码都包含在 JavaScript 包中，因此必须做出一些牺牲：

- 我们必须对支持的语言数量非常保守，因为每增加一种语言都会给我们的包增加千字节。
- 语法高亮逻辑很精简，比 VS Code 等 IDE 中的语法高亮要简单得多。这使得主题创建者对最终结果的控制力降低，也意味着我们无法在 IDE 和 Prism 之间共享主题。
Prism 拥有最小的内置语言集，最终压缩并 gzip 后只有 [26kb](https://bundlephobia.com/package/prism-react-renderer@2.4.0)，对于一个语法高亮器来说非常小，但对于捆绑包来说仍然是一个相当大的补充。

Shiki 不会给 JavaScript 捆绑包增加任何大小，它使用与 VS Code 相同的行业标准 TextMate 语法，并且可以免费支持数十种语言。

这意味着当我想要包含一个 Haskell 代码片段时，就像我 [几年前在随机博客文章中](/career/clever-code-considered-harmful/) 所做的那样，它将被完全语法高亮：

```haskell
pe58 = n
where
a p q = scanl (+) p $ iterate (+ 8) q
b = [[x,y,z] | (x,(y,z)) <- zip (a 3 10) $ zip (a 5 12) (a 7 14)]
c = zip (scanl1 (+) . map (length . filter isPrime) $ b) (iterate (+ 4) 5)
[(n,_)] = take 1 $ dropWhile (\(_,(a,b)) -> 10*a > b) $ zip [3,5..] c
```
作为开发者，Shiki 使用起来非常愉快。它非常灵活且可扩展。例如，我创建了自己的“注释”逻辑，这样我就可以突出显示代码的特定行：

```javascript
function someRandomFunction() {
// 这两行被高亮显示！你可以从背景颜色和左侧的小凸起看出。
return 42;
}
```
在我的旧博客中，语法高亮对于 CSS-in-JS 无法正常工作。我的模板字符串会被视为标准字符串，而不是 JS 中注入的 CSS 代码：

使用 Shiki，我能够重用 [styled-components VSCode 扩展](https://marketplace.visualstudio.com/items?itemName=styled-components.vscode-styled-components) 提供的语法高亮逻辑。因此现在，我的 styled-components 被正确地高亮显示：

```javascript
const FunkyButton = styled.button`
position: absolute;
background: linear-gradient(
to bottom,
red,
gold
);
@media (min-width: 24rem) {
&:focus {
background: gold;
}
}
`;
export default FunkyButton;
```
尽管我非常喜欢 Shiki，但它确实有一些权衡。

由于它使用更强大的语法高亮引擎，因此它不像其他选项那样快。我最初使用标准的服务器端渲染而不是静态编译时 HTML 生成来“按需”渲染这些博客文章，但发现 Shiki 降低了速度，尤其是在包含多个代码片段的页面上。这个问题可以通过切换到静态生成或使用 HTTP 缓存来解决。

Shiki 也非常占用内存；我遇到了 [Node 内存不足](https://github.com/shikijs/shiki/issues/567) 的问题，不得不进行重构以确保我没有生成多个 Shiki 实例。

然而，最大的问题是，有时我需要在 *客户端* 上进行语法高亮。例如，在我的 [渐变生成器](/gradient-generator/) 中，代码片段会根据用户编辑阴影的方式而改变：

无法在编译时生成它，因为代码是动态的！

对于这些情况，我有一个 *第二个* Shiki 高亮器。它更轻量级，只支持少数几种语言。它没有包含在我的标准捆绑包中，我使用 [next/dynamic](https://nextjs.org/docs/pages/building-your-application/optimizing/lazy-loading) 对它进行延迟加载。由于语法高亮本身比较慢，我使用 [useDeferredValue](/react/use-deferred-value/) 来保持应用程序的其余部分快速运行。

最棘手的部分是我需要 *静态服务器组件* 以及 *动态客户端组件*，才能使 SSR 正确工作。在所有内容加载完毕后，我会在客户端秘密地在它们之间切换。

[链接到此标题](#code-playgrounds-6)代码游乐场
除了代码片段之外，我还拥有代码游乐场，类似 Codepen 的小编辑器：

代码游乐场
```javascript
import React from 'react';
import range from 'lodash.range';
import styles from './PrideFlag.module.css';
import { COLORS } from './constants';

function PrideFlag({
  variant = 'rainbow', // rainbow | rainbow-original | trans | pan
  width = 200,
  numOfColumns = 10,
  staggeredDelay = 100,
  billow = 2,
}) {
  const colors = COLORS[variant];
  const friendlyWidth = Math.round(width / numOfColumns) * numOfColumns;
  const firstColumnDelay = numOfColumns * staggeredDelay * -1;

  return (
    <div className={styles.flag} style={{ width: friendlyWidth }}>
      {range(numOfColumns).map((index) => (
        <div
          key={index}
          className={styles.column}
          style={{
            '--billow': index * billow + 'px',
            background: generateGradientString(colors),
            animationDelay: firstColumnDelay + index * staggeredDelay + 'ms',
          }}
        />
      ))}
    </div>
  );
}

function generateGradientString(colors) {
  const numOfColors = colors.length;
  const segmentHeight = 100 / numOfColors;
  const gradientStops = colors.map((color, index) => {
    const from = index * segmentHeight;
    const to = (index + 1) * segmentHeight;
    return `${color} ${from}% ${to}%`;
  });
  return `linear-gradient(to bottom, ${gradientStops.join(', ')})`;
}

export default PrideFlag;
```

从我的博客文章 [动画彩虹旗](/animation/pride-flags/) 中摘录。

对于 React 游乐场，我使用 [Sandpack](https://sandpack.codesandbox.io/)，这是一个由 CodeSandbox 团队创建的绝佳编辑器。我之前写过 [关于我如何使用 Sandpack](/react/next-level-playground/)，所有这些内容仍然相关。

对于静态 HTML/CSS 游乐场，我使用的是我自己对 [agneym's Playground](https://github.com/agneym/playground) 的修改版本。Sandpack *确实* 支持静态模板，但它们依赖于 Service Workers，而 Service Workers 有时会被浏览器隐私设置阻止，从而导致用户体验受损。

[链接到此标题](#interactive-widgets-7)交互式小部件
很多人问我如何在我的文章中构建像这样的交互式演示：

## 你确定吗？
此操作无法撤消。

从我的博客文章 [在 CSS 中设计漂亮的阴影](/css/designing-shadows/) 中摘录。

我从来不知道如何回答这个问题 😅。我没有使用任何特定的库或包，都是标准的 Web 开发内容。我构建了自己的可重用 `<Demo>`
组件，它提供了一个外壳和一套控件，我将它组合到每个单独的小部件中。

也就是说，有一些通用的工具可以提供帮助。我使用 [React Spring](https://www.react-spring.dev/) 以流畅、自然的方式在值之间平滑插值。我使用 [Framer Motion](https://www.framer.com/motion/) 进行布局动画。

拥有两个独立的动画库感觉很放纵，尤其是因为它们都不是很小 ([ 19.4kb](https://bundlephobia.com/package/@react-spring/web@9.7.4) 和 [ 44.6kb](https://bundlephobia.com/package/framer-motion@11.5.4)，分别)。我将 React Spring 作为核心库包含进来，并在需要时动态导入 Framer Motion。

说实话，Framer Motion 应该能够完成 React Spring 可以完成的所有事情，所以如果我必须选择一个“荒岛”动画库，那很可能是 Framer Motion。

[链接到此标题](#database-stuff-8)数据库内容
如果你在台式机上阅读本文，你可能在旁边看到了这个小家伙：

这是一个 *喜欢* 按钮！这有点傻……社交网络使用喜欢按钮来告知他们的算法哪些内容应该被展示。这个博客没有发现算法，所以它除了可爱之外没有任何作用。

每个访问者最多可以点击按钮 16 次，数据存储在 MongoDB 中。数据库记录看起来像这样：

```
{
"slug": "promises",
"categorySlug": "javascript",
"hits": 123456,
"likesByUser": {
"abc123": 16,
"def456": 4,
"ghi789": 16,
// ...
}
}
```
ID 是根据用户的 IP 地址生成的，使用一个秘密盐值进行哈希以保护匿名性。这个博客部署在 Vercel 上，Vercel 通过一个标题提供用户的 IP。

最初我使用在客户端生成的 ID 并存储在 localStorage 中，但传奇侦探 Jane Manchun Wong 向我展示了 [为什么这是一个坏主意](https://twitter.com/wongmjane/status/1232325459842482176)，她通过向 API 端点发送垃圾邮件并生成数万个喜欢来证明这一点。😅

我最喜欢 Next.js 的一件事是，你不需要单独的 Node.js 后端。喜欢帖子的逻辑是在 [路由处理程序](https://nextjs.org/docs/app/building-your-application/routing/route-handlers) 中处理的，它的功能几乎与 Express 端点完全相同。

[链接到此标题](#the-details-9)“细节”
[链接到此标题](#element-cohesion-10)元素凝聚力
我在 *上下文* 样式上花费了不合理的时间，确保我的通用“乐高积木”组件很好地组合在一起。
例如，我有一个 `<Aside>`
用于旁注的组件，以及一个 `<CodeSnippet>`
组件（前面已讨论）。看看当我们将 `<CodeSnippet>`
放在 `<Aside>`
中时会发生什么：

将其与不在旁注中的代码片段进行比较：

```
function findLargestNum(nums: Array<number>) {
if (nums.length === 1) {
return nums[0];
}
return Math.max(...nums);
}
```

`<CodeSnippet>`
在 `<Aside>`
中，它没有透明背景和灰色边框，而是获得了棕色背景。其他细节，如注释和“复制到剪贴板”按钮，也具有自定义颜色。

`<CodeSnippet>`
在 `<Aside>`
中，它没有浅蓝色背景，而是获得了金色背景。其他细节，如注释和“复制到剪贴板”按钮，也具有自定义颜色。

我为所有四个 `<Aside>`
变体（信息、成功、警告、错误）创建了自定义颜色，适用于每种颜色主题（浅色、深色）。代码片段在 `<Aside>`
中也会收到不同的边距/填充，并且会根据视窗大小以及它们是否为容器中的最后一个子元素而改变。考虑到所有可能的组合，这变得相当复杂！

这只是一个例子。许多其他组件也具有“自适应”样式，这些样式会根据其上下文而改变，以确保所有内容都感觉一致。这花费了大量工作，但我发现结果非常令人满意。😄

[链接到此标题](#the-rainbow-11)彩虹
在桌面主页上，您可能已经注意到出现了一个新的彩虹：

![我的博客主页的屏幕截图，显示了我的 3D 吉祥物后面的彩色彩虹](/_next/image/?url=%2Fimages%2Fhow-i-built-my-blog-v2%2Fhomepage-rainbow.png&w=1920&q=75)
这个彩虹会响应您的光标，片段像铁屑对磁铁的反应一样弯曲到光标附近。

还有一个额外的彩蛋：如果您将鼠标悬停在彩虹上几秒钟，就会出现一个小的“编辑”按钮。单击它将打开 🌈 *彩虹配置器*。

![一个控制面板，其中包含几个滑块和控件，用于更改彩虹的参数](/_next/image/?url=%2Fimages%2Fhow-i-built-my-blog-v2%2Frainbow-configurator.png&w=1920&q=75)
**这里有一个转折：**您不仅在更改设备上的彩虹，*您是在为所有人更改它*。每次更改都会立即广播到世界各地，彩虹穿过网络电缆和 Wi-Fi 信号，以便我们都能享受您设计的彩虹。💖
这得益于 [PartyKit](https://www.partykit.io/)，这是由著名的 Sunil Pai 创建的一个很棒的现代工具。它使用 WebSockets，因此更改速度非常快。我无法对 PartyKit 说出足够好的话。开发人员体验是世界一流的。

我忽略了一件事，那就是数百人同时尝试编辑彩虹会多么混乱 😅。当我第一次发布新博客时，我收到了来自一些人的错误报告，他们认为彩虹出现了故障，并不知道其他人正在争夺控制权。现在情况已经平静下来，但我仍然应该找到一种方法来使这一点更加清晰。

[链接到此标题](#view-transitions-12)视图过渡
在页面之间导航时，应该有一个微妙的交叉淡入淡出动画。如果标题位于新位置，它应该滑入到位：

这使用了非常强大的 [视图过渡 API](https://developer.chrome.com/docs/web-platform/view-transitions)。它尚未在所有浏览器中得到支持，但我认为这是一个很酷的小型渐进式增强。

此 API 通过在过渡之前捕获 UI 的虚拟屏幕截图，并操作该屏幕截图和真实 UI，在周围滑动和淡入淡出事物，从而产生两个不同页面上的两个不同元素是相同的错觉。

老实说，它很难使用；我认为 API 设计很棒，但底层问题空间太复杂了，无法避免一些复杂性。预计会遇到一些小问题，例如事物无法保持其纵横比，或者文本出现故障。

我发现 Jake Archibald 的内容对理解视图过渡非常有帮助。例如，他关于 [处理纵横比更改](https://jakearchibald.com/2024/view-transitions-handling-aspect-ratio-changes/) 的文章。

让它在 Next.js App Router 中工作是一个挑战。我使用了 [use-view-transitions](https://github.com/noamr/use-view-transitions) 包，并创建了一个低级 `Link`
组件，它包装在 `next/link`
周围。如果您好奇，可以在 *来源* 窗格中查看它！

[链接到此标题](#search-13)搜索
我的博客终于有了搜索功能！您可以通过单击标题中的放大镜来访问它。
我使用 [Algolia](https://www.algolia.com/) 来完成所有繁重的工作，例如模糊匹配。在某个时候，我可能会将所有博客文章数据提供给 AI 代理并制作一个聊天机器人，但就目前而言，基本搜索似乎已经足够了。

一个小细节：点击“垃圾桶”图标将清除搜索词，但我将其设置为非即时清除。我希望它看起来像垃圾桶正在吞噬每个字符。😄

[链接到此标题](#modern-outline-icons-14)现代轮廓图标
乍一看，这个网站上的图标 *似乎* 与旧图标非常相似，但它们已经过改进。其中许多图标都有新的微交互！

我的流程是从 [Feather Icons](https://feathericons.com/) 的图标开始，因为它们很符合我的审美。然后，我会拆解或重建它们的 SVG，以便我可以对独立的部分进行动画处理。

例如，我有一个箭头符号，它在悬停时会伸展：

我首先获取了 Feather Icons 的 `ArrowRight` 的 SVG 代码，并将其转换为 JSX。最终代码如下所示：

```
import { useSpring, animated } from 'react-spring';
const SPRING_CONFIG = {
tension: 300,
friction: 16,
};
function IconArrowBullet({
size = 20,
isBooped = false,
}: Props) {
const shaftProps = useSpring({
x2: isBooped ? 23 : 18,
config: SPRING_CONFIG,
});
const tipProps = useSpring({
points: isBooped
? '17 6 24 12 17 18'
: '12 5 19 12 12 19',
config: SPRING_CONFIG,
});
return (
<svg
fill="none"
width={size / 16 + 'rem'}
height={size / 16 + 'rem'}
viewBox="0 0 24 24"
stroke="currentColor"
strokeWidth="2"
strokeLinecap="round"
strokeLinejoin="round"
xmlns="http://www.w3.org/2000/svg"
>
<animated.line
x1="5"
y1="12"
y2="12"
{...shaftProps}
/>
<animated.polyline {...tipProps} />
</svg>
);
}
export default IconArrowBullet;
```
就像真正的箭头一样，这个图标由一个轴和一个尖端组成，由 SVG `line` 和 `polyline` 制成。使用 React Spring，我在 [booped](/react/boop/) 时更改了一些点的 x/y 值。这是一个反复试验的过程，移动各个点直到感觉合适。

这个网站上的许多图标都具有类似的微交互。我甚至为其中一个图标计划了一个更特别的彩蛋，这是我在发布前没有完成的。😮

[链接到此标题](#accessibility-15)无障碍性
在 [“关于像素和无障碍性的惊人真相”](/css/surprising-truth-about-pixels-and-accessibility/) 中，我展示了如何使用 `rem` 单位进行媒体查询更易于访问。它确保我们的布局在用户提高浏览器默认字体大小的情况下优雅地适应。

偶尔，读者会注意到 *我的实际博客* 使用了基于 *像素* 的媒体查询。**我甚至没有实践我所宣扬的！**多么虚伪！

当我第一次构建博客的先前版本时，我不知道基于 rem 的媒体查询更易于访问；我在构建我的课程平台时发现了这一点。将我的博客改造为使用基于 rem 的媒体查询是一项大工程，我不想等到完成这项工作才分享我学到的东西！

因此，每当有人给我发邮件询问此事时，我都会分享这个理由，但我仍然对此感到非常尴尬。😅

不用说，这个新博客在整个过程中都使用了基于 rem 的媒体查询。这些年来，我学到了很多关于无障碍性的知识（包括通过我自己的 [短期残疾](/blog/hands-free-coding/)），并将我学到的所有东西都应用到了这个新博客中。

当然，我仍在不断学习，所以如果你在这个博客上发现任何无法访问的内容，请 [告诉我](/contact/)！

[链接到此标题](#app-router-vs-pages-router-16)App 路由器与 Pages 路由器
正如我之前提到的，新博客最大的变化之一是从 *Pages 路由器* 切换到 *App 路由器*。我知道很多人都考虑进行同样的切换，所以我想分享我的经验，帮助你做出决定。

说实话，我的经历有点喜忧参半 😅。让我们从好的方面开始。

心理模型很棒。“服务器组件”范式比 `getServerSideProps` 感觉更自然。肯定存在学习曲线，但我很快就掌握了它。除了改进的人体工程学之外，新系统功能更强大。例如：在 Pages 路由器中，只有顶层路由组件可以执行后端工作，而现在，任何服务器组件都可以。

服务器组件的另一个好处是，我们不再需要将每个 React 组件都包含在我们的客户端捆绑包中。这意味着“静态”组件完全从捆绑包中省略。这也意味着我们可以使用更强大的服务器专用库，例如 Shiki，而不用担心捆绑包膨胀。
理论上，这*应该*会带来一些相当显著的性能提升，但我的实际体验并非如此。事实上，我的新博客的性能*略差*于我的旧博客：

### Lighthouse 报告（旧）
![Lighthouse 报告显示性能得分为 88](/images/how-i-built-my-blog-v2/blog-lighthouse-old.png)
### Lighthouse 报告（新）
![Lighthouse 报告显示性能得分为 88](/images/how-i-built-my-blog-v2/blog-lighthouse-new.png)
不过，这里有*很多*注意事项：

- 这并不是一个完全相同的比较，因为我在新博客中添加了许多新功能和细节。它不是一个简单的 1:1 迁移。
- 一个主要的影响因素是
[CSS 捆绑问题](https://github.com/vercel/next.js/discussions/70168)我之前提到的。如果你不使用 CSS 模块（或编译成 CSS 模块的工具），你不会遇到这个问题。 - 因为我在使用 React Spring 的情况下散布了如此多的交互，*很多*原本静态的组件最终需要变成客户端组件。我实际上并没有那么多服务器组件。 - 我很可能错过了提高性能的机会，或者在我的实现中犯了一些错误。
看着数字很容易让人沮丧，但当我限制我的 CPU/网络并进行并排比较时，我实际上无法分辨出区别。我对较低的 Lighthouse 得分对 SEO 的影响有点担心，但我认为如果 Next 团队解决了 CSS 捆绑问题，它最终应该会大致相当。

说到性能缓慢，**使用 App Router 的开发服务器要慢得多。**随着我的博客的增长，它变得越来越糟糕。以下是当前的统计数据：

- 使用 Pages Router 时，我的开发服务器启动需要 7-12 秒，具体取决于缓存的状态。使用 App Router 后，这些数字已膨胀到 30-60 秒以上。
- Pages Router 中的热重载感觉是即时的；当我从编辑器切换到浏览器时，我的更改就出现了。使用 App Router 时，它需要 1 到 5 秒的时间。
- 有时，页面加载会随机地花费很长时间，就像这样：
![终端截图显示 92 秒的编译时间](/images/how-i-built-my-blog-v2/ninety-two-seconds.png)
这真的很痛苦 😬。当我切换到我的课程平台（仍然使用 Pages Router）时，感觉就像呼吸了一口新鲜空气。

我应该注意：因为我使用的是 Linaria，所以我不得不选择退出 Turbopack，他们基于 Rust 的现代 Webpack 替代方案。启用 Turbopack 后，开发性能可能不是问题。但我怀疑我们中的许多人会遇到同样的情况，我们需要 Webpack 来处理某个包或其他东西，它*不应该*这么慢；Pages Router 使用的是 Webpack，而且速度很快！

**好消息是，Next.js 团队意识到了这些问题，并将开发性能列为优先事项。**App Router 仍处于起步阶段，必然会有一些成长的烦恼。我非常相信 Next.js 团队会解决这些问题（该团队很棒，他们已经解决了我在提出的许多问题！）。App Router 可能被标记为“稳定”，但老实说，对我来说它仍然感觉很新。
React Server Components 和 App Router 背后的愿景令人鼓舞。尽管 Twitter 上有很多关于 React 社区“重新发明”PHP 的笑话，但我确实认为 Meta/Vercel 做了一些真正了不起的事情，一旦他们解决了所有问题，它将毫无疑问地成为构建 React 应用程序的最佳方式。但今天，感觉我们正处于“早期采用者”阶段。

我很高兴将我的博客迁移到 App Router（当 CSS 问题解决后，我会感觉更舒服 😅），但我也不急于迁移我的课程平台。

[链接到此标题](#a-foundation-to-build-on-17)一个可以构建的基础
我已经教授 React 大约 7 年了。我开始在当地的一家编码训练营任教，开发他们的 React 课程，并与学生一对一地合作。我已经通过这个博客发表了 [22 篇关于 React 的文章](/react/)。我还创建了 [The Joy of React](https://www.joyofreact.com/)，这是一门全面的在线课程，深入探讨了 React 的工作原理以及如何有效地使用它。

这门课程侧重于 React 的核心机制，但最后一模块全部关于 Next.js App Router 和 React Server Components。事实上，最终项目让你构建一个基于 MDX 的交互式博客。😄

它看起来像这样：

它不是我们在课程中涵盖的最复杂的东西，但它是最实用的东西之一。最棒的是，你可以*将其用作你实际博客的基础*！这不仅仅是一个人为的课程项目，它可以成为你在互联网上的真实世界中的家园。😄

你可以在此处了解更多信息：

### 最后更新于
2024 年 9 月 24 日