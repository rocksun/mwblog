# From 10-Minute Queries to Real-Time Dashboards: Everactive’s Industrial IoT Stack
Everactive replaced a brittle OpenTSDB setup with Timescale to simplify their stack and scale real-time analytics across thousands of batteryless IoT sensors. They went from six databases to three, dropped query latency from 10 minutes to sub-second, and now manage both relational and time-series data in one place — with fewer crashes, less overhead, and better performance.TL;DR:
*This is an installment of our “Community Member Spotlight” series, where we invite our customers to share their work, shining a light on their success and inspiring others with new ways to use technology to solve problems.*
*In this edition, **Carlos Olmos**, **Dan Wright**, and **Clayton Yochum** from Everactive join us to share how they’re bringing analytics and real-time device monitoring to scenarios and places never before possible. Learn how they’ve set up their data stack (moving from six to only three instances), their database evaluation criteria, their advice for fellow developers, and more.*
# About the Company
[Everactive](https://everactive.com/) combines battery-free, self-powered sensors and powerful cloud analytics to provide “end-to-end” hyperscale IoT solutions to our customers. Our company is undergoing a huge transformation from focusing only on industrial monitoring services ([read more about Industrial IoT](https://en.wikipedia.org/wiki/Industrial_internet_of_things)) to opening our platform to developers that can leverage our technology to create their own solutions and services.
It is not easy to build a platform, less to build an open platform. Flexibility and stability are key factors. We have found so far that with Timescale (and PostgreSQL underneath), we have been able to bend our data models and data serving needs to implement the new use cases for the platform without pain.

We design and build our sensors in-house (down to the chip), and they’re ruggedized for harsh settings and can operate indefinitely from low levels of energy harvested from heat or light. This means our customers’ devices can continuously stream asset health data, despite radio interference and physical obstacles — like equipment, ducts, and pipes — common in industrial settings.

Since they charge themselves, these sensors stay operational well beyond what’s possible with traditional, battery-powered Industrial IoT devices. We ingest data from thousands of sensors** **into Timescale, then surface it to our customers through dashboards, charts, and automated alerts.

Our [initial products](https://everactive.com/solutions/) are designed to monitor steam systems, which are used in various industries and applications, like process manufacturing, chemical processing, and district energy, as well as a range of rotating equipment, such as motors, pumps, fans, and compressors. Currently, we serve large, Fortune 500 manufacturers in many sectors, including Food & Beverage, Consumer Packaged Goods, Chemical Process Industries, Pharmaceuticals, Pulp & Paper, and Facilities Management.

We show customers their data through a web-based dashboard, and we also have internal applications to help our in-house domain experts review and label customer data to improve our automated failure detection.

# About the Team
We’re a small team of software and data engineers, spanning the Cloud and Data Science teams at Everactive.

Between us, we’ve got several decades of experience managing databases, pipelines, APIs, and various other bits of backend infrastructure.

# About the Project
Our key differentiator is that our sensors are batteryless: the custom low-power silicon means that they can be put in more places, without requiring servicing for well over a decade.

In turn, this means that we can monitor factory devices that were formerly cost-prohibitive to put sensors on, due to the difficulty or cost associated with charging batteries; being able to collect data *economically* from more equipment also means that our industrial data streams are more detailed and cover more equipment than our competitors’.

Today, customers place our sensors on steam traps and motors, and we capture a range of metrics — from simple ones, like temperature, to more complex ones, like 3D vibrational data. (You can learn more about steam trap systems and the need for batteryless systems in [this overview video](https://youtu.be/2M79gELukfU).)

*Everactive’s new generation of sensors in the wild, including a sensor on a hydraulic arm with a shipping container and, below, a sensor on a shipping container clasp closer up*
We then use this data to inform our customers about the health of their industrial systems, so they can take action when and where required. “Action” in this sense could mean replacing a steam trap, replacing a bad bearing in a machine, or various other solutions to problems.

For example, we’ll automatically alert customers if their monitored equipment has failed or if machines are off when they should be on, so customers can send a crew to fix the failure, or power on the machine remotely.

In addition to receiving alerts from us, customers can use our dashboards to check the latest data and current status of their equipment at any time.

*One of Everactive’s dashboards, tracking the overall vibration level*
As mentioned earlier, our team’s responsible for delivering these intuitive visualizations to our customers and in-house domain experts — as well as for feeding sensor metrics into our custom analytics to automate failure detection and improve our algorithms.

# Using (and Choosing!) TimescaleDB
Before TimescaleDB, we stored metadata in PostgreSQL and our sensor data in OpenTSDB. Over time, OpenTSDB became an increasingly slow and brittle system.

Our data is very well-suited to traditional relational database models: we collect dozens of metrics in one packet of data, so it makes sense to store those together. Other time-series databases would force us to either bundle metrics into JSON blobs (making it hard to work with in-database) or to store every metric separately (forcing heavy, slow joins for most queries of interest).

**TimescaleDB was an easy choice because it let us double down on PostgreSQL, which we already loved using for metadata about our packet streams.** We looked briefly at competitors like Influx but stopped considering them once it was clear TimescaleDB would exceed our needs.
Our evaluation criteria were pretty simple: will it handle our load requirements, and can we understand how to use it? The former was easy to test empirically, and the latter was essentially “free” as TimescaleDB is “just” a PostgreSQL extension.

This “just PostgreSQL” concept also lets us carefully manage our schema as code, testing and automating changes through CI/CD pipelines. We use [sqitch](https://sqitch.org/), but popular alternatives include [Flyway](https://flywaydb.org/) and [Liquibase](https://www.liquibase.com/). We like sqitch because it encourages us to write tests for each migration and is lightweight (no JVM).

We previously used [Alembic](https://alembic.sqlalchemy.org/en/latest/), the migration component of the popular [SQLALchemy Python ORM](https://www.sqlalchemy.org/), but as our TimescaleDB database grew to support many clients, it made less sense to tie our schema management to any one of them.

We maintain a layer of abstraction within TimescaleDB by separating internal and external schemas.

“The capacity of Timescale to support both traditional schemas and time-series data in the same database allowed us to consolidate into one storage solution”

Our data is stored as (hyper)tables in internal schemas like “packets” and “metadata,” but we expose them to clients through an “API” schema only containing views, functions, and procedures. This allows us to refactor our data layout while minimizing interruption in downstream systems by maintaining an API contract. This is a well-known pattern in the relational database world — yet another advantage of TimescaleDB being “simply” a PostgreSQL extension.

# Current Deployment & Future Plans
*Another example of an Everactive dashboard*
We use [Timescale](https://www.timescale.com/cloud) and love it. We already used PostgreSQL on Amazon RDS and didn’t want to have to manage our own database (OpenTSDB convinced us of that!).

It had become normal for OpenTSDB to crash *multiple times per week* from users asking for slightly too much data at once. **TimescaleDB is clearly much faster than our previous OpenTSDB system. More importantly, nobody has ever crashed it.**

One not-very-carefully-benchmarked but huge performance increase we’ve seen?

We have a frontend view that requires the last data point from all sensors: in OpenTSDB, it required nearly 10 *minutes* to load (due to hard-to-fix tail latencies in HBase), and our first TimescaleDB deployment brought that down to around 7 *seconds*. Further improvements to our schema and access patterns have brought these queries into the sub-second range.

“We moved those schemas from Amazon RDS for PostgreSQL to Timescale. The migration was very simple: moving among PostgreSQL schemas was straightforward”

We have been able to maintain sub-second responses even with the growth of data volume: that’s very good for us. Also, thanks to compression and [continuous aggregates](https://www.timescale.com/blog/an-incremental-materialized-view-on-steroids-how-we-made-continuous-aggregates-even-better/), we have been keeping our table sizes in check and with great performance.

✨

Editor’s Note:For more comparisons and benchmarks, seehow Timescale compares to Amazon RDS for PostgreSQL. To learn more and try Timescale yourself, see our[.]step-by-step Timescale tutorial
Timescale has been so good for us that it’s triggered a wave of transitions to managed solutions for other parts of our stack.** We’ve recently moved our Amazon RDS data into Timescale to further simplify our data infrastructure and make it easier and faster to work with our data.**

About 20 % of our data is metadata kept in a relational database. We moved those schemas from Amazon RDS for PostgreSQL to Timescale. The migration was very simple: moving among PostgreSQL schemas was straightforward.

We chose RDS from the beginning for simplicity. Eventually, once we had Timescale up and running, it became evident that we didn’t need two separate PostgreSQL vendors when we were having such good results with Timescale.

The capacity of Timescale to support both traditional schemas and time-series data in the same database allowed us to consolidate into one storage solution. The instances multiply because we keep three environments (development, staging, and production) for each database, so we went from six (three RDS plus three Timescale) to only three Timescale instances.

As you’ll see in the below diagram, our sensors don’t talk directly to TimescaleDB; they pass packets of measurements to gateways via our proprietary wireless protocol. From there, we use [MQTT](https://mqtt.org/) to send those packets to our cloud.

From our cloud data brokers, [Kafka](https://kafka.apache.org/) processes and routes packets into TimescaleDB (and Timescale), and our TimescaleDB database powers our dashboard and analytics tools. We also added a third component: outbound channels for our platform users.

*Everactive architecture diagram*
Compared to Amazon RDS for PostgreSQL, Timescale also consolidates a lot of the costs associated with operating our instance in AWS — we now have a simpler bill that makes it easier to forecast costs.

From the operation point of view, dealing with fewer instances and relying more on the Timescale Support Team for infrastructure maintenance has reduced our database maintenance workload significantly. Our security operations also benefited from the migration, again thanks to the consolidation and the transfer of certain responsibilities to Timescale.

✨ *Editor’s Note: **Read how our Support Team is raising the bar** on hosted database support.*

We’ll continue to innovate on our technology platform and increase Everactive’s product offerings, including improving our sensors’ wireless range, lowering power requirements to increase energy harvesting efficiency, integrating with additional sensors, and shrinking device form factor. These successive chip platform enhancements will allow us to monitor the condition of more and more assets, and we’re also developing a localization feature to identify *where* assets are deployed.

Ultimately, Everactive’s mission is to generate new, massive datasets from a wealth of currently un-digitized physical-world assets. Transforming that data into meaningful insights has the potential to fundamentally improve the way that we live our lives — impacting how we manage our workplaces, care for our environment, interact with our communities, and manage our own personal health.

# Advice & Resources
If you’re evaluating your database options, here are two recommendations based on our experiences. First, if you have enough time-series data that a general database won’t cut it (millions of rows), TimescaleDB should be your first choice. It’s easy to try out, [the docs are great](https://docs.timescale.com/), and the [community](http://slack.timescale.com/) is very helpful.

Second, don’t underestimate the importance of using solutions that leverage a wide knowledge base shared by many/most backend developers. The increase in team throughput and decrease in onboarding time afforded by TimescaleDB — everyone knows at least *some *SQL — in contrast to OpenTSDB — an esoteric thing built on HBase — has been a huge advantage. We expected this to some degree, but actually experiencing it firsthand has confirmed its value.

Additionally, the use of schema-as-code tools and an internal/external schema separation discussed above have also been cornerstones of our success. We hadn’t been using these tools and patterns at Everactive previously but have since seen them catch on in other projects and teams.

*Want to read more developer success stories? **Sign up for our newsletter** for more Developer Q&As, technical articles, tips, and tutorials to do more with your data — delivered straight to your inbox twice a month.*
*We’d like to thank Carlos, Dan, Clayton, and all of the folks at Team Everactive for sharing their story (special shoutout to Brian, Joe, Carlos, Greg, and Elise for your contributions to this piece!). We applaud your efforts to bring sustainable, cost-effective sensors and easily actionable data to organizations around the world 🙌.*
*This blog post was originally published **here** in February 2021 and updated in February 2023 to reflect Everactive’s data stack and business evolution.*