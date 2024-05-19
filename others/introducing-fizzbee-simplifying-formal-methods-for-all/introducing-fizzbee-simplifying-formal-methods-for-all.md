
<!--
title: FizzBee：为所有人简化形式化(Formal)方法
cover: https://cdn.thenewstack.io/media/2024/05/896e8605-fizzbee.png
-->

您可能听说过 TLA+，但如何使用它进行调试？FizzBee 是一种新的形式化方法系统，您可以在一个周末内掌握它。

> 译自 [Introducing FizzBee: Simplifying Formal Methods for All](https://thenewstack.io/introducing-fizzbee-simplifying-formal-methods-for-all/)，作者 Jayaprabhakar Kadarkarai。

两年前，我们在 The New Stack 上分享了一篇文章，介绍了 [亚马逊自 2012 年以来使用形式化方法验证其分布式系统](https://thenewstack.io/tla-the-best-debugger-optimizer-youve-never-heard-of/)。现在，亚马逊、微软、MongoDB、Confluent、Oracle、Elastic、CockroachDB 等主要参与者都在为其系统采用形式化方法。尽管这种技术在现代软件开发中具有巨大的好处和相关性，但其广泛采用受到现有工具的复杂性的阻碍。

在本文中，我们将向你介绍 [FizzBee](https://fizzbee.io)，一个新的形式化方法系统，你可以在一个周末内掌握它。

## 什么是形式化方法？

形式化方法包括使用数学逻辑来规范、建模、设计和验证复杂系统的严格技术。这些方法特别适用于从事基于云的 SaaS 或分布式系统、并发编程和类似领域的软件工程师，它们提供了一种系统的方法来保证软件和硬件系统中的正确性和 [可靠性](https://thenewstack.io/a-site-reliability-engineers-advice-on-what-breaks-our-systems/)。

> 形式化方法可以发现系统设计中的错误，而我们所知的任何其他技术都无法发现这些错误。
>
> ——亚马逊的 Chris Newcombe

## 我们今天如何发现系统设计错误？

今天，我们依靠起草设计文档和团队审查来发现系统设计错误。然而，这种方法由于效率低下和效果有限而不足。我们依赖于基于过去[经验和已知反模式的模式匹配来识别设计](https://thenewstack.io/the-power-of-prototyping-in-user-experience-design/)缺陷，因为我们缺乏探索所有可能结果的心理能力和时间。这是计算机擅长的：在几分钟内毫不费力地探索数十亿个状态。

## 为什么形式化方法没有流行起来

用于分布式系统规范的最流行的形式化方法工具是 TLA+。虽然许多人认识到它改善其工作的潜力，但障碍在于缺乏学习或使用 TLA+ 的时间。

即使在亚马逊，[Chris Newcombe](https://www.linkedin.com/in/chris-newcombe-b33a081/)，他最初在亚马逊开始使用 TLA+，在说服同事采用 TLA+ 时也面临挑战，因为工程师只有在必要或高管授权的情况下才有空闲时间。

TLA+ 为系统设计提供了强大的验证功能。然而，它的语法和数学方法对于许多软件工程师来说可能令人生畏，尤其是那些更习惯于 [Python](https://thenewstack.io/what-is-python/) 等传统编程语言的人。使用 TLA+ 表达某些算法可能需要复杂的数学公式，而使用 Python 的熟悉语法可以轻松地传达相同的逻辑。

## FizzBee：面向所有人的形式化方法

FizzBee 是形式化方法系统中的最新成员，它以其用户友好的界面和类似 Python 的语法缩小了可访问性差距。这使得各级开发人员都可以轻松表达 [复杂算法和系统](https://thenewstack.io/tutorial-use-ansible-collections-to-help-configure-and-manage-more-complex-systems/) 设计。

1. **易于学习**：如果你编写过一些 Python 脚本，你可以在短短 10 分钟内掌握 FizzBee 代码。然后，你可以在几个小时内学习模型检查原理。
2. **可读性增强**：FizzBee 规范旨在让审阅者和开发人员都能轻松理解。与 TLA+ 等其他工具不同，FizzBee 的熟悉语法确保即使非作者也能理解规范，从而促进更顺畅的审查流程和实施。
3. **多范式灵活性**：FizzBee 提供了多功能的编程选项，包括函数式、命令式、结构化、过程式和面向对象式。这允许开发人员为每个问题选择最佳方法，从而获得简洁且适应性强的解决方案。
4. **可视化**：FizzBee 的状态转换图通过提供可视化表示来帮助调试。这也提高了对模型检查过程的理解，并帮助用户更有效地识别和解决问题。
5. **在线 Playground**：FizzBee 提供了一个[在线 Playground](https://fizzbee.io/play) 用于练习、试验和探索示例，使其可用于学习和探索。

## 建模电汇系统

我们来建模两个账户之间的简单汇款，这是一个展示数据库事务一致性的经典示例。目的是确保在一天结束时，系统中所有用户的总金额不会意外丢失或增加。

### 第一次实现

我们保持简单，我们有两个用户：Alice 和 Bob。只有 Alice 被允许向 Bob 发起电汇。

```
action Init:

  balances = {'Alice': 3, 'Bob': 2}

action FundTransfer:

  any amount in range(0,100):

      if balances['Alice'] &gt;= amount:

        balances['Alice'] -= amount

        balances['Bob'] += amount
```

**Actions**： 

Actions 是系统行为规范的构建块，表示各种行为、操作或事件，如用户交互或计时器事件。模型检查器以不同的顺序重复调用这些操作，以探索系统的潜在状态。

在我们的模型中，我们使用 *action* 关键字定义了两个操作。第一个是 *Init*，一个特殊操作，只调用一次。第二个操作是 *FundTransfer*，这是我们模型中唯一的操作，并且被重复调用。

**State：**

在 *Init* 操作中定义的变量成为系统的状态变量，以后的操作可以修改这些变量。在我们的示例中，一个状态变量由一个 Python 字典表示，其中包含两个账户，余额分别为 3 和 2。

**Non-determinism：**

在测试实现时，我们通常使用单个值进行测试。但是，使用 FizzBee，您可以指定可能的值，并且模型检查器会探索所有组合。

在此示例中，您从 0 到 100 的范围内选择要转账的金额。

*any* 是用于指定非确定性的两个关键字之一。在语法上，这等同于 Python *for* 语句，允许您使用不同的金额重新运行相同的测试。

其余代码很简单：如果 Alice 有足够的资金转账，则从她的账户中扣除该金额并添加到 Bob 的账户中。

**不变量：**

在系统建模中，确保某些属性成立至关重要。一个基本属性是所有账户中余额的总和必须等于 5。

不变量有三种类型：安全性（必须始终为真的条件）、活性（最终必须为真的条件）和稳定性（最终必须为真并保持为真的条件）。

让我们从断言开始，即余额应始终匹配，类似于同一银行账户之间的转账。不变量使用“assertion”关键字指定。

不变量使用 *assertion* 关键字实现。

```
always assertion BalanceMatchTotal:
  total = 0
  for balance in balances.values():
    total += balance
  return total == 5
```

断言类似于 Python 函数，但需要布尔返回值。*True* 表示该条件在该状态下为真。

*always* 关键字表示此条件必须在每个状态下都为真。

**运行模型检查器。**

模型检查器将指示失败，显示在从 Alice 的账户中扣款后但在向 Bob 的账户中记账之前发生上下文切换的跟踪。

![](https://cdn.thenewstack.io/media/2024/05/1cf40e21-invariant.png)

*修复：将这两个步骤放在一个事务中。*

**atomic 关键字：**

使用 *atomic* 确保两个中间步骤一起发生或根本不发生，从而将它们屏蔽在系统的其余部分之外。在开发过程中，这转化为事务或锁。默认情况下，行为是串行的，但您可以明确指定其他行为。

```
atomic action FundTransfer:

  any amount in range(0,100):

    if balances['Alice'] >= amount:

      balances['Alice'] -= amount

      balances['Bob'] += amount
```

应用 *atomic* 后，运行模型检查器会成功。您还可以查看完整状态图以观察系统的行为。

![](https://cdn.thenewstack.io/media/2024/05/34043e41-pr5.png)

**电汇——非原子汇款**

让我们更改要求，即一旦收到电汇请求，Alice 的账户将立即被扣款，但 Bob 的账户可能不会立即被记账。我们只想确保它最终会被记账。

让我们从断言开始。不要总是说，从 always 更改为 always eventually。从任何状态，它最终都会达到谓词变为真的状态。这称为活性期望。（稳定性期望用 eventually always 指定，这里不常用，也不在此讨论）。

```
always eventually assertion BalanceMatchTotal:
  total = 0
  for balance in balances.values():
    total += balance
  return total == 5
```

现在，作为第一次尝试，删除 atomic 关键字（或用 serial 关键字替换它）。因此，借记和贷记分两个步骤进行

现在，当您运行命令时，您会看到它失败并显示此跟踪。

![](https://cdn.thenewstack.io/media/2024/05/7c40d1ed-pr6.png)

这表明，在扣款后，系统可能会崩溃，如果确实如此，它将丢失后续步骤并结巴。结巴表示系统可能不会再取得任何进展。

操作表示系统中可能发生的情况，而不是必须发生的情况。我们需要指定必须发生的情况。这是通过向操作添加关键字 fair 来完成的。

注意：在这种情况下，如果我们将 FundTransfer 操作标记为 fair，它只意味着 Alice 将能够继续汇款，但有可能这笔钱永远不会到达 Bob。

**实施电汇**

它发生在两个 actions 中。在第一个动作中，原子地记录电汇请求并从 Alice 的账户中扣除。在第二个动作中，再次原子地将转账标记为已完成并记入 Bob 的账户。

```
always eventually assertion BalanceMatchTotal:
  total = 0
  for balance in balances.values():
    total += balance
  return total == 5

int:
  balances = {‘Alice’: 3, ‘Bob’: 2}
  wire_requests = []

atomic action Wire:
  any amount in range(1,10):
    if balances[‘Alice’] >= amount:
      balances[‘Alice’] -= amount
      wire_requests.append((‘Alice’, ‘Bob’, amount))

atomic fair action DepositWireTransfer:
  any req in wire_requests:
    balances[req[1]] += req[2]
    wire_requests.remove(req)
```

在这里，我们保留了一个电汇请求列表，其中指明了需要完成的电汇转账的待处理请求。而动作 `DepositWireTransfer` 通过记入 Alice 的账户来完成该步骤。

运行此模型，您会注意到一个错误——死锁。

![](https://cdn.thenewstack.io/media/2024/05/c9e39cb3-pr7.png)

这是因为，当系统开始从 Alice 向 Bob 转账时，Alice 的钱用完了，系统无法取得任何进展。这是我们问题陈述中的一个问题，而不是模型或实现中的问题。我们可以通过允许 Bob 将钱转回 Alice 来轻松解决此问题。我们稍后会进行此更改。现在，为了简单起见，让我们做一个小技巧——添加一个不执行任何操作的动作。真正的代码永远不需要这样做。

```
# Add this temporarily until we fix Bob to transfer money to Alice
atomic action NoOp:
  pass
```

注意：`Pass` 是一个标准 Python 关键字，用于表示一个空块。

现在运行此模型检查器，您会注意到模型检查器通过。这意味着此设计是正确的。

注意：该模型无法直接转换为代码，因为 `wire_requests` 无法以当前形式实现。它是在与发送方相同的银行中的数据库吗？然后，接收方的银行将无法在记入发送方的同时原子地更新。我们将在以后的文章中解决此问题。

您可以在 [https://fizzbee.io](https://fizzbee.io) 上阅读有关 FizzBee 的更多信息并尝试其他示例。

## 正式验证是在编码之前测试您的设计

正式验证允许您在编码之前测试您的设计。如上所示，它可以帮助您专注于基本内容并抽象出细节，类似于在白板上使用基本示例解释设计。

通过使用正式验证，您可以在开始编码之前确保您的设计清晰且正确。但是，务必要记住，虽然正式验证很好地测试了设计，但它并不能取代常规测试的需要。在实现过程中仍然会出现错误，但通常更容易修复。

## 最后的想法：

形式化方法是设计验证的首选。从业者始终强调显著的设计简化和更快的实现。例如，在一个我重新设计了一个 buggy v1 系统的近期项目中，使用 TLA+ 指定 v2 系统的设计导致代码大小减少了 4 倍，同时还纳入了其他功能。但是，需要注意的是，像 TLA+ 这样的工具出了名的难以使用。

如上例所示，与 TLA+ 不同，FizzBee 代码易于阅读和编写，这使其成为经验丰富的软件工程师首次开始使用形式化方法的极具吸引力的替代方案。借助 FizzBee 的模型检查器，可以确保设计正确性，而其简洁且清晰的规范可以传达和记录设计。
