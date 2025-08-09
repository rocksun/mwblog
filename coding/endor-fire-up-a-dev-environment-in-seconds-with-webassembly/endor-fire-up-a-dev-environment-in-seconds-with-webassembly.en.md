Newly launched [Endor](https://thenewstack.io/endor-webassembly-based-server-in-the-browser/) allows developers to create reproducible, isolated testing environments in a few seconds instead of hours or days, thanks to [WebAssembly](https://thenewstack.io/webassembly/)’s lightning-fast speeds.

This capability is especially important in the era of asking questions to [ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/), running agents and [vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/), allowing developers to quickly and securely test that code, Endor’s developers say. Endor provides a way to do so both in the browser and the command line.

WebAssembly is the underlying technology that allows for this to happen, though most developers probably won’t care about the details. WebAssembly offers the lightning-fast speed at which this platform boots up and functions, enabling a [Linux shell](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) to be created on [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) in just a few seconds instead of hours if you’re setting up a testing environment for development purposes.

Some of the advantages of Endor include consistency across platforms and stateless, reproducible environments. This means the environments will run the same regardless of the operating system (though ReveCom only tested in MacOS for this article) and don’t depend on specific libraries being present on the system.

Of course, there is the famous sandbox environment of WebAssembly that protects the system while running these little or large programs as you deem fit. Environments don’t interfere with or conflict with existing dependencies and configuration files on the host machine you’re working with, because file system access and networking are disabled by default.

This extends Endor’s usage to allow for running risky or even insecure code — or destructive chaos tests — without worrying about interfering with or causing problems on the host machine. It also means that when you’re collaborating on a project as a developer, everyone has the exact same testing environment.

Endor WebAssembly-based environments run entirely locally, whether in the browser or in the command line. That means that there are no remote servers, and your code and scripts never leave your machine. However, this also means that performance will be limited by the local CPU and memory.

## Set up and Run

Getting started with Endor as a developer simply consists of accessing the Endor server and installing the shell. On a Mac, at least, it’s advisable to first install Endor using Homebrew:

[![](https://cdn.thenewstack.io/media/2025/07/6640ce68-screenshot-2025-07-31-at-9.11.23%E2%80%AFam.png)](https://cdn.thenewstack.io/media/2025/07/6640ce68-screenshot-2025-07-31-at-9.11.23%E2%80%AFam.png)  
Then access your favorite console — whether you’re on a Mac, PC, or Linux machine — and now you have a working copy of [Alpine Linux](https://thenewstack.io/wizos-a-new-enterprise-linux-built-on-alpines-secure-foundation/) running locally on your machine.

[![](https://cdn.thenewstack.io/media/2025/07/be839b25-screenshot-2025-07-31-at-9.16.36%E2%80%AFam-1024x409.png)](https://cdn.thenewstack.io/media/2025/07/be839b25-screenshot-2025-07-31-at-9.16.36%E2%80%AFam-1024x409.png)

Add your program or code:

[![](https://cdn.thenewstack.io/media/2025/07/cf09abf4-screenshot-2025-07-30-at-10.07.18%E2%80%AFpm-1024x362.png)](https://cdn.thenewstack.io/media/2025/07/cf09abf4-screenshot-2025-07-30-at-10.07.18%E2%80%AFpm-1024x362.png)

And here I’m watching a geeky version of “Star Wars”:

[![](https://cdn.thenewstack.io/media/2025/07/4c78822f-screenshot-2025-07-31-at-9.17.55%E2%80%AFam-1024x405.png)](https://cdn.thenewstack.io/media/2025/07/4c78822f-screenshot-2025-07-31-at-9.17.55%E2%80%AFam-1024x405.png)

[![](https://cdn.thenewstack.io/media/2025/07/e8dc6755-screenshot-2025-07-31-at-9.18.11%E2%80%AFam-1024x524.png)](https://cdn.thenewstack.io/media/2025/07/e8dc6755-screenshot-2025-07-31-at-9.18.11%E2%80%AFam-1024x524.png)

Independently developed by former Bitnami co-founder and developer lead, Endor co-founders CEO [Daniel Lopez Ridruejo](https://www.linkedin.com/in/ridruejo/) and CTO [Angel de Miguel](https://x.com/_angelmm), Endor represents a major milestone or step in WebAssembly’s utility and accessibility, as it is ready to run now for end users.

It’s especially relevant for backend and server aspects of WebAssembly, which developers can use hands-on, as opposed to its use over the past several years in the browser, for which it was originally created, and for cloud infrastructure applications such as lowering latencies using microVMs and improving isolation with Azure’s Hyperlite.

## Wasm Days

WebAssembly has demonstrated its power with extremely fast start times, security advantages and other capabilities. Initially designed for the browser, it is now extending to the server and the edge as the WASI component standards take shape.

During the [Wasm I/O conference](https://2025.wasm.io/) held in Barcelona earlier this year, where Endor was unveiled, it was shown how Endor takes advantage of WebAssembly’s various capabilities and individual services to be combined into a structured environment enabled entirely within the browser or a remote server. There is nothing to download — yet a full server and development environment capability is available directly in the browser. These server capabilities that can be launched and managed in milliseconds thanks to Wasm include databases, web servers and language runtimes that take advantage of browser improvements in storage, networking and compute capabilities.

At Wasm I/O, Lopez Ridreujo and de Miguel presented a demo and discussed Endor, which is built on [Emscripten](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/) and other open source technologies. Both emphasized their commitment to contributing to the open source community as part of this initiative.

“With the use of AI and agentic coding systems, there is an increasing need to provide development environments on demand,” Lopez Ridreujo said. “Endor makes it easy to do so both in the command line and in the browser.”

## Power of the Link

Originally created to run applications in the browser, WebAssembly as a compiler on steroids now extends applications to run across networks, devices, servers and other environments at very fast speeds and with very low latency specs. With Endor, components required to run server applications and development platforms are in the browser.

“The power of the link means that if someone needs to access something, you send them a web address and it works. It makes it easy to share.” Lopez Ridruejo said during Wasm I/O. “We wanted to capture that magic with Endor, just visit a web address or type this one line in the terminal and you have a development environment up and running.”

Various technologies, such as [Python](https://thenewstack.io/what-is-python/), [Ruby](https://thenewstack.io/why-ruby-on-rails-is-still-worth-your-while-as-a-developer/) and [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/), are already being used and distributed with WebAssembly, Lopez Ridruejo said. “Slowly but surely, WebAssembly continues to make inroads in many aspects of development, being a viable alternative to Docker and other technologies for an increasing number of use cases,” de Miguel said. “Endor is just one example of this trend.”

Additionally, unlike traditional servers, Endor’s browser capabilities do not rely on a dedicated server. Instead, a sandbox environment is integrated into the browser itself.

## Everything Runs on the Browser

For developers, Endor’s approach does not rely on traditional virtual machines (VMs). Instead, everything runs on the browser or inside Node for the command line version. Some components, like [PHP](https://thenewstack.io/the-herd-is-strong-php-and-its-developer-ecosystem-at-30/), are compiled directly to Wasm code, while others like [MySQL](https://thenewstack.io/linux-back-up-a-mysql-database-from-the-command-line/) may be running as Linux containers in a Wasm-based hardware emulator. The different pieces are then networked using a virtual TCP/IP network inside the browser. Applications like [phpMyAdmin](https://www.phpmyadmin.net/) can then be deployed on top of it, either by mounting a folder from the local filesystem or cloning a GitHub repository.

By leveraging this technology, tasks traditionally performed on a Linux VM running VirtualBox, [Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) or similar tools can be executed within the browser or a Node environment, Lopez Ridruejo said. Users no longer need to manually install MySQL or configure Docker containers. Instead, they can simply click a button to start MySQL instantly. This approach is more convenient and accessible compared to traditional development workflows, Lopez Ridruejo said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)