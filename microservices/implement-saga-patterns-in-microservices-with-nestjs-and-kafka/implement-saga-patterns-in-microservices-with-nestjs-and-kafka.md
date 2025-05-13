
<!--
title: 使用NestJS和Kafka在微服务中实现 Saga 模式
cover: https://cdn.thenewstack.io/media/2025/04/cb5623d0-lights.jpg
summary: 🔥云原生架构师必看！用 NestJS + Kafka 落地微服务 Saga 模式，解决分布式事务难题！文章深入浅出讲解编排和协调两种 Saga 实现，手把手教你构建订单、支付、库存微服务，保证数据一致性，故障可恢复！告别分布式事务噩梦，拥抱云原生 AI 时代！
-->

🔥云原生架构师必看！用 NestJS + Kafka 落地微服务 Saga 模式，解决分布式事务难题！文章深入浅出讲解编排和协调两种 Saga 实现，手把手教你构建订单、支付、库存微服务，保证数据一致性，故障可恢复！告别分布式事务噩梦，拥抱云原生 AI 时代！

> 译自：[Implement Saga Patterns in Microservices With NestJS and Kafka](https://thenewstack.io/implement-saga-patterns-in-microservices-with-nestjs-and-kafka/)
> 
> 作者：Zziwa Raymond Ian

在[微服务](https://thenewstack.io/microservices/)中处理分布式事务并非易事。与单体应用不同，由于集中式数据库的存在，回滚事务非常简单，而[微服务是独立运行的](https://thenewstack.io/microservices/primer-microservices-explained/)——每个微服务通常都有自己的数据库。这种去中心化的设置使得跨多个服务维护数据一致性尤其具有挑战性。Saga 模式应运而生，它是一种经过验证的策略，用于管理分布式事务，同时确保一致性和可靠性。

在本指南中，我们将分解 [saga 模式](https://thenewstack.io/making-the-saga-pattern-work-without-all-the-headaches/)，探讨它如何应对微服务中的挑战，并向您展示如何使用 [NestJS](https://thenewstack.io/configure-microservices-in-nestjs-a-beginners-guide/)、[Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/) 和 [TypeScript](https://thenewstack.io/what-is-typescript/) 实现它。最后，您将能够构建可以处理复杂事务、保持一致性并从故障中优雅恢复的微服务。

## 为什么微服务需要 Saga 模式？

想象一个电子商务应用程序。当有人下订单时，多个服务会立即启动。订单服务创建订单，支付服务向客户收费，库存服务预留商品，运输服务安排交货。

但是，如果出现问题会怎样？例如，假设客户的帐户中没有足够的钱。如果没有适当的系统，整个过程可能会崩溃，导致数据分散且在服务之间不一致。

Saga 模式通过将大型事务分解为更小的、独立的本地事务来解决这个问题。每个服务单独处理其流程部分，如果出现问题，补偿事务会回滚之前的步骤以保持一致性。这使微服务能够自主运行，但仍保持同步。

## 编排与协调

在微服务中实现 Saga 模式有两种主要方法：编排和协调。每种方法都有其优点和缺点。

### 1. 基于编排的 Saga

在基于编排的 Saga 中，每个微服务监听事件并做出相应的反应，而无需中央协调器。这是一种事件驱动的方法，服务使用 Kafka 或 RabbitMQ 等消息代理进行通信。

**它是如何工作的**：

- 每个服务在完成事务时发布一个事件。
- 其他服务监听这些事件并采取相应的措施。
- 如果发生故障，将自动触发补偿事务。

**示例工作流程**（电子商务订单处理中的编排 Saga）：

- 订单服务创建一个订单并发布一个事件：`OrderCreated`。
- 支付服务监听此事件，扣除金额并发出：`PaymentProcessed`。
- 库存服务监听 `PaymentProcessed`，预留库存并发出：`StockReserved`。
- 如果任何服务失败，则会发布一个事件以触发补偿操作（`PaymentFailed` → 向客户退款）。

**优点：**

- 去中心化和松散耦合（服务独立运行）。
- 可扩展，因为服务处理自己的逻辑，而不依赖于单个协调器。

**缺点：**

- 难以管理和调试，因为没有单一的控制点。
- 事件链可能很复杂且难以跟踪。

### 2. 基于协调的 Saga

在基于协调的 Saga 中，中央 Saga 协调器（或 Saga 管理器）控制事务流程，确保每个步骤都按正确的顺序执行。协调器向每个服务发送命令，并等待响应，然后再继续下一步。

**它是如何工作的**：

- 中央 Saga 协调器服务启动事务并按顺序调用每个微服务。
- 协调器等待响应，然后再进入下一步。
- 如果发生故障，协调器将触发所需的补偿事务。

**示例工作流程**（电子商务订单处理中的协调 Saga）：

- Saga 协调器通过调用订单服务来创建订单来启动事务。
- 然后，协调器调用支付服务以扣除金额。
- 如果付款成功，协调器将调用库存服务以预留库存。
- 如果任何步骤失败，协调器将按正确的顺序触发回滚操作。

**优点：**

- 更易于管理，因为所有逻辑都集中在协调器中。
- 清晰的执行流程，具有更好的错误处理。

**缺点：**

- 单点故障（协调器必须高度可用）。
- 与事件驱动的编排相比，耦合性更低。
解决了这个问题，现在我们来讨论一个大问题：我们何时在微服务中使用 Saga 模式？当处理需要在多个服务之间保持一致性的复杂业务流程时，Saga 模式非常有用。然而，它并不总是最佳解决方案。以下是您应该（以及不应该）使用 Saga 的情况：

**避免使用 Saga 模式的情况：**

- 简单的 CRUD 操作可以由单个服务处理。
- 对性能敏感的操作，其中基于事件的通信可能会增加延迟。
- 如果支持，您可以使用更简单的分布式事务模型，例如两阶段提交 (2PC)。

**使用 Saga 模式的情况：**

- 多个微服务参与单个业务事务（例如订单处理、预订系统）。
- 在分布式系统中，需要在多个数据库之间保持数据一致性。
- 在发生故障时，回滚机制至关重要。
- 事件驱动的通信已经到位（对于编排 Saga）。

在这里，我们将使用基于编排的方法。因此，我们将初始化一个新的 NestJs 项目并安装以下依赖项。在继续操作之前，请确保您已安装 [Node.js](https://nodejs.org/en/download/current)、npm 和 [Docker](https://www.docker.com/)。

*   [@nestjs/microservices](https://www.npmjs.com/package/@nestjs/microservices) — 为 NestJS 中的微服务提供内置支持。
*   [KafkaJS](https://kafka.js.org/) — 用于 JavaScript 的 Kafka 客户端，用于处理事件驱动的消息传递。
*   [@nestjs/config](https://www.npmjs.com/package/@nestjs/config) — 帮助管理环境变量。
*   [@nestjs/typeorm](https://www.npmjs.com/package/@nestjs/typeorm) 和 TypeORM — 用于数据库交互的对象关系映射 (ORM)。
*   PostgreSQL 客户端（如果使用 MySQL，则使用 MySQL2）。

运行以下命令：

```bash
//Initialize new project
npx @nestjs/cli new saga-microservices

//Navigate into project directory
cd saga-microservices

//To install dependencies
npm install @nestjs/microservices kafkajs @nestjs/config @nestjs/typeorm typeorm pg
```

然后，我们将 Kafka 配置为我们的事件代理。Kafka 是一个事件流平台，将处理我们的微服务之间的通信。我们将使用 Docker 安装和设置 Kafka。

现在，在您的项目根目录中创建一个 `docker-compose.yml` 文件，并添加以下配置：

```yaml
version: '3'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
    ports:
      - "2181:2181"
  kafka:
    image: confluentinc/cp-kafka:latest
    depends_on:
      - zookeeper
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    ports:
      - "9092:9092"
```

上面的配置将 Apache Kafka 和 Zookeeper 设置为服务。Zookeeper（使用 `confluentinc/cp-zookeeper:latest` 镜像）对于管理 Kafka 的元数据（例如代理协调和领导者选举）至关重要，并在端口 2181 上侦听。Kafka 服务（使用 `confluentinc/cp-kafka:latest` ）依赖于 Zookeeper，并配置了 `KAFKA_BROKER_ID: 1` （标识代理），在 `zookeeper:2181` 连接到 Zookeeper，并在端口 9092 上发布自身以进行通信。`KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1` 确保在单节点设置中不需要主题复制。`ports` 部分将 Kafka 和 Zookeeper 映射到主机，允许外部服务或应用程序与 Kafka 通信。

现在，我们将启动 Kafka 并通过执行以下命令来确保它确实在运行：

```bash
//Docker command to run kafka in detouched mode
docker compose up -d

//Docker command to ensure the kafka container is running
docker ps
```

![Kafka container being started](https://cdn.thenewstack.io/media/2025/04/92425960-image1a-1024x640.png)

*图 1：Kafka 容器正在启动*

![Evidence of Kafka containers running](https://cdn.thenewstack.io/media/2025/04/3afeec83-image2a-1024x640.png)

*图 2：Kafka 容器正在运行的证据*

现在，我们将为订单、支付和库存创建微服务。

运行以下命令以创建三个独立的 NestJS 应用程序：

```bash
//create the order microservice
npx @nestjs/cli new order-service
cd order-service
npm install
cd ..

//create the payment microservice
npx @nestjs/cli new payment-service
cd payment-service
npm install
cd ..

//create the inventory microservice
npx @nestjs/cli new inventory-service
cd inventory-service
npm install
cd ..
```

接下来，我们将在每个微服务中配置 Kafka，从订单服务开始。首先，我们将在所有微服务中安装 Kafka 依赖项。

`npm install @nestjs/microservices kafkajs`

然后，打开 `src/main.ts` 并修改它以将订单服务注册为基于 Kafka 的微服务。

将 `main.ts` 中的代码替换为以下代码：

```typescript
// main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { MicroserviceOptions, Transport } from '@nestjs/microservices';

async function bootstrap() {
  const app = await NestFactory.createMicroservice<MicroserviceOptions>(AppModule, {
    transport: Transport.KAFKA,
    options: {
      client: {
        clientId: 'order',
        brokers: ['localhost:9092'],
      },
      consumer: {
        groupId: 'order-consumer',
      },
    },
  });
  await app.listen();
}
bootstrap();
```

现在，我们将配置 app.controller.ts 来定义 Kafka 主题和订单处理。


```typescript
import { NestFactory } from '@nestjs/core';
import { MicroserviceOptions, Transport } from '@nestjs/microservices';
import { OrderModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.createMicroservice<MicroserviceOptions>(
    OrderModule,
    {
      transport: Transport.KAFKA,
      options: {
        client: {
          brokers: ['localhost:9092'],
        },
        consumer: {
          groupId: 'order-service-consumer',
        },
      },
    },
  );
  await app.listen();
  console.log('Order Service is running...');
}
bootstrap();
```

现在我们将配置 `app.controller.ts` 来定义 Kafka 主题和订单处理。

```typescript
import { Controller } from '@nestjs/common';
import { MessagePattern, Payload } from '@nestjs/microservices';
import { ClientKafka } from '@nestjs/microservices';
import { Inject } from '@nestjs/common';

@Controller()
export class OrderController {
  constructor(
    @Inject('KAFKA_CLIENT') private readonly kafkaClient: ClientKafka,
  ) {}

  @MessagePattern('order.created')
  handleOrderCreated(@Payload() data: any) {
    console.log('Order Created:', data);
    // Trigger the next service (inventory-service)
    this.kafkaClient.emit('inventory.updated', { orderId: data.orderId });
    return { status: 'ORDER_RECEIVED', orderId: data.orderId };
  }
}
```

上面的代码监听来自 Kafka 的 `order.created` 事件并处理它们。

我们还将下面的代码复制并粘贴到 `module.ts` 中：

```typescript
import { Module } from '@nestjs/common';
import { ClientsModule, Transport } from '@nestjs/microservices';
import { OrderController } from './app.controller';

@Module({
  imports: [
    ClientsModule.register([
      {
        name: 'KAFKA_CLIENT',
        transport: Transport.KAFKA,
        options: {
          client: {
            brokers: ['localhost:9092'], // Update with your Kafka broker(s)
          },
          consumer: {
            groupId: 'order-service-consumer', // Unique consumer group for order-service
          },
        },
      },
    ]),
  ],
  controllers: [OrderController],
})
export class OrderModule {}
```

我们将对支付服务执行相同的操作。

将 `main.ts` 和 `app.controller.ts` 中的代码替换为以下代码：

```typescript
//main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { MicroserviceOptions, Transport } from '@nestjs/microservices';

async function bootstrap() {
  const app = await NestFactory.createMicroservice<MicroserviceOptions>(
    AppModule,
    {
      transport: Transport.KAFKA,
      options: {
        client: {
          brokers: ['localhost:9092'],
        },
        consumer: {
          groupId: 'payment-service-consumer',
        },
      },
    },
  );
  await app.listen();
  console.log('Payment Service is running...');
}
bootstrap();

//app.controller.ts
import { Controller } from '@nestjs/common';
import { MessagePattern, Payload } from '@nestjs/microservices';

@Controller()
export class PaymentController {
  @MessagePattern('payment.processed')
  handlePayment(@Payload() data: any) {
    console.log('Processing Payment:', data);
    return { status: 'PAYMENT_SUCCESS', orderId: data.orderId };
  }
}

//module.ts
import { Module } from '@nestjs/common';
import { ClientsModule, Transport } from '@nestjs/microservices';
import { PaymentController } from './app.controller';

@Module({
  imports: [
    ClientsModule.register([
      {
        name: 'KAFKA_CLIENT',
        transport: Transport.KAFKA,
        options: {
          client: {
            brokers: ['localhost:9092'],
          },
          consumer: {
            groupId: 'payment-service-consumer',
          },
        },
      },
    ]),
  ],
  controllers: [PaymentController],
  providers: [],
})
export class AppModule {}
```

由于我们已经成功创建了微服务并配置了 Kafka，因此我们现在必须实现 Saga 编排器。它管理跨多个微服务的分布式事务中的一系列操作，确保每个服务完成其部分，并在发生故障时触发补偿操作。编排器将使用 Kafka 在订单、支付和库存服务之间进行通信，从而启用 Saga 模式。

接下来，我们将为 Saga 编排器创建另一个微服务。此服务将拥有自己的 Kafka 消费者来接收事件，以及 Kafka 生产者来向其他服务发送命令或请求。

使用以下命令搭建一个新项目并安装依赖项。

```bash
//create project
npx @nestjs/cli new saga-orchestrator

//install dependencies
npm install @nestjs/microservices kafkajs
```

接下来，我们将设置一个 Saga 编排器服务，该服务将侦听来自订单、支付和库存服务的事件，处理事件流，并确保流程正确完成。以下是项目结构：

```
saga-orchestrator/
├── src/
│   ├── controllers/
│   │   └── saga.controller.ts
│   ├── services/
│   │   └── saga.service.ts
│   ├── events/
│   │   ├── order-events.ts
│   │   ├── payment-events.ts
│   │   └── inventory-events.ts
│   └── main.ts
└── package.json
```

然后，我们必须定义 Saga 步骤和事件处理程序。

Saga 将包含不同的步骤，这些步骤是独立的微服务操作，例如订单创建、支付处理和库存更新。每个服务在完成其部分后都会发出事件，协调器将处理这些事件并触发下一步。

Saga 流程示例：

1. **订单服务：** 接收创建订单的请求。发出 `ORDER_CREATED` 事件。
2. **支付服务：** 接收 `ORDER_CREATED` 事件并尝试处理付款。发出 `PAYMENT_SUCCESS` 或 `PAYMENT_FAILED`。
3. **库存服务：** 接收 `PAYMENT_SUCCESS` 事件并更新库存。发出 `INVENTORY_UPDATED` 或 `INVENTORY_FAILED`。
4. **故障处理：** 如果任何步骤失败，协调器将触发补偿操作（取消付款、恢复库存）。

将以下代码复制并粘贴到 `saga.service.ts` 文件中：

```typescript
import { Injectable, OnModuleInit } from '@nestjs/common';
import { ClientKafka } from '@nestjs/microservices';

@Injectable()
export class SagaService implements OnModuleInit {
  constructor(
    @Inject('KAFKA_SERVICE') private readonly kafkaClient: ClientKafka,
  ) {}

  onModuleInit() {
    // Subscribe to response events from Kafka
    this.kafkaClient.subscribeToResponseOf('order_created');
    this.kafkaClient.subscribeToResponseOf('payment_success');
    this.kafkaClient.subscribeToResponseOf('payment_failed');
    this.kafkaClient.subscribeToResponseOf('inventory_updated');
    this.kafkaClient.subscribeToResponseOf('inventory_failed');
  }

  async initiateSaga(orderId: string) {
    await this.kafkaClient.emit('order_created', { orderId });
  }

  async handlePaymentSuccess(orderId: string) {
    await this.kafkaClient.emit('payment_success', { orderId });
  }

  async handleFailure(orderId: string) {
    await this.kafkaClient.emit('compensate_payment', { orderId });
    await this.kafkaClient.emit('compensate_inventory', { orderId });
  }
}
```

接下来，我们需要注册 Kafka 客户端。将以下代码复制并粘贴到 `saga.module.ts` 中：

```typescript
import { Module } from '@nestjs/common';
import { ClientsModule, Transport } from '@nestjs/microservices';
import { SagaService } from './services/saga.service';

@Module({
  imports: [
    ClientsModule.register([
      {
        name: 'KAFKA_SERVICE',
        transport: Transport.KAFKA,
        options: {
          client: {
            brokers: ['localhost:9092'], // Your Kafka broker
          },
          consumer: {
            groupId: 'saga-consumer',
          },
        },
      },
    ]),
  ],
  providers: [SagaService],
})
export class SagaModule {}
```

最后，我们必须配置控制器，然后运行应用程序。将以下代码复制并粘贴到 `saga.controller.ts` 文件中：

```typescript
import { Controller, Get, Param, Inject } from '@nestjs/common';
import { EventPattern, Payload, ClientKafka } from '@nestjs/microservices';
import { SagaService } from './app.service';

@Controller('saga')
export class SagaController {
  constructor(
    private readonly sagaService: SagaService,
    @Inject('KAFKA_SERVICE') private readonly kafkaClient: ClientKafka,
  ) {}

  // ✅ Endpoint to start the saga process
  @Get('start/:orderId')
  async startSaga(@Param('orderId') orderId: string) {
    console.log(`Starting Saga for Order ID: ${orderId}`);
    await this.sagaService.initiateSaga(orderId);
  }

  // ✅ Listen for Order Created event
  @EventPattern('order.created')
  async handleOrderCreated(@Payload() message: any) {
    const { orderId } = message.value;
    console.log(`Order Created Event Received for Order ID: ${orderId}`);
    // Emit inventory update event
    await this.kafkaClient.emit('inventory.update', { orderId });
  }

  // ✅ Listen for Payment Success event
  @EventPattern('payment.success')
  async handlePaymentSuccess(@Payload() message: any) {
    const { orderId } = message.value;
    console.log(`Payment Successful for Order ID: ${orderId}`);
    // Proceed with order completion logic
    //await this.sagaService.completeSaga(orderId);
  }

  // ✅ Listen for Payment Failure event
  @EventPattern('payment.failed')
  async handlePaymentFailed(@Payload() message: any) {
    const { orderId } = message.value;
    console.log(`Payment Failed for Order ID: ${orderId}`);
    // Trigger rollback
    await this.sagaService.handleFailure(orderId);
  }

  // ✅ Listen for Inventory Updated event
  @EventPattern('inventory.updated')
  async handleInventoryUpdated(@Payload() message: any) {
    const { orderId } = message.value;
    console.log(`Inventory Updated for Order ID: ${orderId}`);
    // Emit payment process event
    await this.kafkaClient.emit('payment.process', { orderId });
  }

  // ✅ Listen for Inventory Failure event
  @EventPattern('inventory.failed')
  async handleInventoryFailed(@Payload() message: any) {
    const { orderId } = message.value;
    console.log(`Inventory Update Failed for Order ID: ${orderId}`);
    // Trigger rollback
    await this.sagaService.handleFailure(orderId);
  }
}
```
这个 Saga 控制器负责通过使用 Kafka 的事件驱动通信来协调微服务。它监听与订单创建、支付处理和库存更新相关的事件，同时确保使用补偿事务处理故障。

我们现在可以通过运行 `npm run start:dev` 来运行应用程序。

此时，我们现在有四个应用程序在运行，没有任何错误。然后，我们可以发送一个请求，看看我们的 Saga 编排器控制器是否收到了这些请求。

在终端中，执行以下命令。

```bash
curl -X GET http://localhost:3000/saga/start/12345
```

你应该得到这样的回应：

```json
{ "message": "Saga started for Order ID: 12345"}
```

![Figure 3: Evidence that our request was received and we got a response](https://cdn.thenewstack.io/media/2025/04/299ba483-image3-1024x640.png)

图 3：我们的请求已收到并得到响应的证据

在确认设置按预期工作后，我们需要验证 Saga 编排器设置中不同服务之间的事件流。

首先，我们必须确保所有必要的 Kafka 主题都已正确创建，并且消费者已订阅到正确的主题。您可以列出 Kafka 主题。

使用下面的 Docker 命令，我们可以访问 Docker 容器内的终端。

```bash
docker exec -it a457d90be977 bash
```

使用以下命令检索主题列表：

```bash
kafka-topics --bootstrap-server localhost:9092 --list
```

执行后，我们期望得到以下响应。

```
__consumer_offsets
inventory.updated
inventory_failed.reply
inventory_updated.reply
order.created
order_created.reply
payment.processed
payment_failed.reply
payment_success
payment_success.reply
```

我们现在将重新发送一个 `GET` 请求到 Saga 控制器中的 `saga/start/:orderId` 端点，以触发 Saga 流程。发送请求后，Saga 编排器应收到此请求并记录 Saga 已为订单 ID：12345 启动。
然后，它应该将一个事件（`order.created`）发布到 Kafka。

订单服务应随后使用此事件并对其进行处理。

订单服务应验证订单，并可能将另一个事件（如 `inventory.check`）发送到 Kafka。

库存服务应随后检查库存可用性，并以 `inventory.updated`（成功）或 `inventory.failed.reply`（失败）进行响应。

支付服务应处理支付并相应地发出 `payment_success` 或 `payment_failed.reply`。

最后，Saga 编排器应侦听最终的成功或失败消息，并将响应返回给客户端。

**如果成功：**

```json
{"message": "Saga completed successfully for order 12345"}
```

**如果失败：**

```json
{"message": "Saga failed for order 12345"}
```

借助 Kafka 事件，我们能够以容错方式触发和响应事件，并在必要时实施回滚策略，以确保系统中的一致性。这种 Saga 模式对于涉及多个微服务的长时间运行的业务流程至关重要，每个服务必须在保持原子性和可靠性的同时进行协作。

## 主要收获：

- Kafka 帮助解耦服务，并确保微服务之间的通信是异步且可靠的。
- Saga 编排器确保订单处理系统可以优雅地处理故障，并采取补偿措施，如支付和库存回滚。
- NestJS 提供了一个出色的平台来构建可扩展和可维护的微服务，这些微服务可以轻松地与 Kafka 集成。

您可以在 [GitHub](https://github.com/RaymondZziwa/saga) 上找到此实现的完整代码，以供参考并帮助您开始使用自己的分布式系统。

想要学习如何在 NestJS 中配置微服务吗？深入了解 Andela 的分步指南，[“使用 MySQL 和 Postman 在 NestJS 中配置微服务。”](https://www.andela.com/blog-posts/configure-microservices-in-nestjs-with-mysql-and-postman-a-beginners-guide/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=micrservices-nest-js&utm_term=writers-room)

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)