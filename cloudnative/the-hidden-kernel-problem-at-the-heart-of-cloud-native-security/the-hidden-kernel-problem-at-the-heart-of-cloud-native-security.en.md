Most of us in the cloud native ecosystem live in YAML. We live in APIs, orchestration, controllers and container tooling. We live in user space. The [Linux kernel](https://thenewstack.io/linux-6-18-all-about-the-new-long-term-support-linux-kernel/) sits beneath all of that as an invisible force we rarely think about. Our day-to-day work touches Kubernetes abstractions, not page tables or task structs.

From a security perspective, that is a problem. The kernel is the real boundary. Every container, every Extended Berkeley Packet Filter (eBPF) program, every Container Network Interface (CNI) plugin and every isolation feature ultimately reduces to data structures and code paths inside one monolithic Linux kernel. That kernel has become the scaffolding for performance and security across cloud native. When it fails, everything above it fails.

Here is the unsettling part. We have built an entire ecosystem on a component that was never designed for cloud-scale multitenancy and is now one of the fastest-changing and easiest to exploit parts of our infrastructure.

## **The Kernel Containers Inherit Was Never Designed for This**

If you look at the kernel’s view of a container, the magic disappears quickly. A [container is not an isolated capsule](https://thenewstack.io/what-we-wish-we-knew-about-container-security/). It is a process represented by a task struct. It looks almost identical to any other process except for a few pointers to namespaces and cgroups. Those namespaces create the appearance of a separate environment, but the kernel still runs everything through the same schedulers, the same system call table and the same memory-unsafe C code.

This is the fundamental disconnect. From user space, it feels like containers are isolated. From kernel space, a container is mostly a regular process dressed up with some metadata.

We have made real progress in container security over the last decade. Image scanning, signed supply chains, distroless images and eBPF-based runtime visibility are all meaningful improvements. None of that changes the reality that all workloads still share one kernel that was never designed to isolate hundreds of untrusted tenants. That mismatch sits at the center of today’s risk.

## **It Became a CVE Authority and Looked Too Big To Fail**

When the Linux kernel became its own CVE Numbering Authority, it gave the industry a clearer window into how frequently kernel vulnerabilities are discovered. In early 2025, the kernel alone produced over 100 common vulnerabilities and exposures (CVEs) in a couple of weeks, roughly eight per day. These are not image-level issues. They apply to every container running on that node.

Updating images is trivial. [Updating a kernel](https://thenewstack.io/how-ai-helps-maintain-the-linux-kernel/) is not. Kernel upgrades require node-level intervention, often reboots, and carefully staged drains. The blast radius is large, so many teams postpone the work. Over time, nodes accumulate hundreds or thousands of kernel CVEs while continuing to run critical workloads. Combine that with the fact that the kernel is the single shared boundary for the entire cluster, and the risk becomes obvious. If the kernel goes, everything goes.

## **Exploiting the Kernel Has Turned Into an N-Day Problem**

There is still a belief that compromising the kernel requires nation-state talent. In practice, we live in an n-day world. Vendors fix the bug, the CVE is published and the exploit remains effective for months or years because systems are slow to update.

One example we examined was a use-after-free bug in netfilter that was fixed in early 2024, yet was still being used in ransomware campaigns in late 2025. Public repositories provided the exploit code and even prebuilt binaries. Running it inside an unprivileged container granted root on the host. That single action erased every boundary the kernel enforced. At that point, the only safe move is to rebuild the node.

There was no wizardry involved. No deep kernel knowledge. Just a public exploit and an outdated kernel. That is what n-day risk looks like.

## **User Namespaces and Trading One Attack Surface for Another**

User namespaces were enabled by default in Kubernetes and widely celebrated as an isolation win. Inside a user namespace, a process appears as root but maps to an unprivileged user outside. It sounds elegant in theory.

The kernel does not know or care about that theory. It simply sees a process with elevated privilege. That expanded privilege exposes kernel code paths that the process could not reach before. Many recent kernel exploits depend on user namespaces for exactly this reason. They trade one attack surface for another. User namespaces solve real problems, but they also widen the entry points available to hostile code. They are [a trade-off](https://thenewstack.io/beyond-namespaces-why-kubernetes-needs-real-workload-isolation/), not a security cure.

## **What We Can Realistically Do About a Shared Kernel**

Kernel hardening work is real and valuable. Projects like the Kernel Self-Protection Project improve memory safety and reduce common exploitation techniques. These efforts operate on a very different threat model: one user, one machine, mostly trusted code. Kubernetes assumes the opposite. Hardening helps, but it cannot eliminate the underlying architectural risk of a shared kernel.

There are still practical steps. Seccomp can remove broad categories of system calls. Blocking the unshare system call prevents many user namespace-based exploits. Avoiding privileged containers and unnecessary host mounts reduces exposure. These are meaningful defenses before exploitation. None helps after the kernel is compromised.

The longer-term answer is structural. A shared kernel is like a ship with no watertight compartments. One breach floods the entire vessel. Stronger isolation models contain blast radius by giving workloads their own kernels or isolation domains. Public cloud hypervisors have proven that this works. Apple’s containerization framework shows the same principle applied to local development environments. The pattern is clear.

## **Closing the Last Trust Gap in Container Security**

The cloud native community has made enormous strides. Defaults are safer, supply chains are cleaner and runtime visibility is better than it has ever been. Kernel security has improved, too, thanks to dedicated engineers doing extremely difficult work.

The point is not that Linux is broken. The point is that our trust boundaries need to reflect reality. A shared kernel is too powerful and too complex to assume safety by default. If we combine the progress we have already made with a clearer understanding of kernel risk and stronger isolation approaches, we can close the last major gap in cloud native security. It is time to bring the kernel into the conversation.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/06/e1cc02aa-cropped-4c803797-screenshot-2025-06-09-at-10.04.53%E2%80%AFam.png)

Jed Salazar is field CTO at Edera.

Read more from Jed Salazar](https://thenewstack.io/author/jed-salazar/)