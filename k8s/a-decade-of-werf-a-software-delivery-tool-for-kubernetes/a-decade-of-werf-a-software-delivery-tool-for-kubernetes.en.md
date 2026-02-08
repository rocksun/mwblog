Various cloud native projects are celebrating their first decade. While there are obvious big names, such as Kubernetes itself, Helm, and Cilium, the ecosystem is much wider and includes lesser-known tools that have been around for a while as well. I’ve been involved in the [werf project](https://werf.io/) since its inception more than 10 years ago, and I’d like to share its story to contribute to a broader picture of the present cloud native world.

What is [werf](https://thenewstack.io/werf-automates-kubernetes-based-gitops-workflows-from-the-command-line/)? Basically, it’s an opinionated, all-in-one command-line interface (CLI) tool for building container images and deploying them to Kubernetes. At this point, you might be wondering why anyone might need it, given that today we already have so many other tools performing similar tasks. Good question! To address it, I suggest diving into the project’s history to understand its peculiarities, reasoning behind it, and evolution.

Werf originated from a Linux-focused DevOps service provider that was challenged by automating numerous container orchestration routines for various customers. It happened in 2015-2016 when containers were already widely used, and [even Kubernetes existed](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/), though it was not yet very popular.

When we talk about running applications as containers, what was the first thing the engineers did with them? They built the images by invoking `docker build` and several other commands. That’s exactly how werf started: Making a wrapper for these actions and improving this process by embedding several enhancements, such as different build stages, smart caching, adding third-party artifacts, and even Chef support. (Again, it was when such configuration management tools were widely used, and this kind of integration seemed natural for the Ops world.)

Importantly, it was not a universal type of wrapper. From its inception, it was a tool strongly focused on automating well-established workflows and, thus, forcing specific views on how the images should be built, tagged, etc. While the approach was opinionated, it was based on real-world experience operating infrastructure, not for a single company but for numerous customers across varying industries and sizes. Facilitating the same best practices for orchestrating containers was the very sense of creating werf, and this ideology has lasted since then.

The next big capability werf got was deployment. After you build a container image, you want to run it in some environment, right? At that time (2017), it was obvious that Kubernetes would be the preferred platform to run containerized workloads, and Helm was already around. Thus, werf used Helm to implement deployment to Kubernetes. It was another core idea of the project: despite being opinionated about how you want to get your work done, the fundamental technologies you’re using to achieve that are mainstream: git, Docker, Helm, Kubernetes… In some way, werf became a “glue” for these technologies — for example, you could execute one command, `werf converge`, to (re-)build your app and (re-)deploy it to Kubernetes.

Over the years, other significant capabilities and best practices were added to werf, such as parallel builds, content-based image tagging, advanced resource tracking during deployment, a sophisticated approach to cleaning up the container registry, bundles for distributing release artifacts, ready-to-use integrations for GitLab CI/CD and GitHub Actions, so-called [Giterminism](https://werf.io/docs/v2/usage/project_configuration/giterminism.html) for hermetic builds, and so on.

Eventually, werf evolved into an all-in-one CLI tool with many features on board, proven over years of production use by its creator and later by many other companies. Another fundamental idea behind the project contributed to this growing adoption.

The creators of werf were heavily involved in open source, as their entire service business was built on deploying, configuring, and maintaining Linux servers and endless other open source software needed for web services. This made werf open source and available on GitHub from the very beginning for both ideological and practical — or should I say professional — reasons.

Interestingly, implementing many features in werf resulted in creating other open source projects that turned out to be helpful on their own. Some of such examples include:

* **[Nelm](https://github.com/werf/nelm)** is a Helm fork that enhances its capabilities in many ways, including advanced resource tracking during deployments, flexible ordering for deployed resources, improved CRDs (custom resource definitions) management, and deployment planning. Today, Nelm is not only used as a deployment engine in werf, but also as a standalone CLI tool on its own by many users.
* **[Trdl](https://github.com/werf/trdl)** is a solution for delivering software updates securely from the git repository to the end user. It is used as a default and preferred way of installing/invoking the werf binary.
* **[Kubedog](https://github.com/werf/kubedog)**is a library to watch and follow Kubernetes resources during deployment. Nelm uses it to track resources, and some other tools benefit from leveraging it as well.
* **[Lockgate](https://github.com/werf/lockgate)** is a distributed locking library for Go.

Seeing that more users adopt werf for their needs and are willing to provide stronger guarantees for the project, we decided to donate it to a trusted foundation. At the end of 2022, werf became a [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF) Sandbox project, signaling to the wider tech community that this tool will stay open source and won’t be owned by a single vendor.

Over the past decade, the cloud native ecosystem has evolved significantly, offering software engineers an impressive variety of tools and solutions. At the same time, werf has undergone a long way from a simple wrapper to a comprehensive solution. Being an opinionated and all-in-one tool, it is mostly focused on specific use cases nowadays, such as other DevOps agencies, organizations that want to ensure strict rules for delivering software in Kubernetes, and just some users who like the principles facilitated by werf. (As a side note, perhaps the werf’s subproject Nelm has more potential for a massive adoption.) Nevertheless, werf is actively used in at least 18,000 projects worldwide today and maintains a robust pace of development, continuously adding unique features for its current and potential users.

For me, the story of werf illustrates how a passionate, consistent development of in-house tooling, coupled with dedication to open source, can benefit a wider engineering community and maybe even inspire others.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/01/e9ced2ec-cropped-5f968fd5-dmitry-shurupov-jpeg-scaled-1-600x600.jpeg)

Dmitry Shurupov is a co-founder of Palark GmbH, a Germany-based DevOps and site reliability engineering agency. He started his open source journey back in 2000 and became so passionate that it never stopped. He enjoys writing technical texts and community...

Read more from Dmitry Shurupov](https://thenewstack.io/author/dmitry-shurupov/)