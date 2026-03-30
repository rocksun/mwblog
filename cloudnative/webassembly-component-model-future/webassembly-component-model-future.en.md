The mass adoption of WebAssembly has yet to be realized.

The true turning point for WebAssembly — specifically its ability to ship lightweight code to any number of endpoints with millisecond latency — rests on finalizing the component model.

> “The true turning point for WebAssembly — specifically its ability to ship lightweight code to any number of endpoints with millisecond latency — rests on finalizing the component model.”

Standardizing the component model will allow WebAssembly to replace containers in areas where they typically struggle, regardless of whether Kubernetes is involved. Wasm is better suited for edge devices, serverless environments, and event-driven deployments that require pushing updates to an unlimited number of endpoints simultaneously.

Indeed, WebAssembly has moved far beyond the browser. It shows its maturity via reliable production use across servers, CDNs, and backend services, as well as its broad applicability.

While core WebAssembly is intentionally low-level and difficult to use directly, recent specification work enables higher-level abstractions. Reference types and interface types allow components to expose meaningful APIs without developers needing to understand WASM internals, making the technology more accessible to engineers.

During this talk, “Towards a Component Model 1.0” at Wasm I/O in Barcelona last week, Luke Wagner of Fastly described efforts to make the so-called Component Model easier to adopt, including motivating native browser implementations and closing a few remaining functionality gaps.

> “Achieving a ‘just works’ developer experience requires standards-based answers to coordinated problems… such as how a standard library performs IO or how multiple modules are bundled and linked at runtime.”

While technical improvements like debugging and threading are important, the “higher order bit” for explosive Wasm adoption is a lack of upstream support in popular languages and frameworks, Wagner said.

Achieving a “just works” developer experience requires standards-based answers to coordinated problems, such as how a standard library performs IO or how multiple modules are bundled and linked at runtime. To address this, the strategy involves two layers: the component model, which provides foundational answers for computation and virtualization, and WASI, which defines modular standard APIs for various types of IO, Wagner said.

“I’m going to claim, perhaps contentiously, that a lack of upstream support for all the popular languages, tools, factors, and frameworks so that Wasm can just work both inside and outside the browser is holding up Wasm’s adoption,” Wagner said.

Wagner said WebAssembly Preview 2 factored out the component model layer, while the upcoming Preview 3 extends it to handle concurrency with async functions, strings, and futures. This concurrency feature will serve as a major milestone towards completing the component model.

Moving from “eager” memory allocation to a “lazy” API to reduce heap fragmentation and improve performance by inverting control flow is also planned. Other planned improvements for 1.0 include supporting multi-value returns, adding error context values, and introducing a GC API option for languages that use garbage-collected memory, Wagner said.

“With Preview 3, we’re extending a Wasm module to provide answers to a lot of concurrency questions. And as part of that, finding async functions, strings, and futures as first-class concepts,”  Wagner said. “So, lots of benefits come from this lazy API. But how do we change the API by maintaining that all-important stability, guarantee that I just mentioned?”

Meanwhile, the component model provides standards-based answers to open questions, allowing for “upstream support everywhere, so the host can just work,” Wagner said. “We’ve got a preview for release coming very soon, followed by cooperative threads and a minor release that gives us answers to a bunch of hard concurrency questions,”  Wagner said.

To encourage native browser support, Wagner highlighted JCO, a tool that transpiles components into JavaScript and core WebAssembly that runs in browsers today. Native support would offer performance gains by avoiding JS glue code and allowing direct calls from Wasm into browser code.

 Wagner concluded his talk with a callout to the community to make pull requests that help simplify the component model by building shared tooling around guest and host APIs. The project can also use contributions for more documentation to keep pace with commits.

Contributions for upstreaming and cross-language tooling, and closing key expressivity gaps with features like optional imports, callbacks, subtyping, and more, are also needed, Wagner said.

“And so what I’d ask from everyone here is to use Preview 3 once it’s released, use JCO to simplify your web developer experience with Wasm,”  Wagner said. “And if any of these many Bytecode Alliance projects I mentioned sound interesting, please contribute and say hi to us on Bytecode Alliance at Zulip, and you can read and discuss the component model spec on the GitHub repo.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)