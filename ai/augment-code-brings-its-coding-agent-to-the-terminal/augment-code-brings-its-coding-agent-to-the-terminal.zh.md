目前的趋势是编码代理从IDE转移到命令行。例如，Anthropic的Claude Code、Google的Gemini CLI、OpenAI的Codex CLI以及Aider。至少到今天为止，这个群体中缺少了[Augment Code](https://www.augmentcode.com/)，该公司一直将自己定位为[面向企业的AI编码工具](https://thenewstack.io/augment-code-an-ai-coding-tool-for-real-development-work/)。作为其发布周的一部分，Augment Code今天发布了Auggie CLI编码代理。

除了本周发布的其他新功能外，还包括对其上下文引擎的更新，该引擎现在可以考虑来自分支的最后[10,000次提交](https://www.augmentcode.com/blog/announcing-context-lineage)的信息，一个将Augment Code连接到CircleCI、[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)、Redis、Sentry和Stripe等工具的[一键集成](https://www.augmentcode.com/blog/announcing-easy-mcp)，以及通过指定代理要遵循的多步骤流程来帮助指导编码代理的[任务列表](https://www.augmentcode.com/blog/how-augment-uses-tasklist)。

但这些版本中最引人注目的无疑是CLI代理，Augment Code正在对其代理采取与其他公司不同的策略。虽然该代理可以像Claude Code一样，以交互模式使用，在实现功能并获得反馈时与开发人员来回沟通，但该团队将其CLI代理定位为一种自动化工具。

Augment Code的联合创始人 Guy Gur-Ari 在今天宣布之前的一次采访中告诉我：“我们看到了Claude Code发生的一切，我们试图了解构建类似的东西对我们是否有意义，因为我们已经有了一个IDE功能。” “对我们来说，这实际上是自动化的能力，因为我们希望超越内部循环。我们希望让开发人员尽可能多地自动化软件开发生命周期。”

正如 Augment Code 的 CEO Matt McClernan 在与我交谈时也提到的那样，该团队有点惊讶地发现其用户确实希望在 CLI 中工作。

McClernan 于去年 12 月加入该公司，几周前从 Scott Dietzen 手中接任 CEO 一职，他呼应了 Gur-Ari 的评论，并指出许多客户正在寻找将 Augment Code 及其上下文引擎引入其工作流程和 CI/CD 管道的方法。 他说，CLI 代理将允许开发人员为他们的特定用例构建模板和脚本。

至于交互式体验，该团队表示，它看起来和感觉很像现有的 CLI 代理。 在这一点上，这是一条非常成熟的道路，看起来 Augment Code 并没有试图在那里重新发明轮子。

有趣的是非交互模式。 他说：“我们希望你能够采用与[交互模式]完全相同的提示，然后在非交互模式下运行该工具，然后获得对你想要的非交互程度的某种程度的控制”，他暗示 AI 代理可能仍需要提示开发人员提供更多信息。“你想查看完整的对话历史记录吗？ 或者，如果你只是相信它有效，并且你真的只想要模型给出的最终答案，而不需要所有的工具调用？ 那么你也可以这样做，因为这允许更多的脚本编写，对吧？ 因为那样，你甚至可以在 Unix 管道中运行该工具，作为你工作流程的一部分。”

该团队指出，CLI 代理本质上与该公司在任何地方使用的代理相同，因此它使用与 Augment Code 的其余工具相同的上下文引擎。 该公司长期以来一直认为，正是这种上下文引擎使其在竞争中脱颖而出（尽管例如 [GitLab](https://about.gitlab.com/?utm_content=inline+mention) 也提出了类似的说法）。