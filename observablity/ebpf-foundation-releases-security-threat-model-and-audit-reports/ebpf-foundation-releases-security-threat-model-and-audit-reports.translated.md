# eBPF 基金会发布安全威胁模型和审计报告

![Featued image for: eBPF Foundation Releases Security Threat Model and Audit Reports](https://cdn.thenewstack.io/media/2024/11/f8693200-ebpf-foundation-1024x683.png)

盐湖城——本月早些时候在[KubeCon+CloudNativeCon 北美](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)，[eBPF 基金会](https://ebpf.foundation/)宣布发布了两份关于内核 Linux [eBPF](https://ebpf.io/)编程范例安全的第三方报告：[Control Plane](https://controlplane.com/)的[eBPF 安全威胁模型](https://www.linuxfoundation.org/hubfs/eBPF/ControlPlane%20%E2%80%94%20eBPF%20Security%20Threat%20Model.pdf)和[NCC 集团](https://www.nccgroup.com/us/)的[eBPF 验证器代码审计](https://www.nccgroup.com/media/4lilthtf/ncc_group_nccgroup_e015561_report_2024-11-11_v10.pdf)。由于[eBPF](https://thenewstack.io/what-is-ebpf/)是许多安全程序的核心，因此确保 eBPF 本身确实安全是很有必要的。

特别是，这些报告重点关注新的[eBPF 安全威胁模型](https://www.linuxfoundation.org/hubfs/eBPF/ControlPlane%20%E2%80%94%20eBPF%20Security%20Threat%20Model.pdf)和相应的审计。它们提供了对潜在 eBPF 安全风险（所有事物都存在安全隐患）和相关缓解策略的全面概述。

毕竟，eBPF 本身就能够使工具在沙箱中利用底层 Linux 内核访问权限。它的安全性来自于[eBPF 验证器](https://docs.kernel.org/bpf/verifier.html)、即时 (JIT) 编译器和一些自动缓解措施，并且它还允许通过功能实现更细粒度的权限授予。这使得 eBPF 成为每个人进行深度 Linux 编程的首选。

然而，能力越大，责任越大。在 eBPF 的情况下，这种能力可能导致绕过传统的安全工具或尝试以 eBPF 安全工具无法识别的方式执行攻击。

这并不是说传统的安全措施毫无用处。例如，许多潜在的拒绝服务 (DoS) 攻击可以通过阻止以 CAP_SYS_ADMIN 或 root 身份运行的程序来阻止。

其他熟悉的安全建议包括：

- 授予 eBPF 程序权限时，请遵守最小权限原则。
- 通过强大的供应链安全实践，确保 eBPF 工具和库的完整性。
- 使用最新的安全补丁更新内核和 eBPF 工具。
- 实施全面的监控和日志记录，以检测和响应事件。
- 定期进行威胁建模练习。
- 默认情况下禁用非特权 eBPF 以最大限度地减少攻击面。

eBPF 安全威胁模型更详细地介绍了此类攻击。它还提供了对可能影响 eBPF 实现的潜在漏洞和攻击向量的见解。

## eBPF 审计报告

除了威胁模型之外，eBPF 基金会还提供了一份审计报告。这份文档可能提供了对 eBPF 当前安全态势和改进建议的深入分析。

具体来说，NCC 集团的审查包括：

- 确定 eBPF 验证器试图证明的属性。
- 对 eBPF 验证器主要逻辑的源代码审查，通常通过 `kernel/bpf/verifier.c` 中的 `do_check()` 函数调用。
- 任何可能允许 eBPF 源代码绕过验证器约束从而破坏 eBPF 验证器正确操作的问题，从而导致标准的机密性、完整性和可用性问题。

在进行此审查时，NCC 集团发现了一个值得注意的缺陷，该缺陷可能允许特权攻击者读取和写入任意内核内存 (`find_equal_scalars`)。此安全漏洞已得到修复。

分析师还发现了一些其他代码弱点。缺乏防御性代码，尤其是在检查数组边界和指针有效性方面。此外，一些过长和复杂的函数被确定为重构的候选对象。与以往一样，文档应该更清晰，尤其是在验证器的检查方面。

eBPF 基金会积极主动地解决安全问题值得赞扬。这表明它致力于为这项强大的技术打造一个安全的生态系统。现在，如果其他重要的软件程序也能效仿其做法，在攻击者发现安全漏洞之前先找到并修复它们就好了。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)