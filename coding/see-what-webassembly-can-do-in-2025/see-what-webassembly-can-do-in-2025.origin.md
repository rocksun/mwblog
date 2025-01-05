# See What WebAssembly Can Do in 2025
![Featued image for: See What WebAssembly Can Do in 2025](https://cdn.thenewstack.io/media/2023/12/95c34a5e-year-forecast-1-1024x576.png)
[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) is a compiler on steroids, as I described it a few years ago, irking many proponents. But I would argue that description still holds true, as hopefully by 2025, WebAssembly modules will be able to integrate applications written in the language of your choice deployed across any environment or device running a compatible CPU instruction set. This would enable simultaneous deployment and updates of applications across diverse device types.
Once a niche project at [Mozilla](https://thenewstack.io/mozilla-extends-webassembly-beyond-the-browser-with-wasi/) to a technology integrated across various environments and infrastructures, WebAssembly has grown significantly over the past few years and is in use across various industries.

Early discussions at talks at KubeCon and conferences like [WasmCon](https://events.linuxfoundation.org/wasmcon/) and [Wasm/IO](https://2024.wasm.io/) attracted only a few hundred attendees. In contrast, recent events at these and other conferences such as [KubeCon+CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) have been progressively more packed with attendees actively using and developing WebAssembly, reflecting its increasing relevance in open source communities.

Looking ahead to 2025, it’s anticipated that WebAssembly will see some real adoption beyond the sandbox projects presented at conferences (which are fascinating, more often than not). It may be still be difficult to explain its functionality to laypersons, but there will be more real-world examples showing [what Wasm can do](https://thenewstack.io/amexs-faas-uses-webassembly-instead-of-containers/) as its applications are expected to expand into not only from the browser, but to the server, [serverless computing](https://thenewstack.io/serverless-computing-in-2024-genai-influence-security-5g/), edge deployments and other areas. In some cases, WebAssembly may replace traditional containers and integrate directly with [Kubernetes](https://thenewstack.io/kubernetes/). Then there are the security aspects of WebAssembly that have attracted the attention of the [U.S. government.](https://thenewstack.io/the-feds-push-webassembly-for-cloud-native-security/)

## The Final Mile?
One of WebAssembly’s main features hasn’t been realized yet: a standardization so that applications written in any language that can be distributed through Wasm modules for deployment on any endpoint simultaneously — and asynchronously. Once finalized, a component model will enable WebAssembly to expand its use beyond web browsers and servers. It will allow users to deploy different applications running inside numerous lightweight modules at very high speeds across thousands of endpoints simultaneously.

Much depends on the finalization of a component model and especially its relationship to [WASI](https://thenewstack.io/wasi-preview-2-what-webassembly-can-and-cant-do-yet/), which is the standard interface or API linking the WebAssembly modules to the components. It will support the development of so-called WebAssembly “Worlds,” as groups of compatible Wasm components form an interconnected infrastructure similar to Kubernetes, but without containers. [WASI Preview 2,](https://thenewstack.io/why-wasi-preview-2-makes-webassembly-production-ready/) released in 2024, made some huge strides toward standardization, but we are not there yet. In 2025, we will likely not achieve the Holy Grail, but we could see some pleasant surprises.

Improved WASI and component standards means more languages that can be used with WebAssembly beyond the current stable of Rust, Go and C++.

“In 2025 we need to see tight integration between the WebAssembly System Interface (WASI) and Python, so that every Python developer can write apps that work in Wasm,” [Torsten Volk](https://www.linkedin.com/in/torstenvolk/), an analyst at TechTarget’s Enterprise Strategy Group, said. “This integration is so exciting as it would enable developers to just write reusable Python modules that other developers can pop straight into their own apps. Eliminating the age-old issue of developers continuously recoding already existing programs would be a significant breakthrough in developer productivity.”

Once finalized as soon as in 2025, a component model will enable WebAssembly to not just see its expanding use beyond web browsers and servers, but will be able to allow users to deploy different applications running inside numerous lightweight modules. They are distributed at very high speeds across a few to thousands of endpoints simultaneously through the component interface called World without changing one iota of code, as mentioned above.

Also, as mentioned above, the component model will also enable Wasm to integrate more [programming languages](https://thenewstack.io/programming-languages/).

“From the first day it was announced, WebAssembly’s big gamble was on language support. It’s one thing to build a standard binary format, and it’s altogether different to get dozens of programming languages to compile to that format — yet that’s what has happened with Wasm,” [Matt Butcher,](https://www.linkedin.com/in/mattbutcher) [Fermyon](https://www.fermyon.com/?utm_content=inline+mention) co-founder and CEO, said. “The component model, though, is what takes this binary format to a new level.”

With the component model, a Python developer can use libraries written in Rust and a JavaScript developer can leverage existing Go libraries,” Butcher said. “It no longer matters what the source language was — merely that it was built into a Wasm component.”

## Micro VMs for Edge
The idea of using Wasm modules to serve as lightweight and sandboxed security for edge deployments and management has been around for a while. Called different things depending on the cloud vendor, micro VMs will allow for on-premises or cloud sources to distribute massive amounts of data traffic coming from on-premises systems through the cloud. This is done through very light Wasm modules compared to containers. [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention)Cloud, and others will offer different variations as the standard is worked out in 2025.

“We can now process network traffic as it enters the system using these lightweight sandboxes,” said [Mark Russinovich,](https://www.linkedin.com/in/markrussinovich) CTO and technical fellow of Microsoft Azure, speaking at the [Microsoft Ignite](https://ignite.microsoft.com/) user conference. “This opens up incredible possibilities for real-time, efficient network processing.”

Wasm modules will not replace containers completely, but they will be gradually integrated in cloud native environments to fill in many of the gaps lacking with traditional containers and VMs.

Volk said these will move from the least efficient deployment type — VMs — to the most efficient one —WASM containers — with standard Linux containers being the middle ground.

“I see organizations running VMs, containers and Wasm containers side by side, with Kubernetes acting as the puppet master that takes care of policy compliance, resilience and performance,” Volk said.

In many ways, WebAssembly serves as the missing puzzle piece for deploying and managing network edge devices.

“We are so used to thinking in terms of client and server that edge caught us off guard. It broke us out of our mold,” Butcher said. “With Wasm’s ability to run in just about any environment, our old two-tier client-server model is giving way to a continuum of computing. Edge computing is the keystone of Wasm’s success, and we will see that on full display in 2025.”

## Security is a Real Thing
WebAssembly’s capacity to not only be secure for applications but also serve as a measure of security for applications has been shown to be effective in research papers and other studies over the past few years. However, it hasn’t yet gained significant traction as a standalone security measure.

In 2024, according to a U.S.-government National Institute of Standards and Technology (NIST) paper, “A Data Protection Approach for Cloud-Native Applications,” released earlier this year, WebAssembly could and should be integrated across the cloud native service mesh sphere in particular to enhance security. The framework outlined in the paper may lead to future compliance requirements for WebAssembly or cloud native environments, while also setting the stage for broader use of WebAssembly for security in general.

My prediction is that while we probably won’t see widespread adoption of WebAssembly as a security measure in 2025, this report will likely initiate or prepare the groundwork for serious consideration of how WebAssembly can serve as a security layer, particularly for cloud native applications. So, while WebAssembly may not be required for compliance with U.S. government projects in 2025, it could eventually become a key component in the future.

“Wasm’s tight security can prevent sufficient resource access for many workloads,” Volk said. “But here the Wasm contributors and product vendors have their work cut out for them, as they can prioritize their roadmaps based on what companies are running on standard Linux containers in real life.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)