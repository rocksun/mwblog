# Is Cloud Native a Vibe? Power Users Weigh In
![Featued image for: Is Cloud Native a Vibe? Power Users Weigh In](https://cdn.thenewstack.io/media/2024/07/69288783-cloud-native-vibe-power-users-1024x576.jpg)
Since publishing the [State of Cloud Native Application Platforms 2024](https://go-vmware.broadcom.com/2024-State-of-Cloud-Native-App-Platforms) report in June, we’ve been gathering reactions from the architects, engineers, tech practitioners and IT leaders that represent the [Tanzu Vanguard](https://tanzuvanguard.com/), a community of VMware [Tanzu](https://thenewstack.io/vmware-expands-tanzu-into-a-full-platform-engineering-environment/) Platform power users. This report (and its [ State of Kubernetes](https://tanzu.vmware.com/content/ebooks/stateofkubernetes-2023) predecessor) annually helps readers understand what their peers are doing, what they’re most challenged by and how they’re addressing their most demanding needs.

This year was no different. Organizations are seeing clear value from cloud native architectures, container adoption and application platforms. However, the [need for consistency](https://tanzu.vmware.com/content/blog/2024-trends-in-cloud-native-app-platforms) alongside a growing need for multiple application types and deployment patterns has never been greater.

With these factors in mind, we’ve gathered reactions to the report from the Tanzu Vanguard.

## What Does Cloud Native Mean in Practice?
For the first time, this year the survey asked what it means to be a cloud native enterprise. When asked “When you think of a [cloud native enterprise](https://thenewstack.io/cloud-native/), what comes to mind?” 40% of respondents included “It’s a mindset.” The Tanzu Vanguard members’ perspective echoed that of the survey respondents, with some simply stating it’s about being “cloud agnostic,” like [Todd Kabella](https://www.linkedin.com/in/toddkabella/), a senior systems engineer at CSG International. Others highlighted approaches to application development and architectures.

“*Cloud native for me is a mindset and methodology of building applications following the **12-factor app methodology**. Just because the app is containerized doesn’t mean it’s cloud native. Similarly, just because an app is running in a public cloud doesn’t mean it’s cloud native.”
*

**—**
[Pawel Piotrowski](https://www.linkedin.com/in/pawel-piotrowski-69150350), solutions architect at Axians Poland“*For me, the key attribute that differentiates a cloud native enterprise is continuity. This manifests in several ways:*

*Continuous learning culture: This allows employees to not only stay updated on existing practices but to also anticipate future needs and plan effectively.**Continuous automation: As learning progresses, manual tasks become automated using Infrastructure as Code (IaC) and data-driven approaches, streamlining delivery.**Continuous experimentation and innovation: The combination of learning and automation creates room for continuous experimentation with new technologies, fostering a culture of innovation.”*
**— Jaroslaw Gajewski, lead architect at Eviden/Atos**
“*Cloud native is more than just a way of building apps; it’s a lifestyle and a state of mind. A company that has accepted this fact is working along agile principles with single teams having responsibility for the full lifecycle of their products, which means they own the product. Often, companies like this have **flat hierarchies and value the individual knowledge of every employee to drive the products forward. Surely this is only possible with technology that supports these modern operating models, and it’s much more than just the technology.”
*

**—**
[Jürgen Sußner](https://www.linkedin.com/in/j%C3%BCrgen-su%C3%9Fner-085154192/), enterprise architect at DATEV## Application and Deployment Pattern Diversity Abounds
Another striking finding from the report: Many enterprises are using multiple platforms to support the various application types and deployment patterns that different teams are building and using. This trend compounds the complexity already associated with distributed and hybrid architectures. We asked the Vanguards about this and found that the struggle is real!

“*This is true for us! Depending on the app/business model of a particular organization or specific [line of business] LoB, it might be the case that different patterns are required for different application types. This is the same as with overall infrastructure design — there is no single design that would fit everyone.”
*

**— Pawel Piotrowski**
“*Modernizing an application estate is a continuous process, and the shift from old, monolithic applications to modern service-oriented architectures is often slow and only partially feasible. It’s crucial not to force everything into a container and run it on Kubernetes; some things, like large monolithic applications, are simply not meant to be containerized. It’s necessary to have a platform that can support the full spectrum of your application portfolio.”
*

**—**
[Maximilian Marshall](https://www.linkedin.com/in/maximilian-marschall-8a395918a/), unit lead, Cloud Native International, at Evoila“*You will need more than one path to production, although there may be one standard starting path or starting point that’s suitable for 80% of your teams. But there will be teams with challenges that are simply not covered by the default path. This may mean more complex release strategies or more sophisticated technology selections. So having multiple curated paths is not an anti-pattern; it’s a normal evolution.”
*

**— Jürgen Sussner**
“*While this is true, I think that sometimes we are misinterpreting lack of standardization as multiple patterns, which can lead to a significant increase of entropy.”
*

**— Jaroslaw Gajewski**
## Platform Proliferation Persists
One of our favorite findings in this research is that both [platform engineering teams and developers](https://thenewstack.io/platform-engineers-developers-are-your-customers/) value platform choice. However, as the number of cloud native application platforms and patterns expands, so does complexity and the need for a single platform experience — not just for developers but also for the [platform and I/O engineering teams](https://go-vmware.broadcom.com/cloud-native-platforms-require-infrastructure-platform-engineering) who are building, managing and updating them. This is critical for organizations that need to scale based on seasonal market dynamics, major events and other external factors they can’t control.

“*We use multiple platforms, however we try to keep it within some boundaries and try to standardize it as much as possible where reasonable. Proliferation is mostly caused by multiple teams with different, unique experiences and preferences.”
*

**— Pawel Piotrowski**
“*We are trying to unify platforms as much as we can. For example, we’ve merged many of our applications and are now doing the same with our Kubernetes platforms and cloud implementations.”
*

**—**
[Luis Freixas](https://www.linkedin.com/in/luis-freixas-67217052/), IT administrator at LFConsulting“*It will always be important to have simple management for all your platforms and applications running on them. The quest for a one-platform experience should not, however, interfere with the application itself. Striking a balance between repeatability and innovation is precarious without a cloud native application platform. The commentary on page 14 of **the report** resonates [with me]: ‘This could signal a desire to simplify the status quo, but without giving up the flexibility that is a hallmark of a cloud native mindset.'”
*

**—**
[Christoph Villnow](https://www.linkedin.com/in/hyperconverged/), technical lead at Unique Projects## Security’s Place in Platform Engineering
More than two-thirds of our survey respondents work in a highly regulated industry, which means they are dealing with constant regulatory hurdles and policies. As such, platform engineering teams have to work more closely with their security counterparts to ensure security, compliance, governance and enforcement at scale.

While there is still healthy skepticism from security teams about working with platform engineering, to embrace a [DevSecOps](https://thenewstack.io/build-software-supply-chain-trust-with-a-devsecops-platform/) model, this dynamic needs to change. Compliance, governance and continuous security are platform engineering superpowers that can transform the way we secure applications, regardless where they are running, with little impact on developer experience.

“*Most security teams lack sufficient knowledge about container workloads and how to address the new challenges they present. Additionally, the traditional division between infrastructure, network and security can be quite problematic, as these areas tend to blend into each other in the cloud native ecosystem.”
*

**— Maximilian Marshall**
“*Cloud native security** is totally different than traditional enterprise security. Traditionally, security has been a gate someone has to go through on their way to production. Applying this to cloud native would disrupt the continuous delivery and improvement process. Therefore, security has to be part of the pipeline — not just shifted left, but shifted everywhere. Meanwhile, platform engineers need overall visibility of the whole application landscape to see who is affected by what and how to fix it or if it was fixed. That’s why cloud native application protection platforms are gaining importance.”*

**— Jürgen Sussner**
“*I work with security teams on a daily basis. My observation is that security teams are barely able to keep up the pace of change in today’s application platform landscape. To be fair, tech cycles are seemingly moving faster than ever. Their skepticism is understandable, but they also need to embrace a new cloud native security mindset rather than applying obsolete security strategies that hinder innovation and their ability to compete.”
*

**— Pawel Piotrowski**
“*Central IT has, in all its decades, never lived up to the expectations of the average security team. And the distrust often goes both ways, with governance teams inside enterprises often being seen as obstacles to rapid iteration and innovation. Cloud native technology is by-and-large still considered ‘unproven’ by many enterprises, and its ecosystem often feels like a ‘Wild West.’ Often, security teams are too behind on this ecosystem to even get a sense of where risks lie to their business. Led by a fear of these unknowns, they can even become hostile and block initiatives if they feel things are moving too fast. But the truth is, they often are, and with insufficient guardrails in place.*”
**— Robert Kloosterhuis, technologist, cloud native platforms, at ITQ**

“*Well-educated security teams are working closely with platform teams to understand the advantages of a unified platform experience that can significantly bolster their security posture. We have representatives from security incorporated into our teams, so there is not a separate or siloed security function. This makes it easy to incorporate security policy and knowledge into our platform strategy.”
*

**— Jaroslaw Gajewski**
## Platform Engineering Is Not a Panacea
Platform engineers are expected to build and deliver an application platform that helps disparate application development teams build, test, deploy, run and continuously improve their application security. This can prove to be overwhelming for a fledgling platform engineering team. However, just as developers have adopted modern programming practices like agile, feature-driven development (FDD), test-driven development (TDD) and scrum, platform engineers have adopted a new mindset.

One of the most powerful shifts in platform engineering is treating your [platform as a product](https://tanzu.vmware.com/content/white-papers/why-you-should-treat-platform-as-a-product): one that needs constant improvement, fine tuning and upgrading to stay secure and competitive. Treating your platform as a product is not a magical elixir, but it can help you deliver the best customer experience (in this case, developer experience) possible, so they can build and deliver software quickly and safely.

Be sure to read the [State of Cloud Native Application Platforms 2024](https://go-vmware.broadcom.com/2024-State-of-Cloud-Native-App-Platforms) report in full and learn more about the [trends and benefits](https://thenewstack.io/cloud-native-app-platforms-new-research-shows-struggles-and-hope/) of adopting a cloud native approach to application delivery.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)