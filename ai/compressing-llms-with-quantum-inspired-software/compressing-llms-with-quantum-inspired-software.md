
<!--
title: 基于量子启发的软件压缩大语言模型
cover: https://cdn.thenewstack.io/media/2024/12/a412e797-enrique-laszos-olmos-cropped.png
-->

大语言模型效率低下。总部位于西班牙的Multiverse Computing公司已经开发出使用量子启发式软件压缩LLM的方法。

> 译自 [Compressing LLMs With Quantum-Inspired Software](https://thenewstack.io/compressing-llms-with-quantum-inspired-software/)，作者 Alex Williams。

大语言模型效率低下，这一点毋庸置疑。本周在[AWS re:Invent](https://reinvent.awsevents.com/)上这一点很明显。[推理](https://thenewstack.io/5-open-llm-inference-platforms-for-your-next-ai-application/)是一个热门话题，讨论的重点是如何充分利用大语言模型，同时考虑到训练成本和所需的能源消耗。

[Multiverse Computing](https://multiversecomputing.com/)是一家参与[AWS生成式AI加速器](https://aws.amazon.com/startups/accelerators/generative-ai?lang=en-US)的企业，该公司已经开发出使用量子启发式软件压缩大语言模型的方法。该公司总部位于西班牙圣塞巴斯蒂安，其创始人兼首席执行官在[AWS](https://aws.amazon.com/?utm_content=inline+mention) re:Invent之前接受采访时表示，该公司利用量子启发式张量网络加速计算。

张量网络是强大的数学结构，它使用“试图利用经典计算机模拟量子计算机行为的方法，从而使经典机器运行能够从量子力学定律中受益的算法，这些算法也使真正的量子计算机受益”，[根据一篇关于](https://thenewstack.io/quantum-algorithms-vs-quantum-inspired-algorithms/)量子启发式计算及其与[量子计算](https://thenewstack.io/machine-learnings-next-frontier-quantum-computing/)比较的文章]所述。

[考虑一下训练模型和执行推理所需的成本和能源](https://medium.com/@gmicloud/inference-innovation-how-the-ai-industry-is-reducing-inference-costs-889b79275a8c)。Multiverse使用该公司已发表的研究表明，其技术可将LlaMA-2-7B的内存大小减少93%；它还将参数数量减少70%，将模型的训练速度提高50%，推理速度提高25%。此外，准确率下降幅度为2%到3%。

Lizaso表示，Multiverse与许多已经尝试过大语言模型但发现部署成本高昂的公司合作。问题是：大语言模型需要更高效。它们的规模以参数增长，但准确性仅线性提高。随着计算量的增加，成本也会增加。购买GPU成本高昂，从云服务提供商处购买GPU的成本同样高昂，甚至更高。

Lizaso表示，Multiverse开始与德国工程和技术公司[博世](https://www.bosch.com/)合作，该公司希望获得帮助，在其内部部署AI系统以减少缺陷。

“因此，我们应用了我们的张量网络，”Lizaso说。“我们为[机器学习](https://thenewstack.io/the-ultimate-guide-to-machine-learning-frameworks/)开发了一套全新的算法。效果非常好。因此，我们将这些相同的系统应用于金融和国防等领域。但在2023年某个时候，我们问自己，我们能否只准备一个更好的系统，一个压缩的大语言模型系统？”

## 压缩的未来是什么？

当我们进入量子计算时代时，压缩速度将加快，因此几乎所有事物都将具有一定的嵌入式智能，这是因为量子计算能够分析远远超出经典计算方法所能处理的大量数据。它不像经典计算机那样工作，它不会以1和0的二进制方式处理信息，而是使用一种称为叠加的量子力学特性，[在《The New Stack》之前的文章中](https://thenewstack.io/robots-learn-faster-with-quantum-technology/)，[Kimberly Mok]解释道。

这有点令人难以置信，但本质上，信息同时被处理为1或0，或两者兼而有之。

我们还没有完全进入量子领域。朝着可信赖的量子计算发展的进程是用[量子比特](https://thenewstack.io/quantum-algorithms-vs-quantum-inspired-algorithms/)来衡量的。要实现实用性，量子比特的数量需要达到一百万个甚至更多。当我们都达到那一点时，还有很长的路要走；顺便说一句，我们将看到前所未有的压缩水平。

Lizaso将果蝇的大脑与大语言模型的大小进行了比较。根据最近发表在[《自然》](https://www.nature.com/articles/d41586-024-03029-6)杂志上的一篇文章，果蝇有14万个神经元和5500万个突触，即细胞之间的神经元或连接，该文章发表了一篇关于果蝇大脑图的文章。
一只果蝇拥有智慧。它可以行走、飞行、交配、搏斗。它是自主的。它不需要网络连接。与任何生物相比，大语言模型 (LLM) 并没有做太多事情。但创造需要什么？[前所未有的电力，数十亿美元的训练成本](https://thenewstack.io/meeting-the-operational-challenges-of-training-llms/)。它能做什么？

但如果果蝇的智慧可以嵌入机器人呢？这将开启一种全新的思考方式，让我们看看今天的LLM在我们可以压缩足够的数据来赋予机器人飞行能力时将显得多么原始。这意味着，将来，联网和非联网设备都将在量子计算的帮助下拥有超级智能。果蝇拥有自然赋予的优势。但我们的努力是不可持续的。我们永远无法使用经典计算来获得感知生物的能力。这意味着我们现在能做的事情是不可持续的。

Multiverse公司销售两款产品：CompactifAI 和 Singularity。两者都提供使LLM更高效的功能。该公司支持多种模型，包括[Mistral](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/)、Bert 和 Zephyr。需要访问模型本身才能对其进行压缩。据Multiverse公司称，[OpenAI](https://openai.com/) 提供了一个访问（查询）模型的 API，“因此 Multiverse Computing 的产品无法对其进行压缩。”

权衡？有一些。你需要大量的专业知识，并且可能需要重新训练。准确性仍然是一个问号，但量子启发的计算可能是我们需要解决的一个问题的答案。我们所能为不断增大的LLM提供的电力是有限的。
