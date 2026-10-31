Imagine: There’s a line on the credential report that no one on the platform team can explain. An IAM user called *research-agent-2* has an access key created 14 months ago that was last used 11 months ago. And it’s still active.

The project it supported closed long ago, and the person who approved it doesn’t even work at the company anymore.

While this example is hypothetical, the lifecycle problem isn’t.

This doesn’t require carelessness. An agent is created for a task, the task ends, and nobody revisits its access. A departing person triggers offboarding; a finished agent just leaves a closed tab. AWS IAM user access keys don’t expire automatically, so a forgotten key stays valid until somebody disables or deletes it.

> “A departing person triggers offboarding; a finished agent just leaves a closed tab.”

[OWASP puts improper offboarding first](https://owasp.org/www-project-non-human-identities-top-10/2025/1-improper-offboarding) in its 2025 Top 10 for [non-human identities](https://thenewstack.io/unified-access-ai-agents/), and the remedy reads like this series’ premise: retire what’s no longer needed, and give the rest an accountable owner. The hard part is knowing what exists.

The problem is that attackers move faster than an annual audit ever could. In September 2026, GreyNoise documented an AI-orchestrated campaign against PaperCut servers: the attacker went from an empty workspace to [remote code execution](https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf) at a real victim in under four hours, and once launched, the campaign compromised at least eleven organizations in 26 seconds. That wasn’t an attack using abandoned AWS IAM keys. It shows how quickly exposed access becomes useful once an attacker is in, and why slow inventory and revocation are dangerous.

[An agent’s access](https://thenewstack.io/ai-agent-credential-risks/) can outlive its purpose unless someone governs its lifecycle.

The last three articles covered [attaching an owner at discovery](https://thenewstack.io/attach-owner-cloud-resources/), [reassigning one before a last day](https://thenewstack.io/reassign-cloud-resource-ownership/), and [what happens when the owner is an agent](https://thenewstack.io/ai-agent-cloud-ownership/). Credentials add a related problem, with one distinction. An agent’s deployment identity is what authenticates it, or the deployment platform, to a cloud account.

> “A forgotten VM costs money; a forgotten credential can grant access.”

A provisioned credential is a persistent key, secret, or token that a deployment creates for some other workload; the two have [different owners](https://thenewstack.io/ai-agent-cloud-ownership/) and revocation procedures. A forgotten VM costs money; a forgotten credential can grant access. The remedy is still a query, a policy, and a clock, each used for the part of the problem it can solve.

## 1. The query that finds keys no one is using

[CloudQuery can sync AWS IAM credential reports](https://www.cloudquery.io/blog/aws-iam-user-access-analysis) into `aws_iam_credential_reports` when that table is enabled in the source configuration. The report lists up to two access-key slots per user. This query, written for the ClickHouse dialect CloudQuery Platform uses, takes the latest synced row for each report, turns the slots into rows, and returns active IAM user keys that are at least 90 days old and unused for at least 90 days.

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

The active flags, `access_key1_active` and `access_key2_active`, have no underscore before the digit; the date columns do. On Platform, [a table name already points at the latest complete snapshot](https://www.cloudquery.io/docs/platform/advanced-topics/understanding-platform-views), so the latest-row clause matters on destinations that keep history, where it can also resurface a user deleted since.

The 90-day window is a review threshold, not a verdict: quarterly jobs have quiet keys, and a null or placeholder last-used date means investigate, not “never needed.” The report doesn’t say which agent used an account; correlate with audit logs and a named owner. The query skips the root account, whose access keys need a separate, urgent audit; AWS recommends having none.

On PostgreSQL, quote `"user"` with double quotes, use `interval '90 days'`, and replace `LIMIT 1` BY with `DISTINCT ON`. Here the ARN, which is unique per IAM user, identifies each report:

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

The result is a prioritized review list. Next, the human question matters: who owns this credential, what still depends on it, and when should it stop working?

Other clouds raise the same concern elsewhere. In Entra ID, `entraid_serviceprincipals` includes credential metadata and `entraid_serviceprincipal_owners` shows who’s accountable; inspect identifiers and validity dates, not secret values, since [Microsoft Graph returns secretText only at creation](https://learn.microsoft.com/en-us/graph/api/resources/passwordcredential?view=graph-rest-1.0). In Google Cloud, `gcp_iam_service_account_keys` can inventory service-account keys if that table is enabled in your sync, but inventory alone doesn’t show use; check Google Cloud’s audit logs.

## 2. The policy that keeps agents from minting keys

The query cleans up what exists. An env zero [approval policy](https://docs.envzero.com/guides/policies-governance/approval-policies) can stop certain new keys at deploy time, but only where env zero governs the deployment: policies are enforced at deploy and destroy, not for credentials created in a console, by an external script, or by an env zero task, and they don’t revoke the identity authenticating a deployment. Cloud-native IAM controls, like an AWS service control policy or GCP’s organization policy for service account keys, and the inventory above still do that work.

Assign the policy to a project and every environment under it, subprojects included, inherits it. It doesn’t need to know whether a person or an agent clicked Deploy; it refuses selected long-lived credential types in Terraform and OpenTofu plans. Prefer federation where you can: env zero supports [OIDC-based deployment authentication](https://docs.envzero.com/guides/integrations/oidc-integrations), and an AWS role issues [temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) that expire with the session, though the role itself doesn’t.

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

The policy reads a standard Terraform or OpenTofu plan, or the module map from Terragrunt run-all. A plan with no changes can omit `resource_changes`, so an empty plan counts as valid, while an unrecognized shape is denied rather than silently allowed; attach it only to projects whose templates produce these formats, since Pulumi, CloudFormation, and Kubernetes deployments would all be denied. Replacements include a `create` action, so they’re caught. The resource list is an example, and the policy can’t see a hardcoded secret or a key generated outside Terraform.

The allow rule matters: with it, anything not denied proceeds without manual approval; without it, a policy that returns nothing defaults to pending, and every deployment waits for a person. Test with the full env zero input wrapper, not bare `terraform show -json` output, covering key creation, role-only plans, replacements, run-all, missing plan data, and destroys. `ENV0_PRINT_POLICY_INPUT=true` logs the exact input; `ENV0_OPA_VERSION` pins the OPA version. The policy runs on env zero’s default OPA (0.46.1) and on 1.x, which is why it uses `future.keywords` imports instead of `import rego.v1`.

If an integration genuinely needs a persistent key, don’t just create it in another project. Use a documented exception: a named owner, a specific workload, least privilege, a revocation deadline, secure storage, monitoring, and an approval record. IAM access keys can’t be tagged, so record ownership on the identity and in your credential inventory.

## 3. Make sure you give every key a finite lifespan

AWS doesn’t give IAM user access keys an expiration date, so the end date has to come from somewhere else. For Terraform-managed credentials, an environment TTL gives you a teardown point: put disposable credentials in the same environment as what they serve and set a TTL. But a TTL isn’t credential expiry.

It starts a destroy, and the key disappears only if Terraform manages it and the destroy succeeds. A failed destroy, a locked environment, a manually created key, or an identity managed elsewhere leaves access behind, so verify revocation instead of trusting the countdown. TTLs can be extended or set to infinite, and [TTL limits don’t bind admins](https://docs.envzero.com/guides/policies-governance/policy-ttl). On the Free plan, once an organization passes 250 runs in a month, TTLs are destroyed; wait for the count to reset at the start of the next month (UTC), so a key can outlive its TTL by up to a month.

Govern the trust relationship and permission scope of any OIDC federation, and rotate persistent tokens in the issuing system; destroying infrastructure doesn’t revoke the caller. Terraform-managed access keys also record their secret values in state, so protect the state backend.

For keys outside any environment lifecycle, retire them under control. The credential report doesn’t include key IDs, so look those up, check last-used metadata, confirm the owner and dependency, then deactivate the specific key:

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

Deactivation is reversible, but it isn’t harmless: a quarterly batch or disaster-recovery job can fail long after a typical release cycle. Watch for authentication errors through an observation period matched to the workload’s schedule, get owner sign-off, then delete under your change procedure, since it isn’t reversible.

env zero’s [Free plan](https://docs.envzero.com/changelogs/2026/07/free-plan) includes custom approval policies and environment TTL, with 250 runs a month and 30 active environments. [CloudQuery’s Platform](https://www.cloudquery.io/docs/cli/introduction/platform-vs-cli) has a free tier, and its CLI syncs to your own Postgres. Sync the credential report, run the query, and count the rows. It’s read-only, so the worst outcome is a list you didn’t want to see.

## A credential needs an end date

A resource without an owner costs money until someone notices, and an unowned credential can grant unintended access to whoever finds it.

> “An old key doesn’t need to be labeled orphaned for an attacker to use it; it only needs to be valid.”

Agents who finished last quarter’s projects won’t flag their own credentials, and the next agent to encounter one might not belong to your organization. An old key doesn’t need to be labeled orphaned for an attacker to use it; it only needs to be valid.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/0a9a86e3-cropped-03077771-zrachidi2-600x600.jpg)

Zeen is a designer and builder that's been blessed to live and learn on three continents. He likes problem-solving, being helpful, and making useful things. He got his BSc in Computer Science, but got bored babysitting servers, so he went...

Read more from Zeen Rachidi](https://thenewstack.io/author/zeen-rachidi/)