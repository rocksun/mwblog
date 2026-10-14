Build-or-buy is usually framed as an engineering trade-off, where developer time is weighed against integration and migration overhead, and control against the maintenance burden of a bespoke build. When we put together the [2026 Future of Platform Engineering report](https://octopus.com/publications/future-of-platform-engineering-report), we weren’t trying to settle the trade-off; we were trying to find out whether platform feature-sourcing decisions revealed anything about the platform team. It turns out it does. Across responses from 379 platform professionals, we found that teams predominantly building from scratch are less likely to have a clear strategy in place and to meet fewer of their platform goals.

This question has changed considerably with AI. Agents have made building easier than ever; an internal tool that once took months to build can now be put together in a day. But AI removes the effort of writing code, not the work of owning it. The maintenance, upgrades, and governance that come with a scratch-built feature remain, while the volume of change moving through the pipeline increases. That makes build-versus-buy a sharper strategic question than ever.

We asked platform teams how they support each feature they own: built from scratch, built on an existing template, or bought as an underlying tool. Teams whose dominant approach is building from scratch are far more likely to report that their platform lacks a clear strategy. The association is strong, but it is not as simple as “build from scratch means you don’t have a plan.”

## **Most Teams Buy And Choose Deliberately**

Across the features platform teams own, we found that using an underlying tool is the most common: 51.3% of respondents said this was their primary approach, ahead of building on an existing template (31.2%) and building from scratch (17.5%). High performers lean more heavily on tools (58.8%) than on building from a template (47.8%) or from scratch (33.3%). This could reflect a broader maturity pattern: as architectural choices in Platform Engineering settle, teams increasingly standardize on tools rather than maintain their own. [David Tuite](https://roadie.io/blog/platform-engineering-in-2026-why-diy-is-dead/) has described the alternative as the “build-versus-buy trap,” where teams stuck maintaining custom interfaces sink 6 to 18 months into upgrades and operational overhead instead of shipping value.

![](https://cdn.thenewstack.io/media/2026/10/b4f3ff53-image-1-1024x686.png)

*Build-versus-buy feature implementation approach by goals delivered (source:* [*Octopus*](https://octopus.com/publications/future-of-platform-engineering-report)*).*

The exceptions are where it gets interesting. **Local development** environments, **one-click projects**, and **ephemeral environments** skew toward templates rather than tools, because they’re bound to a specific tech stack and golden paths that off-the-shelf tools rarely provide. **Ephemeral environments** are worth pausing on because they also mark where AI is landing well. Teams whose platforms offer them were far more likely to report that AI has positively affected the speed and stability of software delivery; the same was true of **code coverage** and **cost control**. Among teams reporting an extremely positive effect, more than three-quarters had **ephemeral environments.**

This association also likely reflects the platform rather than the feature. Teams with **ephemeral environments** tend to run on broad platforms with a range of automated delivery capabilities around them, and that breadth itself tracks with positive AI impact on delivery. **Ephemeral environments**, then, could be a sign of a platform mature enough to absorb AI-generated volume and change, without losing stability. This is consistent with [DORA’s research](https://dora.dev/research/2025/dora-report/) finding that organizational gains from AI depend on platform quality: strong platforms amplify the effects, while weaker ones dampen them.

![](https://cdn.thenewstack.io/media/2026/10/b4f3ff53-image-1024x399.png)

*Features ranked by AI impact on software delivery speed and stability (source:* [*Octopus*](https://octopus.com/publications/future-of-platform-engineering-report)*).*

The features that break the pattern reflect fit rather than a reluctance to buy, and the reasoning behind these decisions supports this. When asked to explain their build-or-buy logic, the most common response was a cost-benefit analysis (29.6%), followed by a preference for open source (28.6%), a fit-and-requirements assessment (22.4%), a preference for commercial tools (b22.4%), and building for core differentiation (16.3%). As one respondent summarized it, “Build what makes us unique, buy or adopt what’s standard, and always consider long-term cost and lock-in.” This is the same central idea presented in [domain-driven design](https://octopus.com/blog/your-idp-needs-ddd), which distinguishes the core domain, where custom work creates competitive advantage, from supporting and generic domains, where it mostly adds complexity and maintenance for something that could have been bought.

![](https://cdn.thenewstack.io/media/2026/10/56d98f89-image-1-1024x686.png)

*Reasons behind deciding to build versus buy (source:* [*Octopus*](https://octopus.com/publications/future-of-platform-engineering-report)*).*

## **The Build-from-Scratch Pattern**

Given how deliberately most teams choose, the strategy finding is more interesting. When classified by dominant build method, teams building from scratch are about 3.5x more likely to report a lack of clear strategy as an obstacle (57.9%) than teams building from a template (15.6%) or using an underlying tool (16.7%).

AI clusters here, too, with predominantly build-from-scratch teams more likely to use AI moderately or extensively for legacy modernization and language migration. There is a clear pattern here: the teams building the most lean hardest on AI for maintenance. This isn’t because they use AI more generally: their reported adoption, impact, and expected effects match those of everyone else. The difference is specific to the work that follows custom-built features.

![](https://cdn.thenewstack.io/media/2026/10/56d98f89-image-1024x542.png)

*Build-versus-buy feature implementation due to a lack of a clear strategy and technical complexity. Heatmap showing the percentage of respondents selecting the obstacle by dominant build approach (source:* [*Octopus*](https://octopus.com/publications/future-of-platform-engineering-report)*).*

## **Building First, Deciding Later**

One interpretation is that strategy comes first, and the build-or-buy decision comes later: a team without clear direction has no basis for deciding what to buy, so it builds by default. Another is that building is the strategy rather than a sign of a missing strategy. Building can help identify the problem and show progress before the team has settled on the platform’s purpose.

This is an interesting take, and the one the data can’t tell us which is right. [Simon Wardley’s](https://www.cio.com/article/196094/an-introduction-to-wardley-value-chain-mapping.html) work on mapping describes a similar pattern: teams that can’t see what tools already exist tend to build their own solutions to problems that have already been solved better elsewhere.

With AI, the gap between having an idea and having a working tool has almost closed. An agent can now build a custom incident-management tool before anyone has asked whether one is needed. Building has become easier, but maintaining what gets built hasn’t. [DORA’s research](https://dora.dev/research/2025/dora-report/) suggests why this matters: good platforms provide capabilities and set boundaries on their use, and in AI-assisted development, those boundaries may currently matter more. Established tools come with those boundaries built in; a platform built piece by piece has only the ones someone thought to add.

In either case, the relationship holds. Building from scratch isn’t the problem. Building from scratch by default, without a reason, is where the strategy gap appears.

## **A Better Question Than Build or Buy**

This isn’t a case for buying everything, as we found that some features need to be built around their organization’s own context. It is a case of buying deliberately. Where a team builds from scratch, there should be a reason. When teams buy a tool, the reason is usually already evident: nearly every team buys for the well-defined parts of the platform, and as agents write more code, the value of tools that solve those problems well only grows.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/63781866-cropped-c61358ad-unnamed.png)

Charlotte Fleming, is a developer researcher at Octopus Deploy, conducting industry research on Platform Engineering, AI adoption, and Continuous Delivery. She is the author of Octopus Deploy's Platform Engineering Pulse report and the lead researcher and author of the AI...

Read more from Charlotte Fleming](https://thenewstack.io/author/charlotte-fleming/)