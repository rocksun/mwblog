# 如何在 MacOS、Windows 和 Linux 上运行 Python 脚本

![特色图片：如何在 MacOS、Windows 和 Linux 上运行 Python 脚本](https://cdn.thenewstack.io/media/2025/04/2b530c1e-how-to-run-python-script-1024x683.jpg)

不要每次运行 Python 都复制粘贴相同的命令。本指南将教你运行 Python 脚本的实用方法，无论你使用哪种操作系统、编辑器或自动调度程序。

## 什么是“Python 脚本”？

它是任何包含 Python 代码的纯文本文件，通常以 `.py` 扩展名保存。

在本教程中，我们将使用一个密码生成器脚本。此脚本还包括 Python 模块 `random`。Python 模块是一个包含 Python 代码（函数、类、变量）的文件，可以导入并在其他 Python 程序中重复使用。Python 模块旨在导入和重用，而脚本旨在直接执行以执行特定任务。

## 从命令行运行脚本

### MacOS 和 Linux

打开终端并键入以下命令来运行密码生成器脚本：

如果你想让它可执行并像应用程序一样运行，请按照以下步骤操作：

- 在代码顶部添加一个 shebang。Shebang 告诉操作系统使用 Python 解释器（在本例中为 Python 3），这样你就不需要每次都输入 `python3`。你的代码现在将像这样开始：
- 授予执行权限：
2. 直接运行脚本：

### Windows 10/11

Python 安装时带有一个名为 `py` 的启动器。使用它来运行你的脚本：

或者，如果 Python 设置在你的 PATH 中，你可以运行以下命令：

如果你收到类似 `'python' is not recognized` 的错误，请重新运行安装程序并选中“Add Python to PATH”，或者直接使用 `py` 启动器。

## 传递命令行参数

传递命令行参数允许用户提供输入，而无需更改原始代码。它通过使你的脚本更灵活和模块化来促进一些 Pythonic 原则。传入命令行参数允许一个脚本有效地处理不同的任务或设置。

你需要更新原始密码生成器代码文件以包含 argparse 模块。除了导入 `argparse` 之外，我们将添加一个函数来解析输入并将 `length` 参数传递到 `generate_password()` 中的 `__main__` 块。

如果你在 macOS 或 Linux 上运行脚本，你还需要在文件顶部添加一个 shebang（例如，`#!/usr/bin/env python3`）。此行告诉操作系统在直接执行脚本时使用哪个解释器。

现在我们准备好了！

### MacOS / Linux

- 使脚本可执行：
2. 使用参数运行它：

### Windows

Windows 不像 Unix 系统那样使用 shebang (`#!/usr/bin/env python3`)。但是你仍然可以使用 `python` 或 `python3` 从命令提示符或 PowerShell 运行脚本。

打开命令提示符（或 PowerShell）：

按 `Win + R`，键入 `cmd` 或 `powershell`，然后按 Enter。

- 导航到正确的文件夹
2. 现在使用自定义长度运行脚本：

## 在 IDE 中运行 Python 脚本

在 IDE 中运行脚本为你提供有用的工具，如自动完成、调试和可视化反馈。它非常适合开发。对于更复杂的项目，它比使用命令行更全面。

### 在 PyCharm 中运行 Python

PyCharm 是一个强大的 Python IDE，具有智能编辑、调试和项目工具，可简化开发。它擅长代码完成、调试以及与版本控制和虚拟环境的集成。

- 打开 PyCharm 并创建或打开一个项目。
- 在编辑器中打开 password_generator.py。
- 单击绿色的 ▶ 运行按钮（或按 Shift + F10）。
- PyCharm 会记住运行配置，因此下次你可以一键运行它。

### Visual Studio Code

VS Code 比 PyCharm 更快、更轻、更灵活——非常适合多语言项目和自定义设置。

- 如果需要，安装 Python 扩展。
- 单击解释器名称（左下角）并选择你的 Python 版本。
- 按 F5 或单击文件顶部的 ▶ 运行 Python 文件。

### Jupyter Notebook/JupyterLab

Jupyter Notebook 不是像 VS Code 或 PyCharm 这样的传统 IDE。它以交互式的、基于单元格的执行和实时可视化而著称，所有这些都在一个文档中。Jupyter 非常适合数据分析，但也运行常规 Python 脚本。

Jupyter Notebooks 是我构建教程的首选方式。当我构建应用程序时，我使用 VS Code。

有很多方法可以在 Jupyter 中运行 Python，但这里有一个例子。此示例侧重于在 Jupyter 笔记本中构建和运行代码。它不使用任何保存在其他地方的文件。

我们需要调整我们的 `password_generator.py` 代码，然后它才能在 Jupyter 中工作。

单击运行按钮（左上角的 ▶）后，脚本将要求输入密码长度。输入数字，按 Enter，它将生成你的密码。

## 自动计划和运行脚本

### MacOS 和 Linux: `cron`
`cron`
非常适合用于重复性任务以及在特定时间运行脚本。

**Cron (macOS/Linux)**

*   打开 crontab：

    ```bash
    crontab -e
    ```
*   添加一行以每天凌晨 3:00 运行您的脚本：

    ```cron
    0 3 * * * /usr/bin/python3 /path/to/your/script.py
    ```

现在将按照其指定的时间表运行此脚本。您可以使用以下代码记录输出：

```cron
0 3 * * * /usr/bin/python3 /path/to/your/script.py >> /path/to/your/log.txt 2>&1
```

**Windows：任务计划程序**

*   从“开始”菜单打开“任务计划程序”。
*   单击“创建任务…”（避免使用“基本任务”，因为它受到限制）。
*   在“常规”选项卡上：命名任务并选择“无论用户是否登录都要运行”。
*   在“触发器”选项卡上：单击“新建…”以设置计划。
*   在“操作”选项卡上：
    *   程序/脚本：路径到 `python.exe`（例如，`C:\Users\you\venv\Scripts\python.exe`）
    *   添加参数：脚本的路径（例如，`C:\Projects\password_generator.py`）
*   单击“确定”并输入您的 Windows 密码。

**Linux 服务器：`systemd` 定时器**

`systemd` 是 `cron` 的一种现代替代方案，可确保脚本即使在重新启动后也能运行。以下命令每天凌晨 3 点运行脚本。

创建一个新的定时器文件：

```bash
sudo nano /etc/systemd/system/my-script.service
```

```ini
[Unit]
Description=Run my script daily

[Service]
ExecStart=/usr/bin/python3 /path/to/your/script.py
WorkingDirectory=/path/to/your/script/directory
User=yourusername

[Install]
WantedBy=multi-user.target
```

创建一个定时器文件：

```bash
sudo nano /etc/systemd/system/my-script.timer
```

```ini
[Unit]
Description=Run my script daily

[Timer]
OnCalendar=*-*-* 03:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

启用：

```bash
sudo systemctl enable my-script.timer
sudo systemctl start my-script.timer
```

## 快速故障排除

错误是过程的一部分。如果在执行 Python 脚本时遇到错误，以下是一些快速故障排除技巧，可帮助您回到正轨。

**`ModuleNotFoundError`**

确保您的虚拟环境已激活：

*   Unix：

    ```bash
    source venv/bin/activate
    ```
*   Windows：

    ```powershell
    .\venv\Scripts\activate
    ```

**`Permission denied` (Unix)**

使用 `chmod +x script.py` 使脚本可执行，或使用 `python3 script.py` 运行。

**PATH 混淆**

使用绝对路径（`/usr/bin/python3`, `C:\Projects\password_generator.py`）以避免环境问题。

## 最佳实践

以下是一些最佳实践技巧，您可以在脚本顺利运行后实施。

*   使用虚拟环境隔离依赖项。
*   冻结依赖项以锁定版本。
*   通过保护入口点来避免导入时意外执行。
*   使用 PyInstaller 打包脚本，用于没有 Python 的系统。

## 结论

现在您已经了解了如何在 macOS、Windows 和 Linux 上运行 Python 脚本，您已经拥有了将您的想法从概念转化为执行所需的一切，无论平台如何。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。 订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。