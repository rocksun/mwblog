Let’s just say [Wasm 3.0](https://thenewstack.io/wasm-3-0-offers-new-way-to-handle-javascript-strings/) is an important release. And yet, the component model has not yet been completed. We can say that the great, widely anticipated “[Docker](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) moment” for [WebAssembly](https://thenewstack.io/webassembly/) has not yet been achieved.

My idea of the “Docker moment” for WebAssembly refers to the now-famous tweet by [Solomon Hykes](https://www.linkedin.com/in/solomonhykes), in which he said, to paraphrase, that if WASM+WASI had existed in 2008 and was finalized and in working order, then there would never have been a need for Docker in the first place.

So, the original promise of the greatness of WebAssembly still remains a work in progress. And the “Docker moment” — and how my concept of that translated into actual usage — depends on the component model. And the component model has not yet been completed and depends on the release of Wasi 0.3 (more on that below).

I would also argue that its lateness is not as significant and terrible as it may seem on the surface. That is, there have been some very interesting developments on the server side during the past year or so.

“The beauty of Wasm is that it has been widely adopted in the industry. The feature set of Wasm 3.0 will improve the experience for everyone, not just those targeting the browser,” former Bitnami co-founder and Wasm-based developer tool provider Endor CEO [Daniel Lopez Ridruejo](https://www.linkedin.com/in/ridruejo/) told me. “The component model specification I see as complementing and building on top of the general Wasm spec, and it is making steady progress even if taking longer than many would like.”

## Less Garbage

Wasm 3.0’s standout features — some of which have been in development for up to eight years, include (according to what is covered in the documentation):

**64-bit address space:** Memories and tables can now be declared to use i64 as their address type instead of just i32. This enlargement in theory expands the address space of Wasm applications from 4 gigabytes to (again, theoretically) 16 exabytes. Wasm apps designed to run in the browser — for which Wasm was originally created — means the 64-bit memory is limited to 16 gigabytes, although the possible jump to 16 exabytes on the server side is especially huge.

**Multiple memories:** As noted in the documentation and “contrary to popular belief,” Wasm has always been able to use multiple memory objects — and thus multiple address spaces — simultaneously. But before the release of Wasm 3.0, each memory space had to be declared and accessed and declared in separate modules. This is especially interesting and supports “deploy once, deploy anywhere” simultaneously since a single module can now declare (define or import) multiple memories and directly access them, including directly copying data between them, the Wasm developers say.

**[Garbage collection](https://thenewstack.io/time-to-get-the-garbage-out-of-webassembly/):** Besides further supporting the very lightweight and low-latency aspect of code and applications distributed through Wasm modules, Wasm GC becomes more adaptable and less rigid as it is up to the compilers to configure “engineering suitable representations” for source-language values, including implementation details like method tables. There are no built-in object systems, nor closures or other higher-level constructs, which would inevitably be heavily biased towards specific languages. Instead, Wasm only provides the basic building blocks for representing such constructs and focuses purely on the memory management aspect, its developers say.

Let’s just say that in many ways, Wasm (or WebAssembly) is used extensively, and I would argue many users don’t even realize it. Whether using services such as [Hyperlight](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/) on Azure, [Spin,](https://www.fermyon.com/blog/introducing-spin-v3) or [wasmCloud,](https://wasmcloud.com/) these platforms are enabling WebAssembly’s useful functionalities and the new ones described above.

Again, the component model has not yet been finished, but many component-like capabilities are already embedded, offered and worked around in ways that users can take advantage of through services such as [StackBlitz](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/), endor.dev and others.

In the case of Endor, a lot of fun and utility have been added to WebAssembly functionality. Developers can create reproducible, isolated testing environments in a few seconds instead of hours or days, thanks to WebAssembly’s lightning-fast speeds. Developers can also run agents and vibe coding, allowing developers to quickly and securely test that code, Endor’s developers say. Endor provides a way to do so both in the browser and on the command line.

In my case, I got a very geeky version of the first “Star Wars” released in just a few minutes, after accessing the Endor server and installing the shell.

## Component Rumors

Wasm 3.0 does not include a finalization of the component model. While Endor comes close, the magic Docker-like moment where you just put practically any application in a Wasm module — and you deploy it anywhere you want or send it anywhere you want, and it can be used anywhere you want — still remains in the works.

The standardization will mean that applications can be written in any language that can be distributed through Wasm modules for deployment on any endpoint simultaneously — and asynchronously. Once finalized, a component model will enable WebAssembly to expand its use beyond web browsers and servers. It will allow users to deploy different applications running inside numerous lightweight modules at very high speeds across thousands of endpoints simultaneously.

Much depends on the finalization of a component model, and especially its relationship to WASI, which is the standard interface or API linking the WebAssembly modules to the components. It will support the development of so-called WebAssembly “Worlds,” as groups of compatible Wasm components form an interconnected infrastructure similar to [Kubernetes](https://thenewstack.io/kubernetes/), but without containers. WASI Preview 2, released in 2024, made some huge strides toward standardization, but we are not there yet. In 2025, we will likely not achieve the Holy Grail, but we could see some pleasant surprises. Rumor has it that Wasi 0.3 might not be finalized this year, which would potentially delay the release of Wasi 1.0 and, hence, a working component model.

And again, WebAssembly’s adoption into the working fabric of infrastructure worldwide continues and is not predicated on Wasi 3.0’s release.

“The component portion has been strictly relegated to WASI, so they have not rolled it into the main standard,” [Matt Butcher,](https://www.linkedin.com/in/mattbutcher/) co-founder and CEO of [Fermyon](https://www.fermyon.com/?utm_content=inline+mention), told me. “I therefore agree: We haven’t hit that key Docker moment yet. But we’re getting close.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)