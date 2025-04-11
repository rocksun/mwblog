# GitHub’s New Security Campaigns Fix Security Debt With AI
![Featued image for: GitHub’s New Security Campaigns Fix Security Debt With AI](https://cdn.thenewstack.io/media/2025/04/f627f17e-peter-conrad-ua8pwpht1vw-unsplash-1024x698.jpg)
Photo by Peter Conrad via Unsplash.

GitHub introduced a new AI-based tool for eliminating security debt on Tuesday for its [GitHub Advanced Security and GitHub Code Security](https://github.blog/changelog/2025-03-04-introducing-github-secret-protection-and-github-code-security/) customers. Now, organizations can run [security campaigns](https://docs.github.com/en/enterprise-cloud@latest/code-security/securing-your-organization/fixing-security-alerts-at-scale/about-security-campaigns), which help identify and remediate existing [security](https://thenewstack.io/security/) problems from developers’ GitHub workflows.

“Our data shows that [security debt](https://thenewstack.io/avoiding-technical-security-debt-during-cloud-transformation/) is the biggest unaddressed risk that customers face: Historically, only 10% of lingering security debt in merged code gets addressed, meaning until today, 90% of risks did not get prioritized,” [GitHub’s](https://github.com/) Senior Product Manager [James Fletcher](https://www.linkedin.com/in/james-fletcher-1853a4159/?originalSubdomain=uk) wrote Tuesday in announcing the [general availability of security campaigns](https://github.blog/security/application-security/found-means-fixed-reduce-security-debt-at-scale-with-github-security-campaigns/) on the company’s blog. “Now, our data shows that 55% of security debt included in security campaigns is fixed.”

It relies on an AI code-scanning agent called [Copilot Autofix](https://thenewstack.io/copilot-autofix-ais-answer-to-code-vulnerability-woes/), which was released in 2023. Scans are triggered either on a schedule or upon specified events, such as pushing to a branch or opening a pull request.

## Security Campaigns Address Security Debt
Security campaigns are not just about fixing a vulnerability, [Marcelo Oliveira](https://www.linkedin.com/in/marcelogoliveira22/), GitHub’s new vice president of product, told The New Stack. Security campaigns are designed to remediate security debt that exists in code already in production.

“In most organizations, we’re talking about thousands or tens of thousands of vulnerabilities that are sitting on the backlog, and it’s humanly impossible for these organizations to fix all of these problems,” he said.

The scope means these problems tend to remain.

“We haven’t been able to really drastically help people remediate or reduce security risk,” Oliveira said. “Quarter over quarter, year after year, I would go to customers and the vulnerability trends continue to trend up into the right, instead of really improving.”

Security campaigns target these existing vulnerabilities by remediating long-standing issues from within the developer’s GitHub workflow. Security campaigns even come with predefined templates based on commonly used themes to help scope the campaign. For example, one template is [MITRE’s top 10 known exploited vulnerabilities](https://cwe.mitre.org/top25/archive/2023/2023_kev_list.html).

[GitHub’s security](https://thenewstack.io/github-rolls-out-free-secret-risk-assessment-tool/) overview also provides organizations with statistics and metrics summarizing their overall risk landscape.
“It’s not that developers don’t want to solve the problem,” Oliveira said. “It’s just a competing priority for them, so [we’re] trying to do as much of the work as we possibly can to reduce that overhead for them.”

After security campaigns, there is support within GitHub to help the [code remain clean](https://thenewstack.io/arming-developers-with-the-power-of-clean-code/) and to ensure a developer is not introducing new vulnerabilities into processes, he added.

In order to keep it that way, Oliveira said, security campaigns allow “developers and security people to collaborate on, What issues should I be fixing first, in order to reduce the risk of my applications across my organization?”

## Automating Vulnerability Remediation
Security campaigns, Oliveira said, triage and prioritize security problems into the normal software development life cycle, then create a strategy for reversing that trend.

When an application security manager creates a security campaign, they outline the set of vulnerabilities that the organization wants to remediate.

For instance, the application security manager may want to eradicate all the SQL injection vulnerabilities across an organization on applications that are exposed to the Internet. The solution allows the manager to tag repos that have any exposure to the Internet, that are in production already, and then it reveals any vulnerabilities related to SQL injection.

“It’s not that developers don’t want to solve the problem It’s just a competing priority for them, so [we’re] trying to do as much of the work as we possibly can to reduce that overhead for them.”

— Marcelo Oliveira, GitHub’s vice president of product
“They have a severity of high or critical and then this is going to filter for me everything within my organization that matches that criteria,” Oliveira said. “Now I can package all of these vulnerabilities into a campaign and dispatch this to the appropriate developers across my org — they need to [fix the vulnerability](https://thenewstack.io/root-out-vulnerabilities-in-github-as-you-merge-code-changes/).”

Once the manager has defined what the scope of vulnerabilities is for remediation, then the information is automatically sent to developers within GitHub, where they are alerted to the issue, notified of the campaign and then told what vulnerabilities they need to focus on.

When the campaign is created, Copilot Autofix automatically generates the remediation recommendations and presents the code that needs to be changed to solve the problem.

“What the developer is seeing is not only a ‘Hey, fix this’ alert,” he said. “It’s a ‘We need this alert fixed because it has been prioritized by the application security team according to this criteria.’”

Then the code runs through the [CI process](https://thenewstack.io/engineering-best-practices-of-ci-pipelines/) and is remediated through the pipeline, he said.

Security campaigns basically expand the collaboration platform to include the application security manager, Oliveira said, which allows application security managers and developers to collaborate more effectively.

He added, “We’re also doing as much as we can in terms of [automating the remediation](https://thenewstack.io/aiops-done-right-automating-remediation-and-resiliency/) of that issue.”

## Fixing Vulnerabilities Where Code Lives
Once the campaign alerts are selected and the application security manager specifies a timeline, the campaign automatically communicates the information to any developers working on relevant repos.

The remediation defined by the campaign appears as an issue to be resolved within the repository, so developers can address and manage problems just like any other feature work.

“Using Copilot Autofix to generate code suggestions for up to 1,000 code scanning alerts at a time, security campaigns help security teams take care of triage and prioritization, while you can quickly resolve issues using Autofix — without breaking your development momentum,” Fletcher wrote on the GitHub blog. “Fixing an alert becomes as easy as reviewing a diff and creating a pull request.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)