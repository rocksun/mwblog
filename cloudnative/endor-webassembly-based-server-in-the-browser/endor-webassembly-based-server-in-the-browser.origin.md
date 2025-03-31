# Endor: WebAssembly-Based Server in the Browser
![Featued image for: Endor: WebAssembly-Based Server in the Browser](https://cdn.thenewstack.io/media/2025/03/aa6767f2-getty-images-6dnmfeeaht0-unsplash-1024x683.jpg)
BARCELONA – [WebAssembly](https://thenewstack.io/webassembly/) has demonstrated its power with extremely fast start times, security advantages and other capabilities. Initially designed for the browser, it is now extending to the server and the edge as the [WASI](https://thenewstack.io/why-wasi-preview-2-makes-webassembly-production-ready/) component standards take shape.

During the [Wasm I/O conference](https://2025.wasm.io/) held here this week, it was shown how WebAssembly’s various capabilities and individual services can now be combined into a structured environment enabled entirely within the browser. There is nothing to download — yet a full server and development environment capability is available directly in the browser. These server capabilities that can be launched and managed in milliseconds thanks to [Wasm](https://thenewstack.io/wasm-spin-and-spinkubes-rocky-road-to-cncf-sandbox-status/) include databases, web servers and language runtimes that take advantage of browser improvements in storage, networking and compute capabilities.

It’s called Endor and is largely built on open source. Angel de Miguel and

[@vomkriege]explained at[@wasm_io]how you can leverage Wasm and the browser to build a « dream programming environment. » The browser becomes a computer and overcomes many resource constraints[@thenewstack][pic.twitter.com/4Tan3x3h69]
— BC Gain (@bcamerongain),March 27, 2025
At Wasm I/O, Endor CEO [Daniel Lopez](https://x.com/vomkriege?ref_src=twsrc%5Etfw) and CTO [Angel de Miguel](https://x.com/_angelmm), co-founders of the project, showcased their work. They presented a demo and discussed their project, Endor, which is built on [Emscripten](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/) and other open source technologies. Both emphasized their commitment to contributing to the open source community as part of this initiative.

“Nowadays the hardest part to get started with server software is setting up and configuring everything properly. We built Endor to make it trivial for developers to be up and running with their favorite stack,” Lopez told me. “You just need a browser — it can’t get easier than that.”

## Power of the Link
Originally created to run applications in the browser, WebAssembly as a compiler on steroids now extends applications to run across networks, devices, servers and other environments at very fast speeds and with very low latency specs. With Endor, components required to run server applications and development platforms are in the browser.
“The power of the link means that if someone needs to access something, they don’t need to install anything. They can just visit the web address and it works, it makes it incredibly attractive for sharing,” Lopez said during Wasm I/O. “Now, with just a link, users can run databases, execute PHP code, and perform various tasks. This convenience is both magical and useful.”

Various technologies, such as Python, Ruby and PostgreSQL, are already being used and distributed with WebAssembly, Lopez said.

“The most important aspect of servers is the software that you can run on them. The ability to build solutions to access file systems or networks is irrelevant if the necessary applications are not available. In 2025, server software development primarily involves Docker containers, Linux and package management systems,” De Miguel said. “Our demonstration of Endor showcased an approach that integrates multiple open source components to create a seamless experience, from cloning a GitHub repository to deploying that application, all without leaving the browser.”

Additionally, unlike traditional servers, Endor’s browser capabilities do not rely on a dedicated server. Instead, a sandbox environment is integrated in the browser itself.

## Everything Runs on the Browser
For developers, Endor’s approach does not rely on traditional virtual machines (VMs). Instead, everything runs on the browser. Some components like PHP are compiled directly to Wasm code, while others like [MySQL](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/) may be running as [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) containers in a Wasm-based hardware emulator. The different pieces are then networked using a virtual TCP/IP network inside the browser. Applications like phpMyAdmin can then be deployed on top of it, either by mounting a folder from the local filesystem or cloning a GitHub repository.

By leveraging this technology, tasks traditionally performed on a Linux VM running [VirtualBox](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/), [Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) or similar tools can be executed within the browser, Lopez said. Users no longer need to manually install MySQL or configure Docker containers. Instead, they can simply click a button to start MySQL instantly. This approach is more convenient and accessible compared to traditional development workflows, Lopez said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)