# Implement Saga Patterns in Microservices With NestJS and Kafka
![Featued image for: Implement Saga Patterns in Microservices With NestJS and Kafka](https://cdn.thenewstack.io/media/2025/04/cb5623d0-lights-1024x576.jpg)
Handling distributed transactions in [microservices](https://thenewstack.io/microservices/) is no easy task. Unlike monolithic applications, where rolling back a transaction is straightforward thanks to centralized databases, [microservices operate independently](https://thenewstack.io/microservices/primer-microservices-explained/) — each often with its own database. This decentralized setup makes maintaining data consistency across multiple services especially challenging. Enter the saga pattern, a proven strategy for managing distributed transactions while ensuring consistency and reliability.

In this guide, we’ll break down the [saga pattern](https://thenewstack.io/making-the-saga-pattern-work-without-all-the-headaches/), explore how it addresses challenges in microservices, and show you how to implement it using [NestJS](https://thenewstack.io/configure-microservices-in-nestjs-a-beginners-guide/), [Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/) and[ TypeScript](https://thenewstack.io/what-is-typescript/). By the end, you’ll be equipped to build microservices that can handle complex transactions, maintain consistency and recover gracefully from failures.

**Why Do Microservices Need the Saga Pattern? **
Imagine an e-commerce application. When someone places an order, several services spring into action. An order service creates the order, the payment service charges the customer, the inventory service reserves the items and the shipping service schedules delivery.

But what happens if something goes wrong? Say, for example, the customer doesn’t have enough money in their account. Without a proper system in place, the entire process could fall apart, leaving data scattered and inconsistent across services.

The saga pattern solves this by breaking down a large transaction into smaller, independent local transactions. Each service handles its part of the process individually, and if something goes wrong, compensating transactions roll back the prior steps to maintain consistency. This enables microservices to operate autonomously yet remain in sync.

## Choreography vs. Orchestration
There are two main approaches to implementing the saga pattern in microservices: choreography and orchestration. Each has its advantages and trade-offs.

### 1. Choreography-Based Saga
In choreographed sagas, each microservice listens to events and reacts accordingly without a central coordinator. This is an event-driven approach where services communicate using a message broker like Kafka or RabbitMQ.

**How it works**:
- Each service publishes an event when it completes a transaction.
- Other services listen for these events and take action accordingly.
- If a failure occurs, compensating transactions are triggered automatically.
**Example workflow** (choreographed saga in e-commerce order processing):
- The order service creates an order and publishes an event:
`OrderCreated`
. - The payment service listens for this event, deducts the amount and emits:
`PaymentProcessed`
. - The inventory service listens to
`PaymentProcessed`
, reserves stock and emits:`StockReserved`
. - If any service fails, an event is published to trigger compensating actions (
`PaymentFailed`
→ refund the customer).
**Pros:**
- Decentralized and loosely coupled (services operate independently).
- Scalable since services handle their own logic without relying on a single coordinator.
**Cons:**
- Difficult to manage and debug because there is no single point of control.
- Event chains can be complex and hard to track.
### 2. Orchestration-Based Saga
In orchestrated sagas, a central saga orchestrator (or saga manager) controls the transaction flow, ensuring that each step is executed in the right order. The orchestrator sends commands to each service and waits for responses before proceeding to the next step.

**How it works**:
- A central saga orchestrator service initiates the transaction and calls each microservice in sequence.
- The orchestrator waits for responses before moving to the next step.
- If a failure occurs, the orchestrator triggers the required compensating transactions.
**Example workflow** (orchestrated saga in e-commerce order processing):
- The saga orchestrator starts the transaction by calling the order service to create an order.
- The orchestrator then calls the payment service to deduct the amount.
- If the payment is successful, the orchestrator calls the inventory service to reserve stock.
- If any step fails, the orchestrator triggers rollback operations in the correct order.
**Pros:**
- Easier to manage since all logic is centralized in the orchestrator.
- Clear execution flow with better error handling.
**Cons:**
- Single point of failure (orchestrator must be highly available).
- Less decoupled compared to event-driven choreography.
With that out of the way, we now come to the big question: When do we use the saga pattern in microservices? The saga pattern is beneficial when dealing with complex business processes that require consistency across multiple services. However, it’s not always the best solution. Here’s when you should (and shouldn’t) use saga:

**Avoid the Saga pattern when:**
- Simple CRUD operations can be handled by a single service.
- Performance-sensitive operations, where event-based communication might add latency.
- You can use a simpler distributed transaction model, such as two-phase commit (2PC), if supported.
**Use the Saga pattern when:**
- Multiple microservices participate in a single business transaction (such as order processing, booking systems).
- Data consistency is required across multiple databases in a distributed system.
- Rollback mechanisms are essential in case of failures.
- Event-driven communication is already in place (for choreographed sagas).
Here, we will use the orchestration-based methodology. Therefore, we will initialize a new NestJs project and install the following dependencies. Before you follow through, ensure you have [Node.js,](https://nodejs.org/en/download/current) npm and [Docker](https://www.docker.com/) installed.

[@nestjs/microservices](https://www.npmjs.com/package/@nestjs/microservices)— Provides built-in support for microservices in NestJS.[KafkaJS](https://kafka.js.org/)— A Kafka client for JavaScript to handle event-driven messaging.[@nestjs/config](https://www.npmjs.com/package/@nestjs/config)— Helps manage environment variables.[@nestjs/typeorm](https://www.npmjs.com/package/@nestjs/typeorm)and TypeORM — Object–relational mapping (ORM) for database interactions.- PostgreSQL client (or use MySQL2 if using MySQL).
Run these commands:

12345678 |
//Initialize new projectnpx @nestjs/cli new saga-microservices//Navigate into project directorycd saga-microservices//To install dependenciesnpm install @nestjs/microservices kafkajs @nestjs/config @nestjs/typeorm typeorm pg |
We will then configure Kafka as our event broker. Kafka is an event-streaming platform that will handle communication between our microservices. We’ll install and set up Kafka using Docker.
Now, create a `docker-compose.yml`
file in your project root and add the following configuration:

1234567891011121314151617181920 |
version: '3'services: zookeeper: image: confluentinc/cp-zookeeper:latest environment: ZOOKEEPER_CLIENT_PORT: 2181 ports: - "2181:2181" kafka: image: confluentinc/cp-kafka:latest depends_on: - zookeeper environment: KAFKA_BROKER_ID: 1 KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181 KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092 KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1 ports: - "9092:9092" |
The above configuration sets up Apache Kafka and Zookeeper as services. Zookeeper (using the `confluentinc/cp-zookeeper:latest`
image) is essential for managing Kafka’s metadata, such as broker coordination and leader election, and listens on port 2181. The Kafka service (using `confluentinc/cp-kafka:latest`
) depends on Zookeeper and is configured with `KAFKA_BROKER_ID: 1`
(identifying the broker), connects to Zookeeper at `zookeeper:2181`
and advertises itself on port 9092 for communication. The `KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1`
ensures topic replication isn’t required in a single-node setup. The `ports`
section maps Kafka and Zookeeper to the host machine, allowing external services or applications to communicate with Kafka.
Now we’ll start Kafka and ensure it is indeed running by executing the following commands:

12345 |
//Docker command to run kafka in detouched modedocker compose up -d//Docker command to ensure the kafka container is runningdocker ps |
![Kafka container being started](https://cdn.thenewstack.io/media/2025/04/92425960-image1a-1024x640.png)
Figure 1: Kafka container being started

![Evidence of Kafka containers running](https://cdn.thenewstack.io/media/2025/04/3afeec83-image2a-1024x640.png)
Figure 2: Evidence of Kafka containers running

Now we will create microservices for orders, payments and inventory.

Run the following commands to create three separate NestJS applications:

1234567891011121314151617 |
//create the order microservicenpx @nestjs/cli new order-servicecd order-servicenpm installcd ..//create the payment microservicenpx @nestjs/cli new payment-servicecd payment-servicenpm installcd ..//create the inventory microservicenpx @nestjs/cli new inventory-servicecd inventory-servicenpm installcd .. |
Next we will configure Kafka in each microservice, starting with the order service. First, we will install Kafka dependencies in all microservices.
`npm install @nestjs/microservices kafkajs`
Then, open `src/main.ts`
and modify it to register the order service as a Kafka-based microservice.

Replace the code in the `main.ts`
with the code below:

12345678910111213141516171819202122232425 |
import { NestFactory } from '@nestjs/core';import { MicroserviceOptions, Transport } from '@nestjs/microservices';import { OrderModule } from './app.module';async function bootstrap() { const app = await NestFactory.createMicroservice<MicroserviceOptions>( OrderModule, { transport: Transport.KAFKA, options: { client: { brokers: ['localhost:9092'], }, consumer: { groupId: 'order-service-consumer', }, }, }, ); await app.listen(); console.log('Order Service is running...');}bootstrap(); |
Now we will configure the `app.controller.ts`
to define Kafka topics and order processing.
123456789101112131415161718 |
import { Controller } from '@nestjs/common';import { MessagePattern, Payload } from '@nestjs/microservices';import { ClientKafka } from '@nestjs/microservices';import { Inject } from '@nestjs/common';@Controller()export class OrderController { constructor( @Inject('KAFKA_CLIENT') private readonly kafkaClient: ClientKafka, ) {} @MessagePattern('order.created') handleOrderCreated(@Payload() data: any) { console.log('Order Created:', data); // Trigger the next service (inventory-service) this.kafkaClient.emit('inventory.updated', { orderId: data.orderId }); return { status: 'ORDER_RECEIVED', orderId: data.orderId }; }} |
The code above listens for order.created events from Kafka and processes them.
We will also copy and paste the code below into the `module.ts`
:

123456789101112131415161718192021222324 |
import { Module } from '@nestjs/common';import { ClientsModule, Transport } from '@nestjs/microservices';import { OrderController } from './app.controller';@Module({ imports: [ ClientsModule.register([ { name: 'KAFKA_CLIENT', transport: Transport.KAFKA, options: { client: { brokers: ['localhost:9092'], // Update with your Kafka broker(s) }, consumer: { groupId: 'order-service-consumer', // Unique consumer group for order-service }, }, }, ]), ], controllers: [OrderController],})export class OrderModule {} |
We will do the same for the payment service.
Replace the code in `main.ts`
and `app.controller.ts`
with the code below:

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364 |
//main.tsimport { NestFactory } from '@nestjs/core';import { AppModule } from './app.module';import { MicroserviceOptions, Transport } from '@nestjs/microservices';async function bootstrap() { const app = await NestFactory.createMicroservice<MicroserviceOptions>( AppModule, { transport: Transport.KAFKA, options: { client: { brokers: ['localhost:9092'], }, consumer: { groupId: 'payment-service-consumer', }, }, }, ); await app.listen(); console.log('Payment Service is running...');}bootstrap();//app.controller.tsimport { Controller } from '@nestjs/common';import { MessagePattern, Payload } from '@nestjs/microservices';@Controller()export class PaymentController { @MessagePattern('payment.processed') handlePayment(@Payload() data: any) { console.log('Processing Payment:', data); return { status: 'PAYMENT_SUCCESS', orderId: data.orderId }; }}//module.tsimport { Module } from '@nestjs/common';import { ClientsModule, Transport } from '@nestjs/microservices';import { PaymentController } from './app.controller';@Module({ imports: [ ClientsModule.register([ { name: 'KAFKA_CLIENT', transport: Transport.KAFKA, options: { client: { brokers: ['localhost:9092'], }, consumer: { groupId: 'payment-service-consumer', }, }, }, ]), ], controllers: [PaymentController], providers: [],})export class AppModule {} |
Since we have successfully created the microservices and configured Kafka, we now have to implement the saga orchestrator. It manages the sequence of actions in a distributed transaction across multiple microservices, ensuring that each service completes its part and that compensating actions are triggered in case of failure. The orchestrator will use Kafka to communicate between the order, payment and inventory services, enabling the Saga pattern.
Next we will create another microservice for the Saga orchestrator. This service will have its own Kafka consumer to receive events and a Kafka producer to send commands or requests to other services.

Scaffold a new project and install dependencies with the command below.

12345 |
//create projectnpx @nestjs/cli new saga-orchestrator//install dependenciesnpm install @nestjs/microservices kafkajs |
Next, we will set up a saga orchestrator service that will listen for events from the order, payment and inventory services, handle the flow of events, and ensure that the process is completed correctly. Below is the project structure:
saga-orchestrator/
├── src/
│ ├── controllers/
│ │ └── saga.controller.ts
│ ├── services/
│ │ └── saga.service.ts
│ ├── events/
│ │ ├── order-events.ts
│ │ ├── payment-events.ts
│ │ └── inventory-events.ts
│ └── main.ts
└── package.json

We then have to define saga steps and event handlers.

The saga will have different steps, which are the individual microservice actions like order creation, payment processing and inventory updates. Each service will emit events after completing its part, and the orchestrator will handle these events and trigger the next step.

Example Saga Flow:

**Order service:**Receives a request to create an order. Emits an`ORDER_CREATED`
event.**Payment service:**Receives an`ORDER_CREATED`
event and attempts to process payment. Emits`PAYMENT_SUCCESS`
or`PAYMENT_FAILED`
.**Inventory service:**Receives a`PAYMENT_SUCCESS`
event and updates the inventory. Emits`INVENTORY_UPDATED`
or`INVENTORY_FAILED`
.**Failure handling:**If any of the steps fail, the orchestrator triggers compensating actions (cancel payment, restore inventory).
Copy and paste the code below in the `saga.service.ts`
file:

12345678910111213141516171819202122232425262728293031 |
import { Injectable, OnModuleInit } from '@nestjs/common';import { ClientKafka } from '@nestjs/microservices';@Injectable()export class SagaService implements OnModuleInit { constructor( @Inject('KAFKA_SERVICE') private readonly kafkaClient: ClientKafka, ) {} onModuleInit() { // Subscribe to response events from Kafka this.kafkaClient.subscribeToResponseOf('order_created'); this.kafkaClient.subscribeToResponseOf('payment_success'); this.kafkaClient.subscribeToResponseOf('payment_failed'); this.kafkaClient.subscribeToResponseOf('inventory_updated'); this.kafkaClient.subscribeToResponseOf('inventory_failed'); } async initiateSaga(orderId: string) { await this.kafkaClient.emit('order_created', { orderId }); } async handlePaymentSuccess(orderId: string) { await this.kafkaClient.emit('payment_success', { orderId }); } async handleFailure(orderId: string) { await this.kafkaClient.emit('compensate_payment', { orderId }); await this.kafkaClient.emit('compensate_inventory', { orderId }); }} |
Next, we need to register the Kafka client. Copy and paste the code below in the `saga.module.ts`
:
123456789101112131415161718192021222324 |
import { Module } from '@nestjs/common';import { ClientsModule, Transport } from '@nestjs/microservices';import { SagaService } from './services/saga.service';@Module({ imports: [ ClientsModule.register([ { name: 'KAFKA_SERVICE', transport: Transport.KAFKA, options: { client: { brokers: ['localhost:9092'], // Your Kafka broker }, consumer: { groupId: 'saga-consumer', }, }, }, ]), ], providers: [SagaService],})export class SagaModule {} |
Finally, we have to configure the controller and then run the application. Copy and paste the code below in the `saga.controller.ts`
file:
1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768 |
import { Controller, Get, Param, Inject } from '@nestjs/common';import { EventPattern, Payload, ClientKafka } from '@nestjs/microservices';import { SagaService } from './app.service';@Controller('saga')export class SagaController { constructor( private readonly sagaService: SagaService, @Inject('KAFKA_SERVICE') private readonly kafkaClient: ClientKafka, ) {} // ✅ Endpoint to start the saga process @Get('start/:orderId') async startSaga(@Param('orderId') orderId: string) { console.log(`Starting Saga for Order ID: ${orderId}`); await this.sagaService.initiateSaga(orderId); } // ✅ Listen for Order Created event @EventPattern('order.created') async handleOrderCreated(@Payload() message: any) { const { orderId } = message.value; console.log(`Order Created Event Received for Order ID: ${orderId}`); // Emit inventory update event await this.kafkaClient.emit('inventory.update', { orderId }); } // ✅ Listen for Payment Success event @EventPattern('payment.success') async handlePaymentSuccess(@Payload() message: any) { const { orderId } = message.value; console.log(`Payment Successful for Order ID: ${orderId}`); // Proceed with order completion logic //await this.sagaService.completeSaga(orderId); } // ✅ Listen for Payment Failure event @EventPattern('payment.failed') async handlePaymentFailed(@Payload() message: any) { const { orderId } = message.value; console.log(`Payment Failed for Order ID: ${orderId}`); // Trigger rollback await this.sagaService.handleFailure(orderId); } // ✅ Listen for Inventory Updated event @EventPattern('inventory.updated') async handleInventoryUpdated(@Payload() message: any) { const { orderId } = message.value; console.log(`Inventory Updated for Order ID: ${orderId}`); // Emit payment process event await this.kafkaClient.emit('payment.process', { orderId }); } // ✅ Listen for Inventory Failure event @EventPattern('inventory.failed') async handleInventoryFailed(@Payload() message: any) { const { orderId } = message.value; console.log(`Inventory Update Failed for Order ID: ${orderId}`); // Trigger rollback await this.sagaService.handleFailure(orderId); }} |
This saga controller is responsible for coordinating microservices through event-driven communication using Kafka. It listens to events related to order creation, payment processing and inventory updates while ensuring failure handling with compensating transactions.
We can now run the application by running `npm run start:dev`
.

At this point, we now have four applications running without any errors. We can then send in a request and see if our saga orchestrator controller received these requests.

In the terminal, execute the command below.

`curl -X GET http://localhost:3000/saga/start/12345`
You should then get a response of this nature:

123 |
{ "message": "Saga started for Order ID: 12345"} |
![Figure 3: Evidence that our request was received and we got a response](https://cdn.thenewstack.io/media/2025/04/299ba483-image3-1024x640.png)
Figure 3: Evidence that our request was received and we got a response

After this confirmation that the setup is working as expected, we need to verify the flow of events between the different services in our saga orchestrator setup.

First, we have to ensure that all the necessary Kafka topics are properly created and that the consumers are subscribed to the correct topics. You can list the Kafka topics.

Using the Docker command below, we can gain access to the terminal inside the Docker container.

`docker exec -it a457d90be977 bash`
Use the command below to retrieve the list of topics:

`kafka-topics --bootstrap-server localhost:9092 --list`
Once executed, we expect the response below.

12345678910 |
__consumer_offsetsinventory.updatedinventory_failed.replyinventory_updated.replyorder.createdorder_created.replypayment.processedpayment_failed.replypayment_successpayment_success.reply |
We will now resend a `GET`
request to the `saga/start/:orderId`
endpoint in our Saga controller to trigger the saga process. Once the request is sent, the saga orchestrator should receive this request and log that the saga has started for Order ID: 12345.
Then it should publish an event ( `order.created`
) to Kafka.

The order service should then consume this event and process it.

The order service should validate the order and possibly send another event like `inventory.check`
to Kafka.

The inventory service should then check stock availability and respond with either `inventory.updated`
(success) or `inventory.failed.reply`
(failure).

The payment service should process the payment and emit `payment_success`
or `payment_failed.reply’ accordingly.

Finally, the saga orchestrator should listen for final success or failure messages and return a response to the client.

**If successful:**
12345 |
{"message": "Saga completed successfully for order 12345"} |
**If failed:**
12345 |
{"message": "Saga failed for order 12345"} |
With the help of Kafka events, we were able to trigger and respond to events in a fault-tolerant manner, implementing rollback strategies when necessary to ensure consistency in our system. This saga pattern is crucial for long-running business processes where multiple microservices are involved and each service must collaborate while maintaining atomicity and reliability.
## Key Takeaways:
- Kafka helps decouple services and ensures that communication between microservices is asynchronous and reliable.
- The saga orchestrator ensures that the order processing system can handle failures gracefully, with compensating actions like payment and inventory rollbacks.
- NestJS provides an excellent platform to build scalable and maintainable microservices that can easily be integrated with Kafka.
You can find the full code for this implementation on [GitHub](https://github.com/RaymondZziwa/saga) for reference and to help you get started with your own distributed systems.

Want to learn how to configure microservices in NestJS? Dive into Andela’s step-by-step guide, [“Configure Microservices in NestJS With MySQL and Postman.”](https://www.andela.com/blog-posts/configure-microservices-in-nestjs-with-mysql-and-postman-a-beginners-guide/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=micrservices-nest-js&utm_term=writers-room)

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)