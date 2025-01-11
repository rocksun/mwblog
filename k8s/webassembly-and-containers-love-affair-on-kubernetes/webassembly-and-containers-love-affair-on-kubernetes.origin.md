# WebAssembly and Containers’ Love Affair on Kubernetes
![Featued image for: WebAssembly and Containers’ Love Affair on Kubernetes](https://cdn.thenewstack.io/media/2025/01/a44c06b5-freestocks-r_ov6smbbyk-unsplash-1-1024x683.jpg)
The use of [WebAssembly](https://thenewstack.io/webassembly/) is emerging as an optimal use case to replace containers in Kubernetes environments for certain workloads. Running side by side with [containers](https://thenewstack.io/containers/), [Wasm](https://thenewstack.io/what-makes-wasm-different/) modules can replace heavier containers or be used when very fast cold start times are required, as Wasm modules are scaled up and down.

Heavy containers, for example, are particularly problematic in the sidecar and [service mesh](https://thenewstack.io/service-mesh/) or with [OpenTelemetry](https://thenewstack.io/honeycomb-ios-austin-parker-opentelemetry-in-depth/) for observability solutions. In contrast, WebAssembly components replacing sidecar containers running on Kubernetes offer better, lighter weight, and faster cold start times.

Yes,

[#Wasm]can make sense on Kubernetes, replacing containers in some instances.[@Microsoft]‘s Jiaxiao Zhou detailed how that works during his[@KubeCon_]talk “Running WebAssembly (Wasm) Workloads Side-by-Side with Container Workloads.”[@thenewstack][@fermyontech][#webassembly][pic.twitter.com/WZ1egGyhDG]— BC Gain (@bcamerongain)

[November 15, 2024]
As you’ll see below, running WebAssembly with containers on Kubernetes is doable, as [Jiaxiao Zhou,](https://www.linkedin.com/in/mossaka) senior software engineer at Microsoft, said during a talk, “Running WebAssembly (Wasm) Workloads Side-by-Side with Container Workloads,” at [KubeCon+CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) in Salt Lake City in November.

“Throughout the years I’ve been working on WebAssembly, I’ve been hearing people saying, ‘Can we run WebAssembly in my own existing infrastructure?’ meaning Kubernetes. So, it is imperative to make WebAssembly compatible or runnable in Kubernetes,” Zhou said during his talk.

## The Work Up
![](https://cdn.thenewstack.io/media/2025/01/a013277e-capture-decran-2025-01-06-175647-1024x403.png)
Source: CNCF and Microsoft

WebAssembly is showing promise on Kubernetes thanks to the fact that WebAssembly now meets the OCI registry standard as OCI artifacts. This enables Wasm to meet the Kubernetes standard and the OCI standard for containerization, specifically the OCI artifact format. It also involves compatibility with Kubernetes pods, storage interfaces and more. In that respect, it’s one step toward using Wasm as an alternative to containers.

Additionally, through [containerd,](https://thenewstack.io/azure-kubernetes-service-replaces-docker-with-containerd/) WebAssembly components can be distributed side by side with containers in Kubernetes environments. Zhou likened this to a drop-in replacement for the unit’s containers, integrating with tools such as [Istio](https://thenewstack.io/istio-1-23-drops-the-sidecars-for-a-simpler-ambient-mesh/), [Dapr](https://thenewstack.io/dapr-create-applications-faster-with-standardized-apis/) and OpenTelemetry Collector.

When running applications through WebAssembly as sidecars in a cluster, the two main challenges involve distribution and deployment, as Zhou outlined. A naive approach bundles the Wasm runtime into a container, but a better method offloads the Wasm runtime into the shim process in containerd. This approach allows Kubernetes orchestration of Wasm workloads. The OCI artifact format for WebAssembly, enabling Wasm components to use the same distribution mechanisms as containers, is responsible for the distribution part, Zhou said.

Again, it is possible to bundle the Wasm runtime and the Wasm layers into containerd and run that container in Kubernetes, Zhou said. “Obviously, that works. But we want to do something better: We want to offload the Wasm runtime into the shim process that runs in containerd.”

Because containerd is the de facto runtime for Kubernetes, it can be orchestrated by Kubernetes — “and that’s exactly what we did,” Zhou said. With the [RunWASI](https://github.com/containerd/runwasi) project — for which Zhou is a maintainer — a library for authoring shims is available that can run WebAssembly workloads, It supports multiple WebAssembly runtimes: [Wasmtime](https://thenewstack.io/webassemblys-wasmtime-1-0-revamps-security-performance/), [WasmEdge](https://thenewstack.io/demos-deploying-llms-with-wasmedge/), [SpinKube](https://thenewstack.io/how-to-build-serverless-webassembly-apps-with-spinkube/) and other options to run WebAssembly side by side with containers, Zhou said.

“The magic lies in the shim architecture,” Zhou said. When containerd sends an RPC request into the shim, asking the shim to create a container and start executing a container, the shim will create a new instance. That instance will examine the binary’s first few bytes to see if this is a Linux container or if this is a Wasm binary, Zhou said. “If this is a Wasm binary, we use a Wasm runtime baked into the shim to execute that instance, and if this is a Linux container, we just use the Linux runtime to run that container,” Zhou said. “And this is all possible due to an amazing open source project called Yuki. This is written in Rust, and we use Yuki’s libcontainer executor to write our own Wasm runtime, and we can dispatch the instance into either the Linux case or the Wasm case.”

## Do Drop In
![](https://cdn.thenewstack.io/media/2025/01/34e031ad-capture-decran-2025-01-02-182357-1024x224.png)
Source: CNCF and Microsoft

With WebAssembly on Kubernetes, there are two scenarios that Zhou described: first, as a drop-in replacement for [Linux](https://thenewstack.io/steve-langasek-one-of-ubuntu-linuxs-leading-lights-has-died/) containers — “because they are too heavyweight,” Zhou said. “We want to just rewrite that into WebAssembly, but we still want to use the sidecar container to add logins, OpenTelemetry and such,” Zhou said. The second scenario is where you have a heavyweight Linux container and you can’t just compile it to Wasm because of the language toolchain issues. However, it is possible to “carve out some of the features” or some of the code from your Linux container and compile that into Wasm and run as a sidecar container in the same pod, Zhou said.

Again, running WebAssembly on Kubernetes can overcome some of the downsides associated with containers, Zhou said. Containers can often be hundreds of megabytes in size, and the entire operating system is sometimes bundled inside the container, which “makes it bloated,” Zhou said. Containers also have some slow cold-startup times that can take up to a few seconds, and “that’s not fast enough for some use cases like bursty function workloads,” Zhou said. Containers must be built per architecture — a container built for x86 will not be able to run on Arm — and the inter-container communication has a lot of overhead, Zhou said.

Sidecar containers, in particular, can be especially heavy and large. A [Linkerd](https://thenewstack.io/some-linkerd-users-must-pay-fear-and-anger-explained/) sidecar could consume up to 150 megabytes of disk space because they have bundled the entire [JVM](https://thenewstack.io/chicory-write-to-webassembly-overcome-jvm-shortcomings/) into the sidecar, Zhou said. Sidecar containers consume additional CPU, memory and network resources because they are running as a sidecar to a main application. “So they’re actually competing with your main application for resource consumption. There is some operational complexity given that the sidecar container and main application can be managed by different teams,” Zhou said. “They have different upgrades and version controls. And if your sidecar operates too frequently, it can interrupt your main application, and so all of the three points above will have an active impact on pod scaling and cluster efficiency.”

WebAssembly, on the other hand, has sub-millisecond cold starts. “This is really attractive because now you can start a new WebAssembly instance per request, and it has fast inter-Wasm communication,” Zhou said. “You can compose two Wasm components together, and the communication will be a local function invocation, and that will present a high density for your guest applications.”

There are some downsides for WebAssembly as well. “It’s not the case that any Linux binary can be compiled to WebAssembly. There are some system calls that WASI may not support. And the language toolings are not great,” Zhou said. “I’ve been working on integrating the Go language with WASI for quite some time, and we still don’t have [WASI P2](https://github.com/WebAssembly/WASI/blob/main/wasip2/README.md) for [Go](https://thenewstack.io/golang-how-to-use-the-go-install-command/). And WASI is a relatively new technology, so some of the security boundaries need to be production-tested.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)