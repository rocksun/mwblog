# Are Your Apps Truly Nomadic?
The race to perfect edge computing has accelerated significantly in the past few years — and for good reason. Edge computing delivers data in real-time by processing data locally, closer to both the source and end user. It makes possible always-on, always-connected devices and AI-enabled systems that run [across multiple clouds](https://thenewstack.io/britive-just-in-time-access-across-multiple-clouds/), regions, on-premises, and at the edge.

Today, edge computing powers self-driving vehicles, sophisticated sensors in globally distributed oil and gas operations, and fully connected manufacturing factories worldwide. The applications running on these edge systems must be as mobile and flexible as their support devices.

The need to evolve application architectures to keep pace with innovation is nothing new. Distributed application architectures have evolved drastically and relatively quickly, from the Java monoliths of the early 2000s to the Kubernetes-managed microservices that dominated the 2010s. Now, with edge-native computing and multiregion, multicloud, multi-edge deployments, we’ve entered the age of the location-independent “Nomadic Apps.”

![](https://cdn.thenewstack.io/media/2025/02/fcd8606c-picture1.png)
Figure: Nomadic apps can move freely from cloud to edge

**The Cloud-to-Edge and Edge-to-Cloud Continuum: A New Challenge**
In the cloud era, the push was toward centralization. Despite its name, cloud computing is built around integrating with centralized systems, unlimited storage options, and 24/7 availability. The edge era represents a move in the opposite direction.

Edge computing — with its ability to provide distributed processing under challenging conditions, often in remote locations, operate with [limited compute resources](https://thenewstack.io/limited-compute-resources-low-parameter-rag-can-help/), and function offline — is, in many ways, the cloud’s inverse. It’s about globally distributed systems, applications, and devices.

Edge computing solutions are gradually evolving. They often incorporate existing hardware, software, and servers that cannot be easily exchanged or upgraded without significant cost. Deploying and managing edge systems is also incredibly complex, as they must account for the constraints of these already deployed components and the need for seamless integration with legacy systems like [clouds and data](https://thenewstack.io/alerting-with-grafana-and-influxdb-cloud-serverless/) centers.

Edge apps must be designed for edge computing and devices; that is, they must be edge-native. For example, edge-native apps have very different characteristics and requirements than cloud native apps. They must also be as nomadic — untethered to specific providers, networks, and locations — as the edge environments that they operate within.

Cloud native apps | Pillar | Edge-native apps |
---|---|---|
Optimized for high-performance computing optimization | Workload | Designed for resource-constrained devices to ensure resilience in outages |
Use microservices architecture | Manage updates and versioning across distributed nodes | |
Have nearly unlimited storage resources | Data | Have limited local storage resources |
Replicate and cache data globally | Cache locally and reconcile later | |
Built for inter-service communication management | Connectivity | Built for use with unreliable/intermittent connections |
Operate across multiple instances and/or clouds | Rely on edge-to-cloud communication | |
|
**The Nuts and Bolts of Edge-Native Nomadic Applications **
Historically, messaging systems have evolved incrementally to support emerging application architectures. Messaging frameworks like remote procedure calls (RPCs) led MQSeries and JMS, followed by XML, WebSockets, message queues, and Apache Kafka.

All have tried to incrementally address issues characteristic of complex distributed systems, such as synchronous/asynchronous communication, scaling, fault tolerance, file format standardization, real-time communication, reliability, high-throughput data, decoupling application components, and log data. However, each step forward revealed new technical challenges.

Now, with the demand for nomadic apps that can run efficiently and consistently at the edge and [across distributed environments](https://thenewstack.io/real-time-data-access-across-highly-distributed-environments/) without reconfiguration or code changes, the industry must take its next step.

Building nomadic, location-independent, and flexible edge apps can present a significant challenge for developers. They must find ways to manage connectivity, data synchronization, portability, storage, and dynamic scaling across diverse environments while minimizing in-device computing. That means reimagining messaging systems [supporting data transmission from cloud](https://thenewstack.io/aws-brings-trusted-extension-support-to-managed-postgres/) to edge and edge to cloud despite harsh conditions and intermittent connectivity.

To support the most demanding and aspirational use cases for the edge, developers need messaging systems that:

**Edge-native applications must have bidirectional functionality.**Because there is no single “hub,” they must facilitate reliable data distribution from the edge to the cloud and vice versa. This is crucial for updating AI models, distributing binaries, and communicating time-sensitive data changes with alerting to and from multiple edge locations.**Balance high-value/low-volume and low-value/high-volume data transfers in real-time.**Edge systems process data at the source on edge, maintain efficiency by allocating[data processing tasks based on the](https://thenewstack.io/icymi-deepseek-is-an-open-source-success-story/)ir value and must be resilient despite network outages and intermittent connectivity. For example, high-value/low-volume events like a factory fire or sensor failure would trigger instant data transfers and alerting to facilitate rapid awareness, analysis, and remediation.**Are designed for easy deployment and adjustment with existing infrastructure.**
The requirements of edge-based systems often change based on external factors, scaling, contracting, and folding in existing hardware over their (relatively long) lifespans. The communication layers’ supporting functions must accommodate these changes — in processing needs, environment, and more — with minimal downtime.

Millions of developers and businesses worldwide use [NATS.io](http://nats.io/), an open source tool that supports edge computing expansion and nomadic apps. I designed NATS as a self-protecting, lightweight, and low-latency messaging solution well suited for microservices, computing at the edge, and nomadic and now AI-ready apps.

When designing NATS, I focused on telemetry — automatically collecting and transmitting real-time information from distributed systems, especially remote sources, events, and control. The systems always protect themselves.

NATS advantages include:

- Simplified Connectivity: NATS offers a unified system that supports various messaging models and reduces latency and complexity.
- Integrated Data Management: With JetStream, NATS provides a unified data layer for streaming, key-value stores, and object storage.
- Reduced footprint: A single binary of less than 20MB in size provides the following functionalities:
- Messaging and queueing (including MQTT server functionality)
- Streaming (including reliable store and forward data transmission between the cloud and the edges)
- Key/Value and Object Store
- Service mesh
- Efficient Compute Solutions: NATS Execution Engine (Nex) simplifies deployment and workload management, supporting true application nomadism.
![](https://cdn.thenewstack.io/media/2025/02/72759f71-picture1.png)
Figure: NATS-based edge-native tech stack

As edge computing and AI proliferate, [advancements like NATS’ event-based communication](https://thenewstack.io/what-happens-to-relicensed-open-source-projects-and-their-forks/), which is superior for AI, will offer the flexible and efficient approach needed to seamlessly integrate applications with various platforms and across distributed edge networks.** **

**The Edge of Tech’s Next Generation**
Over the past few years, we’ve hailed each innovation in computing, analytics, and equipment as *the* game-changer for Industry 4.0 and connectivity. However, no single innovation can or will change everything overnight. For example, consider the Internet: It wasn’t until engineers built supplementary tools like web browsers and email clients that its full capabilities were unleashed.

The same is true now. Edge computing, nomadic apps, AI, and the distributed infrastructure powering them are bridging the gap that has hindered or prevented edge-based networks from meeting their full potential. Together, these incremental improvements will usher in the next generation of practical AI applications and “smart” systems that developers, managers, and businesses have been waiting for.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)