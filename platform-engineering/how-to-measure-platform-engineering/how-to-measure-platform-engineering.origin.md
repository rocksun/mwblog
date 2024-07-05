# How To Measure Platform Engineering
![Featued image for: How To Measure Platform Engineering](https://cdn.thenewstack.io/media/2024/07/41800c9f-measuring123-1024x576.jpg)
Though developer burnout has been a strong motivator for [platform engineering](https://thenewstack.io/platform-engineering/), there are many other reasons to adopt this approach. The method you use to track the success of your internal developer platform must be adjusted to account for different motivations for investing time and budget into creating a platform.

Effectively [measuring platform engineering](https://thenewstack.io/platform-engineering/) is even more crucial when it comes to protecting the long-term investment in its development. As an industry, we could face large-scale platform abandonment if stakeholders don’t see the benefits of sustained funding.

Given the many different motivations, how do you measure platform engineering? That’s where [MONK metrics](https://octopus.com/devops/metrics/monk-metrics/) come in.

## What Are the MONK Metrics?
MONK is an acronym for four items:

- Market share
- Onboarding time
- Net Promoter Score (NPS)
- Key customer metrics
Three of the MONK metrics are concrete, while the fourth — key customer metrics — is more abstract. This is how the measurements flex to allow for the different technical and business reasons a platform was introduced.

## The M in MONK: Market Share
Market share is an internal adoption metric. This metric is understood through three tangible numbers:

**Developers**: The number of developers in your organization**Potential users**: How many of them use technology the platform assists**Users**: Out of this second group, how many are actually using the platform
The platform’s adoption can be assessed by the number of users out of the group of potential users. You can express this as a percentage, but the absolute numbers are typically more important.

![The potential user group expands when golden pathways are added. Market share increases as users adopt the platform.](https://cdn.thenewstack.io/media/2024/07/3d6e46bd-example-1024x588.png)
The potential user group expands when golden pathways are added. Market share increases as users adopt the platform. (Source: Octopus)

When considering new feature ideas for the platform, the impact of the change on adoption (the number of users) and relevance (the number of potential users) can inform your decision-making. Will a new [golden path](https://octopus.com/blog/paved-versus-golden-paths-platform-engineering) result in more developers opting to use the platform?

The value of a platform is amplified by the number of users, so market share is a useful measure for all platform engineering initiatives.

## The O in MONK: Onboarding Time
Onboarding time can be expressed in two ways:

- The time it takes a developer to set up their development environment, commit their first change and get it into production.
- The time it takes for a team to introduce elements of the
[internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/).
While you might think about new developers when it comes to onboarding time, it’s also relevant when [developers move to a different team](https://thenewstack.io/engprod-the-secret-of-elite-developer-teams/), pick up an application they haven’t worked on for a while or replace their laptops.

Platform onboarding time is usually reflected in market share metrics, as a difficult or elongated process usually means teams can’t find the time to complete it. You can pay attention to the problem of onboarding pains to see if easing the process increases adoption rates.

To collect developer onboarding time, you should start the clock when a developer starts working on a new codebase and stop the clock when their first commit is in production. If your internal developer [platform solves common problems around developer toolchains](https://thenewstack.io/devops-toolchains-beat-off-the-shelf-platforms/) and deployment pipelines, a new team member should be able to quickly get their first small change into production.

The goal of the onboarding time metric isn’t just to speed up that first change. It’s a useful measure of many concerns that all platform engineering teams share. It reflects the quality of developer documentation and the level of [automation provided once a developer has integrated their changes](https://thenewstack.io/cloud-management-platforms-need-robust-automated-integration/).

## The N in MONK: Net Promoter Score
Net Promoter Score (NPS) is a marketing metric used by two-thirds of the Fortune 1000, with expected scores for software-as-a-service companies in the region of 30 to 40.

To calculate NPS, you need to collect a sample of responses to the following question, which is answered using a scale from 0 (highly unlikely to recommend) to 10 (would definitely recommend):

*How likely are you to recommend the internal developer platform to another developer?*
Responses should be grouped according to the score given. Those who answer with a score below 7 are “detractors,” while those who answer with a score of 9 or above are “promoters.” Your NPS is the percentage of promoters minus the percentage of detractors.

This metric is more useful as a trend rather than a score. You should check in on users occasionally to see if they are becoming more or less satisfied with the platform over time. Crucially, you should allow users to give a reason for their score so you can work out why they are delighted (or upset).

While NPS is far from perfect, anyone developing a software product will understand the benefit of a user-provided indication of satisfaction. The reasons for a user’s rating can be eye-opening and will inform your future direction. By no means does NPS replace regular conversations with your users.

## The K in MONK
Following the three concrete measures, which are broadly applicable to platform engineering teams, the final metric is abstract. This metric should reflect the business and technical motivation for introducing platform engineering.

For example, if teams weren’t spending enough time on feature development due to the burden of managing deployment pipelines and infrastructure, the key customer metric would be the proportion of time spent on new feature development. Or, if the platform is seen as a way to improve developer satisfaction, you could use [developer experience metrics](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/) as key customer metrics.

Many organizations have multiple justifications for adopting platform engineering, so multiple metrics may be required. A simple demonstration of how the platform has brought standardization might be sufficient in some cases.

## DORA Metrics for Platform Engineering
You can’t discuss platform engineering metrics without the subject of the DORA metrics coming up. The DORA metrics measure software delivery performance using deployment frequency, lead time for changes, change failure rates and recovery time after a failed deployment.

If you created a platform to enable developers to increase their software delivery performance, the DORA metrics are useful as key customer metrics (the K in MONK). You’d measure the DORA metrics for the stream-aligned team to demonstrate the platform’s impact.

Additionally, if your platform team is delivering software, it’s useful for them to track their own DORA metrics so they can use them to inform their improvement process. The developers using the platform will appreciate the regular delivery of value, just like external customers do.

While you can’t judge an entire platform engineering initiative solely on DORA metrics, they certainly have a role to play.

## Why MONK Works
MONK metrics work because they mix concrete measures common across the platform engineering industry with contextual success metrics that align with the reasons a platform was considered a worthy investment in the first place.

A strong set of metrics is crucial to the long-term investment in the platform. Without a clear understanding of its value, there’s a good chance developers will eventually be reassigned to feature development at some point in the future.

Designing your key customer metrics also helps describe the vision for the platform, which can guide you in choosing which features to introduce and what ideas aren’t likely to help achieve the platform’s goals.

There’s always a trade-off with metric frameworks between the usefulness of specific metrics and the contextual nature or reality. MONK metrics use the strengths of both.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)