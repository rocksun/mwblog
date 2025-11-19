An AI Gateway won’t solve all of a developer’s API problems, [Jason Ehmke](https://www.linkedin.com/in/jasonehmke) told audiences at the [Kong API Summit 2025](https://konghq.com/events/conferences/api-summit) in New York.

Right now, it’s really the [API Wild West](https://thenewstack.io/reining-in-the-api-wild-west-5-api-testing-best-practices/), the chief technology officer and co-founder of [DevGrid](https://www.devgrid.io/) told audiences during his Oct. 15 presentation, “Creating a Best in Class API Strategy.” DevGrid is an engineering operations platform that provides visibility into software teams and tech stacks.

While AI gateways are a key part of an [API management](https://thenewstack.io/introduction-to-api-management/) strategy, they’re not enough alone, he contended.

“You don’t know who’s in it or not,” Ehmke said. “You have authentication forced in there, but you’re opting in. It’s not mandatory. It’s your rate limiting, but you don’t know what you’re rate limiting for?”

Predictably, this leads to problems. Ehmke shared some related statistics:

“Most people have API security incidents or have delayed releases from API security — it’s a thing. You’re not alone with these problems,” he said. “But the breaches are expensive, maybe something minimal, maybe something big. They are incredibly expensive.”

To tame this Wild West of APIs, Ehmke called for IT divisions to invest in an API platform, which can automate security and [governance](https://thenewstack.io/use-api-governance-tools-for-better-api-experiences/) in ways [API gateways](https://thenewstack.io/api-gateway-checklist-how-strong-is-your-apis-front-door/) do not, he said.

## API Wild West

As it stands, many organizations find themselves with questions about their APIs, he pointed out: There are multiple customer APIs — which is the right one? Is that endpoint supposed to be public? Why did the customer find a PII exposure before IT did?

An API gateway gives you some information, but not enough, he contended. Specifically, it provides:

* A proxy, but no idea who hasn’t migrated;
* Authentication, but it’s opt-in instead of mandatory.
* Rate limiting but no business context; and
* Metrics, but just request counts.

But Ehmke said developers also need to know

* Who owns which APIs, when they break at 3 a.m.?
* Which APIs can be retired without breaking production?
* How to find APIs instead of building duplicates, and
* Whether APIs are compliant with actual evidence.

“It’s time to build a platform that actually governs,” he said.

## An API Utopia

Contrast the Wild West with the idea of API Utopia, which he defined as providing:

* Full real-time visibility of APIs;
* Security built in automatically.
* Reuse API design blocks, enforcing standards;
* Delivery 3 x faster delivery;
* Compliance where auditors and regulators become your fans; and
* APIs that can be monetized easily.

“You can have full visibility, security, reuse, delivery and compliance and monetization all in a single cloud by thinking of it is more than just a gateway,” Ehmke said. “A gateway is part of the posture, but it’s not enough.”

## The 6 Pillars of API Platform Success

To get there, he recommended embracing six pillars of API Platform success.

“We can get better. We can get more done faster,” he said. “We can reduce our security incidents and we can have lower development costs,” he said. “Thinking of it in six different pillars helps just to wrap your heads around what I should be thinking of on my API platform versus just a gateway.”

**Pillar one is to establish clear policies and standards**, where governance is mandatory. Pillar one means requiring:

* The use of OAuth;
* Version all APIs;
* Document fully all APIs; and
* Requiring all APIs to pass security tests.

“These are the things that you put into code, put into law,” Ehmke said.

**Pillar two is the API lifecycle management**, from designing, through building, testing, deploying, operating and retiring your gateway.

“These are automations and tools that you built in your platform,” Ehmke explained. ”Everything should be classified in your platform so that you don’t accidentally get to production [and] the API leaks a social security number. Again, these things happen without the right checks and balances in place,” he said.

For instance, to design a gate, you should ensure it’s OpenAPI 3.1 valid, includes security schemes, auto flows are defined, there are owners in the catalog and data classification, he explained. Building a gate requires a backward compatibility check, semantic versioning, contract tests, as well as assessments of its performance and consumer impact.

The API Platform should handle:

* Inventory and ownership, so there’s a single source of truth for all endpoints;
* Contract testing, so that it auto-runs tests on every change;
* Policy as code that enforces gates in [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) and the gateway.
* Progressive deliveries, such as a canary/shadow/rollback via the gateway;
* A consumer registry that maps callers to versions and performs an impact analysis; and
* Observability so that [Service Level Objective](https://thenewstack.io/service-level-objectives-stop-thinking-in-burn-rates/) (SLO) budgets are wired to deploy rights.

**Pillar three requires automation and tooling** to handle the design time, run time and operations of the platform. For instance, during the design time, there should be code generation from specs, schema validation and mock servers used. Run time should include rate limiting and quotas; auth and transformation and circuit breaking. Operations should allow SLO to auto-rollback, certificate rotation and compliance reports.

“People are expensive. They take vacations, so automate everything that you can,” Ehmke said. “This is a big one. This is a lot of gaps in security. API teams, feature teams, they can get stuff done, but they don’t always think of the big picture of security and compliance.”

**Pillar four covers security and compliance issues**, including authentication, runtime protection and compliance. So, for instance, under authentication, the platform should deliver:

* OAuth 2.0/Open Authorization/OpenID Connect (OIDC);
* mTLS for service mesh;
* API key rotation;
* Zero-trust verification.

Runtime protection includes:

* DDoS mitigation;
* SQL injection blocking;
* Rate limiting per client;
* Payload encryption.

Compliance issues that the platform should address include inventory attestation, Auth type reporting, integration with security tools, and audit logging.

**Pillar five encompasses developer experience** and steps that incorporate developers-helpful capabilities such as the ability to:

* Browse catalog of existing APIs;
* Generate from templates and SDKs;
* Auth/security pre-configured;
* Automated compliance checks;
* Self-Service everything.

“You will have a lot of resistance by putting everything … as proprietary code, or make everything Build Your Own Adventure,” Ehmke said. “But if you make it an easy onboarding experience for your developers, make it upload your spec, get a proxy, I can guarantee you that you’re going to have a lot more people breaking down your door to say, ‘I want to use your new proxy, because it’s so easy to use, I have everything out of the box.’”

Finally, **Pillar six covers monitoring and metrics in an API dashboard** that tells developers the total APIs, the percentage that is compliant, the average response time, security issues, API reuse and developer satisfactions.

[![API Governance Dashboard with total APIs; compliance percentage; average response time; number of security issues; percentage API reuse; and developer satisfaction score.](https://cdn.thenewstack.io/media/2025/11/8455c8f5-api_dashboard.jpg)](https://cdn.thenewstack.io/media/2025/11/8455c8f5-api_dashboard.jpg)

Screenshot from Jason Ehmke’s presentation at Kong API Summit 2025.

## Avoid the Pitfalls

“Now there are some potential pitfalls to all this, because you might have no buy-in, you might not have the right buy-in,” Ehmke warned. “Sure you have your platform, but you haven’t talked to the security team. You haven’t gotten their blessings.”

The most common five pitfalls that create problems are:

1. No executive teeth, so that people ignore the requirements. Executives need to establish hard rules, such as the CISO demanding that without security measures, the API doesn’t deploy.
2. Another typical mistakes is what he calls “Gateway Theater,” which is assuming if you have a gateway, you’re secure.
3. Also — and we’re sure you’ve heard of this one — a common pitfall is “The VP exception,” where a VP makes an exception “just this once” because it’s on deadline. That leads to chaos. So ensure any exceptions are documented. “If somebody pushes for an exception, it’s now their problem in writing,” he said.
4. Making the team do everything manually to avoid the CI/CD pipeline, which will block bad or unsafe apps.
5. Developer revolt is also a potential pitfall. Again, automation and a good developer experience will help in avoiding that pitfall.

“Automate, automate, automate, and that’s the developer experience,” he said. “If the onboarding experience is so visible, developers will find a way to get their VP to give them the exception of not using it, and you’re back to square one.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)