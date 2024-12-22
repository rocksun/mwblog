# Amazon to Save Millions Moving From Apache Spark to Ray
![Featued image for: Amazon to Save Millions Moving From Apache Spark to Ray](https://cdn.thenewstack.io/media/2024/11/9632b561-patrick_ames-ato2024-1024x768.jpg)
For an e-tailer as large as Amazon, even small performance improvements reap significant savings.

By replicating data lake table compaction chores from [Apache Spark](https://thenewstack.io/enhancing-the-flexibility-of-sparks-physical-plan-to-enable-execution-on-various-native-engines/) to the Python-based [Ray](https://www.ray.io/) in the first quarter of 2024, the company found that they could be executed 82% more efficiently.

Given compaction is an essential feature for users of its in-house business intelligence services, the e-tailer may be able to save over 220,000 years of EC2 vCPU computing time. From a typical AWS customer’s perspective, this would work out to saving around $100 million annually in Amazon EC2 on-demand R6g instance charges.

Yes, Amazon uses that much BI internally.

[Anyscale: New Optimized Runtime for Ray, Kubernetes Operator]
Amazon Principal Engineer [Patrick Ames](https://www.linkedin.com/in/patrick-ames-05bb046/) discussed — in a talk at the [All Things Open 2024](https://allthingsopen.org/) conference, held last week In Raleigh, N.C. — [its migration to Ray](https://aws.amazon.com/blogs/opensource/amazons-exabyte-scale-migration-from-apache-spark-to-ray-on-amazon-ec2/).

His message? Ray is not just for building a machine learning pipeline; its current favored use.

“Ray, at its core, is a very general-purpose distributed compute framework that I’d argue could be good at almost any distributed systems area where you decide to magnify and focus its attention,” said Ames, who is also a contributor to the [Ray project](https://github.com/ray-project/ray).

## The Need to Compact
The move to Ray expedites one of Amazon’s most costly operations, compaction. Whenever a data lake table format like the Apache Iceberg or Apache Hudi offers a copy-on-write or merge-on-read functionality, eventually, it will use compaction to reconcile updates to the table.

Previously, Apache Spark did the job.

In his talk, Ames described how Amazon went from using a giant Oracle Data Warehouse in 2016 to running its own fully scalable exabyte-scale [data lakehouse](https://thenewstack.io/showdown-at-the-lakehouse-databricks-muscles-up-with-tabular/) while maintaining [ACID compliance](https://thenewstack.io/acid-transactions-change-the-game-for-cassandra-developers/). The idea was to decouple storage from compute, so database tables could be stored in S3 buckets and users could bring their own query engines.

Initially, the tables were updated through append-only statements, and soon, they grew too unwieldy for even the most robust platform to ingest.

So they put Spark to work rooting out duplicates, a job that, as it turns out, can be quite tricky.

“Finding duplicates is a simple enough problem in theory, but it turns out to get a little nasty when your data starts growing to petabyte scale and beyond, you can no longer fit on a single node,” Ames said.

The Business Data Technologies office within Amazon them looked to Ray for further optimization.

Like Spark, Ray came from the University of California Berkeley. A few of the researchers who worked on Ray went on to start [Anyscale,](https://www.anyscale.com/platform) which offers commercial support for the platform,

Ray had already found a home in the Amazon data scientists thanks to its Pythonic APIs and ability to work with large data sets. [Pandas](https://thenewstack.io/pandas-a-vital-python-tool-for-data-scientists/) are great for single node data sets, but building a data pipeline for a terabyte of data can be difficult, Ames explained.

This is where Ray comes in.

Basically, you take any [Python](https://thenewstack.io/what-is-python/) application that could be parallelizable, put annotations on it for tasks that are distributed functions and actors that are distributed classes, and you can now deploy that code to an arbitrarily large cluster, and it’ll manage a lot of cluster scaling for you,” Ames explained.

![Chart: Business Data Technologies](https://cdn.thenewstack.io/media/2024/11/d604e2bb-heterogenous-ray-clusters.png)
How the Business Data Technologies uses Ray to provision clusters (Amazon).

At Amazon, the technology has the possibility of one day being the “unified” compute framework for all Amazon’s data pipelines, Ames said.

## Amazon BI
Amazon’s internal data lake has “tens of thousands of users,” not only from AWS business analysts but also from partners as well.

Amazon’s Ray compactor currently runs over 25,000 jobs a day, requiring approximately 1.5 million EC2 vCPUs each day. About 40PBs of Apache Arrow data are merged each day, with a cost of about $0.59/TB.

The internal customers are charged per byte for the data they consume from the catalog, which pays for the maintenance of the data catalog. Surprisingly, the largest change in the costs comes from compaction.

“So we just kept throwing money at Spark, and the data sets grew in size,” Ames said, adding that it was not “the most elegant solution.”

The team investigated Ray, found promise there, and re-engined its compaction algorithm to run on the platform. They also investigated how Ray’s data science tools could help with data quality. A lot of Amazon’s code base is in Java, so there was considerable work that was done to create links to Ray’s Python API.

To date, Amazon has been running Spark and Ray compaction jobs in parallel to ensure consistency. This year, however, Spark will be mothballed and all operations will be moved to Ray.

## Results From Working With Ray
Early results showed a definite performance advantage for Ray.

The business unit had found that Spark compacted a GB of data in about 1/2 minute on an [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)‘ EC2 instance. But it would take Ray about a tenth of a minute, leading to what Ames characterized as an 82% efficiency gain based on data from Q1 2024.

![Chart of Ray vs. Spark in terms of efficiency (Amazon)](https://cdn.thenewstack.io/media/2024/11/6f40cf1d-ray-v-spark-efficiency-chart.png)
Ray vs. Spark in terms of efficiency (Amazon).

For these jobs, they also found that the Ray compactor consumed about 55% of a cluster’s total available memory, which Ames admitted was less than optimal, preferring to get it up to 80% or so. Each cluster of servers collectively provides about 36TB of available memory.

One area of concern was reliability, which could, in the words of Ames, “burn into your cost advantage” through the additional costs of rerunning jobs. Initially, in October of 2023, Ray’s first attempt to compact a table only succeeded85% of the time.

Again, not ideal, though by February of 2024, the team upped that to 99.15% which was closer to Spark’s 99.91%.

![Chart: Ray vs. Apache in terms of reliability](https://cdn.thenewstack.io/media/2024/11/00adbcea-ray-v-spark-reliability.png)
Ray vs. Spark in terms of reliability (Amazon).

When the migration is complete, it is projected to reduce its computational needs by roughly 220,000 years of vCPU time annually, which translates to about $100 million, in terms of the typical AWS customer’s Amazon EC2 on-demand R6g instance charges.

## The Future of Ray
Spark still has some advantages, Ames concluded. It still has more general-purpose data processing features than Ray. For instance, Ray still doesn’t have an easy interface for SQL. And so, some customization is still inevitable.

“You can’t just throw a Spark job on Ray and expect to get these kinds of performance gains,” Ames said.

The project team also plans to adapt the compaction algorithm to be used with [Apache Iceberg](https://thenewstack.io/snowflake-databricks-and-the-fight-for-apache-iceberg-tables/), which they hope to release in 2025.

“If any of you are writing iceberg tables using Apache Flink and then trying to read them back with Spark or something else, it should really improve that process a lot,” Ames said.

But overall, Ray is worth a serious look for large scale data operations.

“Ray core is flexible enough to let you craft very optimal solutions to very specific problems,” Ames said. “If you can focus on a particularly onerous and expensive problem that your organization has, it is probably a good area — if your business is willing to invest with you — to turn Ray’s magnifying glass onto that problem.”

*Update (11/08/2024): An earlier edition of this post incorrectly stated that Ray is an Apache project. It is not, but rather it is open source under the Apache license. *
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)