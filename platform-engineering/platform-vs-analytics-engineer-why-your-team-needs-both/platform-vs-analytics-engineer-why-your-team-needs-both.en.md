Leaders often assume one data engineer can do it all — from raw ingestion to polished dashboards. That assumption is why many data initiatives fail before they start.

Data engineering is not a single role, but a set of distinct responsibilities across the medallion architecture: Bronze, silver, and gold. Treating it as a single job often leads to broken pipelines, frustrated teams, and stalled initiatives.

Ashok has spent years on the data side, leading cloud [migration projects and seeing firsthand the gaps in data](https://thenewstack.io/planetscale-rewind-an-undo-button-for-bad-schema-migrations/) engineering skill sets. He’s watched as leaders, desperate for cloud experience, hire for specific tools like BigQuery, Snowflake, Databricks, or Airflow, only to find their new hires struggling with the foundational software engineering needed for a reliable platform.

Gaurav, on the other hand, has led [platform engineering teams](https://thenewstack.io/platform-teams-start-small-to-win-big/) tasked with building large-scale data platforms from scratch. His teams, composed primarily of platform engineers, excelled at building robust ingestion pipelines but hit a wall with data modeling and business logic, revealing the inverse of the problem.

Together, our experiences from opposite ends of the spectrum reveal a critical divide: the skills that build reliable data infrastructure (Bronze and Silver) are fundamentally different from those that deliver business insights (Gold).

## The Software Engineering Foundation of Bronze and Silver Layers

The bronze layer is where data lands in its rawest form: Messy JSON dumps, Kafka streams, or domain-specific feeds, such as healthcare HL7 messages. The silver layer transforms that chaos into trustworthy, governed data through deduplication, schema enforcement, and lineage tracking.

These layers demand the rigor of a production-grade software system:

* **Reliable Data Movement:** Understanding change data capture (CDC), stable ingestion pipelines, and the correct configuration of messaging systems.
* **Robust Testing:** Writing unit tests for transformations and integration tests for end-to-end flows, not just simple validation scripts.
* **Automation:** Managing infrastructure as code (IaC) and deploying via CI/CD pipelines to avoid hidden, manual configurations.
* **Observability:** Implementing deep logging and lineage enables the quick detection, diagnosis, and recovery from failures.

From Ashok’s experience leading migrations, a common pattern emerges. **Many [data engineers are strong with Python](https://thenewstack.io/a-cloud-built-for-python-data-scientists-not-infrastructure-engineers/) for PySpark and SQL, but they lack the skillset to write unit tests, design complex frameworks, or handle infrastructure automation.** When a project begins, these engineers often spend months learning IAM, IaC, and CI/CD from scratch, leading to costly mistakes and significant tech debt. This doesn’t mean they are bad engineers; it means they are the wrong fit for building the foundational Bronze and Silver layers, where engineering discipline is essential.

Conversely, Gaurav’s experience shows the other side of the coin. His team of platform engineers did an excellent job building a platform to get data reliably into the Bronze layer using CDC and Kafka. But the journey from there was hard. **They faced challenges with tools like dbt and SQL Mesh and struggled with data modeling concepts like star schemas and lineage preservation.** Progress was limited until they brought in specialized data engineers and analysts to help them navigate the domain of business logic and analytics.

This contrast reinforces our point: Bronze and Silver require [engineers with strong software engineering foundations](https://thenewstack.io/ai-driven-software-why-a-strong-ci-cd-foundation-is-essential/), whereas Gold requires a distinctly different set of skills.

This is the domain of a Platform Engineer (or a Software Engineer specializing in data). Their world is one of distributed systems, reliability, and automation. They ensure the data “factory” runs on time, every time.

## The Business-First Nature of the Gold Layer

By the time data reaches the gold layer, the battle with chaos is mostly over. Now it is about telling a story. The gold layer is where cleaned and governed data is turned into business-ready insights. This is where models capture revenue, churn, product usage, and marketing KPIs that drive real decisions.

The skills here are different:

* Success is measured not by robust CI/CD pipelines, but by how quickly and accurately business questions can be answered.
* SQL fluency, BI tool expertise, and business acumen take center stage.
* Excelling at this layer requires the ability to design models and metrics that match how the business views the world.
* Teams built only from strong software engineers often struggle here, because gold requires domain knowledge and analytical intuition in addition to technical skills.

The gold layer thrives when engineers operate more like analysts with an engineering discipline, rather than engineers trying to stretch into analytics. This role is often called an Analytics Engineer. They are a hybrid of a data analyst and a software engineer, using tools like dbt to translate business logic into reliable, well-documented data models.

## Why Leaders Must Stop Hiring One-Size-Fits-All Data Engineers

This is where leadership makes the difference. Too many companies treat data engineering as a single role, expecting one person to wrangle raw event streams, build reliable pipelines, and design business dashboards. That expectation sets teams up for failure.

A better approach is to think in terms of skill profiles. The easiest way to surface these differences is during hiring, through the kinds of questions you ask.

**Bronze/Silver (Platform Engineer) interview questions might include:**

* How would you design an idempotent data ingestion pipeline?
* How would you test a complex [data transformation that pulls from multiple sources](https://thenewstack.io/data-commons-can-save-open-ai/)?
* Tell me about a time you had to debug a distributed data system like Kafka or Spark. What was the issue, and how did you resolve it?

**Gold (Analytics Engineer) interview questions might include:**

* The product team wants to change the definition of a “daily active user.” Walk me through the technical steps and communication plan you’d use.
* Here’s a messy dataset and a business question. How would you model this in SQL to answer it reliably?
* How do you balance the need for a “perfect” data model with the business’s need for a “good enough” answer right now?

The best team structures reflect this split. A central **Data Platform team**, staffed with Platform Engineers, owns the Bronze and Silver layers as a reliable service. **Analytics Engineers** either sit in that team or are embedded in business units like Product or Marketing, where they work closely with stakeholders to build the Gold layer. The key is that these roles, responsibilities, and career ladders are distinct, and leaders must treat them that way.

## Building Complementary Data Teams for Lasting Value

Data engineering is not a single role. Bronze and silver layers demand the rigor of software engineering, while gold depends on business context and analytical expertise. Too often, leaders look for one hire to cover it all and end up with gaps, delays, and tech debt.

The sooner leaders stop searching for unicorns and start building complementary teams, the sooner their [data platforms will scale](https://thenewstack.io/scale-data-platforms-with-a-kubernetes-first-approach/) reliably and deliver lasting business value. Leaders who hire for layers, not unicorns, build resilient platforms and empowered teams. That choice is the difference between data chaos and data as a true competitive advantage.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/10/ff70beb5-cropped-e4acc1c4-ashok_singamaneni_photo-scaled-1-600x600.jpg)

Ashok Singamaneni is a Principal Data Engineer and open-source innovator specializing in large-scale data platforms, AI-driven engineering, and distributed systems. He is the co-author of Brickflow - a Databricks-native orchestration framework, and Spark-Expectations - a PySpark data-quality library — together...

Read more from Ashok Singamaneni](https://thenewstack.io/author/ashok-singamaneni/)

[![](https://thenewstack.io/wp-content/uploads/2025/10/e2204003-cropped-05f46027-gaurav-nanda-bio-image-600x600.png)

Gaurav Nanda is an Engineering Manager at Databricks, where he leads the Networking Platform Infrastructure organization that enables large-scale, reliable connectivity for data and AI workloads. His work focuses on service discovery, overload protection, and developer-productivity systems that power Databricks’...

Read more from Gaurav Nanda](https://thenewstack.io/author/gaurav-nanda/)