# Internal Developer Portals: 3 Real World Examples
![Featued image for: Internal Developer Portals: 3 Real World Examples](https://cdn.thenewstack.io/media/2024/08/bde5995d-internal-developer-portal-stories.jpg)
Regardless of their industry, background, technology stack and team composition, organizations are all trying to solve the same problems with platform engineering and [internal developer portals](https://www.getport.io/blog/what-is-an-internal-developer-portal).

At a [Portal Talks 2024](https://www.portaltalks.io/) session hosted by [Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/), leaders from three organizations answered some of the key questions about how internal developer portals are used in real life:

[Tiffany Grafton](https://www.linkedin.com/in/tiffanygrafton/), technical product manager at property and casualty insurer[Great American Insurance Group](https://www.greatamericaninsurancegroup.com/)(GAIG), a company with over 7,000 employees.[Pavel Pikat](https://www.linkedin.com/in/pikat/), technical product owner at[AMCS Group](https://www.amcsgroup.com/), a business management software provider for the waste management, recycling, transportation, manufacturing and utilities industries in more than 80 countries.[Louis Bailleul](https://www.linkedin.com/in/louisbailleul/), chief enterprise architect at[PGS](https://www.pgs.com/)**,**an energy data and intelligence company with nearly 1,000 employees.
You can watch the full [Portal Talks session](https://www.portaltalks.io/) on YouTube.

## Why Choose Platform Engineering?
AMCS Group recognized the need for [platform engineering](https://www.getport.io/glossary/platform-engineering) after following DevOps practices for five or six years. While this drove engineering excellence, the company grew rapidly from 200 to 1,200 employees, and the central [DevOps](https://thenewstack.io/devops/) team had challenges with scaling.

“We were operating with ‘[TicketOps](https://thenewstack.io/internal-developer-portals-can-do-more-than-you-think/),’ where we’d have requests raised by different business units or teams, such as requests for building a pipeline or standing up a service in the cloud,” Pikat said. “As we grew, this became a backlog, where we couldn’t satisfy the demand on time. We were effectively a bottleneck for the organization.”

After looking at industry trends, Pikat realized that AMCS needed platform engineering to enable scale.

For PGS, [the need for platform engineering](https://www.getport.io/blog/the-benefits-and-pitfalls-of-platform-engineering) came from an entirely different perspective. It too had embraced DevOps when it began its move to [cloud native technologies](https://thenewstack.io/cloud-native/) back in 2018. And it found this empowered both developers and software engineers, but in 2020 the company had to downsize due to the pandemic.

“The [IT] organization was left with a huge number of systems and services [and] a much smaller workforce to actually maintain them,” said Bailleul.

“This was compounded by the transition to the cloud, and so it was necessary for us to find a better way to distribute the workload in order to have more hands on the actual machinery. And this is where we ended up with the platform engineering concept, making sure we can provide a product that can be consumed by the rest of the organization in order to build and maintain IT services,” he added.

## Why an Internal Developer Portal?
Ultimately, [platform engineering](https://thenewstack.io/platform-engineering/) is about ensuring the software development process is as efficient and effective as possible and that the developer experience is great. This is why GAIG decided to [build an internal developer portal](https://thenewstack.io/demo-building-an-internal-developer-portal-with-port/).

“We wanted to empower the developer and move the needle ultimately on our company’s profitability,” said Grafton.

Bailleul explained that PGS’s first platform engineering implementation was for [Kubernetes](https://roadmap.sh/kubernetes), but the resulting complexity led the company to seek an internal developer portal.

“It was based on a GitOps approach, where we had a bunch of repositories that people needed to manipulate in order to do whatever they wanted. That was great and worked fantastically well, but the cognitive load in order to use this was insane. And for those who just wanted to get a namespace and deploy their application, it was just too much,” he said.

“We realized we needed that hidden away, but building a UI or a new product to abstract this — that’s not our job; it’s for us to consume. So this is why we searched for a solution that solved that problem,” Bailleul added.

Pikat, of AMCS, said they had some success in using regular pipelines in the version control system to run self-service tooling, albeit for simple scenarios. The need for a portal was clear as the platform team wanted to establish more difficult self-service actions and build an enterprise software catalog, while other stakeholders in other business units wanted to be able to view security and compliance metrics. All of these items were possible via an internal developer portal. AMCS’s initial research focused on [Backstage](https://www.getport.io/glossary/spotify-backstage).

“Most platform engineering teams will look at Backstage initially, but the first thing that comes to mind is complexity because you have to deal with it yourself, and we have a very small team. So after trying to run it locally, it was clear we didn’t have the resources to explore it, so we explored SaaS [Software as a Service] alternatives instead,” Pikat said.

## Using a Portal as a Product
When GAIG decided to build a portal, they took on the [portal-as-a-product](https://www.getport.io/blog/platform-as-a-product-portal-as-a-product-why-you-should-use-both) approach, effectively treating the developers as customers.

“We factored in our high-level goals, our scoping and what we were aiming to go after first. [We were] really homing in on what we can understand about our developers’ needs and gathering all the feedback we can, [both] upfront and along the way,” said Grafton.

This meant conducting sessions with around 20 team members, several IT executive sponsors and various stakeholders to ensure [developers’ needs were being met](https://thenewstack.io/what-devs-really-want-in-an-internal-developer-portal/) and that the project aligned with the business’s goals.

Pikat has taken the same approach at AMCS.

“We’re building a product for our internal people. And you’re naturally going to think of it like a product by building it like any other product development team builds products, with a scrum team, a product owner and scrum master, and with sprints. You get feedback and work on the low-hanging fruit that people have or requests that come in. And then you release what they need, which increases value incrementally,” he said.

GAIG also carried out a [team topologies](https://www.getport.io/glossary/team-topologies) exercise to map the organization and understand the way developer teams were working. This included the UX team running prototype persona workshops so that those creating the portal could establish developers’ UX needs.

## Focusing on Developer Pain Points and Golden Paths
For GAIG’s initial portal launch, the focus has been on discoverability and search in a software catalog. The goal is to provide developers with a single pane of glass to understand all their services and resources. This was because they found during their scoping sessions that developers had issues with visibility into available services, so there was an over-reliance on using other developers to find the right information or difficulty piecing together documentation from multiple tools.

“We knew we would have a strong starting point if we could start solving those needs first,” said Grafton. And initial observations show some early signs of benefits for GAIG.

“Within a small initial control group, we observed a reduction in the time spent identifying who supports a particular service from 30 minutes to two minutes for a few of our developers,” said Grafton. The team hopes they can reduce developers’ time spent on numerous other tasks going forward.

While the portal-as-a-product approach tends to yield the best results for gaining trust and adoption of the portal, there are some pain points that may be more obvious to the team building the portal. For instance, the PGS team noticed that developers didn’t have a way to understand best practices on how to do things, despite having a lot of documentation and tutorials.

“We had a lot of services that were built kind of the same way, but not in the same way, and that caused a lot of frustration. So teams that were working on different products or services had issues with compatibility or consistencies,” said Bailleul.

The team decided that as part of embracing platform engineering, it needed [golden paths](https://thenewstack.io/using-an-internal-developer-portal-for-golden-paths/).

“It’s the preferred way to do something, an easy way to achieve what you want, and you lower the barrier to entry to achieve your goal by making it your preferred way. This has been one of the core foundations of how we put the vision forward for all platforms,” he said.

Introducing an internal developer portal has enabled PGS to use golden paths, and Bailleul believes the company is already reaping the rewards.

“When we started to have good golden paths and a number of good self-service actions, it became a force multiplier. We’ve seen people who weren’t willing to go through the TicketOps or take care of creating something new that were enabled and capable of doing it. That has been great for us as an organization to increase our efficiency and deliver more,” he said.

This realization of golden paths with self-service actions has been revolutionary for AMCS Group, too.

“The development team has a lot of complexity to deal with, so [by] telling them to go and do tasks like creating good repositories or giving them access to do cloud resources to do troubleshooting without any golden path, you’re leaving it to them to [choose] a course in their own time and still have to deliver all of those things,” Pikat said.

This is why Pikat wanted to enable self-service in a way that accounted for governance and abstracting away complexity. To do so, they implemented simple self-service forms that developers have to fill in to gain access or take an action, which provides autonomy with golden paths and guardrails baked in.

“Not only can we enable people to get the things they want in an intuitive way and reduce that 85-minute task involving multiple people to [doing] it yourself in five minutes, but we can sleep at night knowing that they will follow our golden path that we designed for them. We’re not going to break any rules; we’re not going to create a Git repo in the wrong project in our version control system; they won’t forget to put branch policies that we require, etc.” he said.

## Gathering Feedback and Iterating
The team at GAIG is continuing to collect feedback as they roll out the portal to more teams. The soft launch involved a smaller team of about 50 app developers to get initial feedback, and GAIG incorporated changes into the portal before launching it again to a broader group of around 300 developers.

For AMCS, the feedback for its internal developer portal has been hugely positive.

“The first and most frequent feedback we’re hearing from our stakeholders, which are not necessarily just developers but [also] support, professional services and the entire engineering community, is how freaking fast they get the task and job done. And they just love it because it enables them immediately,” said Pikat.

“It makes us proud of our work too, because it’s such a nice feeling to help your colleague be productive, to be a driving force for the team and to help the business,” he added.

At PGS, many of the developers onboarded with the first iteration of their portal had experienced the pain of manual GitOps processes.

“They went into the portal and were blown away by how simple it became,” said Bailleul.

Meanwhile, the second wave of developers who used the portal had no complaints, and this, Bailleul explained, was significant in itself.

“You know it’s effective and you’ve done a good job when your team uses the new service and you don’t get any bad feedback,” he said.

The company compared meantime to resolution (MTTR) between tickets and self-service actions, and Bailleul said that the difference was “pretty impressive.”

Now the developers and other stakeholders using the portal at all three organizations are asking what else is possible with it. They’re also coming up with suggestions for new ideas or features to make the portal even more impactful for the organization.

Port’s [roadmap planner](https://www.getport.io/roadmap-planner) provides inspiration for organizations under the “Looking for Ideas” section. Organizations can also suggest features and vote for other feature requests on Port’s [roadmap board](https://www.getport.io/roadmap). If you want to test an internal developer portal, try our [live demo](https://demo.getport.io/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)