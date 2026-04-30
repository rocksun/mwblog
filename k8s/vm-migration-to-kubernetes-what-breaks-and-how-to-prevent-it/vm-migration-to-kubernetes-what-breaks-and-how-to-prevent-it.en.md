Here is what nobody putting together the business case for a VM migration to Kubernetes will tell you upfront: the compute is the easy part.

Moving workloads off vSphere and onto Kubernetes is conceptually straightforward. The tooling has matured. The architecture is proven. Compute moves, storage remaps, and the platform team has a plan.

The network is where projects quietly stall.

Not because the technology does not work. Because nobody scoped the network properly before the project started. A platform migration turned into a multi-team coordination exercise. The firewall team needed a change window. The security team needed to review a network placement that changed when it should not have needed to. The application team discovered hardcoded IPs that nobody documented.

Six months later, half the VMs are still on vSphere and the project is technically “in progress.”

This is not a skills gap. It happens at the most mature organisations with capable teams. It is a scoping problem, and it has a specific cause: the gap between how VM networking works and how Kubernetes networking works is wider than it looks on a migration plan.

This post is for the people who approve these projects. Here is what actually breaks, and what to decide before it does.

## Why VM Migrations to Kubernetes Stall on the Network

In a traditional hypervisor environment, a VM’s IP address is its identity. Not just technically, as a routing destination, but operationally. It is registered in DNS. Referenced in firewall rules. Watched by monitoring agents. Connected to by peer applications. In regulated environments, it may be in compliance documentation.

Kubernetes was built on different assumptions. Workloads are ephemeral. Addresses come from a range managed by the cluster and mean nothing outside it. Identity is based on labels, not addresses.

When a VM moves into Kubernetes using the default networking model, it gets a new IP. That new IP ripples through everything that referenced the old one. Firewall rules, DNS, security reviews, monitoring, peer applications. None of it is technically hard. The problem is that the platform team owns none of those systems and controls none of those timelines. A migration scoped for one team becomes a coordination exercise across four of them.

*This is the networking tax: the hidden cost of a networking model that does not account for what your VMs are already attached to. Your platform team pays it. Your project timeline absorbs it.*

This is not an edge case. According to [Portworx’s 2024 Voice of Kubernetes Experts report](https://portworx.com/resources/voice-of-kubernetes-expert-report/), 58% of organisations plan to migrate some of their VMs to Kubernetes using technologies like [KubeVirt](https://kubevirt.io/). Of those organisations, 65% plan to do so within the next two years.

The migrations are already happening. The scoping decisions are being made now.

Picture a single VM that has been running for several years. Its IP address is in two firewall rules, a monitoring dashboard, a load balancer backend, and a compliance document that was last audited in 2021. The application team has it hardcoded in a config file nobody has opened in three years. That VM is not unusual. It is representative. Now multiply it by two hundred.

## Two Ways VM Migration to Kubernetes Breaks in Practice

Two failure modes appear repeatedly in VM-to-Kubernetes migrations. Neither is a surprise once you know to look for them.

### The security bottleneck

VLANs in enterprise environments are not just a routing tool. They are a compliance construct. Organisations have spent years segmenting networks to meet PCI-DSS, SOC 2, or internal security policies. Those segments are owned and documented by the security team. Changes to them require sign-off.

When a VM’s network placement changes during migration, even if the VM itself is unchanged, the security team has a legitimate reason to review it. That review takes as long as it takes. The platform team cannot accelerate it.

### Platform fragmentation

The compound result of scope expansion and security bottlenecks is partial migration. The VMs with few dependencies move. The ones with static IPs embedded in firewall rules, or in security-reviewed VLAN segments, stay on vSphere.

The organisation ends up running two platforms in parallel with no agreed path to consolidation. The cost reduction and operational simplification that justified the migration are deferred. The project is technically not cancelled, just permanently not finished.

For many organisations, this is not a planning exercise. Active licence renegotiations and uncertainty about long-term hypervisor roadmaps have moved these conversations from the backlog to the boardroom. The migrations are happening now, and the scoping decisions made in the next quarter will shape whether they succeed.

## The One Question Every VM Migration to Kubernetes Needs Answered

Before any VM migration project is scoped or budgeted, one question is worth an explicit answer: **Is this migration also a modernisation?**

If yes, the network redesign is expected work. The additional team coordination is part of the scope. Budget and timeline accordingly, and plan for the security and network teams to be involved from the start.

If no, the networking model chosen for the migration determines whether lift-and-shift is actually achievable or just aspirational.

This sounds like a technology question. It is not. It is a project scoping question that happens to have a technology answer.

The default Kubernetes networking model was designed for cloud-native workloads. Containers with ephemeral addresses and no upstream dependencies. It was not designed for VMs that have ten years of firewall rules, DNS entries, and compliance documentation attached to a fixed IP address.

Using a model designed for the former to move the latter is where projects run into trouble. *You are not choosing a networking model for your Kubernetes cluster. You are choosing whether your migration is also a modernisation, and whether your budget accounts for that.*

In some organisations, the decision about which networking model to use for VM migration does not belong to the platform team at all. Where VLANs are compliance constructs rather than just routing tools, it is the security team that owns the answer. That is not unusual. It is a reason to get them into the scoping conversation before the architecture is chosen, not after.

## Two Networking Models, Two Different Projects

There are two networking models for running VMs in Kubernetes, and the right one depends on what the migration is actually for.

### The modernisation model

In a Layer 3 (L3) model, the VM gets a new IP address from the cluster’s address range. Traffic is routed between the cluster and the rest of the network. Once the VM is on the cluster network, it operates the same way containers do. Kubernetes-native tooling applies without modification. The long-term operational model is clean.

The trade-off is explicit: everything that referenced the old address needs to be updated. Firewall, DNS, monitoring, peer applications. This is the work. It is expected and budgeted when modernisation is the goal, and for organisations running a small number of VMs, or VMs with few upstream dependencies, it is often the right choice. The issue is not L3 routing. It is using L3 routing on a VM estate that was never scoped for modernisation.

### The lift-and-shift model

In a Layer 2 (L2) model, the existing network segment is extended directly into the Kubernetes cluster. Using KubeVirt to run the VM as a native Kubernetes workload alongside containers, [the VM keeps its original IP address](https://www.tigera.io/blog/kubevirt-networking-how-to-preserve-vm-ip-addresses-during-migration/). The VLAN it lived in is preserved inside the cluster. From the upstream network’s perspective, the workload did not move. The firewall rule still applies. DNS still resolves. The security team does not need to be pulled into a review they did not schedule for.

Calico L2 Bridge Networks provide this capability. The upstream network continues to see the same workload it always did. No change requests. No reconfiguration. No other teams in the room.

The practical consequence: the platform team owns the migration end to end. No firewall change requests sitting in a queue. No security review on a workload that did not change. No application team dependency. The project delivers on its original scope and its original timeline. That is what lift-and-shift is supposed to mean.

*You can migrate a VM from VMware to Kubernetes and it keeps its original IP, stays on its original VLAN. Nothing needs to change. And now it can be protected by Calico network policy and observed through Calico flow logs.*

For teams migrating VMs with years of accumulated network dependencies, that continuity is the difference between a migration that completes and one that gets cancelled.

For a technical breakdown of the L2 Bridge mode, see our blog post, [Lift-and-Shift VMs to Kubernetes with Calico L2 Bridge Networks](https://www.tigera.io/blog/lift-and-shift-vms-to-kubernetes-with-calico-l2-bridge-networks/), which walks through how the network continuity actually works and includes a recorded webinar.

## What Your VM Estate Gains After Migrating to Kubernetes

Choosing the L2 model for migration does not mean your VM estate stays in legacy mode permanently. The migration is the beginning. Day 2 networking is what comes next.

Once the VM is running in Kubernetes, the platform team gains operational capabilities that were not available on the old hypervisor. Traffic visibility, including east-west flows between the migrated VM and other workloads, is available without additional tooling. Security policy can be applied directly to the VM interface using the same constructs the team uses for containers, replacing legacy firewall rules incrementally on whatever timeline the security team sets. This is what Security in Depth looks like in practice. Layered controls applied workload by workload, not a single perimeter replaced in one event.

The VM can also be moved between cluster nodes without network reconfiguration. Same IP, same VLAN, no change to the upstream network. KubeVirt live migration between nodes, without a separate network coordination step.

This is what a policy-first migration enables: the networking and security layer is unified before the workloads move, so day 2 does not require a second migration to get there. Migration and modernisation stay on separate timelines, with separate budgets, managed by separate teams. Neither blocks the other.

A VM that migrated to Kubernetes last quarter can have a new security policy applied today, written by the same security team using the same review process they already have. The migration did not force their hand on timing or tooling. The security team gains a policy model that is version-controlled and auditable. The platform team gains a migration that delivered on its original timeline. Those two outcomes are not in conflict.

## Four Questions to Ask Before Approving a VM Migration to Kubernetes

Four questions are worth an explicit answer before any VM migration project is approved:

1. Is this migration also a modernisation? If yes, budget for multi-team coordination. If no, confirm the networking model supports genuine lift-and-shift.
2. Which VMs have static IPs embedded in firewall rules or compliance documentation? These are the workloads most likely to stall. Identify them before work begins, not during it.
3. Who owns the VLAN segments the migrated VMs currently live in? If it is the security team, they belong in the scoping conversation, not the execution phase.
4. What is the plan for workloads that cannot be modernised? If there is no answer, plan for two platforms running in parallel indefinitely.

Before the project kicks off, run a blast radius analysis on a single VM. Pick one. Map every service connecting to its IP, every firewall rule referencing it, every DNS entry, and who owns each one. That single exercise will tell you more about your true migration scope than any architecture diagram. If the answer fills a spreadsheet, your migration is not a weekend project. If the answer is three lines, start there.

These are not technical questions. They are scope questions. The answers determine whether the migration delivers on its business case or quietly becomes a programme nobody approved.

Interested in learning more about VM Migrations? [Talk to an expert about how you can migrate your VM estate](https://www.tigera.io/contact/).

> ## Frequently asked questions

1. > **Why do VM migrations to Kubernetes stall?** Most stall on the network, not on compute. The default Kubernetes networking model assigns new IP addresses to migrated workloads, which breaks firewall rules, DNS entries, and compliance documentation that referenced the original addresses. What looks like a platform-team project becomes a coordination exercise across the network, security, and application teams.
2. > **What is the difference between Layer 2 and Layer 3 networking for VM migration?** A Layer 3 (L3) model assigns the VM a new IP address from the cluster’s address range — clean for a modernisation project, but it requires updating every system that referenced the old address. A Layer 2 (L2) model extends the existing network segment into the cluster, so the VM keeps its original IP and VLAN. L3 is the modernisation model; L2 is the lift-and-shift model.
3. > **Can a VM keep its IP address when migrating to Kubernetes?** Yes — but only with a Layer 2 networking model that extends the existing network segment into the Kubernetes cluster. With L2 networking, the VM keeps its original IP and VLAN; firewall rules, DNS entries, and peer applications continue to work without reconfiguration.
4. > **Does KubeVirt support lift-and-shift migration?** KubeVirt runs the VM as a native Kubernetes workload, but the networking model determines whether the migration is genuinely lift-and-shift or actually a modernisation in disguise. Pairing KubeVirt with a Layer 2 networking model preserves the VM’s original IP and VLAN — that’s what lift-and-shift means in practice.
5. > **What is the “networking tax” in a VM-to-Kubernetes migration?** The networking tax is the hidden cost of choosing a networking model that doesn’t account for what your VMs are already attached to — firewall rules, DNS, monitoring, peer applications, compliance documentation. None of it is technically hard to fix, but the platform team owns none of those systems and controls none of the timelines. The tax is paid in delayed projects and partial migrations.