Nobody likes waiting around for an app to start, nor database to boot. Certainly not [Vercel](https://thenewstack.io/vercel-goes-all-in-on-vibe-coding-web-apps/). Nor [Prisma](https://www.prisma.io/about).

Vercel’s venture arm has invested in Unikraft, a cloud-hosting company built on the Linux Foundation unikernel technology of the same name. The company raised a $6 million seed round earlier this month, including a bundle from Vercel, a cloud platform for frontend developers. In the deal, Unikraft can also consult Vercel’s expertise at running cloud-based content delivery networks.

And Prisma, a cloud service that offers a [Postgres database system](https://thenewstack.io/how-distributed-postgres-solves-clouds-high-availability-problem/) [serverless](https://thenewstack.io/serverless/) cloud service, has even put the unikernel to work.

In fact, the tiny footprint of a unikernel-based Prisma Postgres instance allowed the company to set up a free tier for curious users.

## How Prisma Uses Unikernels for Database Performance

To run a database, or any time-sensitive application, over a network requires super-low latency and fast boot times.

To get there, Prisma built a tech stack, using [Cloudflare Workers](https://thenewstack.io/cloudflare-launches-workers-unbound-serverless-with-unthrottled-cpu-usage/) edge services running each database inside a dedicated unikernel. The company used [Unikraft](https://github.com/unikraft/unikraft) SDK, based on the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)-backed open source project, to assemble the VMs (through [Docker Compose](https://thenewstack.io/acorn-from-the-eyes-of-a-docker-compose-user/)) and platformed them on [Unikraft Cloud](https://unikraft.com/blog/unikraft-cloud/).

[Unikernels](https://thenewstack.io/why-the-unikernel-might-outpace-generic-linux-for-cloud-native-ops/) are lightweight and single-purpose virtual machines. Each VM has only the application and the minimum amount of kernel needed to run the app.

This approach allows Prisma to run thousands of PostgreSQL instances on a single server and scale them down to zero instances when they are not needed.

“So that allowed Prisma to offer databases at a fraction of the cost per instance,” said [Felipe Huici](https://scholar.google.com/citations?user=hiDoSX0AAAAJ&hl=en), co-founder and CEO of the Unikraft company, and one of the original researchers on the Unikraft project.

[![](https://cdn.thenewstack.io/media/2025/09/53c9487a-unikraft.gif)](https://cdn.thenewstack.io/media/2025/09/53c9487a-unikraft.gif)

## Unikernels vs. Containers: Understanding the Differences

Unikernels gained some prominence about 10 years ago, but were nearly forgotten in the rush of [Docker’s emerging popularity](https://thenewstack.io/docker-fork-talk-split-now-table/).

The two technologies are similar. Both can host applications and supporting libraries. But while containers share the host’s own OS, each unikernel is a “microVM” with its own stripped-down OS.

In design, unikernels are a single-address space binary object: They [do not have](https://unikraft.org/docs/concepts) separation between kernel and user address spaces of a traditional OS. This allows for [much faster execution of applications](https://thenewstack.io/beam-me-up-unikernels/), even compared with traditional container technologies.

The idea of the unikernel arrived at its present state by way of a 2013 paper, “[Unikernels: library operating systems for the cloud](https://dl.acm.org/doi/10.1145/2490301.2451167),” which spawned [MirageOS](https://thenewstack.io/qa-lars-kurth-unikernels/), the first of a number of modern unikernel projects, including Unikraft itself. In 2016, [Docker bought Unikernel Systems,](https://thenewstack.io/dockers-unikernel-purchase-changing-role-os/) which maintained an offshoot of MirageOS. Docker went on to use the technology in its latency-sensitive native applications such as [HyperKit](https://github.com/moby/hyperkit).

But containers were  [such an amazing technology](https://thenewstack.io/shining-historical-lens-containers/) back then, with their ability to make workloads portable, that unikernels seemed unnecessary. Unikernels also required a lot of additional work: Criticisms abounded of inadequate tooling and debugging capabilities. Another non-starter for system architects was the inadequate support of the POSIX standard, the lingua franca of all Linux systems.

## Unikernels for Next-Gen Cloud and AI Workloads

But could a new generation of heavily-distributed cloud applications for the emerging AI market make unikernels worthwhile? This is what Unikraft is betting on. If you are packaging your apps across large numbers of containers, you may want to give unikernels another look, Huici said.

AI workloads, for instance, would be a good fit. They tend to run on large numbers of containers and frequently toggle between being online and offline.

“So if you’re working in infrastructure, you’re having to have many thousands of servers in the data center to cater to millions of millions of very tiny things that are coming up and down all the time. And that’s a big challenge for standard infra,” Huici said.

Huici pointed to how the unikernel image is smaller, faster and more secure than container images, offering boot times in the milliseconds and a throughput 50 to 100% higher than plain vanilla Linux.

## Benefits of Unikernels: Speed, Security and Cost Efficiency

These features neatly solve a number of issues for Prisma. Since [Unikernels](https://thenewstack.io/beam-me-up-unikernels/) boot faster, a new instance is ready in milliseconds rather than the tens of seconds required to boot a containerized version of Postgres. Also, the [security footprint](http://unikernel.org/blog/2017/unikernels-are-secure) is smaller, the unikernels can be customized for performance and they take up less space on the server memory.

In Prisma’s case, a unikernel also eliminates the [cold start problem](https://thenewstack.io/how-to-conquer-cold-starts-for-better-performance/) that can plague microservices and Java applications. It may be cost prohibitive to keep virtual machines or containers running when there is no workload, but booting them down will cause a delay when a new request does come in.

In contrast, the costs for keeping a unikernel running on a server is minimal, thanks to its tiny footprint.

The unikernel architecture also allows Prisma to locate the connection pool on the same machines that run the Prisma Postgres unikernel instances, thereby saving in costly network hops.

## Managing Unikernels with Kubernetes Integration

The Unikraft platform further eases the management burden thanks to a recent integration with Kubernetes, allowing admins to manage unikernels alongside other resources. Each instance operates as a separate node, and you can apply all the Kubernetes scaling logic to these nodes, making them as easy to manage as any other container.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)