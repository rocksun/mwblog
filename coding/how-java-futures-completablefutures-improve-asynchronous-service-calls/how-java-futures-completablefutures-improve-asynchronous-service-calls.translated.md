# Java Futures 和 CompletableFutures 如何改进异步服务调用

![Java Futures 和 CompletableFutures 如何改进异步服务调用特写图像](https://cdn.thenewstack.io/media/2024/03/2f10bcd3-service-calls-2-1024x576.jpg)

企业级分布式编程可能是一项艰巨的任务。与在单个本地计算环境范围内使用资源的应用程序不同，分布式应用程序根据定义使用外部位置的服务。有时，这些外部服务在近距离的另一台计算机上运行；而其他时候，这些服务在云端运行，机器可能在任何地方。

这意味着对这些服务的调用在响应方面是不可预测的。调用可能在预期毫秒数内执行。或者在最坏的情况下，调用可能需要数分钟，甚至数小时。因此，编写阻塞代码只是等待外部调用完成是不好的做法，尤其是在应用程序在运行期间可能进行数百次外部调用时。

更好的解决方案是使用一种技术，该技术能够编写非阻塞代码，异步地进行外部调用，仅在调用完成后才收到通知。通俗地说，这种技术可以被认为是“先触发，稍后通知我”。

在 [Java](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/)中，实现这种异步交互的技术称为 Future，这是本文的主题。

我将简要概述 Java Future 接口和实现该接口的 CompletableFuture 类。我将演示 Future 的非阻塞特性，然后展示如何使用一组 CompletableFutures 创建非阻塞代码链。最后，我将演示如何并行运行一组非阻塞 CompletableFutures。

本文还附带 [GitHub 上的一个存储库，其中包含所有演示代码](https://github.com/reselbob/SimpleFuturesDemo)以及有关如何运行它的说明。

我将在三个示例中演示的用例是一个旅行场景，其中进行航空公司、酒店和汽车租赁预订。第一个和第二个示例按顺序进行预订。第三个示例同时进行预订。但是，在我深入了解详细信息之前，我将解释 Java Future 接口和实现该接口的 CompletableFuture 类的基础知识。

为了充分受益于阅读本文，最好有一些 [Java 编程](https://thenewstack.io/java-adapts-to-cloud-native-computing/)经验和对 [Java 线程](https://thenewstack.io/why-debugging-doesnt-need-to-be-so-complex-or-outdated/)的基本了解。

## Futures 和 CompletableFutures 101

[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)是一个 Java 接口，它定义了以下方法：

| 返回类型 | 方法名称 | 说明 |
|---|---|---|
| 布尔值 | cancel(boolean mayInterruptIfRunning) | 尝试取消 future，成功时返回 true。 |
| V，结果的类型 | get() | 等待异步代码完成，然后返回结果。 |
| V，结果的类型 | get(long timeout, TimeUnit unit)) | 仅等待 timeout 参数定义的时间段。 |
| 布尔值 | isCancelled() | 尝试取消异步代码的执行，成功时返回 true。 |
| 布尔值 | isDone() | 当异步代码完成时返回 true。 |

Future 提供的好处是，接口指定的方法使使用异步代码变得更容易。例如，如果你想知道 Future 的实例是否仍在运行，则调用 isDone() 方法。如果你想获取运行异步代码的 Future 实例的结果，则调用 get() 方法。事情变得更加明显。你无需处理 Future 下面的线程。你只需使用 Future。

[CompletableFuture](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html)是一个 Java 类，它实现了 Future 接口中指定的方法，但还有许多其他方法，为异步代码编程增加了更多功能和多功能性。正如以下演示示例所示， CompletableFuture 类使 Futures 能够链接以及并行运行。

使用 Futures 和 CompletableFutures 进行编码的详细信息显示在以下三个示例中。如前所述，所有三个示例都模拟了一个旅行场景，代表用户进行航空公司、酒店和汽车租赁预订。定义预订的代码在名为 Reservation 的类中描述，如清单 1 所示。

**清单 1：**

Reservation 类包含所有预订使用的等待逻辑。

请注意，
## Reservation 类

Reservation 类由 reservation 的所有实例使用，它有一个名为 `makeReservation(String travelService)` 的方法。

`makeReservation(String travelService)` 有一个 `Thread.sleep()` 语句（清单 1，第 3 行），它模拟了进行预订所需的时间段。

`makeReservation(String travelService)` 在 Reservation 类的航空公司、酒店和汽车租赁实例上异步调用。进行这些调用的情况会因用例而异。

### 顺序运行 Futures

本节介绍按顺序运行航空公司、酒店和汽车租赁预订。每个预订都表示为一个 Future。

![](https://cdn.thenewstack.io/media/2024/03/cd63d425-java-graphic-1-573x1024.png)

**图 1：**按顺序执行一组 Futures。

对 Futures 序列进行编程的逻辑在下面的清单 2 中以代码形式显示。此外，该代码还具有检查正在运行的 Future 以查看其是否“完成”的逻辑。花点时间查看清单 2 中的代码。然后我将讨论一些更有趣的细节。

**清单 2：**按顺序运行 Futures 的代码。

如前所述，清单 2 中的代码创建了航空公司、酒店和汽车租赁预订。每个预订都在一个专用的 Future 中运行。给定的 Future 在由清单 2 中第 7 行创建的 ExecutorService 实例提供的线程中运行。

第一个 Future，即航空公司预订，在第 10 行通过 `Executor.submit()` 方法创建。

`Executor.submit()` 采用一个 lambda 表达式作为参数，该表达式封装了 Reservation 对象的创建，该对象调用实例的 `makeReservation()` 方法。

`Executor.submit()` 返回对航空公司预订的 Future 的引用。

航空公司预订 Future 名为 `airlineFuture`，现在正在运行。

第 13 行的代码创建了一个 while 循环，该循环一直运行到 `airlineFuture.isDone()` 返回 true。运行 while 循环的目的是演示 `Future.isDone()` 的工作原理，

请注意，while 循环中的代码在第 15 行调用 `Thread.sleep(300)`。对 `Thread.sleep()` 的调用将 while 循环的执行延迟了三分之一秒。回到本文开头的清单 1，回想一下预订需要一秒钟才能运行。因此，正在发挥作用的整体逻辑是，在预订完成之前，while 循环将运行四次。这展示了使用 `Future.isDone()` 的强大功能。

`Future.isDone()` 提供了一种简单的方法来检查正在运行的 Future 的状态。

请看下面的清单 3，它显示了清单 2 中运行的代码的控制台输出。来自运行 `airlineFuture.isDone()` 的 while 循环的四行输出提供了上面代码清单中所述逻辑的证据。

此外，返回到上面的清单 2，并注意第 18 行对 `airlineFuture.get()` 的调用。对 `airlineFuture.get()` 的调用在 Future 完成后返回异步运行的 Future 的结果。清单 3 中下面显示的对 `airlineFuture.get()` 的调用的返回是 *Result: Airline is confirmed at 2024-02-27 08:20:37*。

请注意，从 `airlineFuture.get()` 返回的时间是 2024-02-27 08:20:37，但对 `airlineFuture.isDone()` 的四次调用发生在 08:20:37 之前的第二秒。这是进一步的证据，表明对 `Future.isDone()` 的调用将检查 Future，即使它异步运行到调用线程也是如此。

**清单 3：**按顺序运行 Futures 的输出。

清单 2 中第 20-44 行显示的用于进行酒店和汽车租赁预订的代码类似于用于进行航空公司预订的代码。此外，输出也类似，如清单 3 中所示。

了解此演示的重要一点是，`Future.isDone()` 方法提供了一种检查正在运行的 Future 状态的方法，并且对 `Future.get()` 方法的调用将在 Future 完成后返回 Future 的结果，从而提供了一种按顺序运行一组 Futures 的方法。

但是，还有另一种按顺序运行 Futures 的方法。另一种方法是使用 CompletableFuture 类提供的增强功能来实现称为链接的技术。

### 链接的 CompletableFutures

链接 Futures 是一种技术，其中一系列 Futures 自动按顺序运行，而无需调用每个 Future 的 `.get()` 方法。此外，如果原始 Future 返回结果，则该结果将自动传递给后续 Future。

图 2 显示了使用 CompletableFuture 类链接 Futures 的基本概念。使用 CompletableFuture 类链接 Futures 的好处之一是，开发人员可以在链中同步或异步地运行任务。

![](https://cdn.thenewstack.io/media/2024/03/3ef7df44-java-graphic-2-1024x503.png)

**图 2：**在链中运行一系列 CompletableFutures。
**在演示示例中，链接一组 Future 涉及使用 CompletableFuture 类提供的众多[方法](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html#method.summary)中的几个。示例中使用的方法在下表中显示。**

| 方法 | 说明 |
|---|---|
| `.supplyAsync(lambda)` | 通过异步运行由 lambda 表达式封装的方法来启动链。 |
| `.thenAccept(result)` | 同步处理链中先前运行的方法的结果。 |
| `.thenApplyAsync(lambda)` | 通过异步运行由 lambda 表达式封装的方法来继续链。 |

花点时间查看下面清单 4 中的代码。然后，我将讨论有关使用 CompletableFuture 在链中顺序运行 Future 的一些有趣细节。

**清单 4：**用于在链接序列中运行一组 CompletableFuture<T> 的 Java 代码。

清单 4 中上面显示的链的工作方式是，旅行预订（在本例中为航空公司预订）使用静态 CompletableFuture.supplyAsync() 方法异步执行。

CompletableFuture.supplyAsync() 隐式创建 CompletableFuture 的一个实例。

此外，该方法采用两个参数，一个包含要异步运行的方法的 lambda 表达式，以及一个 ExecutorService 的实例，该实例将提供隐式 CompletableFuture 运行的线程。在清单 4 的第 7-15 行中，调用 CompletableFuture.supplyAsync() 启动链，该链继续使用一系列“then”语句运行。

第 16 行的第一个“then”语句是 `.thenAccept()`.

`.thenAccept()` 同步运行代码，接受先前运行的 CompletableFuture 的结果。由上一个 CompletableFuture 返回的值是类型为 String 的确认消息。

由于输出确认消息会对阻塞代码产生较小的影响，因此使用 `.thenAccept()` 是合适的。但是，链中的下一个行为是酒店预订，需要异步运行。因此，下一个“then”子句是 `.thenApplyAsync()`, 它也接受一个 lambda 表达式和一个 ExecutorService 的实例。（请参见清单 4，第 20-28 行。）

`.thenApplyAsync()` 创建一个隐式的 CompletableFuture。

一个同步的 `.thenAccept()` 子句随后处理处理酒店预订的 CompletableFuture 的确认消息。最后，执行另一个 `.thenApplyAsync()` 子句来处理租车预订。

下面的清单 5 显示了链的输出。请注意，航空公司、酒店和租车确认输出以一秒为间隔报告。这是因为预订需要一秒钟才能执行（如清单 1 所示）。清单 5 中的输出说明航空公司、酒店和租车正在按顺序执行和完成，正如 CompletableFutures 的链所预期的那样。

**清单 5：**在链接序列中运行一组 CompletableFuture<T> 的终端输出。

这些示例演示了航空公司、酒店和租车预订按顺序运行。但是，另一个可行的用例是所有预订的执行同时开始并并行运行。对这样的用例进行编码可能是一项艰巨的任务。幸运的是，CompletableFuture 类使并行运行异步代码变得更容易。

## 并行 CompletableFutures

图 3 是一个用例图，其中航空公司、酒店和租车预订作为 CompletableFutures 并行运行。

![](https://cdn.thenewstack.io/media/2024/03/81e1ec33-java-graphic-3-1024x453.png)

图 3：并行运行一组 CompletableFutures。

清单 6 中的代码演示了一组并行运行的 CompletableFutures。花点时间看看代码。然后，我将详细讨论关键方面。

**清单 6：**用于并行运行一组 CompletableFigure<T> 的 Java 代码。

首先要注意的是，清单 6 中的代码使用了一个名为 `. 的预订的新自定义类。类 [TimedReservation](https://github.com/reselbob/SimpleFuturesDemo/blob/main/src/main/java/futuresdemo/simple/TimedReservation.java) TimedReservation 有一个一秒的延迟，并将预订的开始和结束时间报告为控制台输出，精确到毫秒。（请参见第 11、22 和 34 行。）

在执行代码方面，请注意创建了三个 CompletableFutures。

airlineFuture 在第 11 行创建，
hotelFuture 在第 18 行创建，
carRentalFuture 在第 29 行创建。

然后，在第 20 行，调用静态方法 CompletableFuture.allOf()，提供 airlineFuture、hotelFuture 和 carRentalFuture 作为参数。这些 future 现在并行运行。

.allOf() 语句末尾的 .join() 调用使其代码等待所有 future 运行。

在第 43-45 行，对每个 future 调用 `.get()`.

.get() 调用的输出打印到控制台。下面的清单 7 显示了
**TimedReservation 类以及**

在清单 6 中的一般演示代码中的 `main()` 方法中。

**清单 7：**并行运行一组 `CompletableFuture<T>` 的终端输出。

请注意，航空公司、酒店和汽车租赁预订呼叫同时开始。还要注意，它们同时运行一秒钟。此输出显示所有三个 `CompletableFutures` 已并行运行，每个都在自己的线程中运行。它们同时开始，也按预期同时结束，这在以前缀术语 `Result:` 开头的输出行中有所指示。

## 将所有内容放在一起

在本文中，我简要概述了 `Future` 接口和 `CompletableFuture` 类。我采取了操作观点，展示了如何将异步代码作为一组独立的 `Future` 按顺序运行。此外，我还展示了如何使用 `CompletableFutures` 链按顺序运行异步代码。最后，我演示了如何并行运行一组 `CompletableFutures`。

当然，我展示了很多代码和分析。不过，这仅仅是个开始。还有很多东西要学，特别是关于构成 `CompletableFuture` 类的许多方法。

希望我在这里提供的信息能为你提供基本理解，让你能够继续利用 `Futures` 和 `CompletableFutures` 提供的强大功能和简单性。它们是引人注目的技术，将为你节省时间，并让你的 Java 异步编程工作变得更加轻松。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。