Someone posted a question in Slack that seemed straightforward: *What are we actually running across both cloud environments?*

Not what our Infrastructure as Code documentation says. Not what the billing reports show. What’s *actually running*, right now, across every account, every provider, both orgs.

It took an hour of thread replies, three different teams, and at least one “I think we have some Azure stuff from that pilot, let me find the person who knows about it” before we had something close to an answer. The final response was not “here’s the inventory.” It was: “Here’s what we’re pretty confident about, with some gaps we’d need to investigate.”

> “We’re an organization of serious engineers who take infrastructure seriously. Yet, a cohesive map of our stack didn’t exist.”

We’re an organization of serious engineers who take infrastructure seriously. Yet, a cohesive map of our stack didn’t exist. It wasn’t for lack of talent; it was a lack of necessity. That changed the moment that Slack message landed.

## Nobody planned this

I’ve heard “multi-cloud strategy” a lot in conference talks over the past few years. The framing usually involves deliberate architectural choices about workload placement, vendor lock-in avoidance, and high-availability topology across regions and providers.

According to [Flexera’s 2024 State of the Cloud Report](https://www.flexera.com/blog/finops/cloud-computing-trends-flexera-2024-state-of-the-cloud-report/), 89% of enterprises are running workloads across multiple public clouds, up from 87% the year before. That number gets cited constantly in vendor decks as evidence of multi-cloud adoption. What it doesn’t capture is how most of those organizations got there.

What usually happens is accumulation:

* Your core product runs on AWS because that’s what you chose when you started, or when the person who made that choice was working there, or because it was 2014 and the alternatives weren’t mature.
* A [SaaS vendor](https://thenewstack.io/how-to-assess-integration-security-risks-when-evaluating-saas-vendors/) you integrated with runs on GCP, and one of their features requires a GCP-native service, so you stood up a project there.
* Someone built a Cloudflare Worker for the API gateway edge cases because the latency was lower, and it mattered.
* The company you merged with used Azure for its identity layer and some legacy data pipelines, and no one was migrating those this quarter.

Add up enough of those decisions over enough time and across enough teams, and you find yourself running infrastructure across four providers. No strategy session produced this. No architecture review signed off on it. Each individual decision made sense in context; together, they created a cloud footprint that spans providers with no unified view.

![Meme image about multi-cloud strategy adoption](https://cdn.thenewstack.io/media/2026/04/d8619619-1.jpg)

Most cross-provider IaC platforms ([env zero](https://www.env0.com/solutions/cloud-asset-management) included) give you a single place to manage deployments across AWS, GCP, and Azure, with consistent policy enforcement for what goes through your pipelines. That’s genuinely useful. But it only covers resources that went through your pipelines.

Anything that predates the pipeline, came in through an acquisition, or was provisioned outside it: still a blind spot. The [env zero + CloudQuery merger](https://thenewstack.io/closing-cloud-operational-gap/) was specifically about closing that gap, but even so, the problem has to be named clearly.

Solid IaC management gives you visibility into what went through your pipelines. It doesn’t tell you what exists outside them.

## The spreadsheet I gave up on

The cloud consoles are per-provider and per-account. To get a complete picture, the old way, you open the AWS console and navigate account by account, region by region. Then you switch to [GCP](https://thenewstack.io/googles-cloud-idp-could-replace-platform-engineering/) and start over with a completely different interface and mental model.

Then, Azure has its own navigation conventions. None of them talks to each other. There’s no “show me everything” button that works across providers.

Then there’s the tagging problem. In our case, we had two organizations merging, each with different tagging conventions, different levels of enforcement, different ideas about which tags were mandatory, and what the values should look like.

Some resources on the CloudQuery side had a single-owner format. Some resources from the env zero side had a different one. Some resources predated any tagging policy. Some were provisioned by automation that didn’t follow either standard.

Running a query like “who owns this resource?” against the full combined footprint would have required first agreeing on what “owner” even meant, then cross-referencing multiple systems to determine which convention a given resource used.

I tried to build a spreadsheet. I spent most of a day on it, pulling from consoles and cost reports and asking team leads, and by the time I finished the first provider, I had low confidence in the accuracy of what I’d written and decided not to proceed with the other two.

Cost reports tell you what you’re paying for, not what’s running. They’re billing line items, not resource inventory. And asking team leads produces the list of what teams *think about regularly*, which isn’t the same as everything that exists.

One thing I’d do differently if starting over: agree on a single tagging schema before the merger closes, even a minimal one (owner, environment, cost-center), and enforce it from day one. You can’t retroactively tag two organizations’ worth of resources into consistency. You can prevent the next two years of “who owns this?” from being unanswerable.

![Meme image about auditing cloud inventories from AWS consoles](https://cdn.thenewstack.io/media/2026/04/988ec26f-2.jpg)

## The query that answered it

[CloudQuery](https://www.cloudquery.io/blog/complete-guide-building-multi-cloud-asset-inventory) pulls your real cloud state from AWS, GCP, Azure, Kubernetes, Cloudflare, and [dozens of other providers](https://www.cloudquery.io/hub/) into SQL tables you can query directly. Each provider syncs to its own tables (`aws_ec2_instances`, `gcp_compute_instances`, `azure_compute_virtual_machines`), so a cross-provider count looks like this:

```

SELECT 'aws' AS provider, 'ec2_instance' AS resource_type, COUNT(*) AS count
FROM aws_ec2_instances
UNION ALL
SELECT 'gcp', 'compute_instance', COUNT(*) FROM gcp_compute_instances
UNION ALL
SELECT 'azure', 'virtual_machine', COUNT(*) FROM azure_compute_virtual_machines
ORDER BY count DESC;

```

You’d extend that for every resource type you care about. The [pre-built multi-cloud inventory report](https://www.cloudquery.io/hub/reports/multi-cloud-asset-inventory) handles full aggregation automatically, which is what we actually used. But even writing it by hand, going from “we don’t have a picture” to “here’s the breakdown by provider” was a morning, not a week-long audit. I could filter by tag, join on cost data, and cross-reference what the IaC declared with what was actually there.

The question that required three Slack threads became one that took three minutes.

## Where this still falls short

Once the inventory was unified, the next problem arrived quickly: I still had to know what to look for.

At a two-provider scale, you can write the queries. You build a small library of recurring checks (untagged resources, things that shouldn’t be publicly accessible, compute that should have been decommissioned) and run them on a schedule. That works.

The footprint we were dealing with after the merger wasn’t two providers. It was two providers times two organizations, with two different naming conventions, two different policy regimes, and a long tail of resources that neither side had looked at recently. Covering all of it with manually written queries would have required knowing in advance every category of thing that might be wrong. Which you don’t know in advance.

When we went from one cloud footprint to two overnight, I realized we needed the system to surface what was worth looking at, not just respond to questions we thought to ask. The inventory stays current. What looks off comes to you. You no longer have to remember to ask.

Multi-cloud wasn’t a decision we made. It was a condition we found ourselves in, built up through years of individually reasonable choices. The teams I’ve seen handle it well aren’t the ones with the most deliberate cloud architecture. They’re the ones who treated inventory and visibility as foundational infrastructure, who built the unified picture before the merger, before the incident, before the audit forced the question.

> “The teams I’ve seen handle it well aren’t the ones with the most deliberate cloud architecture. They’re the ones who treated inventory and visibility as foundational infrastructure.”

If I were starting over, that’s the first thing I’d put in place. Not because it solves multi-cloud complexity (it doesn’t), but because you can’t govern what you can’t see.

Build the inventory first. Security audits, cost attribution, incident response, compliance prep: all of it assumes you know what’s running. The inventory is the foundation, and it’s the one thing that doesn’t get easier to build retroactively.If you want to run this against your own infrastructure, [CloudQuery’s quick-start guide](https://www.cloudquery.io/product/cloud-asset-inventory) covers the setup. The multi-cloud process is the same as a single provider, just with more source plugins configured.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/07/a0fac1d3-cropped-707f93eb-joe-karlsson.jpg)

Joe Karlsson is a developer advocate at env zero + CloudQuery, where he works on cloud infrastructure tooling and developer experience. He writes about IaC, cloud operations, and the gap between what infrastructure is supposed to do and what it's...

Read more from Joe Karlsson](https://thenewstack.io/author/joe-karlsson/)