# GraalVM (Finally) Gets Java for WebAssembly
![Featued image for: GraalVM (Finally) Gets Java for WebAssembly](https://cdn.thenewstack.io/media/2025/04/74984e01-daniel-dan-fj11x2c4ui8-unsplash-1024x683.jpg)
BARCELONA — [GraalVM](https://thenewstack.io/how-to-build-with-graalvm-inside-github-actions/) now benefits from a WebAssembly ([Wasm](https://thenewstack.io/webassembly/)) backend so that [Java](https://thenewstack.io/introduction-to-java-programming-language/) code and applications can be compiled directly into Wasm modules. Seen as a major development and milestone, the development should serve as a potential boon not just for Java users, but for the evolution of [WebAssembly](https://thenewstack.io/why-webassembly-will-disrupt-the-operating-system/) as a whole.

“This is fantastic news for both Java and Wasm. It broadens mainstream adoption for WebAssembly, especially in corporate environments where Java is prevalent,” [Daniel Lopez](https://x.com/vomkriege?ref_src=twsrc%5Etfw), CEO of Endor, a startup that makes it possible to run server-side software inside your browser, and co-founder and previously CEO of Bitnami, told The New Stack at [Wasm I/O 2025](https://2025.wasm.io/) here last month. “It also helps Java adoption in a lot of new scenarios like browsers.”

Up until now, Java has been a neglected child of sorts. WebAssembly modules have been more conducive for a number of reasons — that we won’t go into here — with [C and C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/), [Rust](https://thenewstack.io/rust-programming-language-guide/) and [Go,](https://thenewstack.io/introduction-to-go-programming-language/) and now even [Python](https://thenewstack.io/python/) is embedded as an interpreter.

Java is a favorite developer language, but the community has long sought to address its downsides, such as less-than-ideal latency specs and its relative heaviness compared to other programming languages, especially for running applications in the browser, serverless, edge computing and other use cases.

WebAssembly, of course, offers what could be described as almost zero latency, sometimes measured in mere fractions of a millisecond. It has gained traction not only in the browser, where it has been a mainstay for over a decade, but also as it expands toward edge computing.

Open source [Chicory](https://thenewstack.io/chicory-write-to-webassembly-overcome-jvm-shortcomings/) was created to bring some of the benefits of Wasm to native [JVM](https://thenewstack.io/how-do-javas-virtual-threads-help-your-business/), bringing with it the security, the tunnel and the isolation aspects WebAssembly modules provide (or sandbox capabilities, to use industry jargon). As a VM-native WebAssembly runtime, Chicory is designed to enable WebAssembly programs to run with zero native dependencies or Java Native Interface (JNI). In other words, while Chicory previously served as an excellent pure-Java Wasm interpreter with lightweight functionality and zero dependencies to make it ultra-portable, [GraalWasm](https://www.graalvm.org/webassembly/docs/) offers use cases for which you would probably not necessarily want to use Chicory anyway.

🧩 The Future of Write Once, Run Anywhere: From Java to WebAssembly by

[@_patrickziegler]&[@fniephaus]@ Wasm I/O 2025▶️ Video:

[https://t.co/Qs8xBdq4RB]🔗 Slides:

[https://t.co/LTvqSrB9v2][#wasmio25][@graalvm]
— Wasm I/O (@wasm_io),April 22, 2025
Previously, WebAssembly for Java execution through GraalVM — which Oracle and other vendors maintain — was missing garbage collection features, which are essential for Java’s memory management, just-in-time compilation, dynamic dispatch capabilities and other features. But as Oracle engineers working on GraalVM, [Patrick Ziegler](https://2025.wasm.io/speakers/patrick-ziegler/) and [Fabio Niephaus](https://www.linkedin.com/in/fniephaus/details/education/), showed in their talk, [The Future of Write Once, Run Anywhere: From Java to WebAssembly](https://www.youtube.com/watch?v=Z2SWSIThHXY&ab_channel=WASMI%2FO) at Wasm I/O 2025, GraalVM and GraalWasm have been shown to overcome these setbacks.

“WebAssembly takes the friction out of deploying code anywhere — from data centers to browsers to IoT devices — and turns it into a seamless experience,” [Torsten Volk,](https://www.linkedin.com/in/torstenvolk) an analyst with TechTarget’s Enterprise Strategy Group, told me. “Supporting WebAssembly is a critical move for Java and its community to shed its legacy image, as this not only enables Java to run at the edge, but also simplifies the combination of Java applications with applications in any language that supports Wasm.”

## The Demo
The backend work to enable GraalVM to further accommodate Java involved the [WasmGC](https://github.com/WebAssembly/gc) proposal and exception handling, Ziegler said during his talk. “This makes mapping Java to Wasm a lot easier,” Ziegler said. “Every Java type is represented as a WebAssembly struct, and exception handling — same story, right? Basically, it maps almost one-to-one to WebAssembly. This helps a lot with reducing complexity and also helps with code size.”

As Ziegler explained and showed, a HelloWorld script written in Java might be around one megabyte in size. “That seems pretty big — and of course, it is — but for a Java program, it’s not that large,” Ziegler said. “Also, this is before you apply compression or run WasmOpt. If you do all of that, you can get the size down to around 300 kilobytes easily.”

Thanks to WasmGC, JavaScript objects with Java can now be shared with a GraalVM JavaScript interoperability API. While all the interactions are backed by Java code, “every button had an event listener that called Java code, which did the actual compilation,” Ziegler said.

“The API handles conversions of all different types for you. It manages method invocation and more,” Ziegler said. “There’s really a lot you can do if you’re targeting a JS embedding.”

Another benefit is the availability of the Java standard library or the JDK. “Of course, not everything is currently working,” Ziegler said. “Features like threading, networking and graphics will currently throw an exception if you call them. But it’s all step-by-step.”

A JavaScript runtime called [GraalJS](https://www.graalvm.org/latest/reference-manual/js/), which implements the WebAssembly ES module integration, is also available. This means you can use JavaScript bindings to facilitate high-level communication between Java and WebAssembly, Niephaus said during this talk. “Whatever wasm-bindgen spits out, you can use that to interface from Java to JavaScript and then from JavaScript to Wasm,” Niephaus said.

## Full Circle
As mentioned above, Java had been conspicuously missing from WebAssembly’s handling of languages or its polyglot capabilities. WebAssembly currently supports a range of languages in addition to low-level languages like Rust, C and C++, as well as more abstracted languages like JavaScript. Through GraalVM, users can run Java in WebAssembly, which could be a potential boon not only for WebAssembly use but also for the very large Java developer and user community.

“I think the reason that news was so exciting to all of us in the language-nerd category is because we were watching the organization that has been shepherding Java adopt one of the coolest virtual machine technologies — GraalVM — and embrace the WebAssembly standard,” Fermyon co-founder and CEO [Matt Butcher](https://www.linkedin.com/in/mattbutcher/) told me during [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) recently. “That’s really exciting.”

Sun Microsystems originally marketed Java as a “write once, run anywhere” language, Volk said. “While this promise held up well in the world of servers and desktops, it fell flat at the edge. The Java Virtual Machine’s appetite for CPU and memory simply proved too great for constrained environments,” he said. “Enter WebAssembly: it is the disruptor that finally delivers on the original Java promise, but without the baggage, with smaller binaries, lightning-fast startup times, lean memory requirements, and the freedom to choose your programming language. WebAssembly takes the friction out of deploying code anywhere — from data centers to browsers to IoT devices — and turns it into a seamless experience.”

GraalVM’s expanded support for WebAssembly is a critical move for “Java and its community to shed its legacy image,” Volk said. “This not only enables Java to run at the edge, but also simplifies the combination of Java applications with applications in any language that supports Wasm,” he said.

Oracle has been seen as being aware of the potential for invigorating Java’s use in WebAssembly since it was introduced, but it stopped short of working to embrace it for the Java community. (An Oracle PR representative did not respond to The New Stack’s queries by email.)

“Oracle has been shepherding the Java project along for years and years. When WebAssembly first came out, Oracle’s concern — or maybe not even Oracle’s, but the Java community’s initial reaction — was, ‘Wait, this is just another kind of bytecode, like Java bytecode. Why are we trying to reinvent the technology that we’ve spent two dozen years perfecting?’” Butcher said. “I think it became evident that they’re different enough and have different enough use cases — one of them being support for the component model, but another being the different performance profiles you get on each.”

The community gradually then began to see WebAssembly as “less threatening,” Butcher said. “Java has been doing some amazing stuff on the virtual machine front, and GraalVM has kind of emerged as the premier performance-focused Java virtual machine,” Butcher said. “So it was fantastic to see Oracle contributing WebAssembly support using GraalVM as the basis for it.”

“I know it sounds harsh to use words like ‘technological laggard,’ but because of their initial reluctance to embrace WebAssembly, they’ve been behind even .NET, Python, Ruby, Rust and Go in adopting it,” Butcher said. “But now that they’ve made this announcement, I think the big takeaway is that the WebAssembly ecosystem as a whole has now been validated by every single major language community — from Swift, Rust and Go, the newer, shinier ones, to C, Java and .NET, the classic enterprise lineup.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)