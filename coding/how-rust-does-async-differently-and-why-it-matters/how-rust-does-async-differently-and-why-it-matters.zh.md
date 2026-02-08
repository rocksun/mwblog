*这是四部曲系列的第一部分。*

如果你来自 JavaScript、Python 或 Go，[Rust 的异步模型](https://thenewstack.io/using-rustlangs-async-tokio-runtime-for-cpu-bound-tasks/)可能会让你感到有些文化冲击。在这些语言中，运行时是一个“黑盒”，它开箱即用。而在 Rust 中，引擎盖是完全打开的，内部看起来非常不同。

为什么要学习这个？大多数开发者“使用”[异步](https://thenewstack.io/3-types-of-asynchronous-programming/)。很少有人理解它。通过揭开[Rust 实现的层层面纱](https://thenewstack.io/why-your-rust-adoption-will-probably-fail-and-how-to-beat-the-odds/)，你不仅在学习一门语言；你还在学习系统如何在架构层面工作。你将从疑惑编译器为何抱怨生命周期，转变为直观地理解你的代码是如何被转换成一台高性能机器的。

**这个四部曲系列将探讨：**

*   **第一部分：基于轮询的模型** (本文) **–** 探讨 Rust 的 Future 为何是“惰性”的，“拉取”模型与其他语言有何不同，以及如何手动构建状态机。
*   **第二部分：Pin 的奥秘 –** 它将揭开 Pin 的神秘面纱，解释自引用结构体，并说明为什么在内存中“移动”一个 Future 可能会很危险。
*   **第三部分：执行器和唤醒器 –** 深入驱动代码的“反应器”，探索唤醒器如何精确地告诉执行器何时唤醒并完成任务。
*   **第四部分：异步编程实践 –** 超越理论，探讨连接、选择和处理超时等实际模式。

## **1. “拉取”模型：惰性是一种美德**

在许多语言中，异步操作是“基于推送”的。当你在 JavaScript 中创建 Promise 或在 Go 中生成 Goroutine 时，操作会立即开始。运行时调度它，并在完成后将结果推送给你。

Rust 的 Future 是“基于拉取”的。它们是惰性的**。**

如果你在 Rust 中调用一个异步函数但没有 `.await` 它（或轮询它），什么都不会发生。函数内部的代码不会执行。

### **代码示例：惰性 Future**

```
use std::time::Duration;

async fn complex_calculation() {
    println!("(2) Starting calculation...");
    tokio::time::sleep(Duration::from_secs(1)).await;
    println!("(3) Calculation finished!");
}

#[tokio::main]
async fn main() {
    println!("(1) Calling the function...");

    // ⚠️ NOTHING HAPPENS HERE
    // The function is called, but the code inside isn't executed yet.
    // It returns a 'Future' state machine.
    let my_future = complex_calculation();

    println!("(4) I haven't awaited it yet, so nothing printed above.");

    // 🚀 NOW the runtime starts pulling the future
    my_future.await;
}
```

将 Rust 的 Future 想象成一个当前暂停的状态机。它在内存中处于休眠状态，直到执行器（运行时）主动询问它：“你完成了吗？” 这个查询过程称为轮询。

执行器轮询 Future。如果 Future 正在等待 I/O（如网络请求），它会返回 `Pending` 并将控制权交还给执行器，允许其他任务运行。当 I/O 准备就绪时，操作系统会通知执行器，执行器随后唤醒 Future 并再次轮询它。

## **2. Future Trait：引擎盖下的秘密**

这种抽象的核心是 Future Trait。简化后，它看起来像这样：

```
pub trait Future {
    type Output;
    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>;
}

pub enum Poll<T> {
    Ready(T),
    Pending,
}
```

当你编写一个 `async fn` 时，Rust 编译器会自动为你生成一个实现此 Trait 的匿名结构体。它将你的线性代码转换为一个状态机，在每个 `.await` 点中断函数。

### **手动构建状态机**

我们将创建一个 `CountdownFuture`。它将：

*   从一个计数开始（本例中为 3）。
*   每当运行时轮询它时，它会递减计数。
*   如果计数不为 0，它会告诉运行时“我还没完成，请再问我一次”（返回 `Pending`）。
*   如果计数为 0，它会说“我完成了！”（返回 `Ready`）。

```
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};
use std::time::Duration;
// 1. The State Machine
// This struct holds the state of our operation.
// In a generated async block, this would hold all your local variables.
struct CountdownFuture {
    count: u32,
}

impl CountdownFuture {
    fn new(count: u32) -> Self {
        Self { count }
    }
}

// 2. The Implementation
impl Future for CountdownFuture {
    // This is what the future returns when it finishes.
    type Output = String;

    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        // Access the inner count
        if self.count == 0 {
            // BASE CASE: We are done!
            return Poll::Ready("Blastoff! 🚀".to_string());
        } else {
            // PROGRESS CASE: We are not done yet.
            println!("Counting down: {}", self.count);

            // Decrement our state
            self.count -= 1;

            // ⚠️ CRITICAL STEP: The Waker
            // If we returned Pending without doing this, the runtime would
            // put this task to sleep and NEVER check it again (a deadlock).
            // By calling `wake_by_ref()`, we tell the runtime:
            // "I made progress! Put me back in the queue to be polled again immediately."
            cx.waker().wake_by_ref();

            // Return Pending to yield control back to the executor
            return Poll::Pending;
        }
    }
}

// 3. Using it
#[tokio::main]
async fn main() {
    let countdown = CountdownFuture::new(3);

    // The runtime will poll this ~4 times until it returns Ready
    let result = countdown.await;

    println!("{}", result);
}
```

## **3. 揭秘魔法**

让我们详细分析一下手动实现中发生的事情。

### **`poll` 签名**

```
fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>)
```

*   **Pin<&mut Self>**: 这允许我们修改状态 (`self.count -= 1`)。Pin 封装器确保即使我们是自引用的（尽管在这个简单示例中不是），我们也能安全使用。
*   **Context**: 这承载着唤醒器（waker）。唤醒器是生态系统中最重要的一部分。它是“回调”机制。

### **返回值**

*   **Poll::Ready(T)**: 契约已履行。值 “T” 被交给调用者，Future 被丢弃。
*   **Poll::Pending**: Future 说：“我现在无法完成。”

### **唤醒器魔法**

这条特殊的代码行经常令人困惑：

```
cx.waker().wake_by_ref();
```

在实际场景中（例如从套接字读取），你不会立即唤醒。你会将这个唤醒器交给操作系统。操作系统会在数据到达时稍后触发它。

在我们简单的倒计时示例中，我们没有等待操作系统的通知。我们只是想立即再次运行。所以我们唤醒自己。这会告诉执行器 (Tokio) 立即将我们的任务放回“就绪”队列的末尾。

## **那么** **Pin**** 呢？**

你可能已经注意到上面函数签名中的 `Pin` 类型，并想知道它到底有什么作用。虽然我们简要地提到了它，但 `Pin` 是 Rust 中最复杂（也是最容易被误解）的话题之一。

为什么编译器强制我们使用它？如果在 Future 运行时我们在内存中移动它会发生什么？

*本系列的第二部分将揭开 Pin 的神秘面纱，探索自引用结构体，并解释为什么 Pin 是使 Rust 的零成本异步成为可能的核心秘诀。*