# 构建一个快速的时间序列预测应用

![Featued image for: Build a Quick Time Series Forecasting App](https://cdn.thenewstack.io/media/2025/05/c0c9e2c8-forecast-1024x620.png)

有没有想过下个月伦敦的天气会怎样？或者，您是否正在尝试预测公司下个季度的销售额？欢迎来到迷人的[时间序列预测](https://thenewstack.io/time-series-forecasting-with-tensorflow-and-influxdb/)世界，这是一种数据科学技术，可以让我们使用历史模式来窥视未来。

## 预测未来的艺术

[时间序列预测](https://www.influxdata.com/time-series-forecasting-methods/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_ts-forecasting_tns)是统计学、数据科学和领域专业知识的交叉点。它是众多业务运营背后的秘诀，从库存管理到财务规划。本教程将说明如何为臭名昭著的难以预测的伦敦天气构建一个实用的天气预报系统。
数据存储将是一个[时间序列数据库](https://www.influxdata.com/time-series-database/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_ts-forecasting_tns)，由于其专注于带时间戳的数据，因此非常适合时间序列预测。

它们旨在高效地存储和检索按时间排序的大量数据，这对于分析历史趋势和模式至关重要。

## 我们的工具包

三种强大的技术不会花费您一分钱：

*   **InfluxDB 3 Enterprise**: 一个强大的时间序列数据库，旨在处理存储、处理和分析大量、高速数据的复杂性，以进行历史时间序列预测。您可以使用免费试用版或免费的家庭许可证。
*   **Prophet**: Facebook Research 强大的开源预测库，可以轻松处理季节性和异常检测。
*   **Open-Meteo API**: 一个免费、全面的天气数据 API，具有全球覆盖范围，用于收集过去六个月的伦敦天气数据。

## 开始使用

**1. 安装 InfluxDB 3 Enterprise**：安装很简单；只需您的电子邮件地址即可免费开始使用。在您的终端中运行以下命令，然后按照提示进行无缝安装。

```
curl -O https://www.influxdata.com/d/install_influxdb3.sh && sh install_influxdb3.sh enterprise
```

**2. 使用默认设置启动 InfluxDB 3 Enterprise**，其中包括一个简单的集群和一个 Parquet 文件作为本地对象存储。

```
influxdb3 serve \
  --node-id host01 \
  --cluster-id cluster01 \
  --object-store file \
  --data-dir ~/.influxdb3
```

**3. 使用以下命令为数据库操作创建一个管理令牌**：

```
influxdb3 create token --admin --host http://localhost:8181
```

**4. 创建一个“.env”文件**，并将管理令牌字符串与以下详细信息一起安全地存储：

```
INFLUXDB_HOST="localhost:8181"
INFLUXDB_TOKEN="your_database_token"
INFLUXDB_DATABASE="weather"
LONDON_LAT="51.5074"
LONDON_LON="-0.1278"
```

**5. Python 和 Prophet 设置**

最后，安装必要的库，例如 Prophet、[requests](https://pypi.org/project/requests/)（用于处理来自 Open-Meteo API 的伦敦天气数据的 Web API 请求）、[dotenv](https://pypi.org/project/python-dotenv/)（用于将凭据存储在环境文件中）和 [InfluxDB v3 Client Library](https://github.com/InfluxCommunity/influxdb3-python)（用于轻松与 InfluxDB 3 Enterprise 通信）。

```
pip install influxdb3-python prophet requests python-dotenv
```

## 步骤 1：收集历史天气数据

旅程从收集伦敦的温度数据开始。使用 Open-Meteo API 获取六个月的历史数据，并将其高效地存储在 InfluxDB 中。创建一个 Python 脚本并将其命名为 `main.py`。

```python
# In main.py
from weather_client import fetch_weather_data
from influxdb_client import DBClient

weather_data = fetch_weather_data()
df = process_api_response(weather_data)  # This function parses the API response
db = DBClient()
db.write_weather_data(df)  # Efficiently writes data to InfluxDB
print("Weather data written to InfluxDB")
```

我们的 DBClient 类负责繁重的批量写入本地 InfluxDB 3 Enterprise 实例的工作，以实现最佳性能。

## 步骤 2：检索天气数据

在安全地存储数据后，可以使用简单的 SQL 查询来检索数据。创建一个 Python 脚本并将其命名为 `influxdb_client.py`。

```python
# influxdb_client.py
def read_data(self):
    query = """
    SELECT time, temperature
    FROM "weather-london"
    WHERE time >= now() - interval '180 days'
    ORDER BY time ASC
    """
    return self.client.query(query=query)
```

## 步骤 3：水晶球时间 – 使用 Prophet 进行预测

现在，到了激动人心的部分：使用 Prophet 生成未来一个月伦敦温度的预测。创建一个 Python 脚本并将其命名为 `forecasting.py`。
# forecasting.py
```python
from influxdb_client import DBClient
from prophet import Prophet

db = DBClient()
df = db.read_data().to_pandas() # Get data from InfluxDB
model = Prophet(yearly_seasonality=True, daily_seasonality=True)
model.fit(df)
future = model.make_future_dataframe(periods=30*24, freq='h') # Forecast 1 month ahead
forecast = model.predict(future)
```

## 预测选择：机器学习 vs. 统计方法

预测并非新鲜事物，[特别是对于时间序列数据](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/)。常用的方法包括统计方法和[机器学习模型](https://thenewstack.io/deploying-scalable-machine-learning-models-for-long-term-sustainability/)。两者之间的主要区别在于：

### 机器学习方法（如 Prophet）：

- 擅长检测复杂、非线性的模式
- 自动处理季节性和趋势变化
- 需要最少的人工调整
- 在较大的数据集上表现更好

### 传统统计方法（如 ARIMA）：

- 提供更清晰的可解释性
- 即使在数据有限的情况下也能表现良好
- 消耗更少的计算资源
- 通常需要更多的统计专业知识

### 新秀：时间序列 LLM

专门为时间序列分析训练的[大型语言模型](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)正在成为一个引人入胜的前沿领域：

**优点**：

- 可以潜在地在没有明确训练的情况下进行预测（零样本学习）
- 可以在不同类型的时间序列数据中很好地泛化

**局限性**：

- 仍处于早期开发阶段
- 计算密集型
- 通常缺乏可解释性
- 可能难以保证长期准确性

**实时 vs. 批量处理**

我们的示例使用批量处理，分析固定的数据集以进行预测。这非常适用于天气预报，它不需要每秒更新。但是，对于像金融交易或 IoT 传感器监控这样可能需要实时预测的应用程序，InfluxDB 3 Core/Enterprise 中的[处理引擎](https://docs.influxdata.com/influxdb3/enterprise/plugins/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_ts-forecasting_tns)是理想的选择。

**总结**

[时间序列预测](https://thenewstack.io/what-is-time-series-forecasting/)在各行各业释放了令人难以置信的可能性。随着像 Prophet 和 InfluxDB 这样的工具变得越来越容易访问，您可以开始以最小的开销实施复杂的预测解决方案。
这个领域在不断快速发展，[时间序列 LLM 代表着最前沿的技术](https://thenewstack.io/bridging-time-series-from-edge-to-cloud/)。保持好奇心，不断尝试，您的预测技能将在我们这个数据驱动的世界中变得越来越有价值。

请随时加入我们的[社区讨论](https://community.influxdata.com/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_ts-forecasting_tns)，提出您的问题和见解。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)