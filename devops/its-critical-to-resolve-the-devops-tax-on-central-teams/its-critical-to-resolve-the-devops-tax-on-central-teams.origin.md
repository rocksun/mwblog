# It’s Critical To Resolve the DevOps Tax on Central Teams
Within [DevOps](https://thenewstack.io/devops/) culture, developers are responsible for deploying and maintaining infrastructure that supports the application code they’re writing. While many herald the rise of DevOps culture as a dramatic improvement in time to production, there are hidden costs for both the developer and the teams supporting them.

Within DevOps, developers are now expected to be experts in:

- Their core application expertise areas (backend, frontend).
- A variety of heterogeneous cloud services and how they fit together.
[Infrastructure as code](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/)configuration and deployment.
These changes to developer responsibility result in overwhelmed developers that cause significant noise at the expense of other central teams.

## The DevOps Tax
Given the shift from on-prem to cloud services, central teams now exist to [manage companies’ cloud platforms](https://thenewstack.io/cloud-management-platforms-need-robust-automated-integration/). With names like Platform, Foundations, Infrastructure, or DevOps, these teams are tasked with the stability of the cloud platform. Instead, they’re spending time supporting developers at the expense of availability, reliability, and scalability.

Central teams spend their time in two primary areas: guiding and assisting developers when they [deploy and triaging or troubleshooting improperly configured infrastructure](https://thenewstack.io/tutorial-configure-deploy-an-edge-application-on-cloud-native-edge-infrastructure/).

This adds up across an organization. One large FinTech company reported supporting 40 manual requests each week, at the rate of hundreds of hours per week, for infrastructure that touches critical applications.

Central teams are stuck in one-off request mode, sacrificing their future to make it through each week. Critical priorities such as overall uptime, performance, and a robust catalog of supported services are neglected.

The downstream effects include overall system degradation, misconfiguration, and impacts on performance. This results in customer-facing outages, downtime, or even incidents.

## Contemporary Attempts at Solving
These impacts haven’t gone unnoticed, and organic solutions have become popular. The most notable of these are HashiCorp’s [Terraform modules](https://developer.hashicorp.com/terraform/language/modules). Modules provide a format for creating basic Terraform templates, which gives users some guidance when deploying cloud infrastructure. However, modules have some drawbacks that aren’t immediately apparent.

In particular, Terraform modules:

- Require a user to know Terraform.
- Abstract away the complexity that may ultimately be impactful.
- Don’t allow for edits to the underlying Terraform.
- Have no built-in UI.
- Often feature poor documentation.
Modules are similar approaches that rely on abstracting or modifying existing tooling, which results in limited improvement and similar issues: cloud stability, developer pain, and underwater central teams.

## Need For a New Approach
Companies [need to reevaluate how their DevOps](https://thenewstack.io/devops-needs-security-champions/) processes and culture impact their business. Proceeding at the status quo will degrade [developer productivity while central teams](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/) accumulate endless technical debt.

As one-off requests continue to take priority, investments in a cloud platform that is available, reliable, and scalable will fall by the wayside. Organizations that want to be successful in the long run and shed the developer tax should:

- Prioritize the critical services and drop manual support for those that don’t matter.
- Focus on automation for critical services.
- Make best practices easy to follow, with golden templates and sensible defaults.
- Adopt scalable thinking to get off the triage treadmill.
## Real-World Examples
When I worked at Netflix, we adopted this new approach across various central teams: security, platform, networking, etc. Here are some examples of real-world projects embedding sensible defaults and automation, helping developers avoid context switching and the need for specialization.

**ConsoleME**: The Netflix identity and security teams previously received many requests for creating and configuring IAM. They created a wizard that eventually became a [popular open source project](https://github.com/Netflix/consoleme).
**Repokid** [is an open source paved road I created at Netflix](https://github.com/Netflix/repokid) to achieve the least privilege. It doesn’t even require developers to interact with it.
**Spinnaker**: Probably the most well-known example, [Spinnaker](https://github.com/spinnaker/spinnaker) automatically creates everything developers need around an application (VPC, security groups, IAM, etc.)
**S3 Slackbot**: We created an S3 Slackbot that automatically created properly configured S3 buckets based on developers choosing options. This was a very successful example that we didn’t open source.
**Alerting and monitoring powered by Mantis**: Netflix created a framework based on the open source tool Mantis that developers could simply drop into their code to get a dashboard with automatic logging.
## Conclusion
While the DevOps culture has been a short-term boon to businesses where software is their core product, it has also resulted in a buildup of debt for central teams that could spell doom for companies that rely on available, reliable, and scalable cloud backbones.

Companies should look to modern approaches, as Netflix has exemplified. These approaches automate and scale central teams instead of expecting those teams to grow linearly with their developer base.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)