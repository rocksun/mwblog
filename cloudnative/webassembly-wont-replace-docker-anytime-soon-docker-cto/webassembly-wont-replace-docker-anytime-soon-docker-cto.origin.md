# WebAssembly Won’t Replace Docker Anytime Soon: Docker CTO
![Featued image for: WebAssembly Won’t Replace Docker Anytime Soon: Docker CTO](https://cdn.thenewstack.io/media/2024/11/57d6f08e-justin_cormack-1024x768.jpg)
Does Docker see [WebAssembly](https://thenewstack.io/webassembly-and-kubernetes-go-better-together-matt-butcher/) as a threat?

There is potential value in [WebAssembly](https://www.thenewstack.io/WebAssembly) though it may not be as a replacement to Docker environment itself, commented [Docker](https://www.docker.com/?utm_content=inline+mention) CTO[ Justin Cormack](https://github.com/justincormack) (as well as member of the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention)‘s Technical Oversight Board), taking some time aside with The New Stack at [KubeCon + CloudNativeCon](https://thenewstack.io/cncf-sics-developers-on-kubernetes-patent-trolls/), held last week in Salt Lake City.

Their use cases are slightly different, and each one is valuable.

A lot of the value around WebAssembly is around code isolation and code componentization, he commented. And this is true of Docker as well, though at a different level of granularity.

WebAssembly, and the WebAssembly System Interface (WASI) promises a secure sandbox where code can be safely executed, while programs [can be built using multiple languages](https://thenewstack.io/why-wasi-preview-2-makes-webassembly-production-ready/) using the component model.

And the same can be said for Docker, of course, which allows developers to package their applications so they are not reliant on the host operating system.

With WASM, you can share “really tiny things,” Cormack said. These are libraries that are “well under the application level.”

This level of granularity has its own value.

Developers like to use libraries, but do they always know what is in them? They may download a JavaScript library for calculations, but only to find it carries some surreptitious code for uploading the user’s passwords.

WebAssembly can serve as a solution to this issue by offering “micro-isolation” to limit a library’s range of actions to just those specified by the dev. So, the library can be used for calculations but is blocked from any network access.

An application built with components might use thousands of libraries, Cormack pointed out.

Giving each library its own container would not be the best way to go about isolating all these libraries, Cormack admitted.

## WebAssembley vs. Docker, a Short History
The topic of WebAssembly versus Docker comes up every few years now. But WebAsssembly is still in its infancy, and some say it lacks a [definitive use case](https://thenewstack.io/true-portability-is-the-killer-use-case-for-webassembly/), while Docker and the container ecosystems are flourishing ecosystems. Entire build processes are set upon containers as their foundations. Stateful applications, such as those involving databases, have found a comfortable home in containers.

In 2019, Solomon Hykes argued on Twitter that if WebAssembly were around in the time that he had been formulating Docker, there would be no need for the container technology.

If WASM+WASI existed in 2008, we wouldn’t have needed to created Docker. That’s how important it is. Webassembly on the server is the future of computing. A standardized system interface was the missing link. Let’s hope WASI is up to the task!

[https://t.co/wnXQg4kwa4]— Solomon Hykes (@solomonstre)

[March 27, 2019]
The comment [made waves](https://news.ycombinator.com/item?id=28109699) and Hykes later walked it back a bit, [explaining to InfoWorld](https://www.infoworld.com/article/3600287/can-wasm-replace-containers.html) that:

*That tweet of mine was widely misunderstood. It was interpreted as WebAssembly is going to replace Docker containers. I did not think then that it would happen, and lo and behold, it did not happen, and in my opinion, will never happen. Now that Docker exists and is a standard, WebAssembly and WASI, as cool as they are, are very different. It’s not at all a replacement. It has a very different shape.*
Thus far, WebAssembly has found [its own niches](https://webassembly.org/docs/use-cases/), in particular [frontend-development](https://thenewstack.io/whos-leading-webassembly-adoption-so-far-vendors/) and for, [as NIST suggests](https://csrc.nist.gov/news/2024/nist-has-published-nist-ir-8505), data protection within cloud native computing environments.

## The Docker AI Catalog
Cormack also had time at KubeCon to discuss Docker’s latest initiative, the [Docker AI catalog](https://hub.docker.com/catalogs/gen-ai?_gl=1*6snjn6*_gcl_au*MTkzNjIzNjg0NS4xNzMxNTIyNDgx*_ga*NTg2NzQ3NjU1LjE3MzE1MjI0ODE.*_ga_XJWPQMJYHQ*MTczMTUyMjQ4MS4xLjEuMTczMTUyMjUyMi4xOS4wLjA.).

“We’ve seen more and more people are consuming AI things from Docker, because it’s where they go for AI,” he said. “A lot of developers are exploring AI, and we’ve been working out what we can do to help them because it’s a whole new domain for them.”

The Docker AI catalog [has been designed](https://www.docker.com/blog/accelerating-ai-development-with-the-docker-ai-catalog/) to simplify the process of integrating AI tools, models, and libraries into applications. Documentation has been included with each artifact, along with configuration guides. [For publishers](https://www.docker.com/partners/programs/), Docker provides a set of metrics of usage, allowing them to further refine their tools for customer demand.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)