# How OVHcloud Made Its 800 Databases More Efficient
![Featued image for: How OVHcloud Made Its 800 Databases More Efficient](https://cdn.thenewstack.io/media/2024/10/5291016d-how-ovhcloud-made-its-800-databases-more-efficient-2-1024x576.jpg)
At [OVHcloud](https://us.ovhcloud.com/), a French cloud services provider, a small dedicated database operations team is tasked with a critical mission: to ensure that internal product teams building the company’s control and data planes can access a resilient, scalable and high-performance database infrastructure.

In September at the [SREday](https://sreday.com/2024-london/) conference in London, [Wilfried Roset,](https://www.linkedin.com/in/wilfriedroset) OVHcloud’s engineering manager for databases and observability, told how the database operations team evolved from troubleshooting performance issues reactively to proactively optimizing database clusters, significantly reducing slow queries and improving observability.

OVHcloud’s database operations team has transformed the way it manages and optimizes its infrastructure. From enhancing observability to scaling hardware and reducing slow queries by 50%, it has successfully built a scalable and reliable database service that meets the needs of its internal product teams.

Its focus on continuous improvement, SQL optimization, and performance metrics driven by [service-level objectives (SLOs)](https://thenewstack.io/sre-fundamentals-differences-between-sli-vs-slo-vs-sla/) serves as a blueprint for database teams facing similar challenges at scale.

## The Challenge: A Growing Demand for Scalable Databases
OVHcloud offers a vast array of cloud services, and the internal product teams developing these services rely heavily on the infrastructure provided by the database operations team.

Rather than focusing on external customers, the database team’s clients are internal engineering teams, responsible for developing OVHcloud’s services. These teams, in turn, need fast, reliable access to databases to build their control planes and data-handling solutions.

With over 100 database [clusters](https://thenewstack.io/kubernetes-building-blocks-nodes-pods-clusters/) running in production, OVHcloud’s infrastructure is built on Kubernetes but can accommodate virtual machines and bare metal servers. It’s a flexible architecture designed to route read and write traffic efficiently through load balancers to dedicated nodes in each cluster.

The challenge, however, lies in maintaining optimal performance at scale, especially as the number of services and customers grows.

## The Infrastructure: Resilient, Flexible Database Clusters
The database clusters OVHcloud runs today typically consist of three nodes. A primary node manages write traffic, while the others handle read-only requests and backups. The architecture is shared across [PostgreSQL](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json/) and [MySQL](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/) databases, with each node designed to offload specialized workloads.

“The setup works well for us because it allows product teams to operate without having to think about database management,” Roset told the SREday audience. “We make sure the infrastructure scales as needed, supports backups and balances the load automatically.”

Product teams benefit from a database system that adapts to their needs, scaling as their services grow while maintaining reliability through efficient load balancing.

## Better Observability Needed
As demand increased, the database team began to experience bottlenecks. Product teams often reported performance issues, but diagnosing these issues proved difficult due to a lack of [observability](https://thenewstack.io/observability/).

“When the head of our public cloud team asked why their control plane was slow, we didn’t have immediate answers. We were SSH-ing into individual servers and tailing logs manually,” Roset said. This reactive troubleshooting was time-consuming and inefficient.

Recognizing the need for a more structured approach to monitoring, the database team implemented an observability stack, pulling logs from PostgreSQL and MySQL into an [OpenSearch](https://thenewstack.io/aws-transfers-opensearch-to-the-linux-foundation/) cluster and centralizing key metrics.

“We integrated system, database, and load balancer metrics into [Grafana](https://thenewstack.io/can-grafana-adaptive-metrics-help-slash-observability-costs/) dashboards,” Roset added. “This allowed us to visualize everything in one place, from slow query counts to overall system health.”

The observability stack gave the team the ability to track performance in real time and respond more quickly to issues, he said. “Before, we would only know about problems after they were reported by product teams. Now, we can see issues happening in real time and address them before they escalate,”

## Upgrading Hardware to Boost Performance
The improved observability revealed that many of the performance issues stemmed from inadequate hardware. As OVHcloud’s internal database workloads grew, the hardware supporting these workloads became increasingly strained.

The database team members realized that they needed to upgrade their infrastructure to better support the demands being placed on it. “We scaled vertically by upgrading to faster CPUs, adding more RAM, improving disk speeds and enhancing network throughput across all of our nodes,” Roset said.

These upgrades were essential to addressing the root cause of many of the performance bottlenecks. However, hardware improvements alone weren’t enough. Inefficient workloads, particularly poorly optimized SQL queries, continued to cause performance issues. This prompted the database team to take a more comprehensive approach to workload optimization.

## Optimizing SQL Queries Reduces Slow Queries by 50%
One area of improvement came from optimizing SQL queries. Initially, the team observed over 2 million slow queries per week on a single database. Armed with insights from its new observability tools, the team set out to reduce this number.

“We defined slow queries as those taking more than one second to execute, but as we optimized the workload, we gradually lowered that threshold to 250 milliseconds,” Roset said.

To tackle slow queries, the team launched a continuous query optimization initiative, analyzing logs each week and identifying the databases responsible for the highest number of slow queries.

Each Monday, Roset said, he would send out a report company-wide, highlighting the databases with the slowest-performing queries from the previous week. “It’s a way to keep everyone aware of the impact of poorly optimized queries,” he said. “If a team’s database consistently shows up on the report, they know they need to take action”

By providing visibility into the performance of specific databases and offering automated feedback to developers, the team was able to cut the number of slow queries from over two million to fewer than 1 million across more than 1,000 databases. “It’s been a huge success.

## SLOs: Establishing Clear Expectations
The team members’ journey toward optimization didn’t stop with better observability and query performance. They implemented SLOs for their database services, setting clear performance targets and ensuring that the databases meet the needs of the product teams they serve.

“We’ve defined SLOs around latency and availability,” Roset said. “For instance, we aim for 99.99% success on database connection attempts and have specific latency targets for query execution.”

To track these objectives, the team uses synthetic monitoring agents and patched [SQL Exporter](https://github.com/justwatchcom/sql_exporter/pull/121) that measures query execution times, providing real-time feedback into their monitoring systems.

This SLO-driven approach has helped the team maintain consistent performance, even as it scales. The synthetic monitoring system allows the data operations engineers to detect issues before they impact product teams and ensures that the databases remain highly available.

## Continuous Improvement: Looking to the Future
Although the database team at OVHcloud has made significant strides in optimizing its infrastructure and reducing slow queries, it continues to look for ways to improve.

One initiative currently underway is the development of a tiered service model, offering different levels of database performance based on how critical the workloads are. For the most critical systems, dubbed “vibranium clusters,” the team provides the highest level of performance and redundancy.

As OVHcloud continues to expand, the database team is also exploring ways to extend its approach to other types of databases, including key-value and columnar stores, to ensure that all of the team’s services benefit from the same level of optimization.

“We’ve made great progress, but we’re never done improving,” Roset said. “We’re always looking for new ways to optimize, scale, and provide better service to our internal teams.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)