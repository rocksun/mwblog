
<!--
title: JavaScript简介
cover: https://cdn.thenewstack.io/media/2022/12/f34b5762-javascript-.jpg
summary: JavaScript 是一种流行的编程语言，广泛应用于 Web 开发、服务器端编程和移动应用开发。它具有灵活性和通用性，并不断更新以适应新的技术发展。学习 JavaScript 的基础知识、高级概念和最佳实践对于成为一名优秀的 Web 开发者至关重要。
-->

JavaScript 是一种流行的编程语言，广泛应用于 Web 开发、服务器端编程和移动应用开发。它具有灵活性和通用性，并不断更新以适应新的技术发展。学习 JavaScript 的基础知识、高级概念和最佳实践对于成为一名优秀的 Web 开发者至关重要。

> 译自：[Introduction to JavaScript](https://thenewstack.io/introduction-to-javascript/)
> 
> 作者：TNS Staff

作为世界上可能最流行的编程语言，JavaScript 通过实现动态和交互式页面来支撑着 Web。但它的灵活性和通用性使其可以应用于浏览器之外的各种平台，从服务器和智能手机到嵌入式系统，并且已经成为在所有这些设备上创建丰富、引人入胜的应用程序的一种方式。该语言的年度更新引入了新特性，并改进了 JavaScript 的功能、可读性和性能。这些更新还提高了开发人员的生产力，确保它是一种编写速度快且易于上手的语言，使其与日益具有挑战性的场景保持相关性。

## JavaScript 简史

JavaScript 的第一个版本，最初名为 Mocha，然后是 LiveScript，是由 [Brendan Eich](https://thenewstack.io/brendan-eich-on-creating-javascript-in-10-days-and-what-hed-do-differently-today/) 在短短 10 天内编写的，作为 Netscape 浏览器的脚本语言。但这并不意味着该语言设计得很差。旨在使网页更具动态性和交互性，它借鉴了 Scheme 和 Java 等现有语言的概念和特性，并且自那时以来得到了广泛的开发。尽管该语言在 1997 年成为 ECMAScript 标准（由 ECMA International 正式发布为 ECMA-262），但在 2009 年 ECMAScript 5 (ES5) 发布后，更新停滞了一段时间，但它拥有一个异常丰富的库和框架生态系统，以帮助 JavaScript 跟上 Web 技术的快速发展。自 2015 年 ES6 发布重大修订版以来，每年都会进行更新，以利用 JavaScript 社区的创造力，并以标准化的方式引入该语言的新特性。

多年来，开发人员意识到 JavaScript 除了浏览器之外，还可以作为一种通用语言在各种平台和环境中使用。2009 年推出的 Node.js 作为一个使用 V8 引擎的开源跨平台运行时，将 JavaScript 带到了服务器端编程。这种扩展使 JavaScript 不仅是创建交互式 Web 界面的工具，而且还是以同样快速、高效的语言处理复杂后端任务的一种方式。

## 当前的相关性

JavaScript 被广泛使用并定期更新，仍然是现代 Web 开发的基石，其中包括移动设备和远超浏览器的环境。它的普遍性是无与伦比的：它在网页中提供交互式元素，为 React、Angular 和 Vue.js 等前端框架提供支持，并且还用于构建桌面应用程序（通过 Electron）、后端服务（通过 Node.js 和 Deno）和无服务器函数（例如，使用轻量级 V8 隔离的 Cloudflare Workers）。JavaScript 的灵活性和适应性使其始终处于 Web 开发趋势的最前沿，使开发人员能够提供越来越复杂的 Web 应用程序。

强大的社区支持和庞大的库和框架生态系统，以及 [TypeScript](https://thenewstack.io/typescript/) 等支持技术和 [WebAssembly](https://thenewstack.io/webassembly/) 等互补平台，帮助 JavaScript 在各种开发场景中保持相关性和通用性。

如果您刚开始使用 JavaScript，那么这里将介绍该语言的基础知识，从变量和数据类型到控制结构和函数。让我们还探讨一下赋予 JavaScript 强大功能和通用性的高级概念——包括关键框架和库——并提供一些关于最佳实践的技巧，以确保您的 JavaScript 代码不仅功能强大，而且高效、可维护和安全。

也许比任何其他语言都更重要的是，JavaScript 受社区驱动，因此与其他开发人员建立联系将有助于您掌握最新进展。

## JavaScript 基础知识

新的 JavaScript 开发人员应该从理解基本语法和数据类型开始。

### 基本概念：变量、数据类型、运算符

* **变量**：在 JavaScript 中，变量用于存储数据值。JavaScript 使用关键字 `var`、`let` 和 `const` 来声明和赋值变量。虽然 `var` 是函数作用域的并且仍然有效，但 `let` 和 `const` 是块作用域的，并且在现代 JavaScript 中更受青睐。`const` 用于不应重新赋值的值。
* **数据类型**：JavaScript 是一种动态类型语言，这意味着变量的类型是在代码运行时而不是在编译时确定的。主要的数据类型有：
  + **原始类型**：String、Number、BigInt、Boolean、Undefined、Null 和 Symbol。
  + **非原始类型**：引用或派生的数据类型用于存储数据集合：Object、Array、Function、Map、Set、WeakMap 和 WeakSet。对象是键值对，数组是有序的值集合。数组和函数在技术上是 JavaScript 中专门的对象；Map 和 Set 是在 ES6 中引入的，分别作为键值和唯一值存储的普通对象的替代方案。
* **运算符**：JavaScript 包括与表达式和语句一起使用的各种运算符，以执行计算和逻辑。这些包括：
  + **算术运算符**：使用 `+`、`-`、`*`、`%` 和 `/` 等运算符执行基本数学运算。
  + **比较运算符**：使用 `==`、`===`、`!=`、`>`、`<`、`>=` 等比较两个值。
  + **逻辑运算符**：三个主要的逻辑运算符是 `&& (and)`、`|| (or)` 和 `! (not)`。它们通过评估表达式中的变量和值来返回 true 或 false。
  + **字符串、位、条件和类型运算符**。
* **使用正则表达式**、文本格式和新兴的国际化选项来处理字符串和显示文本。

### 控制流和错误处理

循环：JavaScript 支持几种类型的循环来重复执行操作：

* **For 循环**：迭代一定次数或循环遍历对象的属性 (For/In) 或值 (For/Of)。
* **While 循环**：只要指定的条件为 true，就继续执行。
* **Do/while 循环**：先执行一次代码块，然后只要指定的条件为 true，就重复执行循环。

使用 break 和 continue 语句来控制循环中代码的流程。

* **条件语句**：这些语句允许在代码中进行决策，通过执行不同的代码块。`if/else` 语句在指定的条件为 true 时执行一个代码块，而在条件为 false 时执行另一个代码块；使用 `else if` 添加进一步的语句来测试。switch 语句用于选择要执行的多个代码块中的一个。
* **错误处理**：使用 `try...catch` 语句处理错误和异常。try 块包含可能引发错误的代码；用于处理该错误的代码位于 catch 块中。使用 final 块来处理无论是否发生错误都将执行的代码。

### JavaScript 函数和作用域

* **函数**：执行特定任务的可重用代码段。它们是 JavaScript 代码的基本构建块，使用 function 关键字声明。
* **表达式**：任何解析为值的有效代码单元——包括变量、字面量、运算符和函数调用——都是 JavaScript 表达式。如果将函数赋值给变量，创建一个函数表达式，则可以省略函数名。
* **箭头函数**：ES6 中引入的箭头函数允许您更简洁地编写函数。您不需要 function 关键字，如果函数由单个表达式组成，则不需要 return 关键字。它们对于短函数特别有用，但不能用作方法或构造函数。
* **闭包**：JavaScript 中的闭包是一个可以访问更广泛变量作用域的特定函数：它自己的作用域、外部函数的作用域和全局作用域。闭包非常强大。您可以使用它们来创建模块化、可重用的代码，在使用异步操作时保留状态，或模拟私有方法和变量，但它们也可能导致内存泄漏和其他意外行为。

### 浏览器中的 JavaScript：DOM 操作、事件

虽然 [JavaScript 语言](https://thenewstack.io/javascript/) 不再只在浏览器中运行，但由于它最初是一种 Web 脚本语言，因此它具有用于处理网页的特定选项：

* **DOM 操作**：文档对象模型 (DOM) 是允许 JavaScript 更改网页的内容和结构的接口，使其具有动态性和交互性：创建、删除或修改 HTML 元素和属性，并实现对页面结构和内容的动态更新。
* **事件**：JavaScript 可以对用户在网页上的操作做出反应——单击按钮、移动光标、按键和输入文本——以显示导航菜单、弹出窗口和其他与页面交互的方式。JavaScript 允许开发人员使用事件侦听器 (addEventListener) 跟踪单击、鼠标移动、按键或表单提交等事件，并定义在事件发生时执行的 JavaScript 函数（事件处理程序）。

## 高级 JavaScript 概念

虽然您可以使用相当简单的 JavaScript 使网页具有交互性，但对于复杂的应用程序，您需要求助于更复杂和强大的编程技术。

### 函数式和面向对象编程

* **JavaScript 支持函数式和面向对象编程 (OOP)**。函数式编程将数据视为不可变的，并将函数视为可以作为参数传递给其他函数、由函数返回和赋值给变量的一等公民。虽然 JavaScript 不强制执行不变性，但函数式模式——例如避免副作用并将函数视为一等公民值——被广泛使用和鼓励。JavaScript 中的 OOP 使用原型机制，JavaScript 对象通过该机制继承特性，因此它的工作方式与经典的面向对象编程语言略有不同。
* **类和对象**：JavaScript 类建立在原型之上，是构造函数和原型的语法糖，为创建对象提供了更清晰的语法。对象是具有属性和方法的类的实例，因此 `Car` 类可能具有诸如品牌和颜色之类的属性，或者诸如 `start()` 之类的方法。使用类将数据与将对该数据进行操作的代码封装在一起。
* **继承和多态**：基于现有类创建新类允许子类重用父类的方法和变量。使用 `extends` 关键字，可以将一个类声明为另一个类的子类。您可以使用多态性来覆盖父类中在子类中无用的任何方法，以执行不同的操作。这对于在代码中创建分层结构、减少冗余和增强可重用性非常有用。例如，电动汽车类可以扩展汽车类，继承其属性并添加诸如电池容量之类的新特性，但会覆盖在加注燃油后未更换油箱盖的警告，并使用代码来检查汽车是否仍然插电。
* **模块和命名空间**：还有其他方法可以在 JavaScript 中组织和封装代码。模块允许您将代码分解为单独的文件（对于大型代码库很有用），或者您可以使用命名空间对象将代码的函数组织到本地组中。如果您想要一种更正式的结构化选项来处理命名空间，TypeScript 会添加一个命名空间关键字。虽然 TypeScript 包含命名空间关键字，但现代代码通常更喜欢 ES6 模块语法 (import/export) 来实现结构和封装。

### 异步编程：回调、Promise、Async/Await

因为 JavaScript 是单线程的，但也经常在浏览器中运行，所以它需要一种运行代码而不阻塞主线程并减慢您正在查看的网页呈现速度的方法。长时间运行的任务会委托给浏览器的后台进程，当它们完成时，会触发一个回调函数来处理结果。诸如网络请求或计时器之类的任务由浏览器 API（在 JS 引擎之外）处理，一旦完成，它们的回调就会被放置在消息队列中，以便由事件循环拾取。

* **回调**：回调是一个作为参数传递给另一个函数并在稍后执行的函数。回调在 JavaScript 中启用异步编程，但很难编写和调试。
* **Promise**：在 ES2015 中引入以处理回调的复杂性，Promise 是一个对象，表示异步操作的最终结果——完成或失败。[Promise](https://thenewstack.io/what-are-promises-in-javascript/) 抽象了异步行为，并使用 `.then()` 和 `.catch()` 提供了一种更简洁、可链接的回调替代方案。
* **生成器**：虽然生成器不直接等待 Promise，但它们可以通过生成 Promise 来编写异步代码——通常通过辅助库或异步流控制进行管理。
* **Async/await**：async/await 语法已在 ES2017 中添加，以便更轻松地使用 Promise 和生成器，并编写看起来更像同步代码的异步代码。在函数之前放置 `async` 关键字以将其标记为异步，并在函数内部使用 `await` 关键字以暂停函数代码的执行，直到 Promise 被解析，然后恢复代码。

## JavaScript 框架和库

虽然您可以使用 JavaScript 从头开始创建交互式网页和应用程序，但框架和库使生活更轻松，为您提供用于常见任务的内置函数（这提高了代码的一致性和可靠性），补充了语言中缺失的功能，提高了跨平台兼容性，以便应用程序可以在更广泛的设备上运行，优化了性能，并使您可以获得来自活跃的开发人员社区的支持。学习它们可能需要做更多的工作，但框架和库提供了结构、模式和额外的工具。

### 流行的 JavaScript 框架：Angular、Ember.js、Vue.js、Babylon.js

* **Angular**：Angular 由 Google 维护，是一个广泛使用的框架，用于构建单页应用程序 (SPA)。它具有用于模块化的基于组件的架构，使用模板来简化创建 UI 视图，并具有丰富的功能，如双向数据绑定、模块化、AJAX 处理和依赖注入。Angular 具有陡峭的学习曲线，但有很多课程和教程，它非常适合构建大规模、高性能的应用程序。不要将它与旧的 Angular.js 混淆，Google 不再开发或支持它。
* **Ember.js**：Ember 是另一个基于组件的框架，用于创建 SPA，它使用模板，提供使其可以快速上手的默认行为，是强烈主观的（以至于所有应用程序都具有相同的结构），并且具有自己的内置路由器、状态管理和开发环境，具有 Inspector 和 Ember CLI，某些其他库（如 Glimmer.js）已采用。
* **Vue.js**：Vue.js 是一个更简单的渐进式框架，用于构建用户界面、SPA 和更小的项目，旨在易于上手并添加到现有项目中。核心库仅关注视图层，并处理数据绑定、CSS 过渡和动画，但您可以添加路由器、调度和 CLI 以进行项目脚手架，并引入更多库（如果您想构建更强大的 SPA）。
* **Babylon.js**：Babylon.js 是一个基于 WebGL 和 JavaScript 的强大 3D 引擎，您可以将 Babylon.js 用作显示 3D 模型和场景的库，或用作具有内置组件的框架，可以帮助您构建复杂的交互式 3D 应用程序。

### JavaScript 库生态系统：React、jQuery、Lodash、Moment.js、D3.js

* **React**：React 由 Facebook（现在是 Meta）开发，是一个声明式、高效且灵活的 JavaScript 库，用于构建用户界面和用于动态应用程序的可重用组件。React 非常强大，通常被视为一个框架。它的虚拟 DOM 优化了对实际 DOM 的更新以提高性能，使开发人员能够创建可以在不重新加载页面的情况下更改数据的大型 Web 应用程序。您需要学习它的 JSX 标记语法，并且它不处理任何服务器端逻辑，但是有一个强大的社区，其中包含许多学习资源。
* **jQuery**：一个持久流行的 JavaScript 库，但随着 ES2015 以来语言的改进，[jQuery](https://thenewstack.io/why-outdated-jquery-is-still-the-dominant-javascript-library/) 处理的许多任务现在可以直接在 JavaScript 中完成。您可能仍然需要它用于依赖它来简化 HTML 文档操作、事件处理、动画和 Ajax 交互的旧项目，但它不太可能成为您新项目的首选。
* **Lodash**：一个实用程序库，通过消除处理数组、数字、对象、字符串等的麻烦来使 JavaScript 更容易，Lodash 具有模块化方法，非常适合迭代数组、对象和字符串；操作和测试值；以及创建复合函数。
* **Moment.js**：多年来，Moment.js 一直是事实上的日期库，但新的 Temporal API（第 4 阶段，在 Node.js 20+ 和现代浏览器中可用）现在是一个标准的替代品。
* **D3.js**：Data-Driven Documents (D3.js) 是一个用于使用 SVG、HTML 和 CSS 而不是专有框架生成动态、交互式数据可视化的库。

### 选择合适的 JavaScript 框架/库：要考虑的因素

当有多个选项时，以选择任何其他开发工具的方式在它们之间进行选择：

* **项目需求**：评估项目的特定需求。对于复杂的企业级应用程序，可能适合使用像 Angular 这样的综合框架。对于具有可重用组件的动态界面，React 是一个不错的选择。对于较小的项目或特定的功能（如数据可视化），可能只需要像 D3.js 这样的库。
* **学习曲线**：考虑学习框架或库所需的时间和精力。React 的学习曲线比 Vue.js 更陡峭，但在大型应用程序中提供了更大的灵活性。
* **社区和生态系统**：强大的社区和生态系统意味着更好的支持、更多的资源——包括文档和教程来帮助您学习——以及框架或库被定期维护和更新的可能性更高。确保快速解决库或框架的任何安全问题。
* **性能**：评估框架或库对您的特定用例的性能影响，因为虽然它们可能提供缓存、压缩、延迟加载或缩小以加快您的应用程序速度，但框架本身的大小和开销最终可能会使您的整体应用程序更大或更小。考虑加载时间、运行时效率和内存消耗等因素。
* **兼容性和灵活性**：查看项目中使用的其他工具和技术，并确保您正在考虑的库或框架与它们配合良好。提前计划：如果您希望添加新特性和技术，那么从一开始就采用支持这些特性的框架可能比在应用程序增长时重写以使用它更有价值。

使用现代 JavaScript，完全可以在没有框架和库的情况下编写强大的应用程序，但选择合适的框架和库可以提高应用程序的性能、效率、可维护性和可扩展性。选择最适合您的项目需求、复杂性和长期目标，以及团队的专业知识和偏好的框架和库。

## 现代 Web 开发中的 JavaScript

JavaScript 已经从仅仅在网页中编写交互脚本发展而来。现代 Web 开发允许开发人员创建具有丰富用户界面和您在桌面应用程序中期望的所有功能的动态、交互式 Web 应用程序，无论是使用 Angular 等框架构建的 SPA，还是运行与前端界面相同 JavaScript 代码的服务器端应用程序，还是使用 Web 技术构建但利用设备上的原生特性的跨平台桌面和移动应用程序。

### 单页应用程序：由 JavaScript 提供支持

SPA 通过让浏览器加载单个 HTML 页面并在用户与应用程序交互时动态更新内容，从而更轻松地构建感觉像应用程序的复杂网站。与传统网站（其中每个页面都是独立的，具有自己的 HTML、CSS 和 JavaScript，并且必须单独维护）不同，SPA 包含整个网站的代码（尽管现代 SPA 通常使用代码拆分来仅在最初加载应用程序的必要部分）。Angular、Ember.js、[React.js](https://thenewstack.io/javascripts-history-and-how-it-led-to-reactjs/) 和 [Vue.js](https://thenewstack.io/meet-vue-js-flexible-javascript-framework/) 等框架提供了结构化的方式来使用 JavaScript 创建响应式和交互式用户界面，无论您是创建移动应用程序还是动态网页。

这种方法避免了页面重新加载，提供了更快、更流畅的用户体验，减少了加载时间，使应用程序感觉更灵敏，并且通过仅下载新数据而不是每次都下载整个页面来减少移动设备的带宽和对电池寿命的影响。使用 JavaScript，SPA 能够实现更具吸引力的界面，包括动画、过渡、拖放交互、推送通知、离线模式和其他使 Web 应用程序感觉更像原生应用程序的功能——尽管您可能需要使用 service worker 和其他高级 JavaScript 功能来支持这些选项。

尽管名称如此，您可以将功能强大且复杂的网站（如 Netflix、Gmail 或 Facebook）构建为 SPA。如果您想要身份验证和推送通知等更高级的功能，您也需要后端代码。SPA 还可以为前端和后端使用相同的 JavaScript 代码，从而简化开发并使其更易于调试和维护。

### 除了 SPA 之外：渐进式 Web 应用程序、Web 组件和 VR

**渐进式 Web 应用程序：** 您可以在 SPA 中构建的许多更有趣的功能都依赖于 service worker 和 Web API。渐进式 Web 应用程序 (PWA) 更进一步。它们通过在本地缓存数据和资源以实现更快的响应和离线使用，使用 service worker 来处理网络请求（包括推送通知），以及模仿原生应用程序的外观和感觉，并可以选择（取决于操作系统）将它们安装在设备的首页上并从应用程序启动器访问它们，从而提供与 SPA 相同的好处。此外，代码拆分允许 PWA 仅加载当前视图的代码，这可以提供比 SPA 更快的初始加载速度。

PWA 在浏览器强制执行的沙盒环境中运行，并且 service worker 在隔离的线程中运行。结合 HTTPS 要求，这有助于防止常见的攻击，如 XSS 和 CORS 滥用。您可以远程更新它们以解决安全问题。它们对于 SEO 也更容易被发现。

缺点是 PWA 比仅在客户端上运行的 SPA 更复杂且成本更高，但某些 SPA 也需要后端组件。

**Web 组件：** Web 组件在十多年前推出，直到 2018 年才在所有主要浏览器中得到支持，因此采用速度一直很慢。但是，在 JavaScript 中使用这些 Web 平台 API 创建具有自己的内容、样式和功能的自定义 HTML 元素，使开发人员能够创建封装的、可重用的、可访问的组件，这些组件不需要特定的框架或库（但它们也可以与您已使用的任何框架或库一起使用）。

**VR：** WebVR 是一个 JavaScript API，使开发人员可以访问虚拟现实设备的特性和传感器，从而使他们可以在其 Web 应用程序中呈现立体视图。它已被弃用，取而代之的是 WebXR 设备 API，但了解其基础知识对于学习基于 Web 的 VR 开发可能很有帮助。

### 服务器端 JavaScript：从 Node.js 到无服务器

* **Node.js：** 通过 Node.js 将 JavaScript 带到服务器彻底改变了该语言的功能。Node.js 是一个构建在 Chrome 的 V8 JavaScript 引擎之上的 JavaScript 运行时，它使用事件驱动的非阻塞 I/O 模型，使其轻量且高效，非常适合在分布式设备上运行的数据密集型实时应用程序。它不再是唯一的服务器端运行时：Deno 和 Bun 也很受欢迎。
* **Express.js：** 此框架提供路由系统、中间件支持、模板引擎和错误处理，以简化使用 Node.js 创建 Web 服务器和 API 的过程。它具有可扩展性和轻量性，简化了编写服务器端逻辑和处理 HTTP 请求的任务。
* **无服务器：** JavaScript 运行时可以在不同的环境中运行，包括边缘计算和诸如 [AWS](https://aws.amazon.com/?utm_content=inline+mention) Lambda、[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure Functions、Cloudflare Workers、[Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Functions 和 Vercel Functions 之类的无服务器平台，使开发人员能够在没有管理服务器基础设施的情况下运行代码片段以响应事件。

### 获取数据、RESTful 服务、使用 Jamstack 进行预构建

JavaScript 在与 API 交互以获取数据方面起着至关重要的作用。JavaScript 中的 fetch API 允许 Web 浏览器向 Web 服务器发出 HTTP 请求，从而获取或发送对 Web 应用程序至关重要的数据。这对于加载新内容、提交表单或与第三方服务交互等功能至关重要。

您想要使用的所有 API 不太可能内置在浏览器中。JavaScript 可以使用 API 来访问和操作来自各种网站和第三方服务的数据，从而使您可以创建动态、交互式网站和 Web 应用程序。JavaScript 可以向 REST API 发送请求，这些 API 使用 HTTP 方法并以 JSON 或 XML 格式返回响应。由于其与 JavaScript 的原生兼容性，大多数现代 REST API 都使用 JSON 作为请求和响应正文。您可以使用 REST API 与后端数据库交互、向 Web 应用程序添加地理位置或在网站上播放音乐。

JavaScript 中的异步选项，尤其是 Promise 和 async/await，简化了处理来自 API 的响应。这允许应用程序保持响应性和高性能，即使在发出多个后台数据请求时也是如此。

如果您不需要复杂的交互或实时更新，并且可以使用来自 CDN 的静态、预构建的 HTML 文件，而不是根据需要构建它们在服务器上，那么 Jamstack（JavaScript、API 和标记）架构方法可能很有用。它使您可以构建将所有逻辑移动到客户端的站点，后端由 API 和无服务器函数组成，所有交互都在页面中生成，身份验证和授权由第三方 API 处理。它可以帮助您提高安全性、性能并降低成本。

## JavaScript 中的最佳实践

通过遵循以下 JavaScript 实现原则来创建健壮、可维护和安全的代码，从而使您的生活更轻松。

### 代码质量：编写干净、可读的代码

* **清晰简洁：** 力求 JavaScript 代码的简洁性。避免不必要的复杂性，力求清晰，不要使您的代码过于缩写，以至于您忘记了它是如何工作的。这使代码更具可读性，并且更容易让其他人（或未来的您自己）理解和维护。
* **一致的编码风格：** 采用一致的编码风格，包括命名约定、缩进和注释。ESLint 等工具可以帮助强制执行编码标准，确保统一的代码库——尤其是在团队环境中。
* **使用描述性的变量和函数名称：** 选择清楚地表明变量和函数的目的和用法的名称。描述性名称使您的代码具有自我记录性，并减少了对过多注释的需求。
* **代码注释和文档：** 在记录代码之前，代码尚未完成。解释当时看起来很明显的决定将有助于以后处理代码的任何其他人——包括您，当您不得不在几个月或几年后重新启动一个项目时。
* **代码重构：** 除了修复特定的错误外，还可以重构您的代码以提高其结构和可读性。重构代码的编写方式而不改变其功能有助于您在技能发展时改进旧代码。有一些开发人员工具可以帮助您做到这一点。

### 性能优化：高效 JavaScript 编码的技巧

* **高效的 DOM 操作：** 尽量减少与文档对象模型 (DOM) 的直接交互，因为这些交互可能会消耗大量性能。使用文档片段或在重新呈现之前更新屏幕外的 DOM。
* **优化循环：** 对循环要小心，尤其是在其他循环中，因为这些循环会严重影响性能。在适当的情况下使用内置方法，如 `forEach`、`map`、`filter` 或 `reduce`。
* **异步加载：** 使用异步 JavaScript 加载脚本，而不会阻止页面的呈现。这提高了加载时间和应用程序的整体性能。
* **内存管理：** 不必要的变量或数据结构可能导致内存消耗增加。通过取消引用未使用的对象来有效地使用垃圾回收，但让 JavaScript 为您处理垃圾回收。

### 安全注意事项：常见漏洞、安全编码实践

* **避免全局变量：** 尽量减少全局变量的使用，以降低代码冲突和潜在安全问题的风险。
* **验证用户输入：** 始终验证和清理用户输入，以防止常见的漏洞，如跨站点脚本 (XSS) 和 SQL 注入，但不要通过拒绝您可以自动重新格式化的输入（如电话号码的结构）来让用户感到沮丧。
* **更新 API 和库：** 确保您使用的是安全且更新的 API 和库版本。定期检查修复漏洞的更新或补丁。
* **实施错误处理：** 强大的错误处理可以防止您的代码暴露敏感信息和系统详细信息。它将使您的站点或应用程序对用户来说不那么令人沮丧。

## JavaScript 中的学习和社区资源

凭借 JavaScript 生态系统的规模，有很多资源可以学习和保持更新。无论您是初学者还是经验丰富的开发人员，都有一些课程和教程可以帮助您提高技能并及时了解 JavaScript 开发的最新趋势。

### 学习路径：JavaScript 教程和在线课程

* **在线课程：** Coursera、edX、Udemy 和 Pluralsight 等常见平台提供全面的课程来学习 JavaScript，涵盖从基本基础知识到高级概念的所有内容。这些课程通常包括有助于巩固学习的实践项目，但它们通常不是免费的。
* **交互式教程：** Codecademy、Educative.io、freeCodeCamp、[JavaScript 30](https://javascript30.com/) 和 JavaScript.info 等网站提供交互式教程和练习，帮助您按照自己的节奏学习。有些是免费的；有些则需要订阅。[Learn JavaScript](https://learnjavascript.online/) 是一组来自 Google 的关于 JavaScript 的免费课程和教程。
* **视频教程：** 除了 [freeCodeCamp](https://www.youtube.com/playlist?list=PLWKjhJtqVAbleDe3_ZA8h3AO2rXar-q2V) 等教程网站提供的 YouTube 频道外，还有许多由业余和专业讲师提供的免费、高质量的视频教程——如 Academind、The Net Ninja、[Programming with Mosh](https://www.youtube.com/c/programmingwithmosh) 和 Traversy Media。[freeCodeCamp 的 134 部分视频教程](https://www.youtube.com/watch?v=PkZNo7MFNFg) 是一个不错的起点。Microsoft 在其 Learn 站点上提供了一个 [适用于 JavaScript 初学者的优秀视频教程系列](https://learn.microsoft.com/en-us/shows/beginners-series-to-javascript/)。
* **文档：** MDN Web Docs 是 Web 技术的权威文档站点，[包括 JavaScript](https://developer.mozilla.org/en-US/docs/Web/javascript)，并包含一系列教程。[caniuse](https://caniuse.com/) 网站将帮助您检查特定 JavaScript 特性在哪些浏览器和平台上受支持。

### JavaScript 社区和支持：论坛、GitHub、Stack Overflow

* **论坛和讨论区：** DEV.to、Stack Overflow、Reddit (r/javascript) 和 MDN Web Docs 论坛等在线社区非常适合寻求帮助、分享知识以及与其他 JavaScript 开发人员建立联系。
* **GitHub：** GitHub 不仅用于代码共享；它也是一个用于协作和学习的平台。探索开源 JavaScript 项目可以深入了解真实世界的代码和开发实践。
* **聚会和本地团体：** Meetup.com 等平台通常列出本地 JavaScript 和 Web 开发团体。参与这些团体可以提供社交机会和社区意识。

### 保持更新：博客、会议、播客和标准

* **博客和新闻通讯：** 关注 JavaScript Weekly、Smashing Magazine 和（尽管名称如此）CSS-Tricks 等博客，以获取最新新闻、文章和教程。新闻通讯是直接在您的收件箱中接收精选内容的好方法。
* **会议和网络研讨会：** 参加 JavaScript 会议和网络研讨会，如 JSConf、React Conf 和 Node.js Interactive。这些活动是从行业专家那里学习和与同行交流的机会。
* **播客：** 如果您想学习 JavaScript 并且您是一个音频而不是视觉学习者，或者您想在休息屏幕时赶上进度，请收听 [20minJS](https://20minjs.com/)、[Full Stack Radio](https://fullstackradio.com/)、[JavaScript Jabber](https://topenddevs.com/podcasts/javascript-jabber)、[Syntax](https://syntax.fm/) 或 [WebRush](https://webrush.io/) 等播客。这些播客可以是一种信息丰富且方便的方式来了解 JavaScript 的最新信息。一些播客，如 [Igalia Chats](https://www.igalia.com/24-7/chats)，其中经验丰富的浏览器工程师介绍了关键的 Web 功能，都有完整的文字记录。
* **标准机构：** 请记住，JavaScript 在不断发展；即使是经验丰富的 JavaScript 开发人员也需要保持最新状态。您需要检查修复错误或替换第三方框架的新语言特性。您可以关注在 GitHub 上创建 ECMAScript 标准的 [TC39 社区](https://tc39.es/) 的工作，或者跟踪跨行业 [Interop 项目](https://github.com/web-platform-tests/interop) 的优先级。

## JavaScript 的结论和未来

JavaScript 语言不仅是当前 Web 开发的主要内容，也是浏览器内外未来创新的驱动力。

### 不断变化的格局：JavaScript 趋势

JavaScript 的未来看起来与您可以使用它构建的应用程序和站点一样充满活力和动态。JavaScript 运行时的大量可用性使其与无服务器计算和物联网等新兴领域相关。JavaScript 还 [补充了 WebAssembly 等技术](https://thenewstack.io/webassembly/will-javascript-become-the-most-popular-webassembly-language/)，后者越来越多地用于浏览器内外对性能至关重要的任务。框架和库在不断发展，新的选项不断涌现，以解决特定的挑战和需求，即使经过验证的特性已成为该语言本身的一部分而标准化。

### JavaScript 职业机会和 JavaScript 技能

对熟练的 JavaScript 开发人员的需求仍然很高。精通 JavaScript 为各种职业机会打开了大门，包括前端和后端开发、移动应用程序开发等等。

### 最后的想法：鼓励持续学习

JavaScript 语言仍然很受欢迎，因为它使开发人员能够为各种场景快速编写代码，并在越来越多的环境中运行该代码。主要的浏览器制造商继续在 JavaScript 引擎中提供出色的性能，并且社区继续找到新的方法来利用这一点。这意味着 JavaScript 开发人员总是有新的东西要学习；请放心，The New Stack 将使您及时了解最新的 JavaScript 发展。