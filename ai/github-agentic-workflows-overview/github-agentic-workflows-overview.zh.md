围绕智能代理的大部分宣传都集中在代码编写上，但如果你能让一个智能代理监控你的GitHub仓库中的事件，并在例如创建新议题时自动运行一套工作流呢？如果你只需向智能代理描述工作流，然后让它为你生成详细的步骤呢？这就是孵化了GitHub Copilot的GitHub Next团队向自己提出的问题。

在接受 *The New Stack* 采访时，GitHub Next的首席研究员 Eddie Aftandilian（他也参与了Copilot的工作）指出，开发者可能希望在持续集成过程中执行许多任务，但这些任务无法通过纯粹的确定性算法现实地完成。它并非旨在取代现有的CI/CD工具，而是通过该团队称之为“持续AI”的能力来增强它们。

“有一整类事情是永远不会完成的，你总是希望一个智能代理监控仓库中的事件，也许按计划运行，或者在创建议题时运行，然后基本上遵循一系列步骤来审查或处理它，” Aftandilian 解释道。

这款名为[GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/)的新工具，[现已在GitHub上线](https://github.github.com/gh-aw/)，并利用GitHub Actions提供沙盒环境和基础设施，以便在可能数百万个仓库中运行智能代理。

## 用例

最基本的用例是在一天结束时运行[每日状态报告](https://github.com/githubnext/agentics/blob/main/workflows/daily-repo-status.md?plain=1)，总结最近的议题、拉取请求、讨论等。但它也可以意味着运行一个每日智能代理，识别团队可能偏离最佳实践的地方并提出修复建议（随后Copilot可以手动或自动标记来修复它们）。

以下是团队提供的几个额外示例，但与所有此类项目一样，开发者无疑会发现更多创造性的方式来使用此类工具：

尽管仍处于预览阶段，Agentic Workflows已支持三大编码智能代理：Claude Code、OpenAI Codex和GitHub自家的Copilot。

## 工作流的智能代理提示

设置这些工作流的一个有趣的初步步骤是微软研究员 Peli de Halleux 在同一次采访中称之为“智能代理创作”的东西。这意味着你只需用几句话描述智能代理应该做什么，该工具就会生成一个完整的、分步的工作流，并建议使用的工具和权限设置（默认为只读）。

“进入门槛基本上已降至接近零，” de Halleux 解释道。“智能代理非常擅长提示，我们可以将调试和优化融入到创作体验中，因为智能代理还可以读取它们的日志并推断它们过去所做的事情。”

这些工具随后会创建两个文件：一个描述智能代理工作流的Markdown文件，以及一个用于GitHub Actions的YAML文件。Markdown文件包含指定要使用的工具和MCPs以及智能代理所拥有权限的头部信息，但大部分内容是对工作流的英文描述。

实际操作中是这样的：

> `---  
> on:  
> schedule: daily  
> permissions:  
> contents: read  
> issues: read  
> pull-requests: read  
> safe-outputs:  
> create-issue:  
> title-prefix: "[repo status] "  
> labels: [report]  
> tools:  
> github:  
> ---`
>
> `# Daily Repo Status Report  
> Create a daily status report for maintainers.  
> Include  
> - Recent repository activity (issues, PRs, discussions, releases, code changes)  
> - Progress tracking, goal reminders and highlights  
> - Project status and recommendations  
> - Actionable next steps for maintainers  
> Keep it concise and link to the relevant issues/PRs.`

## 安全架构

权限是只读的，智能代理绝不允许写入——它可以在议题上评论并参与讨论，但总会有一个验证阶段。写入操作总是被推迟，并在智能代理完成其任务后作为单独的作业运行。

“你希望这些智能代理所做的事情受到保护、经过验证、再次验证，以便获得大量的保障，并了解这些事情的稳定性。这对于我们拥有使用它的信心来说，实际上非常非常重要，” de Halleux 解释道。

GitHub Actions本身已经包含了其安全架构，但该团队随后使用了他们称之为[SafeOutputs](https://github.github.com/gh-aw/introduction/architecture/)的子系统，这是一组可信组件，其输出通过确定性过滤器运行，以便在该级别强制执行策略。

此外，智能代理工作流防火墙可以限制智能代理的访问权限。

## 从代码改进开始

尽管如此，团队仍然建议开发者在让智能代理创建拉取请求之前，先从低风险的输出开始，例如评论、草稿和报告。首先，开发者应该让智能代理专注于改进现有代码，而不是构建新功能。

随着时间的推移，随着智能代理的改进以及开发者对如何使用这些智能代理循环有了更好的直觉，我们可能会看到更雄心勃勃的用例。

然而，团队有一点非常明确：这并非要取代现有的CI/CD工作流。“这种方法将持续自动化扩展到传统CI/CD难以表达的更主观、重复性任务，”文档强调。但它可以为开发者分担大量的日常繁重工作，并理想情况下，带来更好的代码。