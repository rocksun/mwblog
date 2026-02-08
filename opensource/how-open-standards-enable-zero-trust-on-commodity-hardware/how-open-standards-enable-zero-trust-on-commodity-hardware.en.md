Confidential computing has always held a certain promise. The idea that workloads could process sensitive data while remaining isolated even from the infrastructure that runs them has reshaped the way many enterprise security teams think about trust. For years, we have accepted that data should be encrypted at rest and in transit, but data in use has remained exposed to the platform beneath it. Confidential computing proposes to close that gap.

What has slowed adoption is not a lack of interest but a reliance on specialized and expensive hardware. Trusted execution environments demand specific CPUs, constrained instance types, and operational trade-offs that place them out of reach for many real-world deployments. The result is a growing mismatch between the threat models enterprises care about and the tools they can practically deploy.

At the same time, something important is happening in open source. A set of identity and isolation primitives is quietly maturing into an infrastructure layer that looks a lot like the public key infrastructure that underpins the modern web. Instead of encrypting sessions between browsers and servers, these systems establish cryptographic identities for workloads themselves.

Let’s look at how those building blocks come together, why workload identity is becoming central to [zero trust architectures](https://thenewstack.io/what-is-zero-trust-architecture/), and how systems like Edera use open standards to deliver many of the benefits of confidential computing without requiring new hardware.

## **SPIFFE and the meaning of workload identity**

To understand where this is going, it helps to define a few terms. Workload identity is the idea that software should be able to prove what it is and where it is running, independent of network location or static credentials.

Workload attestation is the process of verifying those properties before granting identity. Zero trust is the assumption that [no implicit trust exists based on network position](https://thenewstack.io/zero-trust-for-legacy-apps-load-balancer-layer-can-be-a-solution/), and that every interaction must be authenticated and authorized. Confidential computing, in its strictest sense, aims to ensure that workloads remain isolated and verifiable even from the host platform.

[SPIFFE](https://spiffe.io/), the Secure Production Identity Framework for Everyone, is a specification that [addresses workload identity directly](https://thenewstack.io/the-rise-of-workload-identity-in-cloud-native-with-spiffe-spire/). It defines how workloads are identified, how those identities are represented, and how they can be verified across distributed systems. A SPIFFE ID is a structured identifier bound to a trust domain and a specific workload. It is not a secret and is not tied to an IP address or a long-lived credential. Instead, it becomes meaningful only when paired with a cryptographic document known as an SVID, or SPIFFE Verifiable Identity Document.

An SVID binds a SPIFFE ID to a key pair and a signing authority. This allows workloads to authenticate to each other using short-lived credentials that can be rotated automatically. From the perspective of a developer or operator, this looks familiar. It mirrors the waycertificates work on the web, but the subject is a workload rather than a domain name.

The important distinction is that SPIFFE does not dictate how trust is established. It defines the interface and the format, leaving attestation to the underlying platform. That flexibility is what makes it so powerful. SPIFFE can sit above cloud-provider metadata, operating-system signals, or, in our case, a hypervisor-rooted trust model.

## **SPIRE as the runtime for trust**

SPIRE is the reference implementation of the SPIFFE specification. Where SPIFFE defines what workload identity looks like, SPIRE defines how it is issued and managed in practice. It introduces two main components: a SPIRE Server and SPIRE Agents.

The SPIRE Server acts as the root of trust. It holds the signing keys for the trust domain and enforces registration policies that define which workloads are allowed to receive which identities. The SPIRE Agent runs on each node and performs two related tasks. First, it proves the identity of the node itself through node attestation. Then it performs workload attestation on behalf of processes running on that node.

Node attestation determines whether a machine should be trusted to host workloads in the first place. Workload attestation answers whether a specific process meets the criteria to receive a given identity. Crucially, workloads never carry secrets with them. They request an identity from the local agent at runtime and receive an SVID only if attestation succeeds. Those identities are short-lived and automatically rotated, dramatically reducing the blast radius of compromise.

This separation is what allows SPIRE to fit [cleanly into zero trust models](https://thenewstack.io/clean-data-trusted-model-ensure-good-data-hygiene-for-your-llms/). Trust is established explicitly, continuously, and based on verifiable properties rather than assumptions about the environment.

## Combining zones and isolation

Edera approaches isolation from a different starting point. Instead of sharing a kernel across workloads, Edera runs applications inside zones that behave like lightweight virtual machines. Each zone has its own kernel and is isolated by a type-1 hypervisor with a small trusted computing base. This removes the shared kernel from the trust boundary and eliminates an entire class of container escape attacks.

In this model, zones become the natural unit of trust. A zone is not just a scheduling construct but a security boundary. That makes it an ideal foundation for workload identity. The challenge is proving to a remote party that a workload is actually running inside such a zone.

This is where SPIFFE and SPIRE fit. By rooting node attestation in the hypervisor itself, Edera can use the hypervisor as the underlying platform authority. The hypervisor can vouch for the existence and integrity of zones, while standard workload attestation mechanisms operate inside those zones without modification. Key material and sensitive services like the SPIRE Server can themselves run inside hardened zones, further reducing exposure.

The result is a system where workloads receive cryptographic identities only if they are running inside verified isolated environments. Data can be encrypted directly to those identities, and policies can be enforced based on where and how code is executing, not just who wrote it.

![Verification](https://cdn.thenewstack.io/media/2026/01/befb9a71-image1.png)

This architecture delivers something subtle but important. It provides remote attestation of isolation properties without relying on specialized hardware enclaves. The guarantees come from strong isolation and verifiable identity rather than opaque hardware features. In practice, this covers a large set of real-world threat models that enterprises care about today.

## **Why this matters now**

Enterprise security teams are increasingly forced to reason about workloads rather than hosts. Microservices, multitenant clusters, and AI systems that process sensitive data keep eroding traditional boundaries. At the same time, the cost and complexity of hardware-based confidential computing remain a barrier.

Open standards like SPIFFE and implementations like SPIRE offer an incremental path forward. They allow organizations to adopt zero trust principles at the workload level, establish cryptographic identities, and build policy around verifiable execution contexts. Systems like Edera show how strong isolation and identity can work together to approximate the benefits of confidential computing using commodity infrastructure.

This is not an argument against hardware enclaves. Those technologies will continue to matter for the most sensitive threat models. But it is an argument for paying attention to the broader evolution of workload identity. Just as it quietly became foundational to the web, workload [identity is becoming foundational to modern distributed systems](https://thenewstack.io/identity-distribution-is-essential-for-modern-api-security/).

Understanding how attestation, zones, zero trust, and identity intersect will be critical over the next few years. The pieces are already here. The opportunity now is to learn how they fit together and to build systems that can earn trust rather than assume it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/08/ad6cb73c-cropped-2b76e7c0-marina-moore-600x600.jpg)

Marina Moore is a research scientist at Edera. She is a maintainer of The Update Framework (TUF), a Cloud Native Computing Foundation (CNCF) graduated project that provides secure software update and delivery. She is also a chair of CNCF's TAG...

Read more from Marina Moore](https://thenewstack.io/author/marina-moore/)