With the U.S. government and other institutions calling for the [use of memory-safe programming languages](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) in critical systems, [Jule](https://jule.dev/), a nascent, open source alternative to [C/C++](https://thenewstack.io/microsofts-bold-goal-replace-1b-lines-of-c-c-with-rust/) has emerged.

The Jule homepage describes Jule as a “simple and safe programming language with built-in concurrency, first-class C/C++ interoperability and powerful compile-time capabilities.”

Although the Jule project began in 2022 and is still in beta, its creation demonstrates that developers are looking at systems programming languages other than [C and C++](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/), which are not memory safe, and at [Go](https://thenewstack.io/introduction-to-go-programming-language/) and [Rust](https://thenewstack.io/rust-programming-language-guide/), which are.

Indeed, in 2024, the U.S. [Cybersecurity and Infrastructure Security Agency](https://thenewstack.io/who-should-be-responsible-for-software-security/) and the FBI issued stark warnings about basic security failures that continue to plague critical infrastructure.

In a joint report, the agencies warned that software manufacturers had until January 1, 2026, to create memory safety roadmaps.

“For existing products that are written in memory-unsafe languages, not having a published memory safety roadmap by Jan. 1, 2026, is dangerous and significantly elevates risk to national security, national economic security, and national public health and safety,” the report states.

Enter Jule, a statically typed, compiled, general-purpose systems programming language focused on simplicity, performance, and safety. It is designed to deliver native-level performance, predictable behavior, and practical safety, without sacrificing clarity or developer productivity, the Jule manual says. Jule aims to provide the productivity of Go with the performance of C.

## Jule safety

Jule is heavily influenced by both Go and Rust, mostly Go. The Jule manual explains that while Rust is widely known for its strict and comprehensive safety guarantees, it also effectively addresses safety concerns. Yet Jule takes a less strict, more flexible safety model, closer to Go’s philosophy. And like Go, Jule performs runtime checks for boundary violations and nil dereferencing, ensuring baseline memory safety.

Meanwhile, Jule introduces additional compile-time safety analysis, and it performs static checks to catch common classes of errors early.

However, a key distinction is that Jule adopts an [immutable-by-default](https://users.rust-lang.org/t/is-immutability-by-default-worth-the-hassle/83668) model, similar to Rust. Variables are immutable unless explicitly declared mutable. Under Safe Jule, this rule is strictly enforced: immutable memory cannot be mutated, the Jule manual states.

## C/C++ interoperability

Jule was designed to be interoperable with C and C++ and to coexist with existing C and C++ ecosystems from the jump. It also compiles to C++ as an intermediate representation, and leverages mature backend compilers such as [GCC](https://thenewstack.io/rust-support-is-being-built-into-the-gnu-gcc-compiler/) and [Clang](https://clang.llvm.org/).

Jule doesn’t just provide simple code translation; it also offers built-in language features specifically designed to simplify and [strengthen interoperability](https://manual.jule.dev/integrated-jule/).  
Jule also offers a C++ API for its [runtime](https://manual.jule.dev/runtime/), making it easier to extend Jule or integrate it directly into existing native codebases.

“Most importantly, we refuse to abandon existing C and C++ codebases or rewrite thousands of lines of proven code just to adopt a new language,” the Jule manual says. “We want more than temporary bridges or fragile workarounds. We want interoperability to be a first-class, intentional part of the language design.”

Moreover, although Jule has C/C++ interoperability, “our priority is to develop the standard library packages and compiler with Pure Jule as much as possible,” the manual says. “Integrating an existing C/C++ library for a feature is not a welcomed idea. Instead, it is preferred to design it as a 3rd-party binding library package.”

## Error handling

A question in the manual’s FAQ asks: Why does Jule use exceptionals instead of other error handling methods?

The response [reads](https://manual.jule.dev/some-questions.html#why-does-jule-use-exceptionals-instead-of-other-error-handling-methods:~:text=Exceptional%20handling%20is%20considered%20to%20be%20more%20efficient%20and%20safer%20in%20using%20an%20alternative%20value%20or%20handling%20exceptional%20and%20returning%20in%20elegant.) “exceptional handling is considered to be more efficient and safer in using an alternative value or handling exceptional and returning in elegant. Exceptionals were evaluated as more suitable in terms of readability and safety.”

Exceptionals are typically similar to Go’s error returns, the manual says.

Meanwhile, “Due to Jule being largely influenced by Go, many Go codes can be easily adapted to Jule. Go and Jule share very similar semantics. Implementing existing code is not too difficult,” the Jule manual asserts.

Also, regarding simplicity and maintainability, Jule is heavily influenced by Go.

## Efficiency

Jule’s design aims for high performance while keeping memory usage low. It targets systems-level workloads where efficiency, predictability, and control matter.

Also, Jule’s reference compiler performs its own optimizations to generate high-quality intermediate representation (IR), rather than relying solely on the backend for performance, the manual says.

In addition, for memory efficiency, Jule sidesteps runtime-heavy features such as traditional reflection, relying instead on compile-time reflection that delivers the same expressiveness without runtime costs

Some [observers](https://www.reddit.com/user/iMadz13/) on Reddit noted that the name Jule is too close to [Julia](https://julialang.org/), a high-level, dynamic programming language designed for high-performance numerical and scientific computing.

A redditor named [tegahertz](https://www.reddit.com/user/tegahertz/) replied: “Yes, it is somewhat similar in name but not influenced by Julia. In fact, I can’t say that it is a language designed as a C++ successor. It is only an alternative language to systems programming, but it can be said that C++ is also suitable to be seen as a successor.”

## The future of Jule

While Jule is still in beta, the community, which calls itself “[Julenours](https://jule.dev/code-of-conduct),” is working to make the language more stable and to build a robust standard library.

“To make it easier for the community and official developers to develop any tools for Jule, a significant portion of Jule’s official compiler is included in the standard library,” the manual reads. “The standard library has important stages such as lexer, parser, and semantic analyzer, and is suitable for use in tool development.”

[Andrew Cornwall](https://www.linkedin.com/in/acornwall/), an analyst at Forrester Research, tells *The New Stack*, “Jule hasn’t yet been standardized, which means it’s hard for enterprises to commit to it, regardless of its technical advances. Jule also lacks development tools, so I don’t expect we’ll see pressure from developers to adopt Jule wholesale.”

Moreover, “Very little is written in Jule, so AI code generation will be rudimentary,” Cornwall notes. “Right now, it still looks like Jule is in the passion project phase. That doesn’t mean it won’t break out — Ruby started as a passion project — but it will need more momentum and additional perspectives before it’s ready for prime time.”

While Cornwall identifies several challenges facing Jule’s enterprise adoption, [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at the Futurum Group, offers a more optimistic technical evaluation.

Regarding Jule, “it looks interesting and akin to Go, [Zig](https://ziglang.org/), and, of course, Rust in how it approaches the delicate balancing act many languages must maintain between safety, performance, and simplicity,” Shimmin tells *The New Stack*. “What stands out for me is its emphasis on compile-time capabilities, which typically leads to more predictable and performant code execution, a good thing for systems software.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)