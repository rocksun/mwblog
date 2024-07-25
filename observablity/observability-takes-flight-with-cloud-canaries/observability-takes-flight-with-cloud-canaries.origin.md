# Observability Takes Flight With Cloud Canaries
![Featued image for: Observability Takes Flight With Cloud Canaries](https://cdn.thenewstack.io/media/2024/07/5841b1b9-bird-3386323_1280-1024x682.jpg)
[Observability](https://thenewstack.io/observability/) platforms are increasingly important to [DevOps](https://thenewstack.io/devops/) teams wrestling with the accelerating frequency of deployment and the expanding focus on everything from [security and compliance](https://thenewstack.io/chef-extends-security-and-compliance-across-hybrid-cloud/) to [governance and risk](https://thenewstack.io/governance-risk-and-compliance-with-kubernetes/).
These platforms give software engineers insight into the health and performance of their software systems, giving them the tools to understand what’s working — and just as importantly, what isn’t — fix problems, and adapt their applications and services accordingly. But they don’t come cheap, they’re complex, and they’re locked into the vendors who sell them.

[Mark Callahan](https://www.linkedin.com/in/mark-callahan-1945b53/) three years ago founded [Cloud Canaries](https://cloudcanaries.ai/) to develop an open, AI-based service that could do what these larger platforms do, only a lot quicker, cheaper, and more efficiently. The company came out of stealth this month, offering lightweight agents — called Intelligent Canaries — that can be easily spun up and sent into the cloud or the internet to collect the same information that these larger platforms do to detect problems in software systems, offering real-time performance monitoring, predict issues, and determine ways to resolve them.
The canaries leverage the startup’s [neural network](https://thenewstack.io/airbnb-builds-a-second-neural-network-to-diversify-listings/) and can be created, scheduled, deployed, and managed by Cloud Canaries’ [Aviary platform](https://cloudcanaries.ai/features), which collects the incoming data and includes dashboards for assessing the health of endpoints, services, and [APIs](https://thenewstack.io/api-management/), compliance with SLAs, and forecasting, using a five-day rolling composite, service, and canary forecasts to allow software engineers to proactively fix issues.

Developers can share their canaries internally with others within their organization or make the canaries public and share them with others outside of the company. They also can upload their canaries into Cloud Canaries’ system, creating so-called “template canaries.”

“With the platform that we provide, you can do a couple of things,” Callahan told The New Stack. “You can really do the same solutions that the major vendors are providing if you have the canaries or you share the canaries, but you can do it really quickly. You can whip out a canary within minutes. … You can assign environmental variables, you can assign thresholds, you can send notifications, you can assign schedules, and then you can put that either in a [Kubernetes](https://thenewstack.io/kubernetes/) cluster or you can turn it into a ‘canary agent’ that is executable anywhere you compile it and you put it wherever you want to put it and it just collects data.”

## Feeding Data into AI Models
The data can be fed into the company’s neural network or be saved in third-party AI models from vendors like [Snowflake](https://www.snowflake.com/?utm_content=inline+mention)’s Cortex, a suite of AI tools based on its large language models, or AI models from Databricks, New Relic, DataDog, and other vendors.

Cloud Canaries gives “corporations and enterprises the best of both worlds — the ability to build these canaries and quickly share them … and also get more sophisticated canaries at some subscription price and to have a platform that could manage them and, most importantly, collect the data,” he said.

Callahan became familiar with the canary concept during the last three years of his 17-plus years with [Oracle](https://developer.oracle.com/?utm_content=inline+mention), when he was development manager for [Oracle Cloud Infrastructure](https://thenewstack.io/oracle-touts-new-appdev-tools-distributed-cloud-support/). Canaries were small apps written in Python, Java, or another programming language that simulated user workloads and dispatched into the software system to help DevOps teams and developers what’s going on from a user perspective.

He brought the idea with him to Cloud Canaries, putting him into competition with an array of established companies that offer [observability platforms and tools](https://thenewstack.io/next-gen-observability-monitoring-and-analytics-in-platform-engineering/), including [IBM](https://www.ibm.com?utm_content=inline+mention), Splunk, Datadog, [Amazon](https://aws.amazon.com/?utm_content=inline+mention), Sumo Logic, and [Cisco](http://cisco.com/?utm_content=inline+mention)’s AppDynamics. And it’s a big, growing market, with MarketsandMarkets predicting it will grow from $2.4 billion last year to [$4.1 billion by 2028](https://www.marketsandmarkets.com/Market-Reports/observability-tools-and-platforms-market-69804486.html).

## The Need for Speed
Callahan said Cloud Canaries’ competitive advantages include speed — canaries can be created in minutes — an open platform, and a subscription-based plan that he said will address the most common uses cases at 10% of the cost of the observability platforms, which need to be tuned to their environments and collect, store, and analyze data from logs, metrics, and traces, all to get a view of software system operations. Insights into a system’s performance comes from events and KPI measurements based on the data.

“I talked to customers,” he said. “Oracle was spending $100,000 for one seat and you could do it with some canaries in my platform. Once the platform is developed, everyone’s paying for compute modeling, so I can get to 10 percent now. We get diagnostic information from a lot of different open software platforms, [[Python’s] Django](https://thenewstack.io/what-is-pythons-django/) and Kubernetes, and we can generate canaries through an open API schema.”

Developers using Cloud Canaries can quickly create their own canaries or go into the canary template library, find one they want to use and cut and paste it. It’s easy to do, Callahan said. They also can get canaries from the Canary Marketplace — similar to mobile app marketplaces like Apple’s App Store and Google’s Play — which contains canaries created by Cloud Canaries, DevOps teams of customers, or third-party developers.

## Subscription-Based Canaries
Cloud Canaries offers multiple subscription models, including three Canary models for free for the first three months, after which they get rolled into a paid subscription. The next level is 15 licenses for $49 a month — with 15 canaries running at any time — and 45 licenses for $79 a month (and 45 running at any time). Large enterprises and service providers pay $5,000 to have the technology installed behind their firewall or air-gap.

Canaries on the marketplace will be free via a $1 to $10 subscription.

“The key here is you get the license, and you get everything,” Callahan said. “You don’t have to go back to your CFO to get permission to get something more that you could just run a canary for. That’s the magic on the financial side. One of the reasons that we leveled at this kind of pricing model is I want to have tens of thousands of canaries running at any point in time. That’s the vision — a large number of enterprises running thousands of canaries on the Aviary platform generating data.”

As more companies use more canaries to bring in more data, the possibilities begin to grow and to pull in more revenue, he said. If organizations give the OK, Cloud Canaries will be able to crowdsource some of the data and run it through an AI model. That can lead to more paid-for dashboards and opportunities to become closer partners with enterprises, showing them what steps make sense or give them insights they never had exposure to before.

As more data is collected and run through AI models, the platform will be able to run a more granular level of predictions and forecasting to the point where the canaries will be able to not only identify ways to resolve issues but also to mitigate them.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)