Working in open source software (OSS) sometimes feels like running on a treadmill that never stops. The projects you depend on keep moving, but if you miss a step, you get flung off the back. For many developers, it’s an endless race to keep up with shifting dependencies, urgent common vulnerabilities and exposures (CVEs) and new features.

But not all open source moves at that speed. It exists on a spectrum from fast-moving, feature-rich projects to quietly abandoned ones. In between lies the most overlooked category: [software that is simply “done”](https://thenewstack.io/chainguard-takes-over-maintenance-of-aging-oss-projects/) and ready to graduate into long-term stewardship.

“Done” software should be celebrated. It finally lets developers step off the treadmill without worrying that the ground will shift beneath them.

## **The Underrated Value of ‘Done’ Software**

Not every open source project requires a sprint forever. Some reach a point where the core functionality is complete, the design is stable and the user base is satisfied. “Done” projects become quiet infrastructure that’s dependable and predictable, and only requires occasional maintenance.

[Ingress-nginx](https://github.com/kubernetes/ingress-nginx/) is an example of a project that was “done” long before the community realized it. It’s one of the [most popular open source ingress controllers](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/) for Kubernetes, powering billions of requests in data centers and home labs all around the world. Despite its massive adoption, the project never had more than one or two maintainers who contributed to it in their spare time. Just last month, the Kubernetes community [announced its decision to archive the project](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/) in March 2026.

When a project reaches the “done” phase, it’s an achievement. The code is stable, the design is sound and the community relies on it. These projects are the foundation of a healthy, long-lasting ecosystem, which means they still need occasional upkeep so the community that depends on them can use them securely.

## **Scaling Support for ‘Done’ Projects**

A surprising number of open source projects today have [only one or very few maintainers](https://anchore.com/blog/open-source-is-bigger-than-you-imagine/). When that maintainer wants to step away, people still depend on the project, but no one is formally responsible for its long-term care.

Last year’s [xz-utils incident](https://arstechnica.com/security/2024/03/backdoor-found-in-widely-used-linux-utility-breaks-encrypted-ssh-connections/) showed us what happens when there isn’t a path for handing off projects safely. When xz-utils’ original maintainer — an individual who had dutifully managed its upkeep for 20 years — wanted to step away, a new contributor gradually earned trust, only to [nearly slip in a sophisticated backdoor](https://thenewstack.io/unzipping-the-xz-backdoor-and-its-lessons-for-open-source/). If that attack had succeeded, it could have taken down almost every major system.

We need a way for open source maintainers to gracefully [hand off “done” projects](https://chainguard.dev/unchained/introducing-chainguard-emeritoss) even when they no longer have a significant feature roadmap. We need to offer them a place where:

* Mature projects can transition from individual maintainers to a trusted organization accountable for long-term stewardship.
* CVEs get patched continuously, even without new feature work.
* Reproducibility and trust remain, without weekly commits.

This graduation should signal that the project is stable, valuable and ready for a long life supported by shared responsibility.

## **Forks Are a Critical Strength of Open Source**

Putting a fork in abandoned software is how the community can bring it back to a “done” state. [Kaniko](https://thenewstack.io/kaniko-lives-on-chainguard-forks-googles-dumped-tool/) is one of the clearest examples of this. When Chainguard [forked and took over its maintenance](https://www.chainguard.dev/unchained/fork-yeah-were-bringing-kaniko-back), we inherited a tool that was already doing its job well, which thousands of people relied on. We stepped into the role of long-term custodians for something that was effectively complete. Kaniko required predictable, responsible oversight with occasional updates and minor patches every year. It didn’t need new features. Today, when teams want new features, they can fork Kaniko from a trusted source and build those features themselves.

Forks offer a path for teams to build on a stable foundation without disrupting the project’s core purpose. They preserve user choice, prevent burnout and allow innovation without destabilizing the core. Most importantly, they ensure that open source remains open and free to evolve wherever the community needs it to go.

## **Building a Sustainable Path Forward**

Open source will always have projects that sprint forward and projects that fall behind, but the future of a healthy ecosystem is ensuring mature software has a safe place to land. By establishing graduation paths for “done” software, empowering maintainers to step away safely and encouraging organizations to take on long-term custodial roles, we can prevent the next xz-utils scare.

If working in OSS sometimes feels like running on a treadmill, then “done” software is the rare moment when the pace finally eases. By embracing sustainable stewardship and welcoming forks as part of the open source life cycle, we can build a future where stepping off the treadmill is a sign of success, not failure.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/41b6fad6-danlorenc.jpg)

Dan Lorenc is co-founder and CEO of software supply chain security company Chainguard. Dan has been working on and worrying about containers since 2015 as an engineer and manager. He started projects like Minikube, Skaffold and Kaniko to make containers...

Read more from Dan Lorenc](https://thenewstack.io/author/dan-lorenc/)