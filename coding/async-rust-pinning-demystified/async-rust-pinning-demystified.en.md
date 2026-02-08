*This is the second of a four-part series. Read Part 1:* *[How Rust does Async differently (and why it matters)](https://thenewstack.io/how-rust-does-async-differently-and-why-it-matters/)*

In the previous part of this series, we explored the “pull-based” model of [Rust’s asynchronous engine](https://thenewstack.io/async-rust-in-practice-performance-pitfalls-profiling/). We saw how the compiler transforms async functions into lazy state machines that only make progress when polled by an executor.

However, if you looked closely at the poll method signature we implemented for our `CountdownFuture`, you might have noticed a peculiar wrapper around `self`:

```

fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>
```

In Part I, we focused on the logic — how a future decides whether it is `Ready` or `Pending`. In this post, we are shifting our focus to physics.

Pin is often the most intimidating topic for those [learning async Rust](https://thenewstack.io/async-programming-in-rust-understanding-futures-and-tokio/), yet it is the critical “secret sauce” that makes zero-cost futures possible. It ensures that when our state machine is halfway through an operation, it doesn’t suddenly move to a new location in memory and break every internal reference it holds.

## **1. The problem: Moving the unmovable**

In Rust, every type is movable by default. Whether you pass a variable into a function or assign it to a new name, Rust performs a bitwise copy (memcpy). For 99% of types, this is efficient and safe. But for self-referential structs, it is a disaster.

Imagine a struct where one field is a pointer to another field within itself:

```

struct SelfReferential {
    data: String,
    pointer_to_data: *const String,
}
```

If you move this struct to a new memory address, data moves with it. However, `pointer_to_data` still contains theold memory address. It is now a dangling pointer. Accessing it will cause undefined behavior.

### **The async connection: A concrete example**

To understand why this matters for async Rust, we have to look at how the compiler treats an `.await` point. When you write an async function, the compiler transforms it into a struct that stores the “captured” state of your function.

Consider this innocent-looking code:

```

async fn process_data() {
    let val = String::from("Hello"); 
    let val_ref = &val;              // A reference to a local variable   
    some_async_operation().await;    // The function "pauses" here
    
    println!("{}", val_ref);         // The reference is used after the pause
}
```

### **The ‘lowered’ state machine**

Internally, the compiler generates a struct to hold those variables so they survive while the function is paused. It looks roughly like this:

```

struct ProcessDataFuture {
    val: String,
    val_ref: *const String, // Points to 'val' inside this same struct!
    state: State,
}
```

### **The memory disaster (the ‘move’)**

This is where the physical location of your data becomes critical. Let’s look at what happens in memory if we move this future after it has started.

1. **Before move (At the** **.await** **point):**

* The future is located at address0x1000.
* `val` (the string) is at address 0x1008.
* `val_ref` (the pointer) correctly stores the value 0x1008.

2. **The move:**

You move the future (perhaps by pushing it into a Vec or moving it to another thread).

* The future is now at address 0x2000.
* `val` has moved with the struct and is now at address 0x2008.

3. **The crash:**

* `val_ref` still stores the value 0x1008.
* When the executor resumes the future and tries to use `val_ref`, it reaches back to address 0x1008, which is now garbage memory. Boom.

### **How** **Pin** **saves the day**

When the executor polls this future, it doesn’t just take a normal reference; it requires a `Pin<&mut Self>`.

By pinning the `ProcessDataFuture`, we are effectively telling the CPU: “This struct is now anchored at address 0x1000. It is illegal to move it until it is finished.*“* Because the struct is guaranteed to stay at 0x1000, the internal pointer `val_ref` (pointing to 0x1008) remains valid for the entire life of the operation. This is the only way Rust can safely allow you to have references to local variables across `.await` points.

## **2. What** **Pin<P>** **actually is**

A common misconception is that `Pin` is a new pointer type. It isn’t. `Pin` is a wrapper around an existing pointer (like `&mut T` or `Box<T>`).

It acts as a legal contract with the compiler: “The data pointed to by this pointer will never be moved again until its drop method is called.”

* **The anatomy:** You can move the `Pin` wrapper itself (such as swapping two `Pin<Box<T>>` variables), but you cannot move the `T` sitting inside it.
* **Stability:** Think of it like a foundation. You can’t move a house once the foundation is poured; you can only demolish it (`Drop`).

## **3. The** **Unpin** **marker trait**

Why does `Pin<&mut i32>` still allow you to move the integer? This is because of the `Unpin` trait.

* **Auto-implemented:** Almost every type in Rust (`i32`, `String`, `Vec`) automatically implements `Unpin`. These types are “safe” to move even if they are wrapped in a `Pin`.
* **The role of** **!Unpin****:** Types that are *not* safe to move (like self-referential structs or compiler-generated futures) are marked as `!Unpin`.
* **The distinction:** If `T: Unpin`, then `Pin<P<T>>` behaves exactly like a normal pointer. The pinning logic only “activates” when the underlying type is `!Unpin`.

## **4. Stack pinning vs. heap pinning**

You have two main ways to anchor a value in memory, each with different trade-offs:

### **Heap pinning (****Box::pin****)**

This is the “safe and easy” route. When you use `Box::pin(value)`, the data is moved onto the heap. Since heap allocations have a stable address for their entire lifetime, pinning is trivial.

* **Pros:** Easy to use, no `unsafe` required.
* **Cons:** Requires a heap allocation (performance cost).

### **Stack pinning (****pin!****)**

You can pin a value to the current stack frame using the `std::pin::pin!` macro.

* **Pros:** Zero-cost, no heap allocation.
* **Cons:** The pinned value cannot outlive the current function. It is much more restrictive than heap pinning.

## **5. Modern tooling: The** **pin-project** **crate**

Manually accessing fields of a pinned struct (called Pin Projection) is notoriously difficult to do safely because it often requires `unsafe` code. The industry standard is to use the `pin-project` crate.

It allows you to safely “project” a pinned reference from a struct down to its individual fields without writing a single line of `unsafe` code:

**Practical example: The retryable future**

Here is how you implement a wrapper that retries a failing future up to a certain limit. Note how `#[pin]` allows us to safely handle the inner future even if it’s `!Unpin`.

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

## **6. The `Pin` cheat sheet**

|  |  |  |
| --- | --- | --- |
| **Type Property** | **Wrapped in Pin?** | **Can it move?** |
| **`Unpin`** (e.g. `i32`) | No | **Yes** |
| **`Unpin`** (e.g. `i32`) | Yes | **Yes** (Pin is ignored) |
| **`!Unpin`** (Self-ref) | No | **Yes** (Danger! ⚠️) |
| **`!Unpin`** (Self-ref) | **Yes** | **No** (Safe ✅) |

## **Conclusion**

`Pin` is the invisible anchor that allows Rust’s async engine to be both safe and zero-cost. While it feels like a complex academic concept at first, it boils down to one simple rule: If data points to itself, it must stay put.

By understanding the relationship between `Pin`, `Unpin`, and memory addresses, you are now equipped to handle complex async state machines and custom [futures with confidence](https://thenewstack.io/microsofts-1m-vote-of-confidence-in-rusts-future/).

## **What’s next: Building the engine**

Now that we understand the logic (Part I: state machines) and the physics (Part II: Pinning), it’s time to actually run our code.

A future is just a dormant piece of data sitting in memory; it doesn’t do anything on its own. It needs an engine to drive it. In **Part III**, we will build a custom async runtime from scratch.

We will explore:

* **The executor:** The loop that orchestrates polling.
* **The waker:** How a future tells the executor, “I’m ready to try again!” without wasting CPU cycles.
* **The reactor:** How we bridge the gap between OS-level events (like network I/O) and our Rust state machines.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/01/1f88f3d8-cropped-6d78e1e7-anshul-gupta-600x600.jpeg)

Anshul Gupta is a staff engineer at Meta, where he leads platform initiatives in the Data Infra team to support large-scale data engineering and data pipeline authoring within Meta’s data warehouse. His work focuses on building scalable, resilient infrastructure for...

Read more from Anshul Gupta](https://thenewstack.io/author/anshul-gupta/)