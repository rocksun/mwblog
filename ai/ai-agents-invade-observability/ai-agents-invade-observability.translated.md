# AI 代理入侵可观测性：蛇油还是 SRE 的未来？

### Mooster 和朋友们想加入你的运维团队。

[这份通讯](https://monitoring2.substack.com/archive) 五年前开始，旨在探索新兴的可观测性和监控初创公司。从最无聊的意义上说，这些公司获取运营数据，并从这些数据中为人类创造见解。这总是涉及大量的仪表盘、警报、API 集成以及每月高昂的账单。

这些企业有时会起飞——**Cribl** 自 2019 年首次被提及以来已筹集了 6 亿美元 [参见 2019 年的报道](https://monitoring2.substack.com/p/observability-pipelines-at-kubecon)——有时技术需要一段时间才能成熟 ([看看你，eBPF](https://monitoring2.substack.com/p/ebpf-a-new-bff-for-observability))。还有标准的 IT 炒作周期和监控的新用例，例如[开发人员使用大型语言模型构建应用程序](https://monitoring2.substack.com/p/large-language-model-observability) 或类似[数据可观测性](https://www.gartner.com/en/documents/5533895) 的准趋势。总的来说：日志、指标、跟踪和事件输入，开发人员或运营人员应该获得有用的信息。

截至 2024 年秋季，越来越多人以及大型软件公司认为，这种模式即将随着 AI 的进步而发生根本性改变。本期 *Monitoring Monitoring* 将探讨这对于可观测性业务意味着什么……如果“代理”生成式 AI 能够实现炒作。

#### 无处不在的代理（甚至 CRM 也无法幸免）

下一波生成式 AI 全部围绕着 *代理*，而不是“服务器监控代理”或“仪器代理”的意义（例如 [Dynatrace OneAgent](https://docs.dynatrace.com/docs/setup-and-configuration/dynatrace-oneagent)）。

这种新的代理（或“[代理](https://venturebeat.com/ai/agentic-ai-a-deep-dive-into-the-future-of-automation/)”）重点是指可以*使用真实世界数据采取行动* 的大型语言模型 (LLM)。例如，**OpenAI** 的**最新**模型在使用高级推理解决非常复杂的编程、数学和科学问题方面[做得很好](https://openai.com/index/learning-to-reason-with-llms/)。但 ChatGPT 无法像使用来自销售电话的笔记和内部客户数据来协商和达成合同那样做……至少现在还不行？

Marc Benioff 的一句引言在此处很有用，[减去他对](https://web.archive.org/web/20240913160122/https://fortune.com/2024/09/05/salesforce-ceo-marc-benioff-ai-agents-agentforce-dreamforce-gen-ai-era/)深奥的日本哲学的离题：他最近告诉 *Fortune*：“我们必须将整个公司转向代理”。（旧金山举行的 Salesforce 大型会议 Dreamforce 现已更名为 *Agentforce*。）

与 CRM 和金融科技相比，监控公司才刚刚开始参加代理 AI 派对。最大的问题是：*如果代理 AI 变得像初级运营人员或开发人员一样擅长理解运营数据，包括不同信号和系统之间的联系，会发生什么？*

#### 认识你运维团队的新成员

在代理监控领域，涌现出许多初创公司，它们的功能都超越了[迄今为止主要供应商发布的](https://newrelic.com/platform/new-relic-ai)聊天界面。从广义上讲，它们可以分为以下几类：

DevOps 和/或事件响应代理，试图自动化部分值班或例行维护工作。你可以选择的机器人包括

*Kura*(来自),[Kura](https://www.usekura.com/)*OneGrep Bot*(来自) 和[OneGrep](https://www.usekura.com/)*The Mooster*(来自).[Wildmoose](https://www.wildmoose.ai/) 也在这个领域，但似乎处于预发布阶段（尚未公布机器人名称）[Beeps](https://www.beeps.co/)“代理平台”或代理工具包，以提高自动化程度。

构建了一个围绕代理的解决方案，可以自动化多种类型的工程任务，而[RunWhen](https://www.runwhen.com/)开发了一个开源工具包，用于构建任何类型的通用代理。[Acorn Labs](https://www.acorn.io/)具有云或 Kubernetes 领域特定知识的专家 SRE 代理。

和[Parity](https://www.tryparity.com/)将自己定位在这个领域，尽管 SRE 侧重代理和 DevOps 代理之间的界限很模糊。还有开源项目[Cleric](https://cleric.io/)。[k8sgpt](https://k8sgpt.ai/)
所有这些解决方案的营销都围绕着用更少的资源做更多的事情，在某些情况下，从“副驾驶”或“助手”语言转向更具实体的东西：Parity 和 Cleric 将他们的解决方案定位为实际加入你团队的 SRE：“[我们正在构建一个运营商](https://cleric.io/blog/introducing-cleric)，而不是另一个工具。”

#### 更多 AI 蛇油，还是其他东西？
这并非监控领域第一次出现 AI 炒作周期。从从业者的角度来看，过去 5-7 年中以 AIOps 名义销售的各种功能（充其量）取得了喜忧参半的成功。2010 年代的机器学习算法并没有从根本上改变值班或事件响应工作流程。高级异常检测很有帮助，但如果误报反复在凌晨 3 点叫醒人们，它往往会被关闭（或从日常工作中移除）。

风险投资家认为这次可能有所不同。a16z [在关于 CRM 行业的文章中](https://a16z.com/ai-transforms-sales/)，阐述了其认为 Salesforce 杀手级产品的平台组件：

[T]he core of the next sales platform could be entirely unstructured and multimodal, including text, image, voice, and video. A company’s sales platform could include data about existing and prospective customers from countless sources… Furthermore, the LLM powering the platform would be constantly ingesting data to create the most up-to-date context.

如果我们用“运营数据”、“票务系统”、“值班手册”、“文档”和“源代码控制”替换“语音和视频”（幸运的是，这在 SRE 工作中不是关键部分）——你会得到一个与许多这些初创公司正在构建的解决方案看起来相同的市场架构。

这与 2010 年代监控初创公司从 [创建一种新型数据库](https://monitoring2.substack.com/p/big-prometheus) 开始的历史模式不同，这种数据库的灵感来自大型科技公司内部学习的系统。与 [网络规模](https://www.youtube.com/watch?v=b2F-DItXtZs) 不同，秘诀在于连接更多实时、运营和内部数据的来源，这些来源通过专有的 LLM 粘合剂整合在一起。

至少这是概念，如果它奏效，将改变从业者进行可观察性、监控和事件响应的方式。

#### 基准测试和谋杀之谜
如果每个主要的 APM 供应商和数十家初创公司在明年发布代理，客户将很难分辨什么是 [蛇油](https://www.cs.princeton.edu/~arvindn/talks/MIT-STS-AI-snakeoil.pdf) 以及什么是真正有用的。一种方法是 [在金融领域也看到了](https://github.com/patronus-ai/financebench)，即为评估代理回答问题和展示特定领域知识的能力提供开放的基准测试。

在过去的一周中，Parity 发布了第一个已知的 Kubernetes 或云基准测试 [SREBench](https://sreben.ch/)——您可以在模拟集群中与他们的代理进行竞赛，看看谁能够更快地诊断出根本原因。他们构建了基准测试，[根据他们的博客文章](https://www.tryparity.com/blog/how-and-why-we-made-srebench-swebench-for-k8s)，通过整合他们发现的最接近的现有基准测试中的概念，这些概念可以应用于现代 SRE： [解决谋杀之谜](https://arxiv.org/abs/2310.16049)。

[虽然有许多不同类型的 AI 基准测试可用](https://huggingface.co/collections/open-llm-leaderboard/the-big-benchmarks-collection-64faca6335a7fc7d4ffe974a)，但更多针对运营和事件响应任务的特定领域基准测试是受欢迎的，也是需要的。基准测试 [远非完美](https://www.reddit.com/r/LocalLLaMA/comments/1b933of/llm_benchmarks_are_bullshit/)，但可以帮助未来的代理客户在测量代理在模拟环境中解决问题的有效性方面有一个起点。否则，就像之前的 AIOps 浪潮一样，我们主要依靠分析师报告和热情的销售团队提供的白皮书，这些白皮书说明了您的平均故障修复时间 (MTTR) 将减少多少。
#### 美元符号和困境
我们正处于了解基于 LLM 的代理对可观察性领域影响的早期阶段。除了围绕这些代理在复杂运营环境中的有效性问题外，还有同样多的数据隐私和监管问题尚未解决。您（或欧盟监管机构）是否愿意将包含潜在个人身份信息的数据的交易日志提供给 The Mooster？还有一个悬而未决的问题，即如何监控这些代理以确保合规性和安全性。

定价是另一个问题。如果有效的 SRE 代理需要大量运营数据 *和* 大量 NVIDIA GPU 来完成工作：从您最喜欢的 APM 供应商那里开出的账单上再加几个零。

如果您是风险投资家，[您会看到美元符号](https://foundationcapital.com/goodbye-aiops-welcome-agentsres-the-next-100b-opportunity/)。如果您在监控领域工作，您可能会看到自己工作的终结。如果您是监控供应商的客户，您可能只是厌倦了听到关于 AI 的消息。

由于本周在旧金山举行了 [Agentforce](https://www.salesforce.com/news/press-releases/2024/09/12/agentforce-announcement/)，最后一句话来自 Benioff 在 *Fortune* 杂志的采访中。

“这是关于突破创新者的困境。”

🚗🚗🚗
[订阅](https://monitoring2.substack.com/subscribe) 该新闻稿以获取更新，了解未来几个月的发展情况。

如果您读到这篇文章以为是关于 LLM 监控的，请查看 2023 年初的这篇文章：[大型语言模型可观察性。](https://monitoring2.substack.com/p/large-language-model-observability)

*披露：意见仅代表个人观点，不代表我的雇主。我不是任何提及公司的顾问、雇员或投资者。本新闻稿中没有付费职位、赞助或广告。*