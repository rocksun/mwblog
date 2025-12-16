IBM is no stranger to AI, given its long history with its [AI Watson project](https://thenewstack.io/ibm-tackles-shadow-ai-an-enterprise-blind-spot/) and countless other efforts. But today’s AI hits different.

On Monday, [IBM](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434371219;dc_trk_aid=627496700;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$%7BGDPR%7D;gdpr_consent=$%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1?utm_content=inline+mention) announced that it had begun the process of [acquiring](https://www.confluent.io/blog/ibm-to-acquire-confluent/) streaming data platform Confluent for US $11 billion, or $31 per share, chiefly for what it could bring enterprises in terms of supporting generative AI (GenAI).

Today, enterprise data “is spread across public and private clouds, data centers and countless technology providers,” said IBM Chairman, President and CEO [Arvind Krishna](https://www.linkedin.com/in/arvindkrishna/), in [an investor call Monday](https://www.ibm.com/investor/events/ibm-confluent). “With the acquisition of Confluent, IBM will provide the smart data platform for enterprise IT, purpose-built for AI.”

Such a platform will “connect, process and govern data for applications and AI agents,” according to the strategic vision of Big Blue.

Less than two months ago in New Orleans, [Confluent](https://www.confluent.io/?utm_content=inline+mention) held its annual Current user conference, where it shed some light about how AI operations have changed over time, and what may lie ahead.

## What Does Confluent Offer Enterprises?

With its stewardship of the open source [Apache Kafka project](https://kafka.apache.org/), Confluent provides a leading open source enterprise data streaming platform, one that can process and route data as it comes in, in real time, from multiple sources.

Confluent’s portfolio includes:

In each of the above deployment models, Confluent makes it easier for enterprises to master Kafka through additional services and tooling to simplify operations, enhance security, ensure data quality and accelerate application development.

The company has also invested a lot of effort into a Kafka-adjacent open source data processing technology, [Apache Fink](https://thenewstack.io/3-reasons-why-you-need-apache-flink-for-stream-processing/).

Confluent, based in Mountain View, Calif., has approximately 6,500 clients, 40% of which are in the Fortune 500, the company has estimated. Anthropic, [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), [Google Cloud Platform](https://cloud.google.com/?utm_content=inline+mention), [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) and [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) all count themselves as Confluent customers.

## IBM’s Strategic Plans for Confluent

Real-time contextual processing [will be invaluable](https://thenewstack.io/confluent-provides-a-real-time-context-engine-for-ai/) as enterprises roll out their GenAI projects, IBM is reasoning.

IDC has estimated that more than one billion new logical applications will emerge by 2028, and many of these new apps will produce data that will need to be analyzed, preferably in real time, to reap maximum value.

IBM told its investors that the Confluent purchase would accelerate IBM’s growth. Confluent has estimated that its own potential market, for real-time data processing, has doubled from $50 billion to $100 billion in 2025.

IBM would press the Confluent stack into its own Data and Automation portfolio. The company did a [similar deal earlier this year](https://thenewstack.io/ibm-to-acquire-datastax-to-boost-watsonx-ai-development/) to acquire Datastax for its scalable NoSQL database (and associated AI tooling).

[![Investor slide](https://cdn.thenewstack.io/media/2025/12/4e7bc34b-ibm-confluent-1024x404.png)](https://cdn.thenewstack.io/media/2025/12/4e7bc34b-ibm-confluent-1024x404.png) How IBM sees Confluent (IBM investor slide), a data streaming “pioneer” with robust enterprise connectivity.

In addition to real-time processing, Confluent also offers an advantage in enterprise data management, IBM envisions.

One of the issues that organizations face is the complexity of their data ecosystems, noted Confluent CEO and Co-Founder [Jay Kreps](https://www.linkedin.com/in/jaykreps/), in a press conference at Current.

A streaming platform is one way to put all of these sources of data in the same place.

“If you talk to customers, they’re actually often very frustrated with the complexity that has come out of the cloud provider offerings, where it’s like they have 500 products all from the same [company], but those 500 things don’t work together,” he said. “Where we’ve seen success is taking this problem of working with real-time data, and bringing together as many pieces of the puzzle as possible.”

## The Rise of Event-Driven AI

The purchase is about IBM enhancing its “technical acumen” around AI, said [Subbu Iyer](http://linkedin.com/in/iyersubbu), CEO of real-time AI database company [Aerospike](https://aerospike.com?utm_content=inline+mention), in a statement.

“AI models are hungry for more fresh, relevant, real-time data. Getting the right real-time data and putting it to work fast is the new competitive advantage,” Iyer said.

> “Every AI problem is essentially a data problem.”  
> **— Sean Falconer, Confluent**

In one talk at Current, [Sean Falconer](https://www.linkedin.com/in/seanf/), Confluent’s senior director of AI product, explained how AI has changed over time and how this has changed the operational requirements.

Models were once stagnant things, purpose-built to predict actions within one relatively static domain. GenAI overthrew that model, however. This approach uses a [general foundation model](https://thenewstack.io/introduction-to-llms/), but is continuously augmented by fresh information, via prompts and other contextual data.”It has different meanings in terms of how we think about data requirements,” Falconer said.

[![](https://cdn.thenewstack.io/media/2025/12/e2147b10-confluent-contextual-001-1024x548.jpg)](https://cdn.thenewstack.io/media/2025/12/e2147b10-confluent-contextual-001-1024x548.jpg)

Many problems that enterprise customers want to tackle today through AI cannot be defined through old-school purpose-built models. An airline chatbot, for instance, may pull data in from flight scheduling systems, weather systems, customer data, ticketing systems and untold other systems. It is all assembled on the fly.

This context engineering “can be a real challenge for businesses,” he said.

“Traditional software engineering [is] all about writing code and the data itself doesn’t change the business logic, but in the world of essentially probabilistic models, the data is the input that essentially ends up changing or manipulating the business logic,” Falconer explained.

Anomaly detection and product personalization have similar real-time challenges.

[![](https://cdn.thenewstack.io/media/2025/12/263505d5-confluent-contextual-01-1024x531.jpg)](https://cdn.thenewstack.io/media/2025/12/263505d5-confluent-contextual-01-1024x531.jpg)

## How Kafka Enables Event-Driven Scalability

Kafka, an enabler of event-driven architecture, also addresses the scalability challenges organizations may one day face. With such a proliferation of agents that will soon be upon corporate IT, any support platform would be run most effectively in an event-driven or microservices architecture, such as Kafka’s, Falconer argued.

But what are [agents](https://thenewstack.io/ai-agents-are-morphing-into-the-enterprise-operating-system/), if not [microservices](https://thenewstack.io/microservices/) in disguise?

“When it comes to the idea of these ‘event-driven agents,’ they really serve as the eyes and ears in your organization. You know, we talk about data streaming as being the central nervous system. The sensors of that world are all of the different places where this data originates in real time.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)