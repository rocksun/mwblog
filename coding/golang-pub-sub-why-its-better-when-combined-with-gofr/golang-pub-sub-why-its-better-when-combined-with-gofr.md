
<!--
title: Golang 发布/订阅：为什么与 GoFr 结合使用会更好？
cover: https://cdn.thenewstack.io/media/2024/05/1b47a8e1-gofr-logo-2.png
-->

为了充分利用 Golang 在发布/订阅设置中的能力，GoFr 框架可以帮助简化流程并引入强大的功能。

> 译自 [Golang Pub/Sub: Why It’s Better When Combined With GoFr](https://thenewstack.io/golang-pub-sub-why-its-better-when-combined-with-gofr/)，作者 Robert Kimani。

随着现代系统的演进，对可靠、可扩展和实时通信的需求从未如此强烈。[发布/订阅（pub/sub）](https://thenewstack.io/publish-subscribe-introduction-to-scalable-messaging/) 是一种消息传递模式，允许系统的不同组件进行异步通信。这种解耦架构是物联网 (IoT)、分布式系统和实时应用程序的支柱，在这些应用程序中，响应能力和灵活性至关重要。

在构建这些系统时，[Golang](https://thenewstack.io/go/) 凭借其简单性、效率和内置并发性成为一种显而易见的选择。但为了在发布/订阅设置中充分利用 Golang 的功能，框架 [GoFr](https://thenewstack.io/gofr-a-go-framework-to-power-scalable-and-observable-apps/) 提供了优化的解决方案，简化了流程并引入了强大的功能。

领先的公司已经使用 GoFr 等框架成功实施了发布/订阅系统，以解决复杂的挑战。例如，LinkedIn、Pinterest 和沃尔玛都利用事件驱动架构和发布/订阅来管理海量数据并确保系统可靠性。

GoFr 提供了一套强大的工具和功能，提升了 Golang 的发布/订阅能力，使其成为构建可扩展、实时系统的理想选择，尤其是在物联网领域。通过选择 GoFr，开发人员可以受益于经过验证的框架，该框架简化了开发过程并确保其发布/订阅系统可靠且易于管理。

[事件驱动架构 (EDA)](https://thenewstack.io/the-basics-of-event-driven-architectures/) 是现代、可扩展且具有弹性的实时系统的核心。与服务同步通信的传统请求-响应模型不同，EDA 允许异步通信。这将服务解耦，使它们能够独立运行并实时响应事件。 
对于设备不断生成和交换数据的物联网应用而言，发布/订阅成为一种关键的通信机制。通过实施发布/订阅，物联网系统可以处理大量设备，确保可扩展性、可靠性和实时响应能力。发布/订阅处理高吞吐量、低延迟通信的能力在这些环境中尤其重要。

在本文中，我将向您展示为什么 GoFr 与 Golang 结合是构建高性能发布/订阅系统的完美搭配，以及如何使用 [通信协议 MQTT](https://www.influxdata.com/mqtt) 的物联网示例快速入门。

## 为什么在 Golang 中选择 GoFr 进行发布/订阅？

[Golang 在构建分布式系统方面声名鹊起](https://thenewstack.io/what-made-golang-so-popular-the-languages-creators-look-back/)，因为它具有令人印象深刻的性能和并发模型。发布/订阅架构从 Go 的 goroutine 中获益匪浅，goroutine 允许在不同服务之间进行轻量级异步通信，而不会引入明显的开销。这在必须同时处理多个事件的系统中至关重要。

以下是 GoFr 成为使用 Go 构建物联网系统和其他实时应用程序的开发人员的理想选择的原因：

-   简单性和效率。GoFr 抽象了与设置发布/订阅相关的大部分样板代码，允许开发人员专注于业务逻辑而不是基础设施管理。
-   支持多种消息代理。GoFr 原生支持各种消息代理，包括
    [Apache Kafka](https://thenewstack.io/hybrid-data-collection-from-the-iot-edge-with-mqtt-and-kafka/)、Google 发布/订阅和 MQTT。这种灵活性确保开发人员能够为其特定用例选择最佳代理。
-   全面的监控和安全。凭借内置的监控和安全功能，GoFr 确保您的发布/订阅系统不仅高效，而且安全且易于管理。
-   通过 MQTT 针对物联网进行了优化。MQTT 是一种专为物联网设计的轻量级消息传递协议，GoFr 对 MQTT 的支持使其成为物联网后端的绝佳选择。GoFr 简化了 MQTT 代理的设置和管理，使其能够无缝集成到您的物联网系统中。
-   路由和中间件。使用内置的路由处理和中间件简化了 REST API 的设置。
-   数据库支持。轻松连接到
    [SQL](https://thenewstack.io/how-to-write-sql-queries/)、[NoSQL](https://thenewstack.io/why-choose-a-nosql-database-there-are-many-great-reasons/) 和[时间序列数据库](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/) 以进行数据存储和处理。

## 使用 GoFr 优化发布/订阅
GoFr 在构建时考虑了可扩展性和易用性。它原生支持 MQTT，MQTT 是物联网系统中用于实时通信的最流行协议之一。通过利用 GoFr 内置的 [发布/订阅](https://github.com/gofr-dev/gofr/blob/development/examples/using-publisher/main.go) 功能，您可以轻松设置强大的系统。

以下是使用 GoFr 设置简单的基于 MQTT 的发布/订阅系统的方法。

### 设置开发环境

首先，初始化您的 Go 模块并将 GoFr 包添加到您的项目中：

```
go mod init github.com/gofr_iot_project
go get gofr.dev
```

### 用于发布消息的示例代码

```go
package main

import (
    "encoding/json"
    "gofr.dev/pkg/gofr"
)

func main() {
    app := gofr.New()
  
    app.POST("/light", SmartLight)
  
    app.Run()
}

func SmartLight(ctx *gofr.Context) (interface{}, error) {
    type smartLight struct {
        Mode string `json:"mode"`
    }
  
    var data smartLight
  
    err := ctx.Bind(&data)
    if err != nil {
        return nil, err
    }
  
    msg, _ := json.Marshal(data)
  
    err = ctx.GetPublisher().Publish(ctx, "room-smart-light", msg)
    if err != nil {
        return nil, err
    }
  
    return "Published", nil
}
```

这个简单的示例设置了一个 REST API 端点 `/light` ，它接收有关智能灯模式的数据并将其发布到 MQTT 主题 `room-smart-light`。订阅此主题的任何物联网设备都将收到该消息。

您可以通过在 `.env` 文件中添加以下配置来连接到 [MQTT](https://github.com/gofr-dev/gofr/blob/development/examples/using-subscriber/configs/.env) 代理：

```
PUBSUB_BACKEND=MQTT
```

在配置行 `PUBSUB_BACKEND=MQTT` 中，无需指定其他凭据（如 ID 或密码），因为我们连接的是公共 MQTT 代理。

与私有或安全的代理不同，公共代理不需要用户名或密码等身份验证详细信息。这使得入门和测试系统变得更加容易，而无需担心设置复杂的安全性配置。但是，对于生产环境或更敏感的应用程序，连接到私有代理通常需要凭据才能确保安全的通信。

此外，GoFr 通过提供内置的跟踪器端点来简化跟踪和监控。此跟踪器允许您实时监控数据流，跟踪事件生命周期并识别出现的性能瓶颈或错误。这种级别的可见性在扩展系统或排除故障时至关重要，因为它可以帮助您维护系统运行状况并确保按预期处理事件。

### 用于订阅主题的示例代码

同样，您可以创建一个侦听主题并处理传入消息的订阅者：

```go
app.Subscribe("room-smart-light", func(ctx *gofr.Context) error {
   // Handle the message
   return nil
})
```

## 使用 GoFr 的物联网后端的高级架构

在使用 GoFr 设计物联网后端时，架构通常涉及几个关键组件：

- **API 网关。** API 网关充当管理和路由 API 请求的中心点。借助 GoFr，设置 CRUD API 得到了简化，这要归功于 `AddRESTHandlers` 等功能，这些功能可自动执行路由处理和数据库集成。
- **设备管理。** 安全且可扩展的设备管理对于物联网系统至关重要。GoFr 包含内置的身份验证中间件，该中间件支持 OAuth 和 Basic-Auth 等多种机制，可确保服务之间的安全通信。
- **数据提取和处理。** GoFr 通过 MQTT 和 HTTP 支持实时数据处理。它还与各种数据库无缝集成，可以轻松存储和处理大量数据。
- **监控和安全。** 强大的监控和安全对于任何物联网后端都至关重要。GoFr 提供全面的监控功能，可提供有关系统性能和安全性的见解。

GoFr 的核心是可扩展性和容错能力，使其非常适合处理物联网等高吞吐量系统。它包括重试机制、死信队列和断路器等基本功能，即使在负载过重或组件发生故障的情况下，也能确保系统保持弹性。

死信队列会捕获无法处理的消息并将它们移动到单独的队列以供进一步检查，从而允许操作员以受控方式处理异常。

断路器通过停止与故障服务的通信来防止级联故障，直到它们恢复，从而最大限度地减少单个服务故障对整个系统的影响。

安全性是另一个关键考虑因素，GoFr 支持各种身份验证机制，包括 OAuth、基本身份验证和其他安全通信方法，确保在服务之间安全地传输数据。

尝试将 GoFr 用于使用 Go 构建的发布/订阅系统，看看您是否没有获得我所描述的好处。
