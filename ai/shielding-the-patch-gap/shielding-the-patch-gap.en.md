Four years after Log4Shell became one of the most consequential vulnerabilities in software history, vulnerable instances of the library are still turning up in production environments. That persistence isn’t really a failure of tooling. It’s a fact of how modern applications are built. A typical service pulls in hundreds of transitive open-source dependencies, any one of which can carry a critical CVE that’s difficult to even inventory, let alone test and ship a fix for on short notice.

Now factor in what [AI-assisted vulnerability research](https://thenewstack.io/php2shell-ai-vulnerabilities-maintainers/) is starting to do to that timeline. Attackers can already use large language models to trace exploit paths through unfamiliar codebases and generate working proof-of-concept variants in hours rather than weeks. If that trend holds, security teams are no longer planning for one Log4Shell-scale event every few years. They are preparing for dozens running concurrently, each with a shrinking window between disclosure and exploitation.

## Patching is necessary. It just isn’t sufficient on its own.

Patching remains the durable fix, but compensating controls can augment that longer cycle. The interval between “we know we’re vulnerable” and “we’ve safely shipped the fix” is set by dependency scanning, regression testing, change-management windows, and who owns the affected service, not by how fast an advisory gets published. That interval between the patch release date and the date it is actually deployed in production, called the patch gap or [pre-patch exposure window](https://thenewstack.io/chainguard-mythos-security-harness/), is exactly the period where an unpatched CVE is dangerous. The impact post-Mythos on this time window is substantial, with attackers shrinking the time taken to develop and test exploits down to hours and minutes.

> “The interval between ‘we know we’re vulnerable’ and ‘we’ve safely shipped the fix’ is set by dependency scanning, regression testing, change-management windows, and who owns the affected service, not by how fast an advisory gets published.”

The cloud native ecosystem has spent the last several years building tooling for the two ends of that window: scanners [and SBOM tools](https://thenewstack.io/sbom-sniff-test-hardened-images/) to find what’s vulnerable, prioritization engines to rank what matters most. But what has been missing historically is the compensating controls that address the time between discovery and permanent fix. Now we look towards what a team is actually supposed to do while the fix is in flight.

## Why eBPF keeps coming up as the answer

That gap is why a growing number of teams are [looking towards eBPF](https://thenewstack.io/what-ebpf-means-for-observability-vs-security/) as a mechanism to insert critical and highly effective compensating controls. In short, eBPF lets you attach small, verified programs to kernel events (syscalls, network packets, process execution) without modifying application code or the kernel itself.

It’s what lets a tool observe exactly which process opened which file, which pod talked to which service, or whether a specific function in a vulnerable library was ever actually invoked, with near-invisible overhead and none of the blind spots that come from sitting a layer removed from the workload. eBPF isn’t new (over 10+ years in the Linux kernel!), and it isn’t proprietary to any one project or company. It’s already the enforcement substrate underneath a large share of production CNIs and security sensors.

> “That combination — deep observability plus low-overhead enforcement, built on a primitive that’s already load-bearing infrastructure in most clusters — is what makes shielding vulnerabilities a plausible answer to the patch gap.”

Cilium is one of the clearest examples of how far this has come. What started as an eBPF-based CNI has grown into a sub-project, Tetragon, purpose-built for exactly this kind of runtime security use case: it observes process execution, network activity, and file access at the kernel level and can enforce policy on what it sees, in real time, with no in-process agent and no application code change. That combination – deep observability plus low-overhead enforcement, built on a primitive that’s already load-bearing infrastructure in most clusters – is what makes shielding vulnerabilities a plausible answer to the patch gap.

## Where compensating controls fit in the cycle

Every vulnerability management program already runs some version of the same cycle: discover an exposure, prioritize it against everything else competing for engineering time, remediate it, and verify the fix. Compensating controls have always had a place in that cycle, historically as a stopgap, and often with a focus on network: a firewall rule, a WAF signature, a temporary access restriction.

What’s changing is where that stopgap lives and the level of control. Instead of sitting at the network edge or in a separate tool with its own blind spots, the compensating control now runs alongside remediation, directly on the application workload, using the same runtime visibility that would otherwise be logging the incident after the fact. These compensating controls must inherit the security discipline the rest of cloud native operations already expects: observe before enforcing, roll out gradually, keep an audit trail of what changed, and retire the control the moment the real patch lands and is verified. A handful of vendors are already building toward this. Cisco’s Live Protect architecture, for instance, extends this kind of workload-native enforcement across firewalls and network switches as well as the workload itself, treating protection as one continuous fabric running alongside the existing patching cycle rather than a bolt-on afterthought.

## Filling in the ecosystem

This workflow moves in lockstep with existing scanners and SBOM generation. Those tools still do the job of finding and prioritizing vulnerable components, and vulnerability shielding is useful once that CVE inventory exists. What’s new is the layer in between: a workload-local, kernel-aware control that activates for targeted exploits for a bounded amount of time.

## Closing the AI-accelerated patching gap

Agentic AI is set to make the patch gap worse before it gets better. If attackers can already generate working exploits in hours, we need tooling that closes exposure on the same machine-speed timescale, not on the next change-management cycle.

That’s the outcome eBPF-based vulnerability shielding is aiming for, and it’s still early, fast-moving, open-source work. Isovalent is extending Tetragon toward exactly this verifiable protection, so that closing the pre-patch gap doesn’t mean trading safety for speed. We are looking forward to seeing you in Utah!

---

*KubeCon + CloudNativeCon is taking place in Salt Lake City, Utah, from November 9 to 12. Register Now!*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/10/a47f1b03-jeremyc-erica-parker.jpeg)

Jeremy is a Senior Technical Marketing Engineer at Isovalent - the company behind eBPF, Cilium, and Tetragon. He enjoys the bits and bytes of what makes good security. Prior to joining Isovalent, Jeremy worked in roles as a security engineer...

Read more from Jeremy Colvin](https://thenewstack.io/author/jeremycolvin/)