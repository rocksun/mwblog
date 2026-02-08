<!--
title: Rust 异步编程：Pinning 机制深度解析
cover: https://cdn.thenewstack.io/media/2026/01/5157ef3e-rust.jpg
summary: 本文深入探讨了 Rust 异步编程中的 `Pin` 特性。它解释了自引用结构体在内存移动时可能导致的崩溃问题，以及 `Pin` 如何通过“固定”数据来保证内存安全和零成本 future。文章还区分了 `Unpin` 类型、栈固定与堆固定，并介绍了 `pin-project` crate。核心思想是，当数据指向自身时，`Pin` 是确保数据稳定性的关键。
-->

本文深入探讨了 Rust 异步编程中的 `Pin` 特性。它解释了自引用结构体在内存移动时可能导致的崩溃问题，以及 `Pin` 如何通过“固定”数据来保证内存安全和零成本 future。文章还区分了 `Unpin` 类型、栈固定与堆固定，并介绍了 `pin-project` crate。核心思想是，当数据指向自身时，`Pin` 是确保数据稳定性的关键。

> 译自：[Async Rust: Pinning demystified](https://thenewstack.io/async-rust-pinning-demystified/)
> 
> 作者：Anshul Gupta

*这是四部分系列文章中的第二篇。阅读第一部分：*[Rust 的异步如何与众不同（以及为何重要）](https://thenewstack.io/how-rust-does-async-differently-and-why-it-matters/)*

在本系列文章的上一部分中，我们探讨了[Rust 异步引擎](https://thenewstack.io/async-rust-in-practice-performance-pitfalls-profiling/)的“拉取式”模型。我们看到编译器如何将异步函数转换为惰性状态机，这些状态机只有在被执行器轮询时才会取得进展。

然而，如果您仔细查看我们为 `CountdownFuture` 实现的 poll 方法签名，您可能会注意到 `self` 周围有一个特殊的包装器：

```
fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>
```

在第一部分中，我们关注了逻辑——一个 future 如何决定它是 `Ready` 还是 `Pending`。在这篇文章中，我们将把重点转向物理。

对于那些[学习异步 Rust](https://thenewstack.io/async-programming-in-rust-understanding-futures-and-tokio/) 的人来说，Pin 常常是最令人生畏的话题，但它却是实现零成本 futures 的关键“秘密武器”。它确保了当我们的状态机完成一半操作时，它不会突然移动到内存中的新位置并破坏其持有的每个内部引用。

## **1. 问题：移动不可移动之物**

在 Rust 中，默认情况下每种类型都是可移动的。无论您将变量传递给函数还是将其赋给一个新名称，Rust 都会执行位复制 (memcpy)。对于 99% 的类型来说，这是高效且安全的。但对于自引用结构体来说，这将是一场灾难。

想象一个结构体，其中一个字段是指向其内部另一个字段的指针：

```
struct SelfReferential {
    data: String,
    pointer_to_data: *const String,
}
```

如果您将此结构体移动到新的内存地址，`data` 会随之移动。然而，`pointer_to_data` 仍然包含旧的内存地址。它现在是一个悬空指针。访问它将导致未定义行为。

### **异步连接：一个具体示例**

为了理解这对于异步 Rust 的重要性，我们必须看看编译器如何处理 `.await` 点。当您编写一个异步函数时，编译器会将其转换为一个结构体，该结构体存储您函数的“捕获”状态。

考虑这段看起来无害的代码：

```
async fn process_data() {
    let val = String::from("Hello"); 
    let val_ref = &val;              // A reference to a local variable   
    some_async_operation().await;    // The function "pauses" here
    
    println!("{}", val_ref);         // The reference is used after the pause
}
```

### **“降级”的状态机**

在内部，编译器会生成一个结构体来保存这些变量，以便它们在函数暂停时仍然存在。它大致如下所示：

```
struct ProcessDataFuture {
    val: String,
    val_ref: *const String, // Points to 'val' inside this same struct!
    state: State,
}
```

### **内存灾难（“移动”）**

这就是数据物理位置变得至关重要的地方。让我们看看如果我们在 future 启动后移动它，内存中会发生什么。

1. **移动前（在** **.await** **点）：**

* future 位于地址 0x1000。
* `val`（字符串）位于地址 0x1008。
* `val_ref`（指针）正确存储值 0x1008。

2. **移动：**

您移动 future（可能通过将其推入 Vec 或将其移动到另一个线程）。

* future 现在位于地址 0x2000。
* `val` 已随结构体移动，现在位于地址 0x2008。

3. **崩溃：**

* `val_ref` 仍然存储值 0x1008。
* 当执行器恢复 future 并尝试使用 `val_ref` 时，它会回到地址 0x1008，那里现在是垃圾内存。崩溃。

### **Pin 如何化险为夷**

当执行器轮询这个 future 时，它不仅仅是获取一个普通引用；它需要一个 `Pin<&mut Self>`。

通过固定 (`pinning`) `ProcessDataFuture`，我们实际上是在告诉 CPU：“这个结构体现在锚定在地址 0x1000。在它完成之前，移动它是非法的。” 由于结构体保证停留在 0x1000，内部指针 `val_ref`（指向 0x1008）在整个操作生命周期内都保持有效。这是 Rust 能够安全地允许您在 `.await` 点之间引用局部变量的唯一方法。

## **2. Pin<P> 到底是什么**

一个常见的误解是 `Pin` 是一种新的指针类型。它不是。`Pin` 是一个现有指针（如 `&mut T` 或 `Box<T>`）的包装器。

它充当与编译器的法律合同：“此指针指向的数据在调用其 drop 方法之前，绝不会再次移动。”

* **解剖：** 您可以移动 `Pin` 包装器本身（例如交换两个 `Pin<Box<T>>` 变量），但您不能移动它内部的 `T`。
* **稳定性：** 把它想象成地基。一旦地基浇筑好，你就不能移动房子；你只能拆除它（`Drop`）。

## **3. Unpin 标记 trait**

为什么 `Pin<&mut i32>` 仍然允许您移动整数？这是因为 `Unpin` trait。

* **自动实现：** Rust 中几乎所有类型（`i32`、`String`、`Vec`）都自动实现了 `Unpin`。即使这些类型被 `Pin` 包装，它们也“安全”地可以移动。
* **!Unpin 的作用：** *不*安全移动的类型（如自引用结构体或编译器生成的 futures）被标记为 `!Unpin`。
* **区别：** 如果 `T: Unpin`，那么 `Pin<P<T>>` 的行为与普通指针完全相同。固定逻辑仅在底层类型为 `!Unpin` 时才“激活”。

## **4. 栈固定与堆固定**

您有两种主要方式将值锚定在内存中，每种方式都有不同的权衡：

### **堆固定 (****Box::pin****)**

这是一种“安全且简单”的方法。当您使用 `Box::pin(value)` 时，数据会被移动到堆上。由于堆分配在其整个生命周期内都具有稳定的地址，因此固定是微不足道的。

* **优点：** 易于使用，无需 `unsafe`。
* **缺点：** 需要堆分配（性能成本）。

### **栈固定 (****pin!****)**

您可以使用 `std::pin::pin!` 宏将值固定到当前栈帧。

* **优点：** 零成本，无堆分配。
* **缺点：** 固定值不能超过当前函数的生命周期。它比堆固定更具限制性。

## **5. 现代工具：pin-project crate**

手动访问固定结构体字段（称为 Pin Projection）是出了名的难以安全完成，因为它通常需要 `unsafe` 代码。行业标准是使用 `pin-project` crate。

它允许您安全地将固定引用从结构体“投影”到其各个字段，而无需编写一行 `unsafe` 代码：

**实际示例：可重试的 future**

以下是如何实现一个包装器，该包装器会在达到一定限制之前重试失败的 future。请注意 `#[pin]` 如何允许我们安全地处理内部 future，即使它是 `!Unpin`。

```
use std::pin::Pin;
use std::task::{Context, Poll};
use std::future::Future;
use pin_project::pin_project;

#[pin_project]
pub struct Retry<F, Fut> {
    // A factory function to create a new instance of the future for each retry
    factory: F,
    // The current future attempt we are polling
    #[pin]
    active_fut: Fut,
    retries_left: usize,
}

impl<F, Fut, T, E> Future for Retry<F, Fut>
where
    F: Fn() -> Fut,
    Fut: Future<Output = Result<T, E>>,
{
    type Output = Result<T, E>;

    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        let mut this = self.project();

        match this.active_fut.as_mut().poll(cx) {
            // If it succeeded, or we're out of retries, return the result
            Poll::Ready(Ok(val)) => Poll::Ready(Ok(val)),
            Poll::Ready(Err(e)) => {
                if *this.retries_left > 0 {
                    *this.retries_left -= 1;
                    println!("Future failed. Retries remaining: {}", this.retries_left);
                    
                    // Reset the state: Create a new future and poll it
                    let new_fut = (this.factory)();
                    this.active_fut.set(new_fut);
                    
                    // We must poll again to register the new waker
                    cx.waker().wake_by_ref();
                    Poll::Pending
                } else {
                    Poll::Ready(Err(e))
                }
            }
            Poll::Pending => Poll::Pending,
        }
    }
}
```

## **6. `Pin` 速查表**

| 类型属性 | 是否被 Pin 包装？ | 可以移动吗？ |
| --- | --- | --- |
| `Unpin` (例如 `i32`) | 否 | **是** |
| `Unpin` (例如 `i32`) | 是 | **是** (Pin 被忽略) |
| `!Unpin` (自引用) | 否 | **是** (危险！⚠️) |
| `!Unpin` (自引用) | **是** | **否** (安全 ✅) |

## **结论**

`Pin` 是一个无形的锚点，它使得 Rust 的异步引擎既安全又零成本。虽然它一开始感觉像一个复杂的学术概念，但归结为一个简单的规则：如果数据指向自身，它就必须保持原位。

通过理解 `Pin`、`Unpin` 和内存地址之间的关系，您现在能够自信地处理复杂的异步状态机和自定义 [futures](https://thenewstack.io/microsofts-1m-vote-of-confidence-in-rusts-future/)。

## **下一步：构建引擎**

既然我们理解了逻辑（第一部分：状态机）和物理（第二部分：固定），现在是时候实际运行我们的代码了。

future 只是内存中休眠的数据；它本身不会做任何事情。它需要一个引擎来驱动。在**第三部分**中，我们将从头开始构建一个自定义异步运行时。

我们将探讨：

* **执行器：** 协调轮询的循环。
* **唤醒器：** future 如何告诉执行器“我准备好再次尝试了！”而不会浪费 CPU 周期。
* **反应器：** 我们如何弥合操作系统级事件（如网络 I/O）与 Rust 状态机之间的鸿沟。