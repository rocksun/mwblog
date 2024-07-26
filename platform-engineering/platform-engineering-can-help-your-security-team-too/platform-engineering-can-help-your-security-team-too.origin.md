# Platform Engineering Can Help Your Security Team, Too
![Featued image for: Platform Engineering Can Help Your Security Team, Too](https://cdn.thenewstack.io/media/2024/07/d951d55c-platform-engineering-can-help-your-security-team-too-2-1024x576.jpg)
You’re notified of a new critical vulnerability in a popular [open source project](https://thenewstack.io/a-guide-to-open-source-software-security/). The package is shipped with all the most popular [Linux distributions](https://thenewstack.io/choosing-a-linux-distribution/). It’s in the base image you use to build your [containers](https://thenewstack.io/containers/). The vulnerability is deployed in every single [microservice](https://thenewstack.io/microservices/) you run. What do you do next? Do you have [a plan](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/)?

If only we had a team that excelled at automating the software development life cycle, provided developer-friendly tools for continuously shipping updates, and who could select and validate the open source building blocks your development team needs to run their applications.

If only we had [platform engineering](https://thenewstack.io/platform-engineering/).

Platform engineering is supposed to solve a lot of the friction, delays and interruptions that developers face. However, my own real-world experience as a product director in cybersecurity taught me that platform engineering can also improve an organization’s security.

In October 2022 I was involved in my first [Zero Day](https://thenewstack.io/zero-day-vulnerabilities-a-beginners-guide/) response. OpenSSL notified the world that it had discovered a critical vulnerability in versions 3.0.0 – 3.0.6 of OpenSSL. There was no debate — this advisory required an urgent, organized response.

Not only is OpenSSL packaged with most Linux distributions, but it is also the software that handles the encryption of network connections. We didn’t know the nature of the vulnerability when we started our preparation, but we knew that the potential impact was severe.

We braced ourselves for another [Heartbleed](https://nvd.nist.gov/vuln/detail/cve-2014-0160), the vulnerability [discovered in 2014 in the OpenSSL cryptographic software library](https://thenewstack.io/vulnerabilities-versus-intentionally-malicious-software-components/), which affected a massive number of web servers.

We needed to identify where we were running OpenSSL in production and make a plan to patch the vulnerability. Our microservices were deployed as containers with a Linux distribution baked into each container. We rapidly discovered that every single production service was impacted. Take a deep breath. OK, what next?

With the blast radius identified we then had to prepare to patch, and patch quickly! On this occasion, the remediation process was to update our container-based images.

To do this we had to identify every dockerfile for every service and ensure the base image in the `FROM:`
line was updated. Each container would need to be rebuilt and redeployed through our [CI/CD](https://thenewstack.io/ci-cd/) pipelines and into production. Hundreds of services, hundreds of [dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/), hundreds of updates, hundreds of redeployments … hundreds of people involved.

CI and CD processes were automated but unfortunately, base image upgrades were not. We needed every development team to engage in the response. Some teams had just a handful of services, but others had a lot more. It wasn’t a complicated process but it disrupted hundreds of developers, with the inevitable cost of context switching, communication overhead and validation.

## Building Empathy for the Security Team
I tell this story a lot, even though the Critical categorization of the vulnerability was downgraded to High upon disclosure on Nov. 1. ([CVE-2022-3602](https://nvd.nist.gov/vuln/detail/CVE-2022-3602) and [CVE-2022-3786](https://nvd.nist.gov/vuln/detail/CVE-2022-3786), if you’re interested!

I tell this story because until that day I had resisted [“DevSecOps”](https://thenewstack.io/ebooks/devsecops/best-of-devsecops-trends-in-cloud-native-security-practices/) as a separate thing. I believed that “DevOps has always included security” and “My platform engineering team is building security in.” But I had never lived a day in the life of the security team. I lacked empathy for the security team.

Like many other platform engineering leaders, I prioritized [developer experience (DevEx)](https://thenewstack.io/why-do-developers-lose-1-day-a-week-to-inefficiencies/). I focussed on productivity and developer friction when I spoke about the need to build a [Platform as a Product](https://thenewstack.io/platform-as-a-product-in-4-steps/) (PaaS). My team of platform product managers would conduct user interviews with developers, and then manage security like stakeholders on the peripherals. We didn’t consider security as users of the product.

The return on investment (ROI) of security automation is easy to calculate in terms of “cost of response.” But the real cost of the next Zero Day vulnerability might not be limited to disruption and lost time. Those vulnerabilities could be exploited, leaving your systems open to hackers and doing irreparable reputational damage to your company.

Marc Cluet, executive director of core platform engineering for a global financial services organization (and organizer of [London DevOps ](https://www.meetup.com/london-devops/)for a decade) has always advocated for security as part of the solution.

“As someone who has experience working in highly regulated environments, security has always been a part of the DevOps transformation initiatives I have been a part of,” Cluet told The New Stack in an online interview. “The security processes and solutions you build will need to meet the needs of regulators and the organization’s many different teams including development, operations, security, audit, compliance, governance, etc.”

[“Shifting left”](https://thenewstack.io/the-limits-of-shift-left-whats-next-for-developer-security/) has been a mantra of the DevOps movement for over a decade. But the temptation with this philosophy is to delegate security to the development teams without consideration of what they need to be successful.
[Andy Burgin](https://www.linkedin.com/in/andyburgin), a principal platform engineer in the gambling industry, warned against this in an online interview with The New Stack: “If you use ‘shifting left; as a way to make work/responsibility/accountability someone else’s problem under the banner of ‘empowering,’ you’re completely misusing the term.
“Having tooling/training and above all commitment over compliance in place is far better than simply YOLOing things you don’t want to have to deal with anymore at another team. Socio-technological systems are not a playground for a game of ownership tig.”

## Consider the ‘Security Experience’
When we focus on the outcomes we want to drive by “shifting left,” the conversation changes. We want to prevent and resolve more security issues earlier in the development process, ideally before they are ever deployed to production. We don’t necessarily have to delegate all of that work to the development team.

To ensure you don’t introduce more friction in the development process, you need to take a highly automated approach, informed by the user needs of security teams alongside the needs of developers.

The platform engineering community is thriving and more teams are adopting a Platform as a Product approach for their [internal developer platforms (IDPs)](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) — but often, teams are making the same mistakes I made. They see security as a stakeholder and not as a user of the platform. To succeed, we must take a user-centric approach to both developer experience and security experience.

If you’re part of a platform engineering team, I urge you to conduct user research with your colleagues in security. Ask them what they need from your IDP. Ask them how you can help make their jobs easier.

Security teams need visibility of the [software development life cycle](https://thenewstack.io/ebooks/security/a-blueprint-for-supply-chain-security/) from code to production. They need application context to assess risk and respond appropriately. They need both proactive prevention and reactive incident response to be highly automated.

Security teams value feedback loops to measure their success; Are we getting better at this? What is our mean time to repair (MTTR) for a new critical common vulnerability and exposure (CVE)? Are developers using our security tooling correctly? Where do we have blind spots? What security education do developers need?

Who better to deliver these outcomes than the platform engineering team?

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)