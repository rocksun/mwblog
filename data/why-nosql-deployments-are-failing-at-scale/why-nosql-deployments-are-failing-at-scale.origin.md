# Why NoSQL Deployments Are Failing at Scale
![Featued image for: Why NoSQL Deployments Are Failing at Scale](https://cdn.thenewstack.io/media/2024/10/963d1ed9-leif-christoph-gottwald-im8dxcck1sy-unsplash-1024x576.jpg)
[Leif Christoph Gottwald](https://unsplash.com/@project2204?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-bunch-of-television-screens-hanging-from-the-ceiling-iM8dxccK1sY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
Why does technology become obsolete? There’s no one answer. Sometimes, it’s surpassed by something strictly better. Other times, the underlying need evolves. Technology that serves the needs of an emerging market might prove insufficient when the market matures.

That’s what many businesses are discovering about [NoSQL](https://thenewstack.io/nosql-database-growth-has-slowed-but-ai-is-driving-demand/). And it’s why so many NoSQL implementations are struggling today.

Not so long ago, in the early days of big data, Hadoop was the name on everyone’s lips. Traditional SQL-based data stores were thought to be passé. Every venture-funded startup seemed to have a NoSQL key-value store under the hood. They followed in the footsteps of tech giants like Google, Facebook, and Yahoo, who developed NoSQL technology to manage their rapid growth. It was only natural for startups to reach for the tools that had powered their predecessors’ global success.

But a curious thing happened. The startups that succeeded started tossing their NoSQL databases overboard.

Consider the trajectory of Hbase, a database distributed as part of the standard Apache Hadoop package. Modeled on Google’s famed BigTable, HBase’s popularity soared for a few years and then steadily declined.

Looking at the chart above, one might assume that in 2017, a new database came along to supersede HBase — maybe one that [stored and accessed](https://thenewstack.io/leveraging-web-workers-to-safely-store-access-tokens/) data faster or could address more information. But that’s not what happened. HBase still stores and retrieves the best of them. Its decline in popularity has nothing to do with its raw power. It’s about the complexity of the problems its users are trying to solve.

In the early days of SaaS and big data, startups had their hands full just keeping up with customer growth. They needed an inexpensive [way to store and manage large](https://thenewstack.io/5-ways-ai-improves-knowledge-management/) amounts of high-velocity data. NoSQL tools like HBase filled that role admirably. But querying that data? Keeping it consistent? Those were problems for another time.

Eventually, that time arrived. When it did, it became apparent that companies built on NoSQL had a massive maintenance problem. They had trouble writing queries. Data became unreliable. New [applications were harder and harder to build](https://thenewstack.io/how-to-build-applications-over-streaming-data-the-right-way/). NoSQL, which was so cost-effective initially, began *imposing *costs as the business became more complex.

At this point, many of the companies running HBase were no longer startups. They had expanded worldwide. They had created platforms others used to build businesses. They were hiring data analysts. They were thinking in terms of downtime and SLAs. They weren’t just trying to keep data anymore. They were trying to use it.

That was when NoSQL’s limitations became evident — and a real concern.

For HBase, those included:

**Lack of transaction support:**This means users get none of the ACID properties typical of a modern relational database. Data can become corrupt or logically inconsistent. The more data you have, the harder it becomes to find the problem through brute force when data quality decays.**Lack of a secondary index:**HBase’s lack of secondary indexes means everything must be found via brute-force scan. Not a problem when you don’t need to find data. Not a problem when you have relatively small amounts of data. But when you need to find a needle in a terabyte-scale haystack, the lack of secondary indexes makes every query computationally expensive.**Single point of failure:**HBase’s use of the HDFS file system — with its centralized NameNode directory — created dependencies that made it dangerously vulnerable to crashing.**Unfriendly interface:**NoSQL’s lack of relational architecture is an asset when it comes to quickly storing data but a fundamental problem when it comes to querying it. NoSQL doesn’t eliminate the need for a relational schema. It just forces the burden onto the application, which is much more difficult and expensive to maintain. Altering an explicit SQL database schema with your data structure is much easier than modifying an implicit schema embedded within an application.
Over time, these fundamental issues with running NoSQL at scale became impossible to ignore. Some responded by trying to find a compromise solution. Newer NoSQL databases tried to layer structure over HBase’s key-value architecture, adding transactions with SQL or SQL-like capabilities.

As MIT’s Michael Stonebreaker [put it](https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf): “Despite strong protestations that SQL was terrible, by the end of the 2010s, almost every NoSQL DBMS added a SQL interface.” He adds: “Many of the remaining NoSQL DBMSs also added strongly consistent (ACID) transactions. As such, the NoSQL message has morphed from ‘Do not use SQL — it is too slow!’ to ‘Not only SQL’ (i.e., SQL is fine for some things).”

Over time, NoSQL products came to resemble their RDBMS counterparts. But essential differences remained. By definition, NoSQL solutions lack a schema. That’s both their strength and their weakness. The absence of a data schema enables fast storage and retrieval. It also makes analytics and transactions more difficult. If the schema isn’t realized within the database, it has to be instantiated in the query. If, for example, data needs to be sharded onto different servers, the change has to be reflected within the application code. Some NoSQL solutions allow a schema to be defined externally, but this approach is prone to error in practice. Schema migrations are fragile, hair-raising operations.

The difficulty of changing a database discourages new application development. It makes innovation harder, and few businesses will tolerate that for long.

Pinterest is a good example. It was an early adopter of HBase. At one point, according to a Pinterest Engineering [blog post](https://medium.com/pinterest-engineering/hbase-deprecation-at-pinterest-8a99e6c8e6b7), it was running “50 clusters, 9000 AWS EC2 instances, and over 6 PBs of data” on HBase. And HBase did the job. But over time, as Pinterest grew, it decided HBase’s shortcomings outweighed its benefits. It was too light on [features and cost too much to manage](https://thenewstack.io/whats-the-future-of-feature-management-feature-flags/). As other businesses started to come to the same conclusions, it became harder and harder to find HBase-savvy engineers. Ultimately, Pinterest migrated to an open source, MySQL-compatible distributed SQL solution called TiDB. In doing so, the company improved development velocity and query latency while making performance more predictable.

That might come as a surprise to some. For years, SQL labored under the misimpression that it is inherently slower and less efficient than NoSQL. But that’s simply not the case. Advances in cloud computing and horizontal scale-out have brought recent SQL solutions much closer to raw performance parity with their NoSQL counterparts while still providing all the advantages of an RDBMS. Rather than focusing on one dimension of database functionality — storage and retrieval — distributed SQL seeks to provide high performance across a wide range of transactional and analytical use cases, making it attractive to mature [businesses with complex needs](https://thenewstack.io/5-signs-your-business-needs-an-operations-intervention/) and a wide variety of stakeholders.

Ironically, in moving from NoSQL to distributed SQL, Pinterest and companies like it are following in Google’s footsteps, the same way they were when they adopted NoSQL in the first place. TiDB and other distributed SQL solutions are descendants of Google Spanner. This is software Google created to solve the problems of BigTable, the technology that gave rise to HBase.

In a way, the SaaS industry simply recapitulates the journey Google and other tech giants have been on for the past two decades. Here, we have a technology (SQL/RDBMS) supposedly made obsolete by another technology (NoSQL), which is now being displaced by a more modern iteration of the technology it ousted.

Who is to say the wheel might not turn again? To cite Stonebreaker one last time, “What goes around continues to come around. Another wave of developers will claim that SQL and the [relational model] are insufficient for emerging application domains. People will then propose new query languages and data models to overcome these problems.” But none, he points out, have ever seriously threatened to displace the SQL-based RDBMS.

It’s a useful reminder that over the years, the traditional relational database has proved remarkably capable of absorbing innovation, from clustering to [cloud to vector search](https://thenewstack.io/datastax-adds-vector-search-to-astra-db-on-google-cloud/). Trends in database architecture come and go, but somehow, when the dust settles, SQL always seems to be left standing.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)