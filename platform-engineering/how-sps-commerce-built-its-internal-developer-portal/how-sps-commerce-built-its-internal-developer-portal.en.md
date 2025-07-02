Implementing an internal developer portal isn’t just about choosing a tool; it’s about reshaping the way your engineering teams work and truly empowering them by committing to platform engineering best practices. If you’re considering this path for your organization, learn from our experience at [SPS Commerce](https://www.spscommerce.com/). We operate the world’s largest retail network, connecting suppliers and retailers. We facilitate exchanges of documents like purchase orders and invoices across the global supply chain. Over 50,000 customers use our network, and our tech department is 700 strong.

## A Broken Developer Experience

In recent years, we experienced rapid growth as an organization, and quickly accrued over 2,500 active items in our [service catalog](https://thenewstack.io/30-of-engineer-leads-use-a-spreadsheet-as-a-service-catalog/). With new developers and a suite of new tools to manage, our developer productivity engineering team had a new mandate to design better ways of working.

We quickly learned we’d need to better enable and empower our engineers: Our teams were larger and spread out across projects, and closing the gaps between processes put strain on our developers.

A significant issue was [tool sprawl](https://thenewstack.io/developers-unhappy-with-tool-sprawl-lagging-data-long-waits/). With over 20 development tools actively in use and plans to develop or adopt even more, we saw our developers [spend countless hours each week](https://www.port.io/state-of-internal-developer-portals) wrangling a disjointed ecosystem.

To make matters worse, there was no central hub for seeing the complete context of an application. Imagine trying to understand 2,500 services without a way to display them in a single place! This lack of clarity, amplified by our rapid growth, led us to create disparate processes with spotty documentation across diverse tech stacks, which siloed work and isolated knowledge that should have been shared.

## The Search for a Solution

Our first move toward finding a solution was to create an [internal developer platform](https://thenewstack.io/how-to-foster-a-good-internal-developer-platform-experience/), which helped us abstract away some of the complexities our teams faced. But we quickly hit the platform’s limitations. It still took teams nearly two weeks to achieve their first “Hello, world!”

Despite the painful onboarding process, the platform taught us some important lessons about context and how we present it. Even if the details of our software development pipeline were clearly laid out, so many details existed that it was hard to distinguish between relevant and irrelevant data points.

Context needs to be obvious: If developers still have to piece together information from multiple sources, the benefit of the platform is lost. So, we asked ourselves, what context is essential? How can our platform deliver necessary context while offering developers a way to input their own insights?

## Choosing an Internal Developer Portal

We did our research and identified [internal developer portals](https://thenewstack.io/internal-developer-portals-can-do-more-than-you-think/) as a potential solution for providing the two-way context we needed. But the market offered several different options, each with its trade-offs.

We took a hard look at what we learned from our platform initiative as well as what we still needed, then came up with some critical questions:

* **Are we ready for a developer portal?** Have we already taken some steps to centralize some of that context — perhaps with some type of tagging or categorization system? (Luckily, we had a head start on categorizing during our platform initiative.)
* **Who will be on our implementation team?** Are they frontend or backend focused? What languages do they prefer? How many dedicated developers can be on this project, and for how long?
* **How custom is our toolchain?** Is it so customized that it won’t fit a rigid data model, or are we using standard tools like AWS and Azure pipelines, which most portals support out of the box? (Our toolchain proved to be standard.)

Based on our research, we found some portals offered more rigid data models, which appealed to our executive team because setup would be quick. But these portals were not able to adapt to all of our needs because of their rigidity — and that had the potential to hinder our long-term adoption and perhaps our ability to develop usable solutions for our team.

On the other end of the spectrum, we saw “unopinionated” developer portals that were completely customizable, but required a much more significant initial investment to set up than we could spend, as well as increased long-term maintenance, costs and risks.

We knew that if we wanted to improve the quality of our developer experience, we needed to find a portal that could offer us some opinions to start with, like best practices, while staying flexible in the long term as our needs changed.

We did a thorough evaluation of everything on the market, [from open source portal options all the way to rigid portals](https://www.port.io/blog/top-backstage-alternatives). Ultimately, we chose Port for the following reasons:

* The flexibility of the data model and data ingestion
* The built-in interface designer, which offered an intuitive UI that made uploading and modeling data a breeze
* The option to continue designing the portal using Infrastructure as Code, which let us adopt a routine release schedule across multiple environments

## What a Portal Could Do for Us

One of the things we were most excited to figure out was how to structure our teams and develop an ownership model for our developer portal.

We embraced empathy-driven development — building the [portal with engineers who understand the day-to-day needs](https://thenewstack.io/which-features-does-your-platform-engineering-portal-need/) of delivery teams. We adjusted our reporting lines to a matrix structure where teams report into different VP-level verticals but collaborate regularly.

[![](https://cdn.thenewstack.io/media/2025/06/1e6f7964-sps_commerce_blog-2-1024x616.png)](https://cdn.thenewstack.io/media/2025/06/1e6f7964-sps_commerce_blog-2-1024x616.png)

This approach provided big benefits. Following a [Team Topologies](https://teamtopologies.com/) framework, our delivery teams now act as stream-aligned teams, supported by platform teams like SRE, Platform and Cloud. Our developer productivity engineering team then serves as an enabling team, building empathy and insight into delivery needs.

We also clarified the team’s approach and goals: not to eliminate tool sprawl, but to manage it by connecting tools and context. Rather than replicating every UI, such as Kubernetes dashboards, we focused on deep-linking to them, with the right context built into the URLs.

Another big win we achieved early was improving our builder experience with Infrastructure as Code (IaC). This has helped our developer productivity team prototype data models, mappings and actions quickly, allowing us to iterate fast and gather feedback in real time.

Once we were happy with a configuration, we codified it using IaC. This approach balanced speed and usability with control and consistency across experiences.

## How We Made Our Portal Essential

Looking back, one of the most valuable decisions we made in building our developer portal was prioritizing the integration of our owned data sources into the portal first. This was important not only because they were foundational to our software delivery life cycle (SDLC), but because our ops teams had already invested significant time into defining ownership and relationships among the resources.

We were able to borrow the context from what we’d already built and construct the portal’s primary use cases around it, using the shared ownership and security model we had already implemented. This familiarity and sense of continuity across approaches helped many embrace the portal with the consistency and accuracy that can often be left out of an organization’s software catalog.

### Encouraging Adoption

We also needed to consider how to ensure our developer teams would adopt the portal. We felt that building a suite of high-quality self-service actions would be a great way to build on our foundational data sources.

We also wanted to make it easy to collaborate across teams, while giving developers fast, easy access to setup actions. The portal served as the technical foundation for our reusable action-creation framework, and provided the business logic for each action.

To build our self-service actions, we used:

* Azure Pipelines for CI/CD, deployment and running actions.
* Docker to package action logic in a portable, host-agnostic container.
* [Pulumi](https://www.port.io/blog/using-pulumi-with-an-internal-developer-portal) for Infrastructure as Code, with plug-ins for Port and Azure Pipelines.
* TypeScript and Python to write business logic, depending on team preference. This was the common functionality we needed for all actions, including getting and sending data to Port as well as error handling and logging.
* [Cookiecutter](https://www.port.io/glossary/cookiecutter) to generate action scaffolding and create pull requests automatically.

To tie it all up, we created a suite of documentation, including “how-to” guides and videos and “getting started” pages, as well as a Slack support channel to help those developing the portal.

Now, it only requires about five files to build, deploy and run an action in the portal. The first four configure the action for deployment and runtime; the last contains the logic. Then, we took it one step further: The first action we created in our developer portal was an action that would scaffold an action. This helped us encourage other teams to contribute, without placing all the burden on our small developer productivity engineering team.

### Building Scalable Data Models

We also put a lot of thought into data modeling. From the start, we wanted models that were scalable and maintainable. GitHub was our first data source, and since we treat Dependabot and Code Scanning alerts similarly, we created a unified vulnerability model. This made it easier to view and filter all vulnerabilities in one place and reduced duplication. Some properties, like severity, didn’t map perfectly — for example, Dependabot alerts lack a “severity” field — but we handled this with filters when needed.

For repositories, we built a generic code repo model with a “type” field to support platforms beyond GitHub, knowing we may one day acquire companies using tools like GitLab. This allowed us to integrate new sources by simply adding an integration and mapping, without defining a new model.

While this approach aligned with our goal of unifying related data, it raised questions in areas like pipelines, where GitHub Actions fit well into our pipeline models but conflicted with the concept of a pipeline project. We’re still figuring out the best solution.

Using generic models required more up-front thinking, but it helped us stay true to the developer portal’s purpose: bringing information together, not keeping it separate.

## A More Connected SDLC

Our internal developer portal, powered by Port, has delivered several tangible results for us:

* **We finally have real-time visibility into platform migrations.**  
  One of our biggest wins has been giving teams a live view into major initiatives, like our CI/CD agent migration. Before, we’d hand out Jira tickets with static lists of services to update, and teams had no easy way to track progress. Now, every team can see, directly in the developer portal, exactly which services they still need to migrate. We still have the Jira tickets, but they just link to the portal dashboard. And at the platform engineering level, we have our own dashboards to monitor the overall progress.
* **It’s made Kubernetes and Helm chart upgrades easier to manage.**  
  We’ve used the same approach for Helm chart upgrades. We need teams to stay current so we can move fast with Kubernetes versions, and the portal lets us surface which services are still tied to older charts that block upgrades. It’s made it much easier for teams to self-serve and stay up to date.
* **We’ve been able to consolidate our API catalog and add visibility.**  
  Port gave us enough flexibility that we could start consolidating our API design-first tooling. We’re pulling in OpenAPI and AsyncAPI specs, aligning them with the service catalog, and adding compliance and governance data on top. Now we have a centralized API catalog that also shows things like linting status, errors and warnings across environments, all in one place.
* **We’ve opened up feature flag data to more people.**  
  Before, only a few people had access to feature decision provider data. Now we’ve imported that data into the portal so anyone who needs visibility — like managers, ops or on-call — can see it. They don’t need extra licenses or special access anymore. And we’ve been able to create views to show which flags are active, inactive or stale over time, which has really helped teams clean things up.
* **AI agents are aware of SDLC data.**  
  Using the portal to support AI agents gives us a unified and structured data model to provide them the context they need as well, and grant access to the agent via self-service action integrations. Now teams can ask direct questions in Slack, like, “When did service abc go to production last?”

Building a developer portal isn’t something you’re ever truly “done” with. It’s an ongoing process of iteration, listening and adapting. But so far, it’s already made a meaningful impact in the way our teams work, and we’re excited to keep finding ways to make the developer experience at SPS better, more connected and easier to navigate.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/06/a201a188-cropped-4881b260-travis-profile-2025-scaled-1-600x600.jpeg)

Travis Gosselin is a Distinguished Software Engineer at SPS Commerce. With a passion for technology and a talent for simplifying complex architectures, Travis focuses on creating seamless developer experiences and fostering high-performing teams. A seasoned speaker, architect and blogger, he...

Read more from Travis Gosselin](https://thenewstack.io/author/travis-gosselin/)

[![](https://cdn.thenewstack.io/media/2025/06/fd7fc4d2-cropped-74433789-mark_debeer_headshot.jpg)

Mark DeBeer is a lead software engineer specializing in developer productivity engineering at SPS Commerce. He's passionate about building tools and solutions that help developers work more efficiently. With over a decade of experience in both frontend and mid-tier development,...

Read more from Mark DeBeer](https://thenewstack.io/author/mark-debeer/)