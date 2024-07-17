# What’s New With the Just-Released Linux 6.10 Kernel
![Featued image for: What’s New With the Just-Released Linux 6.10 Kernel](https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux-1024x682.jpg)
The latest Linux kernel, 6.10, is out.

[Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/) wasn’t happy about how the last days running up [the Linux 6.10 release](https://lkml.org/lkml/2024/7/14/250) went. In the end, though, “it also wasn’t noisy enough to warrant an extra rc [release candidate].” So, here we are with the latest Linux kernel ready for work.
This mid-year 2024 kernel upgrade brings a host of exciting features and improvements that enhance performance, security, and hardware support across various platforms.

One of the standout additions in Linux 6.10 is the new [Panthor graphics Direct Rendering Manager (DRM) driver](https://www.collabora.com/news-and-blog/news-and-events/release-the-panthor.html). This delayed code should have arrived in the 6.9 Linux kernel and supports the newer Arm Mali graphics processors. This development is particularly significant for the next generation of devices built around [Arm-based architectures](https://thenewstack.io/arm-eyes-ai-with-its-latest-neoverse-cores-and-subsystems/). It will improve their graphics performance and compatibility.

The kernel also includes several graphics enhancements for Intel users. Top of the list is more preparations for Intel’s forthcoming [Xe2 graphics](https://www.anandtech.com/show/21425/intel-lunar-lake-architecture-deep-dive-lion-cove-xe2-and-npu4/6).

This release also has a significant performance fix for Intel Core hybrid systems with buggy firmware. How significant? Very. On systems with an Intel Core i5 13500H processor and using the earliest eligible virtual deadline first (EEVDF) scheduler, users had to endure as much as a [50% performance hit.](https://www.phoronix.com/news/Linux-6.10-rc6-PM-Intel-Core)

[AMD ](https://www.amd.com/en/products/processors/server/epyc/google-cloud.html?utm_content=inline+mention)has been included, with better ROCm/AMDKFD support for smaller Ryzen APUs and new additions for the upcoming Zen 5 architecture.
At a higher level, the 6.10 release also supports the Intel Arrow Lake-H processors, Lenovo Thinkbook 13x Gen 4, Lenovo Thinkbook 16P Gen 5, and Lenovo Thinkbook 13X laptops, as well as ASUS ROG 2024 laptops. The computers would all work before with Linux, but their Cirrus CS35L41 audio amplifiers had trouble.

Linux 6.10 also brings notable performance and [security improvements](https://thenewstack.io/design-system-can-update-greg-kroah-hartman-linux-security/). Users can expect faster AES-XTS disk and file encryption on modern Intel and AMD CPUs and enhanced IO_uring zero-copy performance. This latest kernel also introduces [MSEAL](https://lwn.net/Articles/954936/). This protects a given virtual memory range against modifications, such as changes to their permission bits. It also implements Trusted Platform Module (TPM) bus encryption and integrity protection.

Hardware support has been expanded, with the kernel now supporting various new devices. These include the ASUS ROG Raikiri Pro controller, 2024 LG laptop models, and improved compatibility with ASUS ROG 2024 laptops.

Linux 6.10 offers several new features for developers and system administrators. Rust fans will be most excited about [Rust language support ](https://thenewstack.io/rust-in-the-linux-kernel/)for the RISC-V architecture. Rust support in the kernel has also been updated to the language’s latest release: [Rust 1.78.0](https://blog.rust-lang.org/2024/05/02/Rust-1.78.0.html).

The release of Linux 6.10 marks another milestone in the continuous evolution of the Linux kernel. As the community begins to adopt this new version, attention now turns to the development of Linux 6.11, and its merge window is already open. A Linux kernel developer’s work is never done!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)