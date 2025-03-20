# “随心所欲”式编程时代已来临 — 但你准备好迎接“随心所欲”式故障处理了吗？

想象一下，完全沉浸在感觉中进行编码，忘记代码的存在。不用自己输入，而是让 [Cursor](https://www.cursor.com/) 和 [Sonnet](https://www.anthropic.com/claude/sonnet) 为你构建一切。当遇到错误时，你不会尝试进行故障排除，而是将错误反馈给 LLM 并复制粘贴修复程序。代码的复杂程度超出了你的理解范围，但最终总能正常运行。OpenAI 创始成员 Andrej Karpathy 这样描述 [“随心所欲”式编程](https://x.com/karpathy/status/1886192184808149383)。

虽然 Karpathy 将其视为周末临时项目的有趣方法，但现实情况是，“随心所欲”式编程（或大量使用 LLM 编写代码）的某种形式已经在大规模发生。Google 报告称，[AI 生成了其 25% 的新代码](https://arstechnica.com/ai/2024/10/google-ceo-says-over-25-of-new-google-code-is-generated-by-ai/)，并且在行业的许多领域，这个数字可能更高。多人[报告](https://www.linkedin.com/feed/update/urn:li:activity:7293680969788653569/)称，包括 HubSpot 在内的公司的软件工程师不再被允许编写软件，而只能提示 LLM。在我看来，“随心所欲”式编程是构建软件的未来。

但是，当 AI 生成的代码在生产环境中出现故障并导致中断时会发生什么？在本文中，我将探讨这个问题，并分享一些让你的工程组织做好准备的想法。

## 在发生中断之前，“随心所欲”式编程只是娱乐

拥有了解他们所操作的代码库的熟练工程师至关重要。强大的工程组织甚至通过在团队成员之间传播知识来确保没有工程师成为[单点故障](https://thenewstack.io/james-webb-space-telescope-and-344-single-points-of-failure/)。

当发生事件时，通常的反应是请[了解受影响部分的工程师](https://thenewstack.io/the-6-pillars-of-platform-engineering-part-1-security/)来快速解决它。然而，随着越来越多的[代码由 LLM 生成](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/)，深入了解代码库的工程师将变得越来越稀少，从而使中断更难诊断和解决。

加州大学伯克利分校的博士生 Shreya Shankar 在一条[推文](https://x.com/sh_reya/status/1873431565650502060)中完美地捕捉到了这个问题，该推文已获得超过 3 亿的浏览量：“为什么没有人谈论由于盲目集成 AI 生成的代码而导致的值班工程师有多糟糕？LLM 是出色的编码员，但却是糟糕的工程师。” 并且由于现在中断的成本为[每分钟 14,000 美元](https://www.bigpanda.io/blog/it-outage-costs-2024/)，因此很明显，团队不能浪费时间来破译由 LLM 编写的代码。

## “随心所欲”式编程遇到“随心所欲”式故障处理

AI 生成的代码不会消失，[61% 的工程团队正在拥抱生成式 AI](https://jellyfish.co/blog/61-of-engineering-teams-are-embracing-generative-ai-heres-why-and-how-to-join-them/)——它只会增加。以下是如何为未来的事件管理做好准备。

首先，使用 AI 驱动的事件管理工具，如 [Rootly](https://rootly.com/ai) 或 [PagerDuty Advanced](https://www.pagerduty.com/platform/generative-ai/)。这些工具处理事件的后勤工作——自动启动通信渠道、为不同的利益相关者起草更新以及管理事后分析。这些工具也已开始使用 AI 将当前事件与过去的事件进行匹配，帮助你快速找到类似的案例以及修复它们的人员，从而缩短平均解决时间。

然后，升级你修复事件的方式。如果你可以使用工具来查明根本原因并提出修复建议，该怎么办？这正是新一波由 LLM 驱动的事件解决工具（标记为 AI SRE 助手）正在做的事情，例如 [Sentry AI](https://sentry.io/changelog/sentry-ai-now-available-for-early-adopters/) 和 [Datadog Bits AI](https://docs.datadoghq.com/bits_ai/)。

这些工具处理与 SRE 相同的数据——[错误日志](https://thenewstack.io/observability-isnt-enough-its-time-to-federate-log-data/)、指标、应用程序跟踪——但也摄取非结构化的人工生成数据，如 Slack 讨论、操作手册和事后分析。它们可以快速[自动化根本原因分析](https://thenewstack.io/machine-learning-for-automated-root-cause-analysis-promise-and-pain/)，突出显示触发问题的提交、可视化它如何影响系统指标以及跟踪导致中断的故障链。因此，当有人收到警报并使用计算机时，根本原因分析已经可以查看。
更高级的工具不仅仅是诊断问题，它们还会提出解决方案。您可以在部署修复程序之前审查、讨论和批准，或者让工具自动处理一切。可以理解的是，一些运维工程师对此持怀疑态度。如果LLM产生幻觉，提出了一个让事情变得更糟的修复方案怎么办？如果没有回滚可用怎么办？逐步部署更改可以帮助降低风险，但这只是需要考虑的众多因素之一。AI驱动的事件解决很有前景，但它也带来了一系列挑战。

然而，自我修复工具并不新鲜：它们已经存在了至少十年以上。Facebook在2011年推出了[FBAR](https://engineering.fb.com/2011/09/15/data-center-engineering/making-facebook-self-healing/)，以自动化机架维护。Dropbox在2016年推出了[Naru](https://www.usenix.org/conference/srecon16europe/program/presentation/mah)，以处理服务器故障、警报和修复。然而，这些都是具有预定义规则的确定性系统，大大降低了搞砸的机会。

在LinkedIn，作为一名高级SRE，我[共同设计了一种自我修复机制](https://patentcenter.uspto.gov/applications/14185537)，用于分布式基础设施，该机制使用机器学习进行根本原因分析和修复，尽管它从未完全实现。随着LLM的兴起，这种方法正在发生，我很高兴看到它变为现实。这个领域的公司正在取得真正的进展。竞争正在升温。市场上至少有20家参与者，风险投资正在[涌入](https://techcrunch.com/2024/12/11/microsofts-m12-invests-another-22-5m-into-nuebird-months-after-its-22m-seed-round/)。进入事件共振（incident vibing）！是的，我刚编了这个词。

## 如果你无法击败他们，就加入他们

随着生成式AI使开发人员的工作效率提高到[两倍](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/unleashing-developer-productivity-with-generative-ai)，这种趋势不会消失。那么，为什么不拥抱事件共振呢？当发生中断时，请坐下来，喝杯咖啡，让你的AI-SRE助手找出如何修复你的Vibe Coding同事的工作。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等。