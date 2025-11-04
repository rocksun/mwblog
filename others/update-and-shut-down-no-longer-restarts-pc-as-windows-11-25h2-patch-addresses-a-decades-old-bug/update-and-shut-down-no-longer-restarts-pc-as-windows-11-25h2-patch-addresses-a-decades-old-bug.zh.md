[![在 Windows 11 中更新并关机](https://www.windowslatest.com/wp-content/uploads/2025/11/Update-and-shut-down-in-Windows-11-696x403.jpg "在 Windows 11 中更新并关机")](https://www.windowslatest.com/wp-content/uploads/2025/11/Update-and-shut-down-in-Windows-11.jpg)

从 Windows 11 25H2 Build 26200.7019（或 24H2 上的 26100.7019）及更高版本开始，当您明确选择“**更新并关机**”时，您的电脑终于会关机。

如果您的电脑在“更新并关机”后重启，您并非孤单一人。这影响了 Windows 11 和 10，并且是最常报告的问题之一。Microsoft 在 Windows 10 中推出了一个有问题的“更新并关机”开关，但直到现在才承认。

我不想回忆有多少次被“更新并关机”欺骗了。当晚上 11 点，第二天早上要去上班，却有待处理的 Windows 更新时。我会选择**更新并关机**，然后上床睡觉，但第二天早上，如果电池没有耗尽，Windows 就会停留在登录界面。

![Windows 11 25H2 中的更新并关机选项](https://www.windowslatest.com/wp-content/uploads/2025/10/Update-and-shut-down-option-in-Windows-11-25H2.jpg)

由于这些更新选项并排显示，您可能会以为自己点击了“更新并重启”而不是“更新并关机”，这可以解释返回登录界面的原因。但实际上，这一直是一个 Windows 错误，如果您无法信任“更新并关机”按钮，您并非孤单一人。

我们不知道究竟是什么原因导致“更新并关机”重启 Windows。但 Microsoft 证实，2025 年 10 月的可选更新（[KB5067036](https://www.windowslatest.com/2025/10/29/windows-11-kb5067036-25h2-adds-new-start-ui-direct-download-links-msu/)）最终修复了一个潜在问题，该问题在某些情况下阻止了“更新并关机”正常工作。

Microsoft 在一份支持文档中[指出](https://support.microsoft.com/en-us/topic/october-28-2025-kb5067036-os-builds-26200-7019-and-26100-7019-preview-ec3da7dc-63ba-4b1d-ac41-cf2494d2123a#)：“解决了可能导致‘更新并关机’在更新后未能实际关闭电脑的潜在问题。”

Microsoft 告诉 Windows Latest，它将在 11 月 11 日的补丁星期二发布“更新并关机”的修复程序，因此可选更新 (KB5067036) 不是必需的。

## 为什么 Windows 11 和 Windows 10 中的“更新并关机”会出问题

Microsoft 不会告诉我们到底发生了什么，但有可能是竞态条件或 Windows 服务堆栈的问题。

当您使用“更新并关机”时，Windows 有两项任务要执行。首先，它将开始安装所有待处理的更新。其次，它将在过程结束时关闭计算机，但关键是这个过程不仅仅是“安装更新并关机”。

![正在处理更新](https://www.windowslatest.com/wp-content/uploads/2025/09/Working-on-updates.jpg)

Windows 不能仅仅因为您告诉它在更新后关机就跳过重启。它必须重启进入脱机服务阶段，此时您会在屏幕上看到“正在处理更新”。这一步是必需的，因为 Windows 在运行时无法完成文件替换。

在“正在处理更新”阶段之后，Windows 应该最终关机，但它没有，而是启动到登录界面。问题很可能出在服务堆栈上，“关机”任务从未在 Windows 重启之间延续。它要么被清除，要么像快速启动这样的竞态条件阻碍了它。

[主页](/)

分享
[时事通讯](#fluentform_4)

订阅

![](https://www.windowslatest.com/wp-content/plugins/push-notification-for-post-and-buddypress/public//img/pushbell-pnfpb.png)

![](https://www.windowslatest.com/wp-content/plugins/push-notification-for-post-and-buddypress/public//img/pushbell-pnfpb.png)

订阅推送通知