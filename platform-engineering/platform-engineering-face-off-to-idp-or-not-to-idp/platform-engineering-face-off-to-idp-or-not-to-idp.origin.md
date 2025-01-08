# Platform Engineering Face-Off: To IDP or Not To IDP?
![Featued image for: Platform Engineering Face-Off: To IDP or Not To IDP?](https://cdn.thenewstack.io/media/2025/01/2a3e64d9-platform-engineering-faceoff-1024x576.jpg)
Platform engineering has become one of the most talked-about topics in modern tech conversations, often touted as the future of developer experience (DevEx) — and some might claim the death of DevOps. ([DevOps is dead! Long live platform engineering!](https://thenewstack.io/devops-is-dead-embrace-platform-engineering))

But what does platform engineering really mean, and how does the concept of an [internal developer platform (IDP)](https://thenewstack.io/platform-engineering/) fit into it? Opinions vary widely, with some advocating for IDPs as the cornerstone of platform engineering, while others caution against the hype, pointing out the risks of oversimplification.

**What It Takes To Develop an Internal Developer Platform**
Before we start debating whether to adopt an IDP, let’s align on the terminology first. IDPs are designed to centralize and streamline how engineering teams interact with infrastructure, tools and processes.

They provide a single interface — often combining automation, self-service capabilities and documentation — to simplify workflows and reduce cognitive load for developers. Commercial solutions like [Port](https://www.getport.io/?utm_content=inline+mention) and [Humanitec](https://humanitec.com/?utm_content=inline+mention) offer ready-made platforms with robust support and integrations, while open source options such as [Backstage](https://thenewstack.io/spotifys-backstage-a-strategic-guide/) allow teams to customize and build their portals. However, adopting, implementing and maintaining an IDP requires significant investment in time, expertise and alignment across teams.

This process often involves:

**Extensive planning**: Teams must carefully assess their current workflows, developer pain points and infrastructure needs to design a platform that fits their unique requirements.**Cross-team collaboration**: An IDP impacts multiple stakeholders — from developers and operations teams to product managers — requiring consensus and ongoing coordination to ensure successful implementation.**Custom development and integration**: While commercial solutions may offer plug-and-play functionality, tailoring an IDP to fit specific organizational needs often demands significant customization, integration with existing tools and extensive testing.**Ongoing maintenance**: An IDP is not a “set it and forget it” solution. It requires regular updates, monitoring and adjustments to keep up with evolving technology stacks, team needs and business objectives.**Cultural adoption**: Beyond technical implementation, an IDP’s success depends on fostering a culture of adoption and engagement, ensuring that teams understand its benefits and incorporate it into their daily workflows.
Organizations must carefully balance the trade-offs between initial setup, long-term maintenance and potential benefits to ensure the platform truly meets their unique needs.

With all that in mind, it’s understandable why there are strong opinions on both sides as to why you should or shouldn’t adopt an IDP. So we will make opposing cases, describing why you should or shouldn’t consider one for your organization.

## Internal Developer Platforms: Pros and Cons
Let’s dive into the debate, exploring both sides — the reasons why an IDP might just be the solution your team needs, and the arguments against relying on one.

**Eran: Say Yes to IDP **
Proponents of IDPs argue they are not just tools but a framework for transforming how developers interact with infrastructure and processes. Here’s why IDPs might be the right choice:

**Streamlined self-service**: IDPs empower developers to access and provision resources independently, reducing bottlenecks and allowing teams to focus on building, not waiting.**Consistency and standardization**: By centralizing documentation, workflows and templates, IDPs promote best practices and reduce errors, making it easier for teams to collaborate and onboard new members.**Better developer experience**: The core promise of platform engineering is to improve DevEx. An effective IDP provides developers with a single pane of glass, simplifying their workflows and removing friction points.**Scalability**: As organizations grow, managing infrastructure and processes becomes exponentially more complex. IDPs offer a scalable solution to maintain order and efficiency, ensuring that platform teams don’t become overwhelmed.
**Ido: IDPs Are No Silver Bullet**
Critics of IDPs often draw parallels to how [Kubernetes](https://roadmap.sh/kubernetes) was hailed as the ultimate solution for microservices but quickly became a complex challenge in itself. Similarly, IDPs are often pitched as the “silver bullet” for platform engineering, when in reality, they may mask deeper organizational issues or lead to more problems than they solve. Here’s the devil’s advocate perspective:

**Overfocus on tooling**: Platform engineering is not about a specific tool but about solving the broader challenge of improving the DevEx of DevOps. An IDP can risk reducing this initiative to an implementation detail, overshadowing the bigger picture. In addition, you may not need a new shiny tool for an old trick. For example, popular tools within existing developer toolchains — like Jira,[Harness](https://harness.io/products/continuous-integration?utm_content=inline+mention)and even[Datadog](https://www.datadoghq.com/?utm_content=inline+mention)— have a “compose for IDP” option. Having a “pure play” IDP is just onboarding another tool, and existing tools can do the job.**Vendor lock-in**: Many IDP solutions are tied to specific vendors or ecosystems, making it harder for an organization to pivot as its needs evolve. What starts as a solution for simplicity can turn into a new form of dependency.**False promises of panacea**: The IDP narrative often simplifies the complexity of platform engineering. Deploying a tool like Backstage or Port is not a magic wand that automatically solves all DevEx challenges. Without addressing organizational processes, workflows and culture, the portal becomes a shiny but hollow artifact.**Mismatch with team needs**: Not all organizations or teams need the same level of abstraction or self-service. A IDP that works for one company might be overkill — or completely irrelevant — for another.
**Beyond the Tooling**
Both sides of the debate highlight a critical truth: Platform engineering is about much more than tools. It’s about addressing the systemic challenges that come with modern software development — creating self-service, repeatable infrastructure, and fostering a culture of collaboration and innovation.

You don’t want to adopt an IDP just because it’s trendy or because vendors promise it will solve all your problems. Instead, the goal is to [evaluate your unique challenges](https://thenewstack.io/the-2024-state-of-platform-engineering-fledgling-at-best/), understand what platform engineering can achieve for your organization and choose the [tools](https://thenewstack.io/platform-engineering-it-is-all-about-the-tooling/) — or approaches — that align with your vision.

**Decision Time!**
The IDP face-off is emblematic of a larger discussion in tech: the tension between the allure of new tools and the underlying principles they aim to address. Whether you choose to IDP or not, the key is to stay focused on the purpose: empowering developers, streamlining operations and building resilient, scalable platforms. Tools like IDPs can be powerful enablers — but only when used thoughtfully and in the right context.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)