# How to Solve Backstage Plugin Isolation Problems With ETL
![Featued image for: How to Solve Backstage Plugin Isolation Problems With ETL](https://cdn.thenewstack.io/media/2024/12/451c988b-plugin-isolation-1024x576.jpg)
Backstage is a popular framework for building an [internal developer portal](https://www.getport.io/blog/what-is-an-internal-developer-portal). Developers often see it as a land of opportunity because they’re able to customize the portal they’re building and tailor it to their organization. Engineers like the idea of building something that they own, and Backstage promises ownership of the software development life cycle (SDLC).

But [Backstage is a huge initiative](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/) to kickstart within an engineering organization, so [there are some complexities](https://www.reddit.com/r/devops/comments/10guddj/backstageio_common_issues_and_pitfalls/) — notably its plugin architecture — that can take some time (perhaps six months or even a year) to become apparent. The out-of-the-box plugins offered by the community only take you so far, meaning you’ll find yourself implementing custom plugins more quickly and frequently than you would have thought.

The problem is, by this point, the engineering team will have invested a significant amount of time in building what they’re looking for. This is the point where it becomes clear that, while the framework is indeed customizable, this plugin complexity creates limitations. Some use cases become impossible to fully benefit from, such as incident management and standards compliance.

This leaves engineers facing a big conundrum: Do they try to fix this plugin data problem because they’ve spent so much time [building this portal](https://thenewstack.io/what-devs-really-want-in-an-internal-developer-portal)? Or do they try to find another solution that doesn’t have the same issues, writing off the time and investment they’ve spent building the portal?

Neither of these options sounds ideal. Before we get to some alternative solutions, let’s get to the heart of the matter.

## What Is Backstage’s Plugin Problem?
The Backstage plugin architecture has been designed so that each plugin stands alone. The advantage of this is that it splits up different sections of the portal, so you can [InnerSource](https://thenewstack.io/how-to-implement-innersource-with-an-internal-developer-portal) building the portal, embrace a large number of plugin builders and split up the responsibilities of those builders.

However, this separation is driven by technology rather than well-defined use cases, which is bad practice. The true value of a portal lies in its ability to serve specific use cases effectively. If the portal is challenging to engineer and set up for these use cases, its potential remains untapped. This approach also goes against the [platform-as-a-product](https://www.getport.io/glossary/platform-as-a-product) mindset that is core to [platform engineering](https://www.getport.io/glossary/platform-engineering) success, where users are treated as customers, and their experience is thereby prioritized and enhanced.

The plugin architecture also resembles splitting up a monolith architecture into different [microservices](https://thenewstack.io/microservices/).

But just as microservices can become difficult to manage due to sprawl, [Backstage plugins](https://www.getport.io/blog/top-5-backstage-plugins) can also become difficult to manage. With limited insight into version control and the quality of the plugins, this problem compounds as a large number of engineers within a team are actively encouraged to build new plugins.

This can result in:

- Code duplication, with multiple plugins doing the same thing, which is a drain on resources.
- Malfunctioning plugins causing downtime for your entire Backstage portal.
- A lack of a centralized and flexible software catalog, resulting in a lack of context and visibility, and slowing down the entire software development life cycle.
## Why Is a Unified Data Model Important?
![Plugins are not integrated and therefore lack the context developers need.](https://cdn.thenewstack.io/media/2024/12/05177008-backstages-lack-of-central-data-model-inner-image-1024x597.png)
Plugins are not integrated and therefore lack the context developers need.

Backstage’s community plugins, such as the Argo CD and Snyk plugins, provide users with the core information that they’re looking for. The Argo CD plugin provides a list of deployments for each service and the latest version in production. Meanwhile, the Snyk plugin provides a list of vulnerabilities for each service.

However, if you want to see a list of vulnerabilities relevant for the deployed versions of a service, you will need to build a new custom plugin. This plugin should query Argo CD to identify the version currently in production, and then cross-reference it with Snyk’s vulnerability data for that version.

This is because the community plugins do not talk to each other, meaning developers cannot get answers to questions such as “Do I have a Snyk vulnerability in production?” or, in the case of the [Google Cloud Platform](https://cloud.google.com/?utm_content=inline+mention) (GCP) plugin, “What services in GCP failed a recent CI deployment?” without manually connecting the dots.

Without integrated plugins, it is impossible to build a comprehensive [incident management](https://www.getport.io/blog/how-internal-developer-portals-improve-incident-management) view that consolidates information from things including on-call tools, recent builds, last CD deployments, rollbacks and GitHub ownership data. The same can also be said for cloud cost optimization and infrastructure management.

To extract real value through context, you need engineers to develop customized plugins. That requires time from both a frontend engineer, who is familiar with the [React framework](https://roadmap.sh/react), and a backend or DevOps engineer. Over time, these resource costs add up, as does the upkeep of version control and quality, for which there is no clear way of tracking within the Backstage framework.

When dealing with service-level objectives (SLOs), standards checks and [scorecards](https://www.getport.io/guide/scorecards), the problem even becomes more apparent. Establishing rules on fragmented data is inherently difficult. Taking production readiness as an example, you may want to create a check to make sure all repositories have a README using information from GitHub. Then, you may want to create a second check to verify that test coverage meets or exceeds 80% as part of your code quality checks by pulling data from a tool like SonarQube. Accomplishing this in Backstage requires integrating the information into the software catalog and building custom plugins to check and present the status of each rule.

Backstage’s plugin model has merits, particularly in its ability to clearly separate responsibilities among stand-alone plugins. However, this approach effectively silos data, making it difficult for developers to achieve the seamless integration they need. Without adopting or favoring a shared data model, the [platform falls short](https://thenewstack.io/portal-vs-platform-why-you-need-to-think-about-both/) of enabling developers to access and leverage interconnected insights effectively for their workflows.

## What Is the Ideal Way for Developers to View Plugins?
One of the key frustrations for developers is that they have to keep switching context between different tools. Most Backstage builders merely shift this issue from the browser to Backstage, with tabs for the likes of Jira, Argo CD and GitHub Actions. This provides no real value to developers, and it means they’ll continue to be frustrated with the amount of context-switching they have to do.

If, for example, a developer is attempting to integrate a new API in a service that is built by a different engineering team, they should be able to easily find and understand information in a single source of truth.

The portal builder should create one clear, personalized view for each persona (e.g., developers, leaders, DevOps, security), providing all the essential information and context a developer needs in one place. That personalization might include presenting different levels of abstraction depending on the role. For example, with Argo CD data, a technical product manager might need a high-level view showing which version is running and the latest commit, while a site reliability engineer (SRE) or backend engineer might require a more detailed health overview of the system.

A clear view of everything minimizes distractions and enables developers to quickly find what they need — within a minute — and return to their work. [Research from GitHub](https://github.blog/news-insights/research/good-devex-increases-productivity/) shows that a good developer experience significantly boosts productivity by fostering focus and reducing interruptions. A portal should support their flow state as it speeds up developers and keeps them in their zone. Increasing velocity leads to increased return on investment for the organization.

Take the example below. Rather than have basic information in the overview and having to look through the tabs of each stand-alone plugin, the portal should enable a comprehensive overview of all the information in one place.

![Switching from separate tabs for specific plugins to one view with all of the information about all plugins in one place.](https://cdn.thenewstack.io/media/2024/12/391398cf-before-and-after.gif)
Switching from separate tabs for specific plugins to one view with all of the information about all plugins in one place.

Plugins also do not expose API endpoints to retrieve data. This causes limitations, as you cannot interact with the data from your CI/CD pipeline or integrate it with your AI agent, reducing the agent’s overall effectiveness.

## How to Fix Your Plugin Architecture
Let’s step back from the portal to consider the plugin architecture from a data engineering perspective. The extract, transform, load (ETL) approach is widely regarded as best practice for consolidating data from multiple sources into a unified repository. [Research](https://link.springer.com/article/10.1007/s11227-024-06413-1?) underscores the importance of ETL in data integration, supporting decision-making and strategic planning.

In this case, ETL means:

**Extract:**Pull information from all the different development tools and data sources.**Transform:**Shape and transform all the extracted information into one logical data model.**Load:**Load the logical data model into Backstage, enabling plugins to determine how to present the data tailored to different personas.
Engineering organizations today have data coming from various sources including:

- Source code management tools, like GitHub,
[GitLab](https://about.gitlab.com/?utm_content=inline+mention), Azure DevOps and so on. - Cloud providers like
[AWS](https://aws.amazon.com/?utm_content=inline+mention), GCP, Azure. - CI/CD tools like CircleCI, Argo CD, GitHub Actions.
- Cloud cost, monitoring and paging tools, and much more.
By applying ETL, individual raw data sets can be shaped to a format and structure that makes sense for organizations to use and learn from. There are two options for how to achieve this.

### Option A: Leveraging a Data Warehouse and Data Engineering
To overcome Backstage’s plugin-data problem, one approach is to centralize data from disparate sources into a unified repository. A data warehouse serves as the backbone of this approach, enabling seamless integration with tools like Jira, Argo CD and GitHub Actions through ETL tools such as Airbyte or Fivetran.

This setup eliminates data silos by consolidating information into a single, scalable storage layer, ready for transformation and use.

Using a data transformation tool like [dbt](https://www.getdbt.com/) transforms the raw data from the lake into a logical, unified model, ensuring consistency across all data points.

![Combining a data warehouse and ETL tools can centralize data into one repository.](https://cdn.thenewstack.io/media/2024/12/45932a29-etl-approach-inner-image-1024x597.png)
Combining a data warehouse and ETL tools can centralize data into one repository.

This shared model allows custom Backstage plugins to access and display centralized insights. Developers benefit from compact, actionable views that combine multiple data streams, such as deployment statuses, CI/CD logs and ownership details, instead of navigating isolated tabs. This integration transforms Backstage into a functional developer portal and enhances productivity and usability.

To support aggregations and more complex features, you can use calculated fields of the chosen data warehouse technology.

This approach has limitations when it comes to establishing [scorecards](https://www.getport.io/blog/using-scorecards-for-standards-compliance-a-repeatable-framework-and-examples) and tracking initiatives, as creating rules directly within a data warehouse is not straightforward. Additionally, the lack of self-service actions that can seamlessly integrate inputs from the data warehouse into the actions is another drawback. Option B might be a better choice in addressing those two issues.

However, Option A still provides meaningful value to developers. By addressing fragmentation and enhancing data collaboration, Backstage can become a more integrated platform.

### Option B: Using a Specialized Developer Data Warehouse Plugin
![Port’s Backstage plugin unifies data and enables no code/low-code data modelling](https://cdn.thenewstack.io/media/2024/12/76951da3-ports-backstage-plugin-inner-image-1024x597.png)
Port’s Backstage plugin unifies data and enables no-code/low-code data modeling.

Port has a new [Backstage plugin](https://backstage-plugin.getport.io/) that is built for developer data and tailored to platform engineers’ needs. It brings together the qualities of a specialized developer data warehouse with no-code/low-code data modeling capabilities to consolidate and centralizes your data. It also acts as a foundation to help overcome other challenges related to Backstage’s standalone plugin issue, such as:

- Integrating with multiple tools, including Jira, GitHub Actions and Argo CD.
- Relying on complex tools like dbt and SQL to structure data.
- Difficulty defining and tracking compliance with standards.
## Recommendations
Building a developer portal is difficult, but building one that developers love is even harder. Providing portal users with more autonomy, better visibility and more context can be the difference between a heavily adopted portal and one that fails to gain traction and that developers reluctantly navigate or avoid altogether.

Learn more about the Port plugin for Backstage: Apply to [join the beta](https://backstage-plugin.getport.io/), explore [Backstage alternatives](https://www.getport.io/blog/top-backstage-alternatives) or [compare Backstage and Port](https://www.getport.io/compare/backstage-vs-port).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)