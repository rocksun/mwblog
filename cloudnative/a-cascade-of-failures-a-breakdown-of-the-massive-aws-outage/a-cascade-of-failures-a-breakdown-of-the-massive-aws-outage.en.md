Somewhere tonight in northern Virginia, a group of [AWS](https://aws.amazon.com/?utm_content=inline+mention) administrators are probably enjoying a beverage after a *very* long day of troubleshooting.

Amazon Web Services [suffered a cascade of failures](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update) Monday across its US-EAST-1 Region, causing multiple outages across a dizzying array of cloud services, including [AWS Lambda](https://thenewstack.io/three-reasons-why-teams-move-away-from-aws-lambda/), Amazon API Gateway, Amazon Appflow, Amazon Aurora DSQL Service and others.

As it is all too often the case, the culprit was [DNS misconfiguration](https://thenewstack.io/why-you-need-distributed-dns-implementation/). Go figure.

Of AWS’ 15 regions worldwide, US-EAST-1 is probably the largest, with clusters of [data centers](https://thenewstack.io/how-much-energy-is-really-being-consumed-by-data-centers/) spread across Loudoun, Prince William, and Fairfax counties. And judging from today’s outage, many of today’s largest businesses have at least a footprint in the region.

AWS is now almost fully recovered, according to the company, with the backlog of customers’ services being completed within the next few hours. Snapchat, Reddit, Venmo and other cloud services reliant on AWS are also showing recovery.

## How US-EAST-1 Went Down

The problem first manifested itself aorund 3 a.m. EDT, when multiple services reported increased error rates of DNS resolution of the DynamoDB API endpoints. That problem was reported within three hours, and by 6 a.m., the staff was confident that, after a ramp-up period, services would soon be at full speed.

“We can confirm global services and features that rely on US-EAST-1 have also recovered. We continue to work towards full resolution and will provide updates as we have more information to share,” they wrote [optimistically in the log](https://health.aws.amazon.com/health/status) at 6:03 a.m.

Almost all the services recovered, that is. Requests to launch new EC2 instances (or services that launch EC2 instances such as ECS) still got met with error rates in the US-EAST-1 region. Initially, the suspected culprit was stale caches, which needed to be flushed.

The admin team remained confident they could easily fix the EC2 problem, though two hours later, errors were still occuring when launching EC2 instances. They advised not launching instances with this region designated as the availability zone.

Worse yet, the Lambda service, shakey from the start, was starting to have significant recovery issues as well. And as the morning wore on, a pestilence of downed AWS services plagued the admin team.

## More Issues With EC2

“We can confirm significant API errors and connectivity issues across multiple services in the US-EAST-1 Region,” they wrote at 10:14 a.m. They traced the problem to the EC2 internal network, which hampered with DynamoDB, SQS, Amazon Connect and other services.

The problem turned out to be the monitoring system for the load balancers that was stressing out the Lambda service.

The last message, posted at 6:48 p.m. EDT, noted that EC2 launches have been restored, though there is a two-hour backlog of work for services that require EC2 launches, such as Redshift, as well as a backlog of analytics and reporting data.

## Widespread Impact on Major Online Businesses

Although only a single region was effected, it would prove to have a profound impact across many of the biggest cloud services on the internet. The Downdetector site, which reports on the availability of cloud services, saw a huge influx of outages of AWS services throughout the day, most all of them from US-EAST-1 Region.

[![chart showing outage complaints](https://cdn.thenewstack.io/media/2025/10/a03c0424-downdetector-1-aws-oct20.png)](https://cdn.thenewstack.io/media/2025/10/a03c0424-downdetector-1-aws-oct20.png)

Source: Downdetector

This in turn caused issues for [the many companies relying](https://www.cnbc.com/2025/10/20/amazon-web-services-outage-takes-down-major-websites.html) on AWS. Downdetector reported AWS-relate3d issues today at [Snapchat](https://downdetector.com/status/snapchat/), [Apple Music](https://downdetector.com/status/apple-music/), [Reddit](https://downdetector.com/status/reddit/), [Venmo](https://downdetector.com/status/venmo/), [Doordash](https://downdetector.com/status/doordash/), [Hulu](https://downdetector.com/status/hulu/) and [Amazon](https://downdetector.com/status/amazon/) itself. The degree to which they were impacted is presumably measured by how heavily they relied on this particular region.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)