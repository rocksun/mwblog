TOKYO —  At the invitation-only [Linux Kernel Maintainers Summit](https://events.linuxfoundation.org/linux-kernel-maintainer-summit/) here, the top [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) maintainers decided, as [Jonathan Corbet](https://social.kernel.org/users/corbet), Linux kernel developer, put it, “The consensus among the assembled developers is that [Rust in the kernel is no longer experimental](https://lwn.net/Articles/1049831/) — it is now a core part of the kernel and is here to stay. So the ‘experimental ‘ tag will be coming off.” As Linux kernel maintainer [Steven Rosted](https://www.linkedin.com/in/steven-rostedt-0159437a/) told me, “There was zero pushback.”

This has been a long time coming. This shift caps five years of sometimes-fierce debate over whether the [memory-safe language](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/) belonged alongside C at the heart of the world’s most widely deployed open source operating system.

## The Signs Were There

The signs were there, though, that this step to [Rust](https://thenewstack.io/rust-programming-language-guide/) acceptance was coming. At the recent Linux Foundation [Open Source Summit Korea 2025](https://events.linuxfoundation.org/open-source-summit-korea/), Torvalds had said, “I think we’ve reached a stage [where] [Rust is truly becoming part of the kernel](https://www.zdnet.com/article/what-linus-torvalds-really-thinks-about-ai-and-software-development-might-surprise-you/), and it’s no longer just an experimental thing.”

No, no, it’s not. It all began when [Alex Gaynor](https://www.linkedin.com/in/alex-gaynor-77518b1ba/) and [Geoffrey Thomas](https://ldpreload.com/) at the 2019 Linux Security Summit said that about two-thirds of Linux kernel vulnerabilities come from memory safety issues. Rust, in theory, could avoid these by using [Rust’s inherently safer application programming interfaces (API).](https://www.youtube.com/watch?v=RyY01fRyGhM)

In the subsequent 2020 Linux Plumbers meeting, developer [Nelson](https://www.linkedin.com/in/nelhage/) Elhage, [in his summary of the Plumbers’ meeting on Rust in Linux](https://lwn.net/Articles/829858/), explained that Linux Rust proponents aren’t “proposing a rewrite of the Linux kernel into Rust; they are focused only on moving toward a world where new code may be written in Rust. The three areas of potential concern for Rust support are making use of the existing APIs in the kernel, architecture support, and dealing with application binary interface (ABI) compatibility between Rust and C.”

In the meantime, [Miguel Ojeda, a Linux kernel developer, started migrating Linux code from C to Rust](https://www.memorysafety.org/blog/memory-safety-in-linux-kernel/). He created the [Rust for Linux project](https://github.com/Rust-for-Linux) to bring out-of-tree Rust modules to Linux in 2019.

By early 2021, Rust was, outside the Linux kernel, being brought closer to the world’s favorite operating system. [Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention) released [Bottlerocket Linux](https://cc.zdnet.com/v1/otc/00hQi47eqnEWQ6T9d4QLBUc?element=BODY&element_label=Bottlerocket+Linux&module=LINK&object_type=text-link&object_uuid=a8cdbe53-ce50-41b6-8d77-2309830e2c5b&position=1&template=article&track_code=__COM_CLICK_ID__&view_instance_uuid=87c931b4-6981-403a-a1b8-222e738ab692&url=https%3A%2F%2Faws.amazon.com%2Fblogs%2Fopensource%2Fannouncing-the-general-availability-of-bottlerocket-an-open-source-linux-distribution-purpose-built-to-run-containers%2F) for containers, which was partly Rust-based. At about the same time, [Sylvestre Ledru](https://www.linkedin.com/in/sylvestreledru/?originalSubdomain=fr), a [Debian Linux](https://www.debian.org/) developer, ported a Rust version of [Coreutils](https://www.gnu.org/software/coreutils/) to Linux using the [LLVM compiler infrastructure](https://llvm.org/) and its [Clang C language front-end](https://clang.llvm.org/) and tooling infrastructure.

## Give Rust A Chance

That March, [Linus Torvalds decided to give Rust a chance](https://www.zdnet.com/article/linus-torvalds-on-where-rust-will-fit-into-linux/). He told me at the time, he was in the ‘wait and see’ camp — I’m interested in the project, but I think it’s driven by people who are very excited about Rust, and I want to see how it actually ends up working in practice.”

“Personally,” Torvalds added, he’s “in no way “pushing” for Rust, [but] I’m open to it considering the promised advantages and avoiding some safety pitfalls, but I also know that sometimes promises don’t pan out.”

As it would turn out, those promises were kept. Backed by financial support from the Internet Security Research Group (ISRG) and [Google](https://cloud.google.com/?utm_content=inline+mention), on Sept. 20, 2021, Ojeda submitted the first pull request for the Rust for Linux project. This added initial Rust support, including Kbuild integration, initial support for built-in modules, and the beginnings of the kernel crate, with Safe Rust abstractions from Alex Gaynor and Geoffrey Thomas.

In those early days, the plan was not to rewrite Linux in Rust; it still isn’t, but to adopt it selectively where it can provide the most security benefit without destabilizing mature C code. In short,  new drivers, subsystems, and helper libraries would be the first targets,

It was not an easy journey. As Ojeda said in June 2022, “The kernel is a huge project with a lot of stakeholders. Since the beginning, it was clear that [adding a second ‘main’ language to the kernel would have both technical and management challenges.](https://www.memorysafety.org/blog/memory-safety-in-linux-kernel/)”

He would be proven right. Rust adoption in the kernel proved contentious within the kernel community. Some maintainers questioned the cost of mixing programming paradigms in Linux. For example, at the.2021 Kernel Maintainers Summit Video4Linux maintainer [Laurent Pinchart](https://www.linkedin.com/in/laurent-pinchart-ba88001/) said [he did not have time to “stop everything and learn Rust](https://lwn.net/Articles/869145/) anytime soon.”

## Resistance

While Rust began to move in, it still faced resistance. As [Dan Williams](https://www.linkedin.com/in/djbw/), senior principal engineer on Intel’s Linux core kernel architecture team, said at the [Linux Plumbers 2024](https://lpc.events/event/18/timetable/) meeting, “[Kernel maintainers tend to be very conservative.](https://www.zdnet.com/article/rust-in-linux-now-progress-pitfalls-and-why-devs-and-maintainers-need-each-other/) They know C backward and forward, but they don’t know Rust.” So, they “don’t know how to review this or debug that because they don’t understand the code.”

Mind you, they have reasons. In a dispute over how to get [Rust to work with the Linux kernel’s Direct Memory Access (DMA)](https://thenewstack.io/rust-integration-in-linux-kernel-faces-challenges-but-shows-progress/) Application Programming Interface (API), the real problem boiled down to, as senior Linux kernel developer [Ted T’so](https://www.linkedin.com/in/tytso/) observed, maintainers don’t have unlimited time, and [they don’t want to increase their “code maintenance burden.”](https://lore.kernel.org/lkml/20250208204416.GL1130956@mit.edu/?utm_source=the+new+stack)

Still, despite the fuss, more and more programs were ported to Rust. By April 2025, the Linux kernel contained about 34 million lines of C code, with only 25 thousand lines written in Rust. At the same time, more and more drivers and higher-level utilities were being written in Rust. For instance, the Debian Linux distro developers announced that going forward, [Rust would be a required dependency  in its foundational  Advanced Package Tool (APT)](https://thenewstack.io/debian-mandates-rust-for-apt-reshaping-ubuntu-and-other-linux-distros/),

## C’s Not Going Anywhere

This change doesn’t mean everyone will need to use Rust. C is not going anywhere. Still, as several maintainers told me, they expect to see many more drivers being written in Rust. In particular, Rust looks especially attractive for “leaf” drivers (network, storage, NVMe, etc.), where the [Rust-for-Linux bindings expose safe wrappers over kernel C APIs](https://mars-research.github.io/doc/2024-acsac-rfl.pdf).

Nevertheless, for would-be kernel and systems programmers, Rust’s new status in Linux hints at a career path that blends deep understanding of C with fluency in Rust’s safety guarantees. This combination may define the next generation of low-level development work.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)