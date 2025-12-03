Ever been to Kate’s Place? Most likely, you have. You just know it by a different name: Helm.

Helm, an open source package manager for Kubernetes that began as a company hackathon project called Kate’s Place, turned 10 in 2025. At [KubeCon + CloudNativeCon North America](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/), Helm 4 was launched — the first new version in six years.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Why so long between versions? We’ll get to that. But first, [Matt Butcher](https://thenewstack.io/author/mattbutcher/), founder and CEO of [Fermyon Technologies](https://www.fermyon.com/?utm_content=inline+mention), a WebAssembly company acquired this month by [Akamai](https://www.linode.com/?utm_content=inline+mention), told me about the origins of Kate’s Place in this episode of The New Stack Makers

Kate’s Place was a package manager for Kubernetes that Butcher and two other developers created more than a decade ago at a hackathon at his then-employer, Deus. The name was a play on “K8s,” and had a coffeehouse theme. “I think we were calling the packages shots or espressos or something like that,” Butcher said, in this On the Road episode recorded at KubeCon in Atlanta in November.

At stake was a $75 gift card, which the Kate’s Place team won. The next day at the office, Butcher’s phone rang; Deus’ CEO and CTO were on the line.

“And they said, ‘We think this idea of a package manager for Kubernetes is just the right thing at just the right time,’” he recalled. “Kubernetes was just gaining momentum, and nobody was doing anything like that at that point. And so, they said, ’Why don’t we just give you a team and you can go build it?’

And I said, ‘That sounds fantastic. I would love to do that.’ They said, ‘Just one thing. We really hate the name.’”

## WebAssembly Plugins

Once it acquired its new name, [Helm](https://thenewstack.io/get-started-with-the-helm-kubernetes-package-manager/) moved quickly, gaining non-Deus contributors (like [Matt Farina](https://www.linkedin.com/in/matthewfarina/), now chief architect of cloud native at SUSE, who joined Butcher for this episode). The project was announced at the first KubeCon and it was among the first projects to graduate from the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention).

Helm 4, which went live during the most recent KubeCon, was the product of a long gestation. “The first Helm was around for matter of months, and then Helm 2 was about a year,” Farina said. “Then Helm 3 was three years.”

After six year of Helm 3, “you get some design debt, things like that. People get crazy ideas you never envisioned in the past that requires you to make breaking changes in a major version. And so we’ve been working on Helm 4 for a while now.”

The latest version includes modernized logging and dependency management, and WebAssembly plugins for portability.

Previously, Helm’s plugin system executed out to the file system, a method it still supports. “But we run on a lot of operating systems — Linux, Mac, Windows — and then a lot of architectures,” Farina said. “It’s not just ARM Intel. We’ve got like five or six different Linux architectures that we support now.

“So if you’re going to write an extension for that, you need a way to make that portable. And so we’ve kind of churned on different ways we could make it portable over the years. Nothing ever fit. …  then this [WebAssembly](https://thenewstack.io/webassembly-still-expanding-frontend-uses-10-years-later/) thing came along. It became really, really popular. And so in the last year, we figured out how to make WebAssembly-based plugins for Helm.”

Looking ahead, he added, “We re-architected the internals so we can start in [versions] 4.1 ,4.2, 4.3, and start rolling out some really new, nice features around charts and the packages to enable people who are installing applications to have some really neat new ways to control the way it’s installed.”

## Why ‘Boring’ Features Have Impact

Helm 4’s latest upgrades tell a bigger story, Butcher said: how more mature projects have to evolve and adapt as the ecosystem grows and use cases expand.

It’s a virtue of a lot of these highly successful open source projects that say they do one thing very, very well. …  in our case, we’ve striven for years to be a really, really good package manager for Kubernetes.”

But now, “So much of the real work now isn’t defining or redefining what package management is.”

Instead, he added, it’s asking “What are the features that are going to help people get stuff done in more effective ways?”

Features that are now vital include things like logging. “Back when we created Helm, [it] was like, Oh, well, that’s the boring thing that we’re not really going to think about,” Butcher acknowledged. “Now, it’s like, well, if we can build good logging, then the integration with all these other tools will be more uniform. It’s going to save platform engineers and DevOps folks a lot of time and energy.”

Such changes, he said, can be “a time saver, a money saver.”

Butcher added, “It might not win any awards for fanciest, flashiest new feature, but it certainly makes a very real difference in the lives of the Helm users.”

Check out the full episode to learn more about Helm 4, including how the project maintainers weigh [user feedback](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/), and what’s new at Fermyon and SUSE.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/7bbd1cfd-cropped-4b732d2f-heatherjoslyn.jpg)

Heather Joslyn is editor in chief of The New Stack, with a special interest in management and careers issues that are relevant to software developers and engineers. She previously worked as editor in chief of Container Solutions, a Cloud Native consulting...

Read more from Heather Joslyn](https://thenewstack.io/author/hjoslyn/)