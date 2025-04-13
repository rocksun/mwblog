# Tackle IaC Tooling Complexity and Growing Cloud Costs in 2025
![Featued image for: Tackle IaC Tooling Complexity and Growing Cloud Costs in 2025](https://cdn.thenewstack.io/media/2025/04/bd1fc482-maze12-1024x576.jpg)
Initially, [Infrastructure as Code (IaC)](https://thenewstack.io/introduction-to-infrastructure-as-code/) promised to ensure simpler, more predictable and highly repeatable cloud operations. By [codifying infrastructure management](https://thenewstack.io/infrastructure-as-code/), organizations aimed to reduce manual errors, standardize configurations and increase operational efficiency. However, as cloud adoption has grown, reality hasn’t quite matched this vision.

Instead, cloud complexity is up year over year as multicloud and multi-IaC environments become the norm. Teams increasingly struggle with fragmented toolchains and persistent skill gaps, plus mounting cloud costs that continue to grow alongside all that complexity.

But what are cloud practitioners getting wrong, and how can they address it?

The [State of Infrastructure as Code 2025 report](https://www.firefly.ai/state-of-iac-2025) highlights the [challenges engineering teams still face](https://thenewstack.io/why-your-infrastructure-as-code-strategy-still-sucks/), showing clearly where IaC practices have drifted (like configurations) from their original intent.

**The Interconnected IaC Challenges **
In addition to a lack of IaC coverage, according to the report, teams increasingly struggle with a few major, and interconnected, challenges:

**Fragmented and complex tooling:**38% of organizations face significant operational difficulties due to fragmented toolchains, leading to confusion, inconsistent practices and excessive cognitive overhead.**Inadequate automation adoption:**A significant portion (24%) continue running IaC manually from local environments, directly undermining its intended automation and consistency benefits.**Escalating cloud costs:**65% report increasing difficulties controlling cloud spending as cloud complexity increases, largely due to missing or poorly integrated cost controls within IaC workflows.
Further complicating matters, nearly half of respondents highlighted the lack of skilled IaC practitioners as their top barrier. The talent shortage makes effective management of complex toolchains and robust cost controls even more difficult, creating a reinforcing cycle of inefficiency, overspending and operational risk.

Recognizing these interconnected challenges, organizations are beginning to adopt several emerging solutions. Simplifying toolchains through standardization, fully embracing automated execution pipelines and embedding proactive cost visibility, such as with the [shift-left FinOps ](https://thenewstack.io/why-finops-belongs-in-your-ci-cd-workflow/)approach, are all becoming essential strategies. Additionally, investing in internal upskilling and knowledge-sharing programs is helping teams close critical IaC skill gaps, enabling them to manage infrastructure efficiently, reliably and cost-effectively.

It’s time to explore practical strategies to simplify IaC tooling, fully embrace automation, integrate proactive cost management through emerging practices like adopting shift-left FinOps practices and close the IaC skills gap effectively.

**Simplifying Your IaC Tooling Landscape**
Tool sprawl isn’t just an inconvenience — it’s a fundamental obstacle to IaC success. Every additional tool or custom script introduced increases both cognitive overhead and technical debt, making systems harder to maintain, troubleshoot and scale. Simplifying the toolchain by standardizing on fewer integrated tools allows teams to reduce operational complexity and enhance maintainability.

Organizations experiencing success have increasingly standardized on a single primary IaC tool (such as Terraform or OpenTofu) complemented by essential supporting tools rather than maintaining overlapping or redundant solutions. Reducing complexity in tooling directly translates into quicker onboarding of new employees, fewer deployment errors, less troubleshooting time and greater overall reliability — aligning closely with IaC’s original goals of simplicity and consistency.

In practice, standardizing the IaC toolchain means using governed, centralized repositories that store version-controlled templates and reusable modules. It also involves enforcing unified policies and consistent tagging standards across environments, ensuring resources are deployed in predictable ways. This approach reduces configuration drift, simplifies auditability, maintainability and makes automating and integrating essential tasks such as security scanning, policy enforcement and cost control far simpler.

**Evolving to Fully Automated by Overcoming the Manual FUD**
Despite automation being central to the IaC promise, our report uncovered a surprising persistence of manual execution, with nearly one-quarter (24%) of teams still running infrastructure deployments manually from their local machines. This practice introduces significant risks: Manual deployments are error-prone, inconsistent, lack auditability and negate many of the potential benefits IaC automation offers.

Often, manual intervention persists because automation workflows are perceived as rigid, difficult to initially configure or due to lack of trust in fully automated deployments. Additionally, legacy systems and processes frequently introduce complexities that are harder to automate immediately.

Shifting fully into automated pipelines — leveraging CI/CD — is critical for operational maturity. Automation not only eliminates the inconsistencies and mistakes common in manual deployments but also enhances traceability, security and compliance. Organizations making this shift have reported faster deployment cycles, fewer outages and improved overall reliability.

To practically overcome the barriers that prevent fully automated IaC, teams can adopt incremental automation strategies. Initially, organizations might automate lower-risk environments (such as development and staging), progressively extending automation to higher-risk production deployments as confidence builds. Regular training, clear documentation and internal knowledge sharing about automation processes can also build trust and familiarity among engineers. Shifting fully into automated CI/CD pipelines eventually reduces errors, increases consistency and improves overall reliability.

**Shifting Cost Checks Left and Into IaC Workflows**
Cost management continues to challenge cloud operations, with 65% of organizations reporting increased difficulty controlling expenditures, especially as complexity grows across multicloud environments. A proactive strategy is essential, starting with a shift-left FinOps approach — embedding automated cost visibility directly into infrastructure provisioning to inform engineers immediately about financial impacts.

Yet effective cost control goes beyond proactive visibility. Organizations should also enforce systematic tagging practices, assigning ownership and project codes to resources to facilitate accurate chargebacks and cost accountability. Leveraging IaC capabilities to enforce configurations — such as auto-stopping idle instances and rightsizing resource allocations — further reduces unnecessary spend.

Incorporating automated cost estimation tools directly into IaC workflows (for instance, Terraform’s cost estimation plugins) provides visibility in pull requests, sparking crucial cost discussions before resources are provisioned. Complementing this with continuous monitoring and optimization platforms like Firefly helps detect underutilized or overpriced resources, maintaining ongoing efficiency across the entire cloud environment.

**Closing IaC Skill Gaps and the Rise of Platform Engineering**
Even the best tools and processes fall short without skilled practitioners to implement and manage them. With nearly half of organizations citing skill shortages as their top barrier, internal upskilling is no longer optional — it’s essential. Effective strategies include structured training programs, mentorship initiatives, documentation standards and community-building activities within teams.

Increasingly, leading organizations employ platform engineering to simplify developer interactions with infrastructure, reducing the cognitive load associated with IaC. By creating standardized, self-service infrastructure platforms, these teams minimize complexity, allowing developers to provision resources easily and reliably. Platform engineering teams also often serve as central hubs of best practices — closing skill gaps, simplifying the developer experience and enhancing job satisfaction.

Organizations also benefit from establishing internal “communities of practice” around IaC, using dedicated communication channels, regular meetups and collaborative coding sessions to distribute knowledge effectively. By promoting continuous learning, these communities further strengthen team capabilities and retention.

**Returning IaC to Its Original Promise**
It is possible to achieve the promise of IaC, by addressing the key issues highlighted in the State of Infrastructure as Code 2025 report, by modernizing your IaC strategy rather than offering one-off, patchwork, isolated solutions.

This includes simplifying and standardizing toolchains to reduce complexity; incrementally transitioning to fully automated CI/CD pipelines; integrating proactive cost management approaches such as shift-left FinOps and resource tagging; and strengthening internal skill sets through structured training, Platform engineering practices and communities of practice.

These steps help return IaC to its original promise — delivering simplicity, predictability and efficiency at scale. In parallel, platforms such as Firefly are built to provide a single place to manage your IaC efficiently at scale and overcome these challenges.

Read the [full report here.](https://www.firefly.ai/state-of-iac-2025)

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)