Just a week after [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) [announced Chainguard Factory 2.0](https://thenewstack.io/chainguard-admitted-factory-1-0-was-brittle-heres-how-2-0-fixes-it/), the company has hit a major milestone that demonstrates the scale of the system now running in production.

Last week, Chainguard said that its software factory, rebuilt around its [DriftlessAF](https://c67dcd9a.streak-link.com/Cwrwy4caWmL0IF9LOQzCv3K1/https%3A%2F%2Fgithub.com%2Fdriftlessaf) open-source agentic reconciliation, had produced more than 500 million unique container build manifests to date. DriftlessAF is an agentic framework that enables bots to use both traditional and agentic AI evaluation approaches to automate reconciliation at scale.

“The emergence and adoption of bleeding-edge AI productivity tools within Chainguard has built up a level of agentic expertise across our engineering team,” Chainguard states in a [blog post](https://www.chainguard.dev/unchained/driftlessaf-introducing-chainguard-factory-2-0).

Rather than scanning or patching upstream binaries, Chainguard regenerates containers and libraries directly from source whenever a change is detected. Factory 2.0 drives all of this.

It operates as a self-correcting system at a massive scale: Each container build manifest represents a reproducible output of the system, spanning initial builds, dependency and vulnerability-driven rebuilds, tooling changes, and generated [SBOMs](https://thenewstack.io/sboms-sboms-everywhere/) and signatures, all reconciled toward a secure-by-default state, the company said.

## Beyond manifests

In addition to surpassing 500 million container build manifests, with millions more generated every month, Factory 2.0 continuously maintains:

* **2,000+** (2,069 at the time this interview) open source projects, offering a minimal, low- or zero-CVE Chainguard image to projects including go, nginx, and [Postgres](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/)
* **340,000+** container image versions, delivering rapid availability of new releases and access to historical versions as upstream projects and architectures evolve
* **27,000+** underlying OS packages assembled and maintained over time

[Dustin Kirkland](https://www.linkedin.com/in/dustinkirkland/), SVP at Chainguard, tells *The New Stack*that the milestone is a sign of stability.

“We’re on a pretty predictable path at this point of adding images to our catalog,” Kirkland says. “We crossed the number 2,000 unique images completely deduplicated across versions, flavors, and architectures.”

That’s a raw number showing the scope of the unique image package projects that Chainguard has hardened and maintains, with zero CVEs for its customers.

“But the big news, the milestone moment, is that we crossed the 2000 images mark. And we’re not stopping there,” Kirkland says. “We’re adding almost 100 images per month to the catalog at this point.

## Half a billion

In addition to the half a billion container build manifests, Chainguard is adding almost a million of those permutations per day, 1.3 million yesterday, Kirkland said. That also includes customers who’ve modified their image or an image that they’re using Chainguard’s custom assembly feature.

That’s something Chainguard announced last year: it allows customers to add or, in some cases, remove images or configurations from their images while still running them through Chainguard’s build system and remaining covered by Chainguard’s service-level agreements.

“Securing the entire software supply chain requires deep technical prowess and automation,” said [Dan Lorenc](https://www.linkedin.com/in/danlorenc/), CEO and co-founder of Chainguard. “Our software factory continuously rebuilds every open source component that engineering teams rely on directly from source and maintains these components continuously over time.”

## 400 organizations

Nearly 400 organizations, from Fortune 500 organizations to startups, use Chainguard Containers. In the past quarter, companies like Black Duck, Nelnet, Rocket Lab, and SolarWinds began building with Chainguard.

“At Second Front, we make it faster and easier to deliver secure, compliant software to government teams and missions where security is non-negotiable,” said [Jeff Davis](https://www.linkedin.com/in/jefedavis/), senior staff platform engineer at [Second Front](https://www.secondfront.com/), in a statement. “Access to Chainguard’s full catalog gives us access to an extensive library of secure, trusted open source images. No surprises, no hoops to jump through, just the freedom to move fast with security and trust built in.”

Chainguard also added new features to simplify the customer experience, including improvements to the Helm Chart user experience and predictable lifecycle management through Chainguard’s new end-of-life updates.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)