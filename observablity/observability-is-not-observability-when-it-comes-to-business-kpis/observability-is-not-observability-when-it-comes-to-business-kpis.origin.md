# ‘Observability’ Is Not Observability When It Comes to Business KPIs
![Featued image for: ‘Observability’ Is Not Observability When It Comes to Business KPIs](https://cdn.thenewstack.io/media/2024/03/70cc7638-ai-generated-8615473_1280-1024x574.png)
When we think of “
[observability](https://thenewstack.io/observability/),” most of us define it as “metrics, logs and traces.” It’s not. What we really mean is to enrich and observe those pre-defined sets of data and then layer analysis on top of them to better measure and understand business [Key Performance Indicators](https://thenewstack.io/measuring-key-kpis-and-platform-engineering-success/) (KPIs) — proactively.
In other words,
[observability isn’t just about collecting and sorting data](https://thenewstack.io/grappling-with-observability-data-management/) sets. It’s not just about alerts, correlations and uptime. Observability is about enabling every single engineer, especially outside of DevOps, to proactively prioritize work efforts based on the analysis of data from all their systems and apps.
And this data goes far beyond just metrics, logs, and traces.
We need to connect these three signals to the true drivers of our company — business KPIs. This requires shifting how our teams operate. Instead of focusing on fire drills and technical KPIs, they should only work on what delivers the highest business value, whether that’s growing revenue, improving the end-user experience or reducing churn. Easier said than done.
Let’s cover how we got to the current state of
[observability and where we need to rethink](https://thenewstack.io/rethinking-observability/) our approach to it moving forward.
**The Problem with APM**
Once upon a time, the goal was to watch data as it came in from various apps, whether hosted on dedicated servers, in the cloud or on end-user devices (mobile and web). Think of a stream of data that we could peer into as it flowed by.
We used agents to more easily integrate and collect data; however, they never collected all the data, just certain types over specific time periods. Picture a stream with a dam at the top that trickled the flow and periodically let specific water droplets through. Viewing this stream, we only saw what the dam let through and wanted us to see.
This APM approach caused us to be too reactive. We instrumented error
[logs and metrics](https://thenewstack.io/metrics-logs-and-traces-more-similar-than-they-appear/) to gather more info, looked for crashes and basically relied on our vendors to decide what data should be let through. We lost the complete picture of our systems, and when we did see an error or oddly trending metric, we often did not have the surrounding contextual data to solve it — at least within a reasonable time frame.
We let problems go unnoticed and instead focused on the most easily addressable issues, like network errors. We inadvertently turned a blind eye to the issues that actually
[affected our business](https://thenewstack.io/how-devops-affects-business-stakeholders-and-leaders/) KPIs.
It’s understandable why we did this because answering the following questions with the limited data types from APM solutions was far from trivial:
- Where were the errors happening in relation to end-user experiences, and did those errors really matter?
- Did the spike in crashes lead to a drop in purchases?
- Was the increase in network errors impacting our business greatly — or at all?
- What did that Apdex score really mean for our roadmap and our business?
What we wanted to know was not, “Were these issues below a certain threshold?” It was, “Were we preventing customers from engaging successfully with our business?”
**The Promise of Observability**
As a potential solution, we asked ourselves, “What if we didn’t sample and instead let all the data through? What if we broke the dam?” The promise of this question was alluring and was definitely better than our prior (and still existing) agent-based APMs.
And so we opened the dam.
With such a
[deluge of data](https://thenewstack.io/strategies-for-navigating-data-deluge/), the complexity became enormous, so we jury-rigged this flow of unstructured data into forms we understood — metrics, logs and traces. It was worlds better and easier to use than the prior APM methodology. We could better identify errors and oddly trending metrics; we could instrument our code less on each release; we could detect issues faster; and we had the hope of possessing more contextual data for faster resolution.
Even so, as we pushed all our
[data into the familiar three pillars of observability](https://thenewstack.io/take-control-of-your-observability-data-before-it-controls-you/), we fell back into old habits. Databases and services that catered to the different pillars appeared, and we created workflows that were often overly biased towards one of the pillars rather than thinking about the cohesive outcome that the three pillars could jointly provide.
When an engineer went to solve a problem — or even understand if a problem was worth investing resources into solving — they often started out with an approach that was tethered to one of the three pillars. They then had to make connections or complex queries to the other two pillars, which could be synthesized into an activity log. This work typically ended up being non-trivial, with not enough connection provided by the tooling to effectively link the three separate pillars.
And thus we were back in a place — albeit with more data — not too far removed from where we were with the APM paradigm.
It also became painfully clear that more data did not inherently solve all problems. To some extent, we just replaced old problems with new ones. We had more data to tackle problems with, but this frequently led to greater dashboard sprawl rather than distilling the data into useful information.
Our teams built systems that collected unstructured data, yet we failed to tap its full potential.
And so our engineering teams are still reactive and focus on Apdex, SLOs and SLAs – not true business-driving KPIs.
**What Observability Should Be**
We all find ourselves in a continual search for faster and faster identification and resolution, but what we really want is to switch to a paradigm of being “proactive.” After all, if we only focus on solving issues faster — falsely equating proactivity with speed — then we’ll forever be responding to fire drills based on technical KPIs. Sure, we’ll get faster at them, but we won’t be making the best decisions for our business.
**“Proactivity” means running all engineering efforts based on leading indicators of core business metrics.** Indicators that map to purchase flows, startup times, user abandonment — the KPIs that are specific to our apps that reflect what our business cares about, like churn, revenue and LTVs.
These leading indicators should be specific to our business and should ultimately connect with the end user of our apps. And so the true goal for whatever structure of data that we end up with is that it must reflect the end-user experience — not myopic, disconnected backend metrics and KPIs. Anything less and we cannot connect technical failures to business failures — and definitely not without massive amounts of toil and guesswork.
After all, apps are not a backend. It’s not enough to care whether a network call fails or a process breaks. Apps are also not just a frontend. It’s not enough to care whether a mobile app crashes or a website freezes. Observability is about understanding everything the individual user experiences.
Specific to the current form of observability, proactivity is not about leading indicators based on our logs, metrics, and traces. Instead, proactivity is about looking for leading indicators based on our users, then using metrics, logs, traces and other types of data to understand where our app is breaking down, why user-connected indicators are trending incorrectly, and what needs to be done to resolve issues.
So when we are looking at our backend metrics, does our data reveal when an end user has a bad experience? Does our set of observability vendors measure the downstream impact of broken experiences and lost revenue?
Unfortunately, the answer right now is: they don’t.
We know where observability needs to go. Understanding the state of our systems is only the first step. The next step is understanding the state of our user experiences. That way, we’re making decisions based on business KPIs as opposed to merely technical ones.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)