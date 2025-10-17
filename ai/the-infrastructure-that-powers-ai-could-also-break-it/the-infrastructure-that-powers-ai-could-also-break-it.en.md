When it comes to securing AI, most conversations focus on the model layer: [Prompt injection](https://thenewstack.io/6-key-security-risks-in-llms-a-platform-engineers-guide/), training data leakage and unsafe outputs. But there’s a more immediate risk that often goes overlooked: the infrastructure powering those models.

AI workloads rely on the same foundations as modern cloud native applications. That means [containers](https://thenewstack.io/introduction-to-containers/), [Kubernetes](https://thenewstack.io/kubernetes/), shared GPU nodes and orchestration layers that were never designed with AI-specific risks in mind. And because these components are being reused at scale, any vulnerability in the stack has the potential to cascade across multiple platforms and users.

As researchers focused on breaking AI infrastructure to make it safer, we’ve seen firsthand how these risks are already showing up in real-world environments.

## **The GPU Is a New Attack Surface**

To run large models efficiently, organizations rely on the NVIDIA Container Toolkit, the default way to run GPU-enabled containers. It’s used widely across all cloud providers, AI platforms and any organization working with NVIDIA GPUs.

So when we found two separate critical container-escape vulnerabilities in the NVIDIA Container Toolkit, we exposed major risks for anyone using shared GPU infrastructure. Both NVIDIAScape (CVE-2025-23266) and CVE-2024-0132 were not edge-case scenarios.

Finding two distinct container escapes that grant root access to the host machine in the same year signals something important: This is a new attack vector. It proves that organizations must design their systems to be resilient, assuming attackers will breach the first line of defense. A container escape is no longer a question of if, but when. The takeaway is clear: [Securing AI doesn’t stop at the model](https://thenewstack.io/evil-models-and-exploits-when-ai-becomes-the-attacker/). It starts with the foundational infrastructure it’s built on.

## **Shared AI Platforms Carry Shared Risk**

Most organizations don’t run their own infrastructure for AI. Instead, they turn to AI as a service providers like Hugging Face or Replicate. Both are platforms designed to simplify deployment and scaling.

With [Hugging Face](https://www.wiz.io/blog/wiz-and-hugging-face-address-risks-to-ai-infrastructure), we found an issue where a malicious model could break out of its container and access neighboring workloads. With [Replicate](https://www.wiz.io/blog/wiz-research-discovers-critical-vulnerability-in-replicate), we identified a vulnerability that let us intercept prompts and responses from other users. Luckily, both companies worked swiftly and collaboratively with us to fix the issues.

But the pattern is clear: Weak isolation between customers’ workloads, overly broad permissions and the lack of proper network segmentation are still too common. With AI moving fast, the basics are sometimes skipped.

But we’ve learned this lesson before: Secure-by-default infrastructure matters, especially at this scale.

## **3 Ways to Strengthen Your AI Infrastructure**

The good news is we don’t need to start from scratch. The cloud security community has already built strong foundations, from least privilege to network segmentation, that apply directly to AI. Here’s where to begin:

1. **Start with secure defaults:** Container isolation, scoped permissions and network segmentation should be non-negotiable. These aren’t “nice to have.” They’re essential building blocks.
2. **Assume something will break:** No single control is foolproof. You can assume the first line of defense would be bypassed. Build layered defenses that limit blast radius and catch failures before they escalate.
3. **Understand your shared responsibility:** Whether you’re running your own models or using a platform, know where the provider’s responsibilities end and yours begin. Secure the data and pipelines under your control.

AI is transforming the way we build and deploy software, but it’s also reshaping our threat models. If we secure the infrastructure powering AI with the same discipline we apply to the cloud, we can stay ahead of risk while keeping innovation moving fast.

*KubeCon + CloudNativeCon North America 2025 is taking place Nov. 10-13 in Atlanta, Georgia.* [*Register now*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/10/e25d1e12-cropped-160ebc8a-nir-ohfeld.jpeg)

Nir Ohfeld is the head of vulnerability research at Wiz. He focuses on cloud-related security research and specializes in the exploitation of cloud service providers, web applications and complex high-level systems. Ohfeld and his team disclosed some of the most...

Read more from Nir Ohfeld](https://thenewstack.io/author/nir-ohfeld/)