Most data processing frameworks are built on a single execution engine. Not Apache Wayang.

Last week, The Apache Software Foundation [debuted](https://news.apache.org/foundation/entry/the-apache-software-foundation-announces-new-top-level-projects-3?ref=dailydev) the [Wayang data processing framework](https://wayang.apache.org/) as a top-level Apache project.

Named after Indonesian puppet theater, Wayang is a data processing framework built for unifying sets of data with its ability to orchestrate multiple data processing frameworks.

For an organization with a lot of data systems, this software is a bit of a Swiss Army knife, able to [execute different types of jobs](https://wayang.apache.org/docs/introduction/benchmark) depending on the needs at hand. It speaks both SQL and Java.

“In Wayang, users can specify any data processing application using one of Wayang’s APIs and then Wayang can choose the data processing platform(s), e.g., Postgres or Apache Spark, that best fits the application,” the GitHub site [explains](https://github.com/apache/incubator-wayang). “Wayang will orchestrate the execution, thereby hiding the different platform-specific APIs and coordinating inter-platform communication.”

Wayang can be used to run federated [SQL queries](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/) across different relational databases. Or, it could pick the most cost-effective processing platform for a given job, and then run that job. For optimal results, it can even break up a job to run across multiple platforms.

“Users face a zoo of specialized platforms to perform data analytics. They typically run their data analytics at a higher cost than necessary, as selecting the right platform is daunting,” some of the technology’s creators wrote in a [2023 paper](https://sigmodrecord.org/publications/sigmodRecord/2309/pdfs/05_Systems_Beedkar.pdf), explaining the need for the technology. “Furthermore, modern applications often require to perform data analytics that goes beyond the limits of a single platform, making the selection of platforms even more difficult.”

(The originator of Wayang, [Dr. Jorge-Arnulfo Quiané-Ruiz](https://www.tu.berlin/en/dima/news-details/in-memoriam-jorge-arnulfo-quiane-ruiz), died unexpectedly in 2023.)

The new project status, “combined with strong community momentum, positions us to enhance the project and reach even more developers,” said [Zoi Kaoudi](https://itu.dk/~zoka/), Apache Wayang PMC Chair, in a statement.

## Wayang’s Three-Layer Abstraction

Wayang’s three-layer architecture wedges an abstraction between an application and supporting data systems, where it can make rule-based decisions about what systems should execute a given job, and then orchestrates those jobs.

[![diagram](https://cdn.thenewstack.io/media/2025/12/a178a58d-wayang-stack-1024x457.png)](https://cdn.thenewstack.io/media/2025/12/a178a58d-wayang-stack-1024x457.png)

Data processing happens at the platform layer, but the platform selection is done through Wayang.

In this setup, the application holds business logic as usual, but the underlying core layer acts as an intermediary, translating application logic into an intermediate representation called a “Wayang plan.”

A cross-platform optimizer automates data system selection. The user doesn’t have to worry about the specific platform being used for the task.

This allows the application to use and intermingle multiple processing engines into one pipeline. For instance, [Apache Flink](https://thenewstack.io/building-real-enterprise-ai-agents-with-apache-flink/), [Apache Spark](https://thenewstack.io/the-good-bad-and-ugly-apache-spark-for-data-science-work/) and [Tensorflow](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/) can all be used together in a single job. Wayang then orchestrates the work.

## One Workflow, Multiple Engines

Data is stored within a single repository, and performance can be enhanced by selectively offloading data to more powerful engines.

Take, for example, a common [deep learning](https://thenewstack.io/demystifying-deep-learning-and-artificial-intelligence/) task: executing a [stochastic gradient descent](https://www.geeksforgeeks.org/machine-learning/ml-stochastic-gradient-descent-sgd/) algorithm. This algo is basically a set of Map/Reduce functions interspersed with some parsing work.

The Wayang query optimizer can determine which of these jobs would best be executed on Apache Spark, and which would be done more efficiently through a single Java process.

It translates the Wayang plan into a specific workflow, weighing in factors such as operating costs and data movement costs, with the goal of minimizing total costs.

Costs can be measured in terms of energy consumption or the compute costs of the runtime execution. By default, Wayang uses linear cost formulas but the user can plug their own optimizer, perhaps a machine learning (ML)-based one.

[![Workflow diagram](https://cdn.thenewstack.io/media/2025/12/48060cd2-wayang-optimizer-1024x225.png)](https://cdn.thenewstack.io/media/2025/12/48060cd2-wayang-optimizer-1024x225.png)

The Wayang optimizer (Wayang).

The frameworks that Wayang currently supports:

* Apache Flink
* Apache Giraph
* GraphChi
* Java Streams
* JDBC-Template
* Postgres
* Apache Spark
* SQLite3

## Commercialization of Wayang

One of the chief committers of the project, [Kaustubh Beedkar](https://web.iitd.ac.in/~kbeedkar/), helped [launch a company](https://www.youtube.com/watch?v=opZdul64pt4) around the technology, Scalytics. Scalytics uses Wayang [as the basis](https://www.scalytics.io/blog/apache-wayang-more-than-a-big-data-abstraction) for the federated data processing feature in its [Scalytics Streaming Intelligence](https://www.scalytics.io/federatedintelligence) platform, marketed to extend the Databricks platform out for edge platforms.

In effect, Wayang can be used to create a “virtual data lake,” according to the company.

“The ultimate goal is to replicate the success of [database systems] for cross-platform applications: users formulate platform agnostic data analytic tasks and an intermediate system decides on which platforms to execute each subtask with the goal of minimizing cost such as runtime or monetary cost,” [noted](https://www.scalytics.io/blog/apache-wayang-more-than-a-big-data-abstraction) the company literature.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

In addition to Wayang, ASF also announced that the [Apache Artemis](https://artemis.apache.org/) messaging platform is now an Apache TLP.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)