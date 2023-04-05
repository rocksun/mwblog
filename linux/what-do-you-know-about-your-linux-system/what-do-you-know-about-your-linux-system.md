# 您对 Linux 系统了解多少？

翻译自 [What Do You Know about Your Linux System?](https://thenewstack.io/what-do-you-know-about-your-linux-system/)

了解获取支持的系统调用和功能以及评估系统安全性和运行时活动的过程。

![](https://cdn.thenewstack.io/media/2023/03/52342a7b-manhattan-3-1024x682.jpg)

你知道 Linux 内核支持的系统调用和功能是与架构相关的吗？你知道 Linux 内核支持多种加固配置选项来保护你的系统吗？

让我们来看看这个过程，以深入了解受支持的系统调用和功能，并评估系统的安全性及其运行时活动。

## 系统状态可视化

内核系统状态可以被视为静态和动态特征以及模块的组合。让我们首先定义什么是静态和运行时系统状态，然后探索如何可视化内核的静态和运行时系统部分。

静态系统视图包括在内核配置中启用的系统调用、特性、静态和动态模块。

运行时系统视图包括在运行时使用的系统调用、`ioctl` 调用和子系统。工作负载可以加载和卸载模块，并通过调整系统参数来更改运行时系统配置以适应其需求。

需要记住的几个关键点：

* 支持的系统调用和 Linux 内核功能是与架构相关的。不同架构上的系统调用编号是不同的。
* auditd 、 checksyscalls.sh 和 get_feat.pl 工具可用于发现支持的系统调用和功能。
* 了解 Linux 内核强化配置选项并确保它们已启用将使系统更安全。
* 采用运行时跟踪可以揭示运行时系统状态。
* 工作负载可能通过加载和卸载动态模块以及调整系统参数来改变系统状态。

## 我们如何检查支持的系统调用？

我们有工具可以检查支持的系统调用和功能。我们可以使用 auditd 工具获取支持的系统调用信息。

来自 auditd 工具系列的 ausyscall –dump 命令会打印出系统上支持的系统调用，并允许映射 syscall 名称和编号。您可以在基于 Debian 的系统上安装 auditd 包：


```
sudo apt-get install auditd
```

Linux 内核工具 `scripts/checksyscalls.sh` 可以用于检查当前架构是否与 i386 相比缺少任何系统调用。

Linux 内核工具 `scripts/get_feat.pl` 可用于列出架构的内核特性支持矩阵。

## 查找支持的系统调用

如前所述，ausyscall 在系统上打印出支持的系统调用，并允许映射 syscall 名称和编号。

```
ausyscall --dump # 打印所有支持的系统调用
```

ausyscall 允许过滤特定的系统调用或关键字符串。当我们使用“open”和“time”选项调用 ausyscall 时，看看它会显示什么：

```yaml
ausyscall open
open 2
mq_open 240
openat 257
     perf_event_open 298
     open_by_handle_at 304
     open_tree 428
     fsopen 430
     pidfd_open 434
     openat2 437
 
ausyscall time
getitimer 36
     setitimer 38
     gettimeofday 96
   times 100
     rt_sigtimedwait 128
     utime 132
     adjtimex 159
     settimeofday 164
     time 201
     semtimedop 220
     timer_create 222
     timer_settime 223
     timer_gettime 224
     timer_getoverrun 225
     timer_delete 226
     clock_settime 227
    	clock_gettime 228
     utimes 235
     mq_timedsend 242
     mq_timedreceive 243
     futimesat 261
   utimensat 280
     timerfd_create 283
     timerfd_settime 286
     timerfd_gettime 287
     clock_adjtime 305
```     

## 查找不支持的系统调用

了解哪些系统调用不受支持也很重要。如前所述，`scripts/checksyscalls.sh` 检查当前架构与 i386 的相比所缺失的系统调用。

```
checksyscalls.sh gcc
             warning: #warning syscall mmap2 not implemented [-Wcpp]
             warning: #warning syscall truncate64 not implemented [-Wcpp]
             warning: #warning syscall ftruncate64 not implemented [-Wcpp]
             warning: #warning syscall fcntl64 not implemented [-Wcpp]
             warning: #warning syscall sendfile64 not implemented [-Wcpp]
             warning: #warning syscall statfs64 not implemented [-Wcpp]
             warning: #warning syscall statfs64 not implemented [-Wcpp]
             warning: #warning syscall fadvise64_64 not implemented [-Wcpp]
```

现在让我们用 ausyscall 进行检查。

```
ausyscall map
      mmap          9
      munmap 11
      mremap 25
      remap_file_pages 216
 
ausyscall trunc
      truncate 76
      ftruncate 77
```

如您所见， `ausyscall` 显示 mmap2、ftruncate64 和 ftruncate64 未在此系统上实现。这与 `checksyscalls.sh` 显示的相符。

## 查找支持的功能

让我们看看如何在系统上找到支持的功能。可以使用 `scripts/get_feat.pl` 列出架构的内核特性支持矩阵。

```
get_feat.pl list
get_feat.pl list –arch=arm64 lists
```

该脚本解析 Documentation/features 以查找支持状态信息。它可用于验证 Documentation/features 下文件的内容，或仅列出它们：

```
--arch option outputs features for an specific architecture, optionally filtering 
           for a single specific feature.
  --feat or --feature option outputs features for a single specific feature.
```

以下是查找是否支持堆栈保护器和任务中线程信息功能的方法：


```
scripts/get_feat.pl --arch=arm64 --feat=stackprotector list
        #
        # Kernel feature support matrix of the 'arm64' architecture:
        #
        debug/ stack protector       :  ok  |            HAVE_STACKPROTECTOR #
        arch supports compiler driven stack overflow protection
 
scripts/get_feat.pl --feat=thread-info-in-task list
        #
        # Kernel feature support matrix of the 'x86' architecture:
        #
        core/ thread-info-in-task  :  ok  |           THREAD_INFO_IN_TASK #
        arch makes use of the core kernel facility to embed thread_info in
        task_struct
```

## 查找内核模块状态

`lsmod` 命令显示当前加载的内核模块。该程序显示 `/proc/modules` 的内容。让我们选择大多数笔记本电脑上都有的 `uvcvideo` 模块：

```
lsmod | grep uvc
uvcvideo              126976  0
videobuf2_vmalloc      20480  1 uvcvideo
uvc                    16384  1 uvcvideo
videobuf2_v4l2         36864  1 uvcvideo
videodev              315392  2 videobuf2_v4l2,uvcvideo
videobuf2_common       65536  4 
                                      Videobuf2_vmalloc,videobuf2_v4l2,uvcvideo,videobuf2_memops
mc                     77824  4 videodev,videobuf2_v4l2,uvcvideo,videobuf2_common
```

可以看到 lsmod 显示了 uvcvideo 和它依赖的模块，以及有多少模块在使用它们。 videobuf2_common 被其他四个模块使用。也就是说，这是这个模块的引用计数，只要引用计数>0， rmmod 就会拒绝卸载它。

您可以从 /proc/modules 获得相同的信息：

```
 grep uvc  /proc/modules
  uvcvideo 126976 0 - Live 0x0000000000000000
  videobuf2_vmalloc 20480 1 uvcvideo, Live 0x0000000000000000
  uvc 16384 1 uvcvideo, Live 0x0000000000000000
  videobuf2_v4l2 36864 1 uvcvideo, Live 0x0000000000000000
  videodev 315392 2 uvcvideo,videobuf2_v4l2, Live 0x0000000000000000
  videobuf2_common 65536 4 uvcvideo,videobuf2_vmalloc,videobuf2_memops,videobuf2_v4l2, Live 0x0000000000000000
  mc 77824 4 uvcvideo,videobuf2_v4l2,videodev,videobuf2_common, Live 0x0000000000000000
```

该信息与一些额外的字段相似。该地址是内核虚拟内存空间中模块的基址。当以普通用户身份运行时，地址全为零。以 root 身份运行时，相同的命令将如下所示：

```
sudo grep uvc  /proc/modules
  uvcvideo 126976 0 - Live 0xffffffffc1c8b000
  videobuf2_vmalloc 20480 1 uvcvideo, Live 0xffffffffc167f000
  uvc 16384 1 uvcvideo, Live 0xffffffffc0ab0000
  videobuf2_v4l2 36864 1 uvcvideo, Live 0xffffffffc0a28000
  videodev 315392 2 uvcvideo,videobuf2_v4l2, Live 0xffffffffc16e9000
  videobuf2_common 65536 4 uvcvideo,videobuf2_vmalloc,videobuf2_memops,videobuf2_v4l2, Live 0xffffffffc094d000
  mc 77824 4 uvcvideo,videobuf2_v4l2,videodev,videobuf2_common, Live 0xffffffffc15eb000
```

现在让我们看看 `modinfo` 向我们展示了什么：

```
  /sbin/modinfo uvcvideo
  filename:       /lib/modules/6.3.0-rc2/kernel/drivers/media/usb/uvc/uvcvideo.ko
  license:        GPL
  description:    USB Video Class driver
  depends:        videobuf2-v4l2,videodev,mc,uvc,videobuf2-common,videobuf2-vmalloc
  retpoline:      Y
  intree:         Y
  name:           uvcvideo
  vermagic:       6.3.0-rc2 SMP preempt mod_unload modversions
  sig_id:         PKCS#7
  signer:         Build time autogenerated kernel key
```

这告诉我们这个模块是在内核存储库中构建的，内核存储库使用构建时自动生成的密钥签名。

让我们对系统进行最后一次健全性检查，看看以下两个命令输出是否匹配：

```
  ps ax | wc -l
  ls -d /proc/* | grep [0-9]|wc -l
```

如果它们不匹配，请仔细检查您的系统。内核 rootkit 安装它们自己的 `ps` 、 `find` 等实用程序来掩盖它们的活动。在我的系统输出匹配。在你哪儿也匹配吗？

## 我的系统是否尽可能安全？

Linux 内核支持多种强化选项以确保系统安全。让我们谈谈可以检查内核配置安全性的 `kconfig-hardened-check` 工具健全性。您可以克隆最新的 `kconfig-hardened-check` 仓库：

```
git clone https://github.com/a13xp0p0v/kconfig-hardened-check.git
cd kconfig-hardened-check
bin/kconfig-hardened-check --config <config file> --cmdline /proc/cmdline
```

这将生成内核安全配置和命令行选项的详细报告，这些选项已启用（OK）和未启用（FAIL），最后是摘要行：

```
[+] Config check is finished: 'OK' - 100 / 'FAIL' - 100
```

您将必须分析信息以确定在您的系统上启用哪些选项是有意义的。

## 了解系统运行时活动

到目前为止，我们已经找到了找到系统静态的方法。现在让我们切换到系统的运行时状态。 Linux 内核事件跟踪功能可以帮助我们了解运行时状态。

启用事件跟踪可以深入了解系统运行时活动。这是一种很好的方式，可以在系统处于某个工作负载/进程正在运行时，识别哪些内核部分被更高级别地使用。

事件跟踪依赖于启用 CONFIG_EVENT_TRACING 选项。您可以在开始工作负载/进程之前启用事件跟踪。事件跟踪允许您在运行时对支持/可用的事件进行启用和禁用追踪。

您可以在以下文件中找到可用的事件、跟踪器和过滤器函数：

```
 /sys/kernel/debug/tracing/available_events
 /sys/kernel/debug/tracing/available_filter_functions
 /sys/kernel/debug/tracing/available_tracers
```

现在这是启用跟踪的方法：

```
sudo echo 1 > /sys/kernel/debug/tracing/events/enable
```

一旦工作负载/进程停止或当您确定您拥有所需的状态时，您可以禁用事件跟踪：

```
sudo echo 0 > /sys/kernel/debug/tracing/events/enable
```

您可以在文件中找到跟踪信息：/sys/kernel/debug/tracing

以下是此文件中显示的信息：

```
 cat trace
 # tracer: nop
 #
 # entries-in-buffer/entries-written: 0/0   #P:16
 #
 #                                _-----=> irqs-off/BH-disabled
 #                               / _----=> need-resched
 #                              | / _---=> hardirq/softirq
 #                              || / _--=> preempt-depth
 #                              ||| / _-=> migrate-disable
 #                              |||| /     delay
 #           TASK-PID     CPU#  |||||  TIMESTAMP  FUNCTION
 #              | |         |   |||||     |         |
```

## 我们如何使用这些跟踪？

您可以将函数映射到系统调用和其他内核功能，以深入了解工作负载/进程运行时的整体系统活动。

## 结论

如您所见，我们有多种工具和功能可供使用，以深入了解系统活动并评估其安全性。