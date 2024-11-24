# 基于 React 的开源数据表格创建工具

![基于 React 的开源数据表格创建工具的特性图像](https://cdn.thenewstack.io/media/2024/11/d98417a9-aggridusethis2-1024x576.jpg)

[AG Grid](https://github.com/ag-grid/ag-grid) 的开发者关系负责人 James Swinton-Bland 并不认为 TanStack Table 是竞争对手。TanStack Table 是一个用于在 React 框架中创建表格的开源库，以前称为 React Table。相反，这家数据网格公司赞助 TanStack Table，并将 TanStack 视为合作伙伴。

“我们的创始人 Niall Crosby，他不幸最近去世了，非常热衷于支持开源社区和开源项目，尤其热衷于支持 Tanner Linsley，”Stinton-Bland 说。“Tanner 的 React Table 解决方案是无头的。这基本上意味着你必须自己构建 UI，必须自己设置样式，并且必须做很多基础工作才能使一切正常工作。”

AG Grid 是一个开源解决方案，是一个功能丰富的 JavaScript 数据网格库，用于在 Web 应用程序中构建交互式和复杂的数据表或网格。JavaScript 网格是一个 UI 组件，用于在 Web 应用程序中显示和管理表格数据。它提供了一种以行和列的形式呈现信息的结构化方式，使用户可以轻松理解和与数据交互。

他补充说，AG Grid 提供了一种将这些网格放入 Web 应用程序的方法。他补充说，它本质上就像 React Table，但“包含所有必要组件”。

“我能描述它的最简单的方式是，它是为 Web 开发人员构建的 Excel，”他说。“本质上，它允许你在 Web 应用程序中放置一个非常强大的表格。”

去年，该公司推出了 AG Charts，这是一个图表库，旨在支持 AG Grid 的集成图表功能，可以突出显示数据并从中构建图表。

“为了支持该功能，我们基本上必须构建一个完整的图表库来实现这一点，并且我们去年决定将其转变为自己的产品，”他说。“现在，AG Charts 是一个完全独立的 JavaScript 图表库，支持 React、Angular 和 Vue，与 AG Grid 非常相似。”

他补充说，这两个产品旨在无缝协同工作，但它们也可以用作独立的应用程序。

## 框架支持

Stinton-Bland 说，对于这两种产品，核心业务逻辑都是用 JavaScript 编写的，这使得解决方案非常快速。AG Grid 和 AG Charts 支持 React、Angular、Vue 和 JavaScript，并完全支持 TypeScript。Solid 曾得到支持，但由于兴趣低于预期，其优先级已被降低，他说道。但是，他补充说，Solid 确实提供了自己的 AG Grid 包装器。

“我们不受任何单个框架的限制，但实际上，我们在其之上为这些框架提供了全面支持，而且它不是一个薄的包装层或类似的东西，”他说。“例如，所有渲染都是用纯 React 完成的。通过这种方式，你可以获得用纯 JavaScript 执行逻辑的所有好处，但你也可以获得它像你期望的任何其他 React 库一样工作的所有好处。”

## AG Grid 的特性

Swinton-Bland 说，AG Grid 可以处理大量数据，而不会从 UI 角度看到任何滞后或性能下降。他们确保优化每个版本。

“由于所有核心业务逻辑都是用纯 JavaScript 编写的，例如，我们没有任何纯 React 库可能带来的开销，”他说。

![AG Grid 中的图表，显示了具有可调整行和列的网格的性能。](https://cdn.thenewstack.io/media/2024/11/3cc1515d-aggrid.jpg)

AG-Grid 示例页面的屏幕截图。

AG Grid 拥有所谓的客户端角色模型和服务器端角色模型。开发人员可以将所有数据交给 AG Grid，它将在客户端进行管理，或者开发人员可以实现服务器端行模型，这将需要开发人员弄清楚他们希望如何将数据从服务器发送到 AG Grid。Stinton-Bland 说，该产品提供的功能使你可以轻松建立这种连接。它还支持树形数据视图、主从视图等功能。
> “如果有更多嵌套数据或不同级别的数据，其中也有功能可以满足这些用例，” Swinton-Bland 说。“它真的非常通用。我认为我们找不到无法处理数据的用例。”

AG Grid 还开箱即用地实现了虚拟化，这意味着 AG Grid 不会一次性将所有数据加载到数据网格和浏览器中，而是加载您看到或希望用户看到的内容以及前后的一些数据。

> “很多其他数据网格也会做类似的事情，”他补充道。“他们也会实现虚拟化，但我们的实现方式的性能要好得多。”

最近，该公司在其网站上建立了一个新的社区版块。在 [tools and extensions](https://www.ag-grid.com/community/tools-extensions/) 下，有一个为 AG Grid 构建的生态系统列表，包括扩展和开源工具。

> “很多公司已经构建了设计系统和自定义主题，”他说。“他们为无代码、[低代码平台](https://thenewstack.io/what-a-low-code-platform-offers-frontend-developers/) 以及其他框架（如 .Net 和 Rust）构建了包装器和集成，AG-Grid 周围和之上构建的生态系统的规模之大，真的让我感到非常惊讶。”

该公司最近收到的功能请求较少，因为“用户请求的功能很少是我们还没有办法实现的。” 尽管如此，AG Grid 仍然接受开发人员的功能请求。

> “[Web 开发](https://roadmap.sh/roadmaps?g=Web+Development)是一个不断发展和变化的领域，因此我们投入了大量精力来维护我们迄今为止构建的所有内容，” Swinton-Bland 说。“AG Charts 现在也是我们的一大重点。作为一个全新的产品，我们不断发布新功能、新系列类型，并努力发展该产品。”

**竞争对手**

AG Grid 将其客户列为亚马逊、Facebook、微软、PayPal 和 FedEx 等。虽然它是创建数据网格和表格的流行开源解决方案，但它并非唯一的开源解决方案。开源竞争对手包括：

*   [Material UI](https://github.com/mui/material-ui) 是一个开源 React 组件库，它实现了 Google 的 Material Design。其客户包括 Netflix、亚马逊、NASA 和 Shutterfly。
*   [SlickGrid](https://github.com/6pac/SlickGrid) 是另一个开源解决方案，专为大型数据集和实时更新而设计。

还有一些专有竞争对手，例如：

*   [DevExpress Data Grid](https://docs.devexpress.com/WindowsForms/3455/controls-and-libraries/data-grid) 是一款商业产品，以其高级过滤、分组和数据透视表功能集而闻名。
*   [Handsontable](https://handsontable.com/)，曾经是开源的，但现在不再是了。目前，它提供了一个免费的非商业许可证，允许开发人员将其用于个人和非营利项目。但是，对于商业用途，需要商业许可证。
*   [Syncfusion Essential JS 2 DataGrid](https://ej2.syncfusion.com/demos/#/fluent2/grid/grid-overview.html)，包括数据编辑、过滤、分组和导出。它为个人和小型商业用途提供免费的社区许可证，但 [具有所有功能的完整版本需要商业许可证](https://ej2.syncfusion.com/documentation/licensing/overview)。

AG Charts 的开源竞争对手包括 [Chart.js](https://github.com/chartjs/Chart.js)、[D3.js](https://github.com/d3/d3) 和 [Plotly.js](https://github.com/plotly/plotly.js)。

[YOUTUBE.COM/THENEWSTACK

技术发展日新月异，不容错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)