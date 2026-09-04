<!--
title: Anthropic Fable 5.1 登场：更便宜、更聪明，且更少拒绝你的请求
cover: https://cdn.thenewstack.io/media/2026/09/ca11b9a3-screenshot-2026-09-01-at-12.45.26-pm-1024x572.png
summary: Anthropic 发布了 Fable 5.1 模型，在降低 75% 缓存读取费用的同时提升了性能。新版本优化了安全防护策略，减少了对合法请求的误拦截，并推出了企业边界防护（EFS）以实现零数据留存，同时增强了防蒸馏机制。
-->

Anthropic 发布了 Fable 5.1 模型，在降低 75% 缓存读取费用的同时提升了性能。新版本优化了安全防护策略，减少了对合法请求的误拦截，并推出了企业边界防护（EFS）以实现零数据留存，同时增强了防蒸馏机制。

> 译自：[Anthropic's Fable 5.1 is a bit cheaper, a bit smarter, and refuses a lot less](https://thenewstack.io/anthropic-fable-5-1-launch/)
> 
> 作者：Frederic Lardinois

**周二，Anthropic 发布了其旗舰模型 Fable 和 Mythos 的最新版本**。Anthropic 承诺，更新后的模型将以更低的成本提供更强的性能，这主要得益于公司降低了缓存读取的价格。

与以往一样，Fable 5.1 和 Mythos 5.1 在底层是相同的模型，但 Fable 5.1 现已全面开放，而 Mythos 5.1 仍仅限于 Anthropic 的受信任访问计划，因为它具有 [Anthropic 所称](https://www.anthropic.com/claude-fable-and-mythos-5-1)“专门设计用于支持网络安全和生命科学领域工作”的防护措施。

价格保持不变，输入/输出 Token 每百万 10 美元/50 美元，但缓存读取价格现仅为每百万 0.25 美元，降幅达 75%。

与 Fable 5 一样，Fable 5.1 仍仅限于 API 使用，以及拥有 Max、Team Premium 和 Enterprise Premium 计划的用户（使用量为其每周限额的 50%）。Pro 订阅者可以通过使用额度来使用它。

## Fable 5.1 基准测试结果

在 Anthropic 分享的基准测试中，Fable 5.1 轻松超越了旧版模型、Anthropic 的 Opus 5 以及 OpenAI 的 GPT-5.6 Sol。现在已经没人再费心去与 Gemini 3.1 Pro 进行比较了。

![](https://cdn.thenewstack.io/media/2026/09/37aee892-screenshot-2026-09-01-at-11.45.05-am-1024x756.png)





*图片来源：Anthropic*

总的来说，Anthropic 表示新模型在几乎所有方面都优于 Fable 5，且成本更低。这在一定程度上取决于具体的基准测试，但大多数情况下，这意味着用户可以将推理模式调低一到两个档次，仍能获得与高设置下 Fable 5 相同的结果，同时 Fable 5.1 总共消耗的 Token 更少。

> 总的来说，Anthropic 表示新模型在几乎所有方面都优于 Fable 5，且成本更低。

除了在 Terminal-Bench-Science 0.1 基准测试（测试模型在使用智能体进行科学研究方面的能力）中表现出大幅提升外，许多改进并不显著。在该测试中，Fable 5.1 得分为 52.6%，而 Fable 5 为 24.7%。

在大多数其他领域，改进幅度在 Fable 5 或 Opus 5 的 2-4% 以内。

因此，Claude Code 中的 Fable 5.1 默认采用高推理模式设置，而在 Claude Cowork 和 Claude.ai 中则默认为中等。

![](https://cdn.thenewstack.io/media/2026/09/37aee892-screenshot-2026-09-01-at-11.45.20-am-1024x744.png)





*图片来源：Anthropic*

## Claude Code 安全防护放宽

Fable 5 的一个问题是它过于谨慎，当感觉到用户触及其安全底线时，往往会退回到 Opus 模型。现在，Anthropic 表示已使这些防护措施更加精确，“确保它们不太可能标记良性内容（例如关于医疗问题的查询，或网络防御者使用模型使其系统更安全），但仍确保它们能针对真正的威胁提供强有力的保护。”

> 对于使用 Claude Code 的编码人员来说，最直接的变化是模型的安全防护措施有望更少地阻碍工作流程。

对于使用 Claude Code 的编码人员来说，最直接的变化是模型的安全防护措施有望更少地阻碍工作流程。

Anthropic 表示，其网络安全防护措施现在每次会话的干预频率比 Fable 5 降低了约 60%，并且模型现在被允许识别代码中的漏洞。

不过，渗透测试、漏洞利用生成和扫描二进制文件漏洞仍未开放，Anthropic 表示将继续把这些请求重定向到其 Opus 模型。

生物学防护措施也进行了类似的更新，现在对关于基础生物学和医学问题的良性请求的干预频率降低了 85%。

## 那些水印怎么办？

Anthropic 最近分享了其为模型生成文本添加水印的技术（针对 2026 年 8 月 2 日之后发布的模型）。

水印是一种不可见的数字标记，用于标记 Claude 编写给定文本的可能性。Anthropic 表示它不会影响输出质量，也不包含任何关于用户、组织或对话的数据。然而到目前为止，Anthropic 之外的人员还没有办法真正检测它。

随着本次发布，Anthropic 正在开启一个检测 API 的私有预览版，“向欧盟法律要求的符合条件的组织（如监管机构、执法部门、媒体、事实核查员、独立研究人员、教育组织和欧盟公民社会团体）开放”。

有义务验证水印以遵守欧盟《人工智能法案》的企业也将获得访问权限，未来计划进行更广泛的推广。

## 数据留存

对于想要使用 Fable 5 的企业来说，Anthropic 的留存政策是一个争议点。虽然 Anthropic 为其其他模型的合格客户提供零数据留存，但 Fable 5 用户必须选择 30 天的留存期。

现在，Anthropic 推出了所谓的 [企业边界防护](https://www.anthropic.com/news/enterprise-frontier-safeguards) (EFS)，称其在提供零数据留存隐私的同时，保留了监控滥用的能力。

“EFS 的工作原理是将数据存储在完全由客户控制的云基础设施中，而不是 Anthropic，”该公司在公告中写道。“它将从今年秋季晚些时候开始，分阶段提供给企业客户。在 EFS 可用之前，符合条件的客户将能够使用 Fable 5.1 进行零数据留存。”

![](https://cdn.thenewstack.io/media/2026/09/bb4999b9-021fdfc765d03eaac26f5d2aa9cb06111b7a9297-3840x4644-1-847x1024.webp)





*图片来源：Anthropic*

Anthropic 表示，该系统是根据客户反馈设计的。毕竟，受监管行业的企业在那些数据留存规则下实际上无法使用该模型。

“因此，我们坐下来与客户一起设计了一个解决方案，旨在提供两全其美的结果：零数据留存的隐私性，以及允许跨时间和账户进行监控的安全能力，”Anthropic 解释道。

在实践中，这意味着 EFS 将数据移动到客户自己的云存储中，例如 Amazon S3、Azure Blob Storage 或 Google Cloud Storage，数据在其中保持加密状态（使用用户的密钥）。然后，它会在该数据上运行 Anthropic 的自动检测，Anthropic 侧不进行人工审查，并将任何警报路由回客户。

截至目前，该工具涵盖了 Claude Code、Claude Enterprise、Claude Platform，以及 Amazon Bedrock、Microsoft Foundry 和 Google Agent Platform 上的 Claude。该公司表示，除了客户自己的云存储账单外，不会有额外费用。

EFS 将从今年秋季开始分阶段推出。在此之前，Anthropic 不会保留 Fable 5 和 Fable 5.1 的任何使用数据。

## 反蒸馏

Fable 5.1 还附带了 Anthropic 所称的加强型防蒸馏机制。当然，该公司一直直言不讳地表达了[其对中国实验室正以工业规模蒸馏](https://thenewstack.io/moonshot-fable5-distillation-accusations/)其模型的怀疑。

其中第一个是对 API 本身的更改：新账户不再能够“在多轮对话中手动编辑 Claude 的先前上下文，同时保留 Claude 先前思维的转录”。

Anthropic 表示，这关闭了“一种常见的、公开记录的蒸馏技术”。然而，这也会阻碍那些重写或压缩对话历史的智能体工具，该公司表示，该限制将扩展到现有账户以及未来的模型版本。