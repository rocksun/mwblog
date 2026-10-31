想象一下：在凭证报告上有一行平台团队无法解释的数据。一个名为 *research-agent-2* 的IAM用户有一个在14个月前创建、11个月前最后使用的访问密钥。而且它仍然处于激活状态。

它所支持的项目早已关闭，批准它的那个人甚至已经不在公司工作了。

虽然这个例子是假设的，但生命周期问题却不是。

这并不需要粗心大意。为了某项任务创建了一个智能体，任务结束后，没有人重新审视其访问权限。离职人员会触发离职交接流程；而完成任务的智能体只留下了一个关闭的标签页。AWS IAM用户访问密钥不会自动过期，因此被遗忘的密钥会一直有效，直到有人禁用或删除它。

> “离职人员会触发离职交接流程；而完成任务的智能体只留下了一个关闭的标签页。”

[OWASP 将不当离职交接列为第一位](https://owasp.org/www-project-non-human-identities-top-10/2025/1-improper-offboarding)，这是其针对[非人类身份](https://thenewstack.io/unified-access-ai-agents/)的2025年十大安全风险之一，其补救措施听起来就像本系列的前提：退役不再需要的资产，并为其余资产指定一个负责任的负责人。困难的部分在于了解究竟存在哪些资产。

问题在于，攻击者的行动速度远快于年度审计的速度。2026年9月，GreyNoise记录了一起针对 PaperCut 服务器的AI编排攻击活动：攻击者在一个真实的受害者机器上，在不到四个小时内就从一个空的工作空间进展到[远程代码执行](https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf)，一旦发起，该攻击活动在26秒内就入侵了至少11个组织。那次攻击并非使用被遗弃的AWS IAM密钥。它展示了暴露出访问权限一旦被攻击者入侵会有多大用处，以及为什么缓慢的清点和吊销流程如此危险。

[智能体的访问权限](https://thenewstack.io/ai-agent-credential-risks/)可能会在其使命结束后依然存在，除非有人对其生命周期进行治理。

前三篇文章涵盖了[在发现时附加负责人](https://thenewstack.io/attach-owner-cloud-resources/)、[在最后一天到来之前重新指派负责人](https://thenewstack.io/reassign-cloud-resource-ownership/)，以及[当负责人是智能体时会发生什么](https://thenewstack.io/ai-agent-cloud-ownership/)。凭证增加了一个相关的问题，但有一个区别。智能体的部署身份是向云账户验证其自身或部署平台的凭证。

> “被遗忘的虚拟机消耗金钱；而被遗忘的凭证则可能授予访问权限。”

预配的凭证是部署为其他工作负载创建的持久密钥、秘密或 Token；这两者具有[不同的所有者](https://thenewstack.io/ai-agent-cloud-ownership/)和吊销程序。被遗忘的虚拟机消耗金钱；而被遗忘的凭证则可能授予访问权限。补救措施仍然是一次查询、一项策略和一个时钟，每个工具都用于解决它所能解决的那部分问题。

## 1. 查找无人使用的密钥的查询

[CloudQuery 可以将 AWS IAM 凭证报告同步](https://www.cloudquery.io/blog/aws-iam-user-access-analysis)到 `aws_iam_credential_reports`（当在源配置中启用该表时）。该报告为每个用户列出最多两个访问密钥槽位。此查询针对 CloudQuery 平台使用的 ClickHouse 方言编写，获取每个报告的最新同步行，将槽位转换为行，并返回已激活且创建时间至少90天前且至少90天未使用的IAM用户密钥。

```

SQL
WITH latest_reports AS (
    SELECT
        _cq_platform_id,
        arn,
        `user` AS principal,
        access_key1_active,
        access_key_1_last_rotated,
        access_key_1_last_used_date,
        access_key2_active,
        access_key_2_last_rotated,
        access_key_2_last_used_date
    FROM aws_iam_credential_reports
    ORDER BY _cq_sync_group_id DESC, _cq_sync_time DESC
    LIMIT 1 BY _cq_platform_id
),
keys AS (
    SELECT _cq_platform_id, arn, principal,
           1 AS key_slot,
           access_key1_active AS active,
           access_key_1_last_rotated AS created,
           access_key_1_last_used_date AS last_used
    FROM latest_reports
    UNION ALL
    SELECT _cq_platform_id, arn, principal,
           2 AS key_slot,
           access_key2_active AS active,
           access_key_2_last_rotated AS created,
           access_key_2_last_used_date AS last_used
    FROM latest_reports
)
SELECT _cq_platform_id, arn, principal,
       key_slot, created, last_used
FROM keys
WHERE principal != '<root_account>'
  AND active = true
  AND created < now() - INTERVAL 90 DAY
  AND (
      last_used IS NULL
      OR last_used < now() - INTERVAL 90 DAY
  )
ORDER BY last_used NULLS FIRST, principal, key_slot;

```

激活标志 `access_key1_active` 和 `access_key2_active` 的数字前没有下划线；而日期列有。在平台上，[表名已经指向最新的完整快照](https://www.cloudquery.io/docs/platform/advanced-topics/understanding-platform-views)，因此最新行子句在保留历史记录的目标上很重要，在那里它还可以重新浮现自那以后被删除的用户。

90天的时间窗口是一个审查阈值，而不是最终定论：季度任务可能会有平静期密钥，而为 null 或占位符的最后使用日期意味着需要调查，而不是“永不需要”。该报告并未说明哪个智能体使用了某个账户；应与审计日志和具名负责人进行关联核对。该查询跳过了根账户，其访问密钥需要进行单独的、紧急的审计；AWS建议不要拥有任何根账户密钥。

在 PostgreSQL 上，用双引号引住 `"user"`，使用 `interval '90 days'`，并将 `LIMIT 1` BY 替换为 `DISTINCT ON`。这里每个 IAM 用户唯一的 ARN 用于标识每个报告：

```

SQL
WITH latest_reports AS (
    SELECT DISTINCT ON (arn)
           arn, "user" AS principal,
           access_key1_active, access_key_1_last_rotated, access_key_1_last_used_date,
           access_key2_active, access_key_2_last_rotated, access_key_2_last_used_date
    FROM aws_iam_credential_reports
    ORDER BY arn, _cq_sync_time DESC
),
keys AS (
    SELECT arn, principal, 1 AS key_slot,
           access_key1_active AS active,
           access_key_1_last_rotated AS created,
           access_key_1_last_used_date AS last_used
    FROM latest_reports
    UNION ALL
    SELECT arn, principal, 2 AS key_slot,
           access_key2_active AS active,
           access_key_2_last_rotated AS created,
           access_key_2_last_used_date AS last_used
    FROM latest_reports
)
SELECT split_part(arn, ':', 5) AS account_id, arn, principal,
       key_slot, created, last_used
FROM keys
WHERE principal <> '<root_account>'
  AND active
  AND created < now() - interval '90 days'
  AND (last_used IS NULL OR last_used < now() - interval '90 days')
ORDER BY last_used NULLS FIRST, principal, key_slot;

```

其结果是一个优化的审查列表。接下来，人类层面的问题至关重要：谁拥有这个凭证，什么仍在依赖它，它应该何时停止工作？

其他云服务在别处也会引起同样的担忧。在 Entra ID 中，`entraid_serviceprincipals` 包含凭证元数据，而 `entraid_serviceprincipal_owners` 显示谁对此负责；应检查标识符和有效性日期，而不是密码值，因为 [Microsoft Graph 仅在创建时返回 secretText](https://learn.microsoft.com/en-us/graph/api/resources/passwordcredential?view=graph-rest-1.0)。在 Google Cloud 中，如果在同步中启用了该表，`gcp_iam_service_account_keys` 可以清点服务账号密钥，但仅凭清点无法显示使用情况；请检查 Google Cloud 的审计日志。

## 2. 防止智能体铸造密钥的策略

该查询清除了现有内容。env zero 的[审批策略](https://docs.envzero.com/guides/policies-governance/approval-policies)可以在部署时阻止某些新密钥，但前提是 env zero 必须对该部署进行治理：策略是在部署和销毁时强制执行的，而不是针对在控制台中、由外部脚本或由 env zero 任务创建的凭证，并且它们不会吊销用于身份验证部署的身份。诸如 AWS 服务控制策略或 GCP 用于服务账号密钥的组织策略等云原生 IAM 控制措施，以及上述清点工作，仍然可以发挥这些作用。

将策略分配给一个项目及其下的每个环境（包括子项目），它们都会继承该策略。它不需要知道是人还是智能体点击了“部署”；它会拒绝 Terraform 和 OpenTofu 计划中选定的长期凭证类型。在可能的情况下首选联合身份验证：env zero 支持[基于 OIDC 的部署身份验证](https://docs.envzero.com/guides/integrations/oidc-integrations)，并且 AWS 角色会颁发随会话过期的[临时凭证](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)（尽管角色本身不会过期）。

```

package env0

import future.keywords.contains 
import future.keywords.every 
import future.keywords.if 
import future.keywords.in

key_resources := {
	"aws_iam_access_key",
	"aws_iam_user_login_profile",
	"aws_iam_service_specific_credential",
	"aws_iam_signing_certificate",
	"google_service_account_key",
	"azuread_service_principal_password",
	"azuread_application_password",
	"azuread_service_principal_certificate",
	"azuread_application_certificate",
}

# A real Terraform or OpenTofu plan carries format_version, and omits
# resource_changes entirely when there is nothing to change.
tf_plan(p) if {
	is_object(p)
	p.format_version
}

standard_plan if {
	not input.plan.is_run_all
	tf_plan(input.plan)
}

run_all_plan if {
	input.plan.is_run_all == true
	is_object(input.plan.modules)
	count(input.plan.modules) > 0
	every _, m in input.plan.modules {
		tf_plan(m)
	}
}

resource_changes := object.get(input.plan, "resource_changes", []) if standard_plan

resource_changes := [rc |
	some _, m in input.plan.modules
	some rc in object.get(m, "resource_changes", [])
] if run_all_plan

deny contains msg if {
	not standard_plan
	not run_all_plan
	msg := "Unsupported plan format for the credential policy"
}

deny contains msg if {
	some rc in resource_changes
	key_resources[rc.type]
	"create" in rc.change.actions
	msg := sprintf("%s: long-lived credential prohibited", [rc.address])
}

allow if count(deny) == 0

```

该策略读取标准的 Terraform 或 OpenTofu 计划，或来自 Terragrunt run-all 的模块映射。没有更改的计划可以省略 `resource_changes`，因此空计划被视为有效，而无法识别的形状将被拒绝而不是静默允许；应将其仅附加到其模板生成这些格式的项目中，因为 Pulumi、CloudFormation 和 Kubernetes 部署都会被拒绝。替换操作包含 `create` 动作，因此它们会被捕获。资源列表是一个示例，且该策略无法看到硬编码的秘密或在 Terraform 之外生成的密钥。

允许（allow）规则至关重要：有了它，任何未被拒绝的内容都无需人工审批即可继续；没有它，返回空内容的策略将默认为挂起状态，并且每个部署都在等待人工处理。应使用完整的 env zero 输入包装器进行测试，而不是裸露的 `terraform show -json` 输出，涵盖密钥创建、仅角色的计划、替换、run-all、缺失的计划数据以及销毁。`ENV0_PRINT_POLICY_INPUT=true` 会记录准确的输入；`ENV0_OPA_VERSION` 会锁定 OPA 版本。该策略在 env zero 的默认 OPA（0.46.1）以及 1.x 版本上运行，这就是它使用 `future.keywords` 导入而不是 `import rego.v1` 的原因。

如果集成确实需要持久密钥，切勿只在另一个项目中创建它。请使用有记录的例外情况：具名负责人、特定工作负载、最小权限、吊销期限、安全存储、监控以及审批记录。IAM 访问密钥无法加标签，因此请在身份信息中和凭证清点中记录所有权。

## 3. 确保为每个密钥赋予有限的寿命

AWS 不会为 IAM 用户访问密钥赋予过期日期，因此结束日期必须来自其他地方。对于 Terraform 管理的凭证，环境 TTL（生存时间）为您提供了一个拆除点：将一次性凭证放在与其服务对象相同的环境中，并设置一个 TTL。但 TTL 并非凭证过期。

它会触发销毁，并且只有在 Terraform 管理它且销毁成功的情况下，密钥才会消失。销毁失败、锁定的环境、手动创建的密钥或在其他地方管理的身份都会留下访问权限，因此请验证吊销情况，而不要信赖倒计时。TTL 可以延长或设置为无限期，并且[TTL 限制无法约束管理员](https://docs.envzero.com/guides/policies-governance/policy-ttl)。在免费计划中，一旦一个组织在一个月内超过 250 次运行，TTL 就会被销毁；请等待计数在下个月初（UTC）重置，因此密钥存活的时间可能会超出其 TTL 最多一个月。

治理任何 OIDC 联合身份验证的信任关系和权限范围，并在颁发系统中轮换持久 Token；销毁基础设施并不会吊销调用方。Terraform 管理的访问密钥还会在状态中记录其秘密值，因此请保护好状态后端。

对于任何环境生命周期之外的密钥，请在受控情况下将其退役。凭证报告不包含密钥 ID，因此请查找它们，检查最后使用情况的元数据，确认所有者和依赖项，然后停用特定密钥：

```

Shell
aws iam list-access-keys \
  --user-name research-agent-2

aws iam get-access-key-last-used \
  --access-key-id &lt;key-id>

aws iam update-access-key \
  --user-name research-agent-2 \
  --access-key-id &lt;key-id> \
  --status Inactive

```

停用是可逆的，但并非毫无风险：季度批量作业或灾难恢复作业可能会在典型发布周期很久之后失败。请在与工作负载时间表相匹配的观察期内注意身份验证错误，获得负责人的签字批准，然后根据您的变更程序进行删除，因为删除是不可逆的。

env zero 的[免费计划](https://docs.envzero.com/changelogs/2026/07/free-plan)包括自定义审批策略和环境 TTL，每月提供 250 次运行和 30 个活动环境。[CloudQuery 的平台](https://www.cloudquery.io/docs/cli/introduction/platform-vs-cli)拥有免费层，其 CLI 可以同步到您自己的 Postgres。同步凭证报告、运行查询并清点行数。它是只读的，因此最坏的结果也只是得到一份你本不想看到的列表。

## 凭证需要一个结束日期

没有负责人的资源会不断消耗金钱，直到有人注意到它，而一个无主的凭证则可能向任何发现它的人授予意外的访问权限。

> “旧密钥不需要被标记为孤立的，攻击者就能使用它；它只需要保持有效即可。”

完成上季度项目的智能体不会自行标记它们的凭证，而下一个遇到该凭证的智能体可能并不属于您的组织。旧密钥不需要被标记为孤立的，攻击者就能使用它；它只需要保持有效即可。