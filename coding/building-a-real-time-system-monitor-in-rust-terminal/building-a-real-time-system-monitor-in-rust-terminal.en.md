System monitoring tools are everywhere, but most are either heavyweight GUI applications or basic command-line utilities that dump static information. What if you could build something in between; a live, interactive terminal dashboard that’s both lightweight and powerful?

That’s exactly what I set out to create with monitor-rs. After working on various system tools, I wanted to explore how [Rust](https://thenewstack.io/the-case-for-rust-as-the-future-of-javascript-infrastructure/)‘s unique features could solve the classic challenges of real-time monitoring: managing concurrent data collection, handling errors gracefully and presenting information clearly without consuming excessive resources.

Monitor-rs tracks CPU usage, memory consumption, disk I/O and network activity in real time, all within a clean terminal interface. This is a practical exploration of what makes  [Rust particularly well-suited](https://thenewstack.io/rusts-expanding-horizons-memory-safe-and-lightning-fast/) for systems programming.

Let’s dig into the implementation details that matter:

* **Zero-cost abstractions**: See how high-level code compiles down to highly efficient machine instructions.
* **Ownership and borrowing**: Understand how [Rust’s unique memory management](https://thenewstack.io/rust-pythons-new-performance-engine/) ensures thread safety without a garbage collector.
* **Fearless concurrency**: Explore how channels and threads are used to manage complex, real-time data flows safely.
* **Robust error handling**: Witness the power of `Result` for building resilient applications.
* **Powerful ecosystem and crates**: Discover how libraries like `sysinfo` and `ratatui` seamlessly extend Rust’s capabilities.
* **Modular design**: Appreciate how Rust’s module system facilitates clear separation of concerns for maintainability.

## **Prerequisites**

Before diving into the code, you’ll need a few things:

* Basic Rust knowledge: Familiarity with concepts like structs, modules and threads will be beneficial.
* A Linux or macOS system: Monitor-rs has been primarily tested on Ubuntu 22.04.
* Familiarity with the terminal: As this is a terminal-based application, comfort with command-line interfaces is helpful.
* Rust and Cargo installed: If you don’t have Rust installed, you can do so with the following command:

`curl --proto '=https' --tlsv1.2 -sSf [https://sh.rustup.rs](https://sh.rustup.rs) | sh`

## **What Is** **monitor-rs****?**

Monitor-rs is a real-time terminal dashboard designed to display critical system performance metrics. It provides insights into:

* CPU usage: See your processor’s utilization at a glance.
* Memory (RAM) utilization: Track how much of your system’s memory is in use.
* Disk read/write throughput: Monitor your storage device’s activity.
* Network traffic: Keep an eye on incoming and outgoing network data.
* Alerting system: Get notified when customizable performance thresholds are exceeded.

It achieves this robust functionality with key Rust libraries:

* [**sysinfo**](https://docs.rs/sysinfo/latest/sysinfo/): For efficient and cross-platform system statistics collection.
* [**Ratatui**](https://docs.rs/ratatui/latest/ratatui/): For rendering the dynamic and interactive TUI dashboard.
* Modular Rust design: Ensuring an easily extensible and maintainable codebase.

## **The** **monitor-rs** **Project Structure: A Modular Deep Dive**

One of the strengths of monitor-rs is its clean, modular architecture. This design principle ensures that different functionalities are well-separated, making the codebase easier to understand, maintain and extend. Here’s a look at the project’s directory layout:

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

This structure clearly delineates responsibilities: `metrics` handles data gathering, `alerting` manages threshold checks, and `ui` is solely concerned with presentation. This separation is key to monitor-rs’s extensibility.

## **Setup and Running the Project**

Getting monitor-rs up and running on your system is straightforward. Follow these steps:

### **Get the Code and Build**

First, clone the monitor-rs repository from GitHub to your local machine. Open your terminal and run:

```
git clone https://github.com/Tinega-Devops/monitor-rs.git
cd monitor-rs
```

Once inside the project directory, compile the application. We recommend building in release mode for optimal performance, as this applies Rust’s full suite of optimizations.

`cargo build --release`

This command will compile monitor-rs and its dependencies. The resulting executable will be placed in the `target/release/` directory.

### **Run the Monitor**

After the compilation is complete, start monitor-rs.

To run the optimized release build:

`./target/release/monitor-rs`

Alternatively, if you’re in the project root and haven’t changed the code since the last build, you can use `cargo run --release`, which will recompile if necessary and then execute the optimized binary:

`cargo run --release`

You’ll instantly see a dynamic, real-time system dashboard appear in your terminal. To quit the application, simply press the `q` key.

## **The Metrics Engine (CPU, Memory, Disk, Network)**

The core of monitor-rs lies in its independent metrics collectors, residing in the `src/metrics/`directory. Each collector is responsible for refreshing specific system values, typically on a one-second interval, ensuring real-time accuracy.

### **CPU Usage**

The CPU usage is collected efficiently using the sysinfo library, specifically within `src/metrics/cpu.rs`.

```
// src/metrics/cpu.rs
pub fn collect(&mut self) -> f32 {
    self.sys.refresh_cpu_all();
    self.sys.global_cpu_usage()
}
```

This snippet first refreshes all CPU information systemwide, then retrieves the overall global CPU usage as a percentage.

### **Memory Usage**

Memory metrics capture both total and used RAM, allowing for a precise utilization calculation, handled in `src/metrics/memory.rs`.

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

It captures the total available memory and the currently used memory, then calculates the ratio to display as a percentage in the UI.

### **Disk Read/Write**

Disk I/O is aggregated from process-level information, and throughput is calculated by comparing current values to previously recorded ones, all within `src/metrics/disk.rs`.

```
// src/metrics/disk.rs (simplified example of delta calculation)
// In a real scenario, this involves iterating through disk information
// and calculating the change since the last collection.
let delta = read.saturating_sub(self.prev_read);
self.prev_read = read;
// ... (rest of the disk I/O collection logic)
```

This ensures it’s displaying actual read/write speeds (in bytes per second ) rather than just cumulative totals. The `saturating_sub` prevents underflow if the current value somehow drops below the previous one (though unlikely for cumulative metrics).

### **Network Traffic**

Network traffic is measured by tracking received (Rx) and transmitted (Tx) bytes. Similar to disk I/O, deltas are computed each second in `src/metrics/network.rs`.

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

This function collects the total received bytes across all network interfaces, calculates the difference from the previous second, and returns this delta, representing the current received throughput.

## **Explaining the Alerting and UI System**

### **Terminal Dashboard (****ratatui****)**

The user interface of monitor-rs is meticulously crafted using the ratatui library, providing a clean and informative dashboard. The core UI orchestration happens in `src/ui/dashboard.rs`. It’s organized into four primary panels, each managed by its own widget (`cpu_widget.rs`, `memory_widget.rs`, etc.):

* CPU: A vivid green gauge indicating current CPU utilization.
* Memory: A clear blue gauge displaying RAM usage.
* Disk I/O: Shows real-time read and write speeds in bytes per second.
* Network I/O: Presents current received (Rx) and transmitted (Tx) network traffic in bytes per second.  
  Here’s a look at the monitor-rs dashboard in action:

[![Figure 1: The real-time system dashboard of monitor-rs, displaying CPU, memory, disk and network metrics.](https://cdn.thenewstack.io/media/2025/10/1dbc09ae-image1-1024x307.png)](https://cdn.thenewstack.io/media/2025/10/1dbc09ae-image1-1024x307.png)

Figure 1: The real-time system dashboard of monitor-rs, displaying CPU, memory, disk and network metrics.

The layout is defined and rendered efficiently:

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

Each UI widget then receives the latest `MetricSnapshot` and renders the live values accordingly, ensuring the display is always up to date. Styling and colors are centrally managed in `src/ui/theme.rs`.

### **Alerting System**

A robust alerting system is a critical feature, allowing users to define custom thresholds for various metrics. These rules are defined in `src/alerting/rules.rs`:

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

The `src/alerting/handler.rs` module is responsible for taking the `MetricSnapshot` and evaluating it against these rules. If a defined rule’s condition is met, an alert is triggered and logged to the `alerts.log` file at the project root. This provides a persistent record of performance events for later review or integration with other monitoring tools.

Example alert entry in `alerts.log`:

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

## **7. Key Takeaways**

Monitor-rs demonstrates several powerful capabilities and best practices in Rust development:

* Real-time resource monitoring with minimal CPU overhead, making it efficient for continuous use.
* A fully extensible design, allowing you to easily add new metrics, create custom widgets or define more sophisticated alert rules.
* Uses powerful and reliable Rust libraries: [sysinfo](https://docs.rs/sysinfo/latest/sysinfo/) for system data, [ratatui](https://docs.rs/ratatui/latest/ratatui/) for text-based user interface (TUI) rendering, [chrono](https://docs.rs/chrono/latest/chrono/) for time handling and [crossterm](https://docs.rs/crossterm/latest/crossterm/) for terminal control.
* Alerts are persisted to a file (`alerts.log`), which can be invaluable for historical logging, proactive monitoring or even auditing system performance over time.
* Highly portable, designed to run seamlessly on any Linux or macOS system.

## **8. Conclusion**

Whether you’re building internal tools, exploring systems programming or sharpening your Rust expertise, monitor-rs demonstrates how powerful terminal applications can be built with surprisingly little code.

In just 700 lines of idiomatic Rust, this project delivers real-time monitoring, modular architecture and a polished terminal interface that rivals GUI alternatives. The combination of sysinfo for system metrics and ratatui for the interface creates a foundation that’s both performant and extensible.

The modular design makes it straightforward to add new metrics, customize the display or integrate additional data sources, with production-ready code that showcases Rust’s strengths in systems programming.

Take a deep dive into Rust and Docker with Andela’s guide “[Building a Dockerized Todo App With React, Chakra UI and Rust](https://www.andela.com/blog-posts/building-a-dockerized-todo-app-with-react-chakra-ui-and-rust/?utm_medium=contentmarketing&utm_source=&utm_campaign=brand-global-the-new-stack&utm_content=docker-rust&utm_term=writers-room)”.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/01/48c6472d-tinegaonchari.jpg)

Tinega is a Senior DevOps Engineer and a technologist for Andela, a private global marketplace for tech talent. Tinega began his tech career in 2018 after completing the Google Africa Developer Scholarship, Andela’s learning program in partnership with Google. Tinega...

Read more from Tinega Onchari](https://thenewstack.io/author/tinega-onchari/)