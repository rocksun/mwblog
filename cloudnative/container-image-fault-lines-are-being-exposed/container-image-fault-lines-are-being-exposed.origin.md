# Container Image Fault Lines Are Being Exposed
![Featued image for: Container Image Fault Lines Are Being Exposed](https://cdn.thenewstack.io/media/2024/07/358d615b-container-images-fault-lines-exposed-1024x576.jpg)
With nearly 16,000 faults in California — and 500 of them “active” — [scientists say](https://www.californiaresidentialmitigationprogram.com/resources/blog/california-earthquake-probabilities) there is more than a 95% chance of a major earthquake in the next 30 years. That’s why in 2013, San Francisco implemented a mandatory seismic retrofit program, which [more than 90%](https://www.nbcbayarea.com/investigations/soft-story-retrofits-in-san-francisco/3267556/) of target structures have successfully completed.

We’re in a similar spot today in software supply chain security, where much of the industry was spooked by the [XZ Utils threat](https://www.chainguard.dev/unchained/if-xzs-backdoors-are-inevitable-how-do-we-stay-secure-the-answer-is-move-faster), which quickly joined other vulnerabilities like [SolarWinds](https://thenewstack.io/lessons-learned-from-2021-software-supply-chain-attacks/) and [Log4j](https://thenewstack.io/one-year-of-log4j/) in infamy. Companies are taking a hard look at their supply chains and wondering what they can do to protect themselves against the “big one.”

Let’s take a look at the foundational issues that have made software supply chain security such a tricky domain, some of the important foundational work that’s being done on the fault lines, and some tips for how you should be thinking about how to best future-proof your company from major software vulnerabilities moving forward

## Exposing the Fault Lines in Software Security
According to [Sonatype](https://www.sonatype.com/?utm_content=inline+mention)‘s [9th Annual State of the Software Supply Chain](https://www.sonatype.com/state-of-the-software-supply-chain/Introduction), there were more than 245,000 malicious [open source packages](https://thenewstack.io/do-open-source-obligations-change-with-packaging-ecosystems/) discovered in the last year (twice the number of all previous years combined). They also found 1 in 8 downloads of open source packages included known risks.

The foundation of software security has some serious cracks that need to be dealt with.

One area where there’s clearly room for improvement is provenance. When you are installing a [container](https://thenewstack.io/containers/) image, you have to know where it came from — but too many developers are still relying on the name of the image, based on the namespace of the repository and the registry it came from. They trust an image because it has a large number of downloads, or turned up first in a search, or because its name indicates it came from their organization or another trusted registry. But this type of data from the namespace is wholly unreliable: Bad actors can mimic naming conventions, and the name proves nothing of an image’s origins — let alone who may have tampered with it in transit.

There’s also a separate problem with reproducibility. Even if I have a Dockerfile and the source used to create the image, if I run a Docker build again, I’ll end up with a slightly different image. There will be things like different timestamps and build IDs, which means I’ll end up with an image that is not identical, bit-wise.

And security scanning is a Whac-A-Mole game. These are great tools that are really powerful, but they give us a lot of output for a majority of container images. Most organizations don’t know what to do with this output. If you get 100 vulnerabilities or 200 vulnerabilities, what do you do with that? You don’t have time to go and investigate each one. And even if you do, the next week, there’s a dozen more. It’s a very difficult situation.

Last but not least, gauging exposure is incredibly difficult. If a vulnerability drops tomorrow and it looks important, CISOs would like to be able to pinpoint the containers they are running in production that are potentially exposed to the vulnerability. But the reality is that even organizations that are attempting to use [software bills of materials (SBOMs)](https://thenewstack.io/a-good-sbom-is-hard-to-find/) are far from able to identify all their software. Existing tooling often misses items and transitive dependencies. (You might not be using a vulnerable library directly, but the database you’re running in production could be!)

When your software supply chain links to a foundation with this many unknowns, not only are you bringing vulnerabilities into your environment: You also can’t even verify what you are running in such a way that would allow for quicker remediation.

Let’s take a look at two key steps for getting this problem under control.

## Sign and Verify the Software You Bring in
The last two years have seen significant progress in adding signatures to container images, primarily due to the widespread adoption of the [Sigstore](https://www.sigstore.dev/) project. This progress greatly increases the ability to understand and prove the provenance of images — where they came from, who built them and if they have been unexpectedly changed in any way.

Sigstore is now used to sign all of the [Kubernetes](https://roadmap.sh/kubernetes) project’s official images, and it is also being adopted in the npm and Homebrew package ecosystems. Sigstore signatures can be stored directly in container registries alongside images, so you don’t have to run separate infrastructure to store signatures. Sigstore also supports “keyless” signing via the OpenID Connect (OIDC) protocol, so you don’t have to worry about keeping private keys safe.

There’s no point in signing things if you aren’t also checking the signatures. Today, the way that’s commonly done in the Kubernetes cluster is to use a policy management tool such as Kyverno or Open Policy Agent (OPA).

## Eliminate Bloat in Your Base Images
The typical container image ships with a lot of bloat — typically, operating system tooling provided by the base Linux distribution — that is not needed to run the application. As well as increasing storage and transfer costs, this bloat represents risk, as it can potentially contain exploitable vulnerabilities.

For example, look at an [NGINX](https://www.nginx.com?utm_content=inline+mention) image in the [Docker](https://www.docker.com/?utm_content=inline+mention) Hub (using Debian by default) and run Snyk, Trivy, Grype or any other scanner. You will find on the order of 100+ dependencies that ship with that single NGINX image, and you inherit the corresponding vulnerabilities whether or not you use any of those other software artifacts.

There’s a cost to those hundreds of dependencies and vulnerabilities that come with the bloat in the typical container image. Even if only a small percentage of the vulnerabilities are realistically exploitable, they cloud your ability to reason with your environment.

It is possible to cut this noise down drastically and get to the point where your reports find only a handful of vulnerabilities that you can cope with. Basically, the answer is to cut the software components in your container images down to the very minimum set of dependencies required, and to continuously update that set.

## What a Better Supply Chain Foundation Buys
In the short term, the combination of using software signatures and minimalist distros and container images will buy you a lot less exposure: exposure to vulnerabilities, exposure to transitive dependencies and exposure to software that has been tampered with.

The point of all this work is to get to a point where you know — and can prove — where all your software comes from, and to be able to exhaustively identify all versions of all software in use. There will always be vulnerabilities, but by using minimal, hardened images, you can minimize the number, and be in a position to immediately identify all occurrences of vulnerable software when the next “big one” hits.

[Chainguard Images](https://www.chainguard.dev/chainguard-images) gives security teams that crucial “Zero CVE” starting point for software supply chain security — container images that are minimal in design, with built-in attestations that describe the origins and exact versions of all of the packages, and continuously updated to remediate new vulnerabilities.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)