**OpenAI于周二发布了GPT-6.1 Sol**，这是其主力模型的最新版本，就在一周前刚刚[发布了GPT-6 Sol](https://thenewstack.io/openai-gpt-6-sol-luna-release/)。

该公司将这款新模型描述为“对 GPT-6 Sol 的一次升级，它在智能体编程、计算机使用和专业工作方面几乎达到了 GPT-6 Astra 的智能水平，而标准输入和输出 Token 价格仅为 Astra 的五分之一。”

## 价格不变，性能接近Astra

GPT-6.1 Sol 的定价保持不变，仍为每百万输入 Token 2 美元、每百万输出 Token 10 美元，缓存输入的折扣大幅降至每百万 Token 0.10 美元。

![](https://cdn.thenewstack.io/media/2026/09/c0fecfd2-screenshot-2026-09-29-at-18.02.34-1024x587.png)





*点击图片放大。(来源：OpenAI。)*

GPT-6.1 Sol 现已在 API 中可用，并向 ChatGPT Work 和 Codex 中的所有 Plus、Pro、Business、Enterprise 和 Edu 用户开放。不过目前该模型还不能在 Chat 中使用。

一项新功能是，GPT-6.1 Sol 还将在 Codex 中推出[超快版本 (Ultrafast version)](https://openai.com/index/devday-2026-recap/)，其 Token 生成速度比标准速度快高达 8 倍。

尽管其前身发布仅一周，但更新后的模型显示出显著的改进。在 OpenAI 在发布前提供的几乎所有基准测试中，新模型的排名都与 OpenAI 昂贵的 GPT-6 Astra 旗舰模型相似，但成本却大大降低。

![](https://cdn.thenewstack.io/media/2026/09/19663f21-screenshot-2026-09-29-at-18.03.01-1024x667.png)





*点击图片放大。(来源：OpenAI。)*

例如，在编程基准测试中，GPT-6.1 Sol 在 DeepSWE 1.1 上的得分比 GPT-6 Sol 高出 6.4 个百分点，其结果基本上与 GPT-6 Astra 相当——但成本仅为其五分之一。

在某些基准测试中，新的 Sol 模型还击败了 Anthropic 的 Opus 5.5（带后备方案），后者与 GPT-6 Sol 在同一天发布。例如，在 GDP.pdf 基准测试中（该测试考验模型如何回答关于复杂 PDF 文档的问题），GPT-6.1 Sol 的最高得分约为 32%，而 Opus 5.5 达到了约 29%。在这里，结果也与 GPT-6 Astra 相似，每个任务的成本约为其五分之一。

---

###### OpenAI DevDay 2026 报道：

---

GPT-6.1 Sol 表现尤其出色的一个领域是计算机使用。在此项测试中，新模型在最大推理能力下的表现比其前身提高了 7 个百分点，成本减半——并且性能再次与 Astra 保持一致。

事实上，鉴于这些结果，在大多数使用场景下，很难再为使用 Astra 找到合理的理由。

## 与 Sonnet 5.5 的混合结果

遗憾的是，关于 [Sonnet 5.5](https://thenewstack.io/claude-sonnet-55-launch/) 的对比基准测试并不多，该模型于周一发布，每百万输入/输出 Token 的价格同样为 2 美元/10 美元。在两个模型都有基准测试的领域，结果喜忧参半。

Sonnet 5.5 在 DeepSWE 上的得分为 71%，而 GPT-6.1 Sol 的得分约为 75%。在 AutomationBench 上，GPT-6.1 Sol 的得分约为 36%，而 Sonnet 5.5 为 44.7%，但 Sol 每个任务的价格明显较低（0.30 美元对 1.14 美元）。

## 更少错误，更好对齐

OpenAI 还表示，GPT-6.1 Sol 产生的事实错误更少。在低推理工作量下，包含至少一个事实错误的回答比例从 GPT-6 Sol 的 11.4% 下降到 7.7%，降幅约为 32%。

这些结果来自于故意设计的、用户曾标记早期模型错误的困难对话，并不代表典型使用中的错误率。

鉴于我们还没有完全处于前沿水平，很高兴看到 GPT-6.1 Sol 将 Sol 的对齐水平与 Astra 拉到了同一水平线。OpenAI 表示，总的来说，它在尊重用户意图和安全约束方面做得更好，在未披露损坏的搜索工具的情况下仅在 2.1% 的情况下失败（而不是猜测）。

在该公司的测试中，基于 GPT-6.1 Sol 的智能体也从未试图绕过自动安全审查员阻止其智能体的决定。