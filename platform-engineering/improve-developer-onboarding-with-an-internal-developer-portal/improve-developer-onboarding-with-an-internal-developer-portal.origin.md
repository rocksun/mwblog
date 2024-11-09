# Improve Developer Onboarding With an Internal Developer Portal
![Featued image for: Improve Developer Onboarding With an Internal Developer Portal](https://cdn.thenewstack.io/media/2024/11/36e7a119-welcome-1024x576.jpg)
Developer onboarding boils down to educating a new teammate on your software development life cycle (SDLC) so that they can deliver software. According to the Society for Human Resources Management, about
[70% of new employees](https://www.shrm.org/topics-tools/news/talent-acquisition/dont-underestimate-importance-good-onboarding) in the United States stay at a company for more than three years if they have a positive, well-structured onboarding experience. This also [boosts their productivity and retention rates](https://www.devlinpeck.com/content/employee-onboarding-statistics) to 58% and 60%, respectively.
But if you’ve ever onboarded a new teammate — or have been onboarded yourself — you know how time-intensive a task like this can be. Sometimes you spend more time
[answering questions and providing feedback](https://thenewstack.io/tackling-developer-onboarding-complexity/) to a new developer than performing tasks associated with the actual role.
Onboarding a new developer consumes so much time and resources that it often appears as its own task in a sprint, which takes away time the team could be spending working on new features. On the flip side, the new developer has to learn so much about their company culture, policies and colleagues — the last thing they need is an inefficient onboarding experience.
An
[internal developer portal](https://thenewstack.io/can-the-internal-developer-portal-solve-alert-chaos/) can streamline the onboarding experience and address numerous onboarding challenges. Let’s explore how.
## Challenges With Onboarding New Developers
There are specific pain points that
[an internal developer portal](https://www.getport.io/blog/what-is-an-internal-developer-portal) can solve. These include: **Lack of defined onboarding processes:**A lack of well-defined processes causes delays, confusion and an altogether negative experience for developers, so much so that it can affect employee retention. **Provisioning tools, access control and visibility:**A new developer must be given access to every part of their new software development life cycle (SDLC). They also may not be able to see other related services in certain tools unless they are given full edit permissions, which can introduce unnecessary risk. Overall, it can sometimes take up to 10 days to grant a new developer access to all of the services they need. **Understanding the code and related software infrastructure:**Every application is unique and complex. Understanding the relationships between different services, runtime resources and engineering teams can take months to grasp. **Providing tasks and template actions:**The end goal of onboarding is to add an effective new member to your team — so why not provide them with exactly what they need to get started? Template tasks and actions make developers autonomous much more quickly, reducing their time to productivity.
A developer needs to remember a lot, such as the order of onboarding tasks, how to deliver role-specific permissions, how services interact with one another — on top of delivering new features or making commits as usual. Let’s dive into each of these
[friction points](https://thenewstack.io/use-your-internal-developer-portal-to-drive-better-appsec/) and examine how an internal developer portal solves them.
## 1. Lack of Defined Onboarding Processes
The goal of onboarding is to help team members become productive as quickly as possible, making that outcome more valuable than documenting the process.
DevOps or platform engineers often bear the brunt of early onboarding because they must provide access and figure out:
- Which tools each developer needs access to.
- How to design their permissions.
- What level of visibility each developer needs into other team setups based on their role.
Figuring out all this consumes valuable time for teams every time a developer has to be onboarded. Without a clear process in place, developers may feel overwhelmed by the complexity of their role, unable to easily identify service owners or best practices, and overall disengaged from their new team. Not only does this negatively affect your new developers, but it also puts additional strain on your existing teams, which are responsible for acclimating the new developer to their engineering environment.
With an internal developer portal, you can create specific onboarding structures for different, common developer personas. This kind of view offers many benefits over the traditional onboarding process (or lack thereof), including repeatability, specificity and standardization of the onboarding experience more generally.
A structured onboarding experience within a
[portal drastically reduces the preparation needed](https://thenewstack.io/which-features-does-your-platform-engineering-portal-need/) to onboard new employees and standardize the process, ensuring that the onboarding experience is consistent and straightforward for all new developers. In turn, this boosts new developer satisfaction and engagement, sometimes by nearly 70%.
## 2. Tools, Access and Visibility
Without proper access to tools and software, a developer can’t make their first commit or do anything of value. On the other hand, if a developer has too much access, that can introduce privacy and security concerns.
In an onboarding context, it can be difficult to keep track of which services each developer needs access to and how much access or type of access they need. This can also change over time as developers leave the company, move teams or projects, or need special permissions to accomplish one-off tasks. That adds to the complexity of permissions for DevOps and platform teams.
If you’re onboarding external developers, including vendors and contractor teams, additional concerns arise when they need access to sensitive production environments or release pipelines to enable new software or build features.
An internal developer portal resolves these concerns with role-based access control (RBAC), which can be designed to grant and revoke access to different services based on time limits as well as role within the organization. Importing single sign-on (SSO) also helps you batch permissions by importing an external team’s infrastructure into your portal:
![A portal can restrict the service view to the user’s services and assets only.](https://cdn.thenewstack.io/media/2024/11/afaff9ce-image1.png)
A portal can restrict the service view to the user’s services and assets only.
An internal developer portal also enables you to control
[what each developer sees](https://thenewstack.io/using-an-internal-developer-portal-for-finops-visibility/), has permission to access and the specific permissions they have within each environment. ![Dynamically decide who can see which catalog pages so only users with management roles can access the Metrics page, for instance.](https://cdn.thenewstack.io/media/2024/11/fdf8f906-image2.png)
Dynamically decide who can see which catalog pages so only users with management roles can access the Metrics page, for instance.
![Dynamic RBAC controls ensure that users can only see their team’s services or assets.](https://cdn.thenewstack.io/media/2024/11/cab338d7-image3.png)
Dynamic RBAC controls ensure that users can only see their team’s services or assets.
These permissions can also be seen at the team level, which becomes helpful when building developer self-service actions and experiences. All of these permissions can also be changed from within the portal, removing the need to jump from service to service.
## 3. Understanding Code and Related Software Infrastructure
Let’s revisit our onboarding situation: You are new to your job and need to understand the code you are responsible for. You need to figure out:
- Where the code runs.
- Which, if any, other microservices it relies on.
- How the microservices are broken down.
- Where to find descriptions of each microservice, if they exist, and their API specs.
- Who is responsible for the other microservices your own service is calling.
At this point, you’re probably laughing because there is no way a single person can remember the thousands of components that are necessary to build a modern website. Even with comprehensive, well-maintained documentation, services and dependencies change frequently enough that any manual documentation is usually immediately out of date.
An internal developer portal provides a service catalog and blueprints, which add to the catalog by graphically demonstrating the relationships between interconnected services. When combined, the service catalog and blueprints provide new developers with a full, up-to-date list of every service the company uses to produce software, from staging and demo environments to their live production environment:
![An informative view of our new developer’s service and its related cloud resources, APIs and runtime assets](https://cdn.thenewstack.io/media/2024/11/9e2e9784-image4.png)
An informative view of our new developer’s service and its related cloud resources, APIs and runtime assets.
![A graphical view of our service, its dependencies and cloud assets](https://cdn.thenewstack.io/media/2024/11/a90520c5-image5.png)
A graphical view of our service, its dependencies and cloud assets.
With these views in the portal, a new developer can understand everything they need to know to get started at once, saving time spent asking questions of managers and peers.
These tools reduce the need for lengthy explanations and whiteboarding to explain the relationships between services and how they interact. They also eliminate the need to maintain separate documentation, as both the blueprint and catalog automatically ingest new services as they’re created and import the relationships between other related services, maintaining an updated graph of service dependencies and relationships in real time.
## 4. Providing a Task View and Template Actions
Now that our new developer has received proper access to tools and understands the service they own and its related components, they still need to know where to start or what their tasks are.
Take a look at the example below, which shows a Plan My Day experience for developers that lays out their tasks for the day:
![A developer experience built in Port, an open internal developer platform](https://cdn.thenewstack.io/media/2024/11/71757543-image6.png)
A developer experience built in Port, an open internal developer platform.
This
[short video on planning experiences](https://www.youtube.com/watch?v=wYCLtXxxRCc&list=PLTwEf67PTkOs3KkKClKbddX2ckHaGDV3Z&index=5) in an open internal developer portal explains more.
An internal developer portal makes it easy to provide a dynamic view of a developer’s tasks so they can identify the
[next thing they need to do](https://thenewstack.io/using-an-internal-developer-portal-for-golden-paths/). You can create views in the portal that show the developer:
- The next onboarding task they need to complete.
- Their open bugs.
- Pull requests that are pending review (and how long they have been waiting).
- Ongoing incidents.
- Key vulnerabilities affecting their service.
![An internal developer portal provides every developer the tasks they own, dynamically filtered.](https://cdn.thenewstack.io/media/2024/11/a0d06f32-image7.png)
An internal developer portal provides every developer the tasks they own, dynamically filtered.
These tasks are often called Day 2 operations, which go beyond the initial phases of training and provide developers with a sense of autonomy, boosting their productivity and satisfaction. Providing Day 2 operations in the portal also reduces time to productivity for new hires by making it obvious where to shift their focus.
Self-service actions also help abstract the complexity of internal processes. These can make it possible for developers to perform tasks or deploy resources following
[golden paths](https://www.getport.io/blog/how-internal-developer-portals-help-you-to-pave-and-remain-on-the-golden-path) immediately, which is not typically expected of new developers until their first month. ![With templated self service actions, it is easy for new developers to perform tasks according to the company’s golden paths, without fear of making mistakes or needing intensive review.](https://cdn.thenewstack.io/media/2024/11/88d0f0c7-image8.png)
With template self-service actions, it is easy for new developers to perform tasks according to the company’s golden paths, without fear of making mistakes or needing intensive review.
Automated workflows, found in some internal developer portals, also enable you to send Slack alerts to managers who need to review work or chain tasks to automate onboarding entirely. You can also
[automate standards management](https://www.getport.io/blog/managing-standards-in-a-developer-portal), which may help a new developer build their knowledge of internal best practices when they’re coding for the first time.
## Wrapping Up
Onboarding new developers requires a ton of groundwork, well-maintained documentation and a repeatable process — things that, under typical circumstances, are time-intensive and complex. An internal developer portal removes some of this complexity by:
**Defining the onboarding process:**Once you’ve built an onboarding experience in your portal, you can use it for new developers or as a template for other types of onboarding experiences, driving standardization. This eliminates the need to maintain internal documentation or onboarding documents outside of the portal. **Provisioning tools, access control and visibility:**Developers can see everything they need to but can only access and edit the services they own **.** **Displaying relationships between code and software infrastructure:**The service catalog boosts autonomy and transparency, making it easier for new developers to orient themselves with the SDLC and take action as needed. **Encouraging autonomy and productivity:**Views within an internal developer portal tailor actions, services, tickets, tasks and more into a single place, making it easier for new developers to pick up work and become productive sooner and with less hands-on training.
If you’re not sure where to start with your onboarding experience, take a look at our
[ultimate developer onboarding checklist](https://www.getport.io/blog/developer-onboarding-checklist) for some inspiration. If you’re not using an internal developer portal yet, check out our [live demo](https://demo.getport.io/organization/home) and [join our community](https://www.getport.io/community)! [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)