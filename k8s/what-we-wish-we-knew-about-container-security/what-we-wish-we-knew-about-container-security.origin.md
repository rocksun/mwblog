# What We Wish We Knew About Container Security
![Featued image for: What We Wish We Knew About Container Security](https://cdn.thenewstack.io/media/2025/06/a8e5422e-lock-1024x681.jpg)
If you had asked us a few years ago what [container security](https://thenewstack.io/container-security-101-a-guide-to-safe-and-efficient-operations/) was all about, we would have focused on software supply chain risks. We would have talked about malicious images, vulnerable dependencies and compromised registries. Those threats are real, but we’ve since come to understand that they only represent a small part of the bigger picture.

The deeper issue is architectural. It’s not just about what’s inside the [container](https://thenewstack.io/year-in-review-containers-get-smaller-faster-more-secure/), but also about the boundary that surrounds it. We once believed that namespaces, cgroups and seccomp provided strong [isolation](https://thenewstack.io/google-investigates-a-new-approach-for-workload-isolation/). What we’ve come to realize is that this belief was based on a dangerous misunderstanding. The Linux kernel that underpins container runtimes is a shared surface, and trusting it to provide isolation between tenants has created serious security blind spots.

This article explores what we’ve learned the hard way about container isolation. We want to share why that insight matters, because the moment you stop assuming the boundary is secure is the moment you start designing systems that truly are.

**The Unix Roots of Linux Security**
Unix was designed with elegance in mind. It gave us foundational ideas like “everything is a file” and “fail fast.” But it wasn’t built for multitenant workloads. And it certainly wasn’t built for running hostile code from unknown sources.

Linux inherited this lineage. It started as a desktop operating system and evolved into the backbone of the modern cloud. Yet it still reflects its roots. The kernel is permissive by default. It was never intended to serve as a hardened boundary between mutually untrusting workloads. Its security model has been retrofitted over time rather than designed with isolation as a first principle.

Today, the Linux kernel spans over 40 million lines of code. Every container shares it. Every namespace, cgroup and security module ultimately runs through this same monolithic layer. That’s a lot of trust to place in an aging foundation.

**Containers: An Abstraction That Leaks**
Containers became popular because they made it easier to package, deploy and scale applications. Orchestration systems like Kubernetes built a whole ecosystem around this abstraction. But that abstraction is thin. Containers are not a separate runtime; they are just processes.

Each container maps to a process ID in Linux. The illusion of separation is created using kernel namespaces. These namespaces hide resources like filesystems, network interfaces and process trees. But the kernel remains shared. That shared kernel becomes the attack surface. And in the event of a container escape, that attack surface becomes a liability.

Common attack vectors include exploiting filesystem mounts, abusing symbolic links or leveraging misconfigured privileges. These exploits often target the host itself. Once inside the kernel, an attacker can affect other containers or the infrastructure that supports them. This is not just theoretical. Container escapes happen, and when they do, everything on that node becomes suspect.

**Why Namespaces Are Not Isolation**
There is a critical difference between limiting what a process can see and enforcing what a process can do. Namespaces do the former; true isolation does the latter.

In Linux, namespaces, cgroups and seccomp filters work together to create the appearance of containment. But they all run on top of the same kernel. If that kernel is compromised, those boundaries collapse. There is no cryptographic guarantee or hardware-enforced separation.

This leads to a few very real consequences:

- A single compromised container can affect everything else on the host.
- Breach remediation often means tearing down entire clusters.
- Many teams operate under a false sense of security.
As the increasingly popular saying goes: Containers don’t contain.

**Rethinking the Boundary: What Virtual Machines Taught Us**
Before containers, we used virtual machines to isolate workloads. Each virtual machine had its own kernel. Hypervisors created strong boundaries between workloads, preventing one tenant from affecting another.

Virtual machines fell out of favor because of performance overhead and slow startup times. But many of those drawbacks have since been addressed. Projects leveraging paravirtualization, for example, now offer performance comparable to containers while restoring strong workload isolation.

Paravirtualization modifies the guest OS to interact efficiently with the hypervisor. It eliminates the need to emulate hardware, reducing latency and improving resource usage. Several open source projects have explored this space, demonstrating that it’s possible to run containers within lightweight virtual machines. These systems preserve compatibility with Kubernetes and require minimal changes to application workflows.

In effect, they allow you to run each container — or even each pod — in its own hardened zone. These zones eliminate shared kernel state and reduce the blast radius of any exploit. While there is some overhead, it is minimal. In many cases, startup times increase by less than a second. That’s a small price to pay for true isolation.

**Isolation Layers: eBPF, Observability and Sandboxing**
Isolation isn’t just about running workloads in separate environments. It’s also about knowing what they’re doing and being able to control their behavior.

This is where technologies like eBPF come in. eBPF allows safe, sandboxed programs to run inside the Linux kernel. These programs can observe system calls, enforce security policies and emit logs without requiring user-space agents.

Tools built on eBPF, such as advanced observability and runtime enforcement platforms, allow teams to monitor and react to behaviors in real time. They don’t stop an attacker from entering the system. But they drastically reduce the time it takes to detect and respond.

Other isolation techniques include syscall sandboxing, filesystem gating and minimal privilege enforcement. Some projects offer hardened container runtimes that integrate these techniques, making it harder for an attacker to escape or escalate privileges.

Together, these efforts are reshaping the idea of what container security really means. It’s no longer just about images and vulnerabilities; it’s about control, visibility and trust boundaries.

**What Comes Next**
We’re entering a new phase of cloud native security. The focus is shifting from detection to prevention, from monitoring to enforcement. Here are some of the big trends emerging:

- Secure-by-default runtimes are becoming more practical. They offer hardened boundaries without requiring developers to change the way they build applications.
- Infrastructure is becoming more composable. Observability, networking and security are merging into a single policy layer.
- GitOps workflows are being extended to include security posture. Security is becoming part of versioned, auditable infrastructure definitions.
The kernel is no longer the final boundary. It is now one component in a layered, programmable security model.

**Isolation Is the Most Important Problem You’re Not Solving**
We built the cloud on speed and scale. Now we’re realizing that speed without safety is a risk we can’t afford. Containers changed the way we think about deployment, but they didn’t solve isolation. In many ways, they obscured the problem.

What we wish we had known is that security doesn’t begin and end with the code inside the container. It begins with the environment it runs on — and how well that environment keeps everything else out.

The real work of container security isn’t just patching CVEs or scanning registries. It’s rethinking what it means to be isolated.

And here’s the big question: In a world of fast-moving workloads, shared infrastructure and ever-evolving threats, is isolation the new scalability? It might be the most important primitive in distributed computing that we still haven’t gotten right.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)