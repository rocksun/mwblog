# API Governance and Developer Experience in a Developer Portal
![Featued image for: API Governance and Developer Experience in a Developer Portal](https://cdn.thenewstack.io/media/2024/08/2c860e27-boaters-1024x576.jpg)
Enterprises often turn to API catalogs when they are seeking a way to increase [API](https://thenewstack.io/using-a-developer-portal-for-api-management/) discoverability and reduce the risk of duplicating business logic. However, while a catalog exposes all available internal APIs with relative ease, a catalog falls short of the transformation in developer experience they are seeking.

When considering how to improve the current developer flow as it relates to building new APIs, they should consider the following three questions (as originally asked by Mark Boyd of Platformable during [Portal Talks 2024](https://www.portaltalks.io/)):

**Are developers happy?**
Are they interested in their work, productive, solving problems and building things? Or are they involved in manually repetitive tasks?**Are costs reduced?**Are the labor costs associated with repetitive tasks high? Do easily avoidable mistakes, misconfigurations and vulnerabilities unnecessarily eat up time that should be dedicated to deep focus? Does this add to customer acquisition costs?
**Is time to market fast?**
Can the business create products and services at pace and earn from new revenue streams as fast as possible?
Boyd’s recommended approach to improving — if not altogether changing — developer experience when developing new APIs is lightweight API governance. This approach outlines a fundamental change to the way new APIs are developed, increases developer happiness, lowers costs and speeds up time to market.

## Lightweight API Governance in an Internal Developer Portal
Let’s explore how and why you should use an [internal developer portal](https://www.getport.io/blog/what-is-an-internal-developer-portal) for lightweight API governance:

## Planning
### Context Provides Developers with a Head Start
When an engineering team determines that an API user needs *something* — whether that is a new API or an additional feature in an existing API — and a solutions architect confirms that the best approach to meeting this need is an API, the planning process should be informed using an API catalog. No [portal will replace valuable legacy knowledge](https://thenewstack.io/which-features-does-your-platform-engineering-portal-need/) in an engineering organization, but using a portal can lead developers down the right path.

For example, instead of asking the most senior developer on the team, “Do you know if an API that performs <business function> exists? If so, who owns it?” you should first refer to your global API catalog hosted in your portal, then familiarize yourself with the API, then reach out to the technical lead or subject matter expert to fill in the gaps.

Developers can use a portal to understand what the API does, how healthy the API is, the rate limits in place and other important testing considerations. In addition, developers can provide ratings for APIs (one through five stars with the option to add a comment) using [self-service actions](https://www.getport.io/glossary/developer-self-service) within their portal of choice. This enables engineering leaders to promote highly-rated APIs and give specific feedback to APIs with low ratings. Combining these specific examples, developers get a head start before working with other APIs.

**Self-service actions** allow developers to perform necessary actions at the click of a button within the guardrails determined by DevOps or security teams, eliminating the need for tickets that hurt productivity.
![Developers can see the information about an API within the portal](https://cdn.thenewstack.io/media/2024/08/b4fda4be-image3.png)
Developers can see the information about an API within the portal.

### Considering Standards
You can involve a [product manager early — easily if you’re developing](https://thenewstack.io/a-portal-as-a-product-approach-for-internal-developer-portals/) an API that serves only your business unit, but with more difficulty if your API extends past the virtual boundaries of what your team controls. Actively documenting product managers, their [standards](https://www.getport.io/blog/using-scorecards-for-standards-compliance-a-repeatable-framework-and-examples) and their roadmaps in a portal can support this effort.

If your engineering team relies solely on wikis that outline standards for developing APIs, but ownership of the wiki is not clear, developers may become frustrated by trying to do the right thing only to be told that the documentation is stale. The best approach is typically not documenting step-by-step guides in wikis, but instead translating these instructions into short self-service actions that allow developers to provide minimal input and receive precisely what they need. Wikis, in this case, are best used for subjective descriptions of approaches rather than task lists. The image below shows one example of how this could look, but keep in mind that all inputs are customizable and that advanced configuration is available.

![A self-service form in a portal provides developers with autonomy when it comes to APIs](https://cdn.thenewstack.io/media/2024/08/6ed28810-image4-938x1024.png)
A self-service form in a portal provides developers with autonomy when it comes to APIs.

Organizations that use several API design tools should ensure developers do not have to guess which one best applies to the task at hand or ask developers a few questions in a self-service action to automatically guide them to the correct design tool. Similarly, it will guide them in writing a specification by asking them to populate a template, rather than having to find the right template.

Developers planning a new API will likely need to consult with another business unit to determine how best to fit into their data model. You can speed up this collaboration by ensuring the data model for a specific team is accurately depicted on a team page in a portal.

When developing this new API, developers should first check the portal to understand the potential API consumer persona and review any existing feature requests as well as API analytics to support their decision-making about what should be included in v1 of this API. Searching within an internal collaboration tool such as Slack or Teams, doing a data call for the latest API needs or reviewing an outdated spreadsheet might lead to developing the wrong features. Using a [portal that maintains](https://thenewstack.io/is-your-internal-developer-portal-maintainable/) the latest open feature requests and distills API analytics into insights that can be useful for decision-making might be a better way to do this.

To conclude the planning process, Boyd recommends writing a press release that announces to the world the new value developers will derive from this new API. This could be the final step of a self-service action that guides developers to planning their API after being pointed to the correct tool. Similarly, it may be beneficial to capitalize on the information stored in a portal about API consumers by broadcasting an announcement to the right potential users directly from a portal using a self-service action. Public announcement channels are sadly sometimes ignored, but channels that are targeted to a specific audience can be selected manually or automatically to ensure the announcement goes to the right audience.

## Golden Paths
DevOps teams often are pained when developers use the wrong template from outdated documentation or seek assistance from them for simple tasks that are inadequately documented. Meanwhile, developers struggle with the need to find the right documentation page, perform all necessary steps by creating a series of interconnected tickets, then circle back several days later to find that an issue has halted the process entirely.

An alternative approach is to translate the documentation into a form of automation and provide API developers with a [golden path](https://thenewstack.io/using-an-internal-developer-portal-for-golden-paths/). This ensures developers get what they need immediately and that standards are upheld.

Boyd described a few key elements that should be included in a single self-service action:

- A repository template with key resources and configurations to enable developers to get started quickly within the guardrails of the best practices for code development.
- A pipeline that can build this repository and push the resulting artifact all the way to production. This should include all steps deemed necessary for the organization to trust the code that is being deployed to production.
- A set of manifests to allow for deploying this application. For example: Helm charts, Kustomize configs or other non-Kubernetes configurations.
[Observability](https://www.getport.io/blog/observability-in-platform-engineering-strategies-for-seamless-integration)baked in. Reasonable defaults for logs, traces, metrics and alerts that can be tweaked as needed, but require minimal thought and input from the developer.
Moving beyond simply creating a new API using a self-service action, portals may also be used for “[Day 2 operations](https://www.getport.io/blog/give-day-2-operations-autonomy-to-your-developers),” which are operations that modify an existing entity. Some examples of this include deploying an API to an API gateway or enriching information for a legacy API without having to copy and paste a metadata template into the repository.

![Examples of quick actions for Day-2 operations within a portal](https://cdn.thenewstack.io/media/2024/08/cf07f20f-image1.png)
Examples of quick actions for Day-2 operations within a portal.

## Ownership and Collaboration
The golden path described above should automatically select ownership of the API. If the API has upstream or downstream API dependencies, this should be automatically inferred or easily declared by the developer that initiates the golden path, and a network of collaborating teams should be automatically inferred based on these declared dependencies.

## DevSecOps Baked-In, Not Bolted-On
Developers with a new API seek DevSecOps’ approval at the most critical time: prior to deploying to production. DevSecOps teams understand that their role is to serve the business purposes of the organization, but are often put into this difficult scenario by well-meaning API developers seeking to put the finishing touches on their API. DevSecOps can work quickly, but often not quickly enough.

To address this requires both a process change and a tool change. DevSecOps should be involved in the API development process. Some of their hard work should be seen in the golden path described above, where the new API is compliant from the beginning due to the inclusion of security steps within the default pipeline.

A default pipeline and discussions with DevSecOps will not solve all security and regulatory issues, so objective security and regulatory standards for APIs may be tracked and enforced automatically using the scorecards in a portal. DevSecOps teams may review the scorecard of an API in development and, if their criteria are met, the API could go to production without the active, direct involvement of DevSecOps. This is what engineering VPs dream of: a fast track to production that satisfies the needs of all.

APIs that process sensitive data (such as PII or PHI) can also benefit from custom properties (such as “type of processed data”) and scorecards that apply only to these APIs, ensuring deployment to production is seamless, aiding both engineering and DevSecOps.

## InnerSource by Default
Organizations with disparate development teams worry about duplication of efforts that unnecessarily slow development. To prevent this, organizations attempt to implement an InnerSource program. Without a way of enforcing this (a custom-built repository scanner or, better yet, a portal with InnerSource-approved golden paths and scorecards), InnerSource programs tend to be an afterthought for engineering teams.

While developers may object to new inner source requirements (for example, repository changes such as the inclusion of detailed GETTINGSTARTED.md, CONTRIBUTING.md or HELPWANTED.md files), they’ll reap the benefits of these when being asked to develop APIs that have already been built or when being asked to develop complex functionality that someone else in the organization has already solved. Ingesting these files (along with the README.md and other documentation, of course) automatically makes them part of the global search functionality in Port. When paired with customizable fields such as “subject matter expert” or “technical lead,” developers are quickly able to find what they’re looking for and collaborate with the right colleague by asking the right questions.

## ‘Help Wanted’ Marketplace and ‘Upcoming Work’ Calendar
Boyd noted that the best portal for use with APIs also includes a calendar of upcoming work, where developers from different teams may view the planned work of other teams. Adding onto this, organizations sometimes need a marketplace of “help wanted” and “help offered,” where engineering team leaders may borrow and loan assistance to ensure their own and the organization’s development needs are being met.

## The Finishing Touches
Finally, some tools only come into play toward the end of the API development process, including linters and API-style enforcement tools. There may be benefits to shifting these tools left, but having a self-service action to stage an API for deployment to production that brings in this final tool set will speed time to market toward the end of the process.

## Conclusion
Returning to the three questions that should guide the enhanced developer experience when developing API:

- Are developers happy?
- Are costs reduced?
- Is time-to-market fast?
Portals play a key role in ensuring the answer to each of these questions is a resounding “yes.” Self-service actions are the golden paths that allow developers to focus on building things and solving problems, largely relieving them of manually repetitive tasks. Scorecards assuage the concerns of DevSecOps and GRC teams early and often, providing objective checks of APIs in development, ensuring approval costs (in terms of time spent on manual checks) are low. API catalogs ensure developers deliver APIs at a fast pace, reducing time to market by speeding up time to discover existing APIs and collaborate on them.

Find out more about [API management in developer portals here](https://www.getport.io/usecase/api-management-and-developer-portals).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)