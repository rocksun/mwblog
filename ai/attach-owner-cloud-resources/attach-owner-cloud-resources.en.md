The engineer who knew why that cloud instance existed has left the company. The instance is still running, the bill keeps growing, and the team must now decide whether it’s safe to shut down. This is a bad time to discover that its ownership history was someone’s memory.

> “Good resource governance has three pillars: continuously synced inventory, policy that blocks resources without tagged owners, and an audit trail that survives every reorg.”

A cost review flags an EC2 instance nobody remembers provisioning. Someone scours Slack for the resource ID, finds nothing, burns half a day chasing dead ends, and eventually stumbles across an exhausted engineer who mumbles the mantra that ends most of these investigations: “I think that’s from the project Priya was running before she left.”

Nobody follows up, because nobody knows how to reach Priya anymore. The instance stays up, because tearing down a fence when you don’t know what it’s protecting you from is a good way to find out the hard way. It’s the platform team equivalent of emotional baggage; they all seem to accumulate some.

Processing this baggage doesn’t require knowing Priya’s replacement, writing better documentation, or hoping the next reorg is more rigorous.

> “Processing this baggage doesn’t require knowing Priya’s replacement, writing better documentation, or hoping the next reorg is more rigorous.”

Solving the problem requires three things that already exist: queries, policies, and logs; and maybe just a little bit of therapy.

## 1. The query that tells you what’s missing an owner

CloudQuery’s asset inventory syncs continuously across every provider a team runs on, into tables you can query directly: `aws_ec2_instances`, `gcp_compute_instances`, `azure_compute_virtual_machines`, and so on. Finding every resource without an assigned owner is as easy as:

```

SQL
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

Run it regularly, and you have a (hopefully short) boring list to refer to when the CFO asks who deployed an expensive instance; instead of being thrown into a frenzied goose chase at 4:59 p.m. on a Friday.

## 2. The policy that prevents it recurring

A query tells you what’s already missing an owner; but how do you prevent the next ownerless resource from being deployed? The answer is a policy, and env zero evaluates [Open Policy Agent](https://thenewstack.io/how-doordash-governs-its-infrastructure-with-open-policy-agent/) rules against every plan before it applies. A rule that requires an owner tag on every new resource looks something like this:

```

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

Add that to the project’s policy set, and a plan that creates a resource without an owner tag doesn’t just get a warning; it doesn’t get created.

## 3. The record that outlives its creator

A tag tells you who owns something today. It doesn’t tell you anything about who asked for it, why, or who signed off. By the time it matters, the person who could’ve answered from memory may no longer be reachable. An audit entry records that at the moment of creation, instead of reconstructing it afterward from the scraps of recollection scattered around the rest of the team. Here’s an example:

```

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

This entry answers the question this whole piece opened with, without [needing Priya or Slack](https://thenewstack.io/if-i-need-slack-to-use-it-its-not-a-platform-as-product/). env zero keeps this record attached to the resource for as long as the resource exists, specifically so it outlasts any individual’s tenure.

## Why this keeps happening

Employee attrition is an age-old challenge that’s only accelerating in the modern era. [US private-sector voluntary turnover runs 22 to 25% a year](https://atlan.com/know/data-for-ai/tribal-knowledge/), so a hundred-person org loses twenty-odd people every year, each one taking a small, specific piece of “why this exists” with them. [Replacing a mid-level employee costs six to nine months of salary, more than double that for senior specialists](https://atlan.com/know/data-for-ai/tribal-knowledge/).

> “Tags were supposed to survive this. In practice they rot the way everything else does.”

That figure doesn’t touch what the departure does to everyone else’s mental model of what’s actually running. Tags were supposed to survive this. In practice they rot the way everything else does: two teams merge and bring incompatible schemas, [provisioning that runs on tribal knowledge accumulates configuration drift for the same reason it accumulates ambiguous ownership](https://www.sigmainfo.net/blog/platform-engineering-idp-stop-losing-developer-velocity-to-tooling-chaos/), and a resource tagged under a policy that’s been replaced twice since its inception isn’t much better documented than one that isn’t tagged at all.

We wrote in April about [the hour it once took our own team to answer, “what are we actually running across both clouds](https://thenewstack.io/multi-cloud-blind-spots/)?” That solved a point-in-time problem. The query, the policy, and the audit entry above stop the same story from playing out again next June.

## The org chart will keep changing. The record doesn’t have to.

None of this stops people from leaving or teams from reorganizing; pretending otherwise is how platform teams end up rebuilding the same spreadsheet every eighteen months. What changes is whether the next “what are we actually running, and who owns it” conversation takes hours of archaeology across three teams, or is a query that already has the answer attached. Institutional knowledge decays at a fairly predictable rate. A [system of record](https://thenewstack.io/netbox-labs-network-intent/) shouldn’t.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/0a9a86e3-cropped-03077771-zrachidi2-600x600.jpg)

Zeen is a designer and builder that's been blessed to live and learn on three continents. He likes problem-solving, being helpful, and making useful things. He got his BSc in Computer Science, but got bored babysitting servers, so he went...

Read more from Zeen Rachidi](https://thenewstack.io/author/zeen-rachidi/)