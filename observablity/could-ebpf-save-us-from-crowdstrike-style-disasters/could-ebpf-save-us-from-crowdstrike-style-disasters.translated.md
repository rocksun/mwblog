# eBPF 能否拯救我们免受 CrowdStrike 式灾难？

![Featued image for: Could eBPF Save Us From CrowdStrike-Style Disasters?](https://cdn.thenewstack.io/media/2024/07/d386ecaf-ebpf-1024x683.png)

英特尔研究员兼系统专家 Brendan Gregg 认为，eBPF 可以防止未来出现类似 Crowdstrike 的灾难。但其他人对此并不确定。

在 [CrowdStrike Windows 安全事故](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/) 之后，安全专家和开发人员都在寻找更安全的方式来运行低级安全程序。在最近的一篇博文中，备受尊敬的系统性能专家、英特尔研究员 [Brendan Gregg](https://au.linkedin.com/in/brendangregg) 建议 [我们可以防止计算机因错误的软件更新而崩溃](https://www.brendangregg.com/blog/2024-07-22/no-more-blue-fridays.html)，即使这些更新涉及内核代码，“这要归功于 [eBPF](https://ebpf.io/)”。

现在，我喜欢 eBPF——这款瑞士军刀程序，[它允许您在 Linux 内核中的虚拟机 (VM) 中运行软件](https://thenewstack.io/swifts-chris-lattner-on-the-possibility-of-machine-learning-enabled-compilers/)。正如 [Isovalent](https://isovalent.com/) 的 CTO 兼联合创始人 Thomas Graf 在 [CloudNativeSecurityCon](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america/) 上的演讲中所说，“通过允许沙箱程序在操作系统中运行，eBPF 使开发人员能够创建在运行时为操作系统添加功能的程序。[操作系统](https://thenewstack.io/choosing-an-operating-system-and-container-runtime-for-your-cloud-native-stack/) 然后通过 Just-In-Time (JIT) 编译器和验证引擎的帮助，保证安全性和执行效率，就像原生编译一样。

深入探讨安全问题，Gregg 写道：“eBPF 程序无法使整个系统崩溃，因为它们会受到软件验证器的安全检查，并且实际上是在沙箱中运行。如果验证器发现任何不安全的代码，程序将被拒绝执行。”

他继续说，[思科最近收购了 Isovalent](https://isovalent.com/blog/post/cisco-acquires-isovalent/)，并宣布了一款新的 eBPF 安全产品：[Cisco Hypershield](https://blogs.cisco.com/security/cisco-hypershield-reimagining-security)，这是一个用于安全执行和监控的框架。Gregg 补充说，“[谷歌](https://www.youtube.com/watch?v=N4YKcMV8iaY) 和 [Meta](https://lpc.events/event/17/contributions/1602/) 已经依赖 eBPF 来检测和阻止其舰队中的恶意行为者。” 因此，显然，eBPF 不仅仅是一个有吸引力的深度技术平台。它已经在 [主要科技公司](https://thenewstack.io/tech-works-how-can-i-make-myself-more-productive/) 的生产环境中使用。

但是，对于任何需要包含内核驱动程序或内核模块的商业软件的人来说，eBPF 真的能解决问题吗？当然，[eBPF 还没有准备好用于 Windows 的生产环境](https://microsoft.github.io/ebpf-for-windows/)，但 Gregg 似乎确信这不会太久。其他人并不确定 eBPF 是否是这两个操作系统完美的安全平台。

在电子邮件采访中，[Pivotal Technologies](https://pvotal.tech/) 的首席执行官 [Yashin Manraj](https://www.linkedin.com/in/yashinmanraj/)（一家 [低运维](https://cloudogu.com/en/glossary/lowops/) 开发公司）告诉我，“Gregg 对 eBPF 消除内核崩溃的潜力持乐观态度，虽然令人信服，但需要仔细考虑。虽然 eBPF 为在内核中运行代码提供了更安全的沙箱，但它不是灵丹妙药。”

Manraj 列出了他的担忧：

- 随着 BPF 程序变得越来越复杂，出现不可预见错误的可能性也随之增加。仔细测试和彻底的代码审查对于减轻这种风险至关重要，不会导致
[系统崩溃，而是特定服务](https://thenewstack.io/linux-skills-manage-system-services/) 停止运行，而系统其余部分保持正常运行。 - 由于 eBPF 程序直接与内核交互，即使是微小的错误也会产生连锁反应，可能
[导致服务](https://thenewstack.io/30-of-engineer-leads-use-a-spreadsheet-as-a-service-catalog/) 不稳定。 - 与任何软件一样，eBPF 程序也可能容易受到攻击。开发人员必须优先考虑安全问题，包括输入验证、内存管理和访问控制。
- 调试 eBPF 程序可能很困难。强大的
[日志记录和跟踪](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/) 机制对于识别和解决问题至关重要。
Manraj 总结道：“最终，eBPF 在防止内核崩溃和服务不可用方面的成功，不仅取决于技术本身，还取决于开发人员和安全专业人员对采用稳健的编码实践和在整个开发生命周期中优先考虑安全的承诺。”

我们还没有达到那个阶段。

深入研究，云运行时安全初创公司 [Sweet Security](https://www.sweet.security/) 的 CTO [Tomer Filiba](https://il.linkedin.com/in/tomerfiliba) 在电子邮件采访中警告说，eBPF 存在自身的安全问题。首先，eBPF 需要高权限（CAP_SYS_ADMIN 或“root”），而拥有这些权限的程序也可以删除重要的 [操作系统文件或弄乱服务器的](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/) 配置。” 这些故障可能是由于错误而不是恶意意图造成的，但它们仍然是一个真正的担忧。

其次，Filiba 继续说，由于 eBPF 可以写入用户空间内存，它可以弄乱“正常程序”。确实，这不会“像驱动程序那样导致内核崩溃，但它会导致程序崩溃。” 当然，这比手动重新启动 [Windows 系统进入“安全模式”并修复问题](https://thenewstack.io/rust-1-77-1-a-patch-release-to-fix-an-issue-with-windows/) 要好，但它仍然会弄乱您的生产工作负载。

尽管如此，“底线是，任何高权限程序都可能对您的环境造成损害，但在风险降低方面，eBPF 远远优越。例如，如果您的 eBPF 代理出现故障，[系统可能仍然可以正常运行](https://thenewstack.io/shell-less-kubernetes-talos-systems-introduces-the-common-operating-system-interface/) 足以让您删除/升级代理。

eBPF 是您未来安全问题的答案吗？好吧，它可能不是答案，尤其是在 Windows 中。尽管如此，在对 eBPF 的乐观和悲观之间，很明显，基于 eBPF 的安全系统将成为低级安全防御和监控平台的重要组成部分。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)