<!--
title: OpenAI安全系统已开始在任务执行中途截断API响应
cover: https://cdn.thenewstack.io/media/2026/09/b13afb24-logan-voss-jpgocgsx3wa-unsplash-scaled.jpg
summary: 随着AI竞速引发安全担忧，OpenAI正考虑放缓模型开发步伐。目前，其安全框架已介入模型运行，导致部分API任务中途被迫中断，这不仅让开发者的预期变得难以捉摸，也凸显了行业在追求性能与安全协同上面临的严峻挑战。
-->

随着AI竞速引发安全担忧，OpenAI正考虑放缓模型开发步伐。目前，其安全框架已介入模型运行，导致部分API任务中途被迫中断，这不仅让开发者的预期变得难以捉摸，也凸显了行业在追求性能与安全协同上面临的严峻挑战。

> 译自：[OpenAI's safety system is already cutting off API responses mid-task](https://thenewstack.io/openai-slowing-ai-development/)
> 
> 作者：Amanda Caswell

**过去几年里，各大AI公司都在竞相**构建最先进的模型，试图以比竞争对手更快的速度发布新产品，每一款新产品的发布都不断提升着人工智能的智力水平。如今，OpenAI 正在思考，在某些情况下放慢脚步是否更有意义。

本周，AI 研究员 Jacob Coxon 从 Anthropic 离职，并[对这场竞赛的发展方向发出了严厉警告](https://thenewstack.io/anthropic-alignment-superintelligence-warnings/)。曾在 OpenAI 工作并参与过 [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/) 训练的 Coxon 指责两家公司在尚不清楚如何将其安全控制在范围之内的情况下，就盲目地竞相开发功能更强大的 AI。

OpenAI 首席执行官 Sam Altman 开始讨论采取行动。据[彭博社报道](https://www.bloomberg.com/news/articles/2026-09-11/openai-is-open-to-slowing-cutting-edge-ai-ceo-sam-altman-tells-staff)，他本周告诉员工，公司愿意放缓最先进 AI 系统的开发速度，并可能与其他前沿实验室进行协调。

> OpenAI 可以选择放慢脚步，但如果像 Anthropic、Google DeepMind 等公司继续保持当前速度，这种放慢将毫无意义。

这一想法存在一个显而易见的问题：OpenAI 可以选择放慢脚步，但如果像 Anthropic、Google DeepMind 等公司继续保持当前速度，这种放慢将毫无意义。

开发人员已经习惯了每隔几个月就有新模型发布，每一款新模型都能弥补上一款模型的不足。但是，如果安全担忧开始阻碍发布或限制访问，团队可能无法再依赖新模型的及时到来。[OpenAI 已经展示了这种情况可能带来的后果](https://openai.com/index/path-to-astra/)。

## 安全暂停已有先例

今年夏天，由于各种不同的原因，OpenAI 两次踩下了“刹车”。

8 月，在内部评估发现 [GPT-6 Astra 存在严重的网络安全隐患](https://thenewstack.io/openai-gpt6-astra-benchmarks/)后，该公司停止了其最大的前沿强化学习运行。此前，在 OpenAI 的 AI 智能体突破隔离并[危及 Hugging Face](https://thenewstack.io/openai-huggingface-sandbox-breach/) 之后，其大部分模型开发工作曾暂停了两周。

OpenAI 最终恢复了工作，但前提是限制了访问权限并增加了更多防护措施。Astra 的发布本身也存在问题。[公开上线时间比计划晚了数天](https://thenewstack.io/gpt6-astra-developer-access-delayed/)，这促使 Altman 为他所称的“混乱发布”进行了道歉。

## 能力触发限制

OpenAI 使用其[预备框架 (Preparedness Framework)](https://openai.com/index/path-to-astra/) 来评估模型在网络安全、生物和化学威胁等领域的能力。Astra 在网络安全方面被评为最高等级的“关键 (Critical)”，这是 OpenAI 首个被评为该等级的商用模型。

达到这一级别后，公司认为模型可以在无需人类逐步引导的情况下，发现并利用加固系统中的零日漏洞。因此，OpenAI 限制了访问权限，进攻性网络功能被放入受控访问程序 Daybreak 中，而企业客户必须主动选择加入 Astra，而不是自动获得访问权限。

这些限制也体现在 API 中。一些早期用户发现[响应在任务执行中途被截断](https://thenewstack.io/astra-api-safety-stops/)，这使得 OpenAI 的安全系统导致模型看起来像是超时了。对于开发人员而言，影响正是在此处变得具体起来。

## 协调仍然是难点

鉴于如此多的 AI 公司都在推动同样的功能，大家共同放慢脚步才合情合理。否则，OpenAI 暂停而其他人继续前进，这不仅会在不一定降低整体风险的情况下失去市场地位。

> 鉴于如此多的 AI 公司都在推动同样的功能，如果大家能共同放慢脚步，才更有意义。

OpenAI 的首席科学家 [Jakub Pachocki](https://www.linkedin.com/in/jakub-pachocki/) 在 9 月 6 日的论文[《异类思维 (An Alien Mind)》](https://openai.com/index/path-to-astra/)中表达了这一观点。他认为，没有哪个实验室能足够好地解决对齐和监控问题，从而可以无限期地以最高速度进行扩展。他希望在行业拥有由第三方审计机构、政府或国际机构支持的共同安全标准之前，自愿放慢速度成为常态。

7 月，超过 1,000 名 AI 从业者签署了[《放慢前沿开发步伐 (Pacing the Frontier)》](https://explainx.ai/blog/pacing-the-frontier-ai-employees-letter-july-2026)公开信，呼吁美国政府解决前沿 AI 开发的速度问题。Pachocki、Anthropic 首席执行官 Dario Amodei 和 Meta 首席科学家赵晟佳 (Shengjia Zhao) 分别签署了该文件。

[彭博社报道称](https://www.bloomberg.com/news/articles/2026-09-11/openai-is-open-to-slowing-cutting-edge-ai-ceo-sam-altman-tells-staff)，OpenAI 一直在研究企业如何在不触犯反垄断法的情况下进行协调。即使这个问题得到解决，各实验室仍需就衡量标准达成一致。他们使用不同的评估和安全框架，因此在一个实验室中严重到足以停止工作的评估结果，在另一个实验室中可能不会产生同样的影响。

## 开发者承担后果

如果模型发布变得越来越难以预测，工程团队将不得不自己解决更多问题。这意味着可能需要重新设计智能体架构、在模型仍然会出错的任务周围添加确定性的护栏，或者从已部署的模型中挖掘更多潜力。

> 如果模型发布变得越来越难以预测，工程团队将不得不自己解决更多问题。

在 AI 智能体并没有如预期般自动为团队节省太多时间的情况下，这增加了工作量。[OpenAI 自身的研究表明，智能体已经为与其合作的人类制造了新的瓶颈](https://thenewstack.io/openai-agent-research-bottleneck/)。模型开发的放缓可能会导致这些团队在更长时间内受限于现有的局限性。