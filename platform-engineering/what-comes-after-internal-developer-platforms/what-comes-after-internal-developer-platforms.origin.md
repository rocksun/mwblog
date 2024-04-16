# What Comes after Internal Developer Platforms?
![Featued image for: What Comes after Internal Developer Platforms?](https://cdn.thenewstack.io/media/2024/04/bbb38350-pendulum-1024x576.jpg)
Things tend to move in cycles. We’re always swinging between one extreme and another, reacting against — and differentiating ourselves from — what came before. This is true in a broadly historical sense and for development.
You could rewrite the history of development tooling in cycles of centralization and decentralization — the constant battle to balance standardization and autonomy, scalability and velocity. Just when it seems we’ve reached a solution, the pendulum swings the other way.
The rise of platform teams has been well documented, and
[management of internal developer platforms](https://thenewstack.io/platform-engineering/) is increasingly a core function. But as the complexity of these systems scales, and the tax of building and maintaining them sours the benefits of vending them, does it feel to anyone else like the pendulum is about to drop?
## The Rise of the Internal Developer Platform
Before containers, there was
[VMware](https://tanzu.vmware.com/tanzu?utm_content=inline+mention), and we were obsessed with making self-provisioning [platforms for developers](https://thenewstack.io/adopting-gitops-for-self-service-developer-platforms-practical-strategies/) so they could interact with infrastructure in a minimal way. We could just ask for the VM we needed and start developing it right away.
When Infrastructure as Code came about, we broke up these VMs and moved toward microservices. Rather than having this monolithic platform, we decided that a decentralized platform that separated concerns would allow us to scale better. Each team could work within their own city-state. And when things didn’t work, the
[culture of DevOps](https://thenewstack.io/best-practices-for-adopting-a-devops-culture-2/) helped the teams communicate with each other.
But this too started to feel out of hand. Containers kept getting smaller and smaller, and the complexity was greater and greater. And now, due to human nature, we’re doing what we always do: something radically different. Each time we reach some tipping point of complexity, we change gears again. Decentralization isn’t working as we’d hoped; we need a more centralized pattern.
Internal developer platforms mark a return to this centralized view of development. We’re building self-provisioning platforms with the hope that developers don’t have to talk to operations.
But we’re coming up against the same pitfalls — just moving our peas from one side of the plate to the other. The complexity never really goes away.
## The Risks of Internal Developer Platforms
Internal developer platforms should, in principle, reduce the cognitive load for developers by lumping all the operational tools that come with containers into one place. But is this kind of centralization really effective? Serving your developers one central platform comes with big risks.
### Overengineering
The analysts said, “Go
[build a platform](https://www.gartner.com/en/newsroom/press-releases/2023-11-28-gartner-hype-cycle-shows-ai-practices-and-platform-engineering-will-reach-mainstream-adoption-in-software-engineering-in-two-to-five-years).” But the problem with recommendations like this is that they are made with companies like Netflix in mind. Most companies are simply not of the same size and scale that they’d ever have the problems that companies like Netflix have, but they’re tasked with solving them anyway.
### Resource Sinkhole
A brand-new platform team might spend two years and millions of dollars building a new internal product for developers: the
[internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/). But there are no guarantees that, once built, this new product will work for people.
Before you’ve spent all those dollars and hours and sweat and tears, how can you know if the platform is ever going to return value?
### Tooling Silos
Enterprise solutions are complex propositions. Increasingly specialized tooling for each stage of the
[software development life cycle](https://thenewstack.io/security-testing-must-be-part-of-software-development-life-cycle/) has made specific organizational roles easier, but has done little to improve collaboration with other roles using their own specialized tools. Each team ends up in a tooling silo.
The original idea behind DevOps was to address this siloing by adjusting organizational structure and improving communication. The internal developer platform envisioned as a foolproof way for a developer to
[deliver their applications without friction](https://thenewstack.io/imagine-a-smarter-ci-pipeline/), marks a shift away from this communication and collaboration. In 2024’s version of “throwing it over the wall,” the wall is between platform teams and developers, and no one quite knows what’s happening on the other side.
We need tools that promote communication in general, not just communication around tools. Let’s acknowledge that stakeholders utilize different required skills and live in different worlds. Rather than seeking the lowest common denominator between these stakeholders, let’s max out their capabilities by giving them the ability to focus on what they’re good at.
## What Comes Next?
What if, instead of ping-ponging between centralization and decentralization, between tooling silos and The One Tool to Rule Them All, we facilitate conversations between tools? What if we provide each of the subject matter experts that make up a complex solution a common framework for describing, deploying and testing their scope of work?
Such a solution would be a lightweight alternative to the IDP all-or-nothing approach, without a completely decentralized free-for-all.
At
[Garden](https://garden.io/), we’re working to help teams [work in a more modular way](https://thenewstack.io/garden-automates-kubernetes-building-deploying-testing/), giving them the ability to source others’ work in order to test their own work against the bigger picture. We believe that tools that handle complexity, rather than abstracting it away or kicking it to other teams, will come next. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)