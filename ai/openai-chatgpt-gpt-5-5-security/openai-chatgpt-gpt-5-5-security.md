<!--
title: “类 Mythos 级黑客能力，向所有人开放”：业界回应 OpenAI GPT 5.5 发布
cover: https://cdn.thenewstack.io/media/2026/04/c88a1521-m-faisal-sbcij29m3iq-unsplash-scaled.jpg
summary: 本文探讨了业界对 OpenAI GPT-5.5 发布的反应。该模型在编程和安全漏洞检测上进步显著，展现出极强的实战能力，但也面临 API 访问受限及推理成本增加等争议。
-->

本文探讨了业界对 OpenAI GPT-5.5 发布的反应。该模型在编程和安全漏洞检测上进步显著，展现出极强的实战能力，但也面临 API 访问受限及推理成本增加等争议。

> 译自：[“Mythos-like hacking, open to all”: Industry reacts to OpenAI’s GPT 5.5](https://thenewstack.io/openai-chatgpt-gpt-5-5-security/)
> 
> 作者：Paul Sawers

OpenAI 或许凭借 ChatGPT 统治了消费级聊天机器人市场，但在开发者中，通过其 [Claude Code 代理](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/) 接入的 Anthropic Claude 模型已成为首选工具。

更广泛地说，这两家公司正步调一致地前进，交替发布功能和模型。因此，在 [Anthropic 上周发布 Opus 4.7](https://thenewstack.io/claude-opus-47-launch/) 之后，其竞争对手跟进只是时间问题。周四，[OpenAI 推出了](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/) GPT-5.5 和 GPT-5.5 Pro，这是其最新的通用模型，在编程和更复杂任务方面有所改进。

## 超越基准测试

OpenAI 自己的头条新闻是“用于实际工作的新一类智能”，这呼应了 AI 公司日益增长的努力，即将他们的模型呈现为已准备好处理日常工作。

该公司还严重依赖基准测试结果来支持这一主张，指出其在编程、推理和系统使用测试中均有提升。但基准测试分数并不总是能反映模型在现实世界使用中的表现，并且 [在某些情况下](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/) 可能会被操纵或完全规避。

这引出了一个更直接的问题：当开发者真正使用 GPT-5.5 时，它的表现如何？

博主兼开源开发者 [Simon Willison](https://www.linkedin.com/in/simonwillison/) 获得了该模型的早期访问权限，他 [将其描述为](https://simonwillison.net/2026/Apr/23/gpt-5-5/) “快速、有效且能力极强”，但很快就遇到了一个明显的限制：缺乏 API 访问，这意味着他无法立即运行他常用的测试。

其中一项测试是他长期运行的“[骑自行车的鹈鹕](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/)”基准测试，要求模型生成一只骑自行车的鹈鹕的 SVG——这是一个故意设置的古怪提示，旨在测试它们处理结构化、陌生任务的能力。

为了绕过缺乏 API 访问的问题，Willison 使用半官方的 Codex “后门” API 构建了自己的插件来运行测试。Willison 发现，该模型的默认输出在此任务上落后于 GPT-5.4，但在给予更多推理时间后有所改善——代价是更高的 Token 使用量和更慢的响应。

“我见过 GPT-5.4 表现更好，所以我加上了 *`-o reasoning_effort xhigh`* 并再次尝试，”Willison 在最初使用 GPT-5.5 效果不佳后表示。“那次花了将近四分钟才生成，但我认为这是一个好得多的尝试。”

简而言之，更好的结果是存在的，但可能是以时间和计算资源为代价的。

其他测试该模型的人员指出，它在所需引导方面的改进非常明显。哈佛大学 AI 研究所的研究员 [Soumitra Shukla](https://www.linkedin.com/in/soumitra-shukla/) 在 X 上 [观察到](https://x.com/soumitrashukla9/status/2047515787695472741)，在 Codex 应用中使用 GPT-5.5 后，新模型“能够直接领会意图”，需要的“手把手指导少得多”，并且处理长期运行的任务更加流畅。

定价也影响了早期的反应。Willison 注意到，一旦进入 API，GPT-5.5 的 [成本](https://openai.com/index/introducing-gpt-5-5/#availability-and-pricing) 大约为其前代产品的两倍，而 GPT-5.5 Pro 的价格则显著更高，这意味着 GPT-5.4 作为低成本替代方案可能具有更长的生命周期。

这种权衡也伴随着 Willison 遇到的访问限制。OpenAI 解释说，API 访问的延迟是由于额外的安全和合规要求，并补充说对 GPT-5.5 和 GPT-5.5 Pro 的支持即将推出。然而，这一推迟发布的决定正值人们对更强大模型如何部署（特别是在编程和网络安全等领域）的审查日益加强之际。

例如，Anthropic 在 [4 月初宣布](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/)，出于安全考虑，它将暂不开放其 Mythos 模型的广泛访问。

对于 OpenAI 来说，其企业化推进使这些同样的担忧成为焦点。该公司仅在本周就推出了 [工作区代理](https://thenewstack.io/openai-shared-workspace-agents/) 和 [专注于 PII 的隐私过滤器](https://thenewstack.io/openai-privacy-filter-pii/) 等功能，并与包括 Nvidia 在内的 [合作伙伴一起测试了 GPT-5.5](https://blogs.nvidia.com/blog/openai-codex-gpt-5-5-ai-agents/)，Nvidia 表示它已为 10,000 多名员工提供了早期访问权限。

这些努力取决于模型在安全关键任务中的表现。

## “类 Mythos 的黑客能力，向所有人开放”

一些早期测试者表示，GPT-5.5 在现实世界的安全任务中已经展现出强大的性能。[Albert Ziegler](https://www.linkedin.com/in/albert-ziegler-6b3b24138/) 曾是 GitHub 研究员和机器学习工程师，现在是安全公司 Xbow 的 AI 负责人，他在 [一篇博文](https://xbow.com/blog/mythos-like-hacking-open-to-all) 中写道，该公司使用内部基准测试针对已知的软件漏洞对 GPT-5.5 进行了评估。

他在文章中写道，在这些测试中，GPT-5.5 将遗漏漏洞的比例降低到了 10%，而 GPT-5 为 40%，[Anthropic 的 Opus 4.6](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) 为 18%，这表明其在渗透测试任务中的表现发生了阶跃式变化。

“每一个被遗漏的漏洞都是现实生活中的隐患，”Ziegler 写道。

Ziegler 将其描述为“*类 Mythos 的黑客能力，向所有人开放*”，指的是 Anthropic 限制访问的网络安全模型。然而，正如 Hacker News 社区的一些人 [指出的](https://news.ycombinator.com/item?id=47883953) 那样，鉴于 Mythos 尚未公开，这种比较很难考证。其他研究人员 [还发现](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)，在给定相同任务的情况下，较小的开源权重模型可以重现 Anthropic 自身 Mythos 示例中显示的大部分分析。

Mythos 缺乏独立验证也 [引发了批评](https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/)，一些人认为，主张与可重复结果之间的差距有破坏这些系统呈现方式信任的风险。

无论如何，更广泛的观点可能仍然成立：对好人有用的东西对坏人也有用。而目前，API 访问的缺乏阻碍了这些能力被轻易滥用的可能性。

## “参差不齐的前沿”

对于 Willison 和其他获得早期访问权限的人来说，描述哪些地方得到了改进并不总是一件容易的事。“正如最近通常的情况一样，很难用语言表达它好在哪里——我要求它构建东西，它就完全按照我的要求构建！”Willison 写道。

[Ethan Mollick](https://en.wikipedia.org/wiki/Ethan_Mollick) 是宾夕法尼亚大学沃顿商学院的 AI 研究员和教授，他也 [表达了类似的观点](https://www.oneusefulthing.org/p/sign-of-the-future-gpt-55)，指出“越来越难以快速展示每一次代际变化”，因为模型曾经难以处理的许多任务现在都变得微不足道了。

尽管如此，Mollick 认为潜在的收益仍然是巨大的。

“我认为这很有意义。这很有意义，因为它表明我们还没有完成 AI 的快速改进，”Mollick 在他的 Substack 专栏 *[One Useful Thing](https://www.oneusefulthing.org/p/sign-of-the-future-gpt-55)* 中坚称。“这很有意义，因为它就是单纯的优秀。这很有意义，因为即使有了这一切，AI 能力的前沿仍然是参差不齐的。”

在他自己的测试中，Mollick 要求 GPT-5.5 Pro 构建一个“程序化生成的 3D 模拟”，展示一个小港口城镇几千年来的演变，并将结果与早期的 OpenAI 模型和开源权重替代方案进行比较。只有 GPT-5.5 Pro 生成的版本能够有意义地模拟随时间推移的变化，而不仅仅是更换静态资产。

他还指出了他所描述的 AI 三个主要层面的进步：模型、应用和 [harnesses](https://thenewstack.io/ai-agent-harness-pricing-split/)——即将模型连接到工具和现实世界工作流程的系统。使用由 GPT-5.5 驱动的 Codex，他能够分析多年的研究数据并起草一篇学术论文，产出了他形容为可与博士项目早期阶段相媲美的作品。

“模型越来越聪明，应用越来越强大，而系统框架越来越完善，使它们在解决实际问题时更加有效，”Mollick 写道。

然而，仔细观察可以发现，AI 能力的“参差不齐的前沿”并未完全消失。虽然模型在诸如编程等输出可以验证和迭代的结构化领域变得非常有效，但它们在更具开放性或创造性的任务中仍然表现挣扎。

在他自己的测试中，Mollick 发现，虽然 GPT-5.5 可以处理复杂的、多步骤的工作——从模拟到起草学术论文——但这些收益并没有平均地扩展到所有任务，特别是在需要持续连贯性或独创性的领域。

“GPT-5.5 显然不是这一过程的终点，但它是沿途值得注意的一步，”Mollick 写道。“参差不齐的前沿仍然存在。只是它比以前远得多。”