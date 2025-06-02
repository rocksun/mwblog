# Linux Kernel 6.15 Boosts Virtualization, GPU, and CPU Performance
![Featued image for: Linux Kernel 6.15 Boosts Virtualization, GPU, and CPU Performance](https://cdn.thenewstack.io/media/2025/05/88c31c76-getty-images-qcp7xpdq3q8-unsplash-1024x768.jpg)
A new kernel graces the [Linux community](https://thenewstack.io/learning-linux-start-here/)! Linux kernel 6.15 is now available, and it delivers the usual plethora of drivers, performance updates, and security mitigations. Sysadmins managing Linux servers with large quantities of RAM, lots of virtual machines, or are concerned about Spectre v2 vulnerabilities will be particularly happy with this release.

Use the details in this article to determine whether you need to update your systems upon kernel 6.15’s release. Start by ensuring you’re familiar with the Linux release candidate system.

### What Are Linux Kernel Release Candidates (RC)?
Linux relies on a rolling schedule of kernel updates preceded by several release candidates (RCs). The release candidates enable contributors to finalize code updates and handle final testing. The team adds no new features during this phase. Those are all decided on with the final pull of the kernel before the first RC.

There are typically seven or eight release candidates, depending on the testing results. The process often lasts two months. The kernel 6.15rc1 release occurred in early April.

## Kernel 6.15 Primary Attributes
Perhaps the best word to describe the new Linux 6.15 kernel is “enhancements.” Enhancements abound, covering CPU, GPU, storage, network, and various general improvements. And, of course, security mitigations are a significant part of the new kernel.

Review the following enhancement categories to learn more about how Linux kernel 6.15 improves the overall functionality and capability of Linux systems.

### General Enhancements
The 6.15 kernel includes various general improvements. A few are:

- Rust programming for Linux kernel code continues to grow.
- Kernel scheduler (
[continued from kernel 6.12](https://thenewstack.io/linux-kernel-6-12-is-official-real-time-app-support-better-scheduling/)) improvements. - Apple Z2 touchscreen and Touch Bar drivers for increased Apple hardware support.
- Apple keyboard backlight driver.
- Xpad game controller driver improvements for Xbox controllers
- Samsung Galaxy Book laptop and 2-in-1 devices driver support.
- Huwei Matebook E Go EC 2-in-1 devices driver support.
### Virtualization Enhancements
Microsoft provided additional improvements for hosting Linux VMs on Hyper-V, including:

- Microsoft Hyper-V support for running as the root partition.
- Microsoft Hyper-V support for offlining CPU cores for Linux VMs.
Another useful improvement is the continued development of [Kernel-based Virtual Machine](https://thenewstack.io/how-to-develop-on-a-linux-desktop-with-an-easy-to-use-vm/) (KVM) features. Kernel 6.15 updates aren’t profound, but they include:

KVM on Intel:

- Shadow Page Table Entries (SPTEs) aging without holding the MMU lock support, enabling scalability and stability.
- Nested emulation improvements with support for VGICv3 on the ARM architecture.
- Interrupt handling enhancements improve reliability throughout the VM lifecycle, especially with teardown processes.
KVM also receives general performance and stability improvements on AMD processors.

### CPU Enhancements
The new kernel continues to take advantage of CPU innovations for increased efficiency, capability, and security. CPU enhancements include:

- Boot parameter setcpuid= for x86 architectures for improved virtualization.
- AMD Zen 6 CPU core identification, adding kernel recognition for next-generation EPYC and Ryzen processors.
- ARMv9 support improvements
- RISC-V instruction set updates.
- Turbostat CPU monitoring capabilities increased from 1024 cores to 8192 cores to support more powerful systems.
- LoongArch support improves stability and reliability for this architecture, growing on work done with
[kernel 6.12](https://thenewstack.io/linux-kernel-6-13-stands-ready-with-security-performance-driver-updates/).
### Memory Enhancements
Memory management receives attention in kernel 6.15. Specifically, you can now control the parallelization of huge page initialization, leading to major improvements in boot times for systems that allocate large numbers of huge pages. The pages themselves help improve performance for memory-intensive workloads. The option optimizes their allocation during boot time.

Add the hugetlb_alloc_threads= boot parameter to your kernel command line to enable this capability. For example, add a value of 4 to allocate four threads. You should notice the biggest difference around scaling VMs, servers with a lot of memory, or servers relying on huge pages.

### GPU Enhancements
New enhancements to the kernel continue with the growing criticality of GPUs in modern processing. Various current and future enhancements find their way into the latest kernel, including:

- NOVA open source driver for
[NVIDIA GPUs](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/)using NVIDIA’s GSP firmware early-stage support. - Intel Xe open source driver support, adding or improving power management and Shared Virtual Memory. It also integrates Direct Rendering Manager (DRM) enhancements to retain compatibility with Linux graphics stacks.
- AMD RX 9070-series fan speed reporting improvements. (Note that kernel 6.13.5 or newer is required for the full feature set supporting these devices.)
- Broadcom BCM74110 thermal driver added for improved temperature control.
Hung GPUs receive some direct attention in the new kernel with the introduction of a standardized user-space reporting mechanism. This feature improves support for applications and desktop environments to alert users and respond to GPU hangs, regardless of hardware and drivers.

### Storage and Filesystem Enhancements
Increasing [storage capabilities](https://thenewstack.io/storage/) is always a topic near and dear to a sysadmin’s heart. Storage enhancements are relatively minor in this kernel but still provide helpful functionality, targeting Btrfs, XFS, NTFS3, and others. Improvements include:

- Filename length limits increase under FUSE from 1024 to 4095, significantly higher than other filesystems (ext4 and XFS limit names to 255 bytes).
- ext4 hardening against fuzzed (intentionally corrupted) filesystem issues via input validation and error handling.
- Copy-on-write support for ext4 was added to increase performance.
- Block sizes can now be greater than page sizes, enabling more flexible filesystem configurations.
- Zstd data compression fast/real-time improvements on Btrfs filesystems.
- Large atomic writes components that will eventually support this feature under ext4 and XFS, improving reliability and performance.
### Network Enhancements
All Linux kernel releases consist of massive numbers of driver updates. Various network device drivers grace the 6.15 kernel, including:

- IPv6 improvements in the network stack to support address generation and packet handling.
### Security Mitigations
The new kernel addresses concerns regarding Spectre v2 variants and related system vulnerabilities. While domain isolation was initially thought to mitigate Spectre v2 problems, some variants circumvent the mitigation, raising additional security problems. The Training Solo class of variants can exploit the branch predictor within a domain to expose data.

Linux kernel 6.15 contains patches designed to address the Training Solo security vulnerability on AMD and Intel processors.

## Wrap Up
From performance enhancements to security mitigations to integrated features, the latest Linux kernel continues pushing the operating system forward. This kernel will likely interest those concerned with Spectre v2 vulnerabilities, running systems with large quantities of RAM, or needing the latest device drivers.

As always, you can wait for your favorite distribution to integrate the new kernel into its update mechanism. If you’re itching to start working with some of these features earlier or want the security/performance benefits included in kernel 6.15, download it from [The Linux Kernel Archives](https://www.kernel.org/) or Linus Torvalds’ [Linux Git tree](https://web.git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)