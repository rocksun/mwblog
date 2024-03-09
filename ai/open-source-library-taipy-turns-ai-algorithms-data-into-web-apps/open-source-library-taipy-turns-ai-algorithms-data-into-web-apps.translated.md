## 开源库 Taipy 将 AI 算法和数据转化为 Web 应用程序

![用于：开源库 Taipy 将 AI 算法和数据转化为 Web 应用程序的特色图片](https://cdn.thenewstack.io/media/2024/03/9ed80d32-python-1024x684.jpg)

一个免费的开源 Python 库允许开发者将数据和 AI 算法转化为可投入生产的 Web 应用程序。该库名为 [Taipy](https://github.com/Avaiga/taipy)，旨在支持数据科学和机器学习工程师构建全栈应用程序。

该 [初创公司](https://www.taipy.io/) 由 [Vincent Gosselin](https://www.linkedin.com/in/vincent-gosselin-5011559/?originalSubdomain=fr) 和 [Albert Antoine](https://www.linkedin.com/in/albert-antoine-7a5a673/) 创立，他们都是技术领域的资深人士。担任首席执行官的 Gosselin 在 IBM 的数据科学和高级分析部门工作了八年，还曾在 DecisionBrain 担任高级分析主管。Taipy 的执行董事 Antoine 曾担任数据分析公司 Avaiga.com 的首席执行官，并在数据科学平台 Dataiku 担任业务发展工作。

“他们在创建 Taipy 时想要解决的问题是数据空间中项目的失败率，”数据科学家兼 Taipy 全球社区经理 [Rym Michaut](https://www.linkedin.com/in/rymguerbi/recent-activity/all/) 在给 The New Stack 的书面回复中解释道。“这些项目大多数都是用 Python 编写的。这就是我们从 Java 转向 Python 的原因。”

### Taipy 的三个组件

开发者无需任何 HTML、 [JavaScript](https://thenewstack.io/2024-predictions-by-javascript-frontend-framework-maintainers/) 或 [CSS](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/) 的先验知识即可使用 Taipy，但需要对 Python 有基本的了解。

该工具由三个组件组成，首先是 Taipy 前端，用于使用简单的 Markdown 语言构建图形用户界面，以创建带有图形元素的交互式页面，根据 [Taipy 常见问题解答](https://www.taipy.io/company/faq)。

“开发者对外观和感觉有很大的控制权，”Michaut 说。“我们为所有应用程序和 UI 组件提供默认的 CSS 样式，但可以通过 Python 或 CSS 代码修改这些样式。我们在外观和感觉方面的主要优势在于布局：我们提供简单的语法来定制应用程序的设计，我们还有一个 [VS Code](https://thenewstack.io/how-to-use-vs-code-as-your-python-ide/) 扩展，它允许你在不运行 Python 代码的情况下预览页面的设计。”

她承认，虽然该库是可定制的，但她表示，“默认布局和外观可能不如其他不太可定制的库令人印象深刻。”为了让开发者了解使用 Taipy 构建真实应用程序的想法，她分享了一个 [财务预测仪表盘模型](https://pl-dashboard.taipy.cloud/group_contributions)，该模型是为一家公司完成的。

![使用 Taipy 制作的应用程序模型](https://cdn.thenewstack.io/media/2024/03/382f65c3-taipy-mockup.png)

由 Taipy 制作的应用程序 [模型](https://pl-dashboard.taipy.cloud/group_contributions)，由 Taipy 提供。

在未来几个月，Taipy 计划发布一个新的低代码产品，该产品将允许用户使用 Web 界面中的拖放式 UI 组件在不编码的情况下编辑前端。

Taipy 后端用于构建和管理数据流，包括可以调用你的代码的管道。它可以调度任务、缓存重复操作，以及并行化任务“以优化管道和场景的性能和流线化管理”，常见问题解答中指出。“Taipy 后端的主要目的是转换标准 Python 代码并增强管道和场景的性能和管理”，它补充道。

第三个组件 Taipy Rest 提供了一种通过 Rest API 访问场景、管道和数据访问器的方法。

“Taipy 还专注于在全面生产应用程序中工作：由于我们使用所谓的回调在用户交互中运行最低必要任务，因此前端和后端在不同的线程上运行，这样即使模型在后台运行，用户仍然可以与应用程序交互，”Michaut 解释道。

Taipy 可以默认连接到 pickle、CSV、Excel、JSON、Mongo、SQL 和 Parquet。

“当然，如果你可以使用 Python 连接到数据源，那么它也可以在 Taipy 中使用几行代码工作，”她补充道。

还有用于连接到 [AWS](https://thenewstack.io/bringing-the-aws-serverless-strategy-to-azure/) 和 [DataBricks](https://thenewstack.io/databricks-sees-and-raises-snowflake-with-gen-ai-llmops-more/) 的文档。

### 与现有数据科学、ML 库集成

The New Stack 问 Michaut，Taipy 是否可以高效地处理大型数据集和复杂的机器学习模型，以及它与现有数据科学和
**机器学习库**

[机器学习库](https://thenewstack.io/ai-ml-best-practices-during-a-gold-rush/)，例如 [scikit-learn](https://scikit-learn.org/stable/)、[TensorFlow](https://thenewstack.io/tutorial-deploying-tensorflow-models-with-amazon-sagemaker-serverless-inference/) 或 [PyTorch](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/)。

“是的，Taipy 可以通过集成其他库高效地处理大型数据集和 [ML 算法](https://thenewstack.io/ml-engineer-teaches-graph-algorithms-with-dungeons-dragons/)。”她回答道。“由于我们的库主要专注于前端，因此我们不会干扰任何可以用 [Python 代码](https://thenewstack.io/what-is-python/) 编写的代码。Taipy 在网页中调用运行 ML 算法所需的各种库，并直接与之交互。例如，你可以从 Taipy 界面更改模型参数，使用按钮运行模型，并在 Taipy 网页中可视化结果。”

它还提供允许用户实时可视化和交互大型数据集的功能。她解释说，其中一项功能是抽取器，它减少了图表上最不修改曲线的点的数量。“我们还有在并行或分布式集群上运行 ML 模型的功能。”她补充道。

## 目标：易用性加上可扩展性

我们还询问了 Taipy 与其他类似框架（例如 [Streamlit](https://streamlit.io/)、[Dash](https://dash.plotly.com/) 或 [Flask](https://flask.palletsprojects.com/en/3.0.x/)）相比如何。Michaud 说，Taipy 的目标是达到这些解决方案所不具备的易用性和可扩展性的完美平衡。

“我们发现 Python 图形包场景分为两极：一方面，Streamlit 等工具易于使用，但无法扩展到生产应用程序。当遇到多个页面/用户或大型数据集/计算时，它们通常会失败。”她表示。“另一方面，Dash 等工具具有可扩展性，但学习曲线陡峭。我们看到了市场的空白，并抓住了它。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)