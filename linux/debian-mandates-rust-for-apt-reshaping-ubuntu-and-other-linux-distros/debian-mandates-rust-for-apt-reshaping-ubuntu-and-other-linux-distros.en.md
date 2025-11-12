One of the world’s oldest and [most influential Linux distributions](https://thenewstack.io/choosing-a-linux-distribution/), [Debian](https://www.debian.org/), has officially announced plans to restructure its development strategy by adopting [Rust](https://thenewstack.io/rust-programming-language-guide/) as a core language for system-level tools and future packages.

[Julian Andres Klode](https://www.debian.org/vote/2025/platforms/jak), a long-time Debian developer and lead maintainer of the [Advanced Package Tool (APT)](https://wiki.debian.org/Apt), announced on the Debian developer list that, going forward, [Rust will be a required dependency for Debian’s fundamental APT package manager](https://lists.debian.org/deity/2025/10/msg00071.html).

Specifically, Klode wrote that he planned “to introduce hard Rust dependencies and Rust code into APT, no earlier than May 2026. This extends at first to the Rust compiler and standard library, and the Sequoia ecosystem.”

Sequoia is a Debian project dedicated to creating a [Rust implementation of OpenPGP](https://wiki.debian.org/OpenPGP/Sequoia#:~:text=Sequoia%20PGP%20is%20a%20project,these%20IRC%20channels%20on%20OFTC:).

Why? Klode explained, “Our code to parse .deb, .ar, .tar, and the HTTP signature verification code would strongly benefit from memory-safe languages and a stronger approach to unit testing.”

## Impact on Ubuntu, Mint, and Other Debian-Based Distros

APT is a core part of Debian. Essentially all Linux distros based on Debian, such as [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/), Mint, and MX Linux, [rely on APT](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/) for package management. This means that Rust code is coming to all these distributions. That’s perfectly fine with dome distribution architects. For example, Canonical has already [incorporated Rust into Ubuntu sudo](https://thenewstack.io/why-sudo-rs-brings-modern-memory-safety-to-ubuntu-26-04/).

The rationale for these moves is to improve the operating system’s security and stability. Rust’s [memory-safe architecture](https://thenewstack.io/moving-from-c-to-rust-clickhouse-has-some-advice/) blocks such common bugs as buffer overflows, null pointer dereferences, and race conditions that have plagued C and C++ codebases for decades.

## The Rationale: Enhancing Security and Stability

If you don’t like it? Too bad. Klonde added, “If you maintain a port without a working Rust toolchain, please ensure it has one within the next six months, or sunset the port.”

Ouch.

Some developers aren’t pleased. [John Paul Adrian Glaubitz](https://github.com/glaubitz) was disappointed to see [“such a confrontational approach” chosen to make the APT announcement](https://lwn.net/ml/all/ad6e60711c8ed3372ed7f324d7b1be23b0722a0d.camel@physik.fu-berlin.de/).

At the same time, [Bjørn Mork](https://github.com/bmork) doubted that moving APT to Rust will be all that helpful. “[Rewriting code means adding new bugs](https://lwn.net/ml/all/87ldkqt09e.fsf@miraculix.mork.no/), whether or not the tools catch some of them. But for fun, let’s assume that we eventually end up with fewer serious bugs in the rewritten software. How long will that take? …  Are we expected to just accept regressions for a while, because the Rust reimplementations eventually will catch up with what we have today?”

## Developer Community Reactions and Concerns

In a follow-up conversation on the Debian developer list, Klonde shrugged. “[Rust already is a hard requirement for most Debian ports](https://lwn.net/ml/all/20251031223819.GA97356@debian.org/), so this is hardly surprising.”

He also pointed out that only four older architectures — alpha, hppa, m68k, and sh4 — are not currently up to speed with Rust. If the developers for these platforms can’t provide Rust support, well, as  ebee\_matteo [put it on Linux Weekly News (LWN)](https://lwn.net/Articles/1044507/), “It’s yet another sign that those architectures do not have enough developers to warrant the continued effort to ensure cross-platform compatibility. … This is not even a Rust/non-Rust debate. It is a ‘Does this port have enough developers and users at all?'”

Looking ahead, Debian’s next major release, Forky, Debian 14, is slated to arrive in mid-2026. It will feature deeper Rust integration not only in APT but potentially in other core utilities, build infrastructure and security-critical modules.

As for those Debian distributions that can’t, or won’t, adopt Rust, they can always follow the path of the Debian-based Linux distro [antiX](https://antixlinux.com/), which continues to build on older Debian releases, such as Debian 12 “Bookworm,” to support 32-bit hardware.

Most developers will eventually join Klode in embracing Rust. Really, it’s not that hard a language to learn, and it does make it easy to write memory-safe code. As someone who has bled over C code, trying — and often failing — to make my program memory-safe, I, for one, welcome how Linux and its distributions are now integrating Rust.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)