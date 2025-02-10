
<!--
title: 如何使用ChatGPT构建Web Components
cover: https://cdn.thenewstack.io/media/2025/02/62417fe4-aakash-dhage-en8upg7tuou-unsplashb.jpg
-->

借助 AI 的帮助，我们可以驾驭原生 Web 平台（包括自定义元素），而无需 JavaScript 工业复合体。

> 译自 [How To Build Web Components Using ChatGPT](https://thenewstack.io/how-to-build-web-components-using-chatgpt/)，作者 Jon Udell。

我一直在思考 [web components](https://thenewstack.io/introduction-to-web-components-and-how-to-start-using-them/) 很长时间。在 1996 年 BYTE 题为 [On-Line Componentware](https://web.archive.org/web/19961220012005/http://www.byte.com/art/9611/sec9/art1.htm) 的故事中，我展示了网站也是可编程的构建块。那是在 Web API 出现之前很久，正如 Tim O’Reilly 在 2007 年一篇关于 [Yahoo! Pipes](https://web.archive.org/web/20070209230148/http://radar.oreilly.com/archives/2007/02/pipes_and_filte.html) 的文章中指出的那样：

> *“早在 1997 年夏天，在我们的第一次 Perl 会议上，Jon Udell 发表了一次让我激动的演讲。Jon 表达了一种愿景，即将网站视为可以重用的数据源，以及一种将整个互联网作为其平台的新编程范式。这远早于 Web 服务的流行。”*

Gartner 分析师 Mark O’Neill 在最近的 [LinkedIn post](https://www.linkedin.com/posts/markwoneill_ai-agents-represent-an-existential-moment-activity-7291846704817991680-3eqJ/) 中（向我 1996 年的文章致敬）认为，我们现在正在进入后 Web-API 时代。

> *“如果真正的 Web API 一直就在我们面前呢？如果它……只是 Web 本身呢？自 2000 年以来，科技史的教训是“Web 总是赢”（有人还记得 WAP 和 WML 吗？）。”*

在评论中，API 专家 Kin Lane 补充道：

> *“只是为了让大家知道，Mike Amundsen 一直在说 web 就是 API。”*

O’Neill 的观点是，LLM 绕过 API，直接与人类可读的 web 交互。三十年前，我意识到网站是适合以编程方式抓取的粗粒度组件。现在我们不需要编写抓取器，AI 可以更有效地为我们完成。但是，还有另一种思考 web components 的方式。

## 从 VBX 到 React

我 1996 年的文章提到了 1994 年 BYTE 的封面故事，题为 [Componentware](https://web.archive.org/web/19961220155530/http://www.byte.com/art/9405/sec5/art1.htm)，其中认为：

> *“VBXes（Visual Basic 自定义控件）今天最好地例证了数十年来的可重用软件概念，这一事实让包括 Microsoft 在内的所有人都感到惊讶。”*

我们中的许多人曾认为，广泛软件重用的引擎将是链接到由熟练程序员编写的程序中的底层对象库。令人惊讶的是，真正获得关注的是由专业开发人员构建并由业务开发人员使用的组件。VBX 生态系统提供了用于图表绘制、网络通信、数据访问、音频/视频播放和图像扫描/编辑的控件。UI 控件包括按钮、对话框、滑块、用于显示和编辑表格数据的网格、文本编辑器、树和列表以及选项卡视图。人们使用这些控件来构建销售点系统、调度和项目管理工具、医疗和法律实践管理系统、销售和库存报告等等。

在 VBX 时代，没有通用的组件重用平台。现在有了，但它不是 React——它是 web 浏览器。

组件生产者和消费者的生态系统并没有延续到 web。我们看到了 [React components](https://thenewstack.io/react-server-components-in-a-nutshell/) 形式的苍白反映，但它们不适用于 20 世纪 90 年代可以有效地使用 Visual Basic 组件的那种开发人员。您不仅需要成为一名熟练的程序员才能创建 React component，还需要成为一名熟练的程序员才能使用它。此外，当然，这些组件绑定到 React 框架。在 VBX 时代，没有通用的组件重用平台。现在有了，但它不是 React——它是 web 浏览器，它已经成熟和标准化到我无法预测的程度（但我很高兴看到）。
对 React 的抵制（[复杂性的商人](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/)，[JavaScript 工业复合体](https://infrequently.org/2024/08/the-landscape/)）正确地关注了其复杂性和脆弱性如何成为开发者和用户都要付出的代价。那应该用什么代替呢？像 [Alex Russell](https://www.linkedin.com/in/alexrussell/) 这样的评论家说，应该倾向于原生 Web 技术。构建渐进式 Web 应用程序，使其作为由简单 CSS 和 JS 支持的原生 HTML 工作，然后叠加现代 Web API 以匹配原生应用程序的体验。对于组件，这意味着避开非标准的 React 组件，而选择标准的 [Web components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)。这种转变的典型例子是 Edge 浏览器，它正在[用 Web components 替换 React 组件](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/)。

## 使用 Web Components

构建和使用 Web components 是什么样的体验？五年前，我试水并用它来制作一个[搜索和查看 Hypothesis 注释](https://jonudell.info/h/facet)的工具。当时已经出现了像 [Lit](https://lit.dev/) 这样的框架，但我希望了解直接使用原生 Web 平台是什么感觉。坦率地说，这不是一次很好的体验。不是因为 Web components 本身比原生平台的任何其他部分更复杂，而是因为掌握整个过程都具有挑战性。这种认知负担是框架旨在解决的问题之一。

> 我们的 AI 助手了解原生平台的所有信息，使我们能够更有效地使用它。

现在情况不同了。我们的 AI 助手了解原生平台的所有信息，使我们能够更有效地使用它。因此，现在似乎是尝试一个实验的好时机。对于组件开发者来说，现在创建简单的库，使组件用户能够以声明式风格，使用 HTML 和 CSS 以及最少的 JavaScript，*无需*像 React 这样的框架来构建基本的 Web 应用程序，这在多大程度上是可行的？

以下是我对一个提供和显示城市表格（或任何其他内容）的应用程序的想法：

```html
<layout-box layout="horizontal" align="center" responsive>
  <data-source id="citiesDS" table="cities" />
  <app-form for="citiesDS" required="city,state">
    <layout-box layout="vertical">
      <h2>Cities</h2>
      <text-box style="width:15em" name="city" placeholder="Keene" />
      <text-box style="width:2em" name="state" placeholder="NH" />
      <text-box style="width:4em" name="population" placeholder="23000" />
      <app-button style="text-align: left;" label="Add City" />
      <list-view style="text-align: left;" for="citiesDS" fields="city,state,population">
        <list-card />
      </list-view>
    </layout-box>
  </app-form>
</layout-box>
```

## 一组最基本的自定义元素

作为此应用程序的作者，您只需编写一些基本的 HTML 和可选的 CSS 来声明数据源、输入字段和用于显示记录的视图。[支持库](https://github.com/judell/SimpleWebComponents)总共只有 260 行代码，定义了 HTML 中使用的自定义元素：

- layout-box
- data-source
- app-form
- text-box
- list-view
- list-card
- app-button

这些库虽然很小，但确实使 HTML 作者（组件使用者）能够实现基本的数据输入和显示。对我（组件生产者）来说，使它们的构建成为可能的是，当然，AI 辅助。

我计划使用 ChatGPT o1，但考虑到这将是一次漫长的对话，并且考虑到 o1 严重的速率限制，我使用了 Claude 和 ChatGPT 4o 来启动工作。这是最初的提示：

*我正在寻找一个 Web components 库，它的特点是绝对的简单性和极简主义，没有依赖项。*

我非常确定没有这样的库，但问一下总没坏处。没有出现任何类似我所想的东西，所以我们开始了。

第一个概念验证通过使用浏览器的本地 `IndexedDB` 来回避存储问题，并通过避免布局和样式来回避设计问题。该练习的目的是创建足够输入和显示数据的一小部分 Web components，并支持一种 HTML 编写体验，该体验不需要任何特殊知识即可使用它们。

> 几乎立即我就有了一个基本的自定义元素库和一个简单的测试应用程序来练习它们。

完成该过程是重新熟悉 Web components（Web components 的基础）的最佳方式。几乎立即，我就有了一个基本的自定义元素库和一个简单的测试应用程序来练习它们。迭代以我们逐渐习以为常的方式进行：尝试一个变体，如果失败则分享错误的屏幕截图，或者，如果成功，则讨论结果的优缺点和后续步骤。有了概念验证，我切换到 o1 来解决我们搁置的问题。

## 与 ChatGPT o1 合作

我想要使用 SQL 来代替 `IndexedDB`，并且本着极简主义的精神，我希望引擎是 `sqlite`。此前，Claude 曾帮助我编写了一个[嵌入 SQLite 的轻量级 httpd](https://github.com/judell/sqlite-server/)，下一步是调整该库的数据层以使用它。这就是 o1 的推理能力发挥作用的地方。

![](https://cdn.thenewstack.io/media/2025/02/c0cf2e7a-components-refactor-db.png)

*来自ChatGPT的组件重构建议*

事情进展基本按计划进行，但有一个小问题。在初始页面加载时（且仅在此时），查询运行了两次。为什么？自定义元素的事件流需要调整。我自己可能需要一段时间才能找到解决方案，但我不需要。o1 提供了几个替代方案；我们讨论了优缺点，我选择了一个，然后继续前进。

接下来：简化应用程序作者的体验。最初的 `index.html` 包含大量的 JavaScript 代码，但我希望一切都是纯声明式的。满足这一要求引发了一场关于不透明接口（组件生产者更容易创建）和可扩展接口（组件消费者可能要求使用）之间由来已久的权衡的讨论。o1 提出并实现了一组可扩展性钩子。最后，我没有包含这些钩子，因为 YAGNI（“你不需要它”），但如果需要，有一个合理的推进路径。

## 风格问题

如果不需要 JavaScript，那么隐藏 CSS 怎么样？我们尝试启用自定义元素来接受对齐、宽度、背景和颜色等内容的简化声明。对于布局组件来说，这感觉还可以，可以用一些语法糖来美化 flex 模型，但其他情况则不然。当 o1 开始尝试重新发明样式继承时，我吹响了哨子并扔下了罚旗。对于执行简单数据录入和显示且不需要主题化的日常应用程序来说，应用程序作者使用一些标准 CSS 并不算过分。

这个快速而廉价的实验暴露了一个结构缺陷。列表组件最初是卡片组件的容器，这些卡片组件是列表内部的，应用程序作者看不到也无法设置样式。这就是将我们推向继承的滑坡的原因。但是这种嵌套不需要像这样隐式：

```
<list ...> </list>
```

最好像这样显式：

```
<list ...> <card ...> </card> </list>
```

因此，我们相应地重构了 `list-view`。

## 演进组件库

就目前而言，该库是对常见模式的概念验证封装。它使 HTML 作者能够创建简单的应用程序，以声明方式实现基本的数据录入和显示，并由一组简单的 Web 组件提供支持。如何扩展这种方法来处理更广泛的模式？

为了激发这个练习，我让 ChatGPT 实现了一种不同的模式：多行选择 + 部分编辑。以下是应用程序的“源代码”：

一位销售人员从贸易展览会返回，带回了一组 CSV 文件中的扫描潜在客户：

```
firstname,lastname,company,email,notes
Alice,Johnson,TechCorp,alice.johnson@techcorp.com,
Bob,Smith,InnovateX,bob.smith@innovatex.com,
 ...
```

notes 列为空。

编写一个独立的 HTML/CSS/JS 应用程序，不依赖任何依赖项，使用文件上传来获取文件，解析记录，并构建如下形式的表单：

```
  for each contact, print
    firstname lastname
    company
    email
  
  then add two inputs
 
    text: notes
    checkbox:  [ ] add to hubspot
```

销售人员查看表单，选中一部分记录，向该部分记录添加注释，然后按提交将该部分记录发送到 HubSpot。这是 API 调用：

```
  curl --request POST \
    --url "https://api.hubapi.com/crm/v3/objects/contacts" \
    --header "Authorization: $TOKEN" \
    --header "Content-Type: application/json" \
    --data '{
      "properties": {
        "firstname": "Alice",
        "lastname": "Johnson",
        "company": "TechCorp",
        "email": "alice.johnson@techcorp.com",
        "custom_notes": "Sample note for Alice Johnson"
      }
    }
```

从这段“源代码”生成的应用程序在第一次尝试时就完美地工作了。组件库如何扩展以更通用的方式支持这种模式？与 o1 的讨论产生了一些想法，但没有明确的前进方向。一个更广泛有用的 Web 组件库需要考虑更广泛的模式。幸运的是，我们现在可以快速轻松地生成展示一系列此类模式的工作应用程序。并且随着将它们提炼成组件的机会出现，我们也可以快速轻松地生成这些组件。

JavaScript 工业综合体不会很快崩溃。但舞台已经为回归到业务开发人员可以访问的可重用组件生态系统做好了准备，只不过这次是基于通用 Web 平台及其核心标准。
