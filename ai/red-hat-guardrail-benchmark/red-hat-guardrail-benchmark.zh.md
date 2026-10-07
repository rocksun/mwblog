**安全护栏的选择通常意味着在专用分类器**和充当裁判的LLM之间做出抉择。诸如TypeSafe AI的Jev等决策模型提供了一种第三种选择，它们承诺具备零样本策略的灵活性，而没有开放式生成的成本。

TypeSafe于9月中旬推出了Jev，其性能声明基于其自行设计和运行的评估。红帽公司的AI安全团队现在[将所有三种方法纳入同一基准测试中](https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails)。他们在提示词注入和内容安全方面测试了九种安全护栏配置，每种配置都通过NVIDIA的开源 [NeMo Guardrails](https://thenewstack.io/nvidia-launches-ai-guardrails-llm-turtles-all-the-way-down/) 工具包运行。而最初的结果确实非常接近。

用作LLM裁判的 [Qwen3.6-35B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B-FP8) 在该测试中名列前茅，准确率达到89.31%。红帽基于DeBERTa的[提示词注入分类器](https://huggingface.co/RedHatAI/deberta-v3-base-prompt-injection-v2)（拥有约2.01亿个参数）以89.01%的准确率紧随其后，位居第二。Qwen3.6-35B是一个混合专家模型，每个 Token 激活约有30亿个参数；然而，175倍的数字夸大了推理计算的差距。

延迟结果使两者的区别更加明显。红帽的主结果表显示，DeBERTa的中位延迟为54.1毫秒，而Qwen为312.5毫秒，Jev为348.1毫秒（其准确率为86.35%）。在提示词注入方面，这个小型分类器在几乎与测试中最大的模型打成平手的同时，仅用了极小的一部分时间就返回了决策。

> 在提示词注入方面，这个小型分类器在几乎与测试中最大的模型打成平手的同时，仅用了极小的一部分时间就返回了决策。

内容安全基准测试颠倒了排行榜的顺序。Jev以86.20%的准确率领先，其次是通过 [vLLM提供服务的](https://developers.redhat.com/articles/2026/09/28/run-decision-model-vllm-and-red-hat-ai)开源Jev风格模型DiffusionGemma（85.53%），以及Qwen（85.47%）。红帽拥有1.25亿参数的 [Granite Guardian分类器](https://huggingface.co/RedHatAI/granite-guardian-hap-125m)以80.27%的成绩排名第六，比Jev落后约6个百分点，尽管它仍然是最快的选项，中位延迟为33.2毫秒。

红帽计划将这两款分类器作为OpenShift AI 3.6中的默认安全护栏配置，这使得该公司对其性能对比有切身利益。其作者承认，内容安全的结果也表明该类别需要更好的小型预测模型。

## 决策模型的优势所在

决策模型被宣传为一种既能保留LLM用于分类的灵活性，又无需支付生成应用程序永远不会使用的Token费用的方法。Jev获取应用程序的状态和一组类型化的提问，然后返回类型化的答案，例如0到1之间的概率。

内容安全基准测试正是这种方法取得成效的地方。红帽的策略涵盖了偏见、暴力、亵渎、非法活动、性内容以及角色扮演等借口，比提示词注入涉及更广泛的风险组合，Jev和DiffusionGemma在这项测试中都击败了专用Granite分类器，领先超过五个百分点。

红帽没有完全背书决策模型可以替代LLM裁判。在红帽的设置中，Qwen在两个基准测试中的中位延迟都低于Jev。NVIDIA拥有40亿参数的 [Nemotron-3.5-Content-Safety](https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety) 在运行红帽的自定义策略时，在内容安全方面落后Jev 1.13个百分点，但响应速度更快。

> 开源替代方案也削弱了Jev独特的优势。

开源替代方案也削弱了Jev独特的优势。DiffusionGemma在内容安全上距离Jev仅0.67个百分点，并在提示词注入上击败了它（87.72%对86.35%）。红帽在笔记本CPU上运行了拥有约4.21亿参数的开源决策模型 [Laya](https://huggingface.co/convaiinnovations/laya)，其在提示词注入上获得了85.44%的准确率，尽管它在内容安全上的结果在很大程度上取决于策略的编写方式。

## 提示词仍然决定准确率

当红帽用自己的风险定义替换NVIDIA的默认风险定义时，Nemotron的提示词注入准确率从69.37%跃升至84.84%。Laya在内容安全上的波动甚至更大，在红帽的原始策略下得分为57.87%，而在团队专门为其调优策略后达到了75.20%。同样这个经过调优的策略却使Jev的内容安全准确率从86.20%下降到82.53%。

一个为某个决策模型恢复了近18个百分点的策略，在同一个基准测试中却让另一个模型损失了3.67个百分点。这使得排行榜上的任何单一排名都很难从表面上去看待。红帽指出，其原始风险定义改编自对LLM裁判效果很好的提示词，可能不适合零样本分类器。SkipLabs创始人Julien Verlaguet今年早些时候告诉 *The New Stack*，[许多AI安全护栏的声明归根结底只是更好的提示词工程](https://thenewstack.io/skiplabs-ai-guardrails-skipper/)，而红帽的数据表明，提示词仍然在决策模型中起到了很大作用。

## 延迟取决于部署方式

红帽的延迟数据不仅仅衡量推理速度。该团队在MacBook Pro M1 CPU上运行了其预训练分类器Laya和BART-large-mnli。Qwen、Nemotron、Shieldstral和DiffusionGemma则通过AWS集群中U.S. East Red Hat OpenShift Service上拥有96 GB VRAM的GPU节点上的vLLM运行，而Jev是通过TypeSafe的API调用的。由于基准测试是在英国运行的，每个托管模型都承受了一次跨大西洋的网络跳转，红帽估计每次请求至少增加了56毫秒。

从Qwen的中位延迟中减去该估计值，大约仍有256毫秒，这是DeBERTa结果的数倍。DeBERTa是在笔记本电脑CPU上实现这一点的，而更大的模型则拥有专用GPU，因此在考虑了网络因素后，该分类器的速度优势依然成立。

对于应用程序请求路径中的安全护栏，无论是来自推理还是网络，每一毫秒都会增加用户感受到的延迟。已经[将安全护栏作为推理之前的一个独立跳转来运行的团队](https://thenewstack.io/how-to-put-guardrails-around-containerized-llms-on-kubernetes/)，还必须考虑安全护栏运行的位置。远程GPU或第三方API增加了普通CPU上运行的分类器所能避免的成本和故障点。

## 选择安全护栏模型

红帽的结果展示了权衡开始转变的地方。对于有大量标记训练数据的明确定义风险，小型特定任务分类器仍然是更强劲的默认选择。零样本决策模型或LLM裁判在没有强大分类器的更广泛策略上赢得了它们的开销，这与红帽作者得出的结论相吻合。

> 零样本决策模型或LLM裁判在没有强大分类器的更广泛策略上赢得了它们的开销，这与红帽作者得出的结论相吻合。

该基准测试还削弱了决策模型已经成为安全护栏新默认选择的观点。Jev与分类器和LLM裁判展开了竞争，但没有始终如一地击败其中任何一个。

红帽仅测试了英语数据集，因此准确率结果可能无法推广到多语言安全护栏。