# Optimizing the 90%: Where Dev Time Really Gets Stuck
![Featued image for: Optimizing the 90%: Where Dev Time Really Gets Stuck](https://cdn.thenewstack.io/media/2025/04/5f4a2b6f-clocks-1024x576.png)
So much focus is placed on the new code your developers write: How can you use AI to speed it up, how do you manage [AI tools](https://thenewstack.io/ai-powered-coding-developer-tool-trends-to-monitor-in-2025/) to ensure they don’t lead to chaos and how much more productive can your developers get?

But the reality is that writing new code is only a fraction of a developers’ overall time. According to Gartner’s latest Emerging Tech report on AI developer tools, only 10% of a developer’s time is spent writing new code for new applications.

So what about [all the other time](https://thenewstack.io/why-do-developers-lose-1-day-a-week-to-inefficiencies/)? The other 90% of developers’ time consists of managing existing code (30%) as well as noncoding tasks such as design, architecture, project planning and documentation. And within that big chunk of time, there’s plenty of scope to reduce bottlenecks.

But with so much attention on code generation, engineering leaders may be missing some glaring opportunities for improvements. Here are three examples of bottlenecks that exist in many engineering organizations that could be overcome.

## 1. Metrics Are in So Many Different Places
While existing frameworks like [DORA](https://thenewstack.io/how-to-track-dora-metrics-in-an-internal-developer-portal/) and [SPACE](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/) are often provided in software engineering intelligence platforms and offer valuable insights into productivity, they don’t tell the entire story and are often rudimentary metrics taken from Jira and source control tools. For instance, standards-based engineering metrics help managers keep an eye on costs, security vulnerabilities, SLO (service-level agreement) compliance, ownership, documentation, adoption of new tools or practices, production readiness and more.

In addition, there are numerous other engineering metrics that can serve as proxy metrics for DORA, but these appear fragmented across many tools used in the software development life cycle (SDLC). They’re neither unified nor collected in one place. While they each can provide valuable insights, trying to consolidate, track and make sense of them can be difficult. And often the approach for consolidation means that [engineering teams don’t trust the data](https://thenewstack.io/50-of-engineers-lack-trust-in-the-data-they-rely-on-most/).

The lack of integration across all metrics means that while you can see your change failure rate or mean time to recovery (MTTR) is high, you won’t be able to understand why, meaning it’s difficult to make adjustments.

## 2. Adding Sentiment to the Mix
Engineering leaders tend to favor system metrics because, before stepping into leadership roles, they were engineers who routinely monitored systems through logs and telemetry data. However, the same approach cannot be applied to measuring people.

This is partly because system data needs to be cleaned before it can be used. Measuring CI build times from pipeline data sounds straightforward, but organizations still have to filter background tasks and adjust for parallelism before they can get reliable metrics. System metrics also don’t capture the human side of engineering work. For example, understanding whether developers are able to stay in the flow state so that they can do the work that matters most.

Traditional engineering metrics can also still be gamed. For instance, measuring deployment frequency might incentivize teams to game the data by just deploying simple, low-impact changes or breaking up larger updates into smaller, less meaningful ones solely to boost the deployment count, rather than focusing on delivering real value or improving stability.

One approach to fill these gaps is through surveys. [Surveys](https://hubs.la/Q03hCnSY0) help you to understand team morale, satisfaction and friction points that don’t show up in system data. While metrics give you the “what,” surveys help you answer the “why” and sometimes the “how.”

Engineering leaders may think a developer survey platform will solve for this, and there are some great options out there, but they don’t usually integrate with all the tools where developers work (for example, Microsoft Azure DevOps).

In addition, these tools often have a steep learning curve, requiring additional time and resources to be used effectively. Using a specialist platform also adds yet another tool to the mix for engineers, who are already using an average of 7.4 tools for everyday operational tasks. [Developer tool sprawl is causing a loss of six to 15 hours weekly for 75% of developers](https://thenewstack.io/developers-unhappy-with-tool-sprawl-lagging-data-long-waits/).

## 3. Using Metrics to Make Actual Improvements
If you do have metrics in place, you still need to make sense of them for your organization. But you’re probably stuck answering some difficult questions:

- What can I do to improve these metrics?
- What actions can I take?
- How can I track these actions and the progress of any improvement attempt?
- How do I report on this and the return on investment (ROI) of any changes to leadership?
That means first being able to consolidate and cross-reference metrics with sentiment, and then having the ability to decide how to make changes in your processes, tooling and culture. The idea is to build a continuous improvement loop.

![Siloed engineering metrics](https://cdn.thenewstack.io/media/2025/04/38cf8d3d-before-2-1024x814.png)
Source: Port

## How to Overcome These Bottlenecks
![](https://cdn.thenewstack.io/media/2025/04/38ed5e05-after-2-1024x776.png)
Source: Port

Consolidating your software engineering intelligence metrics, standards-based metrics and sentiment from developer surveys in an [internal developer portal](https://hubs.la/Q03hCn6-0) enables you to better understand how different areas of your SDLC affect each other. The difference is that instead of being housed in separate dashboards or one-off survey reports, all of the information you need and all the actions you can take are built into your developer portal.

For instance, you would be able to see the correlation between all of the following within your portal:

- A slowdown in deployment frequency
- A spike in incidents by monitoring MTTR
- The number of outages and failed deployments
- The number of incidents that are open versus resolved
In this example, the portal can also provide further context: Did your recent deployment cause this spike in incidents?

A pre-built survey, especially one that is also configurable and shareable within the portal, could be carried out to better understand:

- If engineers are being pulled away from their roadmap tasks, including deployments, because they have to focus on incident management.
- How much time this is diverting from coding.
- What steps are causing a particular time drain.
Using the combination of metrics and sentiment data, you can initiate a plan to improve the incident management approach, like so:

- Immediately create a Slack channel for a responder team.
- Easily find information on who’s on call, owners of services and whether a service is properly monitored, within the software catalog.
- Perform
[Day 2 operations](https://hubs.la/Q03hCrfK0)using self-service actions such as requesting permission to access a cluster, rolling back a service, scaling up a cloud resource and toggling a feature flag.
In addition, a maturity scorecard could be put in place to ensure best practices (such as having the right number of ReplicaSets) are upheld to prevent and mitigate the number of incidents.

You can then track whether these improvements and automations make a difference in incident management response (MTTR) and in deployment frequency, using a dedicated dashboard in the portal.

If the impact is being felt in MTTR and not deployment frequency, then it may be worth looking into how to streamline deployment frequency itself, perhaps by creating self-service actions to scaffold a new service, spin up a development environment or send a reminder to review a pull request.

The key difference is that rather than adopting the most comprehensive survey tool or the most advanced dashboard, you can get all of your metrics in one place, check for correlation, take actions, tailor workflows and track progress, all in one place, shifting the onus from metrics visibility to genuine improvement.

If you’re looking for a way to overcome these bottlenecks, check out Port’s [Engineering360](https://hubs.la/Q03hCc760), a tool combining DORA metrics and developer sentiment inside your portal.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)