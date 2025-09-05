Microsoft has tinkered with Windows security for decades. Now the company is trying to fix it with [Rust](https://thenewstack.io/rust-programming-language-guide/), and they want everyone else to use it, too.

The problem is simple: C and C++ let you write code that looks fine but crashes spectacularly, or worse, gets hacked. Microsoft’s own kernel has been leaking privilege escalation bugs monthly through Win32k.sys, the part that handles graphics and windows.

During his keynote at [RustConf 2025](https://rustconf.com/) this week, entitled “From Blue Screens to Orange Crabs: Microsoft’s Rusty Revolution,” [Mark Russinovich](https://www.linkedin.com/in/markrussinovich/), Microsoft’s [Azure](https://thenewstack.io/microsoft-linux-is-the-top-operating-system-on-azure-today/) CTO, described the situation as being like “an underground oil repository that is leaking oil up a few drops at a time, just consistently.”

So, they started rewriting chunks in Rust. Not the whole thing; just pieces. If you dig into your Windows System32 folder right now, you’ll find a file called win32kbase\_rs.sys. That’s Rust code running in your kernel.

Here’s the thing that actually matters: When a security researcher found a bug in the new Rust version, it crashed the system instead of letting an attacker take over, Russinovich said.

“This we view as a success,” he said. “This code written in [C++](https://thenewstack.io/introduction-to-c-programming-language/), this bug would have actually resulted in a potential elevation of privilege, as opposed to a blue screen crash that’s very deterministic and can’t be exploited.”

Microsoft also rewrote [DirectWrite](https://learn.microsoft.com/en-us/windows/win32/directwrite/direct-write-portal), the font renderer that’s caused countless security problems over the years. Two Microsoft developers did it in six months — 154,000 lines of code. It runs faster than the old version and doesn’t have the same kinds of bugs.

## The Azure Mandate

Russinovich has been pushing Rust internally for years, even before he had the official authority to mandate it.

“I’d actually, even prior to that tweet, told our teams we should stop new projects in [C and C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) and start with Rust if we can’t tolerate a [garbage-collected language](https://thenewstack.io/does-garbage-collection-logging-affect-app-performance/),” he said during his RustConf keynote.

Now, as deputy CISO of Azure (in addition to CTO), he can make it official: “There’s just too much risk in adopting or creating new C++, you will not do it.”

The results are everywhere in Azure. For instance, the [Caliptra](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/securing-hardware-and-firmware-supply-chains/4268815) hardware root of trust was written entirely in Rust from the start.

“If you take a look at the ROM of Caliptra, this is all open source,” Russinovich said. “If you take a look at the firmware of Caliptra, if you take a look at the emulator for Caliptra, they’re all written in Rust.”

[Azure Boost](https://learn.microsoft.com/en-us/azure/azure-boost/overview), the system that manages servers and handles network offloading, mandates Rust for anything touching untrusted data, he said.

“Every place that we’ve got untrusted input handling, the mandate is rewrite it in Rust, and any new agents are written in Rust.”

Even [Hyper-V, Microsoft’s hypervisor](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/) and “one of the most secure pieces of software that Microsoft’s ever created,” is getting the Rust treatment. ARM64 emulation support now ships in Rust, marking the beginning of a gradual transition for this critical component.

Microsoft is officially shipping Rust as part of Hyper-V, and this is just one place where you’ll see continuing growth of Rust in that component, Russinovich said.

“And speaking of hypervisors, there’s the hypervisor itself, and there’s the [Virtual Machine Manager (VMM)](https://learn.microsoft.com/en-us/system-center/vmm/overview?view=sc-vmm-2025). We started this project in Rust from the start, [OpenVMM](https://thenewstack.io/microsoft-open-sources-openvmm-rust-powered-vm-monitor/),” he said.

In fact, there’s a core group of people in the kernel team in Windows that are Rust enthusiasts who said Microsoft needed an open Virtual Machine Manager that sits underneath the virtual machine (VM) on Azure via hosts and talks to Azure Boost, he added.

“This is where we run, for example, emulated network adapters that connect to the Azure Boost network adapter. So, to provide compatibility with existing operating systems, that system is a Linux system,” Russinovich said. “That system runs on open virtual machine manager that’s written in Rust. OpenVMM demonstrates Microsoft’s commitment not just to open source and Rust, but to cross-platform portability. So, open VMM is compatible, not just with Hyper V, not just with Windows, also with Linux and also with KVM [Kernel-based Virtual Machine], and this is completely open source.”

Russinovich also mentioned the [Hyperlight project](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/), an open source Rust library you can use to execute small, embedded functions using hypervisor-based protection for each function call at scale.

In addition, Microsoft released an Azure SDK for Rust earlier this year.

[![](https://cdn.thenewstack.io/media/2025/09/d90ce51f-screenshot-2025-09-03-123836-1-1.png)](https://cdn.thenewstack.io/media/2025/09/d90ce51f-screenshot-2025-09-03-123836-1-1.png)

Mark Russinovich at RustConf.

## Office Goes All In

Meanwhile, Office had a different problem. Its semantic search system, [DiskANN](https://www.microsoft.com/en-us/research/project/project-akupara-approximate-nearest-neighbor-search-for-large-scale-semantic-search/), worked fine for Bing’s hundreds of nodes but couldn’t handle Office’s millions of documents.

“Office wanted millions of nodes in the graph. They realized that the implementation of DiskANN and C just wouldn’t give them the scale and performance that they wanted,” Russinovich said.

So, they rewrote it in Rust. The results were dramatic: better performance at the same accuracy levels and reduced memory usage.

“We saw tremendous wins,” Russinovich noted. The Office entertainment devices division became so convinced, they went “all in on Rust,” preferring it even over memory-safe languages like C# for its concurrency handling.

[Azure Data Explorer](https://azure.microsoft.com/en-us/products/data-explorer) shows what large-scale migration looks like. One developer spent a year porting the data storage layer to Rust, then the query engine followed. The system now processes “literally hundreds of petabytes of data” with 350,000 lines of Rust alongside 2.3 million lines of C# and shrinking amounts of C++, he said.

## Opening the Floodgates to Partners

Now Microsoft wants hardware companies and driver developers to write their own Rust drivers. According to a [blog post](https://techcommunity.microsoft.com/blog/windowsdriverdev/towards-rust-in-windows-drivers/4449718) by [Nate Deisinger](https://techcommunity.microsoft.com/users/nate_deisinger/3156254) from Microsoft’s Windows team, they’ve built a whole framework called [windows-drivers-rs](https://github.com/microsoft/windows-drivers-rs/) that basically translates between Rust and the Windows Driver Kit (WDK).

“By building off the terrific efforts of [the Surface team](https://techcommunity.microsoft.com/blog/SurfaceITPro/safer-drivers-stronger-devices/4431411), we’re starting our journey to make Rust a first-class language for driver developers around the world,” Deisinger wrote in the post the day before Russinovich spoke at RustConf.

The pieces are straightforward: [wdk-build](https://github.com/microsoft/windows-drivers-rs/blob/main/crates/wdk-build) hooks [Cargo](https://thenewstack.io/how-to-write-rust-code-like-a-rustacean/) into the Windows build system, [wdk-sys](https://github.com/microsoft/windows-drivers-rs/blob/main/crates/wdk-sys) provides raw access to Windows driver APIs, [wdk](https://github.com/microsoft/windows-drivers-rs/blob/main/crates/wdk) gives you slightly safer versions and [cargo-wdk](https://github.com/microsoft/windows-drivers-rs/tree/main/crates/cargo-wdk) lets you create and build drivers like any other Rust project, he wrote.

You can make Kernel-Mode Driver Framework (KMDF), User-Mode Driver Framework (UMDF) or Windows Driver Model (WDM) drivers that actually load and run on Windows 11. The catch is you still need to write a lot of unsafe Rust code because Windows kernel APIs weren’t designed for memory safety.

Microsoft is working on fixing that, too. As Deisinger explains in the blog, they want to create safe wrappers so “the majority of driver code can be written in safe Rust.” They’ve got experimental versions working internally, but they’re not ready for public use yet.

## What Developers Actually Think

Microsoft surveyed its own people about Rust. The feedback was overwhelmingly positive once developers got past the initial shock.

“We see developers, if they’re coming from a C++ especially, it’s a shock to them. It’s like, ‘Wow, this is a totally different way,'” Russinovich explained.

But after a few months, something clicks. “After a couple months, they’ve actually shifted their mind and now then become one with the way that Rust borrow checker thinks and works and actually enjoy it,” he said.

Developers love the performance gains.

“This is pretty consistent. Whenever we take a C++ code base and port it to Rust, we typically see a performance improvement,” Russinovich said. “Developers love eliminating bug classes entirely and they love writing code once and not debugging it for days,” he added.

What they don’t like: Mixing with existing C++ and C# code is painful. Async debugging sucks. Dynamic linking has issues. But “the developers that even have these complaints don’t want to give up Rust at this point,” he noted.

## The Secret Weapon: AI Translation

Microsoft is building something potentially game-changing — AI tools that can automatically translate entire codebases from C++ to Rust. Using their [GraphRAG](https://microsoft.github.io/graphrag/) technology, they can create semantic representations of large codebases that language models can reason about and port piece by piece.

Russinovich demonstrated this live, showing a Python game being translated to Rust while maintaining the original project structure and functionality.

“You’re going to see a lot more of this kind of acceleration with the aid of [LLMs](https://thenewstack.io/introduction-to-llms/) [large language models] of code from existing languages, C, C++, specifically to Rust over time.”

This could solve the biggest barrier to Rust adoption — the massive effort required to port existing codebases.

## The Bigger Bet

Microsoft’s Rust push goes way beyond just being trendy. Russinovich frames it as essential for the future.

“We believe that memory-safe languages such as Rust represent the future of secure software engineering,” he said. “Today’s security landscape demands reliability and safety guarantees at every surface from the edge to the cloud.”

They’re not alone. The National Security Agency (NSA) endorsed the shift to memory-safe languages shortly after [Russinovich’s famous 2022 tweet extolling the virtues of Rust](https://thenewstack.io/microsofts-it-outage-reminder-rust-is-better-than-c-c/). [Linux added Rust support](https://thenewstack.io/rust-integration-in-linux-kernel-faces-challenges-but-shows-progress/), he noted. The industry momentum is building.

The driver framework represents Microsoft extending this philosophy beyond its own code. If hardware vendors start writing Rust drivers, Windows gets more secure without Microsoft doing all the work.

But driver development is conservative. People stick with what works. Microsoft is betting that demonstrable security improvements plus comprehensive tooling will be enough to overcome decades of inertia.

The early results are promising. Microsoft has shown that Rust code fails safely where C++ creates vulnerabilities. They’ve deployed it in their most critical systems: kernels, hypervisors, cryptographic libraries. Now they want the whole ecosystem to follow.

As Russinovich put it: “Rust is permeating Microsoft’s core infrastructure at this point, and it’s just going to continue to accelerate.” The driver framework is just the latest piece of that larger transformation.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)