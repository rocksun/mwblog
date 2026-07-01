AI 编程工具不仅能帮助工程师更快地编写代码，还能让他们在涉及特定模式的每一个合并请求（PR）中，以更快的速度、更大的规模犯下同样的错误。我所说的不是那些明显错误的 AI 代码，而是那些虽然能编译通过、通过基本检查且看起来合理的代码，但实际上在逻辑上是错误的、臃肿的，或者与实际需求不符的代码。

在实践中，这通常表现为：AI 对一个只需要 10 行代码的问题进行了过度设计的抽象；代码忽略了代码库的既定模式、命名规范或架构；调用了不存在的 API；或者在不了解原因的情况下盲目复制模式，比如在不需要的地方添加重试逻辑。

这类错误是系统性的，正因如此，它们是可以预防的。

## 你有 CLAUDE.md 和 Skills，但是……

大多数团队的应对方法是尝试给 AI 提供更好的指令。他们将标准记录在 [CLAUDE.md](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/) 文件中，配置 Skills，并描述他们希望模型遵循的约定。这是一种正确的本能，但并不总是有效。

他们要求同一个生成代码的非确定性代理（Agent）去纠正自己的错误。它可能遵循你写的规则，也可能不遵循。这中间既没有证据，也没有审计轨迹，你无法预先知道它会运行出什么结果。CLAUDE.md 文件是生成的输入，而不是验证系统。

> “CLAUDE.md 文件是生成的输入，而不是验证系统。”

可靠地捕获垃圾代码需要结构上相互独立的东西：一个能够独立检查输出、使用不同代理、并且在看到相同代码时每次都能产生相同结果的系统。

## 验证的两个层级

我们 Aviator 一直致力于推动的转变是[将代码审查替换为已验证的意图](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness)。团队不再是让审查者阅读差异文件并问“这看起来对吗？”，而是在代码编写之前就达成共识，确定代码应该做什么，然后由一个独立的验证系统根据该共识检查输出。

将其想象成建筑检查。建筑物的批准不是由建筑师盯着每一个钉子钉下去来完成的，而是由检查员根据蓝图评估完工的结构来完成的。意图驱动的验证遵循同样的模式：规范是蓝图，代理的实现是施工，验证流水线为每个标准生成结论和证据，审查者则基于意图契合度和证据质量进行批准。

> “团队不再是让审查者阅读差异文件并问‘这看起来对吗？’，而是在代码编写之前就达成共识，确定代码应该做什么。”

该模型有两个[层级](https://docs.aviator.co/verify/concepts/verification-layers?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness)，理解为什么需要两个层级而不是一个，是使其奏效的关键。

**用户准则（User criteria）** 是针对特定变更的验收标准，由代理根据表达的意图生成或手动编写。它们仅限于当前的 PR。例如端点路径、响应格式、失败时的行为以及明确排除范围的内容。这就是特定任务意图存在的地方。

[**不变准则（Invariant criteria）**](https://docs.aviator.co/verify/concepts/invariants?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness) 来自团队的“不变性目录”，是自动应用于每个匹配变更的规则。用户提供的验收标准描述了“此变更应该做什么”，而不变准则则描述了“每个变更都必须遵守什么”。它们存在于你的账户中，并统一更新。

你的不变准则应该对规则的描述具体，但对实现方式保持灵活：

* 所有 HTTP 处理程序必须在任何业务逻辑之前调用身份验证中间件。
* “所有迁移都必须声明一个 down 代码块。”

这些规则定义一次，并在每次运行时进行检查。开发人员不需要在规范中包含它们，因为系统会自动加载匹配集。

将检查提升为不变准则的测试标准是“复发性”：任何你在审查评论中多次提到的内容，都应该成为不变准则。Aviator 实际上会自动执行此操作，它会根据过去的评论自动创建不变准则。

当验证运行时，两个层级被组装成一个单一的验收标准列表，并通过同一个流水线。一个添加订阅状态端点的规范可能包含以下用户准则：

*# 添加订阅状态端点*

*## 验收标准*

*– [ ] 端点: GET /api/v1/subscription/status*

*– [ ] 响应包含: status, renewal\_date*

不变性目录随后会自动添加其自身的准则，例如：所有 HTTP 处理程序必须使用 AuthMiddleware。验证过程会检查所有项目：

* ✓ 端点路径正确（用户准则）
* ✓ 响应包含 status, renewal\_date（用户准则）
* ✓ 处理程序使用 AuthMiddleware（不变准则）

所有项目必须通过。规范编写者不需要记住身份验证要求，系统会自动根据目录进行强制执行。

## 作为反垃圾代码注册表的不变准则

[不变准则](https://docs.aviator.co/verify/concepts/invariants?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness)是我们所称的“反 AI 垃圾代码注册表”，这使得工作能够大规模开展。它们解决了最常见的 AI 垃圾代码类别：对约定视而不见、使用了已弃用的 API、模型不知道的模块边界，以及应该适用于任何地方的安全基准。这些内容都不在[模型针对你特定代码库的训练数据](https://thenewstack.io/better-context-will-always-beat-a-better-model/)中。它们存在于资深工程师的脑海中，表现为重复的审查评论。

大多数值得编写的不变准则始于被留言超过两次的审查评论。以下是将真实审查评论转化为不变准则的示例：

针对 PR #4173 的评论：

“请不要直接写入用户表——请通过 `UserRepository.UpdateProfile` 进行。我们上季度因为类似的模式出现了一个部分写入的 bug。”

不变准则主体：

```
Writes to the users table must go through UserRepository. Direct INSERT,
UPDATE, or DELETE statements against the users table are not allowed
outside the repository package. Schema migrations under src/db/migrations are exempt.
```

条件：`file_path_glob: src/**/*.go`（跳过非 Go 文件）。

类别：`functional_correctness`。

你可以挖掘历史审查评论，对其进行聚类，并生成供人工审批的不变准则候选项。你编码的每一个不变准则，都是一个永远不需要再占用审查者时间的检查。

我可能曾说过代码审查是一个不再符合工程工作形态的历史性审批门槛，或者我们可以[停止阅读代码](https://thenewstack.io/future-of-code-reviews/)，但这不会在一夜之间发生。在实践中，随着时间的推移，我们将人类的判断力向上游移动，因为那里的价值更高。并非所有事情都必须经过相同深度的审查。人类应该审查规范、计划、约束和验收标准，而不是审查 500 行的差异代码。

这与规则文件（rules file）的区别还在于[验证](https://docs.aviator.co/verify/concepts/how-verification-works?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness)发生时的情景。编写代理和验证代理是不同的。它们不共享上下文，不共享盲点，并且验证者会为每个标准生成结构化的报告——包括文件引用、推理、通过/失败/部分通过——而不是来自编写代码的同一个模型的直觉性意见。

## 我们构建了什么，以及它发现了什么

在 Aviator，我们最近进行了一项实验，以测试[意图驱动的验证方法](https://www.aviator.co/blog/what-if-code-review-happened-before-the-code-was-written/)：如果代码在编写之前就完成了审查会怎样？

团队没有让 AI 编写代码然后由工程师审查，而是花时间在任何实现开始之前编写并审查了范围、验收标准和边缘情况。然后我们将其交给 AI 代理让其构建。

结果大约产生了 6,000 行代码。第二个代理随后根据规范中的 65 个用户准则项目验证了输出。整个过程耗时 6 分钟。60 个通过，4 个失败，1 个部分通过。

> “你不再是在构建软件了。你是在构建构建软件的机器，而质量控制是该机器的一部分。”

人类审查者仍然发现了一些问题，但在代码生成之前就验证了设计层面的决策，并且整个组织的不变准则在过程中被自动强制执行。

你不是在第十五次留下相同的评论，而是在识别模式、编写一次，并让系统强制后续的每一个变更都遵守它。你不再是在构建软件了。你是在构建构建软件的机器，而[质量控制是该机器的一部分](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness)。