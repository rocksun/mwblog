<!--
title: 年终总结：大语言模型的开发工具与助手
cover: https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1-1024x576.png
-->

今年对于大语言模型来说是个重要的一年。对于开发者而言，LLM的影响主要体现在人工智能开发工具和助手领域。

> 译自 [Large Language Models in 2023: Tools and Assistants for Devs](https://thenewstack.io/large-language-models-in-2023-tools-and-assistants-for-devs/)，作者 David Eastman 曾是一位在伦敦工作的专业软件开发者，曾在 Oracle Corp. 和英国电信（British Telecom）任职，并作为顾问帮助团队更敏捷地工作。他撰写了一本关于 UI 设计的书籍，此后一直在撰写技术文章...

今年对于大语言模型（LLMs）来说是突破性的一年。但是开发者仍然处于充分发挥其力量的早期阶段。

当有人告诉我一位潜在的面试候选人在回答基于网络的问题时使用ChatGPT时，我心情复杂。这有点像学生第一次获得手持计算器的使用权时的感觉。如今，在数学考试中使用计算器已不再被视为问题 —— 它们可以自由使用。最终，算术只是数学的一小部分，而计算器绝对只是一个工具。然而，使用ChatGPT来替代自己的技能和知识似乎既不必要又令人感到绝望。但今年的证据表明，对于开发者来说，**人工智能主要体现在工具或助手的形式中**。

LLM的核心在于那个第一个词：Large。只有在吸收了大量数据后，它们才能表现得如此出色。我尝试使用类似的技术，但没有神经网络的支持，结果没有产生出任何像样的诗歌，但确实展示了吸收文本语料库的过程。

![Zoom](https://cdn.thenewstack.io/media/2023/12/cb636fe5-llm_robot.jpg)

*通过Stable Diffusion获取的图像；提示：“一个巨大的机器人从眼睛中发射激光，所有人都在惊恐奔逃”*

ChatGPT 在回答查询时整合信息的能力是无价的。（尽管对于回答许多查询，你可能会发现 [Perplexity.ai](http://perplexity.ai/) 有更好的体验）许多开发者被他们能够迅速将[一个完全解释的代码示例](https://thenewstack.io/lets-talk-conversational-software-development/)快速引入到他们的项目中的方式所吸引。但作为工具的优势在于它们能够以最小的摩擦提高开发者的效率。

## AI 开发工具

今年主要是关于开发工具，通常包括 AI。Rust 在构建更快的全屏工具方面发挥了作用，[Zed](https://thenewstack.io/zed-a-new-multiplayer-code-editor-from-the-creators-of-atom/) 和 [Warp](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) 都是强有力的例子。Zed 是一个功能齐全的“多人”编辑器，专为速度而建。Zed2 应该很快就会发布，我注意到他们在 [Tailwind](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/) 补全方面的工作。Warp 在命令行方面持续创新。

在工具中采用 AI 对许多努力至关重要。首批大浪潮来自 Visual Studio 中的 [Copilot](https://thenewstack.io/the-changing-role-of-human-developers-in-an-ai-and-llm-world/)。我还看了看 [Replit](https://replit.com/~) 的 [Ghostwriter](https://thenewstack.io/ghost-in-the-ide-testing-replits-ai-helper-ghostwriter/)，以及 [CodiumAI](https://www.notion.so/Sovereign-AI-87ae9e55f1a3419281259457b75b81f9?pvs=21) 的[测试生成器](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/)。[Cursor](https://cursor.sh/) 拥有以 AI 为先导的[编辑器](https://thenewstack.io/testing-an-ai-first-code-editor-good-for-intermediate-devs/)。

其中许多只是对代码示例进行 AI 封装请求而已。但 Copilot 能够在仅看到签名的情况下完成一个类方法，如果方法名相当规范的话。我对像这样直接在代码窗口内部输入代码的功能印象更深，而不是在单独的窗口中输入文本。目前 Microsoft 似乎有更好的方向，但随着其他项目的成熟，这将会改变。

[CodiumAI](http://codium.ai/) 的[测试生成器](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/)确实证明了人工智能可以直接在开发周期中发挥作用，通过根据现有的编码方法生成明智的单元测试。在编码周围有许多辅助任务，人工智能可以提供帮助。

## 但完整的开发周期呢？

这就是我们需要解决代码涉猎者和专业开发者不同需求的地方，以及为什么目前的设计对两者都不太适用。我坦率地认为，完整的开发周期仍然对于涉猎者来说过于棘手，人工智能工具尚不能改变这一点。

请记住，一个缺失的引号仍然可能导致整个代码文件无法编译。但另一方面，每天编码的人们正在寻找许多小而持续的辅助，而不是从网络上获取大块的代码。这些智慧可以由大语言模型得出，但对编辑器界面的精准控制是至关重要的。如果它打断了我的工作流程，任何建议都是无用的。

今年我们看到了一些平台，它们帮助开发者间接地使用大语言模型。我认为现在谈论它们还为时过早，因为来自OpenAI的进一步进展可能会轻松削弱它们的效用。我接触过的一个例子是 [Fixie](https://thenewstack.io/fixie-and-its-agent-approach-to-leveraging-llms/)，它使用一种代理方法来利用大语言模型。

## 开发者应该担心失业吗？

那么关于大语言模型工具编写整个项目呢？开发者的工作是否面临风险？我们现在都必须作弊吗？

开发者有两项每天都在使用的技能，推动工作的进展：建立联系和理解过渡。这对于大语言模型（LLMs）来说几乎是不可及的，但目前这些仍然是特定的人类特质。

项目的过渡需要对员工、组织的财务状况、商业环境等的理解。从关系型数据库转变到[Redis](https://redis.io/)键值存储，然后再转移到云上的新系统，理论上ChatGPT可能会提出这样的建议，但没有人会完全信任那种意见 —— 毕竟，你不能解雇或降职一个网站。

建立联系是需要日常观察生活的，但在技术上并非AI无法做到。Xerox PARC的WIMP视觉界面就是因为设计者脑海中产生了桌面隐喻而诞生的。目前，LLMs主要是响应性的 —— 它们不会突然在浴缸里有所启发。

我对那些认为通用人工智能（AGI）和灾难就在眼前的人有点同情，仅仅因为LLMs的强大给人们带来了惊喜。但实际上，对此几乎没有证据。模式识别对我们来说非常重要，因为这是我们在世界中导航的方式。但硅中的语言理解对我们来说只是一种工具。正如Michael Wooldridge教授所说：“[从任何有意义的角度来看，它并不意识到世界。](https://www.bbc.co.uk/programmes/articles/47L8KPzcQrh24xNZZJ4rdLM/artificial-intelligence-no-longer-a-thing-of-science-fiction)”

我将在我的下一篇文章中写一下我们可能在明年看到的趋势。
