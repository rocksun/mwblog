[Linus Torvalds](https://thenewstack.io/linus-torvalds-reflects-on-20-years-of-git/) wasn’t thrilled with how the final days leading up to the 6.18 release of the Linux kernel went. “[I’d have been happier with slightly less bugfixing noise](https://lkml.org/lkml/2025/11/30/341) in this last week of the release,” the Linux kernel creator wrote Nov. 30 on the Linux kernel mailing list.

Nevertheless, he added, “While there’s a few more fixes than I would hope for, there was nothing that made me feel like this needs more time to cook. So 6.18 is tagged and pushed out.”

Now that version 6.18 is fully cooked, what are the ingredients? And what, exactly, does “long-term support” mean when it comes to the Linux kernel?

|  |  |  |  |
| --- | --- | --- | --- |
| **Kernel version** | **Status in December 2025** | **Planned upstream EOL** | **Notes** |
| 6.18 | New LTS | December 2027 | Designated LTS in early December 2025; sixth active LTS branch. |
| 6.12 | LTS | December 2026 | Also selected as a Civil Infrastructure Platform (CIP); [Super-LTS kernel with up to 10 years of support.](https://www.zdnet.com/article/super-long-term-stable-linux-kernel-arrives/) |
| 6.6 | LTS | December 2026 | Marked LTS in late 2023; widely used as a stable enterprise/desktop base. |
| 6.1 | LTS | December 2027 | Long‑lived branch used by several distros and embedded vendors. |
| 5.15 | LTS | December 2026 | Common in enterprise distributions and long‑term hardware enablement stacks. |
| 5.10 | LTS | December 2026 | Older LTSs, still maintained and widely deployed (e.g., Debian 11, some embedded). |

Once upon a time, long-term support versions of the Linux kernel got six years of long-term support (LTS). That’s no longer the case. In 2023, the [kernel developers cut LTS to two years](https://www.zdnet.com/article/long-term-support-for-linux-kernel-to-be-cut-as-maintenance-remains-under-strain/).

Why? Because Linux code maintainers have been [burning out](https://thenewstack.io/how-to-recognize-recover-from-and-prevent-burnout/). It’s a hard job. And, as [Josef Bacik](https://josefbacik.github.io/), Linux kernel file system developer and maintainer, said in a presentation at the 2022 Linux Storage | Filesystem | MM & BPF Summit, “[Maintainers are burning out [because] maintainers don’t scale](https://www.bilibili.com/video/BV1c14y1b7et/).” Adding insult to injury, they are also [rarely paid for maintenance work](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/).

So it is that we only get two years of “official” LTS — and the clock on the latest release, 6.18, began ticking on Dec. 3, when stable Linux kernel maintainer [Greg Kroah-Hartman](https://www.linkedin.com/in/greg-kroah-hartman) [announced it was officially the newest LTS version](https://git.kernel.org/pub/scm/docs/kernel/website.git/commit/?id=b9ea3472ee1d973f4c27d075c7e4445afa7ade89). This release also sees the LTS Linux 5.4 falling out of support.

## Longer Support for Enterprise Linux Distros

Wait? What’s that you say? You need a heck of a lot longer support time than two years for you and your customers? Well, depending on which distribution you use for production, you’re in luck. Many of the top enterprise Linux distributors offer far longer-term support horizons for their paying customers.

[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) maintains its own [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) kernels for the [distro’s life cycle of 10-plus years](https://access.redhat.com/support/policy/updates/errata). Red Hat does this by backporting security fixes and selected features to a constant kernel version, even when upstream has dropped that branch. RHEL also offers [Extended Life Cycle/Extended Life Cycle Support (ELS](https://www.redhat.com/en/resources/els-datasheet)) add‑ons for older releases, which include kernel security updates beyond standard maintenance.

RHEL‑compatible distributions such as [AlmaLinux](https://almalinux.org/ja/) and [Rocky Linux](https://rockylinux.org/ja-JP) track RHEL’s LTS kernels through their own rebuilds, effectively extending kernel maintenance for users on the same timelines as the corresponding RHEL releases.

[OpenELA](https://openela.org/), the RHEL-compatible Linux distribution backed by [Oracle](https://www.oracle.com/developer?utm_content=inline+mention), [SUSE](https://www.suse.com/ja-jp/) and [CIQ/Rocky Linux](https://ciq.com/products/rocky-linux), also [supports older kernels via the RHEL code tree](https://thenewstack.io/openela-liberates-red-hat-enterprise-linux-source-code/). In addition, [OpenELA explicitly stepped in to maintain the former LTS Linux 4.14](https://www.zdnet.com/article/linux-4-14s-long-term-support-will-live-on-after-all-thanks-to-this-alliance/) until December 2024. Nevertheless, OpenELA [was still releasing Linux 4.14 code in 2025](https://github.com/openela/kernel-lts/releases).

[Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention) was also [supporting 4.14 on Amazon Linux 2.0](https://docs.aws.amazon.com/ja_jp/AL2/latest/relnotes/relnotes-20250818.html)  through the end of October 2025, and the also otherwise obsolete 5.10 kernel through June 20, 2026.

SUSE maintains [SUSE Linux Enterprise Server (SLES)](https://www.suse.com/ja-jp/products/server/) kernels with long life cycles, similar to Red Hat, and offers extended support options. Starting with SLES 16 and its Linux 6.12 kernel, [SUSE now offers 16 years of support](https://www.zdnet.com/article/suse-enterprise-linux-16-is-here-and-its-killer-feature-is-digital-sovereignty/).

Finally, [Canonical](https://canonical.com/) maintains [Ubuntu](https://www.ubuntu.com/) [LTS kernels for up to 15 years](https://thenewstack.io/canonical-extends-ubuntu-linux-support-for-up-to-15-years/) with add‑on support packages. Canonical also offers [LTS for the 4.14 and otherwise out-of-date kernels](https://ubuntu.com/kernel). For example, the company still supports the 11-and-a-half-year-old Ubuntu 14.04 distro.

Why should you use either the official LTS kernel or its commercially supported twins? It’s simple. As Kroah-Hartman said in a 2020 “Ask the Expert” interview at Open Source Summit Europe, [they provide developers with a stable application binary interface (ABI)](https://www.zdnet.com/article/linux-5-10-will-be-the-next-long-term-support-linux-kernel/). It also provides, he’s said, a continuous [stream of security patches](https://www.zdnet.com/article/kernel-security-now-linuxs-unique-method-for-securing-code/). This is far safer than freezing on an old non‑LTS kernel or trying to cherry‑pick fixes yourself.

## What’s New in Linux 6.18?

At the core of 6.18 is a significant upgrade to the [slab memory allocator in the form of “sheaves.”](https://lwn.net/Articles/1010667/) This is a per‑CPU cache mechanism that reduces contention and speeds up memory allocation and freeing operations. The release also includes improved swapping behavior and other virtual machine (VM) tweaks to improve performance under memory pressure, particularly on busy servers and desktops.

One of the most visible and controversial changes is the removal of the experimental [Bcachefs file system](https://bcachefs.org/) from the mainline kernel. Bcachefs is a general-purpose Linux filesystem. It’s designed for systems that need strong data integrity and advanced storage features. In practice, it targets many of the same roles as [Btrfs](https://btrfs.readthedocs.io/en/latest/Introduction.html) or [ZFS](https://zfsonlinux.org/): ample local storage, multidisk arrays and setups that combine SSDs and HDDs for performance and capacity.

Bcachefs was booted out of the kernel largely because its maintainer, [Kent Overstreet](https://www.linkedin.com/in/kent-overstreet-8a281123/), [clashed with kernel maintainers](https://lwn.net/Articles/1035736/), including Torvalds, over patch timing, review practices and public communications. Behind the personal arguments was a technical one: The Bcachefas code fixes often came in late, kernel maintainers said, which clashed with the kernel’s preference for stabilizing during release candidate phases.

Torvalds and other maintainers argued that code that routinely needs that sort of late churn does not yet belong upstream, especially for something as critical as a filesystem. Bcachefx is now shipped as a [Dynamic Kernel Module Support (DKMS)](https://wiki.archlinux.org/title/Dynamic_Kernel_Module_Support) module, which is maintained outside the kernel tree. Distributions that wish to support Bcachefs must build and ship that external module.

On the networking side, Linux 6.18 adds support for [Accurate Explicit Congestion Notification (AccECN)](https://datatracker.ietf.org/doc/draft-ietf-tcpm-accurate-ecn/) in TCP. This enables finer‑grained congestion feedback and potentially better throughput under load. The kernel also introduces PSP‑encrypted TCP connections, an approach that offers hardware‑friendly offload characteristics as an alternative to traditional IPsec or TLS in some environments.

Security hardening continues with support for cryptographically signed [BPF](https://thenewstack.io/what-is-ebpf/) programs. This enables runtime-verified Extended Berkeley Packet Filter (eBPF) payloads, as well as refinements across the security subsystem and multi‑LSM configurations.

A notable infrastructure change is the ability to manage process namespaces using file‑handle‑like objects, similar in spirit to [pidfds](https://lpc.events/event/4/contributions/289/attachments/227/404/pidfds.pdf). This should make container runtimes and low‑level tooling more robust and race‑resistant.

Additionally, the [gradual integration of Rust into the kernel continues](https://thenewstack.io/rust-linux-and-cloud-native-computing/), including support for a Rust Binder driver. This is a [Google](https://cloud.google.com/?utm_content=inline+mention)-driven rewrite of the [Android Binder](https://source.android.com/docs/core/architecture/ipc/binder-overview?hl=ja) driver in Rust. This vital inter-process communication (IPC) system enables two processes on an Android-powered device to communicate with one another.

As with most kernel releases, 6.18 carries a large batch of new and updated drivers across architectures, including x86\_64, ARM, RISC‑V, and others. It also — surprise! — improves support for recent GPUs, SoCs and storage controllers. It also comes with fixes and enhancements for popular handheld gaming PCs such as the Asus ROG Ally and Lenovo Legion Go 2, as well as better power management and device‑tree coverage for laptops and embedded boards.

For end users, that translates into better out‑of‑the‑box hardware support on upcoming distributions that track the new LTS line.

For Linux desktop users — [Jack Wallen](https://thenewstack.io/author/jack-wallen/) and I wave — the main benefits of Linux 6.18 will be faster, more scalable memory allocation, improved network efficiency and broader hardware enablement, especially on modern GPUs and newer ARM‑based systems.

Server operators and cloud providers are likely to focus on dm‑pcache for hybrid storage, the new TCP capabilities, and signed BPF infrastructure as they evaluate 6.18 as a long‑term platform. With support stretching to 2027 and no single “killer” feature, Linux 6.18 positions itself as a conservative but foundational release that many distributions will standardize on for the next few years.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)