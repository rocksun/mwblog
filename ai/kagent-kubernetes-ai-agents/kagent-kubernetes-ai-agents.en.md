**Welcome to another edition of** [**Road to KubeCon**](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/), where we’re tracking interesting movements in the cloud-native and Kubernetes ecosystem as we count down the days to [KubeCon + CloudNativeCon NA 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/), to be held in Salt Lake City, Utah, November 9-12.

In this edition, we get formal, requesting audiences with some key cloud-native players. We also cover new SUSE validation for HPE Morpheus Software and what to expect at Platform Engineering Day this year.

Plus, we check out a new(ish) CNCF sandbox project for running agents as Kubernetes resources, a look at assigning Kubernetes compliance ownership, and a story of when to *not* use Kubernetes in practice.

## **HPE Morpheus Software adds SUSE validation**

If you’re an HVM hypervisor user also using [SUSE](https://www.suse.com/), you’re in luck: [HPE Morpheus Software](https://www.hpe.com/us/en/products/software/morpheus-software.html) has now officially gained SUSE certification, meaning the hypervisor can now support SUSE Linux Enterprise Server (SLES) 16.

*Hewlett Packard Enterprise (HPE) is a presenting sponsor of Road to KubeCon.* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *helps IT organizations modernize infrastructure, streamline operations, and accelerate AI initiatives across hybrid, multi-vendor environments.*

Why does SUSE validation matter? According to [HPE’s announcement](https://community.hpe.com/t5/the-cloud-experience-everywhere/hpe-morpheus-software-earns-suse-certification-expanding/ba-p/7273260), “Operating system validation plays a critical role in reducing deployment risk and ensuring predictable outcomes in production environments.” The validation signals maturity and gives operators more confidence.

The addition arrives at a time when some enterprises are juggling hybrid cloud estates and looking for a unified way to manage their virtual machine infrastructure.

## **Platform Engineering Day goes agentic**

Since 2024, a platform engineering event has run alongside KubeCon + CloudNativeCon events, and this year is no different. [Platform Engineering Day](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/platform-engineering-day/?__hstc=60185074.6ca1230192cfed092778db269d3ad7b2.1791537489880.1792105130187.1792108003203.4&__hssc=60185074.2.1792108003203&__hsfp=81938ec6db9d2925038039e9f02af3cc) will be a co-located event on Monday, November 9, at KubeCon + CloudNativeCon NA 2026.

As [Paula Kennedy](https://www.linkedin.com/in/paulalkennedy/), [Stacey Potter](https://www.linkedin.com/in/staceympotter/), and [Ramiro Berrelleza](https://www.linkedin.com/in/ramiroberrelleza/) share on the [CNCF blog](https://www.cncf.io/blog/2026/10/09/join-platform-engineering-day-at-kubecon-cloudnativecon-north-america-2026/), “Since its inception, the goal has remained simple: create a space where platform engineers and practitioners can learn from one another.” Just as important as sharing wins is sharing anti-patterns and explaining *why* decisions are made, they add.

Based on the [published agenda](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/cncf-hosted-co-located-schedule/?all-sessions=platform-engineering-day), attendees should expect a blend of end-user stories, keynotes, lightning talks, and panels, with a strong focus on agents as both producers and consumers of internal developer platforms.

## **Agents and Kubernetes are formally introduced**

[Luca Berton](https://www.linkedin.com/in/lucaberton/), AI advisor and architect, recently kicked off an interesting series, *[Udienza](https://www.udienza.com/)*. “Udienza” is Italian for an audience with someone you don’t usually get to meet. Cambridge defines it as “a formal interview with someone important.”  
  
So far, Berton’s series has stuck to that definition, featuring short chats with leaders in cloud-native and AI infrastructure, including [Luca Galante](https://www.udienza.com/episodes/luca-galante), [Chris Aniszczyk](https://www.udienza.com/episodes/chris-aniszczyk), [Kat Cosgrove](https://www.udienza.com/episodes/kat-cosgrove), [Manik Surtani](https://www.udienza.com/episodes/manik-surtani), and others.

His [recent interview](https://lucaberton.com/blog/oss-europe-2026-cncf-bob-killen-daniel-krook-interview/) features CNCF directors [Bob Killen](https://www.linkedin.com/in/mrbobbytables) and [Daniel Krook](https://www.linkedin.com/in/krook/). A key takeaway is that Kubernetes is becoming the operating system for AI, serving as the default base layer for a wave of newer projects that solve specific problems on top of it.

They also acknowledged the new traffic stresses of agents, noting that a single human request can trigger about 20 agent requests. And agents expect sub-200-millisecond responses, while a new Kubernetes pod is only guaranteed to spin up in about a second.

To close that gap, they highlighted emerging projects across the stack, like [llm-d](https://llm-d.ai/), for distributed LLM inference, and [Agent Substrate](https://github.com/agent-substrate/substrate), a runtime for large-scale agent deployments.

## **What no one wants to own: Kubernetes compliance**

“Security can write the policy. Security cannot merge the Helm chart.”

That’s the message from [Matteo Bisi](https://www.linkedin.com/in/matteobisi/) of [Reevo](https://www.reevo.it/it/) in a [CNCF blog post](https://www.cncf.io/blog/2026/10/09/who-owns-nis2-and-dora-on-a-kubernetes-platform-team/) published last Friday. He’s hitting on a common issue that many organizations don’t have a clear answer to: who owns compliance? Specifically, who owns ensuring Kubernetes platforms meet the requirements of EU regulations like [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) and [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)?

As the opening pull quote suggests, Bisi argues cloud-native operators have a role to play. He advocates creating “traceability chains” that let risk, legal, and security teams define scope, control requirements, and required evidence, then hand off specific artifacts, sprint items, and recurring operations to platform and application teams.

By aligning on who does what, compliance becomes less of an unresolved bottleneck and more of a plan of attack for these frameworks, with a repeatable handoff for future ones, too.

*As Kubernetes evolves, so do the demands on the teams running it. Presenting sponsor* [*HPE*](https://www.hpe.com/us/en/products/software.html) *helps teams address that complexity with software spanning virtualization, cloud management, observability, and automation.*

## **Spinning up agents on Kubernetes gets boring**

Getting agents running on Kubernetes is starting to feel like just another part of the infrastructure. [kagent](https://kagent.dev/) is an interesting CNCF sandbox project that runs AI agents as Kubernetes custom resources. A new tutorial shows just how routine that has become, using kagent to build an agent that builds other agents.

“You write an Agent with a system prompt, a model, and a list of tools. You apply it, and the controller turns it into a running pod that speaks A2A,” writes [Antonio Berben](https://sessionize.com/antonio-berben) from [Solo.io](https://www.solo.io/) and Felipe Vicens from [Telefónica](https://www.telefonica.com/) [on the CNCF blog](https://www.cncf.io/blog/2026/10/12/from-zero-to-agent-builder-running-kagent-on-your-laptop/) in a post published Monday.

The walkthrough runs on a laptop with a local model through [Ollama](https://ollama.com/) (kagent also supports hosted providers like OpenAI, Anthropic, Azure OpenAI, and Gemini), though the authors found smaller models struggled to produce valid manifests. The builder is fenced in by an allowlist of three tools, requires human approval before anything is applied, and uses RBAC that lets it write only Agent resources. You can drive it through kagent’s UI or its A2A API.

## **A story of when** ***not*** **to use Kubernetes**

On Tuesday at the [Nordic APIs Summit](https://nordicapis.com/events/platform-summit-2026/) 2026 in Stockholm, Sweden, [Faith Sodipe](https://www.linkedin.com/in/sodipefaith/), software developer at [Bauer Media Outdoor UK](https://www.bauermediaoutdoor.co.uk/), took the stage with a presentation that might offend some diehard Kubestronauts.

In the talk, *You Don’t Need Kubernetes: How We Scaled Our API Layer Without the Infrastructure Theatrics*, Sodipe defined [infrastructure theater](https://www.linkedin.com/posts/doerrfeldbill_nordicapis-activity-7515731670164090880-W34d?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA-8zTABlsmtYe-zC-Uf5z3oD5nm6qXDVVo) as “building for the appearance of scale rather than the reality of it.” Too often, platform teams build for a scale that’s disproportionate to production reality.

Bauer Media Outdoor UK’s ingestion system processes close to a million events per day, with bursty traffic and variable payload sizes. At that scale, better system design (fixing connection pool exhaustion, a cache stampede, and slow queries) mattered more than heavyweight container orchestration. The team containerized with [Docker](https://www.docker.com/) but skipped Kubernetes altogether.

As Sodipe [recaps on LinkedIn](https://lnkd.in/p/gMKy56JF), “My message was simple: solve the actual problem, not the problem you assume you have.”

## **Vendor’s take: AI coding evolves platform engineering**

Now that AI coding agents are ubiquitous, is platform engineering less relevant? [Cory O’Daniel](https://www.linkedin.com/in/coryodaniel), one of the early drivers behind [OpenTofu](https://opentofu.org/), the open-source [Terraform](https://developer.hashicorp.com/terraform) alternative, and CEO and co-founder at [Massdriver](https://www.massdriver.cloud/), an internal developer platform (IDP), tells The New Stack that coding agents make platform engineering more important, not less. Yet, the infrastructure surrounding IDPs must evolve.

“The architectural shift I see is from infrastructure as code to infrastructure as data,” says O’Daniel. This doesn’t replace Terraform, OpenTofu, or Git, he says, but involves representing infrastructure as a queryable graph of resources, dependencies, ownership, environments, and policy.

Serving things this way could help agents consume infrastructure information more efficiently. Plus, he says, additional controls are needed more than ever now that anybody can create and ship. “The guardrails are becoming the only control ops has left.”

## **Follow the Road to KubeCon**

*Road to KubeCon is an eight-part series presented by HPE. Before you go, explore how* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *helps IT teams do more with less complexity.*

Road to KubeCon will be here every Friday on *The New Stack*, until KubeCon. Catch up on the latest releases on the [Road to KubeCon archive page](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/).

[Bill Doerrfeld](https://www.doerrfeld.io/), the writer for this series, welcomes community contributions. You can send your PRs, blurbs, hot takes, or cloud-native forecasts through his [contact page](https://www.doerrfeld.io/contact).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/02/96a1456d-cropped-e7e1c083-bill-doerrfeld.jpg)

Bill Doerrfeld is a tech journalist and API thought leader. He is the editor-in-chief of the Nordic APIs blog, a global API community dedicated to making the world more programmable. He is also an active contributor to a handful of...

Read more from Bill Doerrfeld](https://thenewstack.io/author/bill-doerrfeld/)