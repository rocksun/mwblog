# What Platform Engineering Meant for Adidas’s SREs
![Featued image for: What Platform Engineering Meant for Adidas’s SREs](https://cdn.thenewstack.io/media/2024/10/bcdf2973-what-platform-engineering-meant-for-adidass-sres-1024x576.jpg)
Every second counts in e-commerce. So when the global sportswear company Adidas went from less than 3,000 to 29,000 requests per second last Black Friday, that translates to a tenfold increase in orders. If the website can handle it.

A few months prior, the site reliability engineering [(SRE)](https://thenewstack.io/sre-vs-platform-engineer-cant-we-all-just-get-along/) team worked with tech leads, system architects and business to orchestrate a[ platform engineering](https://thenewstack.io/platform-engineering/) transformation that modernized the Adidas architecture from monolithic to microservices. This should’ve enabled scalability.

But when the website’s ability to process coupons went down, this new complexity brought its own challenges — all while under the constant threat of sneaker bots (bots that buy sneakers for resale). At[ DevOpsDays London](https://devopsdays.org/events/2024-london/) in September, the SRE team shared Adidas’s journey of platform engineering, [observability](https://thenewstack.io/observability/),[ security](https://thenewstack.io/security/) and [microservices](https://thenewstack.io/microservices/).

## The Cost of a Monolithic Pace
When[ Andreia Otto](https://www.linkedin.com/in/andreia-otto/), senior director of software engineering for SRE and operations, joined Adidas seven years ago, the company’s software developers had a six-week release cycle.

“The development team was working during six weeks and then after that, we had a one-day call with so many people to go through all the changes, to go through everything that would be live,” she told the DevOpsDays audience. “It was throwing the ball to the other side. Development and operations were really separated.”

Also, infrastructure couldn’t scale in response to demand. The e-commerce team needed to increase order throughput for popular sneaker drops. A couple of years ago, Adidas ran a campaign that had to be extended by three days because so much throttling was needed in order to sell the in-demand stock.

It became clear that a move to microservices was essential to save time and money. Which it did.

“This year, we had a similar campaign that we could run in a couple of hours,” Otto said. “We mobilized way less people in way less time. It’s much cheaper for the company to sell, reducing operational costs and vendor dependency.”

The Adidas SRE team also aimed to reduce operational costs and vendor dependency by using a platform engineering approach to facilitate the move from monolithic to microservices architecture.

The team went from being able to plan for three days for their platform to accept 4,000 orders per minute to rolling out a release in a matter of hours that could accept 40,000 orders per minute.

“We had a big monolith serving everything from frontend to backend,” Otto said. “Now we have full control — obviously much more complexity, but still we have full control.”

## The Adidas Microservices Architecture
Adidas engineering kicked off with implementing a top-down MACH architecture across consumer experience, website, B2B, retail stores and apps:

**Microservices.**The monolith was broken down into business capabilities, including the shopping basket, promotions, logging, B2B and checkout, each into at least one microservice with its own end-to-end CI/CD pipeline and independent lifecycle.**API-first.**“We want to build the capability once and want to be able to use [it] everywhere,” Otto said, which includes being channel-agnostic and enabling reusable APIs.**Cloud native.**This includes a dedicated team for[Kubernetes](https://roadmap.sh/kubernetes)clusters and the adoption of some[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention).**Headless.**“If you work in e-commerce, it’s very clear that the frontend needs to have much more changes during the day than the backend,” Otto said. “If a team needs to deploy more frequently, they [must be] independent of a team that needs to deploy less frequently.”
![Andreia Otto and Ravikanth Mogulla of Adidas explained their company's CI/CD pipeline to the DevOpsDays London audience (Source: Jennifer Riggins).](https://cdn.thenewstack.io/media/2024/10/fd756c42-adidas-cicd-pipeline-1-1024x706.jpg)
Andreia Otto and Ravikanth Mogulla of Adidas explained their company’s CI/CD pipeline to the DevOpsDays London audience (Source: Jennifer Riggins).

At Adidas, the platform engineering team provides the [internal developer platform](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/), [Kubernetes](https://thenewstack.io/kubernetes/), observability tooling and the Kafka-based data platform. The SRE team then sits between the platform and app development teams.

One goal of this move to a new platform, Otto said, was to enable developers by automating everything within Jenkins from the push to the deployment to Kubernetes. Then everything is integrated with Microsoft Teams to increase transparency among the whole engineering organization.

“If a branch or if any code that is deployed is allowed to go to production, we have an automation that will pop up a message in Teams and you can click the button” to approve the release, Otto said. “There was a conscious decision to not automate everything to production. Some teams are more mature, some teams are less mature.”

A more mature team may already have adopted progressive delivery techniques like [canary deployments](https://thenewstack.io/5-deployment-strategies-the-pros-and-cons/), but even they have that final approval before going to production.

## New Platform, New Problems
The presenters showed a Willy Wonka meme that had the DevOpsDays audience LOL-ing:

Often in platform engineering, the why is a lot easier than the how. When Adidas shifted to a microservices platform in July 2023, it may have increased the speed to market, but it also increased its complexity dramatically in four main areas:

- Availability of service.
- Breaking changes in deployments.
- Repeated code.
- Security.
“Before, we had one monolithic, big service that we need to troubleshoot,” as an SRE team, Otto said. “Now, if something goes wrong, we have all of this to figure it out, to make sure that we have proper logs, proper tracing and the whole CI/CD is also independent. It means that the complexity is way higher.”

![Andreia Otto and Ravikanth Mogulla of Adidas show how complex their systems became after moviing from a monolith to microservices.](https://cdn.thenewstack.io/media/2024/10/06fc5cdf-adidas-tech-complexity-1-1024x768.jpg)
Andreia Otto and Ravikanth Mogulla of Adidas showed the DevOpsDays London audience how complex their systems became after moving from a monolith to microservices. (Source: Jennifer Riggins)

Immediately following the migration, the SRE team may have found they had more control, but the system’s complexity had also increased dramatically.

“If there is one thing that our team knows — and I think everybody here in this room also knows — is that you can prepare as much as you can, but things will go wrong, and we need to be ready for that,” Otto told the DevOpsDays audience.

Her co-presenter,[ Ravikanth Mogulla](https://www.linkedin.com/in/ravikanth-mogulla-6b713026/), checkout and payments site reliability engineer lead at Adidas, said that the teams faced some classic challenges, but “we started to improve with each and every incident.”

Here’s more about how the SRE team dealt with the challenges it faced once Adidas made the move to microservices and platform engineering:

### Challenge No. 1: Availability of Service
The first challenge became[ observability](https://thenewstack.io/observability/), with the first major incident happening on Black Friday — when they typically experience 10x traffic. One of the databases responsible for the coupon functionality started having some performance issues, with a lot of calls getting piled up in the upstream services.

“We did not have proper timeouts across different microservices, and we also found that some of the microservices were not matured in terms of tracing,” Mogulla said. In addition, the team discovered that “the service which was also responsible for the issue did not integrate or it did not have the tracing with our [application performance management] tool.”

On one of the biggest shopping days of the year, Adidas had a [mean time to recovery (MTTR)](https://thenewstack.io/to-improve-mttr-start-at-the-beginning/) of close to 90 minutes. For context,[ high-performing organizations](https://thenewstack.io/googles-formula-for-elite-devops-performance/) have an MTTR of under an hour. The SRE team was understandably stressed.

“We knew that something was wrong with the coupon service, [but] the biggest challenge for us was to pinpoint the exact issue because almost every call across all the microservices was failing. It was not straightforward, and we had to loop in a lot of teams,” Mogulla said. “By that time, it was almost 90 minutes, [and] we lost a lot of orders.”

### Challenge No. 2: Breaking Changes in Deployments
The new Adidas microservices architecture is set up with Jenkins orchestration to cascade the calls from the different upstream channels of .com, web, desktop and mobile app to different downstream services.

One day, when the team worked together to update to a new version of the Jenkins SDK, while the other three services simultaneously updated smoothly, for some reason the forced sync of deployment resulted in a half-hour of downtime to the .com service.

“We realized that we were already with the different version and that resulted in close to 35 minutes of mean time to resolution,” Mogulla said. “We realized how much dependency the whole architecture has now.”

### Challenge No. 3: Repeat Code
At Adidas, the SRE team is responsible to get the infrastructure from the platform team and to automate the full [CI/CD](https://thenewstack.io/ci-cd/) pipeline. Once Adidas moved to a microservices platform, each app team became responsible for its own monitoring, security scans, [secrets management](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/), [Helm charts](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/) and [Terraform](https://thenewstack.io/terraform-isnt-dead/) alerting along its own CI/CD pipeline. This resulted in a lot of teams doing the same thing in different ways, across 15 different pipelines.

The SRE team is working to ground Adidas engineering in the DRY Principle — don’t repeat yourself — as an aim to reduce redundant information, especially in areas that are constantly being changed.

The SRE wanted to use the [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) to enable code reuse across the different app teams.

### Challenge No.4: Security
The Adidas platform engineering team takes care of the infrastructure and much of the security, including ingresses and secrets management. It’s an uphill battle against sneaker bots — in fact, three out of the five highest-impact bots are targeting Adidas.

“Whenever we have any of the bigger launches or any of the hype articles, we are more susceptible to the bots,” Mogulla said. Therefore, “we do a lot of things from the [content delivery network], [which] gives us a lot of inbuilt features and we make sure that our endpoints are protected.”

However, Adidas, as a publicly traded company, is beholden to a lot of stakeholders. The business team is worried about false positives, he said, while the SREs are more interested in blocking the false negatives. Finding that balance became tricker as microservices exponentially increased the exposed endpoints to more than 200.

“You cannot block 100% of the bots. There are some bots that bypass all these [CDN-based security] features,” Mogulla said. “Either we find the unique criteria — be it with user agents or maybe TLS fingerprints or hash keys — a lot of criteria, like maybe the referrers [that] we use to block [or] we identify immediate LAN, the ASNs or the IP subnets, so it was straightforward.”

But the sneaker bots continue to become more sophisticated, spanning geographies.

Add to this, “Cloud native is for everybody, including the bots, so they just spin different containers or the clusters in the cloud — and then the attack is massive,” he continued. In response, the SRE team has set up authentication between services and reorganized incident management.

## The New Adidas Observability Platform
Adidas looked to increase its resiliency by putting new failover, observability and security measures in place.

The SRE team started reviewing the timeouts across all the microservices to fix latency issues, determining the right timeout to set for each call, for each endpoint. The team also implemented circuit breaking, to shut off the failure in one system from affecting another, as well as adding an inbuilt [feature flag](https://thenewstack.io/moving-to-the-cloud-presents-new-use-cases-for-feature-flags/) tool.

“As SREs at Adidas, we have resilience and stability as the mindset,” Mogulla said. “And whenever we release something into production, the bigger changes, we always make sure this is behind a[ feature flag](https://thenewstack.io/feature-flags-making-software-delivery-faster/),” he said, with observability being mandatory.

“In fact, the entire transition from the monolith to the microservice was behind a feature flag. With just one click, we were able to switch from the legacy to the new microservice architecture.”

The team has also implemented canary deployments and SDK versioning. And, whenever a new version is ready, the upstream services deploy independently.

The Adidas SRE team switched to [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) for “more vendor-neutral” end-to-end tracing.

“Prior to this [transformation], we had logs for different applications, but all of them were segregated between different tenants,” Mogulla said. “With microservices, we did not want to switch between different tenants. We use [OpenSearch](https://thenewstack.io/aws-transfers-opensearch-to-the-linux-foundation/), and then, in a single tenant, but the logs are separated between the different indexes,” all within a one-stop observability dashboard.

With an eye on increased security — especially against the rampant sneaker bots — the SREs now protect all ingresses with SSL/TLS certificates with secured authentication, with Mozilla SOPs (standard operating procedure encryption) on all certificates. They also maintain seed code with IP addresses on allowlists.

“Every failure is an experience for us,” Mogulla said. It’s not easy, he added, when an organization has so many teams and microservices, “to have that proper coordination and to improve on each incident.”

## Incident Management Is About Stability
Downtime is unavoidable. It’s how you respond that’s most important.

Adidas’s incident management is organized into two teams:

- Site reliability engineering focuses on development and operations.
- Service management focuses on process creation and auditing.
But you don’t start with incident management, Otto said. Instead, you start with defining stability for your organization. Only then, she said, can you measure it.

Stability at Adidas is measured in three metrics:

- Mean time to detect (MTTD).
- Mean time to recover (MTTR).
- Revenue impact.
The latter creates a common language with the business stakeholders of the e-commerce platform.

“If we say we have a common KPI, then we don’t go into that debate: Should I prioritize value? Should I prioritize stability? No. We have one metric that we all understand,” Otto said. Which for Adidas and, frankly, most enterprises, “It’s all about money.”

Something qualifies as a major incident based on those three priority metrics. Then an incident manager is appointed to coordinate all communication among the relevant teams, including SREs, developers and marketing.

The following day includes an incident brief or root cause analysis (RCA). Adidas follows a technical template, which asks questions like:

- What did we miss technically?
- Is observability missing?
- Was a test missing?
- Process-wise, what happened?
This is an intentionally [blameless postmortem](https://thenewstack.io/top-12-best-practices-for-better-incident-management-postmortems/), Otto emphasized, which is especially encouraged by leadership, because “the whole point of having the incident debrief [is] really going into what actually happened and create action items.”

An incident at Adidas closes with problem management, also run by the service management team, in order to prioritize the next steps — looking to ever-tighten the incident management feedback loop.

While Adidas made the switch to a microservices architecture over a year ago, the SRE pair ended by saying that observability and platform engineering are a continuous journey, not a destination.

“That was our journey, moving from monolithic to microservices. There is another one coming up with[ GenAI](https://thenewstack.io/ai/),” Otto concluded. “There is something else that will eventually pop up — it’s continuous learning.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)