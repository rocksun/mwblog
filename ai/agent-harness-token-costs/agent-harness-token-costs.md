<!--
title: Aider、Claude Code和OpenClaw运行相同模型，Token消耗量差异竟高达70倍
cover: https://cdn.thenewstack.io/media/2026/08/40e08666-pablo-merchan-montes-ky6yrouqe44-unsplash-scaled.jpg
summary: 本文探讨了AI编码代理的工具框架（Harness）对成本的影响。研究发现，不同框架在启动开销（Startup tax）和缓存利用率上的巨大差异，导致相同模型下Token使用量可相差70倍。企业在评估AI成本时，应关注每次成功任务的成本及缓存命中率，而非单纯对比Token单价。
-->

本文探讨了AI编码代理的工具框架（Harness）对成本的影响。研究发现，不同框架在启动开销（Startup tax）和缓存利用率上的巨大差异，导致相同模型下Token使用量可相差70倍。企业在评估AI成本时，应关注每次成功任务的成本及缓存命中率，而非单纯对比Token单价。

> 译自：[Aider, Claude Code, and OpenClaw ran an identical model. Token use varied 70-fold.](https://thenewstack.io/agent-harness-token-costs/)
> 
> 作者：Janakiram MSV

**当团队为AI编码代理定价时，**他们倾向于仔细审查模型。但最近的三项基准测试表明，Harness（即引导AI完成任务的软件框架）的重要性可能不亚于模型本身。

原因对于任何Web开发人员来说都很熟悉：每次推理请求都需要上下文。相关的历史记录要么必须重新提供，要么由服务系统重建。因此，提供商在每一轮对话中都会处理大量重复的文本块，包括Harness的系统提示词（system prompt）和工具描述。

6月，一项独立的[基准测试](https://www.eishanlawrence.com/blog/harness-efficiency-bench)在同一12个Python任务上比较了两种模型下的12种配置。8月，Composio在30个企业工作流中比较了8种使用DeepSeek V4 Flash的Harness。与此同时，Artificial Analysis在其[编码代理指数](https://artificialanalysis.ai/agents/coding-agents)中持续追踪Harness与模型的配对情况。

## 三项基准测试的衡量指标

[Composio](https://composio.dev/)报告了涵盖Airtable、Gmail、Google日历、Google表格、GitHub、Slack和PostHog的30个工作流。每项任务都在900秒的上限内运行。一个程序化的验证器（而非LLM评判员）对结果进行评分，使用的是植入诱饵和近乎相同密钥的隔离测试装置。

Composio报告了240次运行，其中129个工作流成功完成。每个成功任务的成本从Pi Agent的0.028美元到Claude Code的0.195美元不等。DeepAgents的通过率与Claude Code完全一致，但每次成功的成本仅为后者的四分之一。

Composio透明地披露了实验控制并不完美。例如，Pi在两个模型提供商之间运行了不同的推理设置，而Prime Agent在30次运行中仅产生了24次可评分结果。这些警告使得该实验无法被称为纯粹的单变量实验。

6月的基准测试衡量的不是美元，而是Token，且范围更广。其作者报告了Aider、Claude Code、Codex、Goose、Hermes、Kilo、Kimi Code、Nanobot、OpenClaw、Opencode和Qwen Code的运行情况，并将Aider的架构师模式（architect mode）单独计算。所有12种配置都在[OpenRouter](https://openrouter.ai/about)上运行相同的任务，因此每个Harness都使用了相同的API和模型。测试套件在DeepSeek V4 Flash和Nvidia的Nemotron 3 Ultra上运行。第二个模型在OpenRouter上提供免费层级，因此您可以免费重新运行它。

报告显示，每个已解决任务的Token数从Aider架构师模式下的约3,500个到OpenClaw的292,000个不等。这一范围之所以具有参考价值，是因为其稳定性极高，因为在两个无关模型之间，排名几乎没有变动。这指向了Harness软件本身，而非模型行为。

Artificial Analysis以更高的统计权重处理同一问题。Artificial Analysis发布了一个组合了DeepSWE、来自Laude Institute的Terminal-Bench v2.1以及Scale AI的SWE-Atlas-QnA的指数。总计326个任务，通过率取三次尝试的平均值。它报告了每种配对的任务成本、Token使用量和端到端耗时。它还发布了一项对照比较，在保持Claude Opus 4.7不变的情况下，在Claude Code、Cursor CLI和Opencode之间进行切换。

## 启动税（Startup tax）

其核心差异源于6月基准测试中衡量的一个关键指标：启动税。在提示词开始任何工作之前，Harness会自带其“行李”。这些行李就是系统提示词、工具描述和环境设置。基准测试显示，Aider在架构师模式下约为700个Token，而OpenClaw约为26,000个。

如果这40倍的开销只支付一次，那尚可容忍，但重发模式使其变得不可接受。作者指出，一个在15轮对话中携带26,000个Token基础开销的Harness，仅在脚手架上就花费了约390,000个输入Token。

测试证实了背后的数学逻辑。启动税乘以轮数可以预测每个已解决任务的Token数，两个模型的R平方值均为0.99。寻求削减代理支出的开发人员应首先查看提示词基础开销和轮数，然后再进行更复杂的优化。

关于该回归数字，有一个需要注意的点。6月的基准测试对每个Harness、任务和模型组合仅进行了一次测试，因此没有方差估计，且代理运行具有随机性。Artificial Analysis在这一点上更有分量，因为它对326个任务中的每一个都进行了三次平均尝试。将6月的开销发现视为该机制的证据，将更大的指数视为比较当前生产级配对的最佳工具。

> 昂贵的Harness并没有囤积上下文；它们只是携带了更沉重的基本开销。

令人惊讶的是，无法解释这种差异的原因。每个Harness的上下文增长速度相似，每轮增加几百个Token，因此增长率并不是区分它们的原因。昂贵的Harness并没有囤积上下文；它们只是携带了更沉重的基本开销。

## 缓存Token重新定义了排行榜

两个Harness实验都指向了第二个机制，Artificial Analysis在其方法论中将其视为实质性因素。这是团队最容易出错的一个环节。

Composio披露，Claude Code仅从缓存中提取了1.5%的输入Token，而Codex约为70%，OMP为57%。新鲜输入的成本大约是缓存输入的五倍。因此，Claude Code的Token消耗量与竞争对手相当，但其账单却并非如此。

6月的基准测试在其设置中也发现了类似的不对称性。在DeepSeek运行中，Codex为该套件计费超过一百万个Token。缓存读取占其中的77%，按正常费率的十分之一计费。按照实际账单计算，Codex在每个已解决任务上的成本比Claude Code更便宜，而后者的原始Token使用量仅为前者的二分之一。

作者将Claude Code接近零的缓存份额归因于服务路径而非其提示词。在该设置中，Claude Code是唯一通过Anthropic风格的Messages端点与OpenRouter通信的Harness。网关对该方言的转换似乎降低了相同流量在OpenAI风格端点上本应获得的缓存命中率。网关行为会发生变化，因此请将其视为观察到的一种路径。

Artificial Analysis将该假设内置于其成本模型中，而非通过发现得出。它警告称，提示词缓存命中率会随提供商路由而有很大差异。其成本模型将缓存输入和缓存写入分开定价，而不是按未缓存费率对每个提示词Token计费。一个必须将缓存写入分开定价的基准测试，正是在告诉开发人员服务路径的重要性。

## 重型Harness的价值何在

解释成本差距并不等于选出最便宜的Harness。观察、行动、检查和重复的代理循环是一个成本倍增器。它在处理陌生的代码、失败的测试和跨多个文件的更改时最有帮助。在一个小型、描述清晰的编辑任务上，循环大多只是重新确认单次调用本可以假设的结果。

但硬任务测试的结果并不符合脚手架论点的预测。跨越成本范围的四个Harness在宽松限制下运行了10个SWE-bench Lite任务，所有四个都解决了完全相同的一个任务。作者报告称，Aider耗费了80万个Token，而Codex花费了1500万个Token。在一个模型上运行10个任务作为归纳基础过于薄弱，因此将其视为一种提示。

质量是“Harness定价论”需要限定的地方，因为基准测试对此有争议。Composio报告了8个Harness的通过率，从OpenCode的46.7%到Pi Agent的66.7%，在同一模型上存在20个百分点的差距。Artificial Analysis在更大的任务集上发布了同样的差距。Harness的选择改变了成本的倍数，并以百分点改变任务成功率，这是数量级的差异而非方向的差异。

## 平台团队应该衡量什么？

企业已经发现，拥有Harness并不能解决成本问题。那些[构建](https://thenewstack.io/enterprise-ai-agent-harness/)自己编码代理的团队仍然需要为底层的推理支付费用。成本控制已经转移到平台层，而不是模型合约。

| 问题 | 衡量指标 | 为什么明显的指标会误导 |
| --- | --- | --- |
| 哪个Harness更便宜？ | 每个已验证结果的成本 | Token计数忽略了通过率和缓存层级 |
| 我们支付的是标价吗？ | 实时流量的缓存份额 | 折扣取决于网关和端点，而不仅仅是Harness |
| 它能承受大提示词吗？ | 传输的字节数与发送的字节数 | 静默截断在输出中表现为成功 |

### 每个成功任务的成本，而非每个任务的成本

单独阅读通过率和Token计数将错误地对Harness进行排名。Claude Code和DeepAgents完成了相同数量的Composio工作流，但一次成功的Claude Code运行成本却高出四倍以上。采购团队应要求提供“每个已验证结果的成本”，并拒绝仅基于Token的比较。

### 实际服务路径上的缓存份额

缓存折扣不仅仅是Harness的属性。它们取决于端点方言、网关和提供商。

> 缓存折扣不仅仅是Harness的属性。它们取决于端点方言、网关和提供商。

平台团队可以在一个下午的时间里验证自己流量的缓存比例，这种练习的价值远高于模型迁移。

### 负载下的提示词保真度

6月的基准测试在每项任务前注入了100,000个Token的无关日志噪音，并报告了五种不同的行为。12种配置中有7种忠实地传输了提示词。Kilo和Opencode丢弃了其中的83%-89%，但仍报告成功。

> 静默截断是最危险的，因为它在Harness输出中看起来完全像是成功。

OpenClaw拒绝运行，Kimi Code崩溃，Claude Code发送了所有内容但表现不佳。静默截断是最危险的，因为它在Harness输出中看起来完全像是成功。

## 接下来是什么

Anthropic、OpenAI、Google和Microsoft在如何对Harness层收费方面已经[出现分歧](https://thenewstack.io/ai-agent-harness-pricing-split/)。DeepSeek随后使其运行时组件在MIT许可下均可替换。开发人员现在可以在公开可用、持续更新的指数中比较Harness与模型的配对。这正是模型定价最初变得充满争议的前提条件。

对于本季度标准化代理平台的企业而言，Harness值得与模型同样的审查。在这些实验中，Harness的选择产生的成本差异足以与模型定价上的巨大差异相匹敌，即便是在模型表现大致稳定的工作负载上。开发人员、平台团队和财务负责人现在有了可以争论的可复现依据。这比三个月前Harness对话所能提供的要多得多。