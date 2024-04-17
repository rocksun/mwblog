## JavaScript 的五大未充分利用的功能

![Top 5 Underutilized JavaScript Features 的特色图片](https://cdn.thenewstack.io/media/2024/04/54cf79eb-getty-images-sdayknbkxeg-unsplash-1024x683.jpg)

[JavaScript](https://thenewstack.io/javascript/) 是一种必不可少的编程语言，但其功能常常未得到充分探索。[JS 拥有广泛的功能](https://thenewstack.io/top-5-javascript-tools-for-ai-engineering/)，可应用于无数的用例，帮助开发人员创建高效、可重用且可适应的代码。

在本文中，我们将探讨五大未充分利用的 JavaScript 功能及其用例。我们还将提供代码示例，展示如何使用 JS 来完成几乎所有事情，从解决日期管理问题到链接函数，甚至检测恶意网站。

## 1. JavaScript 钩子用于检测恶意网站

一个巧妙的 JS 功能是使用钩子作为一种有效的方法，[判断网站是否为假](https://www.identityguard.com/news/how-to-tell-if-a-website-is-fake)，而无需任何特定的 OpSec 或网络安全知识。

钩子是 JS 函数，允许开发人员“钩入”流行的 UI 开发库 React 中的状态和生命周期功能。这意味着 [开发人员可以使用 React](https://thenewstack.io/the-pros-and-cons-of-using-react-today/)，而无需编写单独的类。

在以下示例中，我们将重点关注使用静态和动态组件构建的网页。静态组件始终作为 HTML 源代码的一部分声明，并由浏览器或其已安装的插件呈现。同时，动态组件包括 JS 等脚本，这些脚本通过添加、更改或删除某些元素来修改 HTML 文档，以及 [利用 XMLHttpRequest 和类似对象](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) 进行服务器交互。

### 工作原理

利用工具包（[网络犯罪分子使用的工具包](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/malware/exploits-malware?view=o365-worldwide)）和恶意网站或 Web 应用程序通常依赖混淆来绕过基于签名的保护方法。JS 可用于对网站进行混淆处理，修改代码及其元素，以便浏览器可以读取和处理。

利用工具包通常包含非常大的代码块，以隐藏利用并混淆 Web 浏览器。一旦被 JS 解码，就会添加新的页面元素，例如新的 DIV 元素、新的 JS 元素和加载利用的新 Java 小程序元素。

这意味着在混淆处理过程中可以将 JS 钩子应用于脚本函数，如果检测到任何异常情况（例如添加潜在的恶意 Java 小程序元素），则发出警报。

为此，我们必须首先专注于钩住添加元素的主要方法：[appendChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)、[replaceChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/replaceChild) 和 [document.write](https://developer.mozilla.org/en-US/docs/Web/API/Document/write)。第四种方法稍微有挑战性；因此，应该专注于钩住特定函数，例如 [document.getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById) 或 [document.createElement()](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)。然后可以将对象添加到 MutationObserver 对象，或者我们可以使用 Mutation 事件并监视任何更改。

下面是一个注册钩子的函数示例：

```
function jsh_hook_function(object, property, pre_h_func, post_h_func) {
  const original = object[property];
  object[property] = function(...args) {
    if (pre_h_func) {
      pre_h_func.apply(this, args);
    }
    const result = original.apply(this, args);
    if (post_h_func) {
      post_h_func.apply(this, [args, result]);
    }
    return result;
  };
}
```

## 2. 在 Node.js 中生成报告

报告和文档是健壮网络安全策略的关键要素，但它可能是一个乏味且耗时的过程，尤其是在涉及更敏感信息（例如渗透测试报告、漏洞评估和任何其他与安全相关的信息）时。Jsreport 是一个专门的报告平台，已在开源 JavaScript 运行时环境 Node.js 中开发。该平台具有广泛的用例，包括 HTML 到 PDF 的转换。

只需使用 Chrome 浏览器，您只需
[安装 jsreport npm 包](https://jsreport.net/learn/npm) 并调用单个函数。除了 HTML，该平台还可以转换各种媒介，从而可以使用 JS 单独 [生成 DOCX 文件为 PDF](https://apryse.com/blog/javascript/generate-docx-and-save-as-pdf-in-javascript) 甚至整个电子表格，包括公式。这意味着数据可以保存在单个平台上并转换为报告，而无需第三方工具——非常适合网络安全文档和导出 [渗透测试报告](https://www.getastra.com/blog/security-audit/penetration-testing-report/)，以便测试、分析和数据存储都集中化。

Jsreport 并非 Google Chrome 专用，并且与一系列服务和技术兼容，以打印输出。这包括

[Apache FOP](https://xmlgraphics.apache.org/fop/)，用于呈现 XML 文件。

### 工作原理

安装 jsreport npm 并调用一个函数：

```
const http = require('http');
const jsreport = require('jsreport');
http.createServer(async (req, res) => {
  try {
    const result = await jsreport.render({
      template: {
        content: '<h1>Hello world</h1>',
        engine: 'handlebars',
        recipe: 'chrome-pdf'
      }
    });
    res.setHeader('Content-Type', 'application/pdf');
    result.stream.pipe(res);
  } catch (e) {
    res.writeHead(500, { 'Content-Type': 'text/plain' });
    res.end(`Error generating PDF: ${e.message}`);
  }
}).listen(1337, '127.0.0.1');
```

## 3. 使用生成器控制执行流

生成器是一种可以暂停和恢复的函数类型，它可以帮助开发人员更好地控制执行流。生成器可用于回溯算法、无限序列和

[异步操作](https://www.freecodecamp.org/news/async-generators-as-an-alternative-to-state-management/)；此外，它们还允许创建自定义迭代模式。

这是一个功能强大且用途广泛的 JavaScript 特性，但经常被低估，许多

[软件开发人员](https://thenewstack.io/software-development/) 错失了最大程度控制代码执行的能力。

### 工作原理

这是一个简单的代码示例：

```
function* generatorFunction() {
  yield 'Hello';
  yield 'World';
}
const generator = generatorFunction();
console.log(generator.next().value); // 输出：Hello
console.log(generator.next().value); // 输出：World
```

要指定一个生成器函数，首先应使用 `function*` 语法定义 `generatorFunction`，然后使用 `yield` 关键字暂停函数执行并返回一个值。接下来，通过调用

[generatorFunction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction) 创建生成器对象，然后调用生成器上的 `next` 方法以恢复执行。返回的对象的 `value` 属性还包含已生成的 `value`。

## 4. 使用 Temporal 改进日期管理

多年来，许多开发人员

[抱怨 JavaScript 中的日期管理功能不佳](https://www.freecodecamp.org/news/how-to-format-a-date-with-javascript-date-formatting-in-js/)。幸运的是，Temporal 提供了一个本机解决方案，[提供了一个标准全局对象来替换 date 对象](https://docs.temporal.io/temporal) 以解决一系列问题。例如，一个令人困惑的问题是索引不佳，月份从 0 开始，而日期从 1 开始。

Temporal 支持多个时区和非公历，它是一个开箱即用的解决方案，具有易于使用的 API，可以简化从字符串中解析日期。Temporal 对象不可变的特性（即无法更改）还意味着日期将不受导致意外修改的错误影响。

### 工作原理

以下是开发人员可以利用的几种 Temporal 方法：

a) `PlainDate()` – 创建一个没有时间的日期。

```
new Temporal.PlainDate(2024, 7, 26);
Temporal.PlainDate.from('2024-07-26');
// 两者都返回一个表示 2024 年 7 月 26 日的 PlainDate 对象
```

b) `PlainTime ()` – 创建一个没有日期的时间。

```
new Temporal.PlainTime(20, 24, 0);
Temporal.PlainTime.from('20:24:00');
// 两者都返回一个表示 20:24 的 PlainTime 对象
```

c) `PlainMonthDay ()` – 创建一个月份和日期，但不指定年份。对于每年在同一天重复的日期（例如情人节）来说，这是一个有用的函数。

```
const valentinesDay = Temporal.PlainMonthDay.from({ month: 2, day: 14 });
```

## 5. 使用高阶函数创建可重用代码

在 JavaScript 中，函数是优先级，这允许创建高阶函数来建立代码层次结构。高阶函数将一个或多个函数转换为参数，或者可用于返回另一个函数。这提供了一系列功能，例如组合、
**柯里化和函数链式调用**

[柯里化](https://frontend.turing.edu/lessons/module-3/hof-and-currying.html)和函数链式调用最终帮助开发者创建简化、模块化的代码，这些代码可以在其他项目中轻松重用。

### 工作原理

我们以函数链式调用为例。在此示例中，对象是一个计算器，使用函数链式调用有很多方法可以改变其内部状态并无缝返回每个修改后的状态。

```
const calculator = {
  value: 0,
  add(num) {
    this.value += num;
    return this;
  },
  subtract(num) {
    this.value -= num;
    return this;
  },
  multiply(num) {
    this.value *= num;
    return this;
  },
  getValue() {
    return this.value;
  },
};

const result = calculator.add(5).subtract(2).multiply(3).getValue();
console.log(result); // 输出：9
```

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。