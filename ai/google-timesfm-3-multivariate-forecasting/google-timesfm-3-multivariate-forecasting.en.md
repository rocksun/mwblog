On Monday, Google launched [TimesFM-3](https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/), a 330-million-parameter time-series forecasting model trained on over a trillion real-world and synthetic data time points.

The new model is now available on Hugging Face under a non-commercial license.

Large language models are great at predicting the next word. For businesses, time-series forecasting models essentially try to do the same thing, but for data. Over the last few years, there’s been a lot of work in building better forecasting models. Last year saw the launch of models like Chronos-2 from Amazon and Moirai 2.0 from Salesforce, while more recently, Datadog launched its [Toto 2.0 model](https://www.datadoghq.com/blog/ai/toto-2/).

These models represent a relatively new breed of forecasting models, as they can ingest multiple time series. As Google research scientists Ayush Jain and Rajat Sen explain in the announcement, “most real-world forecasting problems are inherently multivariate: where multiple time series and auxiliary external features jointly impact the future forecast of a time series.”

![](https://cdn.thenewstack.io/media/2026/08/5c4f141b-timesfm3_promotionsgraph.width-1250.png)

Past sales, they explain, only tell part of the story. “A good forecast should also draw on sales of related products (e.g., ice cream cones, syrups), historical foot traffic, and known future events like weather forecasts, promotions, and holidays.”

TimesFM-3 is Google’s first model that was natively pre-trained to handle multiple time series and to do so with zero-shot generalization. This also allows it to forecast multiple related time series in parallel and to include historical data, such as past foot traffic.

In the benchmarks Google shared, TimesFM-3 outperforms all of these, often by a significant margin. The team looked at Salesforce’s Gift-Eval, Amazon/AutoGluon’s FEV-Bench, and Time.

What’s maybe the most surprising here is that TimesFM-2.5, which was state-of-the-art when it launched in September 2025, is now at the bottom of the benchmarks. That’s how fast this field is developing.

![](https://cdn.thenewstack.io/media/2026/08/bf5024b2-timesfm35_time.width-1250-1024x680.png)

## The architecture

Like its predecessors, TimesFM-3 is a decoder-only transformer that chops each time series into patches of 32 data points and treats them roughly the way a language model treats tokens.

What’s new is that these tokens now flow through two alternating kinds of attention layers. The first one looks backward across time within a single series and keeps things strictly causal, so the model can’t see values it shouldn’t know yet. The other looks sideways across all series at a given moment, which is how a promotion in one product line, for example, can inform the forecast for another.

![](https://cdn.thenewstack.io/media/2026/08/d1af83a9-timesfm31_architecture.width-1250-1024x573.png)

Decoding changed, too. Earlier versions generated forecasts one patch at a time, Google’s researchers explain, which added latency and compounded errors along the way.

Instead, TimesFM-3 appends masked placeholder tokens for the entire forecast horizon and then fills them all in with a single forward pass.

## The non-commercial license

Google decided to launch the new model [under a non-commercial license](https://huggingface.co/google/timesfm-3.0-pytorch/blob/main/LICENSE). That’s becoming a bit of a [trend](https://thenewstack.io/glm-5-3-flash-chinese-chips/) in the world of model builders.

TimesFM-2.5 still shipped with the [Apache 2.0 license](https://github.com/google-research/timesfm) — as do Toto 2.0 and Chronos-2.

The TimesFM-3 source code is still under the Apache license. Still, Google notes that “for the time being, TimesFM 3.0 pretrained weights are distributed under the separate `timesfm-non-commercial-license-v1.0` license and are restricted to non-commercial, non-production use. Commercial or production use of the default pretrained weights is **not permitted**.”

Google will soon replace TimesFM-2.5 as the model that powers BitQuery’s [AI.FORECAST](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-forecast) command, so the company is actively monetizing these models.

That’s not unusual, of course. Every player in this market already integrates its forecasting models into its own platform, but Google restricting the state-of-the-art weights while also opening a paid path through its data warehouse is a pretty clear signal of where these labs think the money is in the long run.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)