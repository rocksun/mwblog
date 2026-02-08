*This is the first of a four-part series.*

If you are coming from JavaScript, Python or Go, [Rust’s asynchronous model](https://thenewstack.io/using-rustlangs-async-tokio-runtime-for-cpu-bound-tasks/) can feel like a bit of a culture shock. In those languages, the runtime is a “black box” that just works. In Rust, the hood is wide open, and the engine looks very different.

Why learn this? Most developers “use” [async](https://thenewstack.io/3-types-of-asynchronous-programming/). Very few understand it. By peeling back the [layers of Rust’s implementation,](https://thenewstack.io/why-your-rust-adoption-will-probably-fail-and-how-to-beat-the-odds/) you aren’t just learning a language; you’re learning how systems work at the architectural level. You’ll move from wondering why the compiler is complaining about lifetimes to intuitively understanding how your code is being transformed into a high-performance machine.

**This four-part series will explore:**

* **Part I: The poll-based model** (This article) **–** A look at why Rust futures are “lazy,” how the “pull” model differs from other languages, and how to build a state machine by hand.
* **Part II: The mystery of pinning –** It will demystify Pin, explain self-referential structs, and see why “moving” a future in memory can be dangerous.
* **Part III: Executors and wakers –** A dive into the “reactors” that drive code, exploring how the waker tells the executor exactly when to wake up and finish the job.
* **Part IV: Async in practice –** Moving beyond theory to look at real-world patterns like joining, selecting and handling timeouts.

## **1. The ‘pull’ model: Laziness as a virtue**

In many languages, async operations are “push-based.” When you create a promise in JavaScript or spawn a Goroutine in Go, the operation starts immediately. The runtime schedules it, and it pushes the result to you when it’s done.

Rust futures are “pull-based.” They are lazy**.**

If you call an async function in Rust but don’t `.await` it (or poll it), absolutely nothing happens. The code inside the function is not executed.

### **Code example: The lazy future**

```

use std::time::Duration;

async fncomplex_calculation() {
println!("(2) Starting calculation...");
tokio::time::sleep(Duration::from_secs(1)).await;
println!("(3) Calculation finished!");
}

#[tokio::main]
async fnmain() {
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

Think of a Rust future as a state machine that is currently paused. It sits dormant in memory until an executor (the runtime) actively asks it, “Are you done yet?” This querying process is called polling.

The executor polls the future. If the future is waiting on I/O (like a network request), it returns `Pending` and yields control back to the executor, allowing other tasks to run. When the I/O is ready, the operating system notifies the executor, which then wakes up the future and polls it again.

## **2. The future trait: The engine under the hood**

At the core of this abstraction is the future trait. Simplified, it looks like this:

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

When you write an `async fn`, the Rust compiler automatically generates an anonymous struct for you that implements this trait. It transforms your linear code into a state machine, breaking the function at every `.await` point.

### **Building the state machine by hand**

We will create a CountdownFuture. It will:

* Start with a count (in this case, 3).
* Every time the runtime polls it, it decrements the count.
* If the count is not 0, it tells the runtime “I’m not done, ask me again” (returns `Pending`).
* If the count is 0, it says “I’m done!” (returns `Ready`).

```

use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};
use std::time::Duration;// 1. The State Machine
// This struct holds the state of our operation.
// In a generated async block, this would hold all your local variables.
structCountdownFuture {
count: u32,
}

impl CountdownFuture {
fnnew(count: u32) -> Self {
Self { count }
}
}

// 2. The Implementation
impl Future for CountdownFuture {
// This is what the future returns when it finishes.
typeOutput = String;

fnpoll(mutself: Pin<&mutSelf>, cx: &mut Context<'_>) -> Poll<Self::Output> {
// Access the inner count
ifself.count == 0 {
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
async fnmain() {
let countdown = CountdownFuture::new(3);

// The runtime will poll this ~4 times until it returns Ready
let result = countdown.await;

println!("{}", result);
}
```

## **3. Breaking down the magic**

Let’s break down exactly what is going on in that manual implementation.

### **The** **poll** **signature**

```

fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>)
```

* **Pin<&mut Self>**: This allows us to mutate our state (self.count -= 1). The Pin wrapper ensures we are safe to use even if we were self-referential (though we aren’t in this simple example).
* **Context**: This carries the waker. The waker is the most important part of the ecosystem. It is the “callback” mechanism.

### **The return values**

* **Poll::Ready(T)**: The contract is fulfilled. The value “T” is handed to the caller, and the future is dropped.
* **Poll::Pending**: The future says, “I cannot complete right now.”

### **The waker magic**

This is the specific line that confuses people:

```

cx.waker().wake_by_ref();
```

In a real-world scenario (like reading from a socket), you wouldn’t wake immediately. You would hand this waker to the operating system. The OS would trigger it later when data arrives.

In our simple countdown example, we don’t have an OS waiting for us. We just want to run again immediately. So we wake ourselves up. This tells the executor (Tokio) to put our task back at the end of the “Ready” queue instantly.

## **What about** **Pin****?**

You might have noticed the Pin type in the function signature above and wondered what exactly it does. While we briefly touched on it, Pin is one of the most complex (and misunderstood) topics in Rust.

Why does the compiler force us to use it? What happens if we move a future in memory while it’s running?

*Part II of this series will demystify Pin, explore self-referential structs and explain why pinning is the secret sauce that makes Rust’s zero-cost async possible.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/01/1f88f3d8-cropped-6d78e1e7-anshul-gupta-600x600.jpeg)

Anshul Gupta is a staff engineer at Meta, where he leads platform initiatives in the Data Infra team to support large-scale data engineering and data pipeline authoring within Meta’s data warehouse. His work focuses on building scalable, resilient infrastructure for...

Read more from Anshul Gupta](https://thenewstack.io/author/anshul-gupta/)