<!--
title: Go与SQLite：打造永不中断的持久化后台执行
cover: https://threedots.tech/images/covers/sqlite-durable-execution-social.png
summary: 持久执行保证程序输出正确，业务应用需将输入写入持久存储，结合幂等性与原子性实现。Watermill SQLite 后端是实现持久性的良好选择。
-->

持久执行保证程序输出正确，业务应用需将输入写入持久存储，结合幂等性与原子性实现。Watermill SQLite 后端是实现持久性的良好选择。

> 译自：[Durable Background Execution with Go and SQLite](https://threedots.tech/post/sqlite-durable-execution/)
> 
> 作者：Dima Kotik

**DNS 中断就像山洪暴发。它突然袭来，然后又消失得无影无踪，仿佛从未发生过一样。** “可能又是 DNS 的问题”成了一个梗。但很多时候，我们并不知道确切原因。中断很少持续足够长的时间，以便诊断、隔离、复现、模拟和测试故障情况。我们如何才能确定这类故障将来不会再次损害我们的系统？DNS 可以通过多种方式惊人地失败。

解决 DNS 中断等间歇性故障的更好方法是将其视为不可避免的偶发执行中断。我们可能无法详尽地解决每个故障，但我们可以设计我们的系统来处理其内部逻辑的几乎任何中断。**我们可以强化系统以抵御中断，从而实现*持久执行*。**

## 什么是持久执行？

*持久执行*是一种保证，即无论执行过程中任何地方出现故障，程序输出都是正确的。

具有竞争力的业务应用程序需要*持久执行*。当它缺失时，员工在检测到每个不正确的输出时，都将花费一两个小时来修复。在大型业务应用程序中，不正确的输出往往数周未被发现，导致在节假日期间出现代价高昂的混乱。

我们在谈论 Bug 吗？不。Bug 就是程序。一些间歇性 Bug 会削弱持久性，但持久性损失最常见的原因是执行过程的中断。中断可能由网络中断、服务故障、安全漏洞或延迟更新引起。所有这些原因都很常见。*持久执行*不关心是什么原因造成的。它承诺从几乎任何故障或故障组合中恢复并提供正确的输出。

事件驱动架构（EDA）是支持*持久执行*的行业最佳实践。然而，大多数 EDA 生产系统并非可证明的持久系统。发生了什么？

在我们博客的第二篇客座文章中，我们欢迎 Dima Kotik，他为 Watermill 贡献了 SQLite Pub/Sub 后端。
请大家热烈欢迎 Dima！🎉

*Miłosz & Robert*

保证与愿望之间存在差异。保证需要一些证据，以及从各种系统崩溃中恢复的历史。它始于在集成测试中模拟崩溃条件。在编写了许多此类测试之后，您将意识到一个简单而深刻的原则：***持久执行*始于将执行状态写入存储**。没有其他方法可以做到，因为随机存取存储器或临时存储器中存在的任何东西都可能在系统崩溃时消失。

持久系统的第一步是在解析和验证之后，**在进行任何处理之前**，将其输入存储起来。安全性比持久性更重要，因此输入验证优先。

## 解析和验证后存储输入

等等，什么？我必须立即将所有系统输入提交到存储中吗？是的。这可能吗？并非一次性全部完成，但这并非像人们想象的那么艰巨。

如果您正在使用事件驱动架构和像 [Watermill](https://watermill.io/) 这样的发布/订阅管理库，您就已经成功了一半。Watermill 是 Go 生态系统中最流行的事件总线之一。

Watermill 是一个异常灵活的库，因为它能够桥接来自大量不同后端事件。您的核心业务逻辑可以将事件流式传输到 PostgreSQL 数据库，而您的输入可能最初存储在边缘节点的 SQLite 数据库中，以在不牺牲性能的情况下实现持久性。Watermill 可以将两者无缝连接起来，协同工作。

不幸的是，尽管 Watermill 的文档强烈建议开发者不要使用，但许多使用 Watermill 的业务应用程序仍然在某些地方使用 Go channel 临时后端。此后端是基于 Go channel 的基本内存实现，旨在用于测试目的。事件被排队到异步通道中。当系统崩溃时，它们将消失。如果执行过程因任何原因变慢，它们将用长队列堵塞服务器。它们将与关键服务器进程竞争资源。

换句话说，不要将输入写入随机存取存储器。您这是自找麻烦。

有一个易于使用的持久性即插即用替代方案，可替代临时后端。它不是灵丹妙药，但它是迈向持久计算的轻松第一步。试试新的 [Watermill SQLite 后端](https://watermill.io/pubsubs/sqlite/)。它不需要设置任何额外的基础设施，并且比任何其他存储方法都更具性能和可靠性，因为它不需要网络连接或自定义传输协议。它写入磁盘上的文件。**它不需要 CGO**。

假设我们正在处理图书订单，并且希望将订单作为事件存储在 SQLite 数据库中：

```
db, err := sql.Open("sqlite", "orders.sqlite3?journal_mode=WAL&busy_timeout=1000&cache=shared")
if err != nil {
    return err
}
defer db.Close()

db.SetMaxOpenConns(1) // driver limitation
publisher, err := wmsqlitemodernc.NewPublisher(
    db,
    wmsqlitemodernc.PublisherOptions{
        InitializeSchema: true,
    },
)

msg := message.NewMessage(
    watermill.NewUUID(),
    // serialized order event
    []byte(`{"order_id": "1", "title": "1984", "customer": "Queen Elizabeth II", "address": "Buckingham Palace"}`),
)
if err := publisher.Publish("book_orders", msg); err != nil {
    return err
}

```

对于云实例，请确保您将 SQLite 文件写入明确挂载的持久卷。根文件系统通常是临时的。在考虑了性能影响之后，您可能希望最终将收集到的输入迁移到您的主数据库中。

匹配的订阅者与正常的 Watermill 用法没有区别，除了后端初始化：

```
subscriber, err := wmsqlitemodernc.NewSubscriber(
	db,
	wmsqlitemodernc.SubscriberOptions{
		InitializeSchema: true,
	},
)
if err != nil {
	return err
}

messages, err := subscriber.Subscribe(context.Background(), "book_orders")
if err != nil {
	return err
}

for msg := range messages { // consume messages from the channel
	processBookOrder(db, msg)
}

```

SQLite 发布者和订阅者是即插即用的替代品。**它们也可以在没有 Watermill 路由器的情况下使用。**
换句话说，您可以直接使用低级的 `Publish` 和 `Subscribe` 方法。

完整的示例在[文档](https://watermill.io/pubsubs/sqlite/)中提供。您的代码无需进行其他更改即可实现迈向*持久执行*的第一步：将输入事件写入持久存储。

然而，为了实现完整的持久性，处理图书订单的每个步骤的事件处理程序必须具备两个可证明的特性：

1.  **幂等性**：处理程序可以多次消费同一个事件，而不会生成多个下游事件。
2.  **原子性**：处理程序要么完全成功，要么完全失败。它绝不能部分成功。

这些属性与持久存储的结合确保了*持久执行*。当业务逻辑中的某个步骤因任何原因失败时，它会从上一个安全的系统状态再次尝试。

## 通过事件去重证明幂等性

幂等事件处理程序在处理相同事件时不得更改系统状态。换句话说，任何次数的输入重复对系统都没有影响。我们可以通过事件去重来实现这种效果，但最好是程序逻辑本身就容忍重复。

首先，确保事件消息仅在所有业务逻辑成功执行后才被确认：

```
func processBookOrder(db *sql.DB, msg *watermill.Message) error {
    // use only one database transaction per event handler
    tx, err := db.BeginTx(context.Background(), &sql.TxOptions{
        Isolation: sql.LevelReadCommitted,
    })
    if err != nil {
        return err
    }
    defer func() {
        if err != nil {
            _ = tx.Rollback()
            msg.Nack()
        } else {
            err = tx.Commit()
            // acknowledge the message ONLY AFTER successful transaction commit
            // what happens if the the execution fails here?
            if err != nil {
                msg.Ack()
            } else {
                msg.Nack()
            }
        }
    }()

    // process input using the business domain logic
    // ...
	return nil
}

```

如果事务成功但消息确认在第 16 行失败，会发生什么？如果处理程序是幂等的，事件将被重新处理，但系统状态不会改变。实现这一点的一个简单方法是将数据库表字段 `order_id` 约束为唯一。然后，如果错误是由唯一约束违反引起的，则忽略该错误：

```
// Example for SQLite3 "modernc.org/sqlite/lib"
if err != nil {
    if liteErr, ok := err.(*sqlite.Error); ok {
        code := liteErr.Code()
        if code == lib.SQLITE_CONSTRAINT_PRIMARYKEY || code == lib.SQLITE_CONSTRAINT_UNIQUE {
            // duplicate order id is normal behavior
            // it means that the event was already processed
            // ignore this error
            return nil
        }
    }
    // ...
}

// Example for PostgreSQL's "github.com/lib/pq" driver
if err != nil {
    const  UniqueViolationErr = pq.ErrorCode("23505")
    if errors.Is(err, UniqueViolationErr) {
        // duplicate order id is normal behavior
        // it means that the event was already processed
        // ignore this error
        return nil
    }
    // ...
}

```

如果有多个 SQL 表键约束怎么办？最好的解决方案是进行幂等性测试。然后，系统地优化业务逻辑，直到它能够容忍重复并顺利通过测试。使用 [duplicator](https://watermill.io/docs/middlewares/#duplicator) 处理程序中间件来克隆消息，并检查最终的程序状态与不使用 duplicator 运行测试时相同。

## 通过混沌工程证明原子性

一旦我们实现了幂等性，如何证明业务逻辑过程中每一步的原子性呢？

Watermill 理论上促进了至少一次的原子执行，但也有一些巧妙的方法可以规避它。如果您依赖底层原语，请务必在所有业务逻辑完成**之后**确认消息。并且，确保业务逻辑足够细粒度，以便在中断的情况下**所有内容**都重新运行。

一个简单的规则是：**一个事件处理程序中的所有状态更改都必须在同一个数据库事务中应用**。如果您有两个数据库事务，您将永远无法实现*持久执行*。如果您在事件处理程序内部发布另一个事件，那么该事件发布者必须与事件处理程序在同一个事务中操作。当在发布事件的同时对数据库进行任何额外更改时，[发件箱模式](https://threedots.tech/post/distributed-transactions-in-go/#the-outbox-pattern)至关重要。

如何通过测试证明原子性？编写一个混沌中间件，并将其与重试中间件配对用于您的测试设置：

```
func ApplyChaos(h message.HandlerFunc) message.HandlerFunc {
    failNextOperation := true

	return func(msg *message.Message) ([]*message.Message, error) {
		result, err := h(msg)
		if err != nil {
			return nil, err
		}

        failNextOperation = !failNextOperation
        if failNextOperation {
            return nil, errors.New("world chaos cancelled the event handler")
        }

        return result, nil
    }
}

```

这个中间件会有一半的时间中断事件处理程序。重试中间件应该确保即使系统一半出现中断，操作也能完成。

如何证明事件处理程序是原子的？编写另一个污染消息上下文的中间件：

```
func PolluteContextWithChaos(h message.HandlerFunc) message.HandlerFunc {
	return func(msg *message.Message) ([]*message.Message, error) {
        polluted, cancel := context.WithCancel(msg.Context())
        defer cancel()
        go func() {
            <-time.After(time.Millisecond)
            cancel() // simulate premature cancellation
        }()

        msg.SetContext()
        return h(msg)
	}
}

```

如果您的所有输入和输出操作都支持上下文（它们应该如此——这是最佳实践），那么提前的上下文取消将模拟事件处理程序内部的执行中断。这个简单的示例在毫秒后取消。

模拟各种伪随机取消模式。永远不要使用真正的随机数，因为它会使测试变得脆弱。检查输出是否相同，那么您就已经走在构建持久系统的正确道路上。

## 结论

业务应用程序需要*持久执行*。具有从几乎任何错误或崩溃中恢复的内在能力的程序令人愉快。持久性可以通过适当的系统设计和严格的测试纪律来实现。

您可以看到*持久执行*可能会很快变得复杂，但第一步是最简单的。**将输入事件写入持久卷。**它会立即为您提供一定的持久性。您可以稍后解决其余问题。Watermill 的 [SQLite Pub/Sub 后端](https://watermill.io/pubsubs/sqlite/)是尝试此方法的绝佳选择。这个新驱动程序**不需要 CGO**，并且与 Watermill 一样，是免费和开源的。

云提供商已经开始提供分布式 SQLite 集群，用于提供一定持久性和最快读取速度的用例。这些项目强烈表明，由 SQLite 提供支持的存储是实现*持久执行*的可行且日益理想的选择：

1.  [LiteFS](https://fly.io/docs/litefs/) 保留了所有经典的 SQLite 约定，例如单写入器约束。这让我们有充分的理由预期，未来即使使用全局事务，*持久执行*也能变得快速。
2.  [Turso](https://turso.tech/) 可以在连接不良的边缘或移动设备上舒适地运行。
3.  Cloudflare [持久对象](https://blog.cloudflare.com/sqlite-in-durable-objects/)是 Cloudflare Workers 的 SQLite 持久化伴侣。

与基于 SQLite Pub/Sub 的 Watermill 相比，这些商业产品有两个缺点：(1) 供应商锁定，以及 (2) 将数据库事务可靠地绑定到事件处理程序的一些困难。这意味着 Watermill 可能会让您在实现可证明的*持久执行*的道路上，超越持久性，进一步迈向幂等性和原子性。试一试吧！