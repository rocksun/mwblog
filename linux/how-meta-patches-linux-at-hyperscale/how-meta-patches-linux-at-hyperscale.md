<!--
title:  Meta大规模Linux补丁解决方案
cover: https://cdn.thenewstack.io/media/2023/11/1b8e869d-casey-allen-ujpeghu8unu-unsplash-1024x683.jpg
-->

对Linux系统进行补丁升级，看似简单，但当需要面对成千上万台服务器时，在不停机的情况下完成补丁就变得极具挑战。本文将详细介绍Meta公司是如何解决此类大规模Linux补丁部署的技术难题。

> 译自 [How Meta Patches Linux at Hyperscale](https://thenewstack.io/how-meta-patches-linux-at-hyperscale/)，作者 Steven J. Vaughan-Nichols。

任何具有技术头脑的人都可以修补 Linux 服务器。但是，在不停机的情况下修补成千上万台服务器，这可不容易。

在本月早些时候举行的 Linux 内核顶级开发者仅凭邀请的 [Linux Plumbers 会议](https://lpc.events/)上，[Meta](https://thenewstack.io/meta-adds-cool-new-features-to-python-3-12/) Linux 内核工程师 [Breno Leitao](https://github.com/leitao) 解释了 Facebook 如何在世界各地的数百万台服务器上完成此操作。

如果使用普通技术，Leitao 说将需要超过 45 天的时间才能将新的内核推送到所有机器上。正如他所说，“排空和反排空主机很困难。” 你可以再说一遍。

如果这只是一个小更新，那可能还可以接受，但如果是安全补丁，那就行不通了。

因此，Meta 使用[内核实时补丁(KLP)](https://documentation.suse.com/smart/deploy-upgrade/html/concept-klp/index.html)和 [Red Hat](https://www.openshift.com/try?utm_content=inline-mention) 的 [Kpatch](https://www.redhat.com/en/blog/introducing-kpatch-dynamic-kernel-patching) 来提供快速补丁。在 KLP 中，您可以将最新的安全更新应用于 Linux 内核，而无需重新启动。这可以最大限度地提高系统正常运行时间和可用性。

## 实时内核补丁

内核实时补丁以包含修改代码的包的形式提供，与主内核包分开。实时补丁是累积的，因此最新补丁包含针对内核包的所有前一个补丁的所有修复。每个内核实时包都与其发布的确切内核修订版本绑定。

但是，实时补丁并不能解决所有问题。您无法修补数据或结构。另一个问题是实时补丁通常需要额外的工程工作。正如 Leitao 警告的那样：“这不仅仅是编译实时补丁这么简单，并且知道它是安全的并应用它。这些是内核模块，如果不小心的话，您会中断事物。不能保证补丁本身就是正确的。”

Kpatch 通过比较原始内核和修补内核，然后使用定制的内核模块将新代码修补到正在运行的内核中。然后 Kpatch 进程使用 [ftrace](http://elinux.org/Ftrace) 观察现有进程的堆栈，看是否可以在不产生任何有害影响的情况下进行修补。

当安全时，它会将正在运行的代码重定向到修补的函数，然后删除现在已过时的代码。就这样，你的服务器被修补了，没有任何宕机时间。

当然，在实践中这并非那么简单。 Leitao 解释说：“在 Meta，当我们应用实时补丁时，通常需要一到两秒钟的时间将补丁应用于主机。这显然不是针对类似整个服务器群，而是对主机一到两秒钟真的非常快，相比 [kexec](https://wiki.archlinux.org/title/kexec)(Linux 内核机制用于启动新内核)。它不需要任何宕机时间或工作负载迁移，您只需应用实时补丁，然后继续前进。”

## 如何修补数百万台机器

但是，当谈论成百万台机器时，这还不是全部。Meta 将在修补程序推出期间发现错误，因此管理员首先会修补候选版本层。因此，随着基于 [RPM](https://rpm.org/) 的修补程序的交付，也会自动检查服务器的运行状况。

Meta 查看新内核中的崩溃、主要警报和应用问题及性能。这些数据来自各种源，包括崩溃、[netconsole](https://www.kernel.org/doc/Documentation/networking/netconsole.txt) 结果和核心转储。如果错误率超过每千台服务器一次崩溃，则会拉回补丁并恢复旧内核。

随着超过 10 亿用户，Facebook 也会密切关注性能。正如 Leitao 所说：“实时补丁的性能开销很小，但当相对热的函数被修补时，总是会引起关注。”

尽管 Meta 使用 Kpatch，但也有其他选择。SUSE 提供 [kGraft](https://documentation.suse.com/sles/12-SP4/single-html/SLES-kgraft/)；而 [Oracle](https://developer.oracle.com/?utm_content=inline-mention) 使用 [Ksplice](https://ksplice.oracle.com/)；Canonical 支持 [Livepatch](https://ubuntu.com/security/livepatch/docs/livepatch)。不管代码如何，它们都能提供类似的结果。

因此，如果你不希望服务器、数据中心和云出现宕机时间，请按照 Meta 的例子使用实时补丁。你会很高兴你这样做的。