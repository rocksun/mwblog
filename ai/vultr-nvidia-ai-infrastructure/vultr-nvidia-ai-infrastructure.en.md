[**Vultr**](https://www.vultr.com/) is using Nvidia GPUs and AI agents like OpenClaw to automate infrastructure setup for developers — and says the result costs 50% to 90% less than comparable offerings from major hyperscalers. The platform, built for internal developer portals, lets platform engineering teams train AI on their own security policies, networking rules, and compliance requirements, then expose that as a library of preconfigured options developers can deploy with a click.

During KubeCon+CloudNativeCon Europe, Vultr’s chief marketing officer, [Kevin Cochrane,](https://www.linkedin.com/in/kevinvcochrane) who has acquired a deep technical background over the past two decades, described Nvidia as providing the “fuel” or “electricity” for what Vultr offers.

> “We want to help platform engineers build a frickin’ BMW so that when they get on the freeway, they’re actually getting on the autobahn, and they’re going 240 kilometers an hour.”

“We want to help platform engineers build a frickin’ BMW so that when they get on the freeway, they’re actually getting on the autobahn, and they’re going 240 kilometers an hour,” Cochrane said. “You are going to consume the fuel or electricity, which we offer.”

## **Cheaper compute, automated setup**

With the availability of Nvidia’s resources, Vultr says it can offer a less expensive experience, with its cheaper “fuel” or “electricity” for the compute aspect that is often prohibitively expensive for organizations.

“The challenge is that if you have a BMW, and you’re going to go really fast, you’re otherwise going to wind up investing a lot in compute,” Cochrane added.

Vultr has created this alternative to give platform engineering teams the best of both worlds: high-powered, AI-integrated templates for creating and managing internal developer portals at a very competitive cost. According to Vultr, those savings hold across both this new functionality and its existing offerings.

## Skill files replace manual scripts

In this new approach to AI infrastructure, the platform engineer’s role shifts from manual setup to high-level architectural design. Instead of hand-coding every script, they focus on building core skills, Cochrane told *The New Stack*. These skills are essentially “skill files” that an AI agent, such as OpenClaw, uses to perform specific operational tasks.

To create these, the platform engineer develops a corpus or library of artifacts that serve as a training set. These artifacts represent a “known good set of principles” that have been “pre-baked” and “blessed by everybody” on the technical teams, Cochrane said.

For example, a network engineering team might create a network skill. This file tells the AI exactly how to “create a VPC,” establish a “direct connect” between specific cities, and set up “failover” regions, Cochrane said.

Once these skills are exposed through a developer portal, downstream developers can deploy an application without worrying about “networking,” “data center locations,” or “attaching storage,” Cochrane said.

Since the platform is “100% API-driven,” the AI agent simply uses those skill files to automate the entire configuration, Cochrane says. This ensures that complex requirements, like data privacy and security policies, are handled automatically, preventing developers from “messing that up”.

Ultimately, all the infrastructure complexity is “completely obfuscated,” so the developer can focus solely on the application itself, Cochrane said.

## Nvidia’s stack powers Vultr

Cochrane described three components of Nvidia’s stack that Vultr orchestrates:

* **Nvidia Dynamo**: An “AI operating system” for infrastructure management, both stateful and stateless,s for Kubernetes.
* **Nvidia Vera Rubin Platform**: An integrated system combining GPUs, CPUs, networking, and storage to push the “efficient frontier of tokenomics.”
* **Agentic AI & NemoClaw**: An emphasis on an open source stack (including OpenClaw/NemoClaw) that provides a secure foundation for autonomous agents through higher-level “skills” and abstractions.

## Developers click, not configure

Once the platform engineering team has set up the IDP, the developer can click what they want and need (and not have access to an AI agent that might damage infrastructure or inadvertently run up a $50,000 cloud bill). The developer can use the IDP API to choose the server, by selecting Cloud GPU or Optimized Cloud, for example, and its location, whether in New Jersey, London, or Tokyo.

A “Marketplace” tab is accessed with the Nvidia NemoClaw icon. Other configurations on the menu that Vultr’s system automates include server size, Nvidia GPU models (such as H100 or A100), RAM, and monthly price.

> “All of that complexity should get handled by the platform engineering team, and everything else should be completely obfuscated to the developer. They shouldn’t need to know anything about it.”

“Any developer that’s building some downstream application can use something like OpenClaw and take those skills… they basically just let their claw set up their pipelines, models, pipelines for their codes, and then just go,” Cochrane said. “All of that complexity should get handled by the platform engineering team, and everything else should be completely obfuscated to the developer. They shouldn’t need to know anything about it.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)