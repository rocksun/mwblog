# 你可能错过了：DeepSeek 的开源成功故事

![Featued image for: ICYMI: DeepSeek Is an Open Source Success Story](https://cdn.thenewstack.io/media/2025/01/31d13318-deepseek-1024x768.png)

英伟达股东今天口袋里少了约[4000亿美元](https://x.com/brewmarkets/status/1883887544200499259)，这要归功于一家名为[DeepSeek](https://www.deepseek.com/)的中国人工智能初创公司的开源努力。OpenAI以及其他商业AI模型提供商可能不得不重新考虑他们的商业模式。

而美国[为保持其在人工智能领域的竞争优势所需的5000亿美元数据中心](https://thenewstack.io/ai-power-needs-may-strain-us-grid-as-stargate-project-grows/)？最终可能不再需要了。

上周末引发热议的是[DeepSeek的R1推理模型](https://api-docs.deepseek.com/news/news250120)的发布，该模型显示出与OpenAI的最新版本[O1](https://openai.com/o1/)相当的结果，但训练成本仅为[1/50](https://x.com/_KarenHao/status/1883877988682649931)。

同样重要的是，DeepSeek以完全开源的方式发布，采用[非常宽松的MIT许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)，因此任何其他公司都可以复制该模型。

如果DeepSeek的承诺得到验证，其含义是公司将不再依赖[OpenAI](https://thenewstack.io/open-source-may-yet-eat-googles-and-openais-ai-lunch/)和其他数十亿美元的商业服务来构建他们自己的生成式AI应用程序。

Anthropic AI工程师[观察到](https://stratechery.com/2025/deepseek-faq/)，“DeepSeek为几乎每个人都提供了一份巨大的礼物。”“最大的赢家是消费者和企业，他们可以期待未来有效免费的AI产品和服务。”


## 危中寻机

DeepSeek提出这种新的架构主要是由于一些限制，即美国对[Nvidia H100](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/)（最新的Nvidia GPU）的出口限制。

出于维护人工智能优势的担忧，美国禁止向中国出售英伟达的H100芯片。作为回应，英伟达推出了简化版的H800，DeepSeek的工程师围绕它优化了他们的LLM。

一些巧妙的工程设计表明，训练领先的模型并不一定需要更多的芯片间内存带宽。

Thompson写道：“DeepSeek在这个模型设计中做出的所有决定，只有在你受到H800的限制时才有意义。”“如果DeepSeek能够使用H100，他们可能会使用更大的训练集群，并且更少的优化专门针对克服带宽不足的问题。”

所以他们不得不使用速度较慢的H800，并进行大量的繁琐的AI工程工作，以使其LLM适应较小的平台。

事实上，结果如此之好，以至于引发了许多疑问：当DeepSeek能够以极低的成本做到这一点时，我们是否真的需要5000亿美元的数据中心基础设施或昂贵的英伟达芯片？

它展示了一种无需大型数据中心即可提供AI服务的方法。


## 开源的核心

如果您以前没有听说过DeepSeek，请不要担心。它是[许多在中国大型模型市场竞争的初创公司](https://x.com/RnaudBertrand/status/1883456746058129826)之一。

DeepSeek LLM[实际上是作为该公司的副项目开始的](https://x.com/0xmetaschool/status/1882721476723536178)，是利用其剩余GPU做的一些事情。

首席执行官已经将其开源并发表其工作的论文作为一项骄傲的事情。

DeepSeek首席执行官[告诉](https://www.chinatalk.media/p/deepseek-ceo-interview-with-chinas) [China Talk](https://www.chinatalk.media/p/deepseek-ceo-interview-with-chinas)：“开源、发表论文实际上不会花费我们任何成本。对于技术人才来说，让其他人追随你的创新会带来极大的成就感。事实上，开源更多的是一种文化行为，而不是商业行为。”

该公司并非为了赚钱而选择这条道路，而是为了获得认可，同样重要的是为了吸引更优秀的人才。以及为了公平竞争。

他说：“面对颠覆性技术，封闭源代码创建的护城河是暂时的。即使是OpenAI的封闭源代码方法也无法阻止其他人赶上。”


## 技术方面

为了降低计算成本，工程团队为人工智能领域采用了一些[创新实践](https://stratechery.com/2025/stratechery-updates-deepseek-r1-deepseek-implications/)。
DeepSeek成功的关键在于一种名为蒸馏的技术，简单来说，就是用另一个LLM进行训练。[Amanda Brock](https://www.linkedin.com/in/amandabrocktech/)（[OpenUK CEO](https://thenewstack.io/the-open-source-license-rug-pull-vent-get-your-fill-at-soo25/)）在即将发表在TNS的一篇文章中指出，DeepSeek的开源声明在此方面变得模糊不清。她担心DeepSeek使用的上游数据的合法性。

但模型本身远不如模型的构建方式重要。

另一种策略是回归到一种较旧的技术——[强化学习](https://thenewstack.io/reinforcement-learning-ready-real-world/)——来提高推理能力。传统模型使用带有人工反馈的强化学习来引导模型得出正确的答案。DeepSeek直接将强化学习构建到模型本身中。它可以计算出几种答案，然后使用自我引导推理选择看起来最正确的答案。

Thompson写道：“你不需要教AI如何推理，你只需要给它足够的计算能力和数据，它就会自己学习！”

R1建立在之前版本中大量工程工作的基础上，即DeepSeek的[V3](https://api-docs.deepseek.com/news/news1226)和[V2](https://api-docs.deepseek.com/news/news1210)模型。V2引入了“专家混合”（MOE）的概念，这意味着并非模型的每个部分都会针对每个问题启动，从而节省内存空间（OpenAI的ChatGPT 4.0也使用了MOE，尽管粒度不同）。

V3改进了MOE模型，并通过键值存储减少上下文窗口（用户提供的数据）的大小，进一步节省了内存。

Thompson写道：“V3的训练[令人震惊地便宜](https://arxiv.org/html/2412.19437v1)。DeepSeek声称模型训练耗费了[约270万]个H800 GPU小时，以每GPU小时2美元计算，总共仅需557.6万美元。”

这是500万美元，而不是OpenAI声称其训练尖端模型所需的1000亿美元。

DeepSeek的[API服务](https://api-docs.deepseek.com/guides/reasoning_model)的成本也反映了更高的效率，其百万个token的价格为2.19美元，而[OpenAI O1](https://openai.com/o1/)的百万个token价格为60美元。

您可以通过[应用下载](https://api-docs.deepseek.com/news/news250115)或[网页聊天界面](https://chat.deepseek.com/)测试DeepSeek。

## 价值损失
如果DeepSeek被证明像承诺的那样具有成本效益，其影响将是巨大的。

正如Thompson指出的那样，“OpenAI并没有什么无法复制的特殊秘方”。

Wenfeng认为，OpenAI、英伟达和甲骨文正在利用巨大的计算需求作为进入AI市场的壁垒，而一些优秀的开源技术则完全消除了这种壁垒。

等等。你的意思是说，我们不需要用数据中心和燃煤燃气发电厂覆盖地球，就能在未来挥舞一根神奇的AGI魔杖，让所有后果消失？

是的。这是一个错误的权衡。好好想想这句话。16/

— Karen Hao (@_KarenHao)

[2025年1月27日]
由于推理成本大幅降低，公司可以以之前成本的一小部分构建生成式AI应用。它们仍然会受益于快速的英伟达GPU，但它们并不一定需要充满这些GPU的数据中心。

Thompson指出，特别是GPU供应商英伟达之前高得惊人的股票估值受益于该公司被认为的锁定价值：专有的[CUDA编程模型](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/)以及将多个GPU连接到更大的系统中的能力。

Dropbox副总裁[Morgan Brown](https://www.linkedin.com/in/morganb/) [指出](https://x.com/morganb/status/1883686179276788197)：“对英伟达来说，这很可怕。他们的整个商业模式都是建立在销售利润率高达90%的超高价GPU的基础上的。如果每个人都能突然用普通的游戏GPU进行AI……好吧，你明白问题所在。”

同样，OpenAI现在完全是一家消费科技公司，面临着更大、更商品化的市场。根据[The Information](https://www.theinformation.com/articles/meta-scrambles-after-chinese-ai-equals-its-own-upending-silicon-valley)报道，Meta生成式AI的管理层正在担心在测试结果不如DeepSeek后[构建](https://x.com/a_boutorh/status/1882728052238827966)他们自己的LLama 4模型的[巨额成本](https://x.com/a_boutorh/status/1882728052238827966)。

微软CEO萨蒂亚·纳德拉[援引](https://x.com/satyanadella/status/1883753899255046301)了杰文斯悖论，其中，“随着AI变得更高效和更容易获得，我们将看到它的使用量激增，将其变成一种我们永远无法获得足够的商品。”
即使美国总统唐纳德·J·特朗普在最近的新闻发布会上也承认了开源的力量，即使他没有直接点名。“一家中国公司发布DeepSeek AI应该让我们各行各业警醒，”他说。

🚨特朗普：“一家中国公司发布DeepSeek AI应该让我们各行各业警醒，我们应该专注于竞争以赢得胜利。我们拥有世界上最优秀的科学家。这很不寻常。我们总是拥有这些想法。我们总是走在最前面。”

[https://pic.twitter.com/fFiRjxMTmZ](https://pic.twitter.com/fFiRjxMTmZ) — Autism Capital 🧩 (@AutismCapital) January 28, 2025

“Deepseek R1是我见过的最令人惊叹和印象深刻的突破之一——而且作为开源项目，它是送给世界的宝贵礼物，”Andreessen Horowitz联合创始人Marc Andreesen[评论道](https://x.com/pmarca/status/1882719769851474108)。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展日新月异，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。