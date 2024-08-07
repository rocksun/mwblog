# Bypassing eBPF to Protect Runtimes in Kubernetes Apps
![Featued image for: Bypassing eBPF to Protect Runtimes in Kubernetes Apps](https://cdn.thenewstack.io/media/2024/08/54c24441-bypassing-ebpf-to-protect-runtimes-in-kubernetes-apps-2-1024x576.jpg)
SEATTLE — Kubernetes is a good fit for the scale needed to run generative AI applications. But GenAI poses a security problem that requires new approaches to [protecting runtimes in Kubernetes applications](https://thenewstack.io/the-top-5-kubernetes-security-mistakes-youre-probably-making/).

If anything, [CloudNativeSecurityCon](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america) earlier this summer showed how deeply complex the problems become with new attack vectors that compound with GenAI.

One novel new approach to the problem comes from Operant, a runtime application platform provider co-founded by a team of veterans from Apple, Arm, [Google](https://cloud.google.com/?utm_content=inline+mention), Juniper, Transposit and [VMware](https://tanzu.vmware.com?utm_content=inline+mention).

[Operant](https://www.operant.ai/) protects Kubernetes applications in runtime at every layer of the application. It enforces security policies for services and APIs, everything within a Kubernetes cluster, said [Ashley Roof](https://www.linkedin.com/in/ashleyroof/), co-founder and CMO at Operant.
Roof said customers install Operant and then see a blueprint of their Kubernetes application across all the network layers. Operant’s approach bucks some trends in the cloud native security space, particularly regarding the Extended Berkeley Packet Filter, or [eBPF](https://thenewstack.io/what-is-ebpf/), a [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) technology.

“We do have an eBPF component that does process-level stuff, but a lot of what we’re doing is not related to that,” Roof said. “And so what that allows us to do is reduce a lot of the noise and have unique runtime insights, which then we are able to prioritize and give people a really strong sense of criticality.”

Operant CEO [Vrajesh Bhavsar](https://www.linkedin.com/in/vrajeshio/) said his company wants to support users who want to use eBPF. But he sees better approaches than filtering the data firehose from [eBPF’s observability of the Linux kernel](https://thenewstack.io/ebpf-meaner-hooks-more-webassembly-and-observability-due/).

eBPF is a powerful technology that several vendors have tried to productize in many different ways, he said. Operant built a solution that does not rely on eBPF, which the company believes gives its solution better scalability, avoids inherent risks associated with eBPF, and allows for better contextuality.

## Too Much Data, Too Much “Noise”
eBPF is not scalable because there is too much data, according to Bhavsar. It’s like tapping the floodgates; eBPF runs all the system data from the kernel.

“Just think of all the ephemeral services that come up for a few minutes and then disappear,” Bhavsar said. “When you have a lot of signals just coming from eBPF sensors, you are then heavily dependent on what’s happening at that layer, without having any understanding of what’s happening in all these other layers across the entire Kubernetes stack. And especially in Kubernetes, this is an especially hard and important problem to solve.”

With Kubernetes, he said, you need to think about more than process-level activities. You also want to look at the behavior of your other pods, containers and services. How are they talking across different networks? What about ingress and egress? How are the APIs talking to each other internally and externally?

“And that’s the approach that we are bringing to market, where teams don’t have to sift through this noise that is coming out of eBPF,” Bhavsar said.

But what about all the other layers? How do you find the needles in this giant haystack of data?

It doesn’t make sense to take the firehose of data and ship it somewhere to analyze, Bhavsar said. How do you make sense of what’s going on in the system at the OS and kernel levels? And how do you make sense of what’s happening at all the other layers?

Many of the existing eBPF solutions require writing filters, he said. But that’s not Operant’s approach: “I’m a kernel engineer. I don’t want to write kernel-level filters, and I don’t want customers to write this.”

Bhavsar worked on iOS and macOS at Apple, building data protection systems, dynamic tracing and the company’s secure enclave technology. His background has allowed him to combine security and machine learning and recognize why generative AI poses such a massive risk, requiring a contextual approach focusing on runtime behavior.

Commercial large language models in all varieties are available on sites like [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/). All these models get delivered as containers. These containers connect to APIs and services. Container portability with generative AI is a potent combination that can lead to data leaks. Companies adopting AI now have to rethink their entire security program. It goes beyond code scanning, identity management or getting the configurations right.

It’s more about what is happening at runtime, Bhavsar said. What is the application doing?

“What are these containers doing when talking to each other?” Bhavsar said. “What data payload is moving across all these different systems? What is going on outside of my environment through these AI APIs? And where are these new kinds of risks and attacks?

## As the World Adopts Kubernetes
Everyone is moving towards Kubernetes, especially with GenAI, and adopting models and references.

“We want the world to be ready to secure these environments,” Bhavsar said. But, he added, “a web application firewall or an API gateway is not enough anymore.”

All these applications have deep roots and dependencies that bypass the perimeter, accessing personal, private information such as credit card data.

It’s like a whole new black hole, Bhavsar said, and you can’t manage it manually. There is too much dynamism and ephemerality.

In the old world, you could manually create IP-based rule sets. In Kubernetes, there is no IP address. So engineers must rethink what kind of endpoints to make and what segmentation policies to establish.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)