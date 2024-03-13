# Meet DBOS: A Database Alternative to Kubernetes
![Featued image for: Meet DBOS: A Database Alternative to Kubernetes](https://cdn.thenewstack.io/media/2024/03/633f0359-dbos-1024x703.png)
Turing Award laureate
[Dr. Mike Stonebraker ](https://www2.eecs.berkeley.edu/Faculty/Homepages/stonebraker.html)just keeps on inventing databases. Forty years ago, it was [the first relational system, Ingress](https://thenewstack.io/dr-michael-stonebraker-a-short-history-of-database-systems/), and thirty years ago, it was [PostgreSQL](https://thenewstack.io/postgresql-15-merge-ahead/), More recently, he co-created an in-memory transactional database system, [VoltDB](https://thenewstack.io/voltdb-adds-geospatial-support-cross-site-replication/).
Now, he’s back with a database system designed to replace the entire cloud native computing stack,
[DBOS](https://www.dbos.dev/) (Database Operating System).
Linux
[is too old](https://thenewstack.io/linus-torvalds-remembers-the-days-before-open-source-2/), and [Kubernetes](https://thenewstack.io/managing-kubernetes-complexity-in-multicloud-environments/) [is](https://thenewstack.io/developer-portals-can-abstract-away-kubernetes-complexity/) [too](https://thenewstack.io/dont-let-kubernetes-complexity-stall-your-cloud-momentum/) [complicated](https://thenewstack.io/how-to-fight-kubernetes-complexity-fatigue/), the start-up behind this work has proclaimed. Now a database has been designed to replace all of them.
To make this vision happen,
[DBOS, Inc.](https://www.dbos.dev/), has raised $8.5 million in seed funding led by [Engine Ventures](https://engineventures.com/), along with [Construct Capital](https://constructcap.com/), [Sinewave](https://sinewave.vc/), and [GutBrain Ventures](https://www.gutbrainventures.com/).
The project was founded by Dr. Stonebraker, along with
[Apache Spark](https://thenewstack.io/matei-zaharia-qa/) creator (and [Databricks](https://thenewstack.io/databricks-sees-and-raises-snowflake-with-gen-ai-llmops-more/) co-founder and CTO, [Matei Zaharia](https://people.eecs.berkeley.edu/~matei/)), and a joint team of MIT and Stanford computer scientists.
DBOS
[runs operating system services on top of a high-performance distributed database](https://docs.dbos.dev/). All state, logs, and other system data are stored in SQL-accessible tables.
The result is a scalable, fault-tolerant, and cyber-resilient
[serverless](https://www.thenewstack.io/serverless) compute cloud for cloud native applications, the creators claim.
With an OS running on top of a distributed database, you get fault tolerance, multinode scaling, and state management. Observability and security gets easier. Gone are containers and orchestration layers.
“You write less code because the OS is doing more for you,” Stonebraker said.
Today, distributed systems on largely built on an operating system (Linux) designed to run on single server. This results in an incredible number of different variable states to manage, across the infrastructure stack (app data, authentication systems, messaging, cluster management).
This fragmented nature of course necessitates an untold amount of observation tools, and security tools, as all the states gives malicious hackers a fertile ground to work with.
What could handle a million states with ease? A database, of course.
In the DBOS design, a high-performance distributed OLTP would implement a suite of OS services. It would run on a minimal OS kernel, with support for memory management, device drivers, interrupt handlers, and basic tasks of byte management.
## One Database to Rule Them All
This is not the first time this idea has been raised: As early as 2001, we recall Larry Ellison arguing that middleware was a “
[nitwit idea](https://www.washingtontechnology.com/2001/07/oracle-battles-the-middleware/345552/),” that everything should be managed by a database itself.
The central idea behind this DBOS project comes from a simple idea: Keeping track of the operating system state should be a database problem, Dr. Stonebraker said.
The idea came about from a talk from Zaharia. He noted that the Databricks cloud service for Apache Spark routinely managed a million subtasks at once. All the state and scheduling information was being tracked in a PostgreSQL database, the sluggish performance of which had frustrated the admin team at Databricks.
The database bottleneck could be solved easily enough. In fact, that’s what
[VoltDB was all about](https://github.com/VoltDB/voltdb), concurrent [ACID-compliant](https://thenewstack.io/an-apache-cassandra-breakthrough-acid-transactions-at-scale/) transactional processing that could be spread across multiple servers.
Back in the day, Dr. Stonebraker was an early user of Unix on a PDP 11/40 with 48k of main memory, and 25MB of disk memory. Then, all the states were kept by Unix itself. Of course, a million states is a jump of six orders of magnitude compared to the PDP. But “the amount of the amount of state that the operating system has to keep track of is basically proportional to resources,” Dr. Stonebraker said.
DBOS itself was tested on the Massachusetts Institute of Technology’s
[SuperCloud](https://supercloud.mit.edu/), with over 32,000 processors, terabytes of main memory and lots more terabytes of secondary storage.
At the bottom of the stack is a distributed transactional database system, with a file system, scheduling engine and messaging system all built on top.
They researchers discussed the stack at the
[Very Large Databases Conference 2023](https://vldb.org/2023/?program-schedule), detailing the work in a set of papers, covering ACID [transactions](https://www.vldb.org/pvldb/vol16/p2742-kraft.pdf) and [system replay.](https://www.vldb.org/pvldb/vol16/p3085-li.pdf)
Dr. Stonebraker labeled Linux as “leaky,” meaning there are
[many ways](https://thenewstack.io/leaky-vessels-vulnerability-sinks-container-security/) in which [security vulnerabilities](https://thenewstack.io/zero-day-vulnerabilities-can-teach-us-about-supply-chain-security/) can [be introduced](https://thenewstack.io/lynis-run-a-security-audit-on-linux-for-free/). Plus, building an OS on top of a database would offer the ability to roll back to a state before a vulnerability has been exploited (Think of it as an [Apple Time Machine](https://support.apple.com/en-us/104984) but for servers).
The centralized database will also help in debugging, Dr. Stonebraker said. Breaking applications into microservices
[makes them very hard to debug](https://thenewstack.io/return-of-the-monolith-amazon-dumps-microservices-for-video-monitoring/) or even to get the unwarranted behavior to show up on each test (these are known as “ [Heisenbugs](https://thenewstack.io/an-amazon-anomaly-that-metastasized-into-a-server-eating-monster/)“)
“We run all your microservices transactionally. So parallel microservices are sorted out by our concurrency control system and, basically, there are either no Heisenbugs or they’re much, much harder to run across,” Dr. Stonebraker said.
Originally, the system was mocked up on VoltDB, but he backers wanted to go with an open source key-value system instead, so they went with
[FoundatiolDB](https://www.foundationdb.org/) as the base. (Dr. Stonebraker admitted that any PostgreSQL wire-compatible distributed OLTP system would work, such as, say [CockroachDB](https://www.cockroachlabs.com?utm_source=tns&utm_medium=sponsor&utm_campaign=brand-pipe-tns-sponsor-page-description&utm_content=lp-homepage-learn-more&utm_term=prosp&utm_content=inline-mention)).
## DBOS Cloud: A Distributed Database for Transactional Support
The first commercial service built around is DBOS Cloud, a transactional Functions as a Service (FaaS) platform, available for developers in this initial launch.
DBOS, which runs on
[Amazon Web Services](https://aws.amazon.com/?utm_content=inline-mention)‘ [Firecracker](https://thenewstack.io/aws-wants-its-open-source-firecracker-to-become-faster/), is initially available for developers to experience via DBOS Cloud, which launched today.
DBOS Cloud is a transactional serverless application platform powered by the DBOS operating system, and it can be used to build and run serverless functions, workflows, and applications. Think of it as
[AWS Lambda](https://thenewstack.io/going-serverless-on-aws-lambda-recognize-potential-risks/) but with transactional support. ![](https://cdn.thenewstack.io/media/2024/03/013ae632-dbos-image-1-jpeg.jpg)
DBOS makes fault-tolerant TypeScript code vastly easier to create and less expensive to run (DBOS).
The service provides the following benefits:
- Support for stateful functions and workflows
- Built-in fault tolerance with guaranteed once-and-only-once execution
- Time-travel debugging
- SQL-accessible observability data
- Enablement of cyberattack self-detection and self-recovery
A
[GitHub repository](https://www.dbos.dev/) includes some of the tools the company has developed, including a [ TypeScript framework](https://github.com/dbos-inc/dbos-ts) for interacting with DBOS, and the “ [time-traveler debugger”](https://github.com/dbos-inc/#:~:text=DBOS%20Time%20Travel%20Debugger%20extension%20for%20VS%20Code) for VSCode. ![](https://cdn.thenewstack.io/media/2024/03/0f1ac164-dbos-image-2jpeg.jpg)
DBOS Cloud keeps a complete audit trail of code and data processing and stores it in encrypted SQL tables. The DBOS Cloud Time Travel Debugger allows that data to be replayed and examined to troubleshoot issues, ensure regulatory compliance, or look for fraud, etc. (DBoss)
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)