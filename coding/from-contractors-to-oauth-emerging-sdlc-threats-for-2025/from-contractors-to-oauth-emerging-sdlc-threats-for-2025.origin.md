# From Contractors to OAuth: Emerging SDLC Threats for 2025
![Featued image for: From Contractors to OAuth: Emerging SDLC Threats for 2025](https://cdn.thenewstack.io/media/2024/11/8da7cd41-david-valentine-e6woc_dm19y-unsplash-1024x683.jpg)
[David Valentine](https://unsplash.com/@thephotochad?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-close-up-of-a-black-and-white-photo-of-a-compass-E6woC_DM19Y?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
With every new developer tool, imported OS package, or service account, the [software development lifecycle](https://thenewstack.io/software-development/) (SDLC) attack surface expands. A growing reliance on myriad [AI pipeline tools](https://thenewstack.io/using-ai-for-devops-what-developers-and-ops-need-to-know/) to govern code review and deployment has also made it more challenging to secure the SDLC.

In 2025, attackers won’t target applications directly but will focus on vulnerabilities within the development process. Securing a fully compiled application in the cloud fundamentally differs from protecting its components during development. I expect the SDLC will be the attack surface of choice, enabling adversaries to infiltrate applications before they reach their publicly available environment.

The future of SDLC security will be defined by multilayered threats that target every phase of development. These threats require approaches that anticipate vulnerabilities, from poorly secured contractor pipelines to phishing schemes targeting developers. Organizations must be prepared to tackle these threats head-on or risk devastating breaches.

**The Evolution of Attacks on the SDLC**
Attackers don’t deserve any kind of credit; if anything, they are innovative. They are highly motivated to find patterns and weaknesses to earn clout and money. Attackers are definitely aware if *we *know smaller or isolated gaps that could be used against us.

These weak points—whether from poor configurations, over-provisioned access, or open source dependencies — interact to create larger, more dangerous exploits. A secret leak of a JFrog service account token, for example, combined with poor permission management, could give attackers the access they need to escalate into a much larger breach.

While open source code scanning tools can detect some of these issues, they fall short of providing complete visibility into the scope of potential threats. Most Software Composition Analysis (SCA) tools don’t reveal who imported a vulnerable package, when it was added, or how far it has spread through the repository. Without this critical context, organizations risk missing the bigger picture.

The traditional approach of [managing individual vulnerabilities](https://thenewstack.io/we-need-to-rethink-risk-in-vulnerability-management/) in isolation must give way to a more holistic strategy that accounts for the interconnected nature of modern software ecosystems. Just as a sports team studies its rivals to stay one step ahead, organizations must be aware of the strategies attackers will likely employ in 2025 to safeguard their systems.

Let’s examine three key plays attackers will likely use that security leaders should be vigilant about in the coming year.

**Play 1: Poor Entitlements and Configurations for Contracted Developers**
Outsourcing software development is common practice but opens the door to significant security risks when not properly managed. These outsourced operations lack the same stringent security measures applied to internal teams, creating blind spots that attackers can easily leverage. A common vulnerability in this scenario is the over-provisioning of access rights. For example, a contractor might be granted access to far more [assets in a code repository than needed](https://thenewstack.io/why-infrastructure-as-code-needs-cloud-asset-management/) to do their job. The contractor is likely prolific and doing work for several clients, so they’d be a probable candidate for an attacker to find ways to access their asset logins. An entire repository environment could be compromised if their clients do not enforce proper identity-based entitlement management.

Poorly configured CI/CD pipelines are another critical weakness. When organizations outsource software development, they often have little visibility into the security practices of their contractors’ environments. Attackers can exploit poorly configured pipelines to access source code or manipulate [software delivery](https://thenewstack.io/stop-blaming-regulation-for-poor-software-delivery-performance/) processes. By targeting contractors with weak CI/CD practices, attackers can enter systems that should otherwise be protected, leveraging the outsourced code as a Trojan horse to penetrate deeper into the organization.

As organizations rely more on third-party developers, monitoring and controlling contractor entitlements and configurations is essential.

**Play 2: Leveraging OAuth Phishing**
Regarding the SDLC, attackers will likely increase [OAuth phishing](https://www.bleepingcomputer.com/news/security/gitloker-attacks-abuse-github-notifications-to-push-malicious-oauth-apps/) attempts to target developers, tricking them into authorizing access to sensitive repositories. OAuth, an open-standard authorization protocol, allows users to log in to platforms like GitHub or Jenkins without directly entering their credentials. This tactic is especially effective on mobile devices, where design discrepancies that might alert users to a threat are more complex to notice.

The attacker captures the developer’s credentials through a fraudulent OAuth request and gains unauthorized access to critical systems. Developers, particularly those early in their careers, may unknowingly provide attackers with credentials, believing they’re responding to a legitimate inquiry.

Preventing OAuth phishing can be difficult because it exploits user behavior rather than traditional technical vulnerabilities. While phishing training is essential, the best defense is limiting the damage attackers can cause if they gain access. By restricting developer entitlements to only what is necessary for their role, organizations can reduce the impact of a compromised account and prevent broader system breaches.

**Play 3: Sniffing Out Mismanaged Teams**
The most catastrophic SDLC security breaches in 2025 may not stem from technical vulnerabilities but from poorly managed development teams. Most engineering managers are paid to push products, so security is often a secondary concern. This dynamic has left most of the industry without a clear strategy for assessing team-based risk or identifying managers who aren’t adequately overseeing their SDLC assets. As a result, attackers will increasingly seek out small, mismanaged teams where this oversight is lacking. Such teams often operate with over-provisioned access rights, outdated security practices, and inconsistent accountability, making them prime targets for threat actors.

The risk is amplified when several overprivileged developers are concentrated on the same project. A single team with lax management, working with poorly configured CI/CD pipelines or outdated dependencies, can create a significant breach in an otherwise secure organization. Attackers will zero in on these teams, knowing that a consolidated weak point is easier to exploit than scattered, individual vulnerabilities.

To mitigate these risks, security leaders must monitor SDLC security by team, manager, and project. Accountability at the management level and stronger oversight will help organizations reduce the chances of a single, mismanaged team becoming the entry point for attack.

**Preparing for Game Time **
The attack strategies outlined here represent just a few of the multi-vector threats that organizations will face more of in 2025. Addressing these challenges will require a comprehensive approach beyond technical solutions, incorporating strong oversight and cultural change within development teams.

For security leaders, the plan is clear: anticipate evolving threats and strengthen defenses across the SDLC. By implementing tighter access controls, improving pipeline security, and fostering a culture of accountability, organizations can stay one step ahead of attackers and protect their systems from catastrophic breaches.

*This article is part of The New Stack’s contributor network. Have insights on the latest challenges and innovations affecting developers? We’d love to hear from you. Become a contributor and share your expertise by filling out this form or emailing Matt Burns at mattburns@thenewstack.io.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)