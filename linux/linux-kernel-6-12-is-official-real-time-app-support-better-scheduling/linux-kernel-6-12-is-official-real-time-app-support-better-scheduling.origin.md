# Linux Kernel 6.12 Is Official! Real Time App Support, Better Scheduling
![Featued image for: Linux Kernel 6.12 Is Official! Real Time App Support, Better Scheduling](https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux-1024x682.jpg)
The [latest Linux kernel](https://www.kernel.org/) available as of Nov. 17, 2024, is kernel 6.12. It contains several important features for certain segments of the Linux community. The 6.12 release candidate 1 became available on Sept. 29, 2024, and enjoyed a relatively quiet test period consisting of seven release candidate iterations. I discussed kernel 6.12rc1 [here](https://thenewstack.io/linux-kernel-6-12-prepped-for-superior-scheduling-real-time-ops/).

Now that kernel 6.12 is complete, it’s time for you to decide whether to implement it immediately. This article reviews the most relevant features and offers ways to upgrade your Linux devices.

![](https://cdn.thenewstack.io/media/2024/11/9435442a-button.png)
## Key Features of Kernel 6.12
The two key features to focus on for kernel 6.12 are real-time application support and kernel scheduling. There are plenty more new or updated components, but these two represent the best of the offerings.

**Real-time Computing**: Supports time-sensitive applications by enforcing time constraints on the system. The feature has been in the works for a long time.**Kernel scheduling**: Improved task scheduling for increased efficiency.
Other new or updated capabilities include the following:

- Drivers (55% of the updates).
- Documentation.
- ‘perf’ performance monitoring tool improvements.
- Core kernel development around architecture, filesystem management, and networking.
- Improved support for Rust for kernel development.
Determine whether these features will benefit your organization to [decide](https://thenewstack.io/learning-linux-start-here/) if you need to implement the new kernel immediately.

## Install the New Kernel
Most organizations are content to wait for updates to the primary distribution repositories before installing the new kernel and its corresponding features. Your standard patch testing and scheduling apply here.

However, Ubuntu-based distributions can update the kernel immediately using the [Mainline](https://github.com/bkw777/mainline) application. Begin by installing Mainline, and then browse the available kernels. Mainline also helps you remove older kernels. It’s mainly designed for Ubuntu and its related distributions but will typically work with any [Debian-based distro](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/).

Enterprise customers using [Red Hat Enterprise Linux](https://thenewstack.io/red-hat-enterprise-linux-9-5-arrives-with-enhanced-ai-support-and-automation/) and its related distributions will typically wait for Red Hat to finish testing before deploying the new kernel through the standard update and package manager approaches.

SUSE Linux users can add the
Kernel:HEAD repository to their package manager for the latest kernel offerings or wait for [SUSE](https://thenewstack.io/linux-and-cloud-native-security-suses-strategy/) to test and make the new kernel available through the standard repository.

Check your favorite distribution for instructions on installing kernel 6.12.

Use the uname -r or uname -a commands to display your system’s current kernel version. This information should help you determine whether a kernel update is worthwhile.

![](https://cdn.thenewstack.io/media/2024/11/beef35d6-uname.png)
## Wrap Up
Kernel updates provide additional stability, features, security options, and more, so keeping your system current is typically a good idea. In some cases, that means not waiting for the distribution vendor to test and integrate the new kernel, so you can always add the kernel manually. That’s probably the case for most Linux users when it comes to kernel 6.12. Teams working with real-time applications will benefit the most from this new kernel version.

Keep an eye out for news on kernel 6.13, coming in 2025. This release could include processing improvements for AMD EPYC and Intel Panther Lake CPUs, increased support for pre-M1 Apple devices, removal of ReiserFS, additional drivers, and more.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)