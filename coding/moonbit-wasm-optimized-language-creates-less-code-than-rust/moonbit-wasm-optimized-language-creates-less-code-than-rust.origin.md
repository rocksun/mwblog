# MoonBit: Wasm-Optimized Language Creates Less Code Than Rust
![Featued image for: MoonBit: Wasm-Optimized Language Creates Less Code Than Rust](https://cdn.thenewstack.io/media/2024/06/6c29d018-moonbitlang-1024x573.png)
WebAssembly’s original promise was that many languages could be compiled to it and then run in the browser or other environments. The problem, however, is that existing languages such as Java, Go and even Rust generate a huge amount of WebAssembly code when compiled, even when they’re just printing “Hello World,” said IDEA scientist and language developer [Hongbo Zhang](https://github.com/bobzhang).

“The advantage of WebAssembly is not delivered,” he said. “We say WebAssembly is safe and fast, but when [Go](https://thenewstack.io/golang-variables-and-data-types-an-introduction/) is compiled to WebAssembly, it generates a very large amount of WebAssembly code, and it’s not fast anymore because the language semantics don’t match very well with the Golang,” Zhang said. “So we think there’s a opportunity, a big opportunity, to have a language that is designed for the WebAssembly semantics.”

That’s why Zhang created [MoonBit](https://www.moonbitlang.com/), a new end-to-end [open source](https://www.moonbitlang.com/blog/moonbitlang-core-opensource#:~:text=MoonBit%20is%20a%20Rust%2Dlike,Core%2C%20under%20Apache%20License%202.0.) [programming language optimized for WebAssembly](https://github.com/moonbitlang) and designed for cloud and edge computing, and for frontend applications as well.

“Why we have a very high priority for WebAssembly is because we think WebAssembly has a very great potential. It’s the new instruction set, and it’s cross platform — it’s safe, it’s fast,” he said.

Zhang is not new to creating languages. He was a core contributor to the OCaml programming language, which was popular among academics. He also worked with ReScript and Flow, Meta’s in-house programming language. While at Bloomberg, he created the [BuckleScript compiler](https://www.bloomberg.com/company/press/open-source-at-bloomberg-introducing-bucklescript/), which compiled OCaml to [JavaScript](https://thenewstack.io/javascript-framework-maintainers-on-unification-potential/). [Editor’s Note: BuckleScript was renamed as ReScript compiler.]

MoonBit is [written to take advantage of WebAssembly](https://thenewstack.io/webassembly/using-web-assembly-written-in-rust-on-the-server-side/) in ways an existing language can’t, he explained.

“You cannot change the Golang semantics to adapt to WebAssembly,” he said. “If you need to make a new language, then we can take advantage of the fact, because the WebAssembly standard is already finalized. So you can make it very fast, generate very small WebAssembly code, and we can gain a very good advantage.”

## Moonbit Draws Inspiration from Rust, Go
That places it in a similar category with the language [Grain, which is also designed to compile to Wasm](https://thenewstack.io/meet-grain-the-high-level-language-optimized-for-webassembly/). Interestingly, Grain’s creators cited OCaml as their inspiration. But the difference between the two is that Grain is Wasm-only, whereas MoonBit takes a multi-backend language approach and is optimized for other backends — here meaning server-side development — [including JavaScript](https://www.moonbitlang.com/blog/js-support). It claims a nearly [eightfold performance advantage over Json5 on the JavaScript backend](https://www.moonbitlang.com/blog/js-support). MoonBit is also exploring the possibility of an [AI-native language toolchain](https://www.moonbitlang.com/blog/moonbit-ai) to develop[ AI applications](https://thenewstack.io/5-best-practices-for-building-reliable-genai-apps/).

“Actually we support WebAssembly, JavaScript and native backend, but we have very high priority for WebAssembly,” Zhang said. “If people care about the WebAssembly platform, they already know WebAssembly, and they want to have some very optimal solution for this platform, then MoonBit may be a very good choice, because we generate a code which is performance-wise comparable to Rust, and it also generates even smaller Wasm code than Rust.”

In many ways, MoonBit takes inspiration from Rust, he said. It has pattern matching, static types and type inference, for example. It’s a strongly typed language, like Rust, [Kotlin](https://thenewstack.io/get-started-using-kotlin-multiplatform-with-a-network-listener-project/) and [Java](https://thenewstack.io/remotely-record-java-logs-from-containers/), he added, which means it enforces strict rules about data types.

“We take the good parts of Rust, and we try to make it easy to learn,” he said.

He described it as the best of Rust without some of its pain points.

“Also another advantage is we have very fast compilation, so one pain point of Rust, it takes a very long time to compile,” he said. “We can compile the whole code in a very, very fast time … like one or two orders of magnitude faster than the Rust compilation.”

Where it diverges from Rust is that it soon will ship with a garbage collector, which uses automatic reference counting (ARC). That’s similar to Swift’s approach to garbage collecting. This allows it to do automatic memory management.

MoonBit also draws inspiration in its package system and philosophy from Go, he said.

“Go has a philosophy [of] less is more, and we think this is quite important,” Zhang said. “You have to make the language itself cohesive. We don’t want to continue adding [to] the syntax.”

## IDE Already Available
It’s also different from Rust in that it has fault tolerant type systems and design movements, he said.

“The reason we decided to have a fault tolerant type system is because we want to have the IDE share the same code base with a compiler,” he said. “So for the traditional compiler, when you see a first error … the compiler will stop there and then. But for the developer, I still want to have an IDE to tell me [that the] other information [is] right, even though the program is incorrect. We have the fault tolerant type system, fault tolerant to the parser, so even when the problem is in a very bad state, the type checker can still … give you some information to guide you to do the auto completion.”

When the IDE does not share the same code base as the compiler, it can lead to inconsistent results, he added.

The IDE is another reason that developers may find MoonBit attractive for Wasm. It’s unusual for new languages to start out with an IDE. Usually, that takes years, according to Zhang.

“Because I had plenty of experience working with language tools, I think one big thing to get a language to be usable and enjoyable by the developer is they have the IDE [that’s] very fast, very reliable,” he said. “To make it happen, I designed the whole language type system, to break it very fast, to type check, [and] after the type checking, then the IDE will work from there.”

The compiler only checks the modified paths, so that creates a very fast IDE edit cycle, he added.

## Use Cases for the Moonbit Language
Developers who care about performance may want to give MoonBit a chance, Zhang proposed.

“This is the first choice [if] they want to use WebAssembly for the frontend in the browser or for the serverless coding,” he said. “They may care about the WebAssembly and then a quite important usage is also compiled to JavaScript. Not only with compiling to JavaScript, we also compile to very performant JavaScript code; all the generated JavaScript code is even faster than the handwritten JavaScript.”

MoonBit can run in the cloud or on the edge, he said. It can be used specifically for [Cloudflare Workers](https://thenewstack.io/cloudflare-raises-1-25-billion-for-startups-using-its-workers-platform/), a platform that supports running serverless code at the edge of Cloudflare’s global network because, “the runtime is essentially built-in,” he said. “You can use it for edge computing and serverless computing as well.”

Zhang also has experience with the frontend thanks to his work on ReScript, which is for JavaScript developers.

“For the JavaScript people, we have several advantages,” he said. “One, it has a very strong, solid IDE, and gives you the best performance.”

It also compiles the JavaScript, he added, using a “very fancy optimizer to make the [JavaScript code](https://thenewstack.io/solid-js-creator-outlines-options-to-reduce-javascript-code/) faster.” For example, the company has benchmarked a JSON5 parser, which was written in JavaScript, and migrated to MoonBit the same code base, same algorithm. In that benchmark, MoonBit performed approximately seven times faster than handwritten JavaScript code, he said.

“When people care about WebAssembly backend, they will probably pick up MoonBit as their ideal language choice,” Zhang said. “That’s why the story of MoonBit is from the start WebAssembly, but we have a very ambitious goal, so we’re not only optimized for WebAssembly, also for other backends.”

To explore the language, check out [MoonBit’s online sandbox](https://try.moonbitlang.com/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)