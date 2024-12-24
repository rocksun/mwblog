# Why Platform Engineers Are Embracing WebAssembly for Serverless
![Featued image for: Why Platform Engineers Are Embracing WebAssembly for Serverless](https://cdn.thenewstack.io/media/2024/10/85daa094-mohammad-rahmani-8qeb0fte9vw-unsplash-1024x683.jpg)
[Mohammad Rahmani](https://unsplash.com/@afgprogrammer?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/black-flat-screen-computer-monitor-8qEB0fTe9Vw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
Enthusiasm for WebAssembly ([Wasm](https://thenewstack.io/webassembly/)) has been building for the last few years. And while [some Wasm energy remains](https://thenewstack.io/step-by-step-guide-to-using-webassembly-for-faster-web-apps/) in the browser world, more excitement is concentrated on Wasm on the server side of the equation.

Microsoft, Cloudflare, SUSE, Docker, Red Hat, and other stalwarts have introduced Wasm products or integrations. Multiple open source projects are making their way through CNCF’s project path, and developer interest has surged. For example, the open source[ Spin toolkit](https://www.fermyon.com/spin) for building serverless applications has now been downloaded more than 230,000 times.

What does this mean for platform engineering? Where are we going to see Wasm apps deployed?

**Why Server-Side?**
Virtual machines defined the early cloud. The value proposition was clear: package an operating system and apps inside a virtual machine and securely execute them on someone else’s hardware. A little over a decade ago, open source platforms like OpenStack joined a growing list of cloud providers to make it possible for organizations large and small to run their infrastructure without needing to own their own hardware or lease data center rack space.

As powerful as virtual machines were, they had a few drawbacks that drew the ire of developers and DevOps folks alike. Machine images were slow to build, deploy, and start-up, and they pushed a huge burden of [security and maintenance onto the team](https://thenewstack.io/is-security-a-dev-devops-or-security-team-responsibility/) or individual responsible for building the VM image.

The rapid ascent of Docker containers was no surprise to those who prized experience and ease of use. [Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) made building images easy and attractive for developers. Higher levels of abstraction and smaller sets of dependencies reduced and spread the maintenance burden across responsible parties. Containers started up in only a dozen seconds instead of minutes.

Zeal was outsized, though. Early proponents of container technologies claimed it was the death knell for virtual machines. When Kubernetes arrived on the scene, it showed the opposite to be true: VMs and containers live a happy coexistence. The vast majority of today’s Kubernetes clusters apportion virtual machines as nodes and then pack those virtual machines with containers.

Helpful as they are, containers don’t solve all the problems of modern clouds. They’re great for long-running processes whose expected lifespan is hours, days, or months. However, as a new development pattern called “serverless functions” gained popularity, the weaknesses of containers came into sharp relief.

A serverless function works as an event-driven application. Instead of starting a long-running daemon process that handles hundreds of thousands of requests (or more) during its long lifetime, a serverless function handles just one event — one request. It starts when an event is received, does whatever processing is required, returns a response, and shuts down. Operationally speaking, the virtue of this model is that when a request isn’t being handled, little or no system resources are utilized. Ideally, serverless functions are more efficient, cheaper, and easier to manage. But that requires having the correct runtime. The first generation of serverless did not nail this.

Containers and virtual machines are both optimized for long-running processes. Consequently, if they take a minute or a few dozen seconds to start up, the orchestration logic often absorbs that cost. However, taking minutes or even seconds to start in serverless functions is unacceptable, especially for frontline services. Users simply won’t wait around for a response.

Many attempts have been made to work around these limitations, most commonly being “pre-warming” virtual machines or containers, so they sit idly in a queue awaiting a request. But this is inefficient, driving the cost of operating serverless functions upwards.

What is needed is an isolated and secure runtime that can start up in milliseconds. Wasm is just such a runtime.

**With Your Containers**
With sub-millisecond startup time and a stronger-than-containers security model, Wasm is a fantastic environment for sandboxing short-running processes like serverless functions. Unsurprisingly, many open source tools, including Spin and[ Wasmtime](https://wasmtime.dev/), have evolved to execute Wasm functions in cloud environments. Serverless Wasm is far more efficient and cost-effective than cloud-specific solutions like AWS Lambda or Azure Functions. But there is no reason to pit Wasm against containers — they can work cooperatively.

Serverless functions are great for many applications but not for all. They may provide cheaper, simpler microservices, web backends, API servers, and batch processors. But plenty of services need to run all the time, keeping a pool of threads working continually. Databases, message queues, and legacy applications are examples of these.

Containers provide an excellent base technology for always-on servers. To respect both serverless and always-on use cases, a system should be able to run both containers and Wasm workloads.

We already have a host of container environments, from[ Rancher Desktop](https://www.suse.com/c/rancher_blog/rancher-desktop-1-13-with-support-for-webassembly-and-more/) and[ Docker Desktop](https://docs.docker.com/desktop/wasm/) locally to Kubernetes and Nomad in the cloud. Starting with yet another orchestrator, this time for serverless Wasm would introduce yet more operational complexity into an already complicated environment. It has been far easier to integrate Wasm runners into these existing environments.

On the desktop, both Rancher Desktop and Docker Desktop support running Wasm.[ SpinKube](https://www.spinkube.dev/) brings Wasm support to Kubernetes, providing facilities to run containers and Wasm side-by-side in the same pod. Even enterprise-class Nomad[ can schedule tasks to a Wasm runtime](https://www.hashicorp.com/resources/webassembly-and-hashicorp-nomad-for-next-wave-microservices). Regardless of your infrastructure investments, if you are running containers, it is not hard to also run Wasm in the same services.

SpinKube, submitted earlier this year for[ addition to CNCF’s sandbox projects](https://www.globenewswire.com/news-release/2024/03/21/2849971/0/en/Fermyon-Contributes-SpinKube-to-CNCF-Making-WebAssembly-a-First-Class-Workload-in-Kubernetes.html), integrates a Containerd shim, a few operators, and new CRDs to add Wasm support directly to Kubernetes. Far from introducing performance overhead, SpinKube clusters can host thousands of Wasm applications and [manage several hundred](https://thenewstack.io/what-does-it-take-to-manage-hundreds-of-kubernetes-clusters/) thousand serverless function invocations per second on an 8-node Kubernetes cluster.

**An Evolution of Serverless**
AWS introduced the first wave of serverless functions with Lambda. A decade later, it’s time for a technology-wide upgrade. With Wasm-based serverless functions and projects like SpinKube, it is possible to run front-line web applications using the serverless functions design pattern.

Thanks to Wasm’s portability and the open source nature of Wasm platforms, there is no more cloud lock-in. Run them anywhere [Kubernetes](https://thenewstack.io/how-to-run-databases-on-kubernetes-an-8-step-guide/) runs, anywhere containers run, or even on bare metal as small as a Raspberry Pi. And Wasm’s ultra-fast sub-millisecond cold start time means that not only can your most performance-intensive frontend workloads be run as Wasm, but even your rarely accessed apps can be installed into a Kubernetes cluster without consuming resources all the time.

Wasm has caught the eye of many server-side developers because the tooling is easy to use and straightforward to run. However, the runtime characteristics of Wasm make it so powerful a technology when paired with containers in today’s modern cloud.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)