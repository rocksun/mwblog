
<!--
title: Sprint如何让你慢下来：一种更好的软件构建方式
cover: https://cdn.thenewstack.io/media/2024/05/e06fbfcf-athletics-3108410_1280.jpg
-->

Sprint 承诺加速开发，但通常会产生相反的效果。查看这种构建软件的替代方法。

> 译自 [How Sprinting Slows You Down: A Better Way to Build Software](https://thenewstack.io/how-sprinting-slows-you-down-a-better-way-to-build-software/)，作者 AJ Shankar。

在技术领域，软件 Sprint 已成为一种信仰。在由软件驱动的竞争性行业中，公司会感受到巨大的压力，需要在竞争对手之前发布新产品和功能。常见的做法是设定激进的两周截止日期，由一支小型开发人员团队以流水线式分工，朝着不可更改的发布日期 Sprint 。

但如果这不是构建产品的最佳方式呢？

过去 12 年来，我一直在经营一家软件公司，在此之前，我学习了软件工程，并获得了计算机科学博士学位（编程系统）。虽然 Sprint 、敏捷和现代软件方法论的整个体系中有一些智慧结晶，但它们并不是我们 Everlaw 如今构建软件的方式。

 Sprint 承诺加速开发，但往往会产生相反的效果。此外， Sprint 的无情节奏和令人不满的本质让开发人员精疲力竭并辞职。尽管经济不确定，

[不到一半](https://www.enterprisedb.com/blog/how-build-employee-satisfaction-edb-open-source-talent-survey-2022) 的开发人员表示他们对当前的工作非常满意。

我们使用的方法让工程师能够以正确的方式构建正确的功能，而无需设定截止日期。它支持精简团队，这些团队拥有设计整个功能的自主权，而不仅仅是孤立构建的组件。而且，至关重要的是，它涉及对客户进行纪律约束，不承诺新软件的交付日期。最终结果也许令人惊讶，这是一个产生更高吞吐量的开发过程：每个单位时间内交付更多功能。

我鼓励你考虑这种开发方法，而不是默认采用行业规范，导致高水平的技术债务和开发人员流动率。

##  Sprint 会让你慢下来

截止日期对软件开发的影响与对其他学科的影响不同。 Sprint 可能会产生重大的长期负面后果，鼓励开发人员提交不合格的、目光短浅的代码以按时完成。这会导致代码质量下降、工程决策不佳（以后修复成本高昂）以及工程师沮丧。

因此，虽然在任何给定的时刻，将开发人员投入 Sprint 似乎都是完成任务的最快方式，但实际上，随着 Sprint 的负面影响不断累积， Sprint 会导致随着时间的推移开发出更少的新软件。

听起来直觉上，如果你在 Sprint ，你一定以尽可能快的速度前进，但在软件开发领域，你很少会以直线 Sprint 。通常，你从一个高优先级问题曲折前进到下一个问题，解决过去由于截止日期的压力而引入的问题和缺陷。

如果你一直以直线慢跑，你很可能会走得更远——而且不会那么疲惫。

### 软件截止日期优先考虑速度而不是质量

许多领导者对软件的思考方式与对业务其他部分的思考方式相同，即由截止日期驱动的运营节奏。就像营销团队必须在 10 月 31 日之前制作其节日广告活动，或者财务团队必须在月末结账一样，工程团队也被要求在设定的日期之前发布新产品或功能。

这种想法忽略了这样一个事实：开发软件从根本上不同于其他业务实践，使其不适合截止日期。这里有三个重要原因：

- 工作通常在大型复杂代码库的上下文中完成
- 软件中的正确性标准远高于其他业务领域
- 好或坏决策的下游影响会大量累积

让我们来分解一下。

### 代码库是复杂的野兽

首先，很难预测实现新功能（即使是简单的功能）需要多长时间，因为它很少是孤立完成的。相反，新功能通常添加到现有代码库中，而其细微差别和细微差别（例如有关安全、性能和可维护性的问题）通常只有在编写代码时才会发现。

而且，由于代码是如此相互依赖，因此向良好的实现中添加新功能通常需要重写新功能将依赖的其他代码。这与预设的截止日期产生了矛盾：当工程师深入研究代码时，当截止日期临近时，他们通常必须采取捷径——“意大利面条代码”、“脆弱的实现”等等——即使他们知道实现某事的正确方法，仅仅是因为截止日期没有预料到，也无法适应这些挑战。

### 正确性的高标准

其次，“正确”在软件中的含义与在营销计划或销售策略中的含义不同。你可以按固定截止日期写一篇足够好的新闻稿，如果它可用且真实——即使不完美——也可以发布。然而，在代码中，任何偏离理想的情况都被视为缺陷，必须进行分类。它可以被忽略（导致客户愤怒）或在生产中以高昂的成本修复——通常比发布前修复的成本高出几倍。截止日期会将更多错误推入生产，导致更多工程时间用于修复这些昂贵的生产错误，而用于为客户构建新功能的时间则减少。

### 糟糕的决策复合*

第三，糟糕的实现和架构决策的下游影响会不断复合。营销专业人士今天可以写一篇糟糕的新闻稿，但明天可以写一篇好的。但新代码依赖于旧代码：它的功能、结构和它使用的范例。即使没有明显缺陷的代码也可能在这些方面存在缺陷。现在关于如何架构应用程序的仓促决策可能会让以后添加新功能变得更加困难，从而随着时间的推移减慢开发速度。这种“技术债务”是工程部门的祸害。 Sprint 可以让你今天更快地发布特定功能，但代价是损害未来的开发。

### 人越多，问题越多

当你试图在某个截止日期前发布一个关键的新功能时，通常会分配很多工程师来完成它。然而，大型工程团队面临着两大挑战：巨大的沟通开销和孤立的实现。这些挑战降低了工作效率和质量。

当每个开发人员只负责一个较大实现的狭窄部分时，他们被迫花时间相互协调，即使这样，结构问题也会使交付高质量的实现变得困难。考虑一下一位前端工程师，如果后端团队更改 API 以向前端公开关键信息，他的工作会变得容易得多。进行此类更改所需的沟通和重新排序工作量通常非常大，以至于大多数工程师根本不费心。

更重要的是，最好的实现不仅仅是对每个切片的局部优化，它们是对整个功能的全局优化，在整个堆栈中具有连贯的实现。这些实现在大团队系统中几乎不可能实现，因为除了一个能够预见到所有问题的无所不知的架构师之外，没有人有权在没有超人的沟通水平的情况下做出所有必要的更改。

## 取消截止日期，缩小团队

我们如何构建一个以高吞吐量和快乐的工程师提供高质量代码的系统？

首先，从取消截止日期开始。在我们的模型中，工程师决定何时发布功能。因此，他们能够对现在实施什么与以后实施什么做出原则性的工程决策，从而提供比在两周截止日期的驱动下做出决策时更好的代码。

其次，将较小的团队分配给功能并赋予他们更大的范围。由于团队规模较小（通常只有一名工程师！），许多新功能可以并行开发。这些独行程序员或小团队拥有从后到前的整个实现。没有每日站立会议，也没有不必要的沟通。而且，由于工程师控制着整个堆栈的实现，因此他们可以对如何构建其功能做出原则性的工程决策，而不是受他们碰巧拥有的代码库部分的限制，从而提供更具凝聚力的实现。

这两个想法之间的共同点是，它们在制度上支持做出原则性的决策，因为今天的良好决策会导致明天的更好结果。当工程被视为没有编写代码的背景、正确性要求或复合下游影响的任何其他部门时，这一基本真理很容易被忽视。

违反直觉的结果是，即使单个项目需要更长的时间才能发布（没有截止日期，团队规模较小），但总的生产力更高：我们有更多项目正在进行和完成，并且每个工程师都可以完成更多工作，因为他们花更少的时间来处理关键的生产错误和技术债务，而更多的时间在高质量的代码库中编写代码。

工程师们也更快乐。他们不必因为早先的截止日期而自己扑灭自己点燃的火。他们更自由地协作，因为他们不必权衡帮助同事和自己头上的截止日期。而且，由于他们没有被孤立在代码库的某个特定部分，因此他们不断学习新概念并应对新挑战。下游的好处是更强大的文化——以及更好的工程师。

### 让您的客户满意

您可能会问：我们如何在没有截止日期的情况下及时推出产品？首先，事实证明工程师喜欢发布代码，而且由于他们拥有整个功能，因此他们非常有动力看到自己的项目取得成果。

其次，我们的工程师不会在真空中做出决策。他们明白，在竞争激烈的行业中，交付软件是我们的主要市场优势，我们的用户依靠 Everlaw 的新功能来保持自己的竞争力，而且我们像其他任何企业一样奖励表现出色的员工。

第三，有很多支持和透明度；领导者每周都会与团队核对他们的软件进度，以解决任何障碍。我们不会放任自流，让每个人都走自己的路。我们只是不会设定会损害工作质量（和乐趣）的任意截止日期。

另一个常见问题是我们如何承诺在特定日期向客户交付特定功能，答案是我们不承诺。我们的客户很满意，因为我们生产高质量的软件并交付新功能 [比我们的竞争对手更频繁](https://support.everlaw.com/hc/en-us/sections/201109835-Release-Notes)。请记住：我们方法的全部意义在于我们随着时间的推移发布更多软件。

但是，我们确实与客户分享我们的产品路线图，以便他们可以影响其方向和优先级。但是，如果潜在客户说，“我们需要在 10 月份之前交付此功能，否则您将无法赢得我们的业务”，我们会拒绝，因为这样做会损害我们产品的质量，并对其他客户造成伤害。令人惊讶的是，很多时候，这些潜在客户会理解我们提供的价值，并无论如何与 Everlaw 签约。对于那些没有签约的客户，我们知道他们会回来，因为一两年后我们会走得更远。

这种模式需要领导层的纪律，以及市场营销部门的理解，即由于这项政策，虽然我们今年可能会因此政策失去三笔交易，但明年我们将在尖端产品的支持下赢得 30 笔交易。

## 长期方法赢得比赛

我们的模式专注于长期成果，而不是短期成果，因此并不适合每项业务。例如，仍在确定产品市场契合度的非常早期的初创公司需要快速进行试验，以找出市场想要什么。他们可能希望快速测试假设，因此优先考虑少数功能的开发速度，而不是跨多个功能的吞吐量。

然而，一旦他们建立了产品市场契合度，他们的工程目标就会从主要是实验转变为主要是执行。他们会知道他们需要构建什么才能在自己的行业中获胜，现在他们只需要尽可能快地到达那里。我们的模式最适合他们。

软件开发的黄金三要素是拥有一支快乐、积极的工程师团队，他们编写高质量的代码并发布大量功能。工程师喜欢在我们的系统中工作，因为他们对自己的工作拥有所有权。他们不必为了赶上任意截止日期而损害技术上合理的实现；他们总是在学习新技能和领域，而不是被孤立在代码库的狭窄部分；他们不会不断扑灭生产代码中的火灾；他们以高频率发布有意义的、有凝聚力的解决方案。对高质量代码的强调推动了开发吞吐量，最终使整个企业和我们服务的用户受益。
