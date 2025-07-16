APIs are great for growth, allowing teams to build and ship features at a remarkable pace. Your business most likely thrives on APIs. They are bridges connecting your services, and the very language your applications use to deliver unique value to customers. But this velocity often comes with a hidden and tangled shadow — a growing complexity that quietly undermines the very innovation it was meant to support.

For years, the conversation around this complexity, or API sprawl, felt contained within engineering teams. It was often discussed as a form of technical debt—a messy backend that, while annoying, primarily just slowed down development. But that perspective is now dangerously outdated, according to [Akash Agrawal](https://in.linkedin.com/in/akashmagrawal), VP of DevOps & DevSecOps at [LambdaTest](https://www.lambdatest.com/), an AI-native software testing platform. “In today’s landscape,” he explains, “where digital supply chains are built entirely on APIs, unmanaged sprawl is a direct and significant business risk. Each unknown or unsecured API is a potential vector for a major breach, impacting everything from regulatory [compliance to customer](https://thenewstack.io/suse-launches-a-sovereign-premium-support-service-for-eu-customers/) trust.”

This shift from a contained issue to a core business threat is being supercharged by the frantic pace of modern development. As organizations run an arms race to innovate, they are creating APIs at a rate that manual governance simply cannot handle. And recent AI breakthroughs — especially in automated code and API generation — are increasingly accelerating this proliferation. But combined with poor visibility and a lack of control across environments, this leaves companies exposed to critical [security failures while simultaneously undermining their ability to move](https://thenewstack.io/how-attackers-move-from-azure-active-directory-to-on-prem-ad/) forward effectively.

## How Generative AI Accelerates API Creation Beyond Security Controls

This widespread risk often begins with two well-understood but frequently overlooked vulnerabilities. The first are shadow APIs — undocumented endpoints operating completely off the radar, often created for a temporary purpose and then forgotten. The second are zombie APIs, which are older versions that were meant to be retired but were never fully decommissioned. Both represent open invitations for attackers, but their numbers remained somewhat manageable through traditional, if imperfect, human oversight.

That dynamic has now been completely upended. “Generative AI is the primary force amplifying this long-standing issue. It’s empowering teams to build and deploy faster than ever, which is fantastic for innovation, but it’s also creating APIs at a rate that manual governance simply cannot handle,” says Agrawal, highlighting: “The result is an explosion of shadow APIs created for a specific AI-driven purpose that are never properly documented, secured, or retired.” This reinforces the old security truth — what you can’t see, you can’t secure — and AI is rapidly expanding a landscape that’s already difficult to monitor.

This acceleration has given rise to a risky new developer behavior — a trend known as “vibe coding.” [Edgar Kussberg](https://www.linkedin.com/in/kussberg/), Product Manager at Sonar’s AI division, points out that developers increasingly trust AI-generated code that simply feels right, without performing the necessary due diligence. Because of vibe coding, [APIs are frequently deployed without crucial security](https://thenewstack.io/using-apis-with-low-code-tools-9-best-practices/) controls or proper documentation, creating a new wave of widespread vulnerabilities at an unprecedented scale.

## The Productivity Cost of Unmanaged API Sprawl

The most immediate consequence of API sprawl is a drastic blow to developer productivity. [Yauheni Kanavalik](https://www.linkedin.com/in/kanavalik), a Solution Architect at [EPAM Systems](https://www.epam.com/), explains that this often leads teams into what’s commonly known as “dependency hell” — a state in which development teams shift their focus away from the user and their needs, instead becoming overloaded just trying to navigate the tangled web of integrations. This is a state of paralysis that directly impacts the bottom line.

Kanavalik points to “investigation time” as the key hidden metric — where weeks can pass before a new [feature is even ready for development](https://thenewstack.io/top-5-code-completion-services/). A developer might need to confirm if a similar function already exists, sketch out a sequence of API calls, and then try to contact the owners of those services across multiple time zones and support channels. This initial discovery phase, rather than the coding itself, becomes the biggest bottleneck to delivering value.

This drag on productivity can directly sabotage strategic business initiatives, says [Asad Akram](https://www.linkedin.com/in/aakram1/), Senior Engineering Manager at [Sigma](https://www.sigmacomputing.com/). “Our business intelligence team experienced this firsthand when they built an AI assistant to help users generate API calls from natural language. But the AI frequently gave incorrect suggestions, recommending an API that looked right but failed to deliver the expected result — leading to frustrated users. The root cause was API sprawl; the AI was trying to navigate twelve different but similar APIs tied to the same functional goal.”

This kind of friction has a cumulative effect that business leaders cannot afford to ignore. [Madhu Kochar](https://www.linkedin.com/in/madhu-kochar-637a305/), VP of Automation at [IBM](https://www.ibm.com/in-en), points out that this “API explosion” ultimately leads to increased maintenance and operational costs, reduced developer productivity, and heightened security and compliance risks that directly hinder an organization’s digital transformation initiatives.

## Implementing Continuous Governance for AI-Generated APIs

While the picture of API sprawl seems daunting, organizations can regain control through a multilayered approach that addresses people, process, and technology. It begins not with a new tool, but with a new approach to ownership and expertise.

One of the most effective organizational fixes is the creation of what Kanavalik of EPAM Systems calls a “facade team.” This is a specialized, central team that serves as a single point of entry and ownership for all API integrations. Instead of every developer struggling with the same third-party dependencies, the facade team manages those relationships, standardizes documentation, and provides expert guidance — freeing other teams to focus on building value.

With a clear ownership structure in place, teams can then move on to the tactical work of cleanup and automation. The Sigma team, for example, directly addressed their AI assistant’s failures by consolidating twelve redundant APIs into just three flexible endpoints. This cleanup immediately [improved clarity for both their human developers](https://thenewstack.io/ai-improves-developer-workflow-says-gradle-dev-evangelist/) and their AI systems. And the EPAM team suggests using Large Language Models to automatically generate high-quality API documentation directly from the source code of poorly understood services.

But these tactical fixes must be part of a larger, future-proof strategy. Kussberg of Sonar argues that traditional governance frameworks are “playing catch-up” and are simply not built for an era where AI can autogenerate code. The solution, he advocates, is to implement “CI/CD + CG (Continuous Governance).” This [means embedding automated security](https://thenewstack.io/6-reasons-why-more-automation-means-more-secure-software/), versioning, and governance checks directly into the development lifecycle, ensuring that every API — whether human- or AI-generated — is safe and managed from the moment of its creation.

## Building Facade Teams and Automated Controls for API Security

It’s clear that the conversation about API sprawl has fundamentally changed because of AI advancements. The tangled web of unknown, unmanaged, and forgotten APIs is no longer a background issue of technical debt that can be pushed to the next quarter. It is an active and growing [business risk that directly impacts security](https://thenewstack.io/cloudflare-for-ai-helps-businesses-safely-use-ai/), complicates compliance, and paralyzes the very development teams tasked with innovation.

“The path to reclaiming control hinges on a strategic commitment to visibility, ownership, and embedding proactive security throughout the entire API lifecycle,” says Agrawal. Speaking from his engineering experience at LambdaTest and leading the security efforts for [Kane AI](https://www.lambdatest.com/kane-ai), a GenAI-native testing agent for high-speed quality engineering, he emphasizes the importance of aligning security and velocity from the start. By moving from a state of firefighting to a forward-looking strategy of “Continuous Governance,” organizations can begin to transform their API landscapes. They can shift them from hidden liabilities into the secure, strategic assets that are absolutely essential for building a trustworthy and innovative AI future.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/11/f50df1b2-headshot-600x600.png)

Saqib Jan is a technology analyst with experience in application development, FinOps, and cloud technologies.](https://thenewstack.io/author/saqib-jan/)