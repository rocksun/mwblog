Containerization has transformed how teams build and deploy applications, but it’s also introduced new operational challenges. Traditional [container images](https://thenewstack.io/introduction-to-containers/) often include far more components than necessary — shell utilities, package managers and libraries that never get used by the running application. This bloat increases image sizes, slows deployment and broadens the attack surface.

To meet modern performance and security demands, the industry should consider shifting toward more minimal, deterministic images. This is where chiseled containers — images that include only what’s essential to run the application and nothing else — offer a new path forward.

## **What Are Chiseled Containers?**

Chiseled containers are built by removing most nonessential components from a base image — no shell, no package manager, no runtime dependencies beyond what the application strictly requires. The concept was implemented in the [Ubuntu ecosystem](https://thenewstack.io/why-broadcoms-ubuntu-bet-on-vmware-will-delight-devs-and-ops/), where automation “chisels away” unnecessary layers while maintaining identical runtime behavior and stability. The same principle can be applied across other [Linux distributions and frameworks](https://thenewstack.io/introduction-to-linux-operating-system/).

For example, Canonical benchmarks show image size reductions of up to 90% for .NET applications and about 50% for [Java](https://thenewstack.io/introduction-to-java-programming-language/) workloads compared to standard Ubuntu base images. Smaller images mean faster deployment, fewer CVEs and easier compliance.

[![Bar chart comparing image sizes for chiseled vs. nonchiseled images](https://cdn.thenewstack.io/media/2025/11/4eae37d4-chiseled-nonchisled-graph.jpg)](https://cdn.thenewstack.io/media/2025/11/4eae37d4-chiseled-nonchisled-graph.jpg)

(Source: Broadcom)

## **Why Organizations Are Adopting Chiseled Containers**

Reducing images to only the essential components improves:

* **Security and compliance:** By removing shells, compilers and package tools, chiseled containers significantly reduce exposure to common CVEs. This approach trims up to 80% of a container’s attack surface compared to a traditional image, according to Ubuntu, dramatically reducing the risk of vulnerabilities. This simplifies patching workflows and helps teams maintain compliance based on their regulatory needs, such as Security Technical Implementation Guides (STIG) and Federal Information Processing Standards (FIPS).
* **Performance and efficiency:** Smaller images translate directly into faster pulls, shorter startup times, and lower bandwidth and storage costs. These are especially critical for large-scale microservices or edge workloads.
* **Operational simplicity:** Chiseled containers are deterministic and immutable by design. Without shells or package managers, runtime modification is impossible, which enables consistent builds across environments and eliminates classic “it works on my machine” issues.
* **Sustainability:** Leaner images consume fewer compute and network resources, reducing both cost and environmental footprint.

These benefits translate directly into practical advantages across several key deployment scenarios.

## **Recommended Use Cases for Minimal Images**

Following are some of the areas where chiseled containers are most useful.

* **Regulated workloads:** Healthcare, finance and public sector workloads benefit from secure, predictable auditable runtime environments.
* **E-commerce and burst capacity:** Chiseled containers enable e-commerce and other bursty applications to scale rapidly during traffic spikes, reducing cost and energy use through faster startup and lower overhead.
* **Edge and IoT deployments:** Minimal images deploy quickly over limited connections and run efficiently on constrained devices.

## **How Chiseled Containers Integrate With VKS**

As enterprises adopt minimal container images, consistency across their Kubernetes environments becomes essential. [VMware vSphere Kubernetes Service](https://blogs.vmware.com/cloud-foundation/2025/08/26/broadcom-canonical-partnership/) (VKS), the [CNCF](https://cncf.io/?utm_content=inline+mention)-certified Kubernetes runtime built into VMware Cloud Foundation (VCF), enables platform engineers to deploy and manage both traditional and chiseled containers within a unified platform.

With integrated multicluster management, centralized policy enforcement and a consistent security model, VKS helps teams operationalize minimal, deterministic images while maintaining compliance across clouds and data centers.

Canonical’s chiseled Ubuntu containers, when deployed on VCF, illustrate how organizations can achieve both high performance and strong security within an enterprise Kubernetes footprint.

This demo highlights the advantages of using Canonical’s chiseled Ubuntu containers on VMware Cloud Foundation (VCF).

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## **The Future of Secure Application Deployment**

Chiseled containers aren’t just smaller. They represent a smarter, more secure foundation for modern applications. By removing nonessential components, they deliver measurable improvements in efficiency, reproducibility and compliance. As more organizations modernize their platforms, adopting minimal, deterministic images will become a standard best practice.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2019/12/cd70dd44-f375f18e-aj378412-600x600.jpg)

Pankaj Gupta is Senior Director of Private Cloud Solutions at VMware by Broadcom, where he helps customers unlock the full value of their private cloud investments. Previously, he led go to market initiatives across networking, security, and cloud portfolios at...

Read more from Pankaj Gupta](https://thenewstack.io/author/pankajgupta/)