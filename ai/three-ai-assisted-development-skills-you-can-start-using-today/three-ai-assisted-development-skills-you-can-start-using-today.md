
<!--
title: 你可以立即开始使用的三项AI辅助开发技能
cover: https://cdn.thenewstack.io/media/2025/04/be67445e-aws-ai-developer-skills-use.jpg
summary: AI开发提速！拥抱“氛围编码”，用自然语言驱动代码生成，解放生产力！告别死磕Prompt Engineering，让AI帮你优化！关注嵌入式和代理式AI，如Amazon Q Developer CLI，体验Bedrock和Claude Sonnet 3.7带来的git命令和AWS CLI操作简化，迎接AI Agent重塑的开发未来！
-->

AI开发提速！拥抱“氛围编码”，用自然语言驱动代码生成，解放生产力！告别死磕Prompt Engineering，让AI帮你优化！关注嵌入式和代理式AI，如Amazon Q Developer CLI，体验Bedrock和Claude Sonnet 3.7带来的git命令和AWS CLI操作简化，迎接AI Agent重塑的开发未来！

> 译自：[Three AI-Assisted Development Skills You Can Start Using Today](https://thenewstack.io/three-ai-assisted-development-skills-you-can-start-using-today/)
> 
> 作者：Loraine Lawson

[AI](https://thenewstack.io/ai/) 领域的变化日新月异， 仿佛开发者们总有学不完的东西。The New Stack 最近采访了 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 的生成式 AI (GenAI) 首席开发者倡导者 Antje Barth，了解开发者如何为日益增长的 [AI 驱动的企业](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/)做好准备。

Barth 分享了 AI 如何改变开发，以及软件工程师如何适应 AI 开发的新现实。

## 1. 转向 AI 进行代码创建

当 [大型语言模型](https://thenewstack.io/llm/) (LLM) 在 2022 年底 [OpenAI 的 ChatGPT-3 发布](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/) 后成为焦点时，代码纠正立即成为一个明显的用例。[大量代码助手开始涌现](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/)。

虽然这些仍然很受欢迎，但现在的最前沿是“[氛围编码](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)”，它利用 AI 的自然语言能力来创建代码。这个[术语由](https://x.com/karpathy/status/1886192184808149383?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1886192184808149383%7Ctwgr%5Eb693bc66e22eeb798ec744f69374aeea4cab7926%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fthenewstack.io%2Fvibe-coding-where-everyone-can-speak-computer-programming%2F) [数据科学家](https://roadmap.sh/ai-data-scientist) Andrej Karpathy 在 2023 年创造，此后稳步受到关注。

“有一种新的编码方式，我称之为‘氛围编码’，在这种编码方式中，你完全沉浸在氛围中，拥抱指数，忘记代码的存在，” Karpathy 在 X 上的一篇文章中写道。“这是可能的，因为 LLM（例如带有 Sonnet 的 Cursor Composer）变得太好了。此外，我只是通过 SuperWhisper 与 Composer 交谈，所以我几乎没有碰过键盘。”

氛围编程超越了代码纠正，通过自然语言提示使用 AI 创建整个代码，如果需要，这些提示也用于改进代码。Barth 说，这使得编程更加直观。

她提到了像 [Amazon Q ](https://thenewstack.io/amazon-q-developer-now-handles-your-entire-code-pipeline/)[Developer](https://thenewstack.io/amazon-q-developer-now-handles-your-entire-code-pipeline/) 这样的工具以及市场上其他的代码助手，它们允许用户用自然语言进行交流。她指出，它们不仅仅生成代码，还可以用于整个软件开发生命周期中，以创建单元测试、[文档](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/)和其他开发任务。

“氛围编码目前吸引了所有人的注意力，”Barth 说。“我真的认为这是一种进化，而不是一个全新的概念，这令人兴奋。”

这引发了关于组织是否还需要开发者了解代码的问题。

“业内也有不同的观点，但我强烈认为，编码是一项至关重要的技能，一项超级关键的技能，它不仅仅是编写代码，还要阅读代码，并且能够理解什么是高质量的代码，以及它是否正是我应用程序需要的代码，”她说。

但是，她补充说，“我也看到 AI 辅助和围绕它的工具可以增强你作为开发者的能力，让你更快。”

她设想的过程是使用 AI 快速生成原型代码，并确定一个想法是否可行。当原型被投入到更大的系统中进行生产时，软件工程师的技术知识就发挥作用了。

“围绕氛围编码绝对有很大的机会可以开始，然后，显然可以在整个周期中使用这些工具，”她说。“但知识确实至关重要。”

## 2. 让 AI 编写自己的提示

[提示工程](https://thenewstack.io/developer-tips-in-ai-prompt-engineering/) 在 [ChatGPT-3 问世后风靡一时](https://thenewstack.io/how-will-generative-ai-change-the-tech-job-market/)。但 Barth 认为，除非你只是对此感到好奇，否则没有理由为提示创建而烦恼。

> “现在，我的建议是实际上使用 AI 来创建一个好的提示。”
>
> — Antje Barth, AWS 生成式 AI 首席开发者倡导者

“一年前，我肯定会告诉你，提示工程是一项至关重要的技能，”Barth说。“但现在，我的建议是实际上使用AI来创建好的提示。在你给出详细的指令之前，我会问AI，‘嘿，这就是我想完成的事情；帮我创建一个真正、真正可靠且好的提示来实现这个目标。’”

她补充说，让AI编写自己的提示也是可取的，因为不同的AI系统有不同的、独特的方式来提示。

“我应该对为什么这很重要以及如何构建有一个基本的了解，但实际的提示编写，这些天我完全可以使用AI来完成。”

## 3. 使用嵌入式和代理式AI

部分归功于[AI agents](https://thenewstack.io/ai-agents/)（AI代理），AI正在从最初的聊天机器人界面转变为嵌入式工具，这些工具高度专业化，可以处理工作流程或任务。对于前端和Web应用程序开发人员来说，这是一个特别关键的趋势，他们需要弄清楚如何在用户界面中嵌入AI功能。

例如，[Amazon Q Developer started as a chatbot](https://aws.amazon.com/blogs/devops/aws-chatbot-is-now-named-amazon-q-developer/)（Amazon Q Developer 最初是一个聊天机器人）。虽然你仍然可以这样使用它，但亚马逊在3月6日推出了新的[Amazon Q Developer CLI](https://aws.amazon.com/blogs/devops/introducing-the-enhanced-command-line-interface-in-amazon-q-developer/)（Amazon Q Developer CLI）。Barth说，它基本上是一个增强的代理，可以镜像开发人员在使用Amazon Q的内部开发环境（IDE）中的体验，但从CLI内部进行。

“Q的CLI支持已经推出一年多了，但现在它具有与IDE体验相匹配的代理能力，”她告诉The New Stack。“这意味着，通过代理式AI，系统最终使用高质量的语言模型来帮助它进行推理和规划。在这种情况下，Q Developer CLI构建在[Bedrock](https://thenewstack.io/amazons-bedrock-can-now-check-ai-for-hallucinations/)之上，并使用Claude Sonnet 3.7，因此它具有非常高质量的推理能力，你可以在CLI中使用自然语言聊天，这让生活变得更加轻松。”

Barth说她几乎每天都使用这个工具。它简化的一项任务是处理[git commands](https://git-scm.com/docs)（git命令）。

“例如，我不再需要记住如何在语法中撤销[git](https://thenewstack.io/tutorial-git-for-absolutely-everyone/)提交，”她说。“我可以直接用自然语言告诉它，‘嘿，请为我恢复上次的git提交，’它会为我提供正确的CLI BASH命令。”

类似地，她可以问它，“在这个区域里，我的S3存储桶是什么？”它会将其翻译成正确的AWS CLI语法。

“这就是我们看到代理式AI改善开发者体验的地方，”Barth说。“每个应用程序，可能每个客户体验、用户体验，都将被代理式AI颠覆。”