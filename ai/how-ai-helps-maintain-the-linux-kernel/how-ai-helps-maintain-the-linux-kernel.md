
<!--
title: AI赋能：Linux内核维护提速
cover: https://cdn.thenewstack.io/media/2025/07/331af92b-sasha_levin.jpg
summary: AUTOSEL 是一款利用大型语言模型 (LLM) 辅助 Linux 内核维护的工具，尤其擅长补丁移植、代码生成、CVE 分类等重复性任务。它通过分析代码语义、交叉验证和检索增强生成等技术，减轻了维护人员的工作负担，提高了效率和一致性。
-->

AUTOSEL 是一款利用大型语言模型 (LLM) 辅助 Linux 内核维护的工具，尤其擅长补丁移植、代码生成、CVE 分类等重复性任务。它通过分析代码语义、交叉验证和检索增强生成等技术，减轻了维护人员的工作负担，提高了效率和一致性。

> 译自：[How AI Helps Maintain the Linux Kernel](https://thenewstack.io/how-ai-helps-maintain-the-linux-kernel/)
> 
> 作者：Joab Jackson

认识 AUTOSEL，一位帮助保持内核稳定的 Linux 维护者。

AUTOSEL 是一个脚本，它使用大型语言模型 (LLM) 来完成其任务。

它做着一项吃力不讨好的工作，一项所有内核维护者都厌恶的工作：移植补丁。

移植补丁是一个“非常乏味和令人沮丧的过程”，并且“无法扩展”，NVIDIA 杰出软件工程师 Sasha Levin 在[开源峰会](https://ossna2025.sched.com/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)上的[演讲](https://ossna2025.sched.com/event/1zffD/ai-for-kernel-engineers-sasha-levin-nvidia)中说道。[演示文稿](https://lwn.net/Articles/1026558/)侧重于 AI 如何开始在 Linux 内核社区中使用，以帮助跟上维护 Linux 内核的艰巨任务。

虽然它可能还没有为开源操作系统内核编写令人兴奋的新功能，但 AI 在那些令人麻木地重复但仍然必要的任务中表现出色。换句话说，AI 已经在让 Linux 内核开发人员的生活更轻松，帮助维护 Linux Kernel Stable 和 LTS 树的 Levin 说道。

## 补丁检查

作为世界上最大的开源项目，Linux 内核会不断更新和升级……很多。

这个速度一直保持不变：在 10 周的时间里，有多达 10,000 个新补丁进入主线内核。

Stable 和长期支持 (LTS) 内核维护者通常每天审查大约 100 个补丁，每天如此，包括周末和节假日。

只有少数几个，大约 5-10 个，最终适合移植。

Levin 用 Rust 编写的 [**AUTOSEL**](https://git.sr.ht/~sashal/autosel) 首先对传入的提交进行检查，寻找已提交的提交与过去的移植决策之间的相似之处，并且只建议那些似乎值得进一步审查的提交给人工提交者。

AUTOSEL 由多个 LLM 构建，每个 LLM 都用于特定的优势，以及用于交叉验证以减少错误和幻觉。

对于每次提交，该工具都会创建文本的数学表示（或“嵌入”），这些表示保留内核历史中每次提交的语义含义，使它们易于比较。

对于人工维护者来说，该工具减少了人工必须审查的提交数量。它甚至通过电子邮件解释其推理。

## 了解您的工具

像任何其他工具一样，LLM 的价值取决于用户对其的理解程度。

您可以将[大型语言模型](https://thenewstack.io/how-to-generate-ai-from-a-database-bruce-momjian/)视为下一代编译器，为开发人员提供生产力的飞跃，Levin 说道。它们就像“大型状态机”，但它们的不同寻常之处在于它们以概率性而非确定性的方式执行状态转换。

它们擅长在给定大量参数和用户提供的输入的情况下匹配模式。“温度”参数控制 LLM 的概率性，或者它对其材料的解释有多自由。

## 其他用途

像任何其他技术一样，LLM 首先在次要任务中进行测试。

LLM 在“小型、定义明确的任务”中表现出色。Levin 说道。

其中一种用途是代码生成和重构。定义明确的错误修复或将代码转换为其他形式（例如，标准 API）都是不错的任务。

对于 6.15 内核版本，Levin 让 LLM 编写了一个补丁，将开放式哈希表实现转换为标准 API。

Linux 内核 6.16 包括 `git-resolve`。此工具可以解决不完整或不正确的提交 ID，这是核心开发人员的[一个令人头疼的问题](https://lwn.net/Articles/1001526/)，但发生的频率不足以花费大量时间手动编写工具来找出不完整的 SHA-1 实际连接到哪个提交。

Levin 花了 20 分钟与 LLM 合作创建该工具。

工程师大约需要半天时间才能创建这样的工具，考虑到它所解决的问题的相对稀有性，这不值得付出努力。此外，LLM 还做了很多额外的工作：它创建了一组自测，甚至还编写了文档，而人工工程师即使会编写也会很不情愿。

Levin 说道，内核中可以完成的清理任务无穷无尽。LLM 可以帮助非英语母语人士编写描述性的提交消息。

## CVE 分类

另一项繁琐的任务是对安全漏洞（[CVE](https://thenewstack.io/vulnerability-management-best-practices-for-patching-cves/)）进行分类，这是 Linux 内核社区在 2024 年承担的一项任务。

这项工作包括检查提交，以查看它们是否解决了安全问题。

最初，编写了一组“hacky Bash 脚本”来提供帮助。

LLM 用于将这些脚本替换为一组用 Rust 编写的更精致的工具，其中包括一套完整的测试工具和文档。

以 AUTOSEL 为起点，CVE 分类器使用 LLM 识别解决安全问题的提交，然后继续检查该漏洞是否已在之前的补丁中解决。对于人类来说，这是一项艰巨的任务，因为组成 [Linux 内核](https://thenewstack.io/learning-linux-start-here/) 的代码有 4000 万行。

LLM 可以理解提交的语义含义，这提供了更全面的匹配能力。[检索增强生成](https://thenewstack.io/navigating-the-nuances-of-graphrag-vs-rag/) (RAG) 循环提取内核的开发历史和文档（例如，Git 存储库）以最大限度地减少幻觉。

Levin 指出，LLM 有效地充当了 AI 代理。他们可以直接针对代码存储库运行 [git 命令](https://thenewstack.io/how-to-make-git-a-developers-bff/)，例如 [`git blame`](https://git-scm.com/docs/git-blame)，以便从内核开发本身的历史中学习。

总而言之，到目前为止，AI 已经帮助 Linux 扩展了其维护工作，同时增强了一致性并减少了繁琐任务的人工劳动。