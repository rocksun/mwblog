On Tuesday, AWS [announced](https://aws.amazon.com/blogs/security/security-hub-adds-ai-workload-protection-and-multicloud-support-for-microsoft-azure/) an expansion to [Security Hub](https://aws.amazon.com/security-hub/), its security operations service, to also monitor Microsoft Azure resources, in addition to more tools for protecting AI workloads. This marks the first time the service natively monitors resources outside of AWS.

In total, the launch includes four major updates: [Azure resource monitoring](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-security-hub-supports-monitoring-microsoft-azure/), Amazon GuardDuty AI Protection, [GuardDuty AI-powered investigations](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-guardduty/), and a Security Hub AI inventory. All but the investigations capability, which is in preview in 10 AWS regions, are now generally available. Together, they deliver on the multicloud expansion AWS [promised](https://aws.amazon.com/blogs/security/aws-security-hub-is-expanding-to-unify-security-operations-across-multicloud-environments/) in March, ahead of the RSA Conference.

## AWS keeping Azure secure

The marquee update, though, is support for monitoring Azure resources. Security Hub can automatically find a customer’s Azure virtual machines, container images, serverless Function Apps, and identities on its own. It then checks them for misconfigurations, internet-facing exposure, and vulnerable software, using the [CIS Azure Foundations Benchmark](https://www.cisecurity.org/benchmark/azure). All of these findings from Azure show up right next to AWS findings in a single ranked queue and can trigger the automation workflows teams have already built.

As Michael Fuller, AWS’s director of security services, writes in a blog post announcing the launches: “Your workloads move to new clouds. Your security should already be there.”

Monitoring an Azure resource costs the same as monitoring its AWS equivalent, with no platform fee on top, and there’s a separate 30-day free trial.

## Securing AI workloads

In comparison, [GuardDuty AI Protection](https://docs.aws.amazon.com/guardduty/latest/ug/ai-protection.html) is very much an AWS-centric product. It aims to detect threats specific to Amazon Bedrock and SageMaker workloads, including anomalous model invocations and prompt injection attempts (through an integration with Bedrock Guardrails), and what AWS calls cost harvesting, in which attackers with stolen credentials rack up inference charges on someone else’s account.

Fuller notes that this is a pattern he keeps seeing. “I talked to one security leader recently,” he writes, “whose team only discovered a compromised service account invoking a foundation model thousands of times because finance flagged the bill.”

AI-powered investigations, now in preview, runs an automated first pass over GuardDuty findings to sort real threats from noise. Each investigation returns a disposition with a confidence score, [a MITRE ATT&CK classification](https://attack.mitre.org/), and remediation recommendations, based on 90 days of related activity. AWS claims the analysis wraps up “in minutes what previously took hours.”

The AI inventory, which is now included in Security Hub’s Essentials plan at no extra cost, catalogs AI assets across an organization, including managed services like Bedrock, SageMaker, and AgentCore, models customers run themselves on EC2, ECS, or EKS, and outside model APIs that internal workloads call. The inventory also ties each asset back to the infrastructure beneath it and connects assets to any related GuardDuty findings.

## A crowded field

AWS isn’t the first of the hyperscalers to monitor a competitor’s cloud. Microsoft Defender for Cloud has offered [posture management for AWS since late 2021 and Google Cloud since early 2022](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/security-posture-management-and-server-protection-for-aws-and-gcp-are-now-genera/3271388). Google [closed its $32 billion acquisition of Wiz](https://thenewstack.io/google-cloud-cat-mouse/), whose platform covers all three major clouds, in March — one day after AWS pre-announced this expansion. Security Hub’s coverage, for now, stops at Azure, and AWS hasn’t said whether Google Cloud support will follow.

The AI protections enter a similarly contested market. Wiz, Palo Alto Networks, and CrowdStrike all sell AI security posture management today.

AWS is betting that customers going multicloud will want Security Hub to be the one console, and the one bill, that follows them there. How long “multicloud” means just Azure will be the first test of how serious that bet is.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)