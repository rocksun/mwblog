# Relax About Your DORA Metrics
![Featued image for: Relax About Your DORA Metrics](https://cdn.thenewstack.io/media/2024/11/97c1b755-metrics-1024x576.jpg)
Our jobs require a certain level of precision, so it’s natural that we’ll want to take an exact approach to our software delivery metrics. Some folks might even like a detailed standard to pin their measurement to so they can be sure it’s exactly right.

Investing too much in precision is wasteful and takes time away from something far more important: doing something in response to the data.

## Why Precision Doesn’t Matter
The [DORA metrics](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/) are the most popular [DevOps metrics](https://octopus.com/devops/metrics/). The precision needed for DORA metrics is low, and gets even lower the higher you perform. In general, you want to get a temperature check for the kind of performance you have. For the throughput metrics, the unit of measurement is more informative than the number.

It’s more interesting whether you measure throughput in months, weeks, days or hours than it is to split the hairs to get the exact number. If you deploy once a month, your next milestone will be when you can deploy once a week. When your lead time for changes is a week, your next milestone is to make it a day.

Whether you deploy once every 26 days or every 30 days, you’re effectively deploying monthly. This matters because the improvements you’ll make to shave a day or two off a monthly deployment aren’t the changes you need to get to weekly deployments.

## What About Marginal Gains
The Pareto principle, or the 80/20 rule, states that you get roughly 80% of consequences from just 20% of causes. For your improvement efforts, doing relatively simple things like adding deployment and test automation will provide a significant boost. As you expand your adoption of practices, you’ll find it harder to get the same returns for a similar level of investment.

The concept of marginal gains comes from elite sports. By making tiny improvements to technique and equipment, it’s possible to gain a cumulative effect that wins races. The British cycling team pursued this technique, and by looking for 1% gains in many areas, they achieved an incredible streak of wins in the Olympics and the Tour de France.

[Marginal gains](https://thenewstack.io/the-wrong-way-to-use-dora-metrics/) may be helpful to you in a highly competitive situation, but while you’re deploying monthly, you’re not yet performing at a level where you need to look for marginal gains. Marginal gains answer the Pareto paradox, which only presents itself once you’ve done all the obvious things and must now consider the other 80% to get the next improvement.
To refer back to the cycling example, if your bicycle is still made of heavy steel tubes, you are better off switching to a lighter material than trying to modify the aerodynamics. You should be working on the 20%, not looking for marginal gains among the often-ignored 80%.

When you have on-demand deployments, a low change failure rate, and lead times and recovery times measured in hours or minutes, you can switch to marginal gains if [software delivery is still the constraint](https://thenewstack.io/2-ways-to-reduce-bottlenecks-with-the-theory-of-constraints/) in your organization.

Unsurprisingly, if you can deliver to this level, the appetite for further improvements diminishes. Focus usually moves elsewhere, such as improving the hit rate for new features by connecting more closely to the software’s users.

## It’s All About Improvements
The most common reason precise metrics are requested is that they’re about to be used in an unhealthy way. If you want to stack-rank teams based on software delivery performance, you’ll want to ensure the measurement is done the exact same way in every team. Without precision, the comparison may not be correct.

The four key DORA metrics don’t serve this purpose. The goal of tracking software delivery performance is to improve it. The only valid comparison for improvement is to track the same team and application over time to see how it trends.

When you collect the metrics for improvement, you only need to use them to inform your retrospectives or continuous improvement process. The unintentional side effect of our calendar system is that quarterly to monthly is a three times improvement. It requires an impactful change, and it’s easy to see the difference it makes. Similarly, monthly to weekly is 4x, weekly to daily is 5x, and then you deploy on demand, and it’s no longer the area to focus on.

When you’ve reached high-performance levels, you must zoom back up to view the whole value stream to find where improvement efforts are best directed. Increasing your lead time for changes from 1 hour and 20 minutes to 1 hour and 10 minutes isn’t the best use of your time.

## How To Define Your Metrics
To get started, you don’t need any formal metric solution to use DORA’s four keys. You can open the [quick check](https://dora.dev/quickcheck/) and use the questions to start a conversation with your team. For something like deployment frequency, you probably know off the top of your head whether you deploy quarterly, monthly or weekly. Other metrics, like change failure rate, will need more discussion.

You’ll discover many interesting details as your team develops its thoughts around defining the metrics and where to get the data with minimal fuss. Should the [change failure be measured](https://thenewstack.io/how-measurement-elevation-and-aggregation-change-behaviors/) from when the fault is reported, when it was introduced or when it first affected a user? Is it possible to be sure of the exact date and time? Are pull requests included in the lead time for changes?

While those of us in the community have strong opinions on these, nobody is closer to the work than your team. You understand how things work and are smart enough to collaborate on a lightweight definition that’s easy to obtain and good enough to inform your improvement process.

If your team all agrees on the definition, it doesn’t matter what I say you should do. For example, I strongly believe pull requests and code reviews should be included in the lead time for changes because manual stages in your deployment pipeline are the most fruitful targets for improvement. If your team disagrees, that’s OK.

Teams must be allowed to vary their measurement methods to decide what is useful for them and what they need for their improvement process. They might choose a wrong path, but a team applying continuous improvement will self-correct over time.

## Beyond Software Delivery
Software delivery is part of a wider system. You are working on a code change because there is some value to be unlocked. It’s worth introducing measures that make the state of the end-to-end system visible so you can work out where to target your improvement efforts.

Lead and cycle times can help you find the bottlenecks, and understanding the success of features can bring vital knowledge to your business so you [don’t waste time delivering software changes that aren’t useful to your users](https://thenewstack.io/speed-means-nothing-without-real-feedback/).

When you have great performance against the DORA metrics, spend your time looking for something new to measure instead of trying to achieve even higher performance for no meaningful gain.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)