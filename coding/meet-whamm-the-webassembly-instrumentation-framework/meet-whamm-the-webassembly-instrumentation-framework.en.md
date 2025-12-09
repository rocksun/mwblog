Every once in a while, a particularly interesting release or project is introduced at a larger conference amid zero marketing backing or by large, corporate-esque teams. At [KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/), [Elizabeth Gilbert](https://www.linkedin.com/in/elizabeth-gilbert-2b01aa338/), a doctoral candidate at Carnegie Mellon University, described a project called [Whamm](https://ejrgilbert.github.io/whamm/) that really can work out of the box with one line of code. It does not replace, ameliorate or improve existing tools and processes but can actually do things that have not properly existed before.

Gilbert did an excellent job of describing this project she created and is garnering a significant amount of downloads and forks following her aforementinoed talk, [“Whamm: A Framework for Performant, Sandboxed Instrumentation”](https://colocatedeventsna2025.sched.com/event/28D4w/whamm-a-framework-for-performant-sandboxed-instrumentation-elizabeth-gilbert-carnegie-mellon-university) at the [CNCF](https://cncf.io/?utm_content=inline+mention)-hosted KubeCon + CloudNativeCon co-hosted event [WasmCon.](https://colocatedeventsna2025.sched.com/overview/type/ArgoCon)

Whamm is designed to allows users to instrument their [WebAssembly](https://thenewstack.io/webassembly/), or Wasm, applications with a programming language or code, or lets them program their WebAssembly applications in modules directly. With it, they can debug, monitor, etc., their applications within WebAssembly modules.

Originally introduced in a paper titled [“Flexible Non-intrusive Dynamic Instrumentation for WebAssembly,”](https://dl.acm.org/doi/10.1145/3620666.3651338) Whamm is described as a framework for “Wasm application monitoring and manipulation.” On Gilbert’s [GitHub page,](https://ejrgilbert.github.io/whamm/) she describes Whamm’s instrumentation, monitoring and bytecode rewriting capabilities this way:

* **Instrumentation:** When we say we are “instrumenting a program,” at a high-level we mean we are “injecting some code into a program’s execution to do some operation.” This definition is intentionally generic since instrumentation can really do anything we can imagine! You can use instrumentation to build debuggers, dynamic analyses, telemetry generators, and more.
* **Dynamic analysis:** A dynamic analysis is something that analyzes a program as it is executing (in contrast to a static analysis which analyzes a program that is not running). This type of analysis can gain useful insights into a program as it is able to access information that is not available statically (such as hot code locations, memory accesses over time, code coverage of test suites, etc.).
* **Bytecode rewriting:** This is an example strategy for injecting instrumentation logic into the application. It injects instrumentation through literally inserting new instructions into the application bytecode.

“Instrumentation is really a way to observe your application behavior, which is kind of a flexible enough definition to encapsulate all the different things. It can be observability, but it can also be used for testing use cases, such as fault injection testing,” Gilbert told me at KubeCon + CloudNativeCon after her talk. “You can inject faults into your application to see if it’s able to handle things correctly. Instrumentation can be used to manipulate application execution as well as it’s doing.”

As Gilbert explained, the main motivation for focusing on WebAssembly is the language interoperability. “Since multiple different languages can compile to WebAssembly, this is what is desired for the tooling to be really cool. If you have language-agnostic tooling, then if some new programming language comes along, if it just compiles to WebAssembly, you could get all the tools for free,” Gilbert said. “This polyglot possibility could be really, really cool for a lot of different people. As Wasm becomes more widely targeted, if we have the instrumentation story there, then all the dev tools can be gotten for free, and the platform can hook into all kinds of different things.”

The current status of the project is that it can “do quite a few things, but there is a need to work out more use cases to make it more robust,” Gilbert said. “The project has currently been worked on in isolation. More people, especially engineers, contributing would be ‘killer’ because then the work can go faster.”

Indeed, I already expect to see a number of engineers looking to contribute to and benefit from Whamm.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)