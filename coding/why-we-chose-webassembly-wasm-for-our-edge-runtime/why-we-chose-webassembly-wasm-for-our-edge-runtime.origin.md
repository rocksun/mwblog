# Why We Chose WebAssembly (Wasm) for Our Edge Runtime
![Featued image for: Why We Chose WebAssembly (Wasm) for Our Edge Runtime](https://cdn.thenewstack.io/media/2024/05/decce164-webassembly-at-the-edge-featured-image.jpg)
Edge computing enables organizations to distribute workloads, move them closer to their users and customize outputs more delicately for personalized user experience. However, deploying containers — let alone virtual machines (VMs), with all their operating system overhead — is unfeasible at the edge due to resource limitations.
[WebAssembly (Wasm)](https://thenewstack.io/webassembly/), an open binary format for executables, promises a lightweight and secure alternative better suited for the constrained environments at the edge. In this article, I’ll explain why we at Gcore chose Wasm as the runtime for our latest [edge computing](https://thenewstack.io/edge-computing/) solution, FastEdge. I’ll also share what inspired us to build FastEdge in the first place.
## FastEdge: Satisfying the Demand for Edge Computing
Routing traffic in and out of data centers is a time and money drain. Paired with the rising demand for increasingly personalized web experiences, we needed to explore a new approach to cloud computing. Fortunately, we’d already built a network of edge nodes with our content delivery network (CDN). Adding computation capabilities to our CDN nodes was the next logical step.
To build FastEdge, we first added a Wasm runtime to our CDN nodes and built edge applications for common web application tasks like image resizing, file uploads or content conversion. These apps are closely related to the tasks our CDN performs. They give our customers the benefits of edge computing without needing to code, and let us test and polish our edge platform with real use cases before opening it for custom applications.
We
[released FastEdge](https://gcore.com/fastedge) to the public earlier this year, allowing our customers to build their own edge-powered applications with our software development kits (SDKs).
## Why Wasm?
Wasm is the technology powering FastEdge. It’s an open standard for executables and runtimes similar to Java. However, as the “assembly” aspect of its name implies, Wasm is more low-level, as it’s binary encoded, doesn’t include garbage collection and enables near-native performance. Wasm offers three benefits that make it particularly suitable for our goal of providing secure and performant edge computing with FastEdge: inherently isolated modules, fast module start, and ease of distribution and deployment.
### Inherently Isolated Modules
Wasm enables browsers to run applications with high performance demands, like 3D games. However, running software written in low-level programming languages — like
[Rust](https://roadmap.sh/rust) or [C/C++](https://roadmap.sh/cpp) — on every smartphone and PC on the web has grave security implications, as these languages usually have direct access to system resources.
That’s why Wasm has sandboxed modules, which have to define their function calls at load time so that it’s not possible to dynamically inject new calls. Additionally, each module gets its own heap memory that comes with buffer overflow protection.
It turns out that isolated modules aren’t just good for client software. Cloud providers frequently run third-party applications on their infrastructure, so the providers also benefit from isolation that protects their systems from malicious code. Other solutions based directly on a
[JavaScript](https://thenewstack.io/top-5-underutilized-javascript-features/) runtime, like [V8](https://thenewstack.io/node-js-22-release-improves-developer-experience/), require customization to achieve this isolation level.
### Fast Module Start
Wasm modules can start under a millisecond, making Wasm a great candidate for applying the modern serverless computing approach to the edge. Again, executing demanding applications in a browser has similar requirements as running them in cloud environments. Users don’t want to wait multiple seconds for a website to render, and serverless applications also suffer from long
[cold-start](https://thenewstack.io/how-to-conquer-cold-starts-for-better-performance/) times. Compared to container- or VM-based solutions, a Wasm module’s cold start is significantly shorter.
### Easy To Distribute and Deploy
Wasm is loaded and executed by browsers without requiring a restart of the client or the whole machine. App creators can host a Wasm file on a web server, and the browser takes care of the rest.
As Wasm already allows loading modules from remote servers via HTTP, we simply reused this deployment model for FastEdge to simplify module distribution and unburden edge systems administrators.
## Open Standard, Open Runtime
Unlike other runtime standards, such as JVM and .NET, Wasm has been an open standard created and maintained by multiple organizations since its inception. This intrinsically open approach allows any individual or organization to contribute features and bug fixes that improve the overall quality of the project, making Wasm an appealing choice for cloud applications.
Since Wasm is an open standard, several organizations have implemented runtimes for it. For FastEdge, we chose
[Wasmtime](https://wasmtime.dev/) as our runtime; its creator, the Bytecode Alliance, is a joint effort by multiple organizations. Selecting a runtime for a platform is a serious long-term business investment, and we expect Wasmtime’s collaborative approach to yield quality software. Multiple organizations keep the project up to date and maintain high standards — and that’s protected even if a single contributor or contributing organization leaves, making Wasmtime a solid long-term solution.
Finally, the
[open source approach](https://thenewstack.io/open-source/) also brings the benefit of multiple programming languages to the browser and the edge. It’s possible to compile Rust, C/C++, Go, Zig and other languages to Wasm, so in the long run, FastEdge has the potential to support numerous languages. We currently offer a [Rust SDK](https://github.com/G-Core/FastEdge-sdk-rust/), and plan to release a JavaScript/TypeScript SDK soon.
## Integrating Wasm Into Our Existing Edge Network
Choosing Wasmtime as our Wasm runtime allowed us to deliver a proof of concept for FastEdge in only three months, as Wasmtime already offered features like isolation and host communication. Still, Wasmtime is just a runtime, so we needed to make some additions to make it work with our existing CDN nodes.
We implement host functions for request data like headers and body to allow FastEdge apps access to data outside the runtime. We plan to add more host functions for SQL and NoSQL databases, key-value stores such as Redis, queues and streaming services.
Opting for open source software accelerated the creation of our observability stack. Projects like Prometheus, Grafana and OpenSearch power the monitoring systems we provide developers so they can inspect logs from the edge. Additionally, we’re creating a tool to enable testing edge applications locally.
Finally, we ensured tight integration of FastEdge with our CDN, so edge applications hook into every step of the CDN lifecycle. This way, you can check authorization for downloads, provide authentication for uploads, or modify the body and headers depending on attributes like image size or geographical location.
## FastEdge in Action
We offer two approaches for building and deploying applications with FastEdge:
- A traditional approach with SDKs and tooling that allows developers to build applications.
- A template approach that allows non-technical people to deploy common applications from templates.
For the template approach, we created applications that solve common website tasks, like a Markdown-to-HTML converter and an S3 uploader.
We also experimented with AI at the edge and
[built a website](https://fast-edge-demo.fastedge.gcore.dev/) demonstrating FastEdge’s capabilities using image classification as a use case. The following image shows an image classifier running on FastEdge. Our white paper explains more about [our vision of AI at the edge](https://gcore.com/library/wp-web-assembly-for-ai-inference). ![Image classification at the edge](https://cdn.thenewstack.io/media/2024/05/6533790f-webassembly-at-the-edge-1-1024x399.png)
Image classification at the edge.
We also deployed a low-latency word prediction engine on FastEdge.
![Word prediction at the edge](https://cdn.thenewstack.io/media/2024/05/f1bcef20-webassembly-at-the-edge-2-1024x391.png)
Word prediction at the edge.
Turning to the traditional approach, we encourage developers to build their own apps on FastEdge with
[our Rust SDK](https://github.com/G-Core/FastEdge-sdk-rust/). The following code defines a simple anonymous proxy that extracts a URL parameter at the edge and fetches a website.
This example illustrates how you can use our custom host functions to access request data from the client and send your own requests to any API on the web without revealing the client information to that API. Find the
[full example on GitHub](https://github.com/G-Core/FastEdge-sdk-rust/tree/main/examples/backend).
## Summary
While not originally created for backend applications, many Wasm features are perfectly suited for use at the edge. They allow delivery of smaller and faster applications than container-based solutions and aren’t bound to one programming language. Using Wasm as the core technology for our edge computing platform made it possible to deliver FastEdge quickly with a small team while allowing us to stay flexible and adaptable regarding FastEdge’s future.
With tight CDN integration and application templates, FastEdge does things differently than other edge computing solutions. If you want to personalize your content for a globally distributed customer base or empower your nontechnical teams,
[give FastEdge a try](https://gcore.com/fastedge). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)