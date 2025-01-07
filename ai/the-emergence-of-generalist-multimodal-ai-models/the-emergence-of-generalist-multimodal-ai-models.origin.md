# The Emergence of Generalist Multimodal AI Models
![Featued image for: The Emergence of Generalist Multimodal AI Models](https://cdn.thenewstack.io/media/2025/01/cfb521f4-google-deepmind-3pukewjvszw-unsplashb-1024x576.jpg)
Interest in [multimodal large language models](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/) (MLLMs) has exploded over the last year or so thanks to their versatile capabilities in tackling tasks across multiple varieties of data — text, images and videos, as well as time series and graph data.

Because MLLMs are designed to learn, reason and adapt their behavior based on contextual information — much like how human intelligence works — some experts also believe that further developing multimodal AI is a crucial step toward [artificial general intelligence](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-artificial-general-intelligence-agi) (AGI).

It’s because of this potential downstream impact of multimodal AI that there is now more attention on building truly “generalist” multimodal AI models. Such generalist multimodal models (GMMs) would be able to learn easily across diverse modalities, and adapt and perform well when confronted with different types of tasks.

Current examples of generalist multimodal AI models include:

## Foundation Models Paving the Way
This current trajectory toward generalist multimodal models has its roots in the development of pre-trained, deep-learning [foundation models](https://www.datacamp.com/blog/what-are-foundation-models) for processing natural language, vision, times series and graph-structured data.

Most notably, the 2018 introduction of foundation language models (FLMs) like [BERT](https://www.datacamp.com/blog/what-is-bert-an-intro-to-bert-models) (Bidirectional Encoder Representations from Transformers) was pivotal in establishing the groundwork for models that could be pre-trained on massive text-based datasets using an attention-based architecture. These transformer models eventually paved the way for later large language models, like OpenAI’s [GPT series](https://thenewstack.io/openais-gpt-3-makes-big-leap-forward-for-natural-language-processing/).

Similarly, foundation vision models (FVMs) like the [vision transformer (ViT)](https://huggingface.co/docs/transformers/en/model_doc/vit) and vision-language alignment models like [CLIP](https://medium.com/@melgor89/foundation-models-for-computer-vision-42574d13f6a6) and [LLaVA](https://thenewstack.io/5-multimodal-ai-models-that-are-actually-open-source/) helped to push forward the cross-modal capabilities of multimodal AI models.

While foundational models in language and vision have progressed quickly, efforts in developing foundation time series models (FTMs) and foundation graph models (FGMs) have been progressing more slowly due to the specificity of such models and their limited transferability between distinct datasets.

Nevertheless, the capabilities of time series models like [Informer](https://arxiv.org/abs/2012.07436) and [TimeGPT](https://towardsdatascience.com/timegpt-the-first-foundation-model-for-time-series-forecasting-bf0a75e63b3a), plus [graph neural networks](https://www.assemblyai.com/blog/ai-trends-graph-neural-networks/) (GNNs) like [GROVER](https://arxiv.org/abs/2007.02835), could potentially be translated over into generalist multimodal models — thus allowing GMMs to easily make future predictions based on historical, time-stamped data (i.e., [time series forecasting](https://www.datacamp.com/blog/ai-time-series-forecasting)), or to analyze various sets of entities and their mutual interactions (i.e., [graph data](https://www.assemblyai.com/blog/ai-trends-graph-neural-networks/)).

## Typical Model Pipeline
According to a recent [survey](https://arxiv.org/pdf/2406.05496) from the [Pacific Northwest National Lab](https://www.pnnl.gov/) examining the development of GMMs, a multimodal model with generalist capabilities would typically have the following components:

- Input data pre-processor;
- Universal learning module (encoder, decoder); and
- Output data post-processor.
![](https://cdn.thenewstack.io/media/2024/12/7890f219-generalist-multimodal-ai-survey-munikoti-et-al.png)
Via Munikoti, et al., “Generalist Multimodal AI: A Review of Architectures, Challenges and Opportunities”

Raw data of different modalities is pre-processed with the input data pre-processor, converting it into a form that can then be used by the universal learning module. This can be achieved via serialization or tokenization, where text, audio or images are transformed into a numerical “token” format, so that it can be fed into the encoder of the universal learning module — which functions like a “backbone” for learning and reasoning.

The encoder converts the input token into a representational embedding that is positioned in a high-dimensional semantic space for universal learning. For instance, text-based data could be handled by any LLM, while images could be encoded by models like CLIP, or various modalities by multimodal models like [ImageBind](https://thenewstack.io/top-7-tools-for-building-multimodal-ai-applications/).

Additionally, a [projector](https://www.tandfonline.com/doi/full/10.1080/0952813X.2022.2078889#abstract) might be needed to transform or “project” representational embeddings from the encoder into something that can be understood by the universal learning module.

The decoder then transforms the multimodal representational embeddings into outputs that are relevant to the task, and are informed by the cross-modal context gleaned from the previous steps.

## Challenges
While the field of generalist multimodal AI is continuing to expand, there are still some potential issues to consider.

These include the shortage of multimodal datasets, relative to the abundance of unimodal, text-based and image-based datasets. This is due to cost and the legitimate concerns over data privacy, as well as the considerable computational and labor expense in generating truly comprehensive multimodal datasets that would accurately match massive amounts of text data with audio and image data (for example).

Other hurdles include the lack of sufficiently complex benchmarks to evaluate GMMs, beyond the usual ones that are geared primarily toward text and images.

Another barrier is that current multimodal learning is heavily skewed toward cross-modal learning, which often favors image and text over other modalities. More research is needed to explore and innovate into capturing under-represented modalities — like thermal information in infrared images — which can then be leveraged to further develop generalist multimodal AI models for medical applications.

Despite these challenges, the process of further developing truly generalist multimodal AI is a crucial undertaking, especially with the prospect of establishing the necessary groundwork for AGI.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)