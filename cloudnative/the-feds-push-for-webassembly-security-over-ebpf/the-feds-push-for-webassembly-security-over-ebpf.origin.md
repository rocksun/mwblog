# The Feds Push for WebAssembly Security Over eBPF
![Featued image for: The Feds Push for WebAssembly Security Over eBPF](https://cdn.thenewstack.io/media/2025/02/b7d02bd1-getty-images-mn20kmlxr9a-unsplash-1-1024x683.jpg)
The use of [WebAssembly](https://thenewstack.io/webassembly/) could become mandatory to meet security-compliance requirements while solving other ongoing security conundrums as [Wasm](https://thenewstack.io/what-makes-wasm-different/) becomes more widely adopted.

According to a [National Institute of Standards and Technology (NIST)](https://thenewstack.io/nist-secures-encryption-for-a-time-after-classical-computing/) paper, “[A Data Protection Approach for Cloud-Native Applications](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8505.pdf)” (authors: [Wesley Hales](https://www.linkedin.com/in/wesleyhales) from [LeakSignal](https://www.leaksignal.com/); [Ramaswamy Chandramouli,](https://www.linkedin.com/in/ramaswamy-chandramouli-64b8446) a supervisory computer scientist at NIST), WebAssembly could and should be integrated across the cloud native service mesh sphere in particular to enhance security. The framework outlined in the paper may lead to future compliance requirements for WebAssembly or cloud native environments, while also setting the stage for broader use of WebAssembly for security in general.

The paper emphasizes how WebAssembly modules, with their in situ or in-proxy approach, make WebAssembly a strong candidate for data categorization as data travels between services. With Wasm, data checks across any type of data distributed across one or more cloud native environments are provided.

“A lot of folks have the [eBPF](https://thenewstack.io/what-is-ebpf/) hammer, and everything looks like a nail to them — but it’s not,” the report’s co-author Hales told The New Stack. “eBPF is built for one thing.”

eBPF was originally designed for protection against side-channel attacks, such as the Heartbleed vulnerability — which compromised the OpenSSL cryptographic library — and other kernel-level, related vulnerabilities. eBPF allows you to patch something once it’s discovered and block that activity, Hale explained.

“People are using it for everything because it’s an easy insertion point. That’s one of the benefits of eBPF — it’s easy to install and provides a certain level of visibility. However, it cannot tap into Layer 7 human-readable text, as it operates in the kernel space,” Hale said.

Bringing packets from eBPF at Layer 4 into user space for analysis requires the packets to be mirrored before being analyzed in a container. “This creates a Frankenstein-like process that is not performant at all,” Hales said. “Wasm truly serves the purpose for what we’re doing. We actually prototyped eBPF, and it simply wasn’t going to work for us.”

## eBPF vs. Wasm
Comparing eBPF security to that of Wasm, the authors of the paper wrote:

“Using Wasm to parse human-readable text in Layers 4–7 offers several advantages over technologies like eBPF, particularly regarding handling complex application-layer data, such as HTTP. While eBPF is powerful for data capture and manipulation directly within the kernel, its use for parsing detailed HTTP traffic can be complex and potentially excessive for some applications. This complexity stems from the need to handle the intricacies of HTTP within the kernel — a task that can restrict performance and introduce security concerns if not managed correctly. Additionally, eBPF imposes numerous restrictions and requires extra effort for data processing and general-purpose computation.

“Wasm provides a secure, sandboxed environment that is suitable for efficiently executing code across multiple platforms and parsing application-layer protocols. Wasm can be used in user spaces and server environments, allow easier integration with existing parsing libraries and tools, reduce complexity, and potentially enhance the reliability of parsing operations. Its portability and ability to embed in various runtime environments make it a practical choice for network traffic analysis tasks, including those involving protocols that handle human-readable text.”

In the cloud native world, all data traffic is forced through the [service mesh](https://thenewstack.io/service-mesh/)[ Istio](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/)’s proxy and Wasm by its modular or “sandboxed” design. “You may have 10,000 containers sitting behind an Istio proxy, while all the logging traffic, all the web traffic, even the database traffic all has to go in the proxy and then to wherever the destination is,” Hales said. “So we get to look at all that with Wasm.”

## Big Picture
One takeaway from the paper is not that security with WebAssembly is superior to that of eBPF. What it’s saying, and to restate, is that when taking a step back — whether in observability, security, a comprehensive solution or strategy, or best practices — one should not replace one with the other. It would thus be highly unlikely for the U.S. government, for example, to suddenly mandate WebAssembly and not implement or mandate eBPF for certain use cases. In the commercial world, a comprehensive security or observability player or offering should include eBPF for its range of use cases and WebAssembly for others.

“eBPF was never meant to be a generic computation platform and it has both algorithmic and memory constraints. From a security perspective, it is also a bad practice to push functionality to the kernel (where eBPF resides) when it can be accomplished in the user space like Wasm,” said [Ben Hirschberg,](https://il.linkedin.com/in/ben-hirschberg-66141890) CTO and co-founder of [ARMO](https://www.armosec.io/). “It thus makes much more sense to implement complex observability logic in WASM and leave the required minimal functionality in eBPF.”

Indeed, WebAssembly was designed for so-called sandbox security from the outset. “The most widely used sandboxed application environment is one I guarantee you are running right now: a web browser. The browser is an environment fundamentally built to run untrusted code. WebAssembly’s browser-based heritage is the reason for its first-class sandboxing technology,” said [Matt Butcher,](https://www.linkedin.com/in/mattbutcher) Fermyon co-founder and CEO. Unlike containers and eBPF, security was not an afterthought; it was a core feature from inception to present. I am not surprised to witness the proliferation of Wasm in security-sensitive environments.”

Beyond Istio’s proxy, Wasm provides coverage in a more extensive way than eBPF can, covering data transfers through HTTP, gRPC or [GraphQL](https://thenewstack.io/graphql-federation-the-missing-api-for-your-platform-strategy/), or wherever the network traffic goes, Hales explained. “It doesn’t matter since they’re still all traveling through that pipe of Layer 7 through Layer 4,” Hales said.

“It is useful to think of Wasm as a flexible core technology with well-defined extension methods. It is platform-neutral, meaning it can run on many operating systems and system architectures. And it is now supported by almost all major programming languages,” Butcher said. “Inherently, that makes Wasm more adaptable than eBPF. To put it succinctly: Wasm was built to be general-purpose while eBPF was not.”

*Alex Williams contributed to this article.*
*Editor’s Note: Updated at 2 p.m. EST, Feb. 14 to update the url of “A Data Protection Approach for Cloud-Native Application” to the most recent version.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)