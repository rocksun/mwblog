Microsoft and its subsidiary GitHub have launched a native integration between [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) and [GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) that aims to address what one executive calls decades of accumulated security debt in enterprise codebases.

The integration, announced this week in San Francisco at the [Microsoft Ignite 2025](https://ignite.microsoft.com/en-US/home) conference and now available in public preview, connects runtime intelligence from production environments directly into developer workflows. The goal is to help organizations prioritize which vulnerabilities actually matter and use AI to fix them faster.

“Throughout my career, I’ve seen vulnerability trends going up into the right. It didn’t matter how good of a [detection engine](https://thenewstack.io/is-the-end-of-detection-based-security-here/) and how accurate our detection engine was, people just couldn’t fix things fast enough,” said [Marcelo Oliveira](https://www.linkedin.com/in/marcelogoliveira22/), VP of product management at GitHub, who has spent nearly a decade in application security. “That basically resulted in decades of accumulation of security debt into enterprise code bases.”

According to industry data, critical and high-severity vulnerabilities constitute 17.4% of security backlogs, with a mean time to remediation of 116 days, said [Andrew Flick](https://www.linkedin.com/in/andrewmflick/), senior director of developer services, languages and tools at Microsoft, in a [blog post](https://techcommunity.microsoft.com/blog/appsonazureblog/security-where-it-matters-runtime-context-and-ai-fixes-now-integrated-in-your-de/4470794). Meanwhile, applications face attacks as frequently as once every three minutes, Oliveira said.

The integration represents the first native link between runtime intelligence and developer workflows, said [Elif Algedik](https://www.linkedin.com/in/elifalgedik/), director of product marketing for cloud and AI security at Microsoft, in a [blog post](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/microsoft-defender-for-cloud-innovations-at-ignite-2025/4469386).

Organizations now build more than 500 new applications on average each year, she noted, and as code volume grows, the gap between development and security widens.

[![](https://cdn.thenewstack.io/media/2025/11/90df151e-image-1-1.png)](https://cdn.thenewstack.io/media/2025/11/90df151e-image-1-1.png)

## Bridging the DevSecOps Gap

The integration addresses a fundamental [disconnect between security and development teams](https://thenewstack.io/address-the-communication-gap-between-dev-and-security-teams/). Security teams struggle with alert fatigue, unable to distinguish real exploitable risks from theoretical ones, Oliveira said. Developers, meanwhile, lack clear prioritization signals and often spend time fixing issues that may never be exploited in production, he added.

Flick frames this as the [DevSecOps dilemma](https://thenewstack.io/reframing-devsecops-software-security-to-software-safety/). Despite a decade of improvements in detection accuracy and collaboration between security teams and developers, remediation trends have remained stagnant.

“Quarter after quarter, year after year, vulnerability counts continue to rise,” he wrote in the post about the integration.

The problem, according to Flick, comes down to three challenges: security teams drowning in alert fatigue while AI rapidly introduces new [threat vectors](https://thenewstack.io/modern-attack-methods-jeopardize-cybersecurity-strategies/) that they have little time to understand; developers lacking clear prioritization while remediation takes too long; and both teams relying on separate, nonintegrated tools that make collaboration slow and frustrating.

“Every time that I would go to a new customer, it was so frustrating to look at that curve going up into the right quarter after quarter, year after year,” Oliveira said. “And I would ask customers, ‘What is the biggest challenge for you guys?’ For them, it was always a question of prioritization. There were just too many alerts coming in. And number two, it was costly for them to fix those issues.”

The new integration works bidirectionally. When Defender for Cloud detects a vulnerability in a running workload, that runtime context flows into GitHub, showing developers whether the vulnerability is internet-facing, handling sensitive data or actually exposed in production. This is powered by what GitHub calls the Virtual Registry, which creates code-to-runtime mapping, Flick said.

Further, Flick described how this plays out in practice.

An app is live and serving thousands of customers when Defender for Cloud detects a vulnerability in an internet-facing API that handles sensitive data. In the past, this alert would age in a dashboard while developers worked on unrelated fixes because they didn’t know this was the critical one, he said. Now, a security campaign can be created in GitHub, filtering for runtime risk like internet exposure or sensitive data, notifying the developer to prioritize this issue. The developer views the issue in their workflow, understands why it matters and uses Copilot Autofix to apply an AI-suggested fix in minutes.

The Virtual Registry makes this possible by enabling teams to quickly answer key questions: Is this vulnerability running in production? Is it exposed to sensitive workloads? Do I need to act now?

“By bringing the best of Microsoft Defender for Cloud with GitHub Advanced Security, we’re being able to bring these two worlds of security and development together,” Oliveira explained. “Security leaders would always say, ‘I would love to know if this vulnerability is running somewhere. If it’s not, I don’t care. I don’t need to take an action right now.’ But if it’s running somewhere, if it’s highly exposed, and anybody on the internet can access that service, if it’s dealing with highly sensitive data, that changes completely the picture.”

## Agentic Remediation at Scale

Beyond prioritization, the integration leverages GitHub’s AI capabilities for what Oliveira calls “agentic remediation.” Using [Copilot Autofix](https://github.blog/news-insights/product-news/secure-code-more-than-three-times-faster-with-copilot-autofix/) and the GitHub Copilot coding agent, developers can create security campaigns and assign bulk vulnerability fixes to AI agents, he said.

“We allow you to go and create a campaign, and from that campaign you can assign it to Copilot,” Oliveira said. “Doesn’t matter if it’s 10 vulnerabilities or 100 vulnerabilities, Copilot can help you now go and not only deal with all the potential conflicts, the merging, creating everything into a single PR [pull request], verifying the CI pipeline, and making sure that all those tedious elements that were required from a developer now can be automated for them.”

The developer then reviews the PR rather than doing the tedious work themselves. According to GitHub, Copilot Autofix has been shown to fix 50% of alerts within PRs, with a 70% reduction in mean time to remediation. Security campaigns have seen 68% of alerts remediated.

Meanwhile, Algedik highlighted three tangible benefits the integration delivers: Teams can collaborate without friction as security teams open and track GitHub issues directly from Defender for Cloud; remediation accelerates with AI as Copilot-assisted fixes resolve vulnerabilities without breaking developer flow; and teams can prioritize what matters most by mapping runtime threats directly to their source in code.

“Security, development, and AI now move as one, finding and fixing issues faster and creating a continuous feedback loop that learns from runtime, feeds insights back into development, and redefines how secure apps and agents get built in the age of AI,” she wrote.

[![](https://cdn.thenewstack.io/media/2025/11/2e0200e1-critical-risks-ghas-1-1.png)](https://cdn.thenewstack.io/media/2025/11/2e0200e1-critical-risks-ghas-1-1.png)

Microsoft Defender for Cloud.

The approach represents a shift from what Oliveira calls the old trade-off between speed and security.

“Speed and innovation were basically a trade-off to security. If you wanted to really fix the security problems that were coming in, then they were costly. They would take time,” he said. “The fact that this is now being prevented right at the source, providing guardrails for how development actually executes, dramatically reduces this friction.”

## Embedded Prevention

The integration builds on GitHub’s Universe announcement from two weeks ago, which embedded security verification into agentic coding workflows. The GitHub Copilot coding agent now automatically checks dependencies, scans for first-party code vulnerabilities and catches hardcoded secrets before code reaches developers, he said.

“We’re not only helping you fix existing vulnerabilities, we’re also reducing the number of vulnerabilities that come into the system when the level of throughput of new code being created is increasing dramatically with all these agentic coding agent platforms,” Oliveira said.

He calls this a dual strategy: embedded prevention for new code and scaled remediation for existing vulnerabilities. “99.99999% of the code ever written already exists, and we need to really look at how do we get secure from that existing code base,” he said. “But also, how do we stay secure by ensuring that new things don’t flow into the system as well?”

## Platform vs. Bolt-On

Oliveira also noted that GitHub’s approach is fundamentally different from traditional security tools because of its integration into the development platform itself.

“I think the biggest benefit, and when I meet with customers, I’ve never been in a position as a security vendor where I go in and I have developers saying that they bought the solution because their developers wanted GitHub and security,” he said. “Application security is a team sport. If you don’t have a developer on your team, doesn’t matter how much you scream; it’s not going to change anything.”

For security teams, the integration means being able to open and track GitHub issues directly from Defender for Cloud with full context and vulnerability details. Progress is visible on both sides, allowing teams to collaborate without switching tools.

“We’re not shifting left. We’re shifting security into the platform,” Oliveira said. “We’re embedding it. Our goal here is to make security invisible by putting it into the platform and making sure that this guidance and this correction is done automatically.”

## AppSec Renaissance

Oliveira said he believes the combination of AI capabilities and platform integration represents what he calls an “AppSec Renaissance” that can fundamentally transform how application security works.

“People talk about duality of AI, right, in how AI can create challenges, or it can be the villain or the hero,” he told The New Stack. “For me, I believe that it can be a tremendous hero in this whole picture. With that notion of prevention and remediation from an application security perspective, I think we can really create what I started to call the AppSec Renaissance.”

The integration is available now in public preview.

For organizations building cloud native applications, the integration will help protect code to cloud without slowing down development.

“This velocity of what these coding agents are giving us is an opportunity to avoid those trade-offs,” Oliveira said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)