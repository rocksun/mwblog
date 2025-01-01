# What 2024’s Data Told Us About How Developers Work Now
![Featued image for: What 2024’s Data Told Us About How Developers Work Now](https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png)
2024 saw The New Stack report on a variety of survey-based research about software development. Here are the takeaways we think are most relevant to you as you plan for 2025.

[Platform Engineering and Developer Platforms](#platform-engineering)
- Platform engineers are focused on infrastructure provisioning, which can be problematic because of the diversity of platforms being managed.
- Even though self-service increases productivity for developer teams, too many platform teams are failing to collect and demonstrate metrics of success.
[Open Source](#open-source)
- Paid maintainers keep code safer.
- Maintainers worry about contributions from AI and unknown developers.
[AI and Developers](#ai)
- Time savings and increased productivity, not code quality, are why developers are using AI.
- Led by younger, inexperienced developers, AI tools have rapidly been adopted for use within the development process.
[GitHub Copilot](https://thenewstack.io/a-developer-health-check-on-github-copilot-and-ai-assistants/)did not experience mass adoption.
[Hiring and Careers](#careers)
- Personal job security is stronger than would be expected based on developers’ generalized anxiety.
- Developer salaries and wages have been constrained.
## Programming Languages
[Darryl K. Taft’s](https://thenewstack.io/author/darryl-taft/)post from Dec. 28, “[Language Wars 2024: Python Leads, Java Maintains, Rust Rises](https://thenewstack.io/language-wars-2024-python-leads-java-maintains-rust-rises/),” provides a good summary of this year’s findings.- Unlike many other publications, The New Stack conducted its own independent analysis of the raw data collected for 2024’s
[Stack Overflow](https://stackoverflow.com/)“[Developer Survey](https://thenewstack.io/salary-pressures-not-ai-vex-developers-says-stack-overflow/)” and the[Jetbrains](https://www.jetbrains.com/)[“State of Developer Ecosystem Report.”](https://thenewstack.io/developers-testing-more-jetbrains-study-finds/)
[Other Noteworthy Findings](#other-findings)
- Not all companies are leaving the cloud.
- Customer-facing incidents are on the rise.
## Platform Engineering and Developer Platforms
While not a portmanteau like [DevOps](https://roadmap.sh/devops), [platform engineering](https://thenewstack.io/platform-engineering/) has emerged as the discipline in which the goals of development and operations converge.

Throughout 2024 we reported on more than four survey-based reports that provided insights into platform engineering and internal developer platforms (IDPs). They demonstrated that the vast majority of enterprises have adopted platform engineering, even though they may not have a formal team with that name.

Standardizing infrastructure provisioning and consumption of IDPs is a main focus of 68% platform teams. Improving developers’ experience and productivity with IDPs follows closely as focal points, per the latest version of the “State of Platform Engineering Report.” by Gitpod and [Humanitec](https://humanitec.com/?utm_content=inline+mention).

Companies that adopt a platform for the first time overwhelmingly receive a positive return on investment, but many [platform teams do not know how to measure success](https://thenewstack.io/the-2024-state-of-platform-engineering-fledgling-at-best/). According to the same “State of Platform Engineering” study, only 43% of platform teams surveyed self-described their feedback mechanisms as “ad-hoc" or “inconsistent.”

Worse, 45% of platform teams don’t measure anything at all, while another 26% are collecting performance data but not actually analyzing it.

Even among organizations that are looking at productivity, the jury is still out on how to gauge the success of platform teams. Indeed, the latest DORA report, published by [Google Cloud](https://cloud.google.com/?utm_content=inline+mention), found that [throughput and change stability metrics declined as the maturity of platform engineering programs mature](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/). On the other hand, organizations that use IDPs see higher levels of individual and team productivity, likely due to the self-service made available via an IDP.

Looking forward, we anticipate that organizations will face the question about how many platforms are too many. The issue is coming to a head because 75% of those surveyed for the “2024 State of DevOps Report” from [Puppet by Perforce](https://puppet.com/?utm_content=inline+mention) said they are using at least three internal self-service platforms, which is significantly more than the [59% that had three or more platforms in the previous study](https://thenewstack.io/platform-engineering-more-teams-now-running-3-or-more-idps/).

With at least basic acceptance in the enterprise, platform engineering should see more resources poured into it. A survey by [Rafay Systems](https://rafay.co?utm_content=inline+mention) found that 69% of organizations with platform teams expected staffing for these teams to increase by at least 25% through 2024. However, a challenge facing companies, according to the Rafay report, is that [only 47% of platform teams actually have a budget that is separate from IT](https://thenewstack.io/are-shared-platforms-too-restrictive-a-new-report-says-yes/).

Perhaps platform engineering will divert money dedicated to the purchase of [Infrastructure as Code (IaC)](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/) and CI/CD tools. Indeed, as shown in the [chart above](#datawrapper-chart-25a6c), many platform teams are focused on implementing IaC or building platforms on top of CI/CD systems.

Platform teams may be able to enforce consistent configurations across different environments, but they are also challenged because of the proliferation of IaC tools and frameworks. In fact, 54% of those surveyed for “[Stacked Up 2024: The IaC Maturity Report](https://stackgen.com/2024-stacked-up-the-iac-maturity-report-stackgen),” by [StackGen](https://stackgen.com/?utm_content=inline+mention), face challenges with IaC because multiple tools result in steep learning curves and compatibility issues. Determining [how many IaC frameworks can be managed effectively](https://thenewstack.io/terraform-and-the-tooling-multiverse-in-the-future-of-iac/) will continue to be an issue in 2025.

### Kubernetes and Platform Engineering
Platforms run on top of CI/CD systems are often running on top of Kubernetes, which is why Rafay Systems’ survey of platform teams focused on Kubernetes users. Both topics are faced with complexity problems because of a proliferation of tools.

In fact, according to a 2024 survey by [Spectro Cloud](https://www.spectrocloud.com/?utm_content=inline+mention), 48% of Kubernetes users found it [difficult to decide which stack components](https://thenewstack.io/kubernetes-48-of-users-struggle-with-tool-choice/) to use from the broad cloud native ecosystem. That figure shot up from the 29% who said the same in Spectro Cloud’s 2023 report.

### Best Platform Engineering Reports of 2024
- “
[State of Platform Engineering Report: Volume 3](https://platformengineering.org/state-of-platform-engineering-vol-3)” [VMware by Broadcom's](https://tanzu.vmware.com?utm_content=inline+mention)“[State of Cloud Native App Platforms 2024](https://go-vmware.broadcom.com/2024-State-of-Cloud-Native-App-Platforms)”- DORA's
[“Accelerate State of DevOps](https://dora.dev/research/2024/dora-report/)” - Puppet by Perforce's “
[2024 State of DevOps Report: The Evolution of Platform Engineering](https://www.puppet.com/blog/state-devops-report-2024)” - Rafay's “
[The Pulse of Enterprise Platform Teams: Cloud, Kubernetes and AI](https://rafay.co/the-pulse-of-the-enterprise-platform-team-cloud-kubernetes-and-ai/)” - Spectro Cloud's “
[2024 State of Production Kubernetes](https://info.spectrocloud.com/2024-state-of-production-kubernetes)”
## Open Source
Funding, or the lack of it, for open source maintainers continues to endanger open source software.

2024 saw a proliferation of software bills of materials (SBOMs) and tools that automate dependency management and can reduce some security concerns. However, open source maintainers just don’t have enough time to prioritize security, especially as they are also facing an influx of new threats generated by AI-based coding tools.

Among the key findings:

[Security needs are solved best by paying maintainers](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/). Developers who are compensated for their time working on open source are more than 50% more likely to follow best practices that impact a project’s security posture. That’s according to[Tidelift’s](https://tidelift.com/?utm_content=inline+mention)“[State of the Open Source Maintainer](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/),” which also looked at quality and security concerns about pull requests coming from unknown contributors and generated by artificial intelligence.- Maintainers worry about contributions from AI and unknown developers. The Tidelift report found that because of the
[Linux xz utils backdoor](https://thenewstack.io/linux-xz-and-the-great-flaws-in-open-source/)that was discovered in March, two-thirds of maintainers are less trusting than they used to be of pull requests from non-maintainers of their project. Even more troubling, 64% said they would be less likely to review and accept project contributions that they knew were created with AI-based tools.
In 2025, we expect unpaid volunteers to continue struggling to follow many practices that are becoming increasingly mandatory to comply with new government regulations.

### Other Noteworthy Research on Open Source
- OpenLogic's “
[2024 State of Open Source Report](https://www.openlogic.com/resources/state-of-open-source-report)” - The Linux Foundation's “
[Census III of Free and Open Source Software](https://www.linuxfoundation.org/research/census-iii)”
## AI and Developers
**Time savings and increased productivity, not code quality, are why developers are using AI.**
- Among developers who regularly use an AI tool for coding and other development-related activities, 85% say these types of tools make them perform their job faster than before. That’s according to Jetbrains’ “
[State of Developer Ecosystem Report](https://www.jetbrains.com/lp/devecosystem-2024/).” Much of the time savings are incremental, but 46% said they saved at least two hours a week due to these tools. - In contrast, only 23% say these tools actually improve the quality of the code and solutions being created. This finding should dampen the optimism reported by a
[2024 GitHub survey](https://github.blog/news-insights/research/survey-ai-wave-grows/), which found 90% of U.S. developers claiming that using AI-coding tools increased their code quality. - Overall, the Jetbrains study found that 65% said they spend more than half of their work time coding, which is up from 57% in 2023. In the upcoming year we hope to see if this trend continues and can be linked directly to the use of AI coding tools
**Led by younger, inexperienced developers, AI tools have rapidly been adopted for use within the development process.**
- According to
[Stack Overflow’s “2024 Developer Survey](https://survey.stackoverflow.co/2024/),” younger developers, those with less experience and those living in countries such as India and Brazil are more likely to use and trust AI. Seventy-one percent of developers with less than five years of experience reported using AI tools in their development process, as compared to 49% of developers with 20 years of experience coding.
**GitHub Copilot did not experience mass adoption.**
- GitHub Copilot was used by 41% of respondents in the last 12 months, down from 55% when the same question was asked in 2023 in the “StackOverflow Developer Survey.” We believe the decline is based on a changing perception of the Copilot product.
- Only 26% of developers regularly use GitHub Copilot for coding and other development activities, according to Jetbrains’ “
[State of Developer Ecosystem Report](https://www.jetbrains.com/lp/devecosystem-2024/),” although another 14% have previously tried using it. That compares to 49% that regularly use ChatGPT for coding purposes and another 20% that had previously tried it.
## Hiring and Careers
**Personal job security is stronger than would be expected based on developers’ generalized anxiety.**
- Overall, 67% of respondents feel secure in their current job, while 11% report feeling insecure, according to Jetbrains' “
[State of Developer Ecosystem Report 2024](https://www.jetbrains.com/lp/devecosystem-2024/).” - In that same study, 46% said the current job market for software developers in their city or area is challenging, while 30% said the hiring outlook is favorable.
[Most employers added jobs or kept the status quo in 2023](https://thenewstack.io/tech-hiring-most-employers-added-jobs-or-kept-the-status-quo-in-2023/), according to a Linux Foundation report.
**Developer salaries and wages have been constrained.**
- The median annual
[salary declined significantly](https://thenewstack.io/salary-pressures-not-ai-vex-developers-says-stack-overflow/)among respondents to[Stack Overflow’s “2024 Developer Survey](https://survey.stackoverflow.co/2024/).” For example, the average full-stack developer’s median 2024 salary fell 11% compared to the previous year, to $63,333. - Even if the average or mean salary did not actually decline, research from
[ADP indicates developer salaries did not increase](https://www.adpresearch.com/the-rise-and-fall-of-the-software-developer/)as much as many other professions.
### Other Noteworthy Research on Tech Jobs and Careers
- The Linux Foundation's
[“2024 State of Tech Talent Report](https://www.linuxfoundation.org/research/open-source-jobs-report-2024?hsLang=en)” - Dice's “
[2024 Tech Salary Satisfaction Report'](https://www.dice.com/recruiting/ebooks/dice-tech-salary-report/salary-satisfaction.html)”
## Other Noteworthy Findings
- Not all companies are leaving the cloud. While some companies are moving workloads on-premises from public clouds, news of massive cloud repatriation is overblown. In fact,
[cloud migrations were more likely in 2024](https://thenewstack.io/cloud-migrations-pick-up-the-pace-in-2024/)than before. According to[Flexera’s](https://www.flexera.com/)["2024 State of the Cloud Report](https://info.flexera.com/CM-REPORT-State-of-the-Cloud)," 58% of those surveyed said they were planning to migrate more workloads to the cloud in 2024, up from 44% in 2023. [Customer-facing incidents are on the rise](https://thenewstack.io/customer-facing-incidents-on-the-rise-it-leaders-say/). Fifty-nine percent of IT leaders said they saw more incidents that affected customers than in the previous year, according to a[June survey](https://www.pagerduty.com/resources/learn/cost-of-downtime/)from[PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention). Furthermore, survey participants said the number of incidents increased by 43%. Despite this trend, 69% said their organization is not investing in reducing such incidents.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)