No automaker asks you to pay extra for a seatbelt. The cost is baked into the price of every car because seatbelts prevent harm at an acceptable marginal cost. It’s not even a conversation anymore. Of course your car has a seatbelt.

[Hardened container images](https://thenewstack.io/dockers-sets-free-the-hardened-container-images/) should work the same way. They should be affordable to a two-person startup on day one, ubiquitous by default and treated as a public good that raises safety for everyone. That means minimal bases, non-root execution, read-only filesystems, pinned and verified dependencies, signed provenance and rebuilds on every common vulnerability and exposure (CVE).

These should be standard equipment, not an upsell or a special feature. Vendors can make money in other ways. Open source projects will benefit from having a basic hardened option as an offering for users who wish to start with a minimal attack surface and an official image.

## We’ve Done This Before With HTTPS and TLS

Ten years ago, [HTTPS](https://thenewstack.io/http-3-is-now-a-standard-why-use-it-and-how-to-get-started/) was optional for most websites. Certificates cost money. Configuration was fiddly. Many sites skipped it entirely, leaving users exposed to eavesdropping and man-in-the-middle attacks.

Then Let’s Encrypt launched in 2015, offering free, automated certificates. Browser vendors started marking HTTP sites as “not secure.” Within a few years, HTTPS went from a nice-to-have to table stakes.

Today, over 95% of web traffic is encrypted. No government mandate made that happen. A nonprofit made certificates free and easy, browsers applied social pressure and the default flipped.

The story of TLS adoption follows the same arc. For years, enabling [TLS](https://thenewstack.io/mutual-tls-microservices-encryption-for-service-mesh/) on email servers, databases and internal services was treated as optional hardening, something security-conscious teams did if they had the time and expertise.

Then, cloud providers and platforms started enabling TLS by default. [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure and Google Cloud Platform (GCP) made encrypted connections the path of least resistance. The [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) added TLS as a core requirement for Kubernetes security. Once the default changed, running unencrypted internal traffic became the exception that required justification rather than the other way around.

More recently, the open source community and vendors working with that community rallied around [Docker Official Images (DOI)](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) on Docker Hub. DOI was a way for container users to be sure they were only pulling images from the official project source. The DOI designation became widely popular as the source of truth for clean, official open source images.

When you make the secure option free, easy and default, adoption follows without mandates. What’s more, raising the security standard is something that all vendors will support because, ultimately, it saves them toil and trouble and improves the experience for their customers. It’s a win-win for everyone.

## Security Externalities Are Everyone’s Problem

Software development is barreling ahead at breakneck speed. AI-assisted coding is accelerating velocity. Companies push more code, more quickly, into production environments built on shared foundations. This stresses already stressed patching practices, accelerating the security treadmill and increasing risks for everyone.

Organizations face a tidal wave of CVEs that even sophisticated security teams struggle to triage. Supply chain attacks against widely used packages put millions of servers at risk. Equally critical, the very nature of modern software stacks has become dizzyingly complex and fast-changing. An organization may have literally thousands of software components deployed. And modern developers adopt new open source components more quickly than hardening efforts can keep up.

Forcing technology teams to monkey with configuration settings or allowing them to tweak so-called “golden images” opens the door to many human mistakes that result in breaches and other problems. Expecting them to keep up with the latest security requirements on all the new technologies they try out is asking the impossible.

At the same time, we’re entering an era of AI-enabled vulnerability discovery and exploitation. The bad guys are using it and will be good at AI, too.

In this environment, one team’s unpatched base image or vulnerable open source component quickly becomes everyone’s incident. Any component that is deployed without signed provenance invites compromise, from [typosquatting Node.js packages](https://thenewstack.io/18-popular-npm-packages-compromised-in-attack/) to [dependency-confusion attacks](https://thenewstack.io/npm-security-woes-continue-amidst-a-series-of-cdn-attacks/) that trick builds into pulling attacker-controlled “internal” artifacts, to compromised CI/CD pipelines that silently swap trusted binaries or container images after the code has already been reviewed.

Even smart teams can suffer this fate because to err is human, and the security patching game is unwinnable. In this landscape, supply chain drift leaks laterally across platforms, clouds and customers.

When non-root execution, read-only filesystems, least-capability defaults and signed provenance become table stakes, entire classes of routine compromises fail before they start. The fewer soft targets in the commons, the less oxygen for botnets, cryptominers and opportunistic worms.

This is the “seatbelts” argument, protecting everyone across a wide swath of the technology ecosystem. Just like HTTPS, technology herd immunity only works when the secure default is accessible to everyone at the low, low price of free and easy.

## Safety Features Are Cheap At Scale

So who builds all this stuff, you may say. No doubt, building a first-class hardening pipeline costs real money. You need curation, policy as code, [SLSA](https://thenewstack.io/securing-the-software-supply-chain-with-slsa/)-level attestations, automated rebuilds and, of course, AI guardrails to check your work. But once that infrastructure exists, the per-image marginal cost drops dramatically. Most of the ongoing work is automation and content distribution.

This is exactly how Let’s Encrypt operates. Building and running the certificate authority costs money. Issuing individual certificates costs nearly nothing. The infrastructure investment is amortized across hundreds of millions of certificates. It’s a classic example of economies of scale.

Hardened images follow the same economics. An organization that specializes in hardening can absorb the infrastructure cost and distribute hardened images at marginal cost. The seatbelt gets baked into the car.

## The Business Model Already Exists

Car makers don’t charge extra for seatbelts. They make their margins on trim packages, premium features and service. Seatbelts are *de minimis* — a trifling — and included by default because no manufacturer wants to be the one that ships cars without them.

The same model works for container security. Everyone gets the free baseline: minimal, reproducible base images with no shells or unnecessary tools, non-root execution with dropped capabilities and seccomp profiles, read-only filesystems and locked-down network defaults, pinned and verified dependencies with software bills of materials (SBOMs ) and [Vulnerability Exploitability eXchange (VEX)](https://thenewstack.io/youll-soon-be-using-vulnerability-exploitability-exchange/), continuous rebuilds on CVE and Known Exploited Vulnerabilities Catalog (KEV) signals, and cryptographic signing with machine-verifiable attestations.

Enterprises pay for premium services: FIPS- or Federal Information Processing Standard-validated cryptography, extended LTS branches with severity service-level agreements, regulator-specific attestations and compliance documentation, dedicated mirrors, air-gapped updates, region-specific distribution, migration assistance, break-glass support, custom policy packs and long-term support well beyond standard end-of-life horizons.

Once image hardening is table stakes, then vendors will be incentivized to innovate in new ways to improve their products and user experiences beyond basic security. In the car business, initial seatbelt mandates for three-point restraints led to a series of complementary innovations like seat-belt pre-tensioners, airbags and crumple zones to absorb impact. By solving the safety problem, automakers could then shift their focus and resources to other, more enticing innovations that improved user experience, like better entertainment systems and ergonomic seat controls.

You pay extra for the chauffeur, the four-point racing harness and the vintage car maintenance program. The seatbelt is standard. However, this standard works best with a software-specific twist.

Free hardened images will help everyone if they are simple enough for everyone to retrofit onto their applications. So every application that was designed and deployed prior to hardened images becoming widely desired can easily be retrofitted.

And, should users choose to make changes in their stack, the hardened images can easily be adapted with minimal toil. It should feel more like changing windshield wiper blades than major surgery, a basic task that is easy for any hobbyist, student, small business, startup or enterprise platform team to accomplish.

## Overcoming Price and Complexity as Barriers to Adoption

For hobbyists, students and solo maintainers who might be working on critical open source projects, paying for hardened images was never an option. For startups and small businesses, paying for hardened images competes with every other budget priority. Many simply don’t pay, and they run whatever base image comes up first in a search.

But even organizations with a healthy security budget often run bloated, unpatched images. The problem isn’t always money. It’s expertise and activation energy. Building a hardening pipeline requires specialized knowledge that many teams don’t have.

This is why free alone isn’t enough. It has to be free and easy. Let’s Encrypt didn’t just eliminate certificate costs. It automated the entire issuance and renewal process. You didn’t need to understand [public key infrastructure](https://thenewstack.io/three-vital-aspects-of-financial-grade-security/). You ran a command and got HTTPS.

Hardened images need the same approach. Pull the image and you get the secure default. No pipeline to build, no policies to write, no attestation infrastructure to maintain. The complexity is absorbed by the provider.

## Applying the ‘Let’s Encrypt’ Model to Container Security

This isn’t an abstract call for “the industry” to do better. The container infrastructure, and the vendors who build on top of it, are well-positioned to make this happen.

We are already in a world where hardened images as a free baseline that anyone can access is a feature flag away. A startup on day one gets the same foundational security as an enterprise. No, they won’t get the SLAs, the FIPS validation or the dedicated support. But they get the seatbelt, and that keeps them and everyone around them safer.

When every major image ships hardened by default, running an unhardened base becomes the exception that requires justification. The default flips, just like it did for HTTPS. And the entire ecosystem gets safer as a result. We are now [offering hardened images for free](https://www.docker.com/press-release/docker-makes-hardened-images-free-open-and-transparent-for-everyone/). We hope every other company “selling” hardened images follows suit. This is the best path to a more secure software supply chain as a default setting.

## Stay Safe Out There

Make hardened images as universal and affordable as seatbelts. Make them standard, boring and everywhere. Vendors will still make money, just not by gating the safety features. We have the precedent from HTTPS and TLS. The economics work because marginal costs collapse at scale.

Containers are the mechanism. Now it’s time to flip the default and buckle up.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/ed810c7c-cropped-7a56282f-screenshot-2025-11-05-at-3.30.58%E2%80%AFpm.png)

Michael Donovan is vice president of product at Docker. He is an engineer-turned-product leader with a focus on building enterprise applications for some of the world's largest companies. With over 15 years of experience, his mission is to deliver real...

Read more from Michael Donovan](https://thenewstack.io/author/michael-donovan/)