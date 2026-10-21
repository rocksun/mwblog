Christian Schaller 是红帽公司的工程总监，也是 GNOME 和 Fedora 的长期贡献者。他有一箱老旧的家庭底片需要数字化，但他的扫描仪却无法与 Linux 兼容。他购买了 Plustek OpticFilm 8200i 扫描仪，因为它的列表上显示受支持，但随后却发现制造商悄悄更换了芯片组，导致任何 Linux 驱动都无法识别。他曾尝试让 Claude Code 编写一个能正常工作的驱动，但很长一段时间毫无进展，于是他最终将这个项目搁置了几个月。

当他重新开始这个项目时，[Schaller](https://www.linkedin.com/in/cschalle/) 尝试了不同的方法。在几个小时内，他就得到了第一次能被识别的扫描结果。几天后，该驱动程序还支持了红外扫描。

此后，Schaller [以 MIT 许可证将底层方法作为一个名为 hw-harness 的开源项目进行了发布](https://github.com/cschalle/hw-harness)。它捆绑了一系列工具，用于捕获设备行为、对比能正常工作的实现与损坏的实现，并为编码智能体提供在 Linux 尚不支持的硬件上工作所需的信息。

## 对扫描仪驱动进行逆向工程

Schaller 的灵感来自于 X 平台上的[一则帖子](https://x.com/GloriousEggroll/status/2103816580966830314)，发帖人是 Tom Crider（更为人熟知的名字是 Glorious Eggroll），他曾通过让 AI 智能体访问 Windows 机器来修复鼠标驱动程序。Schaller 将这篇帖子喂给 Claude，并要求它为他的扫描仪构建一个类似的设置。

在他 [周三发布的文章](https://blogs.gnome.org/uraeus/2026/10/15/aiandreverseengineerhardware/) 中，Schaller 描述了从 USB 捕获、寄存器值和控制传输中拼凑出未公开设备协议的繁琐过程。尽管这项工作本身不是很复杂，但他表示，这“需要大量的耐心和技巧”。他早期使用 Claude 构建 SANE 后端程序的尝试陷入了停滞，因为该智能体没有可供对比的可用驱动程序。

有了新设置后，Claude 可以运行制造商的 Windows 软件，捕获 USB 流量，并将其与他的 Linux 驱动程序发送的内容进行对比。它以 Windows 驱动程序为参考，找出 Linux 实现出错的地方，并做出了相应的修改。

> 正如 Schaller 所说，Claude “不会感到厌烦。”

Schaller 认为，Claude Code 自身的改进可能也发挥了作用。更好的是，正如 Schaller 所说，Claude “不会感到厌烦。” 他仍然必须在扫描仪上测试这些更改，因为生成看起来正确的代码与编写一个真正能工作的驱动程序是两码事。

当 Schaller 完成工作时，他的驱动程序已经不再是唯一的选择了。得益于另一位开发人员的贡献，对较新版本 OpticFilm 8200i 的支持已于 9 月登陆 SANE。“这种情况时有发生，”他写道。Schaller 不打算维护一个相互竞争的驱动程序，并表示当 upstream 版本具备他想要的功能时，他会切换到 upstream 版本，而他自己的版本则保留为概念验证。

## 更快的 SANE 扫描仪驱动

他的实现确实有一些优势。它支持用于密集底片的红外除尘和曝光调整，以及 300 到 7,200 dpi 的彩色和灰度扫描。引发整个项目硬件差异的原因是芯片组的更换：较新的 8200i 扫描仪使用的是 Genesys GL128，取代了 SANE 已经支持的 GL845。

Schaller 还[将这两个驱动程序放入单帧测试中](https://htmlpreview.github.io/?https://github.com/cschalle/OpticFilm8200i-sane/blob/main/docs/comparison/drivers-comparison.html)。他的驱动程序在 34.6 秒内完成了全分辨率扫描；upstream 版本则花了 54.4 秒。两者在 3,600 dpi 下解析出了相同的细节，尽管 SANE 支持更多的分辨率选项。这是一个有限的对比，但 Schaller 最终得到了一个可用的驱动程序以及一种可以应用于其他硬件的方法。

扫描仪项目还给了 Schaller 一个构建自己应用程序的理由。他将其命名为 [Negative Vibes](https://github.com/cschalle/negative-vibes)，在 Claude 的帮助下用 Rust 编写，这个 GNOME 应用程序完整保留了原始的 16 位扫描数据，包括红外通道。在此基础上，用户可以去除灰尘、在不修改原图的情况下调整图像、使用 ArgyllCMS 进行色彩校正，并将结果导出为 TIFF、JPEG、PNG 或 DNG 文件。

> 他将其命名为 Negative Vibes，在 Claude 的帮助下用 Rust 编写，这个 GNOME 应用程序完整保留了原始的 16 位扫描数据，包括红外通道。

## 修复 ThinkPad 摄像头

Schaller 还遇到了他的联想 ThinkPad X1 Carbon Gen 14 Aura Edition 上的摄像头问题。在 Linux 下，拍摄出的图像太暗，角落明显较暗，并且带有黄绿色调。这款笔记本电脑使用的是索尼 IMX471 传感器和英特尔的 IPU7 成像系统，但与扫描仪不同的是，它的内部 MIPI 摄像头没有供 Claude 检查的 USB 流量。

他的解决方法是将 Windows 驱动程序的配置文件、注册表项、ACPI 表和设备属性喂给 Claude。他还连接了一个 USB 网络摄像头，为它提供一个正常工作的摄像头来进行对比。事实证明，这正是关键所在。到一天结束时，他已经拥有了 Linux 内核和 libcamera 的补丁。

[内核修复程序](https://cschalle.github.io/mipi-fixes-x1-aura/) 解决了三个问题：一个使 libcamera 使用错误像素区域的裁剪选择漏洞、一个定义错误的测试模式寄存器，以及一个导致摄像头损失约 1.8 档灵敏度的模拟增益限制。Claude 还发现了 libcamera 图像处理中的问题。缺失的镜头阴影校正使得角落比中心暗约 2.7 档，而传感器数据与黑电平计算方式的不匹配则打乱了白平衡。

这种差异是显而易见的。在 Schaller 的暗光测试中，画面亮度从 31.1 提升到了 90.9，且色彩比例比之前更加接近参考网络摄像头。

仍有工作要做。在暗光环境下，蓝色通道仍比参考值低约 17% 左右，并且这两组补丁都尚未合并。英伟达的 AI 开发者技术工程师 [Kate Hsuan](https://www.linkedin.com/in/kate-cheng-26051420b/) 正在审查内核更改，而红帽的首席软件工程师 [Wim Taymans](https://www.linkedin.com/in/wim-taymans-6a4a099/) 则在处理 libcamera 的工作。另一个由 Claude 生成的 Linux 页面缓存修复程序[最近在审查过程中遇到了竞争条件（race condition）](https://thenewstack.io/torvalds-claude-code-kernel/)。

此后，Schaller [在 GitHub 上发布了 hw-harness](https://github.com/cschalle/hw-harness)。他指出，发布的版本并不是他在扫描仪和摄像头项目中所使用的确切工具。相反，该设置在 KVM 虚拟机中运行制造商的 Windows 驱动程序，并将物理设备直通给虚拟机客体。Claude 远程操作 Windows 会话，而 `usbmon` 则在 Linux 主机上捕获流量。接着，开发人员将设备切换回 Linux，使用实验性驱动程序重复该操作，并让 Claude 对比追踪结果。

该代码库包含了用于控制 Windows 虚拟机的 `winctl`、用于捕获流量的 `usbcap`、用于在主机和虚拟机之间切换设备的 `hostdev`，以及用于 Linux 端调试的 `hwdbg`。PowerShell 脚本负责收集设备描述符、注册表项、ACPI 表和 INF 文件。

他说，这种方法可以产出一个“维护人员真正能够合并”的驱动程序。许可问题依然存在，并且这种通用的工具尚未在各种各样的硬件上进行广泛测试。

> 他说，这种方法可以产出一个“维护人员真正能够合并”的驱动程序。