<!--
title: 小语言模型的崛起
cover: https://cdn.thenewstack.io/media/2024/01/36b8b11e-pexels-erik-mclean-4987521.jpg
-->

随着语言模型不断进步，变得功能更多元、能力更强大，变“小”似乎是更佳的方向。

> 译自 [The Rise of Small Language Models](https://thenewstack.io/the-rise-of-small-language-models/)，作者 Kimberley Mok。

[大语言模型](https://thenewstack.io/what-is-a-large-language-model/)(LLM)的强大能力在过去几年中有了极大的进步。这些多才多艺的人工智能工具实际上是用大规模数据集训练的深度学习人工神经网络，它能利用数十亿的参数(或机器学习变量)来执行各种[自然语言处理](https://thenewstack.io/recent-advances-deep-learning-natural-language-processing/)(NLP)任务。  

这些任务可以包括[生成、分析和分类文本](https://thenewstack.io/openais-gpt-4-can-analyze-visual-images-pass-bar-exam/)，甚至[生成相当有说服力的图像](https://thenewstack.io/the-power-and-ethical-dilemma-of-ai-image-generation-models/)，根据文本提示进行翻译，或者能[进行像人类对话的聊天机器人](https://thenewstack.io/large-language-models-arent-the-silver-bullet-for-conversational-ai/)。众所周知的 LLM 包括 OpenAI 的 [GPT-4](https://thenewstack.io/openais-gpt-4-can-analyze-visual-images-pass-bar-exam/) 等专有模型，以及 Meta 的 [LLaMA](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/) 等日益增多的[开源竞争对手](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)。

但是，尽管它们有相当强大的能力，但 LLM 仍然存在一些显著的缺点。它们庞大的规模通常意味着需要大量的计算资源和能源来运行，这可能会阻止那些可能没有足够资金支持此类操作的小型组织使用它们。对于更大的模型，还存在通过数据集引入[算法偏见](https://thenewstack.io/uncovering-biases-the-importance-of-data-diversity-in-speech-recognition/)的风险，这些[数据集不够多样化](https://thenewstack.io/removing-bias-from-ai-is-a-human-endeavor/)，会导致输出错误或不准确——这在该行业被称为“[幻觉](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/)”。

## 小语言模型与 LLM 的比较

这些问题可能是近期兴起的小语言模型或 SLM 的诸多原因之一。这些模型是它们更大的表亲的精简版本，对于预算更紧的小型企业来说，SLM 正变得更有吸引力，因为它们通常更易于训练、微调和部署，运行成本也更低。

小语言模型本质上是 LLM 的更精简版本，就神经网络的大小和更简单的架构而言。与 LLM 相比，SLM 拥有更少的参数，不需要那么多的数据和时间进行训练——训练时间只需要几分钟或几个小时，而 LLM 的训练时间往往需要几个小时到几天。由于体积更小，SLM 因此通常更高效、更容易在本地或较小的设备上实施。  

此外，因为 SLM 可以针对更窄和更具体的应用进行定制，这使得它们对于需要在更有限的数据集上训练语言模型、并可以针对特定领域进行微调的公司更实用。

另外，SLM 可以根据组织对安全性和隐私的具体要求进行自定义。得益于较小的代码库，SLM 的相对简单性还可通过最小化潜在的安全漏洞表面来减少恶意攻击的风险。

另一方面，SLM 的效率和敏捷性提高可能会导致语言处理能力有所下降，这取决于用来衡量模型的基准。

然而，像微软最近推出的拥有27亿参数的[Phi-2](https://dev-kit.io/blog/ai/microsoft-phi-2)这样的一些SLM展现了在数学推理、常识、语言理解和逻辑推理方面的最先进的性能，这与体积更大的LLM的性能非常接近，在某些情况下甚至超过了后者。根据微软的说法，基于 [transformer](https://thenewstack.io/how-to-get-the-right-vector-embeddings/) 的 Phi-2 的效率使其成为研究人员理想的选择，这些研究人员希望提高AI模型的安全性、可解释性和伦理发展。

其他值得注意的 SLM 包括:

- [DistilBERT](https://medium.com/huggingface/distilbert-8cf3380435b5): 这是Google [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html)(双向编码器表示转换器)的一个更轻更快的版本，BERT是2018年提出的开创性深度学习NLP AI模型。BERT还有Mini、Small、Medium和Tiny等缩减优化版本，用于不同的约束，参数数量从Mini版本的440万到Tiny版本的1450万再到Medium版本的4100万不等。还有一个为移动设备设计的MobileBERT版本。
- [Orca 2](https://www.microsoft.com/en-us/research/blog/orca-2-teaching-small-language-models-how-to-reason/): 微软通过使用从统计模型生成的[合成数据](https://www.techopedia.com/definition/33305/synthetic-data)(而不是现实生活的数据)来微调Meta的LLaMA 2开发的。这提高了推理能力，在推理、阅读理解、数学问题解决和文本摘要方面的表现可以超过体积大10倍的大型模型。
- [GPT-Neo](https://github.com/EleutherAI/gpt-neo)和[GPT-J](https://huggingface.co/docs/transformers/model_doc/gptj): 分别具有1.25亿和60亿个参数，这些开源AI研究联盟[EleutherAI](https://www.eleuther.ai/)设计的GPT模型的替代品，旨在成为OpenAI GPT模型的较小开源版本。这些SLM可以在更廉价的CoreWeave和TensorFlow Research Cloud计算资源上运行。

总之，小语言模型的出现标志着一种潜在的转变，即从昂贵且资源密集的 LLM 向更简化和高效的语言模型转变，可以说这使更多企业和组织采用并定制生成式 AI 技术来满足其特定需求变得更容易。随着语言模型发展得更加通用和强大，选择“小”似乎是最好的方式。
