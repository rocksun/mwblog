<!--
title: CI 并非为编程 Agent 而建：揭秘下一代验证架构演进
cover: https://cdn.thenewstack.io/media/2026/05/ad6de1b9-prakasit-khuansuwan-e48vzazk6rq-unsplash-scaled.jpg
summary: 传统 CI 管道对于秒级迭代的编程 Agent 而言过慢。文章提出“计划”概念，通过临时环境和可被 Agent 调用的验证原语，将集成测试左移至开发会话中，实现即时反馈。
-->

传统 CI 管道对于秒级迭代的编程 Agent 而言过慢。文章提出“计划”概念，通过临时环境和可被 Agent 调用的验证原语，将集成测试左移至开发会话中，实现即时反馈。

> 译自：[CI wasn't built for coding agents. Here's what comes next.](https://thenewstack.io/ci-for-coding-agents/)
> 
> 作者：Anirudh Ramanathan

多年来，集成测试一直存在于 CI 管道中，由推送（push）触发，并在十分钟、二十分钟或三十分钟后给出结果。在人类推送代码的时代，这种模式行之有效。但现在不行了：[开发者正在驱动以秒级速度迭代的编程 Agent](https://thenewstack.io/claude-code-agent-view/)，而往返远程管道的速度太慢，无法融入工作发生的循环中。

> “开发者正在驱动以秒级速度迭代的编程 Agent，而往返远程管道的速度太慢，无法融入工作发生的循环中。”

最近，我们一直在重新思考在这个新世界中，集成测试应该是什么样子。我们最终确定的方案是一种我们称之为“计划（plans）”的东西：小型的、Agent 可选取的端到端检查，它们在 Agent 的会话中针对真实的集成环境运行。

## 双循环税（The two-loop tax）

传统上，验证被分为两个循环：

*   **内循环（Inner loop）**：本地开发、单元测试、docker-compose。反馈快，部分是合成的。
*   **外循环（Outer loop）**：CI 管道，基于推送，针对预发布（staging）环境。保真度更高，至少需要十分钟才能得出结论。

对于 Agent 来说，这种往返时间太长，没有实际意义。Agent 在几秒钟内完成修改，无法为远程结论等待十五分钟，因此它从内循环直接交付。它运行的唯一验证是内循环所能提供的，而在大多数情况下，这些验证是部分的且使用 Mock 模拟的。验证代码在完整系统中运行的负担被交给了开发者，导致循环处于开启状态。

一种自然的想法是将 Agent 放入 [CI 本身](https://thenewstack.io/introduction-to-ci-cd/)。让它编写管道、生成测试桩并对失败做出反应。这个方向是对的，也是未来的发展方向。但使“CI 中的 Agent”发挥作用的原语，正是内循环首先需要的：一个足够小的验证单元，以便 Agent 能够编写、选择并在几秒钟内针对真实环境运行。

构建该原语后，内循环可以在编写过程中直接调用它。外循环可以在推送时调用相同的东西。开发者的 Agent 可以将 CI 作为一个验证库来访问，而不是等待远程管道。我们从内循环开始，因为那是目前得出结论的时间瓶颈最严重的地方，但正是这个原语让两个循环得以合并为一个。

## 环境不再是难点

答案的第一部分是人们今天已经在内循环中做的事情：隔离的、按需生成的临时环境，按运行范围划分，并以能够满足 Agent 需求的方式提供对真实下游服务和依赖项的访问。我之前曾在 [The New Stack 上写过如何构建这些环境](https://thenewstack.io/using-istio-or-linkerd-to-unlock-ephemeral-environments/)，该模式具有广泛的适用性。

这里重要的是它带给你的属性：**一个具有生产级保真度的集成环境，按需提供，并限定在正在进行的工作范围内。** Agent 可以在几秒钟内召唤一个环境，对其进行验证，并在不再需要时将其销毁。

![一个具有真实保真度的环境，按运行召唤，并限定在正在进行的工作范围内。](https://cdn.thenewstack.io/media/2026/05/4b2a2693-1-1024x484.png)

## 工作流同样重要

环境是必要的，但还不够。集成测试的另一半——即验证如何被“定义”、选择、运行和响应——是前 Agent 时代的假设根深蒂固的地方。如今的集成测试在管道中运行：重量级的产物，旨在通过复杂的引导、在推送触发下针对固定的一组步骤远端运行。所有这些在 Agent 的会话中都是无法触及的。

所以问题变成了：正确的原语应该是什样子？它需要足够小，以便存在于 Agent 的工作会话中，但又要足够真实，能够捕获针对活跃集群的集成漏洞。它是 Agent 可以在几秒钟内编写、人类可以审查、团队可以保留并重用的东西。它更像是 Agent 在需要时调用的函数，而不是按自身计划运行的管道。

我们将这种原语称为 **计划（plan）**。

## 动作（Actions）与计划（Plans）

计划是一个小型的两层系统。通过绘制图层更容易解释。

![Agent 计划与动作之间各层的工作流图](https://cdn.thenewstack.io/media/2026/05/6accb923-2-1024x471.png)

### 动作（Actions）

类型化的、确定性的构建块。如果你使用过 GitHub Actions 或任何其他工作流运行器，你应该会对这种形式感到熟悉。有两点值得注意：

*   **它们在集成环境中的真实基础设施上运行**，而不是针对 Mock。`request-http` 访问真实的端点，`playwright` 驱动真实的浏览器，`k6` 加载真实的服务。
*   **它们是用 markdown 描述的。** 每个动作的接口、输入和用法都在行内进行了文档化，因此规划 Agent 可以像开发者阅读文档一样阅读动作，并在第一次尝试时正确地组合陌生的动作。

### 计划（Plans）

计划是由动作编译而成的 DAG（有向无环图），缝合在一起以端到端地验证一个用户可见的行为。这些旨在由 Agent 编写。值得指出的是：

*   **使用[自然语言](https://thenewstack.io/sentrys-seer-agent-debug/)编写。** 开发者或 Agent 描述他们想要验证的行为（“执行请求打车流程并断言路线图中显示了两个地点名称”），规划 Agent 随后生成 DAG。
*   **选择提示（Selection hint）。** 每个计划都带有对其验证内容的文字描述。当变更发生时，Agent 会读取整个目录中的提示，并为该差异（diff）选择正确的计划。

这是一个例子：

```yaml
spec:
  selectionHint: "End-to-end ride-request check for HotROD: pick pickup +
    dropoff in the React app, request a ride, assert the resulting
    itinerary shows both location names."
  steps:
  - id: e2e_ride
    action: { actionID: <playwright-action-id> }
    args:
      values:
        script: |
          test('itinerary shows pickup and dropoff', async ({ page }) => {
            await page.goto(process.env.BASE_URL + '/');
            await page.getByRole('button', { name: 'Request Ride' }).click();
            await expect(page.locator('.itinerary')).toContainText("Rachel's Floral Designs");
          });
```

### 为什么计划适用于内循环

每个计划端到端地覆盖一个用户可见的行为，而不是一个管道或整个测试套件。这使得它足够小，可以放入 Agent 的会话中，并且 Agent 可以通过 `selectionHint` 轻松选择正确的计划。

触及打车请求路径的差异代码仅运行覆盖它的那一两个计划，而不会运行任何关于计费或身份验证的计划。底层的环境是真实的，因此返回的答案在秒级内就是有用的，甚至在 PR 开启之前。

## 实践中如何运作

这个例子使用了由 Jaeger 创建的修改版 [HotROD 打车演示应用](https://github.com/signadot/hotrod)。它在 Kubernetes 上模拟了一个具有四个 Go 服务的打车后台。前端协调对地点、司机和路线服务的调用，并由 Redis、MySQL 和 Kafka 支持。

一个 Agent 重命名了地点服务上的一个 Go 结构体字段：`Name` 变成了 `LocationName`。这种类型的重构可以通过编译、通过单元测试，看起来已经完成了。

![Agent 重命名地点服务上的 Go 结构体字段的示例截图。](https://cdn.thenewstack.io/media/2026/05/6890afa2-3-1024x471.png)

*Agent 视角下的变更。集成中断在这里是看不见的。*

在开启 PR 之前，Agent 通过其选择提示从目录中选取现有的打车请求计划并运行它。该计划是一个 Playwright 检查，它在包含修改后服务的临时环境中，通过真实浏览器走完预订流程。

它失败了。前端仍然从 JSON 中读取 Name。字段消失了，路线图渲染为空，断言失败。

![关于哪个断言失败以及在此过程中捕获了什么的结构化报告示例。](https://cdn.thenewstack.io/media/2026/05/b100963b-4-1024x423.png)

*Agent 视角下的失败：关于哪个断言失败以及在此过程中捕获了什么的结构化报告。*

Agent 读取失败，将其追溯到契约，发现前端是受影响的消费者，在那里修改了四个文件，并重新运行计划。

它通过了。开启的 PR 已经针对真实集群进行了验证。

![最终报告的截图，在 Agent 看来，它已经通过了。](https://cdn.thenewstack.io/media/2026/05/b2a2693b-5-1024x606.png)

*最终报告。修复已传播到消费者，差异代码在提交给评审者时已经通过验证。*

## 这改变了 SDLC 的什么

验证“左移”了。以前在 CI 处理时才运行的集成测试，现在在 PR 开启之前，就在 Agent 的会话中针对真实集群运行。以前在预发布阶段才会暴露的错误（局部正确，系统性破坏）在单个 Agent 循环内就被发现并修复。预发布环境重新变回最终的健全性检查，而不是主要的测试平台。

驱动 Agent 的工程师首先感受到这种转变。以前意味着等待 CI 的验证现在就在编写会话中到达，因此当工程师和 Agent 还在共同处理代码时，集成失败就会浮出水面，而不是在循环关闭之后。下游的审查（无论是工程师自己还是同事）变成了对行为的审查，而不是对验证的替代。呈现在人类眼前的是已经针对真实集群通过的差异，以及任何人都可以审计的环境 URL 和计划运行记录。

随着时间的推移，团队会建立一个版本化的计划库。每个计划都是对一种行为“正确性”含义的简短描述。该库最终兼作 Agent 验证的参考资料，以及人类理解系统的文档。

> “随着 Agent 在管道的一端将代码生成压缩到秒级，如果将集成验证固定在外循环，CI 就会变成一个不断积压的任务队列，而不是一种反馈机制。”

我们认为这是一个必要的转变。随着 Agent 在管道的一端将代码生成压缩到秒级，如果将集成验证固定在外循环，CI 就会变成一个不断积压的任务队列，而不是一种反馈机制。结论必须在 Agent 仍在循环中时到达，否则生成的代码与交付的代码之间的差距对于云原生团队来说将持续扩大。

## 我们如何交付它：Agent 技能

上述原语描述了 Agent 需要什么样的验证。问题在于 Agent 如何获取它们。Agent 技能（Agent skills）是正确的形态：限定范围的、可加载的指令，Claude Code、Cursor、Codex 以及其他现代框架已经将它们作为一等扩展（first-class extensions）采用。

技能之所以有意义，有几个原因。它们存在于 Agent 已经工作的地方。它们被故意设计得很窄：编写计划和运行计划是不同类型的工作，将它们分开可以使每个技能足够小，以便 Agent 可以毫无歧义地选择正确的工具。

计划工作流以两项技能的形式发布，按工作形态划分：

[`signadot-plan`](https://www.signadot.com/docs/integrations/coding-agents/agent-skills#signadot-plan?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content) 负责编写。开发者或 Agent 描述他们想要验证的行为，该技能会生成一个草拟计划，由动作目录组合而成，准备好与代码一起进行审查和提交。

[`signadot-validate`](https://www.signadot.com/docs/integrations/coding-agents/agent-skills#signadot-validate?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content) 是运行器。它读取差异，通过选择提示选取正确的计划，启动临时环境，针对真实集群运行计划，并呈现 Agent 可以采取行动的失败信息。

将它们分开可以使每个技能足够小，以便 Agent 能够毫无歧义地选择正确的技能。[基于计划的验证快速入门](https://www.signadot.com/docs/tutorials/quickstart/plan-based-validation?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content)完整地演示了上述示例。

这些技能目前在 Agent 的会话中运行，这正是目前的瓶颈所在。同样的原语也可以向另一个方向延伸：同样的计划可以在推送时在 CI 中运行，针对同样的临时环境，作为内循环检查遗漏的任何内容的兜底。关于这一点，我们下次再谈。