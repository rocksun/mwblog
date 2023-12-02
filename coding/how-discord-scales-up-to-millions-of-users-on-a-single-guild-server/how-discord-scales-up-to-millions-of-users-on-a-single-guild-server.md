<!--
title:  Discord如何实现单服务器数百万用户扩展
cover: https://cdn.thenewstack.io/media/2023/11/d043aa93-fausto-garcia-menendez-chqvnnr8df4-unsplash-e1700600130442-1024x684.jpg
-->

在当今时代，应用的扩展性已与网络、存储、安全及数据本身构成同等重要的因素。

> 译自 [How Discord Scales up to Millions of Users on a Single Guild (Server)](https://thenewstack.io/how-discord-scales-up-to-millions-of-users-on-a-single-guild-server/)，作者 Chris J. Preimesberger。

IT 系统不仅仅是关于处理数据和将数据从一个位置移动到另一个位置以完成生产任务。根据使用案例，它们也关于从一个位置处理数据并将其分发到多个位置，以便完成工作。

这就是“扩展性”这个词出现的地方。扩展性已经成为与联网、存储、安全 —— 当然还有数据本身 —— 一样重要的因素，这些都是完成工作所必需的。

[Discord](https://discord.com/) 知道什么是扩展性。这家 7 岁的免费/开源通信平台将文本、语音和视频聊天功能整合到一个简单的界面中，正在经历巨大的增长和大扩展性的扩展需求。它在游戏玩家中很受欢迎，但它也被来自世界各地的人用来与朋友、家人和社区联系。

Discord 是一个流行工具，原因有很多：它是免费的、易于使用，并提供了各种功能，使其成为一个强大的交流和协作平台。它们包括:

- **屏幕共享**:用户可以与他人实时共享自己的屏幕，这对协作或故障排除很有用。
- **文件共享**:用户可以与他人共享文件，包括图像、视频和文档。
- **机器人**:用户可以为自己的服务器创建或添加机器人来自动化任务，例如内容审核或音乐播放。
- **集成**:Discord 与许多其他服务(如 Twitch、YouTube 和 Spotify)集成，这使得与他人共享内容变得很容易。

## 用于 Midjourney 的流水线

Discord 是连接超过 1600 万 Midjourney 用户的最大平台，Midjourney 是一款正在公测的生成式人工智能程序和服务，由旧金山的独立研究实验室 [Midjourney](https://www.midjourney.com/home) 公司创建和托管。Midjourney 的功能相对简单：用户输入图像提示，并得到 4 张图像作为回报。它可以是任何东西的图像：超级英雄、风景、水果、人类或许多其他项目或概念。

一旦用户用 Midjourney 生成了一个图像，他们可以将其铸造成 NFT(非同质化代币)在任何 [NFT](https://thenewstack.io/metadata-key-to-unlocking-nft-utility/) 市场上，比如 [OpenSea](https://opensea.io/) 或 [Rarible](https://rarible.com/)。NFT 是一种加密货币资产，与唯一的数字对象(如图像、视频或音频文件)相关联。NFT 可用于证明数字艺术品的所有权，并向其他人出售。

Midjourney 类似于其他 AI 艺术生成器，例如 [DALL-E 2](https://thenewstack.io/how-to-lower-your-companys-ai-risk-in-2023/)、Bing 图像创作器、Dream by WOMBO、NightCafe 和 OpenArt。但是 Midjourney 有一些独特的功能，最显著的是它能够以各种艺术风格生成图像。而且因为它也能根据多个提示生成图像，用户可以创建比其他 AI 艺术生成器更复杂和详细的图像。

Discord 的核心技术副总裁 [Mark Smith](https://www.linkedin.com/in/zorkian/) 告诉 The New Stack，他们正在开发公共 API，允许开发者创建自己的 Midjourney 应用程序。但是，还没有公布什么时候会推出。

Midjourney 社区为 Discord 提供了大部分流量。成员们 - 通常同一时间窗口内超过 100 万 - 分享他们的艺术品，提出问题并相互帮助学习如何使用 Midjourney。其他一些在线社区也开始为 Midjourney 用户提供服务，包括 Reddit 和 Facebook。

Discord 显然是这个新兴社区增长的支柱。但它也从一些出色的开发工具中获得了很多帮助。

“Midjourney 的起点是他们有一个网站，但 Discord 是人们实际参与生成式 AI 体验(尤其是其社交方面)的主要途径。”Smith 告诉 The New Stack。“能够与你的朋友们聚在一起，生成一些 AI 艺术，闲聊，玩得开心，然后来回分享 - 这就是目标，而且现在依然如此。同一时间有数百万人在使用它。”

## 开发者如何管理所有这些事务

Discord 可在台式机、Web 和移动设备上使用，允许用户创建和加入服务器，这本质上是专门用于特定主题或兴趣的聊天室。服务器可以是公开的或私人的，它们可以有不同级别的访问和审核。在服务器内 - 也称为公会 - 用户可以创建频道，这就像专门用于特定主题或活动的子房间。频道可以是基于文本、语音或视频的。

保持所有这些频道不间断运行、相互隔离和安全 - 更不用说每分钟都有新的用户和频道激增 - 是一项复杂的开发问题。但是，如果开发者不知道使用什么工具来管理数百万用户的部署——且在单个服务器上，那么这对他们来说就会成为一个问题。

“要成功做到这一点，您需要两件主要东西，”Smith说。“第一件事是您真的需要了解系统的性能以及系统可以执行的操作。它在资源方面消耗了多少?第二件对此很重要的事情是理解您正在努力提供的产品体验。”

## 深入开发过程的核心

Discord 通过充分利用 [Elixir](https://thenewstack.io/elixir-sdk-for-configcat/) 来实现这一点，这是一种动态的函数式编程语言，运行在 [Erlang 虚拟机](https://www.erlang.org/blog/a-brief-beam-primer/)(EVM，常称为 [BEAM](https://www.erlang.org/blog/a-brief-beam-primer/))上。Elixir 被设计来构建可扩展和可维护的应用程序，并被用于各种领域，包括 Web 开发、嵌入式系统、机器学习、数据流水线和多媒体处理。

Smith 说，旧的可以再次变得新的。“Elixir 是索尼爱立信在 20 世纪 60 年代为电信开发的。对于像 Discord 这样的使用案例，当您试图扩展通信来提高可靠性和效率时，它非常合适，”他说。

BEAM 使用基于进程的体系结构，其中每个进程都在自己的隔离内存空间中运行。BEAM 可以限制需要较慢执行的请求，以处理大量并发请求，而不会阻塞或减慢其中任何一个;这是处理所有查询的秘密武器。

Elixir 的一些关键特性包括:

- **并发性**:Elixir 建立在以能够高效处理并发性而闻名的 EVM 之上。这使得 Elixir 成为需要同时处理大量请求的应用程序的不错选择。
- **可扩展性**:Elixir 应用程序很容易进行水平扩展，这意味着它们可以扩展到多台服务器上来处理增加的流量。
- **可维护性**:Elixir 代码通常认为可读性好、易于维护。这得益于它的函数式编程范式，强调不可变的数据和纯函数。
- **工具链**:Elixir 有一个丰富的工具和库生态系统，这使得开发和部署 Elixir 应用程序变得很容易。

“每当在 Discord 上发生一些事情，比如发送消息或有人加入语音频道时，我们会更新在线的每个人在客户端中的 UI(有时称为 '公会')，” Discord 的软件工程师 [Yuliy Pisetskiy](https://www.linkedin.com/in/yuliy-pisetsky-2a3578204/) 在最近的[一篇博文](http://dis.gd/midjourney-blog)中写道。“我们为每个服务器使用单个 Elixir 进程作为发生在该服务器上的所有事情的集中路由点，并为每个连接的用户的客户端使用另一个进程(‘会话’)。”

“公会进程会跟踪属于该公会的用户的会话，并负责将操作分发给这些会话。一旦会话接收到这些更新，它们就会通过 [WebSocket](https://thenewstack.io/the-challenge-of-scaling-websockets/) 连接将它们转发给客户端。”

虽然这些进程很复杂，但通过 Elixir 提供的自动化得以简化，而 Discord 已经掌握了这种横向扩展工具的使用方法。

一些流行的 Elixir 框架和库包括:

- **Phoenix**:[Web 开发框架](https://thenewstack.io/pushup-offers-speed-of-go-in-web-development-framework/)。
- **Nerves**:开发嵌入式系统的框架。
- **Ecto**:数据库库。
- **ExUnit**:[测试框架](https://thenewstack.io/jest-metas-javascript-testing-framework-joins-openjs/)。
- **GenServer**: 开发并发和分布式系统的库。
