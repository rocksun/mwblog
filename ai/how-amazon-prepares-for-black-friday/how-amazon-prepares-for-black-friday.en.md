ATLANTA — When running a web-scale operation, reacting to increased demand means you are already behind the curve, advised a duo of Amazon engineers at the [Kubecon + CloudNativeCon NA](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) conference, held last week in Atlanta.

The two Amazon engineers gave a keynote talk describing how the company prepares for large surges of customer traffic, without breaking the budget or succumbing to suboptimal service.

With [Black Friday](https://thenewstack.io/sre-tips-to-prepare-for-black-friday/) coming up next week, their tips could help other e-tailers ensure they stay up and running even under extreme duress.

[![](https://cdn.thenewstack.io/media/2025/11/d9fa8caf-kubecon25-artur_souza-chunpeng_wang-300x225.jpg)](https://cdn.thenewstack.io/media/2025/11/d9fa8caf-kubecon25-artur_souza-chunpeng_wang-300x225.jpg)

Kubecon 25: Amazon’s Artur Souza and Chunpeng Wang (right). Photo: TNS

In short, reactive scaling, the standard practice of adding more servers when the load approaches capacity, is necessary but not sufficient for these heavy days of traffic.

“It is not enough,” explained [Artur Souza](https://www.linkedin.com/in/barbalho/), Amazon principal engineer. “By the time your monitoring systems detect high CPU utilization and trigger the scaling actions, you are already behind the curve, and a significant portion of your customers are already impacted.”

So the retail giant has turned to predictive modeling.

## Preparing for Peak Traffic Events Like Black Friday

Each year, the company has a few periodic spikes in traffic, most notably Black Friday, and each year, engineers estimate how large these spikes will be. In the U.S., Black Friday is the day after Thanksgiving, when a lot of people are off from work and eager to start shopping for the upcoming holiday season.

Black Friday shopping actually begins on Thursday night, when the company sees an immediate bump in traffic. It subsides overnight but returns the next day. It levels off over the weekend, but returns on Monday (often called Black Monday).

[![](https://cdn.thenewstack.io/media/2025/11/40ae891c-amazon-peak-traffic.png)](https://cdn.thenewstack.io/media/2025/11/40ae891c-amazon-peak-traffic.png)

The initial spike, shown in the graph above twice, is too steep for reactive scaling alone.

In these cases, Amazon has learned to have spare capacity already running.

These events, the engineers explained, have “**large peak-to-mean spreads**,” meaning the maximum number of users is way above the average number.

And all these users are potential paying customers. So when this many users show up this quickly, Amazon wants to accommodate everyone, lest it lose revenue.

## Wake Up, Babe: New Amazon Performance Metrics Have Dropped

A useful metric for the company is **mean time to traffic** (MTT), which is basically the average time it takes for a new instance of a service, via a [container](https://thenewstack.io/containers/) or [serverless](https://thenewstack.io/serverless/), to start accepting users. MTT is used for reactive scaling to determine when the next instance will be needed, based on the CPU utilization of each instance.

Proactive scaling requires another important metric: **breaking point TPS** (transactions per second), which is the number of transactions a service instance can handle before violating its [service-level agreement](https://thenewstack.io/slo-vs-sla-whats-the-difference-and-how-does-sli-relate/) (SLA), a predefined threshold of satisfactory performance set by the business owners (e.g., the time it takes to add an item to the cart).

[![](https://cdn.thenewstack.io/media/2025/11/d8ef592e-amazon-breaking_tps.png)](https://cdn.thenewstack.io/media/2025/11/d8ef592e-amazon-breaking_tps.png)

“So we want to call out our breaking point exactly at that limit, even if the service doesn’t crash, or even if there’s no increase in error rate,” Souza said.

The TPS is combined with the business forecasts of expected traffic. Each service owner can also modify the forecasts with additional independent variables.

“All this is calculated way ahead of the event, so you know what capacity you will need,” Souza said.

[![A slide describing scaling options](https://cdn.thenewstack.io/media/2025/11/07c9b48e-amazon-scaling-options.png)](https://cdn.thenewstack.io/media/2025/11/07c9b48e-amazon-scaling-options.png)

Even serverless functions have MTT, which in this case is the time it takes to react to your demand. [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) has even created an option for users to [prewarm their DynamoDB](https://aws.amazon.com/blogs/database/pre-warming-amazon-dynamodb-tables-with-warm-throughput/) tables so they’ll be ready for sudden traffic demands.

## CloudTune: Amazon’s Predictive Traffic Forecasting System

Forecasts of expected traffic during these peak times “guide everything we do,” said [Chunpeng Wang](https://www.linkedin.com/in/chunpeng-claude-wang/), senior applied scientist at Amazon, who covered the model forecasting portion of the talk.

The forecasts are used not only to estimate the number of services that will be on standby, but in the longer term, even the capacity of future data centers and when they should be built.

Typically, the infrastructure team readies the additional capacity about a month ahead of the expected surge event. It then stress-tests the additional instances for their readiness to hit this mark, identifying those services that could potentially run hot. A backup capacity pool is also readied.

[![chat showing forecasts](https://cdn.thenewstack.io/media/2025/11/4ff5e243-amazon-scaling-forecasts.png)](https://cdn.thenewstack.io/media/2025/11/4ff5e243-amazon-scaling-forecasts.png)

## Balancing Infrastructure Costs and Service Availability

For these events, Amazon has to determine the optimal point between infrastructure costs and availability risk, Wang said.

It could put all the capacity it has available for these peak events, which would be effective but very expensive. But if it doesn’t have enough infrastructure ready, then slow service and even outages could happen.

“The more we spend on infra, the less customer impact; the less we spend, the higher risk of customer impact. Simple as that,” Wang said.

Here is where the forecasts come into play. Each year, the company devises not a single estimate of this year’s traffic, but a statistical range of how much it could get. It then chooses one percentile, such as the 90th percentile, as the risk-to-cost trade-off point, and then provisions the capacity based on this estimate.

## Scaling Complex Interconnected Services

Estimates of service availability can be particularly tricky in Amazon’s case, given that customer transactions involve multiple services. When a potential customer starts shopping, they will use the search service, and when they find something they like, it will evoke the shopping cart service. If all goes well, then various payment and logistics services kick in.

Each of these services may, in turn, call other services (such as databases) for support.

Each service has its own performance characteristics and potential bottlenecks. So the company also has to determine scaling level consistency, or how long it takes a group of interrelated services to boot up. This is called the **fan-out ratio**. Amazon uses this ratio in its forecast model as well, updating these ratios as they change from service modifications.

## Real-Time Forecast Adjustments During Live Events

In 2015, Amazon engineers, working from the guidelines of Amazon’s central economics team, built software for forecasting future traffic patterns, calling it [CloudTune Forecasting](https://www.amazon.science/news-and-features/how-cloudtune-generates-amazon-store-forecasts-for-prime-day-black-friday-cyber-monday).

This internal Amazon system predicts usage patterns, or “peak computation-load forecasts,” a year in advance. Per-week forecasts are done two weeks out, and even per-minute forecasts are done for the next several months.

Visits from robots and other outlying traffic patterns are filtered out of the desired results.

The results are used by hundreds of product teams within Amazon, all looking to anticipate what their own responsibilities will be in supporting traffic demands.  Some have even created processes to convert anticipated usage to capacity orders for servers through the Amazon Elastic Compute Cloud.

## Predicting the Future, One Second at a Time

During the event itself, Amazon continues to monitor usage and feed that live data back into its forecast.

Wang notes there will always be differences from the forecasted model. Users may do more searches in one year and fewer the following year.

“We update our forecast in real time for the rest of the event so that we can have up-to-date scaling guidance and also have enough lead time to respond,” Wang said.

The world’s events can disrupt even the most thoroughly planned model, Wang said. He recalled 2022 when Brazil and Serbia vied for the FIFA World Cup, which was on the same day as Black Friday. But as long as the game was on, there would not be much traffic from Brazil, the Brazilian business team warned the quants. So they were able to make the adjustments to the infrastructure “with surgical precision,” Wang said.

Of course, most businesses do not run at the scale of Amazon. But the tireless work of these engineers shows us that there are always more ways to optimize our own workloads for both cost-effectiveness and customer satisfaction.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)