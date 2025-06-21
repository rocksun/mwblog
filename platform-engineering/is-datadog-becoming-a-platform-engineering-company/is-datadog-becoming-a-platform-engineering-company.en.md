NEW YORK – Datadog’s [internal developer portal (IDP)](https://thenewstack.io/internal-developer-platform-vs-internal-developer-portal-whats-up/), announced at its annual user [DASH](https://www.dashcon.io/speakers/) conference here this month, could replace a number of [platform engineering](https://thenewstack.io/platform-engineering/) processes. But beyond just the platform engineer support, the idea is to make [DevOps](https://thenewstack.io/devops/) and [observability](https://thenewstack.io/observability/) simpler and more accessible for the developer, operations and the nontechnical user. [Datadog](https://www.datadoghq.com/) will become a platform engineering provider and an observability provider — if it can convince DevOps teams to adopt what can be described as observability-centric platform engineering.

Amid the release of over 100 announcements, its IDP reflects demand for what its customers and users are telling them, as well as all observability providers: Customer organizations are seeking to eliminate overlaps in tool use. This means that their volume demand might remain the same or even increase, but they’re actively seeking to shrink the number of different observability tool vendors they work with overall.

Organizations require smarter and simpler-to-interpret telematics data and analytics. In this way, the not-so-technical CTO or other non–DevOps stakeholders can make sense of all those logs and metrics, and in a way that only the in-house observability and security expert could otherwise understand. More and better security integration is demanded as observability is becoming an integral part of securing data and infrastructure. It has been demonstrated that platform engineering can serve as the best way to manage not only observability, but all IT infrastructure together. [AI agents](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/), of course, will play a critical role for all of the observability needs in the present and future context described above.

The above also accounts for why a platform engineering structure is a major component of what Datadog offers with its IDP — one of the most important DASH announcements among the over 100 — and integration with its and other tools and platforms users have at this time.

“In general, we see [SRE](https://thenewstack.io/platform-engineering/sre-vs-devops-vs-platform-engineering/) [site reliability engineering] and platform teams evolving from being very interruption-driven today — dealing with a million fires — toward more mid- and long-term planning: resilience engineering, performance engineering, and also security engineering,” Datadog co-founder and CEO [Olivier Pomel](https://www.linkedin.com/in/olivierpomel) told a group of analysts and journalists during the DASH conference. “We think this will give them more time to elevate security engineering to a top priority.”

While platform engineers will always be needed, the platform and AI agent support should go a long way in eliminating many of the otherwise hands-on tasks of building and maintaining a platform engineering structure. With its IDP, Datadog intends to allow platform engineering team members to spend more time doing the fun stuff of designing or managing backend infrastructure or other tasks with the IDP through platform engineering, while removing many of the manual tasks and toil associated with creating and managing a home-grown platform engineering system.

“Hopefully we can help platform engineering teams work better because they don’t have to build that stuff — they can use it,” Pomel said. “They can then focus on what best practices to put in place internally.”

Observability has become a critical part of platform engineering, as every platform needs to provide developers and the business with real-time insights on compliance, quality, risk and business impact of current development processes, [Torsten Volk](https://www.linkedin.com/in/torstenvolk), an analyst with TechTarget’s Enterprise Strategy Group, told me this week. However, in this case, the tables have turned somewhat.

“Typically, we see developer platform vendors integrate observability tools, but in this case, it is the other way around. Starting with the observability platform is interesting as it provides a great basis for truly data-driven software development, where the development process is tied very closely to how the application behaves in production,” Volk said. “This encourages developers to observe the impact of their code changes on the production application. On the other side of the coin, we can have DevOps engineers and platform engineers continuously monitor, refine and revise the key business metrics they can then use to evaluate the impact of new code releases.”

Datadog’s IDP can be traced back to the company’s humble beginning when it was a fledgling startup in New York City with just a few engineers over 10 years ago.

“The idea was to go back to the founding principle of Datadog: to get everybody on the same page. We didn’t even start with monitoring — we started with, ‘Hey, let’s get Dev and Ops into the same platform,”’ Pomel said. “Over time, we’ve extended that to different personas and said, ‘Let’s bring the security engineers, the product managers, the [FinOps](https://thenewstack.io/finops-what-is-it-and-why-should-developers-sign-on/) people — all the other teams that have to care about the application. Let’s bring them all into the fold.”

## The Menu

[![](https://cdn.thenewstack.io/media/2025/06/710b2b99-screenshot-2025-06-11-at-1.46.51%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/06/710b2b99-screenshot-2025-06-11-at-1.46.51%E2%80%AFpm.png)

As Datadog has shown, observability is only one function the IDP offers to meet the needs of stakeholders, both technical and nontechnical. It’s designed to serve the needs of developers, operations teams, CTOs and nontechnical stakeholders, Datadog says. It provides different DevOps tools available for not only observability for developers, but it’s designed to provide click-as-you-need available tools for not only observability, but a wide range of DevOps and even business intelligence tools. For the developer,  there is also the opportunity to allow them to use their favorite tools provided within the platform.

“We found that many of our users had to build some homegrown solution to tie their docs together with some of their production monitoring, some of their architecture diagrams, and some of their internal processes,” Pomel said. “They were either building that completely in-house or on top of open source, with Backstage being one of the tools they were using.”

Tomorrow’s observability platforms are expected to offer detailed knowledge of not only issues but a holistic analysis of what is occurring now in a network in such a simplified way that the security team, the CTO, the developers and other nontechnical stakeholders understand and make use of. In this case of Datadog’s IDP, the platform engineering component provides the take-off point that could eventually cover all things infrastructure-related as well.

Datadog’s description of its IDP in its [documentation](https://docs.datadoghq.com/internal_developer_portal/) remains a bit lofty, described as a way “to centralize knowledge, streamline processes, and improve operational efficiency.” However, its specific use cases cited cover a wide range of utility that collectively go beyond yesterday’s typical observability cases, especially compared to when Datadog was once a fledgling Application Performance Monitoring (APM) platform provider:

* Simplify API management
* Manage and optimize cloud costs
* Manage app and API protection posture across development teams
* Accelerate developer onboarding
* Manage and map dependencies
* Evaluate production readiness
* Improve incident response
* CI support

During the DASH keynote, [Muhan Guclu,](https://www.linkedin.com/in/muhan-guclu-96a3b991) engineering manager for Datadog, described a nightmare scenario where a service dependency crashed in the middle of the night and how “hard it was to fill in the blanks.” He showed how today, with the IDP’s software catalog, users can use their services “as part of a greater whole.”

As Guclu demonstrated with Datadog’s IDP, a fresh start could be used, or an existing topology could be imported from [Backstage](https://thenewstack.io/five-years-in-backstage-is-just-getting-started/) to address the issue. A clean start included all the individual pieces of the system architecture using what was already in Datadog, Guclu showed. Using AI, these pieces were composed into “context-rich” systems with titles and descriptions explaining how they related, he said.

“Right at the top, it was easy to find where code lived and what documentation was available. Detailed information was provided about the services already being monitored with Datadog. When coming from Backstage, Datadog completed the picture, filled in the gaps and overlaid real-time telemetry onto each component,” Guclu said. “Understanding the system in relation to best practices also caused delays. Best practices were typically only mentioned in occasional migration emails.”

While acknowledging that migrations can often consist of only “changing a couple lines of YAML,” Guclu said the back and forth between infrastructure and platform teams would typically slow down his progress. Using self-service actions, Guclu showed how he could find templates for infrastructure management “quickly and safely” for components such as datastores, or spin up new ones to create an S3 bucket with [Terraform](https://thenewstack.io/terraform-isnt-dead/). Doing that with the IDP requires providing information about the bucket, the region, and a justification, and then creating a pull request.

A new pull request is then automatically created and assigned to the infrastructure team for approval, and “I can view it right in GitHub,” Guclu said. Once the bucket has been created, Guclu showed how it automatically appears as a dependency in the system overview page. “It complies with everything we need it to, covering regulation, internal processes and best practices, and any permissions,” he said. “As a platform engineer, I love the idea of building templates like this, but I don’t wanna have to learn yet another product-specific system.”

At the end of the keynote, Guclu made a bold claim about the IDP’s reach: “Datadog IDP is the only developer portal that knows your system and stays up to date automatically,” Guclu said. “You can understand your services without overhead, track best practices with scorecards and manage your infrastructure with AI.”

## Shift to Platform Engineering

Senior product manager [Brooke Chen](https://www.linkedin.com/in/brooke-chen) discussed how she fought to bring about an IDP in response to customer demands — and agonies. She was the first to believe in the project after “lots of painful enterprise customer conversations,” Chen told me during an interview.

Trends like IDP and the shift from traditional DevOps toward embracing platform engineering are actually more appealing to engineering leadership, including CEOs, VPs and so on, Chen said. Developers and individual contributors (ICs) are ultimately the main beneficiaries of this movement, “but fundamentally, it’s about scaling your engineering practices as you scale your infrastructure,” Chen said.

“I think a lot of engineering leaders face the challenge of being pulled in different directions. With microservices, teams are empowered to adopt their own technology and stack. So, the question becomes: How do you ensure that, at a broad level, teams don’t introduce new risks in the name of moving fast?” Chen said. “Many of our data customers are large organizations, and they care deeply about governance and standardization, all while trying to balance scalability and speed. This is where IDPs come in — they’re a product category that really addresses these concerns effectively.”

While I downloaded and applied basic queries to monitor metrics, access a service, create a pull request and perform other basic tasks with the IDP dashboard, we have so far not tested its full functionality. However, if Datadog’s IDP works like it needs to, it will serve as another leap for observability and DevOps. “Scaling successful DevOps practices across the organization is one of the key unsolved challenges in enterprise technology. Replicating DevOps success needs to be based on metrics that provide comprehensive, quantifiable insights into the speed and scalability of software delivery,” Volk said. “Ultimately, this enables organizations to predict issues and proactively resolve them through automation and process improvements.”

Datadog’s background and know-how for observability have served as a substantial foundation to create an IDP for platform engineering. “The IDP’s metrics-driven approach is the basis for optimal collaboration between developers, operators and the business, as they provide a joint basis for continuously aligned decision-making,” Volk said. “Thinking this all the way to the end, this is the ideal foundation for consistently implementing data-driven decision making across the enterprise.”

## Security Is King

Speaking to changes taking place in observability, Pomel said: “Most of our security customers started with observability. That’s the natural path — they use us for observability, and since we’re already instrumented, it’s easy to add security,” Pomel said during the press and analyst briefing. “But we’re now starting to see customers come to us for security first — especially in [SIEM](https://thenewstack.io/what-separates-an-siem-platform-from-a-logging-tool/) [Security Information and Event Management] — because many large companies have already adopted a SIEM, and they’re now revisiting those choices in light of the cloud and AI. That leads them to call us, even if they haven’t used our infrastructure monitoring or APM products.”

Specific to the IDP, security and observability data do not just extend to the developers but to all stakeholders. “The only way to build products securely is to make security a shared responsibility across development, operations, and security,” Pomel said. “You can’t just have the security team own everything, because they’re too small. In any company, for every security engineer, there are basically 10 operations engineers, and for every operations engineer, there are 10 software engineers. So the leverage really lies with the engineering teams.”

A far-reaching observability platform today must be one part security, one part networking and monitoring, and in Datadog’s case, one part IDP that serves the needs of platform engineering running on top. Datadog’s IDP was designed to break down, or has shown how it will break down, so-called silos among DevOps teams and stakeholders, potentially transforming DevOps into a more platform engineering structure if it works like it’s supposed to.

“Connecting the dots between DevOps, platform engineering, developers and security is critical for successful application development,” Volk said. “Starting with performance metrics and building out the platform from there could ensure a truly data-driven approach to DevOps. This could make it easier for the average enterprise to consistently achieve DevOps success.”

Meanwhile, Datadog’s approach as a Software as a Service (SaaS) provider is different from most of the industry, Pomel said. “The rest of the industry is very fragmented — thin slices of functionality with ecosystems of vendors in each category,” Pomel said. “As a customer, you end up having to buy 12, 15, even 24 different products to cover all your needs. That creates internal usability problems, gaps between tools, and difficulty in getting full value.”

Datadog, with its IDP, started with the idea of providing an integrated platform — “just as we did with observability and we’re now applying that to security,” Pomel said. “And because we already cover observability, we’re already deployed everywhere. We already have the signals we need. We know what’s happening on machines, in networks, with users, with engineers, and with the code. So we already have a lot of the data needed to make this work,” Pomel said. “The challenge, of course, is that there are hundreds of competitors. In every category, there are a dozen companies focused on that one small piece. So our efforts are going into building a full security suite that covers those areas at least as well as those individual vendors — and adds value by eliminating the gaps.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)