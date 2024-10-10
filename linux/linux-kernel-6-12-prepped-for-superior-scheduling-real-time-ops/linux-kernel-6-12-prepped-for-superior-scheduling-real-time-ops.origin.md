# Linux Kernel 6.12 Prepped for Superior Scheduling, Real Time Ops
![Featued image for: Linux Kernel 6.12 Prepped for Superior Scheduling, Real Time Ops](https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux-1024x682.jpg)
The [Linux community](https://thenewstack.io/learning-linux-start-here/) is preparing to release version 6.12 0f the Linux kernel. The 6.12 version is currently in the “release candidate” phase, with 6.12rc1 available as of Sept. 29, 2024. While this kernel release may not include broad steps forward, it does include some interesting and useful features that demonstrate the forward motion of this fascinating OS kernel.

The Linux 6.x kernel brought support for real-time capabilities and kernel scheduling, differentiating it from the previous 4.x and 5.x implementations.

- Kernel 4.x (2015) added power management and performance enhancements, support for ARM processors, and security features.
- Kernel 5.x (2019) added improved CPU scheduling, additional modern hardware supports, and more power/efficiency capabilities.
- Kernel 6.x (2022) added Rust support, significant CPU support for newer Intel processors, plus Apple M1 and AMD processors.
The three latest kernel versions show a continuing path of keeping up with hardware innovations, adding security, increasing efficiency and power management, and kernel performance and scheduling.

What about the “rc1” status? Release candidates accept no additional features and implement only necessary fixes. Release candidates have already undergone testing, placing them in a pre-release status as the final bugs and changes are put into place.

Most of the kernel 6.12rc1 capabilities center on driver updates (about 55%). It includes two significant enhancements and incremental changes to existing functionality. Those may not sound exciting, but they actually represent real and practical forward progress.

## Two New Features To Be Excited About
The official announcement of kernel 6.12rc1 by [Linus Torvalds](https://thenewstack.io/linus-torvalds-c-vs-rust-debate-has-religious-undertones/) highlights two primary features for this release. The first is an improvement to real-time application support, and the second is better kernel scheduling.

### Support for Real-time Computing with PREEMPT_RT
Real-time capabilities enforce time constraints on the system between an event and its response. This feature is critical to supporting time-sensitive applications and represents a significant step forward for the kernel. This is arguably the more critical piece of the new release. It has been hindered by a kernel logging component — a challenge that is now resolved. While real-time computing features have been available for Ubuntu and other releases, this is the first time the capability has been included in the mainline kernel.

### New Kernel Scheduling With sched_ext
Continuing with the performance and efficiency trends throughout kernels 4.x, 5.x, and 6.x, the new *sched_ext* scheduler enables schedule loading using [eBPF programs](https://thenewstack.io/ebpf-reliable-policy-setting-and-enforcement/). These programs run in sandboxed environments, extending kernel capabilities without changing the original code.

## Even More Features
Device driver updates for various features, including USB and Thunderbolt, make up most of this release (about 55%). However, there are other significant improvements across a wide range of components.

### More Rust
Linux began supporting the use of [Rust for kernel development](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/) with the 6.1 version. The 6.12rc1 release enhances that. Rust and C are the two kernel development languages, though Rust support is certainly limited at this point. Expect to see improved support through the following several kernel versions as the maintainers continue integrating it.

### Kernel Panic QR Codes
The new kernel also offers the optional ability to display a QR code for kernel panic events, providing detailed information that is easily gathered and stored on a smartphone or similar device. This is a great example of a new kernel feature written in Rust. Note that it’s disabled by default.

### Architecture Improvements
RC1 includes improvements around the common architectures. Additional support for x86 and ARM processors is probably of the most interest. The above-mentioned real-time integration adds to overall CPU improvements.

### Processor Support for Raspberry Pi 5 and Snapdragon X1
The new kernel also provides native support for the Broadcom BCM2712-based Raspberry Pi 5. This is foundational support, so expect continued progress with the next kernel versions. There is additional support for Qualcomm’s Snapdragon X1 processor found in various platforms.

## Wrap Up
Linus Torvalds estimates about 55% of the release is dedicated to driver updates, with another 5% for documentation and 10% for tooling. The remaining 25% focuses on the significant changes, such as *PREEMPT_RT*, *sched_ext*, and others listed above. Overall, this release consists of over 11,000 commits from about 1700 different authors.

Expect kernel 6.12 to stay in various release candidate versions through October and November, with a likely full release around the first of December. As always, you can get the latest (and archived) kernel releases from the [kernel.org](https://www.kernel.org/) website.

Do you need to upgrade? That mainly depends on whether you need a specific feature enhancement and if you can tolerate frequent kernel changes over the next couple of months. Most Linux users and administrators should remain on the current stable kernel 6.11.2 version for the time being. However, if you develop time-sensitive applications, need the latest and greatest drivers built-in, or are a [Raspberry Pi 5](https://thenewstack.io/the-new-2gb-raspberry-pi-5-another-option-for-linux-sysadmins/) power user, you might be intrigued enough to integrate the new kernel.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)