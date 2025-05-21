<!--
title: Google的Gemini模型更进一步
cover: https://cdn.thenewstack.io/media/2025/05/bbd93769-img_0902-scaled.jpg
summary: Google I/O大会发布 Gemini 2.5 Flash/Pro，性能提升！Deep Think推理模型将通过 Gemini API 提供，并加入 Gemini AI Ultra 计划。全新 Gemini diffusion 模型加速文本生成。Project Mariner 接管浏览器，集成到 AI 模式，实现自动化任务，云原生AI能力更进一步。
-->

Google I/O大会发布 Gemini 2.5 Flash/Pro，性能提升！Deep Think推理模型将通过 Gemini API 提供，并加入 Gemini AI Ultra 计划。全新 Gemini diffusion 模型加速文本生成。Project Mariner 接管浏览器，集成到 AI 模式，实现自动化任务，云原生AI能力更进一步。

> 译自：[Google's Gemini Models Go Deeper](https://thenewstack.io/googles-gemini-models-go-deeper/)
> 
> 作者：Frederic Lardinois

谷歌今年的 [I/O 开发者大会](https://io.google/2025/) 的主题是人工智能。考虑到该公司几周前已经发布了通常会在活动中推出的传统 Android 更新，这实际上并不令人惊讶。去年，谷歌 CEO Sundar Pichai 宣布了 Gemini 时代的开始，在某些方面，我们现在已经进入了 Gemini 2.0 时代（或者可能是 2.5，考虑到其模型的当前版本号）。

在许多方面，今天的 Gemini 公告并非革命性的，而是在谷歌过去一年建立的基础之上构建的。例如，我们没有得到 Gemini 3.0 模型，而是得到了 2.5 Flash 和 Pro 模型的更好版本，它现在在一些标准基准测试中得分更高。

![图片来源: The New Stack](https://cdn.thenewstack.io/media/2025/05/fef263c1-99a2eb37-4a6c-4b17-98c2-e5f946a6c84e-scaled.jpg)

*图片来源: The New Stack.*

在今天的主题演讲之前的新闻发布会上，Pichai 指出，在其他年份，谷歌会在活动前几周保持沉默，并将最佳模型的发布保留到 I/O 大会上，但由于技术发展如此之快，这在“Gemini 时代”是不可能的。

公平地说，它们确实获得了一些新功能，例如用于更自然的对话体验的本机音频输出、新的安全保障等。

有趣的是，消费者将比开发者更早获得这些更新的模型。它现在已在 Gemini 应用程序中提供，Google AI Studio 和 Vertex AI 将在 6 月初获得对 2.5 Flash 的支持，2.5 Pro 将在稍后推出。

## 更进一步

然而，真正的创新在于如何使用这些模型。

例如，谷歌展示了一个增强的“Deep Think”推理模型，用于 2.5 Pro 模型，它建立在今天的研究模型之上，但能够更深入地研究并在响应之前测试多个假设。谷歌表示，这种新模式几乎在所有当前的 Frontier 模型中都优于数学和编码基准。

然而，该模式尚未向消费者或开发者提供，但很快将通过 Gemini API 提供给一些受信任的测试人员。

![图片来源: The New Stack](https://cdn.thenewstack.io/media/2025/05/dc0e57c3-6638bd37-fd0e-48fd-9425-c490a8d7813f-scaled.jpg)

*图片来源: The New Stack.*

所有这些深度意味着该模型将使用相当多的 tokens，并且成本也会相应提高。即将推出，开发者将能够为 Gemini 2.5 Pro 设置一个思考预算，允许他们设置在思考项目期间生成的最大 tokens 数量。

这里还有另一个注意事项：Deep Think 将成为谷歌新的 Gemini AI Ultra 计划的一部分，该计划每月收费 249 美元，甚至高于 OpenAI 每月 200 美元的 [Pro plan](https://openai.com/chatgpt/pricing/)。谷歌的计划将包括访问 Deep Think、提前访问 [Gemini in Chrome](https://gemini.google/cms/login?continue=%2Foverview%2Fgemini-in-chrome%2F%3Fpreview%3Dtrue)、NotebookLM 的更高使用限制，以及以视频为中心的 Whisk 和 Flow 生成式 AI 工具（Flow 是谷歌新的 AI 电影制作工具）。还包括 YouTube Premium 和 30TB 的在线存储。

## 通过 Diffusion 加快速度

谷歌今天还推出了一个新的 Gemini diffusion 模型。通常，diffusion 模型用于图像生成而不是文本生成，以多个步骤生成图像，随着时间的推移变得更加详细，谷歌找到了一种使用这种技术生成文本的方法，模型在生成文本时来回移动。

在公司今天展示的演示中，该模型在一秒钟内生成了数学解决方案。但目前，该公司没有提供有关此模型的任何其他详细信息。

![Google's Gemini Diffusion model](https://cdn.thenewstack.io/media/2025/05/b72864cc-img_0932-scaled.jpg)
图片来源: The New Stack.

## Project Mariner 接管浏览器

也许这些即将推出的新 Ultra 功能中最有趣的是 Project Mariner。Project Mariner 于去年宣布，现在已准备好更广泛地使用，它是谷歌的代理计算机使用工具——这意味着它可以代表用户使用浏览器。Mariner 可以同时处理多达 10 个任务，从查找信息到为用户进行预订和购买商品。这些功能将在今年晚些时候的某个时候添加到 Gemini API 中。

OpenAI 的 Operator 和其他公司最近也宣布了类似的功能。
在谷歌搜索中，谷歌也开始展示 Project Mariner。去年，谷歌在搜索中发布了“AI 模式”。这种模式结合了谷歌搜索及其最新的大型语言模型，以前只作为一项实验提供，但现在，它可以代表所有谷歌用户（在美国）进行研究。

谷歌表示，由于许多此类搜索都是关于完成某件事，因此它正在将 Project Mariner 集成到 AI 模式中，以帮助用户购买门票、进行餐厅预订和进行本地预约。对其他用例的支持将在稍后推出。

AI 模式还将提供个性化建议，这些建议将考虑来自 Gmail 和其他 Google 应用程序的数据。这是一个可选功能，虽然谷歌强调它正在以隐私至上的方式进行所有这些操作，但并非所有人都会对此感到满意。