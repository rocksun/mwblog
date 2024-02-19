<!--
title: API设计的核心原则
cover: https://cdn.thenewstack.io/media/2024/02/f132722d-design-1024x540.jpg
-->

API 应易学易用，难以滥用。同时，良好的设计应考虑到 API 的演进。

> 译自 [What Are the Core Principles of Good API Design?](https://thenewstack.io/what-are-the-core-principles-of-good-api-design/)，作者 Charles Humble 是一位前软件工程师、架构师和首席技术官，曾担任技术和内容团队的高级领导和执行官。他于2014年至2020年担任 InfoQ 的总编辑，并于2020年至2023年担任 Container Solutions 的首席编辑。

在 2007 年在 Google 举行的一场[杰出演讲](https://www.youtube.com/watch?v=aAb7hSCtvGw)中，软件工程师兼技术作者 [Joshua Bloch](https://www.linkedin.com/in/joshua-bloch-37038/) 表示，API 是一种极为重要的商业资源。这主要是因为如果 API 开放给客户使用，他们可能会选择大量投资于此，使得他们难以转向其他方案。

相反，Bloch 表示：“设计不良的 API 可能会导致无尽的支持电话，使得公司极其难以取得进展。”

Bloch 曾主导设计和实现了许多 Java 平台功能，包括 Java 集合框架，他进一步指出：“从 API 设计的角度思考有助于提高您编写的程序的质量。”

即使作为程序员，您不是在处理面向公众的 API，您仍然经常[创建 API](https://thenewstack.io/state-of-the-api-microservices-gone-macro-and-zombie-apis/)。良好的编程是模块化的，而模块之间的界限本身就是 API。同样，如果您在一个现代的、分布式的、微服务类型的系统上工作，服务边界也是 API，尽管其架构略有不同。

然而，API 设计是许多程序员似乎难以应对的一个领域，那么好的 API 的特征是什么呢？

## 名称至关重要

在高层次上，[API 应该易于学习](https://thenewstack.io/a-favored-target-for-attackers-apis-need-more-than-the-security-basics/)和编写，并且难以被滥用。您的 API 也需要不断发展，而一个好的设计会考虑到这一点。

您如何命名事物真的很重要，因为 API 本质上是一种小语言，其用户需要学习。

“真正好的名称能够解决问题并防止误解，因为正确的名称能清晰地表达某个东西是什么，” [SoftIron](https://softiron.com/) 的首席科学家 [Harry Richardson](https://www.linkedin.com/in/harry-richardson-007a69/?originalSubdomain=uk) 告诉 The New Stack。

Richardson 指出，对于开发者来说，名称塑造了我们的心智模型。

“回过头来改变心智模型确实需要相当多的工作，不一定是代码方面的，而是在你思考事物的方式上。”

鉴于此，花时间想出一个非常准确地传达给定 API 做什么的名称确实是值得的。

作为一个作家的标准工具 —— 字典和同义词词典 —— 可能会很有帮助。如果你发现某个东西特别难以命名，这可能表明它试图一次做太多事情。就像一个过于复杂的句子可能需要拆分成两个一样，如果需要，要准备好拆分一个过于复杂的模块。

避免使用不合常理的隐秘缩写，注意一致性的缺失，比如使用多个意思相同的词。例如，如果你需要返回给定员工的基本工资，避免创建两个方法，比如 `getBasicSalary()` 和 `getBaseSalary() `—— 如果你的 API 有一个 `remove()` 方法和一个 `delete()` 方法，你会知道它们之间的区别吗，甚至是否有区别？

使用的语言应该与组织或供应商公开的任何[其他 API 内部一致](https://thenewstack.io/how-to-maintain-api-consistency-as-you-scale/)。这种一致性的需要意味着具有一定程度的中央治理可能会有所帮助。

一些较大型企业，例如，会将高级技术撰写人员的角色扩展到帮助工程团队统一命名方法、属性和字段。

如果您正在使用 REST 风格的系统，独立顾问、O’Reilly 书籍《[Mastering API Architecture](https://www.oreilly.com/library/view/mastering-api-architecture/9781492090625/)》的合著者 Daniel Bryant 建议查看一组现有的 API 指南，因为这些指南可以帮助您确保 API 行为的一致性。对于基于 HTTP 的 API，他推荐考虑使用 [OpenAPI](https://swagger.io/specification/)，还有[其他](https://github.com/microsoft/api-guidelines)一些，包括 [Atlassian](https://developer.atlassian.com/server/framework/atlassian-sdk/atlassian-rest-api-design-guidelines-version-1/)、[Google](https://cloud.google.com/apis/design) 和 [Microsoft](https://news.microsoft.com/?utm_content=inline-mention)。

同时，值得一提的是，虽然所有的 API 都需要适当的名称，但这些名称本身是与领域相关的；例如，为量化人员编写的 API 会使用与为零售商编写的 API 完全不同的语言。理想情况下，选择的术语应该与业务已经使用并且至少了解的术语相匹配。

为了确保这一点，Bryant 告诉 The New Stack，最好进行用户研究，并确保覆盖到可能使用 API 的所有群体。

“QA 人员对 API 应该如何工作有着不同的想法，与开发者看待它的方式相比，”他说。“我经常看到开发者在不询问谁会使用 API 的情况下设计 API，结果暴露了内部域模型。”

他建议以“[Jobs-to-be-Done](https://strategyn.com/jobs-to-be-done/)”思考，即：您的关键任务是什么？您的工作流程是什么？您如何处理它？您希望如何处理它？最后一个问题至关重要，因为惯性会在已建立的流程周围形成。

“如果你能简化事物，你就可以改变人们的世界，而当系统随着时间的推移而发展时，通常会有很好的机会，” Bryant 说道。

## 最少惊讶原则

你的 API 也应该符合所用编程语言的惯用法，并尊重该语言的工作方式。例如，如果 API 用于 Java，应该使用异常来处理错误，而不是像在 C 中那样返回错误代码。

API 应该遵循最少惊讶原则。这可以通过对称性来实现；如果需要添加和删除方法，应该在适当的地方应用这些变化。

一个好的 API 包含了少量的概念；如果我在学习它，我不应该学到太多东西。这不一定适用于方法、类或参数的数量，而是指 API 所涵盖的概念表面积。理想情况下，一个 API 应该只致力于实现一件事情。

最好也避免为了添加而添加任何东西。“有疑问时，就将其留下，” 正如 Bloch 所说的那样。如果确实需要，通常可以将某些内容添加到 API 中，但一旦 API 公开，就无法删除内容。

正如前面提到的，你的 API 需要随着时间的推移而不断发展，因此设计的一个关键部分是能够在不破坏一切的情况下进行后续更改。

“归根结底，关键在于 API 应该反映现实，” Richardson 表示。“所以，例如，如果一个人可以有多个地址或电话号码，即使你目前只关心一个，只允许一个地址并不符合现实。而忽视现实总会给你带来麻烦。”

## API 永不消逝

根据 Richardson 的说法，一个常见的反模式是实现部分 API，因为那是你现在唯一需要的部分。这里的危险在于你没有充分考虑 API，并最终得到了在其他情况下无法正常工作的东西。

“你需要[对 API 设计](https://thenewstack.io/how-radical-api-design-changed-the-way-we-access-databases/)进行比任何其他事情都更多的思考，” Richardson 表示，“因为一旦构建完成，你就不能对其进行更改。”

第二个问题涉及封装和实现细节的泄漏。

“如果实现细节泄漏了，你就无法改变它，” Richardson 说道。“因此，你需要考虑，这里发生了什么操作？数据结构到底是什么？”

通常情况下，错误处理是一个容易被忽视的地方。例如，如果你正在使用数据库作为后端存储，不要让 SQL 错误传播出去，因为如果随后想要更改存储机制，你就无法做到这一点。

与软件开发的任何其他方面一样，认为自己可以将自己关在房间里孤立地工作在 API 上是一个错误。如果你这样做，你就会冒着在设计上投入过多，即使出现问题也是如此的风险。最好经常与利益相关者测试你的想法，就像你对待任何其他系统一样。

在开始编写 API 之前，编写一个简短的规范是个好主意，你可以向利益相关者展示，详细说明它的功能和工作方式。保持规范的简短使其更有可能被阅读，并防止你过度投入解决方案。如果你花了几个月时间写了一个100页的规范，你就不太可能承认它不好。

文档是最被低估的方面之一，不仅在 API 设计中如此，在计算机领域也是如此。技术撰写人员经常被低估和低薪，文档被视为最好是事后再考虑的问题，这体现在“代码就是文档”的最大化原则上。这是危险的胡言乱语。

虽然你希望你的 API 易于理解和学习，但它的文档仍然非常重要。它应该是完整而全面的，至少应该涵盖每个方法、每个字段的作用以及错误条件。

“你希望它列出每个可能返回的错误代码以及在什么情况下，” Richardson 强调道。

花时间完善和修订文档，并避免常见问题，比如使用不容易理解的缩写词。

在开发 API 的过程中继续编写代码。Bloch 指出，开发者经常在过程的中途停下来，但在整个实现过程中继续编写 API 可以让你真正了解它是如何工作的。

“这些代码并不是浪费的，” Bloch 指出，“因为它帮助你生产更好的产品，同时也为其他程序员提供了一组可以学习的示例。”

这些示例至关重要，因为它们将被其他开发人员反复复制，并从根本上影响 API 的使用方式。
