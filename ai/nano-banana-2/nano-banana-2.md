<!--
title: 谷歌Nano Banana 2：闪速呈现，专业级效果
cover: https://cdn.thenewstack.io/media/2026/02/68a98eaf-landscape.png
summary: Google发布了最新图像生成模型Nano Banana 2（即Gemini 3.1 Flash Image）。它融合了Flash的速度与Pro模型的专业功能，显著提升了文本渲染、主体一致性、多图像输入处理和指令遵循能力，并支持实时数据访问，旨在弥合速度与视觉保真度的差距，将成为Gemini应用等产品的默认模型。
-->

Google发布了最新图像生成模型Nano Banana 2（即Gemini 3.1 Flash Image）。它融合了Flash的速度与Pro模型的专业功能，显著提升了文本渲染、主体一致性、多图像输入处理和指令遵循能力，并支持实时数据访问，旨在弥合速度与视觉保真度的差距，将成为Gemini应用等产品的默认模型。

> 译自：[Google's Nano Banana 2 promises Flash speeds with Pro results](https://thenewstack.io/nano-banana-2/)
> 
> 作者：Frederic Lardinois

周四，Google [发布了](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)其最新版本的 [Nano Banana](https://blog.google/products-and-platforms/products/gemini/updated-image-editing-model/) 图像生成模型，该模型有望在几乎所有方面，特别是速度方面，超越去年11月的 Nano Banana Pro 和更早的 Nano Banana 1。

Nano Banana 的官方名称是 Gemini 3.1 Flash Image，其中的“Flash”表明了其出身。Google 的 Flash 模型一直专注于速度而非原始智能，但对于 Nano Banana 2，该公司也正在将 Nano Banana Pro 的许多功能带到这个更快的模型中。

这意味着，例如，新模型还将利用 Gemini 的真实世界知识库，并可以访问来自网络的实时数据和图像。

Google 在今天的公告中解释道：“这种深刻的理解还可以帮助您创建信息图表、将笔记转换为图表以及生成数据可视化。”

它在文本渲染方面也大大改进，这也是大多数第一代图像生成模型曾面临的难题。今天的模型在这方面已经相当不错，而 Nano Banana 2 通过按命令翻译和本地化文本，将其提升了一个台阶。

![](https://cdn.thenewstack.io/media/2026/02/123e9156-infographic-2.png)

*图片来源：Google。*

旧的 Pro 模型并不会消失，至少对于 Google AI Pro 和 Ultra 订阅者来说，他们仍然可以将其用于专业任务。

正如 Google 在其公告中指出，Nano Banana 2 旨在“弥合速度和视觉保真度之间的差距”。

![](https://cdn.thenewstack.io/media/2026/02/ca52721f-museum.png)

图片来源：Google。

Nano Banana 1 的改进包括更好的主体一致性，例如。该模型现在可以在单个工作流中跟踪多达五个角色和14个对象，这应该有助于更容易地进行故事板构思等。这与 Nano Banana Pro [发布时可以做到的](https://blog.google/innovation-and-ai/products/nano-banana-pro/)相匹配。

光照、纹理和细节现在也应该更加真实。

与 Nano Banana Pro 一样，它可以将多张图像作为输入，并将它们组合成一个连贯的结果。

![](https://cdn.thenewstack.io/media/2026/02/69b16203-multi-input.jpg)

*图片来源：Google。*

Google 表示，新模型在遵循指令方面也表现更好，尤其是在处理复杂请求时，并且更容易以不同的纵横比和分辨率生成图像的多个版本。

![](https://cdn.thenewstack.io/media/2026/02/1278f007-aspect-ratio.png)

*图片来源：Google。*

该模型在正式发布前不久在 Gemini 应用中上线，经过一番测试，新模型确实快了很多。它仍然偶尔会犯一些有趣的错误（请看下图喷气式登机桥上的旅客、下面徽标颜色的变化以及被破坏的 United 字样），但当被提示时，它也非常善于修复这些错误。

![](https://cdn.thenewstack.io/media/2026/02/b6e3b695-gemini_generated_image_ueha9sueha9sueha-scaled.png)

*由 Gemini 应用中的 Nano Banana 2 生成的图像。提示：“在机场登机口的一架737飞机上创建一个 *New Stack* 标志的图像。”*

Nano Banana 2 将成为 Gemini 应用以及 Google 搜索的 AI 模式和 Lens 的默认模型。对于使用 Google API 的开发者来说，它现在已在 AI Studio、Gemini API 和该公司的 [Antigravity](https://antigravity.google/) 下一代 IDE 中提供预览。它也将成为 Google 的视频生成工具 Flow 和 Google Ads 的默认模型。