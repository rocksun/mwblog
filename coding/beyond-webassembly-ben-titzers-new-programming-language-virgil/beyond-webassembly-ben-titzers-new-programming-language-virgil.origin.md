# Beyond WebAssembly: Ben Titzer’s New Programming Language, Virgil
![Featued image for: Beyond WebAssembly: Ben Titzer’s New Programming Language, Virgil](https://cdn.thenewstack.io/media/2024/06/2c344377-microarch-1024x683.png)
WebAssembly co-founder
[Ben Titzer](https://www.linkedin.com/in/ben-l-titzer-6b78584/) keeps thinking big…
He’s currently the director of the
[WebAssembly Research Center](https://www.cs.cmu.edu/wrc/) at Carnegie Mellon University (where Titzer is also a [principal researcher](https://s3d.cmu.edu/people/core-faculty/titzer-ben.html) in the school’s Software and Societal Systems department). The center focuses on advancing WebAssembly research in academia, teaching and training students, and broadly supporting the uptake of WebAssembly in new domains.
But Titzer also continues the long-running work on his home-grown programming language
[Virgil](https://github.com/titzer/virgil) — and a special [WebAssembly](https://thenewstack.io/webassembly-adoption-its-complicated-says-cncf-survey/)-running virtual machine named [Wizard](https://github.com/titzer/wizard-engine) that just might have a role in changing the way we run software.
Last month Titzer discussed his work in
[a special appearance](https://youtu.be/QEB6-V7iTqY?si=84JJU2fEcfYn1JId) on a new YouTube channel called the [Microarch Club](https://microarch.club/), for a long interview with [Dan Magnum](https://www.linkedin.com/in/danielmangum/), lead cloud engineer at IoT platform [Golioth](https://golioth.io/).
But it’s been a lifelong interest. During the interview Titzer revealed that even as a high school student, he was
[writing an interpreter in x86 assembly code](https://thenewstack.io/its-no-longer-about-how-you-write-code-but-how-you-operate-it/) for some bytecode “that I made up.”
And by the time he was entering graduate school, Titzer already knew he wanted to write a new programming language called Virgil…
Fitting High-Level Languages on Microcontrollers
[@TitzerBL]describes optimization techniques that can be used to bring high-level language features to microntrollers, such as reference compression, romization, and reachable members analysis. [pic.twitter.com/J6YjcWVA3d]
— Microarch Club (@MicroarchClub)
[May 24, 2024]
## Virgil
Virgil’s repository at GitHub describes it as a language “designed for building lightweight high-performance systems” (with a compiler that produces fast native executables, WebAssembly modules, or JARs for the JVM). “I hope to make Virgil a great systems programming language,” Titzer told me in an email interview, “that strips away legacy cruft and yet has great features for writing robust systems code… things like virtual machines, compilers, kernels, network stacks, etc.
“Rust has a lot of excitement but it can’t do the kinds of things Virgil does.”
Titzer delved into more details on the podcast. As a language for writing at the lowest level, Virgil “needs to have features that allow to do things that are ‘icky’ and ‘dangerous’, from the concept of a pure programming-languages person. Like if you’re really deep into type safety and type theory, then you might be put off by the fact that you can use a pointer to the stack, and walk the stack that way. Or that you can memory-map something, and you have a pointer to that. Or that you can call the kernel. So that sets it apart.”
And there’s one more interesting feature. “I added a feature where you could basically just take machine code, and be like, ‘This is a function now. This is a Virgil function — and it has the ABI of Virgil.”
Titzer quickly acknowledged on the podcast that it’s “absolutely unabashedly an unsafe operation,” but “you need to be able to do that, because there are instructions that I’m never going to convince my compiler to emit, like
[POPCNT](https://www.felixcloutier.com/x86/popcnt) or all the [SIMD instructions](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data)…”
It’s an exciting project. “C’s reign is not absolute,” Titzer once
[wrote](https://news.ycombinator.com/item?id=30705383) in a 2022 comment on Hacker News. “Virgil compiles to tiny native binaries and runs in user space on three different platforms without a lick of [C code](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/), and runs on Wasm and the JVM to boot. I’ve invested 12+ years of my life to bootstrap it from nothing just to show it can be done and that we can at least have a completely different userspace environment.” ![Virgil programming language example code (screenshot from UCLA page)](https://cdn.thenewstack.io/media/2024/05/df0b6345-virgil-programming-language-example-code-screenshot-from-ucla-page.png)
The type of a variable is placed after its declaration statement. Screenshot from a page
[at UCLA](http://compilers.cs.ucla.edu/virgil/overview.html) (where Titzer earned his Masters and PhD degrees)
On the podcast, Titzer added that after more than a decade of work, “It’s definitely been the kind of thing that I’ve carried on the longest, and invested the most over time… lots of nights and weekends, working on that.” And he called Virgil “unabashedly a systems programming language… I mean, this is the kind of thing that you would write a virtual machine in.”
Then he joked that, “I’m doing that now, because I can’t
*stop* myself from writing virtual machines, like an addiction that I have…”
## Wizard
When Titzer was asked on the podcast if Virgil is being used in any applications, he said he was its biggest fan. “There’s like a parser combinator library out there, there’s like socket libraries out there, and a few things like that. It’s mostly been me building systems with it — you know, like the lone maniac in the cathedral organ.
*[He laughs.]* With the candlelight and the cape.
“But, so, I built Wizard, which is a research engine that runs WebAssembly, and is all written in 100% Virgil — there’s no C code.”
The importance of Wizard came up when Titzer was asked what his goal was with Virgil. Is it just to further research, or is he looking for more general adoption?
**Titzer:** I do like the idea of more adoption, but I definitely don’t want to be beholden to users that have demands. *[They laugh.]* **Magnum**: That does complicate things, doesn’t it? **Titzer:** ‘So please use it, but don’t ask for anything…’ I mean, that’s obviously not a tenable position. I do, like, have issues and respond to issues and things like that. But I’m definitely not looking for success. I’m not looking to compete with Rust. I’m not looking to compete with Zig. I’m not looking to make people use it for their next production system. At the same time, I do enjoy having people use it and do cool things with it, contribute back… My goal is WebAssembly research. And so everything I do at the language level has to be narrowly focused on making Wizard better, just because I don’t have time to constantly cycle on language design issues.
Wizard’s repository calls their engine/virtual machine “the first Wasm engine to do fast in-place interpretation of Wasm bytecode.” (“For quick turnaround in testing and debugging, programs can also be run directly on a built-in interpreter.”)
But Titzer elaborated in our email interview, “My primary goal for Wizard is to build a complete enough and fast-enough flexible Wasm engine for research. Research is a bit different than production, so being simple, flexible, approachable, having good introspection and debugging tools, and less legacy code all help that goal.
“I’m not looking to compete with production engines except in dynamic program analysis features. For example, a reasonable use case is to take a program from production, record a trace, and then analyze the trace in Wizard using its more complete toolset.”
## ‘We Must Do This’
At the end of the podcast, Titzer was asked about his vision for WebAssembly’s future — if he saw it growing and becoming a more fundamental part of our computing stack.
“Definitely…” Titzer said. “I think that WebAssembly should be the universal software substrate — it should be the thing that’s at the bottom of software, in the sense that every language compiles to it. And if you’re able to run it, then you’re able to run everything…
“So that means that — it needs to have a few more features, but it also needs to have more ecosystem penetration and more tooling and stuff like that.”
Yes.
As fun as machine code can be, let’s make it (mostly) disappear below a universal portable software abstraction layer.
[https://t.co/4XUuFC9S2g]
— Ben L. Titzer (@TitzerBL)
[May 14, 2024]
Among other things, this would make it easy to
*analyze* every program. “There’s kind of this security model built into it — like you have a handle over what a program is doing, you have clear input and output through the import/export mechanism. I think it has so many different dimensions of potential that I think — we must do this.”
“Obviously CPUs are not going away,” Titzer clarified, adding that “No Instruction Set Architecture that we have now is going to go away… and there’ll be even more CPUs in the future.” But when you have a software substrate, “it makes it very clear what the application wants. And everything below it, you can swap out. That’s the whole point of virtualization, right?”
I asked Titzer what signs he’s seeing that we’re
[headed to a world where WebAssembly](https://thenewstack.io/the-promise-of-webassembly-heads-to-ruby/) might become “software’s final substrate.
“I see a lot of interest in using Wasm in domains that are neither web nor serverless,” Titzer replied. “As a portable, fast, and well-specified bytecode with many languages targeting it, it has the potential of making a domain (e.g. embedded systems, cyber-physical systems, a plugin system for a videogame) programmable in ways it wasn’t before.
“The lightweight sandboxing property is an outgrowth of well-specified encapsulation, and that allows running untrusted Wasm code in all kinds of new ways.”
Then I asked if his WebAssembly-running engine Wizard had a role in bringing us to this world… Titzer agreed that it “helps make this possible by pushing the limits” in the engine space, calling Wizard “a research and incubation platform for engine-based tools that are harder to explore in a production engine…”
Specifically, “fast in-place interpretation makes all of the dynamic analysis and debugging tooling easy to get working. For production engines, it means faster startup and lower memory consumption, so settings where code is dynamically loaded can scale to bigger modules and have quicker response time; that unlocks new possibilities for using Wasm for short, ephemeral computations where big
[ahead-of-time compilation](https://en.wikipedia.org/wiki/Ahead-of-time_compilation) costs would make that prohibitively expensive.”
Towards the end of the podcast, Titzer said he was enjoying the long-term views of academia, working with all the bright people at CMU, and contributing to “the forefront of human knowledge. That’s kind of the point of research…”
And there’s one more consideration. “The next generation of students? They need to have instruction and, you know, be shown the ways… Otherwise, they’ll end up working on — LLMs or something.”
*[He laughs]* “They should work on VMs…. They should work on machine code and optimizations and compilers and stuff! I want to get them excited about it…”
I asked Titzer if he’s seen Wizard being used in educational contexts — and he said he will be using it himself next semester in a course he’s teaching about virtual machines.
And — always looking toward the future — Titzer added that “I hope to package it a bit more to make that possible to do in other courses by other instructors…”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)