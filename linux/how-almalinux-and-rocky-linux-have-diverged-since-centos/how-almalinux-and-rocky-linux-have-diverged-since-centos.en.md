Both [AlmaLinux](https://almalinux.org/) and [Rocky Linux](https://rockylinux.org/) emerged in response to [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)’s [discontinuation of CentOS Linux](https://thenewstack.io/red-hat-deprecates-linux-centos-in-favor-of-a-streaming-edition/), aiming to provide free, community-driven, enterprise-grade operating systems compatible with [Red Hat Enterprise Linux (RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)). That was then. This is now. While they started with similar goals, their strategies, governance and technical directions diverged.

Before diving into that, let’s start with where each came from. [CloudLinux](https://cloudlinux.com/), a CentOS-based company specializing in Web server Linux, [started AlmaLinux](https://thenewstack.io/jack-aboutboul-how-almalinux-came-to-be-and-why-it-was-needed/). From there, the distro moved to the nonprofit [AlmaLinux OS Foundation](https://almalinux.org/members/). Its focus is on providing a stable, RHEL-compatible Application Binary Interface (ABI) platform. Commercial support is available via [TuxCare](https://tuxcare.com/).

[Gregory Kurtzer](https://gmkurtzer.github.io/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform), a CentOS co-founder, founded Rocky Linux, which is governed by the [Rocky Enterprise Software Foundation (RESF)](https://www.resf.org/). This distribution emphasizes a community-driven approach and 1:1 binary compatibility with RHEL. For Rocky support, you can go to [CIQ](https://ciq.com/products/rocky-linux/), Kurtzer’s company.

Both distros rely on the [Red Hat Package Manager (RPM)](https://rpm.org/) and the [Dandified Yum (DNF)](https://opensource.com/article/18/8/guide-yum-dnf) package manager. While Red Hat has also recently adopted [immutable images in place of package patching for RHEL 10](https://thenewstack.io/red-hat-enterprise-linux-10-an-ai-driven-quantum-ready-platform/), neither AlmaLinux nor Rocky Linux has adopted this approach.

For support, each, like Red Hat, offers its major versions 10 years of long-term support — five years of active support (feature and bug updates), followed by five years of security updates and critical bug fixes. So, for example, the newly released 10 editions of both distros get active support until May 2030 and security support until May 2035.

## AlmaLinux Moves Beyond RHEL

So far, they sound pretty much the same, but the closer you look, the more differences you’ll find. For example, AlmaLinux is no longer a strict 1:1 binary clone of RHEL. Instead, it’s built on the [CentOS Stream source code](https://gitlab.com/redhat/centos-stream?utm_source=opensourcewatch.beehiiv.com&utm_medium=referral&utm_campaign=almalinux-boosts-legacy-hardware-support-with-latest-linux-release). Still, thanks to its ABI RHEL compatibility, you can run essentially all RHEL apps on it. At the lowest level, there are differences now between RHEL and AlmaLinux. Will that matter to you? Probably not.

Indeed, many of you will appreciate some of AlmaLinux’s variations. For instance, when Red Hat [dropped support for x86-64-v2 chip microarchitecture](https://developers.redhat.com/articles/2024/01/02/exploring-x86-64-v3-red-hat-enterprise-linux-10), AlmaLinux elected to [continue to ship binaries for this earlier architecture](https://thenewstack.io/almalinux-10-beta-supports-older-x86-chipsets/). This means you can run AlmaLinux 10, the newest distro, on servers using x86-64 processors dating from approximately 2008 to 2013.

There are also a host of other minor differences. These include support for [Simple Protocol for Independent Computing Environments (SPICE)](https://www.spice-space.org/), the virtual desktop protocol, and both Firefox and Thunderbird, which are shipped as RPM packages instead of Flatpak.

In addition, [AlmaLinux 9.4](https://opensourcewatch.beehiiv.com/p/almalinux-boosts-legacy-hardware-support-latest-linux-release) and 10.0 have explicitly reintroduced support for device drivers and hardware that RHEL 9.4 and 10.0 have dropped. This includes storage controllers, network adapters and other components critical to older servers and workstations.

Last, but not least, [AlmaLinux will patch, on request, common vulnerabilities and exposures (CVEs)](https://fossforce.com/2024/04/in-a-first-almalinux-patches-a-security-hole-that-remains-unpatched-in-upstream-rhel/) even if Red Hat has rated them as low or moderate priority.

## Rocky Linux Keeps the Faith

On the other hand, if you want a true RHEL clone that mirrors CentOS’s original model as closely as possible, Rocky Linux is what you want. This is great if your top priorities are stability and predictability.

Let’s say security is what matters the most to you. In that case, CIQ would like to introduce you to [Rocky Linux from CIQ – Hardened](https://ciq.com/products/rocky-linux/hardened/). This version minimizes zero-day and CVE risks by eliminating many potential attack surfaces and common exploit vectors. It includes code-level hardening that blocks commonly used exploit paths, reducing the risk of successful attacks. It also uses [Linux Kernel Runtime Guard (LKRG](https://lkrg.org/)) to detect sophisticated intrusions that evade traditional security measures. All packages within are validated and delivered via a secure supply chain, ensuring that the operating system is delivered securely and is always up to date.

## The Road To Take

So, which should you go with? That’s up to you. Both are excellent distros.

The one thing I can say, though, to the hundreds of thousands — millions? — of you who are still using [CentOS 7 even though it ended its supported life on June 20, 2024](https://opensourcewatch.beehiiv.com/p/centos-7s-end-life-sight-ready), you must bite the bullet and move to a supported Linux. Yes, yes, I know upgrading from CentOS can be costly and time-consuming. But I also know that when — not if — a major security zero-day exploit wrecks existing CentOS installations, you’ll be in a world of trouble. The time to switch to AlmaLinux or Rocky Linux is before that day comes, not after.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)