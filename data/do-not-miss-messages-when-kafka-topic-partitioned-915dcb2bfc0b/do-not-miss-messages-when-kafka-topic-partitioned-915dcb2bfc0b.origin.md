# Do not miss messages when Kafka Topic Partitioned
# Introduction
In the era of event driven communication, one of the de-facto standard message brokers is **Kafka**, which is a message broker that has topic and consumer group concept.

In Kafka, a topic can have many partitions, hence in this way you can increase parallelism of processing messages. This enables us to scale our consumer applications to more than one instance.

While using Kafka, new partitions may be added to a topic. If you do not correctly configure, consumer may miss messages in new partitions, so it is important to do the appropriate setup.

In this article, I will show you how to run a Kafka broker locally and then configure a consumer to consume messages from a topic. While consuming the topic, we will create new partitions and observe that our consumer automatically receives messages from the new partitions.

We will use **Golang** as our programming language and [ IBM/sarama](https://github.com/IBM/sarama) as a Kafka library.

[https://kajalrawal.medium.com/kafka-broker-kafka-topic-consumer-and-record-flow-in-kafka-ec55104977b8](https://kajalrawal.medium.com/kafka-broker-kafka-topic-consumer-and-record-flow-in-kafka-ec55104977b8)
# Running Kafka in Docker
To test our consumers and produces, we will use **Docker** to quickly spin up a Kafka broker. Copy and paste the following docker compose configuration into docker-compose.yml:

`version: '2'`
services:
zookeeper-1:
image: confluentinc/cp-zookeeper:7.4.4
environment:
ZOOKEEPER_CLIENT_PORT: 2181
ZOOKEEPER_TICK_TIME: 2000
ports:
- 22181:2181
kafka-1:
image: confluentinc/cp-kafka:7.4.4
depends_on:
- zookeeper-1
ports:
- 29092:29092
- 9092:9092
environment:
KAFKA_BROKER_ID: 1
KAFKA_ZOOKEEPER_CONNECT: zookeeper-1:2181,zookeeper-2:2181
KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://127.0.0.1:9092,PLAINTEXT_HOST://127.0.0.1:29092
KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
Run the containers:

`> docker-compose up -d`
WARN[0000] /Users/emre.savci/Desktop/my-projects/kafka/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
WARN[0000] Found orphan containers ([kafka-kafka-2-1 kafka-zookeeper-2-1]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
[+] Running 2/2
✔ Container kafka-zookeeper-1-1 Started 0.3s
✔ Container kafka-kafka-1-1 Started
# Balance Strategies
To handle partitions, we can choose from different balance strategies according to our use cases.

I will use Sarama’s source code comments to explain balance strategies.

## Round Robin
This one returns a round-robin balance strategy, which assigns partitions to members in alternating order.

For example, there are two topics (t0, t1) and two consumer (m0, m1), and each topic has three partitions (p0, p1, p2):
M0: [t0p0, t0p2, t1p1]
M1: [t0p1, t1p0, t1p2]

## Range
This one returns a range balance strategy, which is the default and assigns partitions as ranges to consumer group members.

This follows the same logic as [https://kafka.apache.org/31/javadoc/org/apache/kafka/clients/consumer/RangeAssignor.html](https://kafka.apache.org/31/javadoc/org/apache/kafka/clients/consumer/RangeAssignor.html)
Example with two topics T1 and T2 with six partitions each (0..5) and two members (M1, M2):

**M1: {T1: [0, 1, 2], T2: [0, 1, 2]}M2: {T1: [3, 4, 5], T2: [3, 4, 5]}**
## Sticky
This one returns a sticky balance strategy, which assigns partitions to members with an attempt to preserve earlier assignments
while maintain a balanced partition distribution.

Example with topic T with six partitions (0..5) and two members (M1, M2):**M1: {T: [0, 2, 4]}M2: {T: [1, 3, 5]}**

On reassignment with an additional consumer, you might get an assignment plan like:

**M1: {T: [0, 2]}M2: {T: [1, 3]}M3: {T: [4, 5]}**
# Demo
## Example Consumer
type ExampleConsumer struct {
Ready chan bool
}
// Setup is run before the consumer starts consuming, providing an opportunity to setup things.
func (consumer *ExampleConsumer) Setup(session sarama.ConsumerGroupSession) error {
// Mark the consumer as ready
close(consumer.Ready)
fmt.Println("Setup ", "memberid ", session.MemberID(), "sessionid ", session.GenerationID(), "claims ", session.Claims())
return nil
}
// Cleanup is run at the end of a session, to cleanup resources.
func (consumer *ExampleConsumer) Cleanup(session sarama.ConsumerGroupSession) error {
fmt.Println("Cleanup ", "memberid ", session.MemberID(), "sessionid ", session.GenerationID(), "claims ", session.Claims())
return nil
}
// ConsumeClaim must start a consumer loop of ConsumerGroupClaim's Messages().
func (consumer *ExampleConsumer) ConsumeClaim(session sarama.ConsumerGroupSession, claim sarama.ConsumerGroupClaim) error {
fmt.Println("ConsumeClaim ", "memberid ", session.MemberID(), "sessionid ", session.GenerationID(), "claims ", session.Claims())
for message := range claim.Messages() {
fmt.Printf("Message claimed: value = %s, timestamp = %v, topic = %s, partition = %d\n", string(message.Value), message.Timestamp, message.Topic, message.Partition)
session.MarkMessage(message, "")
}
return nil
}
## Configuration and Running
Now let’s configure and run the consumer:

`package main`
import (
"context"
"fmt"
"log"
"time"
"github.com/IBM/sarama"
)
func main() {
brokers := []string{"localhost:9092"}
topic := "example-topic"
groupID := "example-group"
config := sarama.NewConfig()
config.Version = sarama.V3_3_0_0 // Set Kafka version
config.Consumer.Group.Heartbeat.Interval = 1 * time.Second
config.Consumer.Offsets.Initial = sarama.OffsetOldest
config.Metadata.RefreshFrequency = time.Minute * 1
config.Metadata.Full = false
// Set up group strategies
config.Consumer.Group.Rebalance.GroupStrategies = []sarama.BalanceStrategy{
sarama.NewBalanceStrategyRoundRobin(),
}
// Create a new consumer group
consumerGroup, err := sarama.NewConsumerGroup(brokers, groupID, config)
if err != nil {
log.Fatalf("Error creating consumer group: %v", err)
}
defer consumerGroup.Close()
ctx := context.Background()
consumer := &ExampleConsumer{Ready: make(chan bool)}
// Start consumer group session
go func() {
for {
if err := consumerGroup.Consume(ctx, []string{topic}, consumer); err != nil {
log.Fatalf("Error in consumer group: %v", err)
}
// Check if context was canceled, signaling the application to stop
if ctx.Err() != nil {
fmt.Println("Context was canceled")
return
}
// Reset consumer ready channel
consumer.Ready = make(chan bool)
}
}()
// Wait for consumer to be ready
<-consumer.Ready
log.Println("Consumer group is ready")
<-make(chan struct{})
}
Note, we choosed **Round Robin** as our **balance strategy**.

## Producer Code
We will start with a producer to automatically produce messages to every partition in our topic.

`package main`
import (
"fmt"
"time"
"github.com/IBM/sarama"
)
func main() {
brokers := []string{"localhost:9092"}
topic := "example-topic"
config := sarama.NewConfig()
config.Version = sarama.V3_3_0_0 // Set Kafka version
config.Metadata.RefreshFrequency = 1 * time.Minute
config.Producer.Return.Successes = true
config.Producer.RequiredAcks = sarama.WaitForAll
config.Producer.Retry.Max = 3
config.Producer.Partitioner = sarama.NewRoundRobinPartitioner
producer, err := sarama.NewSyncProducer(brokers, config)
if err != nil {
fmt.Println("Error creating producer: ", err)
return
}
defer producer.Close()
for {
partition, _, err := producer.SendMessage(&sarama.ProducerMessage{
Topic: topic,
Value: sarama.StringEncoder("Hello, World!"),
})
if err != nil {
fmt.Println("Error producing message: ", err)
} else {
fmt.Println("Produced message to partition ", partition)
}
time.Sleep(2 * time.Second)
}
}
Now we are ready to see our consumer in action.

## Running All Together
I will start the consumer and producer code that I provided earlier. After waiting a few seconds, we will add a second partition to the Kafka topic, followed by a third partition. The consumer logs will be provided below to demonstrate how the consumer handles these changes.

**Run the Code**
`.../consumer > go run main.go`
.../producer > go run main.go
**Create Partition**
Let’s get into our Kafka container and run the following command while our consumer and producer running:

`> docker exec it <container-id> /bin/sh`
> ./bin/kafka-topics --bootstrap-server localhost:9092 \
--alter --topic example-to \
--partitions 2
Watch the logs and you will see that the consumer starts listening the new partitions. Couple of minutes after let’s create another partition:

`> ./bin/kafka-topics --bootstrap-server localhost:9092 \`
--alter --topic example-to \
--partitions 3
And again, our consumer is able to consume new partitions.

Her are the consumer logs:

`Setup memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 1 claims map[example-topic:[0]]`
2024/12/13 22:25:21 Consumer group is ready
ConsumeClaim memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 1 claims map[example-topic:[0]]
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Cleanup memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 1 claims map[example-topic:[0]]
Setup memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 2 claims map[example-topic:[0 1]]
ConsumeClaim memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 2 claims map[example-topic:[0 1]]
ConsumeClaim memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 2 claims map[example-topic:[0 1]]
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Cleanup memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 2 claims map[example-topic:[0 1]]
Setup memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 3 claims map[example-topic:[0 1 2]]
ConsumeClaim memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 3 claims map[example-topic:[0 1 2]]
ConsumeClaim memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 3 claims map[example-topic:[0 1 2]]
ConsumeClaim memberid sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid 3 claims map[example-topic:[0 1 2]]
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 2
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
Hello, World!, example-topic, partition: 2
Hello, World!, example-topic, partition: 0
Hello, World!, example-topic, partition: 1
We can easily see that our consumer informed about new partitions and starts reading messages from that partitions too.

# Conclusion
✅ Add appropriate balance strategy to your consumer group config
✅ Set an acceptable metadata refresh frequency in config
✅ Choose initial offset as Earliest or Newest according to your needs

Thanks for reading so far, I hope it was engaging for you.