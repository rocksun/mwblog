# 6 Actionable IaC Tips for Cloud Practitioners in 2025
![Featued image for: 6 Actionable IaC Tips for Cloud Practitioners in 2025](https://cdn.thenewstack.io/media/2025/05/ff9e280c-6-iac-tips-cloud-practitioners-1024x576.jpg)
If you’re managing cloud infrastructure today, you’re likely drowning in complexity — and lots of it. According to our latest State of Infrastructure as Code (IaC) Report, a staggering 65% of practitioners report that cloud complexity is trending upward over the last two years, with another 27% feeling it’s just as difficult as before.

IaC is simply [not getting any easier](https://thenewstack.io/iac-is-too-complicated-wheres-that-easy-button), but it’s not for lack of trying.

The hard truth? Most teams are still playing catch-up with [IaC adoption](https://thenewstack.io/introduction-to-infrastructure-as-code/). Here’s what we’re facing, and how to win in the face of challenges.

**The Harsh Reality of Infrastructure as Code in 2025**
The [State of Infrastructure as Code in 2025](https://www.firefly.ai/state-of-iac-2025) report is a mirror reflecting the reality of our industry. It reveals a landscape riddled with contradictions: widespread IaC adoption masking shockingly low maturity, [Terraform’s iron grip](https://thenewstack.io/terraform-and-the-tooling-multiverse-in-the-future-of-iac) slowly loosening and the tantalizing promise of AI remaining largely untapped by most teams. Multicloud is here, but almost no one is equipped to handle it effectively.

But this revelation shouldn’t just feel like a gentle nudge. It’s a full-blown intervention for DevOps and platform engineering leaders. If you’re clinging to outdated assumptions and half-baked implementations, this report is your wake-up call.

**If you’re trying to figure out the right IaC approach for your organization, join us on June 17 at 11:30 a.m. ET | 8:30 a.m. PT, for a special online event, “ Inside the 2025 State of IaC: Tools, Trends, and Tactical Solutions” with Firefly CEO Ido Neeman.**
Here’s a look at the biggest lessons learned from the 2025 report.

**Terraform’s reign faces challenges.**While Terraform still holds 62% market share, only 47% of practitioners plan to continue using it in the future.[OpenTofu usage is surging](https://thenewstack.io/will-opentofu-dethrone-terraform-in-iac), with 12% of respondents currently using it and 27% planning to adopt it. About 5% have already completed migrations from Terraform to OpenTofu, with another 6% planning to make the switch in the next year.**Automation is becoming the standard.**The use of CI/CD or GitOps pipelines for infrastructure deployment has increased to 59% in 2025, while manual CLI runs dropped from 30% to 24% since last year. DevOps teams overwhelmingly ranked automation and GitOps-style delivery as their #1 IaC pipeline capability.**Drift remains a critical issue.**Only a minority (8%) have automated drift remediation, with 40% reporting it takes days to weeks to fix[configuration drift](https://thenewstack.io/chaos-under-control-addressing-cloud-infrastructure-drift). Worse? Seventeen percent have no drift detection process in place whatsoever.**AI adoption is cautious, but growing and full of potential.**About 17% of teams today are already using AI-driven capabilities in cloud operations, with another 41% planning to adopt or actively exploring solutions. When asked which AI capabilities would be most valuable for IaC, popular choices included automated policy compliance and intelligent drift detection. This indicates a wishlist where AI could help, even if actual adoption is nascent.
**Cloud Practitioner Tips: Turning Insights Into Action**
Our annual pulse check on IaC adoption revealed several significant trends, and they’re pointing toward clear areas of opportunity. Small but impactful shifts in DevOps and platform engineering teams’ ways of working can help them get ahead of the key trends on the rise and the top challenges they still face.

Let’s dive into a few actionable strategies that DevOps and platform engineering teams can embrace right away.

### 1. Conquer Multicloud Chaos: Standardize Across Providers
Multicloud environments are here to stay, but they bring added complexity that requires proactive planning. And because multicloud organizations face higher management overhead, planning ahead can help mitigate risks associated with acquisitions or shadow IT initiatives. Teams should:

**Standardize IaC tooling across clouds:**Leverage Terraform providers or similar frameworks to create unified workflows for[AWS](https://aws.amazon.com/?utm_content=inline+mention), Azure and Google Cloud Platform.**Implement cross-cloud tagging and monitoring:**Use consistent tags across all resources to simplify governance and cost analysis.**Design processes with multicloud in mind:**Even if you’re currently single-cloud, prepare for future expansion by building modular IaC templates that can adapt to multiple providers.
### 2. Gradually Codify Legacy Infrastructure
Legacy resources often remain outside IaC control due to complexity or lack of time. The 2025 survey shows that 61% of teams are retrofitting legacy infrastructure piece by piece. But an amended approach can reduce drift risk and ensure that version control benefits extend to older systems.

**Adopt an incremental retrofit strategy:**Capture legacy resources in code during updates or migrations.**Avoid big-bang migrations:**Integrate legacy resources organically over time to reduce disruption.**Prioritize high-risk resources:**Focus on codifying infrastructure tied to compliance or disaster recovery first.
### 3. Invest in Skills Development
Skills gaps remain the #1 challenge for teams adopting IaC. Thankfully, upskilling not only addresses talent shortages but also improves retention by offering career growth opportunities, a key factor in team success. Some great ways to do it?

**Provide formal training:**Host workshops on Terraform, Pulumi or OpenTofu to upskill your team.**Encourage knowledge sharing:**Create Slack channels or regular syncs where engineers can discuss IaC tips and challenges.**Develop reusable modules:**Build internal libraries of standardized templates to simplify onboarding for new engineers.
### 4. Simplify Your Toolchain
Fragmented tools increase cognitive load and deployment errors. But teams with leaner processes report stable or decreasing management effort, and simplifying your toolchain frees up time for higher-value engineering tasks.

**Consolidate overlapping frameworks:**Standardize on one primary IaC engine and one delivery pipeline wherever possible.**Streamline CI/CD pipelines:**Use GitOps-style workflows with minimal manual steps.
### 5. Deploy Like a Pro: Implement Automated GitOps Pipelines
Automation is the gold standard for modern pipelines. It minimizes manual intervention and ensures reliable deployments across environments — a top priority named by 59% of respondents. To get it right:

**Adopt pull request-driven workflows:**Ensure changes are reviewed before deployment using automated plan/apply processes.**Implement GitOps practices:**Use declarative configurations stored in Git repositories as the single source of truth.**Automate drift remediation:**Invest in tools that detect and resolve drift in real time to maintain infrastructure consistency.
### 6. Harness AI’s Power Early (Before It’s Just a Point of Parity)
AI offers transformative potential for cloud governance. Plus, early adopters gain competitive advantages as AI technologies mature, and investing now positions your team at the forefront of innovation.

Leading teams are the ones that:

**Experiment with intelligent tools:**Use AI for policy enforcement, cost optimization and drift detection.**Integrate AI incrementally:**Start with small-scale applications like compliance checks before scaling up.**Focus on actionable insights:**Choose AI solutions that provide clear recommendations rather than abstract predictions.
**Close the IaC Gap: Why Waiting Costs More Than Action**
The gap between IaC leaders and those trailing behind is widening at an alarming rate. With cloud complexity only increasing and security risks growing alongside it, waiting to mature your IaC practice means falling further behind with each passing quarter. The competitive advantage is about shifting from just adoption to mastery and automation.

Incremental improvements in your IaC approach aren’t just nice-to-haves — they’re business imperatives. Organizations that proactively manage drift, implement automated pipelines and standardize their multicloud operations stand to see substantial benefits: faster deployments, fewer outages and more resilient infrastructure. And even small steps can yield significant returns.

Your next move is what matters most. Download the [2025 State of IaC Report](https://www.firefly.ai/state-of-iac-2025) to benchmark your organization against industry peers and start mapping out your path to IaC maturity.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)