# 时间序列预测：一个开源、无需代码的解决方案

![时间序列预测：一个开源、无需代码的解决方案的特色图片](https://cdn.thenewstack.io/media/2025/05/7f2cc57c-time-series-data-wikipedia-manning-1024x576.jpg)

我们周围的一切都在产生数据，因此从历史数据中预测未来趋势不再是一种奢侈，而是一种必需品。但是，如果您无需编写任何代码即可实现复杂的时间序列预测，那会怎么样？我将通过一个示例向您展示如何使用两个[开源工具](https://thenewstack.io/open-source/)：InfluxDB 3 Core 的 Python 处理引擎和 Facebook 的 Prophet 库。

**彻底改变预测实施**

传统的[时间序列预测](https://thenewstack.io/what-is-time-series-forecasting/)通常需要大量的编码专业知识和数天的开发时间。InfluxDB 3 Core 的 Python 处理引擎与[大型语言模型](https://thenewstack.io/what-is-a-large-language-model/) (LLM) 和库相结合，打破了这种模式。曾经需要深厚的技术知识和大量时间投入才能完成的任务，现在可以在数小时内完成，使即使是[基本的 Python](https://thenewstack.io/what-is-python/) 和时间序列理解的人也可以访问高级预测。

这种转变最引人注目的方面是什么？是使用 LLM 构建复杂系统的速度。只需向 LLM 提供 InfluxDB 3 [文档](https://docs.influxdata.com/influxdb3/core/plugins/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)和 [Facebook Prophet 的快速入门指南](https://facebook.github.io/prophet/docs/quick_start.html)，您就可以生成功能性插件代码，连接整个管道并接收优化建议——所有这些都无需手动编码。

**为什么要使用时间序列数据库？**

在深入研究实施之前，让我们解决一个基本问题：为什么要使用像 InfluxDB 这样的专用[时间序列数据库](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/)，而不是通用或关系数据库？

**针对带时间戳的数据进行了优化**

时间序列数据库专门为处理按时间顺序排列的数据而构建。与传统数据库不同，它们针对基于时间的查询和分析进行了优化，从而使查找变化率、识别趋势或计算移动平均值等操作效率更高。

**卓越的数据压缩**

时间序列数据通常包含数百万或数十亿个数据点。时间序列数据库实现了专门的压缩算法，可以显着降低存储要求，而不会牺牲查询性能。

**内置的以时间为中心的函数**

降采样、插值和窗口函数等函数是时间序列数据库中的标准函数，无需复杂的自定义代码。这种原生支持加速了开发并提高了可靠性。

**可扩展的性能**

随着您的监控或物联网 (IoT) 应用程序的增长，您的数据量也会增长。像 InfluxDB 这样的时间序列数据库可以水平扩展，以处理大量带时间戳的数据涌入，而不会降低性能。

**模式灵活性**

时间序列工作负载通常需要适应不断变化的测量结构。InfluxDB 灵活的模式设计可以适应不断发展的数据模型，而无需痛苦的迁移。

考虑到这些优势，像 InfluxDB 这样的时间序列数据库自然成为预测管道的选择。

**预测挑战**

本教程的目标简单而强大：预测 [Wikipedia 上关于 Peyton Manning 的文章](https://en.wikipedia.org/wiki/Peyton_Manning)一整年的每日页面浏览量。我们将从历史数据开始，最终在 InfluxDB 生态系统中实现交互式 Plotly 可视化。要复制此项目，请[下载 InfluxDB 3 Core 或 Enterprise](https://www.influxdata.com/downloads/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)。

本教程涵盖：

- 我如何利用 [ChatGPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/) 来构建此管道。
- 所需的设置和依赖项。
- 创建必要的 InfluxDB 3 资源。
- 数据摄取、预测生成和可视化。

**管道架构**

此解决方案由三个协同工作的专用插件组成：
**load_peyton:** (HTTP 触发的插件，用于从 CSV 导入 Wikipedia 页面浏览量数据并填充 peyton_views 表。[load_peyton_data.py](https://github.com/Anaisdg/influxdb3_plugins/blob/add-fbprophet-plugins/influxdata/Anaisdg/fbprophet/load_peyton_data.py))

**peyton_forecast:** (每日运行的计划插件，用于查询 peyton_views，训练 Prophet 模型并将全面的 365 天预测写入 prophet_forecast。[forecast_peyton.py](https://github.com/Anaisdg/influxdb3_plugins/blob/add-fbprophet-plugins/influxdata/Anaisdg/fbprophet/forecast_peyton.py))

**forecast_plot:** (HTTP 触发的插件，用于检索历史数据和预测数据，合并它们并以 HTML 形式提供交互式 Plotly 可视化。[plot_forecast_http.py](https://github.com/Anaisdg/influxdb3_plugins/blob/add-fbprophet-plugins/influxdata/Anaisdg/fbprophet/plot_forecast_http.py))

![本教程生成的历史页面浏览量数据（蓝色）和预测页面浏览量数据（绿色）。通过 http://localhost:8181/api/v3/engine/plot_forecast 访问。](https://cdn.thenewstack.io/media/2025/05/1a2c1d9a-pageview-data.png)

本教程生成的历史页面浏览量数据（蓝色）和预测页面浏览量数据（绿色）。通过 [http://localhost:8181/api/v3/engine/plot_forecast](http://localhost:8181/api/v3/engine/plot_forecast) 访问。

**从概念到 AI 实现**

我没有采用传统的编码方式，而是采用了 ChatGPT-4o 的提示工程方法。在提供了 InfluxDB 3 的处理引擎文档和 Prophet 的快速入门指南后，我使用了渐进式的自然语言提示：

**初始概念：** “你能为 InfluxDB 3 编写一个使用 Facebook Prophet 预测时间序列数据的插件吗？”

**数据摄取：** “创建一个插件，从公共 CSV（如 Peyton Manning Wikipedia 浏览量）加载历史数据并将其写入 InfluxDB。”

**预测逻辑：** “现在，编写一个计划插件，查询该表，拟合 Prophet 模型并将预测写入另一个表。确保逻辑写入所有预测行。”

**可视化：** “你能构建第三个插件，读取历史数据和预测数据，使用 Plotly 绘制它，并通过 HTTP 以 HTML 页面的形式返回结果吗？”

这种迭代过程将通常需要数小时的编码转化为关于意图和功能的对话。InfluxDB 处理引擎的 [test 命令](https://docs.influxdata.com/influxdb3/core/reference/cli/influxdb3/test/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns) 被证明对验证非常有价值，创建了一个紧密的反馈循环，大大加快了开发速度。

**环境设置**

您可以在本地或容器化运行此示例。 [InfluxDB 3 Core 和 Enterprise](https://www.influxdata.com/downloads/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns) 都支持此工作流程，但我将重点关注 Core（开源版本），使用 Docker 以简化操作。如果您正在寻找高可用性、可扩展性和安全性，我建议使用 InfluxDB 3 Enterprise。

下载 [存储库](https://github.com/Anaisdg/influxdb3_plugins/tree/add-fbprophet-plugins) 后，将文件保存到您的插件目录并执行：

```
1 |
docker run -it --rm --name test_influx -v ~/influxdb3/data:/var/lib/influxdb3 -v /path/to/plugins/:/plugins -p 8181:8181 quay.io/influxdb/influxdb3-core:latest serve --node-id my_host --object-store file --data-dir /var/lib/influxdb3 --plugin-dir /plugin |
```

[此命令](https://docs.influxdata.com/influxdb3/core/reference/cli/influxdb3/serve/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns) 启动一个临时的 InfluxDB 3 Core 容器，并将您的本地目录挂载用于数据持久性和插件访问，公开端口 8181 用于本地交互。

**实施步骤**

**1. 安装依赖项**

首先，安装所需的软件包：

```
12 |
influxdb3 install package plotlyinfluxdb3 install package prophet |
```

**2. 创建数据库**

为预测项目设置专用数据库：

```
1 |
influxdb3 create database prophet |
```

**3. 加载历史数据**

创建并触发数据加载插件：

```
12345 |
influxdb3 create trigger \
 --trigger-spec "request:load_peyton" \
 --plugin-filename "load_peyton_data.py" \
 --database prophet \
 load_peyton
```

执行插件：

```
1 |
curl http://localhost:8181/api/v3/engine/load_peyton |
```

成功执行显示：

```
1 |
{"status": "success", "rows_written": 2905} |
```

**4. 生成预测**

设置预测插件：

```
12345 |
influxdb3 create trigger \
 --trigger-spec "every:1m" \
 --plugin-filename "forecast_peyton.py" \
 --database prophet \
 peyton_forecast
```

虽然此配置用于演示目的的分钟间隔，但生产环境通常每天运行。成功执行后，您将看到：

```
123 |
```
processing engine: 在 'peyton_views' 上运行 Prophet 预测

INFO - Chain [1] 开始处理

INFO - Chain [1] 完成处理

为防止冗余预测，请禁用触发器：

```
inflxudb3 disable trigger --database prophet peyton_forecast
```

**5. 可视化结果**

创建可视化插件：

```
influxdb3 create trigger \ --trigger-spec "request:plot_forecast" \ --plugin-filename "plot_forecast_http.py" \ --database prophet \ forecast_plot
```

通过 [http://localhost:8181/api/v3/engine/plot_forecast](http://localhost:8181/api/v3/engine/plot_forecast) 访问您的交互式可视化。

**超越基础：生产注意事项**

虽然此示例演示了基本概念，但生产实施可以包含：

- 来自 [Hugging Face](https://thenewstack.io/a-hugging-face-project-is-uncovering-deepseek-r1s-secrets/) 的预训练模型，以实现更快的推理。
- 预测准确性监控，以检测模型漂移。
- 性能下降时的自动重新训练。
- 与 InfluxDB 3 的警报功能集成，以进行异常检测。

这些增强功能创建了智能的、自我优化的时间序列管道，可以根据特定的业务需求进行定制。

**进一步探索的资源**

探索以下资源以加深您的理解：

[使用 InfluxDB 3 中新的 Python 处理引擎转换数据](https://www.influxdata.com/blog/new-python-processing-engine-influxdb3/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)

[开始使用：Python 插件和处理引擎](https://docs.influxdata.com/influxdb3/enterprise/get-started/#python-plugins-and-the-processing-engine/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)

[处理引擎和 Python 插件](https://docs.influxdata.com/influxdb3/enterprise/plugins/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)

对于以警报为中心的实施：

[使用 InfluxDB 3 的处理引擎缓存防止警报风暴](https://www.influxdata.com/blog/preventing-alert-storms-influxdb3/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)

[如何使用 InfluxDB 3 处理引擎设置实时 SMS/WhatsApp 警报](https://www.influxdata.com/blog/setting-up-sms-whatsapp-alerts-influxdb3/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)

[使用 InfluxDB 3 Core 和 Enterprise 发出警报](https://www.influxdata.com/blog/core-enterprise-alerting-influxdb3/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_advanced-forecasting_tns)

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)