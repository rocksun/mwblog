# 捕捉性能回归：进化的 eBPF 程序

介绍如何使用映射（maps）在 eBPF 程序和用户空间程序之间进行通信。

翻译自 [Catch Performance Regressions: Evolving eBPF Program ](https://thenewstack.io/catch-performance-regressions-evolving-ebpf-program/) 。

![](https://cdn.thenewstack.io/media/2023/07/985c56c6-bees2-1024x526.jpg)
*这是五篇系列文章中的第三篇。阅读[第一部分](http://yylives.cc/2023/07/08/catch-performance-regressions-in-ebpf-with-rust-intro/)和[第二部分](http://yylives.cc/2023/07/08/catch-performance-in-ebpf-with-rust-xdp-programs/)。*

在这个系列中，我们[学习了 eBPF 是什么](https://thenewstack.io/catch-performance-regressions-in-ebpf-with-rust-intro/)，如何使用 eBPF 的工具，为什么 eBPF 的性能非常重要，以及如何使用[连续基准测试](https://bencher.dev/docs/explanation/continuous-benchmarking)来跟踪性能。我们使用 Aya 逐行在 Rust 中[创建了一个基本的 eBPF XDP 程序](https://thenewstack.io/catch-performance-in-ebpf-with-rust-xdp-programs/)。在接下来的文章中，我们将讨论如何将这个基本的 eBPF XDP 程序演进到新的功能要求。该项目的所有源代码都是开源的，并且可在 [GitHub](https://github.com/bencherdev/bencher/tree/main/examples/ebpf) 上获取。

eBPF 程序本身是完全无状态的。每次调用都是一个全新的 eBPF 程序。为了保持状态、报告其操作或改变其行为， eBPF 程序需要使用“映射”（maps）。映射是持久的数据结构，可供 eBPF 和用户空间程序使用。 eBPF 有几种不同类型的映射：数组、哈希映射、栈、队列等等。它们是 eBPF 程序与用户空间之间可靠通信的唯一方式，反之亦然。在我们的下一个 eBPF XDP 程序的迭代中，我们将使用映射来从 eBPF 程序传递信息回到用户空间程序。

![](https://cdn.thenewstack.io/media/2023/07/d9cafb34-screenshot2.jpg)

在我们应用程序的下一个版本（Version 1）中，我们将实现一个“ Fizz 功能”。这个 Fizz 功能需要：

- 如果 IPv4 源地址可以被 3 整除，则将 “Fizz” 推入队列。
- 否则，只需返回 `XDP_PASS` 。

为了实现这个 Fizz 功能，我们需要创建将在队列映射中传递的消息：

```rust
#[repr(C)]
#[derive(Clone, Copy)]
#[cfg_attr(feature = "user", derive(Debug))]
pub enum SourceAddr {
    Fizz,
}
#[cfg(feature = "user")]
unsafe impl aya::Pod for SourceAddr {}
```

逐行解释：

1. 这个宏告诉 Rust 编译器将这个数据结构表示为 C 程序。
2. `derive` 宏自动实现了 `Clone`（复制消息的能力）和 `Copy`（通过简单地复制比特位来复制消息的能力）。
3. 这第三个宏更加复杂。它取决于是否启用了 “user” 功能。  "user" 功能只在用户空间中使用，它允许我们将我们的消息类型显示为 `Debug` 输出。
4. 我们的消息类型是名为 `SourceAddr` 的枚举。
5. `Fizz` 是我们目前唯一的消息变体。
6. -- 
7. -- 
8. 同样，我们有一个条件宏。下面的代码只在启用了 “user” 功能时由用户空间使用。
9. 实现 Aya 所需的 trait ，将 `SourceAddr` 标记为适用于 eBPF 映射。

我们创建了消息类型后，现在可以对 eBPF 部分进行更改：

```rust
#[map]
pub static mut SOURCE_ADDR_QUEUE: Queue<SourceAddr> = Queue::with_max_entries(1024, 0);

fn try_fun_xdp(ctx: &XdpContext) -> Result<u32, ()> {
    ...
    info!(ctx, "IPv4 Source Address: {}", source_addr);
    let opt_source_addr = (source_addr % 3 == 0).then_some(SourceAddr::Fizz);
    if let Some(source_addr) = opt_source_addr {
        unsafe {
            if let Err(e) = SOURCE_ADDR_QUEUE.push(&source_addr, 0) {
                error!(ctx, "Failed to push source address into queue: {}", e);
            }
        }
    }
    Ok(xdp_action::XDP_PASS)
}
```

逐行解释：

1. 这个 Aya 宏从下一行开始创建一个 eBPF 映射。
2. 我们的 `SourceAddr` 消息的 eBPF 映射将是一个名为 `SOURCE_ADDR_QUEUE` 的队列，最多可以容纳 1,024 条目。
3. --
4. 我们将更新之前[系列的上一部分](/2)中创建的 `try_fun_xdp` 辅助函数。
5. --
6. 删除仅记录 IPv4 源地址的那行代码。
7. 如果 IPv4 源地址可以被 3 整除，则存储 `Some` Fizz 消息。否则，存储 `None` 。
8. --
9. 如果源地址消息是 `Some` ，则...
10. 下面的操作被认为是 `unsafe` 的，因此我们必须明确选择。
11. 尝试将 Fizz 消息推入 `SOURCE_ADDR_QUEUE` 队列。如果出现错误，则...
12. 记录错误和 eBPF 上下文。
13. --
14. --
15. --
16. --
17. 像之前一样，返回 XDP_PASS！
18. --

现在在用户空间接收该消息：

```rust
#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    ...
    spawn_agent(&mut bpf).await?;
    info!("Waiting for Ctrl-C...");
    signal::ctrl_c().await?;
    info!("Exiting...");
    Ok(())
}
```

主函数基本上保持不变。除了在第 5 行我们将添加一个名为 `spawn_agent` 的辅助函数。我们将在接下来的系列中不断演化 `spawn_agent` 函数。

```rust
async fn spawn_agent(bpf: &mut Bpf) -> Result<(), anyhow::Error> {
    let mut xdp_map: Queue<_, SourceAddr> = Queue::try_from(bpf.map_mut("SOURCE_ADDR_QUEUE")?)?;
    loop {
        while let Ok(source_addr) = xdp_map.pop(0) {
            info!("{:?}", source_addr);
        }
    }
}
```

逐行解释：

1. `spawn_agent` 函数是异步的，这就是为什么它必须在 `main` 函数中使用 `.await`。它接受一个可变引用的 eBPF 程序，并返回一个结果，要么是一个空的 `Ok`，要么是与 `main` 函数中使用的相同灵活的 `Err`。
2. 创建一个用户空间中的 `SOURCE_ADDR_QUEUE` eBPF 映射。
3. --
4. --
5. `loop` 处理源地址队列。
6. 尝试从源地址队列中 `pop` 数据。如果成功...
7. 记录源地址消息，即 `Fizz` 。

完成后，我们已经完成了应用程序的 Version 1 。Fizz 功能已经实现。现在让我们不要过于沾沾自喜。让我们添加一个简单的更新。也许你能猜到下面要做什么...

在我们的应用程序的下一个版本，Version 2 中，我们将实现一个 "FizzBuzz 功能"。这个 FizzBuzz 功能要求：

* 如果 IPv4 源地址可以被 3 整除，则将 "Fizz" 推入队列。
* 如果可被 5 整除，则将 "Buzz" 推入队列。
* 如果同时可被 3 和 5 整除，则将 "FizzBuzz" 推入队列。
* 否则，只需返回 `XDP_PASS` 。

和之前一样，我们将从修改共享的消息类型 `SourceAddr` 开始：

```rust
#[repr(C)]
#[derive(Clone, Copy)]
#[cfg_attr(feature = "user", derive(Debug))]
pub enum SourceAddr {
    Fizz,
    Buzz,
    FizzBuzz,
}
#[cfg(feature = "user")]
unsafe impl aya::Pod for SourceAddr {}
```

在这里的唯一更改是第 6 行和第 7 行，我们添加了 `Buzz` 和 `FizzBuzz` 作为可能的 `SourceAddr` 消息。

接下来，我们将更新 eBPF XDP 程序。它也会保持非常相似，只是我们将实现 [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz) 。

```rust
fn try_fun_xdp(ctx: &XdpContext) -> Result<u32, ()> {
    ...
    let opt_source_addr = (source_addr % 3 == 0).then_some(SourceAddr::Fizz);
    let opt_source_addr = match (source_addr % 3, source_addr % 5) {
        (0, 0) => Some(SourceAddr::FizzBuzz),
        (0, _) => Some(SourceAddr::Fizz),
        (_, 0) => Some(SourceAddr::Buzz),
        _ => None,
    };
    ...
    Ok(xdp_action::XDP_PASS)
}
```

在这里的唯一更改是移除第 3 行，并用第 4 行到第 9 行来替换。这里我们判断源地址是否同时可被 3 和 5 整除。如果是，则为 `FizzBuzz` 。如果可被 3 整除，则为 `Fizz` 。如果可被 5 整除，则为 `Buzz` 。否则，为 `None` 。

在用户空间程序中没有任何需要更改的地方。它只是记录发送到它的任何消息， `Fizz` 、 `Buzz` 或 `FizzBuzz` 。我们已经完成了 Version 2。现在我们准备进行编码面试！虽然我们还没有完全完成。我们还想添加一个最后的功能。

在我们的应用程序的下一个版本，Version 3 中，我们将实现一个 "FizzBuzzFibonacci 功能"。这个 FizzBuzzFibonacci 功能要求：

* 如果 IPv4 源地址可以被 3 整除，则将 "Fizz" 推入队列。
* 如果可被 5 整除，则将 "Buzz" 推入队列。
* 如果同时可被 3 和 5 整除，则将 "FizzBuzz" 推入队列。
* 但是，如果 IPv4 源地址除以 256 的余数是 Fibonacci 序列的一部分，则推入 "Fibonacci"。
* 否则，只需返回 `XDP_PASS` 。

和之前一样，我们将从修改共享的消息类型 `SourceAddr` 开始：

```rust
#[repr(C)]
#[derive(Clone, Copy)]
#[cfg_attr(feature = "user", derive(Debug))]
pub enum SourceAddr {
    Fizz,
    Buzz,
    FizzBuzz,
    Fibonacci,
}
#[cfg(feature = "user")]
unsafe impl aya::Pod for SourceAddr {}
```

在这里的唯一更改是在第 8 行，我们添加了 `Fibonacci` 作为可能的 `SourceAddr` 消息。

接下来，我们将更新 eBPF XDP 程序的 `try_fun_xdp` 函数：

```rust
fn try_fun_xdp(ctx: &XdpContext) -> Result<u32, ()> {
    ...
    let opt_source_addr = match (source_addr % 3, source_addr % 5) {
        ...
    };
    let opt_source_addr = is_fibonacci(source_addr as u8)
        .then_some(SourceAddr::Fibonacci)
        .or(match (source_addr % 3, source_addr % 5) {
            (0, 0) => Some(SourceAddr::FizzBuzz),
            (0, _) => Some(SourceAddr::Fizz),
            (_, 0) => Some(SourceAddr::Buzz),
            _ => None,
        });
    ...
    Ok(xdp_action::XDP_PASS)
}

fn is_fibonacci(n: u8) -> bool {
    let (mut a, mut b) = (0, 1);
    while b < n {
        let c = a + b;
        a = b;
        b = c;
    }
    b == n
}
```

我们将不仅实现 FizzBuzz ，还将实现 FizzBuzzFibonacci 的逻辑。这将涉及调用一个名为 `is_fibonacci` 的辅助函数。如果该函数返回 true，则我们的消息是 Fibonacci。否则，我们执行与之前相同的 FizzBuzz 逻辑。`is_fibonacci` 函数计算 Fibonacci 序列，直到达到或超过传入的参数 n 。然后，它检查这两个值是否相等，以表示参数确实属于 Fibonacci 序列。

用户空间程序不需要做任何更改。它只是记录发送到它的任何消息，无论是 `Fizz` 、 `Buzz` 、 `FizzBuzz` 还是 `FizzBuzzFibonacci` 。我们已经完成了 Version 3。现在由于这个改变，再也不会出现任何问题。一切都会变得🌈🦄🌞，我保证...直到我们进入系列的下一个安装程序，生产环境热火朝天🔥🔥🔥，你会重新考虑你所做的所有生活选择，这些选择都导致了你此刻的境地。