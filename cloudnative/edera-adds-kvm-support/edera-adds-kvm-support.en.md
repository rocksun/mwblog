Edera, a top Xen hypervisor company, is shifting gears and will start supporting KVM as well this summer.

If you use Edera for secure, lightweight virtual machines (VMs), you may have seen the company state that its hypervisor of choice, [Xen](https://xenproject.org/), is “architected for security first,” while Linux’s built-in [Kernel-based Virtual Machine (KVM)](https://linux-kvm.org/page/Main_Page) is described as a general‑purpose [hypervisor with an expanded attack surface](https://edera.dev/stories/why-edera-built-on-xen-a-secure-container-foundation#).

That was then. This is now.

At [KubeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) this week in Amsterdam, Edera announced it was porting its zone-based micro-VM isolation model to KVM this summer. *Why?* Customers are demanding KVM support.

As [Alex Zenla](https://www.linkedin.com/in/azenla), Edera’s co-founder and CTO, explains to *The New Stack*, “LVM isn’t a default; it’s a decision. Organizations running KVM-based infrastructure have made deliberate choices about their stack, often with years of tooling, operational expertise, and certification work built around it.

“That investment deserves to be met, not worked around. Edera should work within that architecture. This summer, it will.”

> “KVM isn’t a default; it’s a decision,” Zenla says. “Organizations running KVM-based infrastructure have made deliberate choices about their stack, often with years of tooling, operational expertise, and certification work built around it. That investment deserves to be met, not worked around.”

To understand the differences, let’s quickly review the differences between a type 1 hypervisor, Xen, and a type 2 hypervisor, KVM. Type 1 hypervisors, aka “bare metal” hypervisors, run directly on your hardware to control it and manage VMs. Type 2, or “hosted hypervisors,” run on the operating system just as any other application, albeit in KVM’s case at, as the name suggests, a very low level.

In its announcement, Edera stresses that strong fault isolation “shouldn’t require rebuilding your infrastructure” and that many organizations have consciously standardized on KVM after years of investment in tooling, certifications, and operational practices. Rather than asking those teams to stand up a parallel Xen, Edera will let them run its zones directly on their existing KVM foundations.

Zones remain the core abstraction. Each zone is a single-tenant execution environment with its own kernel, address space, device namespace, and lifecycle. These are designed to eliminate shared-kernel failure modes such as lateral movement and noisy-neighbor interference under stress or misconfiguration.

Today, those zones sit on top of Xen; once KVM support ships, the company says, “the isolation model won’t change. The substrate will.” For enterprises, that means Edera will look, work, and run the same.

Under KVM, every workload will still run in its own kernel, with memory, device namespaces, and lifecycle isolated per zone. Existing orchestration workflows and tooling are preserved, and applications do not need to be re-architected to benefit from the new backend. From the perspective of Kubernetes and platform teams, Edera remains a drop-in approach for wrapping pods or services in micro‑VM‑style isolation.

Under the hood, though, the company is candid about the tradeoffs. Xen centralizes enforcement in a dedicated hypervisor, keeping memory management and scheduling decisions outside the host OS. KVM, on the other hand, relies on the Linux kernel to do its work.

On KVM, Edera cannot lean on the hardware. Instead, it operates in user space, with tight feedback loops on memory pressure, explicit ownership tracking, and more defensive device lifecycle handling.

> “If you’re doing a greenfield project, Xen makes the most sense, but if you have an existing brownfield project where you’re using KVM support, you get the same security and orchestration benefits for both.”

So, which variant should you use? Zenia explains, “If you’re doing a greenfield project, Xen makes the most sense, but if you have an existing brownfield project where you’re using KVM support, you get  the same security and orchestration benefits for both.”

That said,  “There are certain features that we can only do on one or the other.” However, it’s not like the KVM version is lightweight. It’s the true thing. And we also make it easy to swap between them or even run them both simultaneously.”

The big difference, Zenia says, is that “Xen gives you more control and speed on the hardware.” In particular, the Xen-based variation is much faster, “for things like GPU assignment.”

Another big difference for high-assurance computing is that you can escrow secrets within the hypervisor, and we also have a high-performance data channel between different zones in our platform that can only be implemented on our hypervisor. However, the vast majority of standard Kubernetes stuff works.  So functionally, they’re almost equal. Everything that can be technically done right is being done on both.”

Another reason why Edera is adopting KVM is that Xen has been losing popularity. Frankly, there are just fewer Xen users out there. For example, Amazon Web Services (AWS) EC2 was originally based on Xen. AWS  has been migrating to the Nitro platform, which uses a KVM-based hypervisor.

Xen-based instance types are now legacy and are being actively migrated. Other important cloud services, such as T-Mobile, have also bid Xen adieu in favor of KVM because “[Overall KVM offers more functionality](https://public.t-cloud.com/en/blog/product-news/switch-from-xen-to-kvm) and stability in cloud operations.”

That’s not to say Xen will disappear. Far from it! Instead, Zenia explains, “Xen today is all about high-assurance and safety for critical applications. So, now the Xen board is mostly made up of automotive companies.”

That said, Zenia adds that Edera is still a major upstream contributor to the Xen open-source project. However, moving forward, Edera is becoming “hypervisor independent, because technologically we’re not tied to a hypervisor as much as we are tied to our feature set for security-first VMs. So, even as Xen’s popularity declines in general-purpose computing, Edera expects to continue growing and doing well thanks to its new dual-hyperviser strategy.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)