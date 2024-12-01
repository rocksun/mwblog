# Linux内核6.12正式发布！支持实时应用，改进调度

![Linux内核6.12正式发布！支持实时应用，改进调度 的特色图片](https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux-1024x682.jpg)

截至2024年11月17日，最新的[Linux内核](https://www.kernel.org/)版本为6.12。它包含了对某些Linux社区用户来说非常重要的几个特性。6.12候选版本1于2024年9月29日发布，经历了相对平静的七个候选版本迭代测试期。我之前[在此](https://thenewstack.io/linux-kernel-6-12-prepped-for-superior-scheduling-real-time-ops/)讨论过内核6.12rc1。

现在内核6.12已完成，是时候决定是否立即实施了。本文回顾了最相关的特性，并提供了升级Linux设备的方法。

![](https://cdn.thenewstack.io/media/2024/11/9435442a-button.png)

## 内核6.12的关键特性

内核6.12的两个关键特性是实时应用程序支持和内核调度。当然还有许多新的或更新的组件，但这两者代表了最佳功能。

**实时计算**: 通过对系统强制执行时间约束来支持对时间敏感的应用程序。此功能已开发很长时间。**内核调度**: 改进了任务调度，提高了效率。

其他新的或更新的功能包括：

- 驱动程序（55%的更新）。
- 文档。
- ‘perf’性能监控工具改进。
- 围绕架构、文件系统管理和网络的核心内核开发。
- 改进了对Rust用于内核开发的支持。

确定这些特性是否会使您的组织受益，以[决定](https://thenewstack.io/learning-linux-start-here/)您是否需要立即实施新内核。

## 安装新内核

大多数组织都乐于等待主要发行版存储库更新后再安装新内核及其相应的功能。此处适用您的标准补丁测试和调度。

但是，基于Ubuntu的发行版可以使用[Mainline](https://github.com/bkw777/mainline)应用程序立即更新内核。首先安装Mainline，然后浏览可用的内核。Mainline还可以帮助您删除旧的内核。它主要设计用于Ubuntu及其相关发行版，但通常适用于任何[基于Debian的发行版](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/)。

使用[Red Hat Enterprise Linux](https://thenewstack.io/red-hat-enterprise-linux-9-5-arrives-with-enhanced-ai-support-and-automation/)及其相关发行版的企业客户通常会等待Red Hat完成测试后再通过标准更新和包管理器方法部署新内核。

SUSE Linux用户可以将Kernel:HEAD存储库添加到他们的包管理器中以获取最新的内核版本，或者等待[SUSE](https://thenewstack.io/linux-and-cloud-native-security-suses-strategy/)测试并通过标准存储库提供新内核。

查看您喜欢的发行版以了解安装内核6.12的说明。

使用uname -r或uname -a命令显示系统当前的内核版本。此信息应该可以帮助您确定内核更新是否值得。

![](https://cdn.thenewstack.io/media/2024/11/beef35d6-uname.png)

## 总结

内核更新提供了额外的稳定性、功能、安全选项等等，因此保持系统最新通常是一个好主意。在某些情况下，这意味着不必等待发行版供应商测试和集成新内核，因此您可以随时手动添加内核。对于大多数Linux用户来说，内核6.12可能就是这种情况。使用实时应用程序的团队将从这个新内核版本中获益最多。

请关注2025年发布的内核6.13的新闻。此版本可能包括对AMD EPYC和Intel Panther Lake CPU的处理改进、对M1之前Apple设备的支持增强、删除ReiserFS、额外的驱动程序等等。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)