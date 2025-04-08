# Hyperlight Wasm: Azure Goes the Final Wasi Mile
![Featued image for: Hyperlight Wasm: Azure Goes the Final Wasi Mile](https://cdn.thenewstack.io/media/2025/04/1fdb20b5-benoit-deschasaux-9hpzjldfsk4-unsplash-1-1024x514.jpg)
LONDON — Microsoft’s Azure Core Upstream team’s [Hyperlight](https://opensource.microsoft.com/blog/2024/11/07/introducing-hyperlight-virtual-machine-based-security-for-functions-at-scale/) now includes Hyperlight Wasm, marking a long-awaited development in extending and deploying [WebAssembly](https://thenewstack.io/webassembly/) modules and components on [virtual machines](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/) for Azure.

Microsoft has also donated the project to the [CNCF](https://cncf.io/?utm_content=inline+mention).

The [Hyperlight project](https://thenewstack.io/microsofts-hyperlight-webassembly-for-vms-is-open-source/) relies on small, embedded functions using hypervisor-based protection for each function call at scale. Each function request also has its own [hypervisor](https://thenewstack.io/4-reasons-devops-engineers-still-rely-on-hypervisors/) for protection.

This compatibility feature has been years in the making, fulfilling the long-standing promise of WebAssembly and its [polyglot](https://thenewstack.io/webassembly-gets-polyglot-development-boost-in-spin-3-0/) language capabilities.

![](https://cdn.thenewstack.io/media/2025/04/6e86015c-screenshot-2025-04-03-at-12.06.16%E2%80%AFpm.png)
Source: Microsoft

With it, workloads can be deployed, spun up, and spun down to and from VMs on Azure or in any other cloud or on premises environments in milliseconds — without containers. Yes, that’s right — bypassing any worries about operating system compatibility or other concerns with deploying code to a virtual machine. Much of this is owed to [WebAssembly System Interface](https://github.com/WebAssembly/wasi) (WASI) development, which offers interoperability with different endpoints, which in Hyperlight’s case, consists of VMs.

As WebAssembly is the conduit, it is no longer restricted to just other machine languages such as [Rust](https://thenewstack.io/rust-programming-language-guide/) and C, although it can handle those as well. So far, Hyperlight offers compatibility with the following languages with which users can execute workloads in Hyperlight Wasm: C, [Go](https://thenewstack.io/introduction-to-go-programming-language/), Rust, [Python](https://thenewstack.io/python/), [JavaScript](https://thenewstack.io/javascript/) and C#. The trick here, much like with [containers](https://thenewstack.io/containers/), is to also include a language runtime as part of the image.


[@Microsoft]´s Danilo (Dan) Chiarlone and Mikhail Krinkin showed Wasm working on Hyperlight and both with Envoy at[@rejektsio]during their talk
Envoy, and Hyperlight Walk Into a Pod: No Vulnerabilities Allowed.[@thenewstack][pic.twitter.com/GeEiM0enj1]— BC Gain (@bcamerongain)

[March 31, 2025]
Unlike containerized environments, where workloads must first be packaged, distributed, and collected within a container, Hyperlight Wasm allows workloads to be distributed directly from the operating system to the VM. This eliminates the extra overhead of containerization and thus offers additional lightweight benefits associated with sending light workloads with Wasm.

Security is an important aspect of WebAssembly, particularly in this implementation. The code runs in an isolated environment, and a module written in Rust has been embedded in the runtime to address digital vulnerabilities. Microsoft claims they have taken extensive measures to enhance security in this regard.

Building Hyperlight with a WebAssembly runtime enables a programming language to execute in a protected Hyperlight micro-VM “without any prior knowledge of Hyperlight at all,” Microsoft’s [Yosh Wuyts,](https://www.linkedin.com/in/yoshuawuyts/?originalSubdomain=dk) senior developer advocate, and [Lucy Menon](https://popl25.sigplan.org/profile/lucymenon), software engineer and researcher, wrote in a blog post.

Developers can use Hyperlight Wasm to compile for the wasm32-wasip2 target so they can run their programs locally using runtimes like wasmtime or Jco or run them on a server using for Nginx Unit, Spin WasmCloud — or now Hyperlight Wasm, Wuyts and Menon wrote. “If done right, developers don’t need to think about what runtime their code will run on as they’re developing it,” Wuyts and Menon wrote. “That is a degree of developer flexibility that is only possible through standards.”

As Wuyts and Menon described, when the Hyperlight VMM (Virtual Machine Manager) creates a new VM, it creates a new slice of memory and loads the VM guest, which in turn loads the wasm workload, Wuyts and Menon wrote. “This takes about 1-2 milliseconds today, and work is happening to bring that number to be less than 1 millisecond in the future,” Wuyts and Menon wrote.

## In Action
How Hyperlight works with Wasm and Envoy was described and demoed during the [Rejekts](https://cloud-native.rejekts.io/) talk here in London this week. It took place during the talk “Wasm, Envoy, and Hyperlight Walk Into a Pod: No Vulnerabilities Allowed,” which Microsoft engineers [Mikhail Krinkin](https://ie.linkedin.com/in/mikhail-krinkin-57892a86/en) and [Danilo (Dan) Chiarlone](https://x.com/danologue?lang=en) gave.

The talk covered cloud security, particularly isolation methods for running applications. Chiarlone discussed three isolation levels: absence, weak (using kernel features) and strong (using hypervisors like KVM or Microsoft Hyper-V). They described and showed how Hyperlight libraries can be used to leverage limited hypervisor technologies to create micro-virtualization environments. As they described, Hyperlight supports running untrusted code safely, including WebAssembly.

Chiarlone showed how Hyperlight Wasm runs a VM, enters the VM, executes the guest code — which follows function calls — and then having the VM exit and resume execution. The process Chiarlone showed involved the nested sandboxing of the Hyperlight sandbox inside the hypervisor (two layers of isolation), executing the code and outputting the result.

Krinkin demonstrated integrating Hyperlight with Envoy, a service mesh, to sandbox custom plugins. The example involved creating a sandbox for a WebAssembly module that handles TCP connections, emphasizing the importance of configuring constraints to prevent untrusted code from escaping the sandbox.

You will leave ready to utilize Hyperlight to build robust and scalable production solutions with a solid defense-in-depth strategy.

## Performance Benchmarks
Benchmarks were provided. As Chiarlone and Krinkin showed, the latency specifications of cold start times of code in a VM is measured in milliseconds. The extremely fast execution speeds are also palpable when applications compiled to WebAssembly code is run in the browser as well as in serverless or edge environments — in the browser as well, the user access the http: address and the application runs almost instantly since there are no downloads involved or other preliminaries that might otherwise slow down performance.

Since WebAssembly is not specific to a particular architecture — such as x86 or ARM — it instead abstracts over those architectures, functioning as a hardware abstraction layer, Chiarlone said. As explained above, WebAssembly is executed within a sandboxed environment, in which applications must explicitly opt into specific capabilities.

In the demo, Chiarlone said there were capabilities compiled to Wasm with Hyperlight. “These are explicitly granted to an application, allowing it to use them,” Chiarlone said. “However, capability three cannot be used unless explicitly permitted.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)