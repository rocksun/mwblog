# Akamai Picks Up Hosting for Kernel.org
![Featued image for: Akamai Picks Up Hosting for Kernel.org](https://cdn.thenewstack.io/media/2025/03/9883917f-nocc_1-1024x576.jpg)
[Akamai](https://www.akamai.com/) is making a series of announcements today ahead of next week’s KubeCon EU conference in London. Among other news, Akamai today launched an inferencing service for AI applications with additional support for [WebAssembly](https://thenewstack.io/what-is-webassembly-wasm/) (WASM) workloads, and announced that it is now an infrastructure partner for [kernel.org](https://www.kernel.org/), the main distribution system for the Linux kernel source code, and will pick up its hosting and offer cloud computing and content delivery network support.
Akamai says it has signed a multiyear agreement with the Linux Kernel Organization, which itself is managed by the Linux Foundation, to “provide infrastructure services to the project and its global cohort of developers.”

“We’re very committed to open source. We’re built on open source technologies like Linux. We’re heavy kernel users. We’ve been very active in kind of different standards bodies forever,” Akamai SVP of Product Jon Alexander told me. “Open source is very important to Akamai as a company and we want to give back to the community, and supporting the Linux kernel is one way we can do that.”

Chris Aniszczyk, the CTO of the Cloud Native Computing Foundation (CNCF) echoed this. “Akamai has deep roots in the open source community,” he said. “As an important member of CNCF, they have actively contributed to key projects, including OpenTelemetry, Argo, and Prometheus, and donated US$1 million in infrastructure credits for compute infrastructure projects. The support they are providing the Linux kernel further showcases the company’s long-standing stewardship and commitment to the people and software who make open source projects what they are today.”

As for the inference service for AI workloads, dubbed Akamai Cloud Inference, the company is taking an interesting approach by betting on standard RTX 40-series GPUs, which Akamai says allows it to provide better density in its data centers.

“[These chips] have been around for 18 to 24 months now, so relatively old as GPU generations go. But for us, it’s really in that sweet spot of cost and performance, power consumption, and then density that we can get into server chassis. It works really well for us,” Alexander said. “We’ll be rolling out new generations, maybe end of this year, early next year. We’re already testing the next generation of the cards, but we’re really looking for the density that we can we can pack and parallelize workloads.”

Akamai is partnering with Fermyon here to bring that company’s serverless WebAssembly platform to its Cloud Inference platform as well.

Akamai says this will enable developers to query LLMs directly from their serverless, Wasm-based applications that run on its edge network. But what’s maybe even more important, Alexander noted, is that Fermyon’s technology also allows multiple tenants to access the same GPU in a memory-safe way.

It’s still the early days for Wasm in the enterprise, but Akamai hopes to be at the forefront of a developing trend.

Akamai also recently [partnered](https://www.prnewswire.com/news-releases/akamai-and-vast-data-working-to-usher-in-the-era-of-edge-ai-inference-302403897.html) with VAST Data to provide better access to real-time data for these AI applications, and for the container platform that sits at the core of the entire service, Akamai is using the Linode Kubernetes Engine (LKE) and the Akamai App Engine, the company’s [recently announced](https://www.akamai.com/newsroom/press-release/akamai-launches-cloud-agnostic-ready-to-run-application-platform) application platform.

All of this is playing out against the background of Akamai’s current focus of going beyond its content delivery network and into the cloud computing space. Its efforts here include specialized services for some of its core customers (including new video encoding and decoding accelerators it is also launching today, for example), but also going broad with these new AI services and, of course, the Linode cloud, which it acquired in 2022.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)