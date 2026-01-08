[WebAssembly](https://thenewstack.io/webassembly/) made huge strides with the release of Wasm 3.0 and the component model. However, the last lap in the race to WebAssembly’s true fruition is set to come with the planned release of [WASI 0.3.0](https://wasi.dev/roadmap) in 2026, likely in February.

Among other things, this final phase of standardization of the component model will mean that WebAssembly will be able to increasingly replace [containers](https://thenewstack.io/introduction-to-containers/), which are not ideally suited for a number of applications, whether within [Kubernetes](https://thenewstack.io/kubernetes/) or not. These include edge devices, asynchronous and event-driven deployments, serverless environments, and use cases where deployments must reach a large, potentially unbounded number of endpoints simultaneously with a single release.

## Far Beyond the Browser

Indeed, WebAssembly has moved far beyond the browser. It is running reliably in production across browsers, servers, CDNs, and backend services, proving its maturity and broad applicability, [Ralph Squillace](https://github.com/squillace), Microsoft’s principal product manager, Azure Core Upstream, said during the closing remarks at [WasmCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/wasmcon/), a [CNCF](https://cncf.io/?utm_content=inline+mention)-hosted co-located event during [KubeCon+CloudnativeCon North America 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/). “WebAssembly is already working and running in almost every environment.”

While core WebAssembly is intentionally low-level and difficult to use directly, recent specification work enables higher-level abstractions, Squillace said. Reference types and interface types allow components to expose meaningful APIs without developers needing to understand WASM internals, making the technology more accessible to engineers.

“The specification work at the core level… is what allows the component model to actually pass complex structures to form an API that makes sense,” Squillace said.

For those interested in components specifically, the [Bytecode Alliance](https://thenewstack.io/webassembly-to-let-developers-combine-languages/) is open to engineers at no cost, Squillace said. Its focus is on supporting engineers and open source development rather than marketing, and there are resources available — including documentation — that allow developers to start from zero using WebAssembly components.

These choices are not mutually exclusive, Squillace said. WebAssembly and the component model are not about replacing languages, modules, or containers, but about interoperability, safety, and expanding what software can do across languages and environments.

WebAssembly is not perfect, but that is not the point, Squillace said. What matters is what it enables. It is an exciting space built by people who choose to participate, and that is why, he said, this closing is really an opening.

## Core Specs

While core WebAssembly is intentionally low-level and difficult to use directly, recent specification work enables higher-level abstractions. Reference types and interface types allow components to expose meaningful APIs without developers needing to understand WASM internals, Squillace said.

“The specification work at the core level… is what allows the component model to actually pass complex structures to form an API that makes sense,” Squillace said.

At this point, Wasm-based solutions are not a drop-in replacement for containers but are increasingly being adopted in a lot of scenarios that leverage the strengths of WebAssembly. “The component model is a compelling reason to adopt Wasm, even if it is still in its early days. That said, WebAssembly is already adopted to the extent that it is heavily prevalent in many serverless and edge applications,” [Daniel Lopez](https://www.linkedin.com/in/ridruejo/), CEO and co-founder of [Endor](https://endor.dev/), told me. “Many users — and likely most — do not realize it is being used, especially in SaaS and serverless services, under the hood. Wasm already powers a lot of applications and use cases. Additional standardization with broad support from developers and industry players will only help accelerate that adoption.”

Wasm 3.0 does not include a finalization of the component model. While Endor comes close, the magic Docker-like moment where you just put practically any application in a Wasm module — and you deploy it anywhere you want or send it anywhere you want, and it can be used anywhere you want — still remains in the works.

The standardization will mean that applications can be written in any language that can be distributed through Wasm modules for deployment on any endpoint simultaneously — and asynchronously. Once finalized, a component model will enable WebAssembly to expand its use beyond web browsers and servers. It will allow users to deploy different applications running inside numerous lightweight modules at very high speeds across thousands of endpoints simultaneously.

For the opening remarks at WasmCon, a CNCF-hosted co-located event during KubeCon+CloudnativeCon North America 2025; [Bailey Hayes](https://www.linkedin.com/in/baileyhayes/), CTO, Cosmonic, described the core strengths that make WebAssembly so powerful: near-zero cold starts, high workload density, and a lightweight, portable runtime that performs well even in constrained environments. Looking ahead, Hayes heralded the upcoming WASI 0.3.0 release as a major milestone. It previews several features that define the next wave of WebAssembly-based computing, Hayes said. These include language-integrated concurrency with idiomatic bindings for different languages, composable concurrency across components written in different languages, and high-performance streaming enabled by low-level I/O and zero-copy data handling, Hayes said.

## Key Features for the Next Wave

“I want to highlight three key features I’m most excited about for the next wave of computing, including language-integrated concurrency, composable concurrency across components written in different languages, and support for high-performance streaming with low-level I/O and zero copies,” Hayes said.

Much depends on the finalization of a component model, and especially its relationship to WASI, which is the standard interface or API linking the WebAssembly modules to the components. It will support the development of so-called WebAssembly “Worlds”, as groups of compatible Wasm components form an interconnected infrastructure similar to Kubernetes, but without containers. WASI Preview 2, released in 2024, made some huge strides toward standardization, but we are not there yet. In 2025, we will likely not achieve the Holy Grail, but we could see some pleasant surprises. Rumor has it that Wasi 0.3.0 might not be finalized this year, which would potentially delay the release of Wasi 0.3.0 and, hence, a working component model.

“The WASI standardization process has been long, but every new preview release gets us closer to 0.3.0,” Lopez said. “Given the scope and foundational nature of the standard, it is important to get it as right as possible, even if it takes longer than expected.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)