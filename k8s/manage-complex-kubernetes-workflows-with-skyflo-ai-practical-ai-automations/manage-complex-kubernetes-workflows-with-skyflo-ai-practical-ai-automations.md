
<!--
title: 使用AI解决方案管理复杂的Kubernetes工作流程
cover: https://cdn.thenewstack.io/media/2025/05/7edec154-nikita-nikitenko-_gqc-3qtqb0-unsplash-scaled.jpg
summary: 告别深夜告警！AI神器 Skyflo.ai 拯救你的 Kubernetes 工作流。利用 Planner/Executor/Validator Agents，自动化 Pod 状态检查、日志分析、资源验证等繁琐任务。告别 kubectl 命令，拥抱自然语言交互，快速定位并修复 Pending 状态等问题，DevOps 效率🚀提升！
-->

告别深夜告警！AI神器 Skyflo.ai 拯救你的 Kubernetes 工作流。利用 Planner/Executor/Validator Agents，自动化 Pod 状态检查、日志分析、资源验证等繁琐任务。告别 kubectl 命令，拥抱自然语言交互，快速定位并修复 Pending 状态等问题，DevOps 效率🚀提升！

> 译自：[Manage Complex Kubernetes Workflows With an AI Solution](https://thenewstack.io/manage-complex-kubernetes-workflows-with-skyflo-ai-practical-ai-automations/)
> 
> 作者：Karan Jagtiani

当时是凌晨 2:45，我的手机不停地嗡嗡作响，我完全醒着。我们的生产系统宕机了，主要的后端 API Pod 卡在了可怕的“Pending”状态。任何[管理过繁忙的云原生环境](https://thenewstack.io/whats-next-managing-data-in-cloud-native-environments/)的人都知道，深夜警报总是在最糟糕的时候到来。但对我来说，这是一场严峻的考验。我挣扎着起床，浏览 Slack 消息，试图解码出了什么问题。团队当天早些时候发布了一个小更新，确信一切都井然有序。几个小时后，我们意识到最轻微的疏忽都可能演变成重大事件。

那天晚上，我花了将近两个小时挖掘日志、比较资源配置，并确定我们的部署更改是否意外导致了容量问题。一个错误的资源设置就足以破坏整个系统。像这样的深夜作战室对我来说并不陌生。我经历过很多次这样的紧急情况。在我担任云架构师的这些年里，我逐渐体会到云原生系统一旦达到特定规模，就会变得多么脆弱。但即使作为一名经验丰富的从业者，每次事件都会呈现出独特的曲折，提醒我，虽然[云原生工具功能强大](https://thenewstack.io/is-cloud-native-a-vibe-power-users-weigh-in/)，但需要持续的警惕和专业知识才能正确管理。

下面，我将分享我通常如何调试这些事件，以及 Skyflo.ai 的 AI 驱动自动化如何帮助减少在不可避免地出现问题时的深夜恐慌。

## 解开夜晚的谜团：一个真实的调试剧本

当系统崩溃时，人们很容易不假思索地采取行动。但是，如果没有策略地四处奔波，通常会导致更多的混乱。多年来，我采用了一种有条不紊的方法，可以帮助发现根本原因：

**1. 检查 Pod 状态和事件**

首先运行：

`kubectl get pods -n <namespace>`

这会显示哪些 Pod 正在失败。为了更深入地了解，我将描述一个特定的 Pod：

`kubectl describe pod <pod-name> -n <namespace>`

这会显示容器状态、资源使用情况和任何触发的事件。

接下来，我将查看按创建时间排序的总体事件：

`kubectl get events -n <namespace> --sort-by='.metadata.creationTimestamp'`

通常，这些事件包含有关待处理的资源请求、污点或错误配置的宝贵线索。

**2. 梳理日志**

我的下一步是检查失败 Pod 的日志：

`kubectl logs <pod-name> -n <namespace>`

如果容器重启多次，我可能会添加 `--previous`
以查看早期实例的日志：

`kubectl logs <pod-name> -n <namespace> --previous`

在这里，我将查找重复出现的堆栈跟踪或明确的错误消息（例如，内存不足或连接超时）。

**3. 验证资源利用率**

当 Pod 卡在 Pending 状态或反复崩溃时，资源约束通常会发挥作用：

`kubectl top pods`

`kubectl top nodes`

内存或 CPU 使用率峰值可以表明请求/限制是否配置错误。

**4. 查看部署和配置历史记录**

对于通过云原生工具进行的更新，请确认您的系统更改与您的意图相符。如果我使用了 chart 或 pipeline，我将查看修订历史记录：

```
# For Helm-based setups
helm list --all-namespaces
helm history <release-name>
```

或

```
# For Argo-based releases
argo get rollouts -n <namespace>
```

有时，隐藏的回滚或部分部署可能引入了不一致的配置。

这些手动步骤有助于查明问题，但也突出了为什么重复的救火工作如此令人疲惫。调试[复杂的云原生环境](https://thenewstack.io/terraform-beta-supports-multicloud-complex-environments/)可能会变成一个重复的日志、事件和资源定义难题。这就是像 Skyflo.ai 这样的 AI 驱动的解决方案发挥作用的地方。

## 隆重推出 Skyflo.ai：世界上第一个云原生 AI 代理

现代云原生生态系统远比单个开发人员能够有效管理的复杂得多，尤其是在压力下。**Skyflo.ai** 通过提供一个 AI 驱动的开源平台，专门用于自动化这些复杂的步骤，从而为处理运营任务提供了一个全新的视角。Skyflo.ai 不是手动翻阅日志和清单，而是使用专门的多代理架构来协调它们。

**Skyflo.ai 的工作原理**

- **Planner Agent (规划器代理)**: 解析自然语言指令，并将其转换为各种云原生工具中的离散任务。 如果你说“检查为什么主后端 Pod 卡在 Pending 状态”，它知道如何检索日志、查看资源状态和收集事件数据。
- **Executor Agent (执行器代理)**: 安全地执行这些任务，利用与你手动运行相同的命令。 可以把它想象成一个[自动化 DevOps 工程师](https://thenewstack.io/zh/why-internal-developer-portals-need-automations/)，执行有针对性的操作，例如 kubectl logs、扩展 Pod 或描述你环境中的资源。
- **Validator Agent (验证器代理)**: 仔细检查 Executor 的工作，确保结果与你声明的意图一致。 如果你指示它增加内存限制，Validator 将验证新设置是否已生效，而不会引入新问题。

## Skyflo.ai 的深夜救援

假设你在凌晨 2:45 接到同样的令人恐惧的电话：你的生产系统宕机，并且主要的后端 Pod 卡在 Pending 状态。 在一个典型的夜晚，你会跳到你的终端，运行一堆命令，并开始排除过程。 但是使用 Skyflo.ai，工作流程会发生变化：

**1. 用简单的语言描述情况**

你打开 Skyflo.ai 并输入：

* > “生产环境中的主要后端 API Pod 卡在 Pending 状态。 找出问题并修复它。”*

**2. Planner Agent 启动**

无需手动猜测，Planner Agent 决定收集哪些诊断信息。 它指示 Executor Agent 运行一系列命令，例如：

`kubectl get pods -n <namespace>`

`kubectl describe pod <pod-name> -n <namespace>`

`kubectl get events -n <namespace> --sort-by='.metadata.creationTimestamp'`

它也可能检查资源使用情况：

`kubectl top nodes`

这系统地涵盖了所有主要基础。

**3. 自动诊断**

根据收集到的信息，Planner Agent 可能会注意到节点已满，或者配置错误的资源请求阻止了新 Pod 的调度。

你会得到一个简明的解释，例如，“*Pod 仍然处于 Pending 状态，因为请求的内存超过了可用节点容量*。”

**4. 建议的补救措施**

Planner Agent 提出后续步骤。

例如：“*将主后端 API Pod 的内存请求从 2 Gi 减少到 1 Gi*”或“*扩展集群以增加容量*”。 该代理会显示建议的更改，并在应用之前提示你确认。

**5. Executor Agent 采取行动，Validator 检查**

Executor Agent 补丁部署或更新相关的资源清单。 然后，Validator Agent 验证 Pod 是否已正确调度，并在你退出之前验证环境是否再次稳定。

这种方法不仅缩短了事件的持续时间，而且还保持了你的理智。 不再在凌晨 3 点翻找日志； 让 Skyflo.ai 处理重复性任务，而你专注于更高级别的决策。

## 为什么 AI 驱动的自动化正在改变云原生运维

根据我的经验，任何大型生产环境都充满了微妙的复杂性。 资源分配中的一个小错误、错误标记的注释或一个过时的密钥都可能引发混乱，并在多个微服务中蔓延。 **Skyflo.ai** 解决了 [DevOps 团队](https://thenewstack.io/zh/how-a-critical-hosting-failure-solved-a-devops-crisis/) 经常面临的几个关键障碍：

**1. 速度和效率**

AI 驱动的例程不会感到疲劳。 他们有条不紊地检查相关的日志、事件、资源定义或部署历史记录。 这种一致性减少了跟踪根本原因所需的时间。

**2. 可访问的专业知识**

即使是初级开发人员也可以使用简单的语言与 Skyflo.ai 交互，使他们能够像专业人士一样进行故障排除。 同时，经验丰富的架构师可以从更快的洞察力和处理繁重工作的自动化任务中受益。

**3. 降低人为错误的风险**

手动命令容易出现拼写错误和误解。 在使用错误的命名空间运行命令后，我感到非常沮丧。 通过自动平台交叉验证更改，系统会更新正确的环境。

**4. 持续学习**

由于 Skyflo.ai 是专门为云原生构建的，具有多代理、开源模型，因此社区可以在实际场景中对其进行训练，随着时间的推移改进其建议。 随着平台的不断发展，它会理解更多细微的故障排除路径，确保它不会反复陷入相同的问题。

## 你的任务，如果你选择接受它

深夜系统警报可能永远不会完全消失，但它们不必成为个人的噩梦。 像 Skyflo.ai 这样的人工智能驱动的解决方案正在重新定义我们处理复杂云原生问题的方式。 通过自动化繁重的工作并提供智能建议，Skyflo.ai 使你能够专注于重要的事情，例如设计弹性系统而不是救火。
如果您对 AI 驱动的云原生工作流程感兴趣，我邀请您探索并支持 GitHub 上的 Skyflo.ai 项目：[https://github.com/skyflo-ai/skyflo](https://github.com/skyflo-ai/skyflo)。

无论您是经验丰富的[云架构师还是 DevOps 新手](https://thenewstack.io/ship-fast-break-nothing-launchdarklys-winning-formula/)（快速交付，零故障：LaunchDarkly 的制胜秘诀），您的贡献、反馈和功能请求都可以塑造 AI 辅助运营的未来。对于我们这些热爱[云原生技术](https://thenewstack.io/cloud-native/)（以及偶尔的痛苦）的人来说，这是一个激动人心的前沿领域。