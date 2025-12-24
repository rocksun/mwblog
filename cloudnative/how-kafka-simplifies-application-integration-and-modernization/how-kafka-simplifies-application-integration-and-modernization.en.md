In enterprises, applications execute business processes and often create data as a side effect. Traditional business reporting uses this data to provide financial insights and help improve processes and products. But application data is often fragmented and siloed across complex enterprise application estates. In addition, it can be difficult to pull the data out of the application database or the SaaS service it lives in.

![Enterprise application data fragmented into disconnected siloes.](https://cdn.thenewstack.io/media/2025/12/882b9af7-image4-1024x475.png)

Enterprise application data fragmented into disconnected siloes.

Individual users and data engineers often build custom, batch-oriented data pipelines for specific use cases. Fragmentation, duplication and inconsistencies across these application data silos and pipelines prevent data sharing and reuse.

Data locked up in a single application that can’t be shared with other applications will be harder to reuse compared to data that can easily be shared across the enterprise. Shared data can become reusable building blocks for new and improved applications, services and products. This drives better decision-making, improves business processes and product design, and reduces risk.

What’s needed is a way to move enterprise application data to a centralized, shared, open platform that can:

* Decouple sources from destinations to reduce complexity.
* Store shared data that can easily be reused by existing and new applications.
* Leverage shared data as events to drive application behavior.
* Integrate shared data with existing application data sources.
* Allow access to shared data in a real-time stream, historical batch or both as necessary.
* Achieving more reuse in a short period of time by exploiting simple, repeatable data-sharing use cases.

![Enterprise data integrated with Kafka.](https://cdn.thenewstack.io/media/2025/12/816c018e-image3-1024x536.png)

Enterprise data integrated with Kafka.

## Kafka Is the Centralized, Shared, Open Platform You Need

Data architects are looking for shared, real-time, event-driven and open data platforms that are widely used, proven and open source or based on open source protocols.

Apache Kafka decouples data sources from destinations, eliminating point-to-point complexity. Producers publish events to topics without knowing consumers, and consumers subscribe independently, removing direct dependencies and the need to modify applications. Topics become building blocks for event-driven applications and analytics.

Kafka’s event-driven, pub-sub model allows teams to add or change data flows without touching source systems or existing pipelines. In contrast, REST APIs are more synchronous and require tighter integration with application software. This can increase [development times and risk](https://www.morling.dev/blog/the-synchrony-budget/).

![Kafka data sharing between application publishers and subscribers.](https://cdn.thenewstack.io/media/2025/12/d301d035-image2-788x1024.png)

As open source software with a vast ecosystem of connectors and tools, Kafka enables enterprise-wide standardization, allowing any team or application to share and reuse data with fewer custom integrations or vendor lock-in.

Kafka stores data durably as an immutable log, turning transient events into [reusable building blocks](https://www.infoq.com/articles/rethinking-medallion-architecture/) accessible to existing and future applications. With configurable retention, topics can preserve full history or recent windows, enabling replay for onboarding new systems or recovering from failures.

Legacy ERP systems can also benefit from Kafka by streaming order events using Kafka Connect for analytics, fraud detection or new AI services without re-extracting data from the source. This shared, persistent data layer breaks silos and turns application data into enterprise capital ready for broad sharing and reuse.

Kafka can deliver both real-time streaming and historical batch access while improving data reusability using simple, repeatable use cases. Real-time consumers power dashboards or alerts. Kafka can move data to open lakehouses like Apache Iceberg for reporting and analytics.

The faster data can be reused, the faster new projects can happen. Quick wins — such as syncing a database to a search index or feeding logs to security tools — can be deployed quickly using prebuilt connectors. These low-risk, high-impact patterns scale predictably, reducing integration costs and accelerating innovation, including AI experimentation and deployment, all without infrastructure overhauls or disruptive application changes.

## How Data Architects Can Use Kafka in Application Integration

Data architects can use Kafka for application integration, modernization and evolution. Some companies are using a simple pattern to achieve this, called an entity builder*.*

An entity represents a “noun” in the business domain (such as Customer, Order, Product, Employee, Department, Invoice). It is unique, described by a set of attributes and exists independently or dependently in the system. Business processes are built around entities, their relationships and attributes.

Applications store entities and their relationships in a database. After corporate acquisitions or the onboarding of new SaaS applications, it’s common for the same entities, like a customer, to be spread across multiple applications. Merging applications is often impractical. Instead, architects let each application specialize its operations to a particular process or service, but use Kafka to build a centralized log that allows the sharing of common entities.

If the entity is a “Customer,” each application saves all its “Customer” records to a topic and accounts for any changes made to these records. The changes can be fed to a simple event-driven microservice, or you can write or extend a monolith to handle it. Ideally, you’ve done some data modeling work up front to make sure the business owners, data engineers and developers are on the same page on what a “Customer” is and what attributes a customer has in each application. But you don’t have to do a lot of data modeling to get started and to get value.

## Simple Data Modeling To Support Data Liberation

Think about the simple use cases first. Get the application owners together to build a data model around a shared understanding of the “Customer” entity. They need to identify and agree on what a customer is. Sounds simple, right? But things can get complicated fast, and you want to document this as precisely as possible up front before you start the design work.

Your application owners might be reluctant to consider sharing their data. If cajoling the app owners to work together doesn’t work, find a senior executive who can be sold on the business benefits that can move the needle. It can help to point to the business value and opportunities from sharing this information in a Kafka system.

For example, in the financial services industry, let’s assume we have four applications for banking, credit cards, investments and payments. To better understand the meaning of a “Customer” entity across these applications, a data modeling process could ask the following questions:

* What customer identifiers (social security number, date of birth, passport number) are shared across applications and are unique to each customer?
* What information associated with the unique identifier can we use to create a primary key for joins across all application customer entities?
* What attributes are most useful outside the specific application and should be denormalized and shared with the customer entity?
* What customer information would improve the business impact of their application?
* What information shared should be protected from inappropriate access based on privacy, security and compliance requirements?
* As you develop derived or aggregated values for your data model, make sure the values and dimensions are calculated consistently.

![Liberated application “Customer” entities shared via Kafka.](https://cdn.thenewstack.io/media/2025/12/a25f9faf-image1-1024x550.png)

Liberated application “Customer” entities shared via Kafka.

Once you have the shared data model and understanding of the customer entity, you can create Kafka topics based on this shared model from each application. Then the streams can be joined so that two or more streams, one from each company containing customer IDs, can be used with a particular selection of columns/attributes for the use case at hand. This is an example of how the data modeling process also incorporates the materialized views you want for downstream applications. It also shows the event-driven data integration’s power to support new use cases with liberated data.

## Simple Application Development, Incremental Changes

For “Customer,” you can detect any change (new address, changed balances, new payments, etc.) and generate an event to another microservice to handle that particular change (broadcast address updates to other apps, generate offers based on the new address, compliance-related work, etc.).

This is a simple way to get started.

But make sure to finish the project to the end. Then evaluate what went right and what went wrong. Is there a pattern in requests from users you couldn’t meet due to something missing in either your event model or data product? What were the biggest implementation challenges? Did you choose the right data product? Did you contextualize the events in a way that matched consumption patterns? What is the next entity that could be externalized in a data stream that might add value to the existing one (“Customer” in our case)?

This data liberation approach avoids changing monoliths like legacy applications or their data models. You can continue to use it for operations, but modernize around it.

It lets you start building event-driven applications, simple but useful ones, right away. And real-time data sharing between applications becomes possible.

## Conclusion

Integrating new data into existing, mature applications has never been an easy task. But Kafka provides mechanisms to solve this problem using building blocks that emphasize sharing and reusability.

The simple act of sharing event data across applications with Kafka creates business value without requiring expensive or complex application changes. It provides opportunities to modernize enterprise data incrementally with reusable data building blocks.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/04/ad287650-matthewokeefe.jpg)

Matthew O’Keefe is a principal technologist in the Technology Strategy Group at Confluent, working on data modeling, schema discovery and management, and Kafka integrations with relational databases. Prior to Confluent, he was on the database engineering team at Oracle, working...

Read more from Matthew O’Keefe](https://thenewstack.io/author/matthew-okeefe/)