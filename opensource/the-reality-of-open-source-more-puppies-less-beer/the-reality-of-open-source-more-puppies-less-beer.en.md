[The aftermath of Bitnami halting its program](https://thenewstack.io/broadcom-ends-free-bitnami-images-forcing-users-to-find-alternatives/) of maintaining a library of popular open source containers and pulling down its popular Helm charts for those containers has left many teams wondering when the next shoe will drop in open source software. Bitnami’s decision caused significant disruption, compelling the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF) to publish a blog post noting that Bitnami’s action [did not affect the open source status of the Helm project](https://www.cncf.io/blog/2025/09/24/cncfs-helm-project-remains-fully-open-source-and-unaffected-by-recent-vendor-deprecations/).

Bitnami’s move is only the latest major instance of changes to open source availability, packaging and licensing affecting business continuity for users. [Elastic](https://thenewstack.io/amazon-elastic-and-the-fight-for-open-source-freedom-in-the-enterprise/), [HashiCorp](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/), [Redis](https://thenewstack.io/redis-is-open-source-again/), [Linkerd](https://thenewstack.io/buoyant-revises-release-model-for-the-linkerd-service-mesh/) and [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) have all made changes that forced teams to reconsider their use of open source components.

The Bitnami episode is another reminder that open source software is more like a free puppy than a free beer. The costs of ownership are significant and should not be ignored.

Every organization, platform and security team not only needs to look at making sure their scanners are running and their application security process is rock solid. They also need to look at every [open source](https://thenewstack.io/open-source/) container they’re running, who maintains it and how much they trust that organization to continue maintaining it. This is also true for all open source packages. And it’s all strictly business.

None of this is to say the companies that made these changes didn’t have business reasons. But in each case, users had to react and pivot. Whether we like it or not, every open source component has to be viewed through the lens of business continuity.

## The Goodwill Myth of the Open Source Ecosystem

There’s a persistent myth in the open source world that somehow thousands of projects are maintained purely through the goodwill of passionate developers contributing in their spare time. In rare instances, this myth is true.

There are some open source developers maintaining critical projects. They are largely maintaining smaller packages or libraries rather than full products. A similar illusion has existed for organizations generating important open source artifacts, like official container images or packages. Witness what happened with Bitnami.

Reality check. Behind virtually every significant open source project or artifact, there’s a company or a foundation. [Someone is funding](https://thenewstack.io/the-metamorphosis-of-open-source-an-industry-in-transition/) the development. Someone is making the investment. And that [someone expects a return](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/).

In the rare instances when no return is expected, an individual developer or small team is building something interesting but treading a tenuous path. They might burn out or opt to hand off their project. Or, as a solo developer, they might lack the bandwidth to put in place security measures that a more robust organization might.

In the end, as much as we hate to say it, open source is about economics, be it for a business or for an individual. If it no longer makes sense to sustain and maintain, then everyone ends up in pain.

## The Imperative To Look Beyond the Usual Metrics

When engineers evaluate open source technology, they typically focus on the technology itself. They look at social signals like GitHub stars, forks, pull requests, the strength of the community, the quality of the code and the feature set.

Hopefully, they also look at how many maintainers a project has, who those maintainers are, where they work, whether the software is part of a foundation and what the licensing terms are. These factors matter, but they’re insufficient for making a sound business decision about what to depend on.

What’s missing? An evaluation of the company, organization or individuals behind the project. Namely, it’s critical to ask: Who’s funding the development? Is it a single company, a consortium, a foundation with diverse backing, or actually just volunteers? If it’s a company, is that company well-funded and stable? How does the business make money?

If the open source project you’re depending on doesn’t directly contribute to the sponsoring company’s revenue model, that’s a red flag. When economic conditions tighten or strategy shifts, nonrevenue-generating projects are the first to be cut or monetized aggressively. What’s the governance model? Does a single company control all the keys? Are there multiple organizations with meaningful input? Can the project easily be forked and maintained if the primary sponsor exits?

The Bitnami changes, for instance, shouldn’t have surprised anyone paying attention to the business fundamentals. When Broadcom acquired [VMware](https://tanzu.vmware.com?utm_content=inline+mention) and subsequently changed the way Bitnami was distributed, the writing was already on the wall. Look at how Broadcom makes money. Look at its history with acquisitions. The move to restrict what was “free” was entirely predictable.

## The Bitnami Wake-Up Call: Dependencies All the Way Down

Bitnami containers and Helm charts are only the top layer of risk. Every open source project depends on dozens or hundreds of other open source projects. Each of those has its own business model, funding source and risk profile. The risk compounds at every layer.

Consider the dependencies most teams don’t even think about. Your application uses a popular web framework. That framework depends on a specific SSL library. That library is maintained almost entirely by engineers at a single large tech company. What happens if that company shifts priorities? What happens if there’s a critical vulnerability and no one is maintaining it?

This cascading dependency risk means you can’t just evaluate the top-level open source components you’re directly using. You need to understand what’s underneath them, and what’s underneath that. It’s turtles all the way down, and most organizations have no visibility into most of those turtles.

## How To Make Better Decisions

The era of adopting open source without thinking deeply about business continuity is over. Here’s what needs to change in how organizations approach open source.

* **Risk assessment must include business model analysis.** Before adopting any significant open source component, teams need to answer these questions. Is there a sustainable business behind this? How does that business make money? What happens if that business fails or changes direction?
* **Supply chain visibility becomes critical.** Organizations need tooling and processes to understand their full dependency tree, not just their direct dependencies. They need to know who maintains each component and assess the risk at every level.
* **Licensing must be thoroughly understood.** Legal and engineering need to work together to [understand what licenses permit](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) and restrict. This isn’t just about compliance. It’s about ensuring you have the freedom to operate if the primary maintainer disappears or changes terms.
* **Have a resilience strategy.** For truly critical components, organizations need to think about their ability to fork and maintain code themselves if necessary. This might mean contributing to projects you depend on, maintaining relationships with other users of the same technology or keeping expertise in-house.
* **Diversify dependencies.** Where possible, avoid single points of failure in your technology stack. If you’re entirely dependent on one company’s open source offerings across multiple components, you’re exposed if that company’s strategy changes. Look for alternatives and be ready to use them.
* **Rely on hardened images where appropriate**. Hardened image providers remove as many dependencies as possible, generating a secure, minimal container image that is more resilient and less dependent on pulling approved container images for repositories. Also, minimalist images are less likely to be vulnerable to common vulnerabilities and exposures (CVEs) landing during periods of turmoil for an open source project or product company.

## What Open Source Resilience Means in Practice

To be clear, this does not mean abandoning open source or becoming paralyzed by risk. Open source remains one of the most powerful forces in technology, enabling innovation and collaboration at unprecedented scale. But we need to be clear-eyed about the entire spectrum of business risks open source presents, and what the costs or required steps are of mitigating those risks. Without planning and foresight, those costs can come due suddenly, as anyone scrambling to rebuild or find an alternative source for Bitnami containers can attest.

Bitnami’s move merely underscores that open source adoption must also be a strategic business decision, not just a technical one. We have to evaluate not just the code, but the company. Not just the current state, but the likely future trajectory. This is more work. It requires different skills and different processes. But it’s the only way to build on open source with confidence, knowing that the foundation you’re building on will still be there tomorrow.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/ed810c7c-cropped-7a56282f-screenshot-2025-11-05-at-3.30.58%E2%80%AFpm.png)

Michael Donovan is vice president of product at Docker. He is an engineer-turned-product leader with a focus on building enterprise applications for some of the world's largest companies. With over 15 years of experience, his mission is to deliver real...

Read more from Michael Donovan](https://thenewstack.io/author/michael-donovan/)