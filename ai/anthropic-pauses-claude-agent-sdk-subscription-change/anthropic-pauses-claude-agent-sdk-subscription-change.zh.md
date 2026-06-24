Anthropic 暂停了对使用其 Claude [Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) 付费订阅的开发者所受影响的计费变更——在原定生效的当天撤回了这一决定。

此公告发布之前，Anthropic 经历了[动荡的一周](https://thenewstack.io/anthropic-fable-mess-explained/)。6 月 9 日，[该公司发布了](https://thenewstack.io/anthropic-claude-mythos-fable-5/) Fable 5 和 Mythos 5——这是其首批正式发布的[Mythos 类模型](https://thenewstack.io/anthropic-glasswing-mythos-cybersecurity/)，构建了强大的网络安全护栏——然而几天后，[美国政府便发布了出口管制指令](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/)，迫使 Anthropic 向全球所有客户下架了这两款模型。

现在看来，Anthropic 希望通过推迟一项可能导致许多开发者和第三方机构为其 Claude 自动化使用支付更高费用的计费变更，为全球用户群带来一点好消息。

## 拆分使用额度

早在 5 月份，[Anthropic 就曾告知订阅用户](https://x.com/ClaudeDevs/status/2054610152817619388)，它将把使用额度一分为二。在此之前，Claude 订阅用户的所有活动——聊天、在终端编写代码或使用基于 Agent SDK 构建的第三方工具——都从同一个月度额度池中扣除。该公司此前表示，从 6 月 15 日起，Agent SDK 的使用将转为 Pro、Max、Team 和 Enterprise 订阅用户的单独月度限额，Pro 用户为 20 美元，顶级 Max 和 Enterprise 席位最高可达 200 美元。

对于像 [Zed](https://zed.dev/) 这样依赖 Agent SDK 将用户的 Claude 订阅与产品连接起来的第三方工具而言，这一变化影响巨大。在 5 月份公告发布后的第二天，Zed 的增长与营销主管 [Franciska Dethlefsen](http://www.linkedin.com/in/franciskadethlefsen/) 在[博文中指出](https://zed.dev/blog/anthropic-subscription-changes)，之前的订阅费用以大约 API 等效成本 15 到 30 倍的价格补贴了此类使用——这一数字来源于工程师兼企业家 [Matthew Diakonov](https://fazm.ai/about) 的[分析](https://fazm.ai/blog/claude-pro-vs-api-cost-comparison)——而新的额度将按完整的 API 费率计费。

不过，Dethlefsen 指出了一种变通方法：用户如果直接在 Zed 内部的终端运行 Anthropic 官方的 Claude CLI，而不是通过 Agent SDK，则仍可保留现有的订阅限制。

同一工具，根据调用方式的不同，计费方式也不同。

## 暂停变更

然而，周一 Anthropic 开始向订阅用户发送电子邮件，称根据 [Hacker News 等论坛](https://news.ycombinator.com/item?id=48546618)上的报道，计划中的变更已被取消。该公司的[支持文档也已更新](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)，以相匹配的内容证实 Agent SDK 的使用将继续从标准订阅限制中扣除，并且不存在单独的额度需要领取。

“我们正在暂停下述关于 Claude Agent SDK 使用的变更，”消息中写道。“目前，一切都没有改变。”

![暂停变更](https://cdn.thenewstack.io/media/2026/06/834bb16a-screenshot-2026-06-16-at-11-09-17-use-the-claude-agent-sdk-with-your-claude-plan-claude-help-center.png)

*暂停变更*

这一时机为那些已经向用户传达了该变更的公司造成了尴尬局面。[Conductor](https://www.conductor.build/) 是一款基于 Claude Agent SDK 构建的多智能体编码工具，它[发布了一篇文章](https://www.conductor.build/blog/claude-subscription-update)告诉客户他们目前没有问题。“Anthropic 已经推迟了 Claude 计划的订阅更新，”Conductor 团队写道。“您可以继续正常使用您的 Claude 计划进行 Conductor 开发。”

## 坎坷的计费调整之路

6 月 15 日的暂停是 Anthropic 在第三方 Agent SDK 访问方面进行的一系列计费变更中的最新一次，其背后的紧张关系是整个行业都在努力解决的问题。正如 Anthropic 的 Claude Code 负责人 [Boris Cherny 在 4 月份所说](https://x.com/bcherny/status/2040206441756471399?lang=en)，在宣布对第三方工具访问进行早期限制时，订阅“并非为这些第三方工具的使用模式而构建”——这承认了统一费率定价与开放式的代理使用模式并不兼容。

GitHub 得出了相同的结论并采取了行动，在 6 月份[取消了](https://thenewstack.io/github-copilot-token-billing/) Copilot 的统一高级费率模式，转而采用基于 Token 的计费方式——这一变化引起了不少抱怨，但最终还是实施了。

在 Anthropic 计费反转的同一周，[加州联邦法院受理了一起拟议的集体诉讼](https://www.wsj.com/tech/ai/anthropic-sued-over-limits-on-its-200-a-month-ai-plans-e2a109e4)，[指控](https://www.vacadaffanlaw.com/post/kahn-v-anthropic-pbc) Claude 的 Max 订阅层级在进行繁重的编码任务时，其实际使用倍率远低于其广告宣传的水平。

在计费方面，Anthropic 尚未说明修订后的方案何时出台，仅表示它“正在努力更新计划，以更好地支持用户如何使用 Claude 订阅进行构建。”

我们确实知道的是，该公司正因 Fable 和 Mythos 而感受到来自美国政府的压力。再加上其[成为上市公司](https://www.anthropic.com/news/confidential-draft-s1-sec)的计划，以及来自其强劲竞争对手 OpenAI 的[降价传闻](https://www.wsj.com/tech/ai/openai-considers-drastic-price-cuts-anticipating-war-for-users-with-anthropic-9b8c178e)，很明显 Anthropic 正在努力争取开发者的支持——而暂停计费变更就是它目前可以做到的一种方式。