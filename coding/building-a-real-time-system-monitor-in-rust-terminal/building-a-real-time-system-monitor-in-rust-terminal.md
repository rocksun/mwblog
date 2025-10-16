
<!--
title: Rust 终端实时系统监控器开发实战
cover: https://cdn.thenewstack.io/media/2025/10/7e8ef5d9-monitoring.jpg
summary: monitor-rs 是一个轻量级、实时、交互式的 Rust 终端仪表板，用于监控 CPU、内存、磁盘 I/O 和网络活动，提供高效且可扩展的系统性能洞察与警报功能。
-->

monitor-rs 是一个轻量级、实时、交互式的 Rust 终端仪表板，用于监控 CPU、内存、磁盘 I/O 和网络活动，提供高效且可扩展的系统性能洞察与警报功能。

> 译自：[Building a Real-Time System Monitor in Rust Terminal](https://thenewstack.io/building-a-real-time-system-monitor-in-rust-terminal/)
> 
> 作者：Tinega Onchari

系统监控工具无处不在，但大多数要么是重量级的 GUI 应用程序，要么是只能导出静态信息的简单命令行实用程序。如果你能构建一个介于两者之间的工具呢？一个既轻量又强大，能实时、交互式显示的终端仪表板。

这正是我想通过 monitor-rs 来实现的目标。在开发各种系统工具之后，我希望探索 [Rust](https://thenewstack.io/the-case-for-rust-as-the-future-of-javascript-infrastructure/) 的独特功能如何解决实时监控的经典挑战：管理并发数据收集、优雅地处理错误以及在不消耗过多资源的情况下清晰地呈现信息。

Monitor-rs 可以在干净的终端界面中实时跟踪 CPU 使用率、内存消耗、磁盘 I/O 和网络活动。这是对 [Rust 为系统编程](https://thenewstack.io/rusts-expanding-horizons-memory-safe-and-lightning-fast/) 所特别适合之处的实际探索。

让我们深入了解重要的实现细节：

*   **零成本抽象**：了解高级代码如何编译成高效的机器指令。
*   **所有权与借用**：理解 [Rust 独特的内存管理](https://thenewstack.io/rust-pythons-new-performance-engine/) 如何在没有垃圾回收器的情况下确保线程安全。
*   **无畏并发**：探索通道和线程如何用于安全地管理复杂的实时数据流。
*   **健壮的错误处理**：见证 `Result` 在构建弹性应用程序方面的强大功能。
*   **强大的生态系统和 Crate**：发现 `sysinfo` 和 `ratatui` 等库如何无缝扩展 Rust 的功能。
*   **模块化设计**：欣赏 Rust 的模块系统如何促进关注点分离以提高可维护性。

## **先决条件**

在深入代码之前，您需要准备好一些东西：

*   基本的 Rust 知识：熟悉结构体、模块和线程等概念将有所帮助。
*   Linux 或 macOS 系统：Monitor-rs 主要在 Ubuntu 22.04 上进行测试。
*   熟悉终端：由于这是一个基于终端的应用程序，熟悉命令行界面会有所帮助。
*   已安装 Rust 和 Cargo：如果您尚未安装 Rust，可以使用以下命令进行安装：

`curl --proto '=https' --tlsv1.2 -sSf [https://sh.rustup.rs](https://sh.rustup.rs) | sh`

## **monitor-rs 是什么？**

Monitor-rs 是一个实时终端仪表板，旨在显示关键的系统性能指标。它提供以下方面的深入了解：

*   CPU 使用率：一目了然地查看处理器的利用率。
*   内存 (RAM) 利用率：跟踪系统内存的使用量。
*   磁盘读/写吞吐量：监控存储设备的活动。
*   网络流量：关注传入和传出的网络数据。
*   警报系统：当超出可自定义的性能阈值时获得通知。

它通过关键的 Rust 库实现了这些强大的功能：

*   [**sysinfo**](https://docs.rs/sysinfo/latest/sysinfo/)：用于高效且跨平台的系统统计信息收集。
*   [**Ratatui**](https://docs.rs/ratatui/latest/ratatui/)：用于渲染动态和交互式 TUI 仪表板。
*   模块化 Rust 设计：确保代码库易于扩展和维护。

## **monitor-rs 项目结构：模块化深入探究**

monitor-rs 的优势之一在于其整洁、模块化的架构。这种设计原则确保了不同功能之间良好分离，使代码库更易于理解、维护和扩展。以下是项目目录布局：

```
monitor-rs/
├── src/
│ ├── main.rs # App entry point
│ ├── metrics/ # System collectors and data snapshot
│ │ ├── cpu.rs
│ │ ├── disk.rs
│ │ ├── memory.rs
│ │ ├── network.rs
│ │ └── snapshot.rs
│ ├── alerting/ # Alerting rules and evaluation logic
│ │ ├── handler.rs
│ │ └── rules.rs
│ └── ui/ # Terminal UI components
│ ├── dashboard.rs
│ ├── cpu\_widget.rs
│ ├── memory\_widget.rs
│ ├── disk\_widget.rs
│ ├── net\_widget.rs
│ └── theme.rs
├── Cargo.toml # Dependencies and package config
└── alerts.log # File where triggered alerts are logged
```

这种结构清晰地划分了职责：`metrics` 负责数据收集，`alerting` 管理阈值检查，而 `ui` 只关注展示。这种分离是 monitor-rs 可扩展性的关键。

## **项目设置与运行**

在您的系统上启动并运行 monitor-rs 非常简单。请按照以下步骤操作：

### **获取代码并构建**

首先，将 monitor-rs 仓库从 GitHub 克隆到您的本地机器。打开终端并运行：

```
git clone https://github.com/Tinega-Devops/monitor-rs.git
cd monitor-rs
```

进入项目目录后，编译应用程序。我们建议在发布模式下构建以获得最佳性能，因为这会应用 Rust 的全套优化。

`cargo build --release`

此命令将编译 monitor-rs 及其依赖项。生成的可执行文件将位于 `target/release/` 目录中。

### **运行监控器**

编译完成后，启动 monitor-rs。

要运行优化过的发布版本：

`./target/release/monitor-rs`

或者，如果您在项目根目录中，并且自上次构建以来没有更改代码，则可以使用 `cargo run --release`，这将在必要时重新编译，然后执行优化后的二进制文件：

`cargo run --release`

您将立即看到一个动态、实时的系统仪表板出现在您的终端中。要退出应用程序，只需按 `q` 键。

## **指标引擎（CPU、内存、磁盘、网络）**

monitor-rs 的核心在于其独立的指标收集器，它们位于 `src/metrics/` 目录中。每个收集器负责刷新特定的系统值，通常以一秒为间隔，确保实时准确性。

### **CPU 使用率**

CPU 使用率使用 sysinfo 库高效收集，具体在 `src/metrics/cpu.rs` 中实现。

```
// src/metrics/cpu.rs
pub fn collect(&mut self) -> f32 {
    self.sys.refresh_cpu_all();
    self.sys.global_cpu_usage()
}
```

此代码片段首先刷新全系统的 CPU 信息，然后检索全局 CPU 总使用率（以百分比表示）。

### **内存使用率**

内存指标捕获总内存和已用内存，从而可以精确计算利用率，在 `src/metrics/memory.rs` 中处理。

```
// src/metrics/memory.rs
pub fn collect_total(&mut self) -> u64 {
    self.sys.refresh_memory();
    self.sys.total_memory()
}

pub fn collect_used(&mut self) -> u64 {
    self.sys.refresh_memory();
    self.sys.used_memory()
}
```

它捕获总可用内存和当前已用内存，然后计算比率以在 UI 中以百分比显示。

### **磁盘读/写**

磁盘 I/O 从进程级别信息中聚合，并通过比较当前值与先前记录的值来计算吞吐量，所有这些都在 `src/metrics/disk.rs` 中完成。

```
// src/metrics/disk.rs (simplified example of delta calculation)
// In a real scenario, this involves iterating through disk information
// and calculating the change since the last collection.
let delta = read.saturating_sub(self.prev_read);
self.prev_read = read;
// ... (rest of the disk I/O collection logic)
```

这确保它显示的是实际的读/写速度（字节/秒），而不仅仅是累积总量。`saturating_sub` 可以防止在当前值以某种方式低于前一个值时发生下溢（尽管对于累积指标来说不太可能）。

### **网络流量**

网络流量通过跟踪接收（Rx）和传输（Tx）的字节数来测量。与磁盘 I/O 类似，每秒在 `src/metrics/network.rs` 中计算增量。

```
// src/metrics/network.rs
pub fn collect_rx(&mut self) -> u64 {
    self.networks.refresh(true); // Refresh network interfaces
    let (rx, _) = Self::aggregate(&self.networks); // Aggregate total received bytes
    let delta = rx.saturating_sub(self.prev_rx); // Calculate bytes received since last check
    self.prev_rx = rx; // Store current total for next calculation
    delta // Return the delta
}
// Similar logic for collect_tx
```

此函数收集所有网络接口接收到的总字节数，计算与上一秒的差值，并返回此增量，表示当前的接收吞吐量。

## **警报和 UI 系统详解**

### **终端仪表板 (ratatui)**

monitor-rs 的用户界面是使用 ratatui 库精心制作的，提供了一个清晰且信息丰富的仪表板。核心 UI 编排在 `src/ui/dashboard.rs` 中进行。它被组织成四个主要面板，每个面板都由其自己的小部件（`cpu_widget.rs`、`memory_widget.rs` 等）管理：

*   CPU：鲜绿色的仪表盘指示当前的 CPU 利用率。
*   内存：清晰的蓝色仪表盘显示 RAM 使用情况。
*   磁盘 I/O：以字节/秒为单位显示实时读写速度。
*   网络 I/O：以字节/秒为单位显示当前接收（Rx）和传输（Tx）的网络流量。
以下是 monitor-rs 仪表板的运行情况：

[![图 1：monitor-rs 的实时系统仪表板，显示 CPU、内存、磁盘和网络指标。](https://cdn.thenewstack.io/media/2025/10/1dbc09ae-image1-1024x307.png)](https://cdn.thenewstack.io/media/2025/10/1dbc09ae-image1-1024x307.png)

*图 1：monitor-rs 的实时系统仪表板，显示 CPU、内存、磁盘和网络指标。*

布局被高效地定义和渲染：

```
// src/ui/dashboard.rs
let layout = Layout::default()
    .direction(Direction::Vertical)
    .margin(1)
    .constraints([
        Constraint::Length(3), // CPU Gauge height
        Constraint::Length(3), // Memory Gauge height
        Constraint::Length(3), // Disk I/O Block height
        Constraint::Length(3), // Network I/O Block height
        Constraint::Min(0),    // Remaining space for alerts/other
    ])
    .split(f.area());
```

每个 UI 小部件随后都会接收最新的 `MetricSnapshot` 并相应地渲染实时值，确保显示始终保持最新。样式和颜色集中在 `src/ui/theme.rs` 中管理。

### **警报系统**

健壮的警报系统是一个关键功能，允许用户为各种指标定义自定义阈值。这些规则在 `src/alerting/rules.rs` 中定义：

```
pub fn default_rules() -> Vec<AlertRule> {
    vec![
        AlertRule {
            name: "High CPU Usage",
            threshold: 70.0,
            check: |snap| snap.cpu_usage > 70.0,
        },
        AlertRule {
            name: "High Memory Usage",
            threshold: 70.0,
            check: |snap| {
                if snap.total_memory == 0 {
                    false
                } else {
                    (snap.used_memory as f64 / snap.total_memory as f64) * 100.0 > 70.0
                }
            },
        },
        // ... more rules can be added here
    ]
}
```

`src/alerting/handler.rs` 模块负责获取 `MetricSnapshot` 并根据这些规则进行评估。如果满足定义的规则条件，则会触发警报并将其记录到项目根目录下的 `alerts.log` 文件中。这为性能事件提供了持久记录，供以后审查或与其他监控工具集成。

`alerts.log` 中的警报示例条目：

```
[*ALERT*] High CPU Usage triggered at 2025-05-25 20:26:49. Threshold: 5
[*ALERT*] High Memory Usage triggered at 2025-05-25 20:26:49. Threshold: 70
[*ALERT*] High CPU Usage triggered at 2025-05-25 20:26:50. Threshold: 5
[*ALERT*] High Memory Usage triggered at 2025-05-25 20:26:50. Threshold: 70
[*ALERT*] High CPU Usage triggered at 2025-05-25 20:26:51. Threshold: 5
[*ALERT*] High Memory Usage triggered at 2025-05-25 20:26:51. Threshold: 70
[*ALERT*] High CPU Usage triggered at 2025-05-25 20:26:53. Threshold: 5
[*ALERT*] High Memory Usage triggered at 2025-05-25 20:26:53. Threshold: 70
[*ALERT*] High CPU Usage triggered at 2025-05-25 20:26:54. Threshold: 5
[*ALERT*] High Memory Usage triggered at 2025-05-25 20:26:54. Threshold: 70
[*ALERT*] High CPU Usage triggered at 2025-05-25 20:26:55. Threshold: 5
```

## **主要收获**

Monitor-rs 展示了 Rust 开发中的几个强大功能和最佳实践：

*   实时资源监控，CPU 开销极小，使其高效适用于持续使用。
*   完全可扩展的设计，允许您轻松添加新指标、创建自定义小部件或定义更复杂的警报规则。
*   使用强大可靠的 Rust 库：[sysinfo](https://docs.rs/sysinfo/latest/sysinfo/) 用于系统数据，[ratatui](https://docs.rs/ratatui/latest/ratatui/) 用于基于文本的用户界面 (TUI) 渲染，[chrono](https://docs.rs/chrono/latest/chrono/) 用于时间处理，以及 [crossterm](https://docs.rs/crossterm/latest/crossterm/) 用于终端控制。
*   警报被持久化到文件中（`alerts.log`），这对于历史记录、主动监控甚至随着时间的推移审计系统性能来说都是无价的。
*   高度可移植，旨在在任何 Linux 或 macOS 系统上无缝运行。

## **总结**

无论您是构建内部工具、探索系统编程还是磨练您的 Rust 专业知识，monitor-rs 都展示了如何用惊人地少的代码量构建强大的终端应用程序。

这个项目仅用 700 行地道的 Rust 代码，就实现了实时监控、模块化架构和精美的终端界面，可媲美 GUI 替代方案。sysinfo 用于系统指标和 ratatui 用于界面的结合，创建了一个兼具高性能和可扩展性的基础。

模块化设计使得添加新指标、自定义显示或集成额外数据源变得非常简单，其生产就绪的代码展示了 Rust 在系统编程方面的优势。

通过 Andela 的指南《[使用 React、Chakra UI 和 Rust 构建 Docker 化的 Todo 应用程序](https://www.andela.com/blog-posts/building-a-dockerized-todo-app-with-react-chakra-ui-and-rust/?utm_medium=contentmarketing&utm_source=&utm_campaign=brand-global-the-new-stack&utm_content=docker-rust&utm_term=writers-room)》，深入了解 Rust 和 Docker。