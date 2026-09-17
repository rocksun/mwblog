那位知道这台云实例为何存在的工程师已经离职了。实例仍在运行，账单不断增长，团队现在必须决定是否可以安全地将其关闭。如果此时才发现该实例的所有权历史仅仅停留在某人的记忆中，那情况就糟糕了。

> “良好的资源治理有三大支柱：持续同步的资产清单、拦截未标记所有者资源的策略，以及能够应对任何组织架构调整的审计追踪记录。”

一次成本审查标记了一个没人记得是谁部署的 EC2 实例。有人在 Slack 上搜寻资源 ID，却一无所获，浪费半天时间追踪死胡同，最终偶然遇到了一位精疲力竭的工程师，他嘟囔着那句结束大多数此类调查的咒语：“我想那是 Priya 在离开前负责的那个项目。”

没人跟进，因为没人知道如何联系 Priya 了。实例保持运行，因为当你不知道围栏保护的是什么时，拆除它往往会让你付出惨痛的代价。对于平台团队来说，这等同于“情感包袱”；他们似乎总会积累一些。

处理这些包袱并不需要找到 Priya 的接替者、撰写更好的文档，或者寄希望于下一次组织架构调整能更严谨。

> “处理这些包袱并不需要找到 Priya 的接替者、撰写更好的文档，或者寄希望于下一次组织架构调整能更严谨。”

解决这个问题需要三样已经存在的东西：查询、策略和日志；或许还需要一点点心理疏导。

## 1. 告诉你缺少所有者的查询

CloudQuery 的资产清单可以持续同步团队使用的每个云提供商的数据，并汇入你可以直接查询的表中：`aws_ec2_instances`、`gcp_compute_instances`、`azure_compute_virtual_machines` 等。查找所有未分配所有者的资源就像这样简单：

```sql
SELECT resource_id, 'aws' AS provider, 'ec2_instance' AS resource_type
FROM aws_ec2_instances
WHERE tags ->> 'owner' IS NULL
UNION ALL
SELECT resource_id, 'gcp', 'compute_instance'
FROM gcp_compute_instances
WHERE labels ->> 'owner' IS NULL
UNION ALL
SELECT resource_id, 'azure', 'virtual_machine'
FROM azure_compute_virtual_machines
WHERE tags ->> 'owner' IS NULL
ORDER BY provider;
```

定期运行此查询，当首席财务官（CFO）询问是谁部署了昂贵的实例时，你就会有一份（希望很短的）无聊的清单可以参考；而不是在周五下午 4:59 被抛入一场疯狂的搜寻任务中。

## 2. 防止此类问题再次发生的策略

查询可以告诉你哪些资源已经缺少所有者；但你如何防止下一个无主资源被部署呢？答案是策略，env zero 会在应用前评估每一个计划的 [Open Policy Agent](https://thenewstack.io/how-doordash-governs-its-infrastructure-with-open-policy-agent/) 规则。一个要求每个新资源都必须有所有者标签的规则看起来像这样：

```rego
package env0

# METADATA
# title: require owner tag
# description: A resource can't be created without a declared owner.
deny[format(rego.metadata.rule())] {
	resource := input.resource_changes[_]
	resource.change.actions[_] == "create"
	not resource.change.after.tags.owner
}

format(meta) := meta.description
```

将其添加到项目的策略集中，那么任何创建没有所有者标签的资源的计划不仅会收到警告，它将根本无法被创建。

## 3. 比创建者活得更久的记录

标签可以告诉你今天谁拥有某项资源。它不能告诉你是谁申请的、为什么申请，或者谁批准的。当问题真正重要时，那个能凭记忆回答问题的人可能已经无法联系上了。审计条目记录了创建时刻的信息，而不是事后从团队残存的零碎记忆中拼凑。这是一个例子：

```json
{
  "event": "resource.created",
  "resource_id": "i-0a1b2c3d4e5f",
  "requested_by": "j.chen@company.com",
  "approved_by": "platform-lead@company.com",
  "approval_ref": "ENV-4471",
  "stated_purpose": "load test environment, Q3 capacity planning",
  "timestamp": "2026-08-14T09:12:03Z"
}
```

该条目回答了本文开头提出的问题，且无需 [借助 Priya 或 Slack](https://thenewstack.io/if-i-need-slack-to-use-it-its-not-a-platform-as-product/)。env zero 将此记录附加到资源上，只要资源存在，记录就会一直保留，专门确保它比任何个人的任期都长久。

## 为什么这种情况不断发生

员工流失是一个古老的挑战，在现代社会正在加速。[美国私营部门的自愿离职率每年在 22% 到 25% 之间](https://atlan.com/know/data-for-ai/tribal-knowledge/)，因此一个百人规模的组织每年会流失二十多人，每个人带走一小部分关于“为什么这东西存在”的特定知识。[替换一名中级员工的成本是其六到九个月的工资，高级专家的成本更是翻倍](https://atlan.com/know/data-for-ai/tribal-knowledge/)。

> “标签本应解决这个问题。但在实践中，它们像其他一切东西一样腐烂了。”

这个数字还没有触及人员离职对其他人关于“到底运行着什么”的认知模型造成的破坏。标签本应解决这个问题。但在实践中，它们像其他一切东西一样腐烂了：两个团队合并并带来了不兼容的模式；[基于部落知识的资源配置因为同样的原因积累了配置漂移，也积累了所有权模糊的问题](https://www.sigmainfo.net/blog/platform-engineering-idp-stop-losing-developer-velocity-to-tooling-chaos/)；在一个自诞生以来已被更换过两次的策略下标记的资源，其文档记录水平并不比未标记的资源好多少。

我们在四月份写过 [我们自己的团队曾经花费一小时才回答“我们在两个云上到底运行着什么”的问题](https://thenewstack.io/multi-cloud-blind-spots/)。那解决了当时的问题。上面的查询、策略和审计条目可以防止同样的故事在明年六月再次上演。

## 组织架构会不断变化。记录不必如此。

这一切都无法阻止人员流动或团队重组；假装可以做到这一点只会导致平台团队每隔十八个月就得重新建立一次同样的电子表格。真正改变的是：下一次关于“我们到底运行着什么，谁拥有它”的对话，是需要跨越三个团队进行数小时的考古，还是通过一个已经附加了答案的查询即可解决。制度性知识的衰减速度是相当可预测的。而 [记录系统](https://thenewstack.io/netbox-labs-network-intent/) 不应该这样。