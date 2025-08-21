I often hear companies say they need to act faster — ideally in real time — with limited resources. They tell me they are excited about the possibilities of using event-driven architecture to move faster and increase agility. Many have adopted [Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/) or other event-streaming technologies, but have hit a wall in their execution.

After a few years in the event automation space and working with companies at all stages of their event-streaming journeys, I have seen how event management as part of a hybrid integration strategy can help solve these common challenges. Below are four key insights I’ve gathered.

## **Insight 1: Timely Data Is Key to Success**

### The Challenge

Having [real-time data](https://thenewstack.io/ai-powered-event-processing-the-key-to-winning-in-real-time) is critical in today’s fast-paced business environment. The value of data declines rapidly with time, especially in areas like customer actions, transactions, supply chain activity and security events.

### The Solution

Events, as discrete records of what just happened, are the most immediate and context-rich form of data. When integrated into business processes or [leveraged in the context of AI](https://thenewstack.io/how-agentic-ai-is-reshaping-api-self-discovery), they can help enable powerful capabilities like real-time fraud detection, inventory forecasting, personalized customer engagement and automated anomaly detection in operations.

## **Insight 2: Kafka Sprawl Is Costly**

### The Challenge

Many organizations find themselves entangled in operational and governance challenges as they scale their use of Apache Kafka and other event-streaming technologies. These issues often stem from independently deployed Kafka clusters, often from multiple vendors, leading to redundant or duplicate event streams that inflate infrastructure costs. Additionally, security vulnerabilities emerge due to fragmented access controls.

### The Solution

Event automation offers a centralized approach to managing Kafka topics across multiple vendors in a hybrid multicloud landscape. Capabilities may include:

* **AsyncAPI support** enables standardized, machine-readable topics, making them easily discoverable and facilitating unified and consistent governance of the [API and events estate](https://thenewstack.io/why-every-api-strategy-needs-graphql).
* **A reusable event catalog** allows teams to search and self-service event streams, promoting reuse over reinvention, and helping to accelerate development and increase consistency across apps to drive greater return on investment (ROI).
* **An event gateway** enforces security policies, data validation and subscriber controls.
* **Topic virtualization** creates multiple controlled views of the same topic for different consumers, simplifying management and governance and optimizing resource utilization.
* **Interoperability** supports managing Kafka topics from any Kafka-compatible vendor, including IBM, [Confluent](https://www.confluent.io/?utm_content=inline+mention) and Cloudera.

These capabilities help organizations tame event sprawl, encourage reuse and establish a robust governance layer – helping the business to address unwanted costs and inefficiency.

## **Insight 3: Centralized Visibility and Control Help Unlock Developer Agility**

### The Challenge

As event streaming grows in popularity, teams often fear that implementing governance features will stifle developer speed.

### The Solution

Event endpoint management (EEM) helps you establish a strong governance layer without compromising developer agility. By offering centralized visibility, governance and control for Kafka topics, it helps users manage event flows securely and at scale, preventing the architecture from becoming fragile and siloed. Rather than restricting access, it empowers developers and teams with secured, self-service capabilities, enabling them to discover, subscribe and reuse event streams securely and efficiently. Helpful capabilities can include:

* **Centralized subscription control** to ensure proper access without slowing teams down.
* **Secure schema registry integration** to promote consistency and compatibility.
* **Self-service event cataloging** so that developers can discover and reuse topics.
* **Unified governance** across APIs and events, eliminating silos between integration layers.

These help developers move fast while prioritizing governance or compliance.

## **Insight 4: Event Management Spans Every Industry**

Across industries, enterprises are applying event-management capabilities to effectively gain real-time insights, streamline operations and boost AI and machine learning (ML) effectiveness without needing to compromise on costs, security or governance:

* **Retailers** are using event streams for real-time inventory management and to analyze buying behavior. Endpoint management enables this data to be shared across sales, marketing and analytics teams, promoting security and consistency.
* **Banks** apply policy controls through endpoint management to protect sensitive data in Kafka topics used for fraud detection and prevention.
* **Healthcare providers** generate events when a patient is admitted, discharged or transferred, alerting staff and insurers to coordinate care transitions. Endpoint management is used with sensitive personal information that needs to be redacted.
* **Government agencies** use event-driven analytics to make informed decisions from various sources, such as sensors, social media and public feedback.

The real-time enterprise isn’t just a vision. It’s becoming the standard. With the right tools and event management practices, you can get there fast.

[IBM webMethods Hybrid Integration](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.427436753;dc_trk_aid=620568046;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1) includes [IBM Event Automation](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.427260868;dc_trk_aid=620569540;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24%7BGDPR%7D;gdpr_consent=%24%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1)’s event endpoint management capabilities in an integration platform as a service (iPaaS) that can turn your event streams into a controlled, reusable and future-ready foundation for AI, automation and modernization. Explore how IBM can help your team make the most of your real-time data:

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Matt Sunley is a program director of product management for IBM Event Integration. He has been working for IBM, based at the Hursley Lab in the UK, for over 20 years. Having started with a software engineering focus, he developed...

Read more from Matt Sunley](https://thenewstack.io/author/matt-sunley/)