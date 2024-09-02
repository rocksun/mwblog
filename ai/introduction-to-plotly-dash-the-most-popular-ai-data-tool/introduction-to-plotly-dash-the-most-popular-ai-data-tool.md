
<!--
title: 最受欢迎的AI数据工具Plotly Dash简介
cover: https://cdn.thenewstack.io/media/2024/08/a50a2946-and-machines-dly3c1siybc-unsplash.jpg
-->

Plotly Dash 是一款支持数据应用程序的 Python 图表展示工具。它作为 AI 工具越来越受欢迎，因此这里提供我们的入门指南。

> 译自 [Introduction To Plotly Dash, the Most Popular AI Data Tool](https://thenewstack.io/introduction-to-plotly-dash-the-most-popular-ai-data-tool/)，作者 David Eastman。

Python 是数据分析，甚至在一定程度上是 AI 开发的首选语言。[Plotly Dash](https://dash.plotly.com/) 是一款用于支持数据应用程序的演示图表工具。或者用他们的话来说，“Dash 是一个原始的低代码框架，用于在 Python 中快速构建数据应用程序。” 但与往常一样，低代码仍然需要对编程有合理的理解。

本月早些时候，Plotly Dash 被 Databricks 的 [数据 + AI 状态报告](https://www.databricks.com/sites/default/files/2024-06/state-of-data-ai-report.pdf) 评为 [最受欢迎的工具](https://thenewstack.io/ai-dev-tools-ranked-and-astro-adds-support-for-large-sites/)，甚至超过了 Langchain！因此，它显然是 [AI 工程生态系统](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/) 中的一个热门工具。Databricks 写道：“Dash 已经连续两年位居榜首，这表明数据科学家在开发生产级数据和 AI 应用程序方面面临着越来越大的压力。”

在这篇文章中，我将安装并使用 Dash，也许在以后的文章中，我们可以用它来构建一些东西。我之前使用过 [Jupyter 笔记本](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)，但在这里我们将只使用一个经典的 Web 服务器来托管结果。

因此，在我的可靠的 Warp shell 中，我们将 [安装](https://dash.plotly.com/installation) 两个必需的组件。由于我不是一个经常使用 Python 的人，我的 .zshrc shell 配置文件中没有推荐的 Python 版本，因此我添加了它：

```bash
#python export 
PATH="$HOME/Library/Python/3.9/bin:$PATH"
```

然后我使用 pip 安装依赖模块：

```bash
pip install dash 
pip install panadas
```

Dash 将有效地将 HTML 引用匹配到其自己的组件库中，并且还有一些专门编写的交互式图表和表格。

为了测试一切是否正常，我们将尝试 [“最小”](https://dash.plotly.com/minimal-app) app.py 并运行它。

```python
from dash import Dash, html, dcc, callback, Output, Input 
import plotly.express as px 
import pandas as pd 
 
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv') 
 
app = Dash() 
 
app.layout = [ 
    html.H1(children='Title of Dash App', style={'textAlign':'center'}), 
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'), 
    dcc.Graph(id='graph-content') 
] 
 
@callback( 
    Output(component_id='graph-content', component_property='figure'), 
    Input(component_id='dropdown-selection', component_property='value') 
) 
 
def update_graph(value): 
    dff = df[df.country==value] 
    return px.line(dff, x='year', y='pop') 
 
if __name__ == '__main__': 
    app.run(debug=True)
```

我们可以看到一个布局已经建立，以及几个回调。因此，我们以后必须弄清楚它们在做什么。我猜想从 update_graph 方法来看，这是一个人口增长图，即使 CSV 链接名称没有给我们任何线索。

在创建 app.py 文件并运行它之后，最终我得到了一个响应：

![](https://cdn.thenewstack.io/media/2024/08/9aa8db5d-image.png)

因此，查看本地地址上声明的本地站点，我看到了：

![](https://cdn.thenewstack.io/media/2024/08/3be658b0-image-1-1024x578.png)

请注意，“加拿大”是下拉菜单中的默认选择，如果我选择另一个国家，图表会立即更改。因此，这给了我们一些关于回调在做什么的线索。

正如预期的那样，如果我查看 CSV 文件的内容，它包含大量数据点：

```
country,continent,year,lifeExp,pop,gdpPercap
Afghanistan,Asia,1952,28.801,8425333,779.4453145
Afghanistan,Asia,1957,30.332,9240934,820.8530296
...
Canada,Americas,1950,68.28,14011422,10581.26552
Canada,Americas,1951,68.55,14330675,10932.46678
Canada,Americas,1952,68.75,14785584,11367.16112
...
```

这意味着我们可以看到 x 轴和 y 轴标签指的是什么。我们还可以看到我们可以选择绘制的其他数据。

让我们 [分析](https://dash.plotly.com/tutorial) 代码，直到我们弄清楚其余部分。pandas 模块 read_csv 的结果是一个数据帧（因此是“df”）。这只是以后工作的结构。您也可以直接从 Excel 数据表中读取。

`dcc` 模块（Dash 核心组件）为我们提供了下拉菜单和图表。总的来说，布局只是一系列组件：在本例中是标题、下拉菜单和图表。

在这一点上，有趣的是，图表和下拉菜单组件都没有被直接引用。实际上，图表甚至没有接收数据帧。显然，这里有一些经过深思熟虑的 [解耦](https://thenewstack.io/devs-dont-just-read-about-design-patterns-implement-them/)。

现在，我们使用 ID “dropdown-selection” 和 “graph-content”。

```
... 
@callback( 
    Output(component_id='graph-content', component_property='figure'), 
    Input(component_id='dropdown-selection', component_property='value') 
) 
...
```

我们有一个 Output 回调，它首先引用了为 Graph 组件定义的“graph-content” ID，并使用组件的“figure”属性。在这里，我认为“figure”只是指要显示的图表。Input 通过“dropdown-selection” ID 引用 Dropdown 组件，并读取“value”属性。

```
... 
def update_graph(value): 
    dff = df[df.country==value] return px.line(dff, x='year', y='pop') 
...
```

由于只提到了一个方法 update_graph，并且我们在代码中没有使用它，因此它显然被 graph 组件用来更新图表。这只是从下拉菜单中获取国家/地区值。换句话说，我可以将 `dff = df[df.country==value]` 替换为 `dff = df[df.country==’Canada’]` 以查看 DataFrame 中加拿大的统计数据。您可以继续使用实时页面更改代码 - 它会热重载。

因此，当我们更改国家/地区时，图表将重建，csv 的每一行都将输入到 update_graph 方法中；在这种情况下，从一个点到另一个点画一条线。

让我们来试验一下。如果我们正确理解了这一点，我们应该能够使用相同的数据添加一个表格，例如。现在，假设我们获得了表格构造函数，我们需要什么？

- 我们需要导入行。
- 将其作为一行添加到布局中。

如果表格不交互，我们就不需要其他任何东西 - 数据表格本身就是一个完全交互式的组件。

接下来，我将 [表格导入](https://dash.plotly.com/datatable) 添加到现有导入的末尾：

```
from dash import Dash, html, dcc, callback, Output, Input, dash_table
```

我还将 [表格构造函数](https://dash.plotly.com/tutorial) 添加到现有布局中。我们知道它是一个大表格，因此我将使用页面大小：

```py
app.layout = [ 
    html.H1(children='Title of Dash App', style={'textAlign':'center'}), 
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'), 
    dcc.Graph(id='graph-content'), 
    dash_table.DataTable(data=df.to_dict('records'), page_size=10) 
]
```


这已经可以工作了，但我们需要将列限制为国家/地区、人口和年份：

```py
app.layout = [
    html.H1(children='Population by year', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),
    dash_table.DataTable(data=df.to_dict('records'),
       columns=[
          {'name': 'Country', 'id': 'country', 'type': 'text'},
          {'name': 'Population', 'id': 'pop', 'type': 'numeric'},
          {'name': 'Year', 'id': 'year', 'type': 'numeric'}
       ],
       page_size=5,
       style_cell={'textAlign': 'left'}
    )
]
```


请注意，我添加了左对齐、更小的页面大小和更友好的标题。这给了我们：

![](https://cdn.thenewstack.io/media/2024/08/0a3a1999-image-2-1024x631.png)

## 结论

Dash 使用起来非常简单，即使我的 Python 处于非常基础的水平。我一直在研究如何控制数据进入 data_table，这有点技巧。

然而，感觉它并不完全标准化，因此您需要阅读您想要尝试的每个组件的说明。但我建议您在下次想要展示一些数据时尝试一下。
