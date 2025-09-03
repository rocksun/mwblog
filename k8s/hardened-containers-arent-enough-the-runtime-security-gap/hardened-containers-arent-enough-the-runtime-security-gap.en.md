We’ve come a long way from the days of shrink-wrapped software, where applications were developed in monolithic form and deployed on a single machine behind a locked data center door. Today’s systems are distributed, dynamic and elastic. They span clouds, data centers and edge environments. Software no longer lives in one place. It moves, updates and scales in real time. Security, in this new world, cannot be static. It must evolve with the runtime environment itself.

The hardened container image movement has brought welcome discipline to the way software is packaged and distributed. Vendors like [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention), Minimus and [Docker](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) have shown that deterministic, minimal images dramatically reduce risk. But this only addresses part of the problem. The real threats are often the ones you don’t know about. Zero-day exploits, malicious workloads and lateral movement thrive at [runtime](https://thenewstack.io/container-security-and-the-importance-of-secure-runtimes/). If hardened images are the seatbelt, then [hardened runtimes](https://thenewstack.io/how-runtime-hardening-enforces-ai-cloud-native-security/) are the crash cage. Both are essential for a survivable system.

## **Hardened Images Solve for the Past**

The push for hardened images was a response to the sprawl of vulnerabilities in containerized environments. Teams were deploying containers built on outdated base images bloated with unnecessary libraries and tooling. Static scans flagged endless CVEs. Auditors required compliance reports. The security surface became too large to manage.

> A helpful analogy to understanding lateral movement with containers is the difference between a shared hostel versus a private apartment.

By reducing images to only what is needed, security teams were finally able to put some constraints on this chaos. Hardened images ship without shell access, orphaned packages or unused binaries. With this discipline, vulnerabilities are dramatically reduced. Rebuilding images nightly means fewer exposures in the wild. It’s a major step forward.

But these improvements largely address *known* issues at the base image layer. CVEs can be tracked, patched and scanned. But hardened images do not protect against unknown vulnerabilities. They do not stop compromised credentials. They do not contain malicious AI-generated code or prevent a compromised app from exploiting kernel-level flaws. And perhaps most critically, they do not limit what happens once an attacker is inside.

A helpful analogy to understanding lateral movement with containers is [the difference between a shared hostel versus a private apartment](https://medium.com/illumination/how-i-finally-understood-virtual-machines-vs-containers-like-apartment-rentals-e6fa6b21e24c). In a hostel, everyone shares kitchens, bathrooms and living space. If one guest microwaves fish, everyone smells it. Containers behave similarly, sharing the same operating system and resources, which allows issues in one to potentially affect others. Virtual machines, by contrast, are like private apartments with isolated environments and stronger security boundaries.

## **The Runtime Is Where the Action Happens**

Most security incidents today don’t come from obvious malware. They come from sophisticated exploits that chain behaviors together. Credential abuse. Privilege escalation. AI agents responding to poisoned inputs. AI hallucinations can lead to the execution of untrusted or malicious code. These are problems that emerge at runtime, not at build time.

Traditional security tools — SIEMs (security information and event management systems), logging platforms, detection rules — try to keep up by monitoring for anomalies. They rely on signals from the operating system, often delayed, noisy or insufficient. When those tools do generate alerts, the result is alert fatigue, in addition to being too late. Security teams waste countless hours triaging events, many of which are false positives. The signal-to-noise ratio is terrible.

> A hardened runtime creates zones — production-grade sandboxes — of execution where each workload is isolated. They deny default access to shared memory, APIs and system resources.

Part of the problem is that classic security tooling assumes that isolation is already in place. But in shared-kernel container environments, it isn’t. Containers are just processes on the same operating system. There are no hard boundaries. So when a runtime issue occurs, it’s often unclear where the problem lies, who it affects or how far it has spread.

A hardened runtime changes the equation. It [creates zones](https://docs.edera.dev/reference/terminology/zone/) — production-grade sandboxes — of execution where each workload is isolated. These zones deny default access to shared memory, APIs and system resources. They reduce what code can do by default, blocking unscoped syscalls and privileged actions. If something suspicious happens, the runtime can sever network access or pause execution in real time. Instead of alerting and waiting, it acts.

This model dramatically reduces pager fatigue. Teams are no longer flooded with speculative alerts. Runtime hardening ensures that most attacks cannot spread laterally or escalate, even when all the other layers have failed. The result is a security posture that is proactive, not reactive.

## Security by Design, Not by Detection

The shift to hardened runtimes reflects a larger movement in security: from chasing symptoms to engineering prevention. For too long, organizations have treated security as a patching and detection problem. Every new breach leads to more tools, more rules, more dashboards. It is unsustainable.

Hardened runtimes offer a new path. They embed security into the infrastructure itself. Isolation becomes a property of the system, not a policy layered on top. When every workload runs in its own constrained environment, the system becomes easier to reason about. Attack surface shrinks. Blast radius is minimized.

> Hardened runtimes bound AI workloads tightly. They manage GPU drivers in isolated zones. They trace memory access, system calls and network usage from the hypervisor level.

This is especially important in AI environments. AI agents are dynamic. They generate code, hold credentials and interact with systems in unpredictable ways. They run on GPUs, which were never designed for safe multitenancy. Traditional observability tools can’t see into GPU memory. Side-channel attacks, data leakage and tampering are already being reported in the wild.

Hardened runtimes address this by [bounding AI workloads tightly](https://thenewstack.io/ai-clouds-are-flying-blind-the-illusion-of-runtime-protection/). They manage GPU drivers in isolated zones. They trace memory access, system calls and network usage from the hypervisor level. This gives operators real control and forensic insight, even when the workload is opaque or evolving in real time.

## **What Comes Next for Security Teams**

The future of infrastructure security is not about adding more layers. It is about moving control deeper into the execution environment. Hardened runtimes bring security closer to the metal. They enforce trust boundaries by design. And they make observability actionable.

For CISOs and platform teams, this changes the landscape. No longer must they choose between speed and safety. With hardened runtimes, containers can be as fast and portable as ever, while also being secure by default. There is less need to rewrite policies or re-architect clusters just to isolate workloads. The runtime does it for you.

For security engineers, the job becomes clearer. Instead of drowning in alerts, they can focus on real threats. Instead of chasing every new CVE, they can trust the system to contain damage. Security becomes more about infrastructure engineering than incident response.

This does not mean image hygiene is obsolete. Hardened images and hardened runtimes work best together. One reduces the chance of compromise. The other ensures that if compromise happens, it stops there.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/06/e1cc02aa-cropped-4c803797-screenshot-2025-06-09-at-10.04.53%E2%80%AFam.png)

Jed Salazar is field CTO at Edera.

Read more from Jed Salazar](https://thenewstack.io/author/jed-salazar/)