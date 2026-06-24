[Amazon Web Services](https://thenewstack.io/a-cascade-of-failures-a-breakdown-of-the-massive-aws-outage/) has added a third specialized “frontier agent” to its growing portfolio of AI tools aimed at IT operations — this one focused on the cloud bill.

[AWS FinOps Agent](https://docs.aws.amazon.com/finops-agent/latest/userguide/what-is.html), which the company moved into public preview last week, follows the earlier debuts of [AWS’s Security Agent](https://aws.amazon.com/security-agent/) and [DevOps Agent](https://aws.amazon.com/devops-agent/). It enters a domain that has historically relied on dashboards, spreadsheets, and a human analyst’s knowledge, and hands it to an agent that can be asked questions in plain English and that can act on its own when something looks wrong.

In this case, the domain is [FinOps](https://thenewstack.io/how-to-build-a-finops-strategy-that-works/) — the discipline of getting engineering, finance, and business teams to share accountability for cloud spending. AWS frames the new agent as a response to a shift it says is already underway: FinOps work moving from periodic, dashboard-driven reviews toward continuous workflows that run inside the tools engineering teams already use, namely Jira and Slack.

## What the agent does

The core workflow starts where [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) leaves off. Today, an anomaly alert tells a team that something changed; it doesn’t say what or why. FinOps Agent is built to take that next step — correlating the cost spike against AWS CloudTrail’s record of who changed what and when, identifying the triggering change, and assembling an investigation summary that names both a probable root cause and a responsible owner. From there, it can open a Jira ticket or post to a Slack channel automatically.

The agent answers natural-language cost questions, such as “Why did my AWS cost go up last month?” It does so by pulling from Cost Explorer, Cost Optimization Hub, and Compute Optimizer and tying the answer back to specific services and usage drivers. Organizations can upload context files mapping accounts to owners, teams, and tagging conventions, which the agent uses to translate a question like “what’s the cost of Team X” into the right set of accounts.

The public preview also adds scheduled cost reporting (daily, weekly, or monthly, exportable as HTML, PDF, or PPT) and a feature that bundles Cost Optimization Hub and Compute Optimizer recommendations into a Jira ticket engineers can act on.

## The permission model is mostly read-only

For a tool that’s being given broad visibility into billing, usage, and operational data across an account, the access AWS is asking for is constrained. According to AWS’s documentation, the [IAM](https://thenewstack.io/a-deep-dive-into-the-security-of-iam-in-aws/) role FinOps Agent uses is primarily read-only across billing, optimization, monitoring, logging, and infrastructure services — enough to analyze costs, investigate anomalies, and surface savings opportunities, but not enough to touch the resources themselves.

The only write access granted is for managing the agent’s own EventBridge scheduling rules, which drive its recurring automations. It can’t create, modify, or delete EC2 instances, [RDS databases](https://thenewstack.io/diving-into-aws-databases-amazon-rds-and-dynamodb-explained/), Lambda functions, or networking components. The agent is built on Amazon Bedrock, which AWS says includes its standard automated abuse-detection guardrails.

## Early customers

AWS’s announcement mentions four customer accounts, each describing a slightly different pain point the agent is meant to address. [Workday](https://www.workday.com/en-us/homepage.html)‘s AI Platform Infrastructure team, which runs the company’s AI platform across many AWS accounts, described the appeal as consolidating two time sinks — “chasing down cost outliers before they become budget problems” and assembling the monthly reports leadership reviews — into one natural-language interface, according to [Serjesh Sharma](https://www.linkedin.com/in/serjeshsharma/), Manager of Software Development Engineering at Workday.

[Mitre 10](https://www.mitre10.co.nz/), New Zealand’s largest home-improvement retailer, framed it in terms of competing priorities for a lean platform team. Eduard Kleynhans, the company’s Platform Engineering Manager, said recurring cost reviews and anomaly checks have historically “competed directly with reliability and improvement work,” and that the appeal of the agent is having those checks “run continuously in the background” so findings surface only “when there’s something that genuinely warrants attention.”

[Convera](https://convera.com/), a commercial payments company operating in a regulated environment, pointed to a more specific failure mode: small, unintended cost changes that get lost in a shared queue. [Ramesh Singaraj](https://www.linkedin.com/in/rameshsingaraj/), the company’s Infrastructure Engineering and Operations Leader, said the agent’s value is that it routes a Jira ticket “to the engineering team that owns the resource, so the right engineer sees it instead of a shared queue that nobody watches.”

And [AVIV Group](https://www.aviv-group.com/), which operates digital real-estate marketplaces across France, Germany, and Belgium with hundreds of AWS accounts under a centralized FinOps team, framed the agent as a way to offload first-line questions, like the difference between on-demand and Savings Plan pricing, or why a particular anomaly fired, that currently route back to a small central team before resource owners can act. FinOps Director [Jordi Espasa](https://www.linkedin.com/in/jordiespasa/) said answering those questions directly for engineers frees the central team to focus on “chargeback logic, optimization strategy and leadership reporting.”

## What’s still unsettled

The preview is available only in the US East (N. Virginia) Region, though it can manage cost and usage data across other AWS Regions and accounts when deployed from a management account (GovCloud and the Beijing/Ningxia China Regions are excluded). It’s free to use during the preview, subject to a monthly usage limit, though standard charges still apply for any other AWS services the agent touches along the way.

AWS says the agent will expand over time, including cost analysis aimed specifically at AI workloads. This is notable given that AI infrastructure spend is becoming one of the larger line items FinOps teams are being asked to explain.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)