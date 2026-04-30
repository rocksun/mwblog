It was a Tuesday afternoon. Terraform plan came back clean. No changes. I double-checked, because the last few deploys had been messy and I wanted to be sure. Still clean. So I merged the PR, grabbed coffee, and went to a 3 p.m. meeting about Q3 roadmap priorities that I genuinely did not need to attend.

Forty-five minutes later, I had five Slack messages waiting for me.

Our API was returning 403s on a specific endpoint. The service logs were unhelpful, as service logs always are when something is actually wrong (lots of noise, no signal). It took two hours to trace it back to an S3 bucket policy. During an incident three weeks earlier, someone manually tightened the policy in the AWS console to prevent potential exposure. The incident closed, the ticket closed, and the Slack thread went quiet.

Nobody updated the [Terraform](https://thenewstack.io/your-platform-engineering-toolkit-for-terraform-and-beyond/) config. Nobody submitted a PR. The state file had no record of the change because the change never went through Terraform.

From Terraform’s perspective, the policy was exactly as declared. From the real world’s perspective, it had been different for three weeks, and a new deployment finally broke against it.

This is not a horror story. This is a Tuesday.

## How the state file gets out of sync

!["This is fine" meme template relating to Terraform service returning 403s for two weeks](https://cdn.thenewstack.io/media/2026/04/596d12c0-1.jpg)

[Terraform state](https://developer.hashicorp.com/terraform/language/state) isn’t a live record. It’s a snapshot, a JSON document capturing what the infrastructure looked like after the last `terraform apply` ran successfully. env zero has a [thorough writeup on exactly what that file contains and why it matters](https://www.env0.com/blog/a-guide-to-the-terraform-state-file), and the core point is right there in the framing: “a snapshot of what your infrastructure looked like after the last apply.” Not what it looks like now.

That distinction matters more than it sounds. IaC is a declaration of intent. You declare what *should* exist. Terraform reconciles that declaration with what *did* exist at the time of your last apply. But the cloud keeps moving after that.

Here’s what a Terraform state file actually looks like for an S3 bucket policy (abbreviated; real files also include `terraform_version`, `lineage`, resource `mode`, and provider reference):

```

{
  "version": 4,
  "serial": 47,
  "resources": [
    {
      "type": "aws_s3_bucket_policy",
      "name": "api_data",
      "instances": [
        {
          "attributes": {
            "bucket": "prod-api-data-bucket",
            "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",...}]}"
          }
        }
      ]
    }
  ]
}

```

Serial 47. That’s a count of state writes Terraform knows about: applies, `terraform apply -refresh-only` runs, `terraform state` commands. Each one tracked. Everything that happened outside Terraform’s operations: not tracked. If the bucket policy changed manually after serial 47, this file still reflects serial 47’s view of the world.

The obvious question is: what about `terraform refresh`? (It was deprecated in Terraform 0.15; the current equivalent is `terraform apply -refresh-only`.) By default, `terraform plan` also refreshes state from the provider before comparing. It catches drift on resources Terraform already knows about. But it does nothing for the bucket someone created manually three months ago, or the IAM role added as a one-off during an incident. Terraform has no record of them, so it has nothing to refresh. The [gap isn’t just stale data](https://thenewstack.io/bridging-the-data-gap-real-time-user-facing-analytics/) on known resources. It’s resources that never made it into the state file at all.

> “The gap isn’t just stale data on known resources. It’s resources that never made it into the state file at all.”

Manual changes are the obvious culprit: hotfixes applied at 2 a.m., experiments that got partially cleaned up, console changes nobody came back to document. But the subtler problem is [service-managed drift](https://thenewstack.io/the-engineers-guide-to-controlling-configuration-drift/). [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) changes your instance counts. RDS [auto-scales storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling) when it hits a threshold. [ECS Application Auto Scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) adjusts a service’s desired task count in response to load, with Terraform none the wiser. None of that goes through Terraform. It’s not human error. It’s the cloud doing exactly what you configured it to do, in ways your state file was never designed to track. Third-party integrations, policy enforcement tools, and cost optimizers add another layer on top of that.

We had solid pipeline discipline through [env zero](https://www.env0.com/solutions/cloud-asset-management): consistent runs, policy enforcement, team-level controls. But any deployment tool only knows about what goes through it. It tells you about the resources managed through your pipelines. It says nothing about the S3 bucket that got tightened at 11 p.m. on a Thursday.

The state file is a snapshot. In an environment where people are working, fixing things, trying experiments, and making pragmatic compromises, that snapshot can be days or weeks out of date in exactly the ways that matter.

And the dangerous part isn’t just that you don’t know about the drift. It’s that your next `terraform apply` will act on the version of the world it believes in. The engineer who tightened your S3 bucket policy at 2am to stop an exposure? Your next deploy quietly opens it back up. Terraform does exactly what you told it to do. It just didn’t know what happened between applies.

## The problem with “just enforce the pipeline”

Okay, so the fix is obvious, right? Just don’t make manual changes. Enforce the pipeline. If it didn’t go through Terraform, it didn’t happen.

Sure. Good luck with that at scale.

One AWS account, one region, a small team: you can maybe hold the line. You can feel the edges of the infrastructure. Drift still happens, but you catch it quickly because the surface area is small and the team all knows what’s running.

Now add accounts. Staging, prod, disaster recovery, per-region redundancy. Add an acquired team with their own AWS org, their own naming conventions, their own collection of manually-provisioned resources that predate any IaC discipline. Now you’re maintaining dozens of state files. The AWS console shows you one account at a time. The GCP console shows you one project at a time. Scripts work until they don’t, and they have to be written *before* you know what to look for. That’s the problem. Drift doesn’t announce itself.

Console archaeology: opening accounts one by one, trying to build a mental picture by clicking through EC2, S3, IAM, RDS. Fine for a couple of accounts. Completely unsustainable at ten. I would finish an account and immediately lose confidence in the first one I’d checked. I once spent a Friday afternoon manually comparing security groups across three accounts against what the state files described. I found two discrepancies. I also couldn’t shake the feeling I’d missed three more.

The boto3 scripts phase: write a script to enumerate resources, dump to CSV, compare against state. I had one that worked fine until we scaled past the default page size, and it started silently missing instances. `DescribeInstances` paginates, and if you don’t implement the pagination loop correctly, it just returns the first page and stops. No error. Fixed that one, and the S3 enumeration script stopped working for unrelated reasons. I ended up with a small collection of scripts, each covering a different service, each requiring maintenance on a schedule that bore no relation to when I actually needed them.

Manual audits: asking team leads to inventory what their teams were running. This produced lists of what people *thought about regularly*. It missed everything that had become invisible through familiarity.

Every approach hit the same wall: I had to know what I was looking for before I could look for it.

## Querying what’s actually running

![Meme favoring SQL querying cloud state over manually checking the Terraform state file](https://cdn.thenewstack.io/media/2026/04/a91e80e4-2.jpg)

What actually changed how I work: I stopped treating infrastructure as a set of consoles to navigate and started treating it like a database.

[CloudQuery](https://www.cloudquery.io/product/cloud-asset-inventory) syncs your actual cloud state into SQL tables: what exists in your AWS accounts right now, not what Terraform last recorded. You connect it to your accounts, run a sync, and query the infrastructure the same way you’d query a database. Here’s what that looked like for the tagging problem I’d been dealing with:

```

SELECT account_id, region, instance_id, tags
FROM aws_ec2_instances
WHERE tags->>'owner' IS NULL
ORDER BY account_id, region;

```

That query returns every EC2 instance without an owner tag, [across every account](https://www.cloudquery.io/hub/plugins/source/cloudquery/aws/latest/tables/aws_ec2_instances), in one result set. Not account by account. Not region by region. I didn’t have to write account-specific scripts or remember which regions I’d deployed to. The data was normalized and queryable, and the query took maybe two minutes to write.

You can write similar queries for anything you care about: S3 buckets with public access, security groups with open ingress rules, IAM roles with `*` permissions, RDS instances without encryption. The [CloudQuery hub](https://www.cloudquery.io/hub/) has pre-built queries for the most common cases if you don’t want to start from scratch.

The state file tells you what Terraform thinks is running. This tells you what’s actually running.

> “The state file tells you what Terraform thinks is running. This tells you what’s actually running.”

When you do find drift, the fix depends on which direction it went. If Terraform is managing a resource that no longer exists in the cloud, `terraform state rm` removes it from state without destroying anything. If there’s a resource in the cloud that *should* be under Terraform control, `terraform import` pulls it in. Terraform 1.5+ added `-generate-config-out` to auto-generate a starting config, though you’ll still need to review and clean it up (it’s a scaffold, not a finished file). Neither path is glamorous. But knowing which situation you’re in, and finding it before it causes an incident, is most of the work.

## The drift you didn’t know to look for

![Meme template showing four levels of looking for drift](https://cdn.thenewstack.io/media/2026/04/7aad18fb-3.jpg)

Here’s the limit of this approach, though: it still requires you to know what to ask.

Most of the time, that’s fine. I know the questions I care about. I can write queries for known risk patterns and run them on a schedule. That works.

The harder problem is the drift I *didn’t know to look for*. The S3 bucket policy that got tightened during an incident. The IAM role that someone expanded “temporarily” during a debug session and never scoped back down. The EC2 instance that was supposed to be shut down after an experiment but wasn’t. None of these fails loudly. They sit in the gap between declared and actual state, invisible until something breaks against them.

What I keep coming back to is what it would look like if the tool had opinions rather than just data, surfacing anomalies it found on its own instead of waiting for your query. Resources that exist in the cloud but not in any IaC state. Configuration that changed since the last sync. Patterns that look off across accounts. The query layer covers the risks you know about. I want something with enough context to tell me what’s worth looking at without being asked.

The gap doesn’t close by running apply more often or by enforcing the pipeline more strictly. It closes when you stop treating the state file as a source of truth.

The S3 incident I opened with was the last one I accidentally caught. Because after that, I had something to look at instead of waiting for an outage to tell me.

If you’re dealing with this across more than one cloud provider (and if you’ve been through a merger or an acquisition, you probably are), the drift problem gets considerably more complicated. I wrote about that separately in [*Multi-Cloud Happened to Us by Accident*](https://markdowntohtml.com/multicloud-accident-thenewstack-2026.md).

If you want to try the query approach yourself, [CloudQuery’s product page](https://www.cloudquery.io/product/cloud-asset-inventory) has setup instructions for connecting your first cloud account.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/07/a0fac1d3-cropped-707f93eb-joe-karlsson.jpg)

Joe Karlsson is a developer advocate at env zero + CloudQuery, where he works on cloud infrastructure tooling and developer experience. He writes about IaC, cloud operations, and the gap between what infrastructure is supposed to do and what it's...

Read more from Joe Karlsson](https://thenewstack.io/author/joe-karlsson/)