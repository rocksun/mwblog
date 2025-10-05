似乎有一个潜在的假设，即代理式网络 (agentic web) 的最佳语言是 JavaScript。 [Elixir](https://github.com/chrismccord) 开发者 Chris McCord 对此不以为然。

McCord 是基于 [Elixir](https://thenewstack.io/elixir-an-alternative-to-javascript-based-web-development/) 的 [Phoenix Web 框架](https://www.phoenixframework.org/) 的创建者，并在去年 9 月的 [ElixirConf US 2025](https://elixirconf.com/) 上发表了演讲，该演讲最近已在 [YouTube](https://www.youtube.com/watch?v=6fj2u6Vm42E) 上发布。为了证明他的观点，他通过启动一个 AI 代理来创建 Slack 克隆程序开始了他的演讲，该程序使用 [Phoenix](https://github.com/phoenixframework/phoenix) 并在项目中包含一个 Agents.md 文件。

“Agents.md 只是一个扁平的 Markdown 文件，这并不是文档，”他说。“[Agents.md 是为 LLM](https://github.com/openai/agents.md) 设计的，而不是为人类设计的。”

McCord 说，他注意到前沿模型在使用 Elixir 时往往会在几个方面出现问题。为了解决这个问题，他编写了一个定制的 [AGENT.md 文件](https://github.com/phoenixframework/phoenix/commit/50ffaa5aa1c60503f01cd2107edd43f22435f9e7)，以教 AI 编写正确、地道的 Elixir 代码，并警示常见错误，例如 [大型语言模型 (LLM)](https://thenewstack.io/taming-llm-sprawl-why-enterprises-need-an-ai-gateway-now/) 倾向于使用基于索引的列表访问。

“实际上，这只是为了弥补代理所做的愚蠢事情，比如尝试进行基于列表索引的访问，”他谈到 AGENTS.md 文件时说。“AGENTS.md 是我通过消耗大量 token 换来的经验教训。在 [Phoenix.new](https://phoenix.new/) 产品中，它现在已存在于每个项目的初始设置中。”

该文件还通过为代理提供一个一致的架构起点来提供上下文，以确保 AI 生成的代码符合 Phoenix 的约定。他认为，当与 AGENT.md 结合使用时，Elixir 是最适合作为 [代理式 AI 世界](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/) 前端语言的。

## 关于 AI 代理的一些背景信息

McCord 说：“你之所以一直听到关于代理式编码、代理式工作流程的讨论，是因为人们将这些聊天机器人放入循环中，它们实际上可以在现实世界中完成真实的任务，而且完成得非常出色。”“我们正处于它们的能力以及它们能持续工作多久的 [摩尔定律](https://newsroom.intel.com/press-kit/moores-law) 阶段。”

他表示，研究表明代理的任务链接能力每七个月翻一番。

“这意味着，我可以把 [Claude Code](https://thenewstack.io/claude-code-user-base-grows-300-as-anthropic-laundoes-enterprise-analytics-dashboard/)、[Gemini CLI](https://thenewstack.io/googles-gemini-cli-agent-comes-to-github/)，或者任何我想要的 LLM，放到一个循环中，让它执行一项任务，而它在不偏离轨道的情况下实际完成该任务的时间每七个月就会翻一番，”他说。“在不到一年的时间里，我们正经历这种二次方增长。”

他说，即使这种增长趋于平稳，Elixir 也已经突破了一个“有用的价值阈值，即上下文窗口足够大”，LLM 可以在足够长的时间内保持在正轨上，并折叠其窗口但继续解决问题。

> “对我们来说，真正重要的是 Elixir 可以主导这个领域。基本上，现在是我们利用代理构建和创建代理的时候了，而 Elixir 恰好是实现这一目标的完美语言。”
> **—— Chris McCord，Phoenix 框架的创建者**

他补充说，例如，新的 Phoenix 代理可以自行折叠其上下文窗口但仍继续工作。

“它可以在不必要地说‘开始新的聊天，因为我现在脑子里东西太多了’的情况下解决这些长期问题，”McCord 说。“它可以自我总结并继续工作。”

他说，这也意味着开始任务和结束任务之间的时间正在变长。我们正在从简单的聊天体验转向更像是助手，用户可以告诉 LLM 去执行操作，然后发现它确实完成了该操作。

## AI 代理加入劳动力大军

尽管 McCord 建议大家在面对 AI 炒作时要持保留态度，但他也认为许多炒作可能会成为现实——并且会超出编程的早期采用领域。

McCord 指出，OpenAI 首席执行官 [Sam Altman](https://thenewstack.io/openais-sam-altman-sees-a-future-with-a-collective-superintelligence/) 因表示 2025 年将把 [首批 AI 代理引入劳动力市场](https://www.axios.com/2025/01/10/ai-agents-sam-altman-workers) 并将实质性改变公司的产出而受到诸多批评。McCord 说，虽然许多人认为这意味着它将取代所有工作，但如果你仔细想想，Altman 并没有说错。

“他因此受到了很多批评，但有趣的是，今天在座的开发者中，可能有人每天都在使用 [Claude code](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) 或其他编码代理，他们读到这个声明时可能会嗤之以鼻，”他说。“与此同时，他们正在使用一个已经加入他们公司的 AI 代理，该代理正在实质性地改变他们公司的产出。所以我认为这个声明至少在科技公司领域是真实的。”

McCord 说，AI 正在为人们做数小时的独立工作，其水平与专家相当，这正在扩大团队中每个人的能力。

“这是我的亲身经历，”他说。“我每周会消耗数小时的 token，这正在实质性地改变我个人以及公司内部的产出。”

但 AI 公司正在预测更多的进步。例如，[Anthropic 预测](https://ai-2027.com/) 我们很快会看到突破性的解决方案，而这些解决方案若没有 AI，将需要数年才能完成。

McCord 说，无论哪种情况是真实的——AI 的能力正在缓慢减弱，或者我们只是看到了它力量的开始——这对 Elixir 来说都是一个机会。

“对我们来说，真正重要的是 Elixir 可以主导这个领域，”他说。“基本上，现在是我们 [利用代理构建](https://thenewstack.io/dont-build-chatbots-build-agents-with-jobs/) 和创建代理的时候了，而 Elixir 恰好是实现这一目标的完美语言。”

## 偶然的 AI 天才

McCord 指出，Erlang 及其为 Elixir 提供支持的 [虚拟机 BEAM](https://elixirforum.com/t/what-does-beam-have-to-do-with-erlang/50775)，“在多核技术发明之前，意外地创造了适合多核的完美语言。”

“他们在互联网出现之前，意外地创造了适用于现代互联网的完美语言；他们在 [LLM 尚未盛行](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/) 的代理时代之前，意外地创造了完美的语言和虚拟机，”McCord 说。“这就像我们不断地发现这些偶然……完美地契合了编程和计算的现代问题的事物。”

他表示，同样，Elixir“完美地适合真正主导”代理式 AI。

“如果你回顾我们的历史，我们一直致力于站在技术前沿，实现我们的目标，”McCord 说。“我们一直致力于构建我们想要构建的东西，构建我们想要看到的未来。”

他补充道：“而我们一直想构建的，至少对我来说，是服务器、多人游戏、可扩展到数百万用户的协作聊天应用程序。”“我们拥有完美的平台来做到这一点。所以，我们做到了。”

> “这就像我们不断地发现这些偶然……完美地契合了编程和计算的现代问题的事物。”
> **—— McCord**

那么 Elixir 如何帮助 LLM 呢？“我们在 gen server 上内存中维护一个系统索引，我们监控客户端的文件系统，并将每个文件更改连同文件内容发送到服务器，”他说。“在任何时候，LM 都拥有代码库中工作文件的当前视图。”

McCord 说，Elixir 已准备好处理其他人仍在努力解决的 LLM 问题，例如临时缓存和垃圾回收。

“其他人在使用代理时必然需要解决的所有这些问题……对我们来说根本不是问题。我们甚至没有意识到它们是问题，”他说。“我们只是编写一些微不足道的东西，它就能工作。”

问题是，LLM 是在互联网上训练的，而互联网上的大多数代码是 JavaScript。因此 LLM 倾向于用 JavaScript 编写应用程序。这导致 Elixir 社区中出现负面看法，认为 Elixir 将被淘汰；他对此提出了警告。相反，他说，观点应该是任何人都可以在 LLM 的支持下使用 Elixir 或 Phoenix。

他指出 Elixir 生态系统拥有统一的工具。这使得 Elixir 在 AI 时代具有巨大的优势，特别是与 JavaScript 等碎片化的生态系统相比。他指出，Elixir 致力于开发者优先，但这也有利于 LLM。

“除了 [Go](https://thenewstack.io/go-experts-i-dont-want-to-maintain-ai-generated-code/) 之外，我们可能是少数几个拥有这种非碎片化、连贯体验的平台之一，因为我们有 Mix，你的构建工具，”他说。“Phoenix 的所有新功能，我们总是在思考如何最好地服务于 LLM。但通过最好地服务于 LLM，我们实际上是在服务于使用这些大型语言模型工具的开发者。”

社区的重点应该是为每个人提供最佳的 LLM 体验。为此，Elixir 推出了 [Tideway Web](https://tidewave.ai/)，这是一种专门的 AI 编码代理，专为 Ruby on Rails 和 Phoenix/Elixir 生态系统中的全栈开发而设计。他说，它在浏览器中运行，可用于**氛围编程**。

还有 Phoenix.New，一个用于 Phoenix 的远程 AI 运行时，提供低代码应用程序选项。

“一个不是程序员的人也可以进来请求一个应用程序，他们可以在浏览器中拥有一个编辑器，但他们实际上不需要知道自己在做什么，他们就可以真正进入 Phoenix，”他说。“他们可以拥有一个可运行的应用程序，可以尝试运行，然后在电脑上克隆。”

McCord 认为，Elixir 统一的工具和语言设计使其成为代理式 AI 的完美平台：“核心理念是为人们提供使用这些编码代理的最佳体验。”