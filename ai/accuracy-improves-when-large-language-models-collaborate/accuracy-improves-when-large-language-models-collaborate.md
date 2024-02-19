<!--
title: 大语言模型合作提高准确性
cover: https://cdn.thenewstack.io/media/2024/01/aa8b9285-christopher-paul-high-fwrmk19zavc-unsplash-1024x683.jpg
-->

麻省理工学院CSAIL的研究显示，让一组LLM系统共同合作能够产生更准确的答案。

> 译自 [Accuracy Improves When Large Language Models Collaborate](https://thenewstack.io/accuracy-improves-when-large-language-models-collaborate/)，作者 Kimberley Mok。

我们的文化常常推崇自力更生、坚韧不拔的个体，不轻易受他人意见左右，但实际上，我们知道团队合作和在一群人中建立共识同样对于启动项目至关重要。

毫不奇怪，这种基于团队的合作理念也同样适用于[大语言模型](https://thenewstack.io/what-is-a-large-language-model/)（LLMs），正如麻省理工学院[计算机科学与人工智能实验室](https://www.csail.mit.edu/node/2873)（CSAIL）最新的[研究](https://arxiv.org/pdf/2305.14325.pdf)所展示的那样。具体而言，该研究着眼于让一组这些强大的人工智能系统相互合作，采用一种“讨论与辩论”的方式，以达到最佳和最准确的答案。

像 OpenAI 的 [GPT-4](https://thenewstack.io/dev-news-gpt-4-turbo-chrome-talks-pretty-and-worlds-merge/) 和 Meta 的开源 [LLaMA 2](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) 等强大的大语言模型 AI 系统最近引起了很多关注，因为它们能够生成有说服力的类人文本响应，涉及历史、政治和[数学问题](https://thenewstack.io/googles-generative-ai-stack-an-in-depth-analysis/)，以及生成[可接受的代码](https://thenewstack.io/the-changing-role-of-human-developers-in-an-ai-and-llm-world/)、[营销文案](https://thenewstack.io/should-llms-write-marketing-copy/)和[诗歌](https://posts.decontextualize.com/language-models-poetry/)。

然而，这些 [AI 工具产生“幻觉”](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)或提出似是而非答案的倾向是有充分文献记录的；因此，LLMs 作为验证信息来源的可靠性可能会受到影响。

为了解决这个问题，麻省理工学院的团队声称，采用他们的合作方法将显著减少 LLMs 产生不准确信息的倾向，尤其是当与其他方法结合使用时，如[更好的提示设计](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/)、[验证](https://thenewstack.io/test-driven-development-with-llms-never-trust-always-verify/)和用于将一个较大的计算任务拆分成较小的中间步骤的[草稿板](https://medium.com/the-business-of-ai/cook-a-scrumptious-ai-solution-with-llm-scratchpads-8d34ebb8a913)。

## 多智能体辩论

团队的过程涉及向一个 AI 智能体提出数学、推理或国际象棋问题，然后评估和批判其他 AI 智能体对同一问题的回答。然后，该过程将重复进行多个回合，随后将集体反馈重新整合到原始 AI 智能体的回答中以进行更新。

团队解释道：“这个过程促使模型构建出既符合其内部批评者又在其他智能体的回应光线下合理的答案。”

“所得到的模型共识可以同时持有和维护多个推理链和可能的答案，然后提出最终答案。我们的研究结果表明，这种方法显著增强了数学和战略推理在许多任务中的表现。此外，我们的方法提高了生成内容的事实准确性，减少了当代模型容易出现的谬误答案和幻觉。”

![缩放](https://cdn.thenewstack.io/media/2024/01/501a2672-multiagent-debate-mit.jpg)

显示多智能体辩论过程如何帮助生成更准确的计算机科学家传记的图示（这里仅显示了生成的前三个项目符号）。

正如团队所指出的，这个过程类似于团体讨论可能展开的方式，个体在达成某种共识之前探讨问题或问题的各个方面。

理论上，即使并不能保证所有智能体最终会达成明确的一致意见，研究人员发现他们可以调整这种多智能体辩论方法的某些参数，以使及时达成共识和更好的结果变得更加可能。

团队指出：“我们发现可以通过改变语言模型相信自己输出的程度以及相信其他模型生成的输出的程度，通过不同的提示来控制辩论的持续时间。”“总的来说，我们发现鼓励模型基于自己的解决方案更‘固执’的提示导致了更长的辩论和更好的最终解决方案。总体而言，我们观察到语言模型智能体相对较‘随和’，这可能是由于[指令调整](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/)或[基于人类反馈的强化学习](https://huggingface.co/blog/rlhf)。”

此外，研究团队还建议，这种迭代过程的一个重要优势在于它可以无缝地融入所谓的“[黑盒](https://thenewstack.io/explainable-ai-looking-into-the-black-box/)”AI模型中，因为它不需要开发人员或其他专家来调整理解不足的模型的内部工作方式。这种方法将使LLMs的验证过程更加一致和更容易实现。

然而，研究人员承认处理更长的上下文和更复杂的团体讨论可能会带来额外的挑战，并且可能需要更多的计算资源。尽管如此，团队认为这些困难在未来可能会随着性能更好的模型而得到缓解，并且从长远来看，这可能会是 LLMs 的一个值得的权衡。

“这种方法不仅提供了提升现有语言模型性能的途径，而且还提供了一种自动自我改进的手段，”本文的主要作者杜一伦在一份[声明](https://news.mit.edu/2023/multi-ai-collaboration-helps-reasoning-factual-accuracy-language-models-0918)中说道。“通过利用辩论过程作为监督数据，语言模型可以自主增强其事实性和推理能力，减少对人类反馈的依赖，并提供一种可扩展的自我改进方法。随着研究人员继续完善和探索这种方法，我们可以更接近一个未来，语言模型不仅模仿人类语言，而且还表现出更系统化和可靠的思维，开创语言理解和应用的新时代。”
