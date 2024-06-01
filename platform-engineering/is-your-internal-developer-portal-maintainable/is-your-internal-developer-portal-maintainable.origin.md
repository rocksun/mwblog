# Is Your Internal Developer Portal Maintainable?
![Featued image for: Is Your Internal Developer Portal Maintainable?](https://cdn.thenewstack.io/media/2024/05/c7750283-maintenance2-1024x576.jpg)
[Internal developer portals](https://thenewstack.io/how-do-the-internal-developer-platform-and-portal-connect/) are fairly new. As with all things new, there are multiple theories about what exactly should be accomplished using them. There is one thing that everyone can agree on: Internal developer portals and platforms are a [core interface for developers](https://thenewstack.io/internal-developer-portals-can-do-more-than-you-think/), and they need to be easy to maintain and easy to evolve. After all, if people, processes and technology evolve, so do the interfaces serving developers.
How can you tell whether your choice of portal can evolve and be maintainable? Let’s explore all about that.
An effective internal developer portal is made up of several elements:
[the software catalog](https://www.getport.io/product/software-catalog), [developer self-service](https://www.getport.io/product/self-service), [scorecards](https://www.getport.io/product/scorecards-and-initiatives), [automations](https://www.getport.io/product/workflow-automation) and [visualizations](https://www.getport.io/product/dashboards-and-visualizations). While all are part of delivering developer experiences, we’ll examine two:
- The software catalog (service catalog)
- Self-service actions
## Software Catalogs Need a Flexible Data Model
A flexible data model means being able to model your engineering DNA and use cases in the portal, both to:
- Reflect the actual software delivery life cycle (SDLC) and tech stack in the portal, which will make the portal trusted by both developers and managers.
- Add use cases to the portal such as adding AppSec data to support AppSec standard compliance in the portal.
A good portal lets you define, change or add entity kinds in the software catalog as well as the different relationships between those entity kinds.
Let’s look at both of those in more detail.
### Custom Entity Kinds
Entity kinds are things like resources, components and APIs. The entity kinds form what we call the data model of the software catalog. This is the map the software catalog uses to explain the SDLC world to its users. What is left out of the map doesn’t exist in the portal.
Here are some examples of entities that you may want to include in your portal:
- Cloud permissions so you could provide
[just-in-time access](https://www.getport.io/blog/managing-just-in-time-permissions-in-a-developer-portal)and work more securely.
- Alerts so you could
[unify alerts in the developer portal](https://thenewstack.io/can-the-internal-developer-portal-solve-alert-chaos/)and make it easier for developers to understand and resolve issues.
- Incidents so you could
[support on call](https://www.getport.io/blog/how-internal-developer-portals-improve-incident-management)and make it a better experience for developers and reduce mean time to repair (MTTR).
- Vulnerabilities so you could
[bake security into every developer routine](https://www.getport.io/usecase/appsec).
- CI/CD so you could use the portal as a
[CI/CD catalog](https://thenewstack.io/simplify-ci-cd-with-a-general-purpose-software-catalog/).
- API data so you could use the portal for
[API governance](https://www.getport.io/blog/manage-your-apis-using-an-internal-developer-portal)and more.
Being able to include these entities without significant coding is key.
**What to look out for:** portals that have a fixed number of entity kinds (for instance, only the C4 model) or that require coding to change them.
### Understanding Dependencies
Rather than assuming there are fixed relationships between entities, you need the ability to distinguish between different types of dependencies, such as separating runtime cloud resources (compute instances) from storage resources (databases and
[AWS](https://aws.amazon.com/?utm_content=inline+mention) S3 buckets).
You also want your portal to be able to specify multiple, distinct relationships between entities, providing granularity and clarity in understanding resource dependencies.
**What to look out for:** a portal where you cannot control the relationships between entity kinds
### Lack of Context and Trust = Lack of Adoption
Without the ability to use custom entity kinds or distinguish dependencies, your software catalog falls short in representing key aspects of the SDLC. As a result, it offers less context and utility to your stakeholders. This is crucial because developers are less inclined to fully adopt a portal that fails to meet many of their needs.
## Automated, Real-Time Data Ingestion
Internal developer portals, and specifically the software catalog in them, need to remain current. To be maintainable and trusted, this needs to happen automatically. By using auto-discovery, real-time data updates and multiple ways to input data, you can avoid the time-consuming task of manual maintenance, ensuring your portal’s information is always current and accurate.
Here are the basic requirements:
**Auto-Discovery:**The catalog should automatically find the relevant software entities across the organization. This involves scanning various systems and platforms to identify and catalog new or updated entities without needing manual input. Without auto-discovery, you will be dependent on developer toil and that isn’t a good beginning. **Reconciliation and Real-Time Updates:**The catalog should regularly update its data to match “sources of truth” such as third-party systems to ensure its accuracy. This is important for maintaining trust in the portal and applies to all types of data, including costs, permissions, alerts and vulnerabilities. The system should correct any discrepancies between the cataloged information and the actual state of resources. A prime example is security vulnerabilities. The AppSec vulnerability data within the catalog must remain current. If it’s outdated, confidence in the catalog diminishes and it loses its effectiveness in prompting timely actions. Consequently, this undermines the portal’s role as a reliable source of alerts. **Multiple Ingestion Pathways:**Efficient data entry should be automated, avoiding manual input wherever possible. Manual updates are prone to errors and place an unnecessary burden on developers. Automated options include: **REST API:**Allowing automated systems and scripts to directly update the catalog. **IaC (Infrastructure as Code):**Integrating with IaC tools to automatically update the catalog during deployment processes. **Webhooks:**Using webhooks from various platforms to receive updates about resource or configuration changes.
-
These features are vital for keeping a catalog accurate and up to date in a dynamic, large-scale environment, helping to streamline operations and improve efficiency. Without these capabilities, the manual effort needed to maintain the catalog becomes impractical and error-prone, which can significantly slow down the organization. Additionally, requiring developers to manually update the catalog without offering them clear benefits can make it difficult to get them to use the portal.
**What to look out for: **Portals that require developers to carry out a lot of manual work with YAMLs. This isn’t just inconvenient, it can create serious maintainability issues and require too much of developers, without giving them anything in return.
## Plugins Can’t Fix an Inflexible Data Model
There is a tendency to want to solve the problems we just described with plugins. Can’t represent additional types of entities (“kinds”) in the software catalog because of an inflexible data model? No problem, let’s use a plugin.
However, plugins can sometimes exacerbate the problem by lacking the functionality and flexibility you might expect, ultimately hindering the effectiveness of the internal developer portal.
Why is this an issue?
The purpose of a developer portal is to provide developers with relevant, abstracted information tailored to their specific needs. To achieve this, two key elements are necessary:
**Central metadata store:**The software catalog must use a central metadata repository where all data — from the core model or third-party tools — can be contextually searched and used to create comprehensive views of information, such as standards scorecards and more. With some portals, the data of the plugin does not sit alongside the data of the core software catalog. Without this centralization, plugin data cannot be searched effectively, making it difficult to answer important questions like, “Which services have open incidents?” This limitation significantly reduces the software catalog’s usefulness for any internal developer portal use case. Whether you are looking for cost issues or determining which services are not production-ready, you cannot efficiently search for these issues on a microservice-by-microservice basis. **Being able to abstract data to your liking:**The link between the data sourced from third-party systems and the user interface that displays this data is constrained. It can be incredibly difficult to show more or less detail, or display the data differently. Often, changes require forking a plugin, meaning React development skills are required, and these are not commonly found among DevOps engineers. After forking, maintenance is your (and your organization’s) isolated responsibility.
## Self-Service Actions Aplenty (Including Day 2 Ops)
You want your portal to be able to directly provide self-service for a wide range of actions such as: deploying services, rolling back, triggering incidents, creating cloud resources, toggling feature flags, adding secrets, gaining temporary database permissions and setting up development environments.
This means that developers can do more than scaffold new services but also use self-service actions for
[Day 2 operations](https://www.getport.io/blog/give-day-2-operations-autonomy-to-your-developers).
Existing CI/CD pipelines like GitHub Workflows, GitLab CI, Argo Workflows, AWS Lambda and Kubernetes operators come with powerful, ready-to-use actions that enable quick and reliable execution of various tasks.
For instance, GitHub Workflows provides hundreds of built-in actions available in its marketplace, which can be used to efficiently manage a wide range of operations. Even for scaffolding, the Cookiecutter library can be incorporated into CI/CD pipelines to customize and create repositories according to specified standards with greater ease and flexibility.
Given these capabilities, an internal developer portal should focus on enhancing the UI layer of the self-service action forms and strengthening integration with these existing CI/CD engines. This approach ensures a seamless experience for developers, leveraging the strengths of established tools while providing a user-friendly interface.
**What to look out for:** portals that have only one way to trigger self-service actions, forcing you to rip and replace your previous work, and that do not have a strong integration with your current CI/CD pipelines.
## Key Takeaways
An effective internal developer portal hinges on integrating a robust software catalog and comprehensive self-service actions. A flexible data model that supports custom entity types and accurately represents dependencies is essential for creating a useful and dynamic catalog.
Automated, real-time data ingestion ensures that the information remains current, reliable and free from the burdens of manual maintenance. These features collectively enable developers to efficiently find and use the resources they need, fostering a more productive and streamlined development environment.
Moreover, while plugins may offer quick fixes, they often fall short in flexibility and functionality, potentially hindering the overall effectiveness of the portal. Instead, focusing on enhancing the UI layer of self-service action forms and strengthening integration with existing CI/CD pipelines ensures a seamless and efficient experience for developers.
By leveraging the strengths of established tools and providing a user-friendly interface, organizations can build a developer portal that not only meets current needs but also adapts and scales as those needs evolve, ultimately driving greater adoption and satisfaction among developers.
Learn more about internal developer portals at
[Portal Talks](https://www.portaltalks.io/) on June 26-27, which The New Stack’s [Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/) will be hosting. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)