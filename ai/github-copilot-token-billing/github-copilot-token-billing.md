<!--
title: GitHub Copilot 按用量计费正式上线：你需要了解的一切
cover: https://cdn.thenewstack.io/media/2026/06/d76b6e5a-masantocreative-emf3jsxsqtq-unsplash-scaled.jpg
summary: GitHub Copilot正式将包月制改为基于Token的按量计费模式。新方案引入AI积分和全新Max计划，支持组织额度共享，旨在应对智能体任务带来的高昂算力成本。
-->

GitHub Copilot正式将包月制改为基于Token的按量计费模式。新方案引入AI积分和全新Max计划，支持组织额度共享，旨在应对智能体任务带来的高昂算力成本。

> 译自：[GitHub Copilot's usage-based billing is live: Here's what you need to know](https://thenewstack.io/github-copilot-token-billing/)
> 
> 作者：Paul Sawers

我们[早就知道这一天会到来](https://thenewstack.io/github-copilot-usage-billing/)，而截至周一，它已经正式上线。GitHub 正式退役了 Copilot 的高级请求模型，并[将其替换为](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/)[基于 Token 的计费系统](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises)，将您的费用直接与实际使用量挂钩。

这一转变已经酝酿了数月，其背后是开发者使用 Copilot 方式的根本性转变。这款工具在[2021年](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)最初只是一个编辑器内的自动补全工具，而如今已发展成为一个能够处理横跨整个代码库的长期、自主编程任务的平台。

## 按用量计费正式上线：有哪些变化？

在此之前，Copilot 采用固定月费订阅与所谓的“高级请求单元”相结合的模式。高级请求单元是一种额度，允许用户访问更消耗算力的功能（如高级聊天或长时间运行的智能体任务），而无需直接与成本挂钩。GitHub 承担了这些使用背后不断攀升的大部分推理成本，但随着智能体任务变得越来越长、要求越来越高，这种模式变得难以为继。

> “GitHub 承担了这些使用背后不断攀升的大部分推理成本，但随着智能体任务变得越来越长、要求越来越高，这种模式变得难以为继。”

展望未来，每个 Copilot 方案都将包含每月分配的 GitHub AI 积分（Credits），而不是高级请求单元。积分将根据 Token 使用量进行消耗——包括输入、输出和缓存数据——并按照每个模型公布的费率进行扣除。

方案价格整体保持不变。对于个人订阅者，Pro 用户（10 美元/月）每月可获得总计 15 美元的积分，Pro+ 用户（39 美元/月）可获得 70 美元。每个方案都包含与订阅价格 1:1 匹配的固定基本额度，外加一部分可变的充值额度。GitHub 表示，随着模型定价和 AI 成本的变化，它将逐步调整这部分额度。这种所谓的“灵活配额”（flex allotment）充值是在用户提出担忧后引入的，因为他们担心原始的基本额度可能不足以支撑更繁重的智能体工作负载。

GitHub 母公司微软的产品副总裁 [Joe Binder](https://www.linkedin.com/in/joe-binder-ba781ab2/) 明确表示，基本积分是永久性的，而灵活配额部分更多是为了在未来应对 AI 基础设施成本变化而做好的准备。

> “灵活配额……旨在随着 AI 经济效益的变化而进行调整，包括模型定价、新模型以及效率的提升，”

Binder 在[5月份的一篇博客文章](https://github.blog/news-insights/company-news/github-copilot-individual-plans-introducing-flex-allotments-in-pro-and-pro-and-a-new-max-plan/)中写道：“灵活配额是您包含的使用量中的可变部分；它旨在随着 AI 经济效益的变化而进行调整，包括模型定价、新模型以及效率的提升。”

与此同时，Copilot Max 也正式上线，这是一款专为对 Copilot 有重度需求的开发者打造的全新顶级个人方案。

该方案售价为每月 100 美元，包含每月总计 200 美元的积分——其中 100 美元为与订阅价格相匹配的基本积分，外加 100 美元的灵活配额。这使其定位远高于 Pro+，旨在支持持续、高强度的智能体工作，而无需担心频繁触发额度上限。

现有的 Student、Pro 和 Pro+ 订阅者今天即可升级到 Max；然而，为了应对需求，GitHub 目前[暂停了所有个人方案的新用户注册](https://thenewstack.io/github-copilot-signups-paused/)，该公司表示预计将在未来几周内重新开放注册。

![按量计费的样貌](https://cdn.thenewstack.io/media/2026/06/a37f3989-table.png)

*按用量计费的样貌*。

年度方案订阅者需要注意一个重要事项：在方案到期之前，他们将继续使用现有的高级请求系统，到期后则会转为新的月度模式。在此过渡期间，GitHub 提高了年度订阅者的模型倍率。

对于商业和企业客户，每席位价格分别稳定在每月每用户 19 美元和 39 美元，并匹配同等额度的积分。然而，与个人方案不同，商业和企业层级没有灵活配额——每个席位分配的积分与席位单价完全一致，没有额外赠送。为了缓解过渡期的压力，这两个层级在8月份之前都将获得充裕的促销积分——商业客户每用户 30 美元，企业客户每用户 70 美元。代码补全和下一次编辑建议包含在所有付费方案中，不消耗积分。

除了计费方面的变化外，GitHub 还改进了 Copilot 代码审查（code review）的运作方式。代码审查现在除消耗 AI 积分外，还将消耗 GitHub Actions 额度时长（按与其他 Actions 工作流相同的每分钟费率计费），并且组织管理员现在可以设置一个默认的运行器（runner），在所有代码库中自动使用。此前，每个代码库都必须单独配置，这给大型团队带来了额外的管理开销。通过新的组织级运行器设置，管理员只需定义一次，即可应用到所有地方。

## 预算控制

除了价格本身之外，这次变革最有趣的方面无疑是[全新的预算控制系统](https://docs.github.com/en/copilot/concepts/billing/budgets-for-usage-based-billing#user-level-budget)——对于大规模管理 Copilot 的组织来说，它的复杂程度可能超出第一眼所见。

在新模式下，商业和企业版积分在组织层级进行池化（pooled），而不是分配给每个用户的独立池子——这意味着重度用户在需要时可以消耗更多，而轻度用户则可以抵消这部分消耗。

> “重度用户在需要时可以消耗更多，而轻度用户则可以抵消这部分消耗。”

共有四种控制机制协同工作，来管理该积分池的消耗方式以及耗尽时的处理流程：全局用户级预算、个人用户级预算覆盖、成本中心预算和企业级预算。用户级预算始终处于激活状态，并始终强制执行硬性停止——它们限制了任何单个用户从共享池和任何按量计费超额部分中可消耗的上限。其他控制机制仅在共享池耗尽且使用量进入按量计费范围时才会生效。

最重要的一点是要理清企业预算的实际定义。它并不限制每月的总支出。它仅限制共享积分池耗尽后产生的按量计费费用。根据 GitHub 官方文档中的示例，一个拥有 400 个 Copilot Business 席位的组织，无论如何都要支付每月每用户 19 美元、共计 7,600 美元的许可费。在此基础上设置 5,000 美元的企业预算，意味着最高账单为 12,600 美元，而不是 5,000 美元。

毋庸置疑，这里涉及的细节很多，事情很容易变得繁琐棘手。简而言之，如果用户级预算的总和允许了超出共享池所能提供的消耗，差额就会溢出到按量计费使用中。如果企业预算太低，无法弥补这一差额，用户将在达到个人上限之前就被切断服务——GitHub 将此称为“最低剩余空间获胜”规则（lowest remaining headroom wins），这可能会让管理员措手不及。

每当提高用户级预算时，都需要重新审视企业预算的计算。例如：一个个人预算还剩 5 美元的用户可能会被阻止，仅仅因为企业预算只剩下 1 美元——此时他们的个人额度已经无济于事。

正如一位[企业用户在 Reddit 上指出的那样](https://www.reddit.com/r/GithubCopilot/comments/1tbuneg/enterprise_perspective_on_copilots_usagebased/)，对此一个理智的应对方法是从第一天起就将其视作一个 FinOps（云财务运营）问题。

“我们正在对使用情况进行 FinOps 风格的分析，识别重度用户，规划预算上限，[并]指导开发者进行模型选择、Prompt 大小控制以及高效使用，”他们写道。同时他们也承认，团队正在同步探索替代方案，包括直接订阅 OpenAI 和 Anthropic，以及可能采用的[自托管模型](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/)。

## Token 规则：解读全新定价

告别可预测的统一费率定价，势必会在用户中引发一波焦虑，因为他们突然需要去考虑以前从未关心过的事情。在这种情况下，这个“事情”就是 Token——对于许多开发团队来说，现在是时候去了解它们究竟是什么了。

然而，这种焦虑已经开始在现实中蔓延。在 Reddit 上，一些用户将这一改变定性为典型的“诱导转向”（bait-and-switch）——一位 Pro+ 订阅者声称，在同样的使用情况下，他们的预计账单从 39 美元暴涨到了 847 美元。

“我注册的是一款无限量订阅产品，”该[用户写道](https://www.reddit.com/r/github/comments/1ttcpw0/github_copilots_new_creditbased_pricing_is/)，“现在它变成了按需付费，而那份‘慷慨’的配额大概只够应付 2 天的正常工作。这不是我付钱买的产品。”

另一些人则表现得更为务实。“GitHub 在补贴重度用户方面亏损太多了，”[一位用户](https://www.reddit.com/r/GithubCopilot/comments/1tu93g4/i_understand_now_why_github_copilot_switched_to/)写道，他声称自己仅凭一个 Prompt 就烧光了 200 个积分——而以前这些工作仅占他们 40 美元月度配额的一小部分，以前的配额能覆盖大约 1,500 次请求。

他们不得不承认，从账面上来看，GitHub 的决定很难反驳。

那么大家到底是在为什么付费？Token 是 AI 模型处理文本的基本单位——大约相当于三到四个字符，或大约四分之三个单词。与 Copilot 的每一次交互都会消耗它们：输入 Token 对应您发送给模型的内容，输出 Token 对应模型返回的内容，缓存 Token 对应它在整个会话中存储和重复使用的上下文。在旧的高级请求模式下，这些对用户而言既不可见也毫无关联。但在新模式下，它直接决定了你的账单。

关键在于，并非所有模型的成本都相同。GitHub 已经[公布](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)了 Copilot 中所有可用模型的完整按 Token 定价细则——且差异巨大。在 OpenAI 方面，GPT-5 mini 是一个轻量级选择，价格为每百万输入 Token 0.25 美元，而 [GPT-5.5](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/)（一款更强大的模型）则达到每百万输入 Token 5.00 美元，价格是前者的 20 倍。

在 Anthropic 方面，[Claude Haiku 4.5](https://thenewstack.io/anthropic-launches-claude-haiku-4-5/) 的价格为每百万输入 Token 1.00 美元，而[最新发布的 Claude Opus 4.8](https://thenewstack.io/claude-opus-48-release/)（专为繁重任务打造）则为每百万输入 Token 5.00 美元。简单来说，现在选择哪种模型会直接且显着地影响团队的开销——不再可能对所有任务都无脑选用最强大的模型而不用承担额外成本。

好消息是，团队可以针对不同任务选择所使用的模型，并且 Copilot 还提供了一种自动模式，可以根据当前的工作将请求路由到最合适的模型。对于简单的查询，这可能意味着使用较便宜的轻量级模型。而对于复杂的、多步骤的智能体工作，它可能会指向能力更强、同时也更昂贵的模型。

熟悉定价表，并思考某项具体工作究竟需要哪种模型，将成为未来管理 Copilot 开支的重要一环。