
<!--
title: 人人都能“说”编程？AI工具加持，编程范式或将迎来新革命
cover: https://cdn.thenewstack.io/media/2025/02/7d66d2fd-headway-jfr5wu2hmi0-unsplash-1.jpg
-->

随着人工智能工具越来越擅长理解自然语言，开发人员正在拥抱“氛围编程(vibe coding)”——一种新的编程范式，其中口语取代了打字，意图比语法更重要。

> 译自 [Vibe Coding: Where Everyone Can ‘Speak’ Computer Programming](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)，作者 Darryl K Taft。

2023 年，[Andrej Karpathy](https://github.com/karpathy) 表示英语是[最热门的新编程语言](https://x.com/karpathy/status/1617979122625712128)，由此，他再次提供了他对 AI 世界的愿景，以及本月早些时候他创造“vibe coding”一词时[自然语言](https://thenewstack.io/service-simplifies-natural-language-processing-for-developers/)在编程中的应用。

> 有一种我称之为 “vibe coding” 的新型编码，在这种编码中，你完全屈服于 vibes，接受指数，甚至忘记代码的存在。这可能是因为 LLM（例如 Cursor Composer w Sonnet）变得太好了。此外，我只是使用 SuperWhisper 与 Composer 交谈......
>
> — Andrej Karpathy (@karpathy)
>
> [February 2, 2025]

“有一种我称之为'vibe coding'的新型编码，你完全屈服于共鸣，拥抱指数，甚至忘记代码的存在，”他在 X 上的一篇文章中写道，“这可能是因为 LLM（例如 Cursor Composer w Sonnet）变得太好了。此外，我只是使用 SuperWhisper 与 Composer 交谈，所以我甚至几乎不碰键盘。

Karpathy 是 [OpenAI](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/) 的联合创始人，现在创办了一家名为 [Eureka Labs](https://eurekalabs.ai/) 的新 AI+教育公司。

Omdia 的分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 认为 [Cline](https://cline.bot/) 是一种流行的工具，它使用自然语言来帮助编码，并且对于 vibe coding 很有用。
Shimmin 指出，事实上，在 GenAI 领域中，一些主要参与者正在使用英语进行编程，其中包括 Microsoft、OpenAI、Anthropic、Google、IBM 和 AWS 等。他们正在开发具有改进的工具使用和结构化输出的模型。提到的一些关键开发平台包括带有 VS Code 的 GitHub Copilot、Replit（它是 AI 集成的早期采用者）、[Aider](https://aider.chat/)、Cline、[Cursor](https://www.cursor.com/) 和 [Zed](https://zed.dev/)。

同时，Cline 的产品营销主管 [Nick Baumann](https://www.linkedin.com/in/nick-baumann-b145bb154/) 告诉 The New Stack，vibe coding 是一种使用 AI 进行编码的高级方法，用户从最终用户的角度而不是技术规范来描述需求。

“它使用自然语言来传达期望的结果，例如‘使英雄部分更具表现力’，”他说。“它允许 AI 处理技术实现细节。”

在最近的一篇[博客文章](https://cline.bot/blog/from-assembly-to-ai-why-vibe-coding-is-just-another-chapter-in-our-abstraction-story)中，Baumann 写道：“两天前，Andrej Karpathy 用一个他称之为‘vibe coding’的挑衅性想法点燃了 Tech Twitter——在那里你‘完全沉浸在氛围中，拥抱指数，忘记代码的存在。’使用 AI 工具（如 Cline），他演示了在大约一个小时内构建一个完整的 LLM 阅读器应用程序，几乎没有接触键盘。”

## 根本转变

在他的信息量很大的文章中，Baumann 解释了一切，并将 vibe coding 描述为编程演变中的又一个篇章。

但是，“是什么让‘vibe coding’如此引人入胜：它不仅仅是另一层——它可能是我们向计算机表达意图方式的根本转变，”他在文章中写道。“我们不再通过精确的指令告诉机器该做什么，而是转向用自然语言描述我们想要什么。”

此外，“在 Cline，我们认识到这种历史模式。正如 C 没有消除汇编语言，而是使汇编语言对于大多数任务来说变得不必要一样，AI 不会消除传统编码，而是会改变我们花费认知努力的地方，”他写道。

尽管如此，Baumann 指出，“vibe coding”是否会像以前的抽象一样成为根本，还有待观察。“但有一点是明确的：那些完全否定它的人正在呼应 1957 年的汇编程序员、1973 年的系统程序员以及所有其他抵制最终成为标准的新抽象层的群体，”他写道。

## 什么是 Cline？

最初被称为 Claude Dev（因为它专注于 Anthropic 的 Claude Sonnet 3.5 LLM），Cline 被重命名以反映它是一个可以使用你的 CLI（命令行界面）和编辑器 — CLINE 的 AI 助手。

Cline 是一个用于 AI 辅助编码的 VS Code 扩展。它允许在 VS Code 中进行聊天对话，并且可以读取、写入和编辑代码库中的文件。它还会通过检查代码库和提问来主动寻找上下文。
Cline 是一个免费的扩展，但采用“自带 API 密钥”模式。它与各种 AI 模型配合使用，包括 Claude 3.5 Sonnet 和一些 [DeepSeek](https://thenewstack.io/how-to-run-deepseek-r1-on-aws-using-infrastructure-as-code/) 模型，作为一种更便宜的替代方案。

它因“氛围编码 (vibe coding)”而流行，在这种编码方式中，开发人员用自然语言描述期望的结果。该工具旨在表现得像“身边有一个很棒的工程师”，并且可以处理各种级别的规范，从模糊的需求到具体的技术细节。

## 氛围编码者的类型

与此同时，Baumann 在接受 The New Stack 采访时表示，氛围编码者主要分为两类：不借助 AI 辅助就不会编码的编码新手，以及使用 AI 将生产力提高数倍的经验丰富的工程师。

“进行氛围编码的人是使用 AI 进行编码的人，或者是编码新手。这些人如果没有 AI，根本就不会编码……然后是另一类人，他们是非常有经验的工程师，不需要 AI，但发现他们可以进一步利用他们的编码技能，提高 10 倍或 100 倍，”他说。

## 编码的新纪元

Constellation Research 在 2023 年发布的一份报告中写道，开发人员编写代码的职能将在未来五年内开始逐渐消失，并且可能在 15 年后完全消失，该报告由分析师 Holger Mueller 撰写。

“更重要的是，这种情况将使开发人员摆脱掌握代码的需要，因为主要的输入将是语音而不是键盘。语音作为一种输入方式，比任何打字方式都更快、更有效，但关键的创新是软件正在编写软件，”报告称。

他说，这将大大扩大可以构建应用程序的人数。

“实际上，从键盘到语音，以及从代码到自然语言 (NL) 的转变意味着将能够构建更多的软件，并且更多的业务用户将能够掌控他们的自动化命运，”报告写道。

在一次采访中，Mueller 告诉 The New Stack，他通过说话和打字，使用 Microsoft 的 Power Platform 和 ChatGPT 创建了应用程序。从本质上讲，他就是在进行氛围编码。
