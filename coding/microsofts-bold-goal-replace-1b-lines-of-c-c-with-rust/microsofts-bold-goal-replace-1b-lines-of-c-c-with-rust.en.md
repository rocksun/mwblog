[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) is hiring top-level engineers to help to get rid of [C and C++](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/) in its largest codebases and replace that code with [Rust](https://thenewstack.io/rust-programming-language-guide/).

In a [job listing post on LinkedIn](https://www.linkedin.com/posts/galenh_principal-software-engineer-coreai-microsoft-activity-7407863239289729024-WTzf/), [Galen Hunt](https://www.linkedin.com/in/galenh/), distinguished engineer at Microsoft, wrote: “My goal is to eliminate every line of C and C++ from Microsoft by 2030.”

In responding to questions from commenters about why Rust and not [another (more familiar) language like C#](https://thenewstack.io/microsoft-we-are-not-abandoning-c-for-rust/), Hunt mentioned memory safety and concurrence.

“Two reasons for Rust over C#: 1) C# is memory safe, but not concurrent safe, 2) performance (no GC). Just at Microsoft, we have about a billion lines of code that I want to [be] rewritten,” he wrote. “Across the industry, it is probably 20-40BLoC that needs to be written.”

## How Will They Do It?

Hunt said Microsoft will combine AI and algorithms to rewrite Microsoft’s largest codebases.

“Our North Star is ‘1 engineer, 1 month, 1 million lines of code,’” he wrote.

Hunt described the process as “previously unimaginable.” However, the company has built a powerful code processing infrastructure to handle it.

“Our algorithmic infrastructure creates a scalable graph over source code at scale,” he wrote. “Our AI processing infrastructure then enables us to apply AI agents, guided by algorithms, to make code modifications at scale.”

Moreover, this infrastructure is already operating at scale on problems such as [code understanding](https://research.google/pubs/using-an-llm-to-help-with-code-understanding/).

## Joining the Team

Hunt emphasized the importance of a diversity of skills on his team.

“We take on bold risks,” he wrote.

“Our team is driven by a growth mindset. We are a diverse team with a wide range of skills and perspectives,” Hunt wrote. “We have learned that our diversity and growth mindset is critical to success in the rapidly changing world of AI-based tools.”

Hunt is hiring a [Principal Software Engineer](https://careerhub.microsoft.com/careers/job?domain=microsoft.com&pid=1970393556639051) to help Microsoft evolve and augment its infrastructure to enable translating Microsoft’s largest C and C++ systems to Rust.

“A critical requirement for this role is experience building production-quality systems-level code in Rust — preferably at least 3 years of experience writing systems-level code in Rust,” Hunt said. “Compiler, database or OS implementation experience is highly desired. While compiler implementation experience is not required to apply, the willingness to acquire that experience in our team is required.”

Hunt’s team is part of the Future of Scalable Software Engineering group in the EngHorizons organization in [Microsoft CoreAI](https://blogs.microsoft.com/blog/2025/01/13/introducing-core-ai-platform-and-tools/), he wrote.

“Our mission is to build capabilities to allow Microsoft and our customers to eliminate technical debt at scale,” he said.

## The Gradual Move To Rust

Microsoft has been signaling its gradual move to Rust for some time now.

As far back as 2022, [Mark Russinovich](https://www.linkedin.com/in/markrussinovich/), Microsoft [Azure](https://thenewstack.io/microsoft-linux-is-the-top-operating-system-on-azure-today/) CTO, posted on X, formerly known as Twitter, that “it’s time to halt starting any new projects in C/C++ and use Rust” for scenarios where a non-GC language is required.

In addition, at the [RustConf 2025](https://rustconf.com/) conference in September, Russinovich spoke about how Rust was helping Microsoft fix security issues with Windows, among other things.

C and C++ let you write code that looks fine but crashes spectacularly or, worse, gets hacked, he indicated. Microsoft’s own kernel has been leaking privilege escalation bugs monthly through Win32k.sys, the part that handles graphics and windows, Russinovich said.

During his keynote at RustConf 2025, “From Blue Screens to Orange Crabs: Microsoft’s Rusty Revolution,” Russinovich described the situation as being like “an underground oil repository that is leaking oil up a few drops at a time, just consistently.”

So the company started rewriting chunks in Rust. Not the whole thing, just pieces. If you dig into your Windows System32 folder right now, you’ll find a file called win32kbase\_rs.sys. That’s Rust code running in your kernel.

Here’s the thing that actually matters: When a security researcher found a bug in the new Rust version, it crashed the system instead of letting an attacker take over, Russinovich said.

“This we view as a success,” he said. “This code written in [C++](https://thenewstack.io/introduction-to-c-programming-language/), this bug would have actually resulted in a potential elevation of privilege, as opposed to a blue screen crash that’s very deterministic and can’t be exploited.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)