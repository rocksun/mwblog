<!--
title: AWS Graviton5承诺25%性能飞跃
cover: https://cdn.thenewstack.io/media/2025/12/98e59e5e-img_2916-scaled.jpg
summary: AWS发布Graviton5芯片，性能提升25%，核心数192个，改进网络存储。推出Nitro Isolation Engine，用Rust构建，数学保证工作负载隔离。
-->

AWS发布Graviton5芯片，性能提升25%，核心数192个，改进网络存储。推出Nitro Isolation Engine，用Rust构建，数学保证工作负载隔离。

> 译自：[With Graviton5, AWS Promises a 25% Performance Boost](https://thenewstack.io/with-graviton5-aws-promises-a-25-performance-boost/)
> 
> 作者：Frederic Lardinois

LAS VEGAS — 在其年度 re:Invent 大会上，[AWS](https://aws.amazon.com/?utm_content=inline+mention) 今天[发布](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2)了其基于 Arm 的 Graviton 芯片的最新版本。该公司承诺，这些新芯片每个芯片将拥有 192 个核心（高于上一代的 96 个），性能将比两年前发布的 Graviton4 芯片提升高达 25%。

除了更高的速度，该团队还在其 Nitro 虚拟机管理程序卡上增加了一个新层，即 Nitro Isolation Engine，它现在通过数学方式保证不同工作负载相互隔离。

## Graviton5

AWS 副总裁兼杰出工程师 Ali Saidi 的团队开发了这些芯片，他告诉我，目前有超过 9 万名 AWS 客户使用 Graviton 芯片，并且 AWS EC2 计算服务的前 1000 名用户中有 98% 使用它们。正如 AWS 首席执行官 Matt Garman 本周早些时候宣布的那样，AWS 在过去几年中新增的 CPU 容量中，超过 50% 是基于 Graviton 的。

Saidi 表示：“这是一个涵盖我们 EC2 计算的故事，客户在那里获得自己的计算能力并运行自己的工作负载，也涵盖我们的托管服务——无服务器 Redshift 有 90% 基于 Graviton，Elasticache、Amazon、Aurora、DocumentDB，所有这些现在都超过 50% 基于 Graviton。”

[![AWS Graviton 徽标](https://cdn.thenewstack.io/media/2025/12/de5009a0-aa-graviton-5-hero-2000x1125-1.jpg)](https://cdn.thenewstack.io/media/2025/12/de5009a0-aa-graviton-5-hero-2000x1125-1.jpg)

Graviton 徽标。图片来源：AWS。

通过 Graviton5，团队不仅专注于提高原始基准性能，还确保这些性能提升也适用于实际用例。当然，更多的核心对此有所帮助，但正如 Saidi 指出的那样，让这些核心更紧密地排列在一起，也能在可扩展性和延迟方面带来优势。例如，对于某些工作负载，这可能意味着性能提升 30% 到 40%。

他还指出，这些工作负载受益于更大的缓存，每个核心可访问的 L3 缓存是上一代的 2.6 倍（这意味着核心理想情况下等待数据到达以开始计算的时间会大大减少）。

该团队还改进了网络和存储带宽。

## Nitro Isolation Engine

从计算机科学的角度来看，今天更有趣的更新可能并非芯片本身，而是 Nitro Isolation Engine。AWS 长期以来一直承诺其 Nitro 系统——为 EC2 定制的硬件虚拟化系统——将对不同工作负载进行沙盒隔离，并确保它们之间不会泄露任何信息。

这是第六代 Nitro 卡，团队首次决定进一步细分虚拟机管理程序的功能。Saidi 解释说：“我们想：我们能否将操作页表和处理访客状态等功能的代码，放入它自己非常薄的一层中？”

这个新层是用 Rust 构建的，Rust 本身就承诺增强内存和并发安全。但更重要的是，由于团队是从零开始的，它与 AWS 的自动化推理小组合作，从第一天起就将形式化验证作为开发过程的组成部分。

Saidi 解释说：“它在访客保密性方面并没有提供比虚拟机管理程序更多的功能。但我们能够说：看，这就是我们在这方面提升标准的方式。这就是我们努力提高透明度的方式，向你展示我们如何使用形式化验证来实际说明，是的，我们正在保持访客内容彼此隔离，并与我们隔离。”