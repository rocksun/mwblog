# 4 North Star Metrics for Platform Engineering Teams
![Featued image for: 4 North Star Metrics for Platform Engineering Teams](https://cdn.thenewstack.io/media/2024/12/620c4b4a-4-north-star-developer-productivity-metrics-1024x576.jpg)
**Editor’s note:**The author created this post on behalf of DX.
Engineering is a science. That means you can’t improve what you can’t measure. And since every people-led organization is inherently different, measuring developer productivity can feel overwhelming or even impossible.

And since you can’t get a budget for what you don’t measure,[ platform engineering](https://thenewstack.io/platform-engineering/) and developer experience teams are scrambling to measure developer productivity and experience in an actionable way.

[DX](https://getdx.com/?utm_content=inline+mention), the engineering intelligence platform designed by researchers, just released the[ DX Core 4](https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/), which combines the most popular developer productivity metrics frameworks in order to create a common language and prescriptive steps, so that both business and IT can continuously measure and improve developer productivity.
We spoke with DX CEO[ Abi Noda](https://www.linkedin.com/in/abinoda/) to learn the what, how and why now, of the DX Core 4.

## Do We Need Another Framework?
The tech industry is not lacking for developer productivity metrics. In particular, Big Tech companies aren’t shy about what they are measuring, so perhaps they can be an inspiration:

- The
[Engineering Productivity research team](https://landing.google.com/engprod/)at[Google](https://cloud.google.com/?utm_content=inline+mention)follows a mix of self-reported and system-based metrics, in the areas of speed, ease and quality. - Both
[Intercom](https://thenewstack.io/how-intercom-ships-industry-leading-developer-experience/)and[Atlassian measure for developer joy](https://thenewstack.io/measure-developer-joy-not-developer-productivity-atlassian-says/). [Spotify connects DevEx metric](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/)s to customer experience OKRs, factoring in both leading and lagging data.[Meta](https://about.meta.com/?utm_content=inline+mention)uses a complex system of AI and graphs.[Netflix measures DORA and SPACE](https://thenewstack.io/developer-productivity-engineering-at-netflix/), and asks specific questions around sentiment — like “If you were to leave Netflix, would you be sad to leave the tooling behind?” and “Would you recommend your friends work at Netflix because the tooling is so good?“
However, Netflix also has the budget to have a developer productivity team that makes up 15% of its entire engineering division.

Most companies aren’t big tech companies. Most tech teams work at traditional industries still transitioning to the cloud or else are at bootstrapped and early-stage startups and scale-ups that are just starting to consider the impact of developer experience. They are all trying to [do more with less](https://thenewstack.io/is-a-recession-coming-heres-how-to-cut-it-costs-wisely/).

These leaders are sick of hearing that every company’s a unique snowflake and just want a more prescriptive plan to help them measure developer productivity.

The predominant response Noda said his team at DX was hearing was: “Yes, we understand that it’s situationally dependent, but it would be really nice if there was a recommendation of something to start with.”

This wasn’t just CEOs and CTOs begging for clearer instructions. In a time of continuing tech layoffs, platform engineers are looking to prove their worth in a way that non-technical leadership can understand. That’s extra important since research continuously points to[ platform engineers earning significantly higher](https://thenewstack.io/the-2024-state-of-platform-engineering-fledgling-at-best/) salaries than their DevOps peers.

Besides being a growing cost center, platform engineers are also a nascent group at most organizations, which is why platform engineering is often on the chopping block.

“Any platform engineering leader should have something like this in place,” Noda told The New Stack. “If they do not, then they do not have a way of justifying their existence or talking about how they’re moving the needle in the business.”

Business and IT need a shared definition of developer productivity and of the developer experience that’s driving it to give these topics the importance — and the budget — they deserve.

## What Developer Productivity Metrics Exist Now?
The DX Core 4 combines the most common developer productivity frameworks out there, picking four key metrics — kind of a starter pack — and then 12 secondary metrics, once you’re comfortable with the first-round ones, that any engineering organization should consider.

![Table showing DX's Core 4 metrics for developer productivity.](https://cdn.thenewstack.io/media/2024/12/08b8ba13-dx-core-4-1024x516.png)
The DX Core 4 metrics framework. (Source: DX)

The Core 4 are developer productivity metrics that are organized into four buckets:

- Speed.
- Effectiveness.
- Quality.
- Impact.
In order to ground the new approach, let’s break down the three main developer experience (DevEx) frameworks and their strengths and drawbacks.

The oldest metric, Google’s DevOps Research and Assessment (DORA), has been measuring, for the last 10 years, lead time, deployment frequency, change-fail rate, and failed deployment recovery time.

Of the three main frameworks reflected in the Core 4, this is the most prescriptive and quantifiable. However, the[ 2024 DORA research](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/) asked[ more than 100 survey questions](https://dora.dev/research/2024/questions/) across seven areas. Surveying and then interpreting all this data in an actionable way would take several full-time jobs.

Interestingly, if you ask Noda and his team, you may not even have to measure the core four DORA criteria at the start. The DX Core 4 includes change-failure rate as its key metric for quality but relegates the other three as secondary metrics.

In 2021, the [Association for Computing Machinery](https://www.acm.org/) released the[ SPACE of Developer Productivity](https://queue.acm.org/detail.cfm?id=3454124). An acronym for satisfaction and well-being, performance, activity, communication and collaboration, and efficiency and flow, the SPACE framework includes examples of 25 sociotechnical factors you could measure.

The tech industry embraced SPACE as an example of how to start thinking about DevEx in theory. But it didn’t offer any concrete implementation strategy.

In 2023, also in ACM, Noda and other authors involved with the other two frameworks published[ a paper, “DevEx: What Actually Drives Productivity](https://queue.acm.org/detail.cfm?id=3595878).” These[ DevEx metrics](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/) argue that there are three interrelated dimensions of the developer experience: feedback loops, cognitive load and flow state.

For example, when developers have to wait on code reviews, it lengthens the feedback loop and increases the amount a developer has to focus on at any given time while also interrupting the flow. Here again, the tech industry broadly accepted the observations of this research as true, but it didn’t feel it knew what to do with them.

“Developer experience is the key input into improving developer productivity,” Noda emphasized.

The most common metric he has found is counting pull requests (PRs) per engineer. This is flawed because it measures at an individual level, which, he said, “already has a history of being abused in our industry.”

It is also a highly game-able metric. However, he added, it’s the [best signal](https://newsletter.getdx.com/p/measuring-pr-throughputperspectives) the industry has right now, which is why the authors of the Core 4 put diffs per engineer — PRs or merge requests — as the key metric for speed. The model does provide specific guidance for this metric to never be applied at the individual level, but rather to take an average only at the organizational level.

“We acknowledge it’s imperfect, but it is the best signal we have today of output and CEOs, CFOs want this. We say never measure individuals or tie them to their performance. If you do that, people often fluff the numbers and the signal becomes useless,” Noda said. “By counterbalancing speed against developer experience and quality, you create a balanced conversation around productivity.”

It’s also very important, he emphasized, to introduce any measurement as an effort to act as an ally to engineers, not communicating in a way that makes developers feel less secure — and thus less productive and creative — in their jobs.

Not surprisingly, with this in mind, 2023’s wildly unpopular[ developer productivity framework by McKinsey](https://leaddev.com/career-development/what-mckinsey-got-wrong-about-developer-productivity) is missing from this amalgamation of best practices.

## What Is the DX Core 4?
As has been previously explored at length in The New Stack, platform engineering and DevEx teams rarely lack feature requests — internal developer customers are happy to offer feedback early and often. This makes it hard to[ prioritize an internal developer platform roadmap](https://thenewstack.io/platform-engineering-a-workshop-to-help-map-your-strategy/) that balances technical and business demands.

The DX Core 4 aims to combine DORA, SPACE and DevEx in a way that is:

- Meaningful to business stakeholders.
- Consistently measured.
- Combining balanced data — self-reported versus system-based, qualitative versus quantitative.
“Acknowledging that DORA, SPACE and DevEx provide different slivers or different perspectives into the problem, our goal was to create a framework that encapsulates all the frameworks,” Noda said, “like one framework to rule them all, that is prescriptive and encapsulates all the existing knowledge and research we have.”

DORA metrics don’t mean much at the team level, but, he continued, developer satisfaction — a key measurement of platform engineering success — doesn’t matter to a CFO.

“There’s a very intentional goal of making especially the key metrics, but really all the metrics, meaningful to all stakeholders, including managers,” Noda said. “That enables the organization to create a single, shared and aligned definition of productivity so everyone can row in the same direction.”

The Core 4 key metrics are:

- An average of diffs per engineer is used to measure speed.
- The Developer Experience Index, or homegrown developer experience surveys, is used to measure effectiveness.
- A change failure rate is used to measure quality.
- The percentage of time spent on new capabilities to measure impact.
DX’s own DXI, which uses a standardized set of 14 Likert-scale questions — from strongly agree to strongly disagree — is currently only available to DX users. The DXI looks to be a leading indicator that improving your DXI will increase your speed and quality metrics, while also being a predictive measure. For example, a 1% increase in DXI translates to a 0.7% reduction of developer time wasted.

The other piece of the DevEx measurement puzzle that DX aims to fill in is impact. Platform engineering teams, in particular, are struggling the most to measure their impact.

“What’s the actual value delivered?” Noda asked. “Whereas all these [other frameworks] are more operational efficiency and effectiveness, the impact is [asking] what is the value being delivered by engineering?”

In essence, he asked, “Is the investment in engineering going toward innovative and creative things for the business or are they going toward firefighting, meetings and support?”

A platform engineering team is tasked with automating repetition and toil so developers can focus on delivering innovative value to the end customers.

After time spent on greenfield projects, impact measurements drill down to the secondary metric of initiative progress versus return on investment, as well as calculating, at the organizational level, revenue per engineer and research and development as a percentage of total revenue.

For effectiveness, the Core 4 also follows the example of Spotify by measuring time to 10th pull request, as this is an important signal for effective onboarding onto a platform. It also measures effectiveness with ease of delivery, which can be both qualitative and quantitative, as well as more qualitative considerations at the organizational level around regrettable attrition, which is when an employee leaves for avoidable reasons.

As developer perception is a key measure of developer productivity, the new framework harkens back to its predecessors by secondarily measuring the perceived speed of delivery and perceived software quality.

Finally, the Core 4 measures operational health and security metrics —though, interestingly, as a secondary metric.

The DX Core 4 was developed by Noda and DX CTO [Laura Tacho](https://www.linkedin.com/in/lauratacho) over the last year in collaboration with authors of the aforementioned frameworks, including [Nicole Forsgren](https://www.linkedin.com/in/nicolefv/), [Margaret-Anne Storey](https://www.linkedin.com/in/margaret-anne-storey-8419462/) and [Thomas Zimmerman](https://www.linkedin.com/in/tomzimmermann/). It was also tested and iterated on with the DevEx teams at companies like Dropbox, Block and Vercel. Organizations can use the DX Core 4 within the DX platform or on their own.

*This article is part of The New Stack’s contributor network. Have insights on the latest challenges and innovations affecting developers? We’d love to hear from you. Become a contributor and share your expertise by filling out this form or emailing Matt Burns at mattburns@thenewstack.io.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)