# Big Moments in Rust 2024
![Featued image for: Big Moments in Rust 2024](https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png)
The [Rust](https://thenewstack.io/linus-torvalds-c-vs-rust-debate-has-religious-undertones/) project’s headline goal for the year has been the development of a new edition of Rust. [Editions](https://doc.rust-lang.org/edition-guide/index.html) create points in the project’s life cycle that allow new keywords to be added to the language, additions to the standard library and other changes to be made. This is “the largest edition since Rust 2015,” according to [a post on The Rust Blog](https://blog.rust-lang.org/2024/11/27/Rust-2024-public-testing.html).

Most of the changes are subtle, yet significant improvements in the language. [Programmers](https://thenewstack.io/rust-makes-us-better-programmers/) will find the language easier to use. One big change is that creating a direct reference to shared global variables that are open for write access — Rust calls these “mutable statics” — [is now impossible](https://doc.rust-lang.org/nightly/edition-guide/rust-2024/static-mut-references.html). Until now, permitting references has been a hidden source of undefined behavior in the language.

One of the features that I’m most excited about is generators. So far, there’s just been a `gen`
keyword into the language. The work to pull generators into stable Rust can now begin in earnest. (Generators already exist in the so-called “nightly” compiler, which does not provide stability guarantees.)

## Many More People Are Using the Language
One metric that’s useful to track is the number of installs of the official Rust extension for [Visual Studio Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) extension, [rust-analyzer](https://github.com/rust-lang/rust-analyzer), has. The number currently stands at [4.15 million](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer). That’s up from [2.66 million](https://web.archive.org/web/20240110035731/https:/marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) at the start of the year.

Screenshot of the Visual Studio Marketplace page for rust-analyzer, showing 4,148,456 installs of the extension.

## People Shipped Excellent Products
To start, [Tiny Glade](https://store.steampowered.com/app/2198150/Tiny_Glade/) was released. This diorama builder game has proven to be remarkably successful, and the big news from the Rust community was that the game was written entirely in the language.

![](https://cdn.thenewstack.io/media/2024/12/53549d75-picture1.1.jpg)
Screencap from the gameplay trailer from Future Games Show at Gamescom 2023.

On the more serious side, Rust’s advantages are beginning to show themselves with writing software libraries. A Rust implementation of the PNG image file format now [outperforms its traditional C-written counterparts](https://www.reddit.com/r/rust/comments/1ha7uyi/memorysafe_png_decoders_now_vastly_outperform_c/). This is due to the fact that the Rust language provides cross-platform support for SIMD instructions. People writing C libraries need to manually provide implementations for every target architecture.

Image processing is not one-off. [Rustls](https://github.com/rustls/rustls), a Rust-based implementation of [TLS security](https://thenewstack.io/jetstack-secure-promises-to-ease-kubernetes-tls-security/) that underpins HTTPS, is now [faster than BoringSSL and OpenSSL](https://www.memorysafety.org/blog/rustls-performance-outperforms/). The nonprofit that is funding that work, the [Internet Safety Research Group (ISRG)](https://thenewstack.io/rustls-looks-to-provide-a-memory-safe-replacement-for-openssl/) started with [Let’s Encrypt](https://letsencrypt.org/) and is now making strides in improving all aspects of Internet infrastructure. This has included fundamentals like timekeep between computers and now an implementation of a memory-safe, high-performance reverse proxy called [River](https://www.memorysafety.org/blog/river-release/). This seeks to challenge [NGINX](https://www.nginx.com?utm_content=inline+mention)’s dominance in that space.

One thing to look out for in the future is the newly launched [Trifecta Tech Foundation](https://trifectatech.org/). They have a fork of the Rust compiler that can generate an executable that performs compression and decompression that’s [14% faster than what the standard compiler produces](https://trifectatech.org/initiatives/codegen/). Expect these performance improvements to diffuse into the mainline over time. Rust’s blazingly fast and is going to get hotter.

## Confidence In the Language Is Growing
Last March at the [Rust Nation UK](https://www.rustnationuk.com/) conference, [Lars Bergstrom](https://www.linkedin.com/in/lars-a-bergstrom/) revealed that “Rust teams at [Google](https://cloud.google.com/?utm_content=inline+mention) are as productive as ones using [Go](https://thenewstack.io/go/), and more than [twice as productive as teams using C++](https://thenewstack.io/rust-gets-security-wasi-0-2-support-productivity-boost/)”

## The Compiler Is Getting Smarter in Every Release
For me, the 1.79 release was one of the most impactful. Many of my teaching examples, that explained why the borrow checker is needed, stopped working because the borrow checker got smarter. That is, the example code refused to compile — the borrow checker was being overly strict.

## People Are Getting Ambitious
The US Government’s defense research agency [DARPA announced the TRACTOR program](https://thenewstack.io/can-darpas-tractor-pull-c-to-rust-for-memory-safe-overhaul/) to create tools to translate unsafe C to safe Rust. The intent is to rapidly speed up large-scale rewriting systems written in memory unsafe languages, then port them to Rust.

The [Safety-Critical Rust Consortium](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/) was announced in June, aimed at bringing Rust to critical industries. This a major step towards seeing Rust within cars, trains and planes.

In February, Google announced a $1M grant to the [Rust Foundation](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/) to support initiatives to improve [inter-operability of Rust and C++](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/). This grant spawned the wider [Interop Initiative](https://foundation.rust-lang.org/news/google-contributes-1m-to-rust-foundation-to-support-c-rust-interop-initiative/), which has seen the emergence [C++/Rust Interoperability Problem Statement](https://thenewstack.io/the-rust-c-bridge-a-new-path-forward/). Bridging C++ and Rust will mean that it will be much easier for Rust projects to extend existing code bases.

[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) and the Rust Foundation have decided to embark on a project to [formally verify the standard library](https://github.com/model-checking/verify-rust-std). They’ve created an awards scheme for verifying parts of the standard library, with a hope that this will enable new tools and techniques to emerge and eventually the entire standard library’s correctness will be formally verified. The standard library today contains thousands of uses of the `unsafe`
keyword. While the community is confident that those uses are correct, that correctness is not guaranteed. Formal verification will change that.
## The Community Is Getting Stronger
2024 was pleasantly devoid of the “Rust drama” that’s plagued previous years. Indeed, new communications channels emerged.

The Rust Foundation hosted the marquee event for the community, [RustConf](https://rustconf.com/). While this may seem like a fairly insignificant achievement, the conference has been a flashpoint of disagreement and hostility over recent years.

Many conferences and events focused on the language have appeared. Major events are now regularly occurring all over Europe. It’s particularly encouraging to see financial support for areas of disadvantage, such as [Rustaceans Kenya](https://www.linkedin.com/posts/rust-foundation_the-rust-foundation-was-thrilled-to-support-activity-7275198742897573889-7ZC3?utm_source=share&utm_medium=member_desktop).

The year 2024 also saw a revitalization of the podcast scene. There is now a rich collection of podcasts offering differing perspectives, interviews and formats.

For more on the biggest news in [programming languages](https://thenewstack.io/programming-languages/) from 2024, check out Darryl K. Taft’s report, “[Language Wars 2024: Python Leads, Java Maintains, Rust Rises.](https://thenewstack.io/language-wars-2024-python-leads-java-maintains-rust-rises/)“

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)