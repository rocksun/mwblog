**A DNS outage is like a flash flood. It hits you and disappears as if it were never there.** “It was probably the DNS” became a meme. But, half the time, we do not know the exact cause. The outage is seldom long enough to diagnose, sequester, replicate, simulate, and test the failure conditions. How can we be certain that this type of failure will not compromise our systems again in the future? The DNS can fail spectacularly in a variety of ways.

A better way to address intermittent failures, such as DNS outages, is to accept them as unavoidable occasional execution disruptions. We might not be able to address each of them exhaustively, but we can design our system to handle almost any interruption of its internal logic. **We can harden the system against the disruptions to attain *durable execution*.**

## What is Durable Execution?

*Durable execution* is a guarantee that a program output is correct regardless of failures anywhere in the execution process.

Competitive business applications require *durable execution*. When it is absent, an employee will spend an hour or two fixing each incorrect output when it is detected. In large business applications, incorrect output often goes undetected for weeks, resulting in expensive chaos around holidays.

Are we talking about bugs? No. Bugs are the program. Some intermittent bugs erode durability, but the durability loss is most often a result of an interruption of the execution process. The interruption can be caused by a network outage, service failure, security breach, or a delinquent update. All of those reasons are common. *Durable execution* does not care what caused it. It is a promise to recover from almost any failure or combination of failures and deliver the correct output.

Event-Driven Architecture (EDA) is the industry best practice for supporting *durable execution*. However, most EDA production systems are not provably durable. What happened?

In the second guest post on our blog, we welcome Dima Kotik, who contributed the SQLite Pub/Sub backend to Watermill.
Please give Dima a warm welcome! 🎉

*Miłosz & Robert*

There is a difference between a guarantee and a wish. A guarantee has some proof, a history of recovery from a variety of system crashes. It begins with emulating crash conditions in integration tests. After writing many such tests, you will realize a simple but profound principle: ***durable execution* begins with writing execution state into storage**. There is no other way to proceed, because anything present in random-access memory or ephemeral storage is liable to disappear if the system crashes.

The first step of a durable system is to stash its input **before any processing takes place** after parsing and validation. Security is more important than durability, so input validation takes precedence.

## Stash the Input After Parsing and Validation

Wait, what? I have to commit all the system input immediately into storage? Yes. Is that even possible? Not all at once, but this is not as daunting a task as one might imagine.

If you are using event-driven architecture with an publisher/subscriber management library like [Watermill](https://watermill.io/), you are already halfway there. Watermill is one of the most popular event buses in the Go ecosystem.

Watermill is an unusually flexible library in that it can bridge events from a large number of different backends. Your core business logic may stream events to a PostgreSQL database, and your input may initially be stored in a SQLite databases of your edge nodes to achieve durability without sacrificing performance. Watermill can link the two to tango together seamlessly.

Unfortunately, many business applications that utilize Watermill continue to use the Go channel ephemeral backend here and there despite the documentation urging developers not to do it. This backend is a basic in-memory implementation based on Go channels intended for testing purposes. The events are queued into an asynchronous channel. They will disappear when the system crashes. They will clog up the server with a long queue if the execution process slows down for any reason. They will compete for resources with a critical server process.

In other words, do not write input into random-access memory. You are asking for trouble.

There is an easy persistent drop-in replacement for an ephemeral backend. It is not a silver bullet, but it is an easy first step towards durable computing. Try the new [Watermill SQLite backend](https://watermill.io/pubsubs/sqlite/). It does not require setting up any additional infrastructure, and it is more performant and reliable than any other storage method because it does not need a network connection or a custom transport protocol. It writes to a file on a disk. **It does not require CGO**.

Suppose we are processing book orders, and we would like to store the orders as events in an SQLite database:

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

For cloud instances, ensure that you are writing the SQLite file to a persistent volume, which is mounted explicitly. The root file system is typically ephemeral. You may want to eventually migrate the collected input into your main database after thinking about performance implications.

The matching subscriber is not any different from normal Watermill usage other than the backend initialization:

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

The SQLite publisher and subscriber are drop-in replacements. **They can be also used without Watermill router.**
In other words, you can just use low-level `Publish` and `Subscribe` methods.

Full examples are provided in [documentation](https://watermill.io/pubsubs/sqlite/). Nothing else needs to change in your code to achieve this first step towards *durable execution*: write the input events to persistent storage.

For complete durability, however, the event handlers for each step of processing the book orders must have two provable qualities:

1. **Idempotency**: the handler can consume the same event multiple times without generating more than one downstream event.
2. **Atomicity**: the handler either completes successfully or fails completely. It must never succeed partially.

The combination of these properties with persistent storage ensures *durable execution*. When the a step in business logic fails for any reason, it is attempted again from the last safe system state.

## Prove Idempotency with Event Duplication

Idempotent event handlers must not change system state when processing identical events. In other words, any repetition of input any number of times makes no difference to the system. We can achieve this effect by de-duplicating events, but it is best that the program logic itself tolerates repetition.

First, ensure that the event message is acknowledged only after the all the business logic has been executed successfully:

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

What happens if the transaction succeeds but the message acknowledgment fails on line 16? If the handler is idempotent, the event will be reprocessed, but the system state will not change. An easy way to achieve this is to constrain the database table field `order_id` to be unique. Then, drop the error if it is caused by a unique constraint violation:

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

What if there are multiple SQL table key constraints? The best solution is to have an idempotency test in place. Then, methodically groom the business logic until it tolerates repetition and passes the test. Use [duplicator](https://watermill.io/docs/middlewares/#duplicator) handler middleware to clone messages and check that the final program state is the same as running the test without the duplicator.

## Prove Atomicity with Chaos Engineering

Once we achieve idempotency, how can we prove atomicity for every step of the business logic process?

At-least-once atomic execution is theoretically facilitated by Watermill, but there are subtle ways of subverting it. If you rely on low-level primitives, always acknowledge the message **after** all the business logic finishes. And, ensure that business logic is granular enough that **all of it** runs anew in case of an interruption.

A simple rule to follow is that **all state changes in one event handler must apply within the same database transaction**. If you have two database transactions, you will never achieve *durable execution*. If you are publishing another event inside the event handler, that event publisher must operate within the same transaction as the event handler. The [outbox pattern](https://threedots.tech/post/distributed-transactions-in-go/#the-outbox-pattern) is essential when making any additional changes to the database together with publishing the event.

How do you prove atomicity with a test? Write a chaos middleware to pair it with the retry middleware for your testing setup:

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

This middleware will break the event handlers half the time. The retry middleware should ensure that the operations complete even with half of the system experiencing outages.

How do you prove that an event handler is atomic? Write another middleware that pollutes the message context:

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

If all your input and output operations are context-aware (they should be - it is best practice), the premature context cancellation will simulate an execution interruption inside the event handler. This simple example cancels after one millisecond.

Simulate a variety of pseudo-random cancellation patterns. Never use true random, because it will make the tests brittle. Check that the output is the same, and you are well on your way to a durable system.

## Conclusion

Business applications need *durable execution*. Programs that have an innate ability to recover from almost any error or crash are a joy to work with. Durability can be achieved with proper system design and a rigorous testing discipline.

You can see how *durable execution* can get complicated quickly, but the first step is the easiest. **Write the input event to a persistent volume.** It will give you some durability right away. You can work out the rest of it later. [SQLite Pub/Sub backend](https://watermill.io/pubsubs/sqlite/) for Watermill is a great choice to try this. This new driver works **without CGO** and, like Watermill, is free and open source.

Cloud providers have begun to offer distributed SQLite clusters for use cases that offer some durability and the fastest possible read speeds. Those projects are a strong indicator that SQLite-powered storage is a viable and increasingly desirable option for *durable execution*:

1. [LiteFS](https://fly.io/docs/litefs/) keeps all the classic SQLite conventions like the single-writer constraint. This gives good reasons to anticipate that in the future *durable execution* could also become fast even with global transactions.
2. [Turso](https://turso.tech/) comfortably runs on edge or mobile devices with poor connectivity.
3. Cloudflare [durable objects](https://blog.cloudflare.com/sqlite-in-durable-objects/) are an SQLite persistence companion to Cloudflare Workers.

There are two disadvantages to those commerical offerings compared to Watermill over SQLite Pub/Sub: (1) the vendor lock-in and (2) some difficulties in binding database transactions to event handlers reliably. This means that Watermill might get you farther past persistence towards idempotency and atomicity on the journey to provable *durable execution*. Give it a try!