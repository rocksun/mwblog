In its updated 2025 guidance on SBOMs, the [Cybersecurity and Infrastructure Security Agency (CISA) states,](https://www.cisa.gov/sites/default/files/2025-08/2025_CISA_SBOM_Minimum_Elements.pdf) *“An SBOM should include information for all components that make up the target software, including transitive dependencies. There is no minimum depth.”* CISA also indicates that configuration files and fork lineage must be included.

No minimum depth.

A hardened image isn’t hardened until everything, from top to bottom, passes the “sniff test.”

The promise of “hardened” container images is achieving less risk and improved security.

With a bit of savvy and some basic questions about what’s going into an image, security and platform teams can “sniff test” a hardened image to check for [transparency](https://www.docker.com/blog/100-transparency-and-five-pillars/) and accuracy. For any business or organization that is serious about security, these “sniff tests” should be considered valuable tools.

## SBOMs: What they’re supposed to be

To deliver on the promise of supply chain security, a hardened image SBOM must provide [transparency](https://www.docker.com/blog/100-transparency-and-five-pillars/) and include a complete, machine-readable inventory of every component in the image.

### The SBOM test

An SBOM workflow typically includes the following major components: parsing source code, binaries, or container images; validating the SBOM for completeness; cross-referencing components against databases; applying VEX advisories to indicate exploitable vulnerabilities; and scanning the SBOM for licensing compliance.

### Vulnerability scanning and exploitability assessment

A Vulnerability Exploitability eXchange (VEX) document lets you document whether a vulnerability is actually exploitable in your specific context. **Continuous monitoring**: New CVEs are constantly emerging, so it’s imperative that you continuously and automatically check them against your SBOM without re-scanning the artifact itself.

### Compliance and provenance

Your SBOM should list each component’s license (MIT, Apache-2.0, GPL-3.0, etc.) so legal teams can verify that you’re not violating copyleft requirements or using incompatible license combinations. Modern SBOMs can include ~~information on where components came from, who built them, and~~ cryptographic signatures that verify authenticity.

### Supply chain risk management and certifications

When a supply chain attack such as Log4Shell hits, an SBOM paired with proper VEX statements lets you instantly answer “Are we affected?” without waiting for engineering teams to grep through codebases. When a zero-day drops at 2 a.m., you need to know within minutes which systems are affected. An accurate SBOM turns a multi-day investigation into a simple and quick database query.

> When a zero-day drops at 2 a.m., you need to know within minutes which systems are affected. An accurate SBOM turns a multi-day investigation into a simple and quick database query.

**Incompleteness and omissions**: SBOMs can sometimes fail to list every component present in an image. These omissions can be intentional because including every dependency or component can be inconvenient, costly, or delay the release of a hardened image.

**Lack of transparency**: The gap between the promise of total transparency and reality can be wide. The issue here is that if a vendor cannot account for every component, it compromises the trust that is essential to security.

**Validation difficulties**: Verifying an SBOM’s accuracy can be challenging. When a vendor provides only “runtime-only” or “build-only” SBOMs without clear documentation, it becomes difficult for development and/or security teams to know whether they have a complete view of the software supply chain.

**False sense of security**: SBOMs by themselves do not guarantee security. Even with a lengthy, detailed list, if the inventory is incomplete, vulnerability scanners will miss threats due to missing components. This leads to a false sense of safety during audits or even when responding to zero-day incidents.

## **Smelly hardened image SBOMs: More common than you think**

Sometimes, SBOMs don’t pass the sniff test and fail to include every component and artifact. These components are likely omitted because they are inconvenient and would add to the security requirements of the hardened image provider. In some cases, that extra work could delay shipment or be costly.  
  
What are some specific examples of this? Here are three hypothetical examples that are close to real-world discoveries.

### The “latest” tag trap

**The problem**: The latest tag trap refers to depending on floating container tags, such as “latest,” which leads to a false sense of security. For example, you might use the latest tags such as FROM python:latest or FROM mariadb:latest.

**The solution**: Avoid the “latest tag” trap by pinning all container images to immutable SHA256 digests or specific semantic version tags, such as mysql:9-debian-dev.

### Missing package pinning

**The problem**: When developers fail to lock package versions, subsequent builds will automatically pull the latest available versions of the package from the upstream repositories.

**The solution**: This checks whether your SBOM tooling properly captures exact package versions, hashes, and licenses, or defaults to vague, unversioned dependencies that make CVE patching impossible.

### Bloated Base Image (The “Everything Included” Smell)

**The problem**: Using monolithic, bulky base images like FROM ubuntu:latest instead of minimal environments like Alpine or distroless images.

**The solution**: To avoid the missing package pinning issue, pin base images by digest, lock the system and language packages, automate dependency updates, and implement comprehensive image scanning.

Another issue to keep in mind is that AI and ML images often contain extensive dependency trees, including CUDA, PyTorch, and TensorFlow. Because these images can drag in so many frameworks, libraries, and other dependencies, SBOMS must be complete. Ignoring even a single piece of software in these images could lead to disaster.

### Database image… with no OpenSSL

**The problem**: Using a database image with no cryptography

**The solution**: Make sure you use a database image that includes some form of cryptography to protect sensitive data at rest and in transit, such as the Chainguard FIPS images.

### Node.js image without any npm packages

**The problem**: Your Node server’s SBOM doesn’t list any npm packages. None. Nada. Nothing.

**The solution**: If npm packages are used in the build chain or are present in a companion build image, the hardened image vendor should say so and explain their process.

### Enterprise logging with one lonely package

**The problem**: The SBOM shows a single logging library.

**The solution**: Run deep scans and multilingual checks to identify every package included in the image.

## The rapid-fire SBOM sniff test!

Fortunately, every platform and security team can perform a rapid-fire sniff test on SBOMs with a visual scan. This is exactly what it sounds like, and it can be done very quickly. The first step is to ask your vendor whether the SBOM is runtime-only, build-only, or combined, and how it was generated.

Your vendor’s reply may guide you, but you shouldn’t trust it completely. You should immediately proceed to the actual sniff test. This process can take fewer than five minutes and will alert teams to potential SBOM omissions that could later lead to catastrophic failures.

For a basic sniff test, here’s an effective sample workflow.

**Step 1:** Get the SBOM**.**

**Step 2:** Count how many components are listed.

**Step 3:**Look for an entry that says “operating-system” or “alpine” or “ubuntu” or “debian.”

**Step 4:** If you know the image should use Flask, Express, or Spring Boot, make sure it’s there. If so, which version does it include??

**Step 5:** If the SBOM has fewer packages than you would reasonably expect, it could indicate that some packages were omitted or will be added later.

**Step 6:** Search for things you know must be there, such as openssl, ca-certificates, and libc. If they’re missing, the OS layer wasn’t captured.

**Step 7:** Use a container image scanning tool (Docker Scout is one option, but there are also free tools like Syft or Trivy).

## What to demand from hardened image vendors

Hardened image vendors are selling you security and trust. You are paying for this and should demand some basics in return, such as basic credibility, clear scope, validation, transparency, and responsiveness.

## Get a whiff with scratch and sniff

If the SBOM “smells funny” and can’t pass a simple sniff test, do not trust it. Period. If a vendor can’t tell you *exactly* how they build their SBOMs, covering every single step, consider their hardened images suspect. The most important component of any hardened image is trust in the source of truth, and the SBOM must be that.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/5f9772c6-cropped-bfa92ec1-christian-dupuis-600x600.jpeg)

Christian Dupuis is a Senior Principal Software Engineer at Docker with two decades of experience in enterprise software development and cloud native microservice architectures. Prior to Docker, he co-founded Atomist to help reduce barriers to building high-quality software. He previously...

Read more from Christian Dupuis](https://thenewstack.io/author/christian-dupuis/)