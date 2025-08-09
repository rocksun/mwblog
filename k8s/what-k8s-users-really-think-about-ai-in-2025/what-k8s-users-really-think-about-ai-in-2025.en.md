I’ve spent four springs in a row staring at giant spreadsheets of research data and combing through hours of practitioner interviews as I prepare for our annual “State of Production Kubernetes” report.

Each year comes with a signature surprise: In 2022, it was the depth of the [skills gap](https://thenewstack.io/new-research-shows-the-future-is-bright-for-edge-kubernetes/); in 2023, the felt [pain of DevEx](https://thenewstack.io/the-2023-state-of-kubernetes-in-production/); and last year, the impact of [risk and volatility](https://thenewstack.io/kubernetes-48-of-users-struggle-with-tool-choice/) in the cloud native landscape.

2025’s unmistakable headline is AI. Not hype‑cycle speculation, but real workloads, real budgets and — crucially — real operational headaches.

Below is a guided tour of the AI findings from this year’s 455‑respondent study. (It’s just one of five themes we tackle in the full 44‑page report, but it’s the one everyone asks about first.)

## 1. AI Becomes Kubernetes’ New Center of Gravity

One interviewee, a cloud engineering manager in U.S. healthcare, called AI a “modern gold rush,” with leadership “staking the company’s future growth on large‑scale adoption of AI.”

Of course, from an IT perspective, when we talk about businesses embracing AI, what we’re really talking about is new application workloads. And workloads have to run somewhere.

A full 90% of respondents expect the number of AI and machine learning (ML) workloads they run on Kubernetes to grow in the next 12 months — the strongest growth signal in the entire survey.

The demands of AI workloads are also changing organizations’ environment strategy — where they choose to build and run their clusters.

AI is the third strongest driver of cluster placement (after the demands of multicloud strategies and on-premises repatriation). In fact, 28% say they already place clusters in dedicated GPU clouds.

Yet enthusiasm isn’t universal. A public‑sector CIO cautioned that giving algorithms operational control of core business processes (in his example, traffic lights turning green or red) “feels risky for a transit agency.” The big takeaway: Executives see revenue; operators see latency, cost and compliance.

## 2. Edge Kubernetes Rides Shotgun

We’ve always said that for many workloads, AI’s natural home is at the edge, where real-time inference, such as computer vision, can be right next to the data it needs to process and provide real-time, low-latency decisioning. As one interviewee put it:

“AI inference workloads that demand real-time decisions — think autonomous vehicles — belong at the edge, as close as possible to the data source, because millisecond-level latency is non-negotiable.”

This year, the push from AI tipped edge Kubernetes into majority production use for the first time. Half of all enterprises now run production clusters at the edge, up from 38% last year. Of those edge adopters, 81% expect their footprint to grow in 2025.

When we asked what makes edge hard in 2025, the answers shifted dramatically. Traditional worries, like performing Day 2 operations and field engineering challenges, fell away; instead, we saw pain around device performance, connectivity and model management.

[![41% report problems managing AI workloads, up from 25% last year.](https://cdn.thenewstack.io/media/2025/07/cc0bd2ad-k8s-challenges_spectrocloud.png)](https://cdn.thenewstack.io/media/2025/07/cc0bd2ad-k8s-challenges_spectrocloud.png)

Year on year, we see changes in the top challenges users face with edge K8s. This year, it’s all about handling beefy AI workloads. (Source: Spectro Cloud.)

A U.S. manufacturer summed up the new reality:

“Performance is really the biggest issue that I see for AI and Kubernetes. With AI it’s completely different from normal K8s workloads. LLMs [large language models] need sheer horsepower… we’ve spent a lot of time tuning container settings and node profiles to hit our speed targets.”

In other words, edge use cases that may once have focused on lightweight Internet of Things (IoT) telemetry are now about computer‑vision pipelines and real‑time inference that melt weaker hardware and require regular updates.

## 3. AI as a Cost‑Control Strategy — Really

Kubernetes total cost of ownership (TCO) is rising fast (88% of respondents say their bill went up in the past 12 months), and cost was the top challenge they felt this year.

With new AI workloads, and more clusters running in multiple different clouds and other environments, it’s easy for spend to get out of hand.

Each year, we ask what our respondents believe is the biggest opportunity to improve efficiency in their K8s operations. This year, AI is the only efficiency lever that the majority believe in.

Half — 51% — selected “use AI to improve operations” as a top opportunity to increase K8s efficiency, edging out autoscaling and cloud spend optimization.

[![AI has emerged as the leading opportunity to drive K8s operational efficiency.](https://cdn.thenewstack.io/media/2025/07/b8e48e62-k8s-efficiency_spectrocloud.png)](https://cdn.thenewstack.io/media/2025/07/b8e48e62-k8s-efficiency_spectrocloud.png)

AI has emerged as the leading opportunity to drive K8s operational efficiency. (Source: Spectro Cloud.)

And they tell us this is not just wishful thinking, but something they are actively pursuing. An astonishing 92% say they are already investing in next‑gen AI‑powered optimization tools.

Several of our interviewees expounded breathlessly about how they saw AI copilots as an opportunity to right-size clusters to eliminate overspend, or automatically troubleshoot and remediate issues.

“The biggest challenge is that application teams think they know what they want, but we end up with clusters that are not fully utilized. AI can definitely help. With natural-language prompts you could ask, ‘How should we reconfigure and optimize it?’ AI could even generate the YAML manifests: describe your app — how many clusters, nodes, sizes — and it returns the recommendations. You’d chat with it and get the information you need. Could that become a Kubernetes copilot like today’s AI coding assistants? Yes, absolutely — 100% yes.”

Skeptics remain. One U.K. telco director said, “The platform has too many variables that sit outside system control” for a copilot to be trustworthy. A U.S. public‑sector CIO worried more about union backlash than code quality if AI started closing tickets. Still, the spending trend is clear: AI isn’t just a workload; it’s the hoped‑for antidote to Kubernetes sticker shock.

## So What?

While “AI” may be the biggest buzzword in IT, it’s not one thing.

First, it’s a driver for new application demands in this “gold rush.” And every one of those workloads needs the right underlying infrastructure, whether that’s a GPU cloud or an edge box. Chances are, your traditional environments and hardware aren’t sufficient. AI workloads also introduce new management requirements, principally the need to move new versions of large models around on a weekly basis.

Second, it’s a cost pressure. New applications in new places mean more hardware, more software, and, most importantly, more people time to manage the infrastructure estate. Cost was always an issue in operating Kubernetes, and now it’s even tougher.

Third, AI is expected to be an operational silver bullet. Sprinkling AI fairy dust into FinOps tools or into copilots within management platforms is the hoped-for solution to the challenges and costs of managing clusters at scale, in diverse environments. It would be a wonderful thing if we could let AI deal with YAML hell, cure our overprovisioning headaches and investigate the most esoteric root causes. Will reality live up to the expectations? Well, history tells us that the complexity and cost of Kubernetes are not so easy to solve. Time will tell.

## Continue the Exploration

I’ve covered just one slice of the data from our “2025 State of Production Kubernetes” research. The full report has 40+ pages of data, charts and interview stories, covering adoption benchmarks, operational best practices and hot topics like AI and [KubeVirt](https://thenewstack.io/how-to-migrate-your-vms-to-kubevirt-with-forklift/).

Get your copy of the [“2025 State of Production Kubernetes” report](http://spectrocloud.com/state-of-kubernetes-2025), or [register and join our live webinar](https://www.brighttalk.com/webcast/19922/649377) on September 11 for a whistlestop tour of the key findings. See you there — and here’s to another year of surprises in the ever‑evolving world of Kubernetes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/6df0e98a-antnewman.jpg)

Ant Newman is director of content at Spectro Cloud. He has spent 20 years working across the enterprise technology landscape, covering trends from IoT to cybersecurity. After stints agency-side, at Gartner and Cisco, he joined Spectro Cloud to lead its...

Read more from Ant Newman](https://thenewstack.io/author/ant-newman/)