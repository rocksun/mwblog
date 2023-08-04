# 捕捉性能回归：基准测试 eBPF 程序

通过对 eBPF 和用户空间应用程序进行基准测试，防止在生产环境中出现重大性能回归的方法。

翻译自 [Catch Performance Regressions: Benchmark eBPF Program ](https://thenewstack.io/catch-performance-regressions-benchmark-ebpf-program/) 。

![](https://cdn.thenewstack.io/media/2023/07/11df4fb0-firefighting1-1024x622.jpg)
*图片来自 Shutterstock*

这是五篇系列文章中的第四篇。请阅读[第一部分](http://yylives.cc/2023/07/08/catch-performance-regressions-in-ebpf-with-rust-intro/)、[第二部分](http://yylives.cc/2023/07/08/catch-performance-in-ebpf-with-rust-xdp-programs/)和[第三部分](http://yylives.cc/2023/07/08/catch-performance-regressions-evolving-ebpf-program/)。

在这个系列中，我们学习了[什么是 eBPF](http://yylives.cc/2023/07/08/catch-performance-regressions-in-ebpf-with-rust-intro/)，以及处理 eBPF 的工具，为什么 eBPF 的性能很重要，以及如何通过[持续基准测试](https://bencher.dev/docs/explanation/continuous-benchmarking)来追踪它。我们使用 [Aya](https://github.com/aya-rs/aya) 在 Rust 中逐行[创建了一个基本的 eBPF XDP 程序](http://yylives.cc/2023/07/08/catch-performance-in-ebpf-with-rust-xdp-programs/)。然后，我们介绍了如何根据新的功能需求[改进基本的 eBPF XDP 程序](http://yylives.cc/2023/07/08/catch-performance-regressions-evolving-ebpf-program/)。当我们停下来的时候，我们最后一次功能更改在生产环境中导致了严重的性能回归。在本篇中，我们将看看通过对 [eBPF](https://thenewstack.io/ebpf-put-the-kubernetes-data-plane-in-the-kernel/) 和用户空间应用程序进行基准测试来防止这种情况发生。项目的所有源代码都是开源的，可在 [GitHub](https://github.com/bencherdev/bencher/tree/main/examples/ebpf) 上获取。

如约，生产环境出现了严重问题，你重新考虑了导致你陷入这一刻的所有生活选择。自从我们实现了 `FizzBuzzFibonacci` 功能以来已经过去了三个星期，一切似乎都很好...直到不好的时候。在追踪了几个小时的错误，不敢相信地盯着“[可观测性](https://thenewstack.io/observability/)”仪表板，以及进行了大量手动分析之后，你终于锁定了罪魁祸首。它是我们的 `is_fibonacci` 辅助函数：

```rust
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

然后你意识到每次接收到一个数据包时都在重新计算斐波那契数列。当你的唯一终端是在 `1.0.0.0` 时，情况还不算糟糕，但昨天你添加了 `1.255.255.255` 和 `2.255.255.255` 。

修复很简单，尽管在 256 以下的斐波那契数列中没有那么多数字：

```rust
fn is_fibonacci(n: u8) -> bool {
    let (mut a, mut b) = (0, 1);
    while b < n {
        let c = a + b;
        a = b;
        b = c;
    }
    b == n || matches!(n, 0 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233)
}
```

不再每次接收数据包时重新计算斐波那契数列，我们可以直接硬编码这 13 个必要的值。

经过我们的更改并进行紧急推送到生产环境后，我们成功扑灭了火灾。但是为什么我们必须等到生产环境才能发现这个问题‽ 我们应该尽量将这种检测移到尽可能早的开发阶段。实现这一目标的最佳方式是使用软件基准测试。

有两大类软件基准测试：微基准测试和宏基准测试。微基准测试类似于单元测试。例如，对于我们的 `is_fibonacci` 函数的基准测试就是微基准测试。而宏基准测试类似于集成测试。例如，对于我们的 `spawn_agent` 函数的基准测试就是宏基准测试。

在 Rust 中，有三个流行的微基准测试选项：[libtest bench](https://doc.rust-lang.org/rustc/tests/index.html#benchmarks)[、Criterion](https://github.com/bheisler/criterion.rs) 和 [Iai](https://github.com/bheisler/iai)。

虽然 libtest bench 是 Rust 标准库的一部分，但仍被认为是不稳定的，因此只能在每夜版的编译器发布中使用。为了在稳定版的 Rust 编译器上工作，需要使用一个[单独的基准测试工具](https://github.com/bluss/bencher)。然而，这两者目前都没有在积极开发。

在 Rust 生态系统中，最活跃维护的基准测试工具是 Criterion。它可以在稳定版和每夜版的 Rust 编译器上工作，并已成为 Rust 社区的事实标准。与 libtest bench 相比，Criterion 的功能也更为丰富。

Criterion 的一个实验性替代品是 Iai，它与 Criterion 的创建者相同。然而，Iai 使用的是指令计数而不是实际的墙钟时间：CPU 指令、L1 访问、L2 访问和 RAM 访问。这样可以进行单次基准测试，因为这些指标在不同运行之间应该保持几乎相同。

我们将使用这三个选项中最受欢迎的 Criterion。这三个基准测试工具都受到 Bencher 支持，而 Bencher 是我们后面将在本系列中使用的[持续基准测试工具](https://bencher.dev/)。为了使用 Criterion 对我们的代码进行基准测试，我们需要进行一些重构。Criterion 与生成 eBPF 字节码所需的编译器选项不兼容。为了解决这个问题，我们将一些 eBPF 辅助函数转移到一个单独的 Rust 库，称为 crate，这样它们可以独立地进行测试。为了方便起见，我们将它们添加到我们已经为 `SourceAddr` 映射消息创建的 crate 中。

![](https://cdn.thenewstack.io/media/2023/07/86c6cc86-linux4.jpg)

接下来，我们需要更新 Cargo.toml 文件，该文件类似于 21 世纪的 make。我们将添加以下内容：

```toml
[dev-dependencies]
criterion = "0.4"
[[bench]]
name = "source_addr"
harness = false
```

逐行解释如下：

1. 这些是开发依赖项的配置。
2. 将 Criterion 版本 0.4 添加到我们的 crate。
3. 
4. 配置 `cargo bench` 的选项。
5. 基准测试的名称是 `source_addr。`
6. 不使用默认的基准测试框架 (libtest bench)。

然后，我们将更新我们的 `SourceAddr` 代码，添加一个 `new` 的关联函数：

```rust
impl SourceAddr {
    pub fn new(source_addr: u32) -> Option<SourceAddr> {
        is_fibonacci(source_addr as u8)
            .then_some(SourceAddr::Fibonacci)
            .or(match (source_addr % 3, source_addr % 5) {
                (0, 0) => Some(SourceAddr::FizzBuzz),
                (0, _) => Some(SourceAddr::Fizz),
                (_, 0) => Some(SourceAddr::Buzz),
                _ => None,
            })
    }
}
```

这个 `new` 的关联函数与之前在 eBPF XDP 程序中创建 `SourceAddr` 时的工作完全相同，只是现在它被转移到直接定义在 `SourceAddr` 类型上。我们还需要复制之前在本文中修复的 `is_fibonacci` 辅助函数。

现在我们准备编写一些基准测试了！在我们上面提到的 Cargo.toml 中，有一个名为 source_addr 的基准测试文件，我们将在其中添加以下内容：

```rust
fn bench_source_addr(c: &mut Criterion) {
    c.bench_function("SourceAddr", |b| {
        b.iter(|| {
            for i in 0..256 {
                SourceAddr::new(i);
            }
        });
    });
}

criterion_group!(benches, bench_source_addr);
criterion_main!(benches);
```

逐行解释如下：

1. 创建一个函数，它接收一个可变的 Criterion 基准测试收集器。
2. 使用该基准测试收集器，添加一个名为 "SourceAddr" 的基准测试。
3. 运行基准测试多次以确保精度。
4. 这是我们的实际基准测试代码，针对从 0 到 256 的所有数值（不包括 256）……
5. 创建一个新的 SourceAddr 对象并传递该数字。
6. 
7. 
8. 
9. 
10. 
11. 
12. 注册 bench_source_addr 与 benches 测试组。
13. 将 benches 测试组作为我们的基准测试框架的主要函数运行。

如果我们运行 `cargo bench`，将得到类似于以下的输出：

```
$ cargo bench
   Finished bench [optimized] target(s) in 1m 03s
     Running unittests src/lib.rs (/home/epompeii/Code/bencher/examples/ebpf/target/release/deps/ebpf_common-23fb553d75cce271)
 
running 0 tests
 
test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
 
     Running benches/source_addr.rs (/home/epompeii/Code/bencher/examples/ebpf/target/release/deps/source_addr-090d31387638198e)
SourceAddr              time:   [538.49 ns 540.24 ns 542.58 ns]
Found 13 outliers among 100 measurements (13.00%)
  9 (9.00%) high mild
  4 (4.00%) high severe
```

我们已经成功为我们的 eBPF 代码创建了微基准测试！

为了在更高层次进行测试，我们现在要进行宏基准测试。这会变得有点复杂，因为我们将不得不从 Linux 内核本身获取我们的基准测试时间。有三种选项可以实现这一点：`kernel.bpf_stats_enabled`、`bpftool prog profile` 和 `bpftool prog run`。

`kernel.bpf_stats_enabled` 在启用时收集所有 eBPF 程序的 `run_time_ns` 和 `run_cnt` 。但默认情况下是禁用的。该功能在 Linux 内核版本 5.1 中添加。

`bpftool prog profile` 与之前查看过的 `Iai` 类似。它收集指令计数而不是挂钟时间：CPU 指令、LLD 加载、LLC 缺失和周期。该功能在 Linux 内核版本 5.7 中添加，还需要使用 clang >= 10.0.0 构建的 bpftool 。

命令 `bpftool prog run` 用于运行特定的 eBPF 程序。它必须提供输入数据和上下文（XDP 除外），并返回输出数据和上下文。不幸的是，目前它只适用于一小部分 eBPF 程序类型。希望未来能有所改变。该功能在 Linux 内核版本 4.12 中添加。

- BPF_PROG_TYPE_CGROUP_SKB
- BPF_PROG_TYPE_FLOW_DISSECTOR
- BPF_PROG_TYPE_LWT_IN
- BPF_PROG_TYPE_LWT_OUT
- BPF_PROG_TYPE_LWT_SEG6LOCAL
- BPF_PROG_TYPE_LWT_XMIT
- BPF_PROG_TYPE_SCHED_ACT
- BPF_PROG_TYPE_SCHED_CLS
- BPF_PROG_TYPE_SOCKET_FILTER
- BPF_PROG_TYPE_XDP

尽管我们的示例是 XDP 程序，并且支持 `bpftool prog run` ，但我们将使用 `kernel.bpf_stats_enabled` ，因为它适用于所有 eBPF 程序类型。这将需要我们更新用户空间源代码。我们将对此代码进行更改，以使其更易于测试。

```rust
#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    let opt = Opt::parse();
    let shutdown = Arc::new(AtomicBool::new(false));
    let ebpf_shutdown = shutdown.clone();
    ebpf::run(&opt.iface, ebpf_shutdown).await?;
    info!("Waiting for Ctrl-C...");
    signal::ctrl_c().await?;
    info!("Exiting...");
    shutdown.store(true, Ordering::Relaxed);
    Ok(())
}
```

逐行解释：

1. 这是与之前相同的异步主函数。
2. 
3. 再次解析命令行参数。
4. 
5. 创建一个线程安全的 `shutdown` 布尔值，初始化为 `false` 。
6. 复制我们的 `shutdown`  布尔值。
7. 将接口命令行参数和 `shutdown` 布尔值的副本传递给我们的新 `run` 辅助函数。
8. 
9. 再次记录日志
10. 并等待 Ctl+C
11. 这次记录我们正在退出。
12. 然后将我们的 `shutdown` 布尔值设置为 `true` 。
13. 
14. 返回一个空的 `Ok` 。
15. 

现在让我们来看一下那个运行辅助函数：

```
pub async fn run(iface: &str, shutdown: Arc<AtomicBool>) -> Result<Process, anyhow::Error> {
env_logger::init();
let mut bpf = Bpf::load(include_bytes_aligned!(“../path/to/ebpf-bin”))?;
BpfLogger::init(&mut bpf)?;
let program: &mut Xdp = bpf.program_mut(fun_xdp).unwrap().try_into()?;
program.load()?;
program.attach(&opt.iface, XdpFlags::default())?;
let pid = std::process::id();
let prog_fd = bpf.program(fun_xdp).unwrap().fd().unwrap().as_raw_fd();
let handle = tokio::spawn(async move { spawn_agent(&mut bpf, shutdown).await });
Ok(Process {
pid,
prog_fd,
handle,
})
}
pub struct Process {
pub pid: u32,
pub prog_fd: i32,
pub handle: tokio::task::JoinHandle<Result<(), anyhow::Error>>,
}
```

逐行解释：

这是另一个异步函数，接收网络接口 iface 和一个线程安全的关闭布尔值作为参数。如果结果为 Ok，则返回 Process 结构体，否则返回任意错误。
初始化用于用户空间的日志记录器。
加载已编译的 eBPF 字节码。Aya 使得将 eBPF 源代码重新编译成字节码变得简单，因此在用户空间代码编译之前，自动进行了这一步骤。
初始化 eBPF 程序的日志记录。
从 eBPF 字节码中获取 fun_xdp eBPF XDP 程序。
将 fun_xdp eBPF XDP 程序加载到内核中，使用默认标志。
将 fun_xdp eBPF XDP 程序附加到二进制文件的命令行参数指定的网络接口。
获取当前进程 ID。
获取 fun_xdp eBPF XDP 程序的文件描述符。
创建一个异步任务句柄，运行 spawn_agent 函数，并使用之前传递的 shutdown 布尔值。
返回一个成功的结果，包含进程 ID、XDP 程序文件描述符和异步任务句柄。
接下来，我们来看一下更新的 spawn_agent 函数：

async fn spawn_agent(bpf: &mut Bpf, shutdown: Arc<AtomicBool>) -> Result<(), anyhow::Error> {
let mut xdp_map: aya::maps::Queue<_, SourceAddr> = aya::maps::Queue::try_from(bpf.map_mut("SOURCE_ADDR_QUEUE")?)?;
loop {
while let Ok(source_addr) = xdp_map.pop(0) {
info!("{:?}", source_addr);
}
if shutdown.load(Ordering::Relaxed) {
break;
}
}
Ok(())
}
逐行解释：

这是更新后的 spawn_agent 函数，与之前的版本几乎相同，只是现在在每次迭代时检查关闭布尔值（位于第9至11行）。这允许从自定义基准测试工具进行干净的关闭。

创建一个异步运行时。
创建一个线程安全的关闭布尔值，初始化为 false。
创建一个队列映射，用于存储 eBPF XDP 程序返回的数据。映射名为 "SOURCE_ADDR_QUEUE"。
进入一个循环：
从队列映射中不断取出数据，并打印该数据的信息。
如果关闭布尔值为 true，则退出循环。
返回一个成功的结果。
接下来，我们需要添加我们的第一个基准测试到 inventory：

inventory::submit!(EBpfBenchmark {
name: "fun_xdp",
benchmark_fn: fun_xdp_benchmark
});
这样就添加了一个名为 "fun_xdp" 的基准测试，基准测试函数为 fun_xdp_benchmark，其实现如下：

fn fun_xdp_benchmark() -> f64 {
let rt = Runtime::new().unwrap(); // 创建异步运行时
let shutdown = Arc::new(AtomicBool::new(false)); // 创建线程安全的关闭布尔值，初始化为 false
let ebpf_shutdown = shutdown.clone(); // 创建关闭布尔值的副本
let process = rt.block_on(async { ebpf::run(IFACE, ebpf_shutdown).await.unwrap() }); // 使用 run 辅助函数运行 eBPF 程序
let _resp = rt.block_on(async { reqwest::get("https://bencher.dev").await.unwrap() }); // 创建一些网络流量，访问某个网页
let bpf_stats = get_bpf_stats(&process); // 获取 eBPF 程序的统计信息
shutdown.store(true, Ordering::Relaxed); // 设置关闭布尔值为 true
bpf_stats // 返回 eBPF 程序的统计信息
}
逐行解释：

这个 fun_xdp_benchmark 函数不接收任何参数，返回一个 64 位浮点数。
创建一个异步运行时。
创建一个线程安全的关闭布尔值，初始化为 false。
创建关闭布尔值的副本。
将一个预定义的测试网络接口（

IFACE）和关闭布尔值的副本传递给 run 辅助函数，并在这个调用上进行阻塞。
创建一些网络流量，例如访问一个特定网页，并在这个调用上进行阻塞。
通过调用 get_bpf_stats 函数获取当前进程的 eBPF 程序统计信息。
将关闭布尔值设置为 true。
返回 eBPF 程序的统计信息。
最后，我们来看一下 get_bpf_stats 辅助函数：

fn get_bpf_stats(process: &Process) -> f64 {
let fd_info = File::open(format!("/proc/{}/fdinfo/{}", process.pid, process.prog_fd)).unwrap(); // 打开 eBPF XDP 程序的 fdinfo 伪文件
let reader = BufReader::new(fd_info); // 创建一个带缓冲的读取器，以便不会一次性将文件全部加载到内存中
let (mut run_time_ns, mut run_ctn) = (None, None); // 初始化 run_time_ns 和 run_ctn 统计信息为 None
for line in reader.lines().flatten() { // 读取 fd_info 文件的每一行
if let Some(l) = line.strip_prefix("run_time_ns:") { // 如果行以 "run_time_ns:" 开头…
run_time_ns = l.trim().parse::<u64>().ok(); // 将其余部分去除空格并解析为 u64 类型的数值，并保存在 run_time_ns 中
} else if let Some(l) = line.strip_prefix("run_cnt:") { // 否则，如果行以 "run_cnt:" 开头…
run_ctn = l.trim().parse::<u64>().ok(); // 将其余部分去除空格并解析为 u64 类型的数值，并保存在 run_ctn 中
}
}
match (run_time_ns, run_ctn) { // 检查 run_time_ns 和 run_ctn 的值
(Some(run_time_ns), Some(run_ctn)) if run_ctn != 0 => run_time_ns as f64 / run_ctn as f64, // 如果都不为 None，且 run_ctn 不等于 0，则返回平均运行时间
_ => 0.0, // 否则返回 0.0
}
}
逐行解释：

get_bpf_stats 函数接收一个 Process 结构体的引用，并返回一个 64 位浮点数。
打开当前进程的 eBPF XDP 程序的 fdinfo 伪文件。该文件包含了与 eBPF 程序相关的一些信息，包括运行时间等。
创建一个带缓冲的读取器，以便不会一次性将 fd_info 文件全部加载到内存中。
初始化 run_time_ns 和 run_ctn 统计信息为 None。
读取 fd_info 文件的每一行。
如果行以 "run_time_ns:" 开头…
则将其余部分去除空格并解析为 u64 类型的数值，并保存在 run_time_ns 中。
否则，如果行以 "run_cnt:" 开头…
则将其余部分去除空格并解析为 u64 类型的数值，并保存在 run_ctn 中。
检查 run_time_ns 和 run_ctn 的值。
如果它们都不为 None，且 run_ctn 不等于 0，则返回平均运行时间，即 run_time_ns 除以 run_ctn。
否则返回 0.0。
现在我们准备好运行我们的宏基准测试了！首先，我们需要启用 bpf_stats 功能，因为它默认是禁用的。

$ sudo sysctl -w kernel.bpf_stats_enabled=1
kernel.bpf_stats_enabled = 1
然后我们需要将 eBPF 代码编译为 release 模式，因为基准测试是在 release 模式下运行的。

$ cargo xtask build-ebpf --release
...
然后在用户空间 crate 中，我们终于可以运行我们的基准测试了。然而，请注意，我们需要以 root 用户身份运行，因为加载 eBPF 程序需要提升的权限。

$ sudo -E $(which cargo) bench
Finished bench [optimized] target(s) in 0.13s
...
Running benches/xdp.rs (/home/epompeii/Code/bencher/examples/ebpf/target/release/deps/xdp-d7c85fd4c85d089e)
{
"fun_xdp": {
"latency": {
"value": 18249.727272727272,
"lower_bound": null,
"upper_bound": null
}
}
}
太棒了！输出是我们在上面的 main 函数中序列化并打印的 JSON 数据。所使用的 JSON 格式是 Bencher Metric Format（BMF）。BMF 是 Bencher 这个连续基准测试工具所使用的 JSON 格式，在本系列的后续部分中我们将会使用 Bencher 来跟踪我们的微基准测试和宏基准测试，以便在 CI 中发现性能回归。

这篇文章中，我们为防止性能回归迈出了很大的一步。我们将 eBPF 和用户空间的源代码重构为更易于测试，并添加了微基准测试和宏基准测试。在本地工作时，我们可以轻松地查看我们的更改对性能的改进和回归。与单元测试用于防止功能回归的原因相同，基准测试也应该在 CI 中运行，以防止性能回归。这将需要一个连续性基准测试工具。在本系列的下一篇和最后一篇文章中，我们将介绍如何使用 Bencher 在 CI 中跟踪我们的微基准测试和宏基准测试，以便发现性能回归。