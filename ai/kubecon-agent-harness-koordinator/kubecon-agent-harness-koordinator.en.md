**Welcome to another edition of** [**Road to KubeCon**](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/), your source for everything Kubernetes and cloud-native as we count down the days to [KubeCon + CloudNativeCon NA](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/), happening November 9-12 in Salt Lake City, Utah.

This week, we take a look at the state of agent harnesses and what needs to evolve. We also feature HPE’s thoughts on Kubernetes visibility, more sci-fi agentic DevOps, and an impressive scheduler that shows Kubernetes’ default scheduler who’s the boss of GPU utilization.

That plus news from CNCF: what to expect at this year’s ArgoCon, a great opportunity to improve your open source project’s security hygiene, Atlassian’s stack for slashing event-to-metric latency, and a special gift for TNS readers.

## **HPE shares tips for Kubernetes visibility on TNS**

Getting Kubernetes running is a milestone. Knowing who owns the next upgrade, the access request, or failed recovery is an ongoing journey.

This week, we published “[A live Kubernetes cluster can still have an ownership gap](https://thenewstack.io/kubernetes-operations-ownership-governance/),” the second installment in Chris J. Preimesberger’s four-part, HPE-sponsored series. It examines how platform and application teams divide responsibilities after launch, from configuration drift and security policies to upgrade validation and recovery drills. A healthy cluster doesn’t necessarily mean a healthy application — and someone needs to own that gap.

*Hewlett Packard Enterprise (HPE) is a presenting sponsor of Road to KubeCon.* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *helps IT organizations modernize infrastructure, streamline operations, and accelerate AI initiatives across hybrid, multi-vendor environments.*

Missed the opener? [Part one explores Kubernetes self-service](https://thenewstack.io/kubernetes-self-service-platform-teams/): how developers can get approved environments without waiting through ticket queues, while platform teams retain responsibility for access, costs, and lifecycle controls. Together, the articles ask a practical question: How do you give developers more independence while making operational accountability clear?

Next, the series turns to diagnosing slow applications when Kubernetes looks healthy, then to measuring AI inference performance. Both will explore the visibility teams need as their workloads become more demanding on the road to KubeCon.

## **CNCF offers a 10% discount to TNS readers**

This week, *The New Stack* readers get a special treat from Cloud Native Computing Foundation (CNCF). If you’re planning to attend KubeCon + CloudNativeCon NA in Salt Lake City, use the discount code `KCNA26MED10` when you [register at this link](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/?utm_campaign=45192315-KubeCon-NA-2026&utm_source=Media%20Partner%202026) for 10% off your admission.

We’re only 38 days out til KubeCon (or four Road to KubeCon editions out if you count in columns), so better act soon to register and plan your trip.

## **Agent harnesses go cloud-native**

The agent “harness” quickly became a catch-all for everything that surrounds an AI agent: the context, filesystem, subagents, permissions, and more. However, [Craig McLuckie](https://www.linkedin.com/in/craigmcluckie/), founder and CEO of [Stacklok](https://stacklok.com/), says it’s not enough.

To him, most harnesses are too local and built to serve a single developer at a laptop. The typical harness doesn’t scale well enough to serve hundreds of sessions. Sessions break, and you can’t easily move the experience between clients or devices.

This week, he takes to the [CNCF blog](https://www.cncf.io/blog/2026/09/28/the-case-for-a-cloud-native-agent-harness/) to argue for a cloud-native agent harness. To him, that’s a distributed application that separates the agent loop from the infrastructure and services around it.

“Kubernetes taught this industry that a monolith in a container is still a monolith,” he writes. “The lesson applies to agents too.”

## **Koordinator boosts on-Kubernetes GPU allocation >95%**

A [case study](https://www.cncf.io/case-studies/zhuoyu-technology/) published on Tuesday details how Zhuoyu Technology, a Chinese autonomous driving technology company, is dramatically improving Kubernetes utilization with [Koordinator](https://koordinator.sh/), a CNCF sandbox project for efficiently scheduling microservices, AI, and big data workloads.

Zhuoyu Technology runs autonomous driving workloads on Kubernetes-based environments but hit performance inefficiencies with the default Kubernetes scheduler, which capped allocation and utilization. By using Koordinator, the team pushed GPU allocation above 95% and overall GPU utilization above 55%.

The case study demonstrates how certain gaps in the default Kubernetes scheduler can lead to failed launches, low GPU utilization, stranded GPUs, and distributed-job scheduling problems. It also demonstrates how Koordinator is faring well in production environments.

## **CNCF and OpenSSF announce month-long challenge**

[Open Source Security Foundation](https://openssf.org/) (OpenSSF) and CNCF are teaming up to organize the [Security Slam](https://openssf.org/blog/2026/09/23/security-slam-2026-fall-edition/), a 30-day challenge that walks participants through using OpenSSF projects to improve their project’s security posture.

All open source projects are invited to participate. Write [Eddie Knight](https://www.linkedin.com/in/knight1776) and OpenSSF’s [Stacey Potter](https://www.linkedin.com/in/staceympotter), the Slam is “now taking advantage of new tools to greatly broaden the qualifications for participation.”

The challenge runs October 5 through November 6. [Register here](http://securityslam.com/slam26/register) to get involved and follow the objectives as they’re announced. Complete the challenges, and you might just have a fancy award ready for you at the OpenSSF booth (#313) at KubeCon.

## **Atlassian’s cloud-native stack takes event-to-metric below 10 seconds**

In incident detection and response, every second counts. On Wednesday, [Deepak Biswas](https://www.linkedin.com/in/dkbiswas/), senior engineering manager at Atlassian, shared a [deep case study](https://www.cncf.io/blog/2026/09/30/from-40-seconds-to-under-10-rebuilding-incident-detection-on-opentelemetry-apache-kafka-and-apache-flink-on-kubernetes/) on the CNCF blog about Atlassian’s journey to show how far you can go to shave those seconds down.

The detection platform behind AutoHOT, its automated incident creation system, combines [OpenTelemetry](https://thenewstack.io/opentelemetry-prometheus-observability-interoperability/), [Apache Kafka](https://kafka.apache.org/), and [Apache Flink](https://flink.apache.org/) on Kubernetes. Operational telemetry tracks user actions across more than 10 cloud products serving millions of tenants, generating billions of events per day.

The headline says it all: They’ve reduced their event-to-metric *metric* (to be meta about it) from more than 40 seconds to under 10.

Yet, Biswas is honest: “It is not a success story with a bow on it.” They’re still working on fine-tuning. Recall, for instance, fell to 64% in August. Nevertheless, it’s a useful blueprint for others building automated incident detection and response workflows.

*As Kubernetes evolves, so do the demands on the teams running it. Presenting sponsor* [*HPE*](https://www.hpe.com/us/en/products/software.html) *helps teams address that complexity with software spanning virtualization, cloud management, observability, and automation.*

## **Argo CD 4.0 visioning begins**

KubeCon NA will feature [ArgoCon North America 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/argocon/) on the co-located day, Monday, Nov. 9. It’s a full-day, two-track event with practical ideas on improving software delivery, managing data and machine learning pipelines, and implementing progressive delivery.

In a [post on the CNCF blog on Wednesday](https://www.cncf.io/blog/2026/09/30/argocon-north-america-2026-what-to-expect-as-the-argo-community-looks-toward-cd-4-0/), ArgoCon co-chairs Dan Garfield, Christian Hernandez, and Katie Lamkin stress that the event comes as the community begins the visioning process for Argo CD 4.0.

They describe ArgoCon, [whose schedule is live here](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/argocon/#about), as “an opportunity to connect around what users are building today and where the projects are heading next.”

## **Cycle’s** DevOps **control plane gets sci-fi**

“If you told me this existed just a couple of years ago, I would have thought ‘this is science fiction, and it shouldn’t be real,'” says head of engineering [Alexander Mattoni](https://www.youtube.com/watch?v=q4T7U32g7xk) in a [feature announcement video](https://youtu.be/q4T7U32g7xk?si=-mXwRXdDZj1IBGn9) this week, showing off a [new remote MCP server](https://cycle.io/blog/cycle-launches-mcp) for Cycle, the DevOps control plane.

The release essentially means Cycle users can provision, orchestrate, and manage workloads across multicloud and hybrid environments via natural language, using MCP-compatible AI assistants and coding tools.

It follows a string of agentic features being released in the cloud native industry that continue to abstract DevOps and put impressive capabilities into the prompt. What was sci-fi yesterday is becoming more and more the status quo today.

## **Follow the Road to KubeCon**

*Road to KubeCon is an eight-part series presented by HPE at KubeCon + CloudNativeCon North America in Salt Lake City. Before you go, explore how* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *helps IT teams do more with less complexity.*

228 [CNCF projects](https://www.cncf.io/). 1,754 individual contributors to the [latest Kubernetes release](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/). Over 230 sponsors and exhibitors expected at KubeCon NA 2026…

The cloud-native ecosystem is booming. As such, there’s always something going on.

We’ll be here every Friday to track it on *The New Stack* until KubeCon NA.

That means, before we catch up at the show, there’s still a handful of editions and blurbs to pen.

If you’re working in the cloud native space and have something interesting to share, [Bill Doerrfeld](https://www.doerrfeld.io/), the writer of this series, is open to pitches. You can share news, story ideas, or quotes through his [personal contact page](https://www.doerrfeld.io/contact).

If you missed last week’s edition on [OpenTelemetry and Prometheus interoperability](https://thenewstack.io/opentelemetry-prometheus-observability-interoperability/), you can catch up here.

You can also follow the Road to KubeCon [series archive](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/02/96a1456d-cropped-e7e1c083-bill-doerrfeld.jpg)

Bill Doerrfeld is a tech journalist and API thought leader. He is the editor-in-chief of the Nordic APIs blog, a global API community dedicated to making the world more programmable. He is also an active contributor to a handful of...

Read more from Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)