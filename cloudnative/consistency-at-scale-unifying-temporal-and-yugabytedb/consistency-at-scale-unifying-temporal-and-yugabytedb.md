
<!--
title: 规模一致性：Temporal与YugabyteDB的统一之道
cover: https://cdn.thenewstack.io/media/2025/09/f10a1884-twothings.jpg
summary: Manetu开源集成Temporal和YugabyteDB，解决AI部署中可靠性与治理挑战。此方案统一编排与持久性，简化架构，增强韧性，确保大规模信任。
-->

Manetu开源集成Temporal和YugabyteDB，解决AI部署中可靠性与治理挑战。此方案统一编排与持久性，简化架构，增强韧性，确保大规模信任。

> 译自：[Consistency at Scale: Unifying Temporal and YugabyteDB](https://thenewstack.io/consistency-at-scale-unifying-temporal-and-yugabytedb/)
> 
> 作者：Greg Haskins

AI、可靠性和治理并非可选项——它们是其他一切赖以生存的基础。数据平台 [Manetu](https://www.manetu.com/) 通过一个开源集成统一了 [Temporal](https://thenewstack.io/temporal-tackles-microservice-reliability-headaches/) 和 YugabyteDB，消除了复杂性，增强了韧性，并确保了大规模信任。

通过将编排和持久性合并到单个容错系统中，该解决方案解决了可能成就或破坏 [AI 部署](https://thenewstack.io/ai-operations/) 的基础设施挑战。它还强调了这些决策为何不仅对性能至关重要，而且对 AI 治理和可靠性的未来也至关重要。

## **Manetu 采取这种方法的原因**

在企业 AI 领域执行意味着要超越标准功能，这些功能使客户能够安全地参与信息经济。提供任何产品的可靠性和可扩展性方面的信心非常重要，因为技术栈中的任何故障或中断都可能对客户、客户的客户以及可能更广范围可见。

基础设施决策并非背景细节。它们定义了构建在其之上的一切的可靠性、韧性和可信度。

为了达到这些基础设施标准，Manetu 工程团队优先选择了经过验证和实战考验的技术。Temporal 和 YugabyteDB 是支撑其技术栈的两大支柱。通过将它们结合起来，Manetu 将强大的独立组件转变为一个统一的基础，保障了 AI 时代客户所需的信任。

Temporal 确保持久执行，保证关键工作流即使在出现故障时也能完成。YugabyteDB 提供分布式、容错的索引数据存储，能够处理大规模数据。

Manetu 在使这两种技术有效运行方面遇到的挑战并非源于它们各自的优势，而是源于它们的分离操作。Temporal 需要一个高性能、持久的存储，这正是 YugabyteDB 所擅长的。然而，将它们孤立运行会造成重复、增加操作负担，并引入在极端负载下容易出现问题的薄弱环节。

通过为 Yugabyte Cloud Query Language (YCQL) 创建一个开源的 Temporal CustomDataStore 驱动，Manetu 将它们的互补优势转化为一个单一、有韧性的基础。工作流现在在同一个系统中执行和持久化，减少了复杂性，同时增强了信任。对于客户而言，这意味着即使在压力下，策略执行、审计完整性和数据血缘仍能保持不间断。通过选择开源此集成，Manetu 确保了这些优势能够扩展到更广阔的生态系统。

## **从工程决策到客户影响**

这个开源解决方案不仅仅是削减了几毫秒的延迟；它在系统风险成为客户问题之前就将其消除了。

考虑协调失败。在编排层，它们可能表现为操作噪音。然而，在下游，它们体现为破裂的治理承诺，包括审计记录缺失、策略检查被绕过以及工作流陷入停滞。

通过统一编排和持久性，Manetu 创建了一个以一致性为保障的基础。客户体验到的不仅仅是技术改进，还有对以下方面的信心：他们的策略将正确执行，数据血缘将保持完整，并且治理护栏即使在压力下也能坚守。

## **对 AI 基础设施的更广泛影响**

AI 放大一切：速度、复杂性和风险。[大型语言模型](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) 和智能体 AI 系统以机器速度运行，以人类无法达到的规模发出请求和采取行动。如果你的基础动摇，这种放大效应将是灾难性的。

这就是为什么基础设施不能被视为事后才考虑的事情。它设定了可治理的边界，决定了系统是可解释的还是不透明的，并确认了策略是可强制执行的还是仅仅是美好的愿望。

将基础设施选择视为孤立工程细节的企业将面临客户能感受到的治理挑战，从合规漏洞到安全事件再到知识泄露。薄弱的基础会带来不稳定的结果。

## **为什么这个开源集成很重要**

通过将编排和持久性更紧密地结合，Manetu 简化了数据架构，减少了移动部件的数量，并提高了韧性。

开源 Temporal CustomDataStore 驱动以集成 Yugabyte YCQL 的决定是深思熟虑的。它允许更广泛的社区从更坚实的基础中受益。

基础设施提供商做出的每一个设计决策都成为其客户必须承受的决策。可靠性、可观测性和治理不是“以后再添加的功能”。它们需要被融入到基础中，否则它们将根本不存在。

在 AI 时代，一个坚实、[可靠且有韧性的数据](https://thenewstack.io/its-time-for-data-reliability-engineering/) 基础设施至关重要，因为它支撑着其他一切。

## **试用 Yugabyte YCQL 的 Temporal CustomDataStore 驱动**

您是 Temporal 用户，有兴趣使用 temporal-yugabyte 项目吗？通过 [Docker Compose](https://docs.docker.com/compose/) 试用此 [快速入门](https://github.com/manetu/temporal-yugabyte?tab=readme-ov-file#quickstart)：

在终端中，运行以下命令：

```
curl https://bit.ly/45O6aLP > quick-start.yml
docker-compose -f quick-start.yml up
```

这将部署一个完整的 Temporal 实例，预配置 YugabyteDB 作为其主要持久层。

要查看 Temporal UI，请将浏览器指向 <http://localhost:8080>，并在 Temporal 客户端中使用 localhost:7233 作为 Temporal 目标配置。

想了解更多吗？

这个 [GitHub 站点](https://github.com/manetu/temporal-yugabyte) 提供了该开源解决方案的全面描述、其历史、基准测试结果以及配置生产就绪部署的说明。

## **展望未来**

随着企业竞相采用智能体 AI，它们面临着一个岔路口。一条道路将基础设施视为商品管道，冒着治理级联失败的风险。另一条道路将基础设施视为治理本身的基底，这是一个必须保证策略、血缘和信任的层。

AI 的未来不会等待，决定这个未来是建立在可靠和有韧性的基础之上，还是建立在流沙之上，这些选择也刻不容缓。