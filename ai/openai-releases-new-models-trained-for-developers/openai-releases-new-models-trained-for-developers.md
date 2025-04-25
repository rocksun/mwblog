<!--
title: OpenAI发布为开发者训练的新模型
cover: https://cdn.thenewstack.io/media/2025/04/4b2023c3-newopenaimodels_frontend.jpg
summary: OpenAI重磅发布GPT-4.1系列模型！专为开发者打造，前端编码能力飙升，长上下文处理达百万 tokens。同步推出推理模型o3/o4-mini，支持图像“思考”。首个Nano模型GPT-4.1 mini，速度更快成本更低！更有Codex CLI编码代理加持，速来体验！
-->

OpenAI重磅发布GPT-4.1系列模型！专为开发者打造，前端编码能力飙升，长上下文处理达百万 tokens。同步推出推理模型o3/o4-mini，支持图像“思考”。首个Nano模型GPT-4.1 mini，速度更快成本更低！更有Codex CLI编码代理加持，速来体验！

> 译自：[OpenAI Releases New Models Trained for Developers](https://thenewstack.io/openai-releases-new-models-trained-for-developers/)
> 
> 作者：Loraine Lawson

[OpenAI](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/) 在四月份发布了一系列新的 GPT 模型，专注于开发者 AI 需求，包括改进 [前端开发](https://roadmap.sh/frontend) 和一般的编码，以及遵循指令和长上下文的能力。

OpenAI 首席产品官 [Kevin Weil](https://www.linkedin.com/in/kevinweil/) 在 4 月 14 日关于此消息的直播中表示：“我们很高兴地宣布 GPT-4.1，它是 API 中的一系列模型，专门为开发者训练。” “它们甚至在许多关键方面达到或超过了 GPT-4.5。而且，它们首次具有长上下文。”

可以在该公司 [发布 GPT-4.1 模型的帖子](https://openai.com/index/gpt-4-1/) 底部观看直播。

该公司写道，GPT-4.1 模型在各种编码任务中都优于 GPT-4o，包括自主解决编码任务、前端编码、减少不必要的编辑、可靠地遵循 diff 格式以及确保一致的工具使用。

4 月 16 日，这家 AI 公司还推出了 [两个新的推理模型](https://openai.com/index/introducing-o3-and-o4-mini/)：

*   OpenAI o3，它在“编码、数学、科学和视觉理解方面表现出色”。
*   OpenAI o4-mini，这是一个更小、更快的模型，以更低的成本提供结果——尤其是在数学、编码和视觉任务方面，该公司表示。

推理模型是 OpenAI 的首批可以 [“思考”图像](https://openai.com/index/thinking-with-images/) 的模型，据该公司称。这基本上意味着它们不仅仅是“看到”图像，而是可以将视觉信息直接从图像集成到它们的推理链中。例如，开发人员可以将白板图像上传到模型，它们可以解释信息，而不仅仅是看到带有涂鸦的白板。

OpenAI o3 和 o4 模型还可以独立使用所有 ChatGPT 工具，包括网络浏览、Python、图像理解和图像生成，以更有效和独立地解决复杂的多步骤问题。

推理模型今天可供 ChatGPT Plus、Pr 和 Team 用户（o3、o4-mini、o4-mini-high）使用，取代 o1、o3-mini 和 o3-mini-high 模型。o3-pro 将在几周后推出，但目前，Pro 用户仍然可以访问 o1-pro。

最后，这家 AI 公司还在 4 月 16 日推出了 [Codex CLI](https://github.com/openai/codex)。Codex CLI 是一个轻量级的开源 [编码代理，可以在开发人员的本地](https://thenewstack.io/ai-coding-agents-level-up-from-helpers-to-team-players/) 终端中运行。

## 何时使用哪个 GPT-4.1 模型

GPT-4.1 模型仅通过 OpenAI 的 API 平台提供，而不公开在 [ChatGPT](https://thenewstack.io/what-chatgpt-and-claude-can-see-on-your-screen/) 中提供。也就是说，在遵循指令、编码和智能方面的许多改进已逐渐融入到最新版本的 GPT-4o 中。

至于新模型，在 OpenAI 的后期训练技术团队工作的 [Michelle Pokrass](https://www.linkedin.com/in/mpokrass/) 在直播中建议何时使用哪个模型。

Pokrass 说：“在决定何时使用它们时，我们建议从 4.1 开始。它是我们在编码、指令遵循和长上下文这三个维度上的强大工具。” “但是，如果您需要更快的东西，也许用于稍微简单的用例，我建议使用 4.1 mini。”

她补充说，nano 模型——OpenAI 的第一个模型——是用于自动完成、分类或从长文档中提取信息等任务的“绝对主力”。

## GPT-4.1 为开发者提供什么

根据该公司的帖子，对于前端开发人员，GPT-4.1 模型改进了前端编码。

该帖子指出：“GPT-4.1 还在前端编码方面大大改进了 GPT-4o，并且能够创建功能更强大且更美观的 Web 应用程序。” “在我们的正面比较中，付费的人工评分员 80% 的时间更喜欢 GPT-4.1 的网站而不是 GPT-4o 的网站。”

这些模型拥有更大的上下文窗口，最多支持 100 万个上下文 tokens。OpenAI 还表示，由于其改进的长上下文理解能力，GPT-4.1 可以更好地利用该上下文。

该帖子指出：“虽然基准测试提供了有价值的见解，但我们在训练这些模型时侧重于实际效用。” “与开发者社区的密切合作和伙伴关系使我们能够针对对他们的应用程序最重要的任务优化这些模型。”
这使得模型更加可靠。再加上 GPT-4.1 模型更长的上下文理解能力，结果是这些模型在驱动 AI 代理或自动化任务的系统中，比前几代模型更有效。

“我们训练了 GPT-4.1，使其能够可靠地处理完整 100 万上下文长度的信息，”博客文章说。“我们还训练它比 GPT-4o 在注意到相关文本方面更加可靠，并且能够忽略长短上下文长度中的干扰因素。长上下文理解是法律、编码、客户支持和许多其他领域应用的关键能力。”

GPT-4.1 模型在各种格式的代码差异方面也更加可靠，这对希望编辑大型文件的 API 开发者来说非常重要，文章指出。

“我们专门训练了 GPT-4.1，使其能够更可靠地遵循差异格式，这使得开发者只需让模型输出更改的行，而不是重写整个文件，从而节省成本和延迟，”文章指出。

不过，一个很大的吸引力可能是 GPT-4.1 模型承诺以更低的成本点提供更好的性能。

值得注意的是，这些模型具有“2024 年 6 月的最新知识截止日期”，该公司表示。

GPT-4.1 模型在各个方面都优于 GPT-4o 和 GPT-4o mini，“在编码和指令遵循方面有重大提升”，该公司在一篇关于该公告的博客文章中表示。

“当与 [Responses API](https://platform.openai.com/docs/api-reference/responses) 等原语结合使用时，”文章指出，“开发者现在可以构建在实际软件工程中更有用和可靠的代理，从大型文档中提取见解，以最少的人工干预解决客户请求，以及其他复杂任务。”

## 评估 GPT-4.1 模型

为了创建 GPT-4.1 模型，OpenAI 团队为这些模型创建了一个内部评估，该评估借鉴了开发者常见的关注点，例如评估模型的能力：

- 使用特定格式，例如 [XML](https://thenewstack.io/vintage-computer-festival-2017-giant-floppy-disks-json-vanquished-xml/)、[YAML](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/) 或 [Markdown](https://thenewstack.io/introduction-to-markwhen-a-markdown-timeline-tool-for-devs/)。
- 遵循有序指令。
- 理解指定模型应避免的行为的否定指令。
- 如果请求的信息不可用，则训练模型说“我不知道”。

该博客文章还包括有关新模型基准的详细信息。

## OpenAI 的首个 Nano 模型

OpenAI 还发布了其首个 nano 模型，GPT-4.1 mini。

“它在智能评估中与 GPT-4o 相匹配或超过 GPT-4o，同时将延迟降低了近一半，并将成本降低了 83%，”该公司的帖子指出。“对于需要低延迟的任务，GPT-4.1 nano 是我们最快且最便宜的可用模型。”

该帖子接着说，新的 nano 模型以其 100 万个 token 的上下文窗口提供了“卓越的性能，并且在 MMLU 上得分 80.1%，在 GPQA 上得分 50.3%，在 Aider polyglot coding 上得分 9.8%——甚至高于 GPT-4o mini。”