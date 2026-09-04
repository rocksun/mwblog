<!--
title: 英伟达斥资129亿美元收购Hugging Face以掌控模型开源生态
cover: https://cdn.thenewstack.io/media/2026/08/72f30588-alona-savchuk-cmojhp5ybsq-unsplash-scaled.jpg
summary: 英伟达斥资129亿美元收购开源模型库Hugging Face，旨在通过掌握开发者获取模型的核心平台，巩固CUDA软件生态。此举不仅是对抗竞争对手的防御，更是在AI模型日益开源化的趋势下，确保英伟达硬件在未来AI架构中不可替代的战略布局。
-->

英伟达斥资129亿美元收购开源模型库Hugging Face，旨在通过掌握开发者获取模型的核心平台，巩固CUDA软件生态。此举不仅是对抗竞争对手的防御，更是在AI模型日益开源化的趋势下，确保英伟达硬件在未来AI架构中不可替代的战略布局。

> 译自：[Nvidia is paying $12.9 billion to keep open models on its chips](https://thenewstack.io/nvidia-open-models-chips/)
> 
> 作者：Matthew Burns

*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 进展，并解释它们对使用这项技术的人员和组织意味着什么。核心论点很简单：学会使用 AI 的从业者将定义其行业的下一个时代，而本通讯旨在帮助你成为其中一员。*

---

据 [*The Information* 报道](https://www.theinformation.com/articles/nvidia-agrees-buy-open-source-model-repository-hugging-face-12-9-billion)，英伟达本周同意以 129 亿美元收购 Hugging Face。这笔收购让人联想到微软当年收购 GitHub 的举动。

英伟达选择了跟随开发者。它收购了开发者们获取 AI 模型的主要阵地。与此同时，Anthropic 和 OpenAI 正在向一个日益将“免费”视为默认选项的市场兜售溢价服务。

运行这些开源模型也变得越来越容易。本周早些时候，Ollama 发布了一个新版本，支持在 Claude Desktop 中运行 Qwen、DeepSeek 和 Kimi。你只需打开 Anthropic 的应用，点击模型选择器，即可将 Opus 5 替换为 Kimi K3。

我们的同事 Paul Sawers 曾为 *The New Stack* [报道了 Ollama 的这次发布](https://thenewstack.io/ollama-claude-desktop-integration/)。0.33.0 版本于 8 月 21 日上线，它利用本地代理绕过了 Claude Desktop 对非 Anthropic 模型 ID 的限制。在 Mac 菜单栏切换“Use Ollama models”，无论你是在本地还是在 Ollama Cloud 上运行，模型都会出现在 Anthropic 的选择器中。“开源模型应该易于运行、易于构建，并且在人们需要的地方随处可见，”Ollama 首席执行官 Jeffrey Morgan 表示。该公司在 7 月完成了 6500 万美元的 B 轮融资。

硬件也在跟进。苹果本周发布了新款 Mac Mini 和 Mac Studio 配置，看起来就是专为在本地运行大型模型而设计的。Frederic Lardinois 两周前[撰文介绍了阿里巴巴的 Qwen3.8-27B](https://thenewstack.io/qwen38-27b-local-inference/)。其 4-bit 版本大小为 16.1GB，可以在配备 32GB 统一内存的 Mac 上运行；阿里巴巴的内部基准测试显示，它在编程和计算机操作方面达到或超过了 Opus 4.6 Max 的水平。虽然这是阿里巴巴的测试数据，且早期用户反馈该模型有时会“过度思考”，但它确实能塞进一台笔记本电脑里。

转换成本也在随之下降。TNS 作者 Janakirm MSV 从 5 月份就开始关注这一趋势，当时 [OpenCode 在 GitHub 上的星标数量超过了 Claude Code](https://thenewstack.io/anthropic-claudecode-opencode-split/)（分别为 157,000 和 122,000）。他写道，大多数开发者面临的真正决策是“他们的环境是否能容忍单一供应商的束缚”。Jason Calacanis 周三在 X 上发布了商业版本的观点：[“开源目前解决了 90% 的创业用例，所以精明的创始人不会为 Fable 付费。”](https://x.com/Jason/status/2092748113765126313) 他写道，每位员工每月 500 美元感觉还可以，但“当费用达到五位数时，CFO 们就开始紧张了。”创始人是早期信号，而 CFO 是更广泛的信号。

## 英伟达为开发者获取模型的平台买单

那么，129 亿美元为英伟达换来了什么？一个年收入约 1.5 亿美元的网站。英伟达本身已经构建并免费提供自己的开源模型，因此它并不缺乏模型权重。

2018 年，微软斥资 75 亿美元收购 GitHub，因为那是代码的栖息地，拥有它使 GitHub 成为微软希望开发者下一步操作的所有功能的入口。对于模型权重而言，Hugging Face 正是这样的存在。每一个开源模型的发布和每一次微调都发生在那里。这是开发者寻找如何运行模型时的首选平台。

产品分析师 Aakash Gupta [进行了计算](https://x.com/aakashgupta/status/2092810836142354830)来解释这个价格。英伟达刚刚报告季度营收为 962 亿美元，因此 129 亿美元大约相当于 12 天的销售额。而英伟达最大的客户都在构建“逃生路线”：OpenAI 正在与 Broadcom 设计芯片，Anthropic 在亚马逊的 Trainium 上进行训练，谷歌则在自研 TPU 上投入了十年。

开源模型是一种制衡力量，因为下载的模型默认会在英伟达的 CUDA 上进行微调和服务。只要开发者继续选择开源模型，他们也就选择了英伟达的软件栈。Gupta 写道：“英伟达花费了 12 天的营收，以确保其客户的开源竞争对手永远不会消亡。”

这之所以有效，是因为开源模型运行在英伟达的硬件上。下载 Qwen 并进行微调，除非你刻意避开，否则每一步都会在 CUDA 上运行。Broadcom 和亚马逊可以制造芯片，但他们谁也无法让一万个存储库以其为目标。

所以，你为了摆脱单一供应商定价所做的努力，反而让你更深地陷入了另一家的掌控之中。

Hugging Face 同时也是排行榜、数据集和 transformers 库的中心，行业很大一部分都在使用这些。英伟达很快将拥有这一切。坚定的风险投资人 Bill Gurley 在周三[发文解释了原因](https://x.com/bgurley/status/2092812868098175408)：他写道，“开源模型是高风险软件竞争的必然结果。利害关系越大，开源获胜的可能性就越高。这就像水往低处流。”

他在 7 月份为《华盛顿邮报》撰写的长文中[更深入地阐述了这一观点](https://www.washingtonpost.com/opinions/2026/07/20/open-model-ai-is-good-competition-anthropic-openai/)，标题点名了那两家正准备上市的公司：开源 AI 模型是 Anthropic 和 OpenAI 的良好竞争对手。

显而易见的反对意见是，Hugging Face 的下载量并非生产流量，大多数实际工作仍然运行在闭源 API 上。这很合理。但自 2 月份以来，中国开源模型在 OpenRouter 上的美国 token 使用量[占比一直超过 30%](https://aiweekly.co/alerts/chinese-ai-models-hit-record-58-of-us-openrouter-traffic)，最高峰达到 46%。目前，那是市场上转换成本最低的领域。

对于 AI 原生开发者来说，经验教训不是用 Qwen 替换 Claude 或停止向 Anthropic 付费。对于许多工作而言，闭源模型仍然是正确的答案。经验教训是：不要假设今天的默认选择在明天依然适用。

每个 AI 原生应用都有默认值：模型、注册表、绑定工具、API。这些变成了依赖项，而依赖项就成了筹码。据报道，英伟达同意花费 129 亿美元收购开发者寻找和微调模型的首选之地。

这改变了 AI 原生开发者的工作方式。五年前，最优秀的开发者学习 Kubernetes。今天，他们花时间比较基准测试分数，争论哪个模型最聪明。而这正变得不那么重要。真正的难题在于：当底层的默认值发生变化时，如何构建能够生存的系统。

因为变化终将来临。