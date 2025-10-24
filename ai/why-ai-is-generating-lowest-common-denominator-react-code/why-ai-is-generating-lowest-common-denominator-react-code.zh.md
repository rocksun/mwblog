[Seth Webster](https://www.linkedin.com/in/swebster) 不认为我们正处于一个[后 React 时代](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)——或者至少，不*仅仅*是一个后 React 时代。

新成立的[React 基金会](https://thenewstack.io/new-react-foundation-to-manage-framework/)执行董事说：“我们实际上正处于一个后前端框架时代，因为 AI 吐出的就是 React，而且没人关心它吐出的是什么。”“我们正走向一个后代码-管道的世界，我们可以更多地专注于，‘我想要创造的那些令人愉悦的部分是什么？’”

他接着说，问题是，大型语言模型并非基于*最好*的 [React](https://thenewstack.io/react-compiler-is-coming/) 代码进行训练；事实上，[LLM](https://thenewstack.io/introduction-to-llms/) 大多是基于非常糟糕的 React 进行训练的。

他[告诉 The New Stack](https://thenewstack.io/react-foundation-leader-on-whats-next-for-the-framework/)：“它们是基于最低公分母的 React 进行训练的，这就是世界上现有的情况。它们是基于最糟糕的 [Svelte](https://thenewstack.io/svelte-adds-asynchronous-sync-inside-components/) 进行训练的，它们是基于最糟糕的 [Swift](https://thenewstack.io/get-started-with-swift/) 进行训练的，因为它们训练所用的都是公开可用的代码。”“世界上最好的代码，通常隐藏在私有仓库后面，所以它们无法抓取。”

## 为什么 AI 是一个平庸的工程师

他补充说，LLM 无法访问最好的代码，也无法了解工具是如何构建的。因此，AI 更像是一个中等水平、职业生涯中期的工程师。他说，它不是你遇到过的最好的工程师，但也不是最差的。

例如，[Claude](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) 喜欢做的事情之一是在 React 中使用 refs 来跟踪状态。

“这并非我们在 React 中看到的最糟糕的模式，但它也不是一个好的模式，”Webster 说。“这基本上表明模型不理解构建这些东西的最佳方式是创建一个外部服务，然后使用钩子将其与 React 集成，而不是试图将所有业务逻辑塞进 React，而这正是世界上每个人都在做的事情，因为我们让这样做变得太容易了。”

他补充说，这是 React 维护者在 React 架构中犯的一个错误，因为“把所有东西都放到 React 中实在太简单了”——而开发者真正需要[像工程师一样思考](https://thenewstack.io/ai-engineering-what-developers-need-to-think-about-in-2024/)，并以稍微不同的方式构建业务逻辑。

“如果我使用 [Google](https://thenewstack.io/googles-gemini-cli-agent-comes-to-zed/) 或 [GitHub](https://thenewstack.io/github-will-prioritize-migrating-to-azure-over-feature-development/) 等进行身份验证，我应该有单独的服务来处理，”Webster 说。“我应该有一个授权服务，它与我用于不同事物的不同提供商集成。它负责告诉 React 应用程序何时有人登录等等，何时他们的身份验证令牌过期，或者其他任何事情。

“那应该通过钩子集成。你不应该把它放在你的组件中，而模型读取的代码都塞进了业务逻辑中，因为它默认不创建服务。”

## 改善 LLM 的 React 输出是一个目标

他希望作为 React 基金会负责人实现的目标之一是改进流行的[大型语言模型生成的](https://thenewstack.io/better-llm-agent-quality-through-code-generation-and-rag/) React 代码。

他说，这意味着[模型上下文协议（MCP）服务器](https://thenewstack.io/10-mcp-servers-for-frontend-developers/)和[评估](https://thenewstack.io/where-ai-benchmarks-fall-short-and-how-to-evaluate-models-instead/)的结合。根据全球咨询公司 [Thoughtworks](https://www.thoughtworks.com/en-us/insights/decoder/a/ai-evals) 的说法，评估用于根据预定义的指标和业务目标系统地评估 LLM 的准确性和可靠性。他表示，[评估有助于 AI](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/) 实现其“预期目的”。

在那之前，Webster 说，[AI 需要开发者的帮助](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/)才能使代码正确：“它需要大量的指导，而且在未来一段时间内都会如此。”