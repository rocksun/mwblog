# Building a Platform Team at a 153-Year-Old Company
![Featued image for: Building a Platform Team at a 153-Year-Old Company](https://cdn.thenewstack.io/media/2024/06/7bf6b0ed-building-a-platform-team-at-a-153-year-old-company-2-1024x576.jpg)
Every company is different, therefore each platform must be unique.

We hear this a lot at tech events. Taking a bespoke approach to [platform engineering](https://thenewstack.io/platform-engineering/) has companies investing a ton of time and money into customizing open source software and building their own [internal developer platforms](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) from scratch.

As [Abby Bangser](https://www.linkedin.com/in/abbybangser/), principal engineer at [Syntasso](https://thenewstack.io/platform-engineering-demands-a-product-mindset/), put it, the [focus of a platform engineering team](https://thenewstack.io/how-to-foster-a-good-internal-developer-platform-experience/) should be on shared services that are important — like infrastructure, scaling and security — but that aren’t contributing to what makes your business unique.

Platform teams work to reduce cognitive load and tooling complexity to help application developers deliver value to end users faster. So unless you are a platform tooling company, spending time building your own customized platform means you’re not focusing on your organization’s unique value proposition — or improving your internal developer experience.

The digital transformation of 153-year-old [Hellmann Worldwide Logistics](https://www.hellmann.com/en), as described by[ Mathias Gebbe](https://www.linkedin.com/in/mathias-gebbe/) and [Aljoscha Pörtner](https://www.linkedin.com/in/aljoschap/) at [PlatformCon 2024](https://platformcon.com/talks/logbook-of-a-journey-building-a-platform-team-in-a-150-year-old-logistics-company), is both a unique experience and one that has been shared by many more companies of all sectors and sizes. Their lessons uncover platform engineering patterns other organizations can adapt.

## Beware of the Partial Transformation
Hellmann Worldwide Logistics, a one-man business founded in 1871, has now grown to 40,000 employees globally, operating in 54 countries. While Hellmann’s tech stack isn’t quite so old, it certainly needed an upgrade.

“You saw a lot of AS/400 green screens, [Oracle](https://developer.oracle.com/?utm_content=inline+mention), [VMware](https://tanzu.vmware.com?utm_content=inline+mention), an on-premise data center. The code was written in Java Enterprise [Edition], C# and even Visual Basic,” said Gebbe, team lead of the developer experience and platform team.

The on-premise data center had specialized teams, including one for the network, one for the servers and one for the databases. “And the developer teams were siloed because one was building on [IBM](https://www.ibm.com?utm_content=inline+mention) WebSphere Portal server and another team was building flatlines for the employee and customer portal.”

Each of these teams brought a lot of business context, but, Gebbe said, they completely lacked [cloud native](https://thenewstack.io/cloud-native/) experience.

Despite all this, Hellmann’s engineering culture embraced a digital transformation — and the logistics company started not only putting containers on ships, they started putting them on [Moby](https://thenewstack.io/the-moby-project-post-kubernetes-3-new-releases-in-2023/) in the cloud. Product development teams quickly started embracing a [DevOps](https://thenewstack.io/devops/) mindset — “You build it. You run it.” — with shared resources, blueprints and pathways to operation.

## ‘I Don’t Feel Like a Software Developer’
While Hellman’s engineers were mostly still on-premise with some experiences in the cloud, they were using cloud native technology like [Docker](https://www.docker.com/?utm_content=inline+mention)[ Swarm](https://thenewstack.io/docker-swarm-a-user-friendly-alternative-to-kubernetes/) for orchestration.

“But then things drifted apart,” Gebbe said. “We had teams that were more or less lucky, that had the resources, the knowledge, the time, all that to go in the direction of making use of the cloud infrastructure services platform.”

Those stuck on the data center couldn’t achieve as much.

“We also had other teams that were very occupied by product development, and they stuck to the old platform stack.” Gebbe said. These teams were “still ticket driven, had low-to-no automation, and were a bit limited by, for example, could not use distributed file systems.”

Then the teams drifted apart more. Some teams went for [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) cloud, while others went for [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure cloud. Different teams used different source code management tools.

“A colleague of mine once said that, ‘I don’t feel like a software developer here. I’m a test engineer, a DevOps engineer, a first-level support security expert. I’m not a full-stack developer. I’m a complete IT department’,” Gebbe recalled.

Then, he shared a picture with the PlatformCon audience of the crowded [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention)[ landscape](https://landscape.cncf.io/), from which “each and every product team has to find the right solution for their team.”

This [developer burnout](https://thenewstack.io/how-to-recognize-recover-from-and-prevent-burnout/) and overburden of cognitive load is a common impetus for adopting platform engineering.

Like many companies undertaking a platform engineering project, the pendulum needed to swing away from that initial cloud native developer autonomy and toward centralization. This meant the platform team had to make decisions that not everyone was happy with when they were forced to migrate onto the platform.

“The only ones happy in this scenario were the consultancies that support the different product teams by upgrading the infrastructure and databases,” Gebbe remarked. “We really lost time not developing features for our customers.”

## Don’t Build from Scratch
It was time to try something different, inspired by platform stories coming out of other organizations.

The Hellmann team decided to “start with the why,” Pörtner said, taking over the microphone at PlatformCon to reference leadership guru [Simon Sinek](https://x.com/simonsinek). “We defined the mission statement: We strive to unleash all our developer potential to shape the digital future and growth of human.”

From this, the platform team identified seven pillars to build on:

- Transparency
- Trust
- Automation
- Innovation
- Autonomy
- Developer-first
- Security
Platform engineering is about defining [golden paths](https://thenewstack.io/how-to-pave-golden-paths-that-actually-go-somewhere/) of least resistance to releasing software. With these seven values in mind, the clear pathway was via the cloud, with a base of [Kubernetes configuration management](https://thenewstack.io/the-new-basics-of-configuration-management-in-kubernetes/), source code management and [CI/CD](https://thenewstack.io/ci-cd/).

Citing the common software developer affliction of [Not Invented Here Syndrome](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9310.1982.tb00478.x), Pörtner, a platform engineer, said the team originally thought they should build from scratch themselves.

“We deployed databases on our own in our clusters. And it was not a good idea,” he said. “It was better to build the platform based on what’s already there — and we have a cloud provider for exactly that.”

Indeed, managed cloud services and automation [consistently outperform](https://thenewstack.io/want-to-save-the-world-start-by-cutting-your-cloud-costs/) anything self-managed. By using managed services for deploying databases, the Hellmann platform team was able to move more workloads to the cloud and speed up the integration of features used by multiple teams without taking on the cost of build, deploy and manage.

## Build the Thinnest Viable Platform
While laying down that golden path, a common goal of platform engineering is enabling self-service to avoid friction-filled ticket writing and humans in the loop for repetitive work. But trying to automate too much, too soon may be more trouble than it’s worth.

“We think that self-service is key of course,” Pörtner said, but “it’s better to not over-engineer everything, building more and more features because then your team starts to have problems because it’s more complicated.”

Platform engineering runs the risk of becoming an old-fashioned, top-down behemoth platform if not done incrementally.

[Team Topologies](https://thenewstack.io/how-team-topologies-supports-platform-engineering/), a popular model for modern software organizations, recommends starting with a concept called the[ thinnest viable platform](https://thenewstack.io/documentation-is-more-than-your-thinnest-viable-platform/) (TVP) — the bare minimum you can build that makes your developer customers’ lives easier. This is often a lightweight wiki or some sort of documentation.
This may be released in a minimum viable product format for rapid feedback without long-term investment, but [a TVP differs from a minimum viable product (MVP](https://thenewstack.io/mvp-or-tvp-why-your-internal-developer-platform-needs-both/)) because any internal developer platform is something that you have to then build on and maintain.

“That’s something we learned the hard way to not do,” Pörtner said. “We learned that we should ask for more feedback and show them what we do.”

In platform engineering, your developer colleagues are your customers, which should make it easy for rapid feedback, but that’s not always the case.

“When we asked them, the feedback was ‘Make it work,’ because sometimes they are involved in product development and they don’t have time for your questions or giving feedback, or sometimes they don’t know what the feedback really is,” he said.

Or, sometimes if the platform wasn’t really what they needed, engineers would start building ad hoc workarounds.

The Hellmann platform team had to take charge of the platform’s evolution

## Take the Lead in Customer Care
An internal developer platform distinguishes itself by being optional. That means you’ve got to sell your own colleagues on using it.

Like all good product pursuits, a [platform as a product mindset](https://thenewstack.io/platform-engineering-demands-a-product-mindset/) relies on fast feedback and open communication. At Hellmann, this includes:

- Sprint reviews
- Architectural decision records
- Postmortems
- Product roadmaps and upcoming features
The organization also added a help center where developers can ask questions and file issues.

On top of publishing this information, the platform team then asks its customers for requirements. Again, this can be a struggle because the app teams are busy with product development, which is why the platform team hired a product owner, to prioritize stakeholders’ needs.

The product owner, Pörtner said, is “someone who can talk to the teams, prioritize stuff and find a way through the jungle of all the possibilities you have in building a platform and identifying the pain points.”

Platform teams need to be self-aware that they aren’t just building the shiny-shiny or what they think is best.

“In the end, stuff like dependency automation tooling — [Renovate](https://github.com/renovatebot/renovate), [Dependabot](https://github.com/dependabot) — [observability](https://github.com/dependabot) solutions, and secrets management freed up an unbelievable amount of time for the developers and that was really, really a game changer for us and for the teams,” Pörtner said. “And then they started to appreciate our platform. We had the feeling that we are now going in the right direction.”

But then, the platform team still had the habit of building too many features. The busy product teams didn’t have time to make so many updates, so the platform team got into the habit of implementing changes on their behalf. This doesn’t work at scale.

“You have to build your platform in a way that they can integrate easily,” Pörtner said. “Therefore you need documentation and training. And let’s show them how to use it and give them the possibility to work on their own.”

## Don’t Onboard Every Team at Once
Yes, an internal developer platform is focused on shared tooling and processes, but not everyone’s going to have the same entry point.

Such a large organization will always have disparate knowledge and technical experience. Some of Hellmann was already cloud native, while others were working on-premises.

“I won’t lie to you. It’s hard sometimes and you have to be patient and you have to teach them,” Pörtner said, further warning that “sometimes it gets a little bit lost. A huge part of platform development [is] to document stuff and train your developers to do the right things with your platform.”

Add to this, platform engineering teams are most often a handful of people supporting a wide range of teams.

“Take your time for each and every team to onboard on your platform.” Gebbe added. “Find your path. Probably you are not [Netflix](https://thenewstack.io/developer-productivity-engineering-at-netflix/) or [Spotify](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/), but you need to find your way for your developers to provide a good platform.”

A platform engineering strategy is something that is both unique to your organization and one that needs to be cultivated over time.

As Gebbe put it, “You have to build a really good soil, a good ground, and the flowers and butterflies will come, and they will be happy with your platform.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)