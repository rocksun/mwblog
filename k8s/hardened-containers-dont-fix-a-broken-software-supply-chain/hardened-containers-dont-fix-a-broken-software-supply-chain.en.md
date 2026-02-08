The software supply chain is broken, and the recent explosion of hardened container offerings is the industry’s reaction.

A few years ago, secure container images were a niche concern. Today, they’re everywhere. The industry has responded by tightening inspection at the end of the assembly line (more checks, more scanners) while largely ignoring how the parts get sourced, assembled, and verified upstream.

The company I co-founded started working on software [supply chain security](https://thenewstack.io/securing-the-software-supply-chain-a-2035-blueprint/) four years ago, well before [hardened containers](https://thenewstack.io/hardened-containers-arent-enough-the-runtime-security-gap/) were a category. What the past year has made clear is that hardened containers are valuable, but they’re not the problem the industry should be trying to address. The real issue is about trusting where software comes from, and why building open source software directly from source is the only way to secure the entire software supply chain.

## **The benefits and pitfalls of hardened containers**

Containers succeeded because they made developers faster, not because they made systems safer. Docker took off because its early decisions and defaults prioritized flexibility, but they were the opposite of what you’d want from a security perspective: The default user is root, shells are everywhere, package managers are everywhere, and the Docker Hub “Official Images” have been a security nightmare for pretty much their entire existence. Security became something you handled later, typically by scanning and patching whatever appeared in production.

That “we’ll fix it later” mindset is how post hoc hardening became the norm. It requires teams to patch vulnerabilities, strip binaries, rebuild images, change configs, run policy images, and repeat these steps over and over again. It’s hard work, and for many organizations it’s necessary. But it treats the symptom, not the disease.

Hardening an image doesn’t answer the most important question: Do you actually know where the software inside it came from?

Much of today’s container ecosystem is built from opaque binaries, ad hoc build pipelines, and [Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/ "Dockerfiles") that were never designed to be reproducible or auditable.

I ran into this problem firsthand years ago while working on [Google](https://cloud.google.com/?utm_content=inline+mention)’s Distroless project. The goal there was simple: Produce minimal, production-ready container images without shells, package managers, or unnecessary attack surface. What we learned quickly was that you can’t get there reliably by hardening artifacts after the fact. You have to control how the software is built in the first place.

## **The false promise of a ‘hardened containers’ market**

Over the past year, a growing number of vendors have entered the market offering some flavor of “hardened containers.” This has helped force a long-overdue conversation. More organizations now recognize that the status quo for consuming open source software isn’t sustainable, and that’s a good thing. However, all of these companies have emerged with a singular focus on zero common vulnerabilities and exposures (CVEs) and hardened containers. While hardened containers are important, most vendors are fixating on them because it’s easier than fixing the software supply chain.

Broadly speaking, there are two approaches to the “hardened containers” market: 1) post hoc hardening and 2) from-source builds.

Our approach is from-source builds, with some configurations producing hardened containers. We didn’t start by trying to harden existing images; we started by reimagining how software gets built in the first place. Today, we build open source from source, inside a full distro with the automation required to securely build everything. It was the only honest way to secure the entire supply chain, and hardened containers emerged because customers needed them. But they were an outcome, not the goal.

Much of the current market still revolves around hardening artifacts after the fact. But it’s not possible to provide hardened containers with real software choice without from-source builds and your own distro. The downside, people say, is that you need your own distro. I don’t think that’s a downside at all. There’s no other honest way to do it. And besides, you’re already locked in by using a hardened image — to opaque binaries, abandoned images, and ad hoc build pipelines no one remembers how to reproduce.

Ultimately, focusing exclusively on hardened containers misses the bigger point. Even the name is wrong: It implies you’re taking something sketchy and trying to fix it after the fact.

## **Redirecting the focus to software supply chain security**

Our customers rely on hardened containers, so they’re not going anywhere. But the real issue is whether unmanaged software supply chains are sustainable in a world where open source moves this fast and at this scale. At some point, organizations either know how their software was built and maintained, or they shouldn’t ship it.

As we look to the next year, there are several trends I predict will shape the industry:

The current rush to harden container images is understandable. But long-term security doesn’t come from tightening controls at the end of the process. It comes from being able to trust how software is built in the first place.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/41b6fad6-danlorenc.jpg)

Dan Lorenc is co-founder and CEO of software supply chain security company Chainguard. Dan has been working on and worrying about containers since 2015 as an engineer and manager. He started projects like Minikube, Skaffold and Kaniko to make containers...

Read more from Dan Lorenc](https://thenewstack.io/author/dan-lorenc/)