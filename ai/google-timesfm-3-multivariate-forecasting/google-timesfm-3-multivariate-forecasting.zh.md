周一，谷歌发布了 [TimesFM-3](https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/)，这是一个拥有 3.3 亿参数的时间序列预测模型，它是在超过一万亿个真实世界和合成数据点上训练而成的。

目前，该新模型已在 Hugging Face 上发布，采用非商业许可协议。

大型语言模型擅长预测下一个单词。对于企业而言，时间序列预测模型本质上是在做同样的事情，只不过对象是数据。在过去几年中，构建更好的预测模型做了大量工作。去年见证了诸如亚马逊的 Chronos-2 和 Salesforce 的 Moirai 2.0 等模型的发布，而最近，Datadog 发布了其 [Toto 2.0 模型](https://www.datadoghq.com/blog/ai/toto-2/)。

这些模型代表了相对较新的一类预测模型，因为它们可以摄入多个时间序列。正如谷歌研究科学家 Ayush Jain 和 Rajat Sen 在公告中所解释的那样：“大多数现实世界的预测问题本质上是多元的：多个时间序列和辅助的外部特征共同影响着时间序列的未来预测。”

![](https://cdn.thenewstack.io/media/2026/08/5c4f141b-timesfm3_promotionsgraph.width-1250.png)

他们解释说，过去的销售额只能说明部分情况。“一个好的预测还应该借鉴相关产品的销售额（例如冰淇淋蛋筒、糖浆）、历史客流量以及已知的未来事件，如天气预报、促销活动和节假日。”

TimesFM-3 是谷歌第一个原生预训练用于处理多个时间序列并实现零样本泛化的模型。这也使它能够并行预测多个相关的时间序列，并纳入历史数据，例如过去的客流量。

在谷歌分享的基准测试中，TimesFM-3 优于所有这些模型，而且往往领先优势很大。团队考察了 Salesforce 的 Gift-Eval、Amazon/AutoGluon 的 FEV-Bench 和 Time。

这里可能最令人惊讶的是，2025 年 9 月发布时处于行业领先水平的 TimesFM-2.5，现在在基准测试中排名垫底。这就是该领域的发展速度。

![](https://cdn.thenewstack.io/media/2026/08/bf5024b2-timesfm35_time.width-1250-1024x680.png)

## 架构

与它的前代产品一样，TimesFM-3 是一个仅解码器的 Transformer，它将每个时间序列切成 32 个数据点的片段，并以大致类似于语言模型处理 token 的方式处理它们。

新颖之处在于，这些 token 现在流经两种交替的注意力层。第一种层在单个序列内向后回顾时间，并保持严格的因果关系，因此模型无法看到它尚不应该知道的值。另一种层在给定时刻横向查看所有序列，这就是例如一个产品线的促销活动如何为另一个产品线的预测提供信息。

![](https://cdn.thenewstack.io/media/2026/08/d1af83a9-timesfm31_architecture.width-1250-1024x573.png)

解码方式也发生了变化。谷歌的研究人员解释说，早期版本一次生成一个片段的预测，这增加了延迟并在此过程中加剧了误差。

相反，TimesFM-3 为整个预测范围添加了屏蔽的占位符 token，然后通过单次前向传递将它们全部填充。

## 非商业许可

谷歌决定[在非商业许可下](https://huggingface.co/google/timesfm-3.0-pytorch/blob/main/LICENSE)发布该新模型。这在模型构建者领域正成为一种[趋势](https://thenewstack.io/glm-5-3-flash-chinese-chips/)。

TimesFM-2.5 发布时仍然带有 [Apache 2.0 许可](https://github.com/google-research/timesfm)——Toto 2.0 和 Chronos-2 也是如此。

TimesFM-3 的源代码仍然采用 Apache 许可。尽管如此，谷歌指出“目前，TimesFM 3.0 预训练权重根据单独的 `timesfm-non-commercial-license-v1.0` 许可进行分发，并仅限于非商业、非生产用途。**不允许**将默认的预训练权重用于商业或生产用途。”

谷歌很快将取代 TimesFM-2.5，将其作为驱动 BitQuery 的 [AI.FORECAST](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-forecast) 命令的模型，因此该公司正在积极实现这些模型的货币化。

当然，这并不罕见。这个市场中的每个参与者都已经在将自己的预测模型集成到自己的平台中，但谷歌在限制最先进权重的同时，通过其数据仓库开辟付费路径，这很清楚地表明了这些实验室认为长期的盈利点在哪里。