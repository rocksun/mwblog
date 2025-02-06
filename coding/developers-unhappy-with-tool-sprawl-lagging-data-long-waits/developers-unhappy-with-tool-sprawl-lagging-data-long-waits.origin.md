# Developers Unhappy With Tool Sprawl, Lagging Data, Long Waits
![Featued image for: Developers Unhappy With Tool Sprawl, Lagging Data, Long Waits](https://cdn.thenewstack.io/media/2025/02/5c86d3ac-dev-portal-2-1024x576.jpg)
[WrongTog](https://unsplash.com/@wrongtog?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on Unsplash.
Over the last couple of years, the tech industry has accelerated efforts to consolidate tooling and increase automation, in an effort to lighten the cognitive load that slows developers down.

The [internal developer portal ](https://thenewstack.io/internal-developer-portals-can-do-more-than-you-think/)has emerged as an effective way to abstract out this complexity through standardization and better service discovery.

Yet only about half of organizations have adopted this industry best practice, according to [Port’s](https://www.getport.io/?utm_content=inline+mention) new “[State of Internal Developer Portals](https://www.getport.io/state-of-internal-developer-portals)” survey. The 2025 report reflected the experience of 300 developers and engineering leadership in the U.S. and Western Europe. It found that, whether they had an internal dev portal or not, two-thirds of engineering teams still have to wait a day or more for operations to respond to their tickets. Because those [site reliability engineering](https://thenewstack.io/observability/) (SRE) and [DevOps](https://thenewstack.io/devops/) teams are battling their own backlog.

Regardless if they are using internal developer portals, devs are still waiting too long, they still distrust data quality and they overwhelmingly feel dissatisfied with their tooling. The state of the internal developer portal certainly reveals a lot about what developers are experiencing in 2025.

## Overall Dissatisfaction With Dev Tools
There’s simply too much Ops in the life of the Dev.

These aren’t just feature requests. A developer’s daily workflow still relies on reaching out to other teams to accomplish standard tasks. In fact, the report found, 27% of developers have to open a pull request for every instance of [Infrastructure as Code](https://thenewstack.io/introduction-to-infrastructure-as-code/). Another 20% of engineers still handle their own operations.

But even those who have some sort of self-service workflow do not love it. A staggering 94% of respondents said they are dissatisfied with their self-service tooling, with the greatest frustration being:

- Creating cloud resources, cited by 48% of survey respondents.
- Determining compliance, 44%.
- Scaffolding new services or APIs, 44%.
Part of that is the sheer number of tools — the vast majority of respondents have six or more tools to jump between. These are often involved in the operational tasks that do not help developers deliver value. In addition, while there’s this push to build a better developer experience, it’s still rare that organizations treat internal developers as customers and [their platforms as a products](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/).

This has 75% of developers wasting between six and 15 hours a week due to tool sprawl — the overwhelming number of tooling choices software developers face. Navigating and integrating all the options negatively affects [developer experience](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/), by breaking flow, overburdening cognitive load and increasing time to feedback.

On the other hand, it’s not all manual approvals that are slowing devs down. Almost half of developers can create a cloud resource, determine compliance and/or scaffold a new service. Just over a third can create a new [Kubernetes](https://thenewstack.io/kubernetes/) cluster. But again, is that where software developers should be focused?

At a time of alleged tool consolidation, there remains a shockingly high amount of sprawl, with a low number of automated steps.

## No Single Source of Truth
To make matters worse, half of all respondents said they don’t trust the quality of their central data repository.

While some suspicion of data quality is wise, a mere 3% of respondents believed their organization’s metadata is completely trustworthy. As the report noted, if developers don’t feel like they can rely on metadata, they begin to rely on DevOps, SREs or other teams for their institutional knowledge. This doesn’t scale.

To make matters worse, significantly more developers distrust data quality than their engineering leaders do, the report also found, which shows another disconnect from the reality of the developer experience.

“Internal developer portals improve metadata quality and trust by centralizing information, standardizing formats and ensuring real-time accuracy,” [Jim Armstrong](https://www.linkedin.com/in/jdarmstro/), head of product marketing at Port, told The New Stack. This is especially important, he said, when data volumes scale, making manual updates unsustainable.

A surprising 17% of engineering organizations that responded still use spreadsheets to track their microservices data. Another 25% responded to the survey that they use configuration management databases (CMDBs) or enterprise asset management (EAM) systems. Neither function great at scale, Armstrong said, as these solutions struggle with larger data volumes, requiring manual updates that reflect only a snapshot in time rather than the real-time state.

“Without a reliable source of truth, developers are left second-guessing data, leading to inefficiencies and unnecessary back-and-forth,” Armstrong said, as well as often incomplete or inaccurate records of software assets and ownership.

It also means developers are, on average, manually updating the software assets’ metadata frequently.

On the other hand, more than half of the organizations interviewed have opted for an internal developer portal or [Backstage](https://github.com/backstage/backstage) open source framework to create their own dev portal. An internal developer portal leverages APIs and plugins to ensure metadata automatically remains accurate and trusted.

“Portals solve this by automatically aggregating and updating information, giving developers and other users an up-to-date view of services, ownership and dependencies,” Armstrong said. “By eliminating outdated or conflicting metadata, portals ensure teams can trust the information they rely on daily.”

## Standards? What Standards?
Perhaps the most concerning realization from this year’s report was developers’ utter lack of clarity around their organization's standards. More than half of respondents said they aren’t aware of the standards, while another third responded with the cryptic “neutral.”

As standards are unique to each organization, internal developer portals are often adopted as a way to ease or enforce compliance — as well as to raise awareness of them. But all developers and engineering leaders surveyed by Port identified gaps in standards that they didn’t think their organization’s engineering processes complied with — but, again, they weren’t sure.

“While many organizations use a similar mix of tools, how their developers are expected to use them — along with coding standards, definitions of production quality, compliance requirements and legal regulations — varies significantly,” Armstrong said.

“A portal must align with these specific standards, ensuring that each user sees only what’s relevant to their role, responsibilities and the organization's broader governance framework.”

This means not inundating your developers with all the rules — though enforcing them with all the rules. Teams should have real-time visibility into anything they are responsible for and authorized to work on, he continued, including open tasks, feature requests, bugs and vulnerabilities — and who is handling what.

“The portal should also surface the relevant organizational standards for my work, clearly showing whether I’m meeting expectations or falling short, and what steps I need to take to stay compliant,” Armstrong said. “This level of personalization ensures that developers can focus on their work without constantly searching for information or second-guessing what applies to them.”

## A Portal Is Not a Panacea
Only 22% of respondents reported that their issues were resolved, on average, within one day. If teams have adopted an internal developer portal, this number increases to 30% — that’s not exactly a huge improvement.

Adoption of an internal developer portal will not automatically drive resolution times down. Armstrong pointed out some ways to improve all these numbers with an internal developer portal:

**Workflow automation.**A portal must enable self-service actions where developers can initiate and complete requests — without manual intervention.**Developer workflow.**Many organizations are still nascent in their portal adoption, which means portal creators should prioritize and measure for optimization of the developer workflow.**Build trust.**These development teams are used to manual approvals and unreliable data. It’s about mapping out and communicating the pre- and post-automation steps and gradually eliminating bottlenecks — not disrupting the developer workflow like flipping a light switch.
When in doubt, talk to your engineers — before, during and after adopting an internal developer portal. Start simply, solving for their biggest concerns and grow your initiative from there. Only then can you improve internal developer portal adoption rates — and rebuild trust in developer tooling.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)