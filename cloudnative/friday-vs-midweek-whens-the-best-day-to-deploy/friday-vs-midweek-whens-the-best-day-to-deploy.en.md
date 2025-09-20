Picking the right day to deploy software is not as easy as one might think. There are many factors impacting this decision, both internal and external. This article presents opinions from [DevOps](https://thenewstack.io/platform-engineering/platform-engineering-what-is-it-and-who-does-it/) practitioners on what they see as the optimal day to deploy software.

[Luke Philips](https://www.linkedin.com/in/lukephilips/), the owner of Patrick Consulting and a former Staff Software Engineer at a major publishing company, jokes that the classic practice in the organization he worked for was to deploy on Friday and have all weekend to fix the outage.

But jokes aside, the desire to shield customers from deployment hiccups is [crucial in choosing the right time to deploy software](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/) to production.

## Considering the Impact on End Users

[Matt Acree](https://www.linkedin.com/in/matt-acree-1383442/), Field Services Engineer at a healthcare organization, said that deployments on Friday are often driven by the need to minimize a potential negative impact on the user. If you think the impact will be minimal and would like real-time reporting of user issues, a midweek deployment is preferred; however, if the expectation is that there could be a major downtime, then after-hours Friday, with your on-call teams at the ready, would be the route to go, he advises.

## Production vs. Non-Production Deployments

Deploying mid-week is also a preferred timing for [Rahul Kumar Verma](https://www.linkedin.com/in/rahul-kumar-verma-558812161/?originalSubdomain=in), DevOps Engineer at Infosys. He recommends planning production deployments mid-week, not on Friday, as he puts it, “Why get into trouble if the production app goes down?” With Fridays being non-production days, you can wrap up your updates and get things ready for Monday next week.

However, for non-production deployments, he says that you should deploy as needed, including Fridays. This sentiment is also shared by Niall Hatton, founder of PilotPlan. As he puts it: “Don’t deploy to production on Fridays. But anything else is fair game any day, any week.”

## The Importance of a Solid Rollback Plan

[Mandeep Sharma](https://www.linkedin.com/in/mandeep-sharma-8517a92a0/?trk=public_profile_samename-profile&originalSubdomain=in), DevOps Director at a major healthcare technology company, debunks the myth of avoiding Friday deployments. In his opinion, it is a crutch to be safer if [something goes wrong](https://thenewstack.io/automation-all-fun-and-games-until-something-goes-wrong/) when the team is not around. He is a proponent of a solid deployment process, which can detect failures with automation/SRE in place. The missing step that he often sees is a solid rollback plan, which makes deployments safer.

## Why Fast Feedback Cycles Are Crucial

In the opinion of [Orion Edwards](https://www.linkedin.com/in/orionedwards/?originalSubdomain=nz), Lead Software Engineer at Octopus Deploy, choosing the day to deploy depends on how fast your feedback cycle is. For instance, if your system takes 12-24 hours to deploy across regions, deploying on Friday afternoon might mean it doesn’t reach all regions until late Saturday. This could lead to a bad weekend if any issues arise.

Even if your deployment is effectively instant, if you have a global customer base, a Friday afternoon deployment might not start affecting a critical customer until Saturday due to time zones. But if you have fast feedback and understand things like potential local/global impact, you can deploy any time you like.

## How Deployment Automation Drives Success

[Paul Davies](https://www.linkedin.com/in/paulthecyclist/), Engineering Manager at a European bank, agrees that choosing the right deployment day still divides the community. From his perspective, it is about having confidence to release to production, and there are a number of tools and strategies to support it. These can range from manual QA testers and [staging environments to a wide range of automated tests](https://thenewstack.io/metalbears-mirrord-gives-ai-agents-a-staging-environment-to-test-their-code/), canary deployments, and advanced automated monitoring.

On top of that, there’s immediate feedback from production users, who will notice if something breaks. This feedback gets back to engineering teams, who can then roll back the change or apply a fix.

As he summarizes, ideally, we should be able to deploy at 5 p.m. on a Friday, confident that our automated tests and monitoring will catch any issues. A bad rollout could then be automatically rolled back in production, and a bug ticket raised to be addressed the next working day. In reality, however, from what he has seen, this level of automation (and trust) is extremely difficult to achieve. So, if you prefer a stress-free weekend, it’s probably best not to deploy to production as the last thing you do on a Friday afternoon.

## Factoring in Team Well-Being

According to [Kateryna Bakhmat](https://dou.ua/users/kateryna-bakhmat/), DevOps Engineer at Uitware, avoiding deployments on Fridays is a best practice when it comes to the team’s well-being. By the end of the week, engineers and others are usually tired, which can lead to situations where mistakes are more likely to happen. Also, if a deployment contains errors (which happens from time to time), it can lead to increased workloads and extended working hours — and in some cases, it might even require working over the weekend.

She also points out that every situation is different, and sometimes a Friday deployment is necessary; however, from her experience, it’s better to wrap up other tasks on Friday and deploy with a fresh mind on Monday.

## How Organizational Maturity and Resources Matter

[Barbara Teruggi](https://www.linkedin.com/in/barbara-teruggi/?originalSubdomain=es), Security Architect at a global IT service provider, lists the maturity level as a key element for deciding when the right time is to deploy software. She also points out that the size of the company is an important factor. Medium to large companies may have the budget for automation and for having the necessary professionals available or on call during the weekend; however, small companies or startups may not.

Also important is what kind of systems/software your company builds, and when your customers use it the most. She recommends avoiding deploying to production during peak usage time. Another important factor is the criticality of the change you are deploying. How big is the impact to your customers if something goes wrong? Do you depend on other parties to deploy or test as well? Nowadays, many companies integrate their services with those of other companies. Her point is, at least for the time being, humans must be kept in the loop at all times.

Even having all the automation of the world, she would not recommend deploying anything critical on Friday if you don’t have the right people with the right knowledge about what’s being deployed to check on it.

## Why Risk Tolerance Drives Deployment Decisions

A great round-up of thoughts around the optimal day to deploy software comes from [Yury Fedorov](https://www.linkedin.com/in/yury-fedorov-0910a09/), Senior Software Engineer and [Site Reliability](https://thenewstack.io/google-sre-site-reliability-engineering-at-a-global-scale/) Engineering at YouTube. In his view, this question gets to the heart of a major challenge in technology. The simple answer is that nothing is ever truly 100% reliable, as countless factors can lead to failure, and these are often interdependent. You can think of it this way: a complex system is like a Jenga tower. Even if each block (a piece of software, a server, or a process) were perfect, a small shift in one area could cause the entire tower to collapse.

He offers the following breakdown of some of the factors that contribute to this lack of perfection:

* **Complexity:** As systems grow, so do their interconnected parts (software, hardware, infrastructure, dependencies). A change in one area can have an unpredictable ripple effect on another.
* **Human Error:** People make mistakes. Whether it’s a coding error, a misconfigured server, or a typo in a command, human factors are a constant source of potential failure.
* **External Constraints:** Real-world limitations like budget, time, and team knowledge all influence how a system is built and maintained. Sometimes, a compromise has to be made that introduces risk.
* **Process and Operations:** Even with the best intentions, a process can be flawed. For example, deploying a major update on a Friday afternoon might seem efficient, but it leaves little time to fix things if something goes wrong before the weekend. This is why many organizations have specific policies against such deployments, choosing to optimize for safety over speed in certain scenarios.

While [approaches like DevOps aim to automate](https://thenewstack.io/automate-devops-with-an-everything-as-code-approach/) and reduce many of these risks, they can’t eliminate them. Instead, they focus on making failures less frequent, easier to detect, and faster to recover from when they inevitably occur.

As you can see, there are many factors the organization needs to consider when deciding when to deploy. [Automation and a solid rollback plan are key](https://thenewstack.io/release-automation-key-considerations/) to success; however, what needs to be considered is the risk tolerance and burden on the team responsible for deployments.

In summary, as we say at Octopus, “every day is a good day to deploy software, even Fridays” — as long as your processes are repeatable and reliable.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/16a6c9f2-wyganowska_joanna.jpg)

Joanna is the CMO at Octopus Deploy. Joanna has more than 20 years of experience running product marketing for software startups and software giants alike.

Read more from Joanna Wyganowska](https://thenewstack.io/author/joanna-wyganowska/)