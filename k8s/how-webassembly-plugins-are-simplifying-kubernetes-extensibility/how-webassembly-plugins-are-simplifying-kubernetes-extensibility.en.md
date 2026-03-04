The integration of [WebAssembly](https://thenewstack.io/webassembly/) (Wasm) into the [Helm](https://thenewstack.io/helm-4-whats-new-in-the-open-source-kubernetes-package-manager/) ecosystem streamlines the orchestration of [WASI](https://thenewstack.io/wasi-preview-2-what-webassembly-can-and-cant-do-yet/)-compliant binaries across disparate environments, including OCI containers and virtualized infrastructure. By leveraging Helm’s templating engine, developers can standardize the lifecycle of sandboxed modules while maintaining a high degree of portability.

While Wasm inherently provides fault-isolated execution through a capability-based security model, deploying via Helm reinforces this via [Kubernetes](https://thenewstack.io/kubernetes/)-native segmentation. This synthesis ensures that applications benefit from both instruction-level sandboxing and cluster-wide administrative isolation, effectively hardening the microservices architecture.

There is also a a definite difference in speed. Measured in latency and other specs, there can be up to a 40% increase or decrease in latency when comparing legacy Helm 3 plugins to Helm 4 Wasm plugins, according to [ReveCom.](http://www.revecom.io)

Again, the “run once, run anywhere” aspect of Wasm shines here, allowing installation across several different CPU configurations, whether x86, ARM, or others.

With ArgoCD, we haven’t tested it yet, but there would likely be slightly faster specs with Argo, running ArgoCD for the plugin functionality that Wasm offers. However, the Wasm module, as explained above, provides an extra layer of isolation and security. This is not to say that ArgoCD lacks security, but the Wasm plugin adds an additional safeguard for Helm. For the majority of use cases, the performance differences are probably negligible.

## Versus Kubernetes

At first glance, I recall when I asked whether WebAssembly might one day, especially once the component model is finalized, replace Kubernetes to some extent. I would argue that it likely could one day in the distant future, though obviously not completely. However, Helm supporting WebAssembly is not going to help further that possibility. If that day does happen, Helm itself will likely become irrelevant.

[Shivay Lamba](https://www.linkedin.com/in/shivaylamba/?originalSubdomain=in), senior developer experience engineering for Couchbase, largely agreed:

“Helm’s adoption of WebAssembly plugins actually strengthens Kubernetes rather than undermining it. The main motive of the Wasm plugin system for Helm is to help improve the extensibility, security, and maintainability,” Lamba said. “While WebAssembly does introduce a compelling execution and isolation model, Helm using Wasm still assumes Kubernetes as the control plane, scheduler, and lifecycle manager. If WebAssembly were ever to meaningfully replace Kubernetes, it would require a native, Wasm-first orchestration model that removes the need for container-centric abstractions altogether. In that scenario, Helm itself would indeed become less relevant. This new change proposes an evolutionary change, not a revolutionary one. It refines how we extend Kubernetes tooling rather than challenging Kubernetes’ role.”

What we are seeing, though, is a nice added layer of isolation the Wasm Helm plugin offers. The facility to run applications through WebAssembly on Kubernetes has been possible for some time. In fact, if you’re using serverless applications, on the web or on LightXL servers, you might already be using WebAssembly without even realizing it.

What this release does with the plugin, especially if you’re already using Helm, is it significantly reduces the work required to run applications through WebAssembly modules on Kubernetes and containerized infrastructure. In other words, much less work is involved.

“The real value of the Helm Wasm plugin system is pragmatic: it lowers friction. By reducing the operational and cognitive overhead required to run WebAssembly workloads within existing Kubernetes and containerized environments, it makes Wasm more accessible to teams that are already standardized on Helm,” Lamba said. “This aligns well with WebAssembly’s original ‘write once, run anywhere’ promise, not by replacing infrastructure, but by fitting cleanly into it. Importantly, the strong isolation guarantees of Wasm are preserved, while Helm adds familiar packaging, distribution, and lifecycle management. Rather than redefining the platform stack, this release accelerates adoption by meeting developers where they already are.”

One of the creators of Helm, [Matt Butcher](https://www.linkedin.com/in/mattbutcher/), vice president of product management at Akamai Technologies and co-founder, saw the need for a Wasm-like functionality for Helm years ago.

“Back when we were working on Helm 3, we realized we needed to provide our most sophisticated users with a route to customizing the behavior of Helm itself. We investigated using Lua at that time,” Butcher said. “But despite our efforts, we never arrived at a model we liked. Now, several years later, WebAssembly is a better alternative to Lua.”

This helps fulfill one of WebAssembly’s original promises: write your application once, package it as a WebAssembly module, and run it across numerous endpoints, as long as they support the CPU instruction set. At the same time, it continues to support strong isolation.

“You can now write Helm plugins in a wide variety of languages, and get all of the advantages of the WebAssembly runtime: Speed, portability, security, and standards compliance. WebAssembly as a plugin provider has long been a compelling use case, and Helm 4 demonstrates why,” Butcher said. “But this is not the only place we’ll see Wasm in the Kubernetes ecosystem. [CNCF](https://cncf.io/?utm_content=inline+mention) projects like Spin and SpinKube will continue to use WebAssembly for other ends, like serverless functions.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)