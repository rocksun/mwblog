# 使用时间序列语言模型改变预测分析

![使用时间序列语言模型改变预测分析的特色图片](https://cdn.thenewstack.io/media/2024/08/bdc32aa4-snake-4912018_1280-1024x768.jpg)

[大型语言模型](https://thenewstack.io/llm/) (LLM) 如 ChatGPT 和 Bard 的兴起，已经彻底改变了人们工作、交流和学习的方式，这已经不是什么秘密。但 LLM 的应用并不局限于取代搜索引擎。最近，数据科学家将 LLM 用于[时间序列预测](https://thenewstack.io/python-time-series-forecasting-tutorial/)。

[时间序列数据](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/) 在各个领域都很常见，从金融市场到气候科学。与此同时，在人工智能的推动下，LLM 正在彻底改变我们处理和生成人类语言的方式。在这里，我们将深入探讨时间序列 LLM 如何提供创新的预测和异常检测模型。

**什么是时间序列 LLM？**

从高层次上讲，时间序列 LLM 被重新用于处理时间序列数据，而不是文本、视频或图像数据。它们结合了传统时间序列分析方法的优势和 LLM 的高级功能，以进行预测。强大的预测可用于在数据显着偏离预测或预期结果时检测异常。时间序列 LLM 与传统 LLM 之间的一些其他显着区别包括：

* **数据类型和训练：**虽然像 ChatGPT 这样的传统 LLM 在文本数据上进行训练，但时间序列 LLM 在顺序数值数据上进行训练。具体来说，预训练是在大型、多样化的时序数据集（包括真实世界和合成数据集）上进行的，这使得模型能够很好地推广到不同的领域和应用。
* **标记化：**时间序列 LLM 将数据分解成块，而不是文本标记（块指的是时间序列数据的连续段、块或窗口）。
* **输出生成：**时间序列 LLM 生成未来数据点的序列，而不是单词或句子。
* **架构调整：**时间序列 LLM 结合了特定的设计选择来处理时间序列数据的时态特性，例如可变上下文和范围长度。

时间序列语言模型 (LLM) 与传统方法相比，在分析和预测时间序列数据方面具有许多显著优势。与 ARIMA 等传统方法不同，传统方法通常需要大量的领域专业知识和手动调整，时间序列 LLM 利用先进的机器学习技术来自动学习数据。这使得它们成为许多应用的强大而通用的工具，而传统模型可能无法胜任。

* **零样本性能：**时间序列 LLM 可以在没有额外训练或微调的情况下对新的、看不见的数据集进行准确预测。这对于数据频繁出现的新环境特别有用。零样本方法意味着用户不必花费大量资源或时间来训练他们的模型。
* **复杂模式处理：**时间序列 LLM 可以捕获数据中复杂的非线性关系和模式，而传统统计模型（如[ARIMA](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average) 或[GARCH](https://en.wikipedia.org/wiki/Autoregressive_conditional_heteroskedasticity#GARCH)）可能会错过，尤其是对于未见过或未经预处理的数据。此外，调整统计模型可能很棘手，需要深入的领域专业知识。
* **效率：**时间序列 LLM 并行处理数据。与通常按顺序处理数据的传统模型相比，这显着加快了训练和推理时间。此外，它们可以在单个步骤中预测更长的未来数据点序列，从而减少了所需的迭代步骤数量。

**时间序列 LLM 的实际应用**

一些最流行的时间序列 LLM 用于预测和预测分析，包括[Google 的 TimesFM](https://github.com/google-research/timesfm)、[IBM 的 TinyTimeMixer](https://github.com/ibm-granite/granite-tsfm/tree/main) 和[AutoLab 的 MOMENT](https://github.com/moment-timeseries-foundation-model/)。

Google 的 TimesFM 可能最容易使用。使用 pip 安装它，初始化模型，并加载检查点。然后，您可以对输入数组或 Pandas DataFrame 进行预测。例如：

```python
import timesfm

# 初始化模型
model = timesfm.TimesFM()

# 加载检查点
model.load_checkpoint("path/to/checkpoint")

# 对输入数据进行预测
predictions = model.predict(input_data)
```
```python
import pandas as pd
# 例如 input_df 是
# unique_id ds y
# 0 T1 1975-12-31 697458.0
# 1 T1 1976-01-31 1187650.0
# 2 T1 1976-02-29 1069690.0
# 3 T1 1976-03-31 1078430.0
# 4 T1 1976-04-30 1059910.0
# ... ... ... ...
# 8175 T99 1986-01-31 602.0
# 8176 T99 1986-02-28 684.0
# 8177 T99 1986-03-31 818.0
# 8178 T99 1986-04-30 836.0
# 8179 T99 1986-05-31 878.0
forecast_df = tfm.forecast_on_df(inputs=input_df, freq="M", # 月度值
                               value_name="y", num_jobs=-1,)
```Google 的 TimesFM 还支持微调和协变量支持，指的是模型能够将额外的解释变量（协变量）与主要时间序列数据一起纳入并利用，以提高其预测的准确性和稳健性。您可以在 [这篇论文](https://arxiv.org/pdf/2310.10688) 中了解更多关于 Google 的 TimesFM 的工作原理。
[IBM 的 TinyTimeMixer](https://github.com/ibm-granite/granite-tsfm/tree/main) 包含用于对多元时间序列数据执行各种预测的模型和示例。[此笔记本](https://github.com/ibm-granite/granite-tsfm/blob/main/notebooks/hfdemo/ttm_getting_started.ipynb) 突出显示了如何使用 TTM（TinyTimMixer）对数据执行零样本和少样本预测。下面的屏幕截图显示了 TTM 生成的一些估计值：
最后，[AutoLab 的 MOMENT](https://github.com/moment-timeseries-foundation-model/) 具有预测和异常检测的方法，并提供易于理解的示例。它专门用于长周期预测。例如，此笔记本重点介绍了如何通过首先导入模型来预测单变量时间序列数据：

```python
from momentum import MOMENTPipeline
model = MOMENTPipeline.from_pretrained(
    "AutonLab/MOMENT-1-large",
    model_kwargs={
        'task_name': 'forecasting',
        'forecast_horizon': 192,
        'head_dropout': 0.1,
        'weight_decay': 0,
        'freeze_encoder': True, # 冻结补丁嵌入层
        'freeze_embedder': True, # 冻结 Transformer 编码器
        'freeze_head': False, # 线性预测头必须经过训练
    },
)
```
下一步是在您的数据上训练模型以进行适当的初始化。在每个训练周期之后，模型都会在测试数据集上进行评估。在评估循环中，模型使用 `output = model(timeseries, input_mask)` 行进行预测。
```python
while cur_epoch < max_epoch:
    losses = []
    for timeseries, forecast, input_mask in tqdm(train_loader, total=len(train_loader)):
        # 将数据移动到 GPU
        timeseries = timeseries.float().to(device)
        input_mask = input_mask.to(device)
        forecast = forecast.float().to(device)
        with torch.cuda.amp.autocast():
            output = model(timeseries, input_mask)
```
**最后的想法**
时间序列 LLM 代表了预测分析的重大进步。它们将深度学习的力量与 [时间序列预测](https://thenewstack.io/what-is-time-series-forecasting/) 的复杂要求结合在一起。它们能够执行零样本学习、合并协变量支持以及高效地处理大量数据，使其成为各个行业变革性工具。随着我们见证该领域的快速发展，时间序列 LLM 的潜在应用和益处只会不断扩大。

要存储时间序列数据，请查看 [InfluxDB Cloud 3.0](https://www.influxdata.com/products/influxdb-overview/?utm_source=google&utm_medium=cpc&utm_campaign=UP%20-%20NA%20Search%20%7C%20Brand-Related%20-%20InfluxDB%20Cloud%20Free%20Tier%20tCPA%20vs%20CPC%20Bidding%20Brand%20Campaign&utm_term=influx%20db&gclid=CjwKCAjw-7OlBhB8EiwAnoOEkwBTlNjA8OGe19RBzbO2tJGL3fMO48eVyW0l6Eeg6YHVkq7xWsIfARoCMAwQAvD_BwE)，领先的时间序列数据库。您可以利用 InfluxDB v3 Python 客户端库与 InfluxDB 存储和查询您的时间序列数据，并应用时间序列 LLM 进行预测和异常检测。您可以查看以下资源以开始使用：

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)