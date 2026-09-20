<!--
title: Anthropic新推出的Claude Code功能可能让你在午饭前耗尽订阅额度
cover: https://cdn.thenewstack.io/media/2026/09/c8aa7919-logan-voss-_iiaxf2h1eu-unsplash-scaled.jpg
summary: Anthropic升级Claude Code，推出具备任务拆解与并行协调能力的全新Projects功能。该功能可自动分发任务至多线程执行，虽提升了开发效率，但由于每个线程都计入独立会话，将导致订阅额度被迅速消耗，用户需留意使用频率。
-->

Anthropic升级Claude Code，推出具备任务拆解与并行协调能力的全新Projects功能。该功能可自动分发任务至多线程执行，虽提升了开发效率，但由于每个线程都计入独立会话，将导致订阅额度被迅速消耗，用户需留意使用频率。

> 译自：[Anthropic's new Claude Code feature could drain your plan before lunch](https://thenewstack.io/claude-code-parallel-projects/)
> 
> 作者：Amanda Caswell

**Anthropic为Claude Code赋予了新职责**：管理其他Claude Code会话。

Anthropic宣布，从周四开始，部分Claude Pro和Max订阅用户可以通过Claude Code中的云会话访问重新设计的Projects（测试版），访问权限将在接下来的一周内扩展至更多计划用户。

该公司正在重新设计Claude Projects——此前它将聊天内容归集在共享知识库和指令周围——新增了一个协调器，可以接收工程目标，将其分解为更小的任务，并将其分发给并行运行的多个Claude Code会话。这将消除以前开发人员在会话之间分配任务并自行整合结果的手动工作。

“Claude负责界定请求范围、委派工作、协调并行线程、审查输出并组装最终结果，”一位Anthropic代表告诉 *The New Stack*。

一旦开发人员设定了目标，Claude就会决定如何跨线程拆分工作，开发人员可以监控这些线程，或者在需要介入时单独打开它们。每个线程都作为其自己的Claude Code云会话运行，并拥有独立的存储库分支和副本。它可以利用子代理（subagents）、循环和工作流来处理工作的各个小部分。

## 更多的会话意味着消耗更多的计划额度

这种并行方法也可能更快地用尽Token额度。Anthropic表示，当多个线程运行时，Projects会更快达到使用限制，因为每个线程都被计算为一个完整的Claude Code会话。

Anthropic目前正面临由其Max计划付费开发者提起的一项[集体诉讼](https://thenewstack.io/anthropic-claude-max-lawsuit/)，指控称其广告宣传的使用量增加伴随着最初未披露的每周上限。

> “Claude负责界定请求范围、委派工作、协调并行线程、审查输出并组装最终结果。”

## 单个Claude协调工作

例如，一个正在弃用旧API端点的团队可以连接其API、Web和移动端存储库，并让Claude为每个存储库创建一个线程来更新调用方、运行测试并开启PR，然后再确定哪些更改需要优先合并。

开发人员可以通过主Project聊天窗口跟踪工作，或者打开单个线程进行检查或重定向，而无需亲自启动和管理每个Claude Code会话。

协调器并非委托的最后一层，因为当工作需要时，每个工作线程都可以利用Claude Code现有的子代理、循环和工作流进一步拆分其分配的任务。这一审查层可能不仅仅是表面工作：在[测试编码代理对抗私有代码库](https://thenewstack.io/real-swe-coding-benchmark/)的Real-SWE基准测试中，即使是得分最高的Anthropic自有模型Fable 5.1，也有超过60%的时间失败。

这一发现表明，当代理被投入到不熟悉的生产代码中时，协调和输出审查与模型本身的原始能力同样重要。

## 并行线程，熟悉的冲突

每个线程都在自己的分支上工作，这保持了工作的独立性，但并不能阻止两个线程更改相同的代码。当这种情况发生时，Anthropic表示会像处理任何其他Pull Request一样处理合并冲突。

> 每个线程都在自己的分支上工作，这保持了工作的独立性，但并不能阻止两个线程更改相同的代码。

## 项目背景在各线程间共享

此外，Anthropic正在增加共享记忆功能，以便在一个线程中获取的信息可以被其他线程使用，而无需开发人员反复提供相同的上下文。

Projects可以保留诸如更改后的发布日期、功能被删除的原因，或者谁需要批准特定服务的更改等详细信息，这些信息随着工作的持续（历时数天或数周）而不断累积。

Claude还可以记住开发人员希望如何管理项目，包括检查频率、何时启动新线程以及更新的详细程度；同时，一个新库将用户添加的文件与Claude生成的工件一起保留，以便未来的工作可以借鉴项目中已经创建的资料。

用户可以跟踪特定于Project的使用情况，并为协调器和工作线程选择模型和工作强度。此外，支持在开发人员的工具和代码（包括私有网络后的资源）旁边本地运行线程的功能也即将推出。

该测试版将在接下来的一周内扩展到更多Claude Code Pro和Max计划用户，移动端支持即将到来，团队版和企业版访问计划在稍后推出。

已经在通过Projects工作的现有订阅者将保留在当前版本，直到Anthropic为他们升级。此次重组是更广泛的产品整合的一部分：Anthropic最近[合并](https://thenewstack.io/anthropic-claude-unified-interface/)了Claude聊天和其Cowork界面，合并为一个统一的视图，旨在减少消除模式选择带来的摩擦，而非增加摩擦。

> 已经在通过Projects工作的现有订阅者将保留在当前版本，直到Anthropic为他们升级。