# Go Power: Microsoft’s Bold Bet on Faster TypeScript Tools
![Featued image for: Go Power: Microsoft’s Bold Bet on Faster TypeScript Tools](https://cdn.thenewstack.io/media/2025/03/0ca6f42e-highway-393492_1280-1024x682.jpg)
Microsoft has launched an initiative to port the [TypeScript](https://thenewstack.io/typescript/) compiler and tools to a native [Golang](https://thenewstack.io/golang-1-22-redefines-the-for-loop-for-easier-concurrency/) implementation, codenamed “Corsa.”

With the native implementation, Microsoft promises dramatic performance improvements of up to 10x that will both enhance [developer experience](https://thenewstack.io/improving-developer-experience-drives-profitability/) and enable new AI-powered capabilities.

This effort also addresses scaling challenges in large codebases where TypeScript users currently experience long load times, slow type checking, and memory constraints, reads a [blog post](https://devblogs.microsoft.com/typescript/typescript-native-port/) by [Anders Hejlsberg](https://www.linkedin.com/in/ahejlsberg/), a Microsoft technical fellow and co-creator of TypeScript.

Microsoft was able to achieve the performance and meet the scaling challenges by porting the TypeScript compiler to the [Go language](https://thenewstack.io/introduction-to-go-programming-language/).

## Performance
Key performance improvements include reduced build times by approximately 10x, an 8x improvement in project load time, roughly half the memory usage of the current implementation (with further optimizations expected), and language services improvements including significant speedups for completions, quick info, go to definition, and find all references.

“The native implementation will drastically improve editor startup, reduce most build times by 10x, and substantially reduce memory usage,” Hejlsberg wrote.

The new native version showed impressive performance metrics across various popular codebases:

- VS Code (1,505,000 LOC): 77.8s → 7.5s (10.4x faster)
- Playwright (356,000 LOC): 11.1s → 1.1s (10.1x faster)
- TypeORM (270,000 LOC): 17.5s → 1.3s (13.5x faster)
- date-fns (104,000 LOC): 6.5s → 0.7s (9.5x faster)
- tRPC (18,000 LOC): 5.5s → 0.6s (9.1x faster)
- rxjs (2,100 LOC): 1.1s → 0.1s (11.0x faster)
Indeed, “A 10x performance improvement represents a massive leap in the TypeScript and JavaScript development experience…,” Hejlsberg wrote.

In a [video](https://www.youtube.com/watch?v=pNlq-EVld70), Hejlsberg noted that JavaScript (which TypeScript is based) is mainly used “for UI and browser usage and not so much for compute-intensive workloads like compilers and system-level tools.” He added that Microsoft has likely reached the limit “of what we can squeeze out of JavaScript.”

## Port or Rewrite
Hejlsberg said that his team knew that they wanted to do a port and not a rewrite of the TypeScript compiler to Go.

In an [FAQ](https://github.com/microsoft/typescript-go/discussions/410) on the TypeScript effort, [Ryan Cavanaugh](https://www.linkedin.com/in/ryan-cavanaugh-aa4a37106/), development lead for the TypeScript team, wrote:

“Broadly speaking, there are two possible strategies you can take when changing languages:

- In a ‘rewrite’ you start with nothing, and implement a new system that tries to solve the same problem as the original one, disregarding the implementation strategies of the original codebase
- In a ‘port’ you take the existing codebase and convert it to the new language while trying to keep as much the same as possible
Porting is faster to execute, but requires that the new language be at least somewhat architecturally compatible with the original language…”

## Why Go?
Hejlsberg said Microsoft tried prototyping in all the usual suspect target languages (C#, C++, Rust, etc.) but found that Go was the most suitable language for the particular workload they were trying to do.

“Very interesting! JS developers are unfortunately used to slow tools, so a faster compiler that allows for improved editor startup time is very welcome,” [David Mytton](https://www.linkedin.com/in/davidmytton/), CEO of Arcjet, told The New Stack. “Moving to a native compiler makes a lot of sense, although Go is an unusual choice for this type of project. When I saw the announcement I assumed this would be in Rust like most of the other JS tool rewrites: [Rolldown](https://rolldown.rs/), [Turbo](https://turbo.build/) (which [moved](https://vercel.com/blog/how-turborepo-is-porting-from-go-to-rust) from Go to Rust), [Deno](https://github.com/denoland/deno)… I wonder what’s behind that decision.”

Responding to that question, Cavanaugh, in the FAQ, wrote that Go did the best when considering multiple criteria that are particular to this situation.

“By far the most important aspect is that we need to keep the new codebase as compatible as possible, both in terms of semantics and in terms of code structure,” he wrote. “We expect to maintain both codebases for quite some time going forward. Languages that allow for a structurally similar codebase offer a significant boon for anyone making code changes because we can easily port changes between the two codebases…”

The Go-based implementation is available on GitHub (typescript-go repository) and is currently capable of loading many popular TypeScript projects, including the TypeScript compiler itself.

## Versions
Microsoft expects a preview of native `tsc`
capable of command-line typechecking by mid-2025. `tsc`
is the TypeScript compiler. A feature-complete implementation for project builds and language service is expected by the end of 2025.

The most recent TypeScript release was TypeScript 5.8, with TypeScript 5.9 coming soon. The JS-based codebase will continue development into the 6.x series, and TypeScript 6.0 will introduce some deprecations and breaking changes to align with the upcoming native codebase, Hejlsberg said.

“When the native codebase has reached sufficient parity with the current TypeScript, we’ll be releasing it as TypeScript 7.0,” he said.

And, “For the sake of clarity, we’ll refer to them simply as TypeScript 6 (JS) and TypeScript 7 (native), since this will be the nomenclature for the foreseeable future,” Hejlsberg wrote. “You may also see us refer to ‘Strada’ (the original TypeScript codename) and ‘Corsa’ (the codename for this effort) in internal discussions or code comments.”

Meanwhile, benefits beyond speed include support for instant, comprehensive error listings across entire projects and more advanced refactoring capabilities. It also enables deeper code insights previously too expensive to compute and sets the foundation for next-generation AI tools that enhance development. Microsoft also is moving to Language Server Protocol (LSP) for better alignment with other languages.

“The core value proposition of TypeScript is an excellent developer experience,” Hejlsberg wrote. “As your codebase grows, so does the value of TypeScript itself, but in many cases TypeScript has not been able to scale up to the very largest codebases.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)