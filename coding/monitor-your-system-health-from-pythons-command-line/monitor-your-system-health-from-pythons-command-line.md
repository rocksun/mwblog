
<!--
title: 从Python命令行监控你的系统健康
cover: https://cdn.thenewstack.io/media/2025/06/ca124f6f-ahmed-nvkeryvt3ck-unsplash-1.jpg
summary: 告别GUI！用Python `psutil` 库，在CLI玩转系统监控！实时掌握CPU、内存、磁盘I/O等指标，还能定制脚本，集成到`cron`、`systemd`，甚至CI/CD管道。动态诊断，自动化运维，DevOps工程师必备！云原生时代，效率UP！
-->

告别GUI！用Python `psutil` 库，在CLI玩转系统监控！实时掌握CPU、内存、磁盘I/O等指标，还能定制脚本，集成到`cron`、`systemd`，甚至CI/CD管道。动态诊断，自动化运维，DevOps工程师必备！云原生时代，效率UP！

> 译自：[Monitor Your System Health From Python's Command Line](https://thenewstack.io/monitor-your-system-health-from-pythons-command-line/)
> 
> 作者：Jessica Wachtel

[Python](https://thenewstack.io/python/) 的 `psutil` 库是一个强大的工具，可以实时了解系统的性能。你可以在自定义脚本、应用程序中使用它，或者直接从[命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/)中使用。

在[命令行界面 (CLI)](https://thenewstack.io/guis-cli-apis-learn-basic-terms-of-infrastructure-as-code/)中使用 `psutil` 可以提供速度、简单性和灵活性。它对于在终端中工作的开发人员、系统管理员和 DevOps 工程师特别有用。对于学习 CLI 和探索系统资源使用情况的初学者来说，这也是一个很好的切入点。

在以下情况下，你可能会选择在 CLI 中使用 `psutil` 而不是其他方法：

- 你需要动态诊断，例如在 CPU 突然飙升或意外内存使用期间。
- 你希望将系统检查集成到 shell 脚本或 cron 作业中（例如，检测僵尸进程）。
- 你喜欢最小的设置，而不是复杂的监控堆栈。

在 CLI 中使用 `psutil` 还有更多原因，并且许多原因也适用于其他基于 CLI 的脚本：

- 没有 GUI，开销更少。CLI 脚本轻量级、快速，并且可在包括 Windows、macOS 和 Linux 在内的多个平台上运行。
- 根据你关心的内容（CPU 使用率、内存压力、磁盘 I/O 或正在运行的进程）定制脚本，并以你喜欢的任何方式输出它们：纯文本、日志或 JSON。
- 易于自动化。基于 CLI 的 `psutil` 脚本可以轻松插入到 cron、`systemd` 定时器、CI/CD 管道或通过 SSH 进行的远程监控设置中。

## 在 CLI 中使用 `psutil`

首先，确保已安装 `psutil`。

在可以使用终端检查系统健康指标之前，你需要以交互方式运行 Python。

在终端中键入 `python3` 以开始：

### 检查 CPU 使用率

你的笔记本电脑风扇是否意外运行？可能是时候检查 CPU 使用率了。高 CPU 活动会产生热量，从而触发风扇。这可能意味着后台进程卡在循环中，或者更糟糕的是，恶意软件正在静默运行并消耗你的资源。

其他迹象包括一般的运行缓慢或系统无响应、突然的温度飙升或注意到僵尸和失效进程。

以下代码使用 `psutil` 的 `cpu_percent()` 函数。`interval=1` 表示它在一秒钟内测量 CPU 使用率，以提供更准确的读数。该函数返回正在使用的 CPU 百分比，并且 print 语句将其显示为可读的字符串：

```py
import psutil
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU usage: {cpu_percent}%")
```

这将显示你当前正在使用的 CPU 百分比。

### 检查内存使用情况

就像 CPU 一样，如果你的系统感觉运行缓慢或者应用程序意外冻结或关闭，可能是时候检查内存使用情况了。高内存警告是一个明确的信号，需要进行调查。

在下面的代码中，`psutil.virtual_memory()` 获取你的内存统计信息，包括总 RAM、已用 RAM 和可用 RAM。print 语句将值从字节转换为千兆字节，以便于阅读：

```py
mem = psutil.virtual_memory()
print(f"Total: {mem.total / (1024**3):.2f} GB")
print(f"Used: {mem.used / (1024**3):.2f} GB")
print(f"Available: {mem.available / (1024**3):.2f} GB")
print(f"Usage: {mem.percent}%")
```

### 检测到高内存使用率后

你可以随时运行此命令，但在发现高内存消耗后尤其有用。它显示了哪些进程正在使用最多的 RAM。

该代码遍历所有正在运行的进程，过滤掉那些不使用内存的进程，并打印一个列表，其中包含按最高内存使用量排序的进程：

```py

processes = [
    p for p in psutil.process_iter(['pid', 'name', 'memory_percent'])
    if p.info['memory_percent'] is not None
]

sorted_procs = sorted(processes, key=lambda p: p.info['memory_percent'], reverse=True)

for proc in sorted_procs[:5]:
    print("{:>5} {:<25} {:.2f}%".format(
        proc.info['pid'],
        proc.info['name'],
        proc.info['memory_percent']
    ))
```

### 将磁盘使用情况报告保存到日志

当你想要跟踪缓慢增长的存储问题、了解何时发生使用高峰、为监控和警报系统提供数据或只是以最小的影响自动收集磁盘数据时，这非常有用。

该代码首先获取当前日期和时间。然后 `psutil.disk_usage('/')` 提取根分区（你可以将 `/'` 更改为任何路径）的磁盘统计信息。它以 ISO 标准格式化时间，然后在追加模式下打开一个名为 disk_report.log 的文件，以便现有数据保持不变：

```py
from datetime import datetime

usage = psutil.disk_usage('/')
timestamp = datetime.now().isoformat()

with open('disk_report.log', 'a') as f:
    f.write(f"{timestamp} - Disk usage: {usage.percent}%\n")
```

你还可以将其安排为 cron 作业定期运行：

```py
0 * * * * /usr/bin/python3 /path/to/disk_report.py
```

## 结论

在 CLI 中使用 `psutil` 提供了一种快速、灵活的方式来监控系统的健康状况。这是以最小的设置和最大的控制来掌握系统性能的实际步骤。