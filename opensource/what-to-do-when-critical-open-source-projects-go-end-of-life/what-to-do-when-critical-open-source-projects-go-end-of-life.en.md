Ninety-eight percent of organizations use open source software (OSS) regularly, according to the [Linux Foundation](https://www.linuxfoundation.org/press/press-release/openssf-announces-15-new-members-to-further-strengthen-open-source-software-supply-chain-security). Open source is pervasive. It’s embedded into the fabric of most applications we use in our daily lives. But it’s getting harder to keep up the pace of OSS version deprecations and end-of-life (EOL) cycles.

“The life cycle for open source versions is definitely shortening,” [Aaron Frost](https://www.linkedin.com/in/aaronfrost/), co-founder and CEO at [HeroDevs](https://www.herodevs.com/), which offers long-term support for deprecated open source, told The New Stack. “In 2025 alone, there are over 100 scheduled EOLs for top open source projects.”

These EOLs fall into two main categories: EOLs for minor and major versions, and EOLs for entire projects. An example of the first is [the sunsetting of .NET 6](https://thenewstack.io/herodevs-throws-net-6-users-a-post-deprecation-lifeline/), which occurred in late 2024, but many still rely upon it. An example of the latter would be the [complete sunsetting of AngularJS](https://www.herodevs.com/blog-posts/sunsetting-a-framework-lessons-from-angularjs) by [Google](https://cloud.google.com/?utm_content=inline+mention) in 2021.

The world of open source has seen a string of license shifts, shortening version deprecations and outright retirements for popular OSS packages. It’s not uncommon, even for [highly used open source projects](https://thenewstack.io/open-source-is-at-a-crossroads/), to be abandoned without a clear future.

“Somewhere in the tree of dependencies, almost all teams will have at least one package that is underfunded, planning a major version update, or is even considering closing its doors,” [Timothy Lehnen](https://www.linkedin.com/in/hestenet/), CTO of the nonprofit [Drupal Association](https://www.drupal.org/association), told The New Stack.

Sudden shifts leave developers scratching their heads, hurriedly looking for workarounds, maintaining custom forks or reassessing budgets to support commercial alternatives or long-term support plans. So, [what should developers do](https://thenewstack.io/how-developers-can-head-off-open-source-licensing-problems/) when an open source they highly depend on goes belly up?

When OSS you depend on goes EOL (or worse, completely unmaintained), you need an action plan. Below, we’ll consider how companies can prepare for OSS EOL, what maintainers and vendors are doing to support deprecated projects and offer guidance for developer teams reliant on packages with uncertain futures.

## The Open Source EOL Trend Continues

“We are seeing a significant and accelerating trend of open source projects becoming end of life,” [Alyssa Wright](https://www.linkedin.com/in/alyssapwright/), who helps lead [Bloomberg](https://www.bloomberg.com/company)’s open source program office in the office of the CTO, told The New Stack. She credits this to AI adoption ballooning the sheer number of OSS packages in use across the stack, as well as [rampant maintainer burnout](https://thenewstack.io/beat-developer-burnout-how-the-right-platform-makes-a-difference/).

Maintainer equity issues continue to compound the issue of abandoned projects. [According to a 2024 Tidelift report,](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/) 60% of open source maintainers have quit or considered quitting maintaining a project, with one in five saying they’ve already quit.

“The pace mismatch between rapid OSS release cycles and slower enterprise updates further exacerbates these EOL challenges,” Wright added.

It’s not just “shiny new projects” going away, she said — it’s the workhorse middleware, libraries or older versions of popular frameworks. When lost, these key dependencies are challenging to migrate away from.

That said, not everyone sees a red flag. Recent EOLs have more to do with versions, not necessarily entire projects, according to Lehnen: “There are not very many projects that are actually shutting down — the open source ecosystem is actually very healthy.”

It’s challenging to keep pace with updates for rapidly incremental project versions across the software supply chain. Still, Lehnen argues there have been more improvements in open source, both in terms of [financial assistance](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/) and, specifically, in the case of Drupal, improved governance around the versioning systems in place and support for backward compatibility.

Sudden shifts in open source are nothing new, and much of it represents natural tech cycles, said [Neil Hanlon](https://www.linkedin.com/in/hanlonneil/), founder and director of infrastructure at [Rocky Linux](https://rockylinux.org/), a community-supported CentOS replacement.

“It’s easy to cry foul without context, but many of these changes make more sense once you understand the internal dynamics,” Hanlon told The New Stack.

However, he acknowledged that recent examples of projects undergoing major changes are mounting. “There have been more jarring examples — [Ceph](https://thenewstack.io/ceph-20-years-of-cutting-edge-storage-at-the-edge/) and [oVirt](https://www.ovirt.org/) come to mind — where shifts in stewardship or investment created real concern.”

## OSS Shifts Leave Developers in the Lurch

When an OSS project is abruptly abandoned, it can cause many downstream consequences. These mirror any critical software dependency becoming unsupported: security exposures due to unpatched flaws, increased technical debt due to maintaining old code and compatibility issues.

“One of the most pressing issues is that future security vulnerabilities may not be addressed,” [Donald Fischer](https://www.linkedin.com/in/donaldfischer/), vice president at [Sonar](https://www.sonarsource.com/), provider of a tool for continuous code quality, told The New Stack. This may include vulnerabilities in the package itself, as well as break integrations with [transitive dependencies](https://thenewstack.io/a-guide-to-software-dependencies/), which are other open source packages that a project depends on.

Bloomberg’s Wright cites the lack of bug fixes, performance improvements and community help as other big challenges when the lights go out on a project. “Companies are faced with elevated operational and compliance risks due to potential threats to the stability and uptime of their systems,” she said. This all could erode consumer trust and slow innovation.

Whereas planned EOL is part of a regular risk and life cycle management, abrupt abandonments are harder, said Hanlon. And the ripples affect both users and project maintainers, he added: “People often lash out at the maintainers, but in many cases, it’s burnout or health concerns — especially for solo maintainers.”

## What To Do When a Project Goes EOL

Instead of waiting for a sudden EOL situation, organizations should be well-prepared. This encompasses having an inventory of your critical open source dependencies and keeping an eye out for public end-of-support announcements. But when you’re completely caught off guard, there are a few possible steps to take.

### Gather Information

When projects fade, the first step is to gather information. Is it the whole project that’s gone end of life? Or just a version? If it’s the latter, there may be a simple migration path to a minor or major version.

But if the EOL is more serious, Hanlon encouraged transparent communication: Ask the maintainers why the project reached EOL. “Often, by engaging directly, you’ll learn what’s really going on and sometimes even find a path forward by helping,” he said.

### Assess Damage

Next is damage assessment. To inform a mitigation plan, Wright encouraged assessing the impact of the lost dependency from technical, security and business perspectives. This will inform your blast zone and your research into alternative projects.

“Modern software is built on an interconnected web of dependencies,” said Lehnen. What will be helpful, he said, is creating a “risk management tree” that exposes underlying components used across many projects that will require more support.

### Look for Alternatives

If the maintainer steps away, the next logical step is to look for alternative open source projects that are actively maintained. “In many cases, the best solution will be to migrate your software to use an alternative open source package, or a major version of one, that is actively maintained,” said Fischer. Still, this will require code changes, he added, even with the help of AI assistants.

### Take the Reins

If no suitable replacements exist, you could propose collective stewardship or carry the project torch forward on your own. “For truly key open source components, an organization may consider taking on maintenance internally or contributing heavily to the project,” said Wright.

This flexibility is a fundamental strength of open source, opposed to proprietary software, said Lehnen: “Open source software is not maintained by a single actor and can always bring in new maintainers to support it.”

### Fork It

Another option is to fork the project, but it’s a path that shouldn’t be taken lightly. It may require an entire community to support legacy branches, such as the case with [Debian Long Term Support (LTS)](https://www.debian.org/lts/) or Rocky Linux.

“Forking is a fundamental right in open source, but effective forks require deep domain knowledge, often across multiple systems,” said Hanlon. “It’s not something a random team can just pick up and run with.”

### Loop in the Experts

If you feel totally out of your league, another option is to hire consultants or third-party vendors that maintain private software, build patches or offer extended security support. This, Lehnen said, can provide additional runway for users to upgrade to the latest versions.

However, buying your way out of the problem brings some downsides regarding long-term sustainability. As Fischer noted, “When you move to a private fork of an open source package, you lose many of the practical benefits you had from open source.” You become dependent on an external business and its pricing structures.

In such a situation, Hanlon said, “The know-how exists, but the trick is finding and incentivizing the right experts.”

Another path is [working with open source foundations](https://thenewstack.io/does-your-open-source-project-need-foundation-oversight/) to arrange for extended support.

## The Community’s Role in Sustaining OSS

Beyond post-mortem responses, [sustaining important OSS](https://www.infoworld.com/article/3557846/how-do-we-fund-open-source.html) should really begin further upstream. Avoiding project abandonment altogether will require investing in the projects you actively use.

“That doesn’t just mean money — it means showing up, contributing engineering time, asking thoughtful questions and understanding their roadmap,” said Hanlon. “If your business relies on OSS, you’re part of that ecosystem and part of the responsibility.”

Others share this sentiment and understand the importance of investing in the community. “At Bloomberg, we view this as an opportunity to strategically invest in open source health, in order to turn these risks into a demonstration of our commitment to the public good that is open source,” said Wright.

Organizations like Bloomberg are forming open source program offices and investing in internal strategies to contribute back and retain continuity. “How the industry manages end-of-life practices is critical to the health of the entire digital ecosystem,” Wright added.

Thankfully, the industry is also stepping in to help retain critical EOL open source projects through certain funding initiatives. For example, in June, HeroDevs launched a [$20M open source fund](https://www.herodevs.com/blog-posts/herodevs-launches-20-million-sustainability-fund-for-open-source-creators-to-secure-end-of-life-software) to help support end-of-life OSS, offering support to maintainers of high-impact projects.

Other corporate-led funds, pledges, nonprofit initiatives and new sponsorship models have emerged to sustain projects. For instance, [Bloomberg’s FOSS Contributor Fund](https://www.bloomberg.com/company/stories/bloomberg-ospo-launches-foss-contributor-fund/) has issued grants to over 25 different open source projects since its origin in 2023. [The Open Source Pledge](https://opensourcepledge.com/), another corporate-led initiative, has directed over $2 million toward maintainers to date.

Fischer co-founded Tidelift, which was acquired by Sonar in December. Sonar has continued Tidelift’s program of offering grants to open source maintainers. “Supporting OSS projects financially can be a big help for the maintainers and keep the projects from going EOL,” he said.

Still, for Hanlon, a gap remains: Wealthy companies still optimize for themselves more than the greater good. “I’d love to see more maintainers empowered through vendor-backed support contracts and cooperatives that prioritize both economic and technical sustainability,” he said. “Too many efforts still rely on goodwill or one-sided contracts designed to extract, not sustain.”

And, beyond the technology sphere, support is still nascent, Lehnen noted. “Unfortunately, the wider industry is significantly behind in doing what must be done to ensure the long-term sustainability of critical open source software,” he said. It’ll take time for society to rethink public support for digital public goods in the same way we publicly support physical infrastructure.

## ‘It Shouldn’t Be a Surprise’

Software reaching end of life is a typical part of the development life cycle. “It shouldn’t be a surprise that any part of your software stack is reaching end of life,” said Lehnen, noting how timelines and upgrade paths are typically published well in advance.

However, the challenge is that organizations typically rely on thousands of distinct projects, making tracking every EOL timeline challenging. Automated tools can generate a software bill of materials (SBOM) to help keep a better inventory, Fischer said, but it will still require an active response.

“Armed with that information,” he said, “organizations can look for the telltale signs that key packages are nearing end of life, such as dwindling contributions or slowing release cadence, or explicitly end-of-life announcements.”

Still, for teams currently relying on OSS packages with murky futures, Wright recommended proactively developing migration strategies for high-risk dependencies and communicating the importance of OSS health internally.

It doesn’t hurt to get involved, either. Even small contributions, in the form of bug reports or minor fixes, can make a big difference. So, perhaps the best advice, Hanlon suggested, is to act before it’s too late.

“Don’t wait for a blog post to tell you it’s abandoned,” he said. “Reach out, contribute, sponsor the maintainer, show you care.

“The best time to get involved was yesterday.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/02/96a1456d-cropped-e7e1c083-bill-doerrfeld.jpg)

Bill Doerrfeld is a tech journalist and API thought leader. He is the editor-in-chief of the Nordic APIs blog, a global API community dedicated to making the world more programmable. He is also an active contributor to a handful of...

Read more from Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)