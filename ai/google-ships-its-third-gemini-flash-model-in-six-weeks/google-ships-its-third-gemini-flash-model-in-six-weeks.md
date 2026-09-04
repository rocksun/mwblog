<!--
title: Google在六周内发布了第三款Gemini Flash模型
cover: https://cdn.thenewstack.io/media/2026/09/f05d48f5-screenshot-2026-09-02-at-12.36.10-scaled.png
summary: Google近期发布了Gemini 3.8 Flash及Cyber版本，这是其六周内第三次更新Flash系列。该模型在代理式编程和复杂工程任务中表现优异，性价比极高。Cyber版本则通过Fairwind项目向特定合作伙伴开放，专注于自主漏洞检测与修复，旨在提升企业在AI时代的网络安全防御能力。此外，国产模型在部分基准测试中已展现出极强的竞争实力。
-->

Google近期发布了Gemini 3.8 Flash及Cyber版本，这是其六周内第三次更新Flash系列。该模型在代理式编程和复杂工程任务中表现优异，性价比极高。Cyber版本则通过Fairwind项目向特定合作伙伴开放，专注于自主漏洞检测与修复，旨在提升企业在AI时代的网络安全防御能力。此外，国产模型在部分基准测试中已展现出极强的竞争实力。

> 译自：[Google ships its third Gemini Flash model in six weeks](https://thenewstack.io/google-ships-its-third-gemini-flash-model-in-six-weeks/)
> 
> 作者：Frederic Lardinois

**Google虽然已经有一段时间没有发布Gemini Pro模型了**，但在周三，该公司[发布了](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)又一系列的Gemini Flash和Flash Cyber模型。

尽管Gemini 3.7 Flash发布才三周（这是Google六周内第三次发布Flash版本），但新的Flash模型在许多方面表现都大幅超越了前代，尤其是在代理式编程任务和代理式计算机使用方面。

和以前一样，Flash 3.8的定价为每百万输入/输出token $0.75/$3.75。不过这是入门价格，将于2026年12月31日失效，届时将调整为$1.50/$7.50。

## Fairwind限制了Flash 3.8 Cyber的访问

Flash 3.8看起来是一款非常出色的模型，Google将其称为“主力模型”是恰如其分的，但Flash 3.8 Cyber也值得一提。通过这款模型，Google实际上是在效仿Anthropic的策略。

Google将Cyber模型描述为“其最强大的网络安全模型，在漏洞检测和自动化补丁方面具有前沿水平的性能”。因此，它仅通过Google名为[Fairwind](https://deepmind.google/fairwind-program/)的新计划提供给少数“受信任的防御者”。

其中包括约650个受信任的合作伙伴，如Accenture、CrowdStrike、Center for Internet Security、Datadog、Palo Alto Networks、Snowflake和Wiz。

“防御者的优势在于缩短检测漏洞和修补漏洞之间的时间，”Google安全与隐私副总裁Four Flynn在[公告](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/)中写道。“通过Google的Fairwind计划，政府和企业合作伙伴可以获得自主工具，以更快的速度和规模修复系统，使其在应对‘氛围编程’驱动的威胁时保持领先。”

在Flash 3.5 Cyber时，Google曾推出过一个有限访问计划，但当时该计划没有名称，且显得有些随意。

## Gemini 3.8 Flash：长跨度编程与智能体

至于Flash 3.8，Google指出，在处理复杂的工程任务时，该模型通常优于OpenAI的GPT-5.6 Sol以及Anthropic的Claude Sonnet 5和Opus 5等模型。例如，在DeepSWE等基准测试中，它与Opus 5持平，并击败了GPT-5.6 Sol和Sonnet 5。

不过这里有一个警告，Google也强调“3.8 Flash工作起来更费力”。但工作更费力意味着它会消耗更多的token，Google对此表现得很坦诚，并指出：“在复杂的任务中，它表现得更加勤奋——执行额外的推理步骤，并反复调用工具。有时，模型可能会使用更多的token来最大限度地提高性能，特别是在高努力程度下。”

为了抵消这一点，开发者可以选择不同的推理模式，就像以前的模型一样。

![](https://cdn.thenewstack.io/media/2026/09/ce2cb6f2-hromzf5boaalg1y-836x1024.png)

来源：Google。

Google的基准测试不包括前一天才发布的[Anthropic’s Fable 5.1](https://thenewstack.io/anthropic-fable-5-1-launch/)。那是一个更强大的模型，但价格也贵得多。

没有人会称Fable 5.1为“主力模型”，但值得强调的是，在Terminal-Bench 4.0等通用代理基准测试中，Flash 3.8得分为19.1%，而Fable 5.1达到了55.8%，Opus 5达到了51.8%。同时，在专注于编程的Terminal-Bench 2.1上，Flash 3.8的表现优于其竞争对手。

不过，Terminal-Bench在这里是一个特例，因为Gemini模型在其他代理任务上的表现实际上相当不错，即使与其他旗舰模型相比也是如此。

尽管取得了一些令人印象深刻的进步，但Google的模型在计算机使用（OSWorld-2.0上为59%，而Opus 5为75.4%）以及测试模型知识工作任务的基准GDPVal方面仍然存在困难。在GDPVal中，Google的得分为1545，仍远落后于Opus 5的1824，但最终赶上了Sonnet 5的1584。

Google指出，它之所以能在如此短的时间内改进模型，部分原因在于它现在也使用代理循环来改进模型。“今天发布的两个版本都由相同的核心智能驱动，并由旨在递归评估和优化底层模型的长运行代理循环进一步加速，”团队写道。

## 中国模型正在缩小差距

值得注意的是，Google的比较主要集中在OpenAI和Anthropic上，但很难不注意到，在DeepSWE 1.1等一些基准测试中，像GLM-5.3和GLM-5.3 Flash，以及DeepSeek v4 Pro和Kimi K3等中国模型也处于同一水平——而且它们通常提供更好的性价比。

![](https://cdn.thenewstack.io/media/2026/09/8b98daca-gemini-3-8-flash__evals__deepswe.width-2000.format-webp-1024x576.webp)

来源：Google。

## 网络安全基准

至于Flash 3.8 Cyber，Google表示它在CyberGym上提供了“自主漏洞发现的前沿性能”，在那里它击败了7月发布的3.5 Flash Cyber以及“显著更大的前沿模型”。

CyberGym仅涵盖C和C++代码，因此Google还在涵盖20种语言的内部基准测试中测试了该模型，并报告那里的成功率超过70%。

在Collinear的CWE-Bench上，该模型的pass@1得分为47.2%，仅次于Google未透露姓名的“领先前沿模型（47.8%）”。

不过，基准测试的局限性很大。Chrome安全团队表示，该模型产生的正确补丁数量是“最好的商业模型（体积大得多）”的2.6倍，而Wiz报告称，在内部渗透测试基准测试中，其召回率提高了7.5%到9.7%，成本降低了2.3到5.2倍。

## 安全性

在安全方面，Google表示，根据其[前沿安全框架](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)，3.8 Flash在发布时“针对化学、生物、放射和核（CBRN）以及网络攻击领域的滥用提供了防护措施，同时实现了有益的用例”。

Gemini Flash 3.8 Cyber有一套更宽松的防护措施，但这也是它仅向一小部分用户开放的原因。

Google确实指出，新模型在提示词注入方面也更加稳健，例如在Gray Swan IPI基准测试中取得了（几乎）行业领先的结果。

![](https://cdn.thenewstack.io/media/2026/09/cce3a0e3-gemini-3.8-flash_evals_attack__l.width-2000.format-webp-1024x576.webp)

## Gemini Pro？

下一代Gemini Pro模型的发布将会很有趣。这些Flash模型正在迅速改进，虽然Google在Pro版本的发布上有些失误，但该模型或许值得等待。与此同时，Google押注Flash模型的策略也意味着它能够推动一种更具性价比的叙事，而这对美国其他前沿实验室来说更难做到。

照此速度，我们可能会在Gemini 4 Pro到来之前看到Gemini 3.9 Flash。

## 可用性

Gemini 3.8 Flash现已在常见的Google产品中可用，如Antigravity、Google AI Studio、Android Studio和Stitch，以及Gemini Enterprise。

拥有AI Pro和Ultra订阅的用户也可以在Gemini App、Google搜索中的AI模式以及Google表格中的Gemini中使用它。