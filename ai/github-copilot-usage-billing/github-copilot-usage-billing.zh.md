传言属实：GitHub 今天宣布，将彻底改革 Copilot 的收费方式，转向基于用量的计费模式，将成本直接与开发者对 AI 编码工具的使用情况挂钩。

这一变化定于 6 月 1 日生效，Copilot 的订阅计划将保持不变，但会更换负责管理用量的内部系统。目前，Copilot 采用固定月费与所谓的“溢价请求”单元（一种限制访问高级聊天或长时间运行任务等高算力功能的配额）相结合的模式，但并未将这些功能与成本直接挂钩。

该系统将被一种与 Token 消耗相关的基于点数的模式所取代。每个方案都将包含每月的 GitHub AI 点数配额，在点数耗尽后，用户可以选择为额外的用量支付费用。

在周一发布的一篇[博客文章](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)中，GitHub 首席产品官 [Mario Rodriguez](https://www.linkedin.com/in/mariorodriguez3/) 写道，这一变化旨在创建一个更“可持续”的定价模型。

“这一变化使 Copilot 的定价与实际用量保持一致，是迈向可持续、可靠的 Copilot 业务以及为所有用户提供优质体验的重要一步，”Rodriguez 解释道。

> 这一变化使 Copilot 的定价与实际用量保持一致，是迈向可持续、可靠的 Copilot 业务以及为所有用户提供优质体验的重要一步。

此前，GitHub 已采取一系列措施来管理需求，包括停止 [Copilot Pro 免费试用](https://github.blog/changelog/2026-04-10-pausing-new-github-copilot-pro-trials/)、暂停[部分 Copilot 方案的新用户注册](https://thenewstack.io/github-copilot-signups-paused/)，以及收紧现有用户的用量限制。[上周也有传闻称](https://www.wheresyoured.at/news-microsoft-to-shift-github-copilot-users-to-token-based-billing-reduce-rate-limits-2/)，这些变化是在为 GitHub 转向基于 Token 的计费模式铺平道路。

GitHub 并不是唯一一家应对这些压力的公司。Anthropic 最近几周也[调整了](https://x.com/trq212/status/2037254607001559305)其 Claude 模型的限制应用方式，在高峰时段重新分配用量，导致[部分用户更早达到上限](https://thenewstack.io/claude-code-usage-limits/)。该公司还采取措施限制订阅如何应用于 [OpenClaw 等第三方工具](https://thenewstack.io/persistent-ai-agents-compared/)，通过这些集成产生的用量现在需要单独计费。

总的来说，这些变化反映了 AI 编码服务面临的压力日益增大，因为使用场景正转向更长、算力更密集的对话，迫使公司重新思考如何对访问权进行定价和管理。

## 拆解变化内容

自 [2021 年推出](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)以来，Copilot 主要作为固定价格的订阅服务销售，开发者支付月费即可获得 AI 辅助编码支持。

在新的模式下，用量将根据 Token（涵盖输入、输出和缓存数据）进行计算，并使用与特定模型挂钩的费率。

GitHub 表示，这种转变反映了 Copilot 现在处理的是跨项目的长流程、多步骤编码工作，而不再仅仅是编辑器内短促的辅助。

“Copilot 已不再是一年前的那个产品了，”Rodriguez 写道。“它已经从编辑器内的助手进化为一个能够运行长流程、多步骤编码任务，使用最新模型并能在整个代码库中进行迭代的智能体平台。智能体化（Agentic）的使用正在成为默认方式，这带来了显著更高的算力和推理需求。”

> Copilot 已不再是一年前的那个产品了。

深入探究细节发现，所有级别的基础方案定价保持不变，代码补全和 Next Edit 建议等核心功能将继续包含在内，不消耗点数。后备系统也将被移除，这意味着达到限制的用户将不再被切换到低成本模型。Copilot 代码审查现在将结合 GitHub Actions 分钟数和 AI 点数，将用量更直接地与现有的计算计费挂钩。

值得注意的是，这些变化同时适用于个人和商业 Copilot 方案。

对于个人用户，Copilot Pro 和 Pro+ 现在将包含与各方案成本挂钩的每月 AI 点数配额。Pro 用户每月将获得 10 美元的点数，而 Pro+ 用户将获得 39 美元。年度方案的用户将维持现有系统直到订阅结束，届时他们将转入新的月度模式，也可以选择提前转换并获得按比例计算的点数。

对于商业和企业客户，席位单价保持不变。Copilot Business 仍为每用户每月 19 美元，Enterprise 为每用户每月 39 美元，每个级别都会获得相应金额的每月点数。

GitHub 还为组织引入了池化用量，允许一名用户未使用的点数在团队内共享。管理员将能够在不同层面设置支出限额，包括针对单个用户或整个组织，并决定在达到限额后是否允许额外用量。

为了缓解过渡压力，GitHub 将在夏季为商业和企业客户提供更高的点数配额，让团队在系统全面实施前有时间进行调整。管理员还可以在从个人用户到整个组织的各个层面设置支出限制，并选择在达到限制后是允许产生额外费用还是直接切断使用。

这些控制措施旨在让团队能够在固定费用难以消化高强度工作负载的新模式下，管理好用量如何转化为成本。

“基于用量的计费解决了这个问题，”Rodriguez 解释道。“它使定价更好地与实际使用情况保持一致，帮助我们维持长期的服务可靠性，并减少了限制重度用户的需要。”