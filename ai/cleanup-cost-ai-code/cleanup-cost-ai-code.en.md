The world is actively using AI to make our lives more efficient and safe — from creative writing to safer autonomous vehicles to drug discovery. Underneath all this is a common denominator — “code.” We use code to train and build AI models as well as build harnesses and tooling that augment raw models into useful applications. The earliest AI tooling was handwritten, but now AI can self-generate more code at an unprecedented speed and scale, unmatched by humans. Platforms are struggling to meet AI-scale requirements, and GitHub forecasts a [10x jump to 14 billion commits in 2026](https://x.com/kdaigle/status/2040164759836778878). The barrier to building an application has never been lower, but it comes with hidden cleanup costs in the long run.

### But who is writing AI-generated code, who is using it, and what is the cleanup cost?

The core set of users behind AI-generated code should fit into a handful of archetypes:

* **The Inventors**: these are the people and companies behind core AI concepts, large language models (LLMs), and standards such as MCP, including OpenAI, Anthropic, and Google.
* **The Researchers**: academic labs, independent research groups, and benchmark creators who generate the long tail of ideas, talent, and evaluation methods the field runs on.
* **The Platforms**: The distributors, marketplaces, and tooling providers (GitHub, Hugging Face, Cursor, Apple, [Webflow](https://webflow.com/)) whose policies and defaults shape what everyone else can build, ship, and market
* **The Engineering Orgs**: in-house engineering teams at companies of all sizes, rethinking how they operate and embedding AI into both their products and employee workflows. Not just at tech companies, but healthcare providers, grocery chains, oil refiners, and beyond.
* **The Independent Developers**: these are power users who also build new AI applications or bridge existing solutions. They can be open-source developers, freelancers, or third-party developers creating apps within ecosystems such as the Apple App Store or the Webflow marketplace
* **The Citizen Developers**: these are non-engineers (PMs, designers, marketers, analysts) who previously had little or no coding ability but can now generate working code and ship applications.
* **The Regulators**: governments, standards bodies, and sector-specific oversight entities shaping how AI can be built, deployed, and audited. Their decisions ([the EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), [US executive orders](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/), [sector rules](https://www.nist.gov/itl/ai-risk-management-framework)) increasingly define the guardrails within which everyone else operates.
* **The Adversaries:** threat actors ranging from individuals to hacktivist groups to nation-states. As frontier AI models gain serious offensive capabilities, the gap between the attack and defense capabilities is widening fast.

![Diagram showing how archetypes connect, build, and fall under threat](https://cdn.thenewstack.io/media/2026/05/818a6290-1-893x1024.png)

There is barely a B2B or B2C solution untouched by AI, which means literally everyone is a user of AI-generated code. To keep this post focused, we’ll set aside the Foundation and Distribution layers and zoom in on the Building layer: the Engineering Orgs, Independent developers, and Citizen developers who actually generate, ship, and maintain the code. The hidden costs are concentrated here, and so are the levers to address them. Before we jump into these hidden costs, let’s take a sneak peek at the AI-generated code benefits.

## Shared benefits across the building layer

AI has enabled builders to **develop and ship with velocity** never seen before. New API endpoints are being developed, tested, and shipped in 30 mins to a few hours while bug fixes and prototypes are worked on with short flight delays. Internal tools and automation are also being developed faster for a productivity boost across the entire organization. This lets leaner teams or solo entrepreneurs increase their capacity without additional headcount.

Another core benefit is the **democratization of development**. While engineers are working on complex features, citizen developers can build prototypes or fix paper cuts in the product.

Users of AI-enabled products can also move faster, from the comfort of their mobile devices.

The following [LinkedIn post](https://www.linkedin.com/posts/siam-k-ab5a65198_went-to-the-gym-after-my-shift-was-over-share-7456256103954235392-IgF3/) was shared by a Webflow customer:

```
Went to the gym after my shift was over. Laptop was closed. I was already away.  
  
A teammate urgently needed a full CMS collection export as a CSV. Hundreds of items, all fields included.  
  
I opened Claude on my phone.  
  
Described what I needed. Claude connected to the CMS through the MCP, pulled everything in paginated batches, mapped every field correctly, and handed back a clean structured CSV ready to share.  
  
…..  
  
Webflow MCP + Claude is one of the best bridges I’ve used in a production workflow. Every item, every field, zero data loss.  
  
The tools are ready. Most people just haven’t connected them
```

Another solid benefit, which is often less talked about, is **AI-augmented learning, reviewing, and testing**. AI assistants are now integrated across collaboration and documentation platforms, code hosting platforms, and across the internet broadly. This reduces the barrier to learning unfamiliar technologies and makes understanding existing code and architecture much easier and more time-efficient. The builders often spend time planning their work with an AI assistant before the actual execution.

Unlike humans, AI does not tire out or need sleep and can reuse best practices for AI development and reviews to keep things **consistent and pattern-aware**. For a team of junior developers, AI can raise the floor by catching obvious mistakes early.

The benefits above are immense and a reason why AI is so widely adopted. However, some of these benefits are often front-loaded, and it takes time for us to see the hidden cost in the long run. These costs often land further away from the wins and accolades.

## Cleanup costs across the building layer

### The Engineering Orgs

Engineering organizations have been the biggest beneficiaries of AI augmentation, but they are also the ones that accumulate the largest cleanup costs in the long run.

Humans are still required to be in the loop for high-risk changes. The **burden of reviewing** most high-risk code within an organization falls on senior engineers **with** **contextual** understanding.

Engineers who lean heavily on AI, especially those early in their careers, are prone to **erosion of their software engineering skills**. They may also find it hard to move to the next level in the career ladder if their thoughts are not their own.

Another huge hidden cost for AI-generated code is **quality debt**. In the quest to move fast and with AI in charge of low-risk work or reviews, the code is prone to **duplication and subtle logic flaws** that can be exploited later. It also results in weak contextual understanding of the AI-augmented work in the long run. Incidents could also run longer due to a **lack of ownership and understanding** of the impacted surface area.

Engineering orgs can also be hit by **availability issues due to AI vendor concentration**. If a heavily relied-on AI coding vendor has downtime, engineering productivity drops. If the vendor relied on for product AI integrations is down, the customers feel the pain. And if the product relies completely on AI without a manual workflow, the AI vendor downtime is your downtime.

AI productivity gains do not come for free. There is a **large operating cost** to AI-augmented development, and most companies still [do not understand AI budgeting](https://aimagazine.com/news/why-uber-has-already-burned-through-its-ai-budget). Higher token burn per developer is being glorified as a sign of higher productivity, potentially leading to wasteful spending.

And last but not least, the **security cost,** which deserves its own section.

**Overall risk level: High but distributed**

### The independent developers

Independent developers (freelancers, OSS maintainers, third-party app developers) can see significant gains from AI adoption, but it carries a risk to their personal brand. The larger volume of code makes it harder to review with **no peers to review or clean up the code**. There is no legal team preventing copyright violations in your work or from your work. Unintended **mistakes or bad reviews can get a freelancer suspended** from a freelance platform or a developer’s apps kicked out of an ecosystem. One vulnerable plugin shipped to thousands of customers, one license violation in a freelance deliverable, or one buggy release on the App Store can tarnish a developer’s standing in that ecosystem.

> “It takes a contributor five minutes to generate a low-quality AI pull request, and hours for the maintainer to verify and reject it.”

Open-source maintainers face a particularly cruel asymmetry: It takes a contributor five minutes to generate a low-quality AI pull request, and hours for the maintainer to verify and reject it. The [curl project ended its bug bounty](https://thenewstack.io/drowning-in-ai-slop-reports-curl-ends-bug-bounties/) program in January 2026 after this asymmetry became unsustainable; it was not the last project to do so.

**Overall risk level: High and personal**

### The citizen developers

This is the newest archetype, encompassing PMs, designers, marketers, and analysts. Citizen developers can now prototype and showcase their ideas instead of asking someone to build them. They can also fix minor issues in the code that are often lower priority but improve the customer’s quality of life. These developers can now also build internal tools that previously required justification and prioritization of developer resources.

However, the code from citizen developers **often carries quality issues**. While the code solves the problem, it may contain code duplication, lack tests, error checking, or logging, and have no security considerations. If their work touches on high-risk areas such as authentication or PII data, an engineering review will help them address these issues and teach them the tricks of the trade. Lighter and low-risk changes may go straight to production. While bad code from citizen developers is less likely to bring a company down, a high concentration of such changes can reduce code quality in the long run.

When citizen developers contribute code to production, they are usually focused on solving a specific problem rather than thinking about long-term maintainability or incident response. If something breaks later, the original author may not have the depth to debug it, and fixes typically fall on the engineering org to test and ship, adding to their workload.

**Overall risk: Medium, but can aggregate fast**

### The ecosystem problem

We just discussed different archetypes and the hidden cost within their own surface. However, there is a second-order effect when independent developers build for ecosystems or platforms owned by larger companies. This includes not just Apple and Google App stores but marketplace ecosystems from the likes of [Webflow](https://webflow.com/apps), Shopify, and GitHub. E**cosystem owners share responsibility** for AI-generated code written by individual developers.

When customers install an app, and something goes wrong, they blame the platform, not the developers. This is because the marketplace reviewed and allowed the app to exist within their ecosystem. Every bad app that slips through the cracks **reduces customer confidence** in the ecosystem as a whole.

With AI, Independent developers are now shipping their creations faster, resulting in more submissions and reviews for the ecosystem owners. This includes a **high volume of submissions with low-quality and insecure code**. In the past, we were able to manually review all apps; however, this is no longer possible given the AI-augmented submission rate. Emerging ecosystems now are investing more in automated reviews, security guidelines, and developer education.

In addition to new app submissions, **approved apps are now evolving** with the help of AI. Developers are submitting updated app versions with increased capabilities, but with similar problems we discussed above: needing higher permissions, insecure code, or license contamination. Ecosystem owners now have to deal with this problem without **burning their social contract with the developer community**.

GitHub, being both an enterprise solution and a community code-hosting platform, [faces infrastructure and resilience challenges](https://devops.com/github-faces-scaling-issues-as-ai-development-surges/) due to the sheer volume of AI-generated code produced by its AI product and hosted on its platform. This points to larger ecosystems grappling with **scaling issues and increased operating costs.**

**Overall risk: High but quiet**

![Table showing the hidden costs and risk level for each archetype](https://cdn.thenewstack.io/media/2026/05/7d39c100-2-1024x774.png)

### The security cleanup bill

#### More code, more bugs

AI models have evolved over the years, and they are great at syntactic and semantic correctness. However, when no security guidelines are provided, the security benchmarks have seen sluggish improvements.

![Chart plotting LLM release date against security pass rate](https://cdn.thenewstack.io/media/2026/05/498216e6-3-1024x753.png)

*Diagram from [Veracode Spring 2026 GenAI Code Security Update](https://www.veracode.com/blog/spring-2026-genai-code-security/) shows that AI-generated code security pass rates (shown in red) have remained essentially flat since 2023*

The [trend published by Veracode](https://www.veracode.com/blog/spring-2026-genai-code-security/) is concerning, given that more and more code is now AI-generated, with OpenAI claiming the percentage has risen to 80%. The latest AI models still produce code with a **low** **security pass rate for serious vulnerabilities,** such as Cross-Site Scripting and Log Injection attacks. The models also score low on security with programming languages like Java.

AI hallucinations for software dependencies have seemingly improved, but based on research, [AI-written code can still invent package names](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks) or misspell them, an opportunity that **typosquat attackers use for supply chain attacks**.

#### The patch window has closed

While AI models are busy writing insecure code, their offensive capabilities have seen a dramatic jump. The barrier to Vulnerability research has gone down, and [AI models reason](https://thenewstack.io/openai-gpt-5-level-speech/) with the capabilities of top security researchers, if not surpass them. In the past 2 years alone, the time from a vulnerability existing in a system to its **exploitation has gone down from months to days, and in many cases,** [**exploitation begins before a patch even ships**](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026)**.**

![Diagram from Zero Day Clock showcasing the time to exploit down from years to hours](https://cdn.thenewstack.io/media/2026/05/d6fc5509-4-1024x894.png)

*Diagram from [Zero Day Clock](https://zerodayclock.com/) showcasing the time to exploit down from years to hours*

Anthropic recently collaborated with the world’s most critical software providers under [Project Glasswing](https://www.anthropic.com/glasswing) and shared its unreleased model, Claude Mythos. [Mythos found 271 vulnerabilities in Firefox alone](https://blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/), including issues that had survived decades of human security review.

While Mythos is a starting point, open source is catching up fast. Hadrian’s research team has cataloged [70 open source AI pentest tools, up from 5 in April 2023](https://hadrian.io/blog/the-ai-offensive-security-boom-seventy-tools-in-eighteen-months). These tools can work relentlessly and in parallel to find vulnerabilities in every piece of software and code on the internet.

#### Defenders’ burnout

With more code, more bugs, and more exploits, security practitioners are facing serious burnout. While the vulnerability count and the noise have gone up, the security headcount has not. Security practitioners are now **spending more time addressing zero days**, often stemming from relentless package supply chain incidents in recent years.

[Vercel](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident) and [Mercor](https://fortune.com/2026/04/02/mercor-ai-startup-security-incident-10-billion/) are some of the latest victims of these security incident trends. Vercel was breached through a compromised AI tool’s OAuth token, and Mercor lost roughly 4 terabytes of data through the LiteLLM open-source AI gateway, exposing training methodologies for OpenAI, Anthropic, and Meta in the process. Both incidents trace back to the same root — **AI tooling has become the new supply chain attack surface**, and security practitioners are racing to reduce the attacker-to-defender capacity gap.

The Cloud Security Alliance (CSA) recently published a [paper](https://labs.cloudsecurityalliance.org/mythos-ciso/) urging security leaders to build a [Mythos](https://red.anthropic.com/2026/mythos-preview/)-ready security program and prepare for burnout, as the volume of vulnerability disclosures is expected to exceed anything we have experienced before. They **advise security teams to increase capacity and adopt agentic workflows** for security assessments and incidents.

Along with the security incidents, the bug bounty landscape has changed with script kiddies using AI to find and report vulnerabilities. Public Bug bounty programs now see **more AI slop than serious reports**. The burnout from triage (even with AI) has been severe enough that the [curl-](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/) and HackerOne-sponsored [Internet Bug Bounty programs](https://hackerone.com/ibb?type=team) have been suspended.

FIRST, a leading security non-profit recently released its prediction for [2026 to surpass 50,000 CVEs](https://www.first.org/newsroom/releases/20260211) for the first time. Their guidance to organizations is to scale their security operations, but most can’t keep up.

NIST itself is buckling. In April 2026, [the agency announced](https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth) it would **stop enriching most CVEs** in the National Vulnerability Database, citing a 263% surge in submissions between 2020 and 2025. The institution that anchors the world’s vulnerability metadata is publicly throwing up its hands. This is indicative of future trouble for other similar vulnerability data ecosystems.

## What can we do about it: Reduce the cleanup cost

The cleanup cost is real, and there is no silver bullet to fix it. The teams and ecosystems that manage this share a few common patterns, which differ depending on where the cost lands. Here is a prioritized view of what to do about the risk category that hurt the most.

|  |  |  |
| --- | --- | --- |
| **Priority** | **Risk Area** | **What To Do** |
| **P0** | Security and the patch gap | Treat AI-generated code with the same scrutiny as human-written code, ideally more. Run AI-enabled SAST, DAST, and SCA on every PR, including across developer machines. Add a cooldown period before installing newly published packages to [mitigate supply chain](https://thenewstack.io/how-web-assembly-can-mitigate-the-software-supply-chain-crisis/) takeovers. Build incident response playbooks for known categories, such as supply chain. Most importantly, measure fixed findings, not discovered ones. |
| **P1** | Reviewer fatigue and ownership gaps | Stop measuring engineering output by lines of code or PR count. Measure defect rates, incident frequency, and time-to-remediate instead. Establish clear service and package ownership so “nobody really wrote this” is never a valid 2 a.m. answer. Categorize PRs by risk so senior reviewers can focus on the changes that matter, not the queue volume. |
| **P1** | Ecosystem and marketplace governance | Invest in pre-publication automated analysis for marketplace submissions. Set clear AI disclosure policies and third-party developer guidelines. Build incident response paths that account for third-party origin. Plan for review automation now, since pre-AI review processes will not scale. |
| **P2** | Citizen developer guardrails | Guardrails, not gatekeeping. Pre-vetted AI tools, sandboxed environments, and automated security and policy checks at deploy time. Define clear handoff paths when a citizen-built app graduates to something engineering needs to own. |
| **P2** | Skill erosion in engineers | Pair AI usage with explicit reasoning artifacts (design docs, decision records). Treat AI as a force multiplier on existing skills, not a replacement for building them. |

## Where this leaves us

AI-augmented development is a generational shift on the scale of the industrial revolution. Just as machines reshaped what humans built and how they built it, AI is reshaping how software gets created and who can create it. The barrier to building is low, innovation is at its peak, and entire categories of work are being redefined in months instead of decades.

The hidden costs are also real, and they tend to land far from where the velocity wins were booked. We discussed reviewer fatigue within engineering orgs, personal reputation risk for independent developers, quality issues that surface years after shipping, ecosystem-wide trust damage when something goes wrong, and a security landscape where attackers move at machine speed while defenders are still operating at human speed. The asymmetry between the speed of creation and the speed of cleanup is what defines the cost.

> “The asymmetry between the speed of creation and the speed of cleanup is what defines the cost.”

The teams and ecosystems that win with AI-generated code over the long run aren’t the ones moving fastest. They’re the ones who built a method behind the madness. The winners are the ones already accounting for the cleanup strategy from day one. AI will keep stretching the boundaries of what we can imagine. The question is whether the practices around it advance fast enough to keep up.

*This article was originally published on May 12, 2026, on [webflow.com](https://webflow.com/blog/cleanup-cost-ai-generated-code).*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/c4146d85-ankit-headshot-600x600.jpeg)

Ankit Agrawal is a Security Engineering Leader at Webflow, where he leads efforts to secure 1% of the site traffic on the internet. With 13+ years of security and development experience across startups and larger enterprises, he specializes in scaling...

Read more from Ankit Agrawal](https://thenewstack.io/author/ankit-agrawal/)