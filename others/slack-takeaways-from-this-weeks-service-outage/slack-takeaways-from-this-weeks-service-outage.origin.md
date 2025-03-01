# Slack: Takeaways From This Week’s Service Outage
![Featued image for: Slack: Takeaways From This Week’s Service Outage](https://cdn.thenewstack.io/media/2025/02/1cf9b338-slack-logo-outage-2-1024x576.png)
On Wednesday morning, our coworkers at The New Stack started asking each other, in meetings and via panicked emails: Hey, are you having trouble with [Slack](https://api.slack.com/?utm_content=inline+mention)?

Turns out we weren’t alone. The instant-messaging application suffered a widespread service outage, which took its engineers nearly nine hours to resolve, according to the tick-tock account of the incident [posted on the service’s status website](https://slack-status.com/2025-02/1b757d1d0f444c34), which began at 10:47 a.m. U.S. Eastern time.

The New Stack is an [all-remote organization](https://thenewstack.io/build-a-highly-productive-work-from-anywhere-dev-team/), with employees and contributors scattered across the globe; as a result, we rely heavily on Slack to keep us connected. So do users in more than 150 countries. [Slack](https://thenewstack.io/developer-guide-a-new-way-to-build-on-the-slack-platform/), owned by Salesforce, reports that 77 of the Fortune 100 use the messaging service. Slack users include [Airbnb](https://thenewstack.io/how-airbnb-and-twitter-cut-back-on-microservice-complexities/), [Target](https://thenewstack.io/target-embraces-cross-organizational-devops-culture/), [Uber](https://thenewstack.io/devpod-ubers-monorepo-based-remote-development-platform/) and the U.S. Department of Veterans Affairs.

What caused the outage? And what lessons can other engineering teams draw from the incident?

Slack has not publicly revealed the cause of the outage other than the updates it posted on its site during the incident. The company has also not responded to The New Stack’s questions about the outage.

“Remediation work involves repairing affected database shards, which are causing feature degradation issues,” read a Slack status update at 4:04 p.m. EST on Wednesday. “This has become a diligent process to ensure we’re prioritizing the database replicas with the most impact.”

At 7:42 pm EST, the company posted that it had “restored full functionality to all affected Slack features such as sending messages, workflows, threads and other API-related features.”

But the work continued to get back to normal service. On Thursday, it[ posted an update](https://slack-status.com/2025-02/d41e4bfd1ccae26a) timestamped 10:17 a.m. EST, alerting users that events created during the downtime “are queued and currently paused. We expect this to take time and will update hourly on progress made. Apps and integrations continue to function as normal for new submissions and events.”

## The Problem With MySQL
In the absence of a fuller explanation from Slack, what do we know about what could have gone wrong this week?

Here’s what we do know: The Slack app was first introduced in 2013, and from the beginning, [according to a post published in December 2020](https://slack.engineering/scaling-datastores-at-slack-with-vitess/) on the Slack engineering blog, it used [MySQL](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/) as the storage engine for its data. In 2017, it started migrating its data storage to Vitess, an open source database scaling system for MySQL.

As the company grew, the post read, “our application performance teams were regularly running into scaling and performance problems and having to design workarounds for the limitations of the workspace sharded architecture.”

The decision to migrate to Vitess was driven by a common problem organizations face as they scale: how disruptive it would be to abandon its legacy technology. It was deeply wedded to MySQL.

“At the time there were thousands of distinct queries in the application, some of which used MySQL-specific constructs,” read the blog post written by Slack engineers [Rafael Chacón](https://www.linkedin.com/in/rafaelchaconvivas/), [Arka Ganguli](https://www.linkedin.com/in/arkag/), [Guido Iaquinti](https://www.linkedin.com/in/guidoiaquinti), and [Maggie Zhou](https://www.linkedin.com/in/zmagg/). (Chacón and Zhou are now at [Figma](https://www.figma.com/), Ganguli is at [Notion](https://www.notion.com/), and Iaqunti is co-founder of [SafetyClerk](https://safetyclerk.com/)).

“And at the same time we had years of built-up operational practices for deployment, data durability, backups, data warehouse ETL, compliance, and more, all of which were written for MySQL.

“This meant that moving away from the relational paradigm (and even from MySQL specifically) would have been a much more disruptive change, which meant we pretty much ruled out NoSQL datastores like [DynamoDB](https://thenewstack.io/diving-into-aws-databases-amazon-rds-and-dynamodb-explained/) or [Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/), as well as NewSQL like Spanner or [CockroachDB](https://thenewstack.io/how-doordash-migrated-from-aurora-postgres-to-cockroachdb/).”

But likely, sticking to a sharding model may have laid the groundwork for outages like Wednesday’s suggested [Spencer Kimball](https://thenewstack.io/qa-cockroach-labs-spencer-kimball-on-distributing-sql/), co-founder and CEO of [Cockroach Labs](https://www.cockroachlabs.com?utm_source=tns&utm_medium=sponsor&utm_campaign=brand-pipe-tns-sponsor-page-description&utm_content=lp-homepage-learn-more&utm_term=prosp&utm_content=inline-mention).

In Slack’s status updates during Wednesday’s incident, “they mentioned problems with corrupted database shards,” Kimball told The New Stack The word “shard,” he said, indicates that “basically what you do is you have a lot of customers, a lot of data, way too much to put into one single, monolithic database. So you create lots and lots of databases, and you call them shards.

“And so you say, ‘OK, well, customers one through 100 are on shard one, and 100 through 200 are in shard two,’ and so forth, right? Problem is, you’re kind of in the position of managing 100 databases. So you don’t just have one database. You’ve got 100 of them, and all of them are separate. They’re siloed, which is actually a huge problem, because you might have a customer that’s too big to fit on one shard.”

And in that case, there are tradeoffs, Kimball said. On the one hand, “when you lose a shard, you only lose a subset of your customers. But the problem is, you’ve got 100 things to manage, and they all do have their own unique kind of weirdness, because different customers have different ways of using them.”

## Testing What Went Wrong
The flagship product of Kimball’s company, CockroachDB, is a distributed SQL database management system. So he has a vested interest in promoting his product, and in storing data differently than Slack does — in a single, distributed database designed for horizontal scaling, with data redundancy built in.

But he also offered some insight into why Slack’s legacy architecture might be encountering problems with complexity and resilience.

“I don’t know how many shards Slack has, but I imagine there’s quite a few at this point,” he said. “They have become essentially a database company as well as a corporate messaging company, because of the thing they’ve built that accommodates this idea of shards and the resilience on each one of those shards.

“When you have one of these things, every piece of code you write, every new feature you write, it has to also deal with the underlying, exposed reality of this complex architecture that you’ve cobbled together, that, by the way, doesn’t work together. It’s not one integrated, holistic whole.”

If you’re a company like Slack, that’s deeply invested in a MySQL data storage system, with hundreds or thousands of shards, what can you do to prevent service calamities like the one it experienced Wednesday?

“Whatever just happened to them, this should be part of their standard testing process,” Kimball said. The testing crew should focus improving its Recovery Time Objective (RTO), shortening it from the nine-ish hours it took Slack to restore most services after Wednesday’s outage.

Something to keep in mind, he said: “It’s not like Slack is anywhere unique. Everywhere saw these outages that have been happening this year. It’s insane. From the [[Federal Aviation Administration](https://www.reuters.com/business/aerospace-defense/us-faa-pilot-safety-messaging-system-resumes-operations-2025-02-02/)], to [Barclays](https://www.reuters.com/world/uk/britains-lloyds-bank-says-customers-hit-by-payments-service-outage-2025-02-03/) and [Capital One](https://fortune.com/article/capital-one-service-outage-january-2025-update/), everyone has outages.

“But the question is, OK, whatever just happened, let’s routinely test that. And when we have our runbooks and we apply them, what can we optimize our RTO to?”

If organizations can even test their database infrastructure quarterly or twice a year, Kimball said, and ensure that their teams can fix service outages and have visibility into how long it takes to resolve them, ”then you at least know when you’re regressing a little bit, and you know what the cost is going to be when this inevitably happens again.”

Deploying your backup database on a different cloud than the primary database is another best practice, he said.

## The Cost of Resilience
Another issue organizations face, he noted, is that the standard for [resilience](https://thenewstack.io/cdn-outages-exploring-ways-to-increase-resilience/) keeps changing. Ten years ago, when Cockroach Labs was founded, the standard was “let’s survive a data center going away. Because that’s pretty common: Like, when [Google](https://cloud.google.com/?utm_content=inline+mention) started off, it’s like, hey, let’s survive a node or a physical machine failing or something.

“Then it’s, ‘Let’s survive data centers going away. Then it’s, ’Hey, people want to survive [whole regions going away](https://thenewstack.io/google-cloud-services-hit-by-outage-in-paris/).’ And it’s like, now people want to survive whole cloud providers going away.”

Not enough organizations test their systems quarterly or twice a year for resilience, and there’s a good reason why, Kimball said. “It’s expensive to do these things.”

It’s not the simply money at stake, he added, but staff time. Testing and re-architecting a legacy system may not be as important to a company, compared to creating new features and services.

“Some companies decide, let’s just keep our fingers crossed. It might not be a terrible answer, if they’re really under some serious constraints. It’s like, we’ll take the egg on our face if things go wrong and we’ll hope for the best.

“It just depends on what your use case is and what you think the cost will be from the downtime. [For] financial services, that’s not an option anymore, especially with regulator scrutiny. For Slack, you know, maybe they’re going to stay on their thing because it’s just too hard to move. Eventually, you have to modernize things, and they’ll just find the right time.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)