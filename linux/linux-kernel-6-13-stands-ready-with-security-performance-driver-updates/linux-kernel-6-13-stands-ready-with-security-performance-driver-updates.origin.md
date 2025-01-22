# Linux Kernel 6.13 Stands Ready With Security, Performance, Driver Updates
![Featued image for: Linux Kernel 6.13 Stands Ready With Security, Performance, Driver Updates](https://cdn.thenewstack.io/media/2025/01/89696443-getty-images-cobtu8xq11c-unsplash-1024x768.jpg)
It’s time for another new [Linux kernel](https://thenewstack.io/learning-linux-start-here/)! It’s been a couple of months since the [release of Linux kernel 6.12](https://thenewstack.io/linux-kernel-6-12-is-official-real-time-app-support-better-scheduling/), but the wait for the new 6.13 kernel is now over. [Linus Torvalds](https://thenewstack.io/linus-torvalds-c-vs-rust-debate-has-religious-undertones/) released the latest version to the Linux community on Jan. 19, 2025.

The new release implements additional features and hardware support to provide more flexibility, security, and performance, especially for sysadmins and developers working with enterprise-grade systems. Changes include updated drivers, virtualization improvements, additional architecture support, and more.

## What Is a Linux Kernel Release Candidate?
Note that new [Linux](https://thenewstack.io/introduction-to-linux-operating-system) kernels go through a series of release candidate (RC) stages before their final release into the wild. These stages give contributors the opportunity to finalize code updates. The RC period is usually about two months, but the time varies by how quickly developers resolve issues.

No new features are added to the kernel during this stage; only fixes are allowed. Linux kernel RC versions are incremented beginning with one. For example, during its RC stages, this new 6.13 kernel began with 6.13rc1 on Dec. 2, 2024.

This article summarizes the key features found in Linux kernel 6.13 so you can decide how quickly to update your systems.

## Updated Security Features
Kernel 6.13 includes support for running Linux virtual machines (VMs) in protected execution environments called realms under the [Arm Confidential Compute Architecture](https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture) (Arm CCA). This platform enables [workload isolation](https://thenewstack.io/confidential-computing-makes-inroads-to-the-cloud/) from (potentially) untrusted execution environments, including the host operating system and virtualization hypervisors. Isolation occurs at the hardware level with restricted address spaces.

This enhancement is a feature of the 2021 Armv9-A release, which supports workstations, phones, tablets, IoT devices, etc. It offers security, AI, and high-performance computing capabilities. Specifically, the Arm CCA introduces isolated security states called “realms.” It is these realms the Linux 6.13 kernel takes advantage of.

The new kernel also adds support for the 64-bit Arm processor shadow stacks security feature that protects user-space applications and improves performance.

Finally, the kernel’s updated lazy preemption model should increase performance by simplifying configuration options. This change applies to x86, RISC-V, and LoongArch architectures.

## Filesystem Updates
Significant improvements to various Linux filesystems add security and stability to file management. Changes include the following:

**XFS**: The addition of atomic write support to protect data in the event of a power outage.**ext4**: The addition of atomic write support to protect data in the event of a power outage, and various code cleanups and fixes.**Btrfs**: Increased performance capabilities.**FUSE**: The addition of configuration updates to increase stability.
The Flash-Friendly File System (F2FS) is optimized for flash storage devices to maintain their longevity and performance. It was introduced into Linux with kernel 3.8. With kernel 6.13, F2FS receives device aliasing to enable users to manage space more efficiently. This is critical for modern solid-state devices (SSDs).

Also, the 6.13 kernel removes the ReiserFS entirely, ending its support within the Linux platform.

## Raspberry Pi Video Improvements
The new kernel hasn’t neglected the [Raspberry Pi platform](https://thenewstack.io/the-new-2gb-raspberry-pi-5-another-option-for-linux-sysadmins/) either, with a new kernel driver for the Broadcom V3D processor that enables 1MB “super pages” and 64KB “big pages.” Expect better graphics performance from this driver, continuing the Raspberry Pi’s relevance and evolution in modern computing.

## Additional Driver Support
The updated kernel includes additional support for specific processors, graphics processors, audio, and networking chips. Tools such as Dell’s WMAX thermal interface add new management functionality to laptops from various vendors.

More and more peripherals benefit from evolving Linux drivers, including Apple’s Magic Trackpad 2 (USB-C edition), gaming mice, and headsets. Each kernel release adds more drivers to Linux’s inventory, enabling it to keep pace with the massive hardware growth that continues to drive peripheral device development.

## What Else?
Additional features cover too many areas to document completely, but new capabilities exist around networking, storage, memory utilization, and various processor architectures. A few of the following updates deserve attention:

**Networking**: Performance improvements and capabilities centered on per-network namespace locks.**LoongArch**: Support for real-time computing and miscellaneous other updates.**SD Ultra Capacity (SDUC)**: Support for future implementations of 128TB of storage on SD cards.**Wireguard****VPN**: Support for Big TCP GSO for network-intensive workloads over the VPN connection.**SELinux**: Improvements increase performance by implementing policies on specific network links.
Another new feature is basic support for iPhone/iPad A7 through A11 chips, enabling potential future development and capabilities for running Linux on older Apple hardware. Another Apple-oriented feature is the ACPI backlit capability on some Mac platforms.

Finally, kernel 6.13 continues [Rust](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/) integration into the kernel development process with in-place modules. This is an ongoing effort that began with kernel 6.12. Expect additional Rust-based development capabilities in the next several kernel releases.

## Wrap Up
While kernel 6.13 isn’t a revolutionary change, it represents the continued growth and maturity of the 6.x kernel family. These steps forward maintain Linux’s domination of cloud services and server platforms. Client devices may not experience the same benefits (with the exception of Raspberry Pi), but the server-side improvements are welcome.

Expect to see the first release candidate for kernel 6.14 on Feb. 2, 2025, with a likely release of the final version by the end of March.

If you cannot wait for your favorite distribution to include this new kernel in its next release, you can download it from [Linus Torvalds’ own Git repository](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/snapshot/linux-6.13.tar.gz) or [kernel.org](https://www.kernel.org/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)