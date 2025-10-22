Kubernetes namespaces are one of the most familiar tools in the platform engineer’s toolkit. In [an article](https://thenewstack.io/namespaces-a-step-by-step-guide-to-kubernetes-isolation/) published on The New Stack, namespaces were presented as a step-by-step guide to achieving container isolation, a perspective that reflects how many teams use them today.

The term “isolation,” however, is doing a lot of heavy lifting in that framing. Namespaces deliver logical separation, but they don’t enforce the kind of [hardened boundaries](https://thenewstack.io/hardened-containers-arent-enough-the-runtime-security-gap/) that stop workloads from interfering with one another at runtime.

This distinction isn’t just semantic — it’s architectural. And in today’s world of multitenant clusters, AI-driven workloads and GPU sharing, it’s a distinction that determines whether your cluster can withstand a breach or collapse like a house of cards.

## Namespaces Partition, They Don’t Isolate

Namespaces provide developers and operators with an elegant abstraction: They let multiple teams or tenants share a cluster without stepping on each other’s resources. They enforce quotas, enable role-based access control (RBAC), and allow policies to be scoped more cleanly. This is invaluable in reducing administrative chaos.

But namespaces don’t change the fundamental fact that all containers running on the same node share the same kernel. A compromised container in one namespace still has the potential to attack the kernel, exploit shared devices or snoop on GPU memory because the kernel itself is the shared surface.

Amber Wolf’s [piece on namespace boundaries](https://blog.amberwolf.com/blog/2025/september/kubernetes_namespace_boundaries/) underscores this point with real-world examples. When a tenant admin is given full namespace control, they often still retain avenues to affect the entire cluster. Red-team experience shows namespace boundaries don’t hold under pressure. They are policy constructs, not security barriers.

This distinction matters because we often talk about namespaces and isolation as if they’re interchangeable. They aren’t. Namespaces provide partitioning. Isolation is about constraining workloads so tightly that even if one is compromised, it cannot reach across boundaries.

## Namespaces Alone Aren’t Enough for Multitenant Security

The limitations of namespaces show up starkly in modern attack patterns. Container escapes and kernel-level vulnerabilities illustrate the problem:

* **GPU escapes:** Wiz [documented NVIDIA vulnerabilities](https://edera.dev/stories/the-principle-of-isolation) that let attackers escape container boundaries by exploiting hooks and environment variable handling. Namespaces did nothing to stop this because the attack executed against the shared kernel state.
* **Privilege escalation:** Once inside the kernel, attackers can escalate privileges, compromise neighboring workloads and move laterally across nodes.
* **Blast radius:** In a namespace-only model, a single compromised pod can trigger cascading failures that affect every workload on the node. In regulated industries or SaaS multitenancy, that’s unacceptable.

Security models that treat namespaces as hardened boundaries are leaning on a dangerous misconception: that logical separation equals runtime isolation. The moment a container breaks into the kernel, all bets are off.

## A Historical Parallel: VMs vs. Containers

It’s worth remembering that virtualization solved this problem decades ago. Virtual machines (VMs) enforced hard boundaries by giving each workload its own kernel. One VM couldn’t trivially interfere with another. Containers traded this away for speed, density and agility — and those trade-offs were rational at the time.

But times have changed. Lightweight virtualization and hypervisor-backed runtimes have eroded the performance gap that once made VMs less appealing. [Paravirtualization and type-1 hypervisors](https://edera.dev/stories/what-the-f-ck-is-paravirtualization) now offer near-native performance while restoring the strong isolation properties that namespaces lack.

Apple recently [validated this approach](https://thenewstack.io/what-you-need-to-know-about-apples-new-container-framework/) with its new Container Framework, which runs containers inside VM-backed boundaries. Projects like Kata Containers, Firecracker and newer hardened runtimes like Edera’s bring the same principle to Kubernetes. The lesson is clear: We don’t have to choose between speed and security anymore.

## Why Namespaces Fail as Security Boundaries

To see why namespaces don’t equate to isolation, we need to dive into the Linux kernel itself.

* **Namespaces** hide resources like process IDs, filesystems and network interfaces. They change what a container sees.
* **Cgroups** control how much CPU or memory a container can consume. They regulate how much a container uses.
* **Seccomp and AppArmor** restrict system calls or enforce profiles, but they’re still operating inside a shared kernel.

None of these mechanisms prevent one compromised container from attacking the kernel or leveraging vulnerabilities to affect other tenants. At best, they limit visibility and resource usage. They don’t provide the cryptographic or hardware-backed guarantees that modern workloads require.

Contrast that with hypervisor-level isolation:

* Each container (or pod) runs in a lightweight VM with its own kernel.
* No shared kernel state means an escape exploit in one VM doesn’t expose the host or other tenants.
* GPU and device access can be virtualized, eliminating side-channel leakage between workloads.

This is the difference between partitioning and protection.

## Case Study: CVE-2025-23266

Consider [CVE-2025-23266](https://edera.dev/stories/how-edera-eliminates-cve-2025-23266-container-escapes), a three-line NVIDIA container escape that allowed attackers to achieve host-level compromise. The exploit worked because privileged hooks executed inside a shared kernel context. A malicious container could inject a library via `LD_PRELOAD` and escape instantly.

With namespaces alone, this attack succeeded. With hypervisor-level isolation, it would have been contained. The malicious library would never touch the host kernel — it would only affect the isolated guest. This single example highlights why namespaces can’t be the last line of defense.

## The Rise of Hardened Runtimes

This is where hardened runtimes come in. A hardened runtime flips the model by:

1. **Enforcing true execution isolation** – sandboxed zones with separate kernels, no implicit access to peer containers or devices.
2. **Minimizing attack surfaces** – stripping away unnecessary privileges, blocking unscoped syscalls and eliminating host visibility.
3. **Containing threats in real time** – severing network access or pausing execution when anomalies occur.

The result is that entire categories of attacks — privilege escalation, lateral movement, kernel escapes — are structurally impossible, not just harder to detect.

## Why This Matters for AI and GPU Workloads

AI has made solving this problem more urgent. AI agents don’t just analyze data, they execute code, hold credentials and interact with internal systems. GPUs, meanwhile, are shared across multiple tenants and workloads, often with exposed drivers and memory interfaces. Side-channel leakage is not theoretical here; it’s already been demonstrated in practice.

When namespaces are the only control, AI workloads remain vulnerable to the same class of escapes and escalations that have plagued traditional container environments. A hardened runtime with true isolation boundaries is the only way to protect against these risks at scale.

## A Clearer Conversation About Isolation

So where does this leave us? Namespaces are essential: They organize clusters, enforce policies and keep multiteam operations manageable. But they should not be confused with isolation. If Kubernetes is the contract between developers, infrastructure engineers and security teams, then namespaces are the administrative clauses. True isolation, however, is enforced in the runtime.

As an industry, we need to stop conflating these two. Logical separation is not the same as runtime protection. The former reduces clutter; the latter prevents breaches.

The good news is, we don’t need to abandon Kubernetes or containers to get there. Lightweight virtualization, hardened runtimes and hypervisor-backed containers already exist, and they integrate seamlessly with Kubernetes APIs. The technology is here. What’s needed is clarity and the will to shift the way we think about isolation.

## Partitioning vs. Protection

To build secure, resilient infrastructure, we need to reset the conversation. Namespaces are valuable, but they don’t isolate. True isolation requires architectural boundaries that operate at runtime, not just at the control plane.

The next time someone says namespaces provide isolation, remember this: Partitioning is not protection. If your workloads matter — if compliance, multitenancy or AI safety are on the line — then namespaces alone aren’t enough.

The industry must move beyond the illusion of isolation and embrace runtime environments that enforce it for real.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/10/bf1dcaf3-cropped-6b2aab0f-screenshot-2025-10-20-at-2.41.45%E2%80%AFpm-600x600.png)

Lewis Denham-Parry is a staff solutions engineer at Edera. Lewis Denham-Parry spends his days orchestrating containers and his nights testing their security. At Edera, he focuses on delivering the security and isolation we’ve always needed but often lacked. His work...

Read more from Lewis Denham-Parry](https://thenewstack.io/author/lewis-denham-parry/)