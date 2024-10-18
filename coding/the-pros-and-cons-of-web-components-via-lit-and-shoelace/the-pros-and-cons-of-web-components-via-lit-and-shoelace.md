
<!--
title: 通过Lit和Shoelace了解Web Components的优缺点
cover: https://cdn.thenewstack.io/media/2024/09/40a2df9e-getty-images-ft2uhxkefwe-unsplashb.jpg
-->

如果您在更大的 Web 实现团队中工作或领导该团队，请确保您了解 Web 组件库的可能优势。

> 译自 [The Pros and Cons of Web Components, Via Lit and Shoelace](https://thenewstack.io/the-pros-and-cons-of-web-components-via-lit-and-shoelace/)，作者 David Eastman。

虽然开发人员喜欢使用框架库中的组件，但 [web 组件](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/) 正受到越来越多的关注，因为它们可以使用 HTML 和 CSS，并减少了对 JavaScript 的需求。但它们也提供了编写自定义组件的能力，使更大的内部软件资产能够更好地控制页面上的外观和感觉。继 [我们最近关于 Shoelace 的报道](https://thenewstack.io/shoelace-web-components-library-that-works-with-any-framework/)（即将更名为 Web Awesome）之后，我想试用一下 [该库](https://shoelace.style/)。

在深入了解 Shoelace 之前，让我们先快速了解一下它下面的一层，即名为 [Lit](https://lit.dev/) 的 [Google web 组件库](https://thenewstack.io/polymers-web-component-library-litelement-and-how-it-compares-to-react/)。

## 快速了解 Lit

这让我们了解了组件是如何构建的。我们只想挑选出基本的内容，因为这是 Shoelace 构建的基础。我们将查看[这里](https://lit.dev/playground/#project=W3sibmFtZSI6ImluZGV4Lmh0bWwiLCJjb250ZW50IjoiPCFET0NUWVBFIGh0bWw-XG48aHRtbD5cbiAgPGhlYWQ-XG4gICAgPHNjcmlwdCBzcmM9XCIuL2luZGV4LmpzXCIgdHlwZT1cIm1vZHVsZVwiPjwvc2NyaXB0PlxuICAgIDxzdHlsZT5cbiAgICAgIHNwYW4ge1xuICAgICAgICBib3JkZXI6IDFweCBzb2xpZCByZWQ7XG4gICAgICB9XG4gICAgPC9zdHlsZT5cbiAgPC9oZWFkPlxuICA8Ym9keT5cbiAgICA8cmF0aW5nLWVsZW1lbnQgcmF0aW5nPVwiNVwiPjwvcmF0aW5nLWVsZW1lbnQ-XG4gIDwvYm9keT5cbjwvaHRtbD4ifSx7Im5hbWUiOiJpbmRleC5qcyIsImNvbnRlbnQiOiJpbXBvcnQge0xpdEVsZW1lbnQsIGh0bWwsIGNzc30gZnJvbSAnbGl0JztcblxuY2xhc3MgUmF0aW5nRWxlbWVudCBleHRlbmRzIExpdEVsZW1lbnQge1xuICBzdGF0aWMgZ2V0IHN0eWxlcygpIHtcbiAgICByZXR1cm4gY3NzYFxuICAgICAgOmhvc3Qge1xuICAgICAgICBkaXNwbGF5OiBpbmxpbmUtZmxleDtcbiAgICAgICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgICAgIH1cbiAgICAgIGJ1dHRvbiB7XG4gICAgICAgIGJhY2tncm91bmQ6IHRyYW5zcGFyZW50O1xuICAgICAgICBib3JkZXI6IG5vbmU7XG4gICAgICAgIGN1cnNvcjogcG9pbnRlcjtcbiAgICAgIH1cblxuICAgICAgOmhvc3QoW3ZvdGU9dXBdKSAudGh1bWJfdXAge1xuICAgICAgICBmaWxsOiBncmVlbjtcbiAgICAgIH1cblxuICAgICAgOmhvc3QoW3ZvdGU9ZG93bl0pIC50aHVtYl9kb3duIHtcbiAgICAgICAgZmlsbDogcmVkO1xuICAgICAgfVxuICAgIGA7XG4gIH1cbiAgXG4gIHN0YXRpYyBnZXQgcHJvcGVydGllcygpIHtcbiAgICByZXR1cm4ge1xuICAgICAgcmF0aW5nOiB7XG4gICAgICAgIHR5cGU6IE51bWJlcixcbiAgICAgIH0sXG4gICAgICB2b3RlOiB7XG4gICAgICAgIHR5cGU6IFN0cmluZyxcbiAgICAgICAgcmVmbGVjdDogdHJ1ZSxcbiAgICAgIH1cbiAgICB9O1xuICB9XG4gIFxuICBjb25zdHJ1Y3RvcigpIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMuX3JhdGluZyA9IDA7XG4gICAgdGhpcy5fdm90ZSA9IG51bGw7XG4gIH1cbiAgXG4gIHdpbGxVcGRhdGUoY2hhbmdlZFByb3BzKSB7XG4gICAgaWYgKGNoYW5nZWRQcm9wcy5oYXMoJ3ZvdGEnKSkge1xuICAgICAgY29uc3QgbmV3VmFsdWUgPSB0aGlzLnZvdGU7XG4gICAgICBjb25zdCBvbGRWYWx1ZSA9IGNoYW5nZWRQcm9wcy5nZXQoJ3ZvdGUnKTtcblxuICAgICAgaWYgKG5ld1ZhbHVlID09PSAndXAnKSB7XG4gICAgICAgIGlmIChvbGRWYWx1ZSA9PT0gJ2Rvd24nKSB7XG4gICAgICAgICAgdGhpcy5yYXRpbmcgKz0gMjtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICB0aGlzLnJhdGluZyArPSAxO1xuICAgICAgICB9XG4gICAgICB9IGVsc2UgaWYgKG5ld1ZhbHVlID09PSAnZG93bicpIHtcbiAgICAgICAgaWYgKG9sZFZhbHVlID09PSAndXAnKSB7XG4gICAgICAgICAgdGhpcy5yYXRpbmcgLT0gMjtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICB0aGlzLnJhdGluZyAtPSAxO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuICB9XG5cbiAgcmVuZGVyKCkge1xuICAgIHJldHVybiBodG1sYFxuICAgICAgPGJ1dHRvblxuICAgICAgICAgIGNsYXNzPVwidGh1bWJfZG93blwiXG4gICAgICAgICAgQGNsaWNrPSR7KCkgPT4ge3RoaXMudm90ZSA9ICdkb3duJ319PlxuICAgICAgICA8c3ZnIHhtbG5zPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmdcIiBoZWlnaHQ9XCIyNFwiIHZpZXdib3g9XCIwIDAgMjQgMjRcIiB3aWR0aD1cIjI0XCI-PHBhdGggZD1cIk0xNSAzSDZjLS44MyAwLTEuNTQuNS0xLjg0IDEuMjJsLTMuMDIgNy4wNWMtLjA5LjIzLS4xNC40Ny0uMTQuNzN2MmMwIDEuMS45IDIgMiAyaDYuMzFsLS45NSA0LjU3LS4wMy4zMmMwIC40MS4xNy43OS40NCAxLjA2TDkuODMgMjNsNi41OS02LjU5Yy4zNi0uMzYuNTgtLjg2LjU4LTEuNDFWNWMwLTEuMS0uOS0yLTItMnptNCAwdjEyaDRWM2gtNHpcIi8-PC9zdmc-XG4gICAgICA8L2J1dHRvbj5cbiAgICAgIDxzcGFuIGNsYXNzPVwicmF0aW5nXCI-JHt0aGlzLnJhdGluZ308L3NwYW4-XG4gICAgICA8YnV0dG9uXG4gICAgICAgICAgY2xhc3M9XCJ0aHVtYl91cFwiXG4gICAgICAgICAgQGNsaWNrPSR7KCkgPT4ge3RoaXMudm90ZSA9ICd1cCd9fT5cbiAgICAgICAgPHN2ZyB4bWxucz1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnXCIgaGVpZ2h0PVwiMjRcIiB2aWV3Qm94PVwiMCAwIDI0IDI0XCIgd2lkdGg9XCIyNFwiPjxwYXRoIGQ9XCJNMSAyMWg0VjlIMXYxMnptMjItMTFjMC0xLjEtLjktMi0yLTJoLTYuMzFsLjk1LTQuNTcuMDMtLjMyYzAtLjQxLS4xNy0uNzktLjQ0LTEuMDZMMTQuMTcgMSA3LjU5IDcuNTlDNy4yMiA3Ljk1IDcgOC40NSA3IDl2MTBjMCAxLjEuOSAyIDIgMmg5Yy44MyAwIDEuNTQtLjUgMS44NC0xLjIybDMuMDItNy4wNWMuMDktLjIzLjE0LS40Ny4xNC0uNzN2LTJ6XCIvPjwvc3ZnPlxuICAgICAgPC9idXR0b24-YDtcbiAgfVxufVxuXG5jdXN0b21FbGVtZW50cy5kZWZpbmUoJ3JhdGluZy1lbGVtZW50JywgUmF0aW5nRWxlbWVudCk7In0seyJuYW1lIjoidGh1bWJfZG93bi5zdmciLCJjb250ZW50IjoiPHN2ZyB4bWxucz1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnXCIgaGVpZ2h0PVwiMjRcIiB2aWV3Qm94PVwiMCAwIDI0IDI0XCIgd2lkdGg9XCIyNFwiPjxwYXRoIGQ9XCJNMTUgM0g2Yy0uODMgMC0xLjU0LjUtMS44NCAxLjIybC0zLjAyIDcuMDVjLS4wOS4yMy0uMTQuNDctLjE0LjczdjJjMCAxLjEuOSAyIDIgMmg2LjMxbC0uOTUgNC41Ny0uMDMuMzJjMCAuNDEuMTcuNzkuNDQgMS4wNkw5LjgzIDIzbDYuNTktNi41OWMuMzYtLjM2LjU4LS44Ni41OC0xLjQxVjVjMC0xLjEtLjktMi0yLTJ6bTQgMHYxMmg0VjNoLTR6XCIvPjwvc3ZnPiJ9LHsibmFtZSI6InRodW1iX3VwLnN2ZyIsImNvbnRlbnQiOiI8c3ZnIHhtbG5zPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmdcIiBoZWlnaHQ9XCIyNFwiIHZpZXdCb3g9XCIwIDAgMjQgMjRcIiB3aWR0aD1cIjI0XCI-PHBhdGggZD1cIk0xIDIxaDRWOUgxdjEyem0yMi0xMWMwLTEuMS0uOS0yLTItMmgtNi4zMWwuOTUtNC41Ny4wMy0uMzJjMC0uNDEtLjE3LS43OS0uNDQtMS4wNkwxNC4xNyAxIDcuNTkgNy41OUM3LjIyIDcuOTUgNyA4LjQ1IDcgOXYxMGMwIDEuMS45IDIgMiAyaDljLjgzIDAgMS41NC0uNSAxLjg0LTEuMjJsMy4wMi03LjA1Yy4wOS0uMjMuMTQtLjQ3LjE0LS43M3YtMnpcIi8-PC9zdZnPiJ9d)游乐场中的代码。

我们想要做的就是制作一个评分按钮，它可以点赞（并变成绿色）或点踩（红色），并相应地更改评分。

![](https://cdn.thenewstack.io/media/2024/09/63f5385e-image-1024x399.png)

您可以看到我们以模块的形式引入了 JavaScript `index.js`，并使用了我们自己定义的名为 `rating-element` 的标签。在 `<style>` 中定义的 `span` 不会影响组件，因为 Shadow DOM 的隔离性。

让我们从代码中提取有趣的部分：

![](https://cdn.thenewstack.io/media/2024/09/4e259b03-image-1-1024x575.png)

您可以看到 Lit 的导入，以及扩展 *LitElement* 的 *RatingElement* 类的定义。在文件的底部，您可以看到基于 RatingElement 将标签注册为自定义元素：

```
customElements.define('rating-element', RatingElement);
```

有一个 render 方法，它基本上构建了基本元素：
```html
render() { 
 return html` 
  <button 
    class="thumb_down" 
    @click=${() => {this.vote = 'down'}}> 
    <svg xmlns="http://www.w3.org/2000/svg" height="24" viewbox="0 0 24 24" width="24"><path d="..."/></svg> 
  </button> 
  <span class="rating">${this.rating}</span> 
  <button 
    class="thumb_up" 
    @click=${() => {this.vote = 'up'}}> 
    <svg xmlns="http://www.w3.org/2000/svg" height="24" viewbox="0 0 24 24" width="24"><path d="..."/></svg> 
  </button>`; 
}
```

因此，需要编写相当多的代码才能完成一些非常简单的事情，但您确实获得了自己的可重用组件。

## Shoelace

让我们上一层楼，使用一些 Shoelace。现在我们获得了构建组件。

我们将安装一个使用 [rollup bundler](https://rollupjs.org/) 的 Shoelace 模板并从那里开始。 bundler 有助于解析组件，而无需从 Web 延迟加载它们。这使我们更接近标准的开发人员工作流程。

首先，我克隆 rollup 示例模板。这将拥有我们需要的正确 npm 包：

![](https://cdn.thenewstack.io/media/2024/09/25ad3d8e-image-2-1024x276.png)

然后我们安装软件包。您可能还需要执行 `npm update`。

![](https://cdn.thenewstack.io/media/2024/09/0ff3ffd7-image-3-1024x686.png)

最后，运行项目：

![](https://cdn.thenewstack.io/media/2024/09/566e5ad8-image-4-1024x283.png)

并在不同的 shell 选项卡上启动页面：

![](https://cdn.thenewstack.io/media/2024/09/d9c26752-image-5-1024x820.png)

这是您应该看到的：

![](https://cdn.thenewstack.io/media/2024/09/6a0d7445-image-6-1024x477.png)

那么我们是如何让这些组件显示出来的呢？

首先，我们在 index.js 中声明要在包中加载哪些组件：

```js
import '@shoelace-style/shoelace/dist/themes/light.css'; 
import '@shoelace-style/shoelace/dist/themes/dark.css'; 
import SlButton from '@shoelace-style/shoelace/dist/components/button/button.js'; 
import SlIcon from '@shoelace-style/shoelace/dist/components/icon/icon.js'; 
import SlInput from '@shoelace-style/shoelace/dist/components/input/input.js'; 
import SlRating from '@shoelace-style/shoelace/dist/components/rating/rating.js'; 
 
import { setBasePath } from '@shoelace-style/shoelace/dist/utilities/base-path.js'; 
// Set the base path to the folder you copied Shoelace's assets to 
setBasePath('/dist/shoelace'); 
// <sl-button>, <sl-icon>, <sl-input>, and <sl-rating> are ready to use!%
```

这就是 Shoelace 按钮、输入和评级组件的来源。这使得 index.html 变得非常精简：

```html
<!doctype html> 
  <html> 
    <head>   
      <title>Shoelace Rollup Example</title> 
      <link rel="stylesheet" href="dist/bundle.css"> 
    </head> 
    <body> 
      <h1>Shoelace Rollup Example</h1> 
      <sl-button type="primary">Click me</sl-button> 
      <br><br> 
      <sl-input placeholder="Enter some text" style="max-width: 300px;"></sl-input> 
      <br><br> 
      <sl-rating></sl-rating> 
    
      <script src="dist/index.js"></script> 
    </body> 
  </html>
```

请注意，HTML 引用的 index.js 是由 rollup 展开并放置在分发目录中的那个。
想要一个黑暗的主题？只需将 index.html 更改为：

```html
<html class="sl-theme-dark"> 
```

并且因为我们已经在 index.js 中导入了深色主题：

![](https://cdn.thenewstack.io/media/2024/09/437255ea-image-7.png)

最后是一点交互性（不要忘记在更大的更改之间刷新缓存）。

让我们向按钮添加一个 toast 风格的警报（一个进入角落的警报），并在关闭之前为 toast 添加一个持续时间倒计时。

我们将警报组件包含在 index.js 中：

```js
...
import SlIcon from '@shoelace-style/shoelace/dist/components/icon/icon.js';
import SlInput from '@shoelace-style/shoelace/dist/components/input/input.js';
import SlRating from '@shoelace-style/shoelace/dist/components/rating/rating.js';
import SlAlert from '@shoelace-style/shoelace/dist/components/alert/alert.js';
...
```

我们将组件放在 index.html 中，替换按钮代码：

```html
<div class="alert-duration"> 
  <sl-button variant="primary">Show Alert</sl-button> 
  <sl-alert variant="primary" duration="3000" countdown="rtl" closable> 
    <sl-icon slot="icon" name="info-circle"></sl-icon> 
    This alert will automatically hide itself after three seconds, unless you interact with it. 
  </sl-alert> 
</div> 
```

以及 index.js 中的一些控制代码，在结束之前：

```js
const container = document.querySelector('.alert-duration'); 
const button = container.querySelector('sl-button'); 
const alert = container.querySelector('sl-alert'); 
button.addEventListener('click', () => alert.toast()); 
```

结果已经相当令人印象深刻：

![](https://cdn.thenewstack.io/media/2024/09/067f81f5-image-8-1024x242.png)

（您看不到的是警报底部缩小的蓝色倒计时线）

## 结论

这只是使用 Shoelace 之类的库使用 Web 组件的介绍——它们最初需要一些关注，但（像框架一样）有很多丰富的内容。但是，与框架不同，这些主要使用 HTML 和 CSS。

为了让 React 用户更容易过渡，每个 Shoelace 组件都可以作为 React 组件导入。缺点是 SSR（服务器端渲染）仍然不适合 Web 组件。确实，自定义元素与组件并不完全相同；[这里](https://dev.to/ryansolid/web-components-are-not-the-future-48bh)详细说明了这可能导致的问题。

但总的来说，如果您正在考虑在一个更大的 Web 实现团队中工作或领导该团队，请确保您了解 Web 组件库的可能优势。