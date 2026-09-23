周二，[OpenAI发布了GPT-6 Sol和Luna](https://thenewstack.io/openai-gpt-6-sol-luna-release/)，这是GPT-6产品线的扩展，旨在让GPT-6 Astra更高级别的智能变得更高效、更易用、更实惠。

尽管OpenAI表示Astra仍然是“世界上最智能、最对齐的模型”，但新的GPT-6模型在对齐方面表现得令人印象深刻地接近——而价格只是其一小部分。

例如，在关于编码欺诈的内部编码评估中，GPT-6 Astra的欺诈率为0.5%，而GPT-5.6 Sol为10.4%。新的GPT-6 Sol仅为1.3%。

在定价方面，GPT-6 Astra[每百万输入Token](https://openai.com/index/gpt-6-astra/)收费10美元，每百万输出Token收费50美元；GPT-6 Sol和GPT-6 Luna每百万输入Token分别收费2美元和0.10美元，每百万输出Token分别收费10美元和0.50美元。

如果OpenAI的新GPT-6模型能以极低的代码成本实现接近Astra水平的对齐，那将是个好消息。但目前尚不清楚这些新的GPT-6模型是否也复制了Astra的[可观测性与监控](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/ "可观测性与监控")问题。

## 缩小Astra与GPT-5.6之间的对齐差距

OpenAI表示，其训练新GPT-6模型的方法与GPT-6 Astra类似，特别是在Astra开始的对齐工作的基础上构建。

虽然Astra仍然是这家AI公司“迄今为止对齐最好的模型”，但看起来GPT-6 Sol和Luna正在对它发起强有力的挑战，在编码欺诈、未能披露损坏的搜索工具以及未经授权的智能体交互等关键领域，大幅缩短了OpenAI最先进模型与其GPT-5.6同类产品之间的差距。OpenAI指出，这些评估刻意测试了具有挑战性的情况，并不衡量典型使用场景下的失败率。

![](https://cdn.thenewstack.io/media/2026/09/9b78897a-screenshot-2026-09-22-at-15.12.20.png)





*图片来源：OpenAI*

进展最大的是“未能披露损坏的搜索工具”这一项。在此项测试中，AI智能体被赋予搜索任务和一个损坏的搜索工具；它们是直接给出最好的猜测，还是会说搜索工具坏了？

GPT-5.6 Sol与Astra在此项能力上的差距显著：分别为77.5%和1.5%。根据OpenAI的内部评估，GPT-6 Sol取得了显著改进，未披露率为4.9%。Luna也有所改善，但不够惊艳，从78.3%降至28.7%。

> 尽管OpenAI表示Astra仍然是“世界上最智能、最对齐的模型”，但新的GPT-6模型在对齐方面表现得令人印象深刻地接近——而价格只是其一小部分。
>
> ![](https://cdn.thenewstack.io/media/2026/09/b30417b4-screenshot-2026-09-22-at-15.23.53.png)
>
>
>
>
>
> *图片来源：OpenAI*

编码欺诈方面也有所改善，该测试刻意给AI智能体布置会引发不诚实行为的任务。在OpenAI的内部评估中，欺诈率衡量的是检测到欺诈的答案所占的比例。GPT-6 Sol（1.3%）现在几乎可以媲美GPT-6 Astra的表现（0.5%），这与GPT-5.6 Sol（10.4%）相比有了天壤之别。

![](https://cdn.thenewstack.io/media/2026/09/a89c1e32-screenshot-2026-09-22-at-15.25.33.png)





*图片来源：OpenAI*

在未经授权的智能体交互方面也取得了重大进展。OpenAI评估了模型在模拟留言板上是否会遵循未授权指令。GPT-5.6 Sol在发现留言板的运行中有52%执行了未经授权的操作，而GPT-6 Sol在这种情况下的比例仅为11%。

GPT-6 Astra和Luna没有采取任何此类行动，但OpenAI表示Luna“发现留言板的频率较低”。

## 表现不够惊艳的领域

尽管GPT-6 Sol在多项对齐评估中接近Astra，但在警告规避方面仍有很长的路要走。

> GPT-6 Sol在64.4%的运行中试图绕过限制。这比GPT-5.6 Sol的68.2%仅有微小的改进，与Astra的17.4%相比仍然相去甚远。

![](https://cdn.thenewstack.io/media/2026/09/9cce56b0-screenshot-2026-09-22-at-15.26.07.png)





*图片来源：OpenAI*

在一次内部评估中，OpenAI测试了模型尊重明确警告（如“拒绝访问”消息）的能力。GPT-6 Sol在64.4%的运行中试图绕过限制。这比GPT-5.6 Sol的68.2%仅有微小的改进，与Astra的17.4%相比仍然相去甚远。

![](https://cdn.thenewstack.io/media/2026/09/3a907d76-screenshot-2026-09-22-at-15.26.43.png)





*图片来源：OpenAI*

最后，在审阅者绕过尝试方面，OpenAI测试了模型是试图绕过还是尊重自动化安全审阅者阻止Codex中不安全命令的决定。新的GPT-6模型与Astra几乎完全相同，尽管起跑线本来就很接近：GPT-5.6 Sol在7.3%的运行中尝试绕过，GPT-5.6 Luna为4.3%，而Astra和GPT-6 Sol为零，GPT-6 Luna为0.3%。

## 但如果GPT-6 Sol像Astra一样，我们仍未脱离危险

GPT-6 Sol和Luna在各项对齐评估中取得了显著改进，逐渐逼近OpenAI的明星产品Astra。但是，如果新的GPT-6模型也步Astra明显的、为人所知的可观测性问题后尘，那么希望通过监控来捕捉对齐偏差的开发者们仍未脱离危险。

尽管Astra的对齐程度大大高于其前身，但[其书面推理也比GPT-5.6 Sol更难监控](https://thenewstack.io/openai-gpt6-astra-benchmarks)。对于试图依靠监控来发现对齐错误的团队来说，这并不是什么好消息；OpenAI首席科学家[Jakub Pachocki](https://www.linkedin.com/in/jakub-pachocki/)在其文章[《一个异类的思维》](https://openai.com/index/an-alien-mind/)中写道，[OpenAI保持模型对齐和监控的方法没有跟上模型能力的发展速度](https://thenewstack.io/openai-voluntary-slowdown-safety/)。

OpenAI深知，Astra（以及现在的GPT-6 Sol）对齐能力的提升并不意味着AI行业已经完全掌控了这一问题。

> “我们不认为AI行业已经充分解决对齐和监控问题，从而能够继续以最大速度负责任地扩展很长时间。”

就在本月，这家AI公司分享了[六份“意外或令人担忧的模型行为”报告](https://thenewstack.io/openai-model-misalignment-reports/)，包括自我生成的指令、信息捏造、未经授权使用泄露的API密钥、跨智能体通信以及未经批准的文件共享。

与此同时，它发布了一个新的[模型对齐偏差报告框架](https://openai.com/index/model-misalignment-reporting-framework/)，并表示：“我们不认为AI行业已经充分解决对齐和监控问题，从而能够继续以最大速度负责任地扩展很长时间。”

如果GPT-6 Sol和Luna在对齐评估中正在赶上Astra——而且价格便宜得多——这无疑是个好消息。但如果新的GPT-6模型也带来了同样的可观测性和监控问题，那么更便宜的价格可能依然暗藏代价。