# Is Your Internal Developer Platform Missing Orchestration?
![Featued image for: Is Your Internal Developer Platform Missing Orchestration?](https://cdn.thenewstack.io/media/2024/12/208b7e37-daniel-bryant-kubernetes-day-uk-1024x576.png)
[Platform engineering](https://thenewstack.io/platform-engineering/) caught on in the last few years as an answer to the [shortcomings of DevOps.](https://thenewstack.io/platform-engineering-wont-kill-the-devops-star/) Technical sprawl and cloud native complexity have left developers overburdened with cognitive load and Ops engineers frustrated with too many repetitive tasks.
An[ internal developer platform (IDP](https://thenewstack.io/internal-developer-portal-what-it-is-and-why-you-need-one/)) behaves like scaffolding on a building. It’s a supporting structure placed at different levels for different needs, and while anyone can see what’s going on below, it helps keep builders — of construction or of software — focused on the work at hand.

Platform engineering fills in a tech stack gap between app development and operational infrastructure management. This “missing middle,” as [Daniel Bryant](https://thenewstack.io/author/daniel-bryant/), head of product marketing at[ Syntasso](https://www.syntasso.io/), calls it, is needed to manage the platform life cycle.

More organizations than ever are taking on platform engineering projects. But some teams report mixed results — and some indications point to the hype wave breaking.

By 2026, Gartner analysts predict that [80% of organizations will have platform engineering programs ](https://thenewstack.io/platform-engineering-is-for-everyone/)— but the firm also reported that platform engineering has fallen from its height of hype into the “trough of disillusionment.”

“We start to learn stuff because when we hit the ‘trough of disillusionment,’” Bryant said in a presentation at[ Kubernetes Community Days UK](https://community.cncf.io/events/details/cncf-kcd-uk-presents-kubernetes-community-days-uk-london-2024/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) in London in October. “You do start to hear the horror stories and battle stories — I’ve been through it with DevOps. I’ve been through it with microservices. We learn a lot when we go down.

“But, if you’re building platforms, it’s going to be a bit rough” getting to Day Two success, he added.

We’re seeing this already with the recent results of the[ 2024 Accelerate State of DevOps](https://dora.dev/research/2024/dora-report/), also known as the[ DORA report](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/). While individuals and teams felt more productive and organizational software delivery and operations performance increased, throughput decreased by 8%, and change stability decreased by 14% — all due to the adoption of an [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/).

Is there a better way to build an IDP? Bryant talked about the potential of a platform orchestrator — made of existing tooling instead of building your own Platform as a Service — to enable developers to build faster, more efficiently and more safely.

## How Do You Build a Platform?
Over his last 20 years in technology, Bryant has uncovered three different patterns that go into building a platform, each with a different aim:

- Top-down platform: Focused on the application developer, usually delivered in the form of an internal developer portal, most commonly built with
[Backstage](https://thenewstack.io/spotifys-backstage-a-strategic-guide/). - Middle-out platform: Focused on platform engineering, including everything-as-a-service, process automation, managing things at scale and
[Platform as a Product](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/). - Bottom-up platform: Focused on operations or infrastructure, like Terraform,
[Kubernetes](https://roadmap.sh/kubernetes),[Apache Mesos](https://thenewstack.io/apache-mesos-narrowly-avoids-a-move-to-the-attic-for-now/)or[Crossplane](https://thenewstack.io/kubecon-24-crossplane-a-developer-friendly-control-plane/), and the DevOps principle of “You build it, you run it.”
### The Top-Down or Backstage Approach
The top-down way concentrates on the application developer experience. These are the golden paths laid down by the engineers at Spotify, when they created the[ Backstage open source framework](https://github.com/backstage/backstage) for building internal developer portals.

“Backstage is everywhere. It’s got the zeitgeist, right? Fantastic to get started,” Bryant said. But it “can be more of a challenge on the Day Two experience.”

One aim of a modern-day[ platform engineering strategy](https://thenewstack.io/platform-engineering-a-workshop-to-help-map-your-strategy/) should be to [reduce developer cognitive load](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/) — don’t make devs learn something new. The risk for the top-down platform approach is often having to learn [TypeScript](https://thenewstack.io/typescript/) in order to use the open source version of Backstage.

Bryant analogized this method to getting a puppy for Christmas — it seems great at first, but then you have to look after and clean up after it.

The challenge, he said, is that portals like Backstage are often just a “thin facade” that calls a series of infrastructure APIs. This is great for bootstrapping but makes it really hard for upgrades and maintenance, which is why there are Backstage as a Service companies and in-house Backstage teams popping up.

“It has a fantastic developer experience if you’ve got nothing before — you’ve got microservices, you’ve got things everywhere, [and] you don’t know what you got in your estate,” Bryant said. “Backstage and other portals are highly customizable. But one of those anti-patterns that we do see is everyone saying, ‘I can write a plugin for that,’ and then they realize it’s Typescript and they’re not so keen.”

Backstage features a great service catalog and[ technical documentation](https://thenewstack.io/documentation-is-more-than-your-thinnest-viable-platform/), he said, but doesn’t cover the full array of platform needs. With a different platform approach, a portal can serve as what Bryant calls “application choreography,” which focuses just on providing a helpful, searchable interface in the software development life cycle.

### The Bottom-Up or Ops Approach
[Infrastructure as Code](https://thenewstack.io/infrastructure-as-code/) is the way to build a platform that’s bottom-up and operations-focused.
“This is where Terraform or Crossplane is my platform,” Bryant said. “I can orchestrate all my infrastructure by HashiCorp config language, cron jobs, [GitOps](https://thenewstack.io/4-core-principles-of-gitops/) pipelines. It’s highly automatable, which is great for that going fast experience.”

However, this becomes harder and harder with tech sprawl, which makes it increasingly difficult to automate and orchestrate. This can create a two-speed organization of fast-moving platform customers while non-customers are stuck on the legacy software.

Plus, infrastructure abstractions are never perfect, Bryant said, and they leak out to developers, who are left having to know at least something about Kubernetes and other operational complexities that add to cognitive load.

“Not every engineer wants to do that,” Bryant said. “Some just want: Here’s my application. Make it run.”

### The Middle-Out or Orchestrator Approach
Finally Bryant made the case for the middle-out platform strategy that combines tools and processes at a higher level of abstraction.

In this emerging, three-layer stack, first you have app development, where the coding, shipping and running happens.

In between sits the platform orchestration layer, where, Bryant said, platform, developer experience and site reliability engineers focus on design, enablement and optimization. Those working on this — until recently missing — middle piece, concentrate on the internal developer platform life cycle and the platform API.

Then, everything sits on the infrastructure orchestration and composition layer, where the DevOps and platform engineers plan, build and maintain.

“Once you understand the three layers, you can think about the domain boundaries,” Bryant said. “You can think about the APIs. You can think about coupling and cohesion,” allowing technical leadership to decide trade-offs. “This is the way we build out scalable platforms, for that speed, that safety and that efficiency.”

He gave examples of products serving this middle orchestration layer:

[Crossplane Compositions](https://www.crossplane.io/).[Cloud Native Operational Excellence (CNOE)](https://cnoe.io/), an[open source framework](https://thenewstack.io/building-an-idp-with-help-from-the-open-source-cnoe-framework/)for building an internal developer platform.[Humanitec](https://humanitec.com/?utm_content=inline+mention)Resource Definition.[Kratix Promises](https://www.kratix.io/), by Syntasso.[Argo Custom Resource Definition](https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/).[Flux Custom Resource Definition](https://fluxcd.io/flux/flux-e2e/).
## Delivering Platform Developer Experience
Platform engineer success comes down to really thinking about your internal user experience (UX) — developer experience or DevEx.

“You’re now building a product, and therefore, the UX is critical,” Bryant said.

He cited[ Seve Kim](https://www.linkedin.com/in/sevedkim/), product manager at [Spotify](https://thenewstack.io/how-spotify-achieved-a-voluntary-99-internal-platform-adoption-rate/) for Backstage, in what this approach should include: applying basic software design principles — API-first, domain boundaries and object-oriented design — to the platform.

In this strategy, you hide information so each layer is clear on what it is supposed to do. Then, following the concept of progressive disclosure, Bryant said — which is “all about making systems easy to get started but making the hard stuff possible” — as your internal customers become more comfortable with the platform or need to accomplish more difficult things, you can disclose other features as needed.

This way, you aren’t scaring your developer customers up front — because with platform engineering, your platform remains optional to use.

Each developer user base will be slightly different, but Bryant argued that a platform team should focus on serving three pieces:

- User interface.
- Command-line interface.
- API.
Then, work to optimize for automation.

“Business requirements change, user expectations expand and APIs are the core of the platform,” he said, offering specific APIs that can enable what he said is the right level of abstraction:

- Open Application Model:
[OAM](https://oam.dev/),[Score](https://score.dev/). [Kratix Promise Workflows](https://docs.kratix.io/main/reference/promises/workflows).[KubeBuilder](https://book.kubebuilder.io/).- Crossplane.
[Massdriver](https://www.massdriver.cloud/).- Terraform.
“None of these are bad or good. It’s all about trade-offs,” Bryant said, calling OAM and Score more developer-focused, while Massdriver is more implementation-focused.

## Finding the Right Platform Tech Stack
The next step in your platform engineering strategy is to choose the technical stack, usually made up of various best-of-breed tools.

Bryant highlighted some common platform automation stacks, from more to less opinionated:

- BACK stack: Backstage, Argo, Crossplane, Kyverno.
- CNOE framework.
[Kubefirst](https://github.com/konstructio/kubefirst).- Build your own with other Cloud Native Computing Foundation technology.
Whatever you choose, he says, make sure you have clear boundaries around this middle layer. Then, the platform API will define how your developers interact with the platform components, services and workflow across your platform life cycle.

## Adopt a Platform as a Product Mindset
“The real magic happens when you treat your[ platform like a product](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/),” Bryant said in his presentation. “You are actually building for user needs, really understanding what folks are wanting and meeting those needs,” Bryant said.

User input is essential to build your platform successfully. “If you’re building a platform to increase speed, reduce defects, scale-out, then you’ve got to have a much clearer idea of what you’re actually building,” he said, and communicate it quickly to get feedback from your internal developer customers.

Then, as with all product management, it’s key to establish goals and[ DevEx measurements](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/). This includes leading indicators, like:

- Adoption rates.
- Onboarding times.
- Time to nth pull requests.
As well as lagging indicators, like:

- App retention rate.
- Incidents and near misses mitigated.
- Return on investment, usually measured as time saved.
Any form of [platform engineering metrics](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/) needs to mix quantitative quick wins with long-term business goals and qualitative developer experience.

## Bonus Reading Recommendations
In order to understand and achieve the organizational dynamics necessary for platform engineering success, Bryant recommended two[ must-reads](https://www.syntasso.io/post/top-five-platform-engineering-books-for-2024):

- “
[Enabling Microservice Success](https://www.oreilly.com/library/view/enabling-microservice-success/9781098130787/)” by[Sarah Wells](https://thenewstack.io/setting-microservices-up-for-success-real-world-advice/). - “
[Team Topologies](https://thenewstack.io/how-team-topologies-supports-platform-engineering/)” by[Matthew Skelton](https://thenewstack.io/setting-microservices-up-for-success-real-world-advice/)and[Manuel Pais](https://www.linkedin.com/in/manuelpais).
We would also like to add our own free ebook: “[Platform Engineering: What You Need to Know Now](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/).”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)