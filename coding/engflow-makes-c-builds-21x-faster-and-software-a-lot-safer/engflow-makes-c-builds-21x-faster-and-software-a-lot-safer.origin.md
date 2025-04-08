# EngFlow Makes C++ Builds 21x Faster and Software a Lot Safer
![Featued image for: EngFlow Makes C++ Builds 21x Faster and Software a Lot Safer](https://cdn.thenewstack.io/media/2025/04/b0fb4788-skyler-h-xalujbpfbsi-unsplash-1024x575.jpg)
[EngFlow](https://www.engflow.com/), a build acceleration company created by former [Google](https://cloud.google.com/?utm_content=inline+mention) engineers behind the open source [Bazel](https://bazel.build/) project for remote build execution for developers, recently launched the public beta of [CMake RE](https://www.engflow.com/product/cmakere), a remote execution service for users of the [CMake](https://cmake.org/) software [build system](https://thenewstack.io/engflow-bazel-and-more-for-faster-builds/).
EngFlow also recently acquired a company called [tipi.build](https://tipi.build/) to bolster its build acceleration product line.

## Tipi
tipi.build provides fast remote [C](https://thenewstack.io/the-obfuscated-c-code-competition-returns/), [C++](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/), and [Rust](https://thenewstack.io/rust-programming-language-guide/) builds with caching technology based on CMake and [Git](https://thenewstack.io/need-to-know-git-start-here/). Tipi empowers developers to test and build cross-platform instantly, and add cloud CPU cores when needed, bringing continuous integration to developers’ fingertips.

Based in Zürich, Switzerland, Tipi was founded by CMake enthusiasts and C++ developers who want to increase developer flexibility without sacrificing performance or safety. Tipi products are used to develop critical software for the Internet of Things (IoT), financial trading, medical devices, automotive sectors, and more.

Engflow and Tipi previously collaborated on CMake remote build execution services, and the acquisition provides EngFlow customers with deeper expertise in build system modernization and caching.

## CMake RE and HermeticFetchContent
The beta of CMake RE offers remote execution services for CMake software build system users. It also provides build acceleration, caching, and remote execution for C and C++ developers. In addition, its features include local hermetic CMake builds, build and dependency caching, and cloud build distribution.

The new open source project, [HermeticFetchContent](https://tipi.build/blog/20250225-hfc-launch), brings more modern build system features to C and C++ developers. It addresses software safety and continuous delivery challenges and provides dependency management and provenance mechanisms, including [software bill of materials (SBOMs)](https://thenewstack.io/a-good-sbom-is-hard-to-find/).

When combined with CMake RE, HermeticFetchContent speeds up build times significantly — up to [21x faster in some cases](https://github.com/tipi-build/hfc-bench/blob/main/README.md).

“We teamed up with tipi.build, creators of CMake RE and HermeticFetchContent, to optimize our CMake build targeting hundreds of configurations,” said [Jody Hagins](https://cplusplusonline.com/), a C++ engineer in high-frequency trading and an ISO C++ Standards Committee Member, in a statement. “Their approach of source-based, cached builds has not only accelerated our build but also improved safety by allowing us to enable sanitizers across our dependency chain.”

## Codebases Growing Exponentially, as Is C++ Development
These tools are becoming increasingly important as codebases grow larger, especially with AI exponentially adding lines of code, [Helen Altshuler](https://www.linkedin.com/in/helen-altshuler/), CEO at EngFlow, told The New Stack. The technology helps reduce build times from hours to minutes and supports the C and C++ developer community, which is estimated at over 7 million developers.

According to [Damien Buhl](https://www.linkedin.com/in/damien-buhl/), co-founder of Tipi, C++ development is still growing, especially in finance, embedded systems, IoT, and AI. Companies like Google are moving Python codebases to C++ for efficiency, reportedly because 7x fewer servers are needed.

“All the AI companies are using C++ because… If you build the software in C++, you have seven times less servers needed than if you build it with PHP or Python,” Buhl said.

The combined platform (CMake RE) offers a two-layer remote execution system:

- Layer 1 (tipi.build): Local build acceleration with limitations based on machine size.
- Layer 2 (EngFlow): Distributed build system that can scale across thousands of cores.
Together they create a “supercomputer” experience that’s more cost-effective than using large individual machines.

“We’re turning 20,000 cores, or 40,000 cores that are distributed across many computers into one, essentially,” Altshuler told The New Stack. “So, from the customer using remote execution, they have this cluster, so essentially, they have a supercomputer.”

Indeed, AI is already creating a lot of code. AI is also creating a lot of bad code “that slows down significantly. We spoke with some of our customers that now have queues of builds piling up,” she said.

“In the age of even more code and even more test iterations, especially if it’s bad code… it’s important to have the most robust and scalable systems to process that build and test workflow,” Altshuler added.

## Based on Bazel
Google’s Bazel project emerged in recent years as one of the best build systems for today’s complex polyglot codebases and is inherently designed to overcome these issues. Yet, EngFlow’s Bazel cluster technology offers enhanced build system performance for large development teams.

Moreover, the combination of both companies and their respective technologies — tipi.build and EngFlow — brings all the benefits of Bazel remote execution and caching to CMake without requiring disruptive build system migrations, Buhl said.

## Meeting Safety Requirements
Meanwhile, HermeticFetchContent addresses software safety and continuous delivery challenges to meet regulatory requirements.

Engineering platform teams using C and C++ are facing new challenges when it comes to safe and continuous software delivery, particularly as the Federal government calls for [eliminating C and C++ from critical systems](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/).

Compiling and automated testing for Rust, C, and C++ code is compute-intensive, and common codebases can take many hours to compile, generating very large build trees, Buhl noted. The issues are exacerbated when teams add static analyzers and sanitizer instrumentation to their builds and tests to handle safety requirements recently defined by the NSA, the White House, and the European Union.

HermeticFetchContent enables developers to run memory safety checks (sanitizers) on entire dependency chains, Buhl said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)