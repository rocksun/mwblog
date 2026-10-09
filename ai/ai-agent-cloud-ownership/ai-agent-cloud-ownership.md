<!--
title: 你的AI智能体刚刚配置了云资源，谁来承担所有权？
cover: https://cdn.thenewstack.io/media/2026/10/9cace81a-a-c-iz6mqstjffc-unsplash.jpg
summary: 本文探讨了AI智能体频繁创建云资源却导致所有权缺失的问题。通过查询、审批策略和生命周期管理（TTL），企业可以有效追踪、防止智能体自我授权，并清理无人认领的云资产，以应对日益严重的AI资源泛滥挑战。
-->

本文探讨了AI智能体频繁创建云资源却导致所有权缺失的问题。通过查询、审批策略和生命周期管理（TTL），企业可以有效追踪、防止智能体自我授权，并清理无人认领的云资产，以应对日益严重的AI资源泛滥挑战。

> 译自：[Your AI agent just provisioned a resource. Who owns it?](https://thenewstack.io/ai-agent-cloud-ownership/)
> 
> 作者：Zeen Rachidi

环境中共有三十四个资源，包括一个 VPC、子网、一个 RDS 实例，以及一个数周没有任何流量的负载均衡器。所有者标签显示为 `deploy-agent`。没有人手动输入过这个标签；它是自动填充的，因为运行该应用操作的身份没有个人姓名、工牌或离职日期。

最后一点正是核心问题所在。离职员工至少会留下某种痕迹：离职面谈、Slack 聊天记录，或者接手他们烂摊子的经理。智能体却什么也没留下。任务完成，上下文窗口关闭，它们构建的任何东西都会像被遗忘的蜡烛一样继续消耗资源，稳步推高你的云账单。

> “任务完成，上下文窗口关闭，它们构建的任何东西都会像被遗忘的蜡烛一样继续消耗资源，稳步推高你的云账单。”

这与我们前[两篇](https://thenewstack.io/attach-owner-cloud-resources/)[文章](https://thenewstack.io/reassign-cloud-resource-ownership/)所讨论的发现与转移挑战是同一个问题，但它的发生速度要快得多，而且角度更加不可预测。个人的所有权会在工牌周期或组织架构重组后变得陈旧。而智能体的所有权在任务完成的那一秒就会失效，在某些情况下这可能只需要几分钟。幸运的是，解决方案没有改变：它依然是一条查询语句、[一项策略和一个护栏](https://thenewstack.io/galileo-agent-control-open-source/)。唯一的区别在于它们各自检查的内容，因为这次你寻找的不是一个人，而是在搜寻服务账户。

## 1 – 寻找线索的查询

CloudQuery 的[资产清单](https://www.cloudquery.io/docs/platform/features/asset-inventory)已经可以告诉你谁拥有一个带有标签的资源。你所需要做的就是扩展问题，询问所有者是否为人类。将标签与你的身份目录进行交叉比对，任何解析为角色或服务主体（而不是人类账户）的内容都会在每个可加标签的资源类型中立即显现出来：

```

SELECT cloud, account, resource_type, name, tags['owner'] AS owner
FROM (
  SELECT *
  FROM cloud_assets
  ORDER BY _cq_sync_group_id DESC
  LIMIT 1 BY _cq_platform_id
)
WHERE tags['owner'] != ''
  AND (
       (cloud = 'aws'   AND tags['owner'] IN (SELECT role_name FROM aws_iam_roles))
    OR (cloud = 'azure' AND tags['owner'] IN (SELECT display_name FROM entraid_serviceprincipals))
    OR (cloud = 'gcp'   AND tags['owner'] NOT IN (SELECT primary_email FROM googleworkspace_users))
  )
ORDER BY cloud, resource_type, name

```

AWS 和 Azure 都保留了[机器身份](https://thenewstack.io/securing-autonomous-ai-agents/)的原生记录，因此那里的查询可以直接确认：这个所有者是一个角色，而不是一个人。GCP 在 IAM 层没有暴露出相同的信号——这也是本系列的[第二篇文章](https://thenewstack.io/reassign-cloud-resource-ownership/)所遇到的相同缺口——所以检查工作是反过来进行的：如果所有者不在公司实际员工的自有目录中，它也不是一个人。这里出现命中并不证明有什么不对劲；许多[自动化程序本就会合法地代表自身运行基础设施](https://thenewstack.io/flowai-gives-agents-a-greater-role-in-infrastructure-automation/)；但这比滚动查看云账单中的每一个资源要容易筛选得多。

## 2 – 防止智能体拥有自身的策略

查询能找出漏网之鱼，而策略则能防止这种情况再次发生。正是在这里，所有权问题陷入了循环：和大多数编排平台一样，[env zero 将创建环境的任何人视为其所有者](https://docs.envzero.com/guides/admin-guide/environments)。在只有人类创建环境的时代，这是一个合理的默认设置，但那个时代已经结束了。

解决方案是一个[审批策略](https://docs.envzero.com/guides/policies-governance/approval-policies)，它检查所有者标签本身，而不是运行计划的人。只有当每个可加标签的资源都指定了一个所有者、该所有者看起来像是一个人的电子邮件地址、并且它不在你的智能体身份列表中时，部署才能通过审查：

```

package env0

is_deploy {
	startswith(input.deploymentRequest.type, "deploy")
}

# Owner values planned on AWS/Azure tags or GCP labels
owners[[rc.address, owner]] {
	rc := input.plan.resource_changes[_]
	owner := rc.change.after.tags.owner
}

owners[[rc.address, owner]] {
	rc := input.plan.resource_changes[_]
	owner := rc.change.after.labels.owner
}

has_owner(addr) {
	owners[[addr, _]]
}

# Resources that can carry an owner at all
taggable(after) { after.tags == null }
taggable(after) { is_object(after.tags) }
taggable(after) { after.labels == null }
taggable(after) { is_object(after.labels) }

deny[msg] {
	is_deploy
	not input.policyData.agent_identities
	msg := "policyData.agent_identities is missing, so ownership cannot be checked"
}

deny[msg] {
	is_deploy
	rc := input.plan.resource_changes[_]
	taggable(rc.change.after)
	not has_owner(rc.address)
	msg := sprintf("%s has no owner tag", [rc.address])
}

deny[msg] {
	is_deploy
	owners[[addr, owner]]
	not regex.match(`^[^@\s]+@[^@\s]+\.[^@\s]+$`, owner)
	msg := sprintf("%s: owner %s is not a person's email address", [addr, owner])
}

deny[msg] {
	is_deploy
	owners[[addr, owner]]
	lower(owner) == lower(input.policyData.agent_identities[_])
	msg := sprintf("%s: owner %s is an agent identity", [addr, owner])
}

allow {
	count(deny) == 0
}

```

智能体身份列表是一个小的 JSON 文件，env zero 将其作为 `policyData` 传递给策略。如果该文件丢失，策略将采取保守拒绝（fail closed）的策略：

```

{ "agent_identities": ["deploy-agent", "svc-agents@my-project.iam.gserviceaccount.com"] }

```

现在，如果不指定一个真人，apply 操作将无法通过审查，无论是由人类还是服务账户提交的。

> “现在，如果不指定一个真人，apply 操作将无法通过审查，无论是由人类还是服务账户提交的。”

策略的好坏取决于其背后的密钥。env zero [API 密钥默认具有管理员角色](https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/api-keys)，且 TTL 限制不适用于管理员，因此请为每个智能体在其自己的团队中分配一个用户类型的密钥，并将角色范围限定在其工作的一个环境中。[规划者角色](https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/default-roles)将每一次 apply 都转化为需要人类批准的操作，而个人密钥则是错误的工具，因为它带有其所有者的权限。env zero 的[智能体 CLI](https://www.envzero.com/blog/announcing-the-env-zero-agentic-experience-point-your-coding-agent-at-your-infrastructure)采用相同的方式进行身份验证，即每个智能体一个独立作用域的身份，绝不使用共享 Token。

## 3 – 没有什么应该长存

查询和策略可以捕获新的运行，但对于智能体已经构建和遗弃的内容却无能为力，因为这里没有类似于离职日期的机制来触发审查。对于这些资源，我们必须为它们指定一个最后期限。env zero 的[环境 TTL](https://docs.envzero.com/guides/policies-governance/policy-ttl) 会自动销毁任何超过其指定寿命的资源，并在销毁前向环境创建者发出三次警告：提前两天、提前两小时、提前三十分钟。当创建者是经常检查收件箱的人类时，这很管用。但当创建者是部署智能体（deploy-agent）时，这就毫无用处了，因为它们没有收件箱。

因此，不要让智能体成为创建者。由人类创建环境并设置 TTL，然后由智能体向其中部署。警告会发给能够采取行动的人，而 TTL 策略限制仍然可以对非管理员智能体设置的期限进行上限约束。

> “先构建，后认领；如果无人认领，它的存在时间就不会长到构成问题。”

一些平台已经将此设为新的默认标准：[Axiom 允许智能体通过一个未经身份验证的请求启动一个完全工作的账户，](https://axiom.co/docs/console/intelligence/agent-created-orgs)如果如果在二十四小时内无人认领，就会自动删除整个账户。先构建，后认领；如果无人认领，它的存在时间就不会长到构成问题。

## 为什么这种情况一直在发生

在这三部曲的[第一](https://thenewstack.io/attach-owner-cloud-resources/)[二](https://thenewstack.io/reassign-cloud-resource-ownership/)章中，主要的驱动因素是人员流动：人们每隔几年就会离职或更换角色，而没有人去更新所有权标签。智能体的更迭速度可没有这么慢；它们的复制速度快得让人觉得简直像是冰河时代。Gravitee 的[2026年 AI 智能体安全性调查](https://gravitee.io/state-of-ai-agent-security)发现，在 2025 年 12 月到 2026 年 4 月短短的四个月内，企业平均智能体数量大约翻了一番，超过三分之一的组织已经运行了一百多个智能体。

> “它们的复制速度快得让人觉得简直像是冰河时代。”

需要多少人组成的审查团队才能跟上这个速度？Larridin 对[企业环境的扫描](https://larridin.com/blog/ai-agent-governance-enterprise)发现，平均有四十七个智能体在运行，但完全没有分配所有者。这不是因为有人决定它们不该拥有所有者，而是因为在创建它们时根本没有人分配所有权。[另一项引用世界经济论坛的行业分析](https://mstone.ai/blog/ai-agent-sprawl-ownership/)给出了更高的数字：超过一半的组织报告称，对于任何类型的 AI 身份都没有清晰的所有权模型。

审计追踪在这里也没有太大帮助。当每个智能体都通过同一个共享服务账户进行身份验证时，日志可以确认某个资源已被创建，但[它们无法说明是哪一次运行创建的、来自哪个提示词、或者代表谁创建的；](https://www.qovery.com/blog/scoped-policy-controlled-cloud-access-for-ai-agents#why-is-giving-an-ai-agent-broad-cloud-credentials-so-dangerous-in-2026)而所有这些信息本应是所有权标签最初需要提供的。

## 资源需要一个具名的所有者

本系列文章并不是在争论人类或智能体应该停止遗留资源；这只是当前的现实。我们主张的是，遗留的资源在创建的那一刻就附带一个名称，而不是在六个月后的成本审查或安全审计期间才去添加。人员的离职通常会被宣布或注意到，而智能体的则不会；因此，查询、策略和 TTL 计时器必须自主运行。

无论某项资源是由人类还是提示词创建的，在有人发现它之前，它都会不断吸取资源；而且它被忽视的时间越长，账单到期时的金额就会越高。