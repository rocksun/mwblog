When Redis [changed its licensing](https://redis.io/blog/redis-adopts-dual-source-available-licensing/) in 2024, replacing its permissive [BSD](https://en.wikipedia.org/wiki/BSD_licenses) license with proprietary, source-available alternatives, it prompted a major split in the community. Within days, the Linux Foundation [launched Valkey](https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community), an open source fork.

While Redis did [subsequently change course again](https://thenewstack.io/redis-is-open-source-again/), adding the copyleft [AGPLv3](https://www.fsf.org/bulletin/2021/fall/the-fundamentals-of-the-agplv3) open source license as an option in 2025, [Valkey](https://valkey.io/) was already forging its own path for organizations that wanted a permissively licensed project with independent governance.

Much has happened in the intervening months, with Valkey moving to [reduce its memory requirements](https://thenewstack.io/valkey-91-cuts-memory/), introducing new cluster management and access-control features, and more recently starting to [use AI agents to help](https://thenewstack.io/valkey-ai-backporting-agents/) with maintenance work such as backporting fixes.

But for some Redis users, at least one major migration hurdle remains.

## Proxy access

Redis, for the uninitiated, is an in-memory data store widely used for caching and other workloads where fast access is an imperative. Many applications were built to interact with Redis as though it were a single instance, and moving those applications to a distributed [Valkey Cluster](https://valkey.io/topics/cluster-tutorial/) can mean changing code so it can deal with multiple nodes, routing, and differences in how certain commands behave. Commercial Redis products and some cloud services get around this with proxy layers that sit between the application and the underlying cluster, but companies that want to run [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey") themselves have lacked an equivalent option.

And so [Percona](https://www.percona.com/) is now looking to fill that gap with Valkey-proxy, an open source proxy that allows existing applications to connect to a Valkey Cluster without having to be rewritten.

Percona is an open source database software and services company that supports technologies including MySQL, PostgreSQL, and MongoDB. It’s also one of the companies backing the Valkey project, alongside cloud heavyweights including AWS, Google Cloud, and Oracle.

In an interview at the Linux Foundation’s [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/) conference in Prague, [Kyle Davis](https://www.linkedin.com/in/kyle-davis-linux/), general manager for the Redis/Valkey ecosystem at Percona, says that having to rewrite applications before they can move to clustered Valkey deployments is one of the last big blockers to wider adoption.

> “Right now there’s not really any good open source solution for this.”

“Right now there’s not really any good open source solution for this, and so there’s been this gap,” Davis tells *The New Stack*.

For what it’s worth, there are other proxies out there. Davis points to [Envoy](https://www.envoyproxy.io/) as one example, but says it doesn’t fully understand the Valkey protocol and handles connections in a way that means it can’t support everything Valkey can do.

That leaves some companies caught between older applications built around a single Redis instance, and the clustered Valkey deployments they would need as they grow. Valkey-proxy is designed to bridge that divide.

“Now we can address a whole different layer of applications that really didn’t have a good option,” Davis added.

> “Now we can address a whole different layer of applications that really didn’t have a good option.”

## The case for Valkey-proxy

Percona has developed the first version of Valkey-proxy internally, but the plan is to move it into the Valkey project before opening development up to the wider community.

“From there, we’re going to get a lot of contributions from Percona’s customers, customers from other places, and independent developers,” Davis says.

Asked whether hyperscalers like AWS might also contribute, Davis says “potentially,” but adds that it’s difficult to predict because they often have their own tools tied directly to their services.

That makes Valkey-proxy particularly relevant to organizations that manage their own infrastructure, including those running on premises. Davis says the potential user base ranges from smaller companies with limited resources, to large financial services organizations with strict compliance requirements — businesses that may need greater control over where and how their data infrastructure runs.

Moreover, the proxy could also give the Valkey project somewhere to add other capabilities over time.

> “Filling that missing gap allows us to have more flexibility, and now we can start doing things in a different way.”

“It provides a decoupling layer that in the future we can build other components into,” Davis continues. “Filling that missing gap allows us to have more flexibility, and now we can start doing things in a different way.”

For now, however, the focus is on getting the project into users’ hands. Percona received approval in late September for Valkey-proxy to become part of the Valkey project, and is now moving the code from private repositories into the public project.

The aim is to have all of the source code publicly available by the end of October, followed by a release candidate in December and general availability by early 2027.

Davis says the intervening period will be important for finding edge cases as users begin testing the proxy against their own applications. [Freshworks](https://www.freshworks.com/) will be among the first to do so, and Davis says the company is already working with Percona on Valkey-proxy as an early user and design partner, helping uncover issues as development continues.

“That’s going to be a great test case for it,” he adds.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)