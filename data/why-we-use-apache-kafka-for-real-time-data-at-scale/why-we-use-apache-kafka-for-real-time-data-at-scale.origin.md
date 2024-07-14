# Why We Use Apache Kafka for Real-Time Data at Scale
![Featued image for: Why We Use Apache Kafka for Real-Time Data at Scale](https://cdn.thenewstack.io/media/2024/07/8eb38c8c-kafka-real-time-data-scale-1024x576.jpg)
In a world where digital threats are constantly evolving, having accurate, real-time data for security scanning cannot be overstated. Up-to-date data is the lifeblood of [SecurityScorecard](https://securityscorecard.com/). The company provides organizations with a comprehensive view of their security posture by drawing from internet sources to identify potential vulnerabilities, including exposed servers, suspicious IP addresses, compromised employee accounts, malware-infected devices and more.

To keep up with the ever-increasing number of security threats, SecurityScorecard analyzes over 300 types of issues and identifies 200+ billion security vulnerabilities every day. The data collection and processing require not just large amounts of data, but also accurate, real-time data at scale. This need led SecurityScorecard to adopt [data streaming](https://www.youtube.com/watch?v=_RcnZ2XfuXw) and use a combination of Confluent Cloud and Confluent Platform to build streaming data pipelines to scale faster and govern data better.

## Real-Time Pipelines for Data Streaming and Processing
SecurityScorecard builds solutions that mine data from digital sources to identify security risks. Data streaming helps the company detect constantly evolving threats by analyzing information within milliseconds, instead of weeks or months. The company built its platform on open source [Apache Kafka](https://thenewstack.io/ditching-databases-for-apache-kafka-as-system-of-record/) because there is no other system that provides the fundamental tools to build anything that’s needed.

SecurityScorecard’s threat research team used to self-manage Kafka, but spending eight hours a day on upkeep detracted from product development time. The team relied on batch [pipelines to transfer data](https://thenewstack.io/the-unfortunate-reality-about-data-pipelines/) to and from [AWS](https://aws.amazon.com/?utm_content=inline+mention) S3. They also used expensive REST API-based communication for data exchange between systems and RabbitMQ for stream processing activities.

To lighten their load, SecurityScorecard’s threat research development team created [Horus](https://support.securityscorecard.com/hc/en-us/articles/8528362400539-How-SecurityScorecard-collects-data-for-ASI), its global distributed system capable of running any agent-based code anywhere in the world, on top of Confluent. Horus uses real-time streaming pipelines and connectors to process data. The team writes Python-based applications deployed as agents on this system. Currently, these agents are deployed worldwide to perform tasks like IPv4 scanning, web crawling, vulnerability detection and API integrations with partner data feeds.

Since building Horus, SecurityScorecard has saved more than $2 million in streaming infrastructure compared to managing open source Kafka in-house.

Beyond Horus, the threat research team at SecurityScorecard has implemented every [new system and refreshed old systems](https://support.securityscorecard.com/hc/en-us/articles/8528362400539-How-SecurityScorecard-collects-data-for-ASI) on the streaming platform. Some of these include Deep and Dark Web-leaked credentials, collections of leaked passwords and hacker chatter, and global passive sensor data from honeypots in over 90 countries syncing to Kafka. In addition, [BreachDetails](https://support.securityscorecard.com/hc/en-us/articles/19200200869915-Use-BreachDetails-to-respond-faster-to-breaches-in-your-ecosystem), a bespoke breach-incident collection system that monitors the public web and government sites to find data breach notices, lets customers know when their vendors have experienced a security incident.

## Amplification of Data Governance and Efficiency
Data governance is vital to SecurityScorecard. The company uses a custom-built Protobuf library to manage access to sensitive data. SecurityScorecard’s goal is to enable multiple teams to share and govern the same source data more easily. Confluent’s Stream Governance capabilities and role-based access controls will allow the data platform team to control access to the cluster. As data governance becomes increasingly granular, SecurityScorecard can scale streaming to more teams for enhanced security.

Confluent plays a key role in SecurityScorecard’s ability to scan and crawl the web, pushing billions of records from databases tracking breaches. This allows any team to “replay” the data. Fully managed connectors, including [PostgreSQL](https://roadmap.sh/postgresql-dba) and AWS S3 Sink connector, enable teams within the company to access streaming data for diverse purposes. These source connectors create [data archives that act as a historical](https://thenewstack.io/historical-data-and-streaming-friends-not-foes/) record of assets, and link data sources together in real-time for a consistent data layer across the business.

The efficiency of a fully managed system has freed up two full-time roles at SecurityScorecard. One new product, the Attack Surface Intelligence (ASI) module, aggregates petabytes of streaming data from SecurityScorecard via Confluent and pushes it to data sinks via Kafka Connect to allow customers to search the entire internet for open ports, vulnerable machines, threat actors, malware and other information. Another product, Automated Vendor Detection (AVD), processes web crawler and partner data in real time to provide a complete view of a customer’s supply chain security, highlighting connections between the customer and their vendors via data streams.

## Overcoming Data Bottlenecks in a Hybrid Cloud Environment
Previously, [Brandon Brown](https://www.linkedin.com/in/brandon-brown-8529681b/), principal software engineer on SecurityScorecard’s architecture team, faced significant challenges upgrading Kafka versions and managing Amazon Managed Streaming’s (MSK) operational needs. These tasks consumed valuable time during scaling that could have been spent developing business applications.

MSK was not meeting SecurityScorecard’s operational needs and doing something like version upgrades was very difficult and manual. The team needed to figure out cluster size and ran into challenges in deciding the number of brokers to set up.

Since moving to Confluent Cloud, these difficult tasks — like cluster and connector management — became simpler and more reliable. Solving this operational equation, Brown estimates his team saves about $125,000 a year. The migration also alleviated additional operational overhead, with an 80% reduction in Day 2 operational burdens — and an overall 48.3% reduction in projected annual operating costs.

Large JSON files also presented a challenge in building data pipelines. They required extensive processing time. Brown developed a fan-out process to place messages in specific topics with a schema, allowing teams to subscribe to specific topics and consume the data from a Kafka cluster more quickly. Now, Brown’s team consumes binary messages that require no filtering.

## Unmatched Scalability and Data Governance
SecurityScorecard used to scan 80 ports in a month and a half, but now can scan over 2,000 ports in 10 days. This achievement helped the company secure new customers that needed access to extensive data. It also simplified the company’s system and scaled ingested and processed data 10x to 100x.

Moving forward, the threat research and data platform teams have been using streaming data pipelines to enhance data discovery and shareability across all teams. In partnership with the core engineering team, they plan to leverage [Apache Flink](https://thenewstack.io/3-reasons-why-you-need-apache-flink-for-stream-processing/) to reduce custom service deployments for simple join tasks, enhancing real-time data processing, consolidating observability and cutting infrastructure costs.

## Advice for Building Trustworthy and Real-Time Streaming Data Pipelines
When building streaming data pipelines, you should establish the definition of timeliness, always use schemas when interfacing with other teams, leverage the ecosystem, and only develop and maintain what is absolutely necessary.

Timeliness is important because it constrains how quickly you need to react in the case of an issue, and also allows you to define realistic service-level agreements (SLAs) to identify anomalies. Schemas ensure that your consumers know the shape of what they are getting and allow teams to set data quality rules to flag issues early. Leveraging the ecosystem lets you tap into a wealth of knowledge and battle-hardened systems.

While you can write an application to sync data to a data store, by using connectors, you can implement parallelism retry logic and dead-letter queues for free. Otherwise, you have to write the application *and* the tests, and set up appropriate alerting and monitoring. You end up maintaining a system that takes you away from developing business value with data. Using a managed data streaming platform eliminates these problems, so you can focus on innovating instead of infrastructure management.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)