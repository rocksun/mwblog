The environment has thirty-four resources, including a VPC, subnets, an RDS instance, and a load balancer that hasn’t seen any traffic in weeks. The owner tag reads deploy-agent. Nobody typed that in; it was auto-populated because the identity that ran that apply doesn’t have an individual name, badge, or last day.

That last part is the crux of the problem. A departed employee at least leaves some kind of trail: an exit interview, a Slack history, the manager who inherited their mess. Agents leave none of that. The task finishes, the context window closes, and whatever they built keeps consuming resources like forgotten candles steadily burning up your cloud bill.

> “The task finishes, the context window closes, and whatever they built keeps consuming resources like forgotten candles steadily burning up your cloud bill.”

This is the same discovery-and-transfer challenge our last [two](https://thenewstack.io/attach-owner-cloud-resources/) [articles](https://thenewstack.io/reassign-cloud-resource-ownership/) addressed, but it’s happening much faster and from unpredictable angles. A person’s ownership goes stale after a badge cycle or reorg. An agent’s goes stale the second the task is done, which in some instances could be minutes. Luckily, the fix doesn’t change: it’s still a query, [a policy, and a guardrail](https://thenewstack.io/galileo-agent-control-open-source/). The only difference is what each checks for, because you’re not looking for a person this time; you’re hunting service accounts.

## 1 – The query that finds the breadcrumbs

CloudQuery’s [asset inventory](https://www.cloudquery.io/docs/platform/features/asset-inventory) already tells you who owns a tagged resource. All you have to do is extend the question to ask whether the owner is a person. Cross-reference the tag against your identity directory, and anything that resolves to a role or service principal instead of a human account surfaces immediately, across every taggable resource type:

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

AWS and Azure both keep native records of [machine identities](https://thenewstack.io/securing-autonomous-ai-agents/), so the lookup there confirms directly: this owner is a role, not a person. GCP doesn’t expose the same signal at the IAM layer, the same gap the [second piece](https://thenewstack.io/reassign-cloud-resource-ownership/) in this series ran into, so the check works in reverse: if the owner isn’t in the company’s own directory of actual employees, it isn’t a person either. A hit here isn’t proof anything’s wrong; plenty of [automation legitimately runs infrastructure](https://thenewstack.io/flowai-gives-agents-a-greater-role-in-infrastructure-automation/) on its own behalf; but it’s a much shorter list to work through than scrolling through every resource in your cloud bill.

## 2 – The policy that keeps an agent from owning itself

The query finds what slipped through. The policy prevents it from happening again, and this is where the ownership problem doubles back on itself: like most orchestration platforms, [env zero treats whoever creates an environment as its owner](https://docs.envzero.com/guides/admin-guide/environments). That was a sensible default when only people created environments, but that era is over.

The fix is an [approval policy](https://docs.envzero.com/guides/policies-governance/approval-policies) that checks the owner tag itself, not whoever ran the plan. A deployment clears review only if every taggable resource names an owner, the owner looks like a person’s email address, and it isn’t on your list of agent identities:

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

The list of agent identities is a small JSON file that env zero passes to the policy as `policyData`. If the file goes missing, the policy fails closed:

```

{ "agent_identities": ["deploy-agent", "svc-agents@my-project.iam.gserviceaccount.com"] }

```

An apply now can’t clear review without naming a person, whether a person or a service account submitted it.

> “An apply now can’t clear review without naming a person, whether a person or a service account submitted it.”

The policy is only as strong as the key behind it. env zero [API keys default to the Admin role](https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/api-keys), and TTL limits don’t apply to admins, so give each agent a User-type key on its own team, with a role scoped to the one environment it works in. A [planner role](https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/default-roles) turns every apply into a person’s approval, and a personal key is the wrong tool because it carries its owner’s permissions. env zero’s [agent CLI](https://www.envzero.com/blog/announcing-the-env-zero-agentic-experience-point-your-coding-agent-at-your-infrastructure) authenticates the same way, as a scoped identity per agent, never a shared token.

## 3 – Nothing should live forever

The query and policy catch new runs, but neither helps with what agents have already built and abandoned, because there’s no last-day equivalent to trigger a review. For those, we have to assign a last day. env zero’s [environment TTL](https://docs.envzero.com/guides/policies-governance/policy-ttl) automatically destroys anything that outlives its assigned lifespan, warning the environment’s creator three times first: two days out, two hours out, and thirty minutes out. That works when the creator is a person who regularly checks their inbox. It does nothing when the creator is a deploy-agent, because they don’t have inboxes.

So don’t let the agent be the creator. A person creates the environment and sets its TTL, and the agent deploys into it. The warnings land with someone who can act on them, and TTL policy limits still cap what a non-admin agent can set.

> “Build first, claim later, and if it goes unclaimed, it won’t exist long enough to matter.”

Some platforms have already made this the new default: [Axiom lets an agent spin up a fully working account with one unauthenticated request,](https://axiom.co/docs/console/intelligence/agent-created-orgs) then deletes the whole thing automatically if nobody claims it within twenty-four hours. Build first, claim later, and if it goes unclaimed, it won’t exist long enough to matter.

## Why this keeps happening

In the [first](https://thenewstack.io/attach-owner-cloud-resources/) [two](https://thenewstack.io/reassign-cloud-resource-ownership/) chapters of this trilogy, the main driver was turnover: people leave or change roles every few years, and nobody updates the ownership tags. Agents don’t turn over at that pace; they multiply at a rate that makes it look practically glacial. [Gravitee’s 2026 survey of AI agent security](https://gravitee.io/state-of-ai-agent-security) found that average enterprise agent counts roughly doubled in just four months, between December 2025 and April 2026, with over a third of organizations already running over a hundred.

> “They multiply at a rate that makes it look practically glacial.”

How many people would need to be on the review team to keep up with that? [Larridin’s scans of enterprise environments](https://larridin.com/blog/ai-agent-governance-enterprise) found forty-seven agents, on average, running with no assigned owner at all. Not because someone decided they shouldn’t have one, but because no one assigned ownership when they were created. [A separate industry analysis citing the World Economic Forum](https://mstone.ai/blog/ai-agent-sprawl-ownership/) puts the number even higher: with over half of organizations reporting no clear ownership model for AI identities of any kind.

The audit trail doesn’t help much here, either. When every agent authenticates through the same shared service account, the logs can confirm a resource was created, but [they can’t say which run created it, from which prompt, or on whose behalf;](https://www.qovery.com/blog/scoped-policy-controlled-cloud-access-for-ai-agents#why-is-giving-an-ai-agent-broad-cloud-credentials-so-dangerous-in-2026) all information the owner tag was supposed to supply in the first place.

## A resource needs a named owner

Nothing in this series argues that people or agents should stop leaving things behind; that’s simply the present reality. We’re advocating that the things left behind have a name attached the moment they’re created, not six months later during a cost review or security audit. A person’s departure usually gets announced or noticed; an agent’s doesn’t; so the query, the policy, and the TTL clock have to run autonomously.

Whether something was created by a person or a prompt, it’ll keep leeching resources until someone catches it; and the longer it goes unnoticed, the higher the bill will be when it comes due.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/0a9a86e3-cropped-03077771-zrachidi2-600x600.jpg)

Zeen is a designer and builder that's been blessed to live and learn on three continents. He likes problem-solving, being helpful, and making useful things. He got his BSc in Computer Science, but got bored babysitting servers, so he went...

Read more from Zeen Rachidi](https://thenewstack.io/author/zeen-rachidi/)