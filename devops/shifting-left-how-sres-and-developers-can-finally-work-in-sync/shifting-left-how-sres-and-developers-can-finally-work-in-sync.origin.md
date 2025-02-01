# Shifting Left: How SREs and Developers Can Finally Work in Sync
![Featued image for: Shifting Left: How SREs and Developers Can Finally Work in Sync](https://cdn.thenewstack.io/media/2025/01/6c20ccf8-shift-left-sre-1024x576.jpg)
Site reliability engineers ([SREs](https://thenewstack.io/platform-engineering/sre-vs-devops-vs-platform-engineering/)) and developers often face the challenge of balancing speed with stability. For the most part, developers tend to focus on building features and coding, while SREs make sure those features run smoothly in production. But when something breaks, the lines blur — and that’s where [the problems start](https://thenewstack.io/sre-vs-platform-engineer-cant-we-all-just-get-along/).

The [“shift left” movement](https://hubs.la/Q034R5SG0) offers a way forward. It allows teams to tackle reliability and operational concerns earlier in the development process. By sharing ownership, teams can reduce friction and work better together.

## The SRE and Developer Disconnect
SREs are responsible for maintaining reliable systems, overseeing uptime, managing incidents and handling cloud infrastructure. Developers focus on writing code and shipping features. However, these roles often overlap, creating friction between them.

This tension arises from misaligned priorities and a lack of visibility into each other’s workflows. Developers prioritize shipping features and may neglect production requirements until problems arise. While they create applications, they often don’t feel accountable for their reliability. Conversely, SREs strive to maintain uptime but may lack context regarding recent application changes. These dynamics lead to inefficiencies, such as:

- Incomplete visibility leaves SREs unprepared during incidents due to missing insights into recent deployments, dependencies or configuration changes.
- Fragmented ownership results in unclear accountability, causing delays in resolving critical issues.
- A lack of shared frameworks hinders communication and coordination, particularly during high-pressure incidents.
- Product owners or business stakeholders may apply additional pressure on SREs without clear processes, exacerbating an already stressful situation.
Although developers increasingly [embrace the shift-left movement](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/), focusing on production requirements, secure coding and leveraging AI tools to enhance their workflows, these efforts are insufficient. Developers must take full accountability for their applications, encompassing code and reliability. Additionally, [SREs and developers](https://roadmap.sh/devops/devops-vs-sre) must collaborate on a shared framework with a unified source of truth for service ownership, health and dependencies. This foundation enables faster, more effective workflows and mitigates team disconnects.

## Step by Step: Shifting Left in Incident Management
Consider a scenario where a high-severity incident occurs during peak traffic. SREs may have all the infrastructure metrics but lack insights into recent application updates or dependencies. On the other hand, developers might not have access to production monitoring tools, leaving them blind to the issue’s root cause. This lack of shared responsibility turns a manageable problem into a prolonged outage.

Let’s explore a step-by-step guide for managing an incident or outage to demonstrate the impact of shifting left.

### 1. Proactive Prevention
Preventing incidents begin long before they occur. Teams can take several proactive steps to ensure production readiness:

**Define ownership:**Use a unified service catalog to establish clear ownership for every service, including its dependencies, health metrics and escalation paths.**Automate readiness checks:**Implement automated checks for production readiness, such as ensuring proper observability setups, validating CI/CD pipelines and checking for outdated dependencies.**Monitor proactively:**Set up alerts for potential issues, such as increasing error rates, slow response times or anomalies in deployment processes. These alerts allow teams to address problems before they escalate.
### 2. Detecting and Diagnosing the Issue
When an incident occurs, swift detection and diagnosis are crucial:

**Unified visibility:**Teams use a centralized portal to access real-time metrics, logs and dependency maps. This shared view ensures everyone has the information needed to assess the problem.**Ownership identification:**The service catalog automatically identifies the responsible team or individual and notifies them through preconfigured communication channels like Slack or Teams.**Cross-functional insights:**Both developers and SREs can see relevant details about recent deployments, configuration changes and application updates, enabling faster root cause analysis.
### 3. Coordinating the Response
With clear ownership and diagnostic data, the team can focus on resolving the issue:

**Automated incident channels:**An automated communication channel is created to bring together the right stakeholders and provide access to relevant tools and data.**Self-service remediation:**Developers use predefined workflows to address the issue, such as rolling back a faulty deployment, restarting services or scaling resources. These actions can be executed directly from the portal, reducing dependence on SRE intervention.**Escalation protocols:**If the issue requires specialized expertise, SREs step in to handle complex problems or enforce operational standards.
### 4. Post-Incident Improvements
After resolving the incident, teams focus on continuous improvement:

**Root cause analysis:**Teams collaborate to understand what went wrong and document their findings in the service catalog.**Tool enhancements:**Adjust monitoring tools and automated workflows to prevent similar issues in the future.**Process refinement:**Incorporate feedback to improve response procedures, training and documentation.
Ultimately, the solution is to redefine ownership and give everyone access to the tools they need. SREs should focus on setting standards and automating reliability tasks, while developers should own their applications end to end, including uptime and health.

## Unified Service Catalogs: A Key to Shifting Left
A unified [service catalog](https://hubs.la/Q034R6Pr0) can bridge the gap. It provides a clear view of services, their owners and their dependencies. This is an essential piece when implementing the “shift left” approach. By serving as a single source of truth, it provides:

**Clear ownership:**Ensuring every service has a defined owner and team responsible for its health and reliability.**Comprehensive visibility:**Offering insights into dependencies, configurations and compliance with production readiness standards.**Efficient collaboration:**Supporting self-service actions and automated workflows to enable faster, more effective incident resolution.
While the service catalog is critical, it’s part of a broader ecosystem that includes self-service workflows, [incident management automation](https://hubs.ly/Q034Rbr10) and collaboration tools. Together, these features empower teams to work more efficiently and confidently.

## Real Wins With Unified Tools
Teams using unified service catalogs see improvements in proactive prevention and reactive recovery. Here’s a deeper look at the benefits:

**Proactive incident prevention:**With automated compliance tracking, teams can identify and resolve issues before they escalate. For instance, a team might receive automated alerts when an application isn’t meeting[production readiness criteria](https://hubs.la/Q034R67l0), such as missing observability setups or outdated dependencies. By addressing these gaps before release, the team avoids outages and ensures smoother launches.**Faster recovery times:**During an incident, such as when a key service goes down during a peak traffic event, developers can quickly access self-service workflows to roll back changes, restart services or scale resources. Instead of waiting for SREs to intervene, the developer responsible can follow a predefined remediation path in the portal — rolling back a recent deployment or scaling resources with a single click. This significantly reduces the mean[time to recovery (MTTR)](https://hubs.la/Q034R68-0).**Improved collaboration:**With clear visibility into ownership, teams avoid confusion during high-pressure situations. For example, when a failure occurs, a unified portal immediately identifies the service owner and pulls in relevant stakeholders through automated Slack channels. Teams can focus on solving the problem rather than debating who should take action.
Imagine a critical outage occurs late at night. Instead of scrambling to figure out who owns the affected service, the unified portal automatically creates a dedicated Slack channel for the incident, notifies the service owner, and provides access to critical metrics, logs and dependency maps. Within minutes, the team can collaborate effectively to resolve the issue, cutting downtime dramatically. This streamlined approach exemplifies the power of shifting left: equipping teams with the tools to act quickly, confidently and efficiently.

## A New Ownership Model
Shifting left supports a shared accountability model. Developers own their applications, including reliability. SREs provide guidance, tools and high-level support when needed. This balance ensures everyone can focus on what they do best.

For example, developers take the lead in managing the response during an incident. They use the tools the service catalog provides to diagnose and fix the issue. SREs step in only for complex problems or to ensure standards are met. This approach reduces bottlenecks and empowers teams to work more effectively.

## Ready to Shift Left?
A unified service catalog can transform how SREs and developers collaborate. It fosters collaboration, reduces bottlenecks and keeps systems reliable.

Speak to like-minded people who are also shifting left in [Port’s community](https://hubs.la/Q034R7GK0) or see how you can shift left using [Port’s live demo](https://hubs.la/Q034R7-N0).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)