**微软在 AI 编程热潮的初期阶段**，大力推动其工程师使用相关工具。现在，微软想了解所有这些 token 是否产生了任何有价值的成果。

该公司已为其各个部门引入了 AI token 预算，像管理其他昂贵的计算资源一样来管理编程。它为员工提供了监控个人支出情况的方法，并指示工程师使用 OpenAI 的 GPT-5.6 Sol 作为 GitHub Copilot 中的默认模型。

“随着我们加快使用 GitHub Copilot 来实现我们的目标，我们都需要意识到我们是如何消耗 token 的，”微软执行副总裁 [Jay Parikh](https://www.linkedin.com/in/jayparikh) 在一封内部电子邮件中写道，该邮件由 404 Media 首次[报道](https://www.404media.co/microsoft-tells-engineers-tokenmaxxing-is-not-what-we-are-optimizing-for/)。

“我们优化的目标不是‘token 最大化’(Tokenmaxxing)，” Parikh 在备忘录中继续说道，“我希望我们所有人都能专注于最大化那些能为客户和我们的业务带来实质性改变的成果。”

> “我们优化的目标不是‘token 最大化’。我希望我们所有人都能专注于最大化那些能为客户和我们的业务带来实质性改变的成果。”

微软向 [CNBC](https://www.cnbc.com/2026/08/05/microsoft-makes-openai-gpt-5point6-sol-default-in-github-copilot-for-staff.html) 证实了这些变化。内部 Copilot 指南显示，自 7 月以来，微软的每个部门都有一个“AI token 预算目标”。员工可以追踪个人的支出，而微软的数据显示，许多工程师每月消耗的 token 价值从数百美元到数千美元不等。

该公司尚未公布这些预算的具体规模，也未表示工程师在达到预算后会自动失去访问权限。不过，这些准则留出了更严格控制的空间，并警告称，随着微软对支出的监控，各个部门可能会引入进一步的限制。

“因此，我们正在更新内部指导方针，并以我们对待其他每一项关键资源同样的纪律来管理 token 支出，” Parikh 写道。

## GPT-5.6 Sol 现在是默认模型

微软决定将 GPT-5.6 Sol 作为默认模型，这使得“这仅仅是一次削减成本的行动”这种说法变得复杂起来。即便它的成本确实低于微软之前使用的一些模型，但它仍然是 OpenAI GPT-5.6 系列中最昂贵的模型。OpenAI 对 Sol 收取的费用为每百万输入 token 5 美元，每百万输出 token 30 美元。继 7 月 30 日[宣布降价](https://thenewstack.io/gpt-5-6-api-price-cuts/)后，Terra 的价格分别为 2 美元和 12 美元，而 Luna 则分别为 0.20 美元和 1.20 美元。

所以现在不仅关乎哪个模型在基准测试中名列前茅；团队必须弄清楚[每一项工作适合哪种模型，以及额外的能力是否真的物有所值](https://thenewstack.io/agentic-ai-token-costs/)。

Parikh 在邮件中明确了这种区别：“我们优化的不是更少的 token。我们优化的是每个 token 更高的影响力。”

> “我们优化的不是更少的 token。我们优化的是每个 token 更高的影响力。”

## 默认设置开始起到 AI 使用护栏的作用

GitHub 在自动模型选择方面一直在向不同的方向发展。Copilot 可以根据任务、用户订阅和管理员设置的策略，将请求路由到多个模型系列。GitHub 表示，该功能绕过了自然的缓存边界，以避免不必要的成本，其评估显示，在[不降低质量的情况下，token 效率得到了提高。](https://github.blog/changelog/2026-07-01-copilot-cli-auto-model-selection-routes-based-on-task/)

据 CNBC 报道，Copilot 的自动选择有时会将微软员工引导至 [Anthropic 模型](https://thenewstack.io/opus-5-agentic-coding-cost/)。将 Sol 设置为默认值使微软对其内部 token 支出的流向有了更大的控制权，同时员工在需要时仍能访问其他模型。

该公司此前已开始整合其内部编程栈。据 [*The Verge*](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad) 报道，5 月份，微软开始取消其体验与设备部门的大部分 Claude Code 许可证，并指示工程师在 6 月 30 日之前转用 GitHub Copilot CLI。Claude 模型仍然可以通过 Copilot 使用，但让工程师使用[微软自己的工具](https://thenewstack.io/microsoft-mistral-sovereign-ai/)使公司能够更好地控制访问策略、模型选择和使用数据。

## Token 成本增长超过了生产力衡量标准

微软有一些证据表明，编程智能体（Agents）可以提高开发人员的产出。微软研究人员的一项[研究](https://arxiv.org/abs/2607.01418?)考察了 Claude Code 和 GitHub Copilot CLI 在数万名工程师中的推广情况，结果显示，采用这些工具的工程师合并的拉取请求（pull requests）比研究人员估计的在四个月研究期间若不使用该工具多出约 24%。

这些发现给了微软在编程智能体上投入资金的理由，但合并的拉取请求只是衡量产出的一个代理指标。该研究并未确定额外的代码是否减少了 bug、提高了安全性、节省了开发人员的时间，或是为客户提供了更多价值。一个团队可以在[不生产出更好产品](https://thenewstack.io/meta-metacode-engineer-training/)的情况下合并更多的代码。

## 智能体放大了支出问题

随着编程工具超越“自动完成”阶段，挑战也随之增加。例如，[智能体现在可以探索代码库、制定实施计划、运行命令、执行测试并修改自己的工作。](https://thenewstack.io/openai-codex-cloud-evolution/)每一步都会在账单中增加更多的上下文和输出 token。一个反复读取大型代码库或采取不成功方法的智能体，在开发人员干预之前可能会消耗大量的 token。

GitHub 于 6 月 1 日将 Copilot 转为基于使用量的计费模式，并为组织引入了用户级预算控制。管理员可以设置通用预算或调整特定员工的限制。GitHub 在宣布新的 Copilot 计划时表示，更长的智能体运行时间、多步骤任务和能力更强的模型正在给包含的使用量带来压力。该公司于 6 月 1 日启用了基于使用量的计费和用户级控制。

> 一个反复读取大型代码库或采取不成功方法的智能体，在开发人员干预之前可能会消耗大量的 token。

## 全行业范围内的控制措施正在兴起

微软并不是第一家发现“鼓励员工消耗更多 AI”并不能保证生产力同步增长的公司。

据报道，在迅速采用 Claude Code 和 Cursor 等工具后，Uber 在今年前四个月就耗尽了其 2026 年全年的 AI 编程预算。此后，该公司开始专注于更便宜的默认模型、提示缓存，并提高对员工支出的可见性。

亚马逊遇到了该问题的另一个版本。一个旨在将作者记录与产品列表进行匹配的内部 Claude Sonnet 项目据称耗资 180 万美元，超出了计划预算的 860%。这一超支数月未被发现，且该项目从未发布。

[据基于一份亚马逊内部演示文稿的报道](https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-accidentally-spent-usd1-8-million-using-claude-for-menial-coding-task-went-860-percent-over-budget-catastrophically-expensive-coding-blunders-discovered-in-internal-amazon-ai-usage-metrics)，另外两个内部 AI 项目的超支总额达到了 675,000 美元。同样，Adobe、Atlassian 和 Citi 也正在推出各自的控制措施来遏制浪费。

整个行业似乎正在告别那个“使用更多 AI 就足以宣称取得进展”的阶段。企业现在必须证明他们投入的资金正在产生有价值的成果。