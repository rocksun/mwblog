# How To Implement InnerSource With an Internal Developer Portal
![Featued image for: How To Implement InnerSource With an Internal Developer Portal](https://cdn.thenewstack.io/media/2024/08/f53a0533-diving-1024x576.jpg)
Strengthening collaboration and breaking down silos is what InnerSource is all about. The methodology encourages an open source way of thinking toward software development. It’s not a new practice; in fact, the term was first coined back in December 2000 by Tim O’Reilly, founder of O’Reilly Media.

Despite it being a somewhat older term in an industry that loves to move on to the latest buzzwords and trends, it is still very much an [approach that many engineering teams](https://thenewstack.io/monitoring-developer-metrics-team-approach-is-best/) want to incorporate into their organizations. Gartner expects 40% of software engineering organizations to have [InnerSource programs](https://thenewstack.io/github-bloomberg-talk-using-innersource-build-open-source-project-development-behind-company-firewalls/) by 2026. This is because they believe that the approach will improve code reusability, increase standardization and inspire a culture of autonomy and ownership among developers.

Ultimately, the goal of InnerSource is to reduce duplication in development, lack of reuse and the resulting increased costs. However, enterprises tend to struggle with the handoff between overarching strategy and tactical implementation.

While no single tool can ensure that developers will [adopt InnerSource](https://thenewstack.io/adopting-inner-source-culture-within-organizations/), there are approaches that can help to implement InnerSource, including the use of an internal developer portal.

Here are five key ways you can use an [internal developer portal](https://www.getport.io/blog/what-is-an-internal-developer-portal) to help implement and encourage InnerSource within an organization:

## The Importance of a ‘Trusted Committer’
In her book “Understanding the InnerSource Checklist,” Silona Bonewald describes the role of a “trusted committer” as crucial to implementing InnerSource best practices. The trusted committer is a developer — often on a two-week rotation — who mentors other developers and ensures standards are met when people create new pull requests (PRs). Trusted committers lead the effort to reduce silos for their service by:

- Maintaining contribution guidelines
- Reviewing incoming pull requests to ensure they’re in accordance with these guidelines
- Mentoring
[developers who fall outside of the contribution](https://thenewstack.io/building-polyglot-developer-experiences-in-2024/)guidelines - Requesting help from those who commit code to their service.
Portals create a place that makes the work of trusted committers easier, seen, acknowledged and easy to follow.

In the most basic sense, an internal developer portal makes the presence of trusted committers known, just like software ownership can be driven through a portal. Having a portal can ensure “trusted committers” for each service are known and rewarded by:

- Including an automatically updated “trusted committer” schedule.
- Assigning a “trusted committer” tag or property to the developer who is currently serving in this role.
- Gamifying the contribution of each trusted committer by maintaining a dashboard (depicting, for example, the number of PRs merged under their watch or the speed with which they respond to each PR).
Finally, Bonewald notes that serving as a trusted committer takes developers away from writing code, so passively recording their contributions using a portal is an excellent way to provide objective performance metrics in year-end performance conversations.

Bonewald suggests a promotion path to “fellow” for developers who excel as trusted committers, which could be a tag or property depicted proudly on their user profile in a portal.

![Developers may find it helpful to view the current trusted committer for a service they’ve discovered. Trusted committers will also find it helpful to be identified using an automatically updated schedule.](https://cdn.thenewstack.io/media/2024/08/786a11a6-image2.png)
Developers may find it helpful to view the current trusted committer for a service they’ve discovered. Trusted committers will also find it helpful to be identified using an automatically updated schedule.

## Boosting Discoverability
This method and the next are particularly important for organizations that have grown inorganically through acquisitions. Whether acquired companies have become a part of a single legal entity or become subsidiaries, the administrative burden of consolidating into a single source code management tool or adding all developers to all existing source code management tools is an insurmountable task and, without doing this, InnerSource efforts tend to languish in slide decks instead of thriving in the daily work of developers.

An alternative to consolidating tools or organizations is to integrate all existing repositories into a single [catalog](https://www.getport.io/blog/service-catalog-what-is-it-benefits-components) that acts as a foundation for a portal, where developers can discover metadata about all available services without exposing the source code by default. In doing so, developers can understand what a service does, how to contribute to it and who the trusted committer is without ever seeing the source code. This immediately reduces duplication of both [services and APIs](https://thenewstack.io/extending-kubernetes-services-with-multi-cluster-services-api/).

## Being Able To Send Access Requests to the Right Person
Once developers are prepared to contribute to or use the service they’ve discovered using a portal, they can use a self-service action to request access to only the repository in question. By implementing dynamic approvals, this request can be sent to the right person, whether that is the trusted committer, product manager or technical lead.

![Access to a repository can be accomplished with a dropdown and a brief message, then can be routed to the trusted committer (or whoever is best to field these requests).](https://cdn.thenewstack.io/media/2024/08/13988dad-image1.png)
Access to a repository can be accomplished with a dropdown and a brief message, then can be routed to the trusted committer (or whoever is best to field these requests).

## Creating New Services That Are InnerSource-Ready
[Engineering organizations that do not use a portal](https://thenewstack.io/which-features-does-your-platform-engineering-portal-need/) already struggle with streamlining new service creation: Developers must submit individual, co-dependent tickets for a new repository, new pipelines, new project management tools, and others. Adding InnerSource requirements to scaffolding a new service is yet another trigger for developers to switch contexts when they should be — and want to be — writing code.
A welcome alternative to a ticket-driven process is a [self-service action](https://www.getport.io/product/self-service) that allows developers to easily satisfy these requirements from the beginning. Instead of directing them to find, modify, and add the InnerSource documentation requirements (`README.md`
, `CONTRIBUTING.md`
, `GETTINGSTARTED.md`
and `HELPWANTED.md`
), simply ask them to fill out the minimum requirements for these from the beginning in a self-service form. The automation creates the new repository, pipeline and project-management tool, and others can write these files to the new repository, allowing developers to shift their focus to writing the code for the new service nearly immediately.

![Auto-populate the templates in this self-service action to ensure developers provide the right information from the beginning.](https://cdn.thenewstack.io/media/2024/08/53835f57-image4.png)
Auto-populate the templates in this self-service action to ensure developers provide the right information from the beginning.

## Scorecards for Services
The approach above will satisfy InnerSource requirements for new services, but organizations tend to have a vast number of existing services that must be evaluated for compliance with InnerSource standards. Before instructing an InnerSource or DevOps team to create a repository scanner that evaluates all repositories, consider using a custom [scorecard](https://www.getport.io/blog/using-scorecards-for-standards-compliance-a-repeatable-framework-and-examples) in a portal. A scorecard can be used to define, measure and track metrics related to each service or entity in an internal developer portal. In this case, a scorecard can help establish metrics to grade compliance with InnerSource standards, which will help managers or team leads understand the gaps in existing services, then drive time-bound initiatives to fill those gaps.

![Before building a repository scanner to check for InnerSource standards, consider using a scorecard instead.](https://cdn.thenewstack.io/media/2024/08/3d5259fc-image3.png)
Before building a repository scanner to check for InnerSource standards, consider using a scorecard instead.

## Conclusion
By implementing a portal and deliberately configuring it to serve InnerSource purposes, engineering leaders can enjoy the benefits of InnerSource in their organizations. Developers will similarly enjoy the benefits of enhanced discoverability and the ability to easily scaffold a new InnerSource-ready service and quickly find the right person to support their contributions.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)