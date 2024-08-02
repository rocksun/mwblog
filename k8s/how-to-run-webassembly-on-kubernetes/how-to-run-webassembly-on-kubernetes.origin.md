# How To Run WebAssembly on Kubernetes
![Featued image for: How To Run WebAssembly on Kubernetes](https://cdn.thenewstack.io/media/2024/07/8f350ba4-berlin-4068968_1280-1024x663.jpg)
The other day, I was chatting with a platform engineer. “You do WebAssembly stuff, right? It seems like everyone is talking about it as the new way to do serverless. What does that mean?” Originally conceived as a browser technology, [WebAssembly](https://thenewstack.io/webassembly/) (Wasm) is showing up in many places now. In the Kubernetes world, it is providing a new way of running serverless — sometimes called FaaS or Functions as a Service.

[Kubernetes](https://thenewstack.io/kubernetes/) just crossed its [tenth anniversary](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/). In its early days, in 2015 and 2016, we talked about [Kubernetes as a Docker](https://thenewstack.io/docker-versus-kubernetes-start-here/) orchestrator. It sat atop [Docker](https://www.docker.com/?utm_content=inline+mention) and scheduled containers to run on Docker instances.
But Docker itself was not really on board with this. They had created their orchestrator, Swarm, which they believed was superior to Kubernetes. And there was some bad blood. DockerCon disallowed talks about Kubernetes, yet Docker folks showed up at KubeCon to discuss how Swarm was better than Kubernetes. Years later, we’ve all forgiven and moved on. But in that moment, the conflict between the two led Kubernetes in an exciting direction. Instead of remaining Docker-centric, the Kubernetes developers took one hop up the abstraction layer and began calling Kubernetes a *container orchestrator*. And they began attempts to support other container runtimes, such as CoreOS’s rkt (pronounced “rocket”).

Abstracting from the details of the container runtime has big advantages. An area whose innovation was controlled by only one company was suddenly open to all. [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), Samsung, [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention), and many other reputable engineering organizations could bring their formidable talent to the field.

Now, a decade later, the benefits are clear. Containerd is now a well-established project governed by the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention), and it offers so much flexibility that developers have added a variety of containerd “shims” to support around a dozen different low-level runtimes.

One of the technologies supported this way is Wasm.

## From the Browser to the Cloud
Wasm was developed to solve a specific problem: Take library code from languages like C, C++, Rust, Go, and Zig and make them available to JavaScript code running in the web browser. In a way, Wasm was designed to rectify the mistakes made with Java Applets, Silverlight, Flash, and other non-JS browser languages. In this regard, Wasm has been successful. Every mainstream browser supports Wasm, and from Office 365 to Figma, Wasm powers some sophisticated web apps.

But Wasm’s security model, cross-platform support, and compact bytecode format make it a good fit for other applications beyond the browser. BBC and [Amazon](https://aws.amazon.com/?utm_content=inline+mention) use it in their embedded streaming players. Shopify uses it as a plugin language. SingleStore supports Wasm-stored procedures in its database. Most interestingly, Wasm has been making inroads on the cloud.

## Serverless Is the Sweet Spot
Serverless computing, introduced by AWS’s Lambda service, allows the developer to write an event handler instead of an entire server daemon. An event-handling function starts when a request comes in, handles that request (returning a response if necessary), and then shuts down. While a container or VM runs for hours, days, months, or even years, serverless functions run from a few milliseconds to a few minutes. But if your function only runs for a few milliseconds, then the runtime’s performance is a top concern. Early serverless solutions tended toward underwhelming performance.

This is where Wasm shines. A Wasm runtime can cold-start in under one millisecond. This means Wasm functions can scale from zero instances to hundreds of thousands of instances in the blink of an eye — and then back down to zero again just as fast. In an age of enormous cloud bills, this scant resource usage and excellent performance means cloud resources can be scaled down! It takes fewer servers to run Wasm than it does containers.

## Containerd, Meet Wasm
As Knative, OpenWhisk, Fn Project, and other Kubernetes serverless frameworks struggle to perform efficiently, there is clear room for a new generation of serverless inside of Kubernetes.

That’s where[ SpinKube](https://spinkube.dev) comes in. Publicly announced at KubeCon Paris and on track to become a CNCF Sandbox project, SpinKube provides all the plumbing to add Wasm support to containerd and then supports Wasm applications side-by-side with containers inside Kubernetes. Containerd is so well designed that a Wasm binary can be scheduled into the same Kubernetes Pod as a container, and the two can run side-by-side. This means a new kind of ultra-high-performing serverless for Kubernetes can augment existing container apps. Those who want to go all-in on serverless, porting their Lambda and Azure Functions code to Kubernetes, can do so quickly and easily with SpinKube. On the other hand, those who want to begin reducing waste inside their cluster can replace sidecars or low-traffic microservices with Wasm functions… and then gradually migrate what makes sense to them.

Suitable technologies meet the potential of their initial design. Great technologies outgrow their initial design. Kubernetes and Wasm have both done so, bringing them together to solve real performance and cost problems in the modern Kubernetes cluster.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)