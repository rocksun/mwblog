# Microsoft’s IT Outage Reminder: Rust Is Better Than C/C++
![Featued image for: Microsoft’s IT Outage Reminder: Rust Is Better Than C/C++](https://cdn.thenewstack.io/media/2024/07/9caafb56-airport-2373727_1280-1024x682.jpg)
Last week, the blue screen of death (BSOD) appeared on Windows systems across the world, [caused by a faulty configuration update](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/) delivered by security vendor [CrowdStrike](https://thenewstack.io/crowdstrike-ups-its-falcon-cloud-security-game/).

The outage — called by some as being the world’s most severe — paralyzed critical infrastructures. However, a Microsoft official over the weekend also reminded developers about [better coding practices](https://thenewstack.io/infrastructure-as-code-6-best-practices-for-securing-applications/) to improve system reliability and reduce the chances of systems crashing and BSODs.

[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure’s CTO [Mark Russinovich](https://www.linkedin.com/in/markrussinovich/) said developers should slowly deprecate C/C++ and move to the [memory-safe Rust language](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/) to reduce system crashes and BSODs. To be sure, the tweet wasn’t directly related to the faulty CrowdStrike update.
On Saturday, Russinovich [retweeted a 2022 tweet](https://x.com/markrussinovich/status/1814853234445722076) stating, “It’s time to halt starting any new projects in C/C++ and use Rust for those scenarios where a non-GC language is required. For the sake of security and reliability, the industry should declare those languages as deprecated.”

## Null Pointer
BSODs occur for various reasons, including memory errors, driver issues, and process problems in Windows, which rely on a kernel written in C/C++. Coder [Zack Vorhies](https://www.linkedin.com/in/zachvorhies/), who formerly worked at [Google](https://cloud.google.com/?utm_content=inline+mention), said the outage was due to faulty C/C++ code, but that was shot down by Google researcher [Tavis Ormandy](https://github.com/taviso).

Vorhies [attributed the mass outage to a null pointer](https://x.com/Perpetualmaniac/status/1814376668095754753), or a line in code pointing to no valid memory location, which he described as a “null pointer from the memory-unsafe C++ language.”

Ormandy shot down the claim by Vorhies, and [CrowdStrike said](https://www.crowdstrike.com/blog/falcon-update-for-windows-hosts-technical-details/), “This is not related to null bytes contained within Channel File 291 or any other Channel File.”

## Pro Rust
Microsoft has championed Rust for many years now, but internally, moving code over is a work in progress. The company realizes switching from C/C++ can’t be done overnight.

“We are working on it. Already a lot of Rust in Azure and some Rust in Windows,” Russinovich said in a [recent tweet](https://x.com/markrussinovich/status/1815046656469225911).

The approach to Rust is measured; one step first is to create prototype applications that demonstrate Rust code works with Windows. Microsoft is also moving perimeter applications that secure system hardware over to Rust.

## UEFI Firmware
Microsoft is creating its secure boot modules for its Surface hardware around Rust. The UEFI (Unified Extensible Firmware Interface) includes firmware code that takes a system from boot to the Windows OS. The UEFI code typically sits on a motherboard and is accessed when the computer switches on.

The UEFI firmware loads into memory, and Rust provides memory-safe mechanisms to prevent systems from crashing or being exploited. Many hardware vulnerabilities and security concerns initiate inside computer memory.

The U.S. government’s main technology security agency, the [Cybersecurity Infrastructure and Security Agency (CISA)](https://thenewstack.io/why-does-the-nsa-care-about-the-software-supply-chain/), in December called for companies to [switch over to memory-safe technologies](https://www.cisa.gov/news-events/news/urgent-need-memory-safety-software-products).

“Most modern programming languages other than C/C++ are already memory safe. Memory-safe programming languages manage the computer’s memory so the programmer cannot introduce memory safety vulnerabilities,” CISA said in the advisory note.

## Rust To Protect PCs
Microsoft is securing homegrown hardware with security and firmware built around Rust, said [Dave Weston](https://www.linkedin.com/in/dwizzzle/), vice president of enterprise and OS security at Microsoft, in an interview.

The company’s Secured-core initiative includes a stable and secure boot environment for Surface and Windows PCs. The company has transitioned many firmware components from C to Rust, which provides system stability and reduces the chances of vulnerabilities that expose systems to hackers.

Microsoft has also created a real-time OS fully written in Rust for its security processor called Pluton. Pluton includes a trusted platform module (TPM), which stores critical security information such as biometric data.

“Microsoft is invested in making more things secure by design. This is one of the advantages of having our own security processor, rather than waiting for the industry there. We’re going to go towards Rust…. which has huge advantages over traditional native languages in that realm,” Weston said.

Memory leaks have been a major issue for TPMs. [QuarksLab](https://blog.quarkslab.com/vulnerabilities-in-the-tpm-20-reference-implementation-code.html) last year pointed out two vulnerabilities in TPM 2.0 code that expose memory to out-of-bounds read and write, potentially exposing critical information to attacks from hackers in virtualized environments. Memory-safe languages like Rust could help prevent such issues.

## Microsoft’s History With Rust
Mozilla introduced a Firefox browser with Rust components about a decade ago, and a groundswell of programmers is now adopting it. Other memory-safe languages include [Golang](https://thenewstack.io/golang-what-are-constants-in-go-and-how-do-you-use-them/), [Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/), [C#](https://thenewstack.io/microsoft-we-are-not-abandoning-c-for-rust/), Swift, and [Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/).

Microsoft ran two experiments to check the viability of Rust in terms of viability and performance. Win32K is often a common choice for frequent attacks as it offers a convenient escalation of privilege attacks.

“We started Rust right in the place where it would offer the most security value,” Weston said in a [June 20 podcast](https://azuresecuritypodcast.azurewebsites.net/).

The first was the font parser, which created remote attack surfaces in browsers or Office clients. It took two to three months to convert DirectWrite, their modern Web App SDK font parser, to Rust.

“It took roughly two to three months of a couple of developers’ time. And the interesting thing that came out of it is performance actually got better,” Weston said in a podcast.

The second experiment involved some Graphics Device Interface (GDI) surfaces in Win32k, an internal graphics component originally designed in the late 1980s. Microsoft didn’t want to rewrite the entire code, so it experimented with slicing out individual components of Win32k to implement in Rust. The experiment was successfully completed, and the Rust components now ship with Windows.

“This is especially important because Microsoft Windows is compiled with the Visual C++ compiler or C compiler, while Rust’s backend is actually LLVM [Low Level Virtual Machine],” Weston said.

## Rust In Azure
Microsoft is also implementing Rust extensively in Azure.

The company is implementing a virtual machine manager written in Rust that will manage Hyper-V in Azure.

Rust is also being implemented in Azure Boost, which Weston called the “future architecture of Azure.”

“That’s where we are offloading more of the performance aspects of Azure hosts to specialized cards like smart NICs and/or FPGAs for storage,” Weston said.

Microsoft is spending roughly $10 million on Rust tools, with Azure being the first target. The company also wants to establish a long-term support version of Rust, similar to the [Linux operating system](https://thenewstack.io/rust-in-the-linux-kernel/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)