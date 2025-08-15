You may have heard of Apple’s Private Cloud Compute (PCC), announced last year, that allows private access to Apple Intelligence. With all the discussion around this technology and confidential computing, along with the proliferation of “CC” acronyms in the security space, I often get asked: Are these the same thing?

The short answer is no. But here we’ll go through the long answer and compare the threat models of Private Cloud Compute and [confidential computing](https://thenewstack.io/confidential-computing-makes-inroads-to-the-cloud/) to see which problems each actually solves.

What becomes clear in this longer answer is that while both technologies use specialized hardware and allow for remote attestation of a machine, PCC focuses on hardening communication with a node, while confidential computing focuses on [encryption in use](https://thenewstack.io/protect-and-index-sensitive-data-with-polymorphic-encryption/).

Understanding this distinction is crucial for organizations evaluating security technologies and making informed decisions about protecting sensitive workloads.

## **What Is Apple’s Private Cloud Compute?**

Apple [announced PCC](https://security.apple.com/blog/private-cloud-compute/) last summer as its solution to private, off-device use of AI models. Previously, Apple has focused on on-device processing, allowing user data to remain on the device. With the rise of larger AI models in the past few years, this on-device processing is no longer feasible, leading Apple to develop PCC.

The idea with PCC is to achieve similar privacy to on-device processing, while using cloud compute resources.

Specifically, PCC involves specialized nodes created with a hardened hardware software supply chain. These nodes use secure boot to ensure all code is signed by a hardware-backed key, and all data is encrypted at rest with randomized keys that can’t be accessed between reboots.

Data is encrypted from a user device to a specific PCC node, so an attacker cannot direct traffic to a compromised node. For more detail, including some really interesting subtle attacks, I recommend reading Apple’s full [writeup](https://security.apple.com/blog/private-cloud-compute/).

One feature I’ll call out is remote attestation. PCC uses remote attestation to allow nodes to cryptographically attest to running publicly listed software. This remote attestation allows not just Apple, but also external researchers to test this assertion.

The focus here is on proving software integrity and enabling public verifiability — creating transparency about what code is actually running. This provides powerful protection against Apple itself violating the privacy of users.

**PCC’s threat model**: PCC primarily defends against network-level attacks, man-in-the-middle attacks and scenarios where untrusted intermediaries might intercept or redirect user data. It also protects against potential misuse by Apple itself through its transparency mechanisms.

So how does this compare to confidential computing?

## **What Is Confidential Computing?**

Confidential computing allows for the [encryption of data in use](https://thenewstack.io/confidential-computing-is-transforming-data-encryption-in-healthcare-finance/). It does so by running sensitive applications on a hardware trusted execution environment (TEE). This TEE sits alongside the CPU and provides data integrity, data confidentiality and code integrity.

In effect, this moves trust from software to hardware and ensures that other users, and even the operating system, cannot interfere with or read data from an application. For more detail, see my previous post on [confidential computing](https://edera.dev/stories/demystifying-confidential-computing).

One feature I’ll call out for this comparison is remote attestation. In confidential computing, remote attestation provides proof that an application is running on a TEE. The application and environment on the TEE are signed by a hardware key, allowing a remote verifier to ensure that the expected application is running on the expected TEE.

As we explored in our [previous post on remote attestation](https://edera.dev/stories/remote-attestation-in-confidential-computing-explained), this mechanism focuses on proving TEE execution and application identity within an isolated hardware environment.

**Confidential computing’s threat model**: Confidential computing defends against privileged software attacks (including compromised operating systems and hypervisors), multitenant risks in shared cloud infrastructure and scenarios where the cloud provider itself cannot be fully trusted with sensitive data during processing.

## **How Are PCC and Confidential Computing Similar?**

Both PCC and confidential computing include a remote attestation feature. Both prove to a remote party what is running on which device, though they serve different verification purposes and operate at different layers of the technology stack.

Both technologies also make use of specialized hardware for security. PCC uses a specialized hardware supply chain to prevent tampering with PCC nodes, and uses hardware keys on these nodes. Confidential computing uses hardware TEEs to run code in an isolated environment and uses hardware signing keys.

## **Key Differences: PCC vs. Confidential Computing**

PCC and confidential computing have fundamentally different goals and threat models. PCC provides hardened communication with a cloud device to ensure data privacy during transit and processing, but it does not encrypt the application during runtime on the PCC node. The data is decrypted and processed in the clear within the trusted PCC environment.

Confidential computing, on the other hand, provides encryption in use and isolation for sensitive applications running on remote shared infrastructure. Data remains encrypted even during processing, accessible only within the hardware-protected TEE environment.

Put simply: PCC improves trust in the cloud device and the communication path to it by hardening the infrastructure itself, while confidential computing assumes the cloud device and infrastructure will remain untrusted and instead protects data through encryption even during processing.

The remote attestation mechanisms also differ in focus. PCC’s attestation emphasizes software transparency and public verifiability to build trust through openness. Confidential computing’s attestation proves secure execution within isolated hardware environments, focusing on technical guarantees rather than transparency.

## **Should I Be Using PCC or Confidential Computing?**

While PCC provides strong protection for Apple devices using cloud AI processing, it’s not a model that will work for everyone. Apple has an established hardware supply chain that it used to build trusted nodes, and it controls both these nodes and the devices connecting to them, allowing for some powerful cryptographic guarantees. Without these factors in place, PCC would be hard to replicate.

For organizations seeking to protect sensitive workloads in cloud environments they don’t fully control, confidential computing offers a more broadly applicable approach. It provides protection even when using third-party cloud providers and shared infrastructure, making it suitable for a wider range of use cases beyond Apple’s tightly controlled ecosystem.

The choice between these approaches depends on your specific threat model, infrastructure constraints and trust assumptions about your cloud environment.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/08/ad6cb73c-cropped-2b76e7c0-marina-moore-600x600.jpg)

Marina Moore is a research scientist at Edera. She is a maintainer of The Update Framework (TUF), a Cloud Native Computing Foundation (CNCF) graduated project that provides secure software update and delivery. She is also a chair of CNCF's TAG...

Read more from Marina Moore](https://thenewstack.io/author/marina-moore/)