
<!--
title: JavaScript的5项前沿技术
cover: https://cdn.thenewstack.io/media/2024/05/97064ccd-alex-shuper-15wviwvlbdk-unsplash.jpg
-->

从单子到模式匹配，我们将引导您了解高级开发人员使用的最新、最棒的 JavaScript 技术。

> 译自 [Top 5 Cutting-Edge JavaScript Techniques](https://thenewstack.io/top-5-cutting-edge-javascript-techniques/)，作者 Alexander T Williams。

JavaScript 是现代 Web 开发领域必不可少的工具，它不断变化和发展，树立了新的标准。在本文中，我们重点介绍五种前沿 JavaScript 技术，向开发人员展示构建动态 Web 应用程序的新颖创新方法，这些应用程序提供高水平的交互性和性能。从单子到模式匹配，我们将引导你了解高级开发人员的最新最棒的 JS 技术。

## JavaScript 为何如此流行？

JavaScript 因其灵活性而获得极大欢迎，并已确立了自己作为全球 [使用最广泛的编程语言](https://www.statista.com/statistics/793628/worldwide-developer-survey-most-used-languages/)。JS 通常用于创建具有高度交互性的动态 Web 应用程序，例如实时更新、直观、[功能丰富的用户界面](https://thenewstack.io/netlifys-approach-to-the-frontend-according-to-its-new-cto/) 等。此外，JavaScript 允许应用程序跨各种平台运行。

JS 可用于各种项目，例如为电子商务服务提供支持或制作动画和手机游戏。然而，这仅仅是 [该编程语言功能的缩影](https://thenewstack.io/web-development-in-2023-javascript-still-rules-ai-emerges/)。我们还看到 JS 被用于企业环境中，尤其是在关键的 ERP 支持的 [流程（如 SAP 人员扩充](https://www.suretysystems.com/insights/closer-look-sap-staff-augmentation-with-surety-systems/)）中，因为它允许创建 [自定义仪表板](https://thenewstack.io/5-dashboard-design-best-practices/) 和 UI，并构建在原生 Web 平台之上。

许多领先的平台（如 Facebook）使用 [开源用户界面框架](https://reactnative.dev/) React Native，它构建在 JavaScript 之上。这使他们能够构建可在 iOS 和 Android 上运行的移动应用程序（如今，[甚至 Apple Vision Pro](https://thenewstack.io/react-native-fork-supports-development-on-apple-vision-pro/)），同时使用单个代码库。因此，开发时间大大缩短，使用的资源更少，并且用户体验在所有平台和设备上保持一致。

Node.js 等服务器端运行时环境使得在 Web 浏览器之外运行 JavaScript 成为可能，进一步 [提高了应用程序的可扩展性和部署可能性](https://thenewstack.io/node-js-22-release-improves-developer-experience/)。为了使 JS 更加通用和多功能，大量与 JS 兼容的 API 也将 Web 应用程序链接到外部服务。

最后，JavaScript 得到一个强大的 [库和框架生态系统](https://thenewstack.io/learn-more-by-building-your-own-custom-javascript-framework/) 的支持，该生态系统有助于简化和加速开发，允许开发人员选择预先编写的代码来执行特定功能。

## 5项前沿技术

我们选择了五种前沿 JavaScript 技术，开发人员现在应该使用这些技术，以帮助你克服众多开发问题并创建更有效、更用户友好的应用程序。

### 1. Monads（异步操作）

Monads 有助于 [组合需要上下文的函数](https://tech.nextroll.com/blog/dev/2022/11/11/exploring-monads-javascript.html) 以返回一个值，并且在简化错误管理和减少意外结果的可能性方面非常有效。

Monads 旨在尽可能简化代码中函数的组合。它们通常在构建需要最高精度的企业级应用程序时使用。单子可以使代码更易于管理，从而产生复杂的回调、嵌套条件分支等。从本质上讲，单子旨在尽可能简化代码中函数的组合。

单子可以分解为三种函数组合：

- 函数映射：`a => b`
- 具有上下文的函子映射：`Functor(a)=> Functor(b)`
- Monads 展平（从上下文中解包值）并使用上下文映射：`Monad(Monada))=> Monad(b)`

函数组合是 [允许创建函数管道的基础](https://www.freecodecamp.org/news/function-composition-in-javascript/)，从而实现高效的数据流。管道的第一阶段是输入，最后阶段是从其初始状态转换的输出。但是，要实现这一点，管道中的每个阶段都必须能够预测前一阶段将返回什么数据类型。

这正是单子式所擅长的，通过映射函数来建立智能管道。它们以[类似于 Promise 的方式工作](https://thenewstack.io/what-are-promises-in-javascript/)，而且可以无缝地一起使用。

这里有一个单子用来从异步API中获取一个用户，然后将该用户数据传递给另一个异步API来执行计算：

```js
  const composeM = chainMethod => (...ms) => (
    ms.reduce((f, g) => x => g(x)[chainMethod](f))
  );
  const composePromises = composeM('then');
  const label = 'API call composition';
 
  // a => Promise(b)
  const getUserById = id => id === 3 ?
    Promise.resolve({ name: 'Kurt', role: 'Author' }) : undefined;
 
  // b => Promise(c)
  const hasPermission = ({ role }) => (
    Promise.resolve(role === 'Author')
  );
 
  // Compose the functions (this works!)
  const authUser = composePromises(hasPermission, getUserById);
  authUser(3).then(trace(label)); // true
```

### 2. 声明式编程

> 一种声明式方法通常用于开发人员优先考虑简洁的、富有表现力的代码。

JavaScript 中的声明式编程重点关注代码的整体目标，而不是如何实现这些目标。这使得代码更简单，更易读——因此，更易于维护。当开发人员优先考虑简洁、富有表现力的代码以快速交付项目时，通常会使用声明式方法。

让我们将声明式方法与命令式方法进行比较：

命令式：

```js
function evenSum(numbers) {
    let result = 0;
 
    for (let i = 0; i < numbers.length; i++) {
        let number = numbers[i]
        if (number % 2 === 0) {
            result += number;
        }
    }
 
    return result;
}
```

声明式：

```js
const evenSum = numbers => numbers
    .filter(i => i % 2 === 0)
    .reduce((a, b) => a + b)
```

### 3. 用于提高 Node.js 性能的服务器端缓存 

> 服务器端缓存可用于根据使用指标自动扩展资源。

缓存并不是什么新鲜事物，可能不被认为特别新潮，但由于客户端和服务器端 Web 应用程序都可以使用缓存，因此它是提高性能的强大工具。特别是，服务器端缓存可通过加快数据检索来提高 Node.js 性能。

我们来看看内存缓存技术的一个简单示例：

```js
const cache = require('memory-cache');
 
function getDataFromCache(key) {
  const cachedData = cache.get(key);
  if (cachedData) {
    return cachedData;
  }
 
  // If data is not in cache, fetch it from the source
  const data = fetchDataFromSource();
 
  // Store data in cache for future use
  cache.put(key, data, 60000); // Cache for 60 seconds
 
  return data;
}
```

服务器端缓存可以用来基于使用指标自动化资源的扩展。AWS Lambda、Azure Functions 或 Google Cloud Functions 可以被编程为动态调整服务，同时用于 JavaScript 的 AWS SDK 允许您监控使用情况、优化云成本和自动化扩展操作，确保您仅为所需的资源付费。

### 4. 不可变性 

不可变性指的是不能改变的东西。在 JavaScript（及其编程语言）中，它指的是一旦设置后永远不会改变的值。由于应用程序不断地改变和更新，不可变性似乎是不必要的——但事实并非如此。

> 这种技术的好处是能减少调试，减少意外结果。

不可修改的数据非常重要，因为它有助于增强代码库的一致性，简化状态管理。与其修改值，不如创建一个新值，这样可提高可预测性，进而可减少错误（例如，当数据结构意外更改时发生的错误）。这会导致减少调试以及减少意外结果。

不可变性用于 name 值的一个示例：

```js
// Import stylesheets
import './style.css';
 
// Write JavaScript code!
const appDiv = document.getElementById('app');
appDiv.innerHTML = `<h1>Open the console to see results</h1>`;
 
class Person {
  //_name = "Nee";
  //_name = ["Nee", "Ra"];
  _name = { first: "Nee", middle: "L" };
  
  get name() {
    return this._name;
  }
  
  set name(value) {
    console.log('In setter', value);
    this._name = value;
  }
}
 
let p = new Person();
//p.name = "Ra";                        // Setter executes
//p.name.push("Lee");                   // Setter doesn't execute
//p.name = [...p.name, "Lee"];          // Setter executes
//p.name.middle = "Lee";                // Setter doesn't execute
p.name = { ...p.name, middle: "Lee" };  // Setter executes
```

### 5. 模式匹配

模式匹配是一种条件分支，可以简洁地匹配数据结构模式，同时绑定变量。 模式匹配通常用于编写 XSLT 样式表来转换 XML 文档。

> 模式匹配比标准 switch 语句更有效。 

当需要针对任何给定模式测试值时，模式匹配比标准 switch 语句更有效，并且提供了更多的控制，允许开发人员编写更复杂的表达式。

以下是使用 match 模块实现阶乘函数的示例，使用 JU­nify 库：

```js
match = function () {
  var unify = unification.unify;
 
  function match_aux(patterns, value) {
    var i, result;
 
    for (i = 0; i < patterns.length; i += 1) {
      result = unify(patterns[i][0], value);
      if (result) {
        return patterns[i][1](result);
      }
    }
    return undefined;
  }
 
  return function(patterns, value) {
    return match_aux(patterns, value);
  };
}();
 
var fact = function (n) {
  return match([
    [0, function() { return 1; }],
    [$('n'), function(result) {
      return result.n * fact(result.n - 1);
     }]
  ], n);
};
```

## 结论

JavaScript 灵活、多功能，并且可以在各种平台上部署。使用上述技术意味着开发人员可以为其应用程序创建功能强大但简洁的代码。
