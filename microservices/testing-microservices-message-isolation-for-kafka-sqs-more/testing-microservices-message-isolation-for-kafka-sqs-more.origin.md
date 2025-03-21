# Testing Microservices: Message Isolation for Kafka, SQS, More
![Featued image for: Testing Microservices: Message Isolation for Kafka, SQS, More](https://cdn.thenewstack.io/media/2025/03/c0fae648-messages-1024x551.png)
When I talk to engineering leaders about testing event-driven microservices, I hear a common pain point: “Our async flows are nearly impossible to test reliably.”

Previously, we explored how [OpenTelemetry and message isolation](https://thenewstack.io/shift-left-meets-kafka-testing-event-driven-microservices/) enable testing Kafka-based workflows without duplicating infrastructure. The approach resonated with many teams facing the challenge of testing asynchronous flows cost-effectively, but I’ve received numerous questions about extending this pattern to other message brokers.

- “Does this work with AWS SQS?”
- “Can we apply this to RabbitMQ?”
- “What about Google Pub/Sub?”
The short answer is yes. The message isolation pattern works across most popular message brokers but implementation details vary based on each system’s architecture and terminology.

**The Universal Pattern: Message Isolation**
Before diving into specific platforms, let’s recap the core problem and our approach:

**The Problem**
Testing microservices that communicate via message queues presents several challenges:

- Setting up separate test environments is expensive and difficult to maintain.
- Async workflows are hard to verify without full-system tests.
- Integration issues often appear only after code is merged.
- Mocks frequently drift from reality, leading to false positives.
**The Solution**
Our message isolation approach addresses these challenges through these key principles:

**Share infrastructure:**Use a single baseline environment accessible to all sandboxes.**Propagate context:**Pass routing keys in message metadata via OpenTelemetry.**Duplicate messages:**Allow both baseline and sandbox services to receive copies of the same messages.**Selectively process:**Filter messages in consumers based on sandbox routing keys.
The goal is straightforward: Enable multiple developers to test their changes in isolation without interference while avoiding the cost and complexity of duplicating your entire messaging infrastructure.

**Apache Kafka: The Reference Implementation**
Kafka remains our reference implementation for message isolation testing due to its robust consumer group model. In Kafka, multiple consumer groups can independently process the same messages from a topic, creating a natural pattern for our testing approach.

With Kafka, each producer includes a routing key in message headers, and consumer groups provide the isolation mechanism. When a developer deploys their service version to test, it joins a unique consumer group (such as `my-service-group-sandbox123`
), receiving a copy of all messages while the baseline version continues operating in its original consumer group.

**RabbitMQ: Exchanges and Bindings**
RabbitMQ’s architecture differs from Kafka because it uses exchanges and bindings as intermediaries between producers and consumers, allowing more flexible routing patterns.

In RabbitMQ, exchanges distribute messages to queues through bindings. The message isolation pattern works by creating temporary queues for sandbox services that are bound to the same exchanges as the baseline queues. For example, if your baseline service consumes from a queue bound to a topic exchange, your sandbox version would create a new temporary queue bound to the same exchange with matching routing keys.

While RabbitMQ offers broker-level filtering through binding patterns, we still need consumer-side filtering to check the sandbox routing key against a central mapping service. The consumer would extract the routing key from the message headers, call a mapping service to determine if it should process the message and then proceed accordingly.

**Google Cloud Pub/Sub: Subscriptions**
Google Cloud Pub/Sub organizes messages around topics and subscriptions, making message isolation straightforward. A topic can have multiple subscriptions, and each subscription receives a copy of every message published to the topic – aligning perfectly with our sandbox model.

For sandbox testing, create temporary subscriptions to the same topics your baseline services use. The subscriber would implement consumer-side filtering to extract the routing key from message attributes, check against the mapping service and process messages accordingly.

**AWS SQS: The Special Case**
AWS SQS presents a unique challenge for message isolation because it doesn’t natively support the fan-out pattern we rely on in other brokers. In SQS, messages are consumed by a single consumer; there’s no built-in mechanism for multiple consumers to receive the same message, and messages are automatically deleted after being processed.

Therefore, we need to consider alternate approaches:

**Option 1: SNS + SQS Pattern**
Use Amazon SNS (Simple Notification Service) as the entry point to fan out messages to multiple SQS queues. Publishers send messages to an SNS topic, which delivers copies to multiple subscribed SQS queues — one for baseline, and separate ones for each sandbox environment. This approach requires no changes to existing consumers as they continue to read from their dedicated queues.

**Option 2: Dedicated Test Queues**
Create temporary SQS queues for testing with sandboxed producers and consumers. Deploy a new instance of your producer that sends messages to the temporary test queue and configure your test consumer to read from this new queue. Each sandbox gets its own isolated queue, producer and consumer.

For most teams, Option 1 provides the cleanest solution. Setting up an SNS topic that publishes to both your baseline SQS queue and any temporary testing queues maintains the decoupled architecture while enabling the isolation needed for testing. The overhead of message duplication is typically negligible compared to the cost of duplicating your entire infrastructure.

**NATS: Subjects and Queue Groups**
[NATS](https://nats.io/), with its lightweight and high-performance design, offers features well-suited for sandbox testing. We can leverage NATS queue groups, which function similarly to Kafka consumer groups.
By creating sandbox-specific queue groups, test services receive copies of messages without interfering with baseline services. Your test service would join a unique queue group (such as `service-sandbox123`
), subscribe to the same subjects as your baseline service and implement consumer-side filtering based on routing keys.

**Platform Team Implementation**
The message isolation approach becomes much more maintainable when platform teams build reusable components that handle the sandbox-specific logic.

**Creating Sandbox-Aware Consumer Libraries**
Platform teams can create thin wrappers around standard client libraries that automatically handle sandbox filtering:

123456789101112131415 |
public class SandboxAwareKafkaConsumer<K, V> extends KafkaConsumer<K, V> { private final SandboxMappingService mappingService; private final String sandboxId; // Constructor and configuration similar to standard KafkaConsumer @Override public ConsumerRecords<K, V> poll(Duration timeout) { // Get records using parent implementation ConsumerRecords<K, V> allRecords = super.poll(timeout); // Filter records based on routing key in headers return filterRecordsBySandbox(allRecords); }} |
Application developers use this exactly like the standard consumer:
123456 |
// Developers simply use the platform-provided implementationSandboxAwareKafkaConsumer<String, String> consumer = new SandboxAwareKafkaConsumer<>(props);consumer.subscribe(Arrays.asList("my-topic"));// The filtering happens automatically in the poll() method |
This approach makes the sandbox filtering completely transparent to application teams.
**Sandbox Life Cycle Management**
Platform teams can provide standardized hooks around the life cycle of sandboxes that automate resource management:

When a developer creates a new sandbox for testing:

- The platform automatically registers the sandbox ID in the central mapping service.
- Necessary consumer groups, queues or subscriptions are created with consistent naming (
`service-{sandbox-id}`
). - When testing completes, all sandbox-specific resources are automatically removed.
This hook-based approach makes sandbox isolation part of the platform’s core capabilities rather than a burden on each development team.

**Conclusion**
Message isolation patterns work across all major message brokers, though implementation details vary based on each system’s architecture. The approach consistently delivers three key benefits:

**Cost efficiency:**Share infrastructure instead of duplicating it.**Testing fidelity:**Test against real dependencies instead of mocks.**Developer velocity:**Catch issues earlier in the development process.
At [Signadot](https://www.signadot.com/), we’ve implemented these patterns across dozens of customer environments using different messaging systems. Companies like [Brex](https://www.signadot.com/case-studies/brex-uses-signadot-to-scale-developer-testing-across-100s-of-engineers), [Earnest](https://www.signadot.com/case-studies/how-earnest-empowers-developers-for-early-testing) and [ShareChat](https://www.signadot.com/case-studies/sharechat-chooses-signadot-giving-devs-high-quality-testing-feedback) have used these approaches to transform their microservice testing. If you’re interested in exploring how to apply these concepts to your specific environment, sign up and join our [community Slack channel](https://signadotcommunity.slack.com/join/shared_invite/zt-1estxm8pv-qfiaNfiFFCaW~eUlXsVoEQ#/shared-invite/email).

As microservice architectures continue to evolve, effective testing of asynchronous workflows becomes increasingly critical. The message isolation pattern provides a practical, scalable approach regardless of which message broker you’ve chosen.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)