# Platform Engineers Must Have Strong Opinions
![Featued image for: Platform Engineers Must Have Strong Opinions](https://cdn.thenewstack.io/media/2025/03/0c054a1f-platform-engineers-must-have-strong-opinions-1024x576.jpg)
We are living in a golden age of developer experience (DevEx), where developers can choose the tools, frameworks and even editors they prefer. It is easy to have an individual stack for code creation or cloud deployment and assume that it will all work out by the time it gets to production.

However, tool proliferation starts causing more problems than it solves once an organization reaches a tipping point of size and complexity. In response, organizations tend to form platform engineering teams that set guidelines and expectations for deploying infrastructure in a consistent, scalable way.

A platform team must have the mandate and the power to enforce standards for the whole organization, or the developers end up with the worst of both worlds — a lack of autonomy and a high-friction environment for deployment.

This power is not just a negative power to say “that doesn’t meet the guidelines,” but a positive power to create, teach and iterate on practices that serve the whole organization. Asking a platform team to enforce something they think is not helping will not increase your organizational efficiency. Asking developers to adhere to a platform model they don’t understand makes compliance harder for everyone.

## Why Platform Engineering Beats Autonomy
At the dawn of the [DevOps](https://thenewstack.io/devops/) revolution, developers were told, “You build it, you run it.” This meant that developers had the autonomy and responsibility to choose and deploy the infrastructure they wanted for their software. There is no doubt that the widespread adoption of these [DevOps practices](https://blog.heroku.com/twelve-factor-apps) revolutionized the agility, speed and quality of software deployment. That said, even with all of the advantages of [adopting DevOps](https://roadmap.sh/devops) practices, there have been some serious drawbacks.

Giving development teams complete autonomy on infrastructure prevents standardization across applications and teams. Very quickly, the organization’s infrastructure landscape becomes highly fragmented, often leading to increased cloud costs, maintainability issues and security vulnerabilities.

In response to these drawbacks, and the perception that developer time shouldn’t be spent in duplicative effort, organizations began to respecialize into groups that did platform engineering.

[Platform engineering](https://thenewstack.io/platform-engineering/) is a practice to design, build and maintain the underlying platforms and tools development teams use to deploy their applications. Instead of developers choosing from the infinite combinations of infrastructure options, platform engineering teams create standardized, preconfigured environments for developers to choose from. This [increases developer productivity](https://thenewstack.io/developer-productivity-in-2025-more-ai-but-mixed-results/) by reducing decision fatigue and wasted effort. Well-designed development environments lead to fewer issues after deployment.
The platform team’s expertise and experience drives strong opinions about the best tools for the job.

Many platform engineering teams build [internal developer platforms](https://thenewstack.io/internal-developer-portals-should-be-internal-developer-hubs/), which allow development teams to deploy their infrastructure with just a few clicks and reduce the number of issues that slow deployments. Because they are designing the underlying application infrastructure across the organization, the platform engineering team must have a strong understanding of their organization and the application types their developers are creating. This is also an ideal point to inject standards about security, data management, observability and other structures that make it easier to manage and deploy large code bases.

When designing and building these environments, the platform team’s expertise and experience drive strong opinions about the best tools for the job. This combination of organizational knowledge, broad experience and strong opinions enables the platform engineering team to deliver infrastructure that meets the needs of developers and the organization while providing security, performance and easier maintenance.

## How Platform Engineering Is Like Pizza (But Not DevOps)
You may have heard that platform engineering is[ just a rebranding of DevOps](https://thenewstack.io/how-is-platform-engineering-different-from-devops-and-sre/) or site reliability engineering. It’s not, although it’s related. Think of it this way…

Say you arrive at DevOps Pizza Parlor, and the menu is a list of every option you can imagine — and then some — for making a pizza. There’s a long list of ingredients but no guidance on why cinnamon sugar might not go with alfredo sauce. At DevOps Pizza, you can make your own pie any way you like it, with seemingly endless combinations of different sizes, sauces and toppings. Most do-it-yourself pizzas will be fine, and a few of them will be even great. Unfortunately, when given an infinite number of options, mistakes will sometimes be made. “I’ll have a large pizza with the basil pesto base. For toppings, I’ll have pineapple, pickles, jalapeños and anchovies.”

In contrast, the menu at Platform Engineering Pizza Place is a list of predesigned pizzas. The choices are curated by experts, and the chefs in the kitchen ensure that the flavors and toppings are well-suited and will taste wonderful. There is a process for making changes to the standard deployments (“I’d like a large meat-lovers pizza. Please add black olives.”), but the standardized pizza selection provides built-in protection from ill-advised orders. The opinions of the chefs matter. They know how to make a great pie.

Platform engineering teams build internal developer platforms that provide a curated menu of development tools and deployment environments for developers to choose from. This curation provides faster, more reliable and more secure application environments that mitigate the risks of poorly designed application infrastructure.

## Too Many Choices, Too Many Mistakes
To build a successful platform engineering strategy, a platform engineering team must have well-defined opinions about platform deployments. Like pizza chefs building curated pizza lists based on expertise and years of pizza experience, the platform engineering team applies its years of industry experience in deploying software to define software deployments inside the organization.

The platform engineering team’s experience and opinions guide and shape the underlying infrastructure of internal platforms. They put guardrails into deployment standards to ensure that the provided development capabilities meet the needs of engineering organizations and fulfill the larger organization’s security, observability and maintainability needs.

Platform engineering is still a maturing practice. Some organizations and software providers are working to describe their internal or recommended practices for the benefit of others following the same path.

One framework that describes well-architected deployment strategy is the [Twelve Factor App](https://blog.heroku.com/twelve-factor-apps), a methodology designed to improve developer productivity and application maintainability. Recently [open sourced](https://thenewstack.io/heroku-moved-twelve-factor-apps-to-open-source-whats-next/) by Heroku, the Twelve Factor approach outlines Heroku’s opinions on best practices based on its years of experience with customer deployments to help developer teams avoid missteps.

These opinions also shaped [how Heroku designed its modern Kubernetes-based Platform as a Service (PaaS)](https://thenewstack.io/return-to-paas-building-the-platform-of-our-dreams). Heroku’s years of experience deploying services on the web have contributed to its opinions on the most effective ways to deploy applications into the cloud. These opinions may not fully align with your platform engineering team’s, but [using the Twelve Factor approach](https://thenewstack.io/open-source-drives-the-twelve-factor-modernization-project) gives your team a good place to start discussing your organization’s needs and values.

Given the apparent similarity between PaaS platforms and platform engineering teams, a cost-conscious executive might ask “Why can’t I just dissolve my platform engineering team, and have my teams use PaaS instead?”

## Why PaaS Complements, Not Replaces Platform Engineering
PaaS cannot replace a platform engineering team; rather, it is a tool in the platform engineer’s tool belt instead of a one-size-fits-all replacement.

Infrastructure, database, storage and networking deployments are routine but time-consuming tasks for DevOps and platform engineering teams. PaaS services can automate, manage and scale the deployment of common services, giving the platform team additional bandwidth to focus on custom deployments, integrations and applications. PaaS operationalizes years of deployment and infrastructure experience with minimal team involvement.

Creating structure around standardized and optimized deployments leads to integrated environments, faster deployments and better maintainability of applications across an organization. To lighten the load of repetitive tasks, platform engineering teams can use PaaS tools to achieve their overall goal of providing tools for fast deployment of common infrastructure environments.

Heroku’s PaaS helps platform engineering teams simplify and expedite the deployment of well-opinionated infrastructure. Learn more about how Heroku enables you to deliver value to your customers faster by [trying Heroku today](https://signup.heroku.com/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)