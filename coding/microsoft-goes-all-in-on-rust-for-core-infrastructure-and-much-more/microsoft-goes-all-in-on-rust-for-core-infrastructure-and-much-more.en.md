I recently wrote about [Mark Russinovich](https://www.linkedin.com/in/markrussinovich), Microsoft’s Azure CTO, talking about how [Rust code is shipping in Windows](https://thenewstack.io/microsofts-rust-bet-from-blue-screens-to-safer-code/), but I didn’t cover the whole of what he said at [RustConf 2025](https://rustconf.com/) earlier this month in Seattle. In fact, I didn’t even cover the half.

While I wrote primarily about Microsoft rewriting Windows components in [Rust](https://thenewstack.io/rust-programming-language-guide/), that was just the opening act for Russinovich in his keynote at the event. He spent much of his talk showing off projects that reveal how far down the Rust rabbit hole Microsoft has actually gone.

## Virtual Machines in a Millisecond

His [Hyperlight](https://opensource.microsoft.com/blog/2024/11/07/introducing-hyperlight-virtual-machine-based-security-for-functions-at-scale/) discussion was genuinely impressive. Russinovich showed a system that spins up virtual machines (VMs) in 1.5 milliseconds. Not [containers](https://thenewstack.io/introduction-to-containers/) — actual VMs with proper isolation boundaries.

“Look, we don’t want a full-blown hypervisor with a full-blown operating system just to run some user code we don’t trust,” he said, pulling up slides showing the architecture. “This is way overkill for running a tiny function.”

[Hyperlight started](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/) as a [C#](https://thenewstack.io/microsoft-we-are-not-abandoning-c-for-rust/) prototype but got rewritten in Rust when performance became critical. It’s now handling real traffic in [Azure Front Door](https://azure.microsoft.com/en-us/products/frontdoor), where customers can deploy edge functions that process network requests. The use case makes sense — you need strong isolation for untrusted code, but [traditional VMs](https://thenewstack.io/why-chainguard-is-doubling-down-on-virtual-machines-in-a-container-world/) are too slow for functions that might run thousands of times per second.

What’s impressive about Hyperlight is how minimal it is. No guest OS, just a small runtime that provides APIs to the code running inside. It supports [WebAssembly](https://thenewstack.io/webassembly/) and native binaries, but either way, the attack surface is tiny compared to a full VM stack.

In addition, it is all open source, Russinovich said.

## Useful Build Integration

Microsoft also tackled the issue of how to use Rust in existing projects without rewriting everything.

Their answer is a [Cargo](https://doc.rust-lang.org/cargo/) plugin for [MSBuild](https://www.incredibuild.com/integrations/msbuild) that lets you drop Rust modules into [C++](https://thenewstack.io/introduction-to-c-programming-language/) and C# codebases. Russinovich admitted this was born from necessity: “We can’t just tell teams to throw away millions of lines of working code.”

The plugin is straightforward: You write your Rust code, Cargo builds it and MSBuild treats it like any other dependency. But getting the linking and [ABI](https://en.wikipedia.org/wiki/Application_binary_interface) details right took serious work. Microsoft also open sourced this, which suggests it thinks other companies will face the same problem.

This feels like the kind of practical tooling that could move the needle on [Rust adoption](https://thenewstack.io/survey-memory-safe-rust-gains-45-of-enterprise-development/). Most companies are not going to rewrite entire applications, but they might replace security-critical modules if it’s easy enough.

## Guidelines That Don’t Suck

Russinovich said Microsoft also published its “[Pragmatic Rust Guidelines](https://microsoft.github.io/rust-guidelines/)” — essentially its internal playbook for how to write Rust code at enterprise scale. He was straight up about this: “If you’re an experienced Rust developer, none of this will surprise you. It’s really for people who are new.”

What is interesting is that they made two versions — one for humans and a condensed version specifically formatted for AI coding assistants. “You can drop this into your Copilot instructions and the AI will actually follow it,” Russinovich noted.

The guidelines cover things like error handling patterns, Foreign Function Interface (FFI) best practices and when to use different async runtimes. Nothing revolutionary, but having official Microsoft recommendations could help teams avoid common pitfalls.

The AI-optimized version is a smart touch, as a lot of Rust code is getting written with AI assistance these days. Having guidelines that work well with those tools shows Microsoft is thinking practically about how development happens.

## Rewriting the Crown Jewels

Then Russinovich explained that Microsoft is in the process of rewriting its [SymCrypt](https://github.com/microsoft/SymCrypt) cryptographic library in Rust.

SymCrypt is not just another library. It’s Microsoft’s cryptographic core — the code that handles RSA, elliptic curves and every other piece of crypto across Windows, Azure and Office. “This is literally the most sensitive code we have,” Russinovich said.

But it’s not just doing a straight port. [Microsoft Research has formal verification tools for Rust](https://www.microsoft.com/en-us/research/blog/rewriting-symcrypt-in-rust-to-modernize-microsofts-cryptographic-library/), so it’s proving the mathematical properties of the new crypto code. The verified Rust can even be transpiled back to C++ for easier integration with existing systems.

New algorithms like [ML-KEM](https://csrc.nist.gov/pubs/fips/203/final) (the post-quantum key exchange standard) are being written in Rust from scratch. This suggests Microsoft thinks Rust will be its crypto language going forward, not just for new projects, but for its most critical existing code.

The fact that it’s willing to touch SymCrypt at all shows how confident it has become in Rust tooling and developer expertise.

## AI-Powered Code Translation

The most futuristic part of the talk involved [Microsoft’s GraphRAG technology](https://microsoft.github.io/graphrag/) applied to code translation. Russinovich demoed a tool that automatically converts Python applications to Rust while preserving structure and functionality.

He showed a simple side-scrolling game written in [Python](https://thenewstack.io/what-is-python/): three files, maybe 200 lines total. The translation tool analyzed the code structure, understood the relationships between modules and generated equivalent Rust code that compiled and ran identically.

“Normal LLM [large language model] translation gives you garbage,” Russinovich said, showing broken code from a standard ChatGPT translation. “But if you give the AI a semantic understanding of the whole codebase, it can reason about what the code actually does.”

The demo worked, but it is unclear how well this scales to larger, more complex codebases. A three-file Python game is one thing; a million-line C++ application is another entirely.

Still, if Microsoft can make automated translation reliable, it could solve the biggest barrier to Rust adoption. Most companies have enormous existing codebases that they cannot afford to rewrite manually.

## The Reality Check

However, Russinovich was surprisingly candid about Rust’s rough edges. Microsoft’s internal surveys show developers still struggle with interop, async debugging and dynamic linking, he said. The learning curve for C++ developers is genuinely difficult.

“It’s a shock when you’re coming from C++,” he admitted. “Your brain has to completely rewire how you think about memory and ownership.”

But even developers who complain about Rust don’t want to go back to C++, he said. After a few months, they adapt and become advocates. Performance is consistently better. Whole categories of bugs just disappear.

Microsoft has put serious effort into tooling improvements — [Visual Studio Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) integration, debugger support, better error messages. They also have found that AI coding assistants help a lot with Rust’s learning curve.

## The Bigger Picture

Russinovich’s presentation revealed the scope of Microsoft’s bet on Rust. It’s not just using it for new projects — it’s systematically replacing C++ in its most critical systems. Win32k.sys, Hyper-V, SymCrypt, Azure Data Explorer. These are not experiments; they are production systems handling massive scale.

The driver framework extends this beyond Microsoft’s own code. If hardware vendors start writing Rust drivers, Windows gets more secure without Microsoft doing all the work.

Combined with AI translation tools, this could create a tipping point. Right now, Rust adoption is limited by the effort required to get started. But if you can automatically translate existing code and easily integrate Rust modules into existing projects, the barriers start disappearing.

Whether this truly happens depends on execution. Automated translation needs to work reliably on complex codebases. Build integration needs to be seamless. Safe abstractions for driver development need to be complete and well-documented.

But Microsoft seems committed to making it work. As Russinovich put it: “Rust is permeating our core infrastructure. This is just going to accelerate.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)