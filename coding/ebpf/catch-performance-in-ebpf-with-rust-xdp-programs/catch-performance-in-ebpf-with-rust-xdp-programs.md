# 使用 Rust 在 eBPF 中捕获性能： XDP 程序

eBPF 中的 XDP 程序允许进行非常高效的、自定义的数据包处理。eBPF XDP 程序在数据包到达内核网络堆栈之前运行。

翻译自 [Catch Performance in eBPF with Rust: XDP Programs](https://thenewstack.io/catch-performance-in-ebpf-with-rust-xdp-programs/) 。

![](https://cdn.thenewstack.io/media/2023/06/727e2e91-a1-image-1024x683.jpg)

这是五部分系列文章中的第二部分。在此阅读[第一部分](http://yylives.cc/2023/07/08/catch-performance-regressions-in-ebpf-with-rust-intro/)。

在这个系列中，我们[学习了 eBPF 是什么](http://yylives.cc/2023/07/08/catch-performance-regressions-in-ebpf-with-rust-intro/)，以及与之相关的工具，为什么 eBPF 性能很重要，以及如何使用[连续基准测试](https://bencher.dev/docs/explanation/continuous-benchmarking)来跟踪性能。在本系列的这一篇文章中，我们将讨论如何使用 [Aya](https://github.com/aya-rs/aya) 在 Rust 中创建一个基本的 eBPF XDP 程序。该项目的所有源代码都是开源的，可以在 [GitHub](https://github.com/bencherdev/bencher/tree/main/examples/ebpf) 上获取。

eBPF XDP 程序允许进行非常高效的、自定义的数据包处理。eBPF XDP 程序在数据包到达内核的网络堆栈之前运行。[eBPF XDP 程序可以执行四种不同的操作](https://prototype-kernel.readthedocs.io/en/latest/networking/XDP/implementation/xdp_actions.html)：

* `XDP_PASS`：将数据包传递给正常的网络堆栈进行处理。数据包内容可以被修改。
* `XDP_DROP`：丢弃数据包并不对其进行处理。这是最快的操作。
* `XDP_TX`：将数据包转发到它所在的相同网络接口。数据包内容可以被修改。
* `XDP_ABORTED`：在处理过程中出现错误，因此丢弃数据包并不进行处理。这表示 eBPF 程序中的错误。

在我们的基本示例中，如果一切顺利，我们只会执行第一个操作 `XDP_PASS` ，因为我们更关注的是脚手架和进程间通信，而不是数据包处理逻辑。我们的初始版本的 eBPF XDP 应用程序只会记录接收到的每个数据包的 IPv4 源地址。

![](https://cdn.thenewstack.io/media/2023/06/2e702d81-screenshot-2023-06-29-at-9.43.10-am.jpg)

让我们首先看一下内核方面的代码：

```rust
#[xdp(name = fun_xdp)]
pub fn fun_xdp(ctx: XdpContext) -> u32 {
    match try_fun_xdp(&ctx) {
        Ok(ret) => ret,
        Err(_) => xdp_action::XDP_ABORTED,
    }
}
```

逐行解释：

1. 这是一个 Aya 宏，告诉我们我们正在创建一个名为 `fun_xdp` 的 eBPF XDP 程序。
2. 我们的 eBPF XDP 程序的函数定义。它以上下文作为唯一参数输入。上下文告诉我们内核提供给我们的所有信息，并返回一个无符号 32 位整数。
3. 有一个名为 `try_fun_xdp` 的辅助函数，我们将在下面讨论。根据它的返回值，如果返回 `Ok` ，则一切正常，我们返回给定的值。否则，如果得到一个 `Err` ，我们中止执行。

现在让我们来看一下 try_fun_xdp 函数：

```rust
fn try_fun_xdp(ctx: &XdpContext) -> Result<u32, ()> {
    let eth_hdr: *const EthHdr = unsafe { ptr_at(ctx, 0)? };
    unsafe {
        let EtherType::Ipv4 = (*eth_hdr).ether_type else {
            return Ok(xdp_action::XDP_PASS);
        };
    }
    let ipv4_hdr: *const Ipv4Hdr = unsafe { ptr_at(ctx, EthHdr::LEN)? };
    let source_addr = unsafe { (*ipv4_hdr).src_addr };
    info!(ctx, "IPv4 Source Address: {}", source_addr);
    Ok(xdp_action::XDP_PASS)
}
```

逐行解释：

1. `try_fun_xdp` 函数接受一个对上下文的引用，并返回一个 `Result` ，其中包含一个 `Ok` 的无符号 32 位整数值或一个空的 `Err` 。
2. 从上下文中获取以太网头部。注意这里的 `unsafe` 的 `ptr_at` 辅助函数，我们接下来会讨论它。
3. 接下来的操作在 Rust 编译器中也被认为是 `unsafe` 的，因此我们必须显式地选择它们。
4. 对于我们的基本示例，我们只关心 IPv4 ，因此对于其他情况，我们只需要将数据包传递出去。
5. -- 
6. --
7. -- 
8. 提取 IPv4 头部。再次使用 `unsafe` 的 `ptr_at` 辅助函数。
9. 从 IPv4 头部获取源地址。
10. 记录 IPv4 的源地址。
11. --
12. 返回通过！
13. -- 
14. -- 

最后让我们看一下 `ptr_at` 辅助函数：

```rust
#[inline(always)]
unsafe fn ptr_at<T>(ctx: &XdpContext, offset: usize) -> Result<*const T, ()> {
    let start = ctx.data();
    let end = ctx.data_end();
    let len = core::mem::size_of::<T>();
    if start + offset + len > end {
        return Err(());
    }

    Ok((start + offset) as _)
}
```

逐行解释：

1. 因为这个操作将在许多地方进行并且在关键路径中，我们使用宏要求编译器始终内联我们的辅助函数。
2. 这是一个不安全函数，从上下文中以特定的字节偏移量读取泛型类型 `T` 的数据。对于成功读取， `Result` 是一个指向 `T` 的指针的 `Ok` 。否则，返回一个空的 `Err` 。
3. 上下文给定内存的起始地址。
4. 上下文给定内存的结束地址。
5. 泛型类型 `T` 的字节数。
6. 如果起始地址、字节偏移量和T的长度之和大于结束地址，则返回一个空的 Err ，因为我们超出了上下文的界限。如果我们不进行此检查， eBPF 验证器会感到不安，并很可能使我们的构建失败。
7. -- 
8. -- 
9. -- 
10. -- 
11. 从上下文给定内存的特定字节 `offset` 处读取 T 。
12. --

还有一个最后的函数：

```rust
#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! {
    unsafe { core::hint::unreachable_unchecked() }
}
```

逐行解释：

1. 定义一个自定义的 Rust panic 处理函数。
2. 该函数接受 Rust panic 信息，但它从不使用。这个函数永远不应该返回。
3. 给 Rust 编译器一个提示，表明这段代码应该是不可达的。也就是说，我们永远不希望发生 pani c。这是为了让 eBPF 验证器保持快乐的必要条件。
4. -- 

现在转到用户空间的部分。让我们看看我们的 `main` 函数：

```ruby
#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    let opt = Opt::parse();
    env_logger::init();
    let mut bpf = Bpf::load(include_bytes_aligned!("../path/to/ebpf-bin"))?;
    BpfLogger::init(&mut bpf)?;
    let program: &mut Xdp = bpf.program_mut(fun_xdp).unwrap().try_into()?;
    program.load()?;
    program.attach(&opt.iface, XdpFlags::default())?;
    info!("Waiting for Ctrl-C...");
    signal::ctrl_c().await?;
    info!("Exiting...");
    Ok(())
}
#[derive(clap::Parser)]
struct Opt {
    #[clap(long)]
    iface: String,
}
```

逐行解释：

1. 这个宏使用 `tokio` 创建了一个异步运行时来运行我们的程序。
2. 一个异步的 `main` 函数。在 Rust 二进制文件中， `main` 函数是事实上的入口点。该函数的结果是一个空的 `Ok` 或使用 [anyhow](https://github.com/dtolnay/anyhow) crate 捕获所有的 `Err` 。
3. 解析传递给二进制文件的命令行参数。
4. 为用户空间初始化日志记录。
5. 加载我们编译的 eBPF 字节码。Aya 使得将我们的 eBPF 源代码重新编译为字节码变得容易，所以它会在编译用户空间代码之前自动进行。
6. 从我们的 eBPF 程序中初始化日志记录。
7. 从我们的 eBPF 字节码中获取 `fun_xdp` eBPF XDP 程序。
8. 将 `fun_xdp` eBPF XDP 程序加载到内核中，使用默认标志。
9. 将我们的 `fun_xdp` eBPF XDP 程序附加到一个由 `iface` 命令行参数设置的网络接口上。
10. -- 
11. 记录如何退出我们的程序。
12. 等待用户输入 Ctrl + C 。
13. 记录我们的程序正在退出。
14. 以一个空的 Ok 作为我们的结果返回。
15. -- 
16. -- 
17. 这个宏使用 [clap](https://github.com/clap-rs/clap) 来解析在 `Opt` 结构中定义的命令行参数。
18. 命令行参数结构体名为 `Opt` 。
19. 另一个宏，告诉 `clap` 这个字段应该作为长参数名进行解析，即 `--iface` 。
20. 参数的名称是 `iface` ，其值为字符串。

通过以上代码，我们已经创建了一个非常基本的 eBPF 程序。同样，该项目的所有源代码都是开源的，并且可在 [GitHub](https://github.com/bencherdev/bencher/tree/main/examples/ebpf) 上获得。