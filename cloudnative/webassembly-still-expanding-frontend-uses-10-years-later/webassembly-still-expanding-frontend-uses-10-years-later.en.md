It’s been 10 years since Mozilla, Microsoft, Apple and [Google](https://cloud.google.com/?utm_content=inline+mention) announced [WebAssembly (Wasm)](https://thenewstack.io/webassembly/webassembly-what-beginners-need-to-know/) as a collaborative effort. Back then, the goal seemed clear: Create a low-level binary instruction format for compiling older, non-web languages to run in the browser.

Its uses have [grown beyond that initial goal](https://thenewstack.io/when-webassembly-replaces-docker/), but there’s much more that [Wasm offers developers on the frontend](https://thenewstack.io/webassembly/wasm-for-the-frontend-a-look-at-developer-uses/). The list expanded even more with September’s release of Wasm 3.

The New Stack spoke with [Thomas Steiner](https://www.linkedin.com/in/thomassteinerlinkedin/?originalSubdomain=es), developer relations engineer at Google, about the common uses for WebAssembly.

## Wasm for Business Logic

One of the most popular uses for applications is writing the business logic for an application and then using that code across platforms via WebAssembly, according to Steiner.

“That’s a common pattern that we see where people outsource the business logic to a WebAssembly module, and then they pull that module in from various contexts, which can be web applications, native applications, some even use [applications on] the server side,” Steiner told The New Stack. ”If you have a logic that runs on a server that doesn’t necessarily need a frontend, you can also use WebAssembly there.”

He pointed to [Snapchat](https://thenewstack.io/snapchat-open-sources-cross-platform-ui-framework/), which he said more or less has the same app on web and mobile platforms. Rather than recoding the business logic for every platform, Snapchat writes the business logic in one language and then translates it to WebAssembly.

“WebAssembly can be run on the web, but also on the native platforms,” he said. “They can have the same business logic run in different contexts, and they save themselves a lot of development work.”

## JavaScript and WebAssembly

WebAssembly can actually run faster than JavaScript code in many cases, Steiner said. For instance, tasks that are very computationally intense can run faster inside WebAssembly.

It can also be used to address hyphenation issues. JavaScript does not allow hyphenation in variable and function names. For some languages — English and German, for instance — the browser already knows how to deal with hyphenation.

“One thing that we’ve seen used quite frequently is hyphenation,” he said. “There’s some languages where the browser doesn’t know the hyphenation rules.”

When those rules are implemented in libraries and the developer wants to render strings on a web page that are written in a nonsupported language, the developer can do a hyphenation in the WebAssembly module, and then just output the hyphenated text to the web page.

“You input the text that you want to hyphenate. The WebAssembly module does its logic, tells you where it would split words and so on, and then you take those and render it on the screen,” he said. “That’s a common example.”

Another common use case for WebAssembly is with cryptography, if you need to encrypt or decrypt something. It can be used to implement features that are already implemented elsewhere, he added.

“I, for example, maintain a library that converts from raster images and turns them into vector images,” he said. “You can imagine this is a relatively costly operation, so with WebAssembly, we can outsource that processing cost into Assembly, [and] make it run in a separate thread in the browser.”

This allows developers to have a fully interactive frontend that, at the same time, runs very computationally intense jobs in the background.

## A New Approach to JavaScript Strings

[Wasm 3 offers a more efficient way](https://thenewstack.io/wasm-3-0-offers-new-way-to-handle-javascript-strings/) to handle JavaScript strings. We asked Steiner about the significance of this change.

“The core idea of this feature is essentially you have a language, JavaScript, that already has built-in functions for dealing with strings, for example,” he said.

One example is handling Unicode strings, which is quite complex. This kind of feature is already implemented in the [JavaScript language](https://thenewstack.io/javascript/ "JavaScript language"), but if a developer wanted to use the same in WebAssembly, they would need to compile the code to do that and turn it into WebAssembly.

The new method provides an easier option.

“You could just borrow the implementation that it already exists in the JavaScript-land, import it into WebAssembly, make it usable from there, and save yourself from doing some of the compilation work that already exists on the hosting language, like, in this case, JavaScript,” he said.

The new feature creates a mechanism that lets the Wasm module simply call or import the existing, built-in JavaScript string function directly.

## New Languages Due to Garbage Collection

Thanks to the [September Wasm 3 update](https://webassembly.org/news/2025-09-17-wasm-3.0/) that incorporates garbage collection, more higher-level languages are adding support for WebAssembly. Java, OCaml, Scala, Kotlin, Scheme and Dart are some of the languages that now target Wasm for compilation, according to the WebAssembly.org blog announcing the improvement.

In Wasm 3, the WebAssembly team added support for a new and separate form of storage that is automatically managed by the Wasm runtime via a garbage collector. Since Wasm is a low-level language, Wasm GC adds low-level primitives to Wasm, allowing compilers to target Wasm more easily for garbage-collected languages.

“It can declare the memory layout of its runtime data structures in terms of struct and array types, plus unboxed tagged integers, whose allocation and lifetime is then handled by Wasm. But that’s it,” the [Wasm blog post](https://webassembly.org/news/2025-09-17-wasm-3.0/) stated. “Everything else, such as engineering suitable representations for source-language values, including implementation details like method tables, remains the responsibility of compilers targeting Wasm.”

That means no built-in object systems, nor closures or other higher-level constructs, which the post added, “would inevitably be heavily biased towards specific languages.”

“Instead, Wasm only provides the basic building blocks for representing such constructs and focuses purely on the memory management aspect,” the post noted.

## Wasm, Serverless and Backend Liberation

It can also be used to support [serverless](https://thenewstack.io/forrester-on-webassembly-for-developers-frontend-to-backend/) functions on the frontend, although Steiner pointed out “serverless” is a misnomer.

“Of course, there is a server, but the idea is the server is not constantly running,” he said.

[Developers will write their business logic](https://thenewstack.io/what-developers-need-to-know-about-business-logic-attacks/) and the WebAssembly runtime (which is run on the server) quickly spins up, handles the request and then goes to sleep again, he said.

“WebAssembly has a bunch of unique features that make it very fast to spin up in such contexts,” Steiner said. “That’s why, in the WebAssembly ecosystem, a lot of startups are working around supporting WebAssembly on the server as well.”

Fastly is one such company, he added. Fastly is an edge cloud platform and offers a Content Delivery Network (CDN). The high-performance, open source web server [Nginx also supports Wasm](https://blog.nginx.org/blog/server-side-webassembly-nginx-unit) on the server, he added.

There is an entire service stack that runs everything on the server in WebAssembly, he continued. This allows developers to switch the backend provider easily, so the developer isn’t locked into a particular backend technology stack.

“As long as your stack supports WebAssembly, everything that is beyond this WebAssembly runtime, you don’t need to care,” he said.

## Tools for Compiling Wasm

If you see a use for Wasm that might work for your application, here are a few options for compiling to WebAssembly.

One of the most popular tools is **Emscripten**. Originally designed to port video games — specifically a first-person shooter called “Sauerbraten” (or “Syntensity” on the web) — written in C and C++ to the browser, [Emscripten](https://github.com/emscripten-core/emscripten) was created by [Alon Zakai](https://www.linkedin.com/in/alonzakai/), a former Mozilla engineer who now works at Google. It’s open source under both the MIT license and the University of Illinois/NCSA Open Source License. It leverages both Binaryen and is a LLVM/Clang-based compiler.

**LLVM** can be used to compile to WebAssembly for the backend and optimizations. It supports frontends for C, C++ and Rust, leveraging advanced analysis and transformation passes, according to [KodeKloud Notes’ introductory class on Wasm](https://notes.kodekloud.com/docs/Exploring-WebAssembly-WASM/Compiling-to-WebAssembly/WASM-Compilers).

[**Binaryen**](https://github.com/WebAssembly/binaryen) lets developers assemble, optimize and transform Wasm binaries, which makes it ideal for minimizing code size and fine-tuning low-level performance, according to KodeKloud.

[**wasm-pack**](https://github.com/drager/wasm-pack) can compile, test, and publish Rust-based Wasm packages to npm.

[**AssemblyScript**](https://www.assemblyscript.org/) provides a [TypeScript](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/)-flavored syntax that compiles directly to Wasm. It exposes WebAssembly-specific types (e.g., i32, f64) for predictable performance, according to KodeKloud.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)