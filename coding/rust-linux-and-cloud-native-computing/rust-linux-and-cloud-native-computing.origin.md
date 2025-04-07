# Rust, Linux and Cloud Native Computing
![Featued image for: Rust, Linux and Cloud Native Computing](https://cdn.thenewstack.io/media/2025/04/6d6504ec-rust-programming-image-1-1024x584.jpg)
LONDON — In his keynote at [KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/), [Greg Kroah-Hartman](https://thenewstack.io/greg-kroah-hartman-lessons-for-developers-from-20-years-of-linux-kernel-work/), the Linux stable release maintainer, said that Linux, which takes in 76,000 changes annually, with 380 maintainers and 700 developers, is slowly but surely embracing Rust in the Linux kernel.

Why is the poster child for C programming incorporating the comparatively new Rust? Easy: Rust is a lot safer. Kroah-Hartman gave the example of a Bluetooth security bug that was fixed years ago, but, whoops, after looking fine for its first few years, it turns out the fix introduced a new bug. With C, this is all too common. It’s hard to make memory-safe C.

When “we write that code in Rust,” Kroah-Hartman explained, “not only do we catch the error, the compiler catches the bug for you, and that’s very, very important. We want the compiler to note the bug even before the maintainer has to look at this stuff again.”

## Fewer CVEs
Since Rust’s compiler can enforce rules that prevent many of these problems at compile time, this cuts down on the number of [Common Vulnerabilities and Exposures](https://thenewstack.io/how-linux-kernel-deals-with-tracking-cve-security-issues/) (CVEs) in the kernel.

This, in turn, is important for cloud native computing, indeed everything that runs on Linux, such as servers and washing machines, because when there’s a Linux bug today, it’s almost always a security hole because Linux works at such a low level.

Currently, the Linux kernel contains about 34 million lines of C code, with only 25 thousand lines written in Rust. However, [new programs, such as GPU drivers, are being written in Rust](https://thenewstack.io/rust-integration-in-linux-kernel-faces-challenges-but-shows-progress/). This shift is expected to make the code easier to understand and review, leading to improved stability over time.

That’s great, but incorporating Rust into the [Linux kernel](https://thenewstack.io/linux-kernel-6-14-enhanced-drivers-security-performance-improvements/) isn’t easy. Even Linux’s creator Linus Torvalds, as he readies the next Linux kernel release, has said merging Rust into Linux isn’t easy. “[I decided to try to do the merge on my own, but failed.](https://lore.kernel.org/lkml/CAHk-=wjpDpK0cd=tBk2t005nrddL0hXRQ+h+iZPHfVsi6qQY+w@mail.gmail.com/) I came close, but it was good to have your example merge to see what I got wrong. I’ll learn eventually, in the meantime please do continue to give me example merges and I’ll use them as training wheels.”

## Write Code for People, Then for Compilers
Except, as Kroah-Hartman pointed out, “changing kernel developers minds is hard.” For example, prominent software engineer and Linux kernel maintainer Christoph [Hellwig is a C expert, but he, understandably, isn’t thrilled about needing to learn Rust](https://www.phoronix.com/news/Torvalds-Override-On-Rust-Code) as well.

Another reason you may not have thought of — I think everyone can understand not wanting to learn a new programming language — and why “we are grumpy about this [moving to Rust] is because it forces us to review our C code, and our code has evolved over the past 30 years in ways that sometimes we don’t understand it.”

So, he continued, “sometimes we need to go back and look at it and enforce the rules Rust allows us to force, to enforce rules on our C APIs in the kernel that we hadn’t known to do before. So it’s making us re-review older code, and it’s hard. The old person maintainers don’t want to do new things. They don’t want to look at their old stuff at times, but the change can be good.”

That’s because this will make maintaining the code easier. Again, we write code first for people, then compilers. This will make us last the next 30 to 40 years, make the compiler do the work for us, and this lets us, I think, have more fun for maintainers because, again, the compiler can work ahead of time.”

By making it easier for maintainers and developers, it will also “make Linux more secure for you. You can go solve your cloud native computing problems, and that’s very important for you.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)