# Pulumi Launches New Infrastructure Lifecycle Features
![Featued image for: Pulumi Launches New Infrastructure Lifecycle Features](https://cdn.thenewstack.io/media/2024/04/5e950cc6-walter-frehner-i2wcssuw-pi-unsplash-1024x683.jpg)
[Pulumi](https://www.pulumi.com/), a leader in the [Infrastructure as Code](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/) (IaC) arena, has launched a set of new features for its deployment workflow product — [Pulumi Deployments](https://thenewstack.io/pulumi-introduces-one-click-deployments/) — that provide new infrastructure lifecycle management capabilities for the platform.
These features include
[drift detection](https://thenewstack.io/how-drift-detection-and-iac-help-maintain-a-secure-infrastructure/) and remediation, automatic infrastructure cleanup with [time-to-live (TTL)](https://www.techtarget.com/searchnetworking/definition/time-to-live) stacks, and scheduled deployments.
## Get My Drift
Drift is when the state of an organization’s infrastructure differs from the state defined in the organization’s configuration. The new drift detection and remediation feature enables users to continuously monitor infrastructure to detect and notify teams when the actual cloud infrastructure deviates from the IaC source of truth. Drift can be automatically remediated with custom policies that reapply the last known good state from prior deployments, the company said.
To track any deviation, users can set up custom alerts using
[Slack](https://thenewstack.io/slacks-new-dev-portal-offers-ci-cd-python-javascript-aids/), Microsoft Teams, or [webhooks](https://thenewstack.io/new-open-source-standard-brings-consistency-to-webhooks/), or view drift through dashboards in Pulumi Cloud.
## TTL Stacks
Meanwhile, the new Time-to-Live (TTL) Stacks automatically clean up infrastructure based on flexible policies after a certain amount of time has passed. This allows teams to enable self-service without worrying about stale infrastructure and associated costs.
[Joe Duffy](https://www.linkedin.com/in/joejduffy/), co-founder and CEO of Pulumi, said the new features were highly customer-driven.
“Drift detection is the more immediately recognizable and important, however, TTL stacks get my vote [as the most significant new feature]. Many of our customers want to enable self-serve cloud infrastructure for their developers and — especially in the era of AI, data scientists — but fear doing so because of the possibility of costly waste building up,” Duffy told The New Stack. “With TTL stacks, this fear is eliminated, and infrastructure teams now have complete control to eliminate the risk of waste. So, although it’s a little more subtle than drift which everybody will immediately understand, I expect TTL stacks to be a fan favorite.”
In addition, the scheduled deployments feature enables organizations to schedule deployment activities based on an arbitrary
[cron](https://thenewstack.io/move-your-cron-jobs-to-serverless-in-3-steps/) schedule, allowing teams to automate recurring workflows and extend the system with custom policies and operational workflows, the company said.
## Day 2
These new infrastructure lifecycle management capabilities aim to improve the reliability, cost, and security of
[Day 2 operations](https://thenewstack.io/cloud-native-day-2-operations-why-this-begins-on-day-0/). They enable platform teams to deliver faster cloud provisioning while maintaining the necessary guardrails, Duffy said.
Indeed, the new features signal Pulumi tackling more Day 2 operational challenges — a critical area especially for the company’s largest enterprise customers, Duffy told The New Stack. “We see them struggling with pain here every day and we are excited to give them an out-of-the-box solution so they can focus their energy on solving their higher-value business challenges,” he said. “As we evolve from infrastructure as code to many products, infrastructure lifecycle management will be a key theme.”
For instance, “At Oleria, we understand the importance of addressing issues with privacy, security, and data integrity. Earning and maintaining our trust isn’t just a responsibility but a fundamental aspect of our mission,” said
[Jim Alkove](https://www.linkedin.com/in/jalkove/), CEO of [Oleria](https://www.oleria.com/company). “Pulumi also understands how these attributes affect cloud infrastructure,” he added, noting that the new capabilities will help Oleria enable its customers to “securely manage access to decentralized SaaS applications, adaptively and intelligently.”
## Free Pulumi Deployments
With Pulumi Deployments, organizations can avoid building custom home-grown systems. The product includes
[git](https://thenewstack.io/git-at-15-how-git-changed-the-way-we-code/) push-to-deploy, ephemeral review stacks, and UI-based deployment, with a REST API for custom workflows such as blue/green and multiregion deployments.
Pulumi also announced a new free tier for Pulumi Deployments, which applies to the usage of these new features. The company believes these enhancements will help customers make the most of their cloud efforts by allowing them to move faster with confidence.
## On IBM and HashiCorp: “We’ll Out-Innovate”
Meanwhile, Duffy addressed the big issue that could shake up the infrastructure as code space, as IBM is in negotiations to acquire HashiCorp, another IaC leader.
“HashiCorp ceded the innovation agenda for IaC to us years ago,” he said wryly. “IBM is obviously an incredible company with a rich legacy; however, they are best known for world-class consulting and go-to-market, and I expect this acquisition to leave the door open for Pulumi to continue to out-innovate and accelerate gaining market share even further.”
Pulumi has taken an innovative approach to IaC by allowing users to define infrastructure using general-purpose programming languages like JavaScript, TypeScript, Python, and Go. This enables developers to use familiar languages and leverage the power of these languages for abstractions, testing, and reusability.
The
[global infrastructure as code market](https://www.fortunebusinessinsights.com/infrastructure-as-code-market-108777) size was valued at $759.1 million in 2022 & is projected to grow from $908.7 million in 2023 to $3,304.9 million by 2030. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)