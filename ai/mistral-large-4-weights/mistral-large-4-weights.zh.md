**Mistral周二推出了Large 4**，这是该公司自4月底发布Medium 3.5以来首个重大模型发布，也是该公司试图缩小与中国领先开源权重模型差距的最新尝试。

该公司表示，这款新模型在网络安全方面表现尤为出色，Mistral科学副总裁 [Pierre Stock](https://www.linkedin.com/in/pierrestock/) [对路透社表示](https://www.reuters.com/world/china/mistral-ceo-says-new-ai-model-beats-chinese-ones-some-areas-2026-10-06/)，在评估过程中，当模型试图突破其测试环境时，这些能力浮现了出来。他补充说，这种行为在预料之中，公司已经通过软件对其进行了控制。

这一插曲并未放慢Mistral的发布计划。Large 4在X和Reddit上被昵称为“Le Chonk”，呼应了6月在全网传播的关于虚构超大版Mistral模型的 [“Le Chaton Fat”梗](https://www.reddit.com/r/singularity/comments/1wz2r59/le_chaton_fat_is_real/)。目前它正通过Mistral的API进行公开预览，网络安全专家和政府机构正在测试一个安全限制较少的版本，权重将于10月27日发布。

OpenAI和Anthropic在测试其网络安全能力最强的模型时也遇到了类似的行为，并以限制访问作为回应。Mistral则采取了不同的路线，计划在三周后根据自定义许可证发布Large 4的检查点，而不是Large 3所使用的Apache 2.0许可证。一旦权重发布，开发者将能够控制模型的运行方式以及在其周围设置何种防护措施。

> Mistral采取了不同的路线，计划在三周后根据自定义许可证发布Large 4的检查点，而不是Large 3所使用的Apache 2.0许可证。

## 1万亿参数，490亿激活参数

Large 4拥有1万亿的总参数规模，采用了稀疏混合专家（MoE）架构，在推理时会激活49亿个参数，这比 [Large 3](https://mistral.ai/news/mistral-3/) 的675亿总参数和41亿激活参数有了显著提升。

该公司在欧洲数据中心的大约4,000个 Nvidia Grace Blackwell GPU上，从头开始花了大约两个月时间训练了Large 4。Mistral一直强调其相对较小的训练集群，尽管在披露的训练算力如此之少的情况下，很难与美国最大的实验室进行比较。

其稀疏架构通过仅激活模型1万亿参数中的49亿个来保持较低的推理算力，但提供完整的检查点仍需要大量的多GPU设置。

软件工程和网络安全是Large 4的主要目标，其其他应用场景还包括财务分析、卫星与航拍图像、技术图纸和芯片设计。它接受多模态输入，生成文本并支持160多种语言，包括欧盟的所有官方语言。

## 开放权重，无法召回

Mistral支持在网络安全领域开放权重的理由在于控制权。扫描代码或测试系统的安全团队可能会遇到托管模型的安全限制，而 [OpenAI的安全系统已经在任务中途切断API响应](https://thenewstack.io/openai-slowing-ai-development/)，尽管该公司赋予了模型在其自身开发工作流中更多的权限，包括 [在发现漏洞时阻止代码合并](https://thenewstack.io/openai-ai-code-review/)。

> Mistral支持在网络安全领域开放权重的理由在于控制权。

在他们自己的基础设施上运行Large 4可以让团队自己设定这些限制，并将敏感的代码和数据保留在内部。Stock向 [Journal du Net](https://www.journaldunet.com/intelligence-artificielle/1555845-mistral-large-4-la-recette-secrete-de-mistral-ai-pour-rattraper-les-geants/) 提出了另一个论点，指出一旦权重在互联网上被复制，访问权限就再也无法轻易撤销。

## DeepSWE评分需要上下文

Mistral报告在DeepSWE v1.1上的得分为62%，略高于其列出的GLM-5.3的61%。然而，[实时的DeepSWE排行榜](https://deepswe.datacurve.ai/) 显示，GLM-5.3和Kimi K3在其最佳发布配置下约为69%，而GPT-6 Astra、Gemini 3.8 Flash和Claude Opus 5则在74%左右。

其他方面的结果更强。Large 4在 [Harvey法律智能体基准测试](https://www.vals.ai/benchmarks/hlab) 上的任务通过率为15%，在 [Finch](https://aclanthology.org/2026.findings-acl.523/) 上的通过率为67%，在Mistral的测试中，它与DeepSeek V4 Pro 0813并列，领先于GLM-5.3的65%。这些配置的独立结果尚不可用。

就目前而言，这些数字让Large 4看起来很有竞争力，但并没有将其推至榜首。我们都急切地想看看月底当开发者能够在Mistral的API之外运行Le Chonk时，会有什么表现，以及这种性能在其自己的工作负载下能保留多少。

> Large 4在Harvey法律智能体基准测试上的任务通过率为15%，在Finch上的通过率为67%，在Mistral的测试中，它与DeepSeek V4 Pro 0813并列，领先于GLM-5.3的65%。