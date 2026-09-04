AI 编程公司 [Replit](https://replit.com/) 正在通过将其“智能模型路由”系统设为所有账户的默认配置，来全力支持模型路由这一趋势。

该系统会随着任务的演进，自动选择应处理任务的底层模型，Replit 在路由决策时会权衡质量、速度和成本。

该公司表示，这项被称为 [Auto mode](https://docs.replit.com/chat/auto-mode) 的功能将成为所有用户的默认选项，不过 [Core 和 Pro 订阅者](https://replit.com/pricing)在需要更多控制权时，仍然可以覆盖该设置并手动选择模型。

## 模型路由的发展势头

此公告发布之前，模型路由领域出现了一阵[活动热潮](https://thenewstack.io/cursor-ramp-meta-model-router/)。8 月初，据报道 [Stripe 同意收购](https://thenewstack.io/stripe-acquires-openrouter-tokens/)模型网关平台 OpenRouter，交易额为 80 亿美元；就在同一天，[Ramp 推出了 Router.com](https://www.prnewswire.com/news-releases/ramp-launches-routercom-to-cut-companies-rising-ai-bills-302855572.html)，该平台将请求路由至满足特定性能标准且成本最低的模型。

在此之前，SpaceX 旗下的 Cursor 于 7 月[推出了自己的路由器](https://cursor.com/blog/router)，它能为编码请求自动选择模型，并声称能在大幅降低成本的同时提供相当的性能。与此同时，据报道 [Meta 正在开发](https://www.theinformation.com/articles/metas-ai-incubator-developing-openrouter-rival-cut-coding-costs)一个名为“Switchboard”的内部路由器，它通过难度对编码任务进行评分，并将更简单的任务发送给更便宜的模型。

> “在同一个模型系列中，每 token 的费率可以相差几个数量级。与此同时，更便宜、更小的模型的智能水平现在已非常接近其更大的前沿模型，这为我们的成本优化提供了很大的空间。”

Replit 总裁兼 AI 主管 [Michele Catasta](https://www.linkedin.com/in/pirroh/) 表示，推动路由广泛应用的一个原因是简单的经济学逻辑——模型成本与开发者针对特定任务实际所需的性能水平之间的差距日益扩大。

“在同一个模型系列中，每 token 的费率可以相差几个数量级，”Catasta 告诉 *The New Stack*。“与此同时，更便宜、更小的模型的智能水平现在已非常接近其更大的前沿模型，这为我们的成本优化提供了很大的空间。”

Replit 本身已经在朝着这个方向努力了一段时间。Catasta 说，公司最近几个月一直在试验 Auto mode 的早期版本、子代理（subagent）路由以及多次迭代。

“像任何关键的发布一样，我们在向公众发布之前，已经在测试阶段对智能模型路由进行了长时间的全面测试，”他说。“最重要的经验是根据第一性原理理解每一次实验的失效模式，这样我们就能在我们刚刚发布最终系统时不断提升性能。”

## 引入 Auto mode

这项工作的成果于上周显现，当时 [Replit 推出了 Free Mode](https://replit.com/blog/replit-introduces-free-mode)，这是一种成本更低的 Agent 模式，不消耗使用点数，并使用 Auto 代表用户选择模型，但需遵守使用限制。

现在，同样的 Auto 路由方法正在 Replit 更广泛地推广。该公司表示，智能模型路由将成为每个账户的默认设置，所有用户从 Free Mode 开始，由 Replit 决定最适合该任务的模型。

值得注意的是，Free Mode 并不是指“无限使用”意义上的免费。在发布时，Replit 向 Core 和 Pro 订阅者提供该功能且不消耗其使用点数，但实施了每五小时重置一次的限制，Pro 用户享有更高的配额。在 Free Mode 下，用户无法手动选择模型。

不过，Core 和 Pro 订阅者可以切换到 Replit 的 Power 或 Max 模式，在那里他们可以关闭 Auto 并自行选择模型。当 Replit 确定需要更强能力时，也可能会建议将任务移动到这些更高级的模式中，尽管这些模式可能会产生使用成本。

![Auto Mode in Replit](https://cdn.thenewstack.io/media/2026/08/a4ac5fa0-replit-router-1024x476.png)

*Replit 中的 Auto mode*

与此同时，对于企业客户，管理员可以限制 Auto 在每个工作区仅使用一组已批准的模型，从而允许 Replit 在保持符合公司策略的模型选择的同时，继续自动路由任务。

## 代理优势

即使在 SpaceX 同意支付高达 [600 亿美元](https://uk.finance.yahoo.com/news/spacex-completes-record-60-billion-131413932.html)并[收购 Cursor](https://cursor.com/blog/joining-spacex) 之前，这家 AI 编程初创公司就已长期投资于自己的编码模型，包括其 [Composer 系列](https://thenewstack.io/cursors-composer-2-beats-opus/)。最近，在 SpaceX 的支持下，Cursor 也一直在[开发更尖端的模型](https://thenewstack.io/grok-4-6-agent-training/)。

相比之下，Replit 并没有将拥有底层模型层作为其核心卖点。相反，它的押注在于：控制 Agent 及其周围的系统，使 Replit 能够有足够的洞察力在运行过程中做出更好的模型选择决策。

> “从一开始，Replit 就同时拥有 Agent 框架和围绕模型的架构，这反过来使我们能够训练复杂的模型路由器。”

“从一开始，Replit 就同时拥有 Agent 框架和围绕模型的架构，这反过来使我们能够训练复杂的模型路由器，”Catasta 说。“只有这样，我们才能始终以最具竞争力的价格为用户提供有用的智能。”

随着 Agent 任务的展开，这一点变得尤为重要，Replit 指出其系统可以在任务发展过程中改变所使用的模型，在流程的不同阶段寻求能力与成本之间更好的权衡。但对于 Catasta 来说，这种动态路由仍然只是关于 Agent 应如何使用模型这一更广泛研究课题的一部分。

“模型路由仍处于早期开发阶段，我们预计进一步的研究将在客户最需要的时候提供最佳智能，”Catasta 解释道。“路由只是这块拼图中的一部分，它与我们框架研究的其他许多方面紧密集成。”

> “没有任何第三方路由器公司能为我们自己的 Agent 重现同样的结果。”

Replit 还认为，了解人们如何使用其自己的 Agent 给它带来了一个独立的路由提供商难以复制的优势。Catasta 表示，路由器必须推断请求的性质、难度、范围和意图，而 Replit 能够根据专有的使用数据进行训练，并观察其用户群中的这些信号。

“没有任何第三方路由器公司能为我们自己的 Agent 重现同样的结果，”他说。