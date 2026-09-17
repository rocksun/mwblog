<!--
title: GPT Images 2.5发布：承诺实现精准图像局部编辑功能
cover: https://cdn.thenewstack.io/media/2026/09/c91d497d-openai-images-2.5.png
summary: OpenAI推出GPT Images 2.5，新增Flare（快速型）与Sunburst（精准型）模型。新版增强了局部图像编辑能力，但在成本预估和具体性能差异上仍需开发者进一步探索。
-->

OpenAI推出GPT Images 2.5，新增Flare（快速型）与Sunburst（精准型）模型。新版增强了局部图像编辑能力，但在成本预估和具体性能差异上仍需开发者进一步探索。

> 译自：[GPT Images 2.5 promises edits that leave the rest of your image alone](https://thenewstack.io/gpt-images-2-5-sunburst-flare/)
> 
> 作者：Meredith Shubel

**本周，OpenAI发布了GPT Images 2.5**，该公司承诺为一项常见的编辑任务提供更好的结果：修改图像的一部分而不破坏其余部分。

因此，开发者现在有两个新模型可供尝试：Flare和Sunburst。但对于在两者之间进行选择的人来说，还有一些功课要做。OpenAI列出了两者的相同代币费率，但并未解释它们在每张图像成本上的具体差异。

Flare被定位为大多数应用场景中更快速的“默认”选择，而Sunburst则在编辑时提供更高的精度和控制力，但生成时间更长。OpenAI为两个模型列出了相同的代币费率，尽管它们在实际应用中的成本对比尚不明确。

## Flare 对比 Sunburst

OpenAI [称](https://openai.com/index/introducing-chatgpt-images-2-5/) Flare 是“大多数应用场景的默认选择”，使开发者能够以比前代模型更低的延迟提升图像质量。据这家AI公司称，这意味着该模型可以处理任何日常图像生成工作负载，例如社交内容、快速图像原型设计、视觉搜索和图像生成。

最有趣的是，OpenAI表示，Flare交付的图像质量高于GPT-Image-2，且延迟降低了50%。

与此同时，这家AI公司将Sunburst定位为更精确的选择，称该图像模型是“为那些受益于更严密编辑控制的高级视觉工作流程而打造的”。对于从事高风险创意资产（如生产级广告活动或产品图像）工作的开发者来说，Sunburst看起来是更好的选择。

但OpenAI并未明确Sunburst更高的精度在时间和金钱方面相比Flare究竟会增加多少成本。

## 相同的代币费率，未必是相同的账单

在书面上，OpenAI表示Flare和Sunburst具有相同的代币费率：每百万文本输入代币5美元，每百万图像输入代币8美元，每百万图像输出代币30美元。但这并不一定意味着对于同一种图像，使用任一模型的成本都相同。

尽管图像生成定价基于代币数量，但该公司对于如何预估GPT-Image-2.5的代币消耗并没有明确的说明。

如果开发者认为可以参考OpenAI现有的[图像成本计算器](https://developers.openai.com/api/docs/guides/image-prompting)来预估新模型的图像生成成本，那可能要再想想了。该公司确实做出了一个[明确](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)的声明：“代币费率与GPT Image 2一致。GPT Image 2计算器无法预估GPT Image 2.5的代币消耗。”

> 在书面上，OpenAI表示Flare和Sunburst具有相同的代币费率：每百万文本输入代币5美元，每百万图像输入代币8美元，每百万图像输出代币30美元。但这并不一定意味着对于同一种图像，使用任一模型会产生相同的账单。

由于没有保证的方法来预估每个模型将使用多少代币，这意味着在开始使用之前，无法从OpenAI公布的定价中判断使用Flare还是Sunburst生成同类图像的成本。

此外还有延迟问题。

OpenAI称Flare交付的图像质量高于GPT-Image-2，且延迟降低了50%。但Flare与Sunburst相比如何呢？

无论是其发布公告，还是[Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)或[Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)的模型页面，都没有明确说明两者在生成时间上的差异。仅在其发布公告中提到，Sunburst更好的精度伴随着“更长的生成时间”，这让开发者对具体长多少感到困惑。

![](https://cdn.thenewstack.io/media/2026/09/ad835913-openai-image-1-1024x576.webp)

来源：[OpenAI](https://openai.com/index/introducing-chatgpt-images-2-5/)

## 总体而言，Images 2.5 在修改局部而不破坏整体方面变得更出色

通过ChatGPT Images 2.5，OpenAI承诺了更好的图像质量、编辑能力和速度。

具体来说，使用API进行构建的团队可以期待更可靠的参考导向工作流程，这得益于更高的图像保真度，使每次变体与原始源保持更紧密的联系。

编辑功能也得到了升级，具备了新的精度能力，让开发者可以只修改图片的一部分，如产品、背景或文本，同时保留周围的场景。ChatGPT现在还可以更紧密地遵循编辑指令，即使是在多轮编辑中也是如此。在生产工作流程中，开发者通常需要精确的修改，这可以节省团队为了几次微调而重建整个资产的时间。

随着预期的智能和风格改进，ChatGPT有望在第一次尝试时就生成更多正确的图像，甚至不需要额外的编辑。OpenAI还表示，其新的图像模型“在理解复杂的视觉指令并将其转化为连贯结果方面表现更好”。

更简单的编辑、更高的图像质量以及Flare带来的更快的图像生成速度，可能会使图像密集型工作流程变得更加顺畅。但开发者必须对这两个模型进行实验，以确定Sunburst增加的精度是否值得额外的时间，以及潜在增加的成本。