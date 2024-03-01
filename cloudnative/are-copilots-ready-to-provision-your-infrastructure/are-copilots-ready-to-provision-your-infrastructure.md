<!--
title: Copilots准备好用于基础设施了吗？
cover: https://cdn.thenewstack.io/media/2024/02/bf8d229b-copilots3-1024x512.png
-->

如何引入标准化和最佳实践，实现基础设施部署流程的更多自动化？

> 译自 [Are Copilots Ready to Provision Your Infrastructure?](https://thenewstack.io/are-copilots-ready-to-provision-your-infrastructure/)，作者 Rak Siva 是 Team Nitric 的工程副总裁，深信提升软件开发者的体验至关重要。

AI copilots 在编码领域取得了显著进展，提供实时帮助，自动化常规任务，并从大量代码库中提供深思熟虑的建议。这些同行不仅提供了通用建议；它们还根据您的输入提供上下文相关的建议，并生成代码片段，就像有一位经验丰富的开发人员指导您一样。

然而，在代码生成领域，我们仍在不断发展。虽然 [AI copilots](https://thenewstack.io/microsoft-one-ups-google-with-copilot-stack-for-developers/) 可以提出建议，但开发人员需要引导这些建议以使其与其应用程序的意图保持一致。这种相互作用确保了 AI 的帮助与开发人员的领域专业知识相辅相成，在业务和软件/架构领域都至关重要。

当领域知识复杂或缺乏行业标准化时，例如在[生成应用程序运行时环境的基础设施即代码（IaC）](https://thenewstack.io/generative-ai-tools-for-infrastructure-as-code/)时，这种协作变得尤为具有挑战性。经过大量关于 IaC 生成的实验后，很明显，无论我们试图生成 Terraform、AWS 云开发工具包（CDK）还是 Pulumi 代码，都需要相当数量的人工输入和专业知识来生成可用的代码。

挑战出现了：我们如何引入标准化和最佳实践来实现基础设施部署管道的更多自动化？

## 自动化框架可能是关键吗？

现代云应用框架提供了一套高级结构，大大简化了基础设施的自动化。结构是组装更复杂结构或系统所需的基本组件或元素。它们提供了预定义的功能、模式或模板，可用于更有效地构建、管理和扩展应用程序。

以下是构建现代云应用程序常用的结构示例：

| 结构类型    | 描述                                                                                     |
| ---------- | ---------------------------------------------------------------------------------------- |
| APIs       | 通过简化的管理和创建，用于在云服务之间集成和通信的基本组件。                                |
| 消息传递    | 实现了高效的异步消息队列处理以及发布和订阅事件。                                           |
| 对象存储    | 便于与云存储服务进行交互和管理。                                                         |
| 函数       | 通过部署处理 API 路由、定时任务和触发事件的函数构件，简化了开发流程。                     |
| 调度程序    | 自动化和管理任务和工作流的时间和执行。                                                    |
| Websockets | 提供了客户端和服务器之间实时、双向通信的渠道，对于交互式应用程序至关重要。             |

GitHub Copilot，虽然无法完全管理基础设施的全部范围，但似乎在增强应用程序逻辑开发方面表现良好。利用这些高级结构，AI 协作伙伴可以更有效地为[云环境中的应用程序开发和运营任务](https://thenewstack.io/how-to-choose-a-cloud-development-environment/)提供自动化和优化。

将安全最佳实践和合规要求嵌入这些框架中，结合 AI 协助编程工具的分析能力，也可以增强应用程序的整体安全性。例如，框架可以确保所有资源都以最低权限进行配置；用于构建应用程序代码的提示也可以针对创建适当大小的安全足迹 —— 基本上没有不必要的资源。

## 实践中的应用

假设我们正在为一个消息应用程序构建基本后端，使用以下结构：

- Websockets
- 调度程序
- 无服务器函数

```javascript
import { websocket, collection } from "@nitric/sdk";

// A collection to store connections
const connections = collection("connections").for(
  "reading",
  "writing",
  "deleting"
);

// Initialize the WebSocket server
const socket = websocket("socket");

// Store the new connection in the collection
socket.on("connect", async (ctx) => {
  await connections.doc(ctx.req.connectionId).set({});
});

// Remove the disconnected client from the collection
socket.on("disconnect", async (ctx) => {
  await connections.doc(ctx.req.connectionId).delete();
});

 // Broadcast the incoming message to all other connected clients
socket.on("message", async (ctx) => {
  const allConnections = await connections.query().stream();
  const streamEnd = new Promise<any>((res) => allConnections.on("end", res));

  allConnections.on("data", async (connection) => {
    if (connection.id !== ctx.req.connectionId) {
      await socket.send(connection.id, ctx.req.data);
    }
  });
  await streamEnd;
});
```

以下是使用 GitHub Copilot 自动生成的应用逻辑片段，其中包含一些提示性注释，比如“安排一个每两个小时运行一次的任务”。我们希望通知所有连接的用户，让他们知道一个按计划发生的重要事件。

```javascript
// Schedule a task that runs every 2 hours
schedule("pizzaTimeNotification").every("2 hours", async (ctx) => {
  // Retrieve all user connections from the collection
  const allConnections = await connections.query().stream();

  const pizzaTimeMessage = { type: "notification", text: "It's pizza time!" };
  allConnections.on("data", async (connection) => {
    await socket.send(connection.id, ctx.req.data);
  });
});
```

**附注**：需要进行一些微调 —— 代码的第一个版本使用了 `for` 循环而不是 `on` 事件。

```javascript
 // Send the message to all connected users
  for await (const connection of allConnections) {
    await socket.send(connection.id, pizzaTimeMessage);
  }
```

利用这些高级结构，我们不再需要直接生成为该应用程序提供所需运行时所需的 IaC。因此，我们依赖框架来引入领域专业知识，指导应配置和提供哪些内容。

注意：在大多数现代框架的底层是我们实施最佳实践的 IaC。这一点很关键，因为我们仍然可以利用所有出色的工具，在生成式 AI 的早期实验阶段进行静态分析。

在这个示例中，我们允许 AI 帮助我们使用高级构造生成应用程序业务逻辑，比如计划、集合、服务和 API 网关，因此我们可以有效地跳过生成高度定制且难以维护的基础设施代码。

## IaC 迈出的又一步

我们继续推动 IaC 和 IfC（Infrastructure from Code）的边界。由于我们通过 AI 生成的[应用程序代码有了基础设施需求](https://thenewstack.io/serverless-needs-standards-to-be-the-future-of-application-infrastructure/)的底层规范，我们可以再进一步。

下面[是一个应用程序基础设施的实时图像](https://nitric.io/blog/v1-release#visualize-your-app-s-architecture)，当开发人员添加或移除资源时，它会自动更新。

![Zoom]([image.png](https://cdn.thenewstack.io/media/2024/02/8666aade-architecture-dashboard-4-scaled.jpg))

## 拥抱软件开发的未来

一个重要的未来挑战是将 AI 生成的基础设施与遗留系统集成，这是我们在 [Nitric](https://nitric.io/) 上正在探讨的话题。随着 AI 协助编程工具和框架的发展，它们承诺了更加流畅、高效的基础设施供应路径，平衡创新与现有系统的现实。

对我来说，很明显，利用像 Nitric 这样的框架的 AI 协助编程工具不仅仅是方便的工具，而且是我们行业发展的基础。与这些不断发展的工具互动，不仅是为了保持相关性，更是为了塑造[软件开发未来](https://thenewstack.io/ai-machine-learning-and-the-future-of-software-development/)。

我鼓励你踏出这一步。开始一个 Nitric 项目。将 AI 协助编程工具整合到你的工作流程中。探索这些工具开启的可能性领域。最重要的是，与社区分享你的经历。我们的反馈、实验和对这项技术的贡献将有助于引导其发展方向。
