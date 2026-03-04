Confluent recently unveiled support for the Agent2Agent (A2A) protocol, an open standard for inter-agent communication. The platform’s implementation of the popular protocol allows users to employ [Apache Kafka](https://thenewstack.io/apache-kafka-4-1-the-3-big-things-developers-need-to-know/) to orchestrate inter-agent communication via A2A.

With this paradigm, agent calls can trigger event-based actions using Confluent’s Streaming Agents, a collection of capabilities for designing and deploying agents that instantly respond to changes in data’s state. Kafka also stores — in real-time — inter-agent communication for auditability and traceability.

> “If you’ve already invested in agents somewhere else, then this can be a facilitator if you want to turn that agent into an event-driven agent.”

[Sean Falconer](https://www.linkedin.com/in/seanf), the Head of AI at [Confluent](https://www.confluent.io/), tells *The New Stack* that one of the chief advantages of this approach — which was [announced](https://investors.confluent.io/news-releases/news-release-details/confluent-intelligence-expands-real-time-business-data) on February 26 — is that it democratizes the real-time capacity of Streaming Agents for agents devised outside of Confluent.

“If you’ve already invested in agents somewhere else, then this can be a facilitator if you want to turn that agent into an event-driven agent,” Falconer says.

These possibilities are enhanced by the addition of Confluent’s multivariate anomaly detection, which leverages machine learning techniques to analyze cross-variable patterns and identify patterns relevant to operations or business goals. According to Falconer, Kafka — which users can now use for messaging queues with a new Kafka Improvement Proposal (KIP), Queues for Kafka — underlies both capabilities and their synthesis.

“Whether that’s clickstream data or IoT data, as soon as it’s manifested, it’s in Kafka,” Falconer says. “When you combine that with things like anomaly detection and Streaming Agents, you can understand these key moments in the business that are happening, where you’d want to be able to apply AI in a way to create a personalized product or do root cause analysis.”

With Confluent’s A2A implementation, AI can involve any agent.

## How Kafka powers asynchronous A2A communication

A2A has both [synchronous and asynchronous protocols](https://a2a-protocol.org/latest/); Confluent supports the latter. According to Falconer, with this option, agents immediately respond to requests with their identification and can answer questions about whether they’ve completed a task. Because inter-agent communication is provided through [Kafka](https://kafka.apache.org/), users gain numerous advantages, including the ability to have a plethora of subscribers to that communication via Kafka topics. “You want to have it be able to go to your observability tools, your analytics tools, and Kafka’s a really good medium to do that,” Falconer says.

## System tables give agents a built-in audit trail

Kafka’s usefulness for inter-agent communication among multiple independent consumers revolves around its storage capabilities as much as its publisher/subscriber model via topics. Every decision a Streaming Agent makes is written in real time into a system table, which is essentially a Kafka topic with a specific schema for logging that information. Subsequently, “As the agent interacts, it’ll write everything down there,” Falconer explained. Systems tables are imperative for developers building, testing, and perfecting agents, and they also provide observability, traceability, and some explainability in regulated industries. Plus, with Kafka, “You can consume that down into your Open Telemetry system or analytics database,” Falconer says.

## Multivariate anomaly detection runs in the stream, not in a batch

The observability use case is bolstered by Confluent’s multivariate anomaly detection, which enables organizations to assess multiple factors and their relationships to determine whether occurrences are aberrational. According to Falconer, the sundry machine learning techniques that detect anomalous behavior are equally applicable to any data-driven event, including stock market changes. There are techniques that use time series analysis, such as Autoregressive Integrated Moving Average ([ARIMA](https://www.ibm.com/think/topics/arima-model)), as well as those that assess variability in the data, such as Median Absolute Deviation ([MAD](https://arxiv.org/abs/1910.00229)). Other measures take into account seasonality.

A significant benefit of utilizing these approaches is that “It’s not like you have to go and batch-train these,” Falconer says. “They start learning as soon as you turn them on in your streams.”

Additionally, because they rely on traditional statistical machine learning approaches — as opposed to deep neural networks at the scale of language models — Falconer says that “you can run many, many of these for low cost and they’re very high speed, which is great for doing things like monitoring IoT data.”

## Queues for Kafka: pub/sub and message queues in a single topic

Queues for Kafka ([KIP: 932](https://cwiki.apache.org/confluence/display/KAFKA/KIP-932%3A+Queues+for+Kafka)) extends Kafka’s scope to messaging queues, as opposed to its traditional publisher/subscriber methodology. One of the reasons this construct was devised was to simplify the architecture and technological stack for employing formal messaging queues with Kafka, which conventionally required additional infrastructure.

According to Falconer, “What Queues for Kafka might do is take the same topic that you used for log-based pub/sub and allow it to act as a queue. The topic will act like a single source of truth, and then you materialize it to serve whatever your data needs are.”

Although there is some overlap between log-based publisher/subscriber models and messaging queues, they ultimately require distinct semantics. Falconer clarified the difference between the two by likening them to two waiters in a restaurant, each assigned to work a separate set of tables.

> “It’s an important protocol, especially for the future where enterprise agents are going, where businesses are going to be running hundreds or thousands of these things across all kinds of enterprise systems.”

For the waiter analogous to the pub/sub model, even if he is late, only that waiter can take orders from that table. “But with queues, the semantics of it is more like a ticket counter at a deli,” Falconer says. “There’s no one who owns a certain number of the tickets. There’s just a ticket number, and whoever’s free comes and takes your order.”

Neither approach is better; they solve separate problems. Adding this functionality makes Kafka more viable for developers to support a burgeoning number of use cases, without unnecessarily adding infrastructure.

Confluent’s support of the A2A protocol is considerably enhanced by the vendor’s ongoing reliance on Kafka. The open source framework makes inter-agent communication instantly accessible and stores it for traceability, data governance, and auditability. With Queues for Kafka, agents can be as viable for queue-based messaging workloads as they are for those involving Kafka’s publisher/subscriber model. Confluent’s multivariate anomaly detection ensures organizations get low-latency insights across metrics, logs, and KPIs, which benefits almost any streaming data application.

Consequently, applying Kafka to A2A workloads for streaming data could become standard practice. “It’s an important protocol, especially for the future where enterprise agents are going, where businesses are going to be running hundreds or thousands of these things across all kinds of enterprise systems,” Falconer reflected.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/ee3e39b7-cropped-52925a32-jelani-harper-110x110-1.jpg)

Jelani Harper has worked as a research analyst, research lead, information technology editorial consultant, and journalist for over 10 years. During that time he has helped myriad vendors and publications in the data management space strategize, develop, compose, and place...

Read more from Jelani Harper](https://thenewstack.io/author/jelani-harper/)