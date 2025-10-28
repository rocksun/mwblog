LONDON — It turns out that platform engineer is a sales job.

We’ve written a lot about how [DevOps engineer and platform engineer](https://thenewstack.io/platform-engineering-wont-kill-the-devops-star/) roles differ. But while a DevOps team mostly serves just developers and operations, an [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform") (IDP) team serves many stakeholders. And it’s in a [much more fragile place to keep its budget](https://thenewstack.io/why-up-to-70-of-platform-engineering-teams-fail-to-deliver-impact/).

At Team Topologies’ [Fast Flow Conf](https://www.fastflowconf.com/) this month, [Christopher Batey](https://www.linkedin.com/in/christopher-batey/), CTO at the [Core Engineering Consulting Group](https://www.cecg.io/), decided to steer the conversation past the developer customer that’s most associated with an IDP. After all, adoption can’t be your only metric — just because it has users doesn’t mean your IDP is useful or improving the bottom line.

Instead, Batey focused on how to reach the other stakeholders — senior leadership, product management, change management and security — to sell your platform internally.

Don’t worry, this won’t be a sales course — at least not explicitly. It might be a lesson in communication. He presented tips for applying different platform metrics to shape conversations with your platform’s many customers, to demonstrate your value to different audiences and to show how your [platform engineering](https://thenewstack.io/platform-engineering/) team is — hopefully — creating lasting impact on the business.

## Why Platform Engineering Requires a Sales Mindset

Platform projects sometimes use their initial funding to apply great technology — period. That’s when problems can start.

“Many platform engineering teams are delivering great platforms while also struggling to maintain their existence,” Batey said, “You feel like you’ve done a good job, but then the value remains invisible to leadership.”

This dilemma means  [45% of platform engineering teams are disbanded or restructured within 18 months](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering).

Since platform engineering is in its early stages at many organizations, any internal sales strategy has to be grounded in explaining the why, not feature-dumping about what you have or promise you’ll do.

“I really believe platform engineering is the way we scale DevOps,” Batey said. But “in practice, certainly in my experience, we are still asking application engineers to think about too much, to do too much.”

Despite [DevOps](https://thenewstack.io/devops/) having broken down some silos, he said, many developers are still juggling three cloud accounts — for development, user acceptance testing and production — along with writing Terraform or [Pulumi](https://www.pulumi.com?utm_content=inline+mention), setting up databases and cloud identity and access management (IAM), and then having to work out which of often many ways to deploy a container.

These important yet repetitive, non-differential distractions have devs spending less than 30% of their days ([or, by some accounts, even less](https://thenewstack.io/survey-engineers-want-to-code-but-spend-all-day-on-tech-debt/)) creating unique business value.

“Platform engineering,” Batey said, “is really how we get application engineers actually building applications.”

## Focus on Stakeholder Problems, Not Your Solutions

Funding often relies on transforming the way  you demonstrate platform engineering value to stakeholders across the organization. Which is why, as [Matthew Meckes,](https://www.linkedin.com/in/mmeckes)  senior containers specialist at [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), pointed out  [in another Fast Flow Conf talk](https://thenewstack.io/why-up-to-70-of-platform-engineering-teams-fail-to-deliver-impact/), it’s not enough for platform teams to just measure the throughput and stability of their platform. What really matters is how fast a platform can help software development teams deliver software in a safe, secure and reliable way.

Batey is on board with defining platform engineering’s impact more broadly.

“I think the goal of platform engineering is to enable change at speed with security built in, hopefully while maintaining or increasing reliability,” he said. “I prefer this definition of platform engineering over the, ‘I’m building self-service capabilities to enable developers to be productive,’ etc., because it tells us *why* we do platform engineering rather than the current *what* of platform engineering, because the what is always going to change.”

Once you and your platform team are grounded in that *why*, you can then move on to understanding your stakeholders’ varied perspectives and what success means for each. From there, you can create more meaningful metrics that are grounded in their needs.

“I always need to remind myself to frame those discussions based on the person I’m talking to and not the solution that I want to implement,” Batey said. “This is on a Post-It note that I have on my monitor for remote meetings, and it’s something I read out to myself five times before going to an in-person meeting.

The Post-It note, he said, reminds him  “to avoid at all costs discussing your solutions with stakeholders. They do not care about your solutions. They care about their problems. So let’s try to understand them.”

Only then, he continued, can platform engineering teams have accountability and be respected as agents of change.

“As platform engineers, then we should always know how the thing that we’re building is either going to increase the speed at which this company can deliver software,” he emphasized. “It’s going to make a measurable improvement to security, or it’s going to improve reliability.”

## Identifying Your Platform’s Key Stakeholders

“Platform engineers need to talk to everyone,” argued Batey, “because platform engineering’s job is to bring everyone together to actually deliver change to production.”

At most organizations, this includes, but is not limited to:

* Head of engineering.
* Product engineers.
* Change managers.
* Infrastructure teams.
* Security teams.

Start by looking at how a change gets to production. The platform team aims to pay down what Batey called the “coordination tax ” — the friction encountered as change moves to production. Just remember that these steps aren’t just grounded in technology, but include a lot of people and processes along the way.

For the executive stakeholders, risk, return on investment and speed are key metrics, while the head of engineering for product development cares about predictable onboarding, delivery and quality. Both stakeholders have a keen eye on the percentage of time actually spent delivering value to end users.

Since we know that [writing code was never the bottleneck](https://leaddev.com/velocity/writing-code-was-never-the-bottleneck), the rest of the software development life cycle — the outer loop — is where both trends of platform engineering and [AI](https://thenewstack.io/ai/) can have the most impact. Both can help reduce the time to release to production or reduce friction in other key areas like generating documentation and making everything more discoverable.

Unsurprisingly, [security](https://thenewstack.io/security/)’s biggest concerns usually include coverage, speed to remediation and number of endpoint vulnerabilities. Security stakeholders in particular, Batey said, want to be brought in earlier, to really bake it into the platform.

Change management practitioners are most concerned with high-risk changes and how a platform can overall drive a safe, predictive time to production.

Head of infrastructure cares about adoption, consistency and operational excellence.

## How to Structure Conversations with Stakeholders

“I am an engineer by heart. By default, I am not a natural communicator, and I would be much happier writing code, building platform features,” Batey acknowledged. “The only way that I can improve the way I communicate with these people is to systematize it.”

Before talking about any solutions, he works together with stakeholders to verbalize the problem. Then, he looks to quantify it. For each of these stakeholders, Batey presented example problems and then how to quantify them, to then measure for any change.

### Executives

* **Problem:** Product delivery is too slow.
* **Quantified:** Features delivered monthly.

### Change Management

* **Problem:** No trust in the evidence attached to change requests.
* **Quantified:** 95% of change requests include have manually added evidence.

### Security

* **Problem:** Vulnerabilities just keep growing.
* **Quantified:** 35 vulnerabilities in production.

### Head of Engineering

* **Problem:** Engineers struggle to get things done.
* **Quantified:** Service onboarding is two weeks. Pull requests take three days on average to merge.

The stakeholder will not always be aware of a problem they are facing, Batey warned. For instance, security may be completely unaware that every team has a different path to production. All they know is that security tools are not being adopted enough, or no one is taking ownership for fixing bugs.

You start by quantifying how many assets have vulnerabilities, he suggested. Then you bring in external proof of how other businesses have solved the same problem. Finally, you try to create internal proof with a short proof of concept.

Finally, together, you create what Batey refers to as a “library of needles,” or metrics that you co-own, betting that you can move those needles.

## Which Platform Metrics Matter Most to Leadership?

Your platform initiative needs to exhibit measurable values of speed, performance, security and/or cost. Having already gone in depth in discussing security, Batey gave some examples for each of the other three.

### Speed Metrics

* Product launch time.
* Number of user-facing features able to be released.
* Lead time.
* Lead time for changes.
* Deployment frequency.
* Engineering onboarding to join a team and release to production.
* Service onboarding.

This speed is often increased by removing manual actions and approvals.

### Reliability and Performance Metrics

* What percentage is the user-facing product is available? Different nines per features?
* Are there outages during key events?
* Are there service-level agreement breaches?
* [Service-level objectives (SLOs)](https://thenewstack.io/sre-fundamentals-differences-between-sli-vs-slo-vs-sla/).
* Service-level indicators (SLIs).

Working directly with application engineers, Batey added, you can also set:

* Functional test coverage for key business use cases.
* Non-functional test coverage.
* Reliability test coverage.

### Cost Metrics

Total cost of ownership (TCO) and return on investment (ROI) are the key metrics that all team leaders should understand, especially in this time of arguing for your job. He offered some key cost metrics:

* Service cost.
* Cost per customer.
* Cost per user journey.
* Storage cost.
* Hosting cost.

## A Practical Guide to Prioritizing Your Metrics

The hardest part of platform engineering is deciding what to do in what order, Batey said, which can mean teams measure too much. Measurements need a hierarchy, which he grounded in practical examples.

Imagine product releases are slowing down. Executives are complaining that your software organization is falling behind competitors. But then, if teams try to speed up, reliability suffers with more vulnerabilities.

His diagnosis is that a manual set of environments caused differences in testing and production. Developers are skipping automated tests, and security is having to deploy differently for each environment. The solution, he said, that a platform engineering team should present to execs is a standardized, consolidated path to production for key services, making use of consistent, lightweight environments, which are automatically created in a consistent manner.

“Always start simple,” Batey recommended. “Pick a key business use case, find out what components are involved, and, whatever initiative that you’re doing, just make sure it throws some value for those key user journeys.”

Measurement is the best way to translate the value of your platform program, grounded in the accountability of *why*. To do that, start simple, he advised, by picking one key, easily measured business use case per stakeholder.

Just remember, “the goal isn’t to measure everything,” Batey said. “It’s to measure the right things to show the value of the platform features that you build to key people.”

This, of course, includes everyone who holds the purse strings. But also, he said, “you don’t want people to be blocking the things that you’re trying to do.”

[Download the ebook “Platform Engineering: What You Need to Know Now.”](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)