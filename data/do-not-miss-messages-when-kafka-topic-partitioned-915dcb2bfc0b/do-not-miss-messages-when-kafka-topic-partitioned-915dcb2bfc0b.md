
<!--
title: Kafka主题分区时不要丢失消息
cover: ./cover.png
-->

关于负载均衡策略的快速介绍。使用 Golang IBM/sarama 在 Kafka 主题上消费新添加的分区中的事件。

> 译自 [Do not miss messages when Kafka Topic Partitioned](https://itnext.io/do-not-miss-messages-when-kafka-topic-partitioned-915dcb2bfc0b)，作者 Emre Savcı。

## 简介

在事件驱动通信时代，**Kafka**是事实上的标准消息代理之一，它具有主题和消费者组的概念。

在Kafka中，一个主题可以有多个分区，因此可以通过这种方式提高消息处理的并行性。这使我们能够将消费者应用程序扩展到多个实例。

使用Kafka时，可能会向主题添加新的分区。如果配置不正确，消费者可能会错过新分区中的消息，因此进行适当的设置非常重要。

在本文中，我将向您展示如何在本地运行Kafka代理，然后配置消费者以从主题消费消息。在消费主题的同时，我们将创建新的分区，并观察我们的消费者如何自动接收来自新分区的消息。

我们将使用**Golang**作为编程语言，并使用[IBM/sarama](https://github.com/IBM/sarama)作为Kafka库。

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*0ZFcVifygpfnD7Wv.png)

*[https://kajalrawal.medium.com/kafka-broker-kafka-topic-consumer-and-record-flow-in-kafka-ec55104977b8](https://kajalrawal.medium.com/kafka-broker-kafka-topic-consumer-and-record-flow-in-kafka-ec55104977b8)*

## 在Docker中运行Kafka

为了测试我们的消费者和生产者，我们将使用**Docker**快速启动一个Kafka代理。将以下docker compose配置复制并粘贴到`docker-compose.yml`中：

```yaml
version: '2'
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
```

运行容器：

```bash
> docker-compose up -d

WARN[0000] /Users/emre.savci/Desktop/my-projects/kafka/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
WARN[0000] Found orphan containers ([kafka-kafka-2-1 kafka-zookeeper-2-1]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
[+] Running 2/2
 ✔ Container kafka-zookeeper-1-1  Started                                                                                                                                  0.3s
 ✔ Container kafka-kafka-1-1      Started     
```

## 负载均衡策略

为了处理分区，我们可以根据用例选择不同的负载均衡策略。

我将使用Sarama的源代码注释来解释负载均衡策略。

### 轮询

此策略返回轮询负载均衡策略，该策略以交替顺序将分区分配给成员。

例如，有两个主题（t0，t1）和两个消费者（m0，m1），每个主题有三个分区（p0，p1，p2）：

M0: [t0p0, t0p2, t1p1]
M1: [t0p1, t1p0, t1p2]

### 范围

此策略返回范围负载均衡策略，这是默认策略，它将分区作为范围分配给消费者组成员。

这遵循与[https://kafka.apache.org/31/javadoc/org/apache/kafka/clients/consumer/RangeAssignor.html](https://kafka.apache.org/31/javadoc/org/apache/kafka/clients/consumer/RangeAssignor.html)相同的逻辑。

两个主题T1和T2，每个主题有六个分区（0..5）和两个成员（M1，M2）的示例：

```
M1: {T1: [0, 1, 2], T2: [0, 1, 2]} 
M2: {T1: [3, 4, 5], T2: [3, 4, 5]}
```

### 粘性

此策略返回粘性负载均衡策略，该策略尝试保留之前的分配，同时保持均衡的分区分配。

主题T有六个分区（0..5）和两个成员（M1，M2）的示例：

```
M1: {T: [0, 2, 4]} 
M2: {T: [1, 3, 5]}
```

在重新分配和添加额外消费者后，您可能会得到如下分配计划：

```
M1: {T: [0, 2]} 
M2: {T: [1, 3]} 
M3: {T: [4, 5]}
```

## 演示

### 示例消费者

```go
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
```


### 配置和运行

现在让我们配置并运行消费者：

```go
package main

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

```

请注意，我们选择**轮询**作为我们的**平衡策略**。

### 生产者代码

我们将从生产者开始，自动将消息发送到主题中的每个分区。

```go
package main

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
```

现在我们可以看到我们的消费者在运行了。

### 整体运行

我将启动前面提供的消费者和生产者代码。等待几秒钟后，我们将向Kafka主题添加第二个分区，然后是第三个分区。下面将提供消费者日志，以演示消费者如何处理这些更改。

**运行代码**

```
.../consumer > go run main.go
.../producer > go run main.go
```

**创建分区**

让我们进入我们的Kafka容器，并在我们的消费者和生产者运行时运行以下命令：

```bash
> docker exec -it <container-id> /bin/sh
> ./bin/kafka-topics --bootstrap-server localhost:9092 \
--alter --topic example-topic \
--partitions 2
```

观察日志，您将看到消费者开始监听新的分区。几分钟后，让我们创建另一个分区：

```bash
> ./bin/kafka-topics --bootstrap-server localhost:9092 \
--alter --topic example-topic \
--partitions 3
```

同样，我们的消费者能够消费新的分区。

以下是消费者日志：

```
Setup  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  1 claims  map[example-topic:[0]]
2024/12/13 22:25:21 Consumer group is ready
ConsumeClaim  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  1 claims  map[example-topic:[0]]
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
Cleanup  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  1 claims  map[example-topic:[0]]
Setup  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  2 claims  map[example-topic:[0 1]]
ConsumeClaim  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  2 claims  map[example-topic:[0 1]]
ConsumeClaim  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  2 claims  map[example-topic:[0 1]]
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
Cleanup  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  2 claims  map[example-topic:[0 1]]
Setup  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  3 claims  map[example-topic:[0 1 2]]
ConsumeClaim  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  3 claims  map[example-topic:[0 1 2]]
ConsumeClaim  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  3 claims  map[example-topic:[0 1 2]]
ConsumeClaim  memberid  sarama-287eb50b-4f02-49ab-a827-ced69a4fadd6 sessionid  3 claims  map[example-topic:[0 1 2]]
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
```

我们可以很容易地看到我们的消费者被告知新的分区，并开始从这些分区读取消息。

# 结论

- ✅ 为您的消费者组配置添加合适的负载均衡策略
- ✅ 在配置中设置可接受的元数据刷新频率
- ✅ 根据您的需要选择最早或最新的初始偏移量

感谢您的阅读，希望您觉得这篇文章引人入胜。