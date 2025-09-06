AI is racing ahead, reshaping software patterns, business models and infrastructure. But one critical piece of hardware is struggling to keep up. The same GPUs that once brought us realistic shadows in games like “Quake III Arena” and fluid motion in “Counter-Strike” are now powering machine learning (ML) and cloud AI platforms. Originally built for rendering pixels and lighting effects at high speed, [GPUs excel at parallel processing](https://thenewstack.io/the-critical-role-of-gpu-data-orchestration-in-ai-success/). That made them perfect for immersive gaming and now makes them essential for neural networks.

What has not kept pace is [GPU security](https://thenewstack.io/ai-clouds-are-flying-blind-the-illusion-of-runtime-protection/).

While CPUs have evolved to include protections like privilege separation, virtual memory and runtime observability, GPUs remain anchored in a design philosophy built for trusted, single-user environments. This mismatch has created dangerous blind spots in modern infrastructure. In June, [Wiz disclosed another GPU isolation flaw](https://www.wiz.io/blog/nvidia-ai-vulnerability-cve-2025-23266-nvidiascape) that further underscored how GPUs lack basic multitenancy safeguards. These processors were never built to [enforce strict boundaries between workloads,](https://thenewstack.io/what-we-wish-we-knew-about-container-security/) nor to support the telemetry and auditability that modern [AI security](https://thenewstack.io/ai-security-needs-better-infrastructure-not-more-tools/) requires.

Yet GPUs are now deployed in shared, high-stakes environments as if they were hardened infrastructure. That false confidence is precisely what makes this emerging threat so urgent.

## **GPUs and CPUs Are Built To Do Very Different Things**

The makers of CPUs have spent decades developing protections, including privilege levels, virtual memory, process isolation and observability. GPU design still operates on assumptions made for single-user, single-purpose contexts. The GPU was never meant to be shared across workloads or to protect one customer’s data from another.

At the architectural level, GPUs and CPUs differ completely. CPUs are built for general-purpose computing with strong controls over execution and memory. They handle diverse tasks through a small number of cores, each capable of switching between processes and maintaining isolation through virtual memory and strict privilege levels.

[GPUs are optimized](https://thenewstack.io/revolutionizing-storage-the-role-of-gpus-in-modern-infrastructure/) for throughput. They contain thousands of simple cores meant to execute the same instruction across large data sets. This makes them great for rendering and matrix math, but introduces blind spots in context switching and memory isolation. Memory from one workload can persist long after it ends, which becomes a risk in shared environments. Without page tables, memory randomization or syscall boundaries, GPUs are exposed in ways CPUs are not.

GPU security concerns have traditionally focused on this lack of isolation. Many programming models assume the driver manages memory safely and that users are trusted. This assumption falls apart in the cloud. One container or virtual machine (VM) can leave traces of data that another could potentially access. These risks are made worse by how opaque GPU execution remains. There are no mature tools for runtime inspection or behavioral auditing, which limits visibility and control.

## **More Hidden Risks and the Illusion of Safety**

While those classical concerns remain, the deeper story is more urgent. Enterprises are deploying AI workloads into GPU-accelerated clusters while assuming that CPU isolation models still apply. They do not.

First, GPU drivers represent a massive attack surface. These drivers often run with elevated privileges and manage hardware access across workloads. A single vulnerability can compromise the host system. Unlike CPUs, where drivers are smaller and often abstracted by the operating system, GPU drivers handle scheduling, memory and instruction dispatch directly. They are large, complex and often proprietary, making them hard to audit and patch.

Second, telemetry from GPUs is limited. Most tooling reports performance metrics like utilization and memory throughput, not behavioral signals. There is no equivalent of syscall tracing or kernel auditing. Malicious activity, such as key leakage or data scraping, could happen entirely within GPU kernels and remain invisible.

Third, shared GPUs create blind spots in multitenant environments. Workloads often run back to back with no strong guarantees that one tenant’s data is not exposed to another. The belief that GPUs only run harmless math hides the fact that this math often includes sensitive embeddings, weights and tokens. As AI systems grow more complex, the value of what lives temporarily on a GPU increases. Ignoring these risks only delays the emergence of real exploits targeting these gaps.

## **What Linux and Containers Taught Us About Growing Up**

Linux was never designed to secure billions of containers running across cloud environments. It started as a general-purpose operating system intended for individual machines and trusted users. As it became the backbone of modern infrastructure, the assumptions around isolation, visibility and multitenancy no longer held. What followed was a rapid evolution of security tooling, including namespaces, cgroups, seccomp and advanced observability. The ecosystem had to build layers of protection around a kernel that was not originally meant to carry the weight of the cloud.

The same pattern is emerging with GPUs. These processors were created to render graphics and accelerate local compute, not to run sensitive AI workloads from many tenants on shared hardware. Yet that is exactly what they are now expected to do. Like Linux in the early container era, the architecture of GPUs has not caught up with the demands of modern usage. The sooner we recognize this gap, the sooner we can develop the protections that secure AI infrastructure requires. Otherwise, we will continue to accelerate without the safeguards needed to avoid the consequences.

Can you really trust your AI security posture if you don’t understand what’s happening at the GPU level?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/06/e1cc02aa-cropped-4c803797-screenshot-2025-06-09-at-10.04.53%E2%80%AFam.png)

Jed Salazar is field CTO at Edera.

Read more from Jed Salazar](https://thenewstack.io/author/jed-salazar/)