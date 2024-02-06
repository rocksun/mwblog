<!--
title: Web 组件入门指南
cover: https://cdn.thenewstack.io/media/2024/02/b0931de2-blaz-erzetic-g5f0bjq-frs-unsplash-1024x683.jpg
-->

为组织的组件库注入和谐：这是我们的 Web 组件指南，教您如何开始定义自己的组件。

> 译自 [Introduction to Web Components and How to Start Using Them](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/)，作者 David Eastman 曾是一名在伦敦工作的专业软件开发人员，曾在 Oracle Corp. 和英国电信公司担任职务，并担任顾问，帮助团队更加敏捷地工作。

虽然像网络这样的开放创新平台鼓励各种各样的用途，但混乱的缺点体现在定义当前网络是什么的声音喧嚣交加。通常在技术演进的这一点上，行业领袖们会聚在一起制定规则和法规，方便地巩固自己的优势，同时也为消费者提供更清晰的信息。这就是为什么几乎任何人都可以定义构成汽车的重要组件，但可能发现对于网站来说这样做更难。

像画一个圆或把文字放在一个框里这样的简单事情可以用多种方式完成。这是因为，例如，简单的形状不是网络的一级对象。例如，这是在CSS中定义的一个圆：

```css
.circle 
{ 
  height: 150px; 
  width: 150px;  
  border: solid 1px; 
  border-radius: 50%; 
  display: inline-block; 
}
```

在页面上接着是：

```html
<span class="circle"/>
```

现在，这产生了一个漂亮的圆。虽然单词“circle”本身在定义中没有起作用，但它作为HTML和CSS的综合体起到了我需要的对象的创造作用。如果然后问“它是什么颜色的？”，那在很大程度上取决于继承的上下文和包含什么。我可以使用 [playcode.io](http://playcode.io/) 这样的沙盒来确认它是否有效。

我还可以在 App.jsx 文件中使用 [Tailwind](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/) CSS 框架在 playcode.io 中绘制一个圆：

```jsx
<div class="w-20 h-20 rounded-full border-2 
            border-black flex justify-center 
            items-center">
```

结果是另一个漂亮的圆。

Tailwind 是一个不错的框架。然而，接下来我必须有效地继续在所有其他方面使用该库。而且很难保证这些在不同浏览器上能够良好运行。此外，与其前身 Bootstrap 一样，Tailwind 也受命运的摆布。我们真正想要的是一种“官方”方式来表达一个组件。

## 引入 Web Components

Web 组件是[一种](https://kinsta.com/blog/web-components/#:~:text=A%20Web%20Component%20is%20a,forward%2C%20and%20adjust%20the%20volume)“创建一个封装的、单一职责的代码块，可以在任何页面上重复使用”的方式。它们由已存在的标准组成，以 Web API 的形式表达，供各个供应商多年来一直在同意并实现。它们现在已经足够成熟和被广泛使用，可以挑战现有的流行框架。所有现代浏览器都已经支持这个规范一段时间了。

Web 组件允许您定义**自定义元素**（例如“my-circle”），然后注册它们。

这很棒，但正如我所暗示的，控制它们需要在所有其他地方控制 CSS。为了解决这个问题，一个 Web 组件可以在一个**影子 DOM** 中包含它自己的一套规则。这只是一个与主 DOM 不会冲突的独立对象树。

最后，**模板和插槽**允许您定义惰性片段，在渲染时不会显示，但稍后可以重新使用。所以我可以定义这样的东西：

```html
<template id="my-paragraph"> 
 <p>My paragraph</p> 
</template>
```

这不会渲染，但以后可以间接引用并用作通用构建块。

[Web 组件是用 JavaScript 构建的](https://thenewstack.io/how-web-components-are-used-at-github-and-salesforce/)；是的，我知道有些人希望在他们的网站上使用更少的 JS。但现在，这是目前的方式。

## 如何定义自己的 Web 组件

![Zoom](https://cdn.thenewstack.io/media/2024/02/96553101-untitled-1-1024x787.png)

Web 组件是自定义的 HTML 元素，如 `<my-circle />`。名称必须包含连字符，以便它永远不会与 HTML 规范中正式支持的元素发生冲突。因此，我们已经建立了一个关系：浏览器将始终知道 HTML 标签，但将尊重新的标签。它们如何知道新的标签呢？

在将组件定义为一个类之后，您需要使用 CustomElementRegistry 将其注册，如下所示：

```javascript
customElements.define('my-circle', MyCircle);
```

然后，组件需要用 JavaScript 构建。我们知道类的名称，因为我们刚刚注册了它。我在查看[文档](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements)示例后拼凑了这个：

```javascript
class MyCicrle extends HTMLElement {
  constructor() {
    // Always call super first in constructor
    super();
  }
 
  connectedCallback() {
    // Create a shadow root
    const shadow = this.attachShadow({ mode: "open" });
 
    // Create spans
    const wrapper = document.createElement("span");
    wrapper.setAttribute("class", "smallcircle");
 
    // Create some CSS to apply to the shadow dom
    const style = document.createElement("style");
    console.log(style.isConnected);
 
    style.textContent = `
 
      .smallcircle {
        height: 150px;  
        width: 150px; 
        border: solid 1px;  
        border-radius: 50%;  
        display: inline-block;
        color: #ffffff;
      }
    `;
 
    // Attach the created elements to the shadow dom
    shadow.appendChild(style);
    console.log(style.isConnected);
    shadow.appendChild(wrapper);
  }
}
```

我成功在 Playcode 中运行了这段代码，而且没有使用任何包。这只是我们先前圆形示例的手工构建，但是使用了 JavaScript。它确实证明了 Web 组件是可操作的，即使在这个沙盒中也是如此。这两条日志消息记录了在我们附加样式元素之前和之后，影子 DOM 中的变化。connectedCallback 方法是用于使 Web 组件工作的生命周期规范的一部分。当元素首次添加到主文档时，此方法是不可避免的“设置”调用。

所以我刚刚做了很多工作来绘制一个圆。为了证明它的组件性质，让我做更多的事情。通过读取一个属性，我至少可以改变颜色：

![Zoom](https://cdn.thenewstack.io/media/2024/02/e8ae0290-untitled-2-1024x727.png)

毫无疑问，定义自定义元素的清晰性确实使得在页面上使用 Web 组件成为一个愉快的过程。而且代码更改是足够直接的：

```javascript
... 
let clr; 
if (this.hasAttribute("color")) 
{ 
  clr = this.getAttribute("color"); 
} 
else 
{ 
  clr = "white"; 
} 
style.textContent = ` 
 .smallcircle { 
   height: 150px; 
   width: 150px; 
   border: solid 1px; 
   border-radius: 50%; 
   display: inline-block; 
   color: ${clr}; 
 } 
`; 
...
```

我没有使用模板的示例，但使用类似的技术，您可以抓取和克隆它们，然后将它们插入到您的影子 DOM 中。毕竟，在 HTML 中定义 HTML 更容易。

以我扩展 HTMLElement 的方式，我也可以扩展现有的 HTML 元素并从那里开始。

## Web 组件在实际中的应用

但是，Web 组件是否已经太迟出现以[淘汰流行的框架呢](https://thenewstack.io/case-against-web-frameworks/)？在大多数情况下，Web 组件可以与框架组件一起工作，尽管关于**服务器端渲染**的一个独立问题确实是个问题（这里我不会深入讨论）。

Web 组件的强大之处真正体现在一个小型用户体验团队希望开发一个他们知道将经受时间考验的库时。业务和开发团队之间的想法不再需要转化为 [Angular 或 React](https://thenewstack.io/angular-vs-react-how-to-choose-the-right-framework-for-you/)。符合品牌标识的复杂组件可以像普通标签一样使用。不再是一个“my-circle”标签，想象一下一个“my-company-header”标签，它可以在整个组织中使用——用户体验团队控制开发，但没有陷入框架的风险。这将设计师和开发人员拉得更近。

因此，使用 Web 组件，组织的组件库不仅更加稳定，而且不再过于依赖于其他地方定义的另一层，它们使用的语言将远超出开发团队的范围。它为 web 的“西部荒野”带来了一点和谐。
