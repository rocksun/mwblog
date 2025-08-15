在一篇[向开发者介绍 GPT-5 的文章](https://openai.com/index/introducing-gpt-5-for-developers/)中，OpenAI 声称新模型“擅长前端编码，在内部测试中，前端 Web 开发方面击败 OpenAI o3 的几率高达 70%。” OpenAI 的开发者体验负责人 Romain Huet 在 [X 上补充道](https://x.com/romainhuet/status/1953964802432500186)，GPT-5“在前端开发方面非常出色”。此外，还有来自知名前端基础设施公司（如 Vercel）的支持，他们称 GPT-5 为“最佳前端 AI 模型”。

但是，正如互联网上常见的情况一样，您的体验可能会有所不同。似乎也包括那些 OpenAI 曾经用来宣传 GPT-5 发布的人。Theo Browne 是一位知名的 YouTube 影响者，他出现在 [OpenAI 发布日的视频之一中](https://x.com/OpenAIDevs/status/1953535155789865423)。Browne 最初非常喜欢 GPT-5，甚至说 Claude Sonnet 和其他竞争对手“因为 GPT-5 的编码能力，[今天已经不再重要了](https://x.com/theo/status/1953516806104056096)”。然而，今天他的态度发生了 180 度大转变。他现在发布了一个名为“[我对 GPT-5 的看法是错误的](https://www.youtube.com/watch?v=k68ie2GcEc4)”的视频。在视频中，Browne 声称“我现在使用 GPT-5 的体验比我之前测试它时的体验要差很多”。他[在 X 上补充道](https://x.com/theo/status/1955766271083209064)，“gpt-5 在 Cursor 中的表现远不如几周前我使用它时那么好”。

[![Theo Browne 对 GPT-5 的道歉。](https://cdn.thenewstack.io/media/2025/08/fce309f1-gpt5-theo.jpg)](https://cdn.thenewstack.io/media/2025/08/fce309f1-gpt5-theo.jpg)

Theo Browne 对 GPT-5 的道歉。

对于其他非 OpenAI 雇员或附属人员来说，使用 GPT-5 进行编码的体验也未必是积极的。一位 GitHub Copilot 用户[抱怨道](https://github.com/orgs/community/discussions/168107#discussioncomment-14073879)，GitHub Copilot Pro 中的 GPT-5“对其所做的事情给出了非常薄弱的总结或解释”，总体而言，他发现它“非常令人失望”。他补充说，Claude Sonnet 4 “远胜一筹”。

AI 工程专家 Shawn Wang (又名 swyx) 在 GPT-5 发布后的第二天在 X 上发起了一项[氛围编程调查](https://x.com/swyx/status/1953619552581169543)，超过 40% 的人表示“一般般”或“垃圾”。当然，这并不科学，但它确实表明 OpenAI 的宣传攻势过度美化了 GPT-5 的编码能力。（顺便说一句，Wang 是 OpenAI 在其发布日编程中重点介绍的另一位开发者。）

[![Swyx 调查](https://cdn.thenewstack.io/media/2025/08/20db0cb2-screenshot-2025-08-14-at-11.48.57.png)](https://cdn.thenewstack.io/media/2025/08/20db0cb2-screenshot-2025-08-14-at-11.48.57.png)

也有一些有趣的反应。在 X 上，AI 开发者 Kevin Kern [开玩笑说](https://x.com/kregenrek/status/1953507608456831029) GPT-5 偏爱紫色——暗示 GPT-5 产生的用于前端设计并非那么原创。

[![紫色问题](https://cdn.thenewstack.io/media/2025/08/6ef1d850-screenshot-2025-08-14-at-12.17.17.png)](https://cdn.thenewstack.io/media/2025/08/6ef1d850-screenshot-2025-08-14-at-12.17.17.png)

## React 还是 No React？ 你来选择！

具体到前端开发而言，OpenAI 似乎在其“cookbook”[提示指南](https://cookbook.openai.com/examples/gpt-5/gpt-5_frontend)中给了其推广合作伙伴 Vercel 一些好处。它建议使用 Next.js (TypeScript)、React 和 HTML 作为与 GPT-5 一起使用的框架。

许多有抱负的 AI 开发者无疑会要求 GPT-5 帮助他们创建 React 应用程序。这是 [Brice Challamel 的一个例子](https://www.linkedin.com/posts/bricechallamel_ai-gpt5-gpt5-activity-7359280792671252480-tB1D?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAAJc5gB1iiLngl5c8J7iqyPa5uC2oX1J-U)，他的日常工作是 Moderna 的 AI 产品和创新主管。Challamel 决定构建一个“文化发现”应用程序。“GPT-5 帮助我从概念到在 ChatGPT 中获得可用的 React 原型，”他写道，“然后生成完整的堆栈代码包和一个在 Lovable 中部署的提示。”

> “GPT-5 帮助我从概念到在 ChatGPT 中获得可用的 React 原型。”
> **– Brice Challamel, Moderna 的 AI 产品和创新主管**

但 GPT-5 一个有趣的可能之处在于，它也可能使开发者能够*绕过* React。至少这是我从 Ben Hylak 和 Alexis Gauba (一家名为 Raindrop 的 AI 创业公司的联合创始人) 撰写的 [GPT-5 评论](https://www.latent.space/p/gpt-5-review) 中得出的结论（Hylak 在发布日加入了 Browne 和 Swyx 在 OpenAI 开发者席上）。在他的发布前测试中，Hylak 发现他可以使用 GPT-5 创建一个网站，该网站“没有 React、没有捆绑、没有框架”。只有 HTML、CSS 和 JavaScript。

这对组合 GPT-5 一次性创建网站的能力也印象深刻。或者正如 Hylak 所说，“GPT-5 一次性完成的事情，是我以前从未见过的模型可以做到的。”

这就提出了一个有趣的问题：当 GPT-5（以及像 Claude Code 这样的竞争产品）仅通过使用底层 Web 平台就可以开发出一个骨架应用程序时，前端开发者是否还需要使用 React 及其框架来支撑他们的工作？因为这基本上就是 GPT-5 所带来的：为人类开发者“搭建”一个 Web 应用程序的能力，然后人类开发者可以在他们的 IDE 或 Cursor 或 Lovable 等工具中，在该脚手架的基础上进行构建——对其进行润色并发布应用程序。

> 如果我们不再需要 React 作为支撑呢？

换句话说：对于当今许多前端开发者来说，React 和类似的框架一直是他们职业生涯中不变的支撑。许多年轻的前端开发者甚至不知道 [没有 React 框架的世界](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/)。但是，如果我们不再需要 React 作为支撑呢？

好吧，诚然，那是因为我们正在采用一种新的支撑，即 AI 的形式。但关键是，Web 浏览器现在已经达到了 [一定的成熟度](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)，您可以使用 [HTML、CSS 和 JavaScript](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/) 构建复杂的网站和 Web 应用程序。GPT-5 可能已经向许多开发者证明，如今 React 和框架并非总是必需的（当然，这取决于 GPT-5 是否真的像 OpenAI 声称的那么好——这一点目前仍有争议）。

## 开发者关于 GPT-5 的其他注意事项

如上所述，到目前为止，我们已经看到了对 GPT-5 作为前端工具的褒贬不一的评价。但是，前端开发者需要时间才能对其进行适当的评估，尤其是与 Claude Sonnet 相比。但是，正如 Theo Browne 所评论的那样，在过去的一周中，很明显 GPT-5 的不同模型存在差异，以及它们如何集成到某些工具中。

上面引用的 GitHub Pilot 用户可能正在使用功能较弱的 GPT-5 版本，就像 [Hylak 在此处抱怨](https://x.com/benhylak/status/1955460174703104290) Cursor 所谓的“gpt-5”一样。

[![Hylak 关于 Cursor 和 GPT-5 的推文](https://cdn.thenewstack.io/media/2025/08/ab069e71-screenshot-2025-08-14-at-12.23.29.png)](https://cdn.thenewstack.io/media/2025/08/ab069e71-screenshot-2025-08-14-at-12.23.29.png)

正如 Hylak 在该 X 帖子中进一步解释的那样，“gpt-5-high 是我预发布时测试的版本”（换句话说，OpenAI 给了他顶级版本进行测试）。看来，对于非高级版本的 GPT-5，前端编码结果可能不太令人满意。

还值得指出的是，编码 LLM 似乎都具有不同的风格——或者像代码安全公司 [Sonar](https://www.sonarsource.com/%20?utm_content=inline+mention) 在本周发布的 [一项新研究](https://www.sonarsource.com/resources/the-coding-personalities-of-leading-llms/) 中所说的那样，具有不同的“编码个性”。Sonar 的研究称 GPT-4o 为“高效的通才”，Claude Sonnet 4 为“高级架构师”。

[![Sonar 编码个性](https://cdn.thenewstack.io/media/2025/08/fb8ede7f-screenshot-2025-08-14-at-12.20.52.png)](https://cdn.thenewstack.io/media/2025/08/fb8ede7f-screenshot-2025-08-14-at-12.20.52.png)

现在说 GPT-5 具有什么样的编码个性还为时过早，但这是前端开发者将热衷于跟踪的事情。