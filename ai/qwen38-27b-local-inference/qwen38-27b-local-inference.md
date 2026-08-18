<!--
title: 阿里巴巴发布新模型，个人电脑即可体验Opus 4.6级性能
cover: https://cdn.thenewstack.io/media/2026/08/bc5346c0-nigel-hoare-v-uxb6rws84-unsplash-scaled.jpg
summary: 阿里巴巴发布的Qwen3.8-27B模型开源权重，可在个人电脑本地运行。基准测试显示其表现媲美Anthropic的Opus 4.6，在编程、视觉及知识处理任务上表现出色，为开发者提供了强大的本地化AI解决方案。
-->

阿里巴巴发布的Qwen3.8-27B模型开源权重，可在个人电脑本地运行。基准测试显示其表现媲美Anthropic的Opus 4.6，在编程、视觉及知识处理任务上表现出色，为开发者提供了强大的本地化AI解决方案。

> 译自：[Alibaba's new model promises Opus 4.6-level performance on your laptop](https://thenewstack.io/qwen38-27b-local-inference/)
> 
> 作者：Frederic Lardinois

阿里巴巴最近[公开](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)了其拥有2.4万亿参数的Qwen3.8模型权重。这是一个庞大的模型，其基准测试结果使其能够直接与美国实验室开发的闭源前沿模型展开竞争。但更有趣的是，阿里巴巴在上周五还根据Apache 2.0许可证发布了一个[270亿参数的密集型Qwen 3.8版本](https://huggingface.co/collections/Qwen/qwen38)。

这是一个你可以在配置较高的Macbook Pro或Mac Studio等设备上本地运行的模型——而且这样做是非常值得的，因为根据阿里巴巴的基准测试，该模型的性能与Anthropic在Max设置下运行的Opus 4.6处于同一水平。

在相当多的基准测试中，它的表现甚至超过了Anthropic的前旗舰模型（该模型在六个月前，即[2月发布时](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/)曾是行业顶尖水平），特别是在一些计算机使用、编程和知识工作测试中。

再加上该模型还具备视觉能力（包括视频处理），这使其成为本地使用的绝佳选择（前提是你拥有支持它的硬件）。

## 注意事项

像往常一样，这里的注意事项是，基准测试并不总是能衡量模型在现实世界中的表现。对于智能体用例，模型运行的框架与其模型本身同样重要。例如，早期报告称该模型[往往会过度思考](https://news.ycombinator.com/item?id=49299605)。

此外，阿里巴巴的基准测试似乎描述的是原始检查点，而不是大多数本地用户将运行的量化版本。量化可能会使模型在消费级硬件上变得实用，但始终存在质量上的权衡。

尽管如此，总的来说，对于一个可以在本地运行的模型来说，这些结果令人印象深刻。

![](https://cdn.thenewstack.io/media/2026/08/18936970-hpso4qibgaar-sb-1024x895.jpeg)

图片来源：阿里巴巴。

阿里巴巴指出，该模型比上一代Qwen 3.7-Plus有显著提升，尤其是在编程和知识工作任务方面，一些性能飞跃相当令人印象深刻，包括在DeepSWE智能体编程基准测试中从14.2分提升至42.2分。

这仍然落后于当前的最前沿模型（以及其他开源模型，如新发布的[GLM-5.3](https://z.ai/blog/glm-5.3)），但即使是Google的中端Gemini 3.6 Flash在这一测试中也仅达到了49%，而且你近期无法在笔记本电脑上运行该模型。

![](https://cdn.thenewstack.io/media/2026/08/10b0e960-hpso5qhasaelxuc-1024x984.jpeg)

图片来源：阿里巴巴。

阿里巴巴还将该模型与Meta的[Muse Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)进行了比较，这是另一个近期发布的规模大致相当的本地模型。在阿里巴巴报告了两个模型分数的每项测试中，Qwen3.8-27B均处于领先地位。

看来，Glimmer（微光）这个名字用在那款模型上确实很贴切。

## 在本地运行Qwen 3.8 27B所需的硬件

当然，速度是另一个问题。截至目前，阿里巴巴尚未发布参数量更小的Qwen3.8 27B混合专家模型版本。这种模型可以在每个token上激活更少的参数，从而比密集型27B版本运行得更快。例如，它之前曾为Qwen 3.6-35B模型这样做过。

非量化的Qwen3.8-27B仓库大小为55.6GB，这还不算推理运行时和上下文缓存。这不是大多数人会运行的版本。

对Mac用户来说好消息是，社区创建的[适用于Apple芯片的MLX转换版本](https://huggingface.co/mlx-community/Qwen3.8-27B-4bit)已经可用。4-bit版本大约为16.1GB，而[8-bit版本](https://huggingface.co/mlx-community/Qwen3.8-27B-8bit)为29.5GB。这使得拥有32GB统一内存的Mac成为以中等上下文长度运行4-bit版本的合理平台。如果你有48GB或64GB内存，显然会为更高的精度或更长的提示词提供相当大的空间。

默认情况下，该模型支持262,000个token的上下文，通过使用[YaRN方法](https://github.com/jquesnelle/yarn)，该上下文可以扩展到100万个token（阿里巴巴将在其托管的生产版本中进行此项工作）。但这并不意味着你可以在桌面端使用完整的上下文窗口（随着提示词增长，键值缓存会消耗更多内存）。